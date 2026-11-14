---
title: Replication Strategy
type: architecture
category: networking
status: proposed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - multiplayer
  - networking
  - replication
  - performance
---

# Replication Strategy

What the server sends to each client, by which channel, at what rate, and how animals in particular are represented on the network. Bandwidth and CPU budgets are in [[Animal Scalability and Performance Budgets]]; ownership rules in [[Network Ownership]].

> [!info] PROPOSED
> Everything on this page is **PROPOSED**. Platform facts used (UnreliableRemoteEvent drops payloads over 1,000 bytes and does not guarantee delivery or order) were checked on 2026-11-14 ([[Roblox API Reference Notes]]). Code is **illustrative — not executed**.

## 1. Channels

| Channel | Mechanism | Reliable? | Used for |
|---|---|---|---|
| Instance replication | Parts and models under `Workspace`, `ReplicatedStorage` | Yes | World geometry, base models, player characters, bosses' proxy parts |
| Attributes | `Instance:SetAttribute` on server instances | Yes | Low-frequency public state: player level, PvP flag, base module levels |
| `RemoteEvent` (server → client) | Explicit messages | Yes, ordered per remote (*unverified* ordering guarantee) | Spawn, despawn, KO, combat events, profile deltas, odds changes, raid notifications |
| `UnreliableRemoteEvent` (server → client) | Explicit messages | No; may drop or reorder | High-rate animal state snapshots |
| `RemoteFunction` (client → server) | Request and response | Yes | Economy requests |
| `RemoteEvent` (client → server) | Intents | Yes | Combat, ability, commands |

**Rule:** anything that must not be missed (an animal spawning or dying, a hit, a balance change) is reliable. Anything superseded by the next message (an animal's position) is unreliable.

## 2. Animals: two approaches evaluated

Animals are the dominant replication cost: up to 48 companions (16 players × 3), up to 180 simulated wild animals, plus guards and bosses (canonical §15).

### Approach A — server-owned physical models

Each animal is a full `Model` in `Workspace` on the server (Humanoid or AnimationController, physics-driven), with `SetNetworkOwner(nil)` on its root part. Roblox replicates physics and animations to every client.

### Approach B — server-simulated state with client-side visual models

The server holds each animal as a lightweight entity record (position, facing, velocity, state, HP, target). There is **no** animal model on the server. The server sends compact snapshots at reduced, distance-based rates through an `UnreliableRemoteEvent`; each client creates its own visual model from a pooled template, interpolates between snapshots and plays animations by state. Reliable events handle spawn, despawn and KO.

### Comparison

| Criterion | A: physical server models | B: state + client visuals |
|---|---|---|
| Server CPU | Physics and Humanoid cost for every animal; grows with part count | Integer-cheap: vector maths per tick, ground height via raycast at low rate |
| Bandwidth control | Engine decides rates; *unverified* per-part cost; no per-client distance tiers | Full control: rates per distance tier, delta suppression, quantisation |
| Mobile rendering | Every streamed animal is rendered | Client chooses how many to render, with impostors or hiding beyond a cap |
| Hit validation | Can use real parts | Uses server-side shapes (cylinder radius per species); deterministic and cheap |
| Collision with world | Native | Custom: ground snapping by raycast, simple obstacle avoidance |
| Visual smoothness | Engine interpolation, can jitter under load | Interpolation buffer of 100 ms gives smooth motion at 10 Hz |
| Animation sync | Server-played animations replicate (*unverified* details) | Client plays animations from state and event; exact frame sync not needed |
| Exploit surface | Ownership mistakes give a client physics control | No client-owned animal parts exist at all |
| Implementation cost | Low initially | Higher: encoder, decoder, pool, interpolator |
| Fit for 228+ entities on mobile | Poor | Good |

> [!info] PROPOSED recommendation
> **Approach B for companions, wild animals and guards.** Companions are server-simulated with a reduced-rate replicated state and client-side visual models. **Bosses are evaluated per boss**: with at most a handful in a server, a boss may use Approach A (server-owned, `SetNetworkOwner(nil)`) when its attacks need large articulated hitboxes; otherwise it also uses B with server-side proxy shapes. Prototype both in [[M05 - Animal AI]] and measure with the budgets in [[Animal Scalability and Performance Budgets]] before locking the choice.

## 3. Approach B in detail

### 3.1 Snapshot format

Per entity record, 18 bytes, packed with the `buffer` library:

| Field | Type | Bytes | Notes |
|---|---|---:|---|
| Entity id | u16 | 2 | Server-assigned per session; wraps safely with generation checks on spawn |
| Position X, Y, Z | f32 × 3 | 12 | Full precision; quantisation to i16 relative to a region origin is a later optimisation |
| Yaw | u8 | 1 | 256 steps (1.4°) |
| State | u8 | 1 | Enum: Idle, Move, Attack, Ability, Stunned, KO, … |
| HP fraction | u8 | 1 | 0–255; exact HP arrives in reliable `CombatEvent` |
| Flags | u8 | 1 | In combat, invulnerable, commanded, LOD tier |

Packet header: u32 sequence + f32 server time = 8 bytes. With a safety margin below the 1,000-byte limit, one packet carries **up to 52 entities** (8 + 52 × 18 = 944 bytes). Larger sets are split across several packets in the same tick.

### 3.2 Rates per client (relevance tiers)

| Distance from the receiving client's character | Send rate | Status |
|---|---:|---|
| ≤ 120 studs, or own companions, or the client's current target | 10 Hz | **PROPOSED** |
| 120–300 studs | 4 Hz | **PROPOSED** |
| > 300 studs | Not sent; client despawns its visual model | **PROPOSED** |
| Unchanged since last send (idle, no movement > 0.1 stud, same state) | Skipped; keep-alive every 2 s | **PROPOSED** |

These are network rates per receiving client, independent of the AI tick tiers in [[Implementation - Animal AI State Machine#LOD scheduler]] (an entity cannot be sent faster than it is simulated).

### 3.3 Server encoder

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Services/AnimalAIService/Replication (excerpt)

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Workspace = game:GetService("Workspace")

local StateChannel = ReplicatedStorage.Remotes.AnimalState :: UnreliableRemoteEvent

local RECORD = 18
local HEADER = 8
local MAX_PER_PACKET = 52

local seqByPlayer: { [Player]: number } = {}

local function writeRecord(b: buffer, offset: number, e: any)
	buffer.writeu16(b, offset, e.netId)
	buffer.writef32(b, offset + 2, e.position.X)
	buffer.writef32(b, offset + 6, e.position.Y)
	buffer.writef32(b, offset + 10, e.position.Z)
	buffer.writeu8(b, offset + 14, math.floor((e.yaw % (2 * math.pi)) / (2 * math.pi) * 256) % 256)
	buffer.writeu8(b, offset + 15, e.stateCode)
	buffer.writeu8(b, offset + 16, math.clamp(math.floor(e.hp / e.maxHp * 255 + 0.5), 0, 255))
	buffer.writeu8(b, offset + 17, e.flags)
end

-- Called at most 10 times per second per player with the entities due for that player.
local function sendBatch(player: Player, due: { any })
	local i = 1
	while i <= #due do
		local n = math.min(MAX_PER_PACKET, #due - i + 1)
		local b = buffer.create(HEADER + n * RECORD)
		local seq = (seqByPlayer[player] or 0) + 1
		seqByPlayer[player] = seq
		buffer.writeu32(b, 0, seq)
		buffer.writef32(b, 4, Workspace:GetServerTimeNow())
		for k = 0, n - 1 do
			writeRecord(b, HEADER + k * RECORD, due[i + k])
		end
		StateChannel:FireClient(player, b)
		i += n
	end
end
```

> [!warning] Unverified
> Passing a `buffer` through a remote is widely used but was not confirmed on the API page read ([[Roblox API Reference Notes]]). `writef32` for server time loses sub-millisecond precision after long uptimes; if this matters, send time as an f64 or as a tick count. Verify both in [[M02 - Core Project Setup]].

### 3.4 Client interpolation

```lua
--!strict
-- Illustrative — not executed
-- Client/Controllers/AnimalRenderController (excerpt)

local Workspace = game:GetService("Workspace")

local INTERP_DELAY = 0.1 -- seconds behind the newest snapshot (PROPOSED)

type Snap = { t: number, pos: Vector3, yaw: number, state: number }
type Track = { snaps: { Snap }, model: Model?, lastSeq: number }

local tracks: { [number]: Track } = {}
local lastPacketSeq = 0

local function onState(b: buffer)
	local seq = buffer.readu32(b, 0)
	if seq <= lastPacketSeq then
		return -- out of order or duplicate (unreliable channel)
	end
	lastPacketSeq = seq
	local t = buffer.readf32(b, 4)
	local count = (buffer.len(b) - 8) // 18
	for k = 0, count - 1 do
		local o = 8 + k * 18
		local id = buffer.readu16(b, o)
		local track = tracks[id]
		if track then -- tracks are created by the reliable Spawn event, never by snapshots
			local snap = {
				t = t,
				pos = Vector3.new(buffer.readf32(b, o + 2), buffer.readf32(b, o + 6), buffer.readf32(b, o + 10)),
				yaw = buffer.readu8(b, o + 14) / 256 * 2 * math.pi,
				state = buffer.readu8(b, o + 15),
			}
			table.insert(track.snaps, snap)
			if #track.snaps > 8 then
				table.remove(track.snaps, 1)
			end
		end
	end
end

-- Per render frame: sample each visible track at (server now − delay).
local function sample(track: Track): (Vector3?, number?)
	local renderT = Workspace:GetServerTimeNow() - INTERP_DELAY
	local s = track.snaps
	for i = #s, 2, -1 do
		local a, b = s[i - 1], s[i]
		if a.t <= renderT and renderT <= b.t then
			local alpha = (renderT - a.t) / math.max(b.t - a.t, 1e-3)
			return a.pos:Lerp(b.pos, alpha), a.yaw + (b.yaw - a.yaw) * alpha
		end
	end
	local last = s[#s]
	return if last then last.pos else nil, if last then last.yaw else nil -- hold; no extrapolation beyond 0.2 s
end
```

## 4. Other replicated state

| Data | Channel | Recipients | Rate |
|---|---|---|---|
| Own profile (cash, eggs, animals, index) | `ProfileDelta` RemoteEvent with changed sections | Owner only | On change |
| Public player info (level, PvP flag, equipped species ids) | Attributes on the `Player` | All | On change |
| Base module levels | Attributes on the plot model; models swapped by server | All | On change |
| Base storage contents | `ProfileDelta` | Owner only (never others, including raiders, beyond the claim UI list) | On change |
| Raid claimable eggs list | `RaidEvent` | Attacker in an active raid: counts and rarities only | On raid start and per claim |
| Combat events | `CombatEvent` RemoteEvent, batched per 0.1 s | Clients within 150 studs | 10 Hz max |
| Boss telegraphs | `BossTelegraph` RemoteEvent | Clients in encounter | On attack |

> [!danger] Never replicate other players' private data
> Egg storage, odds quotes and animal inventories of other players are never sent to a client. A raider sees what they can claim through the raid UI only ([[UI - Raid Interface]]).

## 5. Combat synchronisation summary

Client predicts its own swing; server resolves; reliable `CombatEvent` drives damage numbers and hit reactions on all clients; animal attack animations play from snapshot state changes and are aligned to `CombatEvent` arrival for the impact frame ([[Latency Handling]]).

## Related documents
- [[Multiplayer Architecture]]
- [[Network Ownership]]
- [[Latency Handling]]
- [[Animal Scalability and Performance Budgets]]
- [[Implementation - Animal AI State Machine]]
- [[Remote Communication Contract]]
- [[Client Controllers]]
- [[Roblox API Reference Notes]]
