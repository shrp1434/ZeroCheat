---
title: Egg Theft Rules
type: system
category: pvp-and-raiding
status: mixed
priority: P0
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - raids
  - eggs
  - theft
  - storage
---

# Egg Theft Rules

Which eggs can be stolen during a raid, how a theft happens and becomes final, and how the per-raid limit works.

> [!success] CONFIRMED
> - Eggs stored in the **base** can be stolen during a raid (D-024).
> - **Backpack eggs can never be stolen** (D-021). Starting capacity: backpack 10, base 50, total 60.
> - Offline bases cannot be raided (D-024).

> [!warning] UNDECIDED (Q-013)
> **The egg theft limit per raid is undecided** ([[Open Questions#Q-013]]). It is a configurable parameter, `MaxEggsStolenPerRaid`, with **no approved default**. Test builds must set it explicitly; the server refuses to start raids if it is missing. This page does not propose a number.

## Which eggs are stealable

| Egg location or state | Stealable? | Status |
|---|---|---|
| Backpack | **Never** | **CONFIRMED** |
| Base storage (Egg Vault), including purchased expansion slots | Yes, after a breach | **CONFIRMED** (base eggs stealable); breach requirement **PROPOSED** |
| Being moved between backpack and base | Not possible: transfers are locked from `Warning` to `Aftermath` | **PROPOSED** |
| Inputs of a merge in progress | Not possible: merging is locked for the defender from `Warning` | **PROPOSED** |
| Being hatched | Not possible: hatching base eggs is locked from `Warning` | **PROPOSED** |
| Eggs the attacker stole earlier from someone else | Yes, once in the attacker's base storage | **PROPOSED** |

Because transfers are locked as soon as the raid enters `Warning`, a defender cannot move eggs from the base to the backpack to protect them once a raid is announced. Moving eggs to the backpack before a raid is a legitimate defensive choice and is part of the design ([[Egg Storage]]).

## How a theft happens (PROPOSED)

| Step | Rule *(new values)* |
|---|---|
| 1. Breach | Eggs can be taken only in the `Breached` state ([[Raid Lifecycle and States]]). |
| 2. Pick up | Attacker holds a `ProximityPrompt` on the open vault for 1.5 s. The server selects an egg (see Q-205 below), reserves a free slot in the attacker's base storage, and marks the egg as **carried**. |
| 3. Carry | `RaidCarryCapacity` = 1: one egg at a time, visible on the attacker's back. Walk speed −15% while carrying. Attacks allowed; specials and dodge allowed. |
| 4. Secure | Entering the extraction point (the raid gate) **secures** the egg: the server commits the transfer to the attacker's base storage in one transaction ([[Raid Anti-Exploit Validation]]). A secured egg is final. |
| 5. Repeat | Until the limit, the end of the raid, or the vault is empty. |

### Dropped eggs

| Event while carrying | Result |
|---|---|
| Attacker defeated | Egg drops where the attacker fell. The defender (or a defender guard) touching it returns it instantly; otherwise it returns automatically after `DroppedEggReturnSeconds` = 10. |
| Attacker disconnects | Egg returns to the vault immediately. |
| Raid ends (any reason) | Egg returns to the vault immediately in `Resolving`. |
| Defender goes offline | Egg returns immediately ([[Raid Eligibility and Offline Protection#Defender leaves mid-raid]]). |

A dropped egg cannot be picked up again by the attacker *(new)*, so dropping is a real defensive win.

## Selection of the egg taken

> [!warning] UNDECIDED (Q-205)
> **Does the attacker choose which egg to take?** Options:
> 1. Attacker chooses from a display that shows each egg's rarity.
> 2. Random uniform among eligible base eggs; rarity revealed on pickup.
> 3. Random, weighted towards lower rarities.
> 4. Attacker chooses a rarity "shelf", then the egg is random within it.
>
> **Recommendation (PROPOSED, unapproved): option 2.** Random selection makes the defender's expected loss proportional to what they store, prevents sniping a single Secret egg and keeps raids from feeling personally targeted. Revealing on pickup keeps the moment exciting and lets the defender prioritise chasing a carried high-rarity egg.

## The per-raid limit (Q-013)

`MaxEggsStolenPerRaid` counts **secured plus carried** eggs. A pickup is refused when `secured + carried ≥ MaxEggsStolenPerRaid`.

The owner must choose both the **form** and the **value** of the limit. Forms the parameter can support (no values proposed):

| Form | Description | Pros | Cons |
|---|---|---|---|
| Flat count | A fixed number per raid | Clear | Same loss for a player with 5 or 200 stored eggs |
| Percentage | A share of eggs in base storage, rounded down | Proportional | Large vaults lose many eggs |
| Flat count capped by percentage | Lower of the two | Proportional at the low end, bounded at the high end | Two numbers to explain |
| Rarity-weighted budget | Each egg costs points by rarity; the raid has a point budget | Limits high-rarity losses specifically | Hard to read during a raid |
| Scaled by Egg Vault level | Higher vault level lowers the limit | Rewards base investment | Penalises new bases, who are most vulnerable |

Implementation supports all forms behind one interface so the decision changes configuration only:

```lua
-- Illustrative Luau, not tested in Roblox Studio.
-- RaidConfig.MaxEggsStolenPerRaid has NO default; it must be set per build.
local function canPickUpEgg(raid, config): (boolean, string?)
	local limit = config.MaxEggsStolenPerRaid
	assert(limit ~= nil, "RaidConfig.MaxEggsStolenPerRaid is not configured (Q-013)")
	local limitValue = (type(limit) == "function") and limit(raid.defenderVaultSnapshot) or limit
	if raid.securedEggs + raid.carriedEggs >= limitValue then
		return false, "TheftLimitReached"
	end
	return true
end
```

## Where stolen eggs go
- Into the attacker's **base storage**, never the backpack *(PROPOSED)*. Stolen eggs therefore remain exposed to raids on the attacker's own base, which keeps theft from becoming a permanent safe gain and discourages routing stolen eggs through alt accounts.
- The slot is reserved at pickup. If the attacker has no free base slot, pickup is refused with `StorageFull`.
- A stolen egg is an ordinary egg of its rarity. When the new owner hatches it, the hatch odds shown are that player's own current odds, disclosed before they commit (D-017, [[Hatch System]]).
- Every transfer is recorded with raid ID, transaction ID, source and destination for audit ([[Raid Anti-Exploit Validation]]).

## Test hooks
- Backpack eggs: zero pickups possible in any raid state, including with forged requests.
- Pickup during `Active` (before breach) is rejected with `NotBreached`.
- With the limit configured as 2 in a test build: the third pickup is refused while two are secured, or one secured and one carried.
- Attacker defeated while carrying: egg back in the vault within 10 s; attacker inventory unchanged.
- Starting a raid with the limit unset fails with a configuration error.
- Cases in [[Test Cases - Raiding]] and [[Test Cases - Inventory and Storage]].

## Related documents
- [[Egg Storage]]
- [[Module - Egg Vault]]
- [[Base Raiding System]]
- [[Raid Lifecycle and States]]
- [[Raid Anti-Exploit Validation]]
- [[Raid Rewards and Defender Compensation]]
- [[Schema - Egg Inventory]]
- [[UI - Raid Interface]]
