---
title: Network Ownership
type: architecture
category: networking
status: mixed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - multiplayer
  - networking
  - network-ownership
  - security
---

# Network Ownership

Roblox lets the physics of an unanchored part be simulated by either the server or one client (its **network owner**). A client that owns a part can move it arbitrarily, and the server accepts the result. Ownership is therefore a security decision as much as a performance one. This page sets the ownership rule for every class of object in the game.

> [!info] PROPOSED
> Rules on this page are **PROPOSED**. `BasePart:SetNetworkOwner`, `GetNetworkOwner`, `SetNetworkOwnershipAuto` and `CanSetNetworkOwnership` exist (signatures verified 2026-11-14, [[Roblox API Reference Notes]]). Behaviour on anchored or welded parts is *unverified*.

## 1. Ownership table

| Object class | Network owner | Anchored? | Rationale | Status |
|---|---|---|---|---|
| Player character | That player's client (Roblox default) | No | Responsive movement; server validates ([[Exploit Prevention]]) | **PROPOSED** |
| Companion animals (Approach B) | No server parts exist; visual models are client-local | n/a | Nothing to own; nothing to exploit | **PROPOSED** ([[Replication Strategy]]) |
| Wild animals (Approach B) | As above | n/a | As above | **PROPOSED** |
| Any AI animal implemented with physical server models (Approach A, prototypes, bosses) | **Server**: `SetNetworkOwner(nil)` on the assembly root | No | Prevents the nearest client from taking automatic ownership and moving the animal | **PROPOSED** |
| Boss proxy hitbox parts | Server (anchored, moved by `CFrame`) | Yes | Anchored parts are server-simulated; no ownership call needed | **PROPOSED** |
| Base modules, walls, turrets, shield domes | Server (anchored) | Yes | Static or server-animated | **PROPOSED** |
| Projectiles (player specials, ranged animals) | Server-simulated maths; client-local VFX only | n/a | Hit outcome is server-side | **PROPOSED** |
| Physics props (crates, rolling rocks) | Server, or anchored | Prefer anchored | Avoid any client-owned prop that can be pushed into other players or bases | **PROPOSED** |
| Vehicles or mounts | Not in scope | — | — | — |
| Client-only visual models (animal visuals, VFX) | Exist only on that client | — | Not replicated; cannot affect the server | **PROPOSED** |

## 2. Why `SetNetworkOwner(nil)` for AI animals

By default, Roblox assigns ownership of unanchored parts automatically, typically to a nearby client (engineering knowledge, *unverified* in detail). For an AI-driven animal with a physical model this means:

1. **Exploit:** the owning client can teleport the animal, freeze it, pull it into a pit, drag a wild Legendary to a farming spot, or move a raid defender out of reach.
2. **Inconsistency:** the animal's movement depends on that client's frame rate and connection; other players see stutter when ownership hands over between clients.
3. **Authority conflict:** the server AI sets a target velocity while the client simulates physics; positions diverge.

Calling `SetNetworkOwner(nil)` on the root of the animal assembly makes the server simulate it, so the server AI and physics agree and no client can move it.

```lua
--!strict
-- Illustrative — not executed
-- Applies only to Approach A models (prototypes, physically simulated bosses).

local function claimServerOwnership(model: Model)
	local root = model.PrimaryPart
	assert(root, "AI model needs a PrimaryPart")
	-- Must be in Workspace and unanchored for ownership to apply (*unverified* precise rules).
	local canSet, why = root:CanSetNetworkOwnership()
	if canSet then
		root:SetNetworkOwner(nil) -- server owns the whole assembly
	else
		warn("Cannot set network owner:", why)
	end
end

-- Audit in Studio and in a debug build: any AI root owned by a player is a defect.
local function auditOwnership(models: { Model })
	for _, m in models do
		local root = m.PrimaryPart
		if root and not root.Anchored then
			local owner = root:GetNetworkOwner()
			if owner ~= nil then
				warn(("AI model %s owned by %s"):format(m.Name, owner.Name))
			end
		end
	end
end
```

| Rule | Detail |
|---|---|
| Call after parenting to `Workspace` | Ownership applies to parts in the world |
| Call on every respawn | A new assembly has a new ownership state |
| Never call `SetNetworkOwnershipAuto` on AI | Auto would hand ownership back to clients |
| Welds join assemblies | Welding a part to a client-owned assembly (for example attaching a captured animal to a player) gives the client ownership of it; never weld AI or loot to characters |

## 3. Player characters

Player characters must remain client-owned for responsive movement. This is the largest trust gap in any Roblox game: the client reports its own position. Mitigations (detailed in [[Exploit Prevention]]):

- Server-side movement validation at 4 Hz with tolerances.
- All gameplay checks use the **server's** view of the character position.
- Range checks include tolerance but cap lag compensation at 0.25 s.
- Server-initiated teleports (portals, regroup, raid entry) open a short grace window in the validator.
- Sensitive interactions (raid claims, station use, shrine) re-check position on the server, regardless of `ProximityPrompt` firing on the client.

## 4. Raid-specific ownership

| Object | Rule | Status |
|---|---|---|
| Knocked-out defender | Remains a server entity in state `KnockedOut`; no model is ever owned by the attacker | **PROPOSED** |
| Claimed eggs | Never become physical carryable parts owned by the attacker; escrow is data-only ([[Implementation - Raid Session Controller]]) | **PROPOSED** |
| Vault door, barricades, turrets | Anchored, server-animated | **PROPOSED** |
| Defender's guards | Server entities (Approach B) | **PROPOSED** |

> [!danger] Carried loot as physics objects
> A design where the attacker physically carries an egg model back to their base must not implement the egg as a part welded to the character. That makes the egg client-owned and trivially teleportable. If carrying is desired for presentation, the server tracks the carry in data and the client renders the egg as a local visual ([[Animation - Raid Interactions]]).

## 5. Test hooks

[[Test Cases - Multiplayer]] and [[Test Cases - Exploit Prevention]]: ownership audit with two clients standing beside an Approach A model; respawned model still server-owned; attempt to move a server-owned part from an exploit-simulating client in Studio (no effect expected); welded-loot static check.

## Related documents
- [[Replication Strategy]]
- [[Multiplayer Architecture]]
- [[Exploit Prevention]]
- [[Latency Handling]]
- [[Implementation - Animal AI State Machine]]
- [[Boss AI]]
- [[Roblox API Reference Notes]]
