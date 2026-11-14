---
title: Configuration Modules
type: implementation
category: engineering
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - configuration
  - data
  - balancing
---

# Configuration Modules

Configuration modules turn [[Canonical Proposed Values]] into typed, frozen, validated Luau tables. They are the only place gameplay numbers appear in code. Every value carries the status it has on the canonical page; changing a number means changing the canonical page first ([[Balance Update Process]]).

> [!info] PROPOSED
> The module split, types and validation rules here are **PROPOSED**. Values marked **CONFIRMED** in comments come from the [[Decision Register]]. Code is **illustrative — not executed**.

## 1. Module inventory

| Module | Location | Visibility | Contents | Status of values |
|---|---|---|---|---|
| `ConfigVersion` | `ReplicatedStorage/Shared/Config` | Public | Version string used in odds tokens | **PROPOSED** |
| `RarityConfig` | `Shared/Config` | Public | Seven rarities, order, colour keys, tier multiplier *M* | Tiers **CONFIRMED**; *M* and colours **PROPOSED** |
| `RosterConfig` | `Shared/Config` | Public | 60 species: id, rarity, family, role, region, pool class | **PROPOSED** (D-032) |
| `RoleConfig` | `Shared/Config` | Public | Role multipliers and basic range | **PROPOSED** |
| `CombatConfig` | `Shared/Config` | Public | Damage formula constants, player combo, specials, cooldowns, leash, combat tag | **PROPOSED** |
| `EggConfig` | `Shared/Config` | Public | Roll price, bulk roll, hatch batch, presentation time | Batch 5 **CONFIRMED**; rest **PROPOSED** |
| `LuckConfig` | `ServerStorage/Config` | **Secret** | Base odds, slopes, pivot, H, tilt, class weights | **PROPOSED** (Q-016, Q-017, Q-018) |
| `StorageConfig` | `Shared/Config` | Public | Backpack 10, base 50, expansion steps | Start values **CONFIRMED**; expansion **PROPOSED** / **UNDECIDED** |
| `AscensionConfig` | `Shared/Config` | Public | Duplicates per step, fees, effects | **PROPOSED** (Q-004, Q-005) |
| `MergeConfig` | `Shared/Config` | Public | Station levels, gates, merges unlocked, fees | 3→1 **CONFIRMED**; levels and fees **PROPOSED** (Q-019) |
| `RaidConfig` | `ServerStorage/Config` | Secret | Duration, egg theft cap, animal theft cap | Animal cap 3 **CONFIRMED**; duration and egg cap **UNDECIDED** |
| `RateLimitConfig` | `ServerStorage/Config` | Secret | Token-bucket parameters per remote | **PROPOSED** ([[Implementation - Rate Limiting]]) |
| `AntiCheatConfig` | `ServerStorage/Config` | Secret | Movement tolerances, violation thresholds | **PROPOSED** ([[Exploit Prevention]]) |
| `PerformanceConfig` | `ServerStorage/Config` | Secret | AI LOD radii and tick rates, replication rates | **PROPOSED** ([[Animal Scalability and Performance Budgets]]) |

Why the luck and raid modules are secret: the luck formula may stay hidden (D-017), and publishing anti-cheat thresholds tells exploiters exactly how far they can push. Rarity colours and roll prices are shown in the UI anyway, so they can be public.

## 2. Shared types

```lua
--!strict
-- Illustrative — not executed
-- ReplicatedStorage/Shared/Types

export type RarityName = "Common" | "Uncommon" | "Rare" | "Epic" | "Legendary" | "Mythical" | "Secret"
export type RoleName = "Tank" | "Bruiser" | "Assassin" | "Skirmisher" | "Ranged" | "Support" | "Controller"
export type PoolClass = "Standard" | "Scarce" | "Elusive"
export type ReasonCode = string -- enumerated in Implementation - Remote Validation Layer

export type RarityDef = {
	name: RarityName,
	index: number,       -- 0..6
	tierMultiplier: number,
	colour: Color3,
}

export type SpeciesDef = {
	id: string,          -- stable key, e.g. "tiger"; never the display name
	displayName: string,
	rarity: RarityName,
	family: string,
	role: RoleName,
	homeRegion: string,
	poolClass: PoolClass,
	speciesTweak: { hp: number, atk: number, def: number, as: number, ms: number },
}

return nil
```

## 3. Rarity configuration

```lua
--!strict
-- Illustrative — not executed
-- Shared/Config/RarityConfig

local Types = require(script.Parent.Parent.Types)
local Freeze = require(script.Parent.Parent.Util.DeepFreeze)

-- Order and names: CONFIRMED (D-003). Multipliers and colours: PROPOSED.
local RARITIES: { Types.RarityDef } = {
	{ name = "Common",    index = 0, tierMultiplier = 1.00, colour = Color3.fromHex("#9AA5B1") },
	{ name = "Uncommon",  index = 1, tierMultiplier = 1.30, colour = Color3.fromHex("#4CC26A") },
	{ name = "Rare",      index = 2, tierMultiplier = 1.70, colour = Color3.fromHex("#3D8BFF") },
	{ name = "Epic",      index = 3, tierMultiplier = 2.20, colour = Color3.fromHex("#A55BFF") },
	{ name = "Legendary", index = 4, tierMultiplier = 2.85, colour = Color3.fromHex("#FFB020") },
	{ name = "Mythical",  index = 5, tierMultiplier = 3.70, colour = Color3.fromHex("#FF4D8D") },
	{ name = "Secret",    index = 6, tierMultiplier = 4.80, colour = Color3.fromHex("#1B1B2F") },
}

local byName: { [string]: Types.RarityDef } = {}
for _, r in RARITIES do
	byName[r.name] = r
end

return Freeze({
	ORDER = RARITIES,
	BY_NAME = byName,
	-- Next rarity for merging; Secret has none (CONFIRMED: no rarity above Secret).
	nextOf = function(name: Types.RarityName): Types.RarityName?
		local r = byName[name]
		local n = RARITIES[r.index + 2] -- Luau arrays are 1-based; index is 0-based
		return if n then n.name else nil
	end,
})
```

## 4. Luck configuration (server-only)

```lua
--!strict
-- Illustrative — not executed
-- ServerStorage/Config/LuckConfig
-- All values PROPOSED. Final formula UNDECIDED (Q-017). Final odds UNDECIDED (Q-016).

return {
	PIVOT = 0.30,
	-- Baseline egg-rarity odds in percent at P = PIVOT (D-031, PROPOSED).
	BASE = {
		Common = 65, Uncommon = 22, Rare = 9, Epic = 3,
		Legendary = 0.8, Mythical = 0.18, Secret = 0.02,
	},
	SLOPE = {
		Common = 0.0, Uncommon = 0.6, Rare = 1.2, Epic = 1.8,
		Legendary = 2.4, Mythical = 2.8, Secret = 3.2,
	},
	-- Hatch pools (Q-018)
	CLASS_WEIGHT = { Standard = 10, Scarce = 6, Elusive = 3 },
	TILT = { Standard = 0, Scarce = 0.5, Elusive = 1.0 },
	H = 1.0,
	-- Odds token (PROPOSED locally in Implementation - Dynamic Luck Calculation)
	TOKEN_BUCKET_SECONDS = 60,
	TOKEN_ACCEPT_PREVIOUS_BUCKET = true,
}
```

## 5. Economy and storage configuration

```lua
--!strict
-- Illustrative — not executed
-- Shared/Config/EggConfig and StorageConfig (combined here for brevity)

return {
	ROLL_PRICE_CASH = 200,        -- PROPOSED (D-039); pricing model UNDECIDED (Q-020)
	BULK_ROLL_COUNT = 5,          -- PROPOSED
	BULK_ROLL_PRICE_CASH = 1000,  -- PROPOSED (no discount)
	MAX_HATCH_BATCH = 5,          -- CONFIRMED (D-016)

	BACKPACK_START = 10,          -- CONFIRMED (D-021)
	BASE_STORAGE_START = 50,      -- CONFIRMED (D-021)
	BACKPACK_STEP = 5, BACKPACK_MAX = 25,       -- PROPOSED
	BASE_STEP = 25, BASE_MAX = 200,             -- PROPOSED
	EXPANSION_CURRENCY = nil :: string?,        -- UNDECIDED (Q-009) — deliberately nil
	EXPANSION_PRICE = nil :: number?,           -- UNDECIDED (Q-010) — deliberately nil

	ANIMAL_STORAGE_WORKING_CAP = 100, -- UNDECIDED (Q-022); working assumption only
}
```

## 6. Raid configuration (server-only)

```lua
--!strict
-- Illustrative — not executed
-- ServerStorage/Config/RaidConfig

return {
	MAX_ANIMALS_STOLEN = 3,              -- CONFIRMED (D-024)
	BACKPACK_EGGS_STEALABLE = false,     -- CONFIRMED (D-021) — never read as a toggle; asserted at boot
	-- UNDECIDED (Q-012). No default. Must be injected by a test harness or a future decision.
	DURATION_SECONDS = nil :: number?,
	-- UNDECIDED (Q-013). No default. Must be injected by a test harness or a future decision.
	EGG_THEFT_CAP = nil :: number?,
}
```

> [!warning] UNDECIDED — raid duration and egg theft limit
> `DURATION_SECONDS` and `EGG_THEFT_CAP` are `nil` on purpose ([[Open Questions#Q-012]], [[Open Questions#Q-013]]). `RaidService` refuses to open raids while either is `nil` ([[Implementation - Raid Session Controller]]). Test places set them through `RaidConfigOverride`, which only loads when `RunService:IsStudio()` is true or when the place is flagged as a test place.

## 7. Configuration version

`ConfigVersion` is a string such as `"2026.11.14-a"`. It changes whenever any value that affects odds, prices or rewards changes. It feeds the odds token ([[Implementation - Dynamic Luck Calculation]]), so a balance hot-fix invalidates every displayed odds quote automatically and players see the new odds before they can commit (D-017, D-041).

| Change | Bump `ConfigVersion`? |
|---|---|
| Any `LuckConfig` value | Yes |
| Roll price, merge fee, ascension fee | Yes |
| Roster or pool class change | Yes |
| Colours, UI strings | No |
| Rate limits, anti-cheat thresholds | No |

## 8. Boot-time validation

`ConfigLoader.loadAndValidate()` runs before any service ([[Module Patterns and Bootstrapping]]). It throws on the first failure.

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/ConfigLoader (excerpt)

local function isFinitePositive(x: any): boolean
	return typeof(x) == "number" and x == x and x > 0 and x < math.huge
end

local function validateLuck(L: any, Roster: any)
	local sum = 0
	for name, base in L.BASE do
		assert(isFinitePositive(base), "LuckConfig.BASE." .. name .. " must be positive and finite")
		assert(typeof(L.SLOPE[name]) == "number", "Missing slope for " .. name)
		-- Every rarity weight must stay positive across P in [0, 1].
		local atZero = 1 + L.SLOPE[name] * (0 - L.PIVOT)
		local atOne = 1 + L.SLOPE[name] * (1 - L.PIVOT)
		assert(atZero > 0 and atOne > 0, "Slope makes weight non-positive for " .. name)
		sum += base
	end
	assert(math.abs(sum - 100) < 1e-9, "Baseline odds must sum to 100, got " .. sum)

	-- Every rarity pool must be non-empty and every class weight positive.
	local poolCount: { [string]: number } = {}
	for _, s in Roster.SPECIES do
		poolCount[s.rarity] = (poolCount[s.rarity] or 0) + 1
		assert(isFinitePositive(L.CLASS_WEIGHT[s.poolClass]), "Bad class weight " .. s.poolClass)
	end
	for name in L.BASE do
		assert((poolCount[name] or 0) > 0, "Empty hatch pool for " .. name)
	end
end

local function validateRaid(R: any)
	assert(R.MAX_ANIMALS_STOLEN == 3, "Animal theft cap is CONFIRMED at 3")
	assert(R.BACKPACK_EGGS_STEALABLE == false, "Backpack eggs are CONFIRMED never stealable")
	-- DURATION_SECONDS and EGG_THEFT_CAP may be nil; RaidService handles that.
end
```

| Check | Rule source |
|---|---|
| Baseline odds sum to 100 | [[Canonical Proposed Values]] §7 |
| All weights positive for P in [0, 1] | [[Implementation - Weighted Random Selection]] precondition |
| Roster has 60 species, 12/11/10/9/8/6/4 | D-004 target **CONFIRMED**, split **PROPOSED** (D-030) |
| `MAX_HATCH_BATCH == 5` | D-016 **CONFIRMED** |
| Backpack 10, base 50 | D-021 **CONFIRMED** |
| Animal theft cap 3 | D-024 **CONFIRMED** |
| Merge rules: 3 → 1, Secret terminal | D-020 **CONFIRMED** |

## 9. Deep freeze helper

```lua
--!strict
-- Illustrative — not executed
-- Shared/Util/DeepFreeze

local function deepFreeze<T>(t: T): T
	if typeof(t) ~= "table" then
		return t
	end
	for _, v in t :: any do
		if typeof(v) == "table" and not table.isfrozen(v) then
			deepFreeze(v)
		end
	end
	if not table.isfrozen(t :: any) then
		table.freeze(t :: any)
	end
	return t
end

return deepFreeze
```

Writing to a frozen table errors at run time, which turns "someone mutated the config at run time" from a silent balance bug into a loud error in testing.

## 10. Live tuning

Live balance changes ship as a new place version with a bumped `ConfigVersion` ([[Content Update Pipeline]]). Remote configuration through a DataStore or MemoryStore is **not** recommended at launch because it bypasses code review and the boot-time validation above. Revisit after launch in [[Live Operations Framework]].

## Related documents
- [[Canonical Proposed Values]]
- [[Luau Implementation Index]]
- [[Module Patterns and Bootstrapping]]
- [[Implementation - Dynamic Luck Calculation]]
- [[Implementation - Raid Session Controller]]
- [[Data Validation and Migration]]
- [[Balance Update Process]]
- [[Versioning and Changelog Policy]]
