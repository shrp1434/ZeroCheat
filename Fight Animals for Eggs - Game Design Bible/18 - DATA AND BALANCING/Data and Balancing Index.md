---
title: Data and Balancing Index
type: index
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - index
  - data
  - balancing
---

# Data and Balancing Index

This folder holds two things: **the numbers** (every proposed value, and the method for tuning and verifying them) and **the data model** (how player state is stored, versioned, saved and recovered). Designers usually start with [[Canonical Proposed Values]] and [[Balancing Methodology]]. Engineers usually start with [[Data Architecture Overview]] and then the schema for the system they are building.

> [!info] Status
> The data architecture, schemas, balancing method and simulations are **PROPOSED**. The game rules they encode (team of **3**, storage **10 + 50**, at most **3** animals stolen per raid, 3:1 egg merging, seven rarities, up to **5** simultaneous hatches) are **CONFIRMED** in the [[Decision Register]].

## Numbers and balancing

| Document | What it is for |
|---|---|
| [[Canonical Proposed Values]] | The single source of every proposed number: rarities, roster, stat model, combat, regions, rewards, odds, ascension, merging, storage, base modules, progression |
| [[Balancing Methodology]] | How stats, economy and probabilities are tuned: Power Index, TTK and Cash-per-hour targets, odds verification, telemetry KPIs and the change process |
| [[Balance Simulation Plan]] | Seven concrete simulations with inputs, outputs, pass criteria and sample results from a Python model of the proposed formulas |

## Data architecture

| Document | What it is for |
|---|---|
| [[Data Architecture Overview]] | Entity model, DataStore key layout, session locking, transaction kinds, runtime architecture, type conventions and size budget |
| [[Data Validation and Migration]] | `schemaVersion`, the ordered migration pipeline, validation and repair classes, rolling-update rules and quarantine |
| [[Save, Load and Recovery]] | Autosave cadence, leave and shutdown saves, retries and budget, lock contention, `ProcessReceipt` idempotency, raid commits, rollback and failure scenarios |

## Schemas

Each schema gives the purpose, a field table, an illustrative Luau type and constructor, invariants, migration notes and a size estimate.

| Document | Profile section | Covers |
|---|---|---|
| [[Schema - Player Profile]] | root and `meta` | Envelope, session lock, identity, settings, pending transactions, idempotency ring |
| [[Schema - Player Progression]] | `progression` | Level, XP and the stored inputs to player strength (Strength itself is derived) |
| [[Schema - Animal Collection]] | `animals` | Animal instances with species, variant, ascension, provenance and lock flags |
| [[Schema - Equipped Team]] | `team` | Exactly three team slots and their invariants |
| [[Schema - Egg Inventory]] | `eggs` | Egg instances, backpack and base locations, `oddsVersion` audit field, backpack expansion |
| [[Schema - Base Data]] | `base` | Plot, modules and upgrades, Merge Station level, vault expansion, guards, shield timers, trophies |
| [[Schema - Economy]] | `economy` | Cash, lifetime source and sink counters, processed purchase receipts |
| [[Schema - Unlocks and Boss Progress]] | `unlocks` | Regions, mini-boss and world boss defeats, onboarding, feature flags |
| [[Schema - Discovery Index]] | `index` | Per-species discovery, defeat counts and ownership history |

## Reading paths

- **Building a gameplay service:** [[Data Architecture Overview]] → the relevant schema → [[Data Consistency and Transactions]] → [[Service - DataService]].
- **Changing a number:** [[Canonical Proposed Values]] → [[Balancing Methodology]] → [[Balance Simulation Plan]] → [[Balance Update Process]].
- **Handling a data incident:** [[Save, Load and Recovery]] → [[Data Validation and Migration]] → [[Test Cases - Persistence]].

## Open questions raised in this folder

| ID | Question | Status |
|---|---|---|
| Q-951 | Where stolen eggs land in the raider's storage, and what happens when it is full | **UNDECIDED** |
| Q-952 | Whether obtaining a species without defeating it counts as "discovered" | **UNDECIDED** |
| Q-953 | Whether percentage bonuses from different sources add or multiply | **UNDECIDED** |
| Q-954 | Where a merge output goes when the vault is full and all inputs come from the backpack | **UNDECIDED** |
| Q-955 | Retention periods for audit, ledger and quarantine records, and erasure handling | **UNDECIDED** |
| Q-956 | Whether to keep a daily profile snapshot store in addition to DataStore version history | **UNDECIDED** |
| Q-957 | What happens when a raider at owned-animal capacity steals an animal | **UNDECIDED** |
| Q-958 | Whether ascension duplicates must match the original's variant | **UNDECIDED** |
| Q-959 | Target split of team damage between the player and their animals | **UNDECIDED** |

These are pending transfer to [[Open Questions]].

## Related documents
- [[Home]]
- [[Vault Map]]
- [[Technical Architecture Index]]
- [[Economy and Monetisation Index]]
- [[QA and Testing Index]]
- [[Decision Register]]
- [[Open Questions]]
