---
title: Ascension Expected Value Analysis
type: analysis
category: progression
status: proposed
priority: P1
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - ascension
  - balancing
  - analysis
  - economy
  - probability
---

# Ascension Expected Value Analysis

How long does it take to fully ascend (A5) one specific animal of each rarity? This page computes the expected rolls, Cash and hours using only canonical values, with and without merging, at the baseline P = 0.30 and at maximum progression P = 1.0. It closes with a judgement and **PROPOSED** tuning options.

> [!info] PROPOSED
> All inputs are **PROPOSED** values from [[Canonical Proposed Values]] (§5–§9, §10). The cash-per-hour model below introduces **new PROPOSED assumptions** (kill rate and average base Cash per kill), which must be validated in playtests ([[Balance Simulation Plan]]). Ascension levels and duplicate counts are **UNDECIDED** ([[Open Questions#Q-004]], [[Open Questions#Q-005]]).

## 1. Method

For a specific animal of rarity *r* with in-pool probability *q* (from [[Hatch Pool Tables]]) and egg odds *p_r(P)*:

- Per-roll chance of that animal: **p = p_r(P) × q**.
- Copies needed to reach A5: **k = 1 + total duplicates** (16 / 14 / 11 / 10 / 8 / 7 / 6 for Common to Secret; [[Ascension Progression Table]]).
- Expected rolls by direct rolling: **k / p** (negative binomial mean; [[Independent Random Outcomes]]).
- 90th percentile: the λ at which a Poisson(λ) count reaches k with 90 % probability, divided by p (accurate for small p).
- **With full merging**, every lower-rarity egg is merged up into rarity *r*. Target-rarity eggs per roll = p_r + Σ_{j<r} p_j × 3^(j − r). Merge fees are charged at the canonical §10 rates ([[Egg Merging#Merge shortcut analysis]]).
- Cash = rolls × 200 + merge fees + ascension fees (15 × FeeBase).

Simplifications: higher-rarity eggs rolled during the chase are ignored (they are a bonus, not a cost); station gates are assumed met (see §4); integer remainders of merges are ignored.

## Cash-per-hour model

**New PROPOSED assumptions** (to be added to [[Canonical Proposed Values]]):

| Assumption | Value | Rationale |
|---|---:|---|
| Effective kill rate | 240 defeats per hour (one per 15 s including travel, target choice and respawn waits) | Wild respawns of 20–120 s for Common to Epic (§6) and multiple spawn points per region |
| Average base Cash per defeat | 15 | A spawn mix of roughly 70 % Common, 20 % Uncommon, 8 % Rare, 2 % Epic gives 13.4; rounded up for occasional Legendary and rare-spawn events |
| Cash bonuses | [[Module - Multiplier Shrine]] +10 % per level; [[Module - Trophy Hall]] +1 % per unique boss trophy | §12 |
| All Cash spent on rolls and fees | Yes | Upper bound on speed; real players also buy base upgrades |

`Cash per hour = 240 × 15 × RegionMultiplier × (1 + CashBonuses)` (from §6).

| Profile | Region farmed (multiplier) | Bonuses | Cash per hour | Rolls per hour | PS profile |
|---|---|---|---:|---:|---|
| Beginner | Whisperwood Forest (×1.0) | none | 3,600 | 18.0 | P = 0.05 |
| Intermediate | Emerald Canopy (×2.2) | Shrine L2 +20 %, 4 trophies +4 % | 9,821 | 49.1 | P = 0.30 |
| Advanced | Skyreach Peaks (×6.2) | Shrine L4 +40 %, 8 trophies +8 % | 33,034 | 165.2 | P = 0.60 |
| Endgame | Starfall Sanctuary (×11.5) | Shrine L5 +50 %, 12 trophies +12 % | 67,068 | 335.3 | P = 0.95 |

Profiles match [[Progression Score Specification#Worked player profiles]]. **Sensitivity:** every figure in hours below scales inversely with kill rate. At 180 defeats per hour, multiply hours by 1.33; at 360, by 0.67. Hours at P = 0.30 use the intermediate rate; hours at P = 1.0 use the endgame rate.

## 2. Results at baseline (P = 0.30, 9,821 Cash per hour)

Two animals per rarity: the most common class (Standard) and the rarest class (Elusive). For Secret, the Scarce [[Titanoboa]] is also shown.

| Rarity | Animal (class, q) | k | Direct rolls (mean) | Direct rolls (P90) | Direct Cash | Direct hours | Merge rolls | Merge fees | Merge Cash | Merge hours |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Common | [[Rabbit]] (S, 10.20 %) | 16 | 241 | 321 | 49,746 | 5.1 | — | — | — | — |
| Common | [[Woodpecker]] (E, 3.06 %) | 16 | 804 | 1,070 | 162,321 | 16.5 | — | — | — | — |
| Uncommon | [[Fox]] (S, 10.99 %) | 14 | 579 | 784 | 118,818 | 12.1 | 292 | 6,321 | 67,673 | 6.9 |
| Uncommon | [[Penguin]] (E, 3.30 %) | 14 | 1,930 | 2,614 | 389,061 | 39.6 | 973 | 21,071 | 218,575 | 22.3 |
| Rare | [[Wolf]] (S, 11.76 %) | 11 | 1,039 | 1,455 | 213,778 | 21.8 | 397 | 25,933 | 111,320 | 11.3 |
| Rare | [[Arctic Fox]] (E, 3.53 %) | 11 | 3,463 | 4,850 | 698,593 | 71.1 | 1,323 | 86,443 | 357,066 | 36.4 |
| Epic | [[Tiger]] (S, 13.33 %) | 10 | 2,500 | 3,551 | 512,000 | 52.1 | 691 | 93,993 | 244,218 | 24.9 |
| Epic | [[Snow Leopard]] (E, 4.00 %) | 10 | 8,333 | 11,838 | 1,678,667 | 170.9 | 2,304 | 313,311 | 786,061 | 80.0 |
| Legendary | [[Lion]] (S, 15.38 %) | 8 | 6,500 | 9,564 | 1,324,000 | 134.8 | 1,177 | 275,071 | 534,510 | 54.4 |
| Legendary | [[Komodo Dragon]] (E, 4.62 %) | 8 | 21,667 | 31,880 | 4,357,333 | 443.7 | 3,924 | 916,903 | 1,725,699 | 175.7 |
| Mythical | [[Sabre-Tooth Tiger]] (S, 22.22 %) | 7 | 17,500 | 26,330 | 3,548,000 | 361.3 | 1,906 | 669,985 | 1,099,242 | 111.9 |
| Mythical | [[Giant Squid]] (E, 6.67 %) | 7 | 58,333 | 87,767 | 11,714,667 | 1,192.8 | 6,354 | 2,233,283 | 3,552,140 | 361.7 |
| Secret | [[Mosasaurus]] (S, 34.48 %) | 6 | 87,000 | 134,483 | 17,496,000 | 1,781.5 | 3,048 | 1,491,118 | 2,196,779 | 223.7 |
| Secret | [[Titanoboa]] (Sc, 20.69 %) | 6 | 145,000 | 224,138 | 29,096,000 | 2,962.6 | 5,081 | 2,485,197 | 3,597,298 | 366.3 |
| Secret | [[Tyrannosaurus Rex]] (E, 10.34 %) | 6 | 290,000 | 448,276 | 58,096,000 | 5,915.5 | 10,161 | 4,970,393 | 7,098,595 | 722.8 |

Check (Tyrannosaurus Rex, direct): p = 0.0002 × 3/29 = 2.069 × 10⁻⁵; 6 / p = **290,000 rolls**; × 200 = 58,000,000 Cash + 96,000 fees = 58,096,000 Cash; ÷ 9,821 = **5,915 hours**.

## 3. Results at maximum progression (P = 1.0, 67,068 Cash per hour)

At P = 1.0 the egg odds are 53.1386 / 25.5392 / 13.5381 / 5.5428 / 1.7528 / 0.4356 / 0.0530 %, and pool tilt raises Scarce and Elusive shares ([[Dynamic Progression Luck]]).

| Rarity | Animal (class, q) | Direct rolls | Direct P90 | Direct Cash | Direct hours | Merge rolls | Merge fees | Merge Cash | Merge hours |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Common | [[Rabbit]] (S, 9.40 %) | 320 | 426 | 65,574 | 1.0 | — | — | — | — |
| Common | [[Woodpecker]] (E, 4.79 %) | 628 | 836 | 127,135 | 1.9 | — | — | — | — |
| Uncommon | [[Fox]] (S, 10.06 %) | 545 | 738 | 111,977 | 1.7 | 322 | 5,699 | 73,047 | 1.1 |
| Uncommon | [[Penguin]] (E, 5.13 %) | 1,068 | 1,447 | 216,681 | 3.2 | 631 | 11,174 | 140,348 | 2.1 |
| Rare | [[Wolf]] (S, 10.95 %) | 742 | 1,039 | 154,367 | 2.3 | 359 | 21,902 | 99,752 | 1.5 |
| Rare | [[Arctic Fox]] (E, 5.59 %) | 1,455 | 2,037 | 296,915 | 4.4 | 704 | 42,944 | 189,827 | 2.8 |
| Epic | [[Tiger]] (S, 12.30 %) | 1,467 | 2,084 | 305,355 | 4.6 | 547 | 79,231 | 200,644 | 3.0 |
| Epic | [[Snow Leopard]] (E, 6.27 %) | 2,876 | 4,086 | 587,207 | 8.8 | 1,073 | 155,356 | 381,889 | 5.7 |
| Legendary | [[Lion]] (S, 14.03 %) | 3,254 | 4,788 | 674,860 | 10.1 | 851 | 236,939 | 431,043 | 6.4 |
| Legendary | [[Komodo Dragon]] (E, 7.15 %) | 6,381 | 9,389 | 1,300,197 | 19.4 | 1,668 | 464,587 | 822,123 | 12.3 |
| Mythical | [[Sabre-Tooth Tiger]] (S, 19.49 %) | 8,244 | 12,404 | 1,696,862 | 25.3 | 1,344 | 614,960 | 931,841 | 13.9 |
| Mythical | [[Giant Squid]] (E, 9.94 %) | 16,165 | 24,322 | 3,281,063 | 48.9 | 2,636 | 1,205,804 | 1,781,021 | 26.6 |
| Secret | [[Mosasaurus]] (S, 30.12 %) | 37,603 | 58,125 | 7,616,513 | 113.6 | 2,112 | 1,435,955 | 1,954,287 | 29.1 |
| Secret | [[Titanoboa]] (Sc, 24.40 %) | 46,423 | 71,760 | 9,380,584 | 139.9 | 2,607 | 1,772,784 | 2,390,182 | 35.6 |
| Secret | [[Tyrannosaurus Rex]] (E, 15.36 %) | 73,731 | 113,971 | 14,842,104 | 221.3 | 4,141 | 2,815,598 | 3,739,700 | 55.8 |

**Whole Secret set.** Reaching 6 copies of all four Secrets needs on average **42.0 Secret eggs** (Monte Carlo, 20,000 trials; 90th percentile 58), only slightly more than the 39.1 for [[Tyrannosaurus Rex]] alone, because the other three accumulate in parallel. At P = 1.0 that is about **64 hours** with full merging (4.30 M Cash) or **242 hours** by direct rolling (16.2 M Cash).

## 4. Gate realism

Merging columns assume the needed station level. In practice:

| Station level needed | Gate | Typical profile when reached |
|---|---|---|
| L1 (Uncommon, Rare targets) | none | Beginner |
| L2 (Epic) | Region 2 unlocked | Beginner to intermediate |
| L3 (Legendary) | Region 4 unlocked | Late intermediate (level 28+) |
| L4 (Mythical) | Region 6 + 1 world boss | Advanced (level 52+) |
| L5 (Secret) | Region 8 | Endgame (level 80+) |

So the P = 0.30 merge figures for Mythical and Secret are **theoretical**: an intermediate player cannot merge those tiers. The relevant Secret comparison is at P ≈ 0.95–1.0: **56 hours with merging versus 221 hours direct** for the hardest Secret.

## 5. Judgement

| Band | Verdict (PROPOSED) |
|---|---|
| Common to Rare | **Healthy.** A5 Standard animals in 5–22 h at baseline; minutes to a few hours at endgame. Elusive Commons (16.5 h at baseline) feel slow for a Common; acceptable as a collection goal |
| Epic and Legendary | **Healthy mid-to-late goals.** Merging halves the time. Tiger A5 ≈ 25 h with merging at baseline, 3 h at endgame |
| Mythical | **Reasonable long goal.** 14–27 h at endgame with merging |
| Secret | **Two problems in opposite directions.** Without merging, Secret A5 is an extreme chase (Tyrannosaurus Rex 221 h even at P = 1.0; 5,900 h at baseline). With merging, the entire Secret set takes about 64 h at endgame, which is short for the game's apex goal and is gated mainly by Cash, not by play variety |

> [!danger] Concerns
> 1. **Merging decides the Secret endgame.** Players who do not understand merging face a 4× longer chase. The UI must teach merging well before Station L5 ([[New Player Onboarding]], [[UI - Egg Merging]]).
> 2. **Owned-animal capacity.** At 335 rolls per hour, hatching everything fills a 100-animal collection in under 20 minutes. Surplus disposal is **UNDECIDED** (Q-305); without it the analysis above is not achievable in practice.
> 3. **Variance.** P90 values are about 1.5× the mean for Secrets (k = 6). One in ten players chasing Tyrannosaurus Rex directly at P = 1.0 needs more than 114,000 rolls (340 h).
> 4. **Elusive versus Standard ratio.** The Elusive Secret takes about 1.9× as long as a Standard Secret at P = 1.0. Combined with marketing focus on dinosaurs, Tyrannosaurus Rex will be the most-requested and slowest animal.
> 5. **Assumption risk.** The kill-rate and average-Cash assumptions drive every hour figure. Playtest telemetry must replace them before any number here is used for tuning.

## 6. Tuning options (all PROPOSED)

| Option | Effect on Tyrannosaurus Rex A5 at P = 1.0 (merge path) | Effect elsewhere | Notes |
|---|---|---|---|
| A. Keep canonical values | 55.8 h | — | Accept merging as the intended endgame path |
| B. Raise top merge fees (Legendary → Mythical 24,000; Mythical → Secret 125,000) | **132.8 h** (8.91 M Cash) | Mosasaurus 68.4 h; Giant Squid 40.6 h | Recommended first lever. Keeps rolls relevant; see [[Egg Merging#Merge shortcut analysis]] |
| C. Reclassify Tyrannosaurus Rex from Elusive to Scarce | 38.3 h (q rises from 15.36 % to 22.38 %); direct 50,600 rolls | Secret pool total becomes 32 at baseline (Titanoboa and Tyrannosaurus Rex 18.75 % each) | Reduces the outlier without touching the economy ([[Open Questions#Q-018]]) |
| D. Secret A5 needs 4 duplicates instead of 5 (k = 5) | −17 % time | Weakens the duplicate value of Secrets | Duplicates are **UNDECIDED** ([[Open Questions#Q-005]]) |
| E. Add a Secret-only ascension material from world bosses | Depends on drop design | Couples bosses to ascension | Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]); listed as an option only |
| F. Leave as is, add long-term goals beyond Secret A5 | — | — | See [[Long-Term Goals and Endgame]] |

Options B and C together give about 91 hours for Tyrannosaurus Rex (and about 75 hours for each Standard Secret), an apex chase of roughly 75–90 hours at endgame with merging, and keep direct rolling meaningful. No option breaks independence (D-018) or the 3 → 1 merge rule (D-020).

## Related documents
- [[Ascension System]] · [[Ascension Progression Table]] · [[Ascension and Progression Index]]
- [[Egg Merging]] · [[Egg Merging Station]] · [[Independent Random Outcomes]] · [[Dynamic Progression Luck]]
- [[Hatch Pool Tables]] · [[Dynamic Luck Probability Tables]]
- [[Expected Value Calculations]] · [[Progression Bottleneck Analysis]] · [[Cash Sources and Sinks]] · [[Wild Animal Cash Rewards]]
- [[Balance Simulation Plan]] · [[Long-Term Goals and Endgame]]
