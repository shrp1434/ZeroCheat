---
title: Luau Implementation Index
type: index
category: engineering
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - index
  - luau
  - engineering
---

# Luau Implementation Index

This folder turns the design and the technical architecture into concrete, typed Luau patterns. It sits between [[Technical Architecture Index]] (what services exist and what they own) and the game-system folders (what the rules are). Every code block here is **illustrative — not executed**: nothing has been run in Roblox Studio at the time of writing, and every API we depend on is tracked in [[Roblox API Reference Notes]].

> [!info] Status
> Patterns and code here are **PROPOSED**. Where code encodes a **CONFIRMED** rule (team of three, hatch up to five, backpack 10 + base 50, three animals per raid, backpack eggs never stealable, offline bases never raidable, undefeated defenders never stealable, 3 → 1 merges), the code comments say so. **UNDECIDED** values such as raid duration ([[Open Questions#Q-012]]) and the egg theft limit ([[Open Questions#Q-013]]) are configurable with no default.

## Orientation

| If you are… | Start with |
|---|---|
| New to the codebase | [[Luau Coding Standards]] → [[Module Patterns and Bootstrapping]] → [[Configuration Modules]] |
| Working on eggs | [[Implementation - Weighted Random Selection]] → [[Implementation - Dynamic Luck Calculation]] → [[Implementation - Egg Roll and Hatch Flow]] |
| Working on progression transactions | [[Implementation - Egg Roll and Hatch Flow#Transaction helper]] → [[Implementation - Ascension Transaction]] → [[Implementation - Egg Merge Transaction]] |
| Working on combat or AI | [[Implementation - Combat Damage Pipeline]] → [[Implementation - Animal AI State Machine]] |
| Working on raids | [[Implementation - Raid Session Controller]], then [[Data Consistency and Transactions]] |
| Reviewing security | [[Implementation - Remote Validation Layer]] → [[Implementation - Rate Limiting]] → [[Exploit Prevention]] |

## Documents

| Document | One-line description |
|---|---|
| [[Luau Coding Standards]] | `--!strict`, naming, server-authority rules, no-yield transactions, review checklist |
| [[Module Patterns and Bootstrapping]] | Single entry point per side, registry, two-phase `Init`/`Start`, remote gateway, lifecycle hooks |
| [[Configuration Modules]] | Typed, frozen, boot-validated config built from [[Canonical Proposed Values]]; secret versus public config; `ConfigVersion` |
| [[Implementation - Weighted Random Selection]] | Pure cumulative-weight selector with validation and floating-point residue handling; test vectors |
| [[Implementation - Dynamic Luck Calculation]] | Exact Progression Score, egg-rarity and hatch-tilt formulas; `oddsVersion` token and stale-token rejection |
| [[Implementation - Egg Roll and Hatch Flow]] | Full server flow: idempotency, capacity, atomic debit and credit, five-egg hatch limit, reason codes |
| [[Implementation - Ascension Transaction]] | Duplicate consumption with ownership, species, equipped and raid locks; rollback |
| [[Implementation - Egg Merge Transaction]] | 3 → 1 merge with station gates, fees, locks, capacity and rollback |
| [[Implementation - Combat Damage Pipeline]] | Intent-only client, server range, cooldown and line-of-sight checks, canonical damage formula |
| [[Implementation - Animal AI State Machine]] | States and transitions for wild animals, companions and guards; LOD tick-rate scheduler |
| [[Implementation - Raid Session Controller]] | Raid state machine, configurable timers, theft caps, KO verification, offline protection, transfer commit |
| [[Implementation - Remote Validation Layer]] | Gateway pipeline, validator combinators, schemas, sanity bounds, shared reason codes |
| [[Implementation - Rate Limiting]] | Per-player token buckets, parameters, violation scoring and thresholds |
| [[Roblox API Reference Notes]] | Every Roblox API relied on, with verification status |

## Cross-cutting conventions

- **Client sends intent, server decides outcomes** ([[Server-Client Responsibilities]]).
- **One transaction helper** for every economy mutation: snapshot → mutate → invariants → commit or roll back, with no yields.
- **Idempotency keys** on every economy request.
- **Odds tokens** on every roll and hatch.
- **Reason codes**, not errors, for expected failures.

## Related documents
- [[Technical Architecture Index]]
- [[Multiplayer and Security Index]]
- [[Service Architecture]]
- [[Remote Communication Contract]]
- [[Data and Balancing Index]]
- [[QA and Testing Index]]
