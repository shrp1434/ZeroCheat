---
title: Scope and Launch Targets
type: vision
category: game-vision
status: mixed
priority: P0
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - vision
  - scope
  - launch
  - production
---

# Scope and Launch Targets

This page defines what ships at launch, what is explicitly out of scope, and what is held for live updates. Milestone sequencing is in [[Development Roadmap]]; delivery risks are in [[Risk Register]].

## 1. Launch content targets

| Area | Launch target | Status | Source |
|---|---|---|---|
| Animals | 60 species | **CONFIRMED** target (D-004) | [[Animal Index]] |
| Rarity split | 12 / 11 / 10 / 9 / 8 / 6 / 4 | **PROPOSED** (D-030) | [[Canonical Proposed Values#1. Rarity tiers]] |
| Rarities | 7 (Common → Secret) | **CONFIRMED** (D-003) | [[Egg Rarity System]] |
| Egg types | 7, one per rarity | **PROPOSED** | [[Common Egg]] … [[Secret Egg]] |
| Variants | Selected species; Golden, Diamond, Rainbow, Shadow, Neon as examples | Existence **CONFIRMED** (D-028); acquisition **UNDECIDED** ([[Open Questions#Q-006]]) | [[Animal Variants]] |
| World | Hub plus 8 regions in one shared world | Shared world **CONFIRMED** (D-025); layout **PROPOSED** (D-035), **UNDECIDED** ([[Open Questions#Q-001]]) | [[World Overview and Map]] |
| Mini-bosses | 8 (one per region) | Existence **CONFIRMED** (D-012); roster **PROPOSED** | [[Boss Design Overview]] |
| World bosses | 4 | Existence **CONFIRMED** (D-012); roster **PROPOSED** | [[Boss Design Overview]] |
| Base modules | 7 modules + Egg Merging Station + plot expansion | Modular bases **CONFIRMED** (D-022); availability **UNDECIDED** ([[Open Questions#Q-007]]) | [[Player Base System]] |
| Ascension | A1–A5 | **PROPOSED** (D-037), levels **UNDECIDED** ([[Open Questions#Q-004]]) | [[Ascension System]] |
| Egg merging | 5 station levels | Mechanic **CONFIRMED** (D-020); levels **PROPOSED** (D-038) | [[Egg Merging Station]] |
| Player level cap | 100 | **PROPOSED** | [[Player Progression and Levelling]] |
| PvP | Optional | **CONFIRMED** (D-023); activation **UNDECIDED** ([[Open Questions#Q-011]]) | [[PvP System]] |
| Raids | Optional | **CONFIRMED** (D-024); duration **UNDECIDED** ([[Open Questions#Q-012]]); egg limit **UNDECIDED** ([[Open Questions#Q-013]]) | [[Base Raiding System]] |

## 2. Technical launch targets (PROPOSED)

From [[Canonical Proposed Values#15. Server and performance targets (PROPOSED)]]:

| Target | Value |
|---|---|
| Players per server | 16 (**UNDECIDED**, [[Open Questions#Q-031]]) |
| Simulated wild animals per server | ≤ 180 |
| Wild animals with full AI near players | ≤ 60 |
| Companions per player | 3 |
| Frame rate | 60 FPS mid-range PC; 30 FPS minimum mid-range mobile |

Region-level budgets that make these numbers achievable are in each region document and in [[Animal Scalability and Performance Budgets]].

## 3. Scope classification (MoSCoW)

| Feature | Class | Status | Notes |
|---|---|---|---|
| Hybrid real-time combat (player + 3 animals) | Must | **CONFIRMED** | D-005, D-006 |
| Wild spawning and respawn | Must | **CONFIRMED** | D-011, [[Wild Animal Spawning and Respawn]] |
| Animal Index (discovered vs owned) | Must | **CONFIRMED** | D-029, [[Animal Index Feature Specification]] |
| Egg rolls, two-stage hatching, 5-at-once | Must | **CONFIRMED** | D-015, D-016 |
| Odds disclosure with version tokens | Must | Principle **CONFIRMED** (D-017); token **PROPOSED** (D-041) | [[Randomised Reward Compliance]] |
| Ascension | Must | **CONFIRMED** mechanic | D-019 |
| Egg merging and station | Must | **CONFIRMED** mechanic | D-020 |
| Egg storage 10 + 50 | Must | **CONFIRMED** | D-021 |
| Base lock on team changes | Must | **CONFIRMED** | D-010 |
| Modular base | Must | **CONFIRMED** | D-022 |
| Mini-bosses and world bosses | Must | **CONFIRMED** | D-012 |
| Optional PvP and raids | Must | **CONFIRMED** | D-023, D-024 |
| Storage expansion | Should | Purchasable **CONFIRMED**; currency and price **UNDECIDED** | [[Open Questions#Q-009]], [[Open Questions#Q-010]] |
| Variants | Should | **CONFIRMED** to exist | Acquisition **UNDECIDED** ([[Open Questions#Q-006]]) |
| Seasonal events | Could | **PROPOSED** | [[Seasonal and Limited-Time Events]] |
| Player-to-player trading | Won't (launch) | **PROPOSED** (D-045) | [[Open Questions#Q-026]] |
| Per-animal levelling | Won't (launch) | **PROPOSED** (D-042) | [[Open Questions#Q-021]] |
| Clans / guilds | Won't (launch) | **PROPOSED** | Not in the owner brief |
| Selling Cash for Robux | Won't | **PROPOSED** (D-044) | [[Open Questions#Q-032]] |

## 4. Content budget per region (PROPOSED)

| Region | Home species | Mini-boss | World boss present | Landmarks | Sub-zones |
|---|---:|---|---|---:|---:|
| [[Region - Whisperwood Forest]] | 16 | [[Mini-Boss - Bramblehorn]] | [[World Boss - Ironbark Colossus]] (border) | 4 | 4 |
| [[Region - Sunscorch Savanna]] | 11 | [[Mini-Boss - Dustmane]] | [[World Boss - Thunderhoof]] | 4 | 4 |
| [[Region - Emerald Canopy]] | 8 | [[Mini-Boss - Vinecoil]] | — | 4 | 4 |
| [[Region - Coral Coast]] | 5 | [[Mini-Boss - Hammertide]] | [[World Boss - Abyssal Leviathan]] | 4 | 4 |
| [[Region - Frostfang Tundra]] | 6 | [[Mini-Boss - Rimeback]] | — | 4 | 4 |
| [[Region - Skyreach Peaks]] | 5 | [[Mini-Boss - Stormtalon]] | [[World Boss - Ashwing Condor]] (rim) | 4 | 4 |
| [[Region - Emberheart Caldera]] | 4 | [[Mini-Boss - Cinderjaw]] | [[World Boss - Ashwing Condor]] (rim) | 4 | 4 |
| [[Region - Starfall Sanctuary]] | 5 | [[Mini-Boss - Eclipse Panther]] | — | 4 | 4 |
| **Total** | **60** | **8** | **4** | 32 | 32 |

Later regions have fewer home species; their wild populations are topped up with **PROPOSED** secondary appearances of earlier species (see each region document).

## 5. Expected playtime to milestones (PROPOSED, for planning only)

Derived from the XP curve `XP(L) = round(100 × L^1.6)` and the region multipliers in [[Canonical Proposed Values#5. Regions (PROPOSED — world layout is UNDECIDED, Q-001)]], assuming combat-only XP and roughly 6 seconds per wild defeat including travel. These numbers are rough planning inputs to be replaced by [[Balance Simulation Plan]] results.

| Milestone | Cumulative XP | Approximate active play |
|---|---:|---|
| Level 5 | 1,902 | 15–20 min |
| Level 8 (Savanna gate) | 7,223 | 60–75 min |
| Level 18 (Canopy gate) | 65,564 | 5–6 h |
| Level 28 (Coral gate) | 212,416 | 9–11 h |
| Level 40 (Tundra gate) | 544,664 | 14–17 h |
| Level 52 (Peaks gate) | 1,085,664 | 20–24 h |
| Level 65 (Caldera gate) | 1,949,231 | 27–32 h |
| Level 80 (Sanctuary gate) | 3,357,134 | 36–44 h |
| Level 100 (cap) | 6,016,706 | 55–70 h |

Collection completion (all 60 species, A5 favourites, variants) is designed to extend well beyond the level cap. See [[Long-Term Goals and Endgame]].

## 6. Post-launch expansion lanes

1. **New regions** attached to the ring, each with a mini-boss and 4–6 species ([[Content Expansion Guidelines]]).
2. **New species** in existing pools (with re-normalised, re-disclosed odds).
3. **Seasonal world bosses and events** ([[Seasonal and Limited-Time Events]]).
4. **Variants** once acquisition is decided ([[Open Questions#Q-006]]).
5. **New base modules** ([[Base Upgrade System]]).

## 7. Scope guardrails

- No feature ships that requires Robux to progress (D-027).
- No feature ships that lets a player lose something they could not see at risk beforehand ([[Design Principles and Fairness Charter]]).
- Any new system that touches odds must go through [[Randomised Reward Compliance]].
- Any feature outside this page needs an entry in [[Product Backlog]] and an owner decision.

## Related documents
- [[Game Vision Index]]
- [[Development Roadmap]]
- [[M22 - Launch]]
- [[Risk Register]]
- [[Product Backlog]]
- [[Progression Bottleneck Analysis]]
