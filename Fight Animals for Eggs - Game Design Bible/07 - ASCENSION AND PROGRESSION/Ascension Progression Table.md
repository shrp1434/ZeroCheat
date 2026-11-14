---
title: Ascension Progression Table
type: spec
category: progression
status: proposed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - ascension
  - progression
  - data
  - balancing
---

# Ascension Progression Table

The step-by-step numbers for every rarity and ascension level. Rules and flows live in [[Ascension System]]; time-to-complete analysis lives in [[Ascension Expected Value Analysis]].

> [!info] PROPOSED (D-037)
> Source: [[Canonical Proposed Values]] §9. Five levels are a working assumption (**UNDECIDED**, [[Open Questions#Q-004]]); duplicate counts are **UNDECIDED** ([[Open Questions#Q-005]]). Cumulative columns are derived here.

**Fee formula:** step *n* costs `FeeBase(rarity) × n`, where FeeBase is 100 / 200 / 400 / 800 / 1,600 / 3,200 / 6,400 for Common to Secret. Total fees to A5 = FeeBase × (1 + 2 + 3 + 4 + 5) = **15 × FeeBase**.

## Step tables by rarity

### Common (FeeBase 100)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees | HP / ATK / DEF | Ability | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 → A1 | 1 | 1 | 2 | 100 | 100 | ×1.08 | +5 % | Coloured trim |
| A1 → A2 | 2 | 3 | 4 | 200 | 300 | ×1.16 | +10 % | Eye glint |
| A2 → A3 | 3 | 6 | 7 | 300 | 600 | ×1.24 | +15 % | Soft aura |
| A3 → A4 | 4 | 10 | 11 | 400 | 1,000 | ×1.32 | +20 % | Particle accents |
| A4 → A5 | 5 | 15 | 16 | 500 | 1,500 | ×1.40 | +25 % | Crest and full aura |

### Uncommon (FeeBase 200)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 200 | 200 |
| A1 → A2 | 2 | 3 | 4 | 400 | 600 |
| A2 → A3 | 3 | 6 | 7 | 600 | 1,200 |
| A3 → A4 | 3 | 9 | 10 | 800 | 2,000 |
| A4 → A5 | 4 | 13 | 14 | 1,000 | 3,000 |

### Rare (FeeBase 400)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 400 | 400 |
| A1 → A2 | 1 | 2 | 3 | 800 | 1,200 |
| A2 → A3 | 2 | 4 | 5 | 1,200 | 2,400 |
| A3 → A4 | 3 | 7 | 8 | 1,600 | 4,000 |
| A4 → A5 | 3 | 10 | 11 | 2,000 | 6,000 |

### Epic (FeeBase 800)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 800 | 800 |
| A1 → A2 | 1 | 2 | 3 | 1,600 | 2,400 |
| A2 → A3 | 2 | 4 | 5 | 2,400 | 4,800 |
| A3 → A4 | 2 | 6 | 7 | 3,200 | 8,000 |
| A4 → A5 | 3 | 9 | 10 | 4,000 | 12,000 |

### Legendary (FeeBase 1,600)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 1,600 | 1,600 |
| A1 → A2 | 1 | 2 | 3 | 3,200 | 4,800 |
| A2 → A3 | 1 | 3 | 4 | 4,800 | 9,600 |
| A3 → A4 | 2 | 5 | 6 | 6,400 | 16,000 |
| A4 → A5 | 2 | 7 | 8 | 8,000 | 24,000 |

### Mythical (FeeBase 3,200)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 3,200 | 3,200 |
| A1 → A2 | 1 | 2 | 3 | 6,400 | 9,600 |
| A2 → A3 | 1 | 3 | 4 | 9,600 | 19,200 |
| A3 → A4 | 1 | 4 | 5 | 12,800 | 32,000 |
| A4 → A5 | 2 | 6 | 7 | 16,000 | 48,000 |

### Secret (FeeBase 6,400)

| Step | Duplicates | Cumulative duplicates | Copies owned incl. target | Fee | Cumulative fees |
|---|---:|---:|---:|---:|---:|
| A0 → A1 | 1 | 1 | 2 | 6,400 | 6,400 |
| A1 → A2 | 1 | 2 | 3 | 12,800 | 19,200 |
| A2 → A3 | 1 | 3 | 4 | 19,200 | 38,400 |
| A3 → A4 | 1 | 4 | 5 | 25,600 | 64,000 |
| A4 → A5 | 1 | 5 | 6 | 32,000 | 96,000 |

The stat, ability and visual columns shown for Common are identical for every rarity: +8 % HP / ATK / DEF and +5 % ability effectiveness per level, with the same visual tier per level ([[Ascension System#Visual tiers]]).

## Effective tier multipliers

Combined multiplier on HP, ATK and DEF = rarity multiplier *M* × (1 + 0.08 × A). This is the number to compare animals of different rarities and ascension levels (before role and species tweaks).

| Rarity (M) | A0 | A1 | A2 | A3 | A4 | A5 |
|---|---:|---:|---:|---:|---:|---:|
| Common (1.00) | 1.000 | 1.080 | 1.160 | 1.240 | 1.320 | 1.400 |
| Uncommon (1.30) | 1.300 | 1.404 | 1.508 | 1.612 | 1.716 | 1.820 |
| Rare (1.70) | 1.700 | 1.836 | 1.972 | 2.108 | 2.244 | 2.380 |
| Epic (2.20) | 2.200 | 2.376 | 2.552 | 2.728 | 2.904 | 3.080 |
| Legendary (2.85) | 2.850 | 3.078 | 3.306 | 3.534 | 3.762 | 3.990 |
| Mythical (3.70) | 3.700 | 3.996 | 4.292 | 4.588 | 4.884 | 5.180 |
| Secret (4.80) | 4.800 | 5.184 | 5.568 | 5.952 | 6.336 | 6.720 |

**Crossover rule.** At every tier, **A4** is the first level that exceeds A0 of the next rarity (Common A4 1.320 > Uncommon A0 1.300; Mythical A4 4.884 > Secret A0 4.800), and A3 always falls short. A5 of one rarity is almost exactly A1 of the next (within 0.02, for example Epic A5 3.080 versus Legendary A1 3.078). Changing the +8 % step or the tier multipliers moves this crossover; [[Animal Stat Budget Model]] owns the decision.

## Summary per rarity

| Rarity | Copies to A5 | Total duplicates | Total fees | Fees as rolls (at 200 Cash) |
|---|---:|---:|---:|---:|
| Common | 16 | 15 | 1,500 | 7.5 |
| Uncommon | 14 | 13 | 3,000 | 15 |
| Rare | 11 | 10 | 6,000 | 30 |
| Epic | 10 | 9 | 12,000 | 60 |
| Legendary | 8 | 7 | 24,000 | 120 |
| Mythical | 7 | 6 | 48,000 | 240 |
| Secret | 6 | 5 | 96,000 | 480 |

Ascension fees are small next to the cost of collecting the duplicates (for example, Secret fees of 96,000 Cash versus several million Cash of rolls; see [[Ascension Expected Value Analysis]]). They act as a pacing tax at the moment of ascending, not as a main sink.

## Data representation (PROPOSED)

```lua
-- Illustrative Luau configuration (not executed).
local AscensionConfig = table.freeze({
	maxLevel = 5,
	statPerLevel = 0.08,
	abilityPerLevel = 0.05,
	duplicates = { -- index by rarity 0..6, then step 1..5
		[0] = { 1, 2, 3, 4, 5 }, [1] = { 1, 2, 3, 3, 4 }, [2] = { 1, 1, 2, 3, 3 },
		[3] = { 1, 1, 2, 2, 3 }, [4] = { 1, 1, 1, 2, 2 }, [5] = { 1, 1, 1, 1, 2 },
		[6] = { 1, 1, 1, 1, 1 },
	},
	feeBase = { [0] = 100, [1] = 200, [2] = 400, [3] = 800, [4] = 1600, [5] = 3200, [6] = 6400 },
})
-- fee for step n = feeBase[rarity] * n
```

Lives in [[Configuration Modules]].

## Related documents
- [[Ascension System]] · [[Ascension Expected Value Analysis]] · [[Ascension and Progression Index]]
- [[Animal Stat Budget Model]] · [[Animal Statistics Database]]
- [[UI - Ascension]] · [[Test Cases - Ascension]]
- [[Canonical Proposed Values]]
