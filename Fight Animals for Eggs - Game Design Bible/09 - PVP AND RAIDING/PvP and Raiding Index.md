---
title: PvP and Raiding Index
type: index
category: pvp-and-raiding
status: mixed
priority: P0
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - pvp
  - raids
  - index
---

# PvP and Raiding Index

This folder covers the two optional player-versus-player modes: **PvP combat** between players and their teams, and **base raiding**, where one player attacks another's base to steal stored eggs and knocked-out defending animals. Both reuse the combat rules in [[Combat Index]].

> [!success] CONFIRMED
> - PvP is optional; players choose whether to take part (D-023).
> - Raids are optional. Eggs in base storage can be stolen. A defending animal can be stolen only after it has been knocked out; undefeated defenders cannot be stolen. **Maximum three animals stolen per successful raid.** Offline bases cannot be raided. Bases are protected by shields and physical defences (D-024).
> - Backpack eggs can never be stolen (D-021).

> [!warning] UNDECIDED
> - PvP activation method ([[Open Questions#Q-011]])
> - Raid duration ([[Open Questions#Q-012]]): configurable `RaidDurationSeconds`, no approved value
> - Egg theft limit per raid ([[Open Questions#Q-013]]): configurable `MaxEggsStolenPerRaid`, no approved default
> - Defeat penalties ([[Open Questions#Q-014]])
> - What a stolen animal keeps ([[Open Questions#Q-025]])
> - Raid matchmaking ([[Open Questions#Q-029]])
> - Shield acquisition ([[Open Questions#Q-030]])
> - Which animals defend a base ([[Open Questions#Q-033]]) and whether the defender's team joins ([[Open Questions#Q-035]])
> - New questions raised here: Q-203, Q-205 to Q-210 (listed for the lead to add to [[Open Questions]])

## Reading order
1. [[PvP System]], then [[PvP Activation Options]].
2. [[Base Raiding System]] (the overview), then [[Raid Lifecycle and States]].
3. The rules: [[Raid Eligibility and Offline Protection]], [[Shield Mechanics]], [[Egg Theft Rules]], [[Animal Theft Rules]].
4. The robustness layer: [[Raid Disconnection Handling]], [[Raid Anti-Exploit Validation]].
5. Outcomes: [[Raid Rewards and Defender Compensation]].

## Documents in this folder

| Document | One-line description | Status |
|---|---|---|
| [[PvP System]] | Rules shared by every PvP format: damage scaling, encounter design, rewards and safeguards. | mixed |
| [[PvP Activation Options]] | Comparison of opt-in toggle, arena zones, duel requests and PvP regions, with a labelled recommendation (Q-011). | undecided |
| [[Base Raiding System]] | Overview of raids: roles, objective, defences, theft, what "successful" means, and the parameter list. | mixed |
| [[Raid Lifecycle and States]] | The raid state machine and the end-to-end lifecycle sequence diagram. | mixed |
| [[Raid Eligibility and Offline Protection]] | Who can raid whom, the precise definition of "online", and mid-raid departure handling. | mixed |
| [[Shield Mechanics]] | Shield types, the rules for applying and breaking them, and options for acquisition (Q-030). | mixed |
| [[Egg Theft Rules]] | Which eggs can be stolen, how theft is secured, and the configurable limit (Q-013). | mixed |
| [[Animal Theft Rules]] | Knock-out-first capture, the three-animal cap and the definition of a successful raid. | mixed |
| [[Raid Disconnection Handling]] | What happens when the attacker, the defender, both or the server drop. | proposed |
| [[Raid Anti-Exploit Validation]] | Server checks for every theft and claim, and collusion and alt-account defences. | proposed |
| [[Raid Rewards and Defender Compensation]] | Attacker gains, defender rewards, post-raid protection and compensation options. | mixed |

## Raid parameters at a glance

| Parameter | Value | Status |
|---|---|---|
| `MaxAnimalsStolenPerRaid` | 3 | **CONFIRMED** (D-024) |
| `RaidDurationSeconds` | None approved | **UNDECIDED** ([[Open Questions#Q-012]]) |
| `MaxEggsStolenPerRaid` | None approved; no default | **UNDECIDED** ([[Open Questions#Q-013]]) |
| All other raid timers and caps | See [[Base Raiding System#Raid parameters]] | **PROPOSED** |

## Related documents
- [[Combat Index]]
- [[Player Bases Index]]
- [[Base Defence Overview]]
- [[Animal Guards and Base Defence AI]]
- [[Egg Storage]]
- [[Service - RaidService]]
- [[Service - PvPService]]
- [[UI - Raid Interface]]
- [[UI - PvP Interface]]
- [[Test Cases - Raiding]] · [[Test Cases - PvP]]
- [[M15 - Base Raids]]
