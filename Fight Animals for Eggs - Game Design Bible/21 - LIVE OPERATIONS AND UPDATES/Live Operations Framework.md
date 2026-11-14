---
title: Live Operations Framework
type: process
category: live-ops
status: mixed
priority: P1
owner: Live Operations Director
last_updated: 2026-11-14
tags:
  - live-ops
  - updates
  - operations
  - incident-response
---

# Live Operations Framework

How *Fight Animals for Eggs* is run after launch: what kinds of updates exist, who approves them, how the game's health is watched, how incidents are handled and how players are told. The detailed rules for each update type live in their own documents and are linked from here.

> [!info] PROPOSED
> This whole framework is a **PROPOSED** operating model. Game rules it references keep their own status. Release cadence is **UNDECIDED** (Q-1104).

## Evergreen principle

The game must remain enjoyable **without** constant releases. Live updates add breadth, freshness and reasons to return; they must never be the only thing holding the loop together.

What makes the base game evergreen (all already in the design):

| Evergreen source | Why it lasts without updates | Owning document |
|---|---|---|
| Independent hatches feeding ascension | Every duplicate has value; collection goals last a long time | [[Ascension System]], [[Independent Random Outcomes]] |
| Deterministic merging | A guaranteed path up the rarities, independent of luck | [[Egg Merging]] |
| Base progression | Per-module upgrades give long-term, self-directed goals | [[Base Upgrade System]] |
| Discovery index | Completion goal across 60 species and eight regions | [[Animal Index Feature Specification]] |
| Recurring bosses | World bosses respawn on a schedule; shared fights recur naturally | [[Boss Design Overview]] |
| Optional PvP and raids | Player-driven variety for those who opt in | [[PvP System]], [[Base Raiding System]] |
| Long-term goals | Endgame targets that do not expire | [[Long-Term Goals and Endgame]] |

Rules that follow from the principle:

1. **No update is required to keep progression possible.** If players hit a wall, fix it with a balance update; do not wait for content to paper over it.
2. **No content that expires player power.** Nothing a player earns is time-limited in effect.
3. **A quiet period is not a failure.** Engagement dips between updates are expected; a collapse between updates is a design signal (R-035 in [[Risk Register]]).
4. **Content is released when it is ready**, not to fill a calendar slot.

## Update classes

Every change shipped after launch belongs to exactly one class. The class sets the version bump, the approvals and the minimum testing.

| Class | Examples | Version impact | Approval | Minimum testing |
|---|---|---|---|---|
| **Hotfix** | Exploit fix, data bug, crash | PATCH | Live Operations Director + Lead Engineer | Targeted fix test + smoke subset |
| **Config-only change** | Kill switch, spawn timer tweak, event toggle | Config version only (no game build) | Live Operations Director; odds changes also need odds sign-off (Q-1117) | Config validation + parity check |
| **Patch** | Bug fixes, small quality improvements | PATCH | Production Manager | Affected test cases + regression subset |
| **Balance update** | Stat, ability, cost or reward tuning | MINOR (or PATCH if config-only) | Economy and Progression Designer + owner for economy-wide changes | [[Balance Update Process]] |
| **Economy adjustment** | Prices, sinks, multipliers | MINOR | Owner | [[Balance Update Process]] + [[Expected Value Calculations]] re-run |
| **Content update** | New animals, variants, bosses, eggs, base modules | MINOR | Owner | [[Content Update Pipeline]] full path |
| **Seasonal update** | Seasonal decoration, seasonal event | MINOR | Owner | [[Seasonal and Limited-Time Events]] |
| **Limited-time event** | Boss surge, community goal | MINOR or config-only | Live Operations Director + owner | [[Seasonal and Limited-Time Events]] |
| **Major expansion** | New region, new system | MAJOR | Owner | Full milestone, structured like [[M16 - World Design]] |

Versioning rules are defined in [[Versioning and Changelog Policy]].

## Content types and where their rules live

| Content type | Rules | Pipeline notes |
|---|---|---|
| New animals | [[Content Expansion Guidelines#Adding an animal without breaking hatch pools]] | Always changes a hatch pool: odds-table version bump |
| New variants | [[Content Expansion Guidelines]], [[Animal Variants]] | Acquisition is **UNDECIDED** ([[Open Questions#Q-006]]) |
| New bosses | [[Content Expansion Guidelines]], [[Boss Design Overview]] | Rewards follow whatever [[Open Questions#Q-015]] decides |
| New areas | [[Content Expansion Guidelines]], [[World Overview and Map]] | Major expansion if it adds a region |
| New eggs | [[Content Expansion Guidelines]], [[Egg System Overview]] | Seven rarities are **CONFIRMED**; no new rarity tier |
| New base modules | [[Content Expansion Guidelines]], [[Player Base System]] | Progression Score maximum changes; luck re-verified |
| Seasonal content and limited-time events | [[Seasonal and Limited-Time Events]] | Permanence **UNDECIDED** (Q-1105) |
| Balance updates and economy adjustments | [[Balance Update Process]] | Compensation **UNDECIDED** (Q-1107) |
| Bug fixes | [[Bug Reporting and Severity]], [[Content Update Pipeline#Hotfix lane]] | Severity decides lane |

## Cadence

> [!warning] UNDECIDED (Q-1104)
> The live update cadence is not decided. Options:
> - **A. Content-led:** release when an update passes its gates; no fixed rhythm.
> - **B. Regular rhythm:** a fixed cycle for content updates, with patches and hotfixes in between.
> - **C. Hybrid:** a regular patch rhythm for fixes and balance, content-led for content.
>
> **Recommendation (PROPOSED):** option C. It gives players a predictable fix rhythm without forcing content to ship unfinished, and it fits the evergreen principle. No dates are set here.

## Roles

| Role | Responsibility in live ops |
|---|---|
| Project owner | Approves content, economy and odds changes; final authority |
| Live Operations Director | Owns this framework, the pipeline, event plans, incident command and release go/no-go |
| Production Manager | Plans update scope against capacity; maintains [[Product Backlog]] |
| Economy and Progression Designer | Balance and economy evidence and proposals |
| Lead Engineer | Build integrity, hotfixes, kill switches, data safety |
| Security Engineer | Exploit triage and post-incident hardening |
| QA Lead | Regression, statistical verification, release sign-off for testing |
| Community and support (role **UNDECIDED**, part of Q-1101) | Patch notes distribution, player reports, feedback summaries |

## Health monitoring

Metrics are collected through [[Service - AnalyticsAndLoggingService]] and shown on the [[Development Dashboard]]. Alert thresholds are set from beta baselines in [[M21 - Beta Testing]] (**PROPOSED**: no thresholds are fixed before real data exists).

| Area | Metrics to watch | Investigation trigger |
|---|---|---|
| Stability | Server errors per session, client errors, crash reports | Rise above beta baseline |
| Persistence | DataStore errors, throttled writes, failed loads, session-lock conflicts | Any failed load; sustained throttling |
| Item integrity | Item audit (issued versus held), raid transfer reconciliation | Any mismatch |
| Odds | Displayed versus server parity checks, observed versus expected outcome rates | Any parity failure; outcome rate outside test tolerance |
| Economy | Cash income and spend per hour per region, roll volume, merge volume | Outside the modelled band in [[Expected Value Calculations]] |
| Progression | Distribution of players by region, level and station level | Large stall at one point ([[Progression Bottleneck Analysis]]) |
| PvP and raids | Raid count, raid outcomes, raided-player return rate | Defender return rate falls (R-004) |
| Performance | Client frame rate and memory by device class, server frame time | Below targets in [[Performance Guidelines]] |
| Monetisation | Purchase failures, receipt processing errors | Any unprocessed receipt |

## Incident response

> [!danger] Data loss, duplication, odds or purchase faults
> These are always top severity. The first action is to stop the harm (kill switch), then fix, then reconcile, then communicate.

| Step | Action | Owner |
|---|---|---|
| 1. Detect | Alert, player report or internal test | Anyone |
| 2. Triage | Assign severity using [[Bug Reporting and Severity]]; open an incident record | Live Operations Director |
| 3. Contain | Flip the relevant kill switch (rolls, hatches, merges, ascension, raids, PvP, shop, events) | Lead Engineer |
| 4. Fix | Hotfix lane in [[Content Update Pipeline#Hotfix lane]] | Lead Engineer |
| 5. Reconcile | Repair affected profiles from logs; never grant compensation without an audit | Lead Engineer, Economy and Progression Designer |
| 6. Communicate | In-game notice and patch notes stating what happened and what was done | Live Operations Director |
| 7. Review | Post-incident review; new test case; risk register update | QA Lead, Security Engineer |

**PROPOSED response targets** (local values, not in [[Canonical Proposed Values]]): for a top-severity incident, decide on containment within **1 hour** of confirmation and ship a fix or rollback within **24 hours**. These are operating targets, not promises to players.

**Kill switches** are server-side config flags read by each service. They must be changeable without publishing a new game build. A flag stored in a data store and polled by servers, or broadcast through MessagingService, are both feasible patterns; propagation delay and request budgets are *unverified* and must be measured during [[M21 - Beta Testing]]. Design detail belongs in [[Configuration Modules]].

## Player communication

1. Every release has player-facing patch notes ([[Versioning and Changelog Policy]]).
2. **Any odds change is announced in advance** in-game, and the new odds are visible on the roll and hatch screens from the moment they take effect (D-017).
3. Nerfs are explained with the reason and the evidence class (telemetry, simulation, feedback).
4. Incident notices say what happened, what players need to do (usually nothing) and what was repaired.
5. Never describe an **UNDECIDED** item as decided in public communication.

## Fairness rules for every live update

> [!success] CONFIRMED principles that bind live ops
> - Actual odds are shown before the player commits and never changed silently after purchase (D-017).
> - Hatches stay independent: no pity, no bias towards unowned animals, no history effects (D-018).
> - Hidden luck never affects wild encounter rarity (D-017).
> - The game stays fully playable without Robux; paid random rewards are not the main revenue mechanism (D-027).
> - Team size stays three; storage start values, merge ratio and raid protections stay as confirmed.

## Related documents
- [[Live Operations Index]]
- [[Content Expansion Guidelines]]
- [[Content Update Pipeline]]
- [[Seasonal and Limited-Time Events]]
- [[Balance Update Process]]
- [[Versioning and Changelog Policy]]
- [[M23 - Live Updates]]
- [[Risk Register]]
