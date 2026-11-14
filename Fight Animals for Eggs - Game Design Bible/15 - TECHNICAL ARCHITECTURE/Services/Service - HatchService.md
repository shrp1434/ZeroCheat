---
title: Service - HatchService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - hatching
  - eggs
  - probability
---

# Service - HatchService

> [!info] PROPOSED
> Layer **6**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design sources: [[Hatch System]], [[Independent Random Outcomes]], [[Hatch Pool Tables]]. Flow detail: [[Implementation - Egg Roll and Hatch Flow]]. Schema: [[Schema - Animal Collection]].

> [!success] CONFIRMED rules enforced here
> Hatching picks an animal from the egg rarity's pool (stage 2 of D-015). **Up to five** eggs per hatch (D-016). Every hatch is independent: no duplicate protection, no bias towards unowned animals, no influence from earlier hatches (D-018). Odds disclosed before commit (D-017).

## Responsibility

- Issue **hatch quotes** for 1 to 5 eggs, listing each egg's rarity and that pool's current per-species odds, with `quoteId` and `oddsVersion`.
- Commit **hatches**: consume the eggs and create one animal per egg, each drawn independently with the quoted pool odds, in a single transaction.
- Enforce **≤ 5 eggs per request**, ownership, locks, hatch-location rules and owned-animal capacity.
- Mark hatched species as owned in the index.
- Request a priority save after hatching Legendary or rarer animals (**PROPOSED**).

## Inputs

| Input | Source |
|---|---|
| `Hatch/GetHatchQuote`, `Hatch/RequestHatch` | Client |
| Egg records and helpers | [[Service - EggService]] |
| Pool odds and `oddsVersion` | [[Service - LuckService]] |
| `IsAtOwnBase` | [[Service - BaseService]] |
| `IsInCombat` | CombatService (read via a lower-layer query: `Systems/CombatTags`, so HatchService does not depend on layer 7) |
| Animal record creation | `Systems/AnimalLedger` |
| Owned flag | [[Service - IndexService]] |

## Outputs

| Output | Consumer |
|---|---|
| `animals`, `eggs`, `index` profile changes | Client via deltas |
| `AnimalsHatched(player, results)` signal | Analytics, notifications, TeamService (UI hints only) |
| `egg_hatched` analytics with `oddsVersion` | [[Service - AnalyticsAndLoggingService]], [[Statistical Testing of Probabilities]] |

## Dependencies

[[Service - EggService]], [[Service - LuckService]], [[Service - IndexService]], [[Service - BaseService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `WeightedRandom`, `QuoteStore`, `AssetLocks`, `AnimalLedger`, `CombatTags`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `AnimalsHatched` | `(player, results: { HatchResult }, quote: HatchQuote)` |
| Remotes | `Hatch/GetHatchQuote`, `Hatch/RequestHatch` | [[Remote Communication Contract#2.4 Eggs, luck and hatching]] |

## Data structures

```lua
--!strict
export type AnimalRecord = {
	id: string,              -- server-issued
	speciesId: string,
	rarity: Rarity,
	ascension: number,       -- 0..5
	variant: string?,        -- acquisition UNDECIDED (Q-006); nil at launch unless decided
	obtainedAt: number,
	source: "Hatch" | "Raid" | "Event" | "Admin",
}

export type HatchQuote = {
	quoteId: string,
	userId: number,
	eggs: { { eggId: string, rarity: Rarity, pool: OddsTable } },  -- 1..5 entries
	oddsVersion: string,
	expiresAt: number,
}

export type HatchResult = { eggId: string, animalId: string, speciesId: string, rarity: Rarity }
```

**PROPOSED values used:** maximum 5 eggs per request (**CONFIRMED**); quote lifetime 60 s; replay window 30 s; owned-animal capacity 100 (working assumption, **UNDECIDED** [[Open Questions#Q-022]]).

## Hatch location and timing

| Rule | Status |
|---|---|
| Backpack eggs: hatch anywhere outside combat | **PROPOSED** ([[Canonical Proposed Values#7. Eggs, rolls and hatching]]) |
| Base-stored eggs: hatch only at the player's own base | **PROPOSED** |
| Result decided instantly; client plays a 3.5 s (single) or 5.0 s (multi) reveal, skippable after first viewing | **PROPOSED** |
| Timed incubation alternative | **UNDECIDED** ([[Open Questions#Q-023]]). If chosen, a new `incubating` egg state with a server timestamp is added; the roll of the species still happens at the moment the player confirms, against the disclosed odds |

## Public API

```lua
--!strict
function HatchService:HandleGetHatchQuote(player: Player, p: { eggIds: { string } }): Result<HatchQuote>
function HatchService:HandleRequestHatch(player: Player, p: { quoteId: string, oddsVersion: string }): Result<{ results: { HatchResult } }>
function HatchService:InvalidateQuotes(player: Player, reason: string): ()   -- on OddsInvalidated, raid start, egg removal
```

## Commit

```lua
--!strict
-- Illustrative Luau, not tested.
local MAX_PER_HATCH = 5 -- CONFIRMED (D-016)

function HatchService:HandleRequestHatch(player, p)
	local replay = QuoteStore:GetConsumedResult(player, p.quoteId)
	if replay then return replay end

	local quote = QuoteStore:Peek(player, p.quoteId, "Hatch") :: HatchQuote?
	if not quote then return Err("E_QUOTE_UNKNOWN") end
	if workspace:GetServerTimeNow() > quote.expiresAt then return Err("E_QUOTE_EXPIRED") end
	if p.oddsVersion ~= quote.oddsVersion or not Luck:IsCurrent(player, quote.oddsVersion) then
		QuoteStore:Discard(player, p.quoteId)
		return Err("E_STALE_ODDS")
	end
	assert(#quote.eggs >= 1 and #quote.eggs <= MAX_PER_HATCH)

	local recheck = revalidateLocationAndCombat(player, quote)   -- base eggs need IsAtOwnBase, no combat tag
	if not recheck.ok then return recheck end

	local results = {}
	local ok = Data:Mutate(player, "hatch", { "eggs", "animals", "index" }, function(data)
		if AnimalLedger.freeSlots(data) < #quote.eggs then return false end
		local ids = {}
		for _, e in quote.eggs do table.insert(ids, e.eggId) end
		if not Eggs:RemoveEggsInProfile(data, ids) then return false end   -- all must still exist
		for _, e in quote.eggs do
			-- Independent draw per egg, using the exact quoted pool odds (D-017, D-018)
			local speciesId = WeightedRandom.pick(rng, e.pool)
			local animal = AnimalLedger.addInProfile(data, speciesId, e.rarity, "Hatch")
			Index:MarkOwnedInProfile(data, speciesId)
			table.insert(results, { eggId = e.eggId, animalId = animal.id, speciesId = speciesId, rarity = e.rarity })
		end
		return true
	end)
	if not ok then return Err("E_ANIMAL_STORAGE_FULL") end

	local response = Ok({ results = results })
	QuoteStore:Consume(player, p.quoteId, response)
	AssetLocks:ReleaseAll(player, "HatchQuote", p.quoteId)
	HatchService.AnimalsHatched:Fire(player, results, quote)
	if anyAtLeast(results, "Legendary") then Data:RequestPrioritySave(player, "rare_hatch") end
	return response
end
```

Quote-time checks (in `HandleGetHatchQuote`): 1 ≤ count ≤ 5 (`E_HATCH_LIMIT`), no duplicate egg IDs, every egg owned (`E_NOT_OWNED`), none locked (`E_ASSET_LOCKED`), base eggs only at the base (`E_NOT_AT_BASE`), not in combat (`E_IN_COMBAT`), free animal slots ≥ count (`E_ANIMAL_STORAGE_FULL`). On success the eggs are soft-locked under the quote until it is consumed, discarded or expires, so they cannot be merged or moved in between.

## Error handling

| Case | Code |
|---|---|
| More than 5 eggs or none | `E_HATCH_LIMIT` / `E_INVALID_PAYLOAD` |
| Eggs not owned or already consumed | `E_NOT_OWNED` |
| Odds changed | `E_STALE_ODDS` (client re-quotes) |
| Quote expired | `E_QUOTE_EXPIRED` |
| Owned-animal storage full | `E_ANIMAL_STORAGE_FULL` |
| Raid started on the player's base after the quote | Quote invalidated by RaidService; `E_QUOTE_UNKNOWN` (shown as generic retry) |

## Security requirements

- The client never names a species, a pool or a weight. It sends only a `quoteId` and the `oddsVersion` it displayed.
- Species are drawn with the **quoted** pool table after checking the token is current; odds are never recomputed between display and draw.
- Independence (D-018): the draw does not read the collection, index, previous hatches or duplicate counts. A static review rule forbids reading `data.animals` or `data.index` before `WeightedRandom.pick` in this function.
- Egg consumption and animal creation are one `Mutate`: no egg can be consumed without producing its animal, and no animal can appear without consuming its egg.

## Testing requirements

| Test | Type |
|---|---|
| Hatch of 6 eggs rejected at quote time | Unit |
| Hatch of 5 eggs consumes exactly 5 and creates exactly 5 animals | Unit |
| Same quote confirmed twice: one set of animals | Unit |
| Merge attempted on an egg inside an open hatch quote: `E_ASSET_LOCKED` | Integration |
| Owning every Common species does not change Common pool frequencies over 1,000,000 hatches | Statistical (D-018) |
| Observed species frequency per pool matches [[Hatch Pool Tables]] within confidence intervals | Statistical |
| Base egg hatch attempted away from base: `E_NOT_AT_BASE` | Unit |
| Hatch during combat tag: `E_IN_COMBAT` | Unit |

Full list: [[Test Cases - Egg Rolls and Hatching]].

## Related documents
- [[Technical Architecture Index]]
- [[Hatch System]]
- [[Hatch Pool Tables]]
- [[Independent Random Outcomes]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Schema - Animal Collection]]
- [[Service - EggService]]
- [[Service - LuckService]]
- [[UI - Egg Hatching]]
- [[Animation - Egg Hatch]]
