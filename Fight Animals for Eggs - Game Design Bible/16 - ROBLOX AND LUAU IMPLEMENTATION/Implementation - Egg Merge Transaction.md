---
title: Implementation - Egg Merge Transaction
type: implementation
category: eggs
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - eggs
  - merging
  - transactions
  - security
---

# Implementation - Egg Merge Transaction

Server implementation of merging three eggs of one rarity into one egg of the next rarity at the [[Egg Merging Station]]. Game rules are owned by [[Egg Merging]]; this page shows enforcement.

> [!success] CONFIRMED (D-020)
> 3 eggs of one rarity → 1 egg of the next rarity. A purchased Egg Merging Station is required. Higher rarities need station upgrades. Secret eggs cannot be merged further (there is no rarity above Secret).

> [!info] PROPOSED
> Station levels, gates and fees ([[Open Questions#Q-019]]), merging at the base, output to base storage, the instant result with animation ([[Open Questions#Q-034]]), and all locks and codes on this page are **PROPOSED**. Code is **illustrative — not executed**.

## 1. Station gates and fees (canonical §10, PROPOSED)

| Input rarity | Output rarity | Station level needed | Fee (Cash) |
|---|---|---:|---:|
| Common | Uncommon | 1 | 100 |
| Uncommon | Rare | 1 | 300 |
| Rare | Epic | 2 | 900 |
| Epic | Legendary | 3 | 2,700 |
| Legendary | Mythical | 4 | 8,000 |
| Mythical | Secret | 5 | 25,000 |
| Secret | — | — | Not mergeable (**CONFIRMED**) |

Station purchase and upgrades are handled by [[Service - BaseService]]; level gates such as "Region 4 unlocked" apply to buying the upgrade, not to each merge.

## 2. Checks

| # | Check | Reason code |
|---|---|---|
| M1 | Profile loaded | `NOT_READY` |
| M2 | Station owned (level ≥ 1) | `STATION_NOT_OWNED` |
| M3 | Player at own base, within interaction range of the station | `NOT_AT_BASE` / `OUT_OF_RANGE` |
| M4 | Not in an active raid (as attacker or defender) | `IN_RAID` |
| M5 | Exactly three distinct egg uids | `INVALID_PAYLOAD` |
| M6 | All three owned by the caller | `EGG_NOT_FOUND` |
| M7 | All three the same rarity | `RARITY_MISMATCH` |
| M8 | Rarity below Secret | `MAX_RARITY` |
| M9 | Station level unlocks this merge | `STATION_LEVEL_TOO_LOW` |
| M10 | No egg locked (`lockedBy` set by raid escrow, a pending hatch or another merge) | `EGG_LOCKED` |
| M11 | Base storage has room for the output after inputs are removed | `BASE_STORAGE_FULL` |
| M12 | Cash ≥ fee | `INSUFFICIENT_CASH` |

> [!warning] UNDECIDED (Q-903) — output when base storage is full
> Canonical §10 sends the output to base storage and notes total capacity always frees by two. But if all three inputs come from the backpack and base storage is full (50/50), base storage has no room for the output. Options: (a) reject with `BASE_STORAGE_FULL` (implemented as the safe prototyping behaviour), (b) place the output in a freed backpack slot, (c) let the player choose. Option (b) would make the output unstealable, which changes raid exposure. Not decided.

> [!danger] Why merging is blocked during a raid
> If a defender could merge base eggs mid-raid, they could shrink the stealable pool on demand, and an attacker could not reliably resolve a claim. M4 and M10 together make the stealable set stable for the whole raid ([[Raid Anti-Exploit Validation]]).

## 3. Payload

```lua
-- RequestMergeEggs (RemoteFunction)
{
	eggUids: { string },   -- exactly 3
	idemKey: string,
}
```

## 4. Code

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Services/MergeService (excerpt)

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local HttpService = game:GetService("HttpService")

local Txn = require(script.Parent.Parent.Shared.Txn)
local Idem = require(script.Parent.Parent.Shared.Idempotency)
local Registry = require(script.Parent.Parent.Registry)
local RarityConfig = require(ReplicatedStorage.Shared.Config.RarityConfig)

local MERGE_INPUT_COUNT = 3 -- CONFIRMED (D-020)

-- PROPOSED (Canonical Proposed Values §10). Keyed by INPUT rarity.
local MERGE_RULES: { [string]: { level: number, fee: number } } = table.freeze({
	Common    = { level = 1, fee = 100 },
	Uncommon  = { level = 1, fee = 300 },
	Rare      = { level = 2, fee = 900 },
	Epic      = { level = 3, fee = 2700 },
	Legendary = { level = 4, fee = 8000 },
	Mythical  = { level = 5, fee = 25000 },
	-- Secret intentionally absent: not mergeable (CONFIRMED)
})

export type MergeRequest = { eggUids: { string }, idemKey: string }

local MergeService = { Name = "MergeService" }

function MergeService.handleMerge(player: Player, req: MergeRequest): any
	local DataService = Registry.get("DataService")
	local BaseService = Registry.get("BaseService")
	local RaidService = Registry.get("RaidService")

	local cached = Idem.get(player, req.idemKey)
	if cached then
		return cached
	end
	local profile = DataService.getLoadedProfile(player)
	if not profile then
		return { ok = false, reason = "NOT_READY" }
	end
	if #req.eggUids ~= MERGE_INPUT_COUNT then
		return { ok = false, reason = "INVALID_PAYLOAD" }
	end
	if RaidService.isInActiveRaid(player) or RaidService.isBaseUnderRaid(player) then
		return { ok = false, reason = "IN_RAID" }
	end
	if not BaseService.isAtOwnBase(player) then
		return { ok = false, reason = "NOT_AT_BASE" }
	end
	if not BaseService.isNearModule(player, "EggMergingStation") then
		return { ok = false, reason = "OUT_OF_RANGE" }
	end

	local output: any = nil
	local feeCharged = 0

	-- ===== No yields from here =====
	local ok, reason = Txn.run(profile, { "eggs", "economy" }, function(data)
		local stationLevel = data.base.modules.EggMergingStation or 0
		if stationLevel < 1 then
			return false, "STATION_NOT_OWNED"
		end

		local byUid: { [string]: any } = {}
		for _, egg in data.eggs.items do
			byUid[egg.uid] = egg
		end

		local chosen: { [string]: boolean } = {}
		local rarity: string? = nil
		local fromBase = 0
		for _, uid in req.eggUids do
			if chosen[uid] then
				return false, "INVALID_PAYLOAD"
			end
			chosen[uid] = true
			local egg = byUid[uid]
			if egg == nil then
				return false, "EGG_NOT_FOUND"
			end
			if egg.lockedBy ~= nil then
				return false, "EGG_LOCKED"
			end
			if rarity == nil then
				rarity = egg.rarity
			elseif egg.rarity ~= rarity then
				return false, "RARITY_MISMATCH"
			end
			if egg.location == "Base" then
				fromBase += 1
			end
		end
		assert(rarity ~= nil)

		local rule = MERGE_RULES[rarity]
		local nextRarity = RarityConfig.nextOf(rarity :: any)
		if rule == nil or nextRarity == nil then
			return false, "MAX_RARITY"
		end
		if stationLevel < rule.level then
			return false, "STATION_LEVEL_TOO_LOW"
		end

		-- Capacity: output goes to base storage (PROPOSED). Inputs removed from base free slots.
		local baseCount = 0
		for _, egg in data.eggs.items do
			if egg.location == "Base" then
				baseCount += 1
			end
		end
		if baseCount - fromBase + 1 > data.eggs.baseCapacity then
			return false, "BASE_STORAGE_FULL" -- see Q-903
		end

		if data.economy.cash < rule.fee then
			return false, "INSUFFICIENT_CASH"
		end

		-- Mutation
		local kept = table.create(#data.eggs.items)
		for _, egg in data.eggs.items do
			if not chosen[egg.uid] then
				table.insert(kept, egg)
			end
		end
		output = {
			uid = HttpService:GenerateGUID(false),
			rarity = nextRarity,
			location = "Base",
			source = "Merge",
			acquiredAt = os.time(),
		}
		table.insert(kept, output)
		data.eggs.items = kept
		data.economy.cash -= rule.fee
		feeCharged = rule.fee
		return true, nil
	end, {
		function(data)
			return data.economy.cash >= 0, "negative cash"
		end,
		function(data)
			local b, s = 0, 0
			for _, egg in data.eggs.items do
				if egg.location == "Backpack" then b += 1 else s += 1 end
			end
			return b <= data.eggs.backpackCapacity and s <= data.eggs.baseCapacity, "capacity exceeded"
		end,
	})
	-- ===== End of no-yield region =====

	local response
	if ok then
		response = { ok = true, egg = output, fee = feeCharged }
		Registry.get("AnalyticsAndLoggingService").logMerge(player, req.eggUids, output, feeCharged)
		DataService.requestSave(player, "merge")
	else
		response = { ok = false, reason = reason }
	end
	if ok or reason == "RARITY_MISMATCH" or reason == "MAX_RARITY" or reason == "EGG_NOT_FOUND" then
		Idem.put(player, req.idemKey, response)
	end
	return response
end

return MergeService
```

## 5. All-or-nothing and rollback

The three input eggs are removed, the output egg is added and the fee is charged inside one `Txn.run` ([[Implementation - Egg Roll and Hatch Flow#Transaction helper]]). If anything fails, the `eggs` and `economy` snapshots are restored. The count invariant (net −2 eggs) is implied by the capacity invariant and is asserted directly in unit tests.

| Failure point | Effect |
|---|---|
| Any check M5–M12 | No change; reason code returned |
| Error during mutation | Snapshot restored; `INTERNAL_ERROR` |
| Crash before save | Profile reverts to the last save: three inputs still present, no output, fee not charged |
| Crash after save | Merge durable |

There is no window in which the output exists while the inputs also exist, or in which the inputs are gone without an output, because both changes are inside the same in-memory transaction and the same save.

## 6. Worked example

Station level 2 (Stonebound Hatchery Forge). The player selects three Rare eggs: two from base storage (base 50/50) and one from the backpack.

- M9: Rare→Epic needs level 2: pass.
- M11: base count 50 − 2 + 1 = 49 ≤ 50: pass.
- Fee 900 Cash debited. Base storage now 49/50, backpack one fewer. Total eggs −2.

If instead all three Rare eggs came from the backpack with base at 50/50: 50 − 0 + 1 = 51 > 50 → `BASE_STORAGE_FULL` (see Q-903).

## 7. Edge cases

- **Mixed locations:** allowed (canonical §10: input eggs may come from the backpack or base storage).
- **Egg in a pending hatch:** a hatch completes within its own transaction, so a separate `lockedBy = "hatch"` only exists if timed incubation is adopted (Q-023).
- **Station downgraded or destroyed in a raid:** station levels cannot decrease in the current proposal; if base damage is ever introduced, M9 re-reads the level inside the transaction.
- **Animation:** 2.5–6 s by tier is client-only; the result is already committed ([[Animation - Egg Merge]]).

## 8. Test hooks

[[Test Cases - Egg Merging]]: every reason code; Secret input; station level boundaries; base-full with backpack inputs; idempotent replay; merge attempt during a raid on the player's base.

## Related documents
- [[Egg Merging]]
- [[Egg Merging Station]]
- [[Egg Storage]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Implementation - Raid Session Controller]]
- [[Data Consistency and Transactions]]
- [[Service - MergeService]]
- [[UI - Egg Merging]]
