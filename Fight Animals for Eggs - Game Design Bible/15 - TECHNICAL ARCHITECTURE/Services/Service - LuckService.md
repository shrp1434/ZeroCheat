---
title: Service - LuckService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - luck
  - probability
  - compliance
---

# Service - LuckService

> [!info] PROPOSED
> Layer **4**. Design is **PROPOSED**; code is illustrative Luau, not tested. The formula is **PROPOSED** (D-036) and its final form is **UNDECIDED** ([[Open Questions#Q-017]]). Specification: [[Progression Score Specification]], [[Dynamic Progression Luck]]. Implementation detail: [[Implementation - Dynamic Luck Calculation]]. Generated odds: [[Dynamic Luck Probability Tables]], [[Hatch Pool Tables]].

> [!success] CONFIRMED rules enforced here (D-017, D-018)
> Hidden progression-based luck changes egg-rarity odds and hatch odds, and **does not** change wild encounter rarity. The formula may stay hidden, but the **actual odds must be shown before the player commits** and must never change silently after a purchase. Hatches are independent.

> [!info] PROPOSED (D-041): odds version tokens
> Displayed odds are bound to a server-issued `oddsVersion`. A confirm carrying a stale token is rejected and the client re-displays the new odds.

## Responsibility

- Compute each player's **Progression Score** (PS, 0–1000) and normalised progression `P` **server-side only**.
- Compute the player's current **egg-rarity odds** and **hatch-pool odds** from `P` and config.
- Issue and check `oddsVersion` tokens; fire `OddsInvalidated` whenever the odds a player would receive change.
- Never send PS, `P`, slopes or tilt values to the client; only final odds go out, inside quotes issued by [[Service - EggService]] and [[Service - HatchService]].

It does **not** roll anything. Rolling is done by EggService and HatchService with `Systems/WeightedRandom` ([[Implementation - Weighted Random Selection]]).

## Inputs

| PS input (from [[Canonical Proposed Values#8. Dynamic progression luck (PROPOSED — final formula UNDECIDED, Q-017)]]) | Points | Source signal |
|---|---|---|
| Player level | 4 per level, max 400 | `ProgressionService.LevelChanged` |
| Unique species discovered | 3 each, max 180 | `IndexService.SpeciesDiscovered` |
| Unique mini-bosses defeated | 10 each, max 80 | `ProgressionService.BossFirstDefeat` |
| Unique world bosses defeated | 20 each, max 80 | `ProgressionService.BossFirstDefeat` |
| Regions unlocked beyond the first | 20 each, max 140 | `ProgressionService.RegionUnlocked` |
| Base progression | `round(120 × TotalModuleLevels / 44)`, max 120 | `BaseService.ModuleLevelChanged` |

Config: `LuckConfig` (pivot 0.30, per-rarity `Base_r` and slope `s_r`, `H = 1.0`, tilt per pool class) and `AnimalCatalogue` (pool membership and class: Standard 10, Scarce 6, Elusive 3). Both carry an explicit `version` string bumped by every balance update ([[Balance Update Process]]).

## Outputs

| Output | Consumer |
|---|---|
| `GetEggOdds`, `GetHatchPoolOdds` results with `oddsVersion` | EggService, HatchService |
| `OddsInvalidated(player, reason)` signal and `Luck/OddsInvalidated` remote | EggService and HatchService (drop open quotes), client |
| `luck.ps_changed` debug log; PS decile in roll analytics | AnalyticsAndLoggingService |

## Dependencies

[[Service - ProgressionService]], [[Service - IndexService]], [[Service - BaseService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]].

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `OddsInvalidated` | `(player: Player, reason: "ProgressionChanged" \| "ConfigChanged")` |
| Remote S→C | `Luck/OddsInvalidated` | `{ reason }`, coalesced to at most one per second |

## Data structures

```lua
--!strict
export type Rarity = "Common" | "Uncommon" | "Rare" | "Epic" | "Legendary" | "Mythical" | "Secret"

export type PSBreakdown = {
	level: number, discovered: number, miniBosses: number,
	worldBosses: number, regions: number, base: number,
	total: number,          -- 0..1000
}

export type OddsTable = { [string]: number }   -- key -> probability in [0, 1], sums to 1 (within 1e-9)

export type LuckState = {
	ps: PSBreakdown,
	p: number,                       -- clamp(ps.total / 1000, 0, 1)
	oddsVersion: string,             -- see "Token design"
	eggOdds: OddsTable,              -- cached, rarity -> probability
	poolOdds: { [Rarity]: OddsTable },-- cached, speciesId -> probability
}
```

The Progression Score is **derived**, not stored: it is recomputed from profile data on load and on every input signal. This avoids a second source of truth ([[Schema - Player Progression]]).

## Public API

```lua
--!strict
-- Server-only. None of these are exposed through remotes.
function LuckService:GetProgressionScore(player: Player): PSBreakdown
function LuckService:GetEggOdds(player: Player): (OddsTable, string)                    -- odds, oddsVersion
function LuckService:GetHatchPoolOdds(player: Player, rarity: Rarity): (OddsTable, string)
function LuckService:GetOddsVersion(player: Player): string
function LuckService:IsCurrent(player: Player, oddsVersion: string): boolean
function LuckService:FormatForDisplay(odds: OddsTable): { [string]: string }            -- display strings (precision Q-810)
```

## Calculation

```lua
--!strict
-- Illustrative Luau, not tested. Mirrors Canonical Proposed Values §8.
local function eggOdds(p: number): OddsTable
	local weights, total = {}, 0
	for _, rarity in Rarity.ORDER do
		local cfg = LuckConfig.eggs[rarity]                 -- { base = 65, slope = 0.0 } ...
		local w = cfg.base * (1 + cfg.slope * (p - LuckConfig.pivot))
		w = math.max(w, 0)                                  -- slopes are positive, guard anyway
		weights[rarity] = w
		total += w
	end
	for rarity, w in weights do
		weights[rarity] = w / total
	end
	return weights
end

local function poolOdds(p: number, rarity: Rarity): OddsTable
	local weights, total = {}, 0
	for _, species in AnimalCatalogue.byRarity[rarity] do
		local class = LuckConfig.poolClasses[species.poolClass] -- { weight = 10, tilt = 0 } ...
		local w = class.weight * (1 + LuckConfig.H * (p - LuckConfig.pivot) * class.tilt)
		weights[species.id] = w
		total += w
	end
	for id, w in weights do
		weights[id] = w / total
	end
	return weights
end
```

### Worked example (illustrative only; authoritative values are in [[Dynamic Luck Probability Tables]])

A player at level 20 (80 points), 15 species discovered (45), 2 mini-bosses (20), no world bosses (0), 2 regions beyond the first (40) and 8 of 44 module levels (`round(120 × 8 / 44)` = 22). **PS = 207**, **P = 0.207**, so `P − 0.30 = −0.093`.

| Rarity | Weight `Base × (1 + s × −0.093)` | Normalised odds |
|---|---:|---:|
| Common | 65.0000 | 66.99% |
| Uncommon | 20.7724 | 21.41% |
| Rare | 7.9956 | 8.24% |
| Epic | 2.4978 | 2.57% |
| Legendary | 0.6214 | 0.640% |
| Mythical | 0.1331 | 0.137% |
| Secret | 0.0140 | 0.0145% |
| **Sum** | 97.0344 | 100.00% |

If this player levels up to 21 while the roll screen is open, PS becomes 211, the `oddsVersion` changes, the client receives `Luck/OddsInvalidated`, and a confirm with the old token returns `E_STALE_ODDS`. The player then sees the new odds and confirms again.

## Token design

`oddsVersion = LuckConfig.version .. ":" .. AnimalCatalogue.version .. ":" .. tostring(ps.total)`

- It changes **exactly** when the odds a player would receive change (PS or config change) and never otherwise.
- It is not a secret: forging it gains nothing, because the server compares it with the token it computes now. A client can only ever confirm at its **current** odds.
- Quotes (issued by EggService and HatchService through `Systems/QuoteStore`) store the `oddsVersion` and the exact odds table they displayed. At commit, the roll uses the **quoted** odds table, and only after checking that the quoted `oddsVersion` equals the current one. So the odds applied are always identical to the odds displayed.

> [!danger] Compliance
> Never apply odds that differ from the quote, even favourably. Never recompute odds between check and roll. A mismatch is a P0 bug ([[Randomised Reward Compliance]], [[Roblox Monetisation Policy Requirements]]).

## Display precision

> [!warning] UNDECIDED (Q-810): odds display precision
> At `P = 0` the Secret egg probability is about 0.000885%, so a fixed two-decimal format would display "0.00%", which arguably misrepresents the odds. Options: (a) fixed four decimal places for every rarity; (b) significant-figure formatting (for example three significant figures, so "0.000885%"); (c) "less than 0.01%" style text plus exact values in an info panel. The choice affects UI layout and compliance wording. Recommendation (**PROPOSED**): option (b), because it shows the real value without padding common rarities. `FormatForDisplay` implements whichever is chosen; the probabilities used for rolling are never rounded.

## Error handling

| Case | Behaviour |
|---|---|
| Profile not loaded | `GetEggOdds` returns `nil`; callers respond `E_NOT_READY` |
| Odds do not sum to 1 within 1e-9 or contain NaN | Boot-time and runtime assertion; feature disabled with `E_FEATURE_DISABLED`; `Error` log (P0) |
| Pool for a rarity is empty | Boot-time validation fails; hatching that rarity disabled |
| Config hot reload | All players' tokens change; `OddsInvalidated` with `ConfigChanged` to everyone |

## Security requirements

- PS, `P` and internal parameters never leave the server. Analytics records PS only as a decile bucket.
- No remote reads luck state directly. Odds reach the client only inside quotes.
- LuckService is not a dependency of SpawnService (wild rarity is unaffected by luck, D-017).
- Independence (D-018): no input in this service reads hatch history, duplicates or ownership. A static test asserts `poolOdds` reads only `P` and catalogue data.

## Testing requirements

| Test | Type |
|---|---|
| Egg odds at P = 0.30 equal the baseline 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 % exactly | Unit |
| Odds for P = 0, 0.5, 1 match [[Dynamic Luck Probability Tables]] to 6 decimal places | Unit |
| Every hatch pool sums to 1 at P = 0, 0.3, 1; matches [[Hatch Pool Tables]] | Unit |
| PS breakdown matches a hand-computed fixture for 10 profiles | Unit |
| Levelling up between quote and confirm yields `E_STALE_ODDS` and no charge | Integration ([[Test Cases - Egg Rolls and Hatching]]) |
| Owning or not owning a species never changes pool odds | Unit (D-018) |
| Over 1,000,000 simulated rolls at fixed P, observed rates fall within 99.9% confidence intervals | Statistical ([[Statistical Testing of Probabilities]]) |

## Related documents
- [[Technical Architecture Index]]
- [[Dynamic Progression Luck]]
- [[Progression Score Specification]]
- [[Implementation - Dynamic Luck Calculation]]
- [[Dynamic Luck Probability Tables]]
- [[Hatch Pool Tables]]
- [[Randomised Reward Compliance]]
- [[Independent Random Outcomes]]
- [[Service - EggService]]
- [[Service - HatchService]]
