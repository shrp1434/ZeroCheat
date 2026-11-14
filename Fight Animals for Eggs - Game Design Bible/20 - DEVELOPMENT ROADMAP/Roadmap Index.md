---
title: Roadmap Index
type: index
category: roadmap
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - index
  - roadmap
  - milestones
---

# Roadmap Index

This folder holds the production plan: the staged roadmap, the risk register and one document per milestone. Everything in it is **PROPOSED**. The plan uses **relative complexity (S, M, L, XL)** and contains **no dates**. Dates depend on staffing, which is **UNDECIDED** (Q-1101).

**Start here:**
1. [[Development Roadmap]]: stages, dependency graph, parallel tracks, critical path and stage gates.
2. [[Risk Register]]: every known project risk with likelihood, impact, mitigation, owner and trigger.
3. The milestone documents below, each with objective, deliverables, dependencies, complexity, risks, acceptance criteria, tests, open questions and key documents.

## Core documents

| Document | Purpose |
|---|---|
| [[Development Roadmap]] | The staged plan, the Mermaid dependency graph of all 23 milestones, tracks, gates and the critical path |
| [[Risk Register]] | Design, economy, compliance, technical, security, scope, team and live-ops risks |

## Milestones

| ID | Milestone | Stage | Size | One-line description |
|---|---|---:|:---:|---|
| M01 | [[M01 - Pre-production]] | 0 | M | Lock scope, working assumptions, architecture spikes and the production plan |
| M02 | [[M02 - Core Project Setup]] | 1 | M | Project hierarchy, services, persistence, remote validation, logging and config |
| M03 | [[M03 - Player Movement]] | 1 | S | Player controller, camera and input on PC, mobile and gamepad |
| M04 | [[M04 - Player Combat]] | 2 | L | Player basic combo, specials, dodge, Player Strength and the damage pipeline |
| M05 | [[M05 - Animal AI]] | 2 | L | Wild and companion AI state machines, spawning, leash and performance LOD |
| M06 | [[M06 - Animal Combat]] | 2 | L | Three-animal team combat, abilities, targeting commands, rewards and kill credit |
| M07 | [[M07 - Animal Collection]] | 3 | M | Owned animals, discovery index, team equipping and the base lock rule |
| M08 | [[M08 - Egg Rolling]] | 3 | M | Cash-to-egg rolls with progression luck and server-bound odds disclosure |
| M09 | [[M09 - Hatching]] | 3 | M | Hatch up to five eggs from rarity pools, storage and hatch presentation |
| M10 | [[M10 - Ascension]] | 3 | M | Duplicate-consuming ascension with stat and visual tiers |
| M11 | [[M11 - Egg Merging]] | 4 | M | Three-to-one merging at the upgradeable Egg Merging Station |
| M12 | [[M12 - Player Bases]] | 4 | L | Personal base plots, module slots, egg vault and team change point |
| M13 | [[M13 - Base Upgrades]] | 4 | M | Per-module upgrade levels, costs, effects and visual changes |
| M14 | [[M14 - Base Defence]] | 4 | L | Physical defences, shields and animal guard AI |
| M15 | [[M15 - Base Raids]] | 5 | XL | Optional PvP and raids with the confirmed theft and protection rules |
| M16 | [[M16 - World Design]] | 6 | XL | Hub and all launch regions, spawn tables, hazards and unlock flow |
| M17 | [[M17 - Boss Encounters]] | 6 | L | Eight mini-bosses and four world bosses with scheduling |
| M18 | [[M18 - UI and UX]] | 7 | L | UI consistency, onboarding, accessibility, shop and notifications |
| M19 | [[M19 - Multiplayer Testing]] | 7 | L | Full-server load, raid and persistence robustness, exploit red-teaming |
| M20 | [[M20 - Optimisation]] | 7 | L | Server, client, memory and network performance to target |
| M21 | [[M21 - Beta Testing]] | 8 | L | External beta, telemetry-driven tuning and compliance review |
| M22 | [[M22 - Launch]] | 8 | M | Release readiness, launch operations and the first hotfix window |
| M23 | [[M23 - Live Updates]] | 9 | M | Recurring content, balance and event updates through the live ops pipeline |

## Conventions used in milestone documents

- **Dependencies** link upstream milestones (must be done first) and downstream milestones (waiting on this one).
- **Risks** cite IDs from the [[Risk Register]].
- **Open questions** cite IDs from [[Open Questions]]; new roadmap questions use the Q-11xx range and are written without links until the lead adds them to that page.
- **Acceptance criteria** are checklists; a milestone is done only when every box is ticked and the [[Definition of Done]] is met.

## Related documents
- [[Home]]
- [[Development Dashboard]]
- [[Product Backlog]]
- [[Definition of Done]]
- [[Live Operations Index]]
- [[QA and Testing Index]]
- [[Decisions Index]]
