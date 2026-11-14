---
title: Roblox Project Hierarchy
type: architecture
category: technical-architecture
status: proposed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - project-structure
  - rojo
  - luau
---

# Roblox Project Hierarchy

> [!info] PROPOSED
> The folder tree, bootstrap and Rojo layout below are **PROPOSED** for [[M02 - Core Project Setup]]. Code is illustrative Luau and has not been run.

This page fixes **where everything lives** in the Roblox DataModel. It improves the original sketch in three ways: (1) server code is split into `Services` (stateful, one per domain), `Systems` (stateless helpers and shared server utilities) and `Data` (schemas, migrations, server-only config); (2) the client has exactly one LocalScript and a `Controllers` folder that mirrors the server's services; (3) everything the server spawns at runtime goes into dedicated `Runtime` folders so streaming, cleanup and instance counting are trivial.

## 1. Placement rules

| Rule | Why |
|---|---|
| Anything a client must never read (wild animal templates, boss templates, hatch pool weights beyond what is disclosed, server config) lives in `ServerStorage` or `ServerScriptService` | Both are not replicated to clients |
| Anything both sides need (types, config the client displays, Signal, rarity enums) lives in `ReplicatedStorage/Shared` or `ReplicatedStorage/Config` | Single definition for both sides |
| Companion models are cloned **by the server** from `ServerStorage/AnimalTemplates` into `Workspace/Runtime/Companions` | The client never chooses which model represents an animal |
| UI-only animal previews (index screen, hatch reveal) use `ReplicatedStorage/Assets/AnimalPreviews` | Lightweight display meshes with no scripts and no collision |
| Remotes are created at boot by `Systems/Net` from `Shared/RemoteManifest` | The contract on [[Remote Communication Contract]] and the code cannot drift apart |
| No Script or LocalScript anywhere except the two bootstraps | One entry point per side, deterministic load order |
| Instances placed by designers in Workspace use **CollectionService tags** and attributes, not names, to be discovered | Renaming a part never breaks code |

## 2. Full tree

```text
game
├── Workspace
│   ├── World                         -- static, designer-authored geometry
│   │   ├── Hub_HatchlingHaven        -- egg shrine, base portals, safe zone volume
│   │   ├── Region_01_Whisperwood     -- one Model per region (StreamingMode: Default)
│   │   ├── Region_02_Sunscorch
│   │   ├── ...                       -- Regions 03 to 08 (see World Overview and Map)
│   │   └── RegionVolumes             -- invisible, non-colliding parts tagged "RegionVolume" with attribute RegionId
│   ├── Bases
│   │   ├── Plot_01 ... Plot_16       -- empty plot anchors, one per server slot (16 = max players, Q-031)
│   │   │   ├── PlotBounds            -- invisible part defining the at-base volume (tag "PlotBounds")
│   │   │   ├── SpawnLocation         -- player respawn at their own base
│   │   │   └── ModuleSockets         -- attachment points, tag "ModuleSocket", attribute SocketId
│   ├── AnimalSpawns
│   │   └── <RegionId>                -- folder per region
│   │       └── SpawnPoint parts      -- tag "AnimalSpawn"; attributes: RegionId, Rarity, PoolId, MaxAlive
│   ├── BossSpawns
│   │   ├── MiniBoss_<Id>             -- arena centre part; tag "BossSpawn"; attributes: BossId, Kind = "Mini"
│   │   └── WorldBoss_<Id>            -- attributes: BossId, Kind = "World", ArenaRadius
│   └── Runtime                       -- created by the server, never authored
│       ├── WildAnimals               -- live wild animal models
│       ├── Companions                -- live equipped companions (3 per player)
│       ├── Bosses
│       ├── Guards                    -- raid defenders spawned from pens (Q-033)
│       ├── Projectiles               -- server-authoritative hitboxes only; visuals are client-side
│       └── Drops                     -- temporary cash or egg pick-up visuals, if used
│
├── ReplicatedStorage
│   ├── Shared                        -- ModuleScripts required by both sides
│   │   ├── Types                     -- exported Luau types (Result, AnimalRecord, EggRecord, ...)
│   │   ├── Signal                    -- pure Luau signal class
│   │   ├── RemoteManifest            -- list of every remote: name, kind, direction (source of truth for Net)
│   │   ├── NetClient                 -- client wrapper over remotes (requires only RemoteManifest)
│   │   ├── Rarity                    -- ordered rarity enum and helpers
│   │   ├── Schemas                   -- payload validators shared for client-side pre-checks
│   │   ├── ErrorCodes                -- code to localisation key map
│   │   └── Util                      -- Maid/Trove-style cleanup, table utils, Promise-free task helpers
│   ├── Config                        -- data-only ModuleScripts; mirror Canonical Proposed Values
│   │   ├── RarityConfig
│   │   ├── AnimalCatalogue           -- 60 species: id, rarity, role, family, region, pool class
│   │   ├── CombatConfig
│   │   ├── EggConfig                 -- prices, baseline odds, hatch limits
│   │   ├── LuckConfig                -- slopes, pivot, PS weights (displayable parts only)
│   │   ├── AscensionConfig
│   │   ├── MergeConfig
│   │   ├── BaseConfig
│   │   ├── RegionConfig
│   │   ├── BossConfig
│   │   ├── RaidConfig                -- duration = nil (Q-012), eggTheftLimit = nil (Q-013)
│   │   ├── ProgressionConfig
│   │   └── FeatureFlags
│   ├── Remotes                       -- created at runtime by Systems/Net; folders per domain
│   │   ├── Data, Combat, Eggs, Hatch, Ascension, Merge, Base, Team, Raid, PvP, Boss, World,
│   │   └── Progression, Index, Notify, Settings, Telemetry
│   └── Assets                        -- replicated, script-free visual assets
│       ├── AnimalPreviews            -- display meshes for UI viewports (ANM-###)
│       ├── EggModels                 -- EGG-## models for roll and hatch presentation
│       ├── VFX                       -- ParticleEmitter, Beam and Trail templates (VFX-###)
│       ├── Animations                -- Animation objects (ANI-###); loaded through Animator:LoadAnimation
│       └── UI                        -- image and icon references (UI-###)
│
├── ServerScriptService
│   ├── Bootstrap                     -- the ONLY server Script
│   ├── Services                      -- one ModuleScript per service (18, see Service Architecture)
│   │   ├── DataService ... AnalyticsAndLoggingService
│   ├── Systems                       -- stateless or narrowly stateful server modules
│   │   ├── ServiceLoader             -- require, sort, Init, Start, Shutdown
│   │   ├── Net                       -- creates remotes, wraps handlers with gate (validation + rate limit)
│   │   ├── Validation                -- payload schema checks (see Implementation - Remote Validation Layer)
│   │   ├── RateLimiter               -- token buckets (see Implementation - Rate Limiting)
│   │   ├── WeightedRandom            -- see Implementation - Weighted Random Selection
│   │   ├── DamagePipeline            -- see Implementation - Combat Damage Pipeline
│   │   ├── AnimalLedger              -- the only writer of animal records
│   │   ├── AssetLocks                -- in-memory locks on animals and eggs
│   │   ├── QuoteStore                -- server-issued quote and request IDs with expiry
│   │   └── ZoneQuery                 -- point-in-volume checks for regions and plots
│   └── Data
│       ├── ProfileSchema             -- default profile + version (see Schema - Player Profile)
│       ├── Migrations                -- ordered migration functions (see Data Validation and Migration)
│       ├── ServerConfig              -- non-disclosed values (hatch pool tilt internals, anti-cheat thresholds)
│       └── DataStoreAdapter          -- the only module that touches DataStoreService
│
├── ServerStorage                     -- server-only assets, never replicated
│   ├── AnimalTemplates               -- rigged companion/wild models per species (ANM-###), no scripts
│   ├── WildAnimalTemplates           -- wild-specific wrappers: hitbox, aggro sensor attachments
│   ├── BossTemplates                 -- BOS-## models and phase props
│   ├── BaseModules                   -- MOD-## models per module and level (L1 to L5)
│   ├── MergeStationModels            -- 5 visual tiers of the Egg Merging Station
│   └── TestFixtures                  -- Studio-only test data; stripped from published builds
│
├── StarterPlayer
│   ├── StarterPlayerScripts
│   │   ├── ClientBootstrap           -- the ONLY LocalScript
│   │   └── Controllers               -- one ModuleScript per controller (see Client Controllers)
│   └── StarterCharacterScripts       -- empty by default (the default Animate script may be replaced, see Player Combat)
│
├── StarterGui
│   └── Interfaces                    -- one ScreenGui per screen; ResetOnSpawn = false
│       ├── MainHUD, TeamSelection, AnimalInventory, AnimalIndex, EggRolling, EggHatching,
│       ├── EggStorage, Ascension, EggMerging, BaseManagement, BaseUpgrades, RaidInterface,
│       └── PvPInterface, BossHealthBar, Notifications, Settings, Progression, Shop
│
├── SoundService                      -- SoundGroups: Master, Music, SFX, UI, Ambient (see Audio Mixing and Priority)
├── Lighting                          -- per-region presets applied by the client LightingController
└── TextChatService                   -- default configuration
```

## 3. Folder purposes and replication

| Container | Replicates to client | Purpose | Who writes at runtime |
|---|---|---|---|
| `Workspace/World` | Yes (streamed) | Static terrain and props | Nobody |
| `Workspace/Bases/Plot_NN` | Yes (streamed) | Base anchors; modules cloned into sockets | BaseService |
| `Workspace/AnimalSpawns` | Yes, but parts are tiny and transparent | Designer-placed spawn markers | Nobody; SpawnService reads tags |
| `Workspace/BossSpawns` | Yes | Arena markers | Nobody |
| `Workspace/Runtime/*` | Yes (streamed) | Live entities | SpawnService, AnimalAIService, BossService, RaidService |
| `ReplicatedStorage/Shared`, `Config`, `Assets` | Yes | Shared code, config, script-free assets | Nobody |
| `ReplicatedStorage/Remotes` | Yes | Remote instances | `Systems/Net` at boot |
| `ServerScriptService/*` | No | All server code | — |
| `ServerStorage/*` | No | Templates the client must not inspect | — |
| `StarterGui/Interfaces` | Copied into `PlayerGui` | UI layouts; logic lives in controllers | Client controllers |

> [!danger] Spawn markers and hidden data
> Any attribute on a Workspace instance is visible to every client. `AnimalSpawn` markers therefore carry a **PoolId** but never per-species weights or rare-spawn chances; those stay in `ServerScriptService/Data/ServerConfig`. Rare-spawn chances are design values, not purchase odds, so hiding them does not conflict with the odds disclosure rule in [[Randomised Reward Compliance]].

## 4. Single-script bootstrap

### Server

```lua
--!strict
-- ServerScriptService/Bootstrap (Script). Illustrative Luau, not tested.
local ServerScriptService = game:GetService("ServerScriptService")
local ReplicatedStorage = game:GetService("ReplicatedStorage")

local ServiceLoader = require(ServerScriptService.Systems.ServiceLoader)
local Net = require(ServerScriptService.Systems.Net)

Net.createRemotes(require(ReplicatedStorage.Shared.RemoteManifest))

local loader = ServiceLoader.new(ServerScriptService.Services)
local ok, err = loader:LoadAll()     -- require, validate layers, Init in order
if not ok then
	warn("[BOOT_FAILED]", err)
	return                            -- server stays unready; clients show a retry screen
end
loader:StartAll()                    -- Start in order, each in task.spawn

game:BindToClose(function()
	loader:ShutdownAll()             -- reverse order; DataService flushes last
end)

ReplicatedStorage:SetAttribute("ServerReady", true)
```

### Client

```lua
--!strict
-- StarterPlayer/StarterPlayerScripts/ClientBootstrap (LocalScript). Illustrative.
local ReplicatedStorage = game:GetService("ReplicatedStorage")

if not ReplicatedStorage:GetAttribute("ServerReady") then
	ReplicatedStorage:GetAttributeChangedSignal("ServerReady"):Wait()
end

local ControllerLoader = require(ReplicatedStorage.Shared.Util.ControllerLoader)
local loader = ControllerLoader.new(script.Parent:WaitForChild("Controllers"))
loader:LoadAll()
loader:StartAll()

require(ReplicatedStorage.Shared.NetClient).fire("Session", "ClientReady")
```

The client controller lifecycle matches the server lifecycle (`Init` then `Start`). See [[Client Controllers]] and [[Module Patterns and Bootstrapping]].

## 5. Rojo-compatible layout (optional)

Rojo is a widely used community tool that syncs files on disk into Roblox Studio, letting the team use Git, code review and external editors. It is **optional**: the hierarchy above works identically in a Studio-only workflow. If the team adopts it, the recommended layout is:

```text
repo/
├── default.project.json
├── src/
│   ├── shared/            -> ReplicatedStorage.Shared
│   ├── config/            -> ReplicatedStorage.Config
│   ├── server/
│   │   ├── Bootstrap.server.luau   -> ServerScriptService.Bootstrap (Script)
│   │   ├── Services/      -> ServerScriptService.Services
│   │   ├── Systems/       -> ServerScriptService.Systems
│   │   └── Data/          -> ServerScriptService.Data
│   └── client/
│       ├── ClientBootstrap.client.luau -> StarterPlayerScripts.ClientBootstrap (LocalScript)
│       └── Controllers/   -> StarterPlayerScripts.Controllers
├── tests/                 -> ServerStorage.TestFixtures (Studio-only place)
└── place/
    └── World.rbxl         -- binary place holding Workspace, Assets, ServerStorage models
```

```json
{
  "name": "FightAnimalsForEggs",
  "tree": {
    "$className": "DataModel",
    "ReplicatedStorage": {
      "Shared": { "$path": "src/shared" },
      "Config": { "$path": "src/config" }
    },
    "ServerScriptService": {
      "Bootstrap": { "$path": "src/server/Bootstrap.server.luau" },
      "Services": { "$path": "src/server/Services" },
      "Systems": { "$path": "src/server/Systems" },
      "Data": { "$path": "src/server/Data" }
    },
    "StarterPlayer": {
      "StarterPlayerScripts": {
        "ClientBootstrap": { "$path": "src/client/ClientBootstrap.client.luau" },
        "Controllers": { "$path": "src/client/Controllers" }
      }
    }
  }
}
```

Notes:
- Rojo's file conventions map `*.server.luau` to Script, `*.client.luau` to LocalScript, other `*.luau` files to ModuleScript, and a folder containing `init.luau` to a ModuleScript with children. Support for the `.luau` extension depends on the Rojo version (*unverified* for the exact version; `.lua` works everywhere).
- **Sync code, not art.** Models, meshes, terrain and UI layouts stay in the place file (or `.rbxm` model files managed by the art team). Only `src/` is synced. Instances in the project file without a `$path` are left alone by Rojo when unknown children exist (*unverified*; confirm with the Rojo version you adopt).
- `ReplicatedStorage/Remotes` is **not** in the project file: it is created at runtime from `RemoteManifest`.
- `ReplicatedStorage/Assets`, `ServerStorage` and `Workspace` are owned by the place file. Art imports follow [[Asset Naming Conventions]].

## 6. Naming conventions

| Thing | Convention | Example |
|---|---|---|
| Service module | `<Domain>Service` | `HatchService` |
| Client controller | `<Domain>Controller` | `HatchPresentationController` |
| Config module | `<Domain>Config` | `RaidConfig` |
| Remote | `<Domain>/<VerbNoun>` folder path | `Eggs/RequestRoll` |
| CollectionService tag | PascalCase noun | `AnimalSpawn`, `PlotBounds` |
| Attribute | PascalCase | `RegionId`, `EntityId`, `Health` |
| Species ID | lowercase snake | `snow_leopard`, `haasts_eagle` |

## Related documents
- [[Technical Architecture Index]]
- [[Service Architecture]]
- [[Client Controllers]]
- [[Module Patterns and Bootstrapping]]
- [[Configuration Modules]]
- [[Asset Naming Conventions]]
- [[Asset Register]]
- [[Replication Strategy]]
- [[Performance Guidelines]]
