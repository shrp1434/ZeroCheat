---
title: Statistical Testing of Probabilities
type: qa
category: qa
status: proposed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - statistics
  - probability
  - eggs
  - luck
  - compliance
---

# Statistical Testing of Probabilities

How QA proves that egg rolls, hatches and rare spawns follow the odds the game discloses, that dynamic progression luck produces exactly the intended odds, and that every outcome is independent. This page is the method; the individual test cases are in [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Egg Merging]] and [[Test Cases - Animal AI]].

> [!success] CONFIRMED rules under test
> - Two-stage randomness: roll decides rarity, hatch picks an animal from that rarity's pool (D-015).
> - Progression luck changes egg-rarity and hatch odds, never wild encounter rarity. Actual odds are shown before commit and never change silently after purchase (D-017).
> - Every hatch is independent: no duplicate protection, no bias towards unowned animals, no history influence (D-018).

> [!info] PROPOSED
> All odds, slopes, pool weights and spawn chances tested here are **PROPOSED** values from [[Canonical Proposed Values]] §6–§8 (final values **UNDECIDED**: [[Open Questions#Q-016]], [[Open Questions#Q-017]], [[Open Questions#Q-018]]). The methods, significance levels and sample sizes on this page are **PROPOSED** QA standards. When the owner changes a value, the expected-value tables below are regenerated; the method does not change.

All numbers below were computed with Python 3 from the canonical formulas (not from Roblox). The generator tables [[Dynamic Luck Probability Tables]] and [[Hatch Pool Tables]] must agree with them to six decimal places; any disagreement is an S2 data bug.

## 1. Two kinds of test

| Kind | Question answered | Pass criterion | Run cost |
|---|---|---|---|
| **Deterministic** (exact) | Does the code compute the intended odds and map a random number to the intended outcome? | Exact equality within floating-point tolerance `1e-9` | Milliseconds |
| **Statistical** (sampling) | Does the full pipeline (RNG, selection, service, storage) produce outcomes at the intended rates, independently? | A hypothesis test does not reject at the stated significance level | Seconds to minutes in the offline harness |

Deterministic tests come first. A statistical test cannot tell you *why* rates are wrong, and it can miss small errors. A deterministic test pins the formula to exact values and catches off-by-one and boundary errors that sampling would need millions of draws to detect.

## 2. The luck formula as a pure function

`LuckService` exposes `computeRarityOdds(P)` and `computePoolOdds(rarity, P)` as pure functions ([[Implementation - Dynamic Luck Calculation]]). Tests call them directly with fixed `P` and compare to the exact values below.

**Formula** ([[Canonical Proposed Values]] §8): `w_r(P) = Base_r × (1 + s_r × (P − 0.30))`, normalised to 100%. `P = clamp(PS / 1000, 0, 1)`.

### 2.1 Exact expected egg-rarity odds (%)

| P | Raw weight sum | Common | Uncommon | Rare | Epic | Legendary | Mythical | Secret |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.000 | 90.433600 | 71.875940 | 19.948338 | 6.369314 | 1.525981 | 0.247696 | 0.031847 | 0.000885 |
| 0.004 | 90.561152 | 71.774705 | 19.978544 | 6.408046 | 1.547683 | 0.255827 | 0.034028 | 0.001166 |
| 0.100 | 93.622400 | 69.427829 | 20.678812 | 7.305944 | 2.050791 | 0.444338 | 0.084595 | 0.007690 |
| 0.215 | 97.289520 | 66.810896 | 21.459660 | 8.307164 | 2.611792 | 0.654541 | 0.140981 | 0.014966 |
| 0.300 | 100.000000 | 65.000000 | 22.000000 | 9.000000 | 3.000000 | 0.800000 | 0.180000 | 0.020000 |
| 0.500 | 106.377600 | 61.103089 | 23.162771 | 10.490930 | 3.835394 | 1.113016 | 0.263965 | 0.030834 |
| 0.700 | 112.755200 | 57.647009 | 24.194006 | 11.813202 | 4.576286 | 1.390623 | 0.338432 | 0.040442 |
| 1.000 | 122.321600 | 53.138612 | 25.539234 | 13.538083 | 5.542766 | 1.752757 | 0.435573 | 0.052975 |

### 2.2 Required properties (deterministic test cases)

| Property | Assertion |
|---|---|
| Pivot | `computeRarityOdds(0.30)` returns exactly 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 |
| Sum | Every output sums to 100 within `1e-9` |
| Positivity | Every tier is strictly positive for every `P` in [0, 1] (the smallest slope factor is Secret at P = 0: `1 + 3.2 × (−0.30) = 0.04`) |
| Monotonicity | Common is non-increasing and every other tier is non-decreasing in `P`, checked on a grid of 1,001 points |
| Clamp | `PS = −50` gives the P = 0 row; `PS = 1,250` gives the P = 1 row |
| Purity | Calling the function 10,000 times with the same `P` gives identical results; no global state changes |
| No wild effect | `SpawnService` rarity selection produces identical results for the same seed whatever the player's `P` (D-017) |

### 2.3 Worked Progression Score example

A level-20 player with 15 species discovered, 2 unique mini-bosses, no world bosses, 2 regions unlocked beyond the first and 11 of 44 total module levels:

| Input | Points |
|---|---:|
| Level 20 × 4 | 80 |
| 15 species × 3 | 45 |
| 2 mini-bosses × 10 | 20 |
| 0 world bosses | 0 |
| 2 regions × 20 | 40 |
| Base: `round(120 × 11 / 44)` = `round(30.0)` | 30 |
| **PS** | **215** |

`P = 0.215`. The expected odds are the 0.215 row of table 2.1 (Secret 0.014966%). A brand-new level-1 player with nothing else has `PS = 4`, `P = 0.004` (Secret 0.001166%).

> [!note] Rounding edge
> `round(120 × 1 / 44) = round(2.727) = 3`. The base-progression term must use the rounding rule in [[Progression Score Specification]]; QA tests `TotalModuleLevels` = 0, 1, 11, 22, 33 and 44, expecting 0, 3, 30, 60, 90 and 120.

### 2.4 Exact expected hatch-pool odds (% per animal)

`w_i(P) = ClassWeight_i × (1 + 1.0 × (P − 0.30) × Tilt_i)`; Standard 10 / tilt 0, Scarce 6 / tilt 0.5, Elusive 3 / tilt 1.0. Class counts come from the roster in [[Canonical Proposed Values]] §2.

| Pool | Animals (S / Sc / E) | P = 0: S / Sc / E | P = 0.30: S / Sc / E | P = 1.0: S / Sc / E |
|---|---|---|---|---|
| Common | 12 (8 / 2 / 2) | 10.5932 / 5.4025 / 2.2246 | 10.2041 / 6.1224 / 3.0612 | 9.3985 / 7.6128 / 4.7932 |
| Uncommon | 11 (7 / 3 / 1) | 11.4416 / 5.8352 / 2.4027 | 10.9890 / 6.5934 / 3.2967 | 10.0604 / 8.1489 / 5.1308 |
| Rare | 10 (7 / 2 / 1) | 12.1507 / 6.1968 / 2.5516 | 11.7647 / 7.0588 / 3.5294 | 10.9529 / 8.8719 / 5.5860 |
| Epic | 9 (6 / 2 / 1) | 13.8313 / 7.0539 / 2.9046 | 13.3333 / 8.0000 / 4.0000 | 12.3001 / 9.9631 / 6.2731 |
| Legendary | 8 (5 / 2 / 1) | 16.0514 / 8.1862 / 3.3708 | 15.3846 / 9.2308 / 4.6154 | 14.0252 / 11.3604 / 7.1529 |
| Mythical | 6 (3 / 2 / 1) | 23.6407 / 12.0567 / 4.9645 | 22.2222 / 13.3333 / 6.6667 | 19.4932 / 15.7895 / 9.9415 |
| Secret | 4 (2 / 1 / 1) | 36.7647 / 18.7500 / 7.7206 | 34.4828 / 20.6897 / 10.3448 | 30.1205 / 24.3976 / 15.3614 |

**Two-stage product check.** The chance that one roll eventually becomes a [[Tyrannosaurus Rex]] (Secret, Elusive) is `Secret odds × Elusive share`: 0.000068% at P = 0 (1 in 1,464,163), 0.002069% at P = 0.30 (1 in 48,333) and 0.008138% at P = 1 (1 in 12,288). These figures are used for the end-to-end test in §5.4 and for disclosure review in [[Randomised Reward Compliance]].

## 3. Deterministic selection tests (stub RNG)

[[Implementation - Weighted Random Selection]] maps a uniform draw `u` in [0, 1) to a tier through cumulative weights. With a stub RNG that returns scripted `u`, the expected mapping at P = 0.30 is:

| Tier | Interval of `u` | Test values of `u` | Expected |
|---|---|---|---|
| Common | [0, 0.65) | 0, 0.649999999 | Common |
| Uncommon | [0.65, 0.87) | 0.65, 0.869999999 | Uncommon |
| Rare | [0.87, 0.96) | 0.87, 0.959999999 | Rare |
| Epic | [0.96, 0.99) | 0.96, 0.989999999 | Epic |
| Legendary | [0.99, 0.998) | 0.99, 0.997999999 | Legendary |
| Mythical | [0.998, 0.9998) | 0.998, 0.999799999 | Mythical |
| Secret | [0.9998, 1) | 0.9998, 0.999999999 | Secret |

> [!warning] Floating-point boundaries
> In binary floating point, `0.65 + 0.22` is not exactly `0.87`. QA recommends (**PROPOSED**) that weights are converted to integers (for example parts per hundred million) and drawn with `Random:NextInteger(1, total)`, so each boundary is exact. Whatever the implementation, the boundary test above must pass and the last tier must be reachable (`u` just below 1 must never fall off the end and return nil).

## 4. Goodness-of-fit: chi-squared

### 4.1 Method

1. Fix the configuration: `P`, pool, `oddsVersion`.
2. Draw `n` outcomes through the real service code with a recorded seed.
3. Count observed `O_k` per category; expected `E_k = n × p_k`.
4. Statistic `χ² = Σ (O_k − E_k)² / E_k`, degrees of freedom `df = k − 1`.
5. Reject if `χ²` exceeds the critical value at the chosen significance level `α`.

**Validity rule:** every `E_k ≥ 5`. If a tier has `E_k < 5`, either increase `n` or merge the sparse tiers into one category *for the chi-squared test only*, and test each merged tier separately with the binomial method in §4.4.

Minimum `n` for `E ≥ 5` at P = 0.30: Mythical 2,778; Secret 25,000; Tyrannosaurus Rex end-to-end 241,667. At P = 0, Secret needs 564,972.

### 4.2 Critical values

| df | Used for | α = 0.05 | α = 0.01 | α = 0.001 |
|---:|---|---:|---:|---:|
| 3 | Secret pool (4 animals) | 7.815 | 11.345 | 16.266 |
| 5 | Mythical pool (6) | 11.070 | 15.086 | 20.515 |
| 6 | Egg rarity (7 tiers) | 12.592 | 16.812 | 22.458 |
| 7 | Legendary pool (8) | 14.067 | 18.475 | 24.322 |
| 8 | Epic pool (9) | 15.507 | 20.090 | 26.124 |
| 9 | Rare pool (10) | 16.919 | 21.666 | 27.877 |
| 10 | Uncommon pool (11) | 18.307 | 23.209 | 29.588 |
| 11 | Common pool (12) | 19.675 | 24.725 | 31.264 |

**PROPOSED gate significance:** `α = 0.001` per test for release gates (false alarms are expensive and the gate runs often), with Holm–Bonferroni correction across the family of tests in one gate run (§7).

### 4.3 Power: why chi-squared alone is not enough

The omnibus test spreads its power across all tiers, and Common dominates the statistic. Using the noncentral chi-squared distribution (Patnaik approximation, df = 6, α = 0.001, power 0.90, required noncentrality λ ≈ 30.2), the number of rolls needed to detect specific faults is:

| Fault injected (P = 0.30) | Rolls needed (omnibus χ²) |
|---|---:|
| Luck applied with P = 0 instead of 0.30 | ≈ 1,030 |
| Luck applied with P = 0.35 instead of 0.30 | ≈ 46,800 |
| Legendary 0.8% → 1.0% (taken from Common) | ≈ 59,700 |
| Secret 0.02% → 0.03% (taken from Common) | ≈ 604,000 |

The omnibus test is therefore a broad net. Rare tiers get their own targeted test.

### 4.4 Per-tier binomial test and sample sizes

For a tier with disclosed probability `p₀`, test `H₀: p = p₀` two-sided. The sample size to detect a true probability `p₁` with significance `α` and power `1 − β` is:

`n = [ (z_{1−α/2} × √(p₀(1−p₀)) + z_{1−β} × √(p₁(1−p₁))) / (p₁ − p₀) ]²`

with `z_{0.995} = 2.5758`, `z_{0.9995} = 3.2905`, `z_{0.90} = 1.2816`.

Required rolls, power 0.90 (upward deviation / downward deviation):

| Tier (p₀ at P = 0.30) | ±50% relative, α 0.01 | ±50%, α 0.001 | ±25%, α 0.001 | ±10%, α 0.001 |
|---|---:|---:|---:|---:|
| Common (65%) | 19 / 32 | 30 / 45 | 162 / 185 | 1,092 / 1,147 |
| Rare (9%) | 682 / 497 | 940 / 720 | 3,582 / 3,152 | 21,656 / 20,587 |
| Epic (3%) | 2,209 / 1,574 | 3,040 / 2,285 | 11,515 / 10,037 | 69,389 / 65,714 |
| Legendary (0.8%) | 8,510 / 6,020 | 11,701 / 8,743 | 44,236 / 38,436 | 266,287 / 251,860 |
| Mythical (0.18%) | 38,106 / 26,901 | 52,380 / 39,076 | 197,927 / 171,829 | 1,191,111 / 1,126,183 |
| **Secret (0.02%)** | **343,606 / 242,448** | **472,302 / 352,186** | **1,784,415 / 1,548,779** | **10,737,684 / 10,151,454** |

**Reading the Secret row.** To detect that Secret is really 0.03% instead of the disclosed 0.02% (a 50% relative error) with 90% power at α = 0.001, QA needs about **472,000 rolls**. To detect a 10% relative error (0.022%), about **10.7 million**. This is why the release gate uses 10 million rolls per configuration (§8): the minimum detectable relative error in Secret is then roughly 10%.

> [!danger] Never accept "we rolled 10,000 times and saw two Secrets"
> With p = 0.02%, the chance of seeing **zero** Secrets is 81.9% in 1,000 rolls, 36.8% in 5,000 and 13.5% in 10,000. Manual or small-sample observations say nothing about rare-tier correctness. Bug reports that claim "Secret odds are wrong" from player anecdotes must be checked against telemetry with the method in §5, not against small samples.

## 5. Confidence intervals (Wilson score)

For reporting observed rates, QA uses the Wilson score interval, which behaves correctly when the count is small or zero (the normal approximation does not).

`centre = (p̂ + z²/2n) / (1 + z²/n)`, `half-width = z × √(p̂(1−p̂)/n + z²/4n²) / (1 + z²/n)`, where `p̂ = x / n`.

Worked examples (95%, z = 1.96, unless stated):

| Observed | n | Wilson interval | Verdict against disclosed p₀ |
|---|---:|---|---|
| 0 Secret | 10,000 | 0% – 0.0384% | Consistent with 0.02%. Zero is not evidence of a fault. |
| 2 Secret | 10,000 | 0.005485% – 0.072900% | Consistent; interval is very wide |
| 5 Secret | 25,000 | 0.008543% – 0.046814% | Consistent |
| 200 Secret | 1,000,000 | 0.017414% – 0.022970% | Consistent |
| 2,000 Secret | 10,000,000 | 0.019143% – 0.020896% | Consistent (99.9%: 0.018582% – 0.021527%) |
| 20,000 Secret | 100,000,000 | 0.019725% – 0.020279% | Consistent |
| 1,800 Mythical | 1,000,000 | 0.171881% – 0.188502% | Consistent with 0.18% |
| 8,000 Legendary | 1,000,000 | 0.782728% – 0.817650% | Consistent with 0.8% |

Rolls needed for a 95% Wilson half-width of a given relative size at Secret 0.02%: ±25% ≈ 307,000; ±10% ≈ 1.92 million; ±5% ≈ 7.68 million.

### 5.1 Live telemetry check

After launch, observed counts per tier are grouped by `oddsVersion` bucket (players with the same displayed odds). For each bucket with enough volume, QA computes the 99.9% Wilson interval and checks that the disclosed `p₀` lies inside it. Because live `P` varies per player, the check also runs on the **aggregate expected rate** `Σ p₀(player_i) / n`, which must lie inside the aggregate interval. A disclosed value outside the interval on two consecutive weekly checks opens an S1 compliance bug ([[Bug Reporting and Severity]]).

## 6. Independence tests

Independence is a **CONFIRMED** promise (D-018). The simulation stream for these tests records every outcome in order, per simulated player.

### 6.1 Runs test (Wald–Wolfowitz)

Code each roll as 1 (Common) or 0 (not Common). With `n₁` ones and `n₂` zeros, the expected number of runs is `E[R] = 2n₁n₂/n + 1`, variance `Var[R] = 2n₁n₂(2n₁n₂ − n) / (n²(n − 1))`. `Z = (R − E[R]) / √Var[R]`.

Example: one million rolls at P = 0.30, so about 650,000 Common: `E[R] ≈ 455,001`, `SD ≈ 455.0`. Reject at α = 0.001 if `|Z| > 3.29`, that is if the observed runs fall outside roughly 453,504 – 456,498. Too few runs means streaks (for example a hidden "pity" or "bad luck" mechanism); too many means forced alternation (for example a hidden "anti-duplicate" rule). Repeat with the binary split "Rare or better versus below Rare".

### 6.2 Lag autocorrelation

Code outcomes as tier index 0–6 and compute the sample autocorrelation `r_k` for lags k = 1…20. Under independence, `r_k` is approximately normal with mean 0 and SD `1/√n`. For n = 1,000,000 the α = 0.001 bound is `±3.29/√n = ±0.00329` per lag (Holm–Bonferroni across the 20 lags). Repeat for animal index within each pool.

### 6.3 Conditional distribution after an outcome

The most direct test of "no influence from earlier hatches":

1. From the simulation stream, select every outcome that **immediately follows** a trigger outcome, for example a Legendary-or-better roll, a duplicate hatch, or an unowned-animal hatch.
2. Chi-squared test the follower distribution against the same expected distribution (same `P`) as all rolls.

At P = 0.30, Legendary-or-better has probability 1.0%, so 10 million rolls yield about 100,000 followers: enough for the omnibus test and for a ±10%-relative test down to Epic.

### 6.4 Duplicate and ownership bias

D-018 forbids duplicate protection and bias towards unowned animals. Test with simulated players who own a fixed subset of a pool:

- Let `U` be the set of unowned animals. The expected probability that one hatch yields an unowned animal is `Σ_{i∈U} w_i / Σ w`. For a player at P = 0.30 who owns all 8 Standard Common animals, `U` is the 2 Scarce and 2 Elusive animals: `(6 + 6 + 3 + 3) / 98 = 18.367%`.
- Run 200,000 Common hatches for this player; binomial test the unowned count against 18.367%.
- Repeat for a player who owns the whole pool (expected duplicate rate 100%; any non-duplicate outcome is impossible and is a P0 failure) and for a player who owns nothing (rates equal the pool table).
- Compare animal distributions between "owns everything" and "owns nothing" players with a two-sample chi-squared test; they must not differ.

### 6.5 Multi-hatch independence

Hatching five eggs at once (D-016) must produce five independent draws.

- **Position test:** for 200,000 five-egg Common hatches, chi-squared test the animal distribution at each position 1–5 separately against the pool odds.
- **Pair test:** build the 12 × 12 contingency table of (position 1 animal, position 2 animal) and run a chi-squared test of independence (df = 121). Repeat for positions (1, 5).
- **Same-animal rate:** the probability that all five eggs give the same animal is `Σ p_i⁵`; compare the observed count with a binomial test.

### 6.6 Merged eggs are ordinary eggs

An egg created by [[Egg Merging]] must hatch exactly like a rolled egg of the same rarity. Two-sample chi-squared test of 100,000 hatches of merged Rare eggs against 100,000 hatches of rolled Rare eggs at the same `P` (see TC-MRG-031).

## 7. Multiple testing and failure protocol

One gate run performs many tests. With 40 tests at α = 0.001, the chance of at least one false alarm is about 3.9%. QA applies **Holm–Bonferroni**: sort p-values ascending; reject test *i* (1-based) if `p_i < α / (m − i + 1)` and every earlier test was rejected.

When a statistical test fails:

1. Re-run the **same seed**. If the result differs, the harness is non-deterministic: S2 tooling bug.
2. Run the deterministic tests (§2, §3). A deterministic failure locates the bug.
3. Run **one** confirmation with a new seed and double `n`. If it also fails, raise an S1 bug.
4. Never re-run with new seeds until a test passes. Seeds and results of every run are logged.

## 8. Release gate (PROPOSED)

| Suite | Configurations | Sample size per configuration | Tests |
|---|---|---:|---|
| Egg rarity | P = 0, 0.30, 1.0 and two random P values per run | 10,000,000 rolls | Omnibus χ² (df 6), per-tier binomial, Wilson report, runs, lag ACF |
| Hatch pools | All 7 pools at P = 0, 0.30, 1.0 | 1,000,000 hatches per pool | Omnibus χ², per-class binomial |
| Independence | P = 0.30 | 10,000,000 rolls; 200,000 five-egg hatches | §6.1–§6.5 |
| Ownership bias | 3 ownership profiles | 200,000 hatches each | §6.4 |
| Rare spawns | Legendary 50%, Mythical 25%, Secret 10% per window | 5,000 windows each (fake clock) | Binomial |
| Wild unaffected by luck | P = 0 and P = 1 players | 100,000 spawn decisions each | Two-sample χ² |
| End-to-end | P = 0.30 | 2,000,000 rolls then hatches | Tyrannosaurus Rex rate (expected 0.002069%) via Wilson |

Rare-spawn windows: detecting Mythical 25% versus 20% at α = 0.01 with power 0.9 needs about 1,060 windows; Secret 10% versus 5% about 443; Legendary 50% versus 40% about 367. 5,000 windows gives margin and the run costs nothing with a fake clock.

## 9. Illustrative harness

```lua
--!strict
-- Illustrative Luau. Not executed in Roblox Studio.
local LuckService = require(script.Parent.LuckService) -- pure functions only
local Selection = require(script.Parent.WeightedSelection)

local TIERS = { "Common", "Uncommon", "Rare", "Epic", "Legendary", "Mythical", "Secret" }

local function chiSquared(observed: { number }, expectedPct: { number }, n: number): number
	local stat = 0
	for i, pct in expectedPct do
		local e = n * pct / 100
		assert(e >= 5, "Expected count below 5: merge tiers or increase n")
		stat += (observed[i] - e) ^ 2 / e
	end
	return stat
end

local function runRarityGate(p: number, n: number, seed: number): (number, { number })
	local rng = Random.new(seed)
	local odds = LuckService.computeRarityOdds(p) -- array of 7 percentages
	local counts = table.create(#TIERS, 0)
	for _ = 1, n do
		local index = Selection.pickIndex(odds, rng)
		counts[index] += 1
	end
	return chiSquared(counts, odds, n), counts
end

local stat = runRarityGate(0.30, 10_000_000, 20261114)
print(("chi2 = %.3f, reject at alpha 0.001 if > 22.458"):format(stat))
```

> [!note] Implementation notes
> - The harness calls the same `pickIndex` used by `EggService`; testing a copy proves nothing.
> - Production never re-seeds per request (for example from `os.time()`), which would make outcomes predictable. Tests seed explicitly; production uses one unseeded `Random.new()` per server.
> - Performance of 10 million iterations in Studio is *unverified*; the harness may need to run in batches across frames or in an offline Luau runtime.

## 10. Disclosure checks that are not statistical

These are deterministic and live in [[Test Cases - Egg Rolls and Hatching]]:

- The odds the client displays equal the odds the server will use (INV-10 in [[QA Strategy]]).
- No non-zero tier is displayed as "0%": at P = 0 Secret is 0.000885%, so the display needs enough precision or a "< 0.001%" format agreed with [[Randomised Reward Compliance]].
- A stale `oddsVersion` is rejected without charge (D-041).
- An egg's rarity never changes after the roll.

## Related documents

- [[QA Strategy]]
- [[Test Plan Matrix]]
- [[Test Cases - Egg Rolls and Hatching]]
- [[Test Cases - Egg Merging]]
- [[Test Cases - Animal AI]]
- [[Dynamic Progression Luck]]
- [[Dynamic Luck Probability Tables]]
- [[Hatch Pool Tables]]
- [[Independent Random Outcomes]]
- [[Probability Balancing]]
- [[Randomised Reward Compliance]]
- [[Implementation - Weighted Random Selection]]
- [[Implementation - Dynamic Luck Calculation]]
- [[Service - LuckService]]
