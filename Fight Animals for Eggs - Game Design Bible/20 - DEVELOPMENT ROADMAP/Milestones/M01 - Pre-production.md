---
title: M01 - Pre-production
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - pre-production
milestone: M01
stage: 0
complexity: M
---

# M01 - Pre-production

> [!info] PROPOSED milestone
> Stage 0 · Size **M** · Critical path: **yes** · Exit gate: **G0 Concept locked** ([[Development Roadmap#Stage gates]])

## Objective

Turn the owner brief into a buildable plan. At the end of M01 the team agrees what is being built, which owner decisions are **CONFIRMED**, which values are **PROPOSED** working assumptions, how the code will be structured, and the order of work. No production content is built here; only proofs that remove the largest technical unknowns.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Vision, pillars and fairness charter reviewed by the owner | Design | [[Vision Statement and Pillars]], [[Design Principles and Fairness Charter]] |
| Launch scope statement and draft cut line (Q-1103) | Production | [[Scope and Launch Targets]] |
| Core loop and session flow agreed | Design | [[Core Gameplay Loop]], [[Session Flow and Player Journey]] |
| First balance pass for every number | Design | [[Canonical Proposed Values]] |
| Working assumption for every "Blocks prototype" question | Production | [[Open Questions]] |
| Architecture overview and service list | Engineering | [[Architecture Overview]], [[Service Architecture]] |
| Spike: one wild animal and one companion with server-side AI at target counts | Engineering | [[Animal Scalability and Performance Budgets]] |
| Spike: DataStore session-locked save and load | Engineering | [[Save, Load and Recovery]] |
| Style frames and one finished low-poly test animal through rig, animation and in-engine lighting | Art | [[Art Bible]], [[Animal Modelling Principles]], [[Animal Rig Standards]] |
| Sound pillars and a reference palette | Audio | [[Sound Bible]] |
| QA strategy and test plan skeleton | QA | [[QA Strategy]], [[Test Plan Matrix]] |
| Roadmap, risk register and backlog | Production | [[Development Roadmap]], [[Risk Register]], [[Product Backlog]] |

## Dependencies

- **Upstream:** none. This is the first milestone.
- **Downstream:** [[M02 - Core Project Setup]], [[M16 - World Design]] (art direction and region list feed greybox work).

## Complexity

**M.** Mostly documentation and decisions, but the two spikes (AI scale and persistence) carry real technical uncertainty. The size grows if owner decisions take several rounds (R-029).

## Risks

| Risk | Why it matters here |
|---|---|
| R-029 (owner decision latency) | Many "Blocks prototype" questions must at least have a working assumption before M02. |
| R-030 (no cut line) | Without a cut line, every later slip delays launch. |
| R-027 (art scope) | The test animal sets the throughput baseline for 60 animals. |
| R-018 (server simulation cost) | The AI spike gives the first real measurement against the PROPOSED budgets. |
| R-031 (key-person dependency) | Staffing is **UNDECIDED** (Q-1101). |

## Acceptance criteria

- [ ] The owner has reviewed the vision, scope and core loop documents.
- [ ] Every **CONFIRMED** fact in [[Decision Register]] is reflected without contradiction in the design documents.
- [ ] Every "Blocks prototype" question has a written working assumption marked **PROPOSED**.
- [ ] The AI spike reports frame cost for the PROPOSED animal counts in [[Canonical Proposed Values#15. Server and performance targets (PROPOSED)]].
- [ ] The persistence spike saves, reloads and recovers from a forced server shutdown without loss.
- [ ] The test animal passes the art review and has a measured production effort, used to re-check R-027.
- [ ] The roadmap and risk register have been reviewed by every track lead.

## Testing requirements

No feature test cases run in M01. QA delivers the plan that later milestones execute:
- [[QA Strategy]] and the first version of [[Test Plan Matrix]], mapping each milestone to its test documents.
- Agreement on the statistical method for odds verification in [[Statistical Testing of Probabilities]].
- Spike results are recorded as evidence, not as passed tests.

## Open questions

Must have a working assumption before G0:
- [[Open Questions#Q-008]] (pens display), [[Open Questions#Q-011]] (PvP activation), [[Open Questions#Q-021]] (animal levelling), [[Open Questions#Q-023]] (hatch timing), [[Open Questions#Q-025]] (stolen animal state), [[Open Questions#Q-028]] (aquatic movement), [[Open Questions#Q-031]] (server size), [[Open Questions#Q-033]] (base defenders), [[Open Questions#Q-034]] (merge timing).

Should be discussed now, decided by beta:
- [[Open Questions#Q-001]] (world layout), [[Open Questions#Q-002]] (catalogue), [[Open Questions#Q-007]] (modules at launch).

New roadmap questions:
- **UNDECIDED** (Q-1101): staffing and discipline ownership.
- **UNDECIDED** (Q-1103): launch scope cut line.

## Key vault documents
- [[Vision Statement and Pillars]] · [[Scope and Launch Targets]] · [[Core Gameplay Loop]]
- [[Canonical Proposed Values]] · [[Decision Register]] · [[Open Questions]]
- [[Architecture Overview]] · [[Art Bible]] · [[Sound Bible]] · [[QA Strategy]]

## Related documents
- [[Development Roadmap]]
- [[Risk Register]]
- [[Roadmap Index]]
- [[M02 - Core Project Setup]]
- [[M16 - World Design]]
