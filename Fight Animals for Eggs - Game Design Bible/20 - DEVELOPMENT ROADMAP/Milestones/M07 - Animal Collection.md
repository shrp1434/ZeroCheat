---
title: M07 - Animal Collection
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - collection
  - animal-index
milestone: M07
stage: 3
complexity: M
---

# M07 - Animal Collection

> [!info] PROPOSED milestone
> Stage 3 · Size **M** · Critical path: **yes** · Exit gate: **G3 Core loop slice**

## Objective

Replace the debug-granted team used in [[M06 - Animal Combat]] with real ownership. Players own animals, the discovery index records every species they defeat (D-029 **CONFIRMED**: discovered and owned are distinct), and the team of three is equipped only at the player's own base and locked after leaving it (D-010 **CONFIRMED**). Until [[M12 - Player Bases]] exists, a stub base zone stands in as the team change point.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Owned-animal collection with unique instance IDs | Engineering | [[Animal Collection System]], [[Schema - Animal Collection]] |
| Equipped team record and base lock enforcement on the server | Engineering | [[Team Equipping and Base Lock Rule]], [[Schema - Equipped Team]], [[Service - TeamService]] |
| Discovery index: defeat registers a species; owned flag separate | Engineering | [[Animal Index Feature Specification]], [[Schema - Discovery Index]], [[Service - IndexService]] |
| Collection storage limit with a configurable cap (**UNDECIDED**, working assumption 100) | Engineering, Design | [[Animal Collection System]] |
| Inventory, team selection and index screens (functional) | UI | [[UI - Animal Inventory]], [[UI - Team Selection]], [[UI - Animal Index Screen]] |
| Index rewards hook into the Progression Score (3 points per species, PROPOSED) | Engineering | [[Progression Score Specification]] |
| Variant data field on owned animals, inert until variants are designed | Engineering | [[Animal Variants]] |

## Dependencies

- **Upstream:** [[M06 - Animal Combat]].
- **Downstream:** [[M08 - Egg Rolling]], [[M12 - Player Bases]].

## Complexity

**M.** Mostly data and UI, but every later transaction (hatch, ascension, merge, theft) mutates this data, so its schema and IDs must be right first time.

## Risks

| Risk | Why it matters here |
|---|---|
| R-003 (team lock friction) | First playable version of the base lock. |
| R-017, R-025 (transfers and duplication) | Unique instance IDs make later audits possible. |
| R-010 (storage frustration) | Collection cap is **UNDECIDED**. |

## Acceptance criteria

- [ ] Defeating a species for the first time registers it as discovered; owning it is tracked separately.
- [ ] Team changes succeed only inside the player's own base zone; outside it the server rejects every change request, including forged ones.
- [ ] The team is exactly three animals; empty slots are allowed only if [[Team Equipping and Base Lock Rule]] says so.
- [ ] The collection cap is read from config; reaching it is handled as the owning document specifies.
- [ ] Each owned animal has a unique ID that survives save, load and migration.
- [ ] Progression Score updates when a new species is discovered.

## Testing requirements

- [[Test Cases - Inventory and Storage]]: collection limits, team equipping, index states.
- [[Test Cases - Persistence]]: collection and team survive rejoin and server shutdown.
- [[Test Cases - Exploit Prevention]]: team change outside base, forged instance IDs.

## Open questions

- [[Open Questions#Q-022]]: owned-animal storage capacity (working assumption 100).
- [[Open Questions#Q-002]]: final catalogue.
- [[Open Questions#Q-006]] and [[Open Questions#Q-024]]: variant acquisition and stat effect; the data field is reserved now.

## Key vault documents
- [[Animal Collection System]] · [[Animal Index Feature Specification]] · [[Team Equipping and Base Lock Rule]]
- [[Schema - Animal Collection]] · [[Schema - Equipped Team]] · [[Schema - Discovery Index]]
- [[Service - TeamService]] · [[Service - IndexService]] · [[Animal Index]]

## Related documents
- [[Development Roadmap]]
- [[M06 - Animal Combat]]
- [[M08 - Egg Rolling]]
- [[M12 - Player Bases]]
- [[Core Gameplay Loop]]
