---
title: Roblox API Reference Notes
type: reference
category: engineering
status: mixed
priority: P1
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - roblox-api
  - reference
  - engineering
---

# Roblox API Reference Notes

Every Roblox engine API the vault relies on, with a one-line description of how we use it and a verification status. This page prevents two failure modes: designing around an API that does not exist, and relying on a behaviour (a limit, an ordering guarantee) that the documentation does not promise.

## How to read the status column

| Status | Meaning |
|---|---|
| **Verified (signature)** | The class, member and signature were checked against the official Roblox engine API reference on 2026-11-14. Behaviour beyond the signature is not implied. |
| **Verified (behaviour)** | A specific behaviour or limit was stated on an official Roblox documentation page checked on 2026-11-14. The behaviour is quoted in the notes. |
| **Unverified** | From engineering knowledge; verify before use. Treat as *unverified* in all designs. |

> [!danger] Limits change
> Budgets and quotas below were read on 2026-11-14 and can change without notice. Re-check before [[M22 - Launch]] and after any platform announcement. Owner: Senior Luau Engineer. No external URLs are recorded here; use the Creator Hub search for the class name. Platform reading lists are in [[Roblox Platform References]].

## 1. Data and cross-server

| API | Used for | Status | Notes |
|---|---|---|---|
| `DataStoreService:GetDataStore(name)` | Player profile store, raid journal | Unverified | Standard entry point |
| `GlobalDataStore:GetAsync` | Profile load | Verified (signature) | `(key, options)`; yields |
| `GlobalDataStore:SetAsync` | Not used for profiles (no compare step) | Verified (signature) | `(key, value, userIds, options)`; yields |
| `GlobalDataStore:UpdateAsync` | Profile save with session-lock check | Verified (signature) | `(key, transformFunction)`; yields. Transform arguments, nil-to-cancel and no-yield-in-transform behaviour are **unverified** on the page read; confirm before relying on them ([[Data Consistency and Transactions]]) |
| `GlobalDataStore:RemoveAsync` | GDPR-style deletion tooling | Verified (signature) | |
| `GlobalDataStore:IncrementAsync` | Not used for profiles | Verified (signature) | |
| `DataStore:ListVersionsAsync` / `GetVersionAsync` | Recovery of corrupted profiles ([[Save, Load and Recovery]]) | Verified (signature) | |
| DataStore request budgets | Save cadence ([[Service - DataService]]) | Verified (behaviour) | Standard reads and writes: `60 + numPlayers × 40` requests per minute per server. Ordered writes: `30 + numPlayers × 5` |
| DataStore value size | Profile size budget | Verified (behaviour) | 4,194,304 characters per key; per-key throughput 4 MB of writes per minute |
| DataStore per-key write cooldown | Save coalescing | Unverified | Not stated on the limits page read; we coalesce to ≤ 1 write per 6 s anyway |
| `MemoryStoreService:GetSortedMap(name)` | Raid locks | Unverified | Entry point |
| `MemoryStoreSortedMap:UpdateAsync(key, transform, expiration)` | Acquire raid lock atomically | Verified (signature) | Memory stores guide: transform may return `nil` to abort; `DataUpdateConflict` is listed for concurrent updates |
| `MemoryStoreSortedMap:GetAsync` / `SetAsync` / `RemoveAsync` / `GetRangeAsync` | Read and release locks | Verified (signature) | |
| MemoryStore limits | Lock sizing | Verified (behaviour) | Expiration between 0 and 3,888,000 (unit presumed seconds, 45 days). Memory quota `64 KB + 1.2 KB × users` per experience. Request units `1000 + 120 × concurrent users` per minute |
| `MessagingService:PublishAsync(topic, message)` | Server-wide announcements (rare spawns, world boss) across servers if needed | Verified (signature) | Size limit and delivery guarantees not stated on the page read; treat as best-effort |
| `MessagingService:SubscribeAsync(topic, callback)` | Same | Verified (signature) | Returns a connection |

## 2. Monetisation and policy

| API | Used for | Status | Notes |
|---|---|---|---|
| `MarketplaceService.ProcessReceipt` | Developer product grants ([[Monetisation Product Concepts]]) | Verified (behaviour) | Set once by one server script. Return `PurchaseGranted` only after the grant is durably recorded; return `NotProcessedYet` on failure so the receipt is retried. A newer `BindReceiptHandler` API also exists; evaluate before launch |
| `MarketplaceService:UserOwnsGamePassAsync(userId, gamePassId)` | Game pass checks | Verified (signature) | Yields; wrap in `pcall` |
| `MarketplaceService:PromptProductPurchase(player, productId, ...)` | Purchase prompts | Verified (signature) | Outcome via `PromptProductPurchaseFinished` |
| `PolicyService:GetPolicyInfoForPlayerAsync(player)` | `ArePaidRandomItemsRestricted` check ([[Roblox Monetisation Policy Requirements]]) | Verified (signature) | Field name appears in the official sample; full field list not on the page read |

## 3. Networking and replication

| API | Used for | Status | Notes |
|---|---|---|---|
| `RemoteEvent` (`FireServer`, `FireClient`, `FireAllClients`, `OnServerEvent`, `OnClientEvent`) | Intents and server broadcasts | Unverified (standard) | |
| `RemoteFunction` (`InvokeServer`, `OnServerInvoke`) | Economy requests with responses | Unverified (standard) | `InvokeClient` is banned ([[Luau Coding Standards]]) |
| `UnreliableRemoteEvent` | Batched animal state ([[Replication Strategy]]) | Verified (behaviour) | Same methods as RemoteEvent. No delivery or ordering guarantee; include a sequence number. Payloads larger than 1,000 bytes are dropped |
| Remote argument rules | Validation ([[Implementation - Remote Validation Layer]]) | Verified (behaviour) | Functions do not replicate; metatables stripped; do not mix numeric and string keys; non-string keys become strings; non-replicated Instances arrive as `nil` |
| `BasePart:SetNetworkOwner(player?)` | `nil` = server ownership for AI animals ([[Network Ownership]]) | Verified (signature) | Behaviour on anchored parts not stated on the page read; *unverified* that it errors |
| `BasePart:GetNetworkOwner()` | Ownership audits | Verified (signature) | |
| `BasePart:SetNetworkOwnershipAuto()` | Never used for AI | Verified (signature) | |
| `BasePart:CanSetNetworkOwnership()` | Guard before setting ownership | Verified (signature) | Returns a tuple with an error reason |
| `Workspace.StreamingEnabled` | Instance streaming for large world ([[Animal Scalability and Performance Budgets]]) | Verified (signature) | Streaming behaviour details unverified |
| `Workspace:GetServerTimeNow()` | Shared server timeline for interpolation and lag compensation | Verified (signature) | |
| `Player:GetNetworkPing()` | Lag compensation rewind | Verified (signature) | Unit (assumed seconds) **unverified** |
| `buffer` library (`create`, `writeu8`, `writeu16`, `writef32`, `readu16`, `len`) | Compact state packets | Verified (signature) | Whether buffers pass through remotes is **unverified** on the page read; widely used in practice. Confirm in [[M02 - Core Project Setup]] |

## 4. Simulation, AI and spatial queries

| API | Used for | Status | Notes |
|---|---|---|---|
| `RunService.Heartbeat` | AI scheduler, replication batching | Verified (signature) | Passes `deltaTime` |
| `RunService.Stepped`, `PreSimulation`, `PostSimulation` | Not used at launch | Verified (signature) | |
| `RunService:IsStudio()` / `IsServer()` | Test hooks, config overrides | Verified (signature) | |
| `PathfindingService:CreatePath(agentParameters)` | Blocked-path fallback for AI | Verified (signature) | Agent parameters as in official samples |
| `Path:ComputeAsync`, `Path:GetWaypoints`, `Path.Blocked` | Same | Verified (usage in official samples) | Formal signatures on the `Path` page not read |
| `WorldRoot:Raycast(origin, direction, params)` | Line of sight, steering | Verified (signature) | Returns `RaycastResult?` |
| `WorldRoot:GetPartBoundsInRadius(position, radius, params)` | Area attacks fallback | Verified (signature) | |
| `RaycastParams` / `OverlapParams` | Filters | Unverified | |
| `CollectionService` (`AddTag`, `RemoveTag`, `HasTag`, `GetTagged`, `GetInstanceAddedSignal`) | Tagging spawn points, vaults, modules | Verified (signature) | |
| `Humanoid.WalkSpeed` | Player speed (16 default) | Unverified | Default 16 is engineering knowledge; matches canonical §4 |
| `Model:PivotTo` / `GetPivot` | Teleports, model placement | Unverified | |
| `ProximityPrompt` (`MaxActivationDistance`, `RequiresLineOfSight`, `HoldDuration`, `Triggered(player)`) | Hatching shrine, station, raid claims (UI only; server re-validates) | Verified (signature) | Units and defaults not stated on the page read |

## 5. Lifecycle and utilities

| API | Used for | Status | Notes |
|---|---|---|---|
| `Players.PlayerAdded` / `Players.PlayerRemoving` | Profile load and save | Unverified (standard) | |
| `Player:Kick(message)` | Anti-cheat threshold action | Verified (signature) | |
| `Player.UserId` | Keys | Verified (signature) | |
| `Player.AccountAge` | Alt-account heuristics ([[Exploit Prevention]]) | Verified (signature) | Read-only, not replicated; unit (days) **unverified** |
| `game:BindToClose(fn)` | Shutdown saves | Verified (signature) | Handler may yield (official sample). Maximum wait time **unverified**; design for a short window |
| `DataModel.JobId` | Session-lock owner id, raid lock owner | Verified (signature) | |
| `Random.new(seed)` / `NextNumber()` / `NextNumber(min, max)` / `NextInteger` / `Shuffle` / `Clone` | All gameplay randomness | Verified (signature) | Range of `NextNumber()` (assumed [0, 1)) and calling `new()` without a seed are **unverified**; the selector guards against `u ≥ 1` ([[Implementation - Weighted Random Selection]]) |
| `HttpService:GenerateGUID(wrapInCurlyBraces)` | Egg, animal, raid and idempotency ids | Verified (signature) | We pass `false` |
| `HttpService:JSONEncode` / `JSONDecode` | Journal payloads, debugging | Verified (signature) | |
| `task` library (`spawn`, `defer`, `delay`, `wait`, `cancel`, `synchronize`, `desynchronize`) | Scheduling | Verified (signature) | |
| `table.freeze`, `table.isfrozen`, `table.clone` | Frozen config | Verified (signature) | Whether `freeze` is shallow is **unverified**; we deep-freeze anyway ([[Configuration Modules]]) |
| `bit32.bxor`, `band`, `lshift`, `rshift` | FNV-1a odds token hash | Verified (signature) | |
| `coroutine.create` / `resume` / `status` / `close` | Yield detection in `Txn.run` | Unverified | `coroutine.close` availability: confirm |
| `debug.profilebegin` / `debug.profileend` | MicroProfiler labels | Unverified | |
| `os.clock`, `os.time`, `math.round`, `string.format` | Timing, buckets, formatting | Unverified (standard Luau) | |

## 6. Presentation (used by other folders)

| API | Used for | Status |
|---|---|---|
| `TweenService` | UI and egg animation tweens | Unverified |
| `ContentProvider:PreloadAsync` | Preloading hatch assets | Unverified |
| `Animator:LoadAnimation` | Animal and player animations ([[Animation Bible]]) | Unverified |
| `ParticleEmitter`, `Beam`, `Trail`, `Highlight` | VFX ([[VFX Bible]]) | Unverified |
| `SoundService`, `SoundGroup` | Mixing ([[Audio Mixing and Priority]]) | Unverified |
| `UIGridLayout`, `UIListLayout`, `UIAspectRatioConstraint`, `UIScale` | UI layout ([[UI Design System]]) | Unverified |
| `GuiService`, `UserInputService`, `ContextActionService` | Input across platforms | Unverified |
| `TextChatService` | Chat | Unverified |

## 7. Things we deliberately do not rely on

- Any client-side anti-cheat API. There is none we depend on; all enforcement is server-side ([[Security Architecture]]).
- Exact physics replication rates for server-owned parts (unverified; see [[Replication Strategy]]).
- Ordering between different remotes, or between a remote and property replication. Never assume a `RemoteEvent` arrives after a property change it depends on.

## Related documents
- [[Luau Implementation Index]]
- [[Roblox Platform References]]
- [[Luau Coding Standards]]
- [[Data Consistency and Transactions]]
- [[Replication Strategy]]
- [[Network Ownership]]
- [[Implementation - Remote Validation Layer]]
