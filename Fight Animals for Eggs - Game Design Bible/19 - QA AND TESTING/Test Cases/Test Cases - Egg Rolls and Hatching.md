---
title: Test Cases - Egg Rolls and Hatching
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
  - hatching
  - luck
  - compliance
---

# Test Cases - Egg Rolls and Hatching

Test cases for the egg roll (stage 1: rarity), dynamic progression luck, odds disclosure, and hatching (stage 2: animal from the rarity pool). System documents: [[Egg Roll System]], [[Hatch System]], [[Dynamic Progression Luck]], [[Independent Random Outcomes]], [[Randomised Reward Compliance]]. Statistical method: [[Statistical Testing of Probabilities]].

> [!success] CONFIRMED rules under test
> Two-stage randomness (D-015); up to five eggs hatched at once (D-016); luck affects egg and hatch odds only, odds shown before commit and never changed silently (D-017); every hatch independent (D-018); Cash buys rolls (D-014); storage 10 + 50 (D-021).

> [!info] PROPOSED values used
> Roll price 200 Cash, bulk ×5 for 1,000 Cash (D-039, Q-020); baseline odds 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02% (D-031, Q-016); luck formula (D-036, Q-017); pool weights (Q-018); `oddsVersion` tokens (D-041); hatch location rule and instant hatch with animation (Q-023); owned-animal capacity working assumption 100 (Q-022). Where an expected result depends on a PROPOSED behaviour that the owning system document may still change, the row says **PROPOSED**.

**Conventions.** Priority P0–P3 as in [[QA Strategy]]. Types: functional, edge, negative, security, performance, statistical. "No state change" means Cash, eggs, animals and the ledger are byte-identical before and after (INV-01 to INV-03). Every case ends with the invariant report.

**Fixtures.** `QA_SetCash(n)`, `QA_SetProgressionScore(ps)`, `QA_FillStorage(container, count, rarity)`, `QA_SetOwnedAnimals(list)`, `QA_StubRng(values)`, `QA_ForceCombatTag(seconds)`. All are QA-build-only hooks.

## 1. Rolling eggs

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-EGG-001 | Single roll charges price and delivers one egg | Cash 1,000; free capacity | 1) Open egg shrine. 2) Read displayed odds. 3) Confirm single roll. | Cash 800. Exactly one egg added with the rolled rarity. Ledger has one entry `roll −200`. | P0 | functional | D-014, D-039 |
| TC-EGG-002 | Roll with Cash exactly equal to the price | Cash 200; free capacity | 1) Confirm single roll. | Roll succeeds. Cash is exactly 0, not negative. One egg added. | P0 | edge | D-014 |
| TC-EGG-003 | Roll with one Cash short | Cash 199 | 1) Attempt single roll. | Confirm button disabled; a crafted request is rejected with reason `insufficient_cash`. No state change. | P0 | negative | D-014 |
| TC-EGG-004 | Bulk roll ×5 | Cash 1,000; ≥ 5 free slots | 1) Confirm Roll ×5. | Cash 0. Five eggs added; each rarity drawn independently (rarities may differ). One ledger entry `roll_bulk −1,000` or five entries of −200 (either, consistently). | P0 | functional | D-039 |
| TC-EGG-005 | Bulk roll with insufficient Cash | Cash 999 | 1) Attempt Roll ×5. | Rejected `insufficient_cash`. No partial rolls (**PROPOSED**: bulk is all-or-nothing). No state change. | P1 | negative | D-039 |
| TC-EGG-006 | Roll with no available egg capacity anywhere | Backpack 10/10 and base 50/50 (no expansions) | 1) Attempt single roll. | Rejected before payment with reason `no_capacity` and a message pointing to storage or merging. Cash unchanged. No egg created or discarded. | P0 | edge | D-021 |
| TC-EGG-007 | Roll destination when one container is full | Backpack 10/10; base 20/50 | 1) Single roll. | Egg placed in the container defined by the destination rule in [[Egg Storage]]; capacity never exceeded (INV-06). The roll result screen states where the egg went. | P0 | edge | D-021 |
| TC-EGG-008 | Bulk roll with fewer than five free slots | Total free slots 3; Cash 1,000 | 1) Attempt Roll ×5. | **PROPOSED**: rejected before payment (`no_capacity`, "need 5 free slots"). Never charge for an egg that cannot be stored. Final policy **UNDECIDED** (Q-1003). | P1 | edge | D-021 |
| TC-EGG-009 | Double-tap confirm | Cash 400 | 1) Tap confirm twice within 50 ms. | Exactly as many rolls as distinct request IDs accepted by the server; a repeated request ID is processed once. With one UI request ID: Cash 200, one egg. | P0 | edge | D-041 |
| TC-EGG-010 | Roll while combat-tagged | Combat tag active | 1) Attempt roll at the shrine. | Behaviour follows [[Egg Roll System]] location rules; whatever the rule, the roll either completes fully or is rejected with no state change. | P2 | edge | D-014 |
| TC-EGG-011 | Roll result is server-authoritative | Network inspector in QA build | 1) Roll. 2) Inspect the request payload. | Request contains only intent (`count`, `oddsVersion`, `requestId`). The rarity arrives in the server response; no rarity is computed on the client (INV-11). | P0 | security | D-015 |
| TC-EGG-012 | Egg rarity never changes after the roll | Rolled a Rare egg | 1) Level up. 2) Rejoin. 3) Move egg between containers. | The egg remains Rare in every state; its rarity field is immutable. | P0 | functional | D-017 |
| TC-EGG-013 | Rolling does not register animals in the index | Fresh profile | 1) Roll several eggs. | Index unchanged; rolls create eggs, not discoveries or ownership. | P2 | functional | D-029 |
| TC-EGG-014 | Cash-purchased rolls are not a Robux product | Shop configuration | 1) Inspect all Robux products. | No Robux product grants Cash or rolls directly (**PROPOSED** D-044; Q-032). If any paid random item is ever added, it is hidden from players for whom `ArePaidRandomItemsRestricted` is true. | P0 | security | D-027, D-044 |

## 2. Luck and odds disclosure

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-EGG-021 | Odds shown before every roll | Any player | 1) Open roll UI. | All seven tiers and their current percentages are visible before the confirm control is active. | P0 | functional | D-017 |
| TC-EGG-022 | Displayed odds equal server odds | `QA_SetProgressionScore(215)` | 1) Open roll UI. 2) Compare with `computeRarityOdds(0.215)`. | Display shows 66.810896 / 21.459660 / 8.307164 / 2.611792 / 0.654541 / 0.140981 / 0.014966 % to the display precision. | P0 | functional | D-017, D-036 |
| TC-EGG-023 | Baseline odds at the pivot | `QA_SetProgressionScore(300)` | 1) Open roll UI. | Exactly 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 %. | P0 | functional | D-031, D-036 |
| TC-EGG-024 | Odds at the extremes | PS 0, then PS 1000 | 1) Read odds at each. | PS 0: Secret 0.000885%. PS 1000: Secret 0.052975%, Common 53.138612%. Full rows match [[Statistical Testing of Probabilities]] table 2.1. | P0 | functional | D-036 |
| TC-EGG-025 | Progression Score clamp | `QA_SetProgressionScore(1250)`, then `(-50)` | 1) Read odds. | Identical to PS 1000 and PS 0 respectively. No error, no NaN. | P1 | edge | D-036 |
| TC-EGG-026 | Stale `oddsVersion` is rejected | Roll UI open with token A | 1) Via QA hook, add XP so the player levels up (odds change, token B issued). 2) Confirm roll with token A. | Rejected `stale_odds`. No charge. UI re-displays the new odds with token B and requires a new confirmation. | P0 | edge | D-017, D-041 |
| TC-EGG-027 | Odds change while the UI is open | Roll UI open | 1) Discover a new species in the background (PS rises). | UI updates the displayed odds (or marks them outdated) before the next confirmation is possible. Odds never change between confirm and result. | P0 | functional | D-017 |
| TC-EGG-028 | Another player's `oddsVersion` | Two players with different PS | 1) Player A submits a roll with player B's token. | Rejected `invalid_odds_token`. Tokens are bound to user ID. No state change. | P0 | security | D-041 |
| TC-EGG-029 | Forged or malformed `oddsVersion` | Exploit test client | 1) Send `oddsVersion` = random string, nil, number, very long string. | All rejected; no state change; security log entry written. | P0 | security | D-041 |
| TC-EGG-030 | Client attempts to modify hatch or roll probabilities | Exploit test client with modified local odds module and a crafted payload containing an `odds` table | 1) Change client-side odds to 100% Secret. 2) Roll 1,000 times. 3) Hatch with a payload field forcing an animal. | Server ignores client odds and extra fields. Outcomes follow server odds (with 1,000 rolls at PS 300 the Secret count is consistent with 0.02%: Wilson 95% upper bound contains it). Payload rejected or extra fields discarded; security log entry written. | P0 | security | D-017 |
| TC-EGG-031 | No non-zero tier is displayed as 0% | PS 0 | 1) Read Secret odds display. | Displayed as a non-zero value (0.000885% or a "< 0.001%" format approved in [[Randomised Reward Compliance]]). Never "0%". | P0 | edge | D-017 |
| TC-EGG-032 | Displayed odds sum | Any PS | 1) Sum displayed tier values. | Sum is 100% within the display rounding tolerance stated on the UI. | P2 | functional | D-017 |
| TC-EGG-033 | Formula stays hidden | Any player | 1) Inspect remotes and replicated data. | Client receives final odds and token only. Slopes and pivot are not replicated (the formula may stay hidden; the odds may not). | P2 | security | D-017 |
| TC-EGG-034 | Luck does not affect wild encounters | Players at PS 0 and PS 1000 in the same region | 1) Run TC-AI-042. | Wild spawn rarity distribution is identical for both players. | P0 | statistical | D-017 |
| TC-EGG-035 | Monotonic odds | Unit test | 1) Evaluate odds on 1,001 points of P. | Common non-increasing; every other tier non-decreasing; all tiers > 0; sum 100. | P1 | functional | D-036 |

## 3. Selection and statistics

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-EGG-036 | Cumulative boundary mapping | Stub RNG; PS 300 | 1) Feed each `u` value in [[Statistical Testing of Probabilities]] §3. | Every `u` maps to the expected tier; `u` just below 1 returns Secret, never nil. | P0 | edge | D-015 |
| TC-EGG-037 | Rarity distribution at the pivot | Harness; PS 300 | 1) 10,000,000 rolls. 2) Omnibus χ² and per-tier binomial. | χ² ≤ 22.458 (df 6, α 0.001); no per-tier test rejects after Holm–Bonferroni. | P0 | statistical | D-031 |
| TC-EGG-038 | Rarity distribution at P = 0 and P = 1 | Harness | 1) 10,000,000 rolls at each. | Same criteria against table 2.1 rows. | P0 | statistical | D-036 |
| TC-EGG-039 | Secret rate Wilson interval | Output of TC-EGG-037 | 1) Compute 99.9% Wilson interval for Secret. | Interval contains 0.02% (with 2,000 expected Secrets the 99.9% interval is about 0.0186% – 0.0215%). | P0 | statistical | D-031 |
| TC-EGG-040 | Roll independence | Harness | 1) Runs test and lag-1…20 autocorrelation on 1,000,000 rolls. | `|Z| ≤ 3.29`; every `|r_k| ≤ 0.00329` after correction. | P0 | statistical | D-018 |
| TC-EGG-041 | Conditional distribution after a Legendary-or-better roll | Harness, 10,000,000 rolls | 1) Collect the roll after each Legendary+ roll. 2) χ² against pivot odds. | Not rejected at α 0.001. | P0 | statistical | D-018 |
| TC-EGG-042 | Bulk rolls equal five singles | Harness | 1) 2,000,000 bulk rolls (10,000,000 eggs). | Distribution matches single-roll odds; position-in-bulk has no effect (χ² per position). | P1 | statistical | D-018 |

## 4. Hatching

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-EGG-046 | Hatch one egg | One Common egg in backpack; out of combat | 1) Select egg. 2) Read hatch odds. 3) Confirm. | Egg removed; exactly one animal from the Common pool added; index marks it owned. Animal decided by the server before the animation starts. | P0 | functional | D-015 |
| TC-EGG-047 | Hatch odds shown before hatch | Common egg selected | 1) Open hatch confirmation. | Per-animal odds for the Common pool at the player's current P are displayed with a hatch `oddsVersion`. | P0 | functional | D-017 |
| TC-EGG-048 | Stale hatch odds token | Hatch confirmation open | 1) Level up via QA hook. 2) Confirm with old token. | Rejected `stale_odds`; egg not consumed; new odds displayed. | P0 | edge | D-041 |
| TC-EGG-049 | Hatch five eggs at once | Five eggs selected | 1) Confirm multi-hatch. | Five eggs removed; five animals added, each from its own egg's rarity pool; one 5.0 s multi-hatch presentation (skippable after first viewing, **PROPOSED**). | P0 | functional | D-016 |
| TC-EGG-050 | Attempt to hatch six eggs | Six eggs available | 1) Try to select a sixth egg in UI. 2) Send a crafted request with six egg IDs. | UI selection stops at five with a "maximum 5" message. Crafted request rejected entirely (`too_many_eggs`); **no** egg consumed, not even the first five. | P0 | edge | D-016 |
| TC-EGG-051 | Hatch request with zero eggs | — | 1) Send an empty list. | Rejected `invalid_request`; no state change. | P2 | negative | D-016 |
| TC-EGG-052 | Same egg ID twice in one request | One egg | 1) Send `[eggA, eggA]`. | Rejected `duplicate_egg`; egg not consumed; no animal granted. | P0 | security | D-016 |
| TC-EGG-053 | Mixed-rarity multi-hatch | One Common, one Epic, one Secret egg | 1) Hatch all three. | Each animal comes from its own egg's pool (Common animal from the Common egg, etc.). | P0 | functional | D-015 |
| TC-EGG-054 | No duplicate protection | Player owns all 12 Common animals | 1) Hatch 50 Common eggs (or harness 200,000). | Every result is a duplicate; distribution matches pool odds (§6.4 of the statistics page). No re-roll, no conversion. | P0 | statistical | D-018 |
| TC-EGG-055 | No bias towards unowned animals | Player owns all 8 Standard Common animals; PS 300 | 1) Harness 200,000 Common hatches. | Unowned share consistent with 18.367% (binomial, α 0.001). | P0 | statistical | D-018 |
| TC-EGG-056 | No history influence | Harness | 1) Distribution of the hatch after a duplicate vs after a new animal. | Two-sample χ² not rejected. | P0 | statistical | D-018 |
| TC-EGG-057 | Five-egg independence | Harness, 200,000 five-egg Common hatches | 1) Per-position χ². 2) Pair contingency (1,2) and (1,5). | No test rejects at α 0.001 after correction. | P0 | statistical | D-016, D-018 |
| TC-EGG-058 | Pool odds with luck tilt | PS 1000 | 1) Harness 1,000,000 Secret-egg hatches. | Rates match 30.1205 / 30.1205 / 24.3976 / 15.3614 % (Mosasaurus, Quetzalcoatlus, Titanoboa, Tyrannosaurus Rex). | P0 | statistical | D-017, Q-018 |
| TC-EGG-059 | Backpack egg hatch outside combat | Backpack egg; no combat tag; in the wild | 1) Hatch. | Succeeds anywhere outside combat (**PROPOSED** location rule). | P1 | functional | Q-023 |
| TC-EGG-060 | Backpack egg hatch while combat-tagged | Combat tag active | 1) Attempt hatch. 2) Wait for the 8 s tag to expire. 3) Retry. | Step 1 rejected `in_combat`; egg not consumed. Step 3 succeeds. | P1 | edge | Q-023 |
| TC-EGG-061 | Base-stored egg hatch away from base | Egg in base storage; player in a region | 1) Attempt hatch of the base egg. | Rejected `must_be_at_base` (**PROPOSED** rule); egg not consumed. | P1 | negative | Q-023 |
| TC-EGG-062 | Base-stored egg hatch at own base | Player inside own base | 1) Hatch base egg. | Succeeds; base storage frees one slot. | P1 | functional | Q-023 |
| TC-EGG-063 | Hatch with owned-animal storage full | Owned animals at the configured capacity (working assumption 100, Q-022) | 1) Hatch one egg. | **PROPOSED**: rejected before consumption (`animal_storage_full`). Final behaviour **UNDECIDED** (Q-1004). The egg is never consumed without an animal being granted. | P0 | edge | Q-022 |
| TC-EGG-064 | Multi-hatch exceeding remaining animal capacity | Capacity − 2 owned; five eggs selected | 1) Confirm. | **PROPOSED**: whole request rejected with "room for 2". Never a partial hatch that consumes eggs without granting animals (Q-1004). | P1 | edge | Q-022 |
| TC-EGG-065 | Disconnect during hatch animation | Hatch confirmed | 1) Kill the client during the animation. 2) Rejoin. | Animal is in the collection; egg is gone; result screen can be replayed from the hatch log or the animal appears flagged "new". | P0 | edge | D-015 |
| TC-EGG-066 | Skip hatch animation | Animation already viewed once | 1) Hatch; press skip. | Result shown immediately; same animal as the server log. | P3 | functional | Q-023 |
| TC-EGG-067 | Hatched animal registers in index as owned | Animal discovered but not owned | 1) Hatch it. | Index entry changes from "discovered" to "owned"; PS discovery points unchanged if already discovered (**PROPOSED**: PS counts discoveries, not ownership). | P1 | functional | D-029 |
| TC-EGG-068 | Defender hatches an egg that a raider is stealing | Active raid; egg E in base storage | 1) Defender confirms hatch of E. 2) Raider confirms theft of E in the same server frame. | Exactly one operation commits. Either the defender owns the new animal and the theft is rejected `egg_unavailable`, or the raider owns E and the hatch is rejected. E exists in exactly one place (INV-01). See TC-MP-020. | P0 | edge | D-024 |
| TC-EGG-069 | Variant odds disclosure (if variants come from hatching) | Variant acquisition configured through hatching (Q-006) | 1) Open hatch confirmation. | If enabled, variant chances are displayed before commit with the same token rules. If disabled, no variant can result from a hatch. | P1 | functional | D-028 |

## 5. Coverage summary

| Area | Cases | Key decisions |
|---|---|---|
| Roll purchase and capacity | TC-EGG-001 to 014 | D-014, D-021, D-039 |
| Luck and disclosure | TC-EGG-021 to 035 | D-017, D-036, D-041 |
| Selection statistics | TC-EGG-036 to 042 | D-015, D-018, D-031 |
| Hatching | TC-EGG-046 to 069 | D-015, D-016, D-018 |

## Related documents

- [[Statistical Testing of Probabilities]]
- [[Test Cases - Egg Merging]]
- [[Test Cases - Inventory and Storage]]
- [[Test Cases - Exploit Prevention]]
- [[Egg Roll System]]
- [[Hatch System]]
- [[Dynamic Progression Luck]]
- [[Independent Random Outcomes]]
- [[Randomised Reward Compliance]]
- [[Service - EggService]]
- [[Service - HatchService]]
- [[Service - LuckService]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[UI - Egg Rolling]]
- [[UI - Egg Hatching]]
