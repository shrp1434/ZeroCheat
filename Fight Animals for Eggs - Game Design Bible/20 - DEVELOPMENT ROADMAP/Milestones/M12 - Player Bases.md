---
title: M12 - Player Bases
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
milestone: M12
stage: 4
complexity: L
---

# M12 - Player Bases

> [!info] PROPOSED milestone
> Stage 4 · Size **L** · Critical path: **yes** · Exit gate: **G4 Base alpha**

## Objective

Give every player a personal modular base (D-022 **CONFIRMED**) inside the shared world. The base is where the team is changed (D-010), where base-stored eggs live (base storage 50, **CONFIRMED**), and where modules are placed. This milestone builds plots, module slots and construction (level 1). Upgrade levels follow in [[M13 - Base Upgrades]].

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Plot allocation and release per server, base loading on join | Engineering | [[Player Base System]], [[Service - BaseService]] |
| Base layout, module slots and plot expansion stages | Design, Engineering | [[Base Layout and Plot Expansion]] |
| Base data schema | Engineering | [[Schema - Base Data]] |
| Module construction for launch modules (list **UNDECIDED**) | Engineering | [[Module - Animal Pens]], [[Module - Egg Vault]], [[Module - Training Grounds]], [[Module - Multiplier Shrine]], [[Module - Trophy Hall]] |
| Team change point replaces the M07 stub | Engineering | [[Team Equipping and Base Lock Rule]] |
| Base storage tied to the Egg Vault module | Engineering | [[Egg Storage]], [[Module - Egg Vault]] |
| Travel between hub, regions and base | Design, Engineering | [[Hub - Hatchling Haven]] |
| Base management screen | UI | [[UI - Base Management]] |
| Level-1 module models and plot kit | Art | [[Base Art Direction]] |
| Base ambience | Audio | [[Sound - Base and Raid Alerts]] |

## Dependencies

- **Upstream:** [[M07 - Animal Collection]].
- **Downstream:** [[M11 - Egg Merging]], [[M13 - Base Upgrades]].

## Complexity

**L.** Per-player instanced space in a shared server, persistence of placed modules, streaming of up to the server's player count in bases, and the art load of every module.

## Risks

| Risk | Why it matters here |
|---|---|
| R-018 (server cost) | Up to 16 bases (working assumption) loaded per server. |
| R-019 (mobile memory) | Bases near each other must stream. |
| R-003 (team lock) | Base travel time sets the cost of the lock. |
| R-016 (DataStore budgets) | Base data adds write volume. |

## Acceptance criteria

- [ ] Every joining player receives a plot and their saved base loads within the target in [[Performance Guidelines]].
- [ ] Leaving releases the plot without leaving orphaned instances.
- [ ] Modules can be built in valid slots only; construction cost is debited atomically.
- [ ] Team change works only inside the player's own base; another player's base does not count.
- [ ] Base storage holds the **CONFIRMED** 50 eggs at start; backpack 10 is unchanged.
- [ ] Base progression contributes to the Progression Score as specified in [[Progression Score Specification]].

## Testing requirements

- [[Test Cases - Bases and Upgrades]]: plot allocation, construction, slot rules, team change point.
- [[Test Cases - Persistence]]: base save, load and migration.
- [[Test Cases - Inventory and Storage]]: base storage capacity.
- [[Test Cases - Mobile Performance]]: several bases in view.

## Open questions

- [[Open Questions#Q-007]]: which modules ship at launch. Blocks beta.
- [[Open Questions#Q-008]]: whether owned animals are physically displayed in pens. Blocks pens.
- [[Open Questions#Q-009]]: storage expansion currency (Egg Vault expansion is separate from module level).

## Key vault documents
- [[Player Base System]] · [[Base Layout and Plot Expansion]] · [[Base Upgrade System]]
- [[Service - BaseService]] · [[Schema - Base Data]] · [[UI - Base Management]]
- [[Shared World and Player Sessions]] · [[Base Art Direction]]

## Related documents
- [[Development Roadmap]]
- [[M07 - Animal Collection]]
- [[M11 - Egg Merging]]
- [[M13 - Base Upgrades]]
- [[Player Bases Index]]
