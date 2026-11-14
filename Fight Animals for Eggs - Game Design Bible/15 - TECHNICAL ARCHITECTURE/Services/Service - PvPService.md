---
title: Service - PvPService
type: technical-service
category: technical-architecture
status: mixed
priority: P1
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - pvp
  - combat
  - security
---

# Service - PvPService

> [!info] PROPOSED
> Layer **3**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design: [[PvP System]], [[PvP Activation Options]], [[Multiplayer Combat Rules]].

> [!success] CONFIRMED rule enforced here (D-023, D-024)
> PvP is optional and base raiding is optional. No player can be damaged by another player, or raided, without having chosen to take part.

> [!warning] UNDECIDED: activation method ([[Open Questions#Q-011]])
> How a player opts in (for example a toggle at the base, dedicated PvP zones, or invitations to duels or arenas) is not decided. PvPService is written against an **activation strategy interface** so the chosen method is one module, and `FeatureFlags.PvP` stays `false` until the owner decides. PvP defeat penalties are **UNDECIDED** ([[Open Questions#Q-014]]).

## Responsibility

- Hold each player's **PvP participation** and **raid participation** state (server-side only).
- Answer `CanDamage(attackerUserId, victimUserId, context)` for every player-versus-player hit, including companion damage attributed to an owner.
- Enforce safety rules: no PvP damage in safe zones (the hub, the victim's own shielded plot), a cooldown on leaving PvP after recent PvP combat, and no participation changes while in combat.
- Broadcast public PvP status for nameplates (`PvP/StatusChanged`).
- Register the `PvP` defeat-penalty handler with CombatService once penalties are decided.

## Inputs

| Input | Source |
|---|---|
| `PvP/SetParticipation` (only if the chosen strategy uses a toggle) | Client |
| Zone membership (PvP zones, safe zones) | `Systems/ZoneQuery` |
| Combat tags | `Systems/CombatTags` |
| Saved preferences | Profile (`pvp` section) |

## Outputs

| Output | Consumer |
|---|---|
| `CanDamage` answers | [[Service - CombatService]] |
| `IsRaidParticipant` answers | [[Service - RaidService]] |
| `ParticipationChanged(player, pvp, raids)` signal | RaidService, analytics |
| `PvP/StatusChanged` | All clients |

## Dependencies

[[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `ZoneQuery`, `CombatTags`. PvPService does **not** depend on CombatService (it is in a lower layer); CombatService calls it.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `ParticipationChanged` | `(player, pvpActive: boolean, raidsOptedIn: boolean)` |
| Remote C→S | `PvP/SetParticipation` | `{ pvp: boolean?, raids: boolean? }` |
| Remote S→C | `PvP/StatusChanged` | `{ userId, pvpActive }` |

## Data structures

```lua
--!strict
export type PvPSection = {
	pvpPreferred: boolean,      -- persisted preference (meaning depends on strategy)
	raidsOptedIn: boolean,      -- persisted
	lastChangedAt: number,
}

export type PvPContext = {
	raidId: string?,            -- set when both entities belong to the same raid
	zoneId: string?,
}

export type ActivationStrategy = {
	name: string,                                   -- e.g. "Toggle", "Zone", "Duel" (options in PvP Activation Options)
	isActive: (player: Player) -> boolean,
	onRequest: ((player: Player, wants: boolean) -> Result<boolean>)?,
	onZoneChanged: ((player: Player, zoneId: string?) -> ())?,
}
```

**PROPOSED values introduced here:** leave-PvP cooldown **30 s** after the last PvP damage dealt or received; participation change cooldown **10 s**.

## Public API

```lua
--!strict
function PvPService:SetStrategy(strategy: ActivationStrategy): ()     -- chosen once Q-011 is decided
function PvPService:IsPvPActive(player: Player): boolean
function PvPService:IsRaidParticipant(player: Player): boolean
function PvPService:CanDamage(attacker: Player, victim: Player, ctx: PvPContext): boolean
function PvPService:HandleSetParticipation(player: Player, p: { pvp: boolean?, raids: boolean? }): Result<{ pvp: boolean, raids: boolean }>
```

```lua
--!strict
-- Illustrative Luau, not tested.
function PvPService:CanDamage(attacker, victim, ctx)
	if attacker == victim then return false end
	if ctx.raidId then
		return RaidContext.bothIn(ctx.raidId, attacker, victim) -- raid combat rules (see Base Defence Overview, Q-035)
	end
	if not FeatureFlags.PvP or not strategy then return false end
	if ZoneQuery.isSafeZone(victim) or ZoneQuery.isSafeZone(attacker) then return false end
	return strategy.isActive(attacker) and strategy.isActive(victim)
end
```

`RaidContext` is a tiny lower-layer registry that RaidService writes (`raidId → { attacker, defender }`) so PvPService can answer without depending on RaidService.

## Error handling

| Case | Code |
|---|---|
| Feature disabled or strategy has no toggle | `E_FEATURE_DISABLED` |
| Change while in combat | `E_IN_COMBAT` |
| Leaving PvP within 30 s of PvP combat | `E_IN_COMBAT` |
| Change within 10 s of the last change | `E_RATE_LIMITED` |

## Security requirements

- Participation is server state. The client UI only requests changes.
- `CanDamage` is checked on **every** hit, so a player who leaves PvP is protected from the next hit onwards (subject to the leave cooldown).
- Companion damage is attributed to the owner and checked the same way.
- Safe-zone checks use server positions.
- Exploit to watch: toggling PvP on only to ambush and off before retaliation; the 30 s leave cooldown counters it ([[Exploit Prevention]]).

## Testing requirements

| Test | Type |
|---|---|
| With `FeatureFlags.PvP = false`, no player-versus-player damage is possible outside raids | Unit |
| Victim not opted in: 0 damage from player and companions | Unit |
| Both opted in but victim in the hub safe zone: 0 damage | Unit |
| Leaving PvP within 30 s of a PvP hit refused | Unit |
| Strategy swap (Toggle ↔ Zone) changes behaviour without other code changes | Unit |

Full list: [[Test Cases - PvP]].

## Related documents
- [[Technical Architecture Index]]
- [[PvP System]]
- [[PvP Activation Options]]
- [[Multiplayer Combat Rules]]
- [[Player Defeat and Penalties]]
- [[Service - CombatService]]
- [[Service - RaidService]]
- [[UI - PvP Interface]]
- [[Test Cases - PvP]]
