---
title: Module - Trophy Hall
type: system
category: base
status: mixed
priority: P2
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - bosses
  - multipliers
---

# Module - Trophy Hall

**Asset ID:** MOD-07 (**PROPOSED**). **Slot:** flexible.

> [!info] PROPOSED
> Displays boss trophies. +1% Cash per unique boss trophy displayed, max **+12%** (8 mini-bosses + 4 world bosses) ([[Canonical Proposed Values]] §12).

> [!warning] UNDECIDED
> - Boss rewards, including whether a trophy is a reward at all: **UNDECIDED** ([[Open Questions#Q-015]]). This module assumes the recommended option in [[Boss Rewards]] (a trophy on the first defeat of each unique boss).
> - Whether the bonus counts trophies **displayed** (capacity-gated) or **earned**: **UNDECIDED** (Q-407). This page models "displayed", which gives the module levels a function.
> - Module availability: **UNDECIDED** ([[Open Questions#Q-007]]).

## 1. Purpose

A visible record of boss victories that rewards the full boss roster with a small permanent Cash bonus. It turns the [[Boss Design Overview]] roster into a collection goal at the base.

## 2. Footprint and appearance

| Property | Proposal |
|---|---|
| Footprint | 24 × 30 studs inside a 32 × 32 slot |
| Height | 10 studs (L1) to 20 studs (L5) |
| Appearance | A timber longhouse that becomes a columned hall. Each trophy is a stylised low-poly statuette of the boss (horn, mane, coil, fin, etc.) on a plinth with a nameplate |
| Materials | Timber and thatch; then stone columns, brass plinths, crystal skylights, gold frieze |

Trophy models: one per boss, BOS-## derived statuettes (**PROPOSED**, to be listed in the [[Asset Register]]).

## 3. Upgrade levels

| Level | Cost (Cash) | Trophy plinths | Max Cash bonus at this level | Visual change |
|---:|---:|---:|---:|---|
| L1 | 1,000 | 3 | +3% | Small timber hut with three plinths |
| L2 | 2,500 | 5 | +5% | Extended longhouse, banners |
| L3 | 6,250 | 7 | +7% | Stone columns, brass plinths, lanterns |
| L4 | 15,625 | 10 | +10% | Crystal skylight, world-boss alcoves |
| L5 | 39,063 | 12 | +12% | Golden frieze depicting all twelve bosses, soft aura |

Total: **64,438 Cash**. The 12 plinths at L5 match the 12 bosses, so a fully upgraded hall can show every trophy.

## 4. Functionality

| Function | Proposal |
|---|---|
| Earn trophy | On the first defeat of each unique boss (recommended option in [[Boss Rewards]]); stored in `base.trophies` |
| Display | Player chooses which earned trophies fill the plinths; filling is free and instant |
| Bonus | +1% Cash per unique trophy displayed, additive with the [[Module - Multiplier Shrine]] |
| Inspect | Each plinth shows the boss name, first defeat date and fastest defeat time (for bragging rights) |
| Progression Score | Levels count towards the 44 base levels. Boss defeats already add PS separately ([[Progression Score Specification]]) |

## 5. Dependencies

- Free slot; level cap `PlotStage + 1`.
- Requires boss defeats, so the module's value grows with region progress. Realistic timeline: 3 trophies by Emerald Canopy, 7–8 by Frostfang Tundra, 12 only at endgame (Starfall Sanctuary requires at least two world bosses).
- Depends on Q-015 (trophies as rewards) and Q-407 (displayed vs earned).

## 6. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.TrophyHall = { level, slot }`, `base.trophies = { [bossId] = { firstDefeat, bestTime } }`, `base.displayedTrophies = { bossId, ... }` |
| Validation | Displayed list ⊆ earned trophies; length ≤ plinth count; no duplicates |
| Instances | `Plot_##.Modules.TrophyHall` with `Plinth_01..12` attachments; trophy models cloned by the server from `ServerStorage.Trophies` |
| Streaming | Atomic module; trophy idle shimmer is client-side |

## 7. Animation and VFX

- Earning a trophy (in the world): "Trophy earned" toast; a ghost statuette flies toward the base direction ([[UI - Notifications]]).
- Placing a trophy: statuette descends onto the plinth with a rarity-neutral gold sparkle.
- Upgrade: columns rise, frieze is revealed by a sweeping light ([[Animation - Base Upgrades]]).

## 8. Raid interaction

Trophies cannot be stolen or damaged. Raiders entering the hall can inspect them. No raid effect (**PROPOSED**).

## Related documents
- [[Boss Rewards]]
- [[Boss Design Overview]]
- [[Module - Multiplier Shrine]]
- [[Progression Multipliers]]
- [[Cost Tables]]
- [[Player Bases Index]]
