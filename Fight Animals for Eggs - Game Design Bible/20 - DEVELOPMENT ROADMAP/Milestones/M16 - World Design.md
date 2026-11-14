---
title: M16 - World Design
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - world
  - regions
  - art-production
milestone: M16
stage: 6
complexity: XL
---

# M16 - World Design

> [!info] PROPOSED milestone
> Stage 6, running in parallel from stage 2 · Size **XL** · Critical path: no (13 units of schedule slack) but **throughput-critical** · Exit gate: **G5 Feature complete**

## Objective

Build the one large shared world (D-025 **CONFIRMED**): the hub and every launch region, with spawn tables, hazards, unlock flow, ambience and the full launch roster placed in its home regions. The PROPOSED layout is the hub plus eight regions (D-035), but the world layout is **UNDECIDED** ([[Open Questions#Q-001]]). M16 is also the container for producing the remaining roster art, since every animal must be placed in a region.

> [!info] PROPOSED — how this milestone runs
> M16 starts with greybox work as soon as [[M03 - Player Movement]] defines traversal metrics, and continues alongside stages 2–5. It is tracked by **throughput** (regions greyboxed, regions dressed, animals finished) at every gate, not only at its own end.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| World map, adjacency and scale | Design | [[World Overview and Map]] |
| Hub with egg shrine and base portals | Design, Art | [[Hub - Hatchling Haven]] |
| Launch regions: greybox, then dressed | Design, Art | [[Region - Whisperwood Forest]], [[Region - Sunscorch Savanna]], [[Region - Emerald Canopy]], [[Region - Coral Coast]], [[Region - Frostfang Tundra]], [[Region - Skyreach Peaks]], [[Region - Emberheart Caldera]], [[Region - Starfall Sanctuary]] |
| Region unlock gates and progression | Design, Engineering | [[Region Unlock Progression]] |
| Spawn tables and points per region | Design | [[Wild Animal Spawning and Respawn]] |
| Environmental hazards | Design, Engineering | [[Environmental Hazards]] |
| Environment kits (ENV-###) and lighting per region | Art | [[Environment Art Direction]], [[Lighting Direction]], [[Asset Register]] |
| Remaining roster models, rigs and animation sets (ANM-001 to ANM-060) | Art, Animation | [[Animal Index]], [[Animal Modelling Principles]], [[Animal Rig Standards]] |
| Ambient VFX and region ambience | VFX, Audio | [[VFX - Environment Ambient Effects]], [[Sound - Ambient World]], [[Music Direction]] |
| Streaming configuration for the world | Engineering | [[Performance Guidelines]] |

## Dependencies

- **Upstream:** [[M01 - Pre-production]] (art direction, region proposal), [[M03 - Player Movement]] (traversal metrics). Spawn tables need the M05 spawn service.
- **Downstream:** [[M17 - Boss Encounters]], [[M20 - Optimisation]].

## Complexity

**XL.** The largest content load in the project: up to eight regions, 60 animals and their animation sets, kits, lighting, ambience and music.

## Risks

| Risk | Why it matters here |
|---|---|
| R-027 (art scope) | Roster and region production rate decides whether beta has final art. |
| R-006 (too many regions) | Each region needs a distinct purpose. |
| R-019 (mobile memory) | Region kits and streaming. |
| R-021 (pathfinding) | Terrain must support animal navigation. |

## Acceptance criteria

- [ ] Every launch region is reachable and gated according to [[Region Unlock Progression]].
- [ ] Each region has its spawn table, spawn points, hazards and mini-boss arena placed.
- [ ] Wild encounter rarity is driven only by spawn tables and respawn rules, never by player luck (D-017).
- [ ] All launch animals exist in-engine with locomotion, attack, hit, ability and defeat animations, and pass the art review in [[Animal Modelling Principles]].
- [ ] No horror styling or meme animals anywhere (D-026 **CONFIRMED**).
- [ ] Streaming keeps memory within the device budget while crossing every region boundary.
- [ ] Region ambience and music transition cleanly at boundaries.

## Testing requirements

- [[Test Cases - Animal AI]]: spawning and navigation in each region.
- [[Test Cases - Mobile Performance]]: memory and frame rate per region and at boundaries.
- [[Test Cases - Multiplayer]]: many players spread across regions in one server.

## Open questions

- [[Open Questions#Q-001]]: exact world layout.
- [[Open Questions#Q-002]]: final animal catalogue.
- [[Open Questions#Q-027]]: ancient lineage theme for Mythical and Secret tiers.
- [[Open Questions#Q-028]]: aquatic movement on land.
- **UNDECIDED** (Q-1103): whether any launch region can move to a post-launch update under the cut line.

## Key vault documents
- [[World Overview and Map]] · [[Region Unlock Progression]] · [[Wild Animal Spawning and Respawn]]
- [[Environment Art Direction]] · [[Lighting Direction]] · [[Animal Index]] · [[Asset Register]]

## Related documents
- [[Development Roadmap]]
- [[World Design Index]]
- [[M17 - Boss Encounters]]
- [[M20 - Optimisation]]
- [[Risk Register]]
