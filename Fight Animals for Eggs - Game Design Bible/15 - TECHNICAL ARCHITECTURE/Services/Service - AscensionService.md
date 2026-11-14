---
title: Service - AscensionService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - ascension
  - animals
  - transactions
---

# Service - AscensionService

> [!info] PROPOSED
> Layer **5**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design: [[Ascension System]], [[Ascension Progression Table]]. Transaction detail: [[Implementation - Ascension Transaction]]. Levels **UNDECIDED** ([[Open Questions#Q-004]]), duplicate counts **UNDECIDED** ([[Open Questions#Q-005]]); the working values are in [[Canonical Proposed Values#9. Ascension (PROPOSED — levels Q-004, duplicates Q-005)]].

> [!success] CONFIRMED rule enforced here (D-019)
> Ascension consumes duplicates of the same animal. The original animal is retained.

## Responsibility

- Validate and commit ascension of one owned animal by **one level per request**: consume the required duplicates of the **same species**, charge the Cash fee, increment the level.
- Provide authoritative previews (required duplicates, eligible duplicate IDs, fee).
- Notify combat and AI so an equipped companion's stats update at once (+8% HP, ATK and DEF of base per level; +5% ability effectiveness per level, **PROPOSED**).

## Inputs

| Input | Source |
|---|---|
| `Ascension/GetPreview`, `Ascension/RequestAscend` | Client |
| Animal records | Profile `animals` section via `Systems/AnimalLedger` |
| `IsEquipped(player, animalId)` | [[Service - TeamService]] |
| Asset locks (raid claims, open quotes) | `Systems/AssetLocks` |
| Cash debit | [[Service - EconomyService]] |
| Combat tag | `Systems/CombatTags` |

## Outputs

| Output | Consumer |
|---|---|
| `animals` and `economy` section changes | Client via deltas |
| `AnimalAscended(player, animalId, newLevel)` signal | AnimalAIService (refresh companion stats), analytics |
| `animal_ascended`, `cash_sink` analytics | AnalyticsAndLoggingService |

## Dependencies

[[Service - EconomyService]], [[Service - TeamService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `AnimalLedger`, `AssetLocks`, `CombatTags`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `AnimalAscended` | `(player, animalId: string, newLevel: number, consumedIds: { string })` |
| Remotes | `Ascension/GetPreview`, `Ascension/RequestAscend` | [[Remote Communication Contract#2.5 Ascension, merging, base, team]] |

## Data structures

```lua
--!strict
export type AscensionRule = {
	duplicates: { number },   -- duplicates needed for A1..A5
	feeBase: number,          -- fee for step n = feeBase * n
}

-- Mirrors Canonical Proposed Values §9 (PROPOSED)
local RULES: { [Rarity]: AscensionRule } = {
	Common    = { duplicates = { 1, 2, 3, 4, 5 }, feeBase = 100 },
	Uncommon  = { duplicates = { 1, 2, 3, 3, 4 }, feeBase = 200 },
	Rare      = { duplicates = { 1, 1, 2, 3, 3 }, feeBase = 400 },
	Epic      = { duplicates = { 1, 1, 2, 2, 3 }, feeBase = 800 },
	Legendary = { duplicates = { 1, 1, 1, 2, 2 }, feeBase = 1600 },
	Mythical  = { duplicates = { 1, 1, 1, 1, 2 }, feeBase = 3200 },
	Secret    = { duplicates = { 1, 1, 1, 1, 1 }, feeBase = 6400 },
}
local MAX_LEVEL = 5 -- PROPOSED (Q-004)

export type AscensionPreview = {
	animalId: string,
	currentLevel: number,
	nextLevel: number?,           -- nil at max
	duplicatesRequired: number,
	eligibleDuplicateIds: { string },
	fee: number,
}
```

Worked example: a Rare [[Wolf]] at A2 going to A3 needs **2** Wolf duplicates and a fee of `400 × 3` = **1,200 Cash**. After commit, the Wolf's HP, ATK and DEF are base × 1.24 (A3 = +24%).

## Duplicate eligibility

| Rule | Status |
|---|---|
| Same `speciesId` as the target | **CONFIRMED** (D-019) |
| Owned by the requester, not the target itself, no repeats in the list | **PROPOSED** |
| Not equipped in the team | **PROPOSED** (protects the player from consuming an active companion) |
| Not locked (raid, open quote, pending transaction) | **PROPOSED** |
| Variant duplicates: may a Golden or other variant animal be consumed, and must variants match? | **UNDECIDED** (Q-801) |
| Duplicates that are themselves ascended (A1+): consumable or not, and any refund | **UNDECIDED** (Q-802); working assumption: only A0 duplicates are eligible |
| Location: anywhere outside combat, or only at the base | **UNDECIDED** (Q-805); working assumption: anywhere outside combat, via `AscensionConfig.requireAtBase = false` |

## Public API

```lua
--!strict
function AscensionService:GetPreview(player: Player, animalId: string): Result<AscensionPreview>
function AscensionService:HandleRequestAscend(player: Player, p: {
	animalId: string, duplicateIds: { string }, expectedLevel: number,
}): Result<{ animalId: string, newLevel: number }>
function AscensionService:GetStatMultiplier(level: number): number      -- 1 + 0.08 * level
function AscensionService:GetAbilityMultiplier(level: number): number   -- 1 + 0.05 * level
```

## Commit

```lua
--!strict
-- Illustrative Luau, not tested. Full transaction: Implementation - Ascension Transaction.
function AscensionService:HandleRequestAscend(player, p)
	if CombatTags.isTagged(player) then return Err("E_IN_COMBAT") end
	local data = Data:GetProfile(player) and Data:GetProfile(player).data
	if not data then return Err("E_NOT_READY") end

	local target = data.animals.records[p.animalId]
	if not target then return Err("E_NOT_OWNED") end
	if target.ascension ~= p.expectedLevel then return Err("E_STALE_STATE") end
	if target.ascension >= MAX_LEVEL then return Err("E_MAX_ASCENSION") end

	local nextLevel = target.ascension + 1
	local rule = RULES[target.rarity]
	local required = rule.duplicates[nextLevel]
	local fee = rule.feeBase * nextLevel

	local check = validateDuplicates(player, data, target, p.duplicateIds, required)
	if not check.ok then return check end                      -- E_DUPLICATES_INVALID / E_ASSET_LOCKED

	local ok = Data:Mutate(player, "ascend", { "animals", "economy" }, function(d)
		if not Economy:DebitInProfile(d, fee, "AscensionFee") then return false end
		if not AnimalLedger.removeInProfile(d, p.duplicateIds) then return false end
		local t = d.animals.records[p.animalId]
		if not t or t.ascension ~= p.expectedLevel then return false end
		t.ascension = nextLevel
		return true
	end)
	if not ok then
		return Err(Economy:GetCash(player) < fee and "E_INSUFFICIENT_CASH" or "E_INTERNAL")
	end

	AscensionService.AnimalAscended:Fire(player, p.animalId, nextLevel, p.duplicateIds)
	return Ok({ animalId = p.animalId, newLevel = nextLevel })
end
```

## Error handling

| Case | Code |
|---|---|
| Target not owned | `E_NOT_OWNED` |
| Already at A5 | `E_MAX_ASCENSION` |
| `expectedLevel` mismatch (double click, stale UI) | `E_STALE_STATE` |
| Wrong count, wrong species, includes target, equipped, repeated ID, ascended duplicate | `E_DUPLICATES_INVALID` |
| Duplicate or target locked | `E_ASSET_LOCKED` |
| Not enough Cash | `E_INSUFFICIENT_CASH` |
| In combat | `E_IN_COMBAT` |

## Security requirements

- The client never sends a level, stat or fee. `expectedLevel` is only a staleness guard.
- Duplicates are validated by server records; species is read from the record, never from the payload.
- Fee, consumption and level increment are one `Mutate`.
- The target is retained in all cases (D-019); the code path never removes `p.animalId` (a unit test asserts the target ID is not in `duplicateIds`).
- A target or duplicate that is claimed in an active raid is locked and cannot be ascended or consumed ([[Service - RaidService]]).

## Testing requirements

| Test | Type |
|---|---|
| Each rarity and level: required duplicates and fee match the table | Unit (35 cases) |
| Including the target in `duplicateIds` is rejected | Unit |
| Using a different species as a duplicate is rejected | Unit |
| Double submit with the same `expectedLevel` ascends once | Unit |
| Insufficient Cash leaves duplicates intact | Unit |
| Equipped companion stats update immediately after ascension | Integration |
| Locked (raid-claimed) duplicate rejected | Integration ([[Test Cases - Raiding]]) |

Full list: [[Test Cases - Ascension]].

## Related documents
- [[Technical Architecture Index]]
- [[Ascension System]]
- [[Ascension Progression Table]]
- [[Ascension Expected Value Analysis]]
- [[Implementation - Ascension Transaction]]
- [[Schema - Animal Collection]]
- [[UI - Ascension]]
- [[Test Cases - Ascension]]
