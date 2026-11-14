---
title: Expected Value Calculations
type: analysis
category: economy
status: proposed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - expected-value
  - eggs
  - merging
  - balancing
---

# Expected Value Calculations

Expected Cash costs for eggs of every rarity, the comparison between direct rolling and the merge chain, ascension targets and time to a maxed base. All inputs are **PROPOSED** values from [[Canonical Proposed Values]]; computed with python3 for this document (calculation scripts were temporary and are not part of the vault). Results are expectations, not guarantees: every roll and hatch is independent (D-018).

## 1. Egg-rarity odds used

Odds from the §8 luck model, `w_r(P) = Base_r × (1 + s_r × (P − 0.30))`, normalised. Authoritative table: [[Dynamic Luck Probability Tables]].

| P | Common | Uncommon | Rare | Epic | Legendary | Mythical | Secret |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 71.876% | 19.948% | 6.369% | 1.526% | 0.248% | 0.0318% | 0.0009% |
| 0.30 (pivot) | 65.000% | 22.000% | 9.000% | 3.000% | 0.800% | 0.1800% | 0.0200% |
| 0.50 | 61.103% | 23.163% | 10.491% | 3.835% | 1.113% | 0.2640% | 0.0308% |
| 0.70 | 57.647% | 24.194% | 11.813% | 4.576% | 1.391% | 0.3384% | 0.0404% |
| 1.00 | 53.139% | 25.539% | 13.538% | 5.543% | 1.753% | 0.4356% | 0.0530% |

## 2. Cash per egg by direct roll

Expected Cash to obtain one egg of rarity *r* = `200 / p_r`.

| P | Common | Uncommon | Rare | Epic | Legendary | Mythical | Secret |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 278 | 1,003 | 3,140 | 13,106 | 80,744 | 628,011 | 22,608,400 |
| 0.30 | 308 | 909 | 2,222 | 6,667 | 25,000 | 111,111 | 1,000,000 |
| 0.50 | 327 | 863 | 1,906 | 5,215 | 17,969 | 75,768 | 648,644 |
| 0.70 | 347 | 827 | 1,693 | 4,370 | 14,382 | 59,096 | 494,540 |
| 1.00 | 376 | 783 | 1,477 | 3,608 | 11,411 | 45,917 | 377,536 |

### Variance for a Secret egg by direct roll

| P | Rolls for a 50% chance of ≥ 1 Secret | Cash | Rolls for 90% | Cash |
|---:|---:|---:|---:|---:|
| 0.30 | 3,465 | 693,000 | 11,512 | 2,302,000 |
| 1.00 | 1,307 | 261,500 | 4,343 | 868,700 |

## 3. Merge chain

Merging: 3 same-rarity eggs → 1 egg of the next rarity (**CONFIRMED**). Fees and station gates **PROPOSED** ([[Cost Tables]]).

### Method

Each rolled egg is worth `3^r` **Common-equivalents (CE)** because three of tier *r* merge into one of tier *r + 1*. The expected CE per roll is `Σ p_r × 3^r`. A Secret egg is 729 CE. Merge fees are counted for every merge actually performed when all rolled eggs below the target are fed upward (mixed inputs, fractional expectations).

| P | CE per roll | Cash per CE |
|---:|---:|---:|
| 0.00 | 2.587 | 77.3 |
| 0.30 | 4.161 | 48.1 |
| 0.50 | 5.053 | 39.6 |
| 0.70 | 5.845 | 34.2 |
| 1.00 | 6.877 | 29.1 |

### Cost of each rarity via rolling and merging (mixed inputs)

| Target | P = 0.30 rolls | Roll Cash | Merge fees | **Total** | Direct roll | Direct ÷ merge | P = 1.00 total | Direct ÷ merge |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Uncommon | 2.3 | 458 | 50 | **508** | 909 | 1.79 | 503 | 1.56 |
| Rare | 4.2 | 849 | 277 | **1,126** | 2,222 | 1.97 | 934 | 1.58 |
| Epic | 9.2 | 1,843 | 1,253 | **3,096** | 6,667 | 2.15 | 2,320 | 1.56 |
| Legendary | 22.6 | 4,528 | 5,290 | **9,817** | 25,000 | 2.55 | 7,136 | 1.60 |
| Mythical | 60.5 | 12,103 | 21,269 | **33,373** | 111,111 | 3.33 | 24,613 | 1.87 |
| Secret | 175.2 | 35,038 | 85,696 | **120,734** | 1,000,000 | 8.28 | 93,288 | 4.05 |

### Pure-Common chain (worst case, every input a Common)

| Target | Commons | Roll Cash (P = 0.30, 308 per Common) | Fees | Total |
|---|---:|---:|---:|---:|
| Legendary | 81 | 24,923 | 10,800 | 35,723 |
| Mythical | 243 | 74,769 | 40,400 | 115,169 |
| Secret | 729 | 224,308 | 146,200 | 370,508 |

### Findings

1. **Merging is always cheaper in expectation than direct rolling**, by ~1.6–2.6× for Uncommon to Legendary and by **~4–8× for Secret**. Merge fees, not rolls, are the real price of high rarity: at P = 0.30 fees are ~71% of the Secret chain's cost.
2. The Secret advantage is bounded by **access**: the Mythical → Secret merge needs station L5 (1,000,000 Cash, Region 8). Including the station, the first merged Secret costs ~1.42 million Cash of cumulative station and chain spend at P = 1.0 (1,327,500 + ~93,300), which is above the direct-roll expectation of ~377,500; every subsequent Secret costs ~93,000.
3. Because merging is deterministic given eggs and fees, it gives a **predictable path** to high rarity, which supports the fairness charter ([[Design Principles and Fairness Charter]]).

> [!warning] UNDECIDED (Q-405)
> Should the merge path be this much cheaper than the direct roll? Options: (a) keep it (merging is the intended late sink, D-038); (b) raise high-tier fees so the Secret ratio is ~2×; (c) lower the Secret roll weight further so direct Secrets are pure luck moments. Recommendation (**PROPOSED**): (a) for launch, with telemetry on the share of Secrets obtained by merge.

### Time and throughput

At P = 1.0 one Secret via the chain takes ~106 rolls and ~52.5 merges. At 2.5–6 s per merge animation (canonical §10) that is ~3.5 minutes of merging per Secret, which is acceptable. Storage needed at any moment is small if merges are done as eggs arrive.

## 4. Ascension targets

Secret pool weights at P = 1.0 (H = 1.0): Standard 10, Scarce 8.1, Elusive 5.1 ([[Hatch Pool Tables]]). A5 needs the original plus 5 duplicates = 6 copies; fees 96,000.

| Secret animal | Pool class | Hatch chance at P = 1.0 | Expected Secret eggs for 6 copies | Expected Cash (merge path) |
|---|---|---:|---:|---:|
| [[Mosasaurus]] | Standard | 30.1% | 19.9 | ~1.95 million |
| [[Quetzalcoatlus]] | Standard | 30.1% | 19.9 | ~1.95 million |
| [[Titanoboa]] | Scarce | 24.4% | 24.6 | ~2.39 million |
| [[Tyrannosaurus Rex]] | Elusive | 15.4% | 39.1 | ~3.74 million |

At the endgame maximum (~101,000 Cash per hour) an A5 Tyrannosaurus Rex is ~37 hours of play in expectation. This is the deepest Cash goal in the game and a healthy long-term target ([[Long-Term Goals and Endgame]], [[Ascension Expected Value Analysis]]).

## 5. Time to max base

Simulation (solo, income from [[Wild Animal Cash Rewards]], Shrine bought first, then cheapest available item; trophies earned as regions are cleared):

| Share of income spent on the base | 10 of 44 levels | 20 levels | 30 levels | 40 levels | All 44 levels |
|---:|---:|---:|---:|---:|---:|
| 30% | 9.8 h | 22.8 h | 46.0 h | 85.3 h | 140.1 h |
| 50% | 6.4 h | 15.7 h | 32.9 h | 63.2 h | **118.2 h** |
| 70% | 4.7 h | 12.2 h | 26.1 h | 51.0 h | 118.2 h |
| 100% | 3.5 h | 9.7 h | 21.0 h | 41.2 h | 118.2 h |

At ≥ 50% spend, the last level is gated by the **Region 8 unlock** (station L5), not by Cash. At 2 hours of play per day, a maxed base takes ~2 months.

## Related documents
- [[Cost Tables]]
- [[Egg Pricing]]
- [[Egg Merging]]
- [[Egg Merging Station]]
- [[Dynamic Luck Probability Tables]]
- [[Hatch Pool Tables]]
- [[Ascension Expected Value Analysis]]
- [[Progression Bottleneck Analysis]]
- [[Probability Balancing]]
