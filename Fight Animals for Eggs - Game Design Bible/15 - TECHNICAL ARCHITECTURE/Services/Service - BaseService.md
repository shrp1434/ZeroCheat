---
title: Service - BaseService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - base
  - modules
  - upgrades
---

# Service - BaseService

> [!info] PROPOSED
> Layer **3**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design: [[Player Base System]], [[Base Upgrade System]], [[Base Layout and Plot Expansion]], [[Base Defence Overview]], [[Shield Mechanics]]. Schema: [[Schema - Base Data]]. Module availability at launch is **UNDECIDED** ([[Open Questions#Q-007]]).

> [!success] CONFIRMED rules enforced here
> Every player has a modular base with individually upgradeable sections (D-022). The team can only be changed at the player's own base (D-010; BaseService provides the authoritative at-base test). The Egg Merging Station is purchased and upgraded, and changes appearance per upgrade (D-020). Bases are protected by shields and physical defences (D-024).

## Responsibility

- Assign each joining player one of the 16 plots and build their base from saved data; free the plot on leave.
- Validate and commit module construction and upgrades (L1–L5), plot expansion (4 stages) and Egg Merging Station purchase and upgrades (5 levels), including gates.
- Swap module and station models (`ServerStorage/BaseModules`, `ServerStorage/MergeStationModels`) to match levels.
- Provide the **authoritative at-base test** (`IsAtOwnBase`) and fire `AtBaseChanged`.
- Expose base bonuses: Cash multiplier (Multiplier Shrine, Trophy Hall), player Strength and companion stat bonus (Training Grounds).
- Hold shield state and the defence layout that RaidService activates during raids.
- Report total module levels for the Progression Score.

## Inputs

| Input | Source |
|---|---|
| `Base/RequestUpgrade`, `Base/RequestPlotExpansion` | Client |
| Region unlocks and world boss defeats (station gates) | [[Service - ProgressionService]] |
| Cash | [[Service - EconomyService]] |
| Character positions | Server view of characters, via `Systems/ZoneQuery` |
| Shield triggers | RaidService (after a raid) and the shield rules chosen for [[Open Questions#Q-030]] |

## Outputs

| Output | Consumer |
|---|---|
| `base` profile section | Client via deltas |
| `AtBaseChanged(player, atBase)` | TeamService (lock), EggService, MergeService, HatchService, client (`Base/AtBaseChanged`) |
| `ModuleLevelChanged(player, moduleId, level)` | LuckService (PS base term), CombatService (bonuses), analytics |
| `ShieldChanged(player, active, untilTime)` | RaidService, clients (shield VFX) |
| Models under `Workspace/Bases/Plot_NN` | Clients |

## Dependencies

[[Service - EconomyService]], [[Service - ProgressionService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `ZoneQuery`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `AtBaseChanged` | `(player, atBase: boolean)` |
| Signal | `ModuleLevelChanged` | `(player, moduleId: ModuleId, level: number)` |
| Signal | `ShieldChanged` | `(player, active: boolean, untilTime: number?)` |
| Signal | `PlotAssigned` / `PlotReleased` | `(player, plot: Model)` |
| Remotes | `Base/RequestUpgrade`, `Base/RequestPlotExpansion`, `Base/AtBaseChanged` | [[Remote Communication Contract#2.5 Ascension, merging, base, team]] |

## Data structures

```lua
--!strict
export type ModuleId = "AnimalPens" | "EggVault" | "DefenceStation" | "ShieldGenerator"
	| "TrainingGrounds" | "MultiplierShrine" | "TrophyHall" | "MergeStation"

export type BaseSection = {
	modules: { [ModuleId]: number },   -- 0 = not built, 1..5
	plotStage: number,                 -- 0..4 (0 = starting plot)
	trophies: { [string]: boolean },   -- unique boss trophies displayed
	shield: { activeUntil: number?, rechargeReadyAt: number? }, -- rules Q-030
	guardAssignments: { string },      -- animal IDs at guard posts (Q-033)
}

export type ModuleSpec = { id: ModuleId, baseCost: number, maxLevel: number }
```

**Costs** (from [[Canonical Proposed Values#12. Base modules (PROPOSED — availability Q-007)]]):
- Modules: `Cost(L) = round(BaseCost × 2.5^(L − 1))` for L = 1–5 (L1 is construction). Rounding is half-up, matching the canonical table (for example 1,000 × 2.5⁴ = 39,062.5 → 39,063).
- Plot expansion: `5,000 × 3^(n − 1)` for stages 1–4.
- Egg Merging Station: 2,500 / 15,000 / 60,000 / 250,000 / 1,000,000 with gates: L2 Region 2 unlocked; L3 Region 4; L4 Region 6 and one world boss defeated; L5 Region 8.

**Bonuses:**

| API | Formula (**PROPOSED**) |
|---|---|
| `GetCashBonus` | `0.10 × ShrineLevel + min(0.01 × uniqueTrophies, 0.12)` |
| `GetStrengthBonus` | `0.05 × TrainingGroundsLevel` |
| `GetCompanionStatBonus` | `0.04 × TrainingGroundsLevel` |
| `GetTotalModuleLevels` | Sum of 7 module levels + station level + plot stage (max 44) |

## Public API

```lua
--!strict
function BaseService:GetPlot(player: Player): Model?
function BaseService:IsAtOwnBase(player: Player): boolean
function BaseService:GetModuleLevel(player: Player, moduleId: ModuleId): number
function BaseService:GetStationLevel(player: Player): number
function BaseService:GetTotalModuleLevels(player: Player): number
function BaseService:GetCashBonus(player: Player): number
function BaseService:GetStrengthBonus(player: Player): number
function BaseService:GetCompanionStatBonus(player: Player): number
function BaseService:IsShielded(player: Player): boolean
function BaseService:SetShield(player: Player, untilTime: number, reason: string): ()   -- called by RaidService
function BaseService:GetDefenceLayout(player: Player): { { kind: string, level: number, cframe: CFrame } }
function BaseService:HandleRequestUpgrade(player: Player, p: { moduleId: ModuleId, expectedLevel: number }): Result<{ moduleId: ModuleId, newLevel: number }>
function BaseService:HandleRequestPlotExpansion(player: Player, p: { expectedStage: number }): Result<{ stage: number }>
```

## At-base detection

- Every 0.25 s (**PROPOSED**), `ZoneQuery` tests each character's root position against its own plot's `PlotBounds` volume expanded by 2 studs.
- On a change, fire `AtBaseChanged`. A short hysteresis (0.5 s outside before reporting "left") avoids flicker at the boundary.
- The test always uses the **server** position of the character. A client cannot claim to be at its base.
- Death or teleport away from the base reports "left" immediately.

## Upgrade commit

1. Check `moduleId` is available (Q-007 availability list in `BaseConfig`), `expectedLevel` equals current level (`E_STALE_STATE`), level < 5 (`E_MAX_LEVEL`), player at own base (`E_NOT_AT_BASE`), gates met (`E_UPGRADE_GATE`).
2. `Mutate({ "base", "economy" })`: debit the cost, increment the level.
3. Swap the model in the socket; fire `ModuleLevelChanged`.

Upgrades are instant at launch; build timers are not proposed.

## Error handling

| Case | Behaviour |
|---|---|
| No free plot (more than 16 players) | Should not happen with `MaxPlayers = 16`; if it does, log `Error` `base.no_plot` and kick with a retry message |
| Model missing for a level | Use the previous level's model, log `Error` |
| Upgrade failures | Codes as above; no change |
| Player leaves mid-upgrade | Mutation is synchronous; nothing is half-applied |

## Security requirements

- Costs, gates and bonuses come only from config and server state.
- `IsAtOwnBase` uses server positions and the player's **own** plot only.
- Shields cannot be set from any remote.
- Plot geometry is server-built; client-side changes to the base are visual only and ignored by the server.
- Players inside another player's plot during a shield are pushed out by the shield (rules in [[Shield Mechanics]]); BaseService exposes `IsInsidePlot(player, plotOwner)` for that check.

## Testing requirements

| Test | Type |
|---|---|
| Cost of every module and level matches the canonical table | Unit (35 cases) |
| Station L4 refused without one world boss defeated | Unit |
| Upgrade request while away from base refused | Unit |
| Double submit with the same `expectedLevel` upgrades once | Unit |
| At-base flag flips within 0.75 s of crossing the boundary | Integration |
| 16 players join; each gets a distinct plot; leaving frees it | Integration ([[Test Cases - Bases and Upgrades]]) |
| Cash bonus with Shrine L3 and all 12 trophies = 0.30 + 0.12 = 0.42; a 13th trophy entry (corrupt data) still caps at 0.12 | Unit |

## Related documents
- [[Technical Architecture Index]]
- [[Player Base System]]
- [[Base Upgrade System]]
- [[Base Layout and Plot Expansion]]
- [[Egg Merging Station]]
- [[Shield Mechanics]]
- [[Schema - Base Data]]
- [[UI - Base Management]]
- [[UI - Base Upgrades]]
- [[Test Cases - Bases and Upgrades]]
