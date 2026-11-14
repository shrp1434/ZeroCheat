---
title: Test Cases - Bases and Upgrades
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - base
  - upgrades
---

# Test Cases - Bases and Upgrades

Test cases for personal modular bases, module construction and upgrades, plot expansion, module effects, shields and physical defences (outside of the raid flow itself, which is in [[Test Cases - Raiding]]). System documents: [[Player Base System]], [[Base Layout and Plot Expansion]], [[Base Upgrade System]], [[Base Defence Overview]], [[Shield Mechanics]], [[Service - BaseService]], [[UI - Base Management]], [[UI - Base Upgrades]].

> [!success] CONFIRMED rules under test
> Every player owns a modular base whose sections are upgraded separately; base progression can contribute to multipliers, strength and progression (D-022). Bases are protected by shields and physical defences (D-024). The team can be changed only at the player's own base (D-010).

> [!info] PROPOSED values used
> Module list and costs `Cost(L) = BaseCost × 2.5^(L − 1)`, L1–L5; plot expansion `5,000 × 3^(n − 1)`, 4 stages; module effects ([[Canonical Proposed Values]] §12). Which modules ship is **UNDECIDED** ([[Open Questions#Q-007]]). Pen display is **UNDECIDED** ([[Open Questions#Q-008]]). Shield duration, recharge and acquisition are **UNDECIDED** or unspecified ([[Open Questions#Q-030]]) and are tested as configuration.

**Fixtures.** `QA_SetModuleLevel(module, level)`, `QA_SetPlotStage(n)`, `QA_SetCash(n)`, `QA_SetConfig(key, value)`, `QA_StartRaidAgainst(player)`.

## 1. Base ownership and placement

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BAS-001 | Base assigned on join | New player joins | 1) Observe. | A plot is assigned and the player's base (starting layout) loads; portal or route from the hub per [[Player Base System]]. | P0 | functional | D-022 |
| TC-BAS-002 | Base restored on rejoin | Upgraded base | 1) Rejoin on another server. | Same modules, levels, plot stage and station level; layout identical. | P0 | functional | D-022 |
| TC-BAS-003 | 16 bases on one server | Full server (16 players, Q-031) | 1) All join. | Every player receives a plot; no overlapping bases. | P0 | functional | D-022 |
| TC-BAS-004 | Plot release on leave | Player leaves | 1) Observe the plot. 2) New player joins. | Base removed from the world (offline bases are not present and cannot be raided); plot reusable. | P0 | functional | D-022, D-024 |
| TC-BAS-005 | Base boundary for the team rule | Player at the edge of the base | 1) Step in and out. | The server's "inside own base" flag changes exactly at the authored boundary; the UI indicator matches. | P0 | edge | D-010 |
| TC-BAS-006 | Cannot modify another player's base | Visiting another base | 1) Try to upgrade or place a module there. | Rejected `not_owner`. | P0 | security | D-022 |

## 2. Module upgrades

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BAS-010 | Animal Pens cost curve | Enough Cash | 1) Build and upgrade L1–L5. | 1,000; 2,500; 6,250; 15,625; 39,063. | P1 | functional | D-022 |
| TC-BAS-011 | Shield Generator cost curve | Enough Cash | 1) L1–L5. | 2,500; 6,250; 15,625; 39,063; 97,656. | P1 | functional | D-022 |
| TC-BAS-012 | Multiplier Shrine cost curve | Enough Cash | 1) L1–L5. | 3,000; 7,500; 18,750; 46,875; 117,188. | P1 | functional | D-022 |
| TC-BAS-013 | Cost rounding | Unit test of the cost function | 1) Evaluate all modules L1–L5. | Matches [[Canonical Proposed Values]] §12 exactly (half values round up, for example 39,062.5 → 39,063). | P1 | edge | D-022 |
| TC-BAS-014 | Sequential upgrades only | Module L1 | 1) Request L3 directly. | Rejected `invalid_level`. | P1 | negative | D-022 |
| TC-BAS-015 | Upgrade with exactly enough Cash | Cash = cost | 1) Upgrade. | Succeeds; Cash 0. | P1 | edge | D-022 |
| TC-BAS-016 | Upgrade with insufficient Cash | Cash = cost − 1 | 1) Upgrade. | Rejected; nothing changes. | P0 | negative | D-022 |
| TC-BAS-017 | Maximum level | Module L5 | 1) Attempt L6. | Rejected `max_level`; UI shows max. | P2 | edge | D-022 |
| TC-BAS-018 | Sections upgrade independently | All modules L1 | 1) Upgrade Multiplier Shrine to L2. | Only the shrine changes level, effect and appearance; every other module is unchanged. | P0 | functional | D-022 |
| TC-BAS-019 | Upgrade visuals | Any module L1 → L5 | 1) Upgrade each level. | Model changes per [[Base Art Direction]]; upgrade animation plays ([[Animation - Base Upgrades]]); other players see the new model. | P1 | functional | D-022 |
| TC-BAS-020 | Module availability flag | A module disabled in configuration (Q-007) | 1) Open base UI. 2) Send a build request. | Disabled module hidden; request rejected `module_unavailable`. | P1 | negative | D-022 |
| TC-BAS-021 | Upgrade during a raid against own base | Raid active | 1) Owner upgrades Shield Generator or Defence Station. | **PROPOSED**: defensive module upgrades are rejected `raid_in_progress` until the raid ends; non-defensive upgrades follow [[Base Upgrade System]]. | P1 | edge | D-024 |

## 3. Module effects

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BAS-030 | Training Grounds | L0 → L3 | 1) Read Strength and an equipped animal's ATK. | Player Strength ×1.15; equipped animal stats ×1.12; unequipped animals unchanged. | P1 | functional | D-022, D-007 |
| TC-BAS-031 | Multiplier Shrine | L5 | 1) Defeat a Common in Whisperwood. | +15 Cash (10 × 1.0 × 1.5). | P1 | functional | D-022 |
| TC-BAS-032 | Trophy Hall bonus and cap | Trophies for 5 unique bosses, then all 12 | 1) Read Cash bonus. | +5%, then +12% (capped at 12%). A second trophy of the same boss adds nothing. | P1 | functional | D-022 |
| TC-BAS-033 | Bonuses stack additively | Shrine L2 (+20%) and 3 trophies (+3%) | 1) Defeat a Common in Whisperwood. | Cash = 10 × (1 + 0.20 + 0.03) = 12.3 before the rounding rule in [[Wild Animal Cash Rewards]]. | P2 | functional | D-022 |
| TC-BAS-034 | Egg Vault level does not change capacity | Egg Vault L1 → L5 | 1) Read base storage capacity. | Unchanged; only security and visuals change. Capacity changes only through expansion (D-021, Q-009). | P1 | functional | D-021 |
| TC-BAS-035 | Base progression in Progression Score | Total module levels 0, 1, 11, 22, 33, 44 | 1) Read the base term. | 0, 3, 30, 60, 90, 120. | P1 | functional | D-036 |
| TC-BAS-036 | Animal Pens display | Pens built; display rule per Q-008 | 1) Own 100 animals. | If animals are displayed, the count and LOD follow [[Module - Animal Pens]] and the frame-rate budget holds (TC-MOB-030). If not displayed, no animal models are spawned. | P1 | performance | D-022 |

## 4. Plot expansion

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BAS-040 | Plot expansion costs | Enough Cash | 1) Buy stages 1–4. | 5,000; 15,000; 45,000; 135,000. | P1 | functional | D-022 |
| TC-BAS-041 | Beyond the last stage | Stage 4 | 1) Attempt stage 5. | Rejected. | P2 | edge | D-022 |
| TC-BAS-042 | Module slots | Stage 0 with all slots used | 1) Try to build another module. 2) Expand. 3) Retry. | Step 1 rejected `no_slot`; step 3 succeeds. | P1 | functional | D-022 |
| TC-BAS-043 | Expanded plot fits on the server map | 16 players all at stage 4 | 1) Inspect plots. | No overlap or clipping between neighbouring bases. | P1 | edge | D-022 |

## 5. Shields and physical defences

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BAS-050 | Active shield blocks raids | Shield active (however acquired, Q-030) | 1) Attacker attempts to start a raid. | Rejected `shielded`; the shield is visible ([[Animation - Shield Activation]]). | P0 | functional | D-024 |
| TC-BAS-051 | Shield duration and recharge from configuration | Shield Generator L1 → L5; durations configured as `T_shield(L)` | 1) Activate; advance the clock. | Shield lasts exactly `T_shield(L)` and recharges per configuration; no hard-coded values. | P1 | functional | D-024 |
| TC-BAS-052 | Shield expiry at a boundary | Shield expires at time t | 1) Attempt a raid at t − ε and t + ε. | Rejected before t; allowed after t (if other eligibility rules pass). | P1 | edge | D-024 |
| TC-BAS-053 | Defence Station traps | Defence Station L1 | 1) Raider walks through a trap. 2) Owner walks through it. 3) Non-raider visitor walks through it. | Only the raider is affected. | P0 | functional | D-024 |
| TC-BAS-054 | Defence scaling with level | Defence Station L1 → L5 | 1) Measure trap and turret effects. | Values follow [[Module - Defence Station]]; each level strictly stronger. | P2 | functional | D-024 |

## Related documents

- [[Test Cases - Raiding]]
- [[Test Cases - Egg Merging]]
- [[Test Cases - Inventory and Storage]]
- [[Player Base System]]
- [[Base Upgrade System]]
- [[Base Layout and Plot Expansion]]
- [[Base Defence Overview]]
- [[Shield Mechanics]]
- [[Module - Animal Pens]]
- [[Module - Egg Vault]]
- [[Module - Defence Station]]
- [[Module - Shield Generator]]
- [[Module - Training Grounds]]
- [[Module - Multiplier Shrine]]
- [[Module - Trophy Hall]]
- [[Service - BaseService]]
