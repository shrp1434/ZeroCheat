---
title: M09 - Hatching
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - hatching
  - hatch-pools
milestone: M09
stage: 3
complexity: M
---

# M09 - Hatching

> [!info] PROPOSED milestone
> Stage 3 · Size **M** · Critical path: near-critical (4 units of slack) · Exit gate: **G3 Core loop slice**

## Objective

Complete stage two of the **CONFIRMED** two-stage randomness: hatching picks an animal from the egg's rarity pool (D-015). Up to **five** eggs hatch at once (D-016). Every hatch is independent: no duplicate protection, no bias towards unowned animals, no history influence (D-018). Hatch odds include progression luck and are shown before the hatch is committed.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Hatch-pool weight calculation with class weights and tilt | Engineering | [[Hatch Pool Tables]], [[Dynamic Progression Luck]] |
| Hatch transaction: select up to five eggs, consume, pick animals, add to collection, atomic save | Engineering | [[Implementation - Egg Roll and Hatch Flow]], [[Service - HatchService]] |
| Hatch location rules (backpack anywhere outside combat, base eggs at base, PROPOSED) | Engineering | [[Hatch System]] |
| Hatch odds display per pool, with `oddsVersion` binding | UI, Engineering | [[UI - Egg Hatching]], [[Randomised Reward Compliance]] |
| Egg storage screen | UI | [[UI - Egg Storage]] |
| Hatch presentation: single and multi-hatch, skippable after first viewing | Animation, VFX | [[Animation - Egg Hatch]], [[Egg Animations]], [[VFX - Rarity and Variant Effects]] |
| Rarity reveal sounds | Audio | [[Sound - Eggs]] |
| Independence verification harness | QA | [[Independent Random Outcomes]], [[Statistical Testing of Probabilities]] |

## Dependencies

- **Upstream:** [[M08 - Egg Rolling]].
- **Downstream:** [[M10 - Ascension]], [[M11 - Egg Merging]], [[M15 - Base Raids]] (stealable base eggs).

## Complexity

**M.** Shares the roll machinery. The multi-hatch transaction and independence proof are the main work.

## Risks

| Risk | Why it matters here |
|---|---|
| R-011 (odds mismatch) | A second disclosed table per rarity. |
| R-013 (pool changes) | Pool structure built here is what live updates will extend. |
| R-005 (bad-luck perception) | Duplicates are intended; their value comes from [[M10 - Ascension]]. |
| R-025 (duplication) | A multi-egg transaction interrupted mid-way must not duplicate or lose eggs. |

## Acceptance criteria

- [ ] One to five eggs hatch in one transaction; six or more are rejected (D-016).
- [ ] Displayed hatch odds equal server odds for every pool at several Progression Score levels.
- [ ] Every pool sums to 100% after normalisation, checked automatically on every build.
- [ ] Statistical tests show no correlation between a hatch result and the player's collection or previous hatches.
- [ ] An interrupted hatch (server shutdown mid-transaction) leaves either the eggs or the animals, never both and never neither.
- [ ] Base-stored eggs cannot be hatched away from the base (PROPOSED rule, config-driven).
- [ ] The hatch presentation can be skipped after first viewing and never delays the server result.

## Testing requirements

- [[Test Cases - Egg Rolls and Hatching]]: multi-hatch, pool selection, location rules, presentation.
- [[Test Cases - Inventory and Storage]]: storage changes after hatching, collection cap interaction.
- [[Statistical Testing of Probabilities]]: per-pool distributions and independence tests.
- [[Test Cases - Persistence]]: hatch transaction under shutdown.

## Open questions

- [[Open Questions#Q-018]]: final hatch pools.
- [[Open Questions#Q-023]]: hatch timing and location.
- [[Open Questions#Q-006]]: variant acquisition (whether hatching can produce variants).
- **UNDECIDED** (Q-1118): whether eggs owned before a later hatch-pool change hatch under the pool current at hatch time or the pool in force when they were rolled. Needed before the first post-launch animal ([[Content Expansion Guidelines]]).

## Key vault documents
- [[Hatch System]] · [[Hatch Pool Tables]] · [[Independent Random Outcomes]]
- [[Egg Storage]] · [[Egg Animations]] · [[Service - HatchService]]
- [[Randomised Reward Compliance]] · [[Probability Balancing]]

## Related documents
- [[Development Roadmap]]
- [[M08 - Egg Rolling]]
- [[M10 - Ascension]]
- [[M11 - Egg Merging]]
- [[Content Expansion Guidelines]]
