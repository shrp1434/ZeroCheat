---
title: Implementation - Weighted Random Selection
type: implementation
category: eggs
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - probability
  - eggs
  - hatching
  - testing
---

# Implementation - Weighted Random Selection

Weighted selection is used twice in every egg's life: once by the roll to pick a rarity and once by the hatch to pick a species from that rarity's pool (two-stage randomness, D-015, **CONFIRMED**). It is also used by spawn tables and boss attack selection. One shared, tested implementation serves all of them.

> [!info] PROPOSED
> Design and code are **PROPOSED**. Code is **illustrative — not executed**.

## 1. Requirements

| # | Requirement | Source |
|---|---|---|
| R1 | Runs on the server with a `Random` object created by `Random.new()` | [[Luau Coding Standards]] §3 |
| R2 | Cumulative-weight selection: an outcome's chance is its weight divided by the total | [[Probability Balancing]] |
| R3 | Floating-point safety: the final positive bucket catches any rounding residue, so selection never returns `nil` | This document |
| R4 | Validation: every weight is a finite, positive number; at least one entry exists | This document |
| R5 | Pure core: the selection function takes a uniform number `u` in [0, 1) and has no side effects, so tests can drive it deterministically | [[Statistical Testing of Probabilities]] |
| R6 | Independence: no state carried between calls (no pity, no duplicate protection, no history) | D-018 **CONFIRMED** |

> [!success] CONFIRMED — independence
> Every hatch is independent. The selector must never read the player's collection, recent results or streaks. Any such input is a compliance defect ([[Independent Random Outcomes]]).

## 2. Algorithm

Given entries `e₁ … eₙ` with weights `w₁ … wₙ`, total `W = Σwᵢ`, and a uniform `u ∈ [0, 1)`:

1. `target = u × W`.
2. Walk the entries keeping a running sum `c`. Return the first `eᵢ` for which `target < c + wᵢ`.
3. If the loop finishes without returning (possible only when floating-point error makes `c` end slightly below `target` near `W`), return the **last** entry. Because all weights are validated positive, the last entry is always a legitimate outcome and the residue it absorbs is of the order of 1e-15 of the total.

Why a strict `<`: with `u = 0`, `target = 0` and the first entry is returned (it has positive width). With `u` just under 1, `target` is just under `W` and lands in the last bucket. Each bucket is the half-open interval `[c, c + wᵢ)`.

For large tables used many times (spawn tables), a prefix-sum array plus binary search gives O(log n). Hatch pools have at most 12 entries, so a linear scan is simpler and fast enough.

## 3. Code

```lua
--!strict
-- Illustrative — not executed
-- ReplicatedStorage/Shared/WeightedRandom
-- Pure functions. The algorithm is public; the WEIGHTS for luck and pools are
-- server-only data passed in by the caller (see Configuration Modules).

export type Entry<T> = { value: T, weight: number }

export type ValidationError =
	"EMPTY"
	| "NOT_A_NUMBER"
	| "NOT_FINITE"
	| "NOT_POSITIVE"

local WeightedRandom = {}

local function isFinite(x: number): boolean
	-- NaN fails x == x; infinities fail the bounds.
	return x == x and x ~= math.huge and x ~= -math.huge
end

-- Returns (true, total) or (false, error, offendingIndex).
function WeightedRandom.validate<T>(entries: { Entry<T> }): (boolean, number | ValidationError, number?)
	if #entries == 0 then
		return false, "EMPTY", nil
	end
	local total = 0
	for i, e in entries do
		local w = e.weight
		if typeof(w) ~= "number" then
			return false, "NOT_A_NUMBER", i
		end
		if not isFinite(w) then
			return false, "NOT_FINITE", i
		end
		if w <= 0 then
			return false, "NOT_POSITIVE", i
		end
		total += w
	end
	if not isFinite(total) then
		-- Individually finite weights can still overflow when summed.
		return false, "NOT_FINITE", nil
	end
	return true, total, nil
end

-- Pure selection. `u` must be in [0, 1). Caller must have validated entries.
-- Returns the chosen entry's value and its index.
function WeightedRandom.selectWithUniform<T>(entries: { Entry<T> }, total: number, u: number): (T, number)
	assert(u >= 0 and u < 1, "u must be in [0, 1)")
	local target = u * total
	local cumulative = 0
	for i, e in entries do
		cumulative += e.weight
		if target < cumulative then
			return e.value, i
		end
	end
	-- Floating-point residue: the final bucket catches it (R3).
	local last = #entries
	return entries[last].value, last
end

-- Convenience wrapper for services. `rng` is a Random owned by the calling service.
function WeightedRandom.select<T>(entries: { Entry<T> }, rng: Random): (T, number)
	local ok, totalOrErr, idx = WeightedRandom.validate(entries)
	if not ok then
		error(("WeightedRandom.select: invalid weights (%s at %s)"):format(tostring(totalOrErr), tostring(idx)))
	end
	-- Random:NextNumber() with no arguments is used as a uniform in [0, 1).
	-- *Unverified*: the half-open upper bound is not stated on the API page;
	-- the guard below makes the code correct either way.
	local u = rng:NextNumber()
	if u >= 1 then
		u = 0.9999999999999999
	end
	return WeightedRandom.selectWithUniform(entries, totalOrErr :: number, u)
end

-- Exact probabilities for display. Used to build the odds shown before commit (D-017).
function WeightedRandom.probabilities<T>(entries: { Entry<T> }): { number }
	local ok, totalOrErr = WeightedRandom.validate(entries)
	assert(ok, "invalid weights")
	local total = totalOrErr :: number
	local out = table.create(#entries)
	for i, e in entries do
		out[i] = e.weight / total
	end
	return out
end

return WeightedRandom
```

### Prefix-sum variant (spawn tables)

```lua
--!strict
-- Illustrative — not executed
export type Prepared<T> = { values: { T }, prefix: { number }, total: number }

local function prepare<T>(entries: { { value: T, weight: number } }): Prepared<T>
	local values, prefix = table.create(#entries), table.create(#entries)
	local c = 0
	for i, e in entries do
		c += e.weight
		values[i] = e.value
		prefix[i] = c
	end
	return { values = values, prefix = prefix, total = c }
end

local function selectPrepared<T>(p: Prepared<T>, u: number): T
	local target = u * p.total
	local lo, hi = 1, #p.prefix
	while lo < hi do
		local mid = (lo + hi) // 2
		if target < p.prefix[mid] then
			hi = mid
		else
			lo = mid + 1
		end
	end
	return p.values[lo] -- lo == #prefix when residue pushes target to the end
end
```

## 4. The `Random` object

| Rule | Detail | Status |
|---|---|---|
| One `Random` per service | `local rng = Random.new()` at module load in `EggService` and `HatchService`. No seed argument, so the engine seeds it. *Unverified*: the API page lists `new(seed)`; calling without a seed is standard practice but confirm in Studio. | **PROPOSED** |
| Never seed from player data or time on the client | Predictable seeds are an exploit. | **PROPOSED** |
| Never share `Random` with the client | Results are sent, not generators. | **PROPOSED** |
| Seeded `Random` only in tests | `Random.new(12345)` for reproducible test runs. | **PROPOSED** |

## 5. Worked example

The baseline egg-rarity weights at P = 0.30 are 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 (D-031, **PROPOSED**). The total is 100.

| Rarity | Weight | Cumulative upper bound | `u` range that selects it |
|---|---:|---:|---|
| Common | 65 | 65 | [0, 0.65) |
| Uncommon | 22 | 87 | [0.65, 0.87) |
| Rare | 9 | 96 | [0.87, 0.96) |
| Epic | 3 | 99 | [0.96, 0.99) |
| Legendary | 0.8 | 99.8 | [0.99, 0.998) |
| Mythical | 0.18 | 99.98 | [0.998, 0.9998) |
| Secret | 0.02 | 100 | [0.9998, 1) |

`u = 0.99985` → target 99.985 → Secret. `u = 0.65` → target 65 → not `< 65`, so it falls to Uncommon (half-open interval).

> [!warning] Floating-point note
> `65 + 22 + 9 + 3 + 0.8 + 0.18 + 0.02` in binary floating point may not equal exactly 100. This is why the total is computed by summing the same weights in the same order the loop uses, and why the final bucket catches the residue. Never compare against a literal 100.

## 6. Test hooks

| Test | Input | Expected |
|---|---|---|
| T1 lower edge | `u = 0` | First entry |
| T2 upper edge | `u = 0.9999999999999999` | Last entry |
| T3 bucket boundary | Baseline table, `u = 0.65` | Uncommon |
| T4 residue | Weights `{0.1, 0.2, 0.3}` with `u` just below 1 | Third entry, never `nil` |
| T5 validation | Weight `0`, `-1`, `0/0`, `math.huge`, `"5"` | Each rejected with the right error |
| T6 overflow | Two weights of `1e308` | `NOT_FINITE` |
| T7 single entry | One entry | Always that entry |
| T8 distribution | 1,000,000 draws with seeded `Random` on the baseline table | Chi-square within the bound in [[Statistical Testing of Probabilities]] |
| T9 independence | Draw sequence statistics (runs test) | No serial correlation detected |
| T10 no side effects | Call twice with same `u` | Same result; entries table unchanged |

Cases are mirrored in [[Test Cases - Egg Rolls and Hatching]].

## 7. Edge cases

- **Zero-weight entries.** Rejected by validation. A species that must be removed from a pool is removed from the list, not given weight 0. This makes "this animal cannot hatch" explicit in data review.
- **Very small weights.** Secret at P = 0 has weight 0.0008 (see [[Implementation - Dynamic Luck Calculation]]). Double precision handles this comfortably; the issue is display rounding, handled by the UI ([[UI - Egg Rolling]]).
- **Order dependence.** Results depend on entry order for a given `u`, but probabilities do not. Keep a stable order (rarity index, then roster order) so seeded tests are reproducible.

## Related documents
- [[Implementation - Dynamic Luck Calculation]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Independent Random Outcomes]]
- [[Probability Balancing]]
- [[Statistical Testing of Probabilities]]
- [[Hatch Pool Tables]]
- [[Dynamic Luck Probability Tables]]
- [[Service - EggService]]
- [[Service - HatchService]]
