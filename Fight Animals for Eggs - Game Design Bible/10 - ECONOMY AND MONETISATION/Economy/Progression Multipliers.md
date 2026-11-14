---
title: Progression Multipliers
type: spec
category: economy
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - multipliers
  - progression
  - balancing
---

# Progression Multipliers

Every multiplier that scales income, combat power or odds, how they stack, and their maximum values. Values are from [[Canonical Proposed Values]]; this page owns the **stacking rules** for the economy. The combat damage pipeline itself is owned by [[Damage, Defence and Health Model]].

> [!success] CONFIRMED
> Base progression can contribute to multipliers, strength and progression (D-022). Progression luck changes egg-rarity and hatch odds but not wild encounter rarity (D-017).

## 1. Register of multipliers

| # | Multiplier | Applies to | Value | Stacking | Source | Status |
|---:|---|---|---|---|---|---|
| 1 | Region multiplier | Wild HP and ATK, Cash, XP | ×1.0 to ×11.5 | Multiplicative | [[Region Unlock Progression]] | **PROPOSED** |
| 2 | Wild HP / ATK multiplier | Wild animals versus companion stats | HP ×2.0, ATK ×0.75 | Multiplicative | §4 | **PROPOSED** |
| 3 | Multiplier Shrine | Cash | +10% per level, max +50% | Additive in `CashBonuses` | [[Module - Multiplier Shrine]] | **PROPOSED** |
| 4 | Trophy Hall | Cash | +1% per displayed unique trophy, max +12% | Additive in `CashBonuses` | [[Module - Trophy Hall]] | **PROPOSED** |
| 5 | Training Grounds (player) | Player Strength | +5% per level, max +25% | Additive with other Strength bonuses | [[Module - Training Grounds]] | **PROPOSED** |
| 6 | Training Grounds (animals) | HP, ATK, DEF of the 3 equipped animals | +4% per level, max +20% | Multiplicative after ascension (**PROPOSED** order) | [[Module - Training Grounds]] | **PROPOSED** |
| 7 | Rarity tier *M* | Animal HP, ATK, DEF | 1.00 to 4.80 | Multiplicative | [[Animal Stat Budget Model]] | **PROPOSED** |
| 8 | Ascension | Animal HP, ATK, DEF | +8% of base per level, max +40% | Additive within ascension | [[Ascension System]] | **PROPOSED** |
| 9 | Ascension (abilities) | Ability damage, heal, duration | +5% per level, max +25% | Additive within ascension | [[Ascension System]] | **PROPOSED** |
| 10 | Rally Cry | Team damage | +15% for 6 s | Temporary | [[Player Combat]] | **PROPOSED** |
| 11 | Progression luck | Egg-rarity and hatch weights | Slope per rarity around P = 0.30 | Odds re-normalised | [[Dynamic Progression Luck]] | **PROPOSED** (formula **UNDECIDED** [[Open Questions#Q-017]]) |
| 12 | Robux boosts | — | **None proposed for Cash** | — | [[Monetisation Product Concepts]] | D-044 **PROPOSED**; [[Open Questions#Q-032]] |

## 2. Cash stack

```
Cash = round( BaseCash × RegionMultiplier × (1 + ShrineBonus + TrophyBonus) )
```

| Case | Region | CashBonuses | Effective multiplier on base Cash |
|---|---:|---:|---:|
| New player | ×1.0 | 0 | ×1.00 |
| Mid-game (Region 4, Shrine L3, 5 trophies) | ×3.2 | 0.35 | ×4.32 |
| Endgame maximum | ×11.5 | 0.62 | ×18.63 |

> [!info] PROPOSED rule: one additive bucket
> All Cash bonuses share one additive bucket. Additive stacking keeps the late-game ceiling at ×18.63 rather than letting multiplicative bonuses compound unpredictably, and any future bonus source must enter the same bucket with a stated cap.

## 3. Combat power stack

```
AnimalStat = Reference × M(rarity) × Role × SpeciesTweak × (1 + 0.08 × AscensionLevel) × (1 + 0.04 × TrainingLevel)
PlayerStrength = (10 + 2 × (Level − 1)) × (1 + 0.05 × TrainingLevel + OtherStrengthBonuses)
```

| Case | Animal ATK (Bruiser) | Player Strength |
|---|---:|---:|
| Common, A0, no grounds, level 1 | 20.0 | 10.0 |
| Rare, A2, grounds L3, level 40 | 20 × 1.70 × 1.16 × 1.12 = 44.2 | 88 × 1.15 = 101.2 |
| Secret, A5, grounds L5, level 100 | 20 × 4.80 × 1.40 × 1.20 = 161.3 | 208 × 1.25 = 260.0 |

Maximum non-rarity growth for an animal: `1.40 × 1.20 = ×1.68`. This is deliberately smaller than the rarity range (×4.8), so rarity remains the main power axis and base investment is a steady supplement.

## 4. Odds "multiplier" (luck)

Luck is not a Cash multiplier, but it changes the effective price of rarity. At P = 1.0 compared with P = 0.30:

| Rarity | Raw weight multiplier at P = 1.0 | Direct-roll Cash per egg at P = 0.30 | At P = 1.0 |
|---|---:|---:|---:|
| Common | 1.00 | 308 | 376 |
| Rare | 1.84 | 2,222 | 1,477 |
| Legendary | 2.68 | 25,000 | 11,411 |
| Secret | 3.24 | 1,000,000 | 377,536 |

(Raw weight multipliers are `1 + s_r × (P − 0.30)`; final odds are re-normalised, which is why Common becomes slightly more expensive. Full table: [[Dynamic Luck Probability Tables]].) Because base levels contribute up to 120 of 1,000 PS, a full base alone moves P by +0.12; every base upgrade therefore also **invalidates the odds token** ([[Base Upgrade System]]).

## 5. Rules for adding a multiplier (PROPOSED)

1. State which bucket it enters (Cash additive, Strength additive, animal multiplicative, odds).
2. State a cap. No uncapped multiplier may ship.
3. If it can be obtained with Robux in any way, it must be reviewed against D-027, D-044 and [[Roblox Monetisation Policy Requirements]] before design continues. A Robux-obtainable Cash multiplier makes Cash indirectly purchasable ([[Open Questions#Q-032]]).
4. Add it to [[Canonical Proposed Values]] and this register.

## Related documents
- [[Economy Overview]]
- [[Wild Animal Cash Rewards]]
- [[Module - Multiplier Shrine]]
- [[Module - Trophy Hall]]
- [[Module - Training Grounds]]
- [[Player Strength]]
- [[Dynamic Progression Luck]]
- [[Expected Value Calculations]]
