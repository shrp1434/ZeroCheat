---
title: Schema - Discovery Index
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - animal-index
  - progression
---

# Schema - Discovery Index

## Purpose

Stores, per species, whether the player has discovered it, how often they have defeated it, and whether they have ever owned it. The feature is owned by [[Animal Index Feature Specification]] and served by [[Service - IndexService]]. The number of discovered species feeds the Progression Score (3 points per species, max 180).

> [!success] CONFIRMED
> Defeating wild animals registers them in the index, and the index distinguishes discovered animals from owned animals (D-029).

> [!warning] UNDECIDED
> Whether obtaining a species by hatching, stealing or an event, without ever defeating it in the wild, also counts as "discovered" (for the index and for the Progression Score) is **UNDECIDED** (Q-952). The schema keeps `discoveredAt` (defeat-based) and `firstOwnedAt` (acquisition-based) separate so either rule can be applied as a derived value.

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `species` | `{ [string]: SpeciesEntry }` | Required | `{}` | Keys are species IDs in config | Absent key = never encountered |

`SpeciesEntry`:

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `discoveredAt` | `number?` | Optional | `nil` | Unix seconds | First wild defeat of this species (D-029). `nil` if never defeated. |
| `defeatedCount` | `number` | Required | `0` | Integer ≥ 0 | Wild defeats credited to this player |
| `everOwned` | `boolean` | Required | `false` | Boolean; once `true`, never `false` | Owned at any point, even if since consumed or stolen |
| `firstOwnedAt` | `number?` | Optional | `nil` | Unix seconds; required if `everOwned` | |
| `hatchedCount` | `number` | Required | `0` | Integer ≥ 0 | Times hatched. Analytics and display only. |
| `variantsSeen` | `{ [string]: boolean }` | Required | `{}` | Keys are variant IDs eligible for the species | Variants ever owned |

### Derived values (never stored)

| Value | Derivation |
|---|---|
| Currently owned | Any instance with this `speciesId` in [[Schema - Animal Collection]] |
| Owned count | Count of those instances |
| Highest ascension owned | Max `ascension` among those instances |
| Discovered species count (for PS) | Count of entries with `discoveredAt ~= nil` (or per the Q-952 rule) |
| Index completion % | Discovered count / species in config |

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type SpeciesEntry = {
	discoveredAt: number?,
	defeatedCount: number,
	everOwned: boolean,
	firstOwnedAt: number?,
	hatchedCount: number,
	variantsSeen: { [string]: boolean },
}

export type DiscoveryIndex = { species: { [string]: SpeciesEntry } }

local function newDiscoveryIndex(): DiscoveryIndex
	return { species = {} }
end

local function entry(index: DiscoveryIndex, speciesId: string): SpeciesEntry
	local e = index.species[speciesId]
	if e == nil then
		e = { discoveredAt = nil, defeatedCount = 0, everOwned = false, firstOwnedAt = nil, hatchedCount = 0, variantsSeen = {} }
		index.species[speciesId] = e
	end
	return e
end

-- Called by IndexService when kill credit is awarded for a wild animal.
local function recordDefeat(index: DiscoveryIndex, speciesId: string, now: number): boolean
	local e = entry(index, speciesId)
	e.defeatedCount += 1
	if e.discoveredAt == nil then
		e.discoveredAt = now
		return true -- newly discovered: Progression Score changes
	end
	return false
end

-- Called in the same transaction that adds an animal instance.
local function recordOwned(index: DiscoveryIndex, speciesId: string, variant: string?, viaHatch: boolean, now: number)
	local e = entry(index, speciesId)
	if not e.everOwned then
		e.everOwned = true
		e.firstOwnedAt = now
	end
	if viaHatch then e.hatchedCount += 1 end
	if variant then e.variantsSeen[variant] = true end
end
```

## Invariants

1. Every key exists in species config (60 at launch). Unknown keys are kept and flagged (soft failure).
2. `everOwned = true` for every species that has at least one instance in the collection (auto-repair sets it if missing, and sets `firstOwnedAt` to the earliest `obtainedAt`).
3. `everOwned` never goes back to `false`, even if every instance is consumed by ascension or stolen.
4. `discoveredAt ~= nil` implies `defeatedCount ≥ 1` (auto-repair: raise the count to 1).
5. Discovery is recorded only from server-awarded kill credit ([[Combat Rewards]]). It never depends on client reports.
6. Nothing in this schema influences hatch odds for a particular species. Owning or not owning a species must never bias outcomes (D-018). The only link to odds is the aggregate discovered count inside the Progression Score.

## Edge cases

| Case | Handling |
|---|---|
| Player hatches a Secret before ever meeting one in the wild | `everOwned = true`, `discoveredAt = nil`. Whether it counts as discovered is Q-952. |
| Player's only Tiger is stolen | `everOwned` stays `true`; "currently owned" becomes false (derived) |
| Defeat credited by shared kill credit (≥ 10% contribution) | Each credited player records the defeat |
| Very high defeat counts | Integers up to 2^53 are exact; no cap needed |

## Migration notes

- If Q-952 is decided as "acquisition counts as discovery", no migration is required: the derived count changes. Players' Progression Scores may rise, which changes their odds. That is a disclosed odds change handled through [[Balance Update Process]].
- Adding per-species "first seen" (seen but not defeated) would be a new optional field with default `nil`.

## Size estimate

About 220 bytes per entry with all variants seen; all 60 species ≈ 13 KiB. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Animal Index Feature Specification]]
- [[UI - Animal Index Screen]]
- [[Service - IndexService]]
- [[Progression Score Specification]]
- [[Schema - Animal Collection]]
- [[Animal Index]]
- [[Data and Balancing Index]]
