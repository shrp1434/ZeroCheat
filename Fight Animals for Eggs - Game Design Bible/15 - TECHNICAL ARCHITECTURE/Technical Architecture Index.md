---
title: Technical Architecture Index
type: index
category: technical-architecture
status: proposed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - index
  - navigation
---

# Technical Architecture Index

How *Fight Animals for Eggs* is built on Roblox: a **server-authoritative, service-based** Luau codebase with one server Script, one client LocalScript, 18 domain services, a strict remote contract and explicit performance budgets. Everything in this folder is **PROPOSED** engineering design; it enforces the **CONFIRMED** rules in the [[Decision Register]] and leaves every **UNDECIDED** value as a configuration hook.

## Orientation

| If you want to... | Start with |
|---|---|
| Understand the whole system in one page | [[Architecture Overview]] |
| Know where a script, model or folder goes | [[Roblox Project Hierarchy]] |
| Write or review a service | [[Service Architecture]], then the service page below |
| Know whether the client or server decides something | [[Server-Client Responsibilities]] |
| Add or change a remote | [[Remote Communication Contract]] |
| Build UI or client gameplay code | [[Client Controllers]] |
| Log, report errors or add analytics | [[Logging and Error Handling]] |
| Check a frame, memory or instance budget | [[Performance Guidelines]] |

Implementation deep-dives (weighted random selection, the damage pipeline, the raid session controller, validation and rate limiting) are in [[Luau Implementation Index]]. Networking, security and persistence internals are in [[Multiplayer and Security Index]] and [[Data and Balancing Index]].

## Architecture documents

| Document | What it covers |
|---|---|
| [[Architecture Overview]] | Server and client diagrams, service dependency graph, core data flow, build order |
| [[Roblox Project Hierarchy]] | Full DataModel tree with folder purposes, single-script bootstrap, optional Rojo layout |
| [[Service Architecture]] | Service module shape, lifecycle, dependency layers, signals, state ownership, transactions, feature flags |
| [[Server-Client Responsibilities]] | Authority matrix for every outcome, prediction allowance, validation tolerances |
| [[Remote Communication Contract]] | Every RemoteEvent, RemoteFunction and UnreliableRemoteEvent with schema, validation, rate limit and response |
| [[Client Controllers]] | Client controller catalogue, StateStore, odds display contract |
| [[Logging and Error Handling]] | Structured logs, error categories, player-facing error codes, analytics events, alerts |
| [[Performance Guidelines]] | Server frame budget, AI level of detail, StreamingEnabled, instance budgets, client and mobile memory targets |

## Services

| Layer | Service | One line |
|---:|---|---|
| 0 | [[Service - AnalyticsAndLoggingService]] | Structured logging, suspicion scores, AnalyticsService adapter, client telemetry |
| 1 | [[Service - DataService]] | Session-locked profiles, atomic `Mutate`, replication deltas, saves |
| 2 | [[Service - EconomyService]] | Cash ledger, composable debits and credits, receipt processing |
| 2 | [[Service - ProgressionService]] | XP, levels, region unlocks, unique boss defeats, base Strength |
| 2 | [[Service - IndexService]] | Discovered and owned species; discovery count for the Progression Score |
| 3 | [[Service - BaseService]] | Plots, module upgrades, merge station, at-base test, bonuses, shields |
| 3 | [[Service - PvPService]] | PvP and raid participation, `CanDamage`, activation strategy hook (Q-011) |
| 4 | [[Service - LuckService]] | Progression Score, egg and hatch odds, `oddsVersion` tokens (D-041) |
| 4 | [[Service - TeamService]] | Exactly 3 slots, base lock (D-010) |
| 5 | [[Service - EggService]] | Egg inventory and capacity, roll quotes and rolls |
| 5 | [[Service - AscensionService]] | Duplicate consumption, fees, ascension levels |
| 6 | [[Service - HatchService]] | Hatch quotes and up to 5 independent hatches per request |
| 6 | [[Service - MergeService]] | 3 → 1 merges gated by station level |
| 7 | [[Service - CombatService]] | Entities, damage, cooldowns, kill credit, reward dispatch, defeat hooks |
| 8 | [[Service - AnimalAIService]] | Companion, wild and guard AI with level-of-detail scheduling |
| 9 | [[Service - SpawnService]] | Wild spawn points, respawn timers, rare-spawn announcements |
| 9 | [[Service - BossService]] | Mini-boss and world boss schedules, phases, eligibility |
| 10 | [[Service - RaidService]] | Raid eligibility, sessions, KO-before-steal, theft commit |

## Status summary

> [!success] CONFIRMED rules enforced in code
> Team of 3 (D-006); team changes only at own base (D-010); up to 5 hatches per request (D-016); two-stage randomness (D-015); odds shown before commit and never silently changed (D-017); independent hatches (D-018); Backpack 10 + Base 50 with backpack eggs never stealable (D-021); max 3 animals stolen per successful raid, KO-before-steal, no raids on offline bases (D-024); merge 3 → 1 with station gates (D-020).

> [!warning] UNDECIDED values kept as configuration hooks
> Raid duration ([[Open Questions#Q-012]]) and egg theft limit ([[Open Questions#Q-013]]) ship as `nil`, which disables raids. Also: PvP activation ([[Open Questions#Q-011]]), defeat penalties ([[Open Questions#Q-014]]), boss rewards ([[Open Questions#Q-015]]), storage expansion currency and price ([[Open Questions#Q-009]], [[Open Questions#Q-010]]), stolen animal retention ([[Open Questions#Q-025]]), shield acquisition ([[Open Questions#Q-030]]) and raid defenders ([[Open Questions#Q-033]]). New technical questions raised in this folder are Q-801 to Q-810; they are listed on the pages that raise them.

## Related documents
- [[Home]]
- [[Development Dashboard]]
- [[Luau Implementation Index]]
- [[Multiplayer and Security Index]]
- [[Data and Balancing Index]]
- [[Template - Technical Service]]
- [[M02 - Core Project Setup]]
