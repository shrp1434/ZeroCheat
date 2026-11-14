---
title: Service - ProgressionService
type: technical-service
category: technical-architecture
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - progression
  - levelling
  - regions
---

# Service - ProgressionService

> [!info] PROPOSED
> Layer **2**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design: [[Player Progression and Levelling]], [[Region Unlock Progression]], [[Player Strength]]. Schemas: [[Schema - Player Progression]], [[Schema - Unlocks and Boss Progress]].

## Responsibility

- Own player **XP** and **level** (cap 100; XP needed to reach the next level `XP(L) = round(100 × L^1.6)`).
- Own **unique boss defeats** (8 mini-bosses, 4 world bosses) and **region unlocks** (8 regions; requirements in [[Canonical Proposed Values#5. Regions (PROPOSED — world layout is UNDECIDED, Q-001)]]).
- Unlock player specials by level: Power Strike L1, Ground Slam L10, Rally Cry L25.
- Compute **base Strength** `10 + 2 × (Level − 1)`, player HP and DEF from level. Effective Strength (with base bonuses) is assembled by CombatService.
- Fire the signals that feed the Progression Score.

## Inputs

| Input | Source |
|---|---|
| `AddXP(player, amount, source)` | CombatService (wild defeats), BossService (if boss XP is part of rewards, **UNDECIDED** Q-015) |
| `RecordBossDefeat(player, bossId, kind)` | [[Service - BossService]] |
| `ProgressionConfig`, `RegionConfig` | Config |

## Outputs

| Output | Consumer |
|---|---|
| `progression` and `unlocks` profile sections | Client via deltas |
| `LevelChanged`, `RegionUnlocked`, `BossFirstDefeat` signals | LuckService (PS), CombatService (stats), BaseService (station gates), analytics |
| `Progression/LevelUp`, `Progression/RegionUnlocked` remotes | Client |
| `level_reached`, `region_unlocked`, `boss_defeated` analytics | AnalyticsAndLoggingService |

## Dependencies

[[Service - DataService]], [[Service - AnalyticsAndLoggingService]].

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `LevelChanged` | `(player, oldLevel: number, newLevel: number)` |
| Signal | `RegionUnlocked` | `(player, regionId: string, regionIndex: number)` |
| Signal | `BossFirstDefeat` | `(player, bossId: string, kind: "Mini" \| "World")` |
| Remotes | `Progression/LevelUp`, `Progression/RegionUnlocked` | [[Remote Communication Contract#2.7 Progression, index, shop, telemetry]] |

## Data structures

```lua
--!strict
export type ProgressionSection = {
	level: number,          -- 1..100
	xp: number,             -- XP towards the next level
	totalXp: number,
}

export type UnlocksSection = {
	regions: { [string]: number },       -- regionId -> os.time() unlocked; Whisperwood at start
	miniBosses: { [string]: number },    -- bossId -> first defeat time
	worldBosses: { [string]: number },
}

export type RegionRequirement = {
	regionId: string,
	index: number,                -- 1..8
	minLevel: number,
	requiredBoss: string?,        -- previous region's mini-boss
	minUniqueWorldBosses: number?,-- Starfall Sanctuary: 2
}
```

## Public API

```lua
--!strict
function ProgressionService:GetLevel(player: Player): number
function ProgressionService:XPToNext(level: number): number             -- round(100 * level ^ 1.6)
function ProgressionService:AddXP(player: Player, amount: number, source: string): ()
function ProgressionService:RecordBossDefeat(player: Player, bossId: string, kind: "Mini" | "World"): boolean -- firstTime
function ProgressionService:IsRegionUnlocked(player: Player, regionId: string): boolean
function ProgressionService:GetUnlockedRegionCount(player: Player): number
function ProgressionService:GetUniqueBossCounts(player: Player): (number, number)  -- mini, world
function ProgressionService:IsSpecialUnlocked(player: Player, specialId: string): boolean
function ProgressionService:GetBaseStrength(player: Player): number    -- 10 + 2 * (L - 1)
function ProgressionService:GetPlayerHP(player: Player): number        -- 100 + 12 * (L - 1)
function ProgressionService:GetPlayerDEF(player: Player): number       -- 5 + 0.5 * (L - 1)
```

```lua
--!strict
-- Illustrative Luau, not tested.
function ProgressionService:AddXP(player, amount, source)
	assert(amount >= 0 and amount == amount, "invalid XP")
	local old, new
	Data:Mutate(player, "xp", { "progression" }, function(data)
		local p = data.progression
		old = p.level
		p.totalXp += amount
		if p.level >= MAX_LEVEL then return true end
		p.xp += amount
		while p.level < MAX_LEVEL and p.xp >= self:XPToNext(p.level) do
			p.xp -= self:XPToNext(p.level)
			p.level += 1
		end
		if p.level >= MAX_LEVEL then p.xp = 0 end
		new = p.level
		return true
	end)
	if new and new > old then
		ProgressionService.LevelChanged:Fire(player, old, new)
		evaluateRegionUnlocks(player)      -- level may satisfy a pending requirement
	end
end
```

Worked example: level 1 → 2 needs `round(100 × 1^1.6)` = **100 XP**; level 10 → 11 needs `round(100 × 10^1.6)` = **3,981 XP**. A single large grant can cross several levels; each crossing is reported in one `LevelChanged` with old and new levels, and specials unlocked in between are listed in `Progression/LevelUp`.

Region unlocks are **automatic** when both the level and the boss requirement are met (**PROPOSED**), evaluated after every level change and every first boss defeat. Starfall Sanctuary additionally needs at least 2 different world bosses.

## Error handling

| Case | Behaviour |
|---|---|
| Negative or NaN XP | Assertion inside the mutation; nothing applied; `Error` log (server bug) |
| Unknown boss ID | Ignored, `Warn` log |
| Level above 100 in saved data | Clamped on load, `data.repaired` log |

## Security requirements

- No remote grants XP, levels, unlocks or boss defeats. All come from server events.
- Region access is enforced on the server: entering a locked region's volume triggers the barrier rules in [[Region Unlock Progression]] (teleport back), checked by `ZoneQuery` against server positions.
- Level-up rates are monitored with the Cash rate guard ([[Service - EconomyService]]) for farming exploits.

## Testing requirements

| Test | Type |
|---|---|
| `XPToNext` matches the formula for L = 1..99 | Unit |
| Large XP grant crosses multiple levels correctly; cap at 100 | Unit |
| Region 2 unlocks at level 8 only after Bramblehorn is defeated; order of the two events does not matter | Unit |
| Starfall Sanctuary needs 2 distinct world bosses (same boss twice does not count) | Unit |
| Specials unlock at 1, 10, 25 | Unit |
| `RecordBossDefeat` returns `firstTime` only once per boss | Unit |

## Related documents
- [[Technical Architecture Index]]
- [[Player Progression and Levelling]]
- [[Region Unlock Progression]]
- [[Player Strength]]
- [[Progression Score Specification]]
- [[Schema - Player Progression]]
- [[Schema - Unlocks and Boss Progress]]
- [[UI - Progression Interface]]
