---
title: M02 - Core Project Setup
type: milestone
category: roadmap
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - engineering
  - architecture
milestone: M02
stage: 1
complexity: M
---

# M02 - Core Project Setup

> [!info] PROPOSED milestone
> Stage 1 · Size **M** · Critical path: **yes** · Exit gate: **G1 Technical foundation** (with M03)

## Objective

Build the technical skeleton every later feature plugs into: the Roblox project hierarchy, service bootstrapping, a persistent player profile, a validated remote layer, rate limiting, logging and configuration modules. After M02, adding a feature means adding a service and a config file, not inventing infrastructure.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Place hierarchy and folder conventions | Engineering | [[Roblox Project Hierarchy]] |
| Service bootstrap and module patterns | Engineering | [[Module Patterns and Bootstrapping]], [[Service Architecture]] |
| DataService: session-locked load, autosave, `game:BindToClose` flush, retry and recovery | Engineering | [[Service - DataService]], [[Save, Load and Recovery]] |
| Player profile schema v1 with schema version field and migration hook | Engineering | [[Schema - Player Profile]], [[Data Validation and Migration]] |
| Remote communication contract and validation layer | Engineering | [[Remote Communication Contract]], [[Implementation - Remote Validation Layer]] |
| Per-remote rate limiting | Engineering | [[Implementation - Rate Limiting]] |
| Logging, error handling and analytics service skeleton | Engineering | [[Logging and Error Handling]], [[Service - AnalyticsAndLoggingService]] |
| Configuration modules generated from canonical values, with a config version | Engineering, Design | [[Configuration Modules]], [[Canonical Proposed Values]] |
| Coding standards and review checklist | Engineering | [[Luau Coding Standards]] |
| Separate test environment so test data never touches production saves (structure **UNDECIDED**, Q-1109) | Engineering, QA | [[Data Architecture Overview]] |
| Persistence and exploit test harness | QA | [[Test Cases - Persistence]], [[Test Cases - Exploit Prevention]] |

## Dependencies

- **Upstream:** [[M01 - Pre-production]] (architecture and persistence spike).
- **Downstream:** [[M03 - Player Movement]], [[M05 - Animal AI]], and indirectly every feature milestone.

## Complexity

**M.** Well-understood patterns, but mistakes here are expensive later. Persistence and remote validation must be reviewed by two engineers (R-031).

## Risks

| Risk | Why it matters here |
|---|---|
| R-016 (DataStore budgets) | Write scheduling designed now avoids rework at load-test time. |
| R-023 (remote exploitation) | Every remote must pass validation from day one. |
| R-032 (doc and code drift) | Config generated from [[Canonical Proposed Values]] keeps numbers in one place. |
| R-031 (key-person dependency) | Data layer needs a second owner. |

## Acceptance criteria

- [ ] A player joins, receives a default profile, leaves, rejoins and gets the same profile.
- [ ] Two servers cannot hold the same profile at once (session lock verified).
- [ ] A forced shutdown flushes pending saves; no profile loses committed changes.
- [ ] Every client-to-server remote is declared in the contract and passes through validation; an undeclared or malformed call is rejected and logged.
- [ ] Rate limits reject bursts above the configured rate without disconnecting legitimate players.
- [ ] Config values are read from configuration modules only; no gameplay numbers are hard-coded.
- [ ] Each configuration module exposes its version, and the build logs the versions it loaded.
- [ ] Test sessions cannot write to production data stores.

## Testing requirements

- [[Test Cases - Persistence]]: load, save, session lock, shutdown flush, corrupted-data recovery.
- [[Test Cases - Exploit Prevention]]: malformed remote payloads, flooding, wrong types, out-of-range values.
- Unit tests for the validation layer and migration hook (illustrative test approach in [[Luau Coding Standards]]).

## Open questions

- [[Open Questions#Q-031]]: server size affects DataStore load per server. Use the working assumption of 16.
- **UNDECIDED** (Q-1108): analytics stack (Roblox built-in analytics only, or additional external telemetry through HttpService, which would need a privacy review).
- **UNDECIDED** (Q-1109): staging structure (a separate test experience versus test places) and how production data stores stay isolated.

## Key vault documents
- [[Architecture Overview]] · [[Service Architecture]] · [[Server-Client Responsibilities]]
- [[Service - DataService]] · [[Data Architecture Overview]] · [[Save, Load and Recovery]]
- [[Remote Communication Contract]] · [[Implementation - Remote Validation Layer]] · [[Implementation - Rate Limiting]]
- [[Configuration Modules]] · [[Roblox API Reference Notes]]

## Related documents
- [[Development Roadmap]]
- [[Risk Register]]
- [[M01 - Pre-production]]
- [[M03 - Player Movement]]
- [[M05 - Animal AI]]
- [[Security Architecture]]
