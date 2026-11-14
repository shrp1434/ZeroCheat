---
title: Schema - Egg Inventory
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - eggs
  - storage
---

# Schema - Egg Inventory

## Purpose

Stores every unhatched egg the player owns, where it is (backpack or base storage), how it was obtained and, for rolled eggs, the exact odds version the player saw when they committed the roll. Rules are owned by [[Egg Storage]], [[Egg Roll System]], [[Hatch System]] and [[Egg Merging]].

> [!success] CONFIRMED
> Storage starts at **Backpack 10 + Base 50 = 60** (D-021). Backpack eggs can never be stolen; base eggs can be stolen during an eligible raid (D-024). Up to **5** eggs hatch at once (D-016). Merging turns **3** eggs of one rarity into **1** egg of the next rarity (D-020). Odds must be shown before committing and never change silently after a purchase (D-017).

> [!warning] UNDECIDED
> Storage expansion currency and price are **UNDECIDED** ([[Open Questions#Q-009]], [[Open Questions#Q-010]]). The schema stores only the number of expansion steps bought, so no migration is needed whichever currency is chosen. Egg theft limits per raid are **UNDECIDED** ([[Open Questions#Q-013]]).

## Inventory fields (`eggs`)

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `instances` | `{ [string]: EggInstance }` | Required | `{}` | Keys are GUIDs equal to each value's `id` | Both locations in one map; location is a field |
| `backpackExpansionSteps` | `number` | Required | `0` | Integer 0–3 | Backpack capacity = `10 + 5 × steps` (max 25, PROPOSED steps) |

Base (vault) capacity is derived from `base.storage.vaultExpansionSteps` in [[Schema - Base Data]]: `50 + 25 × steps` (max 200, PROPOSED steps).

## Egg instance fields

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `id` | `string` | Required | `HttpService:GenerateGUID(false)` | 36-character GUID, unique across the profile | Server-generated |
| `rarity` | `Rarity` | Required | — | One of the seven rarity names | `"Common"` … `"Secret"` |
| `location` | `"backpack" \| "base"` | Required | — | One of the two | Base eggs can only be hatched at the player's base (PROPOSED) |
| `obtainedVia` | `"roll" \| "merge" \| "steal" \| "reward"` | Required | — | One of the four | Provenance |
| `obtainedAt` | `number` | Required | `os.time()` | Unix seconds, ≤ now | |
| `oddsVersion` | `string?` | Optional | `nil` | **Required** when `obtainedVia = "roll"`; pattern below | The odds version displayed and accepted when the roll was committed (audit) |
| `rollId` | `string?` | Optional | `nil` | GUID; required when `obtainedVia = "roll"` | Links to the roll record in `AuditLog_v1` |
| `sourceRef` | `string?` | Optional | `nil` | ≤ 64 characters | Merge: merge transaction ID. Steal: raid ID. Reward: reward or grant ID. |
| `prevOwnerId` | `number?` | Optional | `nil` | Required when `obtainedVia = "steal"` | Audit only |
| `pendingTx` | `string?` | Optional | `nil` | Transaction ID | Locks the egg during a hatch, merge or raid transfer |

### The `oddsVersion` value (PROPOSED)

Odds are a pure function of the odds configuration version and the player's Progression Score at the moment of the roll ([[Dynamic Progression Luck]], [[Progression Score Specification]]). The stored value is therefore deterministic and short: `o<configVersion>.p<PS as 4 digits>`, for example `"o12.p0347"`. Audit tooling can recompute the exact table the player was shown from it. The token issued to the client (D-041, **PROPOSED**) may carry extra fields such as a nonce and expiry, but only this deterministic part is persisted. Validation pattern: `^o%d+%.p%d%d%d%d$` (Luau string pattern).

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
local HttpService = game:GetService("HttpService")

export type Rarity = "Common" | "Uncommon" | "Rare" | "Epic" | "Legendary" | "Mythical" | "Secret"
export type EggLocation = "backpack" | "base"
export type EggVia = "roll" | "merge" | "steal" | "reward"

export type EggInstance = {
	id: string,
	rarity: Rarity,
	location: EggLocation,
	obtainedVia: EggVia,
	obtainedAt: number,
	oddsVersion: string?,
	rollId: string?,
	sourceRef: string?,
	prevOwnerId: number?,
	pendingTx: string?,
}

export type EggInventory = {
	instances: { [string]: EggInstance },
	backpackExpansionSteps: number,
}

local BACKPACK_BASE, BACKPACK_STEP = 10, 5 -- 10 CONFIRMED, step PROPOSED
local VAULT_BASE, VAULT_STEP = 50, 25 -- 50 CONFIRMED, step PROPOSED

local function newEggInventory(): EggInventory
	return { instances = {}, backpackExpansionSteps = 0 }
end

local function newRolledEgg(rarity: Rarity, location: EggLocation, oddsVersion: string, rollId: string, now: number): EggInstance
	return {
		id = HttpService:GenerateGUID(false),
		rarity = rarity,
		location = location,
		obtainedVia = "roll",
		obtainedAt = now,
		oddsVersion = oddsVersion,
		rollId = rollId,
		sourceRef = nil,
		prevOwnerId = nil,
		pendingTx = nil,
	}
end

local function counts(inv: EggInventory): (number, number)
	local backpack, base = 0, 0
	for _, egg in inv.instances do
		if egg.location == "backpack" then backpack += 1 else base += 1 end
	end
	return backpack, base
end

local function backpackCapacity(inv: EggInventory): number
	return BACKPACK_BASE + BACKPACK_STEP * inv.backpackExpansionSteps
end
```

## Invariants

1. **Backpack eggs ≤ backpack capacity**, with a base capacity of **10** (`10 + 5 × backpackExpansionSteps`).
2. **Base eggs ≤ vault capacity**, with a base capacity of **50** (`50 + 25 × vaultExpansionSteps`).
3. Every `id` is unique across eggs and animals in the profile.
4. Eggs with `location = "backpack"` are never included in a raid manifest. The raid controller filters by location and the ledger validator rejects a manifest containing one ([[Egg Theft Rules]]).
5. `obtainedVia = "roll"` requires `oddsVersion` and `rollId`. A rolled egg without them is a soft failure (kept, flagged for review), because a missing audit trail is a compliance issue but not a reason to remove the player's egg.
6. Eggs never change rarity. Merging consumes three eggs and creates a new one with a new ID.
7. A hatch request contains 1–5 eggs, all unlocked; base eggs only when the player is at their base.
8. A merge consumes exactly 3 unlocked eggs of the same rarity, which must not be `"Secret"`, with the required [[Egg Merging Station]] level ([[Schema - Base Data]]).
9. A commit that would exceed either capacity is rejected, never over-filled. Over-capacity found on load (for example after a config error) is a soft failure: nothing is deleted, and adding eggs to that location is blocked until it is back within capacity.

## Edge cases

| Case | Handling |
|---|---|
| Roll when the backpack is full | The roll's destination rule lives in [[Egg Roll System]]. The data layer rejects any commit that has no free slot in the chosen location. Capacity is checked **before** Cash is deducted, in the same synchronous block. |
| Merge output when base storage is full | The canonical rule says the output goes to base storage. If all three inputs come from the backpack and the vault is full, base storage would exceed capacity. Validation must check `baseCount − inputsFromBase + 1 ≤ vaultCapacity`. The resolution (block the merge, or place the output in the backpack) is **UNDECIDED** (Q-954). |
| Stolen eggs arriving at the raider | Destination and full-storage behaviour are **UNDECIDED** (Q-951). The data layer only guarantees invariants 1–2 at commit time. |
| Odds changed between display and confirmation | The server rejects the stale token and nothing is written ([[Randomised Reward Compliance]]) |
| ×5 roll | Five eggs, one `rollId` each, sharing the same `oddsVersion` |

## Migration notes

- If expansion step sizes change, `backpackExpansionSteps` and `vaultExpansionSteps` keep their meaning as "steps bought". A migration may convert steps if the new sizes would reduce anyone's capacity. Reducing a capacity below a player's current egg count must never delete eggs.
- A new `obtainedVia` value (for example `"event"` for event-exclusive eggs) needs a schema bump.

## Size estimate

About 265 bytes per egg with optional fields filled (Python mock). Starting maximum 60 eggs ≈ 16 KiB; full expansion of 225 eggs ≈ 58 KiB, about 1.4% of the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Egg Storage]]
- [[Egg Roll System]]
- [[Hatch System]]
- [[Egg Merging]]
- [[Implementation - Egg Roll and Hatch Flow]]
- [[Implementation - Egg Merge Transaction]]
- [[Storage Expansion Economics]]
- [[Schema - Base Data]]
- [[Data and Balancing Index]]
