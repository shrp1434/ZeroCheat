---
title: M21 - Beta Testing
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - beta
  - telemetry
  - compliance
milestone: M21
stage: 8
complexity: L
---

# M21 - Beta Testing

> [!info] PROPOSED milestone
> Stage 8 · Size **L** · Critical path: **yes** · Exit gates: entry needs **G6 Beta ready**; exit is **G7 Launch ready**

## Objective

Validate the game with external players: fun, economy, progression pace, retention signals, stability and compliance. Use telemetry to tune PROPOSED values, rehearse live operations (hotfix lane, balance update, communication), and complete the compliance review. The beta format is **UNDECIDED** (Q-1102).

> [!warning] UNDECIDED — entry condition
> External beta should not start until every "Blocks beta" question in [[Open Questions]] has an owner decision. The list is in [[Development Roadmap#Decisions needed per gate]].

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Beta plan: cohort, access method, feedback channels, data wipe policy (**UNDECIDED**, Q-1102) | Production, Live Ops | [[Live Operations Framework]] |
| Telemetry dashboards for economy, progression, retention signals and errors | Engineering, Economy | [[Service - AnalyticsAndLoggingService]], [[Development Dashboard]] |
| Economy and progression tuning passes | Economy | [[Balance Update Process]], [[Balancing Methodology]], [[Expected Value Calculations]] |
| Free-to-play audit (full game without Robux) | Economy, Design | [[Free-to-Play Experience]] |
| Compliance review: odds disclosure, paid random item classification, content rating answers | Compliance | [[Randomised Reward Compliance]], [[Roblox Monetisation Policy Requirements]] |
| Statistical re-verification of every odds table in the beta build | QA | [[Statistical Testing of Probabilities]] |
| Live-ops rehearsal: one hotfix, one balance update, one config-only change | Live Ops | [[Content Update Pipeline]], [[Versioning and Changelog Policy]] |
| Full regression | QA | [[Test Plan Matrix]] |

## Dependencies

- **Upstream:** [[M18 - UI and UX]], [[M20 - Optimisation]].
- **Downstream:** [[M22 - Launch]].

## Complexity

**L.** External players, real telemetry, tuning loops, and the first live-ops rehearsal.

## Risks

| Risk | Why it matters here |
|---|---|
| R-001 (loop fun) | First external validation. |
| R-007, R-008 (inflation, late-game wall) | Real economy data. |
| R-004 (raids punishing) | Defender retention in real cohorts. |
| R-011, R-012 (compliance) | Final review before launch. |
| R-036 (hotfix speed) | Rehearsed here. |

## Acceptance criteria

- [ ] Every "Blocks beta" question was resolved before external access.
- [ ] Telemetry shows each region's Cash income within the modelled band, or the model and values have been updated through the balance process.
- [ ] The free-to-play audit confirms every system can be completed without Robux.
- [ ] Every disclosed odds table matches the server and passes statistical re-verification.
- [ ] The compliance review is signed by the agreed approver (Q-1117).
- [ ] One hotfix and one balance update were shipped through the pipeline with full changelog entries.
- [ ] No open defect at the top severity levels in [[Bug Reporting and Severity]].
- [ ] Every "Blocks launch" question has an owner decision before G7 is reviewed.

## Testing requirements

- All test case documents: [[Test Cases - Combat]], [[Test Cases - Animal AI]], [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Inventory and Storage]], [[Test Cases - Ascension]], [[Test Cases - Egg Merging]], [[Test Cases - Bases and Upgrades]], [[Test Cases - Raiding]], [[Test Cases - PvP]], [[Test Cases - Bosses]], [[Test Cases - Multiplayer]], [[Test Cases - Persistence]], [[Test Cases - Exploit Prevention]], [[Test Cases - Mobile Performance]].
- [[Statistical Testing of Probabilities]] on the beta build.

## Open questions

Must be resolved before external beta: [[Open Questions#Q-001]], [[Open Questions#Q-002]], [[Open Questions#Q-004]], [[Open Questions#Q-006]], [[Open Questions#Q-007]], [[Open Questions#Q-009]], [[Open Questions#Q-012]], [[Open Questions#Q-013]], [[Open Questions#Q-014]], [[Open Questions#Q-015]], [[Open Questions#Q-020]], [[Open Questions#Q-022]], [[Open Questions#Q-024]], [[Open Questions#Q-027]], [[Open Questions#Q-029]], [[Open Questions#Q-030]], [[Open Questions#Q-035]].

New:
- **UNDECIDED** (Q-1102): beta format and whether beta progress carries into launch.
- **UNDECIDED** (Q-1117): odds sign-off authority.
- **UNDECIDED** (Q-1116): content rating questionnaire answers.

## Key vault documents
- [[Live Operations Framework]] · [[Balance Update Process]] · [[Content Update Pipeline]]
- [[Randomised Reward Compliance]] · [[Roblox Monetisation Policy Requirements]] · [[Free-to-Play Experience]]
- [[Test Plan Matrix]] · [[Statistical Testing of Probabilities]] · [[Development Dashboard]]

## Related documents
- [[Development Roadmap]]
- [[M20 - Optimisation]]
- [[M22 - Launch]]
- [[Risk Register]]
- [[QA and Testing Index]]
