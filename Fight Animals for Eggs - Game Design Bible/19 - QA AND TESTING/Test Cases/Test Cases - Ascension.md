---
title: Test Cases - Ascension
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - ascension
  - progression
---

# Test Cases - Ascension

Test cases for ascending animals by consuming duplicates. System documents: [[Ascension System]], [[Ascension Progression Table]], [[Implementation - Ascension Transaction]], [[Service - AscensionService]], [[UI - Ascension]].

> [!success] CONFIRMED rules under test
> Ascension consumes the required duplicates of the same animal; the original is kept (D-019). Duplicates come from independent hatches (D-018).

> [!info] PROPOSED values used
> Five levels A1–A5 (D-037, [[Open Questions#Q-004]]); duplicate requirements and fees `fee(n) = base × n` per rarity ([[Open Questions#Q-005]]); +8% HP/ATK/DEF and +5% ability effectiveness per level ([[Canonical Proposed Values]] §9).

**Duplicates and fees used in the expected results** (from [[Canonical Proposed Values]] §9):

| Rarity | Duplicates A1 / A2 / A3 / A4 / A5 | Total | Fee for step *n* | Total fees A0 → A5 |
|---|---|---:|---|---:|
| Common | 1 / 2 / 3 / 4 / 5 | 15 | 100 × n | 1,500 |
| Uncommon | 1 / 2 / 3 / 3 / 4 | 13 | 200 × n | 3,000 |
| Rare | 1 / 1 / 2 / 3 / 3 | 10 | 400 × n | 6,000 |
| Epic | 1 / 1 / 2 / 2 / 3 | 9 | 800 × n | 12,000 |
| Legendary | 1 / 1 / 1 / 2 / 2 | 7 | 1,600 × n | 24,000 |
| Mythical | 1 / 1 / 1 / 1 / 2 | 6 | 3,200 × n | 48,000 |
| Secret | 1 / 1 / 1 / 1 / 1 | 5 | 6,400 × n | 96,000 |

**Fixtures.** `QA_GrantAnimal(species, count, ascension)`, `QA_SetCash(n)`, `QA_KillServerMidTransaction(stage)`.

## 1. Core ascension

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-ASC-001 | Common A0 → A1 | Original [[Rabbit]] A0 plus 1 duplicate; Cash 100 | 1) Open ascension. 2) Confirm. | Original becomes A1 and keeps its instance ID; 1 duplicate consumed; Cash 0; ledger `ascension_fee −100`. | P0 | functional | D-019 |
| TC-ASC-002 | Common A1 → A2 | Original A1 plus 2 duplicates; Cash 200 | 1) Confirm. | A2; 2 duplicates consumed; fee 200. | P0 | functional | D-019 |
| TC-ASC-003 | Common A0 → A5 full path | Original plus 15 duplicates; Cash 1,500 | 1) Ascend five times. | Final A5; 15 duplicates consumed in total; total fees 1,500; Cash 0. | P1 | functional | D-019, D-037 |
| TC-ASC-004 | Secret first step | Original [[Mosasaurus]] plus 1 duplicate; Cash 6,400 | 1) Confirm. | A1; fee 6,400. | P1 | functional | D-019 |
| TC-ASC-005 | Secret A4 → A5 | Original A4 plus 1 duplicate; Cash 32,000 | 1) Confirm. | A5; fee 32,000. | P1 | functional | D-037 |
| TC-ASC-006 | Ascending without enough duplicates | Common A2 with 2 duplicates (needs 3) | 1) Open ascension. 2) Send a crafted request anyway. | UI shows "2 / 3 duplicates" and the confirm is disabled. Request rejected `insufficient_duplicates`. No duplicate consumed, no fee charged, level unchanged. | P0 | edge | D-019 |
| TC-ASC-007 | Enough duplicates, not enough Cash | Common A0 with 1 duplicate; Cash 99 | 1) Confirm. | Rejected `insufficient_cash`; nothing consumed. | P0 | negative | D-019 |
| TC-ASC-008 | Beyond the maximum level | Original A5 with spare duplicates | 1) Attempt ascension. | UI shows "Max"; request rejected `max_level`; nothing consumed. | P0 | edge | D-037 |
| TC-ASC-009 | Duplicates must be the same species | Original Rabbit; offered duplicate is a [[Squirrel]] | 1) Send request with the Squirrel's ID. | Rejected `not_duplicate`; nothing consumed. | P0 | negative | D-019 |
| TC-ASC-010 | Original used as its own duplicate | Original A | 1) Request ascending A consuming A. | Rejected `invalid_duplicate`; A unchanged and still owned. | P0 | security | D-019 |
| TC-ASC-011 | Same duplicate listed twice | Common A1 needs 2; one duplicate D | 1) Request with `[D, D]`. | Rejected `duplicate_id`; D not consumed. | P0 | security | D-019 |
| TC-ASC-012 | Duplicate owned by another player | Another player's instance ID | 1) Request. | Rejected `not_owned`; security log. | P0 | security | D-019 |
| TC-ASC-013 | Extra duplicates supplied | Needs 1; request lists 3 | 1) Confirm. | **PROPOSED**: rejected `wrong_duplicate_count` (the client must send exactly the requirement); nothing consumed. | P1 | negative | D-019 |

## 2. Equipped, defending and special animals

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-ASC-020 | Ascending an equipped animal at base | Equipped original; duplicates available; at own base | 1) Ascend it. | Accepted (**PROPOSED**); team composition unchanged; new stats apply immediately to the companion. | P0 | edge | D-010, D-019 |
| TC-ASC-021 | Ascending an equipped animal away from base | As above, player in a region | 1) Attempt. | Behaviour follows the location rule in [[Ascension System]]. Whatever the rule, the team composition never changes (D-010) and the result is either fully applied or rejected. Final rule **UNDECIDED** (Q-1005). | P1 | edge | D-010 |
| TC-ASC-022 | Equipped animal offered as a duplicate | Copy B is equipped; copy A is the target | 1) Request consuming B. | **PROPOSED**: rejected `duplicate_equipped` (consuming an equipped animal would change the team, which D-010 forbids away from base and the UI must make explicit at base). Final rule (Q-1005). | P0 | edge | D-010 |
| TC-ASC-023 | Ascended copy offered as a duplicate | Copy B is A2 | 1) Select B as fodder. | UI warns that B's ascension is lost; server accepts only with the explicit confirmation flag (**PROPOSED**). | P2 | edge | D-019 |
| TC-ASC-024 | Variant copy as duplicate or target | A variant copy (for example Golden) of the species | 1) Use it as fodder. 2) Use it as the target. | Eligibility follows the configured variant rule (Q-006, Q-024); whether variant copies count as duplicates is **UNDECIDED** (Q-1006). The UI states which copies are eligible before commit. A variant original keeps its variant after ascension. | P1 | edge | D-028 |
| TC-ASC-025 | Animal defending during an active raid | Raid in progress; the animal is a knocked-out defender | 1) Owner attempts to ascend it or use it as fodder. | **PROPOSED**: rejected `in_raid` while the raid is active, so theft and ascension cannot interleave. Exactly one operation commits under any timing (INV-02). | P0 | edge | D-024 |

## 3. Stat effects

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-ASC-030 | Stat increase per level | Animal with base HP 200, ATK 20, DEF 10 (reference stats) | 1) Read stats at A0, A3, A5. | A3: HP 248, ATK 24.8, DEF 12.4. A5: HP 280, ATK 28, DEF 14 (+8% of base per level, additive). | P0 | functional | D-037 |
| TC-ASC-031 | Ability effectiveness | Same ability at A0 and A5 | 1) Compare damage, heal and duration. | A5 is ×1.25 of A0 for the ability component. | P1 | functional | D-037 |
| TC-ASC-032 | AS and MS unaffected | Any animal | 1) Compare attack speed and move speed A0 vs A5. | Unchanged (ascension affects HP, ATK, DEF and ability effectiveness only). | P2 | functional | D-037 |
| TC-ASC-033 | Visual tier per level | One animal from A0 to A5 | 1) Inspect after each step. | A1 coloured trim; A2 eye glint; A3 soft aura; A4 particle accents; A5 crest and full aura ([[Animation - Ascension]], [[VFX - Rarity and Variant Effects]]). Visible to other players. | P1 | functional | D-037 |
| TC-ASC-034 | Ascension does not change Player Strength | Equipped animal ascended | 1) Read Player Strength. | Unchanged (D-007). | P1 | functional | D-007 |

## 4. Transactions and robustness

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-ASC-040 | Double confirm | Requirements met for one step | 1) Tap confirm twice quickly. | Exactly one step applied; duplicates and fee consumed once. | P0 | edge | D-019 |
| TC-ASC-041 | Server dies mid-transaction | `QA_KillServerMidTransaction(after_consume)` | 1) Ascend. 2) Rejoin on another server. | Either the full ascension (level up, duplicates gone, fee paid) or nothing; never duplicates gone without the level-up (INV-02, INV-03). | P0 | edge | D-019 |
| TC-ASC-042 | Client disconnect during animation | Ascension confirmed | 1) Disconnect during the animation. 2) Rejoin. | Ascension persisted. | P1 | edge | D-019 |
| TC-ASC-043 | Rate of requests | Exploit client | 1) Send 50 ascension requests per second. | Throttled by the rate limiter ([[Implementation - Rate Limiting]]); every accepted request is valid. | P1 | security | D-019 |
| TC-ASC-044 | Ascension progress UI | Partial duplicates | 1) Open the ascension screen. | Shows current level, next-step requirement, owned eligible duplicates and fee; matches the server. | P2 | functional | D-019 |

## Related documents

- [[Test Cases - Egg Rolls and Hatching]]
- [[Test Cases - Raiding]]
- [[Test Cases - Persistence]]
- [[Ascension System]]
- [[Ascension Progression Table]]
- [[Ascension Expected Value Analysis]]
- [[Implementation - Ascension Transaction]]
- [[Service - AscensionService]]
- [[UI - Ascension]]
