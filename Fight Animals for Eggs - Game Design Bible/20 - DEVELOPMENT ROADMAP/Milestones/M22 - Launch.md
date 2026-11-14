---
title: M22 - Launch
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - launch
  - release
milestone: M22
stage: 8
complexity: M
---

# M22 - Launch

> [!info] PROPOSED milestone
> Stage 8 · Size **M** · Critical path: **yes** · Exit gate: **G8 Launched**

## Objective

Release *Fight Animals for Eggs* publicly on Roblox (D-001 **CONFIRMED**) with the 60-animal launch target (D-004) and the launch scope agreed under the cut line. Launch is an operations milestone, not a feature milestone: no new features enter after G7. The work is release readiness, launch-day operations and the first stabilisation window.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Release candidate built and versioned (first public MAJOR version, all config versions recorded) | Engineering | [[Versioning and Changelog Policy]] |
| Release checklist completed and signed | Production, QA, Compliance | [[Versioning and Changelog Policy#Release checklist]] |
| Production data stores verified clean of test data; schema version recorded | Engineering | [[Data Validation and Migration]] |
| Experience settings, content rating questionnaire and monetisation settings reviewed | Production, Compliance | [[Roblox Monetisation Policy Requirements]], [[Roblox Platform References]] |
| Store page assets (thumbnails, icon, description) consistent with the art direction | Art | [[Art Bible]], [[Visual Reference Placeholders]] |
| Launch monitoring: error rates, DataStore errors, purchase failures, economy dashboards | Engineering, Live Ops | [[Service - AnalyticsAndLoggingService]], [[Development Dashboard]] |
| On-call rota and incident process for the stabilisation window | Live Ops | [[Live Operations Framework]] |
| Hotfix lane ready, with kill switches for rolls, hatches, raids and the shop | Engineering, Live Ops | [[Content Update Pipeline#Hotfix lane]] |
| Launch patch notes | Live Ops | [[Template - Update]] |

## Dependencies

- **Upstream:** [[M21 - Beta Testing]].
- **Downstream:** [[M23 - Live Updates]].

## Complexity

**M.** Little new code, but high coordination load and zero tolerance for data or compliance errors.

## Risks

| Risk | Why it matters here |
|---|---|
| R-016 (DataStore budgets) | Launch concurrency is the peak load. |
| R-022 (update rollout interrupts transactions) | Hotfixes during the stabilisation window. |
| R-036 (hotfix speed) | First real use. |
| R-011, R-012 (compliance) | Any disclosure fault at launch is maximum impact. |
| R-034 (overwork) | Launch crunch. |

## Acceptance criteria

- [ ] Every "Blocks launch" question in [[Open Questions]] has an owner decision recorded in the [[Decision Register]].
- [ ] The release checklist is complete with no waived compliance item.
- [ ] Odds tables in production match the signed odds tables by version number.
- [ ] No Robux product grants Cash unless [[Open Questions#Q-032]] was decided otherwise and the paid-random-item requirements are implemented.
- [ ] Monitoring alerts fire in a launch rehearsal for each kill-switch scenario.
- [ ] The stabilisation window ends with no open top-severity defect and no unreconciled item audit.

## Testing requirements

- Release smoke subset from [[Test Plan Matrix]]: [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Persistence]], [[Test Cases - Exploit Prevention]], [[Test Cases - Raiding]].
- [[Statistical Testing of Probabilities]]: verification of the release odds tables.
- [[Test Cases - Mobile Performance]]: release candidate benchmark run.

## Open questions

Must be resolved before launch: [[Open Questions#Q-003]], [[Open Questions#Q-005]], [[Open Questions#Q-010]], [[Open Questions#Q-016]], [[Open Questions#Q-017]], [[Open Questions#Q-018]], [[Open Questions#Q-019]], [[Open Questions#Q-026]], [[Open Questions#Q-032]].

New:
- **UNDECIDED** (Q-1116): content rating questionnaire answers.
- **UNDECIDED** (Q-1115): update rollout method for post-launch hotfixes.
- **UNDECIDED** (Q-1119): exploit disclosure or bug-report reward programme.

## Key vault documents
- [[Versioning and Changelog Policy]] · [[Content Update Pipeline]] · [[Live Operations Framework]]
- [[Roblox Monetisation Policy Requirements]] · [[Randomised Reward Compliance]] · [[Scope and Launch Targets]]

## Related documents
- [[Development Roadmap]]
- [[M21 - Beta Testing]]
- [[M23 - Live Updates]]
- [[Risk Register]]
- [[Changelog]]
