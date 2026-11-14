---
title: Mini-Boss - Stormtalon
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - skyreach-peaks
  - flying
---

# Mini-Boss - Stormtalon

| Field | Value |
|---|---|
| Asset ID | BOS-06 |
| Type | Mini-boss (2 phases) |
| Base animal | Giant eagle with storm-charged feathers |
| Region / arena | [[Region - Skyreach Peaks]] / Thunderspire eyrie |
| Recommended level | 60–66 |
| Gate role | Key for [[Region - Emberheart Caldera]] (with level 65) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Stormtalon nests on the summit of Thunderspire, where storms never clear. Its feathers crackle with static, and when it beats its wings the wind can throw a careless climber off the peak. It is the game's first **aerial boss**. Its lesson: **ranged pressure and punish windows**. Stormtalon alternates between perching (melee-reachable) and hovering (reachable by Ranged companions, ranged abilities and the moments after a dive).

## 2. Arena: Thunderspire eyrie

- Roughly circular summit platform, **60-stud radius**, with a giant woven nest at the centre (low, walkable).
- **Three lightning rods** (ancient metal spires) at 35 studs from centre. Standing behind a rod relative to Stormtalon blocks Gale Wingbeat's push; rods also attract Storm Call strikes in phase 2.
- Edges drop away. A fall returns the player to the arena's entrance ledge with the standard 10% max HP fall damage (floored at 1 HP, [[Environmental Hazards]] H7). They remain a participant if back within 20 s.
- Ambient Summit Lightning (HZ-14) is disabled inside the arena; the boss supplies its own.

## 3. Stats (PROPOSED)

`HP = 200 × 30 × 6.2`, `ATK = 20 × 2.4 × 6.2`, `DEF = 10 × 2.4`.

| Stat | Value |
|---|---:|
| Max HP (solo) | 37,200 |
| ATK | 298 |
| DEF | 24 |
| Flight | Hover height 8–12 studs (reachable by melee only during dives and perches) |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Sky Hunter | 100–50% | Perch 10 s / hover 8 s cycle; rakes, dives, feather volleys, wingbeats | At 50%: 2.5 s; Stormtalon spirals upward and the storm intensifies; rods begin to hum |
| 2: Eye of the Storm | 50–0% | Shorter perches (7 s), Storm Call, Thunder Dive | — |

## 5. Attack list

Damage percentages are of a level 64 player's max HP (856 HP, DEF 36.5); one SkillMultiplier point ≈ 25.5%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Talon Rake | 1, 2 (perched) | Light | 1.0 | Cone 90°, 10 studs | 0.5 s orange cone, wings spread | 0.3 s / 0.5 s | ~26% | Dodge or step behind |
| Feather Volley | 1, 2 (hovering) | Light | 0.9 | 5 lines 25 × 2 studs fanned at targets | 0.7 s orange lines, wings pulled back | 0.4 s / 0.6 s | ~23% per line | Move between lines |
| Dive Bomb | 1, 2 | Heavy | 1.9 | Line 40 × 6 studs ending at the target's position | 0.9 s red line, shriek, tucks wings | 0.6 s / **2.0 s grounded** | ~48% | Sidestep, then punish while it is grounded |
| Gale Wingbeat | 1, 2 | Control | 0.5 | Cone 60°, 30 studs; pushes 15 studs | 1.0 s purple cone, wings rise high | 0.6 s / 0.8 s | ~13% + push toward the edge | Stand behind a rod or dodge roll through |
| Storm Call | 2 | Signature | 2.2 | 4 circles 7 studs on players plus one on each rod | 1.5 s red circles, crackling | 0.3 s / 0.6 s | ~56% | Move off your circle; stay away from rods while it charges |
| Thunder Dive | 2 | Ultimate | 2.4 | Ring: 6–40 studs from the landing point at the nest | 2.5 s red ring, gold safe circle within 6 studs of the nest | 0.5 s / 3.0 s grounded | ~61% | Move into the nest's gold circle; punish the long grounded window |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Flight cycle:** perch (melee rotation) and hover (ranged rotation) alternate; the cycle timer is visible through animation (it shakes its feathers 1 s before taking off).
- **Target selection:** highest threat, except Dive Bomb, which targets the player furthest from the nest (discouraging edge-camping).
- **Edge logic:** Gale Wingbeat is only aimed toward an edge if the target is more than 20 studs from the edge, so it cannot instantly knock a player off without a telegraph and some space to react.
- **Rotation (P2):** Storm Call every 14 s; Thunder Dive every 30 s.
- **Reset:** arena empty 10 s → returns to the nest, full HP.

## 7. Multiplayer scaling

- Max HP: 37,200 solo; 52,080 (2); 81,840 (4); 141,360 (8, cap).
- Feather Volley adds one line per 2 participants beyond the first (max 9).
- Credit: ≥ 5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 6.2; R3 a fixed-rarity egg (for example Epic or Legendary); R4 first-defeat trophy; R5 cosmetic (for example a storm-feather glider trail). Confirmed regardless: Emberheart gate key, +10 PS.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Chime Pavilions Waystone; contribution kept until reset. Falls are not knock-outs (H7).

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Huge eagle with slate-blue feathers edged in electric cyan; wingspan readable from the ground ([[Boss Art Direction]]) |
| Animation | Feather-shake before take-off, wing tuck before Dive Bomb, grounded recovery with wings spread ([[Animation - Boss Attacks]]) |
| VFX | Static sparks on feathers, lightning circles with reduced-flash alternative, wind cone lines for Wingbeat ([[VFX - Combat Effects]]) |
| Sound | Piercing shriek before dives, thunder rolls, humming rods in P2 ([[Sound - Bosses]]) |
| Camera | Auto-tilt upward while the boss hovers, per [[Camera Behaviour Guidelines]] |

## 11. Test hooks

- Gale Wingbeat on a player 15 studs from the edge → not aimed at the edge.
- Fall from the eyrie → returned to the entrance ledge, still a participant if back within 20 s.
- Thunder Dive gold circle fits 8 players.
- Hovering height keeps the boss reachable by Ranged companions (28-stud range, [[Canonical Proposed Values#3. Animal stat model (PROPOSED)]]).

## Related documents
- [[Boss Design Overview]]
- [[Region - Skyreach Peaks]]
- [[Boss AI]]
- [[Animal Roles]]
- [[Test Cases - Bosses]]
