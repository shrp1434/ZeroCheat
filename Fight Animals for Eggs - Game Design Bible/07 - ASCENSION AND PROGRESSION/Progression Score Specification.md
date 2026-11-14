---
title: Progression Score Specification
type: spec
category: progression
status: proposed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - progression
  - luck
  - data
  - server-authoritative
---

# Progression Score Specification

The Progression Score (PS) is the single number, 0–1000, that drives [[Dynamic Progression Luck]]. This page specifies its inputs, weights, caps, data sources, recalculation triggers, worked profiles and tuning levers.

> [!info] PROPOSED (D-036)
> Every input, weight and cap on this page is **PROPOSED** and comes from [[Canonical Proposed Values]] §8. The final luck formula and its inputs are **UNDECIDED** ([[Open Questions#Q-017]]).

> [!success] CONFIRMED context (D-017)
> The formula may be hidden from players; the resulting odds must be disclosed before every commit. PS never influences wild encounters.

## 1. Formula

`PS = LevelPts + DiscoveryPts + MiniBossPts + WorldBossPts + RegionPts + BasePts`, clamped to 0–1000.

`P = clamp(PS / 1000, 0, 1)`, then the rarity and pool formulas in [[Dynamic Progression Luck]] apply (pivot P₀ = 0.30).

## Inputs and data sources

| Input | Points | Cap | Max points | Share of 1000 | Data source (persisted) | Notes |
|---|---|---:|---:|---:|---|---|
| Player level | 4 per level | level 100 | 400 | 40 % | `level` in [[Schema - Player Progression]] | Level 1 counts as 4 points |
| Unique animals discovered | 3 per species | 60 species | 180 | 18 % | Discovered set in [[Schema - Discovery Index]] | Discovery = defeated in the wild (D-029). **Owned** status does not count |
| Unique mini-bosses defeated | 10 each | 8 | 80 | 8 % | Boss first-defeat flags in [[Schema - Unlocks and Boss Progress]] | First defeat only |
| Unique world bosses defeated | 20 each | 4 | 80 | 8 % | Same schema | First defeat only; must meet the boss credit rule in [[Boss Design Overview]] (≥ 2.5 % contribution or 60 s in combat) |
| Regions unlocked beyond the first | 20 each | 7 | 140 | 14 % | Region unlock flags in [[Schema - Unlocks and Boss Progress]] | Whisperwood Forest and the hub do not count |
| Base progression | `round(120 × TotalModuleLevels / 44)` | 44 levels | 120 | 12 % | Module levels in [[Schema - Base Data]] | 7 modules × 5 + Egg Merging Station 5 + Plot Expansion 4 = 44 |
| **Total** | | | **1000** | **100 %** | | |

**Inputs that never count (PROPOSED):** Cash held or spent, number of rolls or hatches, owned animals, ascension levels, PvP or raid results, play time, Robux spending. Counting rolls or spend would turn luck into a purchasable or grindable outcome and break the fairness charter ([[Design Principles and Fairness Charter]]).

**Monotonicity (PROPOSED requirement).** Every input is a "first time" flag or a level that never decreases, so PS never falls. Raids cannot remove module levels, discoveries or boss flags. Players therefore never see their odds worsen through play.

## 2. Server-side computation

PS is computed **only on the server**, only from the persisted profile. No remote accepts PS, P or odds from the client.

```lua
-- Illustrative Luau (not executed). Lives in LuckService.
local MAX_MODULE_LEVELS = 44

local function computeProgressionScore(profile): number
	local levelPts = 4 * math.clamp(profile.progression.level, 1, 100)
	local discoveryPts = 3 * math.min(profile.discovery.count, 60)
	local miniPts = 10 * math.min(profile.bosses.miniDefeatedCount, 8)
	local worldPts = 20 * math.min(profile.bosses.worldDefeatedCount, 4)
	local regionPts = 20 * math.clamp(profile.unlocks.regionCount - 1, 0, 7)
	local moduleLevels = math.min(profile.base.totalModuleLevels, MAX_MODULE_LEVELS)
	local basePts = math.round(120 * moduleLevels / MAX_MODULE_LEVELS)
	return math.clamp(levelPts + discoveryPts + miniPts + worldPts + regionPts + basePts, 0, 1000)
end
```

Counts are derived from stored sets (for example `discovery.count` is the size of the discovered set), never from a separately stored counter that could drift. Detail: [[Implementation - Dynamic Luck Calculation]], [[Service - LuckService]].

## 3. Recalculation triggers

| Trigger | Source service | Action |
|---|---|---|
| Profile load (join) | [[Service - DataService]] | Compute PS, cache |
| Level-up | [[Service - ProgressionService]] | Recompute; invalidate `oddsVersion` tokens |
| New species discovered | [[Service - IndexService]] | Recompute; invalidate tokens |
| First defeat of a mini-boss or world boss | [[Service - BossService]] | Recompute; invalidate tokens |
| Region unlocked | [[Service - ProgressionService]] | Recompute; invalidate tokens |
| Module, station or plot upgrade committed | [[Service - BaseService]] | Recompute; invalidate tokens |
| Luck configuration change (`configVersion`) | Live config via MessagingService | Recompute for all players on the server; invalidate all tokens |

Recalculation is cheap (six integer reads) and synchronous with the triggering transaction, so the next odds request always reflects the new PS. If a player has a roll or hatch panel open when PS changes, their next commit is rejected as stale and the new odds are shown ([[Randomised Reward Compliance]]).

## Worked player profiles

These four profiles are used throughout the vault ([[Dynamic Progression Luck]], [[Ascension Expected Value Analysis]], [[Probability Balancing]]).

| Input | Beginner | Intermediate | Advanced | Endgame |
|---|---|---|---|---|
| Level | 6 → **24** | 27 → **108** | 55 → **220** | 96 → **384** |
| Species discovered | 6 → **18** | 24 → **72** | 40 → **120** | 56 → **168** |
| Mini-bosses defeated | 0 → **0** | 3 ([[Mini-Boss - Bramblehorn]], [[Mini-Boss - Dustmane]], [[Mini-Boss - Vinecoil]]) → **30** | 6 (up to [[Mini-Boss - Stormtalon]]) → **60** | 8 → **80** |
| World bosses defeated | 0 → **0** | 1 ([[World Boss - Ironbark Colossus]]) → **20** | 2 (plus [[World Boss - Thunderhoof]]) → **40** | 4 → **80** |
| Regions beyond the first | 0 → **0** | 2 (Savanna, Canopy) → **40** | 5 (to Skyreach Peaks) → **100** | 7 (all) → **140** |
| Module levels (of 44) | 3 → round(8.18) = **8** | 11 → round(30.0) = **30** | 22 → round(60.0) = **60** | 36 → round(98.18) = **98** |
| **PS** | **50** | **300** | **600** | **950** |
| **P** | **0.05** | **0.30** | **0.60** | **0.95** |
| Secret odds | 0.0043 % | 0.0200 % | 0.0358 % | 0.0510 % |
| Typical region farmed | Whisperwood Forest | Emerald Canopy | Skyreach Peaks | Starfall Sanctuary |

Each profile respects the region gates in [[Region Unlock Progression]] (for example the advanced player is level 55 ≥ 52 with [[Mini-Boss - Rimeback]] defeated, so Skyreach Peaks is open; the endgame player is level 96 ≥ 80 with all world bosses defeated, so [[Region - Starfall Sanctuary]] is open).

**Observations.**
- Level dominates early (48 % of the beginner's PS) but only 40 % of the maximum. Level and discovery together give at most 580 (400 + 180); the remaining 420 points come from bosses, regions and the base, so top luck needs every pillar.
- The pivot P = 0.30 is reached around level 27 with modest bosses and base, which by the levelling model in [[Player Progression and Levelling]] is roughly 33 hours of play. Everyone before that point plays with below-baseline odds (see the warning in [[Dynamic Progression Luck]]).

## 4. Tuning levers

| Lever | Current | Effect of raising | Risk |
|---|---|---|---|
| Points per level | 4 | Luck grows with grinding | Makes luck a pure time sink |
| Points per discovery | 3 | Rewards exploration and fighting every species | Discovery of Secret wild spawns (10 % per 45-min window) becomes a luck bottleneck |
| Boss points | 10 / 20 | Rewards challenge content | Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]); keep PS points separate from boss loot |
| Region points | 20 | Rewards the main progression path | Overlaps strongly with level (regions are level-gated) |
| Base points | 120 cap | Rewards base investment | Base modules cost Cash: must never be sold for Robux, or luck becomes purchasable ([[Open Questions#Q-032]]) |
| Total scale (1000) and pivot | 0.30 | — | See [[Probability Balancing]] |
| Diminishing returns | none (linear) | A concave curve (for example `P = (PS/1000)^0.8`) gives more luck early | Adds a hidden transform; still allowed because odds are disclosed |

### Content expansion

Adding animals, bosses or regions after launch would push the maxima past 1000 (for example 70 species × 3 = 210). **PROPOSED rule:** at each content update, rescale per-input points so each input keeps its share (discovery points = round(180 × discovered / rosterSize)), and apply `PS_new = max(PS_old_stored, PS_new_computed)` for one season so no player's odds drop when the denominator grows. A rescale is a luck configuration change and follows [[Balance Update Process]] and [[Content Expansion Guidelines]].

## 5. Tests

- Unit: each profile above computes exactly 50 / 300 / 600 / 950.
- Unit: caps hold (level 150 in a corrupted profile counts as 100; region count 0 gives 0, not −20).
- Integration: each trigger invalidates the odds token.
- Security: a remote carrying a PS or odds field has it ignored and is logged ([[Test Cases - Exploit Prevention]]).

## Related documents
- [[Dynamic Progression Luck]] · [[Dynamic Luck Probability Tables]] · [[Probability Balancing]]
- [[Player Progression and Levelling]] · [[Region Unlock Progression]] · [[Boss Design Overview]] · [[Base Upgrade System]]
- [[Animal Index Feature Specification]] · [[Schema - Player Progression]] · [[Schema - Discovery Index]] · [[Schema - Unlocks and Boss Progress]] · [[Schema - Base Data]]
- [[Service - LuckService]] · [[Implementation - Dynamic Luck Calculation]]
- [[Ascension and Progression Index]]
