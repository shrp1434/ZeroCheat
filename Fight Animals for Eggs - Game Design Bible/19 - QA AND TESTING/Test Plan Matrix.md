---
title: Test Plan Matrix
type: qa
category: qa
status: proposed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-plan
  - traceability
  - coverage
---

# Test Plan Matrix

The coverage map for QA: which systems are tested at which level, which test-case documents gate which milestone, how confirmed decisions trace to test cases, and where every mandatory edge case and every **UNDECIDED** parameter is covered. Levels L1–L8 are defined in [[QA Strategy]].

> [!info] PROPOSED
> The matrix is a **PROPOSED** plan. Case counts are as written on 2026-11-14 and are updated whenever a test-case document changes.

## 1. Test-case documents

| Document | ID prefix | Cases | P0 | P1 | P2 | P3 |
|---|---|---:|---:|---:|---:|---:|
| [[Test Cases - Combat]] | TC-CMB | 57 | 20 | 31 | 6 | 0 |
| [[Test Cases - Animal AI]] | TC-AI | 38 | 16 | 15 | 7 | 0 |
| [[Test Cases - Egg Rolls and Hatching]] | TC-EGG | 60 | 42 | 12 | 5 | 1 |
| [[Test Cases - Inventory and Storage]] | TC-INV | 37 | 26 | 9 | 2 | 0 |
| [[Test Cases - Ascension]] | TC-ASC | 29 | 15 | 11 | 3 | 0 |
| [[Test Cases - Egg Merging]] | TC-MRG | 34 | 21 | 9 | 4 | 0 |
| [[Test Cases - Bases and Upgrades]] | TC-BAS | 34 | 10 | 20 | 4 | 0 |
| [[Test Cases - Raiding]] | TC-RAID | 49 | 34 | 13 | 2 | 0 |
| [[Test Cases - PvP]] | TC-PVP | 19 | 9 | 9 | 1 | 0 |
| [[Test Cases - Bosses]] | TC-BOSS | 23 | 5 | 12 | 6 | 0 |
| [[Test Cases - Multiplayer]] | TC-MP | 22 | 11 | 10 | 1 | 0 |
| [[Test Cases - Persistence]] | TC-PER | 27 | 21 | 5 | 1 | 0 |
| [[Test Cases - Exploit Prevention]] | TC-EXP | 39 | 32 | 7 | 0 | 0 |
| [[Test Cases - Mobile Performance]] | TC-MOB | 28 | 12 | 12 | 4 | 0 |
| **Total** | | **496** | **274** | **175** | **46** | **1** |

By type: functional 195, edge 137, security 75, performance 36, negative 35, statistical 18.

## 2. System × test level

✓ = primary coverage at that level; ○ = secondary or sampled; — = not applicable.

| System | L1 Unit | L2 Integration | L3 Statistical | L4 Multi-client | L5 Playtest | L6 Soak/load | L7 Device | L8 Live |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Damage and player combat | ✓ | ✓ | ○ | ✓ | ✓ | ○ | ✓ | ○ |
| Animal abilities and targeting | ✓ | ✓ | — | ✓ | ✓ | ○ | ✓ | — |
| Wild AI, spawning, rare spawns | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ |
| Egg rolls and odds disclosure | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ |
| Dynamic progression luck | ✓ | ✓ | ✓ | ○ | ○ | — | — | ✓ |
| Hatching and independence | ✓ | ✓ | ✓ | ✓ | ✓ | ○ | ✓ | ✓ |
| Egg storage and expansion | ✓ | ✓ | — | ✓ | ✓ | — | ○ | ○ |
| Team equipping and base lock | ✓ | ✓ | — | ✓ | ✓ | — | ○ | ○ |
| Ascension | ✓ | ✓ | — | ✓ | ✓ | — | ○ | ○ |
| Egg merging and station | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ | ○ |
| Bases, modules, plot expansion | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | — |
| Raids, theft, offline protection | ✓ | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| PvP | ✓ | ✓ | — | ✓ | ✓ | ○ | ✓ | ○ |
| Bosses | ✓ | ✓ | ○ | ✓ | ✓ | ✓ | ✓ | ○ |
| Multiplayer sessions and replication | — | ✓ | — | ✓ | ✓ | ✓ | ✓ | ✓ |
| Persistence | ✓ | ✓ | — | ✓ | ○ | ✓ | — | ✓ |
| Exploit prevention | ✓ | ✓ | — | ✓ | — | ○ | — | ✓ |
| Mobile performance | — | — | — | ○ | ✓ | ✓ | ✓ | ✓ |

## 3. Milestone gates

A milestone exits only when the listed documents pass their gate (100% P0, ≥ 95% P1; see [[QA Strategy]] §8). Milestones are defined in [[Development Roadmap]].

| Milestone | Gating test documents | Statistical gate |
|---|---|---|
| [[M02 - Core Project Setup]] | Persistence (TC-PER-001 to 014, 020, 021, 050), Exploit Prevention §1 and TC-EXP-040 | — |
| [[M03 - Player Movement]] | TC-EXP-034, TC-MOB-050 to 052 | — |
| [[M04 - Player Combat]] | Combat §1–§3, §6 | Damage roll range (TC-CMB-003) |
| [[M05 - Animal AI]] | Animal AI §1–§3, §5 | Rare-spawn chances (TC-AI-032 to 034), luck independence of spawns (TC-AI-042) |
| [[M06 - Animal Combat]] | Combat §4, §5, §7, §8; Animal AI §1 | — |
| [[M07 - Animal Collection]] | Inventory §3, §4 | — |
| [[M08 - Egg Rolling]] | Egg Rolls §1–§3; Inventory §1 | Full egg-rarity gate |
| [[M09 - Hatching]] | Egg Rolls §4 | Hatch-pool, independence and ownership-bias gates |
| [[M10 - Ascension]] | Ascension (all) | — |
| [[M11 - Egg Merging]] | Egg Merging (all) | Merged-egg equivalence (TC-MRG-031) |
| [[M12 - Player Bases]] | Bases §1 | — |
| [[M13 - Base Upgrades]] | Bases §2–§4; Inventory §2 | — |
| [[M14 - Base Defence]] | Bases §5; Animal AI §4 | — |
| [[M15 - Base Raids]] | Raiding (all); PvP (all); Exploit Prevention §5 | — |
| [[M16 - World Design]] | Animal AI §3; TC-BOSS-030, 032; TC-MOB-004 | Rare spawns re-run on final spawn tables |
| [[M17 - Boss Encounters]] | Bosses (all) | — |
| [[M18 - UI and UX]] | All UI-facing cases; TC-MOB-020 to 023, 050 to 054 | — |
| [[M19 - Multiplayer Testing]] | Multiplayer (all); Raiding §5; Persistence (all) | — |
| [[M20 - Optimisation]] | Mobile Performance (all); TC-AI-060 to 062 | — |
| [[M21 - Beta Testing]] | Full regression | Full release gate ([[Statistical Testing of Probabilities]] §8) |
| [[M22 - Launch]] | Full regression; Exploit Prevention (all) | Full release gate |
| [[M23 - Live Updates]] | Regression subset for touched systems | Release gate if any odds, pool or luck value changed |

## 4. Decision traceability

| Decision | Rule (short) | Primary test cases |
|---|---|---|
| D-005 | Real-time hybrid combat, specials with cooldowns | TC-CMB-001 to 019, 090, 091 |
| D-006 | Team of exactly three | TC-INV-060 to 063, 069, 070; TC-AI-001 |
| D-007 | Player Strength separate | TC-CMB-020 to 024; TC-ASC-034 |
| D-008 | Manual and automatic abilities | TC-CMB-030 to 036 |
| D-009 | Auto-target and manual commands | TC-CMB-040 to 045; TC-AI-003, 004 |
| D-010 | Team changes only at own base | TC-INV-064 to 068, 072; TC-EXP-021; TC-ASC-020 to 022 |
| D-011 | Wild respawn, rarer is slower | TC-AI-030 to 041 |
| D-012 | Bosses exist | TC-BOSS-001 to 041 |
| D-013 | Mixed defeat penalties (values **UNDECIDED**) | TC-CMB-080 to 083; TC-PVP-020; TC-RAID-052, 053; TC-BOSS-024 |
| D-014 | Cash from wild animals buys rolls | TC-EGG-001 to 006; TC-CMB-063 to 070; TC-PER-033, 034 |
| D-015 | Two-stage randomness | TC-EGG-011, 036, 046, 053 |
| D-016 | Up to five eggs hatched at once | TC-EGG-049 to 052, 057 |
| D-017 | Luck on eggs only; odds disclosed; no silent change | TC-EGG-012, 021 to 035, 047; TC-AI-042; TC-EXP-010 |
| D-018 | Independent hatches | TC-EGG-040, 041, 054 to 057; TC-MRG-031 |
| D-019 | Ascension consumes duplicates, keeps original | TC-ASC-001 to 044 |
| D-020 | Merging 3 → 1, station required and upgraded | TC-MRG-001 to 035 |
| D-021 | Storage 10 + 50; backpack never stolen; expansion | TC-INV-001 to 028; TC-RAID-021; TC-EGG-006 |
| D-022 | Modular base, separate upgrades | TC-BAS-001 to 043 |
| D-023 | Optional PvP | TC-PVP-001 to 016; TC-EXP-030 |
| D-024 | Optional raids; theft rules; three-animal limit; offline protection | TC-RAID-001 to 062; TC-EXP-050 to 057; TC-MP-020 to 022 |
| D-025 | Shared world, solo and multiplayer | TC-MP-001 to 035; TC-PER-003 to 021 |
| D-027 | Fully playable without Robux | TC-INV-026; TC-EGG-014; TC-PER-040, 041 |
| D-029 | Index: discovered versus owned | TC-CMB-069; TC-EGG-067; TC-EXP-014 |
| D-041 (PROPOSED) | `oddsVersion` tokens | TC-EGG-026 to 029, 048; TC-EXP-011 |

## 5. Mandatory edge cases

| Edge case | Test case | Expected result (summary) |
|---|---|---|
| Hatching six eggs | TC-EGG-050 | UI stops at five; crafted request rejected entirely; no egg consumed |
| No available egg capacity | TC-EGG-006, TC-EGG-008 | Roll refused before payment; nothing created or discarded |
| Merging eggs of different rarities | TC-MRG-018 | Rejected; nothing consumed; no fee |
| Stealing backpack eggs | TC-RAID-021, TC-EXP-050 | No prompt; IDs not replicated; crafted request rejected |
| Stealing a defending animal that was not defeated | TC-RAID-031, TC-EXP-051 | Rejected `not_knocked_out` |
| Stealing four animals in one raid | TC-RAID-033, TC-RAID-034 | First three succeed, fourth rejected, limit survives reconnect |
| Raiding an offline player | TC-RAID-003, TC-RAID-004 | Base absent; request rejected; data untouched |
| Disconnecting during a raid (attacker) | TC-RAID-040 | Raid concludes; committed transfers stay; uncommitted cancelled |
| Disconnecting during a raid (defender) | TC-RAID-041 | No theft after disconnect; committed transfers stand (end rule Q-1009) |
| Two players interacting with the same egg simultaneously | TC-MP-020 | Exactly one commits; the other has no side effects |
| A client attempting to modify hatch probabilities | TC-EGG-030, TC-EXP-010 | Server odds only; outcomes unaffected; logged |
| Ascending without enough duplicates | TC-ASC-006 | Rejected; nothing consumed; no fee |
| Changing team away from base | TC-INV-064, TC-EXP-021 | Rejected `not_at_base` |
| Team of two or four | TC-INV-061, TC-INV-062, TC-INV-063 | Four rejected; two rejected when three are owned; fewer-than-three owners per Q-1002 |
| Leaving the base mid-selection | TC-INV-066, TC-INV-067 | Pending selection discarded; old team kept; no partial team |
| Stale `oddsVersion` | TC-EGG-026, TC-EGG-048 | Rejected without charge; new odds displayed |
| Roll with Cash exactly equal to the price | TC-EGG-002 | Succeeds; Cash 0 |
| Integer overflow on Cash | TC-PER-034, TC-EXP-027 | Clamps at `MAX_CASH`; no wrap or precision loss |
| Merging Secret eggs | TC-MRG-017 | Not selectable; rejected |
| Merging without the station | TC-MRG-001 | Rejected `no_station` |
| Merging Epic at station level 2 | TC-MRG-013 | Rejected; requires level 3 |
| DataStore failure mid-save | TC-PER-010, TC-PER-011, TC-RAID-047 | Retries; no partial overwrite; no loss |
| Rejoining another server mid-raid | TC-RAID-045, TC-RAID-046, TC-PER-022 | Old raid ended; lock respected; committed state loaded |
| Stolen equipped animal | TC-RAID-036, TC-INV-073 | Victim's team never references it; slot per Q-025 |
| Ascending an equipped animal | TC-ASC-020, TC-ASC-021, TC-ASC-022 | Allowed at base without changing the team; equipped copies are not fodder (Q-1005) |
| Mythical wild rare-spawn announced to the server | TC-AI-035 | Everyone on the server notified; other servers not |
| Boss leash reset | TC-BOSS-012, TC-BOSS-013 | Full HP, threat cleared, no reward for pre-reset damage |
| Merge output with base storage full | TC-MRG-026 | No egg destroyed; capacity never exceeded (Q-1001) |
| Hatch with owned-animal storage full | TC-EGG-063, TC-EGG-064 | Refused before consumption (Q-1004) |
| Same ID used twice in one request | TC-EGG-052, TC-MRG-020, TC-ASC-011, TC-INV-069 | Rejected; no duplication |
| Crash between two profile writes | TC-RAID-044, TC-PER-042 | Item in exactly one profile after recovery |

## 6. UNDECIDED parameter coverage

| Parameter | Q-ID | Symbol in tests | Test cases |
|---|---|---|---|
| Raid duration | [[Open Questions#Q-012]] | `T_raid` | TC-RAID-010 to 013, 027; TC-EXP-055 |
| Egg theft limit | [[Open Questions#Q-013]] | `L_egg` | TC-RAID-022, 023; TC-INV-028; TC-EXP-054 |
| Defeat penalties | [[Open Questions#Q-014]] | penalty row per battle type | TC-CMB-080, 081; TC-PVP-020, 023; TC-RAID-052, 053; TC-BOSS-024 |
| Expansion currency and price | [[Open Questions#Q-009]], [[Open Questions#Q-010]] | `C_exp`, `P_exp(step)` | TC-INV-020 to 026 |
| PvP activation | [[Open Questions#Q-011]] | server PvP state | TC-PVP-001 to 005 |
| Boss rewards | [[Open Questions#Q-015]] | reward row | TC-BOSS-021 to 023 |
| Stolen animal properties | [[Open Questions#Q-025]] | configuration branch | TC-RAID-036 to 038; TC-INV-073 |
| Shield acquisition | [[Open Questions#Q-030]] | shield state | TC-BAS-050 to 052; TC-RAID-005, 016 |
| Raid defenders | [[Open Questions#Q-033]], [[Open Questions#Q-035]] | `Defending` flag | TC-AI-050 to 053; TC-RAID-051 |
| Owned-animal capacity | [[Open Questions#Q-022]] | `N_animals` | TC-EGG-063, 064; TC-INV-040; TC-RAID-039 |
| Hatch timing and location | [[Open Questions#Q-023]] | location rule | TC-EGG-059 to 062, 066 |
| Merge timing | [[Open Questions#Q-034]] | animation length | TC-MRG-032 |
| Pen display | [[Open Questions#Q-008]] | display flag | TC-BAS-036; TC-MOB-030 |
| Module availability | [[Open Questions#Q-007]] | availability flag | TC-BAS-020 |

## Related documents

- [[QA Strategy]]
- [[QA and Testing Index]]
- [[Statistical Testing of Probabilities]]
- [[Bug Reporting and Severity]]
- [[Product Backlog]]
- [[Development Roadmap]]
- [[Decision Register]]
- [[Open Questions]]
