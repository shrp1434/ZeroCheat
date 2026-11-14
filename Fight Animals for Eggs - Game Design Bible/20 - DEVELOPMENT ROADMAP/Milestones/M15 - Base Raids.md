---
title: M15 - Base Raids
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - raids
  - pvp
  - security
milestone: M15
stage: 5
complexity: XL
---

# M15 - Base Raids

> [!info] PROPOSED milestone
> Stage 5 · Size **XL** · Critical path: **yes** (largest node) · Exit gate: **G5 Feature complete** (with M16, M17)

## Objective

Ship optional PvP and optional base raiding (D-023, D-024 **CONFIRMED**) with every confirmed protection enforced on the server:

> [!success] CONFIRMED rules this milestone must enforce
> - PvP and raiding are optional.
> - Eggs stored in the base can be stolen; **backpack eggs can never be stolen**.
> - A defending animal can be stolen only after it has been knocked out; **undefeated defenders cannot be stolen**.
> - **Maximum three animals stolen per successful raid.**
> - **Offline bases cannot be raided.**
> - Bases are protected by shields and physical defences.

> [!warning] UNDECIDED — build configurable, decide nothing
> Raid duration ([[Open Questions#Q-012]]) and the egg theft limit ([[Open Questions#Q-013]]) are **UNDECIDED**. They ship as config values with no approved default. The PvP activation method is **UNDECIDED** ([[Open Questions#Q-011]]); all documented options are built behind a switch or the chosen one is built after the decision.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| PvP opt-in framework per the activation options | Engineering, Design | [[PvP System]], [[PvP Activation Options]], [[Service - PvPService]] |
| Raid lifecycle state machine | Engineering | [[Raid Lifecycle and States]], [[Implementation - Raid Session Controller]], [[Service - RaidService]] |
| Raid eligibility: online check, shields, matchmaking bands (options) | Engineering, Design | [[Raid Eligibility and Offline Protection]] |
| Egg theft with configurable limit | Engineering | [[Egg Theft Rules]] |
| Animal theft with knock-out check and three-animal cap | Engineering | [[Animal Theft Rules]] |
| Cross-player transfer transaction with reconciliation | Engineering | [[Data Consistency and Transactions]] |
| Disconnect handling for attacker and defender | Engineering | [[Raid Disconnection Handling]], [[Disconnect Handling]] |
| Anti-exploit validation for every raid action | Security | [[Raid Anti-Exploit Validation]] |
| Rewards and defender compensation (values PROPOSED) | Design, Economy | [[Raid Rewards and Defender Compensation]] |
| Raid and PvP interfaces | UI | [[UI - Raid Interface]], [[UI - PvP Interface]] |
| Raid interaction animations and alerts | Animation, Audio | [[Animation - Raid Interactions]], [[Sound - Base and Raid Alerts]] |

## Dependencies

- **Upstream:** [[M14 - Base Defence]], [[M09 - Hatching]] (base-stored eggs).
- **Downstream:** [[M18 - UI and UX]], [[M19 - Multiplayer Testing]].

## Complexity

**XL.** Two players' persistent data change in one event, under real-time combat, with either side able to disconnect at any moment. It is also the most exploit-attractive feature.

> [!info] PROPOSED scheduling note
> Start a raid-transaction spike while [[M14 - Base Defence]] is still in progress, so the riskiest part of the critical path is de-risked early.

## Risks

| Risk | Why it matters here |
|---|---|
| R-024 (raid exploits) | Highest-scoring risk tied to a single feature. |
| R-017 (cross-player transfer) | Duplication or loss of stolen items. |
| R-004 (raids feel punishing) | Defender retention. |
| R-009 (multi-account farming) | Feeding raids between alt accounts. |
| R-016 (DataStore budgets) | Raid writes on two profiles at once. |

## Acceptance criteria

- [ ] A player who has not opted in cannot be attacked in PvP and cannot have their base raided, according to the activation rule in force.
- [ ] A raid cannot start against an offline player's base, or against an active shield.
- [ ] No test can steal a backpack egg.
- [ ] No test can steal a defender that was not knocked out during that raid.
- [ ] No successful raid transfers more than three animals.
- [ ] Egg theft stops at the configured limit; changing the config changes the behaviour without code changes.
- [ ] Raid duration is read from config; no value is presented to players as final until [[Open Questions#Q-012]] is decided.
- [ ] Every disconnect case in [[Raid Disconnection Handling]] ends with both profiles consistent: each stolen item exists exactly once.
- [ ] Every raid action is validated on the server and logged with a raid ID.

## Testing requirements

- [[Test Cases - Raiding]]: every **CONFIRMED** rule above, plus eligibility, shields and rewards.
- [[Test Cases - PvP]]: opt-in, damage between players, leaving PvP.
- [[Test Cases - Exploit Prevention]]: forged theft, teleporting into bases, raid-and-leave abuse.
- [[Test Cases - Multiplayer]]: raids with spectators and other players nearby.
- [[Test Cases - Persistence]]: transfer reconciliation after crashes.

## Open questions

- [[Open Questions#Q-011]]: PvP activation method.
- [[Open Questions#Q-012]]: raid duration.
- [[Open Questions#Q-013]]: egg theft limit.
- [[Open Questions#Q-014]]: raid defeat penalties.
- [[Open Questions#Q-025]]: what a stolen animal keeps.
- [[Open Questions#Q-029]]: raid matchmaking.
- [[Open Questions#Q-030]]: shield acquisition.

## Key vault documents
- [[Base Raiding System]] · [[Raid Lifecycle and States]] · [[Raid Eligibility and Offline Protection]]
- [[Egg Theft Rules]] · [[Animal Theft Rules]] · [[Raid Disconnection Handling]] · [[Raid Anti-Exploit Validation]]
- [[PvP System]] · [[PvP Activation Options]] · [[Implementation - Raid Session Controller]] · [[Threat Model]]

## Related documents
- [[Development Roadmap]]
- [[M14 - Base Defence]]
- [[M19 - Multiplayer Testing]]
- [[PvP and Raiding Index]]
- [[Risk Register]]
