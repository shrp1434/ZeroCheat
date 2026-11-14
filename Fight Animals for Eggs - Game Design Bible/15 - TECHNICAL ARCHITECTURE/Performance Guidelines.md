---
title: Performance Guidelines
type: spec
category: technical-architecture
status: proposed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - performance
  - optimisation
  - mobile
  - ai
---

# Performance Guidelines

> [!info] PROPOSED
> All budgets on this page are **PROPOSED** targets for prototyping and [[M20 - Optimisation]]. Values that already exist in [[Canonical Proposed Values#15. Server and performance targets (PROPOSED)]] are reused: 16 players per server (Q-031), ≤ 180 simulated wild animals, ≤ 60 with full AI near players, 3 companions per player, 60 FPS on mid-range PC and a 30 FPS floor on mid-range mobile. Every other number here is a **new PROPOSED value**. Per-entity budgets in more depth: [[Animal Scalability and Performance Budgets]].

## Worst-case server population

| Entity | Count | Source |
|---|---:|---|
| Players | 16 | Q-031 working assumption |
| Companions | 48 | 16 × 3 (D-006) |
| Wild animals simulated | ≤ 180 | Canonical |
| Wild animals with full AI | ≤ 60 | Canonical |
| Bosses alive | ≤ 1 world boss + ≤ 8 mini-bosses (one per region) | [[Boss Design Overview]] |
| Raid guards | ≤ 2 concurrent raids × guard count (Q-033) | **PROPOSED** concurrency cap |
| Bases | 16 plots | [[Roblox Project Hierarchy]] |

**AI-driven entities, worst case:** 48 companions + 180 wild + 9 bosses + guards ≈ **240**. The tick scheduler below is sized for that.

## Server frame budget

The server simulates at 60 Hz (16.7 ms per frame). Budgets are **average** per frame measured over 60 s, with a p99 ceiling. Measured with MicroProfiler labels (`debug.profilebegin` / `debug.profileend`) around each service's Heartbeat work.

| Work | Average budget | p99 ceiling | Owner |
|---|---:|---:|---|
| Animal AI (all tiers, including companions) | 4.0 ms | 8.0 ms | [[Service - AnimalAIService]] |
| Combat (hit resolution, cooldowns, combat tags) | 1.5 ms | 4.0 ms | [[Service - CombatService]] |
| Spawning and respawn timers | 0.3 ms | 2.0 ms | [[Service - SpawnService]] |
| Bosses | 0.8 ms | 3.0 ms | [[Service - BossService]] |
| Raids | 0.4 ms | 2.0 ms | [[Service - RaidService]] |
| Zone checks (region, at-base) | 0.3 ms | 1.0 ms | [[Service - BaseService]] |
| Data delta flush and replication of profile views | 0.3 ms | 1.5 ms | [[Service - DataService]] |
| Everything else (remote handlers, logging) | 0.4 ms | 2.0 ms | All |
| **Total scripted work** | **8.0 ms** | **14.0 ms** | |

The remaining ~8 ms per frame is headroom for Roblox physics, replication and garbage collection. If total scripted work exceeds 10 ms average in a full server, the AI scheduler lowers tick rates first (see LOD), never combat validation.

### Rules

- No service connects more than **one** `RunService.Heartbeat` handler. Work is time-sliced inside that handler.
- Hot paths allocate nothing per frame: reuse tables, avoid closures in loops, cache `Vector3` constants.
- `PathfindingService:CreatePath(...):ComputeAsync` is limited to **8 computations per second per server** through a queue; direct `MoveTo` / steering is used when there is line of sight.
- Spatial queries (`workspace:GetPartBoundsInRadius`, `Raycast`) use `OverlapParams` / `RaycastParams` with collision groups or filter lists so they scan only relevant parts.
- No `while true do wait() end` loops. Use `task.wait`, `task.delay` or the scheduler.
- DataStore calls never happen in Heartbeat; they run in their own threads ([[Service - DataService]]).

## AI tick rates and level of detail

The AI scheduler assigns each AI entity a tier every 0.5 s based on the distance to the **nearest player character** and whether it is in combat.

| Tier | Condition | Tick rate | Behaviour | Status |
|---|---|---:|---|---|
| **Active** | In combat, or within 80 studs of a player; companions always | 10 Hz | Full state machine, ability use, target selection, pathfinding allowed | **PROPOSED** |
| **Near** | 80 to 200 studs | 4 Hz | Wander and idle; perception checks; no pathfinding (steering only) | **PROPOSED** |
| **Far** | 200 to 400 studs | 1 Hz | Idle only; returns to spawn if displaced; animations paused on server side (clients do not have it streamed) | **PROPOSED** |
| **Dormant** | > 400 studs, or no player in the region | 0 Hz | Not simulated; entity may be despawned and represented by a spawn-point record | **PROPOSED** |

Additional rules:
- At most **60** wild animals may be in Active tier at once (canonical). If more qualify, the furthest from players are clamped to Near; companions, bosses and raid guards are exempt and always Active.
- Ticks are **staggered**: each entity gets a phase offset so 10 Hz entities are spread across six frames rather than all running on the same frame.
- Per-tick work per entity target: ≤ 0.05 ms in Active tier. At 60 Active wild + 48 companions + 9 bosses at 10 Hz that is about 117 × 10 × 0.05 = 58.5 ms per second ≈ **1.0 ms per frame**, leaving the rest of the 4 ms AI budget for Near/Far tiers, pathfinding and ability resolution.
- The state machine is specified in [[Implementation - Animal AI State Machine]] and behaviour in [[Wild Animal AI]] and [[Animal Combat Behaviour]].

> [!warning] UNDECIDED (Q-809): movement technique
> Whether AI-driven animals move as **unanchored, server-owned physics assemblies** (driven by `AlignPosition` / `AlignOrientation` constraints, with `BasePart:SetNetworkOwner(nil)`) or as **anchored models moved by the server** (for example with `workspace:BulkMoveTo`) has a large effect on server cost and client smoothness. Neither is chosen. M05 must prototype both with 180 animals and measure server frame time and client visual quality. How anchored CFrame updates are interpolated on clients is *unverified*. See [[Network Ownership]].

## StreamingEnabled

**PROPOSED:** `Workspace.StreamingEnabled = true`.

| Setting | Proposal | Reason |
|---|---|---|
| `StreamingMinRadius` | 128 studs | Covers melee and ranged combat plus command range (80 studs) |
| `StreamingTargetRadius` | 384 studs | Enough for region landmarks; low memory on mobile |
| `StreamOutBehavior` | Opportunistic | Lets low-memory devices drop distant content |
| Region models | `ModelStreamingMode = Default` | Stream in parts as needed |
| Animal and boss models | `ModelStreamingMode = Atomic` | An animal never appears with missing limbs |
| Player's own base plot | `PersistentPerPlayer` for the owner (*unverified* behaviour details; confirm in Studio) | Base UI and prompts always available to the owner |
| Teleports (base portals, region travel) | `Player:RequestStreamAroundAsync(position)` before moving the character | Avoids falling through unstreamed ground |

Client code must always assume an instance may not be streamed in: use `WaitForChild` with a timeout or `CollectionService` instance-added signals, never direct indexing into `Workspace/Runtime` or `Workspace/World`.

## Instance and asset budgets

| Item | Budget | Notes |
|---|---:|---|
| Animal model (companion or wild) | ≤ 15 BaseParts, ≤ 4,000 triangles (Common to Epic), ≤ 7,000 (Legendary to Secret) | Low-poly direction ([[Animal Modelling Principles]]) |
| Animal bones | ≤ 40 per rig | [[Animal Rig Standards]] |
| Active `ParticleEmitter` per animal | ≤ 3 at quality tier 3, ≤ 1 at tier 1 | A5 aura counts as one ([[VFX - Rarity and Variant Effects]]) |
| Boss model | ≤ 40 BaseParts, ≤ 20,000 triangles | [[Boss Art Direction]] |
| Base, fully upgraded | ≤ 1,200 BaseParts per plot | 16 plots × 1,200 = 19,200 parts |
| Displayed animals in pens | Depends on Q-008; if displayed, ≤ 6 visible per base using simplified idle-only models | [[Module - Animal Pens]] |
| Region geometry | ≤ 25,000 BaseParts per region; prefer MeshParts and Terrain | [[Environment Art Direction]] |
| Total `Workspace` BaseParts (server) | ≤ 220,000 | Including all regions, bases and runtime |
| Client-streamed BaseParts (typical) | ≤ 40,000 on mobile | Measured in the Developer Console |
| Texture memory (client) | ≤ 250 MB on mobile | [[Material and Texture Direction]] |
| Sounds playing simultaneously | ≤ 24 | [[Audio Mixing and Priority]] |

## Client budgets

| Metric | Mid-range PC | Mid-range mobile | Status |
|---|---|---|---|
| Frame rate | 60 FPS | 30 FPS minimum | Canonical |
| Scripted client work per frame | ≤ 3 ms | ≤ 5 ms | **PROPOSED** |
| Total client memory (peak, full 16-player server) | ≤ 2,000 MB | **≤ 1,000 MB** target, 1,200 MB hard ceiling | **PROPOSED** |
| Lua heap (client) | ≤ 150 MB | ≤ 100 MB | **PROPOSED** |
| Time to interactive after join | ≤ 15 s | ≤ 25 s | **PROPOSED** |
| Inbound network | ≤ 60 KB/s average | ≤ 40 KB/s average | **PROPOSED** |

`PerformanceController` (see [[Client Controllers]]) sets a quality tier:

| Tier | Trigger | Effect |
|---|---|---|
| 3 (High) | Default on PC | Full VFX, all aura particles, shadows per Lighting |
| 2 (Medium) | Mobile default, or PC below 50 FPS for 10 s | Halved particle rates, simplified damage numbers, fewer ambient effects |
| 1 (Low) | Below 28 FPS for 10 s, or memory above 900 MB | Single particle per animal, no trails on companions, reduced ambient audio, nameplates only on targeted entities |

The tier never changes gameplay information: telegraphs, health bars, rarity colour and odds display are always shown ([[UI Accessibility Standards]]).

## Network guidelines

- Profile deltas are coalesced and flushed once per Heartbeat per player ([[Service - DataService]]).
- `Combat/HitConfirm` batches up to 8 hits per message and stays under the 1,000-byte UnreliableRemoteEvent payload limit documented by Roblox.
- Health uses replicated attributes rather than remotes; only change the attribute when the integer HP changes.
- World announcements go to all clients; combat confirms only to players within 150 studs (**PROPOSED**) of the event.

## Measurement plan

| When | What | Tooling |
|---|---|---|
| Every milestone from [[M05 - Animal AI]] | 16-bot load test with 180 wild animals; record server frame time per service label | MicroProfiler, server Developer Console |
| [[M19 - Multiplayer Testing]] | 16 real clients including 4 mobile devices; record FPS, memory and network | Developer Console, `Telemetry/ClientMetrics` |
| [[M20 - Optimisation]] | Fix every budget breach above or record an exception | [[Test Cases - Mobile Performance]] |
| Live | `perf_sample` analytics by platform class | [[Logging and Error Handling#Analytics events]] |

## Related documents
- [[Technical Architecture Index]]
- [[Animal Scalability and Performance Budgets]]
- [[Service - AnimalAIService]]
- [[Replication Strategy]]
- [[Network Ownership]]
- [[Client Controllers]]
- [[Test Cases - Mobile Performance]]
- [[M20 - Optimisation]]
