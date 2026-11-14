---
title: M14 - Base Defence
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
  - defence
  - shields
milestone: M14
stage: 4
complexity: L
---

# M14 - Base Defence

> [!info] PROPOSED milestone
> Stage 4 · Size **L** · Critical path: **yes** · Exit gate: **G4 Base alpha**

## Objective

Build the protections that make optional raids fair: physical defences (barricades, traps, turrets), shields (D-024 **CONFIRMED**: bases are protected by shields and physical defences) and animal guard AI. Raid sessions themselves are built in [[M15 - Base Raids]]; M14 delivers everything a raid will be fought against, testable in a sandbox raid with internal attackers.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Defence Station structures and their upgrade effects | Engineering, Design | [[Module - Defence Station]], [[Base Defence Overview]] |
| Shield Generator: shield states, duration and recharge (values PROPOSED) | Engineering | [[Module - Shield Generator]], [[Shield Mechanics]] |
| Guard AI on the M05 state machine | Engineering | [[Animal Guards and Base Defence AI]] |
| Defender selection with a configurable rule (**UNDECIDED**) | Engineering, Design | [[Animal Guards and Base Defence AI]] |
| Knock-out state for defending animals (needed by theft rules) | Engineering | [[Animal Theft Rules]] |
| Shield activation animation and VFX | Animation, VFX | [[Animation - Shield Activation]] |
| Defence and alert sounds | Audio | [[Sound - Base and Raid Alerts]] |
| Sandbox raid scene for internal testing | QA, Design | [[Test Cases - Raiding]] |

## Dependencies

- **Upstream:** [[M13 - Base Upgrades]] (defence modules upgrade), [[M05 - Animal AI]] and [[M06 - Animal Combat]] (guard behaviour, through the chain).
- **Downstream:** [[M15 - Base Raids]].

## Complexity

**L.** Guard AI inside a confined space, turret targeting, shields that interact with raid eligibility, and many states that the theft rules depend on.

## Risks

| Risk | Why it matters here |
|---|---|
| R-004 (raids feel punishing) | Defences are the defender's agency. |
| R-024 (raid exploits) | Knock-out state is what decides whether an animal can be stolen. |
| R-018 (server cost) | Guards and turrets add AI agents. |

## Acceptance criteria

- [ ] Defence structures work at each upgrade level as configured.
- [ ] An active shield blocks raid entry; shield state is server-authoritative and visible to attackers and defenders.
- [ ] Guards defend, can be knocked out, and the knocked-out state is recorded on the server per raid.
- [ ] An undefeated (not knocked out) defender is flagged as not stealable (D-024 **CONFIRMED**).
- [ ] Defender selection uses a config switch so that any outcome of [[Open Questions#Q-033]] can be enabled without code changes.
- [ ] Sandbox raids run with internal attackers and produce logs that QA can replay.

## Testing requirements

- [[Test Cases - Bases and Upgrades]]: defence modules and shield levels.
- [[Test Cases - Raiding]]: shields, knock-out state, defender eligibility (sandbox).
- [[Test Cases - Animal AI]]: guard behaviour.
- [[Test Cases - Exploit Prevention]]: shield bypass, forged knock-out events.

## Open questions

- [[Open Questions#Q-030]]: shield acquisition (automatic, generated or purchasable).
- [[Open Questions#Q-033]]: which animals defend a base.
- [[Open Questions#Q-035]]: whether the defender's own equipped team joins when present.
- [[Open Questions#Q-008]]: pens display affects which guard models exist in the base.

## Key vault documents
- [[Base Defence Overview]] · [[Animal Guards and Base Defence AI]] · [[Shield Mechanics]]
- [[Module - Defence Station]] · [[Module - Shield Generator]] · [[Animal Theft Rules]]

## Related documents
- [[Development Roadmap]]
- [[M13 - Base Upgrades]]
- [[M15 - Base Raids]]
- [[PvP and Raiding Index]]
- [[Risk Register]]
