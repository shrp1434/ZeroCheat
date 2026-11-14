---
title: Schema - Unlocks and Boss Progress
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - progression
  - bosses
  - regions
---

# Schema - Unlocks and Boss Progress

## Purpose

Stores which regions the player has unlocked, which mini-bosses and world bosses they have defeated (and how often), onboarding progress, and one-off feature flags. These feed region access ([[Region Unlock Progression]]), merge-station gates ([[Egg Merging Station]]), trophies ([[Module - Trophy Hall]]) and the Progression Score ([[Progression Score Specification]]).

> [!success] CONFIRMED
> Mini-bosses and world bosses exist (D-012).

> [!warning] UNDECIDED
> Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]). This schema records defeats only; it does not record reward claims beyond the per-spawn eligibility, which is runtime state. The world layout is **UNDECIDED** ([[Open Questions#Q-001]]); region IDs come from config so the proposed eight regions can change without a migration.

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `regions` | `{ [string]: number }` | Required | `{ whisperwood_forest = createdAt }` | Keys are region IDs in config; value = unlock time (Unix seconds) | The hub and the first region are available from the start |
| `miniBosses` | `{ [string]: BossRecord }` | Required | `{}` | Keys are mini-boss IDs in config (8 proposed) | |
| `worldBosses` | `{ [string]: BossRecord }` | Required | `{}` | Keys are world boss IDs in config (4 proposed) | |
| `onboarding` | `OnboardingState` | Required | `{ step = 0 }` | `step` integer ≥ 0 | Owned by [[New Player Onboarding]] |
| `features` | `{ [string]: boolean }` | Required | `{}` | Keys from a config list | One-off "seen" or "unlocked" flags, for example `pvpIntroSeen`, `raidIntroSeen` |

`BossRecord`: `firstDefeatedAt` (Unix seconds), `defeatCount` (integer ≥ 1), `lastDefeatedAt` (Unix seconds). A defeat is credited under the same contribution rule as wild kill credit ([[Multiplayer Combat Rules]]).

`OnboardingState`: `step` (integer), `completedAt` (`number?`).

Region IDs (PROPOSED): `whisperwood_forest`, `sunscorch_savanna`, `emerald_canopy`, `coral_coast`, `frostfang_tundra`, `skyreach_peaks`, `emberheart_caldera`, `starfall_sanctuary`. Mini-boss IDs: `bramblehorn`, `dustmane`, `vinecoil`, `hammertide`, `rimeback`, `stormtalon`, `cinderjaw`, `eclipse_panther`. World boss IDs: `ironbark_colossus`, `thunderhoof`, `abyssal_leviathan`, `ashwing_condor`.

### Derived values (never stored)

| Value | Formula | Used by |
|---|---|---|
| Region unlock eligibility | Level requirement plus previous mini-boss defeated (plus 2 world bosses for Starfall Sanctuary) | [[Region Unlock Progression]] |
| PS: mini-bosses | `10 × count(miniBosses)` (max 80) | [[Progression Score Specification]] |
| PS: world bosses | `20 × count(worldBosses)` (max 80) | as above |
| PS: regions | `20 × (count(regions) − 1)` (max 140) | as above |
| Trophies available to display | Keys of `miniBosses` and `worldBosses` | [[Schema - Base Data]] |

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type BossRecord = { firstDefeatedAt: number, defeatCount: number, lastDefeatedAt: number }

export type UnlocksAndBossProgress = {
	regions: { [string]: number },
	miniBosses: { [string]: BossRecord },
	worldBosses: { [string]: BossRecord },
	onboarding: { step: number, completedAt: number? },
	features: { [string]: boolean },
}

local STARTING_REGION = "whisperwood_forest"

local function newUnlocks(now: number): UnlocksAndBossProgress
	return {
		regions = { [STARTING_REGION] = now },
		miniBosses = {},
		worldBosses = {},
		onboarding = { step = 0, completedAt = nil },
		features = {},
	}
end

local function recordBossDefeat(records: { [string]: BossRecord }, bossId: string, now: number): boolean
	local record = records[bossId]
	if record == nil then
		records[bossId] = { firstDefeatedAt = now, defeatCount = 1, lastDefeatedAt = now }
		return true -- first defeat: may change PS, trophies and gates
	end
	record.defeatCount += 1
	record.lastDefeatedAt = now
	return false
end
```

## Invariants

1. The starting region is always present. If it is missing on load it is re-added (auto-repair).
2. Every unlocked region beyond the first satisfied its gate when it was unlocked. Gates are **not** re-checked on load, because tuning changes must never re-lock content a player legitimately reached.
3. Every key in `miniBosses` and `worldBosses` exists in config. Unknown keys are kept and flagged (soft failure).
4. `defeatCount ≥ 1` and `firstDefeatedAt ≤ lastDefeatedAt`.
5. A first defeat that changes the Progression Score changes the player's odds. The next odds display uses the new score, and any odds token issued before the change becomes stale ([[Dynamic Progression Luck]]).
6. Per-spawn reward eligibility ("once per player per spawn") is runtime state on the server and is not stored here.

## Edge cases

| Case | Handling |
|---|---|
| Player defeats a world boss twice in one spawn window | One defeat credited per spawn (runtime check). `defeatCount` increases once. |
| Region list changes in a content update | New regions are absent until unlocked. A removed region's key is kept and flagged; PS counts only regions present in config. |
| Onboarding redesigned | Migrate old `step` values to the new step numbering in a dedicated migration ([[New Player Onboarding]]) |

## Migration notes

- If regions are re-ordered or gates change, no migration is needed for players who already unlocked them (invariant 2).
- If PS inputs change (Q-017), only the derived formula changes; the stored records stay as they are.

## Size estimate

About 1.5 KiB with all regions and bosses recorded. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Region Unlock Progression]]
- [[Boss Design Overview]]
- [[Boss Rewards]]
- [[Progression Score Specification]]
- [[Service - BossService]]
- [[Service - ProgressionService]]
- [[Schema - Base Data]]
- [[Data and Balancing Index]]
