---
title: Implementation - Ascension Transaction
type: implementation
category: progression
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - ascension
  - transactions
  - security
---

# Implementation - Ascension Transaction

Server implementation of one ascension step: consume duplicates of the same species, keep the original, raise its ascension level and charge the Cash fee. Rules are owned by [[Ascension System]] and [[Ascension Progression Table]]; this page shows the enforcement.

> [!success] CONFIRMED (D-019)
> Ascension consumes the required duplicates of the same animal. The original animal is retained.

> [!info] PROPOSED
> Five levels A1–A5 ([[Open Questions#Q-004]]), the duplicate counts ([[Open Questions#Q-005]]) and the fees `FeeBase × n` from [[Canonical Proposed Values]] §9 are **PROPOSED**. The payload, locks, one-step-per-request rule and the high-value confirmation are **PROPOSED** here. Code is **illustrative — not executed**.

## 1. Rules enforced

| # | Check | Reason code | Status |
|---|---|---|---|
| A1 | Profile loaded | `NOT_READY` | **PROPOSED** |
| A2 | Target animal exists and is owned by the caller | `ANIMAL_NOT_FOUND` | **PROPOSED** |
| A3 | Target below the maximum level (A5) | `MAX_ASCENSION` | **PROPOSED** (Q-004) |
| A4 | Exactly the required number of duplicates for the next step | `WRONG_DUPLICATE_COUNT` | **PROPOSED** (Q-005) |
| A5 | Duplicates are distinct, owned, and not the target | `INVALID_PAYLOAD` / `ANIMAL_NOT_FOUND` | **PROPOSED** |
| A6 | Every duplicate has the same `speciesId` as the target | `SPECIES_MISMATCH` | **CONFIRMED** principle (D-019) |
| A7 | No duplicate is in the equipped team | `ANIMAL_LOCKED` | **PROPOSED**: consuming an equipped animal would change the team, which is only allowed at base (D-010) |
| A8 | No involved animal is raid-locked (registered as a defender or guard in an active raid, or in theft escrow) | `ANIMAL_LOCKED` | **PROPOSED** |
| A9 | Caller is not in an active raid | `IN_RAID` | **PROPOSED** |
| A10 | Variant duplicates follow the variant policy | `VARIANT_NOT_ALLOWED` | **UNDECIDED** (Q-902) |
| A11 | High-value duplicates (ascended or variant) need `confirmHighValue = true` | `CONFIRMATION_REQUIRED` | **PROPOSED** (UX safety) |
| A12 | Cash ≥ fee | `INSUFFICIENT_CASH` | **PROPOSED** |

> [!warning] UNDECIDED (Q-902)
> Whether a variant animal (for example a Golden variant) counts as a duplicate of its base species, and whether variants may be consumed at all, is not decided. It depends on variant acquisition ([[Open Questions#Q-006]]) and stat bonuses ([[Open Questions#Q-024]]). The code reads `AscensionConfig.VARIANT_DUPLICATE_POLICY`, which defaults to `"reject"` as the safe prototyping choice. That default is not a design decision.

Whether ascension may only be performed at the player's base is left to [[Ascension System]]; the handler exposes a `REQUIRE_AT_BASE` flag (default `false`) so the rule can be switched without code changes.

## 2. Payload

```lua
-- RequestAscend (RemoteFunction), validated by the Remote Validation Layer
{
	targetUid: string,            -- 36-character GUID
	duplicateUids: { string },    -- 1..5 entries (max duplicates for any single step is 5)
	confirmHighValue: boolean?,
	idemKey: string,
}
```

The client chooses which duplicates to consume (so a player can keep a preferred copy). The server never auto-selects in this request; an "auto-pick" UI button runs client-side and sends explicit uids.

## 3. Code

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Services/AscensionService (excerpt)

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Txn = require(script.Parent.Parent.Shared.Txn)
local Idem = require(script.Parent.Parent.Shared.Idempotency)
local Registry = require(script.Parent.Parent.Registry)
local AscensionConfig = require(ReplicatedStorage.Shared.Config.AscensionConfig)
local RosterConfig = require(ReplicatedStorage.Shared.Config.RosterConfig)

--  AscensionConfig (PROPOSED values from Canonical Proposed Values §9):
-- 	MAX_LEVEL = 5,
-- 	DUPLICATES = {
-- 		Common    = { 1, 2, 3, 4, 5 },
-- 		Uncommon  = { 1, 2, 3, 3, 4 },
-- 		Rare      = { 1, 1, 2, 3, 3 },
-- 		Epic      = { 1, 1, 2, 2, 3 },
-- 		Legendary = { 1, 1, 1, 2, 2 },
-- 		Mythical  = { 1, 1, 1, 1, 2 },
-- 		Secret    = { 1, 1, 1, 1, 1 },
-- 	},
-- 	FEE_BASE = { Common = 100, Uncommon = 200, Rare = 400, Epic = 800,
-- 	             Legendary = 1600, Mythical = 3200, Secret = 6400 },
-- 	VARIANT_DUPLICATE_POLICY = "reject", -- UNDECIDED (Q-902)
-- 	REQUIRE_AT_BASE = false,

export type AscendRequest = {
	targetUid: string,
	duplicateUids: { string },
	confirmHighValue: boolean?,
	idemKey: string,
}

local AscensionService = { Name = "AscensionService" }

local function isLocked(player: Player, data: any, animal: any): boolean
	if animal.lockedBy ~= nil then
		return true -- raid escrow, guard duty during a raid, or another flow
	end
	return false
end

local function isEquipped(data: any, uid: string): boolean
	for _, equippedUid in data.team.equipped do -- exactly three slots (D-006)
		if equippedUid == uid then
			return true
		end
	end
	return false
end

function AscensionService.handleAscend(player: Player, req: AscendRequest): any
	local DataService = Registry.get("DataService")
	local RaidService = Registry.get("RaidService")
	local BaseService = Registry.get("BaseService")

	local cached = Idem.get(player, req.idemKey)
	if cached then
		return cached
	end
	local profile = DataService.getLoadedProfile(player)
	if not profile then
		return { ok = false, reason = "NOT_READY" }
	end
	if RaidService.isInActiveRaid(player) then
		return { ok = false, reason = "IN_RAID" }
	end
	if AscensionConfig.REQUIRE_AT_BASE and not BaseService.isAtOwnBase(player) then
		return { ok = false, reason = "NOT_AT_BASE" }
	end

	local newLevel = 0
	local feeCharged = 0

	-- ===== No yields from here =====
	local ok, reason = Txn.run(profile, { "animals", "economy", "team" }, function(data)
		-- Index the collection once.
		local byUid: { [string]: any } = {}
		for _, a in data.animals.items do
			byUid[a.uid] = a
		end

		local target = byUid[req.targetUid]
		if target == nil then
			return false, "ANIMAL_NOT_FOUND"
		end
		if isLocked(player, data, target) then
			return false, "ANIMAL_LOCKED"
		end
		if target.ascension >= AscensionConfig.MAX_LEVEL then
			return false, "MAX_ASCENSION"
		end

		local species = RosterConfig.BY_ID[target.speciesId]
		local rarity = species.rarity
		local step = target.ascension + 1
		local required = AscensionConfig.DUPLICATES[rarity][step]
		if #req.duplicateUids ~= required then
			return false, "WRONG_DUPLICATE_COUNT"
		end

		local consume: { [string]: boolean } = {}
		local highValue = false
		for _, uid in req.duplicateUids do
			if uid == req.targetUid or consume[uid] then
				return false, "INVALID_PAYLOAD" -- target listed as its own duplicate, or repeated uid
			end
			local d = byUid[uid]
			if d == nil then
				return false, "ANIMAL_NOT_FOUND"
			end
			if d.speciesId ~= target.speciesId then
				return false, "SPECIES_MISMATCH"
			end
			if isEquipped(data, uid) or isLocked(player, data, d) then
				return false, "ANIMAL_LOCKED"
			end
			if d.variant ~= nil then
				if AscensionConfig.VARIANT_DUPLICATE_POLICY == "reject" then
					return false, "VARIANT_NOT_ALLOWED"
				end
				highValue = true
			end
			if d.ascension > 0 then
				highValue = true
			end
			consume[uid] = true
		end
		if highValue and req.confirmHighValue ~= true then
			return false, "CONFIRMATION_REQUIRED"
		end

		local fee = AscensionConfig.FEE_BASE[rarity] * step
		if data.economy.cash < fee then
			return false, "INSUFFICIENT_CASH"
		end

		-- Mutation. Everything above is read-only, so a failure before this point
		-- leaves data untouched; Txn's snapshot protects the lines below.
		local kept = table.create(#data.animals.items - required)
		for _, a in data.animals.items do
			if not consume[a.uid] then
				table.insert(kept, a)
			end
		end
		data.animals.items = kept
		target.ascension = step
		data.economy.cash -= fee

		-- Guards assigned from pens are unassigned if consumed (raid not active, checked above).
		if data.base and data.base.guardUids then
			for i = #data.base.guardUids, 1, -1 do
				if consume[data.base.guardUids[i]] then
					table.remove(data.base.guardUids, i)
				end
			end
		end

		newLevel = step
		feeCharged = fee
		return true, nil
	end, {
		function(data)
			if data.economy.cash < 0 then
				return false, "negative cash"
			end
			-- The original must still exist (D-019).
			for _, a in data.animals.items do
				if a.uid == req.targetUid then
					return true, nil
				end
			end
			return false, "target animal missing after ascension"
		end,
	})
	-- ===== End of no-yield region =====

	local response
	if ok then
		response = { ok = true, targetUid = req.targetUid, newLevel = newLevel, fee = feeCharged }
		Registry.get("AnalyticsAndLoggingService").logAscension(player, req.targetUid, newLevel, req.duplicateUids, feeCharged)
		DataService.requestSave(player, "ascension")
		Registry.get("TeamService").refreshStatsIfEquipped(player, req.targetUid) -- +8% HP/ATK/DEF per level
	else
		response = { ok = false, reason = reason }
	end
	if ok or reason == "SPECIES_MISMATCH" or reason == "ANIMAL_NOT_FOUND" or reason == "MAX_ASCENSION" then
		Idem.put(player, req.idemKey, response)
	end
	return response
end

return AscensionService
```

## 4. Rollback

`Txn.run` deep-copies `animals`, `economy` and `team` before the mutator runs. Rollback happens in four situations:

| Trigger | Example | Result |
|---|---|---|
| Mutator returns `false` | `INSUFFICIENT_CASH` found after validation | Snapshot restored (nothing had changed yet) |
| Mutator throws | A nil index on a corrupt record | Snapshot restored, `INTERNAL_ERROR` returned by the gateway |
| Mutator yields | A developer adds a `DataStore` call inside | Snapshot restored, error raised, caught in tests |
| Invariant fails | Target missing after the edit | Snapshot restored, error raised and logged as a severity 1 defect ([[Bug Reporting and Severity]]) |

All-or-nothing means: either all duplicates are removed **and** the level rises **and** the fee is charged, or none of these happens.

## 5. Stats are derived, never stored

The profile stores `ascension` only. HP, ATK and DEF are computed when needed:

`Stat = Reference × M(rarity) × RoleMultiplier × SpeciesTweak × (1 + 0.08 × ascension) × (1 + TrainingGroundsBonus)`

(+8% per level and the Training Grounds +4% per level are **PROPOSED**, canonical §9 and §12.) Storing derived stats invites desynchronisation and makes balance patches require data migration ([[Data Validation and Migration]]).

## 6. Worked example

A player owns four [[Tiger]] copies (Epic) and ascends the original from A0 to A1, then A1 to A2.

| Step | Duplicates required | Fee (`800 × n`) | Copies left including original |
|---|---:|---:|---:|
| A0 → A1 | 1 | 800 | 3 |
| A1 → A2 | 1 | 1,600 | 2 |
| A2 → A3 | 2 | 2,400 | 0 duplicates left — blocked until another Tiger hatches |

Full Epic path A0 → A5: 9 duplicates and 800 × (1+2+3+4+5) = **12,000 Cash** (**PROPOSED**). Expected-value analysis is in [[Ascension Expected Value Analysis]].

## 7. Edge cases

- **Duplicate currently equipped:** rejected; the player returns to base and unequips first (D-010).
- **Target currently equipped:** allowed; the team does not change, only the target's stats.
- **Target or duplicate listed twice:** `INVALID_PAYLOAD`.
- **Stolen-animal edge:** an animal in theft escrow carries `lockedBy = raidId` and cannot be used. What a stolen animal keeps (including its ascension) is **UNDECIDED** ([[Open Questions#Q-025]]).
- **Concurrent merge or hatch request:** processed sequentially; no shared animals between flows, but cash is shared and is re-read inside each transaction.

## 8. Test hooks

[[Test Cases - Ascension]]: each reason code; A5 target; Secret path (1 duplicate per step); forced invariant failure; idempotent replay; equipped duplicate; variant duplicate under each policy.

## Related documents
- [[Ascension System]]
- [[Ascension Progression Table]]
- [[Ascension Expected Value Analysis]]
- [[Implementation - Egg Roll and Hatch Flow#Transaction helper]]
- [[Team Equipping and Base Lock Rule]]
- [[Data Consistency and Transactions]]
- [[Service - AscensionService]]
- [[UI - Ascension]]
