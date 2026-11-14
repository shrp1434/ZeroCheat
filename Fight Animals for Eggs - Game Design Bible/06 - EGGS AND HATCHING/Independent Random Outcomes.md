---
title: Independent Random Outcomes
type: system
category: eggs
status: mixed
priority: P0
owner: Systems Designer
last_updated: 2026-11-14
tags:
  - eggs
  - probability
  - fairness
  - maths
---

# Independent Random Outcomes

Every egg roll and every hatch in *Fight Animals for Eggs* is an **independent** random event. This page explains what that means mathematically, what it implies for players, and the rules that engineering, UI and live-ops must follow to keep the promise.

> [!success] CONFIRMED (D-018)
> Every hatch is independent: **no duplicate protection, no bias towards unowned animals, no influence from earlier hatches.** Duplicates are a feature: they feed [[Ascension System|ascension]] (D-019).

The only thing that changes odds is the player's Progression Score through [[Dynamic Progression Luck]], and those odds are always disclosed before committing (D-017). Luck is a function of *progress*, never of *roll history*.

## 1. Independence in one sentence

The outcome of a roll depends only on the disclosed odds at that moment and a fresh random number. It does not depend on how many times the player has rolled, what they got last time, what they own, or what anyone else rolled.

## 2. The mathematics

### 2.1 Product rule

For independent events *A* and *B*: **P(A ∩ B) = P(A) × P(B).**

- Two Legendary eggs in two consecutive rolls at baseline: 0.008 × 0.008 = **0.000064** (1 in 15,625).
- A specific animal from a roll is itself a product of the two stages: P(Secret egg) × P(Tyrannosaurus Rex | Secret pool) = 0.0002 × 3/29 = **0.0000207** (1 in 48,333) at baseline.
- Five Commons in a ×5 bulk roll: 0.65^5 = **11.6 %**.

Independence also means **P(A | B) = P(A)**: given that the last roll was a Secret, the next roll is still a Secret with probability 0.02 %. Not more, not less.

### 2.2 Rolls until the first X: the geometric distribution

If each roll succeeds with probability *p*, the number of rolls *N* up to and including the first success follows a geometric distribution:

- P(N = n) = (1 − p)^(n−1) × p
- **Expected value E[N] = 1 / p**
- Median ≈ ln(0.5) / ln(1 − p) ≈ 0.693 / p for small p
- Rolls needed for a 90 % chance ≈ ln(0.1) / ln(1 − p) ≈ 2.303 / p

### 2.3 At least one in *n* rolls

**P(at least one X in n rolls) = 1 − (1 − p)^n.**

A useful consequence: rolling exactly the expected number of times (n = 1/p) gives only about **63.2 %** chance of success, because (1 − p)^(1/p) → e^(−1) ≈ 0.368.

### 2.4 Worked numbers at baseline (P = 0.30)

| Target | p per roll | Expected rolls (1/p) | Median rolls | Rolls for 90 % | P(≥1 in 100 rolls) | P(≥1 in 1,000 rolls) |
|---|---:|---:|---:|---:|---:|---:|
| Epic egg | 3 % | 33.3 | 23 | 76 | 95.24 % | ≈100 % |
| Legendary egg | 0.8 % | 125 | 86 | 287 | 55.21 % | 99.97 % |
| Mythical egg | 0.18 % | 556 | 385 | 1,278 | 16.49 % | 83.50 % |
| Secret egg | 0.02 % | 5,000 | 3,466 | 11,512 | 1.98 % | 18.13 % |
| A specific [[Tiger]] (3 % × 10/75) | 0.4 % | 250 | 173 | 574 | 33.02 % | 98.18 % |

Reading the Secret row: half of all players need more than **3,466** rolls for their first Secret egg by direct rolling; one in ten needs more than **11,512**. These long tails are why [[Egg Merging|merging]] exists as a deterministic alternative.

### 2.5 Multiple copies: the negative binomial

Collecting *k* copies of something with per-roll probability *p* takes on average **k / p** rolls. The variance is k(1 − p)/p², so the relative spread shrinks as k grows (standard deviation ÷ mean ≈ 1/√k). This drives the duplicate maths in [[Ascension Expected Value Analysis]].

### 2.6 No memory

The geometric distribution is **memoryless**: P(N > m + n | N > m) = P(N > n). A player who has rolled 4,000 times without a Secret still expects **5,000 more** rolls on average, exactly as on their first roll. There is no "due" outcome.

## 3. Why there is no duplicate protection

| Reason | Explanation |
|---|---|
| Owner decision | D-018 is **CONFIRMED** |
| Duplicates are progress | Ascension needs 5–15 duplicates per animal ([[Ascension Progression Table]]). Protection would starve ascension |
| Honest odds | With protection, the "real" odds would depend on the collection, so the disclosed table would be wrong for almost everyone. Independence keeps disclosure simple and exact |
| No hidden state | No counters to persist, corrupt, desync or exploit |
| Consistent with merging | The player's deterministic lever is merging, which is visible and controllable, not a hidden pity timer |

> [!danger] Forbidden implementations
> - Re-rolling a result because the player already owns it.
> - Weighting by ownership, by time since the last rare, by spend, or by session length.
> - Pity counters, "bad luck protection", streak breakers, or guaranteed rares after N rolls.
> - Seeding the generator per player in a way that makes sequences predictable (for example seeding from UserId).
> - Passing any collection or history data into the sampling function. The sampler's only inputs are the disclosed odds and the server's `Random` object ([[Implementation - Weighted Random Selection]]).

## 4. The gambler's fallacy and UI copy

The gambler's fallacy is the belief that a run of misses makes a hit "due". Independence makes it false here, and the UI must not encourage it.

| Do (PROPOSED copy) | Do not |
|---|---|
| "Every roll has the same odds shown above." | "You're due a Legendary!" |
| "Your odds improve as you progress." | "So close!", "Almost a Secret!" |
| "Duplicates power up your animals through ascension." | Progress bars towards a guaranteed rare (unless it is genuinely deterministic, like merge counts) |
| Show the count of eggs owned per rarity (factual) | "Unlucky streak" counters, "rolls since last Legendary" displays |
| Show merge progress ("2 of 3 Epic eggs") because merging is deterministic | Near-miss animations that tease a higher rarity before revealing a lower one ([[Egg Animations]]) |

## 5. Implementation notes

- **One server `Random` object per service**, created with `Random.new()`. Whether an unseeded `Random.new()` draws from a high-entropy source is *unverified* against official documentation; if not, seed it once at server start from a mix of `os.clock()`, `tick()` and a server GUID. Never use the client's RNG for outcomes.
- **Draw order is irrelevant to fairness** as long as no information leaks; bulk rolls draw each egg in sequence from the same generator.
- **Statistical verification**: the QA suite runs 10 million draws per configuration and applies a chi-squared test, plus a runs test for serial independence ([[Statistical Testing of Probabilities]]).

## 6. Worked FAQ for support staff

| Player says | Correct answer |
|---|---|
| "I rolled 300 times and got no Legendary, the game is rigged." | At baseline, P(no Legendary in 300) = 0.992^300 ≈ **9.0 %**. Roughly one in eleven players has that experience. Check their PS: below the pivot their odds are lower than 0.8 % |
| "I got two Secrets in a row, is that a bug?" | Possible but very rare: 1 in 25 million at baseline. Escalate for an audit-log check, but do not assume an exploit |
| "Does owning everything make duplicates more likely?" | No. Odds are identical whether you own zero or all animals in the pool |

## Related documents
- [[Egg Roll System]] · [[Hatch System]] · [[Dynamic Progression Luck]]
- [[Egg Merging]] · [[Ascension System]] · [[Ascension Expected Value Analysis]]
- [[Randomised Reward Compliance]] · [[Design Principles and Fairness Charter]]
- [[Implementation - Weighted Random Selection]] · [[Statistical Testing of Probabilities]]
- [[Expected Value Calculations]] · [[Glossary]]
