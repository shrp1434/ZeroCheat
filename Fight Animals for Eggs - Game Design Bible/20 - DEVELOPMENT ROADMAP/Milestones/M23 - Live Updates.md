---
title: M23 - Live Updates
type: milestone
category: roadmap
status: mixed
priority: P1
owner: Live Operations Director
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - live-ops
  - updates
milestone: M23
stage: 9
complexity: M
---

# M23 - Live Updates

> [!info] PROPOSED milestone
> Stage 9 · Size **M per update cycle** (recurring) · Critical path: **yes** (it is the final, open-ended stage)

## Objective

Run the game as a sustainable live product. M23 is not a one-off milestone; it is the recurring cycle through which every post-launch update passes: new animals, variants, bosses, areas, eggs, base modules, seasonal content, limited-time events, balance updates, bug fixes and economy adjustments. The rules for each live in folder 21, starting at [[Live Operations Index]].

> [!important] Evergreen requirement
> The game must stay enjoyable without constant releases. Updates add breadth and freshness; they never patch a loop that is only fun when new content is arriving. See [[Live Operations Framework#Evergreen principle]].

## Deliverables (per update cycle)

| Deliverable | Track | Owning document |
|---|---|---|
| Update proposal on the update template | Live Ops, Design | [[Template - Update]] |
| Content built to expansion rules (roster, pools, bosses, areas, modules) | All tracks | [[Content Expansion Guidelines]] |
| Pipeline stages from proposal to retrospective | Live Ops | [[Content Update Pipeline]] |
| Event plans, where the update contains an event | Live Ops, Design | [[Seasonal and Limited-Time Events]] |
| Balance and economy changes with evidence | Economy | [[Balance Update Process]] |
| Version numbers, odds-table version, changelog and release checklist | Live Ops, Engineering | [[Versioning and Changelog Policy]] |
| Post-release monitoring and retrospective | Live Ops | [[Live Operations Framework]] |

## Dependencies

- **Upstream:** [[M22 - Launch]].
- **Downstream:** none; each cycle feeds the next.

## Complexity

**M per cycle.** A content update with a new animal is roughly the size of a small vertical slice (model, rig, animation, VFX, audio, stats, pool re-verification). Larger updates (a new region) are planned as separate milestones using the same structure as [[M16 - World Design]].

## Risks

| Risk | Why it matters here |
|---|---|
| R-013 (pool changes without re-verification) | Every new animal changes a hatch pool. |
| R-035 (release treadmill) | Content cadence must be sustainable. |
| R-037 (FOMO) | Limited-time content rules. |
| R-038 (nerf trust) | Balance updates affect long-term investment. |
| R-036 (hotfix speed) | Live exploits. |

## Acceptance criteria (per update)

- [ ] The update proposal is approved and uses [[Template - Update]].
- [ ] Every changed hatch pool is re-normalised to 100%, re-verified statistically and re-disclosed before release, with the odds-table version incremented.
- [ ] The release checklist in [[Versioning and Changelog Policy#Release checklist]] is complete.
- [ ] Player-facing patch notes and the internal [[Changelog]] entry are published with the release.
- [ ] Post-release monitoring shows no regression in errors, economy or performance, or a rollback or hotfix has been executed.

## Testing requirements

- Regression on every affected area, minimum: [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Persistence]], [[Test Cases - Exploit Prevention]].
- [[Statistical Testing of Probabilities]] for every changed odds table.
- Feature-specific test case documents for the content added (for example [[Test Cases - Bosses]] for a new boss).
- [[Test Cases - Mobile Performance]] benchmark for any new region or VFX-heavy content.

## Open questions

- **UNDECIDED** (Q-1104): live update cadence.
- **UNDECIDED** (Q-1105): permanence of limited-time content.
- **UNDECIDED** (Q-1106): how post-launch animals enter pools, and whether animals may ever be retired from a pool.
- **UNDECIDED** (Q-1107): compensation policy after nerfs.
- **UNDECIDED** (Q-1112): seasonal progression tracks and whether any paid tier is allowed.
- **UNDECIDED** (Q-1113): event currency.
- **UNDECIDED** (Q-1118): pool binding for unhatched eggs across a pool change.
- [[Open Questions#Q-006]]: variant acquisition (governs variant drops).
- [[Open Questions#Q-026]]: trading (out of scope at launch, D-045).

## Key vault documents
- [[Live Operations Index]] · [[Live Operations Framework]] · [[Content Expansion Guidelines]]
- [[Content Update Pipeline]] · [[Seasonal and Limited-Time Events]] · [[Balance Update Process]] · [[Versioning and Changelog Policy]]

## Related documents
- [[Development Roadmap]]
- [[M22 - Launch]]
- [[Template - Update]]
- [[Risk Register]]
- [[Changelog]]
