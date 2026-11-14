---
title: Test Cases - Bosses
type: test-cases
category: qa
status: mixed
priority: P1
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - bosses
  - combat
---

# Test Cases - Bosses

Test cases for mini-bosses and world bosses: spawning, announcements, AI and leash, contribution and rewards, progression gates. System documents: [[Boss Design Overview]], [[Boss AI]], [[Boss Rewards]], [[Service - BossService]], [[UI - Boss Health Bar]], the eight mini-boss and four world-boss documents.

> [!success] CONFIRMED rules under test
> Mini-bosses and world bosses exist (D-012). Defeat penalties vary by battle type (D-013).

> [!warning] UNDECIDED
> Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]); tests assert "the configured reward is granted exactly once per eligible player per spawn". Boss defeat penalties are **UNDECIDED** ([[Open Questions#Q-014]]).

> [!info] PROPOSED values used
> Mini-boss respawn 10 minutes per server; world-boss cadence 45 / 50 / 55 / 60 minutes, announced 2 minutes ahead for [[World Boss - Ironbark Colossus]] (the lead time for the others is read from configuration); one reward per player per spawn; kill credit ≥ 10% (D-040); region gates and Progression Score points ([[Canonical Proposed Values]] §5, §8).

**Fixtures.** `QA_AdvanceClock(s)`, `QA_SpawnBoss(id)`, `QA_SetBossHP(pct)`, `QA_MarkBossDefeated(id)`, `QA_SetConfig("BossReward", id, row)`.

## 1. Spawning and announcements

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BOSS-001 | Mini-boss respawn | [[Mini-Boss - Bramblehorn]] defeated | 1) Advance 9 min 59 s. 2) Advance to 10 min. | Absent at 9:59; present at 10:00 on this server only. | P1 | functional | D-012 |
| TC-BOSS-002 | World boss cadence | Fresh server | 1) Advance the clock and record spawn times for each world boss. | Ironbark every 45 min, [[World Boss - Thunderhoof]] 50, [[World Boss - Abyssal Leviathan]] 55, [[World Boss - Ashwing Condor]] 60, per server. | P1 | functional | D-012 |
| TC-BOSS-003 | World boss announcement | 16 players on the server | 1) Advance to 2 min before Ironbark's spawn. | Every player on the server receives the announcement exactly 2 min before the spawn; players on other servers do not. | P1 | functional | D-012 |
| TC-BOSS-004 | Overlapping world-boss spawns | Cadences coincide (for example at a common multiple) | 1) Advance to the overlap. | Both spawn and both are announced; performance holds (TC-MOB-012). | P2 | edge | D-012 |
| TC-BOSS-005 | Boss still alive at its next cadence | Boss undefeated when the next spawn is due | 1) Advance. | No second copy spawns; behaviour per [[Boss Design Overview]] (despawn or persist). | P2 | edge | D-012 |

## 2. AI, phases and leash

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BOSS-010 | Phase transitions | Boss with phases per its document | 1) Reduce HP across each threshold. | Each phase starts once at its threshold; no phase skipped by burst damage (the transition still triggers). | P1 | functional | D-012 |
| TC-BOSS-011 | Telegraphs | Any boss | 1) Observe each attack. | Every heavy attack has a readable telegraph that starts before the hit ([[Animation - Boss Attacks]], [[Combat Feedback and Readability]]). | P1 | functional | D-012 |
| TC-BOSS-012 | Boss leash reset | Boss engaged | 1) Kite the boss beyond its leash boundary (per [[Boss AI]]). | Boss returns to its arena, resets to full HP, clears its threat table and returns to phase 1. **PROPOSED**: contribution records are cleared, so no reward is granted for pre-reset damage. | P1 | edge | D-012 |
| TC-BOSS-013 | Leash exploit by edge kiting | Players attack from just outside the leash | 1) Attempt repeatedly. | Boss cannot be damaged without retaliation from outside its arena; repeated resets give no reward. | P1 | security | D-012 |
| TC-BOSS-014 | Boss with nobody engaged | All players leave the arena | 1) Wait. | Boss resets per [[Boss AI]] (**PROPOSED**: full reset after the combat tag window). | P2 | edge | D-012 |
| TC-BOSS-015 | Boss is server-owned | Exploit client | 1) Attempt to move the boss locally. | No effect on the server. | P0 | security | D-012 |

## 3. Contribution and rewards

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BOSS-020 | Contribution threshold | Three players | 1) A deals 9.9%, B 10.0%, C the rest. | B and C eligible; A not (D-040). | P0 | edge | D-040 |
| TC-BOSS-021 | Reward exactly once per spawn | Reward row configured (Q-015) | 1) Defeat the boss. 2) Duplicate the final-hit request. | Each eligible player receives the configured reward once; ledger has one entry per player. | P0 | functional | Q-015 |
| TC-BOSS-022 | Same player, next spawn | Player defeated the previous spawn | 1) Defeat the next spawn. | Eligible again (once per player per spawn). | P1 | functional | Q-015 |
| TC-BOSS-023 | Player leaves before the kill | A contributed 30%, leaves before the defeat | 1) Others defeat the boss. | **PROPOSED**: A receives nothing (not present at defeat); no error. | P2 | edge | Q-015 |
| TC-BOSS-024 | Boss defeat penalty | Player defeated by a boss | 1) Observe. | Configured boss penalty (Q-014) applied exactly once. | P1 | functional | D-013 |

## 4. Progression effects

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BOSS-030 | Region gate | Level 8; Bramblehorn not defeated | 1) Try to enter Sunscorch Savanna. 2) Defeat Bramblehorn. 3) Retry. | Step 1 blocked; step 3 allowed ([[Region Unlock Progression]]). | P0 | functional | D-035 |
| TC-BOSS-031 | Progression Score: unique bosses only | — | 1) Defeat Bramblehorn twice. 2) Defeat Ironbark Colossus twice. | PS +10 for the first Bramblehorn, +0 for the second; +20 for the first Ironbark, +0 for the second. | P1 | functional | D-036 |
| TC-BOSS-032 | Starfall Sanctuary needs two different world bosses | Level 80; Cinderjaw defeated; Ironbark defeated twice | 1) Try to enter [[Region - Starfall Sanctuary]]. 2) Defeat Thunderhoof. 3) Retry. | Step 1 blocked (only one unique world boss); step 3 allowed. | P1 | edge | D-035 |
| TC-BOSS-033 | Merge station L4 gate | Region 6 unlocked; no world boss | 1) Attempt L4 (TC-MRG-005). | Blocked until one world boss is defeated. | P1 | functional | D-038 |
| TC-BOSS-034 | Trophy Hall | First defeat of a boss | 1) Check the Trophy Hall. | One trophy for that boss; Cash bonus +1% (cap 12%). | P2 | functional | D-022 |

## 5. Load

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-BOSS-040 | Full server at a world boss | 16 players and 48 companions | 1) Fight for 5 minutes. | Server heartbeat stable; client frame rate per TC-MOB-012. | P0 | performance | D-025 |
| TC-BOSS-041 | Boss health bar accuracy | 16 players damaging | 1) Compare [[UI - Boss Health Bar]] with the server. | Within one replication interval of server HP; never shows the boss dead while the server has it alive. | P2 | functional | D-012 |

## Related documents

- [[Test Cases - Combat]]
- [[Test Cases - Animal AI]]
- [[Test Cases - Multiplayer]]
- [[Boss Design Overview]]
- [[Boss AI]]
- [[Boss Rewards]]
- [[Service - BossService]]
- [[UI - Boss Health Bar]]
- [[Region Unlock Progression]]
