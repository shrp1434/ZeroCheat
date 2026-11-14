---
title: Schema - Base Data
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - base
  - storage
---

# Schema - Base Data

## Purpose

Stores the player's modular base: plot expansion stage, each module's level and placement, the Egg Merging Station level, base egg storage expansion, guard assignments, shield timers and the trophy display. Gameplay rules are owned by [[Player Base System]], [[Base Upgrade System]], [[Base Layout and Plot Expansion]], [[Base Defence Overview]] and [[Shield Mechanics]]. Costs and effects come from [[Canonical Proposed Values]] §10–§12.

> [!success] CONFIRMED
> Every player has a modular base whose sections are upgraded separately (D-022). The Egg Merging Station must be purchased and upgraded for higher rarities (D-020). Base storage starts at **50** (D-021).

> [!warning] UNDECIDED
> Which modules ship at launch ([[Open Questions#Q-007]]), whether owned animals are displayed in pens ([[Open Questions#Q-008]]), which animals defend ([[Open Questions#Q-033]]) and how shields are acquired ([[Open Questions#Q-030]]) are all open. The schema keys modules by ID, so adding or removing a module type needs config, not a migration.

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `plotStage` | `number` | Required | `0` | Integer 0–4 | 0 = starting plot; 1–4 = plot expansions bought (`5,000 × 3^(n−1)` Cash) |
| `modules` | `{ [string]: ModuleState }` | Required | `{}` | Keys are module IDs from config | Absent key = not built |
| `mergeStationLevel` | `number` | Required | `0` | Integer 0–5 | 0 = not purchased. Levels 1–5 per canonical §10. |
| `storage` | `BaseStorage` | Required | `{ vaultExpansionSteps = 0 }` | See below | Base egg storage |
| `guards` | `{ string }` | Required | `{}` | Unique owned animal IDs; length ≤ guard capacity from config | Defender assignments (Q-033) |
| `shield` | `ShieldState` | Required | all `0` | Unix seconds ≥ 0 | Persistent raid protection timers |
| `trophiesDisplayed` | `{ string }` | Required | `{}` | Unique boss IDs, each in `unlocks` as defeated; length ≤ 12 | Drives the Trophy Hall Cash bonus (+1% per unique trophy, max 12%) |
| `lastUpgradeAt` | `number?` | Optional | `nil` | Unix seconds | Analytics |

`ModuleState`:

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `level` | `number` | Required | `1` on construction | Integer 1–5 | L1 = construction. Cost `BaseCost × 2.5^(L−1)` |
| `slotIndex` | `number` | Required | — | Integer, unique among modules, < slots unlocked by `plotStage` | Placement on the plot |
| `builtAt` | `number` | Required | `os.time()` | Unix seconds | |
| `upgradedAt` | `number?` | Optional | `nil` | ≥ `builtAt` | |

Module IDs at the proposed launch: `animal_pens`, `egg_vault`, `defence_station`, `shield_generator`, `training_grounds`, `multiplier_shrine`, `trophy_hall`. The Egg Merging Station has its own field because its levels unlock merge tiers rather than a stat curve ([[Egg Merging Station]]).

`BaseStorage`: `vaultExpansionSteps` (integer 0–6; capacity `50 + 25 × steps`, max 200 PROPOSED). The Egg Vault **module level** affects vault security and visuals, not capacity; capacity expansion is separate ([[Module - Egg Vault]], [[Open Questions#Q-009]]).

`ShieldState`: `activeUntil` (shield up until this time), `cooldownUntil` (no new shield before this time), `lastRaidedAt` (last successful raid against this base). Durations are owned by [[Shield Mechanics]] and [[Module - Shield Generator]].

### Derived values (never stored)

| Value | Formula | Used by |
|---|---|---|
| Vault capacity | `50 + 25 × storage.vaultExpansionSteps` | [[Schema - Egg Inventory]] |
| Total module levels | `Σ modules[i].level + mergeStationLevel + plotStage` (max 44) | Progression Score base term `round(120 × total / 44)` |
| Training Grounds bonus | +5% player Strength, +4% equipped animal stats per level | [[Player Strength]], combat |
| Cash bonus | Multiplier Shrine +10% per level; Trophy Hall +1% per displayed unique trophy | [[Progression Multipliers]] |
| Merges unlocked | From `mergeStationLevel` and config | [[Egg Merging Station]] |
| Shield active | `os.time() < shield.activeUntil` | [[Raid Eligibility and Offline Protection]] |

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type ModuleState = {
	level: number,
	slotIndex: number,
	builtAt: number,
	upgradedAt: number?,
}

export type ShieldState = { activeUntil: number, cooldownUntil: number, lastRaidedAt: number }

export type BaseData = {
	plotStage: number,
	modules: { [string]: ModuleState },
	mergeStationLevel: number,
	storage: { vaultExpansionSteps: number },
	guards: { string },
	shield: ShieldState,
	trophiesDisplayed: { string },
	lastUpgradeAt: number?,
}

local MAX_MODULE_LEVEL = 5
local MAX_TOTAL_LEVELS = 44 -- 7 modules x 5 + station 5 + plot 4

local function newBaseData(now: number): BaseData
	return {
		plotStage = 0,
		modules = {},
		mergeStationLevel = 0,
		storage = { vaultExpansionSteps = 0 },
		guards = {},
		shield = { activeUntil = 0, cooldownUntil = 0, lastRaidedAt = 0 },
		trophiesDisplayed = {},
		lastUpgradeAt = nil,
	}
end

local function totalModuleLevels(base: BaseData): number
	local total = base.mergeStationLevel + base.plotStage
	for _, module in base.modules do
		total += module.level
	end
	return math.min(total, MAX_TOTAL_LEVELS)
end
```

## Invariants

1. `0 ≤ plotStage ≤ 4`; `0 ≤ mergeStationLevel ≤ 5`; every module `1 ≤ level ≤ 5`.
2. Every module key exists in module config. A module removed from config is kept with its level and flagged for review; its cost is refunded only by an explicit, reviewed migration.
3. `slotIndex` values are unique and within the slots unlocked by `plotStage` ([[Base Layout and Plot Expansion]]).
4. Upgrades go up by exactly one level per transaction, and gates (region unlocks for station levels 2–5, plus a world boss defeat for level 4) are checked against [[Schema - Unlocks and Boss Progress]] at the time of purchase. Gates are not re-checked on load: an upgrade legitimately bought stays bought.
5. `guards` contains unique owned animal IDs, and each has `locks.guarding = true`. The guard list is the authority.
6. `trophiesDisplayed` contains only bosses the player has defeated, at most 12, no duplicates.
7. Shield timestamps are non-negative integers and never later than `now + longest shield duration in config`. How the timers relate to each other is defined by [[Shield Mechanics]] once shield acquisition is decided ([[Open Questions#Q-030]]).
8. Base data stores no egg instances. Eggs in base storage live in [[Schema - Egg Inventory]] with `location = "base"`.

## Worked example

A player has Animal Pens L3, Egg Vault L2, Training Grounds L4, Multiplier Shrine L2, Merge Station L2 and plot stage 1. Total levels = 3 + 2 + 4 + 2 + 2 + 1 = 14. The base term in the Progression Score is `round(120 × 14 / 44) = 38` of a possible 120 points.

## Migration notes

- Timed upgrades (construction that takes real time) are not proposed. If they are adopted, add an optional `upgradeInProgress = { targetLevel, completesAt }` per module in a migration with default `nil`.
- If the maximum module level changes, `MAX_TOTAL_LEVELS` changes in config and the Progression Score base term rescales automatically, which will change odds for existing players. That is a disclosed odds change and must follow [[Balance Update Process]].

## Size estimate

About 1.2 KiB with all modules built and maximum guards and trophies. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Player Base System]]
- [[Base Upgrade System]]
- [[Base Layout and Plot Expansion]]
- [[Egg Merging Station]]
- [[Shield Mechanics]]
- [[Service - BaseService]]
- [[Cost Tables]]
- [[Schema - Egg Inventory]]
- [[Data and Balancing Index]]
