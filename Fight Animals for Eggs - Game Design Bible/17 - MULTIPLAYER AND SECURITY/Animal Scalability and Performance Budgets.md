---
title: Animal Scalability and Performance Budgets
type: architecture
category: performance
status: mixed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - performance
  - multiplayer
  - ai
  - mobile
  - networking
---

# Animal Scalability and Performance Budgets

Animals are the game: every player brings three, the world is full of wild ones, and bosses and raid guards add more. This page sizes the worst case, sets server, network and client budgets, and defines the levers (LOD, batching, culling) that keep the game at the canonical frame-rate targets. General performance rules are in [[Performance Guidelines]].

> [!info] PROPOSED
> Targets from [[Canonical Proposed Values]] §15 (**PROPOSED**): 16 players per server ([[Open Questions#Q-031]]), ≤ 180 simulated wild animals, ≤ 60 with full AI near players, 3 companions per player, 60 FPS on mid-range PC and 30 FPS minimum on mid-range mobile. All other budgets on this page are **PROPOSED** local values. Cost-per-operation figures are **assumptions** to be replaced by MicroProfiler measurements in [[M20 - Optimisation]].

## 1. Entity census (worst case per server)

| Population | Count | Basis | Status |
|---|---:|---|---|
| Wild animals, simulated | 180 | Canonical §15 | **PROPOSED** |
| of which full AI (tier A) | ≤ 60 | Canonical §15 | **PROPOSED** |
| Companions | 48 | 16 players × 3 (team size **CONFIRMED**) | Players **UNDECIDED** (Q-031) |
| Raid guards | 12 | Assumption: up to 2 concurrent raids × 6 defenders; which animals defend is **UNDECIDED** ([[Open Questions#Q-033]]) | Assumption |
| Mini-bosses | 8 | One per region (canonical §5) | **PROPOSED** |
| World boss | 1 | One active at a time per server | **PROPOSED** |
| **Total simulated** | **≈ 249** | | |
| Pen display animals | 0 server-simulated | If adopted ([[Open Questions#Q-008]]), client-only decorative models, capped per base | **UNDECIDED** |

> [!warning] UNDECIDED (Q-008) — pens
> Displaying every owned animal is not feasible: at the working assumption of 100 owned animals ([[Open Questions#Q-022]]) × 16 players that is 1,600 models. If pens display animals, the recommendation is a client-only display of at most 6 per base, chosen by the owner, never simulated or replicated as entities, and culled beyond 150 studs.

## 2. AI LOD tiers

Defined in [[Implementation - Animal AI State Machine#LOD scheduler]] and summarised here with the load they generate.

| Tier | Condition | Tick rate | Max entities (worst case) | Ticks per second |
|---|---|---:|---:|---:|
| A | ≤ 80 studs from a player or in combat | 10 Hz | 60 wild + 48 companions in combat + 12 guards + 9 bosses = 129 | 1,290 |
| B | 80–200 studs | 4 Hz | 120 wild | 480 |
| C | 200–400 studs | 1 Hz | (shared with B in the worst case) | — |
| D | > 400 studs | 0 | Any remainder | 0 |
| Companion idle | Out of combat | 5 Hz | (included above when idle: 48 × 5 = 240) | — |
| **Worst case total** | | | | **≈ 1,770 ticks/s ≈ 30 per frame at 60 Hz** |

## 3. Server CPU budget

| Item | Budget per Heartbeat (≈ 16.7 ms at 60 Hz) | Assumption behind the estimate | Status |
|---|---:|---|---|
| AI ticks | ≤ 3.0 ms (hard cap in the scheduler) | 30 ticks × ≤ 0.05 ms = 1.5 ms expected | **PROPOSED** |
| Movement integration and ground snapping | Included in AI | Ground raycast at ≤ 4 Hz per moving entity | **PROPOSED** |
| Pathfinding | Off-frame; ≤ 10 `ComputeAsync` per second | Queued, asynchronous | **PROPOSED** |
| Combat resolution | ≤ 1.0 ms | ≤ 100 hits per second server-wide | **PROPOSED** |
| Replication encoding | ≤ 1.5 ms | 16 clients × 10 Hz, ≤ 80 records each | **PROPOSED** |
| Position history recording | ≤ 0.3 ms | 249 entities at 20 Hz | **PROPOSED** |
| Everything else (economy, raids, data) | ≤ 2.0 ms | Event-driven, mostly idle | **PROPOSED** |
| **Total game script time** | **≤ 8 ms** | Leaves the rest for engine physics and networking | **PROPOSED** |

The scheduler enforces the AI cap by carrying work to the next frame. If the AI cap is hit for more than 10% of frames over a minute, the server demotes tier A to 8 Hz and tier B to 2 Hz and logs an alert (**PROPOSED** automatic degradation).

## 4. Batching

| What | How | Effect |
|---|---|---|
| AI updates | One Heartbeat scheduler, round-robin with staggered start times ([[Implementation - Animal AI State Machine]]) | No frame spikes when many animals spawn together |
| Re-tiering | Once per second for all entities | Distance checks amortised |
| Proximity queries | Spatial hash grid of 50-stud cells, rebuilt at 4 Hz | `findHostile` checks ~9 cells instead of 249 entities |
| Snapshots | One packet (≤ 52 records) per client per tick, per tier ([[Replication Strategy]]) | Few remote calls; under the 1,000-byte unreliable limit |
| Combat events | Aggregated per 0.1 s per client | ≤ 10 reliable messages per second per client |
| Saves | Coalesced per player | DataStore budget ([[Data Consistency and Transactions]]) |

## 5. Network bandwidth per animal

**Assumptions** (state all; replace with measurements):

1. Approach B snapshots, 18 bytes per animal record, 8-byte packet header ([[Replication Strategy]]).
2. Protocol overhead per remote call is not included (unknown, *unverified*); a 20% allowance is added in the totals.
3. Delta suppression skips idle, unchanged animals. The scenario totals below **ignore** this saving, so they are conservative; if 40% of wild animals are idle at a time, real wild-animal traffic is roughly 40% lower.
4. Rates: 10 Hz within 120 studs, 4 Hz within 120–300 studs, none beyond.

| Per animal, per receiving client | Bytes per second |
|---|---:|
| Near (10 Hz) | 18 × 10 = **180 B/s** |
| Mid (4 Hz) | 18 × 4 = **72 B/s** |
| Idle with 2 s keep-alive | 9 B/s |

| Scenario (one receiving client) | Near | Mid | Payload | + 20% overhead |
|---|---:|---:|---:|---:|
| Solo farming in a region | 3 own + 15 wild | 25 wild | 3.2 + 1.8 = 5.0 KB/s | **6.0 KB/s** |
| Busy region, 4 players together | 12 companions + 25 wild | 30 wild | 6.7 + 2.2 = 8.9 KB/s | **10.6 KB/s** |
| World boss with 16 players | 48 companions + 1 boss + 15 wild | 20 wild | 11.5 + 1.4 = 12.9 KB/s | **15.5 KB/s** |
| Raid at a base | 3 + 3 companions + 6 guards | 10 wild | 2.2 + 0.7 = 2.9 KB/s | **3.5 KB/s** |

Combat events add roughly 30 bytes per hit; 50 visible hits per second at a world boss adds ≈ 1.5 KB/s. The worst case stays under **20 KB/s** per client of game-originated traffic, which is the **PROPOSED** budget. Server egress at 16 clients in the world-boss case: ≈ 16 × 17 KB/s ≈ 270 KB/s.

For comparison, Approach A (physical server models) gives the engine control over rates and cost scales with part count; it was not estimated because per-part replication cost is *unverified*. Measure it in the [[M05 - Animal AI]] prototype before final selection.

## 6. Client culling and rendering

| Lever | PC | Mobile | Status |
|---|---:|---:|---|
| Max fully animated animal models | 60 | 30 | **PROPOSED** |
| Beyond the cap | Nearest first; the rest hidden or shown as static low-detail meshes | Same | **PROPOSED** |
| Visual model despawn distance | 300 studs | 200 studs | **PROPOSED** |
| Animation update | Full within 60 studs; stop secondary animations (tail, idle fidgets) beyond | Beyond 40 studs | **PROPOSED** |
| Ambient particle emitters per animal | ≤ 2, disabled beyond 80 studs | ≤ 1, disabled beyond 50 studs | **PROPOSED** |
| Rarity and ascension auras | Full within 60 studs | Within 40 studs; simplified beyond | **PROPOSED** ([[VFX - Rarity and Variant Effects]]) |
| Model pooling | Reuse visual models per species; never destroy on despawn within a session | Same | **PROPOSED** |
| Interpolated tracks | ≤ 120 | ≤ 80 | **PROPOSED** |
| Client script time for animal rendering | ≤ 3 ms per frame | ≤ 5 ms per frame | **PROPOSED** |

Model, rig and texture budgets per animal are owned by [[Animal Modelling Principles]] and [[Animal Rig Standards]]. The engineering request to art is: one skinned mesh or a small number of mesh parts per animal, no unions, and a low-detail variant for culling.

## 7. Instance budgets

| Item | Budget | Status |
|---|---|---|
| Server-side instances per animal (Approach B) | 0 (entity is data only); bosses ≤ 10 anchored proxy parts | **PROPOSED** |
| Client instances per animal visual | ≤ 40 including bones, attachments and effects | **PROPOSED** |
| Base model per player | ≤ 1,500 parts at max upgrades ([[Base Art Direction]] owns detail) | **PROPOSED** |
| Total streamed parts near a mobile client | ≤ 25,000 | **PROPOSED** |

## 8. Mobile budget summary

| Budget | Target at 30 FPS (33.3 ms frame) | Status |
|---|---|---|
| Total client script time | ≤ 8 ms | **PROPOSED** |
| Animated animals on screen | ≤ 30 | **PROPOSED** |
| Active particle emitters | ≤ 40 | **PROPOSED** |
| Network in | ≤ 20 KB/s game traffic | **PROPOSED** |
| Memory | Track the platform memory warnings in Studio's device emulation; budget set in [[M20 - Optimisation]] | **UNDECIDED** pending measurement |

## 9. Stress tests

Defined in [[Test Cases - Mobile Performance]] and [[Test Cases - Multiplayer]]:

1. 249 simulated entities, 16 bot clients, world boss active: server script time ≤ 8 ms at the 95th percentile.
2. Mobile reference device in the world-boss scenario: ≥ 30 FPS at the 5th percentile over 2 minutes.
3. Packet loss 5% on the unreliable channel: no visible teleporting beyond 0.2 s holds.
4. Spawn 100 wild animals in one frame: no frame over 25 ms on the server.

## Related documents
- [[Performance Guidelines]]
- [[Implementation - Animal AI State Machine]]
- [[Replication Strategy]]
- [[Network Ownership]]
- [[Wild Animal Spawning and Respawn]]
- [[Module - Animal Pens]]
- [[Animal Modelling Principles]]
- [[Test Cases - Mobile Performance]]
- [[M20 - Optimisation]]
