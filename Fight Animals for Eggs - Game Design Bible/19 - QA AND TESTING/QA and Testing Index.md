---
title: QA and Testing Index
type: index
category: qa
status: proposed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - testing
  - index
---

# QA and Testing Index

This folder defines how *Fight Animals for Eggs* is verified: the strategy and gates, the coverage plan, the statistical method for proving egg odds, the bug process, and 496 test cases across 14 documents.

## Orientation

- **New to QA here?** Read [[QA Strategy]] first (quality goals, global invariants INV-01 to INV-12, test levels, environments, gates). Then use the [[Test Plan Matrix]] to find the cases for the system you are working on.
- **Working on eggs, luck or spawns?** Any change to odds, pools, slopes or selection code must pass the gate in [[Statistical Testing of Probabilities]].
- **Found a bug?** Follow [[Bug Reporting and Severity]]. Invariant failures and odds-disclosure problems are always S1.
- **Writing a test case?** Use [[Template - Test Case]] and the table format used in every test-case document: ID, Title, Preconditions, Steps, Expected result, Priority (P0–P3), Type (functional, edge, negative, security, performance, statistical) and the related decision or question ID.

> [!warning] UNDECIDED values are tested as parameters
> Raid duration ([[Open Questions#Q-012]]), the egg theft limit ([[Open Questions#Q-013]]), defeat penalties ([[Open Questions#Q-014]]) and other open items are tested through configuration symbols (`T_raid`, `L_egg`, penalty rows). No test document states a value for them.

## Core documents

| Document | Purpose |
|---|---|
| [[QA Strategy]] | Quality goals, global invariants, test levels L1–L8, environments, testability requirements, gates and regression suites |
| [[Test Plan Matrix]] | Case counts, system × level coverage, milestone gates, decision traceability, mandatory edge-case index, UNDECIDED-parameter coverage |
| [[Statistical Testing of Probabilities]] | Exact luck and pool expected values, chi-squared and binomial methods, sample sizes for rare tiers, Wilson intervals, independence tests, release gate |
| [[Bug Reporting and Severity]] | Severity S1–S4, priority P0–P3, required fields, triage workflow, statuses, beta reports |

## Test cases (folder `Test Cases`)

| Document | Prefix | Scope |
|---|---|---|
| [[Test Cases - Combat]] | TC-CMB | Damage formula, player combo and specials, Strength, animal abilities, targeting, combat tag, wild modifiers, rewards, kill credit, defeat |
| [[Test Cases - Animal AI]] | TC-AI | Companions, wild AI, leash, respawn, rare-spawn chances and announcements, luck-independence of spawns, guard AI, AI budgets |
| [[Test Cases - Egg Rolls and Hatching]] | TC-EGG | Roll purchase and capacity, luck and disclosure, `oddsVersion`, selection statistics, hatching up to five, independence, hatch location |
| [[Test Cases - Inventory and Storage]] | TC-INV | Backpack and base storage, expansion (currency and price UNDECIDED), animal collection, team equipping and base lock |
| [[Test Cases - Ascension]] | TC-ASC | Duplicate requirements and fees, invalid duplicates, equipped and defending animals, stat effects, transactions |
| [[Test Cases - Egg Merging]] | TC-MRG | Station purchase, upgrades and gates, merge rules, mixed rarities, Secret eggs, capacity, merged-egg fairness |
| [[Test Cases - Bases and Upgrades]] | TC-BAS | Base ownership, module cost curves, module effects, plot expansion, shields and physical defences |
| [[Test Cases - Raiding]] | TC-RAID | Eligibility, offline protection, raid duration, egg theft and limit, animal theft and the three-animal limit, disconnects, defences |
| [[Test Cases - PvP]] | TC-PVP | Opt-in state, damage legality, penalties, fairness under latency |
| [[Test Cases - Bosses]] | TC-BOSS | Spawn cadence, announcements, phases, leash reset, contribution and rewards, progression gates, load |
| [[Test Cases - Multiplayer]] | TC-MP | Server capacity, sessions, shared combat, simultaneous interactions, replication and network conditions |
| [[Test Cases - Persistence]] | TC-PER | Save and load, DataStore failures, session locking, migration, Cash integrity, receipts, environment separation |
| [[Test Cases - Exploit Prevention]] | TC-EXP | Remote validation, probability tampering, ownership and duplication, combat and movement cheats, raid exploits, build hygiene |
| [[Test Cases - Mobile Performance]] | TC-MOB | Frame-time targets per scenario, soak, load time, bandwidth, mobile usability |

## Related documents

- [[Product Backlog]]
- [[Definition of Done]]
- [[Development Roadmap]]
- [[Risk Register]]
- [[Exploit Prevention]]
- [[Randomised Reward Compliance]]
- [[Performance Guidelines]]
- [[Template - Test Case]]
- [[Home]]
