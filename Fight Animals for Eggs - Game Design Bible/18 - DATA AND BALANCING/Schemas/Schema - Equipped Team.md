---
title: Schema - Equipped Team
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - team
---

# Schema - Equipped Team

## Purpose

Stores which three owned animals the player has equipped. The rules (team changes only at the player's own base, locked after leaving until the player returns) are owned by [[Team Equipping and Base Lock Rule]] and enforced by [[Service - TeamService]].

> [!success] CONFIRMED
> Team size is exactly **three** (D-006). The team can only be changed at the player's own base and is locked from leaving the base until returning (D-010).

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `slot1` | `string?` | Optional | `nil` | `nil` or the ID of an owned animal instance | Slot order is display order ([[UI - Animal Team Display]]) |
| `slot2` | `string?` | Optional | `nil` | As above, distinct from the other slots | |
| `slot3` | `string?` | Optional | `nil` | As above, distinct from the other slots | |
| `revision` | `number` | Required | `0` | Integer ≥ 0, +1 per change | Lets the client discard stale team-change responses |
| `changedAt` | `number?` | Optional | `nil` | Unix seconds | Time of the last successful change (made at base) |

> [!info] Why three named fields and not an array
> An array `{id, nil, id}` has a hole, which does not serialise reliably to a DataStore (*unverified* exact behaviour). Three named optional fields always serialise cleanly, and missing keys simply mean empty slots. In memory, helpers expose the slots as an ordered list of three.

The team lock state ("locked because the player left base") is **not stored**. It is runtime state derived from the player's position and recomputed on spawn ([[Data Architecture Overview]] §3).

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type EquippedTeam = {
	slot1: string?,
	slot2: string?,
	slot3: string?,
	revision: number,
	changedAt: number?,
}

local TEAM_SIZE = 3 -- CONFIRMED

local function newEquippedTeam(): EquippedTeam
	return { slot1 = nil, slot2 = nil, slot3 = nil, revision = 0, changedAt = nil }
end

local function getSlot(team: EquippedTeam, i: number): string?
	if i == 1 then return team.slot1 elseif i == 2 then return team.slot2 elseif i == 3 then return team.slot3 end
	error("team slot out of range")
end

-- Server-side change request, called only when TeamService has confirmed the player is at their own base.
local function setTeam(profile, ids: { string? }, now: number): (boolean, string?)
	local seen = {}
	for i = 1, TEAM_SIZE do
		local id = ids[i]
		if id ~= nil then
			local animal = profile.animals.instances[id]
			if animal == nil then return false, "NOT_OWNED" end
			if seen[id] then return false, "DUPLICATE" end
			if animal.locks.pendingTx ~= nil then return false, "BUSY" end
			seen[id] = true
		end
	end
	local team = profile.team
	for i = 1, TEAM_SIZE do
		local old = getSlot(team, i)
		if old then profile.animals.instances[old].locks.equipped = false end
	end
	team.slot1, team.slot2, team.slot3 = ids[1], ids[2], ids[3]
	for id in seen do profile.animals.instances[id].locks.equipped = true end
	team.revision += 1
	team.changedAt = now
	return true, nil
end
```

## Invariants

1. The team has **exactly 3 slots**. There is no `slot4`; any extra slot key is a hard failure (rule H7 in [[Data Validation and Migration]]).
2. Each slot holds a **unique owned animal instance ID** or `nil`. `nil` is permitted only during setup, while the player owns fewer than three eligible animals, or transiently after an animal leaves the collection (see edge cases). The server prompts the player to fill empty slots at base.
3. No two slots hold the same ID.
4. For every animal, `locks.equipped` is true exactly when its ID is in a slot. The team is the authority; the flag is repaired on load.
5. Changes are accepted only when TeamService confirms the player is at their own base (runtime check, not stored).
6. An animal with `locks.pendingTx` set cannot be equipped.
7. Whether an equipped animal may also be a base guard depends on [[Open Questions#Q-033]] and [[Open Questions#Q-035]]. The validator reads a config flag (`allowEquippedGuards`) so the data model works for either decision.

## Edge cases

| Case | Handling |
|---|---|
| Equipped animal consumed by ascension | Impossible: equipped animals cannot be duplicates ([[Schema - Animal Collection]] invariant 7) |
| Equipped animal stolen in a raid (only possible if it defended and was knocked out) | The slot is cleared in the same transaction as the theft. What happens to the rest of the defender's team is **UNDECIDED** ([[Open Questions#Q-025]]). |
| Slot references an unknown ID on load | Slot cleared (auto-repair), logged |
| Team change requested away from base | Rejected with `TEAM_LOCKED`; no write |
| Player owns only 1 animal after onboarding | `slot1 = id`, `slot2 = nil`, `slot3 = nil` is valid |

## Migration notes

- Team presets or loadouts, if ever added, belong in a new optional field (`presets`) and must still resolve to exactly three slots when applied.
- Team size is **CONFIRMED** at three. A change would need a new owner decision and a migration that maps slot fields; do not generalise the schema to N slots in anticipation.

## Size estimate

About 150 bytes. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Team Equipping and Base Lock Rule]]
- [[Service - TeamService]]
- [[UI - Team Selection]]
- [[Schema - Animal Collection]]
- [[Animal Guards and Base Defence AI]]
- [[Data and Balancing Index]]
