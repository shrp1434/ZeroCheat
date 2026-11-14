---
title: Mini-Boss - Hammertide
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - coral-coast
  - aquatic
---

# Mini-Boss - Hammertide

| Field | Value |
|---|---|
| Asset ID | BOS-04 |
| Type | Mini-boss (2 phases) |
| Base animal | Giant hammerhead shark crowned with coral |
| Region / arena | [[Region - Coral Coast]] / Breakwater Lagoon |
| Recommended level | 36–42 |
| Gate role | Key for [[Region - Frostfang Tundra]] (with level 40) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Hammertide patrols the shallow Breakwater Lagoon, its wide hammer-shaped head encrusted with coral. It moves through knee-deep water and above it in short surging leaps, using the same "air-swim" language proposed for aquatic companions (D-043 **PROPOSED**; aquatic movement is **UNDECIDED**, [[Open Questions#Q-028]]). Its lesson: **use elevation and timing**. The lagoon floods in rhythm with the boss's attacks, and three wooden jetties are the safe ground.

## 2. Arena: Breakwater Lagoon

- Shallow lagoon, **90 × 70 studs**, water 2 studs deep (no movement penalty for players; Hammertide is faster in water).
- Ringed by breakwater rocks (`BossArena` boundary).
- **Three jetties** (4 studs above the water, 20 × 6 studs each) at the north, east and west sides. Riptide Surge cannot reach players on jetties.
- Tide pools at the edges hold shallow sand where Hammertide cannot follow (it beaches briefly if it lunges there: 1.5 s vulnerable).

## 3. Stats (PROPOSED)

`HP = 200 × 30 × 3.2`, `ATK = 20 × 2.6 × 3.2`, `DEF = 10 × 2.5`.

| Stat | Value |
|---|---:|
| Max HP (solo) | 19,200 |
| ATK | 166 |
| DEF | 25 |
| Move speed | 20 studs/s in water; Hammer Ram 55 studs/s |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

The Assassin-like profile (lower HP coefficient, higher ATK) makes Hammertide fast and punishing but quicker to defeat than Rimeback.

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Patrol | 100–50% | Rams, head slams, fin slices | At 50%: 2.5 s; Hammertide dives under, the lagoon churns, coral on its head glows |
| 2: Frenzy | 50–0% | +30% attack speed, Whirlpool, Riptide Surge | — |

## 5. Attack list

Damage percentages are of a level 40 player's max HP (568 HP, DEF 24.5); one SkillMultiplier point ≈ 23.5%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Fin Slice | 1, 2 | Light | 1.0 | Line 20 × 3 studs as it passes | 0.5 s orange line, dorsal fin breaks the surface | 0.3 s / 0.4 s | ~24% | Step off the line |
| Head Slam | 1, 2 | Heavy | 1.8 | Circle 9 studs in front | 0.9 s red circle, head rises out of the water | 0.3 s / 1.2 s | ~42% | Back off or dodge; punish during recovery |
| Hammer Ram | 1, 2 | Heavy | 1.9 | Line 45 × 7 studs | 0.9 s red line, tail thrashes | 0.8 s / 1.0 s (1.5 s beached if it ends on sand) | ~45% | Sidestep; bait it towards tide-pool sand |
| Tidal Wake | 1, 2 | Control | 0.7 | Line 30 × 10 studs | 1.0 s purple line, wave builds | 0.5 s / 0.5 s | ~16% + 10-stud knockback | Dodge roll through (0.3 s invulnerability) |
| Whirlpool | 2 | Control | 0.5 per s | Circle 14 studs; pulls 4 studs/s toward centre | 1.2 s purple spiral | 5.0 s | ~12% per s at centre | Walk outward; stay out of the centre |
| Riptide Surge | 2 | Ultimate | 2.3 | Arena-wide wave except jetties | 2.5 s red foam line from one side, conch-like boom | 1.5 s / 2.0 s | ~54% + knockback | Stand on a jetty (gold decal) |
| Frenzy Bite | 2 | Signature | 2.2 | Cone 60°, 10 studs, three quick bites | 1.5 s red cone, jaws open | 0.9 s / 1.0 s | ~52% if all hit | Dodge after the first bite |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Movement:** circles the lagoon in water; approaches jetties only to Head Slam (it cannot climb).
- **Target selection:** highest threat, but Hammer Ram prefers the target furthest away in open water.
- **Jetty pressure:** if more than half of participants stand on jetties for 6 s, it uses Tidal Wake against a jetty to push players off, so jetties are a timing tool, not a permanent safe spot.
- **Rotation (P2):** Whirlpool every 16 s, Riptide Surge every 30 s, Frenzy Bite every 12 s.
- **Reset:** arena empty 10 s → full HP.

## 7. Multiplayer scaling

- Max HP: 19,200 solo; 26,880 (2); 42,240 (4); 72,960 (8, cap).
- With 5+ participants, Whirlpool spawns two smaller vortices (10 studs) instead of one.
- Credit: ≥ 5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 3.2; R3 a fixed-rarity egg (for example Rare or Epic); R4 first-defeat trophy; R5 cosmetic (for example a coral crest). Confirmed regardless: Frostfang gate key, +10 PS.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Lantern Stack Waystone; contribution kept until reset.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Stylised hammerhead with coral crown; friendly-majestic eyes, no gore or exposed teeth rows beyond the stylised norm ([[Boss Art Direction]], D-026) |
| Animation | Dorsal-fin surfacing before Fin Slice, head-rise before Head Slam, beached flop loop on sand ([[Animation - Boss Attacks]]) |
| VFX | Water trails consistent with D-043 air-swim style, foam lines for wakes and surges, spiral whirlpool decal ([[VFX - Combat Effects]]) |
| Sound | Water rush loop, deep boom before Riptide Surge, splash cues per attack ([[Sound - Bosses]]) |

## 11. Test hooks

- Players on jetties take no damage from Riptide Surge.
- Hammer Ram ending on sand → 1.5 s beached state.
- Jetty-camping 6 s → Tidal Wake targets a jetty.
- Whirlpool pull cannot drag a player through the arena boundary.

## Related documents
- [[Boss Design Overview]]
- [[Region - Coral Coast]]
- [[Boss AI]]
- [[Animal Families]]
- [[Test Cases - Bosses]]
