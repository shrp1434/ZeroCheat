---
title: Combat Index
type: index
category: combat
status: mixed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - index
---

# Combat Index

This folder defines how fighting works in *Fight Animals for Eggs*: the player, the three equipped animals, wild animals and bosses, and the rules that join them in a shared multiplayer world. PvP and base raids reuse these rules and add their own; they live in [[PvP and Raiding Index]].

> [!success] CONFIRMED foundations
> - Real-time hybrid combat: the player and their animals fight together. The player has basic attacks and special moves; special moves may have cooldowns (D-005).
> - Exactly **three** equipped animals (D-006). Team changes only at the player's own base (D-010).
> - Player strength is separate from animal strength (D-007).
> - Animal abilities can be manual or automatic; both kinds exist (D-008).
> - Animals auto-target nearby enemies; players can issue manual target commands (D-009).
> - Wild animals respawn, rarer ones more slowly (D-011). Mini-bosses and world bosses exist (D-012).
> - Defeat penalties are mixed by battle type; exact penalties are **UNDECIDED** ([[Open Questions#Q-014]]).

Everything else in this folder (formulas, timings, AI behaviour, controls) is **PROPOSED** unless marked otherwise. All numbers come from [[Canonical Proposed Values]]; new local values are flagged where they appear.

## Where to start

| If you are… | Read first |
|---|---|
| New to the combat design | [[Combat System Overview]] |
| Balancing numbers | [[Damage, Defence and Health Model]], then [[Player Strength]] |
| Building AI | [[Combat States and State Machine]], [[Animal Combat Behaviour]], [[Wild Animal AI]], [[Boss AI]] |
| Building input and UI | [[Targeting and Command System]], [[Abilities and Cooldowns]], [[Combat Feedback and Readability]] |
| Working on networking | [[Multiplayer Combat Rules]] |
| Working on economy | [[Combat Rewards]], [[Player Defeat and Penalties]] |

## Documents in this folder

| Document | One-line description | Status |
|---|---|---|
| [[Combat System Overview]] | Pillars, participants, the combat loop and the end-to-end combat flow diagram. | mixed |
| [[Player Combat]] | The player's basic combo, three specials, dodge roll, movement and controls. | mixed |
| [[Player Strength]] | The player Strength statistic, its sources and how it scales against animal power. | mixed |
| [[Animal Combat Behaviour]] | Companion follow, formation, engage, leash, low-health retreat, knock-out and recovery. | proposed |
| [[Targeting and Command System]] | Auto-target scoring algorithm, manual commands, and input on PC, mobile and gamepad. | mixed |
| [[Damage, Defence and Health Model]] | Damage and defence formulas, time-to-kill targets per region and worked examples. | proposed |
| [[Abilities and Cooldowns]] | Manual and automatic animal abilities, player specials, cooldown rules and ability UX. | mixed |
| [[Combat States and State Machine]] | State machines for the player, companions and wild animals (Mermaid). | proposed |
| [[Wild Animal AI]] | Temperaments, aggro, threat, chase, leash and reset for wild animals. | proposed |
| [[Boss AI]] | Mini-boss and world boss phases, telegraphs, threat, scaling and anti-cheese rules. | proposed |
| [[Player Defeat and Penalties]] | Separate unapproved rule sets for wild, mini-boss, world boss, PvP and raid defeats. | mixed |
| [[Combat Rewards]] | Cash, XP, index registration and kill credit from combat. | mixed |
| [[Multiplayer Combat Rules]] | Shared-world co-operation, no friendly fire, contribution, server authority. | mixed |
| [[Combat Feedback and Readability]] | Damage numbers, telegraphs, hit feedback, health bars and accessibility. | proposed |

## Open questions owned or touched by combat

- Defeat penalties: **UNDECIDED** ([[Open Questions#Q-014]]).
- Boss rewards: **UNDECIDED** ([[Open Questions#Q-015]]).
- Final animal statistics: **UNDECIDED** ([[Open Questions#Q-003]]).
- Per-animal levelling: **UNDECIDED** ([[Open Questions#Q-021]]); this folder assumes D-042 (no per-animal XP).
- New questions raised here: Q-201 (manual abilities as auto-cast option), Q-202 (wild egg drops), Q-204 (companion knock-out recovery), Q-211 (player damage share), Q-212 (rare-spawn group scaling). They are listed for the lead to add to [[Open Questions]].

## Related documents
- [[PvP and Raiding Index]]
- [[Canonical Proposed Values]]
- [[Team Equipping and Base Lock Rule]]
- [[Boss Design Overview]]
- [[Service - CombatService]]
- [[Service - AnimalAIService]]
- [[Test Cases - Combat]]
- [[M04 - Player Combat]] · [[M05 - Animal AI]] · [[M06 - Animal Combat]]
