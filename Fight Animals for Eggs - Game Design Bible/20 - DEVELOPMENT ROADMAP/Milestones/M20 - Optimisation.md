---
title: M20 - Optimisation
type: milestone
category: roadmap
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - performance
  - optimisation
milestone: M20
stage: 7
complexity: L
---

# M20 - Optimisation

> [!info] PROPOSED milestone
> Stage 7 · Size **L** · Critical path: **yes** · Exit gate: **G6 Beta ready**

## Objective

Reach the PROPOSED performance targets with full content: 60 FPS on a mid-range PC and a 30 FPS minimum on a mid-range phone, within the server budgets for animals and players ([[Canonical Proposed Values#15. Server and performance targets (PROPOSED)]]). Optimisation is guided by measurements from [[M19 - Multiplayer Testing]], not by guesswork.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Server profile and fixes: AI LOD, spawn budget, combat pipeline cost | Engineering | [[Animal Scalability and Performance Budgets]], [[Service - AnimalAIService]] |
| Client profile and fixes: draw calls, animation count, VFX particle budgets | Engineering, Technical Art | [[Performance Guidelines]], [[VFX Bible]] |
| StreamingEnabled tuning per region and base area | Engineering | [[Performance Guidelines]] |
| Mesh, texture and LOD budgets enforced on every asset | Art | [[Animal Modelling Principles]], [[Material and Texture Direction]] |
| Network bandwidth reduction (UnreliableRemoteEvent for cosmetic streams, batching) | Engineering | [[Replication Strategy]], [[Remote Communication Contract]] |
| Memory budget per device class | Engineering | [[Performance Guidelines]] |
| Audio voice limits and streaming | Audio | [[Audio Mixing and Priority]] |
| Performance regression benchmarks for every future build | QA, Engineering | [[Test Cases - Mobile Performance]] |

## Dependencies

- **Upstream:** [[M16 - World Design]] (full content), [[M19 - Multiplayer Testing]] (measurements).
- **Downstream:** [[M21 - Beta Testing]].

## Complexity

**L.** Cross-cutting work across every system, art asset and device class.

## Risks

| Risk | Why it matters here |
|---|---|
| R-018 (server cost) | Main mitigation milestone. |
| R-019 (mobile) | Main mitigation milestone. |
| R-002 (readability) | Cutting VFX must not hurt combat readability. |

## Acceptance criteria

- [ ] The reference mid-range phone holds the PROPOSED 30 FPS minimum in the busiest tested scenario (world boss with a full server).
- [ ] The reference mid-range PC holds the PROPOSED 60 FPS in the same scenario.
- [ ] Server frame time stays within budget in a full-server soak with the PROPOSED animal counts.
- [ ] Client memory stays inside the device budget while traversing every region.
- [ ] Benchmark scenes are automated and run on every release candidate.
- [ ] No optimisation changes gameplay outcomes (damage, odds, rewards); regression tests confirm this.

## Testing requirements

- [[Test Cases - Mobile Performance]] (all).
- [[Test Cases - Multiplayer]]: full-server performance.
- [[Test Cases - Combat]] and [[Test Cases - Egg Rolls and Hatching]]: outcome regression after optimisation.

## Open questions

- [[Open Questions#Q-008]]: physical display of owned animals in pens (largest optional performance cost).
- [[Open Questions#Q-031]]: server size.
- **UNDECIDED** (Q-1110): platform priority, including whether console is a launch target.

## Key vault documents
- [[Performance Guidelines]] · [[Animal Scalability and Performance Budgets]] · [[Replication Strategy]]
- [[Animal Modelling Principles]] · [[VFX Bible]] · [[Audio Mixing and Priority]]

## Related documents
- [[Development Roadmap]]
- [[M16 - World Design]]
- [[M19 - Multiplayer Testing]]
- [[M21 - Beta Testing]]
- [[Roblox Platform References]]
