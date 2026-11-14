---
title: Mini-Boss - Cinderjaw
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - emberheart-caldera
---

# Mini-Boss - Cinderjaw

| Field | Value |
|---|---|
| Asset ID | BOS-07 |
| Type | Mini-boss (2 phases) |
| Base animal | Colossal ember-scaled crocodile with obsidian scutes |
| Region / arena | [[Region - Emberheart Caldera]] / Magma Basin |
| Recommended level | 74–80 |
| Gate role | Key for [[Region - Starfall Sanctuary]] (with level 80 and 2 different world bosses) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Cinderjaw is the ancient lord of the caldera's lava lake: a crocodile the size of a ship, its back ridged with black obsidian and its jaws glowing from within. It glides through lava between basalt islands. It fits the proposed "ancient lineage" fiction (D-033 **PROPOSED**, [[Open Questions#Q-027]]) without being a hatchable species. Its lesson: **arena awareness under a shrinking space**. Outer islands sink as the fight progresses, and players must manage space, burning pools and grabs together.

## 2. Arena: Magma Basin

- Lava lake with a **central basalt island (50-stud diameter)** and **four outer islands (24-stud diameter)** linked by stone bridges (8 studs wide).
- Cinderjaw is immune to lava and moves through it at 22 studs/s; it surfaces beside an island to attack.
- **Sinking islands:** at 75%, 50% and 25% HP, one outer island sinks over 5 s (telegraphed by cracking and steam); players on it must cross a bridge. The fourth outer island stays for the whole fight.
- Lava contact uses the boss-arena rule: **lava here is part of the encounter**, dealing 15% max HP per second with bounce-out, and **can** knock out ([[Environmental Hazards]] H3). The edge of every island has a 1-stud glowing lip so the boundary is obvious.

## 3. Stats (PROPOSED)

`HP = 200 × 38 × 8.5`, `ATK = 20 × 2.3 × 8.5`, `DEF = 10 × 3.4`.

| Stat | Value |
|---|---:|
| Max HP (solo) | 64,600 |
| ATK | 391 |
| DEF | 34 |
| Move speed | 22 studs/s in lava; 12 studs/s on islands |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Basin Lord | 100–50% | Snaps, tail slams, magma spit, Death Roll; first island sinks at 75% | At 50%: 2.5 s; Cinderjaw dives, the lake brightens, a second island sinks |
| 2: Eruption | 50–0% | Lava Wave, Eruption; third island sinks at 25% | — |

## 5. Attack list

Damage percentages are of a level 78 player's max HP (1,024 HP, DEF 43.5); one SkillMultiplier point ≈ 26.6%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Jaw Snap | 1, 2 | Light | 1.0 | Cone 70°, 12 studs | 0.5 s orange cone, jaws part with inner glow | 0.25 s / 0.7 s | ~27% | Step aside |
| Tail Slam | 1, 2 | Heavy | 1.8 | Arc 180°, 16 studs behind | 0.9 s red arc, tail lifts out of lava | 0.3 s / 1.2 s | ~48% | Stay in front or dodge through |
| Magma Spit | 1, 2 | Light + zone | 0.9 impact | 3 circles 6 studs; leave burning pools for 6 s | 0.8 s orange circles, throat swells | 0.3 s / 0.5 s | ~24% + pools 3% max HP per s | Dodge out; avoid pools |
| Death Roll | 1, 2 | Control | 0.5 per s for 2 s | Grab one target at the island edge within 8 studs | 1.0 s purple circle, head lunges | Hold 2 s, then release 8 studs away on the same island | ~13% per s | Keep away from edges; allies deal 3% of boss max HP to break early |
| Lava Wave | 2 | Signature | 2.2 | Line 60 × 12 studs across an island | 1.5 s red line, lava surges up | 0.6 s / 0.8 s | ~59% | Dodge roll through (0.3 s invulnerability) or move off the line |
| Eruption | 2 | Ultimate | 2.4 | Arena-wide except gold circles (one per remaining island) | 2.5 s red glow across the basin, deep rumble | 1.0 s / 2.5 s | ~64% | Stand in a gold circle |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Positioning:** Cinderjaw circles the island holding the most participants and surfaces beside the highest-threat target; it climbs onto the central island only for Tail Slam and Eruption.
- **Grab preference:** Death Roll prefers a target standing within 8 studs of an edge, rewarding players who fight from island centres.
- **Island timing:** sinking is HP-driven, never time-driven, so a slow group is not punished twice (the soft enrage already covers stalling).
- **Rotation (P2):** Lava Wave every 12 s; Eruption every 30 s.
- **Reset:** arena empty 10 s → full HP, all islands restored.

## 7. Multiplayer scaling

- Max HP: 64,600 solo; 90,440 (2); 142,120 (4); 245,480 (8, cap).
- Magma Spit adds one circle per 3 participants beyond the first.
- Credit: ≥ 5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 8.5; R3 a fixed-rarity egg (for example Legendary); R4 first-defeat trophy; R5 cosmetic (for example an obsidian scute base ornament). Confirmed regardless: part of the Starfall gate, +10 PS.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Ember Heart Waystone; contribution kept until reset.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Long crocodilian with black obsidian scutes, ember-orange underglow and glowing jaw interior; stylised, not grotesque (D-026, [[Boss Art Direction]]) |
| Animation | Throat swell for Magma Spit, lunge-and-roll for Death Roll, belly-flop climb onto the central island ([[Animation - Boss Attacks]]) |
| VFX | Lava splash, burning pool decals with clear edges, island crack and steam before sinking ([[VFX - Combat Effects]]) |
| Sound | Bubbling lava bed, deep jaw clap, rising rumble before Eruption ([[Sound - Bosses]]) |

## 11. Test hooks

- Islands sink at 75/50/25% HP with a 5 s telegraph; never with a player stuck on an unreachable island.
- Death Roll releases the target on the same island, never into lava.
- Eruption gold circles exist for every remaining island.
- Lava inside the arena can knock out; ambient lava outside the arena cannot (H2 versus H3).

## Related documents
- [[Boss Design Overview]]
- [[Region - Emberheart Caldera]]
- [[Environmental Hazards]]
- [[Boss AI]]
- [[Test Cases - Bosses]]
