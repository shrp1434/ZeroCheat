---
title: M11 - Egg Merging
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - egg-merging
milestone: M11
stage: 4
complexity: M
---

# M11 - Egg Merging

> [!info] PROPOSED milestone
> Stage 4 · Size **M** · Critical path: no (10 units of slack) · Exit gate: **G4 Base alpha**

## Objective

Build the deterministic egg path: **three** eggs of one rarity merge into **one** egg of the next rarity (D-020 **CONFIRMED**). Merging needs a purchased **Egg Merging Station** at the player's base. The station must be upgraded before it can merge higher rarities and physically changes appearance at each upgrade. Secret eggs cannot be merged further. Levels, costs and fees are **PROPOSED** ([[Open Questions#Q-019]]).

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Station purchase and five upgrade levels with gates | Engineering, Economy | [[Egg Merging Station]], [[Canonical Proposed Values#10. Egg merging and the Egg Merging Station]] |
| Merge transaction: validate three same-rarity eggs, station level, fee, consume, create output in base storage | Engineering | [[Implementation - Egg Merge Transaction]], [[Service - MergeService]] |
| Merge rules (inputs from backpack or base storage; output to base storage) | Design | [[Egg Merging]] |
| Merge screen | UI | [[UI - Egg Merging]] |
| Five station models, one per level, visibly different | Art | [[Base Art Direction]], [[Egg Art Direction]] |
| Merge animation by tier | Animation, VFX | [[Animation - Egg Merge]] |
| Merge sounds | Audio | [[Sound - Eggs]] |

## Dependencies

- **Upstream:** [[M09 - Hatching]] (eggs and storage), [[M12 - Player Bases]] (the station sits in the base).
- **Downstream:** [[M18 - UI and UX]]; raids in [[M15 - Base Raids]] must respect merge outputs stored in the base.

## Complexity

**M.** Similar transaction shape to ascension, plus five art states for the station.

## Risks

| Risk | Why it matters here |
|---|---|
| R-025 (duplication) | Three-in, one-out transaction under interruption. |
| R-008 (late-game wall) | Station levels 4–5 are the largest PROPOSED cash sinks. |
| R-010 (storage) | Merging frees storage; output goes to base storage, where it is raidable. |

## Acceptance criteria

- [ ] Merging requires a purchased station; without one, the request is rejected.
- [ ] Each merge tier is available only at or above its station level.
- [ ] Exactly three eggs of the same rarity produce exactly one egg of the next rarity; Secret eggs cannot be merged.
- [ ] Merge results are deterministic: no random outcome is involved, so no odds table applies to the merge itself.
- [ ] The station model changes at every upgrade level and replicates to visitors.
- [ ] An interrupted merge leaves the three inputs or the one output, never both and never neither.
- [ ] The number of stored eggs always falls by two after a merge (three in, one out), freeing two slots.

## Testing requirements

- [[Test Cases - Egg Merging]]: tiers, gates, fees, Secret limit, output location.
- [[Test Cases - Inventory and Storage]]: inputs from both locations, capacity changes.
- [[Test Cases - Bases and Upgrades]]: station purchase and upgrade visuals.
- [[Test Cases - Persistence]]: merge under shutdown.

## Open questions

- [[Open Questions#Q-019]]: final station upgrade costs.
- [[Open Questions#Q-034]]: merge timing (instant with animation versus timed).
- **UNDECIDED** (Q-1114): whether any future event eggs can be merged (see [[Seasonal and Limited-Time Events]]).

## Key vault documents
- [[Egg Merging]] · [[Egg Merging Station]] · [[Implementation - Egg Merge Transaction]]
- [[Service - MergeService]] · [[UI - Egg Merging]] · [[Cost Tables]]

## Related documents
- [[Development Roadmap]]
- [[M09 - Hatching]]
- [[M12 - Player Bases]]
- [[M13 - Base Upgrades]]
- [[M18 - UI and UX]]
