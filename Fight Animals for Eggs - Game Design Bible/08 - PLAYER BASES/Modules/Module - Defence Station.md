---
title: Module - Defence Station
type: system
category: base
status: proposed
priority: P1
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - defence
  - raiding
---

# Module - Defence Station

**Asset ID:** MOD-03 (**PROPOSED**). **Slot:** flexible hub building (recommended front row) plus perimeter pieces that attach to fixed points on the gate edge.

> [!success] CONFIRMED context
> Bases are protected by shields **and physical defences** (D-024). This module is the physical-defence layer.

> [!warning] UNDECIDED
> Raid duration is **UNDECIDED** ([[Open Questions#Q-012]]); all timings here are expressed in seconds for an at-level raider and must be retuned once `T_raid` is chosen. Module availability: **UNDECIDED** ([[Open Questions#Q-007]]).

## 1. Purpose

Costs a raider time and health before they reach guards and the vault. It is the first layer a raider meets and the main reason to plan a raid rather than walk in.

## 2. Footprint and appearance

| Element | Footprint (studs) | Placement |
|---|---|---|
| Watchtower hub | 14 × 14, 20 tall (L5: 28) | Flexible slot |
| Gate | 16 wide × 12 tall | Fixed, front edge |
| Barricade segments | 8 × 2 each, up to 6 | Fixed sockets along the approach |
| Trap pads | 6 × 6 each, up to 4 | Fixed sockets inside the gate |
| Turrets | 4 × 4 base, up to 2 | Fixed sockets flanking the gate |

Appearance: a friendly frontier outpost. Turrets are nature-themed launchers (seed pods, pinecones, crystal shards), never firearms, in line with [[Art Bible]] and [[Base Art Direction]].

## 3. Upgrade levels

**Gate breach time** is defined as seconds for a reference at-level raider team, and converted to HP at raid start using that raider's damage output (**PROPOSED**), so the gate stays meaningful at every progression band.

| Level | Cost (Cash) | Gate breach time | New element (PROPOSED) | Visual change |
|---:|---:|---:|---|---|
| L1 | 2,000 | 8 s | Timber palisade gate, 2 barricades | Log palisade, rope lashings, small lookout |
| L2 | 5,000 | 12 s | Bramble snares (2 trap pads): 40% slow for 2 s, 10 s re-arm | Stone footings, bramble coils |
| L3 | 12,500 | 16 s | Seed-pod launcher turret (1): 2% raider max HP per hit, 1 hit per 1.5 s, 40-stud range | Stone tower, brass launcher |
| L4 | 31,250 | 20 s | Second turret, 4 barricades, 4 trap pads | Crystal-tipped tower, violet signal lantern |
| L5 | 78,125 | 25 s | Thunderstone totem: every 8 s a chain pulse stuns up to 2 raider animals for 0.5 s; 6 barricades | Gold-capped tower, crackling storm crown |

Total: **128,875 Cash**.

> [!info] PROPOSED safety rails
> - Turret and pulse damage is a **percentage of the raider's max HP**, capped so the whole perimeter can remove at most **35%** of an at-level raider's HP if the raider walks straight through without fighting the turrets.
> - Turrets and traps never damage animals being stolen, guards or the owner.
> - Turrets can be destroyed by raiders (turret HP = 6 s of reference raider damage) and respawn when the raid ends.

## 4. Functionality

| Function | Detail |
|---|---|
| Gate | Blocks the only entrance. Raiders breach it by damage. The owner and friends pass through |
| Barricades | Force a path around the approach, lengthening exposure to turrets |
| Traps | Slow raiders; visible to raiders (no hidden traps, for fairness) |
| Turrets | Target the nearest raider player first, then raider animals |
| Totem (L5) | Crowd-control pulse on raider animals only |

Outside raids, the gate is open for the owner, friends and approved visitors, and every hostile element is inert.

## 5. Dependencies

- Slot for the watchtower. Perimeter sockets exist on every plot stage.
- Level cap `PlotStage + 1`.
- Turrets require line of sight; barricade sockets are placed so they cannot block line of sight to the gate.

## 6. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.DefenceStation = { level, slot }` |
| Instances | `Plot_##.Modules.DefenceStation` (tower), `Plot_##.Perimeter.Gate`, `Barricade_1..6`, `Trap_1..4`, `Turret_1..2` with attributes `Hp`, `MaxHp`, `Armed` |
| Raid-time logic | [[Service - RaidService]] spawns a defence controller for the raid; turret targeting at 4 Hz; projectiles simulated on the server with client-side visual tracers ([[Replication Strategy]]) |
| Hit validation | Damage to gate and turrets uses the normal combat pipeline ([[Implementation - Combat Damage Pipeline]]) with a raid context flag |
| Streaming | Perimeter parts are part of the plot model; turret VFX are client-only |
| Network ownership | All defence parts anchored and server-owned |

```lua
-- Illustrative Luau (not executed)
local GATE_BREACH_SECONDS = { 8, 12, 16, 20, 25 }

local function computeGateHp(level: number, raiderReferenceDps: number): number
	-- raiderReferenceDps is computed at raid start from the raider's player Strength and team stats
	return math.floor(GATE_BREACH_SECONDS[level] * raiderReferenceDps)
end
```

## 7. Animation and VFX

- Upgrade: palisade logs drop in one by one, tower telescopes upward ([[Animation - Base Upgrades]]).
- Raid start: lanterns flash, gate shutters slam, turrets rise from hatches ([[Animation - Raid Interactions]]).
- Turret shot: arcing seed-pod with a Trail and a puff of petals on impact ([[VFX - Combat Effects]]).
- Trap: brambles burst from the pad; slowed raider shows a vine-wrap decal.
- Totem pulse: Beam chain between targets, short thunder SFX ([[Sound - Base and Raid Alerts]]).

## 8. Raid interaction

| Phase | Behaviour |
|---|---|
| Pre-raid | Raider sees the gate, tower level and turret count in the raid preview |
| Breach | Gate HP set from the raider's reference damage; breaching opens the gate for the rest of the raid |
| Inside | Traps and turrets active until destroyed |
| Post-raid | Everything restored to full instantly |
| Disabling | Whether raiders can temporarily disable the tower itself is **UNDECIDED** (Q-403); working assumption: only turrets can be destroyed |

## Related documents
- [[Base Defence Overview]]
- [[Module - Shield Generator]]
- [[Animal Guards and Base Defence AI]]
- [[Base Raiding System]]
- [[Raid Anti-Exploit Validation]]
- [[Base Art Direction]]
- [[Cost Tables]]
- [[Player Bases Index]]
