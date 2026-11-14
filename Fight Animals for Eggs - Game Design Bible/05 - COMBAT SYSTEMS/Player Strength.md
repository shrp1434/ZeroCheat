---
title: Player Strength
type: system
category: combat
status: mixed
priority: P0
owner: Gameplay Systems Architect
last_updated: 2026-11-14
tags:
  - combat
  - player
  - progression
  - strength
---

# Player Strength

Player Strength is the statistic that powers the player character's own attacks. It is separate from animal strength.

> [!success] CONFIRMED
> Player strength is a separate statistic from animal strength (D-007). Base progression can contribute to multipliers, strength and progression (D-022).

> [!info] PROPOSED
> The formulas and sources below are proposals from [[Canonical Proposed Values]] §4, §12 and §13.

## 1. Definition

```
BaseStrength      = 10 + 2 × (Level − 1)
EffectiveStrength = BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)
```

- `TrainingGroundsBonus` = +5% per [[Module - Training Grounds]] level (L5 = +25%).
- `OtherStrengthBonuses` is reserved for future sources (events, temporary buffs). At launch it is 0. Any new source must be added to [[Canonical Proposed Values]] and to [[Progression Multipliers]].
- Bonuses inside the bracket are **additive** with each other.
- Strength replaces ATK in the damage formula for player attacks: `Damage = EffectiveStrength × SkillMultiplier × (100 / (100 + DEF_target)) × Random(0.95, 1.05)`.

## 2. What Strength does and does not affect

| Affects | Does not affect |
|---|---|
| Basic combo, Power Strike, Ground Slam damage | Animal stats (they come from rarity, role, species, ascension and Training Grounds animal bonus) |
| PvP player damage (subject to the PvP scalar in [[PvP System]]) | Player HP or DEF (those scale with level only) |
| Raid damage against base structures ([[Base Raiding System]]) | Egg odds, luck or rewards |
| — | Rally Cry (a percentage buff, not Strength-scaled) |

## 3. Strength curve

| Level | Base Strength | TG L0 | TG L3 (+15%) | TG L5 (+25%) | Full combo damage vs DEF 10, TG L5 |
|---:|---:|---:|---:|---:|---:|
| 1 | 10 | 10.0 | 11.5 | 12.5 | 34.1 |
| 10 | 28 | 28.0 | 32.2 | 35.0 | 95.5 |
| 25 | 58 | 58.0 | 66.7 | 72.5 | 197.7 |
| 50 | 108 | 108.0 | 124.2 | 135.0 | 368.2 |
| 75 | 158 | 158.0 | 181.7 | 197.5 | 538.6 |
| 100 | 208 | 208.0 | 239.2 | 260.0 | 709.1 |

Full combo damage = `EffectiveStrength × 3.0 × 100/110`, before ±5% variance.

## 4. Player power versus animal power

A Common reference animal has ATK 20; a Secret reference has ATK 96 (×4.8), and A5 adds +40%. Player Strength grows linearly with level (×20.8 from L1 to L100), while animal ATK grows with rarity and ascension (×6.7 from Common A0 to Secret A5, ×8.1 with Training Grounds L5).

That difference means the player's share of total damage rises as the game progresses:

| Region (on-curve team, see [[Damage, Defence and Health Model#On-curve reference teams]]) | Player level | Player share of team damage |
|---|---:|---:|
| Whisperwood Forest | 5 | 48% |
| Emerald Canopy | 24 | 61% |
| Frostfang Tundra | 47 | 66% |
| Starfall Sanctuary | 90 | 66% |

> [!warning] UNDECIDED (Q-211)
> **Should the player or the animals be the main damage source in late game?** The "team is the hero" pillar ([[Combat System Overview]]) suggests the player should stay at 30–40% of total damage. Options:
> 1. Keep the canonical curve (player becomes the main damage dealer from mid-game).
> 2. Reduce Strength growth from 2 to about 1.2 per level (player share stays near 40–45%).
> 3. Keep Strength growth but reduce combo multipliers from 0.8 / 0.8 / 1.4 to 0.6 / 0.6 / 1.0.
> 4. Add an animal-side scaling term tied to player level (larger change to the stat model).
>
> **Recommendation (PROPOSED, unapproved):** option 2. It changes one canonical number, leaves the combo feel untouched and preserves the collection pillar. The change must be made in [[Canonical Proposed Values]], not here.

## 5. Displaying Strength

- The HUD shows effective Strength with a breakdown tooltip (base + each bonus). See [[UI - Player Strength Display]].
- The comparison "player Strength versus team power" must never be presented as a single combined number. They are separate statistics (D-007).

## 6. Data and implementation
- Stored: player level and module levels only. Effective Strength is **derived** on the server at load and whenever a source changes, never saved or trusted from the client ([[Schema - Player Progression]]).
- Recalculation triggers: level up, Training Grounds upgrade completion, buff start or end.
- Illustrative Luau:

```lua
-- Illustrative Luau, not tested in Roblox Studio.
local function getEffectiveStrength(level: number, trainingLevel: number, otherBonus: number): number
	local base = 10 + 2 * (level - 1)
	return base * (1 + 0.05 * trainingLevel + otherBonus)
end
```

## 7. Test hooks
- L1, TG0 → 10.0; L50, TG3 → 124.2; L100, TG5 → 260.0.
- A client-sent Strength value is ignored; damage always uses the server-derived value ([[Test Cases - Combat]]).

## Related documents
- [[Player Combat]]
- [[Damage, Defence and Health Model]]
- [[Module - Training Grounds]]
- [[Player Progression and Levelling]]
- [[Progression Multipliers]]
- [[UI - Player Strength Display]]
- [[Animal Stat Budget Model]]
