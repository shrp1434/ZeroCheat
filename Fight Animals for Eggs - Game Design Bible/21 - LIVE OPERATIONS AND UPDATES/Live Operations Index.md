---
title: Live Operations Index
type: index
category: live-ops
status: proposed
priority: P1
owner: Live Operations Director
last_updated: 2026-11-14
tags:
  - index
  - live-ops
  - updates
---

# Live Operations Index

This folder defines how *Fight Animals for Eggs* is run and grown after launch. It covers the long-term content framework (new animals, variants, bosses, areas, eggs, base modules, seasonal content, limited-time events, balance updates, bug fixes and economy adjustments), the pipeline that ships them, and the versioning that keeps odds disclosure honest across updates.

Two ideas run through every document here:
- **Evergreen first.** The game must stay enjoyable without constant releases. Updates add freshness, they do not hold the loop together.
- **Odds never change silently.** Every update that touches a random outcome re-normalises, re-verifies and re-discloses the odds and bumps the odds-table version before release (D-017 **CONFIRMED**).

Everything in this folder is **PROPOSED** unless it quotes a confirmed decision. The roadmap milestone that runs this work is [[M23 - Live Updates]].

## Documents

| Document | One-line description |
|---|---|
| [[Live Operations Framework]] | Evergreen principle, update classes, cadence options, roles, health monitoring, incident response and fairness rules |
| [[Content Expansion Guidelines]] | Rules for adding animals, variants, bosses, areas, eggs and base modules, including the hatch-pool re-normalisation rules with a worked example |
| [[Content Update Pipeline]] | Standard, config-only and hotfix lanes from proposal to retrospective, plus rollback and environments |
| [[Seasonal and Limited-Time Events]] | Event principles, formats, lifecycle and the undecided questions on event eggs, currency and permanence |
| [[Balance Update Process]] | Evidence, change limits, approvals, nerf handling, economy and odds changes |
| [[Versioning and Changelog Policy]] | MAJOR.MINOR.PATCH game versions, config versions including `oddsTableVersion`, changelog formats and the release checklist |

## Where to start

| You want to... | Read |
|---|---|
| Add a new animal | [[Content Expansion Guidelines]] then [[Content Update Pipeline]] |
| Plan an event | [[Seasonal and Limited-Time Events]] |
| Change a number after launch | [[Balance Update Process]] |
| Ship a fix fast | [[Content Update Pipeline]] (hotfix lane) |
| Prepare a release | [[Versioning and Changelog Policy]] (release checklist) |
| Write an update proposal | [[Template - Update]] |

## Open questions owned by this folder

Raised in this folder and awaiting addition to [[Open Questions]]: **UNDECIDED** Q-1104 (cadence), Q-1105 (limited-time permanence), Q-1106 (how new animals enter pools; retirement), Q-1107 (nerf compensation), Q-1112 (seasonal tracks), Q-1113 (event currency), Q-1114 (event eggs), Q-1115 (rollout method), Q-1117 (odds sign-off authority), Q-1118 (pool binding for unhatched eggs), Q-1119 (exploit reporting programme).

## Related documents
- [[Home]]
- [[Roadmap Index]]
- [[M23 - Live Updates]]
- [[Randomised Reward Compliance]]
- [[Economy and Monetisation Index]]
- [[Changelog]]
- [[Templates Index]]
