---
title: Product Backlog
type: backlog
category: production
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - production
  - backlog
  - planning
  - epics
---

# Product Backlog

The prioritised list of work needed to build and launch *Fight Animals for Eggs*. Items are grouped into epics that follow the milestones in [[Development Roadmap]]. Every story has an ID, a priority, a milestone, its dependencies and acceptance criteria that point to test cases in [[QA and Testing Index]]. Every story is also subject to the [[Definition of Done]] for its work type.

> [!info] PROPOSED
> The backlog content, ordering and milestone placement are **PROPOSED** by production. The backlog contains **no dates or deadlines**; sequencing comes from priority and dependencies. Features that depend on an **UNDECIDED** item are built with configurable parameters and list the Q-ID under *Depends on*; they cannot be closed for launch until the question is decided or the owner waives it.

## Priority scale

| Priority | Name | Meaning |
|---|---|---|
| **P0** | Essential | Required for launch or for a confirmed rule; the game is not shippable without it |
| **P1** | High | Expected at launch; cutting it noticeably harms the experience |
| **P2** | Medium | Valuable; can slip to a post-launch update |
| **P3** | Low | Nice to have; candidate for live operations |

## Backlog rules

1. **IDs are permanent.** Stories use `BL-###`, epics `EP-##`. Removed items are marked *Cut* with a reason, never renumbered.
2. **One owner decision per blocked item.** If a story depends on a Q-ID, the Production Manager tracks the question in [[Open Questions]] and raises it at the owner review.
3. **Definition of Ready.** A story may start when: its design document exists in the vault; its values come from [[Canonical Proposed Values]] or are configurable; its dependencies are done or stubbed; its acceptance criteria and test cases are written; and art or audio needs are listed in the [[Asset Register]].
4. **Acceptance.** A story is accepted when its acceptance criteria pass and the [[Definition of Done]] for its work type is met. QA signs off P0 stories.
5. **New items** are written with [[Template - Task]] and added to the right epic.

## Epic overview

| Epic | Name | Milestone | Priority | Stories |
|---|---|---|---|---|
| EP-01 | Pre-production decisions and scope | [[M01 - Pre-production]] | P0 | BL-001 to BL-004 |
| EP-02 | Core project and platform services | [[M02 - Core Project Setup]] | P0 | BL-010 to BL-020 |
| EP-03 | Player movement and controls | [[M03 - Player Movement]] | P0 | BL-025 to BL-027 |
| EP-04 | Player combat | [[M04 - Player Combat]] | P0 | BL-030 to BL-036 |
| EP-05 | Animal AI and spawning | [[M05 - Animal AI]] | P0 | BL-040 to BL-045 |
| EP-06 | Animal combat, rewards and defeat | [[M06 - Animal Combat]] | P0 | BL-050 to BL-056 |
| EP-07 | Animal collection, team and index | [[M07 - Animal Collection]] | P0 | BL-060 to BL-065 |
| EP-08 | Egg rolling, luck and storage | [[M08 - Egg Rolling]] | P0 | BL-070 to BL-078 |
| EP-09 | Hatching | [[M09 - Hatching]] | P0 | BL-080 to BL-085 |
| EP-10 | Ascension | [[M10 - Ascension]] | P0 | BL-090 to BL-094 |
| EP-11 | Egg merging | [[M11 - Egg Merging]] | P0 | BL-100 to BL-104 |
| EP-12 | Player bases | [[M12 - Player Bases]] | P0 | BL-110 to BL-112 |
| EP-13 | Base upgrades and storage expansion | [[M13 - Base Upgrades]] | P0 | BL-115 to BL-120 |
| EP-14 | Base defence | [[M14 - Base Defence]] | P0 | BL-125 to BL-127 |
| EP-15 | Base raids and PvP | [[M15 - Base Raids]] | P0 | BL-130 to BL-138 |
| EP-16 | World and regions | [[M16 - World Design]] | P0 | BL-140 to BL-147 |
| EP-17 | Boss encounters | [[M17 - Boss Encounters]] | P1 | BL-150 to BL-154 |
| EP-18 | UI and UX | [[M18 - UI and UX]] | P0 | BL-160 to BL-166 |
| EP-19 | Content production: animals, art, animation, audio | Several (per story) | P0 | BL-170 to BL-179 |
| EP-20 | Multiplayer hardening | [[M19 - Multiplayer Testing]] | P0 | BL-180 to BL-182 |
| EP-21 | Optimisation | [[M20 - Optimisation]] | P0 | BL-185 to BL-187 |
| EP-22 | Beta | [[M21 - Beta Testing]] | P0 | BL-190 to BL-192 |
| EP-23 | Launch readiness and monetisation | [[M22 - Launch]] | P0 | BL-195 to BL-198 |
| EP-24 | Live operations | [[M23 - Live Updates]] | P2 | BL-200 to BL-203 |

## EP-01 Pre-production decisions and scope

Goal: remove prototype blockers and lock scope for the vertical slice.

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-001 | **Resolve prototype-blocking questions.** Get owner decisions or recorded working assumptions for Q-008, Q-011, Q-021, Q-023, Q-025, Q-028, Q-031, Q-033, Q-034. | P0 | [[M01 - Pre-production]] | — | Each question has a decision in the [[Decision Register]] or a working assumption noted in [[Open Questions]]; the [[Changelog]] records each change. |
| BL-002 | **Vertical slice definition.** One region, 6–8 animals, rolling, hatching, team at base, one mini-boss, base with two modules. | P0 | [[M01 - Pre-production]] | BL-001 | Scope written in [[Scope and Launch Targets]]; owner approves. |
| BL-003 | **Style test.** Three animals of different rarities modelled to the [[Art Bible]] and shown in-engine. | P1 | [[M01 - Pre-production]] | — | Approved by the art director against [[Animal Modelling Principles]] and [[Rarity Visual Language]]; meets the art-asset DoD. |
| BL-004 | **Risk review.** Initial [[Risk Register]] with owners for duplication, odds disclosure, data loss and mobile performance. | P1 | [[M01 - Pre-production]] | — | Each top risk has a mitigation and a linked test document. |

## EP-02 Core project and platform services

Goal: a secure, testable foundation every later feature builds on.

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-010 | **Project hierarchy and bootstrapping** per [[Roblox Project Hierarchy]] and [[Module Patterns and Bootstrapping]]. | P0 | [[M02 - Core Project Setup]] | — | Services start in a defined order; server-only modules not replicated (TC-EXP-041). |
| BL-011 | **Configuration modules** for every tunable, including all UNDECIDED parameters, with validation at boot. | P0 | [[M02 - Core Project Setup]] | BL-010 | Values match [[Canonical Proposed Values]]; invalid configuration disables the feature loudly (TC-EXP-029, TC-RAID-012). |
| BL-012 | **DataService**: load, save with `UpdateAsync`, session lock, retries, autosave, `BindToClose`. | P0 | [[M02 - Core Project Setup]] | BL-010 | TC-PER-001 to 014, 020, 021 pass. |
| BL-013 | **Profile schema v1 and migration framework** ([[Schema - Player Profile]] and related schemas). | P0 | [[M02 - Core Project Setup]] | BL-012 | TC-PER-030 to 032, 035 pass. |
| BL-014 | **Remote validation layer** and the [[Remote Communication Contract]]. | P0 | [[M02 - Core Project Setup]] | BL-010 | TC-EXP-001, 003, 005 pass. |
| BL-015 | **Rate limiting** per player and per remote. | P0 | [[M02 - Core Project Setup]] | BL-014 | TC-EXP-004 passes. |
| BL-016 | **Logging and analytics service** with event schema for rolls, hatches, merges, ascensions, thefts and saves. | P1 | [[M02 - Core Project Setup]] | BL-010 | Events documented in [[Service - AnalyticsAndLoggingService]]; TC-EXP-042 passes. |
| BL-017 | **QA hooks and invariant report**, present only in the QA build. | P0 | [[M02 - Core Project Setup]] | BL-010 | INV-01 to INV-12 computed on demand; TC-EXP-040 passes on staging. |
| BL-018 | **Injectable RNG and clock** for all random draws and timers. | P0 | [[M02 - Core Project Setup]] | BL-010 | Seeded runs reproduce exactly; production uses one unseeded server `Random`. |
| BL-019 | **Environments**: QA test experience and staging place with separate DataStores. | P0 | [[M02 - Core Project Setup]] | — | TC-PER-050 passes. |
| BL-020 | **Cash ledger** in EconomyService: integer Cash, ledger reasons, `MAX_CASH` clamp. | P0 | [[M02 - Core Project Setup]] | BL-012 | TC-PER-033, 034 and TC-EXP-027, 028 pass. |

## EP-03 Player movement and controls

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-025 | **Character movement and camera** per [[Camera Behaviour Guidelines]]. | P0 | [[M03 - Player Movement]] | BL-010 | Walk speed 16 studs/s; camera behaviour signed off by design. |
| BL-026 | **Server movement validation** (speed, teleport, locked regions). | P1 | [[M03 - Player Movement]] | BL-025 | TC-EXP-034, 035 pass. |
| BL-027 | **Touch, gamepad and keyboard input baseline** using ContextActionService. | P0 | [[M03 - Player Movement]] | BL-025 | TC-MOB-050 to 052 pass. |

## EP-04 Player combat

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-030 | **Damage pipeline** ([[Implementation - Combat Damage Pipeline]]). | P0 | [[M04 - Player Combat]] | BL-011, BL-018 | TC-CMB-001 to 008 pass. |
| BL-031 | **Basic three-hit combo** with cadence and reset. | P0 | [[M04 - Player Combat]] | BL-030 | TC-CMB-010 to 012 pass. |
| BL-032 | **Specials**: Power Strike, Ground Slam, Rally Cry with level unlocks and cooldowns. | P0 | [[M04 - Player Combat]] | BL-030 | TC-CMB-013 to 016, 018, 019 pass. |
| BL-033 | **Dodge roll.** | P1 | [[M04 - Player Combat]] | BL-025 | TC-CMB-017 passes. |
| BL-034 | **Player statistics and Strength** (HP, DEF, Strength, bonus hooks). | P0 | [[M04 - Player Combat]] | BL-030 | TC-CMB-020 to 023 pass. |
| BL-035 | **Combat state machine and combat tag.** | P0 | [[M04 - Player Combat]] | BL-030 | TC-CMB-050 to 053 pass. |
| BL-036 | **Combat feedback**: damage numbers, hit VFX and SFX, telegraphs. | P1 | [[M04 - Player Combat]] | BL-030 | TC-CMB-091 passes; [[Combat Feedback and Readability]] checklist met. |

## EP-05 Animal AI and spawning

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-040 | **AI state machine framework** ([[Implementation - Animal AI State Machine]]). | P0 | [[M05 - Animal AI]] | BL-018 | Illegal transitions logged; unit tests for every transition. |
| BL-041 | **Wild animal AI**: aggro, chase, attack, leash and reset. | P0 | [[M05 - Animal AI]] | BL-040, BL-030 | TC-AI-020 to 025 and TC-CMB-061 pass. |
| BL-042 | **SpawnService** with authored points and per-rarity respawn timers. | P0 | [[M05 - Animal AI]] | BL-040 | TC-AI-030, 031, 039 to 041 pass. |
| BL-043 | **Rare-spawn windows and server announcements** for Legendary, Mythical and Secret. | P1 | [[M05 - Animal AI]] | BL-042 | TC-AI-032 to 038 pass. |
| BL-044 | **AI level of detail and server budgets.** | P0 | [[M05 - Animal AI]] | BL-041 | TC-AI-041, 060 to 062 pass. |
| BL-045 | **Companion follow and stuck recovery.** | P0 | [[M05 - Animal AI]] | BL-040 | TC-AI-001, 002, 009 pass. |

## EP-06 Animal combat, rewards and defeat

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-050 | **Companion auto-targeting.** | P0 | [[M06 - Animal Combat]] | BL-045 | TC-CMB-040, TC-AI-003, 005, 006 pass. |
| BL-051 | **Manual target commands** on PC and touch. | P0 | [[M06 - Animal Combat]] | BL-050 | TC-CMB-041 to 045, TC-AI-004 pass. |
| BL-052 | **Ability framework**: manual and automatic, cooldowns, global cooldown. | P0 | [[M06 - Animal Combat]] | BL-030 | TC-CMB-030 to 036 pass. |
| BL-053 | **Launch ability set** for every role archetype in [[Animal Abilities Catalogue]]. | P0 | [[M06 - Animal Combat]] | BL-052 | Each ability implemented from data; balance review per [[Balancing Methodology]]. |
| BL-054 | **Combat rewards and shared kill credit** (≥ 10%, D-040). | P0 | [[M06 - Animal Combat]] | BL-020, BL-041 | TC-CMB-063 to 070, TC-MP-010 to 012 pass. |
| BL-055 | **Defeat framework** configurable per battle type. | P0 | [[M06 - Animal Combat]] | BL-035; Q-014 | TC-CMB-080 to 083 pass with placeholder rows; final values blocked by Q-014. |
| BL-056 | **Index registration on defeat** (discovered vs owned). | P0 | [[M06 - Animal Combat]] | BL-041 | TC-CMB-069, TC-EXP-014 pass. |

## EP-07 Animal collection, team and index

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-060 | **Animal collection model** with unique instance IDs ([[Schema - Animal Collection]]). | P0 | [[M07 - Animal Collection]] | BL-013 | TC-INV-041 passes. |
| BL-061 | **Team equipping and base lock** (exactly three; only at own base). | P0 | [[M07 - Animal Collection]] | BL-060, BL-111 | TC-INV-060 to 062, 064 to 074, TC-EXP-020, 021 pass. |
| BL-062 | **Animal index** feature and screen. | P0 | [[M07 - Animal Collection]] | BL-056 | TC-INV-043 passes; [[Animal Index Feature Specification]] met. |
| BL-063 | **Animal inventory UI** with sort and filter. | P1 | [[M07 - Animal Collection]] | BL-060 | TC-INV-042, TC-MOB-022 pass. |
| BL-064 | **Owned-animal capacity** as configuration. | P1 | [[M07 - Animal Collection]] | BL-060; Q-022 | TC-INV-040 passes with the working assumption. |
| BL-065 | **Starter animals and fewer-than-three rule** for onboarding. | P0 | [[M07 - Animal Collection]] | BL-061; Q-1002 | [[New Player Onboarding]] flow playable; TC-INV-063 passes for the decided rule. |

## EP-08 Egg rolling, luck and storage

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-070 | **LuckService** pure functions and Progression Score. | P0 | [[M08 - Egg Rolling]] | BL-011 | Exact values in [[Statistical Testing of Probabilities]] §2 reproduced; TC-EGG-022 to 025, 035 pass. |
| BL-071 | **Weighted selection** with exact boundaries. | P0 | [[M08 - Egg Rolling]] | BL-018 | TC-EGG-036 passes. |
| BL-072 | **Roll transaction** (single and ×5) in EggService. | P0 | [[M08 - Egg Rolling]] | BL-020, BL-070, BL-071, BL-075 | TC-EGG-001 to 011, 014 pass. |
| BL-073 | **`oddsVersion` tokens** (D-041). | P0 | [[M08 - Egg Rolling]] | BL-070 | TC-EGG-026 to 029, TC-EXP-011 pass. |
| BL-074 | **Odds disclosure UI** ([[UI - Egg Rolling]]). | P0 | [[M08 - Egg Rolling]] | BL-073 | TC-EGG-021, 027, 031, 032 and TC-MOB-053 pass. |
| BL-075 | **Egg storage** containers and transfers ([[Egg Storage]]). | P0 | [[M08 - Egg Rolling]] | BL-013 | TC-INV-001 to 009 pass. |
| BL-076 | **Statistical harness and egg-rarity gate.** | P0 | [[M08 - Egg Rolling]] | BL-071, BL-072 | TC-EGG-037 to 042 pass with logged seeds. |
| BL-077 | **Egg roll presentation**: shrine interaction, [[Animation - Egg Roll]], [[Sound - Eggs]]. | P1 | [[M08 - Egg Rolling]] | BL-072 | Animation and sound DoD met; TC-MOB-006 passes. |
| BL-078 | **Compliance review of disclosure** against [[Randomised Reward Compliance]] and [[Roblox Monetisation Policy Requirements]]. | P0 | [[M08 - Egg Rolling]] | BL-074; Q-032 | Written sign-off; TC-EGG-014 passes. |

## EP-09 Hatching

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-080 | **HatchService**: one to five eggs, pool selection, validation. | P0 | [[M09 - Hatching]] | BL-070, BL-071, BL-060 | TC-EGG-046, 049 to 053, 063 to 065, 068 pass. |
| BL-081 | **Hatch odds display and token.** | P0 | [[M09 - Hatching]] | BL-073 | TC-EGG-047, 048 pass. |
| BL-082 | **Hatch location rules.** | P1 | [[M09 - Hatching]] | BL-080, BL-035; Q-023 | TC-EGG-059 to 062 pass. |
| BL-083 | **Hatch presentation**: single and multi-hatch, skippable ([[Animation - Egg Hatch]], [[UI - Egg Hatching]]). | P1 | [[M09 - Hatching]] | BL-080 | TC-EGG-066, TC-MOB-005 pass. |
| BL-084 | **Independence and ownership-bias gate.** | P0 | [[M09 - Hatching]] | BL-080, BL-076 | TC-EGG-054 to 058 pass. |
| BL-085 | **Seven egg models** (EGG-##) per [[Egg Art Direction]]. | P1 | [[M09 - Hatching]] | BL-003 | Art-asset DoD met for each. |

## EP-10 Ascension

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-090 | **Ascension transaction** ([[Implementation - Ascension Transaction]]). | P0 | [[M10 - Ascension]] | BL-060, BL-020 | TC-ASC-001 to 013, 040 to 043 pass. |
| BL-091 | **Stat and ability scaling** per level. | P0 | [[M10 - Ascension]] | BL-090 | TC-ASC-030 to 032, TC-CMB-035 pass. |
| BL-092 | **Ascension visual tiers A1–A5** and [[Animation - Ascension]]. | P1 | [[M10 - Ascension]] | BL-090 | TC-ASC-033, TC-MOB-008 pass. |
| BL-093 | **Ascension UI** ([[UI - Ascension]]). | P1 | [[M10 - Ascension]] | BL-090 | TC-ASC-044 passes. |
| BL-094 | **Equipped, defending and variant rules** for ascension. | P1 | [[M10 - Ascension]] | BL-090; Q-1005, Q-1006, Q-006 | TC-ASC-020 to 025 pass for the decided rules. |

## EP-11 Egg merging

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-100 | **Merge transaction** ([[Implementation - Egg Merge Transaction]]). | P0 | [[M11 - Egg Merging]] | BL-075, BL-101 | TC-MRG-010 to 028, 030, 033 to 035 pass. |
| BL-101 | **Egg Merging Station** purchase, sequential upgrades and gates. | P0 | [[M11 - Egg Merging]] | BL-115 | TC-MRG-001 to 007, 009 pass. |
| BL-102 | **Station models L1–L5** with visible change per upgrade. | P0 | [[M11 - Egg Merging]] | BL-101 | TC-MRG-008 passes; art-asset DoD met for all five. |
| BL-103 | **Merge UI** ([[UI - Egg Merging]]). | P1 | [[M11 - Egg Merging]] | BL-100 | TC-MRG-017, 018, 027 UI steps pass. |
| BL-104 | **Merge animations by tier** ([[Animation - Egg Merge]]). | P2 | [[M11 - Egg Merging]] | BL-100; Q-034 | TC-MRG-032, TC-MOB-007 pass. |

## EP-12 Player bases

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-110 | **Plot allocation and base lifecycle** (join, leave, 16 bases). | P0 | [[M12 - Player Bases]] | BL-012 | TC-BAS-001 to 004, 006 pass. |
| BL-111 | **Base boundary detection** used by the team rule. | P0 | [[M12 - Player Bases]] | BL-110 | TC-BAS-005 passes. |
| BL-112 | **Base management UI** ([[UI - Base Management]]). | P1 | [[M12 - Player Bases]] | BL-110 | UI DoD met. |

## EP-13 Base upgrades and storage expansion

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-115 | **Module framework and cost curves.** | P0 | [[M13 - Base Upgrades]] | BL-110, BL-020; Q-007 | TC-BAS-010 to 021 pass. |
| BL-116 | **Module effects**: Training Grounds, Multiplier Shrine, Trophy Hall, base progression in PS. | P1 | [[M13 - Base Upgrades]] | BL-115, BL-070 | TC-BAS-030 to 035, TC-CMB-024 pass. |
| BL-117 | **Plot expansion** and module slots. | P1 | [[M13 - Base Upgrades]] | BL-115 | TC-BAS-040 to 043 pass. |
| BL-118 | **Storage expansion purchases** with configurable currency and price. | P1 | [[M13 - Base Upgrades]] | BL-075; Q-009, Q-010 | TC-INV-020 to 028 pass; launch blocked until Q-009 and Q-010 are decided. |
| BL-119 | **Module models L1–L5** (MOD-##) per [[Base Art Direction]] and [[Animation - Base Upgrades]]. | P1 | [[M13 - Base Upgrades]] | BL-115 | TC-BAS-019 passes; art and animation DoD met. |
| BL-120 | **Animal Pens** including the display decision. | P2 | [[M13 - Base Upgrades]] | BL-115; Q-008 | TC-BAS-036, TC-MOB-030 pass. |

## EP-14 Base defence

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-125 | **Shield Generator and shield state.** | P0 | [[M14 - Base Defence]] | BL-115; Q-030 | TC-BAS-050 to 052 pass; [[Animation - Shield Activation]] DoD met. |
| BL-126 | **Defence Station** traps and turrets. | P1 | [[M14 - Base Defence]] | BL-115 | TC-BAS-053, 054, TC-AI-055 pass. |
| BL-127 | **Guard AI** for defending animals. | P0 | [[M14 - Base Defence]] | BL-040; Q-033, Q-035 | TC-AI-050 to 054 pass. |

## EP-15 Base raids and PvP

PvP placement in this milestone is **PROPOSED**; it shares combat legality and opt-in infrastructure with raids.

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-130 | **Raid eligibility and offline protection.** | P0 | [[M15 - Base Raids]] | BL-110, BL-125; Q-029, Q-1008 | TC-RAID-001 to 008, TC-EXP-053 pass. |
| BL-131 | **Raid session controller** with configurable `T_raid` ([[Implementation - Raid Session Controller]]). | P0 | [[M15 - Base Raids]] | BL-130, BL-018; Q-012 | TC-RAID-010 to 016 pass; launch blocked until Q-012 is decided. |
| BL-132 | **Egg theft** with configurable `L_egg`; backpack eggs never exposed. | P0 | [[M15 - Base Raids]] | BL-131, BL-075; Q-013, Q-1007 | TC-RAID-020 to 027, TC-EXP-050, 054 pass; launch blocked until Q-013 is decided. |
| BL-133 | **Animal theft** of knocked-out defenders, maximum three per raid. | P0 | [[M15 - Base Raids]] | BL-131, BL-127; Q-025 | TC-RAID-030 to 039, TC-EXP-051, 052 pass. |
| BL-134 | **Cross-profile transfer log** for theft settlement. | P0 | [[M15 - Base Raids]] | BL-012 | TC-RAID-044, TC-PER-042 pass. |
| BL-135 | **Raid disconnection handling** (attacker, defender, both, shutdown, rejoin). | P0 | [[M15 - Base Raids]] | BL-131, BL-134; Q-1009 | TC-RAID-040 to 047 pass. |
| BL-136 | **Raid UI, alerts and summary** ([[UI - Raid Interface]], [[Sound - Base and Raid Alerts]]). | P1 | [[M15 - Base Raids]] | BL-131 | TC-RAID-013 to 015 pass. |
| BL-137 | **PvP state and damage legality** with configurable activation. | P1 | [[M15 - Base Raids]] | BL-030, BL-050; Q-011 | TC-PVP-001 to 031 pass for the decided activation method. |
| BL-138 | **Raid rewards and defender compensation.** | P2 | [[M15 - Base Raids]] | BL-131 | TC-RAID-054 passes per [[Raid Rewards and Defender Compensation]]. |

## EP-16 World and regions

Region list and layout are **PROPOSED** (D-035, Q-001).

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-140 | **Hub** ([[Hub - Hatchling Haven]]): shrine, portals, safe zone. | P0 | [[M16 - World Design]] | BL-025 | TC-CMB-052, TC-PVP-014 pass; environment DoD met. |
| BL-141 | **Regions 1–2** (Whisperwood Forest, Sunscorch Savanna). | P0 | [[M16 - World Design]] | BL-042 | Spawn tables, routes and art pass review; TC-MOB-004 passes for these regions. |
| BL-142 | **Regions 3–4** (Emerald Canopy, Coral Coast). | P0 | [[M16 - World Design]] | BL-141 | As BL-141. |
| BL-143 | **Regions 5–6** (Frostfang Tundra, Skyreach Peaks). | P1 | [[M16 - World Design]] | BL-142 | As BL-141. |
| BL-144 | **Regions 7–8** (Emberheart Caldera, Starfall Sanctuary). | P1 | [[M16 - World Design]] | BL-143 | As BL-141; TC-BOSS-032 passes. |
| BL-145 | **Region unlock gates** ([[Region Unlock Progression]]). | P0 | [[M16 - World Design]] | BL-141, BL-150 | TC-BOSS-030, 032, TC-EXP-035 pass. |
| BL-146 | **Environmental hazards** ([[Environmental Hazards]]). | P2 | [[M16 - World Design]] | BL-141 | Hazards readable and fair; no damage in the hub. |
| BL-147 | **Spawn tables per region** for all 60 species. | P0 | [[M16 - World Design]] | BL-042; Q-002 | Every species spawns in its home region; TC-AI-042 passes on final tables. |

## EP-17 Boss encounters

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-150 | **Boss framework**: phases, telegraphs, leash reset, contribution ([[Boss AI]]). | P0 | [[M17 - Boss Encounters]] | BL-040, BL-054 | TC-BOSS-010 to 015, 020 pass. |
| BL-151 | **Eight mini-bosses.** | P1 | [[M17 - Boss Encounters]] | BL-150 | TC-BOSS-001, 030, 031 pass for each; boss art and animation DoD met. |
| BL-152 | **Four world bosses** with cadence and announcements. | P1 | [[M17 - Boss Encounters]] | BL-150 | TC-BOSS-002 to 005, 040, TC-MOB-012 pass. |
| BL-153 | **Boss rewards** as configuration. | P1 | [[M17 - Boss Encounters]] | BL-150; Q-015 | TC-BOSS-021 to 023 pass; launch blocked until Q-015 is decided. |
| BL-154 | **Boss health bar** ([[UI - Boss Health Bar]]). | P1 | [[M17 - Boss Encounters]] | BL-150 | TC-BOSS-041 passes. |

## EP-18 UI and UX

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-160 | **UI design system** components ([[UI Design System]], [[UI Visual Styling]]). | P0 | [[M18 - UI and UX]] | — | Components documented and reused by every screen. |
| BL-161 | **Main HUD** with team display and Strength display. | P0 | [[M18 - UI and UX]] | BL-160 | [[UI - Main HUD]], [[UI - Animal Team Display]], [[UI - Player Strength Display]] specs met; TC-MOB-050 passes. |
| BL-162 | **Notifications** for rare spawns, bosses and raids. | P1 | [[M18 - UI and UX]] | BL-160 | TC-AI-035, TC-BOSS-003, TC-RAID-014 pass. |
| BL-163 | **Settings** including graphics quality and audio groups ([[UI - Settings]]). | P1 | [[M18 - UI and UX]] | BL-160 | Settings persist; low-quality mode used in TC-MOB captures. |
| BL-164 | **Accessibility pass** against [[UI Accessibility Standards]]. | P1 | [[M18 - UI and UX]] | BL-161 | TC-MOB-051 to 054, TC-PVP-005 pass. |
| BL-165 | **New player onboarding** ([[New Player Onboarding]]). | P0 | [[M18 - UI and UX]] | BL-065, BL-072, BL-080 | A new tester completes roll, hatch, equip and first fight unaided in playtest. |
| BL-166 | **Progression interface** ([[UI - Progression Interface]]). | P2 | [[M18 - UI and UX]] | BL-070 | Shows level and unlocks; does not reveal the hidden luck formula (TC-EGG-033). |

## EP-19 Content production: animals, art, animation, audio

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-170 | **Common and Uncommon animal models** (23, ANM-001 to ANM-023). | P0 | [[M07 - Animal Collection]] | BL-003; Q-002 | Art-asset DoD met for each; registered in [[Asset Register]]. |
| BL-171 | **Rare and Epic animal models** (19, ANM-024 to ANM-042). | P0 | [[M09 - Hatching]] | BL-170 | As BL-170. |
| BL-172 | **Legendary, Mythical and Secret animal models** (18, ANM-043 to ANM-060). | P0 | [[M16 - World Design]] | BL-171; Q-027 | As BL-170. |
| BL-173 | **Rigs and locomotion** per [[Animal Rig Standards]] and [[Animation - Animal Locomotion]]. | P0 | [[M05 - Animal AI]] | BL-170 | Animation DoD met per rig family. |
| BL-174 | **Attacks, hit reactions, defeat and victory animations.** | P0 | [[M06 - Animal Combat]] | BL-173 | Animation DoD met; TC-CMB-091 passes. |
| BL-175 | **Ability animations and VFX** ([[Animation - Animal Abilities]], [[VFX - Combat Effects]]). | P1 | [[M06 - Animal Combat]] | BL-053 | Animation and VFX DoD met; TC-MOB-002 passes. |
| BL-176 | **Rarity and ascension VFX** ([[VFX - Rarity and Variant Effects]]). | P1 | [[M10 - Ascension]] | BL-092 | TC-MOB-008 passes. |
| BL-177 | **Variant material sets** (VAR-###). | P2 | [[M16 - World Design]] | Q-006, Q-024 | Art-asset DoD met; eligibility per [[Animal Variants]]. |
| BL-178 | **Core sound set**: vocalisations, combat impacts, eggs, UI ([[Sound Bible]]). | P1 | [[M18 - UI and UX]] | BL-174 | Sound DoD met; mix per [[Audio Mixing and Priority]]. |
| BL-179 | **Music** per [[Music Direction]]. | P2 | [[M18 - UI and UX]] | — | Sound DoD met for each track. |

## EP-20 Multiplayer hardening

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-180 | **Full-server sessions and replication budgets.** | P0 | [[M19 - Multiplayer Testing]] | All gameplay epics | TC-MP-001 to 007, 030 to 035 pass. |
| BL-181 | **Concurrency safety** for shared items (commit ordering, reservations). | P0 | [[M19 - Multiplayer Testing]] | BL-100, BL-132, BL-133 | TC-MP-020 to 024, TC-EGG-068, TC-MRG-028 pass. |
| BL-182 | **Latency handling** for combat and PvP. | P1 | [[M19 - Multiplayer Testing]] | BL-030 | TC-CMB-090, TC-PVP-030, 031 pass. |

## EP-21 Optimisation

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-185 | **Mobile performance pass.** | P0 | [[M20 - Optimisation]] | BL-180 | All P0 and P1 cases in [[Test Cases - Mobile Performance]] pass on the reference tiers (Q-1010). |
| BL-186 | **Streaming and memory budgets.** | P0 | [[M20 - Optimisation]] | BL-141 | TC-MOB-004, 040 pass. |
| BL-187 | **Server heartbeat budget.** | P0 | [[M20 - Optimisation]] | BL-044 | TC-MOB-045, TC-AI-060 pass. |

## EP-22 Beta

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-190 | **Beta programme** and feedback intake ([[Bug Reporting and Severity]] §7). | P0 | [[M21 - Beta Testing]] | BL-185 | Testers onboarded; reports triaged. |
| BL-191 | **Telemetry dashboards** for observed odds by `oddsVersion`, Cash flow and raid outcomes. | P0 | [[M21 - Beta Testing]] | BL-016 | Live odds check in [[Statistical Testing of Probabilities]] §5.1 runs on beta data. |
| BL-192 | **Balance simulation and tuning** per [[Balance Simulation Plan]]. | P1 | [[M21 - Beta Testing]] | BL-191 | Tuning changes follow [[Balance Update Process]]. |

## EP-23 Launch readiness and monetisation

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-195 | **Monetisation products** consistent with [[Monetisation Principles]] (no essential progression behind purchases). | P1 | [[M22 - Launch]] | BL-012; Q-032 | TC-PER-040, 041, TC-INV-026 pass; owner approves the product list. |
| BL-196 | **Compliance checklist** for paid random items and odds disclosure (`PolicyService` checks if any paid random item exists). | P0 | [[M22 - Launch]] | BL-078, BL-195 | Checklist in [[Roblox Monetisation Policy Requirements]] complete. |
| BL-197 | **Release regression and statistical gate.** | P0 | [[M22 - Launch]] | All P0 stories | Gates in [[QA Strategy]] §8 met. |
| BL-198 | **All beta- and launch-blocking questions decided** (including Q-009, Q-010, Q-012, Q-013, Q-014, Q-015, Q-016 to Q-019). | P0 | [[M22 - Launch]] | — | Each decided in the [[Decision Register]] or waived by the owner in writing. |

## EP-24 Live operations

| ID | Story | Priority | Milestone | Depends on | Acceptance criteria |
|---|---|---|---|---|---|
| BL-200 | **Content update pipeline** ([[Content Update Pipeline]]). | P1 | [[M23 - Live Updates]] | BL-197 | A test content drop goes through every pipeline stage to staging with its checklist complete and the regression subset passing. |
| BL-201 | **Balance update process with statistical gate** ([[Balance Update Process]]). | P1 | [[M23 - Live Updates]] | BL-076 | Any odds change passes the release gate before deployment. |
| BL-202 | **Seasonal and limited-time events framework** ([[Seasonal and Limited-Time Events]]). | P3 | [[M23 - Live Updates]] | BL-200 | Event content follows [[Content Expansion Guidelines]]. |
| BL-203 | **Versioning and changelog** for player-facing updates ([[Versioning and Changelog Policy]]). | P2 | [[M23 - Live Updates]] | BL-200 | Each release has version notes. |

## Parking lot (not in the backlog)

| Item | Reason |
|---|---|
| Player-to-player trading | Out of scope at launch (**PROPOSED** D-045, Q-026) |
| Per-animal levelling | Not planned (**PROPOSED** D-042, Q-021) |
| Timed incubation and timed merges | Alternatives to the proposals under Q-023 and Q-034 |

## Summary by priority

| Priority | Stories |
|---|---:|
| P0 | 86 |
| P1 | 42 |
| P2 | 8 |
| P3 | 1 |
| **Total** | **137** |

## Related documents

- [[Backlog Index]]
- [[Definition of Done]]
- [[Development Roadmap]]
- [[Risk Register]]
- [[QA and Testing Index]]
- [[Test Plan Matrix]]
- [[Open Questions]]
- [[Decision Register]]
- [[Template - Task]]
