---
title: Dynamic Luck Probability Tables
type: spec
category: eggs
status: proposed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - probability
  - luck
  - balancing
---

# Dynamic Luck Probability Tables

> [!info] PROPOSED, generated
> Egg-rarity odds at sample progression levels, computed from the formula in [[Canonical Proposed Values]] §8. The final formula is **UNDECIDED** ([[Open Questions#Q-017]]); the final probabilities are **UNDECIDED** ([[Open Questions#Q-016]]). The mechanism is explained in [[Dynamic Progression Luck]]. Progression Score inputs are in [[Progression Score Specification]].

> [!important] Disclosure
> Players never see this table or the formula. Before every roll, they see **their own exact current odds**, computed by the server ([[Decision Register|D-017]], [[Randomised Reward Compliance]]).

## Formula

```text
P    = clamp(ProgressionScore / 1000, 0, 1)
w_r  = Base_r × (1 + s_r × (P − 0.30))
Odds = w_r / Σ w   (all seven rarities)
```

## Egg-rarity odds by progression

| P | PS | Common | Uncommon | Rare | Epic | Legendary | Mythical | Secret | Sum |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 0 | 71.88% | 19.95% | 6.369% | 1.526% | 0.2477% | 0.0318% | 0.00088% | 100.0000% |
| 0.1 | 100 | 69.43% | 20.68% | 7.306% | 2.051% | 0.4443% | 0.0846% | 0.00769% | 100.0000% |
| 0.2 | 200 | 67.14% | 21.36% | 8.181% | 2.541% | 0.6280% | 0.1339% | 0.0140% | 100.0000% |
| 0.3 | 300 | 65.00% | 22.00% | 9.000% | 3.000% | 0.8000% | 0.1800% | 0.0200% | 100.0000% |
| 0.4 | 400 | 62.99% | 22.60% | 9.769% | 3.431% | 0.9613% | 0.2233% | 0.0256% | 100.0000% |
| 0.5 | 500 | 61.10% | 23.16% | 10.49% | 3.835% | 1.113% | 0.2640% | 0.0308% | 100.0000% |
| 0.6 | 600 | 59.32% | 23.69% | 11.17% | 4.217% | 1.256% | 0.3023% | 0.0358% | 100.0000% |
| 0.7 | 700 | 57.65% | 24.19% | 11.81% | 4.576% | 1.391% | 0.3384% | 0.0404% | 100.0000% |
| 0.8 | 800 | 56.06% | 24.67% | 12.42% | 4.916% | 1.518% | 0.3726% | 0.0448% | 100.0000% |
| 0.9 | 900 | 54.56% | 25.11% | 12.99% | 5.238% | 1.639% | 0.4049% | 0.0490% | 100.0000% |
| 1.0 | 1000 | 53.14% | 25.54% | 13.54% | 5.543% | 1.753% | 0.4356% | 0.0530% | 100.0000% |

Every row sums to 100% before display rounding. Rounded values shown to players must use a largest-remainder method so the displayed numbers also sum to exactly 100% ([[Randomised Reward Compliance]]).

## Expected rolls to obtain one egg of each rarity

Expected rolls = 1 / p (geometric distribution; see [[Independent Random Outcomes]]). Merging is excluded.

| P | Uncommon | Rare | Epic | Legendary | Mythical | Secret |
|---:|---:|---:|---:|---:|---:|---:|
| 0.0 | 5 | 16 | 66 | 404 | 3,140 | 113,042 |
| 0.3 | 5 | 11 | 33 | 125 | 556 | 5,000 |
| 0.6 | 4 | 9 | 24 | 80 | 331 | 2,795 |
| 1.0 | 4 | 7 | 18 | 57 | 230 | 1,888 |

## Player profile examples

| Profile | Example PS | P | Rare+ total | Legendary | Mythical | Secret |
|---|---:|---:|---:|---:|---:|---:|
| Beginner (first session) | 50 | 0.05 | 9.049% | 0.3477% | 0.0587% | 0.00435% |
| Intermediate (baseline pivot) | 300 | 0.30 | 13.00% | 0.8000% | 0.1800% | 0.0200% |
| Advanced | 600 | 0.60 | 16.98% | 1.256% | 0.3023% | 0.0358% |
| Endgame | 950 | 0.95 | 20.83% | 1.696% | 0.4205% | 0.0510% |

The profile breakdowns (which inputs produce each PS) are in [[Progression Score Specification]].

## Luck multiplier relative to baseline

| Rarity | P = 0.0 | P = 0.3 | P = 0.6 | P = 1.0 |
|---|---:|---:|---:|---:|
| Common | ×1.11 | ×1.00 | ×0.91 | ×0.82 |
| Uncommon | ×0.91 | ×1.00 | ×1.08 | ×1.16 |
| Rare | ×0.71 | ×1.00 | ×1.24 | ×1.50 |
| Epic | ×0.51 | ×1.00 | ×1.41 | ×1.85 |
| Legendary | ×0.31 | ×1.00 | ×1.57 | ×2.19 |
| Mythical | ×0.18 | ×1.00 | ×1.68 | ×2.42 |
| Secret | ×0.04 | ×1.00 | ×1.79 | ×2.65 |

Common odds fall as P rises because the other weights grow while the Common weight stays fixed. This is the intended source of luck: the formula never removes Common eggs entirely.

## Related documents

[[Dynamic Progression Luck]] · [[Hatch Pool Tables]] · [[Egg Roll System]] · [[Implementation - Dynamic Luck Calculation]] · [[Statistical Testing of Probabilities]]
