---
title: Development Dashboard
type: dashboard
category: navigation
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - dashboard
  - development
  - production
---

# Development Dashboard

The working view for engineers, QA and producers. For design, see the [[Design Dashboard]].

> [!danger] Implementation status
> No game code exists yet. All Luau in the vault is **illustrative** and has not been run in Roblox Studio. No test has been executed against a build. Probability tables were verified by a Python generator against the proposed formulas only.

## Milestones

```mermaid
flowchart LR
    M01["M01 Pre-production"] --> M02["M02 Project setup"]
    M02 --> M03["M03 Movement"] --> M04["M04 Player combat"]
    M02 --> M05["M05 Animal AI"] --> M06["M06 Animal combat"]
    M04 --> M06
    M06 --> M07["M07 Collection"] --> M08["M08 Egg rolling"] --> M09["M09 Hatching"]
    M09 --> M10["M10 Ascension"]
    M09 --> M11["M11 Egg merging"]
    M07 --> M12["M12 Bases"] --> M13["M13 Base upgrades"] --> M14["M14 Base defence"] --> M15["M15 Raids"]
    M12 --> M11
    M06 --> M16["M16 World"] --> M17["M17 Bosses"]
    M18["M18 UI and UX"]
    M15 --> M19["M19 Multiplayer testing"]
    M17 --> M19
    M19 --> M20["M20 Optimisation"] --> M21["M21 Beta"] --> M22["M22 Launch"] --> M23["M23 Live updates"]
```

The full plan, with dependencies and the critical path, is in [[Development Roadmap]]. Risks are in the [[Risk Register]].

## Engineering entry points

| Topic | Document |
|---|---|
| Architecture | [[Architecture Overview]] · [[Service Architecture]] · [[Roblox Project Hierarchy]] |
| Client/server contract | [[Remote Communication Contract]] · [[Server-Client Responsibilities]] |
| Implementation guides | [[Luau Implementation Index]] · [[Luau Coding Standards]] |
| Data | [[Data Architecture Overview]] · [[Save, Load and Recovery]] · [[Data Validation and Migration]] |
| Multiplayer | [[Multiplayer Architecture]] · [[Replication Strategy]] · [[Animal Scalability and Performance Budgets]] |
| Security | [[Security Architecture]] · [[Exploit Prevention]] · [[Threat Model]] |
| Performance | [[Performance Guidelines]] |
| Platform APIs | [[Roblox API Reference Notes]] |

## Server-authority checklist

Every one of these is validated on the server, never trusted from the client ([[Security Architecture]]):

| Validation | Owning service |
|---|---|
| Cash transactions | [[Service - EconomyService]] |
| Egg rolls and odds tokens | [[Service - EggService]] · [[Service - LuckService]] |
| Hatch results (at most 5 per request) | [[Service - HatchService]] |
| Animal ownership | [[Service - DataService]] |
| Ascension | [[Service - AscensionService]] |
| Egg merging | [[Service - MergeService]] |
| Inventory capacity (10 / 50) | [[Service - EggService]] |
| Combat damage | [[Service - CombatService]] |
| Team of 3 and base lock | [[Service - TeamService]] |
| Raid eligibility, offline protection, theft (KO first, max 3 animals) | [[Service - RaidService]] |
| Player progression and Progression Score | [[Service - ProgressionService]] |

## QA

| Need | Document |
|---|---|
| Strategy and coverage | [[QA Strategy]] · [[Test Plan Matrix]] |
| Probability verification | [[Statistical Testing of Probabilities]] |
| Bug process | [[Bug Reporting and Severity]] |
| Done criteria | [[Definition of Done]] |

## Backlog

The prioritised P0–P3 backlog is in [[Product Backlog]] ([[Backlog Index]]).

## Related documents

[[Home]] · [[Technical Architecture Index]] · [[Multiplayer and Security Index]] · [[QA and Testing Index]] · [[Roadmap Index]]
