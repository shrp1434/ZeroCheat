---
title: Schema - Animal Collection
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - animals
  - ascension
---

# Schema - Animal Collection

## Purpose

Stores every animal a player owns as a unique **instance**, including its species, variant, **ascension level**, provenance and lock flags. Gameplay rules are owned by [[Animal Collection System]] and [[Ascension System]]. Stats are never stored: they are computed from species config, rarity, ascension and base bonuses ([[Animal Stat Budget Model]], [[Animal Statistics Database]]).

> [!success] CONFIRMED rules this schema must support
> Duplicates are consumed by ascension and the original is kept (D-019). Every hatch is independent (D-018), so no field here may feed back into hatch odds. An animal can be stolen only after it has been knocked out while defending, with at most **3** stolen per successful raid (D-024).

> [!info] PROPOSED
> Five ascension levels A1–A5 are the working assumption ([[Open Questions#Q-004]]); duplicate counts are in [[Canonical Proposed Values]] §9 ([[Open Questions#Q-005]]). Owned-animal capacity is **UNDECIDED** ([[Open Questions#Q-022]]); the prototyping assumption is 100.

## Collection fields (`animals`)

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `instances` | `{ [string]: AnimalInstance }` | Required | `{}` | Keys are GUIDs equal to each value's `id` | Keyed map, never an array |
| `capacityExpansionSteps` | `number` | Required | `0` | Integer ≥ 0, ≤ config maximum | Placeholder for capacity expansion if Q-022 adds it. Capacity itself is derived from config. |

## Animal instance fields

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `id` | `string` | Required | `HttpService:GenerateGUID(false)` | 36-character GUID, unique across the whole profile | Generated on the server at creation. Never reused. |
| `speciesId` | `string` | Required | — | Exists in species config (60 at launch) | For example `"tiger"`, `"great_white_shark"`, `"haasts_eagle"` |
| `variant` | `string?` | Optional | `nil` | `nil` or a variant ID eligible for this species in config | `nil` = normal. Examples: `"golden"`, `"diamond"`, `"rainbow"`, `"shadow"`, `"neon"`. Acquisition is **UNDECIDED** ([[Open Questions#Q-006]]). |
| `ascension` | `number` | Required | `0` | Integer 0–5 | 0 = not ascended, 5 = A5 |
| `obtainedAt` | `number` | Required | `os.time()` | Unix seconds, ≤ now | Time this player obtained this instance |
| `obtainedVia` | `"hatch" \| "steal" \| "event"` | Required | — | One of the three | Provenance |
| `sourceRef` | `string?` | Optional | `nil` | ≤ 64 characters | Hatch: egg instance ID. Steal: raid ID. Event: event or grant ID. |
| `oddsVersion` | `string?` | Optional | `nil` | Required when `obtainedVia = "hatch"`; matches the odds-version pattern | The hatch-odds version displayed when the hatch was committed (audit) |
| `prevOwnerId` | `number?` | Optional | `nil` | Positive integer; required when `obtainedVia = "steal"` | Audit only. Never displayed to other players. |
| `ascendedAt` | `number?` | Optional | `nil` | Unix seconds | Time of the latest ascension step |
| `locks` | `AnimalLocks` | Required | all clear | See below | System locks |
| `userLocked` | `boolean` | Required | `false` | Boolean | Player-set "protect" toggle that prevents use as an ascension duplicate |

### Lock flags (`locks`)

| Field | Luau type | Default | Authority | Meaning |
|---|---|---|---|---|
| `equipped` | `boolean` | `false` | [[Schema - Equipped Team]] slots | In one of the three team slots. Recomputed from the team on load. |
| `guarding` | `boolean` | `false` | `base.guards` in [[Schema - Base Data]] | Assigned as a base defender. Which animals defend is **UNDECIDED** ([[Open Questions#Q-033]]). |
| `pendingTx` | `string?` | `nil` | `data.pending` in [[Schema - Player Profile]] | ID of an open transaction touching this animal, for example `"asc:<guid>"` or `"raid:<raidId>"` |

## Ascension data

Ascension changes only two fields on the kept original (`ascension`, `ascendedAt`) and **removes** the consumed duplicate instances. It is an intra-profile transaction, so it is atomic ([[Implementation - Ascension Transaction]]).

| Check before ascending from *n* to *n+1* | Source |
|---|---|
| `n < 5` | This schema |
| Exactly `DupesFor(rarity, n+1)` duplicate instances selected, same `speciesId` as the original | [[Canonical Proposed Values]] §9 |
| Whether duplicates must also match the original's `variant` | **UNDECIDED** (Q-958) |
| Every duplicate: `locks.equipped = false`, `locks.guarding = false`, `locks.pendingTx = nil`, `userLocked = false` | This schema |
| The original is not one of the duplicates | This schema |
| Cash fee `BaseFee(rarity) × (n+1)` affordable | [[Schema - Economy]] |

Total duplicates to reach A5 at the proposed values: Common 15, Uncommon 13, Rare 10, Epic 9, Legendary 7, Mythical 6, Secret 5. The time this takes is simulated in [[Balance Simulation Plan]].

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
local HttpService = game:GetService("HttpService")

export type ObtainedVia = "hatch" | "steal" | "event"

export type AnimalLocks = {
	equipped: boolean,
	guarding: boolean,
	pendingTx: string?,
}

export type AnimalInstance = {
	id: string,
	speciesId: string,
	variant: string?,
	ascension: number,
	obtainedAt: number,
	obtainedVia: ObtainedVia,
	sourceRef: string?,
	oddsVersion: string?,
	prevOwnerId: number?,
	ascendedAt: number?,
	locks: AnimalLocks,
	userLocked: boolean,
}

export type AnimalCollection = {
	instances: { [string]: AnimalInstance },
	capacityExpansionSteps: number,
}

local function newAnimalCollection(): AnimalCollection
	return { instances = {}, capacityExpansionSteps = 0 }
end

local function newAnimalInstance(speciesId: string, via: ObtainedVia, now: number, sourceRef: string?): AnimalInstance
	return {
		id = HttpService:GenerateGUID(false),
		speciesId = speciesId,
		variant = nil,
		ascension = 0,
		obtainedAt = now,
		obtainedVia = via,
		sourceRef = sourceRef,
		oddsVersion = nil,
		prevOwnerId = nil,
		ascendedAt = nil,
		locks = { equipped = false, guarding = false, pendingTx = nil },
		userLocked = false,
	}
end
```

## Invariants

1. Every key of `instances` equals the value's `id`, and every `id` is unique across animals **and** eggs in the profile.
2. `0 ≤ ascension ≤ 5`, integer.
3. `speciesId` exists in config. If a species is removed from config, the instance is kept and flagged `orphaned` by a migration, never deleted silently ([[Data Validation and Migration]]).
4. `variant` is `nil` or eligible for that species in [[Animal Variants]].
5. `locks.equipped == true` if and only if the instance ID is in one of the team's three slots. The team is the authority.
6. `locks.guarding == true` if and only if the ID is in `base.guards`.
7. An instance with any lock set, or with `userLocked = true`, can never be consumed, merged, or moved by any transaction other than the one named in `pendingTx`.
8. Number of instances ≤ owned-animal capacity (prototype: 100, Q-022). Exceeding it is a soft failure: nothing is deleted, but new acquisitions are blocked until the player is under capacity. What happens when a raider at capacity steals an animal is **UNDECIDED** (Q-957).
9. `obtainedVia = "steal"` requires `sourceRef` (raid ID) and `prevOwnerId`. `obtainedVia = "hatch"` requires `sourceRef` (egg ID) and `oddsVersion`.
10. The number of animals stolen in a raid is **not** stored here. It belongs to the raid session and the raid ledger.

## Edge cases

| Case | Handling |
|---|---|
| Ascension selects an equipped duplicate | Rejected. The UI only offers unlocked duplicates ([[UI - Ascension]]). |
| Animal stolen while it is the player's ascension original | Allowed if it was knocked out while defending. The full instance record moves to the raider; whether its ascension is kept is **UNDECIDED** ([[Open Questions#Q-025]]). |
| Starter animal from onboarding | `obtainedVia = "event"`, `sourceRef = "onboarding"` ([[New Player Onboarding]]) |
| Hatch of five eggs | Five instances created in one transaction, each with its own `sourceRef` and the same `oddsVersion` |

## Migration notes

- Adding a new `obtainedVia` value (for example `"trade"` if trading is ever approved, [[Open Questions#Q-026]]) requires a schema bump so older servers refuse the newer data instead of treating it as corrupt.
- If the ascension cap changes, a lower cap needs an explicit migration with a refund rule. It must not be handled by the validator clamp, which would silently destroy value.

## Size estimate

About 380 bytes per instance with all optional fields filled (Python mock, compact JSON). 100 instances ≈ 37 KiB; 1,000 ≈ 370 KiB, about 9% of the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Animal Collection System]]
- [[Ascension System]]
- [[Ascension Progression Table]]
- [[Implementation - Ascension Transaction]]
- [[Animal Theft Rules]]
- [[Schema - Equipped Team]]
- [[Schema - Discovery Index]]
- [[Data and Balancing Index]]
