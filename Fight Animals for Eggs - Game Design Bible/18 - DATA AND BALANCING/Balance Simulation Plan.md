---
title: Balance Simulation Plan
type: plan
category: balancing
status: mixed
priority: P1
owner: Balancing Analyst
last_updated: 2026-11-14
tags:
  - balancing
  - simulation
  - probability
  - economy
  - combat
---

# Balance Simulation Plan

The simulations that every balance change must pass before it reaches a playtest, as required by [[Balancing Methodology]]. Each simulation lists its inputs, method, outputs and pass criteria, followed by sample results.

> [!warning] About the sample results
> Every "sample result" on this page comes from a **Python model of the proposed formulas** in [[Canonical Proposed Values]], run on 2026-11-14. They are **not** measurements from the game, which does not exist yet. They show what the proposed numbers imply and where they fail their targets. The in-engine versions of these tests (marked "engine" below) must be run in Roblox Studio once the systems exist.

> [!info] PROPOSED
> The simulations, pass criteria and the new targets they reference are **PROPOSED**. Values that depend on **UNDECIDED** items (raid egg theft limit, what a stolen animal keeps) are treated as swept parameters, never as chosen values.

## Overview

| ID | Simulation | Question it answers | Runs on | Blocking for |
|---|---|---|---|---|
| SIM-01 | Roll and hatch odds convergence | Do the formulas and the implementation produce the disclosed odds? | Model + engine | Any odds or pool change |
| SIM-02 | Merge-chain economy | How much cheaper is a high-rarity egg through merging than through rolling? | Model | Merge, roll price or odds change |
| SIM-03 | Ascension time-to-complete | How long does A5 take per rarity and pool class? | Model (Monte Carlo) | Ascension, odds, pool or price change |
| SIM-04 | Combat TTK per region | Do par players kill wild animals within target times? | Model, then engine | Stat, combat or region change |
| SIM-05 | Cash pacing | How fast does a par player afford milestones? | Model | Income or cost change |
| SIM-06 | Raid theft impact | How much can one successful raid cost the defender? | Model (parameter sweep) | Raid rule decisions, Q-013, Q-025, Q-033 |
| SIM-07 | Profile size | Does the save stay inside the DataStore budget? | Model + engine | Schema change |

Common model assumptions: Progression P = 0.30 (the published baseline) unless stated; the par loadouts and kill mix in [[Balancing Methodology]] §4–§5; Merge Station levels available as needed; no Robux purchases.

---

## SIM-01 Roll and hatch odds convergence

**Inputs:** baseline odds and slopes (canonical §7–§8), hatch pool composition from the launch roster (canonical §2), weight classes and tilts, P values {0, 0.30, 0.50, 0.75, 1.00}, seeds.

**Method:**
1. Structural checks from [[Balancing Methodology]] §6 at P = 0, 0.01, …, 1.00.
2. Model: draw N rolls with the formula's probabilities and compare observed with expected counts.
3. Engine: call the real server roll and hatch functions in a Studio test place (no DataStore writes) with the same P values, using fresh `Random.new()` objects as in production ([[Implementation - Weighted Random Selection]]).

**Sample size.** To estimate a probability *p* within a relative half-width *ε* at 95% confidence, `n = 1.96² × (1 − p) / (p × ε²)`.

| Rarity | p at P = 0.30 | n for ±20% | n for ±10% | n for ±5% |
|---|---:|---:|---:|---:|
| Common | 65% | 52 | 207 | 828 |
| Uncommon | 22% | 341 | 1,363 | 5,449 |
| Rare | 9% | 972 | 3,885 | 15,538 |
| Epic | 3% | 3,106 | 12,422 | 49,685 |
| Legendary | 0.8% | 11,909 | 47,636 | 190,544 |
| Mythical | 0.18% | 53,260 | 213,039 | 852,153 |
| Secret | 0.02% | 480,104 | 1,920,416 | 7,681,664 |

The Secret tier drives the run size: **2 million rolls per P value** gives ±10% on Secret. Hatch pools need far fewer: the smallest share at P = 0.30 is an Elusive Common at 3.06%, which needs about 12,200 hatches per pool for ±10%.

**Outputs:** observed versus expected table, per-rarity z-scores, chi-square statistic (df = 6 for rarities; df = pool size − 1 for pools).

**Pass criteria:**
- All structural checks pass.
- At each P value: chi-square below the 99.9% critical value (22.46 for df = 6), and every per-rarity |z| < 4.
- Over 20 seeds, no more than 1 seed fails the chi-square test (false alarm rate consistent with α = 0.001).
- Engine run: same criteria, plus the displayed odds table equals the model table for the same `oddsVersion` to 6 decimal places.

**Sample result** (model, N = 1,000,000, P = 0.30, seed 20261114):

| Rarity | Expected | Observed | z |
|---|---:|---:|---:|
| Common | 65.0000% | 64.9898% | −0.21 |
| Uncommon | 22.0000% | 22.0479% | +1.16 |
| Rare | 9.0000% | 8.9985% | −0.05 |
| Epic | 3.0000% | 2.9733% | −1.57 |
| Legendary | 0.8000% | 0.7898% | −1.14 |
| Mythical | 0.1800% | 0.1803% | +0.07 |
| Secret | 0.0200% | 0.0204% | +0.28 |

Chi-square = 4.82 (pass). Formula odds at P = 0 and P = 1 for reference: Common 71.88% → 53.14%, Legendary 0.248% → 1.753%, Secret 0.0009% → 0.0530%. All seven pools sum to 100% at every P tested.

---

## SIM-02 Merge-chain economy

**Inputs:** odds at P, roll price (200 Cash), merge fees per tier (100 / 300 / 900 / 2,700 / 8,000 / 25,000), 3:1 merge ratio (**CONFIRMED**).

**Method:** expected-value flow. Eggs reaching tier *k* per roll: `f_k = p_k + f_(k−1) / 3`. Merges at tier *k* per roll: `f_k / 3`. Cost per target egg = `(roll price + Σ merges × fee) / f_target`. Also the "Common-equivalent" value of a roll: `E = Σ p_r × 3^r`.

**Outputs:** rolls and Cash per egg of each rarity, direct versus full merging; fee share.

**Pass criteria (PROPOSED, new):** for Legendary and above, the full-merge Cash cost per egg should be 10–50% of the direct-roll cost, so merging is clearly worthwhile but direct rolls still matter. The fee share for Mythical and Secret should stay ≥ 50%, so merge fees remain the main late-game sink (D-038, **PROPOSED**).

**Sample result** (model, P = 0.30): `E = 4.161` Common-equivalents per roll.

| Target egg | Direct: rolls per egg | Merging: rolls per egg | Merging: Cash per egg (rolls + fees) | Merge cost ÷ direct cost | Fee share |
|---|---:|---:|---:|---:|---:|
| Uncommon | 4.5 | 2.3 | 508 | 56% | 10% |
| Rare | 11 | 4.2 | 1,126 | 51% | 25% |
| Epic | 33 | 9.2 | 3,096 | 46% | 40% |
| Legendary | 125 | 22.6 | 9,817 | 39% | 54% |
| Mythical | 556 | 60.5 | 33,373 | 30% | 64% |
| Secret | 5,000 | 175.2 | 120,734 | 12% | 71% |

Result: passes the fee-share criterion and the 10–50% band, but Secret sits near the lower edge. Full merging makes Secret eggs 28.5× more frequent per roll than direct rolling. Merging 729 Commons into one Secret costs 146,200 Cash in fees alone. The Station L5 price (1,000,000) and the Mythical → Secret fee are the main controls ([[Open Questions#Q-019]]).

---

## SIM-03 Ascension time-to-complete

**Inputs:** duplicates per rarity (15 / 13 / 10 / 9 / 7 / 6 / 5 to A5), ascension fees (`BaseFee × n`), pool share of the target species at P = 0.30 (Standard and Elusive classes), odds, merge fees, Cash per hour from SIM-05.

**Method (Monte Carlo, 400 trials per case):** sample how many target-rarity eggs are needed to hatch `1 + duplicates` copies of the target species (negative binomial on its pool share), then simulate rolls one by one until enough target-rarity eggs exist, either directly or with every lower egg merged up. Record rolls, merge fees and ascension fees. Convert Cash to hours at the par income of the region where that rarity is typically pursued.

Caveats: all lower eggs are merged toward the target, so animals the player would have hatched from them are given up; eggs of higher rarities are ignored; P is held at 0.30 although real P rises (conservative).

**Outputs:** median and P90 rolls; mean Cash; hours of par farming.

**Pass criteria:** the time-to-milestone targets in [[Balancing Methodology]] §5: Standard-class A5 in 8–20 h of par farming; Elusive-class ≤ 3.5× Standard.

**Sample result** (model, with merging):

| Rarity | Class | Copies | Species share | Median rolls | P90 rolls | Mean Cash | Region used | Hours |
|---|---|---:|---:|---:|---:|---:|---|---:|
| Common | Standard | 16 | 10.20% | 232 | 315 | 49,262 | 1 | 12.0 |
| Common | Elusive | 16 | 3.06% | 772 | 1,026 | 157,684 | 1 | 38.5 |
| Uncommon | Standard | 14 | 10.99% | 289 | 393 | 68,410 | 2 | 10.2 |
| Rare | Standard | 11 | 11.76% | 389 | 563 | 114,052 | 3 | 10.3 |
| Epic | Standard | 10 | 13.33% | 666 | 956 | 247,221 | 4 | 14.1 |
| Epic | Elusive | 10 | 4.00% | 2,206 | 3,246 | 779,506 | 4 | 44.3 |
| Legendary | Standard | 8 | 15.38% | 1,142 | 1,720 | 544,366 | 6 | 15.4 |
| Mythical | Standard | 7 | 22.22% | 1,830 | 2,909 | 1,119,163 | 8 | 15.7 |
| Secret | Standard | 6 | 34.48% | 2,834 | 4,179 | 2,113,972 | 8 | 29.7 |
| Secret | Elusive | 6 | 10.34% | 9,322 | 15,305 | 7,009,191 | 8 | 98.6 |

Without merging, the same goals take far longer: Epic Standard 29 h, Legendary Standard 36 h, Mythical Standard 50 h, Secret Standard 240 h, Secret Elusive 812 h.

Result: Standard classes pass for Common to Mythical. **Secret Standard fails** (29.7 h > 20 h) and Elusive ratios are about 3.1–3.3× (pass). Elusive Commons take 38.5 h at region-1 income, but players realistically finish them later at higher income (about 9 h at region-4 income). Levers: Secret duplicate count, Secret ascension fee (6,400 × n), Elusive weight.

---

## SIM-04 Combat TTK per region

**Inputs:** canonical stat model (§3), combat values (§4), region multipliers (§5), Training Grounds and ascension bonuses, par loadouts ([[Balancing Methodology]] §4). Player damage per second = Strength × (3.0 per 1.35 s combo + Power Strike 3.0 per 6 s + Ground Slam 2.0 per 12 s from L10), with Rally Cry's average uplift (+15% for 6 s of every 25 s) from L25. Animal DPS = ATK × AS. Damage reduction `100 / (100 + DEF)`. Bonus stacking is multiplicative in the model (the real rule is **UNDECIDED**, Q-953).

**Method:** deterministic expected-value model first (no dodging, full uptime, no abilities beyond the player's specials). Engine version: scripted bot fights in a Studio test place with real AI, abilities and movement, 30 fights per cell.

**Outputs:** TTK per wild rarity per region, player and animal DPS, animal damage share, player time-to-defeat when focused by a same-tier wild Bruiser.

**Pass criteria:** TTK within the [[Balancing Methodology]] §4 bands; player time-to-defeat ≥ 6 s; animal damage share inside the band chosen for Q-959 (not yet decided, reported only).

**Sample result** (model):

| Region | Par | Player DPS | Animal DPS | Animal share | TTK Common | TTK Rare | TTK Legendary | TTK Secret | Player time-to-defeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | L5, Common A0 | 49 | 54 | 52% | 4.7 s | 8.6 s | 16.0 s | 31.4 s | 11.1 s |
| 2 | L14, Uncommon A1 | 109 | 79 | 42% | 3.9 s | 7.1 s | 13.1 s | 25.8 s | 10.3 s |
| 3 | L24, Rare A1 | 178 | 107 | 38% | 3.8 s | 6.9 s | 12.7 s | 24.9 s | 8.2 s |
| 4 | L35, Epic A1 | 248 | 138 | 36% | 3.9 s | 7.1 s | 13.2 s | 25.8 s | 6.2 s |
| 5 | L47, Epic A3 | 339 | 165 | 33% | 4.2 s | 7.7 s | 14.2 s | 27.8 s | **5.9 s** |
| 6 | L59, Legendary A2 | 437 | 207 | 32% | 4.5 s | 8.3 s | 15.3 s | 30.0 s | **4.2 s** |
| 7 | L72, Legendary A4 | 549 | 243 | 31% | 5.1 s | 9.2 s | 17.1 s | 33.4 s | **3.9 s** |
| 8 | L90, Mythical A3 | 679 | 297 | 30% | 5.6 s | 10.1 s | 18.7 s | 36.7 s | **2.9 s** |

Result: TTK passes in regions 1 and 5–8 for every rarity. In regions 2–4 several cells are slightly **too fast**: for example Rare 6.9 s in region 3 (band 7–11), Epic 9.3–9.6 s in regions 2–4 (band 10–15), Legendary 12.7 s and Mythical 17.7 s in region 3. The largest miss is 7% below the lower bound, so the mid-game par loadout is slightly over-powered relative to the region multipliers 1.5, 2.2 and 3.2. Player time-to-defeat fails from region 5. Animal share falls steadily: player Strength (`10 + 2 × (L − 1)`, ×1.25 at Training Grounds L5) outgrows par animal ATK. Levers: player HP and DEF curves, the wild ATK multiplier, Strength growth per level, aggro rules that make wild animals prefer animal targets ([[Wild Animal AI]]).

---

## SIM-05 Cash pacing

**Inputs:** SIM-04 TTK, base Cash per rarity (§6), region multiplier, Shrine (+10% per level) and Trophy Hall (+1% per trophy) from the par loadout, 8 s overhead per kill, kill mix 55 / 27 / 13 / 5 (Common / Uncommon / Rare / Epic), costs from §10 and §12.

**Method:** expected value. `kills per hour = 3600 / Σ mix × (TTK + 8)`; `Cash per hour = kills per hour × Σ mix × BaseCash × RegionMultiplier × (1 + bonuses)`.

**Pass criteria:** rolls-per-hour bands and time-to-milestone targets in [[Balancing Methodology]] §5.

**Sample result** (model):

| Region | Kills per hour | Cash per kill | Cash per hour | Rolls per hour |
|---|---:|---:|---:|---:|
| 1 | 257 | 16.0 | 4,095 | 20.5 |
| 2 | 278 | 24.2 | 6,719 | 33.6 |
| 3 | 281 | 39.3 | 11,065 | 55.3 |
| 4 | 278 | 63.3 | 17,585 | 87.9 |
| 5 | 270 | 97.7 | 26,331 | 131.7 |
| 6 | 261 | 135.6 | 35,436 | 177.2 |
| 7 | 250 | 202.1 | 50,435 | 252.2 |
| 8 | 239 | 297.3 | 71,067 | 355.3 |

| Milestone | Hours (target) |
|---|---|
| Merge Station L1 in region 1 | 0.61 (≤ 1.0) pass |
| Merge Station L2 in region 2 | 2.23 (≤ 3.0) pass |
| Merge Station L3 in region 4 | 3.41 (≤ 4.0) pass |
| Merge Station L4 in region 6 | 7.06 (≤ 8.0) pass |
| Merge Station L5 in region 8 | 14.07 (≤ 15.0) pass, marginal |
| Shrine L4 in region 5 | 1.78 (≤ 2.0) pass |

All seven modules to L5 cost 805,469 Cash, plot expansion 200,000 and the station 1,327,500: 2,332,969 in total. Rolls per hour pass every band. At region 8 a par player earns about 355 rolls per hour, so storage capacity and hatch throughput, not Cash, limit the roll loop at endgame.

---

## SIM-06 Raid theft impact

**Inputs:** defender vault of 50 eggs drawn from the roll distribution at P = 0.30 (conservative: real vaults may hold more merged high-rarity eggs); egg theft limit swept over {0, 1, 3, 5, 10} (**UNDECIDED**, [[Open Questions#Q-013]]: these are sweep points, not proposals); raider egg choice "random" or "highest rarity first"; 0–3 stolen animals (**CONFIRMED** maximum 3); stolen animal keeps or loses its ascension (**UNDECIDED**, [[Open Questions#Q-025]]); defender par income (SIM-05).

**Method:** Monte Carlo, 4,000 vaults per cell. Egg value = `3^rarity` Common-equivalents × 48.1 Cash (one roll's Cash ÷ `E`, fees excluded). Animal value = Cash to re-obtain the species with merging (SIM-02 and SIM-03).

**Outputs:** expected and median Cash lost per raid; loss in hours of the defender's par income.

**Pass criteria (PROPOSED, new):** the median loss from one successful raid, excluding stolen animals, is ≤ 1 hour of the defender's par income; including up to 3 stolen animals, ≤ 3 hours. The criteria inform the Q-013, Q-025 and Q-033 decisions; they do not decide them.

**Sample result** (model, eggs only):

| Egg limit (sweep) | Region-4 defender: random pick | Region-4: highest first (median) | Region-8 defender: highest first (median) |
|---:|---:|---:|---:|
| 1 | 213 Cash (0.01 h) | 1,298 (0.07 h) | 1,298 (0.02 h) |
| 3 | 579 (0.03 h) | 3,893 (0.22 h) | 3,028 (0.04 h) |
| 5 | 1,024 (0.06 h) | 4,758 (0.27 h) | 4,181 (0.06 h) |
| 10 | 2,063 (0.12 h) | 5,768 (0.33 h) | 5,768 (0.08 h) |

Animal replacement cost (Standard class, A0, with merging): Common 3,015; Rare 7,217; Epic 13,823; Legendary 29,430; Mythical 54,465; Secret 101,610 Cash.

| Animal scenario (3 stolen, region-4 defender) | Cash lost | Hours |
|---|---:|---:|
| Three Epic A0 | 41,469 | 2.4 (pass ≤ 3) |
| Three Epic A5, ascension kept by the raider | about 741,700 | about 42 (fail) |

Result: with a vault built from plain rolls, egg losses are small for every swept limit. The dominant risk is ascended animals: if knocked-out defenders can be ascended animals **and** a stolen animal keeps its ascension, one raid can erase tens of hours. The answers to Q-025 and Q-033 matter far more for raid fairness than the egg limit.

---

## SIM-07 Profile size

**Inputs:** the nine schemas, worst-case field contents, collection sizes {3, 100, 500, 1,000} animals and {10, 60, 225} eggs.

**Method:** build mock profiles and JSON-encode them compactly (model); in the engine, `HttpService:JSONEncode` on generated profiles.

**Pass criteria:** the largest realistic shape (100 animals, 225 eggs) is under 256 KiB (the warning threshold in [[Data Architecture Overview]]); a 1,000-animal stress profile is under 1 MiB.

**Sample result** (model): 21 KiB (new player), 72 KiB (100 animals, 60 eggs), 121 KiB (100 animals, 225 eggs), 450 KiB (1,000 animals). Pass.

---

## Running and recording simulations

- Every run records: date, config version, seeds, sample sizes, model version and pass or fail per criterion, attached to the change in [[Balance Update Process]].
- Seeds used for the sample results: SIM-01 20261114; SIM-03 fixed per case; SIM-06 99.
- The Python model used for these samples was a working script, not a maintained tool. Before beta, the model should be rebuilt as a versioned tool that reads the same generated config as the game, so the model and the game cannot drift apart.
- Engine runs belong in the QA plan ([[Statistical Testing of Probabilities]], [[Test Plan Matrix]]).

Planned additions once inputs exist: boss TTK (needs boss HP, [[Boss Design Overview]]); PvP time-to-kill ([[PvP System]]); Progression Score pacing over a full player journey ([[Progression Score Specification]]); defeat-penalty cost per battle type once [[Open Questions#Q-014]] is decided.

## Related documents
- [[Balancing Methodology]]
- [[Canonical Proposed Values]]
- [[Balance Update Process]]
- [[Statistical Testing of Probabilities]]
- [[Expected Value Calculations]]
- [[Ascension Expected Value Analysis]]
- [[Progression Bottleneck Analysis]]
- [[Raid Rewards and Defender Compensation]]
- [[Data and Balancing Index]]
