---
title: Schema - Player Progression
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
  - player-strength
---

# Schema - Player Progression

## Purpose

Stores the player's level and experience, the stored inputs to **player strength**, and nothing that can be derived. Player strength is a separate statistic from animal strength (**CONFIRMED**, D-007), so it has its own section here rather than living with animals. Rules are owned by [[Player Progression and Levelling]] and [[Player Strength]]. Formulas and numbers come from [[Canonical Proposed Values]] §4 and §13.

> [!info] PROPOSED
> All fields and limits are **PROPOSED**. Whether animals level individually is **UNDECIDED** ([[Open Questions#Q-021]]); the working assumption is no (D-042), so this schema has no per-animal XP.

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `level` | `number` | Required | `1` | Integer 1–100 (level cap, §13) | Clamp on load (auto-repair) |
| `xp` | `number` | Required | `0` | Integer ≥ 0 and `< XP(level)` unless `level = 100` | XP towards the next level. `XP(L) = round(100 × L^1.6)` |
| `totalXp` | `number` | Required | `0` | Integer ≥ 0, ≥ sum of XP thresholds below `level` | Lifetime XP for analytics and repair |
| `permanentStrengthBonuses` | `{ [string]: number }` | Required | `{}` | Keys are bonus source IDs from config; values 0–1 (fractions) | Reserved for future permanent bonuses that cannot be derived from other data (for example a one-off event reward). Empty at launch. |
| `lastLevelUpAt` | `number?` | Optional | `nil` | Unix seconds | Analytics |

### Derived values (never stored)

| Value | Formula (PROPOSED, from canonical values) | Inputs |
|---|---|---|
| Player HP | `100 + 12 × (Level − 1)` | `level` |
| Player DEF | `5 + 0.5 × (Level − 1)` | `level` |
| Base Strength | `10 + 2 × (Level − 1)` | `level` |
| Effective Strength | `BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)` | `level`, Training Grounds level in [[Schema - Base Data]], `permanentStrengthBonuses` |
| Specials unlocked | Power Strike at L1, Ground Slam at L10, Rally Cry at L25 | `level` |
| Progression Score contribution | `4 × level` (max 400) | `level`; see [[Progression Score Specification]] |

> [!warning] UNDECIDED
> Whether percentage bonuses from different sources add together or multiply is not specified anywhere (for example Training Grounds +5% Strength per level with a future permanent bonus, or ascension +8% with Training Grounds +4% for animals). This schema stores the inputs only, so either rule can be applied without a migration. **UNDECIDED** (Q-953).

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type PlayerProgression = {
	level: number,
	xp: number,
	totalXp: number,
	permanentStrengthBonuses: { [string]: number },
	lastLevelUpAt: number?,
}

local function newPlayerProgression(): PlayerProgression
	return {
		level = 1,
		xp = 0,
		totalXp = 0,
		permanentStrengthBonuses = {},
		lastLevelUpAt = nil,
	}
end

-- Derived, computed on demand by ProgressionService.
local function xpToNext(level: number): number
	return math.round(100 * level ^ 1.6)
end

local function effectiveStrength(progression: PlayerProgression, trainingGroundsLevel: number): number
	local base = 10 + 2 * (progression.level - 1)
	local bonus = 0.05 * trainingGroundsLevel
	for _, value in progression.permanentStrengthBonuses do
		bonus += value -- additive stacking shown for illustration only (Q-953)
	end
	return base * (1 + bonus)
end
```

## Invariants

1. `1 ≤ level ≤ 100`.
2. If `level < 100`, `0 ≤ xp < xpToNext(level)`. If `level = 100`, `xp` is held at `0` and further XP only increases `totalXp`.
3. `totalXp ≥ Σ xpToNext(L)` for `L = 1 … level − 1` (plus `xp`). If this fails, `level` and `xp` are recomputed from `totalXp` (auto-repair) because `totalXp` is the more robust counter.
4. Every key in `permanentStrengthBonuses` exists in the bonus config. Unknown keys are moved to `_unknown` (soft failure), never applied.
5. Level-ups are applied by the server only, in `ProgressionService`, after server-validated XP gains ([[Service - ProgressionService]]).

## Worked example

A player at level 9 with 520 / `xpToNext(9) = round(100 × 9^1.6) = 3,363` XP gains 3,000 XP. New `xp` = 3,520 ≥ 3,363, so `level = 10`, `xp = 157` (below `xpToNext(10) = 3,981`), `totalXp += 3,000`, and Ground Slam becomes available (derived, so no field changes for it).

## Migration notes

- If the level cap rises, no migration is needed: players at the old cap simply start earning `xp` towards the next level. Whether XP banked in `totalXp` while capped is converted retroactively is a design decision for [[Player Progression and Levelling]], not an automatic repair. A lower cap is handled by the validator clamp.
- If per-animal levelling is ever adopted (Q-021), it belongs in [[Schema - Animal Collection]], not here.

## Size estimate

About 120 bytes with an empty bonus map. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Player Progression and Levelling]]
- [[Player Strength]]
- [[Progression Score Specification]]
- [[Module - Training Grounds]]
- [[Schema - Player Profile]]
- [[Canonical Proposed Values]]
- [[Data and Balancing Index]]
