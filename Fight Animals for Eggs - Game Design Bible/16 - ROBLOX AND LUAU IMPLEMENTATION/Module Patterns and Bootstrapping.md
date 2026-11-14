---
title: Module Patterns and Bootstrapping
type: implementation
category: engineering
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - engineering
  - architecture
  - bootstrapping
---

# Module Patterns and Bootstrapping

> [!info] PROPOSED
> This document defines how server services and client controllers are loaded, initialised and started. The list of services and their responsibilities is owned by [[Service Architecture]]; the folder layout is owned by [[Roblox Project Hierarchy]]. Code is **illustrative — not executed**.

## 1. Goals

1. **One entry point per side.** Exactly one server `Script` and one client `LocalScript` run game code. Everything else is a `ModuleScript`. This gives a deterministic start order and removes "which script ran first" bugs.
2. **Two-phase start.** Every service has `Init()` (wire up, no yielding, no cross-service calls that depend on start-up) and `Start()` (may yield, may call other services). All `Init()` calls finish before any `Start()` runs.
3. **No remote is connected before its service is ready.** Requests that arrive before the player's profile has loaded are answered with `NOT_READY` ([[Implementation - Remote Validation Layer#Reason codes]]).
4. **Server-only code never replicates.** Services and secret configuration sit in `ServerScriptService` and `ServerStorage` ([[Configuration Modules]]).

## 2. Folder roles (summary)

| Location | Contents | Replicated to client |
|---|---|---|
| `ServerScriptService/ServerMain` (Script) | Server bootstrap | No |
| `ServerScriptService/Services/*` | One ModuleScript per service, e.g. `HatchService` | No |
| `ServerStorage/Config/*` | Secret config: luck slopes, pool weights, rate limits, anti-cheat thresholds | No |
| `ReplicatedStorage/Shared/*` | Types, pure helpers (weighted selection, damage formula), public config | Yes |
| `ReplicatedStorage/Remotes` (Folder) | RemoteEvent, RemoteFunction and UnreliableRemoteEvent instances, created by the server at boot | Yes |
| `StarterPlayer/StarterPlayerScripts/ClientMain` (LocalScript) | Client bootstrap | Yes (client only) |
| `ReplicatedStorage/Client/Controllers/*` | One ModuleScript per controller | Yes |

> [!danger] Pure helpers in `ReplicatedStorage` are visible to exploiters
> Placing the weighted-selection algorithm in `Shared` is safe: the algorithm is not a secret. Placing the luck **slopes** or **pool weights** there is not, because D-017 allows the formula to stay hidden. Keep the data server-side and pass it into the shared pure functions.

## 3. Service contract

```lua
--!strict
-- Illustrative — not executed
-- ReplicatedStorage/Shared/Types/ServiceTypes

export type Service = {
	Name: string,
	Init: (self: any) -> (),   -- must not yield
	Start: (self: any) -> (),  -- may yield; runs in its own thread
}

return nil
```

A typical service:

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Services/HatchService

local HatchService = {
	Name = "HatchService",
}

local deps: {
	DataService: any,
	LuckService: any,
	RemoteGateway: any,
}? = nil

function HatchService:Init()
	-- Resolve dependencies through the registry; do not call them yet.
	local Registry = require(script.Parent.Parent.Registry)
	deps = {
		DataService = Registry.get("DataService"),
		LuckService = Registry.get("LuckService"),
		RemoteGateway = Registry.get("RemoteGateway"),
	}
end

function HatchService:Start()
	assert(deps, "HatchService started before Init")
	deps.RemoteGateway.bindFunction("RequestHatchEggs", function(player, payload)
		return HatchService.handleHatch(player, payload)
	end)
end

function HatchService.handleHatch(player: Player, payload: any): any
	-- See Implementation - Egg Roll and Hatch Flow
	return { ok = false, reason = "FEATURE_DISABLED" }
end

return HatchService
```

## 4. Registry

The registry is a plain name → module table. It is filled by the bootstrap before any `Init()` runs, so `Registry.get` inside `Init()` always succeeds. It prevents circular `require` chains: services require the registry, never each other directly.

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Registry

local Registry = {}
local services: { [string]: any } = {}
local locked = false

function Registry.register(name: string, module: any)
	assert(not locked, "Registry is locked after boot")
	assert(services[name] == nil, "Duplicate service: " .. name)
	services[name] = module
end

function Registry.get(name: string): any
	local s = services[name]
	assert(s ~= nil, "Unknown service: " .. name)
	return s
end

function Registry.lock()
	locked = true
end

return Registry
```

## 5. Server bootstrap

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/ServerMain

local ServerScriptService = game:GetService("ServerScriptService")
local Registry = require(ServerScriptService.Registry)
local ConfigLoader = require(ServerScriptService.ConfigLoader)

-- 1. Validate configuration first. A bad config must stop the server
--    before any player can roll an egg against wrong odds.
ConfigLoader.loadAndValidate() -- errors on failure (see Configuration Modules)

-- 2. Explicit start order. Data and the remote gateway come first.
local ORDER = {
	"RemoteGateway",               -- creates Remotes folder, rate limiter, validator
	"DataService",
	"AnalyticsAndLoggingService",
	"EconomyService",
	"ProgressionService",
	"IndexService",
	"LuckService",
	"EggService",
	"HatchService",
	"AscensionService",
	"MergeService",
	"TeamService",
	"CombatService",
	"AnimalAIService",
	"SpawnService",
	"BossService",
	"BaseService",
	"PvPService",
	"RaidService",
}

local servicesFolder = ServerScriptService.Services
for _, name in ORDER do
	local module = require(servicesFolder:FindFirstChild(name) :: ModuleScript)
	Registry.register(name, module)
end
Registry.lock()

-- 3. Init phase: synchronous, no yields.
for _, name in ORDER do
	local s = Registry.get(name)
	local ok, err = pcall(s.Init, s)
	if not ok then
		error(("Init failed for %s: %s"):format(name, tostring(err)))
	end
end

-- 4. Start phase: each in its own thread so one slow Start cannot block others.
for _, name in ORDER do
	local s = Registry.get(name)
	task.spawn(function()
		local ok, err = pcall(s.Start, s)
		if not ok then
			warn(("Start failed for %s: %s"):format(name, tostring(err)))
			-- AnalyticsAndLoggingService records the failure; the gateway
			-- marks that service's remotes as FEATURE_DISABLED.
		end
	end)
end
```

| Step | Failure behaviour | Status |
|---|---|---|
| Config validation | Server errors out; no players are served. The matchmaker routes players to other servers. *Unverified*: exact platform behaviour when a server script errors at start; test in [[M02 - Core Project Setup]]. | **PROPOSED** |
| `Init` failure | Fatal, same as above | **PROPOSED** |
| `Start` failure | Non-fatal; that feature's remotes return `FEATURE_DISABLED` | **PROPOSED** |

## 6. Client bootstrap

The client mirrors the server with controllers (`EggRollController`, `CombatInputController`, `AnimalRenderController` and so on, listed in [[Client Controllers]]). Two differences:

1. Controllers may not assume server data is present. They wait for the `ProfileReady` event from the server before enabling economy UI.
2. A controller failure must degrade gracefully: the HUD stays usable even if, for example, the egg roll controller failed to start.

```lua
--!strict
-- Illustrative — not executed
-- StarterPlayerScripts/ClientMain

local ReplicatedStorage = game:GetService("ReplicatedStorage")
local Controllers = ReplicatedStorage:WaitForChild("Client"):WaitForChild("Controllers")

local ORDER = {
	"NetController",          -- wraps remotes, attaches idempotency keys and sequence numbers
	"InputController",
	"HUDController",
	"AnimalRenderController", -- client-side visual models, see Replication Strategy
	"CombatInputController",
	"EggRollController",
	"HatchController",
	"BaseController",
	"RaidController",
}

local loaded = {}
for _, name in ORDER do
	local m = require(Controllers:WaitForChild(name) :: ModuleScript)
	loaded[name] = m
	local ok, err = pcall(m.Init, m)
	if not ok then warn("Controller init failed", name, err) end
end
for _, name in ORDER do
	local m = loaded[name]
	task.spawn(function()
		local ok, err = pcall(m.Start, m)
		if not ok then warn("Controller start failed", name, err) end
	end)
end
```

## 7. Remote gateway pattern

All remotes are created by `RemoteGateway` on the server at boot. Services never touch `OnServerEvent` or `OnServerInvoke` directly. The gateway applies, in this order: rate limit → payload validation → readiness check → handler → logging. The pipeline is specified in [[Implementation - Remote Validation Layer]].

```lua
-- Illustrative — not executed
RemoteGateway.bindFunction("RequestHatchEggs", HatchService.handleHatch, {
	schema = Schemas.HatchRequest,     -- type and shape
	bucket = "Economy",                -- rate limit bucket
	requiresProfile = true,
})
```

## 8. Player lifecycle hooks

| Hook | Owner | Notes |
|---|---|---|
| `Players.PlayerAdded` | DataService | Begins profile load with session lock ([[Data Consistency and Transactions]]). Other services subscribe to DataService's `ProfileLoaded` signal, not to `PlayerAdded`. |
| `Players.PlayerRemoving` | DataService | Runs `onPlayerLeaving` callbacks synchronously (raid end, hatch completion), then saves and releases the lock ([[Disconnect Handling]]). |
| `game:BindToClose` | DataService | Saves all loaded profiles in parallel. Shutdown wait time is *unverified*; design for a short window and save on every transaction anyway. |
| Players already present | DataService `Start` | Iterate `Players:GetPlayers()` once at start to catch players who joined before the service connected. |

## 9. Anti-patterns

- A `Script` inside each animal model. Use one AI service ([[Implementation - Animal AI State Machine]]).
- `require` cycles between services. Use the registry.
- `WaitForChild` on the server for instances the server itself creates.
- Services storing references to `Player` objects after `PlayerRemoving` (memory leak and stale-state bugs).

## Related documents
- [[Luau Implementation Index]]
- [[Luau Coding Standards]]
- [[Configuration Modules]]
- [[Service Architecture]]
- [[Roblox Project Hierarchy]]
- [[Client Controllers]]
- [[Remote Communication Contract]]
- [[Service - DataService]]
