---
title: Test Cases - Multiplayer
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - multiplayer
  - networking
  - concurrency
---

# Test Cases - Multiplayer

Test cases for the shared world: server population, session handling, replication, shared combat, concurrency between players and network conditions. System documents: [[Multiplayer Architecture]], [[Shared World and Player Sessions]], [[Replication Strategy]], [[Network Ownership]], [[Latency Handling]], [[Disconnect Handling]], [[Data Consistency and Transactions]], [[Multiplayer Combat Rules]].

> [!success] CONFIRMED rules under test
> One large shared world supporting single-player and multiplayer play (D-025). Team of three per player (D-006). Raids and PvP are optional (D-023, D-024).

> [!info] PROPOSED values used
> 16 players per server ([[Open Questions#Q-031]]); 3 companions per player; ≤ 180 simulated wild animals; shared kill credit ≥ 10% (D-040).

**Test setup.** Studio local server with several clients for functional cases; the QA test experience with real devices for 16-player cases. Concurrency cases use `QA_CommitBarrier(n)`, a QA-build hook that holds *n* incoming requests and releases them in the same server step, so "simultaneous" is reproducible rather than a matter of luck.

## 1. Server population and sessions

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MP-001 | Server capacity | Server with 16 players | 1) A 17th player joins the experience. | The 17th is placed on another server; the full server is unaffected. | P0 | functional | Q-031 |
| TC-MP-002 | Shared world visibility | 4 players in one region | 1) Move around together. | Each sees the others, their companions and the same wild animals in the same states. | P0 | functional | D-025 |
| TC-MP-003 | Solo play in a shared server | One player ignores everyone else for 30 minutes | 1) Play the core loop alone. | No forced interaction; no system requires a second player (D-025). | P1 | functional | D-025 |
| TC-MP-004 | Late joiner state | Boss at 40% HP, several upgraded bases, a rare-spawn alive | 1) New player joins. | Sees correct boss HP, every base at its current levels and the rare-spawn. | P1 | functional | D-025 |
| TC-MP-005 | Player leaves cleanly | Player with companions and a base | 1) Leave. | Character, companions and base are removed for everyone; no orphaned models or AI; profile saved. | P0 | functional | D-025 |
| TC-MP-006 | Same account on two servers | Account in server 1 | 1) Join server 2 with the same account (for example from another device). | Session lock prevents two writable sessions (INV-12): server 2 waits for the lock or server 1's session ends first; no data from either session is lost or duplicated. | P0 | security | D-025 |
| TC-MP-007 | Server shutdown with a full server | 16 players | 1) Trigger shutdown. | `game:BindToClose` saves all 16 profiles within the shutdown time limit (30 s per Roblox documentation, *unverified* at time of writing); save failures are logged with user IDs. | P0 | edge | D-025 |

## 2. Shared combat

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MP-010 | Two players, one wild animal | A and B both deal ≥ 10% | 1) Defeat it. | Both receive the full reward; both register the species in their index. | P0 | functional | D-040 |
| TC-MP-011 | Contribution from animals only | A's animals deal 15%; A deals 0% | 1) B finishes it. | A receives the full reward. | P1 | functional | D-040 |
| TC-MP-012 | Kill-credit farming check | Five players tag a Common for exactly 10% each | 1) Repeat 100 times. | Each eligible player is rewarded per kill; telemetry flags unusual Cash rates per [[Inflation and Farming Exploit Risks]]. No duplicate reward per player per kill. | P1 | functional | D-040 |
| TC-MP-013 | Rare-spawn race | Mythical rare-spawn; 10 players converge | 1) Fight it together. | All with ≥ 10% are rewarded; the announcement reached all (TC-AI-035). | P1 | functional | D-011 |

## 3. Concurrency between players

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MP-020 | Two players interacting with the same egg simultaneously | Raid active; egg E in defender D's base storage; D and attacker A both act on E | 1) `QA_CommitBarrier(2)`. 2) D confirms hatch (or merge, or move to backpack) of E; A confirms theft of E. 3) Release. | Exactly one request commits. The other is rejected with `egg_unavailable` and has no side effects (no Cash charged, no counter consumed). E, or the animal hatched from it, exists in exactly one profile (INV-01). Repeat 50 times: never two successes, never zero successes with E missing. | P0 | edge | D-024 |
| TC-MP-021 | Two attackers, same egg | Only if Q-1008 allows concurrent raids | 1) Both confirm theft of E at the barrier. | Exactly one succeeds. | P0 | edge | D-024 |
| TC-MP-022 | Two attackers, same knocked-out defender | As TC-MP-021 for an animal | 1) Both confirm. | Exactly one succeeds; the animal counter of only that raid increases. | P0 | edge | D-024 |
| TC-MP-023 | Same player, two devices, same egg | Session lock correctly prevents this | 1) Attempt hatch from two devices. | Second device cannot act (no second session); if it somehow reaches the server, the request is rejected. | P0 | security | D-025 |
| TC-MP-024 | Many players rolling at once | 16 players roll ×5 within one second | 1) Barrier release. | Every roll processed independently; no shared-state corruption; each player's Cash and eggs correct. | P1 | performance | D-015 |

## 4. Replication and network conditions

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MP-030 | Bandwidth at full server | 16 players, 48 companions, region near cap | 1) Record network receive per client for 10 minutes. | Within the per-client budget in [[Replication Strategy]]; companion updates use the throttled path. | P0 | performance | D-025 |
| TC-MP-031 | Cosmetic events over unreliable channel | Hit sparks, footsteps | 1) Inspect remote usage. | Cosmetic-only updates may use `UnreliableRemoteEvent`; anything affecting state (damage, theft, purchases) uses reliable remotes ([[Remote Communication Contract]]). | P1 | functional | D-025 |
| TC-MP-032 | High latency | 250 ms simulated | 1) Fight, roll, hatch, change team at base. | Every action completes; UI shows pending state; no double submissions. | P1 | performance | D-025 |
| TC-MP-033 | Packet loss and reconnection | Brief network drop on a client | 1) Drop for a few seconds. | Client reconnects per [[Disconnect Handling]] or is removed cleanly; no duplicated actions on reconnect. | P1 | edge | D-025 |
| TC-MP-034 | StreamingEnabled correctness | Players in distant regions | 1) Teleport between regions. | Content streams in before interaction is possible; no falling through unloaded terrain; companions arrive with the player. | P1 | functional | D-025 |
| TC-MP-035 | System messages | Rare-spawn and boss announcements | 1) Observe chat and notifications. | System announcements are delivered through the approved channel ([[UI - Notifications]] and TextChatService system messages); player chat is filtered by the platform. | P2 | functional | D-025 |

## Related documents

- [[Test Cases - Raiding]]
- [[Test Cases - Persistence]]
- [[Test Cases - Exploit Prevention]]
- [[Test Cases - Mobile Performance]]
- [[Multiplayer Architecture]]
- [[Shared World and Player Sessions]]
- [[Replication Strategy]]
- [[Network Ownership]]
- [[Latency Handling]]
- [[Disconnect Handling]]
- [[Data Consistency and Transactions]]
- [[Multiplayer Combat Rules]]
