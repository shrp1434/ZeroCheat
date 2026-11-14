---
title: M13 - Base Upgrades
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - bases
  - upgrades
milestone: M13
stage: 4
complexity: M
---

# M13 - Base Upgrades

> [!info] PROPOSED milestone
> Stage 4 · Size **M** · Critical path: **yes** · Exit gate: **G4 Base alpha**

## Objective

Make each base section upgradeable on its own (D-022 **CONFIRMED**). Implement the PROPOSED level 1–5 cost curve, module effects (Cash multiplier, Strength and team stat bonuses, trophy bonus), plot expansion stages, and a visible change for every level. Base progression feeds multipliers, Player Strength and the Progression Score.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Upgrade transaction and level rules | Engineering | [[Base Upgrade System]], [[Service - BaseService]] |
| Cost curve and per-module costs from config | Economy | [[Canonical Proposed Values#12. Base modules (PROPOSED — availability Q-007)]], [[Cost Tables]] |
| Module effects wired into Cash, Strength and stat pipelines | Engineering | [[Progression Multipliers]], [[Player Strength]], [[Module - Training Grounds]], [[Module - Multiplier Shrine]], [[Module - Trophy Hall]] |
| Plot expansion stages and slot unlocks | Engineering, Design | [[Base Layout and Plot Expansion]] |
| Level 2–5 module models (and level visuals for defence modules, used in M14) | Art | [[Base Art Direction]] |
| Upgrade animation and sounds | Animation, Audio | [[Animation - Base Upgrades]], [[Sound - Base and Raid Alerts]] |
| Upgrade screen | UI | [[UI - Base Upgrades]] |
| Bottleneck check of base costs against income | Economy | [[Progression Bottleneck Analysis]] |

## Dependencies

- **Upstream:** [[M12 - Player Bases]].
- **Downstream:** [[M14 - Base Defence]].

## Complexity

**M.** Mechanically simple; the art load (several levels per module) and the economic tuning are the real cost.

## Risks

| Risk | Why it matters here |
|---|---|
| R-007 (inflation) | Multiplier Shrine and Trophy Hall bonuses stack with region multipliers. |
| R-008 (late-game wall) | L5 costs are the steepest base sink. |
| R-027 (art scope) | Up to five visual states per module. |

## Acceptance criteria

- [ ] Each module upgrades independently from level 1 to its configured maximum.
- [ ] Costs match the config table; insufficient Cash fails cleanly.
- [ ] Every module effect is applied on the server and visible in the relevant UI (for example Player Strength shown in [[UI - Player Strength Display]]).
- [ ] Every level has a distinct visual state that replicates to visitors.
- [ ] The Progression Score base component updates as module levels change.
- [ ] Bonus stacking matches the formulas in [[Progression Multipliers]] in a worked-example test.

## Testing requirements

- [[Test Cases - Bases and Upgrades]]: costs, effects, level caps, plot expansion, visuals.
- [[Test Cases - Persistence]]: upgrade state survives rejoin.
- [[Test Cases - Exploit Prevention]]: forged upgrade requests and concurrent purchases.

## Open questions

- [[Open Questions#Q-007]]: base module availability at launch.
- [[Open Questions#Q-009]] and [[Open Questions#Q-010]]: storage expansion currency and pricing (separate from module levels).

## Key vault documents
- [[Base Upgrade System]] · [[Base Layout and Plot Expansion]] · [[Cost Tables]]
- [[Progression Multipliers]] · [[UI - Base Upgrades]] · [[Animation - Base Upgrades]]

## Related documents
- [[Development Roadmap]]
- [[M12 - Player Bases]]
- [[M14 - Base Defence]]
- [[Economy Overview]]
- [[Player Bases Index]]
