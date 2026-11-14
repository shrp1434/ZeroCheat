---
title: Service - EggService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - eggs
  - inventory
  - probability
---

# Service - EggService

> [!info] PROPOSED
> Layer **5**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design sources: [[Egg System Overview]], [[Egg Roll System]], [[Egg Storage]], [[Egg Pricing]]. Schema: [[Schema - Egg Inventory]]. Flow detail: [[Implementation - Egg Roll and Hatch Flow]].

> [!success] CONFIRMED rules enforced here
> Cash buys egg rolls (D-014). The roll decides egg rarity (stage 1 of D-015). Odds are shown before commit and never silently changed (D-017). Storage starts at **Backpack 10 + Base 50 = 60**; backpack eggs can never be stolen; extra space can be bought, currency and price **UNDECIDED** (D-021, [[Open Questions#Q-009]], [[Open Questions#Q-010]]).

## Responsibility

- Own the **egg inventory**: every egg record, its location (Backpack or Base) and storage capacity.
- Issue **roll quotes** (price, odds, destination, `quoteId`, `oddsVersion`) and commit **rolls**: debit and rarity selection in one transaction.
- Move eggs between backpack and base storage (at the player's own base).
- Provide composable add, remove and transfer helpers used inside other services' mutations: HatchService (consume), MergeService (consume 3, add 1), RaidService (theft transfer).
- Enforce capacity on every insertion and the "backpack eggs are never stealable" rule on every transfer.
- Query `PolicyService` at join and expose the result for any future paid random product.

## Inputs

| Input | Source |
|---|---|
| `Eggs/GetRollQuote`, `Eggs/RequestRoll`, `Eggs/MoveEggs` | Client |
| Current egg odds and `oddsVersion` | [[Service - LuckService]] |
| Cash checks and debits | [[Service - EconomyService]] |
| `IsAtOwnBase(player)` | [[Service - BaseService]] |
| Capacity expansions | Profile (written by a storage-expansion product once Q-009/Q-010 are decided) |
| Egg locks | `Systems/AssetLocks` |

## Outputs

| Output | Consumer |
|---|---|
| `eggs` profile section changes | Client via DataService deltas |
| `EggsRolled(player, eggs)`, `EggsAdded`, `EggsRemoved` signals | Analytics, HatchService (quote invalidation), UI notifications |
| `egg_rolled`, `cash_sink` analytics | AnalyticsAndLoggingService |

## Dependencies

[[Service - LuckService]], [[Service - EconomyService]], [[Service - BaseService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `WeightedRandom`, `QuoteStore`, `AssetLocks`. Roblox: `PolicyService`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `EggsRolled` | `(player, eggs: { EggRecord }, quote: RollQuote)` |
| Signal | `EggsAdded` | `(player, eggs: { EggRecord }, source: EggSource)` |
| Signal | `EggsRemoved` | `(player, eggIds: { string }, reason: string)` |
| Remotes | `Eggs/GetRollQuote`, `Eggs/RequestRoll`, `Eggs/MoveEggs` | [[Remote Communication Contract#2.4 Eggs, luck and hatching]] |

## Data structures

```lua
--!strict
export type EggLocation = "Backpack" | "Base"
export type EggSource = "Roll" | "Merge" | "Raid" | "Event" | "Admin"

export type EggRecord = {
	id: string,              -- server-issued, unique within the profile
	rarity: Rarity,
	location: EggLocation,
	obtainedAt: number,      -- os.time()
	source: EggSource,
}

export type EggsSection = {
	records: { [string]: EggRecord },
	backpackCapacity: number,    -- 10 at start (CONFIRMED), max 25 (PROPOSED)
	baseCapacity: number,        -- 50 at start (CONFIRMED), max 200 (PROPOSED)
	nextEggSerial: number,
}

export type RollQuote = {
	quoteId: string,
	userId: number,
	count: number,               -- 1 or 5
	price: number,               -- 200 or 1,000 Cash (PROPOSED, Q-020)
	odds: OddsTable,             -- exact odds that will be applied
	display: { [string]: string },
	oddsVersion: string,
	destination: { backpack: number, base: number }, -- how many eggs go where
	expiresAt: number,
}
```

**PROPOSED values introduced here:** quote lifetime **60 s**; consumed-quote replay window **30 s** (a repeat confirm returns the original result).

## Destination rule

> [!warning] UNDECIDED (Q-804): where newly rolled eggs go
> When a roll produces eggs, they must be stored somewhere. Options: (a) backpack first, overflow to base storage, reject only if both are full; (b) backpack only, reject if it is full; (c) base storage only. Option (a) is convenient but places overflow eggs where they can be stolen in a raid, which the player must be told in the quote. Recommendation (**PROPOSED** working assumption): (a), with the destination split shown in the quote. The service implements all three through `EggConfig.rollDestination`.

Roll location (anywhere, only at the egg shrine in [[Hub - Hatchling Haven]], or shrine and base) is a design rule owned by [[Egg Roll System]]; the service enforces it through `ZoneQuery` using `EggConfig.rollLocation`.

## Public API

```lua
--!strict
-- Read
function EggService:GetEggs(player: Player): { [string]: EggRecord }
function EggService:GetFreeCapacity(player: Player): { backpack: number, base: number }
function EggService:GetPolicyFlags(player: Player): { paidRandomItemsRestricted: boolean }

-- Composable helpers: ONLY inside DataService:Mutate with "eggs" declared
function EggService:AddEggInProfile(data: ProfileData, rarity: Rarity, location: EggLocation, source: EggSource): EggRecord?
function EggService:RemoveEggsInProfile(data: ProfileData, ids: { string }): boolean          -- all or nothing
function EggService:TransferBaseEggsInPair(from: ProfileData, to: ProfileData, ids: { string },
	toLocation: EggLocation): boolean   -- refuses any egg whose location is Backpack

-- Remote handlers (bound by Net)
function EggService:HandleGetRollQuote(player: Player, p: { count: number }): Result<RollQuote>
function EggService:HandleRequestRoll(player: Player, p: { quoteId: string, oddsVersion: string }): Result<{ eggs: { EggRecord } }>
function EggService:HandleMoveEggs(player: Player, p: { eggIds: { string }, to: EggLocation }): Result<{ moved: number }>
```

## Roll commit

```lua
--!strict
-- Illustrative Luau, not tested.
function EggService:HandleRequestRoll(player, p)
	local replay = QuoteStore:GetConsumedResult(player, p.quoteId)
	if replay then return replay end                      -- idempotent retry

	local quote = QuoteStore:Peek(player, p.quoteId, "Roll") :: RollQuote?
	if not quote then return Err("E_QUOTE_UNKNOWN") end
	if workspace:GetServerTimeNow() > quote.expiresAt then return Err("E_QUOTE_EXPIRED") end
	if p.oddsVersion ~= quote.oddsVersion or not Luck:IsCurrent(player, quote.oddsVersion) then
		QuoteStore:Discard(player, p.quoteId)
		return Err("E_STALE_ODDS")
	end

	local rolled = {}
	local ok = Data:Mutate(player, "egg_roll", { "eggs", "economy" }, function(data)
		if not Economy:DebitInProfile(data, quote.price, "EggRoll") then return false end
		local placement = planPlacement(data, quote.count)   -- same rule the quote used
		if not placement then return false end
		for i = 1, quote.count do
			local rarity = WeightedRandom.pick(rng, quote.odds) -- the QUOTED odds, never recomputed
			local egg = EggService:AddEggInProfile(data, rarity, placement[i], "Roll")
			if not egg then return false end
			table.insert(rolled, egg)
		end
		return true
	end)

	if not ok then
		-- distinguish the common rule failures for the player
		if Economy:GetCash(player) < quote.price then return Err("E_INSUFFICIENT_CASH") end
		return Err("E_STORAGE_FULL")
	end

	local result = Ok({ eggs = rolled })
	QuoteStore:Consume(player, p.quoteId, result)          -- keeps result for the 30 s replay window
	EggService.EggsRolled:Fire(player, rolled, quote)
	Log:Event("egg_rolled", player, { count = quote.count, oddsVersion = quote.oddsVersion })
	return result
end
```

`rng` is a single server `Random.new()` instance (seeded by the engine); every egg draws independently. See [[Implementation - Weighted Random Selection]] and [[Independent Random Outcomes]].

## Error handling

| Case | Code |
|---|---|
| Unknown, foreign or already-discarded quote | `E_QUOTE_UNKNOWN` |
| Quote older than 60 s | `E_QUOTE_EXPIRED` |
| Odds changed since the quote | `E_STALE_ODDS` (client re-quotes; nothing charged) |
| Not enough Cash | `E_INSUFFICIENT_CASH` |
| No room for all eggs under the destination rule | `E_STORAGE_FULL` or `E_BACKPACK_FULL` (checked at quote time and again at commit) |
| Move while not at own base | `E_NOT_AT_BASE` |
| Egg locked (raid claim, pending merge or hatch quote) | `E_ASSET_LOCKED` |
| `PolicyService` call fails | Treated as most restrictive; logged |

## Security requirements

- The client never names a rarity. Rarity is chosen by server RNG with the quoted odds.
- Debit and egg creation are one `Mutate`; there is no state in which a player is charged without eggs, or gets eggs without being charged.
- `TransferBaseEggsInPair` checks `location == "Base"` for **every** egg and fails the whole transfer otherwise: backpack eggs are never stealable (D-021).
- Eggs on the defender's side are locked against moves, hatching and merging while a raid on their base is active (**UNDECIDED**, Q-808, see [[Service - RaidService]]); otherwise a defender could empty base storage mid-raid.
- `PolicyService:GetPolicyInfoForPlayerAsync` is called once per session; if `ArePaidRandomItemsRestricted` is true, any future product that sells a random item for Robux must be hidden and refused for that player. Egg rolls bought with Cash are not paid random items as long as Cash cannot be bought with Robux (D-044 **PROPOSED**, [[Open Questions#Q-032]]).

## Testing requirements

| Test | Type |
|---|---|
| Quote then confirm: Cash debited by exactly the quoted price; eggs created equal count | Unit |
| Confirm after levelling up: `E_STALE_ODDS`, Cash unchanged | Integration |
| Same `quoteId` confirmed twice: second returns the same eggs, no second charge | Unit |
| Quote from player A used by player B: `E_QUOTE_UNKNOWN` | Exploit test |
| Roll ×5 with 3 free backpack and 1 free base slot: rejected before charge | Unit |
| Backpack egg included in a theft transfer: whole transfer fails | Unit |
| 1,000,000 rolls at fixed odds match within confidence intervals | Statistical |
| Storage expansion remote/product absent while `StorageExpansion` flag is off | Unit |

Full list: [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Inventory and Storage]].

## Related documents
- [[Technical Architecture Index]]
- [[Egg Roll System]]
- [[Egg Storage]]
- [[Egg Pricing]]
- [[Schema - Egg Inventory]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Implementation - Weighted Random Selection]]
- [[Service - LuckService]]
- [[Service - HatchService]]
- [[Randomised Reward Compliance]]
