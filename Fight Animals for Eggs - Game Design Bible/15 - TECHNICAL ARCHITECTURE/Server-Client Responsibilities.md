---
title: Server-Client Responsibilities
type: architecture
category: technical-architecture
status: mixed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - security
  - authority
  - networking
---

# Server-Client Responsibilities

The authority matrix. For every outcome in the game it states **who decides**, what the client is allowed to do, and how the server validates. If a feature is not on this page, it is not ready to build.

> [!danger] The golden rule
> The client is a **display and an input device**. It never decides an outcome, never sends an amount of cash, a rarity, a species, a damage number, a stat, a level or a capacity. Every such value sent by a client is ignored or treated as an assertion to check (for example `expectedLevel` used only to detect stale UI). The threat analysis is in [[Threat Model]] and the detection layer in [[Exploit Prevention]].

## 1. Principles

| # | Rule | Example |
|---:|---|---|
| 1 | Client sends **intent with identifiers**, never values | `RequestHatch({ quoteId, oddsVersion })`, not `{ species = "tyrannosaurus_rex" }` |
| 2 | Server reads **only its own state** to validate | Position comes from the server's view of the character, not from the payload |
| 3 | Client may **predict presentation** but not results | The basic-attack animation plays at once; the damage number appears only on `HitConfirm` |
| 4 | Every client claim has a **tolerance and a ceiling** | Attack range check allows a latency margin, capped (see [[Service - CombatService]]) |
| 5 | Rejections are **silent to the exploiter, clear to the honest player** | Response carries an error code; detail goes to server logs only |
| 6 | Identifiers are **server-issued** | Animal IDs, egg IDs, quote IDs and raid IDs are generated on the server; a client can only reference IDs it was sent |

## 2. Authority matrix

| Outcome | Decided by | Owning service | Client role | Server validation (summary) | Status |
|---|---|---|---|---|---|
| Cash balance and every credit or debit | Server | [[Service - EconomyService]] | Displays balance from deltas | Credits only from server events (kill credit, refunds); debits checked against balance inside the commit | **PROPOSED** design of a **CONFIRMED** rule (D-014) |
| Wild defeat reward amount | Server | [[Service - CombatService]] → EconomyService | Shows reward popup | `BaseCash × RegionMultiplier × (1 + CashBonuses)` computed from config and BaseService bonuses | **PROPOSED** |
| Kill credit eligibility | Server | [[Service - CombatService]] | None | ≥10% of max HP contributed within the 8 s combat-tag window (D-040) | **PROPOSED** |
| Egg roll price and odds | Server | [[Service - EggService]], [[Service - LuckService]] | Shows quote; confirms | Quote issued by server; confirm must present matching `quoteId` and current `oddsVersion` (D-041) | **PROPOSED** |
| Egg roll result (rarity) | Server | [[Service - EggService]] | Plays roll animation with the result it receives | Server RNG only; result chosen in the same commit as the debit | **CONFIRMED** rule (D-015, D-017) |
| Egg storage location and capacity | Server | [[Service - EggService]] | Shows storage | Backpack 10 + base 50 start (D-021); expansions from profile; reject before debit if full | **CONFIRMED** start values |
| Moving eggs between backpack and base | Server | [[Service - EggService]] | Requests a move | Player must be at own base; capacity of destination; eggs not locked | **PROPOSED** |
| Hatch count per request | Server | [[Service - HatchService]] | Selects up to 5 eggs | 1 to 5 eggs, all owned, not locked; base-stored eggs only at the base | **CONFIRMED** limit (D-016) |
| Hatch result (species per egg) | Server | [[Service - HatchService]] | Plays reveal | Independent weighted pick per egg from the rarity's pool with the quoted weights (D-018) | **CONFIRMED** rule |
| Animal ownership | Server | `Systems/AnimalLedger` via Hatch, Ascension, Raid | References animal IDs | Every animal ID in a request must exist in the requester's collection | **CONFIRMED** principle |
| Ascension | Server | [[Service - AscensionService]] | Selects target and duplicates | Same species, owned, not equipped, not locked, correct count for the level, fee affordable, level below 5 | **PROPOSED** values (Q-004, Q-005) |
| Egg merging | Server | [[Service - MergeService]] | Selects 3 eggs | Exactly 3, same rarity, not Secret, station owned and at the required level, at own base, fee affordable | **CONFIRMED** rule (D-020), **PROPOSED** values |
| Team composition | Server | [[Service - TeamService]] | Picks animals for 3 slots | Exactly 3 slots, owned, no duplicates, not locked, player at own base (D-006, D-010) | **CONFIRMED** rule |
| Team lock | Server | [[Service - TeamService]] | Shows lock icon | Set on leaving the plot volume, cleared on returning; server-side zone test | **CONFIRMED** rule (D-010) |
| Player movement | Client (physics owner of own character) | — | Moves character | Sanity checks: speed, teleport distance, noclip into plots during shields; see [[Exploit Prevention]] | **PROPOSED** |
| Player attack hit and damage | Server | [[Service - CombatService]] | Sends attack intent with aim | Cooldown, combo timing, range with latency margin, line of sight, PvP permission; damage formula server-side | **PROPOSED** |
| Animal attacks and abilities | Server | [[Service - AnimalAIService]], [[Service - CombatService]] | Sends manual ability or target command | Ability owned by that companion, cooldown, 0.5 s global cooldown, target valid and in range | **PROPOSED** |
| Target commands | Server | [[Service - CombatService]] | Selects target | Target exists, is hostile to the player, within command range | **PROPOSED** |
| Knockout and defeat | Server | [[Service - CombatService]] | Shows KO state | HP tracked only on server; attributes replicate for display | **PROPOSED** |
| Defeat penalties | Server | [[Service - CombatService]], [[Service - PvPService]], [[Service - RaidService]] | Shows summary | Hook per battle type; values **UNDECIDED** ([[Open Questions#Q-014]]) | **UNDECIDED** |
| Wild spawn selection and respawn | Server | [[Service - SpawnService]] | None | Respawn timers by rarity; luck never affects wild rarity (D-017) | **CONFIRMED** rule, **PROPOSED** timers |
| Boss spawn, phases, reward eligibility | Server | [[Service - BossService]] | Shows telegraphs and health bar | Schedule server-side; eligibility once per player per spawn; rewards **UNDECIDED** ([[Open Questions#Q-015]]) | **PROPOSED** / **UNDECIDED** |
| Discovery index | Server | [[Service - IndexService]] | Shows index | Registered on credited wild defeat (D-029) | **CONFIRMED** rule |
| XP, level, region unlocks | Server | [[Service - ProgressionService]] | Shows level-up | XP only from server events; unlock requires level and boss defeat from config | **PROPOSED** values |
| Progression Score and current odds | Server | [[Service - LuckService]] | Shows **final odds only** | PS never sent to the client; odds sent inside quotes | **CONFIRMED** principle (D-017), **PROPOSED** formula (Q-017) |
| Base module upgrades | Server | [[Service - BaseService]] | Requests upgrade | Next level only (`expectedLevel`), cost from formula, gates, at own base | **PROPOSED** |
| Shield state | Server | [[Service - BaseService]] | Shows shield | Acquisition **UNDECIDED** ([[Open Questions#Q-030]]) | **UNDECIDED** |
| Raid eligibility | Server | [[Service - RaidService]] | Requests raid on a visible base | Defender online and in the same server, opted in (Q-011), not shielded, matchmaking band (Q-029), raids feature enabled | **CONFIRMED** offline rule |
| Egg theft | Server | [[Service - RaidService]] → EggService | Interacts with vault | Base-stored eggs only, never backpack; per-raid limit configurable and **UNDECIDED** ([[Open Questions#Q-013]]) | **CONFIRMED** rule / **UNDECIDED** limit |
| Animal theft | Server | [[Service - RaidService]] → AnimalLedger | Interacts with KO'd defender | Defender knocked out during this raid; ≤ 3 animals per successful raid; retention rules **UNDECIDED** ([[Open Questions#Q-025]]) | **CONFIRMED** rule |
| Raid duration and outcome | Server | [[Service - RaidService]] | Shows timer | Duration from config; **UNDECIDED** ([[Open Questions#Q-012]]) | **UNDECIDED** |
| PvP participation | Server | [[Service - PvPService]] | Requests opt-in (method **UNDECIDED**, [[Open Questions#Q-011]]) | Server state only; combat checks it on every PvP hit | **CONFIRMED** optional (D-023) |
| Robux purchases | Server | [[Service - EconomyService]] (receipt handling) | Prompts purchase | `MarketplaceService.ProcessReceipt` grants; idempotent by purchase ID; no Cash for Robux (D-044, **PROPOSED**) | **PROPOSED** |
| Settings (audio, camera, quality) | Client, persisted by server | [[Service - DataService]] | Owns values | Server validates shape and ranges only | **PROPOSED** |
| VFX, sounds, camera, UI animation | Client | — | Fully owns | Not validated; no gameplay effect | **PROPOSED** |

## 3. Client prediction allowance

| Action | Predicted on the client | Confirmed by the server | Rollback on rejection |
|---|---|---|---|
| Basic attack | Swing animation, swing sound | `Combat/HitConfirm` (damage number, hit VFX) | None needed; a swing that hits nothing is valid |
| Special move | Wind-up animation and cooldown UI | Hit confirms; `Combat/CooldownSync` | Cooldown UI resets on `Combat/ActionRejected` |
| Dodge roll | Roll movement (character is client-owned) | Server grants i-frames if within cooldown | If rejected, server applies damage normally; no positional rollback |
| Target command | Target marker | Companion behaviour changes | Marker clears on rejection |
| Egg roll | **Nothing**; spinner only | Result in response | — |
| Hatch | **Nothing**; the reveal starts after the response | Result in response | — |
| Team change | **Nothing** | New team in response | — |

Outcome-bearing actions are never predicted, so there is nothing to roll back. See [[Latency Handling]].

## 4. Validation tolerances (PROPOSED)

These are new **PROPOSED** values introduced here and used by [[Service - CombatService]]. They should be added to [[Canonical Proposed Values]].

| Check | Tolerance |
|---|---|
| Melee range | Role basic range + 4 studs + min(ping × player speed, 6 studs) |
| Ranged range | Role basic range + 6 studs |
| Attack rate | Combo cadence of 0.45 s per hit with 0.1 s jitter allowance |
| Character speed | Flag if horizontal speed exceeds 1.5 × current WalkSpeed over a 1 s window (dodge roll excluded) |
| Teleport | Flag if displacement between two server Heartbeats exceeds 30 studs without a server-initiated teleport |
| At-base test | Character root inside `PlotBounds` expanded by 2 studs |

Flags feed the suspicion score in [[Exploit Prevention]]; a single flag never kicks a player.

## 5. Worked example: a forged hatch

An exploiter fires `Hatch/RequestHatch` with `{ quoteId = "Q-guess", oddsVersion = "v999" }`.

1. `Net` gate: payload shape valid, rate limit fine.
2. `QuoteStore:Take(player, "Q-guess")` returns nothing: quote IDs are per player, random and single use.
3. Response `E_QUOTE_UNKNOWN`. Log entry `security.quote_unknown` with the user ID, increments the suspicion counter.
4. Nothing is consumed, nothing is created. Even a valid stolen quote ID from another player fails because quotes are keyed by user ID.

## Related documents
- [[Technical Architecture Index]]
- [[Remote Communication Contract]]
- [[Security Architecture]]
- [[Threat Model]]
- [[Exploit Prevention]]
- [[Latency Handling]]
- [[Network Ownership]]
- [[Raid Anti-Exploit Validation]]
- [[Test Cases - Exploit Prevention]]
