---
title: Service - IndexService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - index
  - collection
  - progression
---

# Service - IndexService

> [!info] PROPOSED
> Layer **2**. Design is **PROPOSED**; code is illustrative Luau, not tested. Feature design: [[Animal Index Feature Specification]], [[Animal Collection System]]. Schema: [[Schema - Discovery Index]]. Screen: [[UI - Animal Index Screen]].

> [!success] CONFIRMED rule (D-029)
> Defeating wild animals registers them in the index. The index distinguishes **discovered** animals from **owned** animals.

## Responsibility

- Record a species as **discovered** when the player receives kill credit for a wild animal of that species.
- Record a species as **owned** when the player obtains one (hatch, raid theft).
- Keep simple per-species counters for the index screen (wild defeats, first discovered time).
- Provide the unique-discovery count for the Progression Score (3 points per species, max 180).
- Notify the client of first-time discoveries.

## Inputs

| Input | Source |
|---|---|
| `RegisterDiscovery(player, speciesId)` | [[Service - CombatService]] (kill credit) |
| `MarkOwnedInProfile(data, speciesId)` inside a mutation | [[Service - HatchService]], [[Service - RaidService]] |

## Outputs

| Output | Consumer |
|---|---|
| `index` profile section | Client via deltas |
| `SpeciesDiscovered(player, speciesId, firstTime)` | [[Service - LuckService]] (PS), analytics |
| `SpeciesOwned(player, speciesId, firstTime)` | LuckService (if ownership is ever added to PS), analytics |
| `Index/SpeciesDiscovered` | Client toast |

## Dependencies

[[Service - DataService]], [[Service - AnalyticsAndLoggingService]].

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `SpeciesDiscovered` | `(player, speciesId: string, firstTime: boolean)` |
| Signal | `SpeciesOwned` | `(player, speciesId: string, firstTime: boolean)` |
| Remote S→C | `Index/SpeciesDiscovered` | `{ speciesId, firstTime }` (only sent when `firstTime` is true) |

## Data structures

```lua
--!strict
export type IndexEntry = {
	discoveredAt: number?,   -- os.time() of first credited wild defeat (or first ownership, see below)
	ownedEver: boolean,      -- has ever owned at least one
	wildDefeats: number,     -- capped at 1e6
}

export type IndexSection = {
	entries: { [string]: IndexEntry },  -- speciesId -> entry; absent = undiscovered
	discoveredCount: number,            -- cached; recomputed and verified on load
}
```

"Currently owned" is not stored here; it is derived from the animal collection ([[Schema - Animal Collection]]) so it can never disagree with it. The index screen shows three states: undiscovered, discovered, owned.

## Discovery by hatching

> [!warning] UNDECIDED (Q-806): does obtaining an animal count as discovering it?
> A player can hatch or steal a species they have never fought. Options: (a) ownership also sets `discoveredAt` (index stays intuitive: every owned animal is discovered, and it counts towards the Progression Score); (b) discovery is only from wild defeats, as literally stated in D-029, so an owned-but-undiscovered state exists. The service supports both with `IndexConfig.ownershipCountsAsDiscovery`; working assumption **(a)**, `true`. Because discovery feeds the Progression Score, the choice slightly changes odds progression and must be settled together with [[Open Questions#Q-017]].

## Public API

```lua
--!strict
function IndexService:RegisterDiscovery(player: Player, speciesId: string): boolean  -- returns firstTime
function IndexService:MarkOwnedInProfile(data: ProfileData, speciesId: string): boolean -- inside Mutate with "index"
function IndexService:IsDiscovered(player: Player, speciesId: string): boolean
function IndexService:HasOwned(player: Player, speciesId: string): boolean
function IndexService:GetDiscoveredCount(player: Player): number
```

```lua
--!strict
-- Illustrative Luau, not tested.
function IndexService:RegisterDiscovery(player, speciesId)
	if not AnimalCatalogue.byId[speciesId] then return false end  -- bosses and unknown IDs ignored
	local firstTime = false
	Data:Mutate(player, "discovery", { "index" }, function(data)
		local entry = data.index.entries[speciesId]
		if not entry then
			entry = { discoveredAt = nil, ownedEver = false, wildDefeats = 0 }
			data.index.entries[speciesId] = entry
		end
		entry.wildDefeats = math.min(entry.wildDefeats + 1, 1e6)
		if entry.discoveredAt == nil then
			entry.discoveredAt = os.time()
			data.index.discoveredCount += 1
			firstTime = true
		end
		return true
	end)
	if firstTime then
		IndexService.SpeciesDiscovered:Fire(player, speciesId, true)
	end
	return firstTime
end
```

## Error handling

| Case | Behaviour |
|---|---|
| Unknown species ID (config mismatch after a content update) | Ignored, `Warn` log once per species per server |
| `discoveredCount` disagrees with entries on load | Recomputed from entries; `Info` log `index.recount` |
| Profile not loaded at credit time | Skipped; the next credited defeat registers it |

## Security requirements

- No remote writes the index. Discovery comes only from server-side kill credit; ownership only from server transactions.
- Kill credit already requires ≥ 10% contribution (D-040), so a player cannot discover a species by tagging it with a single hit.

## Testing requirements

| Test | Type |
|---|---|
| First credited defeat sets `discoveredAt` and fires `SpeciesDiscovered` once | Unit |
| Second defeat increments `wildDefeats` only | Unit |
| Non-credited contributor (< 10%) does not discover | Integration with CombatService |
| Hatch sets `ownedEver`; with `ownershipCountsAsDiscovery = true` it also discovers | Unit |
| Discovering all 60 species gives 180 PS points | Unit with LuckService |
| Index screen state equals derived ownership after an ascension consumes the last duplicate | Integration |

## Related documents
- [[Technical Architecture Index]]
- [[Animal Index Feature Specification]]
- [[Animal Collection System]]
- [[Schema - Discovery Index]]
- [[Progression Score Specification]]
- [[Service - LuckService]]
- [[UI - Animal Index Screen]]
