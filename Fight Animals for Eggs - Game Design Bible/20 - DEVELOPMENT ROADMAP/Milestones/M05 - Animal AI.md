---
title: M05 - Animal AI
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - ai
  - spawning
milestone: M05
stage: 2
complexity: L
---

# M05 - Animal AI

> [!info] PROPOSED milestone
> Stage 2 · Size **L** · Critical path: **yes** (co-critical with M04) · Exit gate: **G2 Combat slice**

## Objective

Build the shared AI foundation for wild animals and companion animals: a server-side state machine, spawning and respawn with rarity-scaled timers (D-011 **CONFIRMED**), leash and reset, companion following, and AI level-of-detail so the PROPOSED server budgets hold. Combat behaviour on top of this foundation is finished in [[M06 - Animal Combat]].

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| AI state machine (idle, wander, alert, chase, attack, leash, reset, defeated) | Engineering | [[Implementation - Animal AI State Machine]], [[Wild Animal AI]] |
| Companion follow, formation and catch-up behaviour | Engineering | [[Animal Combat Behaviour]] |
| Spawn service: spawn points, rarity respawn timers, rare-spawn windows and announcements | Engineering, Design | [[Service - SpawnService]], [[Wild Animal Spawning and Respawn]] |
| AI service with LOD tiers (full AI near players, simplified far away) | Engineering | [[Service - AnimalAIService]], [[Animal Scalability and Performance Budgets]] |
| Network ownership policy for animals | Engineering | [[Network Ownership]] |
| Pathfinding and steering approach | Engineering | [[Implementation - Animal AI State Machine]] |
| Four body-plan locomotion sets (quadruped, biped, bird, air-swim aquatic) | Animation | [[Animal Rig Standards]], [[Animation - Animal Locomotion]] |
| First 6–10 slice animals modelled and rigged | Art | [[Animal Modelling Principles]], [[Asset Register]] |
| Ambient vocalisation hooks | Audio | [[Sound - Animal Vocalisations]] |

## Dependencies

- **Upstream:** [[M02 - Core Project Setup]], [[M03 - Player Movement]].
- **Downstream:** [[M06 - Animal Combat]], [[M14 - Base Defence]] (guard AI, through M06 and the base chain), [[M16 - World Design]] (spawn tables per region).

## Complexity

**L.** Many simultaneous agents on the server, four body plans, and LOD that must not change gameplay outcomes.

## Risks

| Risk | Why it matters here |
|---|---|
| R-018 (server simulation cost) | The PROPOSED budget of 180 simulated and 60 full-AI animals is first proven here. |
| R-021 (pathfinding cost) | Navigation choices constrain level design in M16. |
| R-027 (art scope) | Body-plan rig sharing is decided here and drives roster cost. |

## Acceptance criteria

- [ ] Wild animals wander, notice players, chase, leash at the PROPOSED range and reset to full HP.
- [ ] Respawn times follow rarity from config; rarer animals respawn more slowly (D-011).
- [ ] Rare-spawn windows roll and announce on the server as configured.
- [ ] Spawn rarity is **not** affected by any player's progression luck (D-017 **CONFIRMED**). A test confirms the spawn service never reads luck values.
- [ ] Companions follow their owner, catch up after teleports and never block the player.
- [ ] A soak with the PROPOSED maximum animal counts keeps the server within its frame budget.
- [ ] LOD transitions are invisible to a player standing at the boundary.

## Testing requirements

- [[Test Cases - Animal AI]]: state transitions, leash, respawn timers, rare-spawn windows, companion following.
- [[Test Cases - Mobile Performance]]: client cost of animated animals near the player.
- [[Test Cases - Multiplayer]]: AI replication with several players.

## Open questions

- [[Open Questions#Q-028]]: aquatic movement on land (D-043 proposes air-swimming). Blocks the aquatic locomotion set.
- [[Open Questions#Q-031]]: server size sets the companion count (3 per player).
- [[Open Questions#Q-008]]: physical display of owned animals in pens would add AI or static instances; working assumption needed for budget planning.

## Key vault documents
- [[Wild Animal AI]] · [[Animal Combat Behaviour]] · [[Wild Animal Spawning and Respawn]]
- [[Service - AnimalAIService]] · [[Service - SpawnService]] · [[Implementation - Animal AI State Machine]]
- [[Animal Scalability and Performance Budgets]] · [[Network Ownership]] · [[Animal Rig Standards]]

## Related documents
- [[Development Roadmap]]
- [[M03 - Player Movement]]
- [[M06 - Animal Combat]]
- [[M20 - Optimisation]]
- [[Risk Register]]
