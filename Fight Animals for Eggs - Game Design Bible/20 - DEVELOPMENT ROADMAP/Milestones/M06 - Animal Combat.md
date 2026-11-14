---
title: M06 - Animal Combat
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - combat
  - abilities
milestone: M06
stage: 2
complexity: L
---

# M06 - Animal Combat

> [!info] PROPOSED milestone
> Stage 2 · Size **L** · Critical path: **yes** · Exit gate: **G2 Combat slice**

## Objective

Complete the hybrid combat slice: the player fights alongside exactly **three** equipped animals (D-006 **CONFIRMED**). Animals auto-target nearby enemies and accept manual target commands (D-009). Abilities exist in both manual and automatic forms (D-008). Defeating wild animals pays Cash and XP (D-014) with shared kill credit (D-040, **PROPOSED**). At the end of M06 the game is a small but complete action game.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Team combat behaviour: auto-target, role behaviour, manual command override | Engineering, Design | [[Animal Combat Behaviour]], [[Targeting and Command System]] |
| Ability framework for manual and automatic abilities, with the PROPOSED global cooldown | Engineering | [[Abilities and Cooldowns]], [[Animal Abilities Catalogue]] |
| Role tuning for the seven roles | Design | [[Animal Roles]], [[Animal Stat Budget Model]] |
| Slice roster stats from the database | Design | [[Animal Statistics Database]] |
| Rewards: Cash and XP per defeat, region multiplier, kill credit at 10% contribution | Engineering, Economy | [[Combat Rewards]], [[Wild Animal Cash Rewards]], [[Multiplayer Combat Rules]] |
| Player XP and levelling | Engineering | [[Player Progression and Levelling]], [[Service - ProgressionService]] |
| Animal attack, hit-reaction, ability, defeat and victory animations for slice animals | Animation | [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]] |
| Ability VFX and sounds | VFX, Audio | [[VFX - Combat Effects]], [[Sound - Abilities]] |
| Team display and command UI | UI | [[UI - Animal Team Display]], [[Targeting and Command System]] |
| Readability pass | Design, Art | [[Combat Feedback and Readability]] |

## Dependencies

- **Upstream:** [[M04 - Player Combat]], [[M05 - Animal AI]].
- **Downstream:** [[M07 - Animal Collection]], [[M17 - Boss Encounters]].

## Complexity

**L.** Combines the two largest stage-2 systems and introduces the first economy flow.

## Risks

| Risk | Why it matters here |
|---|---|
| R-002 (readability) | The first time four friendly combatants share the screen. |
| R-001 (loop fun) | G2 playtest is the first real test of the pillar. |
| R-007 (cash inflation) | Shared kill credit and multipliers are first measured. |
| R-009 (multi-account farming) | Kill credit rules must resist alt-account farming. |

## Acceptance criteria

- [ ] A team of exactly three animals fights with the player; a fourth cannot be equipped.
- [ ] Animals auto-target the nearest valid enemy and switch to a commanded target on order.
- [ ] Manual abilities fire on input with cooldowns; automatic abilities fire on their conditions.
- [ ] Each role's Power Index in the slice stays inside the band defined in [[Animal Stat Budget Model]].
- [ ] Two players damaging the same wild animal both receive the full reward when each passes the contribution threshold; a player below it receives nothing.
- [ ] Cash and XP awarded match [[Canonical Proposed Values#6. Wild rewards and respawn (PROPOSED)]] for the region multiplier.
- [ ] G2 playtest: at least most testers can say which animals are theirs and what they are attacking (R-002 trigger not fired).

## Testing requirements

- [[Test Cases - Combat]]: team combat, abilities, targeting, rewards.
- [[Test Cases - Animal AI]]: combat states for companions and wild animals.
- [[Test Cases - Multiplayer]]: kill credit, shared targets.
- [[Test Cases - Exploit Prevention]]: forged ability use, reward farming.

## Open questions

- [[Open Questions#Q-003]]: final animal statistics.
- [[Open Questions#Q-014]]: defeat penalties in wild combat (configurable).
- [[Open Questions#Q-021]]: per-animal levelling (working assumption: none, D-042).

## Key vault documents
- [[Combat System Overview]] · [[Animal Combat Behaviour]] · [[Targeting and Command System]]
- [[Abilities and Cooldowns]] · [[Animal Abilities Catalogue]] · [[Animal Roles]]
- [[Combat Rewards]] · [[Multiplayer Combat Rules]] · [[Service - CombatService]]

## Related documents
- [[Development Roadmap]]
- [[M04 - Player Combat]]
- [[M05 - Animal AI]]
- [[M07 - Animal Collection]]
- [[M17 - Boss Encounters]]
