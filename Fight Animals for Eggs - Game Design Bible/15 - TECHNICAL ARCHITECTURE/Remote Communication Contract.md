---
title: Remote Communication Contract
type: spec
category: technical-architecture
status: proposed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - networking
  - remotes
  - security
  - contract
---

# Remote Communication Contract

> [!info] PROPOSED
> This is the **complete PROPOSED list** of every RemoteEvent, RemoteFunction and UnreliableRemoteEvent in the game. A remote that is not in this table must not exist. `ReplicatedStorage/Shared/RemoteManifest` is generated from (or checked against) this table, and `Systems/Net` creates exactly these instances at boot ([[Roblox Project Hierarchy]]). All rate limits are new **PROPOSED** values.

The validation and rate-limiting machinery is implemented in [[Implementation - Remote Validation Layer]] and [[Implementation - Rate Limiting]]. Who decides each outcome is in [[Server-Client Responsibilities]].

## 1. Patterns

### 1.1 Which remote type to use

| Need | Remote type | Why |
|---|---|---|
| Client asks for a transactional outcome and needs the answer | **RemoteFunction, client to server** (`InvokeServer`) with strict validation | Simple request/response; the server is the callee, so only the client can be left waiting |
| An outcome with odds that must be disclosed first | **Two RemoteFunctions**: a quote, then a confirm carrying the **server-issued** `quoteId` and `oddsVersion` | Enforces D-017 and D-041; the quote is single-use and expires |
| Client sends a stream of intents (attacks, commands) | **RemoteEvent, client to server** | Fire-and-forget; server answers with state changes or `Combat/ActionRejected` |
| Server pushes authoritative state | **RemoteEvent, server to client** | Reliable and ordered |
| High-frequency cosmetic data (hit numbers, telegraphs, client metrics) | **UnreliableRemoteEvent** | Lower overhead; loss is acceptable |
| Server needs something from the client | **Never a RemoteFunction.** Server fires a RemoteEvent; the client answers with its own request | See §1.2 |

### 1.2 Never invoke the client

> [!danger] Server-to-client RemoteFunction invocation is forbidden
> Roblox documents three failure modes of `RemoteFunction:InvokeClient`: if the client errors, the error is thrown on the server; if the client disconnects mid-call, `InvokeClient` throws; and **if the client never returns, the server thread yields forever**. An exploiter can therefore pin server threads (and whatever locks or open transactions they hold) at will. No code in this project calls `InvokeClient`, and `Net` refuses to create a RemoteFunction with a server-to-client direction.

When the server needs a client decision (for example "do you accept this raid alert?"), it fires a RemoteEvent with a server-issued `requestId`, stores the pending request with an expiry, and the client answers through a client-to-server remote that includes that `requestId`. A missing answer simply expires.

### 1.3 Envelope rules

- Every remote takes **exactly one table argument** (the payload). Schemas reject unknown keys, holes in arrays, mixed key types, `NaN` and infinite numbers.
- Roblox converts non-string table keys to strings and drops functions, metatables and non-replicated instances across the boundary; payloads therefore contain only strings, numbers, booleans, `Vector3` and plain arrays or string-keyed tables.
- An empty team slot is the empty string `""`, never `nil` (a `nil` inside an array truncates it).
- Every RemoteFunction returns a `Result`: `{ ok = true, data = ... }` or `{ ok = false, code = "E_..." }`. Codes are listed in [[Logging and Error Handling#Player-facing error codes]].
- Identifiers (`animalId`, `eggId`, `quoteId`, `raidId`, `entityId`) are server-issued strings of 1 to 40 characters matching `^[%w_%-]+$`.
- Server time for countdowns uses `workspace:GetServerTimeNow()`; fields named `...At` are server timestamps in seconds.

### 1.4 Rate-limit model

Token bucket per player per remote: `rate` tokens per second, capacity `burst`. An empty bucket drops the call (events) or returns `E_RATE_LIMITED` (functions). Sustained abuse (bucket empty for more than 10 s) raises a `security.rate_abuse` log entry; it never kicks on its own. Global ceiling (**PROPOSED**): 60 inbound remote calls per second per player across all remotes.

### 1.5 Idempotency

| Mechanism | Used by |
|---|---|
| Single-use `quoteId`; a repeat confirm of an already consumed quote within 30 s returns the **original** result | Eggs/RequestRoll, Hatch/RequestHatch |
| `expectedLevel` or `expectedStage` must equal current state, so a duplicate request fails with `E_STALE_STATE` and changes nothing | Ascension, base upgrades, plot expansion |
| Consumed IDs no longer exist, so repeats fail with `E_NOT_OWNED` | Merge, egg moves, raid claims |
| `seq` numbers on combat intents; server ignores a `seq` ≤ the last processed | Combat/BasicAttack |

## 2. Complete remote table

Direction: **C→S** client to server, **S→C** server to client (owner, nearby or all). Type: **RE** RemoteEvent, **RF** RemoteFunction (client invokes server only), **URE** UnreliableRemoteEvent. Rate: `rate/s (burst)`.

### 2.1 Session, data, settings, notifications

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Session/ClientReady` | RE | C→S | `{}` | Once per session; repeats ignored | 0.1/s (1) | Server sends `Data/ProfileSnapshot` when the profile is loaded |
| `Data/ProfileSnapshot` | RE | S→C owner | `{ seq: int, schemaVersion: int, view: ClientProfileView }` | — | — | Client replaces its `StateStore` |
| `Data/ProfileDelta` | RE | S→C owner | `{ seq: int, changes: { { path: string, value: any } } }` | — | Coalesced per Heartbeat | Client applies in `seq` order; a gap triggers `Data/RequestResync` |
| `Data/RequestResync` | RE | C→S | `{ lastSeq: int }` | Integer ≥ 0 | 0.1/s (2) | Server re-sends a snapshot |
| `Settings/Save` | RE | C→S | `{ settings: { [key]: number \| boolean \| string } }` | Whitelisted keys, numbers clamped 0–1, enums checked, ≤ 32 keys | 0.5/s (3) | Persisted; echoed by delta |
| `Notify/Toast` | RE | S→C owner | `{ code: string, params: { [string]: string \| number }? }` | — | — | NotificationController shows the localised message |

### 2.2 Combat

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Combat/BasicAttack` | RE | C→S | `{ seq: int, aim: Vector3, targetId: string? }` | `aim` unit length ±0.05; alive; not stunned; combo cadence 0.45 s with jitter allowance; range and line of sight from **server** positions; PvP permission if the target is a player | 4/s (6) | Damage applied; `Combat/HitConfirm` to nearby players; or `Combat/ActionRejected` |
| `Combat/UseSpecial` | RE | C→S | `{ specialId: "PowerStrike" \| "GroundSlam" \| "RallyCry", aim: Vector3, targetId: string? }` | Unlocked by level (L1, L10, L25); cooldown 6 / 12 / 25 s; same range rules | 2/s (3) | `Combat/CooldownSync` + hit confirms, or rejection |
| `Combat/Dodge` | RE | C→S | `{ dir: Vector3 }` | Unit vector; 4 s cooldown | 1/s (2) | Server grants 0.3 s invulnerability window |
| `Combat/UseAnimalAbility` | RE | C→S | `{ slot: 1 \| 2 \| 3, targetId: string? }` | Slot occupied by a live companion; ability is manual; its cooldown and the 0.5 s global cooldown elapsed | 4/s (6) | AnimalAIService casts; `Combat/CooldownSync` |
| `Combat/CommandTarget` | RE | C→S | `{ mode: "Attack" \| "Follow" \| "Hold", targetId: string? }` | Target exists, hostile to the player, within 40 studs of the player (**PROPOSED**, [[Targeting and Command System]]) | 4/s (8) | Companions retarget (D-009) |
| `Combat/HitConfirm` | URE | S→C nearby | `{ h: { { a: string, t: string, d: int, k: int } } }` (batched, ≤ 8 hits, < 1,000 bytes) | — | ≤ 20 messages/s per client | Damage numbers and hit VFX only |
| `Combat/EntityState` | RE | S→C nearby | `{ entityId: string, state: "KnockedOut" \| "Defeated" \| "Revived" \| "Despawned" }` | — | — | Animation and UI state |
| `Combat/CooldownSync` | RE | S→C owner | `{ key: string, readyAt: number }` | — | — | Cooldown UI |
| `Combat/ActionRejected` | RE | S→C owner | `{ action: string, seq: int?, code: string }` | — | ≤ 5/s | Client cancels predicted cooldown UI |
| `Combat/PlayerDefeated` | RE | S→C owner | `{ battleType: "Wild" \| "Boss" \| "PvP" \| "Raid", summary: { [string]: number }? }` | — | — | Defeat screen; penalty content **UNDECIDED** ([[Open Questions#Q-014]]) |
| `Combat/RewardGranted` | RE | S→C owner | `{ entityId: string, cash: int, xp: int, speciesId: string? }` | — | Coalesced 0.25 s | Reward popup |

Entity health is **not** sent through remotes: the server sets `Health` and `MaxHealth` attributes on entity models, which replicate to clients that have the model streamed in.

### 2.3 World, spawns and bosses

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `World/Announcement` | RE | S→C all | `{ kind: "RareSpawn" \| "WorldBossSoon" \| "WorldBossSpawned" \| "WorldBossDefeated", regionId: string, subjectId: string, at: number }` | — | — | Server-wide banner (Mythical and Secret rare spawns, world bosses 2 min ahead) |
| `Boss/PhaseChanged` | RE | S→C all | `{ bossInstanceId: string, phase: int }` | — | — | Music and health-bar state |
| `Boss/Telegraph` | URE | S→C nearby | `{ b: string, atk: string, o: Vector3, s: int, w: number }` | — | ≤ 10/s | Ground decals and warning VFX |
| `Boss/EncounterResult` | RE | S→C participants | `{ bossInstanceId: string, eligible: boolean, contribution: number }` | — | — | Result card; rewards **UNDECIDED** ([[Open Questions#Q-015]]) |

### 2.4 Eggs, luck and hatching

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Eggs/GetRollQuote` | RF | C→S | `{ count: 1 \| 5 }` | Profile loaded; not in a raid as attacker | 2/s (4) | `RollQuote { quoteId, oddsVersion, odds: { [Rarity]: number }, price, destination, expiresAt }` |
| `Eggs/RequestRoll` | RF | C→S | `{ quoteId: string, oddsVersion: string }` | Quote belongs to player, unexpired, unconsumed; `oddsVersion` equals the current version (else `E_STALE_ODDS`); cash ≥ price; free capacity ≥ count | 2/s (4) | `{ eggs: { { id, rarity, location } } }` |
| `Eggs/MoveEggs` | RF | C→S | `{ eggIds: { string } (1–10), to: "Backpack" \| "Base" }` | Player at own base; eggs owned, unlocked, not already there; destination capacity | 2/s (4) | Updated locations |
| `Luck/OddsInvalidated` | RE | S→C owner | `{ reason: "ProgressionChanged" \| "ConfigChanged" }` | — | Coalesced 1 s | Open roll or hatch UI re-requests a quote and shows the new odds |
| `Hatch/GetHatchQuote` | RF | C→S | `{ eggIds: { string } (1–5) }` | ≤ 5 eggs (D-016); owned; unlocked; base eggs only at the base; out of combat; free animal storage ≥ count | 2/s (4) | `HatchQuote { quoteId, oddsVersion, eggs: { { eggId, rarity, pool: { [speciesId]: number } } }, expiresAt }` |
| `Hatch/RequestHatch` | RF | C→S | `{ quoteId: string, oddsVersion: string }` | As for the quote, re-checked at commit; eggs still present | 1/s (2) | `{ results: { { eggId, animalId, speciesId, rarity } } }` |

### 2.5 Ascension, merging, base, team

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Ascension/GetPreview` | RF | C→S | `{ animalId: string }` | Owned | 4/s (6) | `{ currentLevel, nextLevel, duplicatesRequired, eligibleDuplicateIds, fee }` |
| `Ascension/RequestAscend` | RF | C→S | `{ animalId: string, duplicateIds: { string } (1–5), expectedLevel: int 0–4 }` | See [[Service - AscensionService]] | 1/s (2) | `{ animalId, newLevel }` |
| `Merge/RequestMerge` | RF | C→S | `{ eggIds: { string } (exactly 3) }` | See [[Service - MergeService]] | 1/s (2) | `{ egg: { id, rarity, location = "Base" } }` |
| `Base/RequestUpgrade` | RF | C→S | `{ moduleId: ModuleId, expectedLevel: int 0–4 }` | Module available (Q-007), next level only, cost affordable, gates met, at own base | 1/s (3) | `{ moduleId, newLevel }` |
| `Base/RequestPlotExpansion` | RF | C→S | `{ expectedStage: int 0–3 }` | Next stage only, affordable, at own base | 1/s (2) | `{ stage }` |
| `Base/AtBaseChanged` | RE | S→C owner | `{ atBase: boolean }` | — | — | Base UI availability |
| `Team/SetTeam` | RF | C→S | `{ slots: { string, string, string } }` (`""` = empty) | Exactly 3 entries; at own base (D-010); each non-empty ID owned, unique, unlocked | 1/s (3) | `{ slots }` |
| `Team/LockChanged` | RE | S→C owner | `{ locked: boolean }` | — | — | Lock icon on the team display |

### 2.6 Raids and PvP

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Raid/GetEligibleTargets` | RF | C→S | `{}` | Raids enabled; requester opted in | 0.5/s (2) | `{ targets: { { userId, bandLabel } } }` |
| `Raid/RequestRaid` | RF | C→S | `{ defenderUserId: int }` | See [[Service - RaidService]] eligibility | 0.2/s (1) | `{ raidId, startsAt }` |
| `Raid/ClaimEgg` | RF | C→S | `{ raidId: string, eggId: string }` | Raid active, requester is attacker, egg is in the defender's **base** storage, within interaction range of the vault, egg limit not reached (**UNDECIDED** value, [[Open Questions#Q-013]]) | 2/s (3) | `{ eggsClaimed, eggLimit }` |
| `Raid/ClaimAnimal` | RF | C→S | `{ raidId: string, animalId: string }` | Defender animal **knocked out in this raid**, within range, fewer than **3** animals claimed | 1/s (2) | `{ animalsClaimed, animalLimit = 3 }` |
| `Raid/RequestEnd` | RF | C→S | `{ raidId: string }` | Requester is attacker | 0.2/s (1) | Raid resolves per [[Raid Lifecycle and States]] |
| `Raid/IncomingAlert` | RE | S→C defender | `{ raidId: string, attackerUserId: int, startsAt: number }` | — | — | Alarm and UI |
| `Raid/StateChanged` | RE | S→C attacker and defender | `{ raidId: string, state: string, role: "Attacker" \| "Defender", endsAt: number? }` | — | — | Raid HUD |
| `Raid/ClaimsUpdated` | RE | S→C attacker and defender | `{ raidId: string, eggsClaimed: int, eggLimit: int, animalsClaimed: int, animalLimit: int }` | — | — | Counters |
| `Raid/Result` | RE | S→C attacker and defender | `{ raidId: string, outcome: string, eggs: { [Rarity]: int }, animals: { string } }` | — | — | Result screen |
| `PvP/SetParticipation` | RF | C→S | `{ pvp: boolean?, raids: boolean? }` | Exists only if the chosen activation method uses a toggle (**UNDECIDED**, [[Open Questions#Q-011]]); cooldown and not in combat | 0.2/s (2) | `{ pvp, raids }` |
| `PvP/StatusChanged` | RE | S→C all | `{ userId: int, pvpActive: boolean }` | — | — | Nameplate indicator |

### 2.7 Progression, index, shop, telemetry

| Remote | Type | Dir | Payload schema | Validation | Rate | Response / effect |
|---|---|---|---|---|---|---|
| `Progression/LevelUp` | RE | S→C owner | `{ level: int, unlocks: { string } }` | — | — | Level-up celebration |
| `Progression/RegionUnlocked` | RE | S→C owner | `{ regionId: string }` | — | — | Map update |
| `Index/SpeciesDiscovered` | RE | S→C owner | `{ speciesId: string, firstTime: boolean }` | — | — | Index toast |
| `Shop/PurchaseGranted` | RE | S→C owner | `{ productKey: string }` | — | — | Confirmation; the purchase prompt itself is opened client-side with `MarketplaceService:PromptProductPurchase` and granted in `ProcessReceipt` |
| `Telemetry/ClientError` | URE | C→S | `{ msg: string ≤ 200, stack: string ≤ 500, ctx: string ≤ 32 }` | Lengths; untrusted text, never displayed to other players | 5 per 60 s (5) | Logged as `client.error` |
| `Telemetry/ClientMetrics` | URE | C→S | `{ fps: number, memMb: number, pingMs: number, tier: int }` | Ranges | 1 per 60 s (1) | Aggregated performance metrics |
| `Telemetry/UIFunnel` | RE | C→S | `{ funnel: string, step: int }` | Whitelisted funnel names; step 1–20 | 10 per 60 s (10) | Onboarding and UI funnel analytics (untrusted, analytics only) |

## 3. Illustrative manifest and gate

```lua
--!strict
-- ReplicatedStorage/Shared/RemoteManifest (excerpt). Illustrative Luau.
export type RemoteKind = "Event" | "Function" | "Unreliable"
export type Direction = "ToServer" | "ToClient"

export type RemoteSpec = {
	kind: RemoteKind,
	dir: Direction,
	rate: number?,   -- tokens per second (ToServer only)
	burst: number?,
}

return {
	Eggs = {
		GetRollQuote = { kind = "Function", dir = "ToServer", rate = 2, burst = 4 },
		RequestRoll  = { kind = "Function", dir = "ToServer", rate = 2, burst = 4 },
		MoveEggs     = { kind = "Function", dir = "ToServer", rate = 2, burst = 4 },
	},
	Combat = {
		BasicAttack = { kind = "Event", dir = "ToServer", rate = 4, burst = 6 },
		HitConfirm  = { kind = "Unreliable", dir = "ToClient" },
	},
	-- ...every row of the table above
} :: { [string]: { [string]: RemoteSpec } }
```

```lua
--!strict
-- ServerScriptService/Systems/Net (excerpt). Illustrative Luau, not tested.
local function bindFunction(domain: string, name: string, schema: Schema, handler: Handler)
	local spec = Manifest[domain][name]
	assert(spec.kind == "Function" and spec.dir == "ToServer", "only client-to-server functions exist")
	local remote = Remotes[domain][name] :: RemoteFunction
	remote.OnServerInvoke = function(player: Player, payload: unknown)
		if not RateLimiter.take(player, domain .. "/" .. name, spec.rate, spec.burst) then
			return { ok = false, code = "E_RATE_LIMITED" }
		end
		local valid, parsed = Validation.check(schema, payload)
		if not valid then
			Log:Security("invalid_payload", player, { remote = name })
			return { ok = false, code = "E_INVALID_PAYLOAD" }
		end
		local ok, result = xpcall(handler, debug.traceback, player, parsed)
		if not ok then
			Log:Error("handler_error", player, { remote = name, trace = result })
			return { ok = false, code = "E_INTERNAL" }
		end
		result.detail = nil -- never leak server detail
		return result
	end
end
```

Handlers bound to RemoteFunctions **must not yield on DataStores or other players**. They read in-memory state only, so the client's `InvokeServer` returns within a frame or two.

## 4. Change control

Adding, removing or changing a remote requires: a row in this table, an updated manifest, a schema in `Shared/Schemas`, a test in [[Test Cases - Exploit Prevention]] (malformed payload, rate abuse, forged IDs), and an entry in the [[Changelog]]. Remote names are part of the client contract; renaming one is a breaking change for any client still running an older build during a rolling update ([[Content Update Pipeline]]).

## Related documents
- [[Technical Architecture Index]]
- [[Server-Client Responsibilities]]
- [[Implementation - Remote Validation Layer]]
- [[Implementation - Rate Limiting]]
- [[Replication Strategy]]
- [[Latency Handling]]
- [[Security Architecture]]
- [[Exploit Prevention]]
- [[Randomised Reward Compliance]]
- [[Logging and Error Handling]]
