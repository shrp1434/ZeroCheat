---
title: Cost Tables
type: spec
category: economy
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - costs
  - data
  - balancing
---

# Cost Tables

Every Cash price in the game in one place, transcribed from [[Canonical Proposed Values]]. If a number here ever disagrees with the canonical page, **the canonical page wins**; fix this page. All values are **PROPOSED** unless marked otherwise.

## Egg rolls

| Item | Price (Cash) | Status |
|---|---:|---|
| Single roll | 200 | **PROPOSED** (D-039); model **UNDECIDED** ([[Open Questions#Q-020]]) |
| Bulk roll ×5 | 1,000 | **PROPOSED** (no discount) |

## Base modules

`Cost(L) = BaseCost × 2.5^(L − 1)`. L1 = construction. Module availability is **UNDECIDED** ([[Open Questions#Q-007]]).

| Module | L1 | L2 | L3 | L4 | L5 | Total |
|---|---:|---:|---:|---:|---:|---:|
| [[Module - Animal Pens]] | 1,000 | 2,500 | 6,250 | 15,625 | 39,063 | 64,438 |
| [[Module - Egg Vault]] (L0 Egg Crate free) | 1,500 | 3,750 | 9,375 | 23,438 | 58,594 | 96,657 |
| [[Module - Defence Station]] | 2,000 | 5,000 | 12,500 | 31,250 | 78,125 | 128,875 |
| [[Module - Shield Generator]] | 2,500 | 6,250 | 15,625 | 39,063 | 97,656 | 161,094 |
| [[Module - Training Grounds]] | 1,500 | 3,750 | 9,375 | 23,438 | 58,594 | 96,657 |
| [[Module - Multiplier Shrine]] | 3,000 | 7,500 | 18,750 | 46,875 | 117,188 | 193,313 |
| [[Module - Trophy Hall]] | 1,000 | 2,500 | 6,250 | 15,625 | 39,063 | 64,438 |
| **All modules** | **12,500** | **31,250** | **78,125** | **195,314** | **488,283** | **805,472** |

## Plot Expansion

`5,000 × 3^(n − 1)`. Details: [[Base Layout and Plot Expansion]].

| Stage | Cost | Cumulative | Slots after purchase | Module level cap after purchase |
|---:|---:|---:|---:|---:|
| 1 | 5,000 | 5,000 | 4 | L2 |
| 2 | 15,000 | 20,000 | 5 | L3 |
| 3 | 45,000 | 65,000 | 6 | L4 |
| 4 | 135,000 | 200,000 | 7 | L5 |

## Egg Merging Station

The station is **CONFIRMED** to exist, to need purchase and upgrades; all values are **PROPOSED** ([[Open Questions#Q-019]]). Owned by [[Egg Merging Station]].

| Level | Name | Cost | Cumulative | Extra gate | Merges unlocked |
|---:|---|---:|---:|---|---|
| 1 | Twig Nest Press | 2,500 | 2,500 | — | Common→Uncommon, Uncommon→Rare |
| 2 | Stonebound Hatchery Forge | 15,000 | 17,500 | Region 2 unlocked | Rare→Epic |
| 3 | Crystal Incubator | 60,000 | 77,500 | Region 4 unlocked | Epic→Legendary |
| 4 | Aurora Crucible | 250,000 | 327,500 | Region 6 unlocked + 1 world boss defeated | Legendary→Mythical |
| 5 | Celestial Convergence Altar | 1,000,000 | 1,327,500 | Region 8 unlocked | Mythical→Secret |

## Merge fees

Three eggs of one rarity → one of the next (**CONFIRMED**). Fees **PROPOSED**.

| Merge | Fee per merge | Merges in a full 729-Common chain | Fee subtotal |
|---|---:|---:|---:|
| Common → Uncommon | 100 | 243 | 24,300 |
| Uncommon → Rare | 300 | 81 | 24,300 |
| Rare → Epic | 900 | 27 | 24,300 |
| Epic → Legendary | 2,700 | 9 | 24,300 |
| Legendary → Mythical | 8,000 | 3 | 24,000 |
| Mythical → Secret | 25,000 | 1 | 25,000 |
| **Total** | | **364** | **146,200** |

The fee schedule is near-constant per tier of a chain (~24,000), so every tier of the chain costs about the same in fees. Expected costs with mixed-rarity inputs are in [[Expected Value Calculations]].

## Ascension fees

Fee per step n = `RarityFee × n` (n = 1..5). Duplicates per [[Ascension Progression Table]] (levels **UNDECIDED** [[Open Questions#Q-004]], duplicates **UNDECIDED** [[Open Questions#Q-005]]).

| Rarity | A1 | A2 | A3 | A4 | A5 | Total fees | Duplicates A1–A5 | Total duplicates |
|---|---:|---:|---:|---:|---:|---:|---|---:|
| Common | 100 | 200 | 300 | 400 | 500 | 1,500 | 1/2/3/4/5 | 15 |
| Uncommon | 200 | 400 | 600 | 800 | 1,000 | 3,000 | 1/2/3/3/4 | 13 |
| Rare | 400 | 800 | 1,200 | 1,600 | 2,000 | 6,000 | 1/1/2/3/3 | 10 |
| Epic | 800 | 1,600 | 2,400 | 3,200 | 4,000 | 12,000 | 1/1/2/2/3 | 9 |
| Legendary | 1,600 | 3,200 | 4,800 | 6,400 | 8,000 | 24,000 | 1/1/1/2/2 | 7 |
| Mythical | 3,200 | 6,400 | 9,600 | 12,800 | 16,000 | 48,000 | 1/1/1/1/2 | 6 |
| Secret | 6,400 | 12,800 | 19,200 | 25,600 | 32,000 | 96,000 | 1/1/1/1/1 | 5 |

A5 on one animal of every species: **1,083,000 Cash** in fees.

## Storage expansion

| Location | Step | Steps | Max | Price | Currency |
|---|---|---:|---:|---|---|
| Backpack | +5 | 3 | 25 | **UNDECIDED** ([[Open Questions#Q-010]]) | **UNDECIDED** ([[Open Questions#Q-009]]) |
| Base storage | +25 | 6 | 200 | **UNDECIDED** (Q-010) | **UNDECIDED** (Q-009) |

Options and illustrative ladders: [[Storage Expansion Economics]].

## Grand totals

| Bundle | Cash |
|---|---:|
| All base modules L5 | 805,472 |
| Plot Stage 4 | 200,000 |
| Station L5 | 1,327,500 |
| **Full base** | **2,332,972** |
| A5 every species | 1,083,000 |
| **Base plus full ascension of the index** | **3,415,972** |

## Related documents
- [[Canonical Proposed Values]]
- [[Cash Sources and Sinks]]
- [[Expected Value Calculations]]
- [[Base Upgrade System]]
- [[Egg Merging Station]]
- [[Ascension Progression Table]]
- [[Economy and Monetisation Index]]
