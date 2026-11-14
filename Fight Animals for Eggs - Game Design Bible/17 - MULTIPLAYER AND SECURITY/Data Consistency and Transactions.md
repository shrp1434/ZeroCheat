---
title: Data Consistency and Transactions
type: architecture
category: data
status: proposed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - data
  - persistence
  - transactions
  - security
  - multiplayer
---

# Data Consistency and Transactions

How the game keeps player data correct when many requests arrive at once, players change servers, servers crash, and raids move items between two players. Profile structure is owned by [[Data Architecture Overview]] and the schema pages; save and recovery operations by [[Save, Load and Recovery]]; the service by [[Service - DataService]].

> [!info] PROPOSED
> Every mechanism here is **PROPOSED**. DataStore and MemoryStore signatures and the quoted limits were checked on 2026-11-14 ([[Roblox API Reference Notes]]). Some `UpdateAsync` transform semantics are *unverified* and flagged below. Code is **illustrative — not executed**.

## 1. Consistency layers

| Layer | Problem it solves | Mechanism |
|---|---|---|
| 1. In-memory transaction | Partial updates inside one server | `Txn.run` / `txn2`: snapshot, mutate without yielding, invariants, rollback ([[Implementation - Egg Roll and Hatch Flow#Transaction helper]]) |
| 2. Idempotency | Retries and double submits | Per-player key cache; receipt ids for Robux purchases |
| 3. Session lock | Two servers loading the same profile (rejoin, second device) | Lock field written with `UpdateAsync` |
| 4. Durable save | Crash loses in-memory state | `UpdateAsync` after transactions, coalesced; autosave; save on leave and shutdown |
| 5. Two-profile journal | Raid transfer where one save succeeds and the other fails | Raid journal entry as the commit point, plus `appliedRaids` per profile |
| 6. Cross-server locks | Same defender targeted from two servers; defender profile moving servers mid-raid | MemoryStore sorted-map lock with expiry |

## 2. Session locking

Each profile record stores a lock:

```lua
-- Stored value for key "player_<UserId>" (illustrative)
{
	schemaVersion = 3,
	data = { ... },            -- profile sections: economy, eggs, animals, team, base, index, raids, ...
	meta = {
		lock = { jobId = "<DataModel.JobId>", acquiredAt = 1763100000, heartbeatAt = 1763100060 }?,
		saveCount = 412,
		lastSavedAt = 1763100060,
	},
}
```

| Parameter | Value | Status |
|---|---|---|
| Autosave interval (also refreshes `heartbeatAt`) | 60 s | **PROPOSED** |
| Lock timeout (stale lock may be taken over) | 300 s since `heartbeatAt` | **PROPOSED** |
| Load retries when the lock is held | 5 attempts, back-off 2, 4, 6, 8, 10 s | **PROPOSED** |
| Coalesced transaction saves | ≤ 1 write per player per 6 s | **PROPOSED** |

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Services/DataService/SessionLock (excerpt)

local DataStoreService = game:GetService("DataStoreService")
local store = DataStoreService:GetDataStore("PlayerProfiles_v1")

local LOCK_TIMEOUT = 300
local JOB = game.JobId

export type LoadResult = "loaded" | "locked" | "error"

-- *Unverified*: the transform receives the current value (nil for a new key), may return nil
-- to cancel the write, and must not yield. Confirm against the GlobalDataStore guide before use.
local function tryLoad(userId: number): (LoadResult, any?)
	local loaded: any = nil
	local lockedElsewhere = false
	local ok, err = pcall(function()
		store:UpdateAsync("player_" .. userId, function(current: any)
			local now = os.time()
			local rec = current or { schemaVersion = 0, data = nil, meta = { saveCount = 0 } }
			local lock = rec.meta.lock
			if lock and lock.jobId ~= JOB and now - lock.heartbeatAt < LOCK_TIMEOUT then
				lockedElsewhere = true
				return nil -- cancel: another live server owns this profile
			end
			rec.meta.lock = { jobId = JOB, acquiredAt = now, heartbeatAt = now }
			loaded = rec
			return rec
		end)
	end)
	if not ok then
		warn("Profile load error", userId, err)
		return "error", nil
	end
	if lockedElsewhere then
		return "locked", nil
	end
	return "loaded", loaded
end

-- Returns false if this server no longer owns the lock (another server stole a stale lock).
local function save(userId: number, profile: any, release: boolean): boolean
	local stillOwner = true
	local ok, err = pcall(function()
		store:UpdateAsync("player_" .. userId, function(current: any)
			if current and current.meta.lock and current.meta.lock.jobId ~= JOB then
				stillOwner = false
				return nil -- never overwrite a profile owned by another server
			end
			local now = os.time()
			local rec = {
				schemaVersion = profile.schemaVersion,
				data = profile.serialise(), -- strips transient fields such as lockedBy, escrow, quotes
				meta = {
					saveCount = ((current and current.meta.saveCount) or 0) + 1,
					lastSavedAt = now,
					lock = if release then nil else { jobId = JOB, acquiredAt = profile.lockAcquiredAt, heartbeatAt = now },
				},
			}
			return rec
		end)
	end)
	if not ok then
		warn("Profile save error", userId, err)
		return true -- still owner as far as we know; retry later
	end
	return stillOwner
end
```

If `save` returns `false`, this server has lost ownership (it was paused beyond the lock timeout and another server took over). The profile is marked read-only, all economy remotes return `NOT_READY`, and the player is kicked with a "please rejoin" message. This prevents two servers writing divergent copies.

> [!note] Community libraries
> ProfileStore and its predecessor ProfileService are widely used community modules that implement session locking on DataStores. Adopting one is a valid alternative to the code above; evaluate in [[M02 - Core Project Setup]] (**PROPOSED** evaluation).

## 3. Write budget check

Standard write budget per server: `60 + numPlayers × 40` requests per minute (checked 2026-11-14). At 16 players: **700 writes/min**.

| Source | Worst case per minute at 16 players | Notes |
|---|---:|---|
| Autosave (60 s) | 16 | |
| Coalesced transaction saves (≤ 1 per 6 s per player) | 160 | Only if every player trades constantly |
| Raid commits (journal + index + 2 profiles) | ~8 | Assumes ≤ 2 raids per minute per server |
| Leave saves | ≤ 16 | |
| **Total** | **≈ 200** | ~29% of budget, leaving headroom for retries |

## 4. Saving rules

1. Transactions mark the profile dirty; `requestSave` coalesces.
2. Raid commits and Robux grants use `saveNow` (immediate, still respecting the per-player minimum gap by queuing).
3. `PlayerRemoving`: run leaving callbacks, then save with `release = true`, retrying up to 3 times.
4. `BindToClose`: save all loaded profiles in parallel with `task.spawn` and wait for completion.
5. Transient fields (`lockedBy`, raid escrow, odds quotes, idempotency caches) are never serialised. A crash therefore always yields a clean, unlocked profile.

## 5. Two-profile transfers: the raid journal

A raid commit changes **two** profiles. Both are loaded and locked in the same server, so the in-memory part is atomic (`txn2`). The risk is durability: one save may succeed and the other fail (crash between them). The journal makes the transfer recoverable without duplication.

| Step | Action | Crash after this step leads to |
|---|---|---|
| 1 | `txn2` applies the transfer in memory; both profiles get `raids.applied[raidId]` | Nothing durable yet; both revert; transfer never happened (consistent) |
| 2 | **Commit point:** `UpdateAsync("raid_<raidId>")` writes the journal entry `{ attackerId, defenderId, eggUids, animalRecords, status = "committed" }`, and appends `raidId` to `raididx_<attackerId>` and `raididx_<defenderId>` | Journal exists; neither profile saved. On next load, each profile applies its side (below) |
| 3 | Save defender profile | Defender durable; attacker applies on next load |
| 4 | Save attacker profile | Both durable |
| 5 | Mark journal `status = "applied"` (best effort) | Harmless if skipped |

**Reconciliation on load:** after loading a profile, read its `raididx_<userId>` list. For each journal entry with `status = "committed"` whose `raidId` is not in `raids.applied`:

- Defender side: remove the listed eggs and animals **if present**, then set `applied[raidId]`.
- Attacker side: add the listed eggs and animals **if not already present by uid**, then set `applied[raidId]`.

Because every item has a unique uid and both sides check `applied[raidId]` and uid presence, reconciliation is idempotent and an item can never end up in both profiles once both have loaded. `raids.applied` keeps the last 50 raid ids (**PROPOSED**).

## 6. Robux purchases

`MarketplaceService.ProcessReceipt` grants must be durable before returning `PurchaseGranted`; otherwise return `NotProcessedYet` so Roblox retries (behaviour per the official sample, checked 2026-11-14). The profile stores processed `PurchaseId`s (last 100, **PROPOSED**) so a retried receipt is not granted twice. Which products exist is owned by [[Monetisation Product Concepts]]; no product grants Cash (D-044, **PROPOSED**).

## 7. Cross-server considerations

| Concern | Approach | Status |
|---|---|---|
| Same profile in two servers | Session lock (§2) | **PROPOSED** |
| Same defender raided from two servers | MemoryStore lock `RaidLocks/<defenderUserId>` acquired with `UpdateAsync` before `Countdown`; TTL = duration + countdown + 60 s grace ([[Implementation - Raid Session Controller]]) | **PROPOSED** |
| Raids against players in other servers | Not at launch; would need teleport and the MemoryStore lock as a hard requirement | **UNDECIDED** (Q-901) |
| Server-wide announcements across servers | `MessagingService`; best-effort, never used for economy | **PROPOSED** |
| Global leaderboards | Ordered DataStore, updated at most once per 5 min per player; out of launch scope | **PROPOSED** |
| Clock skew between servers | Only lock timeouts compare times across servers; the 300 s timeout dwarfs normal skew | **PROPOSED** |
| Trading | Out of scope at launch (D-045, **PROPOSED**); would need the journal pattern | — |

### MemoryStore raid lock sizing

Each lock value is about 100 bytes. The experience-wide memory quota is `64 KB + 1.2 KB × users` and the request-unit limit `1000 + 120 × concurrent users` per minute (checked 2026-11-14). With two lock operations per raid (acquire and release), raid locks use a negligible fraction of both.

## 8. Invariants audited

| Invariant | Where checked |
|---|---|
| Cash ≥ 0 | Every economy transaction |
| Backpack ≤ capacity; base ≤ capacity | Roll, merge, raid commit |
| Animals ≤ capacity (Q-022) | Hatch, raid commit |
| Equipped team has exactly 3 valid owned animals, or empty slots only where the rules allow (Q-025) | Team change, ascension, raid commit |
| Egg and animal uids unique within a profile | Load-time validation ([[Data Validation and Migration]]) |
| Stolen animals per raid ≤ 3 | Raid commit |
| No backpack egg in any raid journal | Raid commit, journal write |

## Related documents
- [[Service - DataService]]
- [[Data Architecture Overview]]
- [[Save, Load and Recovery]]
- [[Data Validation and Migration]]
- [[Implementation - Raid Session Controller]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Disconnect Handling]]
- [[Schema - Player Profile]]
- [[Roblox API Reference Notes]]
