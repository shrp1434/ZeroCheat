---
title: Test Cases - Animal AI
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - ai
  - animals
  - spawning
---

# Test Cases - Animal AI

Test cases for companion animal behaviour, wild animal AI, spawning and respawn, rare-spawn events, base guard AI and AI performance budgets. System documents: [[Animal Combat Behaviour]], [[Wild Animal AI]], [[Wild Animal Spawning and Respawn]], [[Animal Guards and Base Defence AI]], [[Implementation - Animal AI State Machine]], [[Service - AnimalAIService]], [[Service - SpawnService]]. Boss AI is covered in [[Test Cases - Bosses]].

> [!success] CONFIRMED rules under test
> Animals auto-target nearby enemies and accept manual commands (D-009). Wild animals respawn; rarer animals respawn more slowly (D-011). Luck never changes wild encounter rarity (D-017). A defending animal can be stolen only after being knocked out (D-024).

> [!info] PROPOSED values used
> Respawn times and rare-spawn chances ([[Canonical Proposed Values]] §6); leash 60 studs and combat tag 8 s (§4); ≤ 180 simulated wild animals and ≤ 60 with full AI per server (§15). Which animals defend a base is **UNDECIDED** ([[Open Questions#Q-033]], [[Open Questions#Q-035]]); tests use the set the server marks `Defending`.

**Fixtures.** `QA_AdvanceClock(s)`, `QA_ForceSpawnRoll(result)`, `QA_ShowAIState(on)` (overhead state labels), `QA_SpawnWild(species, point)`, `QA_SetProgressionScore(ps)`, `QA_ForceKnockOut(animalId)`.

## 1. Companion behaviour

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-AI-001 | Companions follow the player | Three animals equipped; no enemies | 1) Walk, sprint and jump across a region for 2 minutes. | All three follow in formation per [[Animal Combat Behaviour]]; none falls more than the configured catch-up distance behind for longer than the configured time. | P0 | functional | D-006 |
| TC-AI-002 | Stuck recovery | Companion trapped behind geometry | 1) Walk away. | After the configured stuck timeout the companion repaths or is repositioned near the player; it never stays stuck permanently. | P1 | edge | D-006 |
| TC-AI-003 | Auto-engage on nearby enemy | Wild enemy enters acquisition range | 1) Stand still. | Companions acquire and attack per the targeting priority; acquisition only within the configured range. | P0 | functional | D-009 |
| TC-AI-004 | Commanded focus overrides auto-targeting | Two enemies | 1) Command focus on the farther one. | All three switch to the commanded target; resume auto-targeting when it dies. | P0 | functional | D-009 |
| TC-AI-005 | Companions ignore illegal targets | Another player (PvP off) and their companions nearby | 1) Stand next to them for 60 s. | Companions never attack them or their animals. | P0 | negative | D-023 |
| TC-AI-006 | Companions do not fight in the hub | Player in the hub with wild animal at the boundary | 1) Observe. | Companions do not engage across the safe-zone boundary. | P1 | edge | D-025 |
| TC-AI-007 | Knocked-out companion | One companion's HP reaches 0 | 1) Continue fighting. | It enters the knocked-out state, stops acting, and recovers per [[Animal Combat Behaviour]]; the other two continue. | P1 | functional | D-005 |
| TC-AI-008 | Aquatic companion movement on land | An aquatic companion (for example [[Dolphin]]) | 1) Walk on land and over water. | Moves with the air-swim behaviour (**PROPOSED**, D-043, Q-028); never stuck at the shoreline. | P2 | functional | D-043 |
| TC-AI-009 | Flying companion over gaps | A bird companion | 1) Cross a gap the player jumps. | Follows without falling or teleporting visibly. | P2 | edge | D-006 |
| TC-AI-010 | Companion reacts to team lock state | Player leaves base | 1) Try to make a companion "swap" via the UI. | No swap possible away from base (D-010); companions unaffected. | P1 | negative | D-010 |

## 2. Wild animal AI

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-AI-020 | Wild state machine | `QA_ShowAIState(on)` | 1) Approach, attack, retreat, kite past the leash. | States follow Idle → Alert/Aggro → Chase → Attack → Return → Idle as defined in [[Wild Animal AI]]; no illegal transition logged. | P0 | functional | D-011 |
| TC-AI-021 | Leash distance | Engaged wild animal | 1) Kite to 59 studs. 2) Kite to 61 studs. | Keeps fighting at 59; at 61 returns to spawn and resets to full HP. | P1 | edge | D-011 |
| TC-AI-022 | Threat between several players | Two players attack the same wild animal | 1) Player A deals more damage, then B. | Target switching follows the threat rule in [[Wild Animal AI]]; no rapid flip-flopping more than once per configured interval. | P2 | functional | D-040 |
| TC-AI-023 | Defeat removes the animal cleanly | Wild animal defeated | 1) Observe. | Defeat animation plays, model despawns, reward granted once, respawn timer starts at the moment of defeat. | P0 | functional | D-011 |
| TC-AI-024 | Wild animals are server-owned | Exploit client | 1) Try to move a wild animal by setting its position locally. | No effect on the server or other clients; network owner is the server ([[Network Ownership]]). | P0 | security | D-011 |
| TC-AI-025 | Wild animal killed while returning | Animal in Return state at 30% HP | 1) Defeat it before it resets. | **PROPOSED**: defeat is valid; reward granted to eligible contributors. | P2 | edge | D-011 |

## 3. Spawning and respawn

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-AI-030 | Respawn time per rarity | One spawn point per rarity | 1) Defeat each animal. 2) Advance the clock. | Common respawns at 20 s, Uncommon 35 s, Rare 60 s, Epic 120 s (±1 server tick). | P1 | functional | D-011 |
| TC-AI-031 | Rarer animals respawn more slowly | Table from TC-AI-030 | 1) Compare. | Respawn time is strictly increasing with rarity. | P0 | functional | D-011 |
| TC-AI-032 | Legendary spawn window | Legendary point in a region | 1) Run 5,000 windows of 300 s with the fake clock. | Spawn occurs in a share of windows consistent with 50% (binomial, α 0.01). | P1 | statistical | D-011 |
| TC-AI-033 | Mythical rare-spawn chance | Mythical point | 1) Run 5,000 windows of 900 s. | Share consistent with 25% (binomial, α 0.01; 1,060 windows already detect 20%). | P1 | statistical | D-011 |
| TC-AI-034 | Secret rare-spawn chance | Secret point | 1) Run 5,000 windows of 2,700 s. | Share consistent with 10%. | P1 | statistical | D-011 |
| TC-AI-035 | Mythical wild rare-spawn announced to the server | 16 players on one server, in different regions; second server running | 1) `QA_ForceSpawnRoll(success)` for a Mythical point. | Every player on this server receives the announcement (notification and sound per [[UI - Notifications]] and [[Sound - UI Feedback]]) at spawn time; players on the other server receive nothing. | P0 | functional | D-011 |
| TC-AI-036 | Secret rare-spawn announcement | As TC-AI-035 for Secret | 1) Force spawn. | Same as TC-AI-035, with the Secret presentation. | P1 | functional | D-011 |
| TC-AI-037 | Announcement for a player joining mid-event | Rare-spawn alive | 1) New player joins. | **PROPOSED**: joiner sees the active rare-spawn marker or message; no duplicate announcement to existing players. | P2 | edge | D-011 |
| TC-AI-038 | Rare-spawn despawn | Mythical spawned, nobody engages | 1) Advance past its lifetime per [[Wild Animal Spawning and Respawn]]. | Despawns cleanly; next window starts; no duplicate spawn at the same point. | P2 | edge | D-011 |
| TC-AI-039 | Spawns at authored points only | Region with tagged spawn points (CollectionService) | 1) Observe 30 minutes of spawns. | Every spawn position matches an authored point; none inside geometry or inside the hub. | P1 | functional | D-011 |
| TC-AI-040 | Respawn timers continue when nobody is near | Region empty of players | 1) Defeat animals, leave the region for 5 minutes, return. | Animals have respawned per their timers (dormant simulation does not stop timers). | P2 | edge | D-011 |
| TC-AI-041 | Server population cap | Full server | 1) Count simulated wild animals. | ≤ 180 simulated; ≤ 60 running full AI near players; spawn system never exceeds the cap. | P0 | performance | D-011 |
| TC-AI-042 | Luck does not change wild encounter rarity | Players at PS 0 and PS 1000 | 1) Harness 100,000 spawn decisions for each with the same seeds, then independent seeds. | Same seeds: identical outcomes. Independent seeds: two-sample χ² not rejected (α 0.001). The spawn code path has no dependency on `LuckService`. | P0 | statistical | D-017 |

## 4. Base guard AI

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-AI-050 | Defenders engage raiders | Active raid; defenders marked `Defending` | 1) Raider enters the base. | Defenders acquire and attack the raider and the raider's animals; they never attack the owner or non-raiders. | P0 | functional | D-024, Q-033 |
| TC-AI-051 | Defenders stay within the base | Raider kites outside the base boundary | 1) Leave the boundary. | Defenders stop at the boundary and return to guard positions. | P1 | edge | D-024 |
| TC-AI-052 | Knocked-out defender state | Defender HP reaches 0 | 1) Observe server state and visuals. | Server flag `KnockedOut = true`; clear visual state (per [[Animation - Raid Interactions]]); stays knocked out until the recovery rule in [[Animal Guards and Base Defence AI]]. Only now is it eligible for theft (TC-RAID-030). | P0 | functional | D-024 |
| TC-AI-053 | Defender recovery removes theft eligibility | Defender recovers before being taken | 1) Attempt theft after recovery. | Theft rejected `not_knocked_out`. Eligibility is evaluated at commit time. | P0 | edge | D-024 |
| TC-AI-054 | No defenders exist when offline | Owner offline | 1) Inspect base. | No raid possible and no defender AI runs (D-024 offline protection). | P1 | functional | D-024 |
| TC-AI-055 | Defence Station turrets target only raiders | Turret active; owner and a non-raider visitor present | 1) Observe turret targeting. | Turrets target raiders only ([[Module - Defence Station]]). | P0 | functional | D-024 |

## 5. AI performance

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-AI-060 | Server AI cost at cap | 16 players spread across regions; 180 wild animals; 48 companions | 1) Record server heartbeat time for 10 minutes. | AI update stays within the server budget in [[Animal Scalability and Performance Budgets]]; no sustained heartbeat drops. | P0 | performance | D-025 |
| TC-AI-061 | AI level of detail | Animals far from all players | 1) Inspect AI tier. | Far animals use the simplified tier (no pathfinding requests); they switch to full AI when a player approaches. | P1 | performance | D-025 |
| TC-AI-062 | Pathfinding request rate | Busy region | 1) Count PathfindingService requests per second. | Within the configured rate cap; requests are reused or throttled rather than issued per frame. | P1 | performance | D-025 |

## Related documents

- [[Test Cases - Combat]]
- [[Test Cases - Bosses]]
- [[Test Cases - Raiding]]
- [[Test Cases - Mobile Performance]]
- [[Statistical Testing of Probabilities]]
- [[Wild Animal AI]]
- [[Wild Animal Spawning and Respawn]]
- [[Animal Combat Behaviour]]
- [[Animal Guards and Base Defence AI]]
- [[Implementation - Animal AI State Machine]]
- [[Animal Scalability and Performance Budgets]]
