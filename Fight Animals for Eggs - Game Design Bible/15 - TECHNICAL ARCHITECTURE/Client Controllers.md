---
title: Client Controllers
type: architecture
category: technical-architecture
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - client
  - controllers
  - ui
  - luau
---

# Client Controllers

> [!info] PROPOSED
> Controller list, responsibilities and patterns are **PROPOSED**. Code is illustrative Luau and has not been run.

The client is a set of **controllers**: ModuleScripts in `StarterPlayer/StarterPlayerScripts/Controllers`, loaded by the single `ClientBootstrap` LocalScript ([[Roblox Project Hierarchy#4. Single-script bootstrap]]). Controllers present the world, collect input and ask the server for outcomes. They never decide outcomes ([[Server-Client Responsibilities]]).

## 1. Controller rules

| Rule | Detail |
|---|---|
| Same lifecycle as services | `Init(registry)` (no yielding, no remotes) then `Start()` |
| One source of truth | `StateStore` holds the replicated profile view. Controllers read it and subscribe to its change signals. Only `StateStore` handles `Data/ProfileSnapshot` and `Data/ProfileDelta` |
| All networking through `NetClient` | No controller touches a RemoteEvent instance directly; `NetClient` applies client-side schema pre-checks and local rate limits to avoid pointless rejections |
| UI layout lives in `StarterGui/Interfaces` | Controllers bind behaviour to the ScreenGuis; designers can edit layout without touching code |
| No outcome prediction | Roll, hatch, merge, ascension, team and upgrade screens wait for the server response (spinner allowed) |
| Cosmetic prediction only for combat | Attack animations and cooldown UI may start immediately ([[Latency Handling]]) |
| Quality-aware | VFX and companion visual detail read the current quality tier from `PerformanceController` |
| Clean-up | Each controller owns a Trove/Maid-style cleaner for connections tied to the character or a screen |

## 2. Controller catalogue

| Controller | Responsibility | Reads | Sends (remotes) | Server pages |
|---|---|---|---|---|
| `StateStore` | Holds `ClientProfileView`; applies `seq`-ordered deltas; requests resync on a gap; exposes `Changed(path)` signals | `Data/ProfileSnapshot`, `Data/ProfileDelta` | `Data/RequestResync` | [[Service - DataService]] |
| `NetClient` (shared module) | Wraps remotes, pre-validates payloads, local rate limiting, maps error codes to localised messages | — | All C→S remotes | [[Remote Communication Contract]] |
| `InputController` | Maps keyboard, mouse, touch and gamepad to actions via `ContextActionService` and `UserInputService`; exposes `Action` signals | Settings | — | — |
| `CameraController` | Third-person combat camera, base camera, hatch reveal camera; respects [[Camera Behaviour Guidelines]] | Settings | — | — |
| `CombatController` | Turns input into intents; plays predicted swing animations through `Animator:LoadAnimation`; handles `ActionRejected` and `CooldownSync` | `StateStore` (level, specials) | `Combat/BasicAttack`, `UseSpecial`, `Dodge`, `UseAnimalAbility` | [[Service - CombatService]] |
| `TargetingController` | Soft-lock target selection, target marker (`Highlight`), manual target commands (D-009) | Entities in range | `Combat/CommandTarget` | [[Targeting and Command System]] |
| `CompanionVisualController` | Client-side polish on server-owned companions: ability VFX, idle flourishes, nameplates; lowers detail by quality tier | `Workspace/Runtime/Companions` | — | [[Service - AnimalAIService]] |
| `EntityPresentationController` | Health bars from `Health` and `MaxHealth` attributes, KO and defeat states, damage numbers from `HitConfirm` | `Combat/HitConfirm`, `Combat/EntityState` | — | [[Combat Feedback and Readability]] |
| `InterfaceController` | Screen stack, modal rules, back navigation, input sinking, `GuiService` selection for gamepad | `UI Navigation Map` rules | — | [[UI Navigation Map]] |
| `HUDController` | Cash, level, XP bar, player strength, team panel, region name | `StateStore` | — | [[UI - Main HUD]], [[UI - Animal Team Display]] |
| `EggController` | Roll screen: requests a quote, displays **server odds exactly as received**, confirms with `quoteId` and `oddsVersion`, re-quotes on `Luck/OddsInvalidated` or `E_STALE_ODDS` | `StateStore` (cash, storage) | `Eggs/GetRollQuote`, `Eggs/RequestRoll`, `Eggs/MoveEggs` | [[Service - EggService]], [[UI - Egg Rolling]] |
| `HatchPresentationController` | Egg selection (≤ 5), hatch quote with per-pool odds, reveal sequence after the server result, skip after first viewing | Hatch quote | `Hatch/GetHatchQuote`, `Hatch/RequestHatch` | [[Service - HatchService]], [[UI - Egg Hatching]] |
| `InventoryController` | Animal inventory and egg storage screens, filters, sort | `StateStore` | — | [[UI - Animal Inventory]], [[UI - Egg Storage]] |
| `TeamController` | Team selection at the base; shows the lock state away from base | `StateStore`, `Team/LockChanged`, `Base/AtBaseChanged` | `Team/SetTeam` | [[Service - TeamService]], [[UI - Team Selection]] |
| `AscensionController` | Ascension preview and confirm | Preview response | `Ascension/GetPreview`, `Ascension/RequestAscend` | [[Service - AscensionService]], [[UI - Ascension]] |
| `MergeController` | Merge selection of 3 eggs, station level gating display | `StateStore` | `Merge/RequestMerge` | [[Service - MergeService]], [[UI - Egg Merging]] |
| `BaseController` | Base management and upgrades, `ProximityPrompt` hooks on module sockets, plot expansion | `StateStore` | `Base/RequestUpgrade`, `Base/RequestPlotExpansion` | [[Service - BaseService]], [[UI - Base Management]] |
| `RaidController` | Target list, raid HUD, claim prompts, alarm for defenders, result screen | `Raid/*` S→C remotes | `Raid/*` C→S remotes | [[Service - RaidService]], [[UI - Raid Interface]] |
| `PvPController` | PvP status UI and the opt-in control (form depends on Q-011) | `PvP/StatusChanged` | `PvP/SetParticipation` | [[Service - PvPService]], [[UI - PvP Interface]] |
| `BossController` | Boss health bar, phase music cue, telegraph decals | `Boss/*` | — | [[Service - BossService]], [[UI - Boss Health Bar]] |
| `IndexController` | Index screen (discovered vs owned, D-029) | `StateStore`, `Index/SpeciesDiscovered` | — | [[Service - IndexService]], [[UI - Animal Index Screen]] |
| `ProgressionController` | Level-up and region unlock presentation | `Progression/*` | — | [[Service - ProgressionService]], [[UI - Progression Interface]] |
| `NotificationController` | Toast queue, world announcements, error code messages | `Notify/Toast`, `World/Announcement` | — | [[UI - Notifications]] |
| `ShopController` | Product prompts via `MarketplaceService:PromptProductPurchase`, confirmation display | `Shop/PurchaseGranted` | — | [[UI - Shop]], [[Monetisation Principles]] |
| `VFXController` | Pools and plays `ParticleEmitter`, `Beam` and `Trail` effects; obeys quality tier caps | Signals from other controllers | — | [[VFX Bible]] |
| `AudioController` | `SoundGroup` routing, music state by region and combat, ducking | Settings | — | [[Audio Mixing and Priority]] |
| `LightingController` | Applies per-region lighting presets on region change | Region volumes | — | [[Lighting Direction]] |
| `SettingsController` | Settings screen; saves through the server | `StateStore` | `Settings/Save` | [[UI - Settings]] |
| `PerformanceController` | Measures frame time and memory, sets quality tier 1–3, sends metrics | Engine stats | `Telemetry/ClientMetrics` | [[Performance Guidelines]] |
| `TelemetryController` | Captures client script errors (`ScriptContext.Error`) and UI funnel steps | — | `Telemetry/ClientError`, `Telemetry/UIFunnel` | [[Service - AnalyticsAndLoggingService]] |

## 3. Odds display contract (EggController and HatchPresentationController)

> [!success] CONFIRMED principle (D-017)
> The actual odds must be shown before the player commits, and odds must never change silently after a purchase.

Client obligations:
1. Never compute or round odds itself beyond the display format the server supplies. The quote contains the display strings or values exactly as the compliance page requires ([[Randomised Reward Compliance]]). Display precision is **UNDECIDED** (Q-810, see [[Service - LuckService]]).
2. The confirm button is disabled until a quote is on screen and enabled only while `expiresAt` is in the future.
3. On `E_STALE_ODDS`, `E_QUOTE_EXPIRED` or `Luck/OddsInvalidated`, replace the odds on screen with a fresh quote and require a new confirmation. Never auto-confirm.

```lua
--!strict
-- EggController excerpt. Illustrative Luau, not tested.
local function openRollScreen(count: number)
	local quote = NetClient.invoke("Eggs", "GetRollQuote", { count = count })
	if not quote.ok then
		Notify.showError(quote.code)
		return
	end
	RollScreen:ShowOdds(quote.data.odds, quote.data.price, quote.data.expiresAt)
	RollScreen.Confirm:Once(function()
		local result = NetClient.invoke("Eggs", "RequestRoll", {
			quoteId = quote.data.quoteId,
			oddsVersion = quote.data.oddsVersion,
		})
		if result.ok then
			RollPresentation:Play(result.data.eggs)
		elseif result.code == "E_STALE_ODDS" or result.code == "E_QUOTE_EXPIRED" then
			openRollScreen(count) -- show the new odds; the player must confirm again
		else
			Notify.showError(result.code)
		end
	end)
end
```

## 4. StateStore

```lua
--!strict
export type ClientProfileView = {
	cash: number,
	level: number,
	xp: number,
	eggs: { [string]: { rarity: string, location: "Backpack" | "Base" } },
	capacity: { backpack: number, base: number },
	animals: { [string]: { speciesId: string, ascension: number, variant: string? } },
	team: { string },            -- 3 entries, "" for empty
	teamLocked: boolean,
	index: { [string]: { discovered: boolean, owned: boolean } },
	base: { modules: { [string]: number }, plotStage: number, stationLevel: number },
	settings: { [string]: number | boolean | string },
}
```

The view excludes server-only fields (session lock, purchase history, suspicion score, Progression Score). The authoritative schema is [[Schema - Player Profile]].

Resync rule: if a delta arrives with `seq ~= lastSeq + 1`, the store discards it and fires `Data/RequestResync`. Because RemoteEvents are ordered and reliable this should only happen after a hot reload in Studio; it is a defensive measure.

## 5. Mobile and input notes

- Touch controls are created by `InputController` with `ContextActionService:BindAction(..., createTouchButton = true)` for attack, special, dodge and ability buttons, plus custom buttons styled per [[UI Design System]].
- UI scales through `UIScale` and `UIAspectRatioConstraint`; layout uses `UIListLayout` and `UIGridLayout` ([[UI Accessibility Standards]]).
- Controllers must not create per-frame allocations in `RenderStepped` or `Heartbeat`; see [[Performance Guidelines#Client budgets]].

## 6. Testing requirements

| Test | Type |
|---|---|
| StateStore applies a snapshot then 100 random deltas and matches the server view | Unit (Studio test place) |
| EggController never sends `RequestRoll` without a displayed quote | Unit with a stub NetClient |
| Re-quote on `OddsInvalidated` replaces displayed odds before confirm becomes active | UI test |
| All controllers start with no profile (slow DataStore) and recover when it arrives | Integration |
| Touch layout usable on a 16:9 and a 4:3 viewport | Manual, [[Test Cases - Mobile Performance]] |

## Related documents
- [[Technical Architecture Index]]
- [[Architecture Overview]]
- [[Roblox Project Hierarchy]]
- [[Remote Communication Contract]]
- [[UI and UX Index]]
- [[UI Navigation Map]]
- [[Latency Handling]]
- [[Performance Guidelines]]
