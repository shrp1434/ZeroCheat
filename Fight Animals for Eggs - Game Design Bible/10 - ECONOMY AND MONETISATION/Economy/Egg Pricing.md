---
title: Egg Pricing
type: spec
category: economy
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - eggs
  - pricing
---

# Egg Pricing

The price of an egg roll and how that price interacts with income, storage, merging and compliance. Roll mechanics are owned by [[Egg Roll System]]; odds by [[Dynamic Luck Probability Tables]].

> [!success] CONFIRMED
> Cash buys egg rolls (D-014). The roll decides rarity; the hatch decides the animal (D-015). Actual odds must be shown before committing and must never change silently (D-017).

> [!info] PROPOSED (D-039)
> **200 Cash per roll, flat.** Bulk roll ×5 for 1,000 Cash (no discount; convenience only).

> [!warning] UNDECIDED
> The pricing model (flat versus scaled) is **UNDECIDED** ([[Open Questions#Q-020]]). Final egg probabilities are **UNDECIDED** ([[Open Questions#Q-016]]).

## 1. What the flat price does across the game

| Region | Raw Cash per hour | Roll as % of hourly income | Minutes of farming per roll | Rolls per hour |
|---|---:|---:|---:|---:|
| 1 Whisperwood Forest | 5,086 | 3.93% | 2.4 | 25 |
| 2 Sunscorch Savanna | 8,452 | 2.37% | 1.4 | 42 |
| 3 Emerald Canopy | 13,222 | 1.51% | 0.9 | 66 |
| 4 Coral Coast | 19,232 | 1.04% | 0.6 | 96 |
| 5 Frostfang Tundra | 27,284 | 0.73% | 0.44 | 136 |
| 6 Skyreach Peaks | 37,591 | 0.53% | 0.32 | 188 |
| 7 Emberheart Caldera | 48,254 | 0.41% | 0.25 | 241 |
| 8 Starfall Sanctuary | 62,422 | 0.32% | 0.19 | 312 |

Rolls become ~12× cheaper relative to income. This is **intended acceleration** (D-039): late players roll in bulk and feed the merge chain, where the scaling **merge fees** become the real price of rarity ([[Expected Value Calculations]]).

## 2. Options for Q-020

| Option | Rule | Pros | Cons | Compliance notes |
|---|---|---|---|---|
| A. Flat (D-039) | 200 Cash always | Readable; one number; rolls feel generous late | Rolls trivial late; storage and hatch throughput become the limiter | Simple to disclose |
| B. Region-scaled shrines | Egg shrines in each region; price × region multiplier; **same odds** (luck is PS-based, not region-based) | Keeps rolls meaningful | Players pay more for identical odds, which feels bad; luck is already PS-driven | Must still show odds per shrine |
| C. Progression-scaled price | Price rises with PS (e.g. `200 × (1 + 4P)`) | Roll stays ~constant share of income | Punishes progress; hides a second scaling; confusing with luck also rising | Price must be shown before commit |
| D. Tiered eggs | Several egg types with different prices and **different** base odds | Familiar to players; clear choice | Adds tables to maintain; must not conflict with the CONFIRMED two-stage model | Each egg type needs its own disclosure |

> [!info] PROPOSED recommendation: keep Option A for launch
> The flat price is easy to understand and to disclose, and the economy already has scaling sinks. Revisit after beta if telemetry shows rolls stop mattering before Region 4 (roll spend < 30% of income) **and** storage friction appears. Option D is the preferred fallback because it adds choice rather than a tax. Final decision: **UNDECIDED** (Q-020).

## 3. Storage and throughput limits

Late-game rolling is limited by storage, not by Cash.

| Constraint | Value | Late-game effect |
|---|---|---|
| Total egg storage at start | 60 (**CONFIRMED**) | Fills in ~12 minutes of Starfall income if all Cash is rolled |
| Hatch batch | 5 eggs (**CONFIRMED**) | 312 rolls per hour ≈ 63 multi-hatches ≈ 5.2 min of animations (5.0 s each, skippable after first view) |
| Owned-animal cap | 100 (working assumption, [[Open Questions#Q-022]]) | Overflows quickly; requires ascension or release (Q-406) |
| Merge | 3 → 1 | Each merge frees two slots; merging is the pressure valve |

This is the main reason storage expansion has real value even though rolls are cheap ([[Storage Expansion Economics]]).

## 4. Roll transaction rules (PROPOSED)

- Price, odds and `oddsVersion` are displayed before confirmation; the server rejects stale tokens (D-041; [[Randomised Reward Compliance]]).
- Cash is deducted only if a storage slot is available for every egg in the batch (backpack first, then base if at base, per [[Egg Storage]]).
- Bulk ×5 is five independent rolls (D-018); the result list is shown in roll order.
- Ledger entry per batch: `{ reason = "EggRoll", count, price, oddsVersion }`.

```lua
-- Illustrative Luau (not executed)
local ROLL_PRICE = 200

local function tryRoll(player: Player, count: number, oddsVersion: string)
	assert(count == 1 or count == 5)
	if not LuckService.IsCurrentOddsVersion(player, oddsVersion) then
		return false, "OddsChanged" -- client must re-display odds
	end
	if not EggService.HasFreeSlots(player, count) then return false, "StorageFull" end
	if not EconomyService.TrySpend(player, ROLL_PRICE * count, "EggRoll", { count = count, oddsVersion = oddsVersion }) then
		return false, "InsufficientCash"
	end
	return true, EggService.RollEggs(player, count) -- server-side Random, independent per egg
end
```

## 5. Edge cases

| Case | Handling |
|---|---|
| Player levels up between viewing odds and confirming | Token stale → rejected, odds re-shown, no Cash taken |
| Only 3 free slots, player requests ×5 | Rejected before payment; UI offers ×1 |
| Price changed by live config | New price shown in the UI before confirmation; a server-side `priceVersion` follows the same pattern as `oddsVersion` (**PROPOSED**) |

## Related documents
- [[Egg Roll System]]
- [[Dynamic Luck Probability Tables]]
- [[Expected Value Calculations]]
- [[Cost Tables]]
- [[Storage Expansion Economics]]
- [[Randomised Reward Compliance]]
- [[UI - Egg Rolling]]
- [[Economy Overview]]
