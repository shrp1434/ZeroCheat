---
title: Test Cases - Egg Merging
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - eggs
  - merging
  - base
---

# Test Cases - Egg Merging

Test cases for merging three eggs into one egg of the next rarity, and for buying and upgrading the Egg Merging Station. System documents: [[Egg Merging]], [[Egg Merging Station]], [[Implementation - Egg Merge Transaction]], [[Service - MergeService]], [[UI - Egg Merging]], [[Animation - Egg Merge]].

> [!success] CONFIRMED rules under test
> Three eggs of one rarity make one egg of the next rarity; merging needs a purchased Egg Merging Station; higher rarities need station upgrades; the station's appearance changes with each upgrade (D-020). Secret is the highest rarity, so Secret eggs cannot be merged.

> [!info] PROPOSED values used
> Station levels, costs, gates and merge fees (D-038, [[Open Questions#Q-019]]); merging at the player's base; inputs from backpack or base; output to base storage; instant result with a 2.5–6 s animation ([[Open Questions#Q-034]]).

| Station level | Cost (Cash) | Extra gate | Merges unlocked | Fee (Cash) |
|---:|---:|---|---|---|
| 1 | 2,500 | — | Common→Uncommon; Uncommon→Rare | 100; 300 |
| 2 | 15,000 | Region 2 unlocked | Rare→Epic | 900 |
| 3 | 60,000 | Region 4 unlocked | Epic→Legendary | 2,700 |
| 4 | 250,000 | Region 6 unlocked + 1 world boss defeated | Legendary→Mythical | 8,000 |
| 5 | 1,000,000 | Region 8 unlocked | Mythical→Secret | 25,000 |

**Fixtures.** `QA_SetStationLevel(n)`, `QA_FillStorage(container, count, rarity)`, `QA_UnlockRegion(n)`, `QA_MarkBossDefeated(id)`, `QA_SetCash(n)`.

## 1. Station purchase and upgrades

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MRG-001 | Merging without the station | No station purchased; 3 Common eggs | 1) Open merge UI. 2) Send a crafted merge request. | UI shows the purchase prompt instead of the merge panel. Request rejected `no_station`; no eggs consumed, no fee. | P0 | negative | D-020 |
| TC-MRG-002 | Buy the station | At own base; Cash 2,500 | 1) Purchase Level 1 (Twig Nest Press). | Cash 0; station L1 placed in the base with the L1 model. | P0 | functional | D-020, D-038 |
| TC-MRG-003 | Upgrade costs | Station L1; gates met; enough Cash | 1) Upgrade to L2, L3, L4, L5. | Charges 15,000, 60,000, 250,000, 1,000,000 respectively. | P1 | functional | D-038 |
| TC-MRG-004 | Upgrade gate: region | Station L1; Region 2 locked; Cash 15,000 | 1) Attempt L2. | Rejected `gate_not_met` with the gate shown; no Cash taken. Succeeds after `QA_UnlockRegion(2)`. | P0 | negative | D-038 |
| TC-MRG-005 | Upgrade gate: world boss for L4 | Station L3; Region 6 unlocked; no world boss defeated | 1) Attempt L4. 2) Defeat one world boss. 3) Retry. | Step 1 rejected; step 3 succeeds. | P1 | negative | D-038 |
| TC-MRG-006 | Skip a level | Station L1, all gates met | 1) Send a request to upgrade straight to L3. | Rejected `invalid_level`; upgrades are sequential. | P1 | negative | D-020 |
| TC-MRG-007 | Upgrade beyond L5 | Station L5 | 1) Attempt L6. | UI shows max; request rejected. | P2 | edge | D-038 |
| TC-MRG-008 | Appearance changes per level | Station L1 → L5 | 1) Inspect the model after each upgrade, from the owner's and another player's client. | Five distinct models (Twig Nest Press, Stonebound Hatchery Forge, Crystal Incubator, Aurora Crucible, Celestial Convergence Altar) per [[Egg Merging Station]]; replicated to other players; upgrade animation per [[Animation - Base Upgrades]]. | P0 | functional | D-020 |
| TC-MRG-009 | Station counts towards base progression | Station L3 | 1) Read Progression Score inputs. | Station level contributes 3 of the 44 total module levels. | P2 | functional | D-036 |

## 2. Merge rules

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MRG-010 | Common → Uncommon | Station L1; 3 Common eggs; Cash 100; at base | 1) Select three. 2) Confirm. | Three Common eggs removed; one Uncommon egg added; fee 100. | P0 | functional | D-020 |
| TC-MRG-011 | Uncommon → Rare at L1 | Station L1; 3 Uncommon; Cash 300 | 1) Confirm. | One Rare egg; fee 300. | P0 | functional | D-020 |
| TC-MRG-012 | Rare → Epic needs L2 | Station L1; 3 Rare | 1) Attempt. 2) Upgrade to L2. 3) Retry with Cash 900. | Step 1 rejected `station_level_too_low` (UI shows "requires Level 2"); step 3 succeeds, fee 900. | P0 | negative | D-020 |
| TC-MRG-013 | Merging Epic at station level 2 | Station L2; 3 Epic eggs; Cash 2,700 | 1) Attempt Epic → Legendary. | Rejected `station_level_too_low` ("requires Level 3"); no eggs consumed, no fee. | P0 | edge | D-020 |
| TC-MRG-014 | Epic → Legendary at L3 | Station L3; 3 Epic; Cash 2,700 | 1) Confirm. | One Legendary egg; fee 2,700. | P1 | functional | D-020 |
| TC-MRG-015 | Legendary → Mythical at L4 | Station L4; 3 Legendary; Cash 8,000 | 1) Confirm. | One Mythical egg; fee 8,000. | P1 | functional | D-020 |
| TC-MRG-016 | Mythical → Secret at L5 | Station L5; 3 Mythical; Cash 25,000 | 1) Confirm. | One Secret egg; fee 25,000. | P1 | functional | D-020 |
| TC-MRG-017 | Merging Secret eggs | Station L5; 3 Secret eggs | 1) Try to select Secret eggs in the merge UI. 2) Send a crafted request. | Secret eggs are not selectable ("highest rarity"). Request rejected `max_rarity`; nothing consumed. | P0 | edge | D-020 |
| TC-MRG-018 | Merging eggs of different rarities | Station L5; 2 Common + 1 Uncommon | 1) Try in UI. 2) Send crafted request. | UI only allows eggs of the first selected rarity. Request rejected `mixed_rarity`; no egg consumed, no fee. | P0 | edge | D-020 |
| TC-MRG-019 | Two eggs or four eggs | Station L1 | 1) Request with 2 Common. 2) Request with 4 Common. | Both rejected `wrong_count`; exactly three are required. | P0 | negative | D-020 |
| TC-MRG-020 | Same egg ID three times | One Common egg | 1) Request `[E, E, E]`. | Rejected `duplicate_egg`; E not consumed; no output egg (no duplication). | P0 | security | D-020 |
| TC-MRG-021 | Insufficient fee | Station L1; 3 Common; Cash 99 | 1) Confirm. | Rejected `insufficient_cash`; nothing consumed. | P0 | negative | D-038 |
| TC-MRG-022 | Merge away from base | Station L1; player in a region | 1) Send merge request. | Rejected `must_be_at_base` (**PROPOSED** location). | P1 | negative | D-020 |
| TC-MRG-023 | Eggs owned by another player | Crafted request with another player's egg IDs | 1) Send. | Rejected `not_owned`; security log. | P0 | security | D-020 |

## 3. Inputs, outputs and capacity

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MRG-024 | Mixed input sources | 2 Common in backpack, 1 in base | 1) Merge. | Accepted; output egg goes to base storage. Backpack −2, base −1 + 1. | P1 | functional | D-020 |
| TC-MRG-025 | Base-only inputs free two slots | Base 50/50; 3 Common in base | 1) Merge. | Base 48/50. | P1 | functional | D-020 |
| TC-MRG-026 | Base full, all inputs from the backpack | Base 50/50; 3 Common in backpack | 1) Merge. | Output placement is **UNDECIDED** (Q-1001). Expected invariant: either the merge is rejected before anything is consumed, or the output goes to a slot that is free after consumption. An egg is never destroyed, and no container exceeds capacity (INV-01, INV-06). | P0 | edge | D-020, D-021 |
| TC-MRG-027 | Output visibility to raids | Merge with backpack inputs | 1) Merge. | The UI states that the output egg goes to base storage, where it can be stolen during a raid (**PROPOSED** warning). | P2 | functional | D-021, D-024 |
| TC-MRG-028 | Merge during a raid on own base | Raid active; inputs in base storage | 1) Defender merges while the raider steals one of the inputs in the same frame. | Exactly one operation commits. If the theft wins, the merge is rejected `egg_unavailable` and no fee is charged. If the merge wins, the theft is rejected. (See TC-MP-020.) | P0 | edge | D-024 |

## 4. Output fairness and presentation

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MRG-030 | Output rarity is deterministic | Any merge | 1) Merge 3 Rare at L2. | Output is always exactly one Epic egg; no random element in the merge itself. | P0 | functional | D-020 |
| TC-MRG-031 | Merged eggs hatch like rolled eggs | Harness; PS 300 | 1) Hatch 100,000 merged Rare eggs and 100,000 rolled Rare eggs. 2) Two-sample χ². | Not rejected at α 0.001; the egg record carries no hidden modifier ([[Statistical Testing of Probabilities]] §6.6). | P0 | statistical | D-018, D-020 |
| TC-MRG-032 | Merge animation length by tier | L1 to L5 merges | 1) Time each animation. | Between 2.5 s and 6 s, longer for higher tiers; result committed on the server before the animation starts. | P2 | functional | Q-034 |
| TC-MRG-033 | Disconnect during merge animation | Merge confirmed | 1) Kill the client. 2) Rejoin. | Output egg present; inputs gone; fee charged once. | P0 | edge | D-020 |
| TC-MRG-034 | Server dies mid-merge | `QA_KillServerMidTransaction(after_inputs_removed)` | 1) Merge. 2) Rejoin elsewhere. | All-or-nothing: either three inputs gone with output present and fee paid, or nothing changed. | P0 | edge | D-020 |
| TC-MRG-035 | Double confirm | Requirements for one merge | 1) Double-tap confirm. | One merge only. | P0 | edge | D-020 |

## Related documents

- [[Test Cases - Egg Rolls and Hatching]]
- [[Test Cases - Inventory and Storage]]
- [[Test Cases - Bases and Upgrades]]
- [[Test Cases - Raiding]]
- [[Egg Merging]]
- [[Egg Merging Station]]
- [[Implementation - Egg Merge Transaction]]
- [[Service - MergeService]]
- [[UI - Egg Merging]]
