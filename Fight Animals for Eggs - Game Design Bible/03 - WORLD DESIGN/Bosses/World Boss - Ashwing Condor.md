---
title: World Boss - Ashwing Condor
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - world-boss
  - skyreach-peaks
  - emberheart-caldera
  - flying
---

# World Boss - Ashwing Condor

| Field | Value |
|---|---|
| Asset ID | BOS-12 |
| Type | World boss (3 phases) |
| Base animal | Giant condor with ember-lit feathers |
| Location / arena | Ashen Rim, between [[Region - Skyreach Peaks]] and [[Region - Emberheart Caldera]] |
| Recommended level | 70 |
| Spawn cadence | Every 60 min per server, announced 2 min ahead (canonical) |
| Lifetime | Retreats after 900 s if undefeated (**PROPOSED**) |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

The Ashen Rim is where cold mountain wind meets the caldera's heat. Once an hour, a vast condor rises out of the volcano on a thermal, its feathers glowing like embers at the tips and trailing ash. The Ashwing Condor is the **hardest world boss** and the last that most players need for the Starfall gate. Its lesson: **use the environment to reach the enemy**. In phase 2 the caldera vents become **thermal updrafts** that carry players up to the boss's high perches.

## 2. Arena: Ashen Rim

- Long ridge, **150 × 60 studs**, with the caldera's glowing slope on one side and the cold peaks on the other.
- **Three perches** (rock pinnacles 25 studs high) along the ridge; the condor lands on them.
- **Four vents** along the caldera edge: inert in phase 1, **thermal updrafts** in phases 2–3 (riding one lifts a player to perch height for 6 s, server-validated, [[Exploit Prevention]]).
- **Five rock windbreaks** on the cold side are the gold safe zones for Ashstorm and Firestorm Descent.
- Falls off the ridge return players to the arena's ends (H7 fall rule, [[Environmental Hazards]]).
- Reachable from both regions: players arriving from Skyreach Peaks need not have unlocked Emberheart Caldera; the arena volume belongs to the rim (**PROPOSED**).

## 3. Stats (PROPOSED)

`HP = 200 × 100 × 8.5`, `ATK = 20 × 2.3 × 8.5`, `DEF = 10 × 3.2` (E = 8.5).

| Stat | Value |
|---|---:|
| Max HP (solo) | 170,000 |
| ATK | 391 |
| DEF | 32 |
| Flight | Circles at 30–40 studs; dives to the ridge; perches at 25 studs |
| Lifetime | 900 s |

Target time-to-kill: designed for groups of 4–8 (about 3 min for 6); solo is possible but will often run close to the 900 s retreat timer.

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Rising Ember | 100–66% | Circles and dives; lands on the ridge every 25 s for 8 s | At 66%: 2.5 s; the condor screams; the vents ignite into updrafts |
| 2: Thermals | 66–33% | Perches high; players ride updrafts to reach it; Cinder Rain | At 33%: 3.0 s; ash clouds roll over the whole rim |
| 3: Ashstorm | 33–0% | Ashstorm pulses; Firestorm Descent every 45 s | — |

## 5. Attack list

Damage percentages are of a level 70 player's max HP (928 HP, DEF 39.5); one SkillMultiplier point ≈ 30.2%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Talon Swipe | 1–3 (landed) | Light | 0.9 | Cone 100°, 12 studs | 0.5 s orange cone | 0.3 s / 0.6 s | ~27% | Dodge or step behind |
| Ember Dive | 1–3 | Heavy | 1.8 | Line 50 × 8 studs ending at a target | 0.9 s red line, wings fold, ember trail | 0.6 s / 2.0 s landed | ~54% | Sidestep, then punish the landed window |
| Wingfire Sweep | 1–3 | Heavy | 1.8 | Cone 120°, 20 studs | 1.0 s red cone, wings spread wide with glowing tips | 0.6 s / 1.0 s | ~54% | Get behind the condor or out of range |
| Ash Cloud | 1–3 | Control | 0.4 | Circle 16 studs | 1.0 s purple circle, ash billows | Cloud lasts 6 s | ~12% + companions inside lose auto-targeting | Leave the cloud; re-issue target commands |
| Cinder Rain | 2, 3 | Signature | 2.1 | 8 circles 7 studs along the ridge | 1.5 s red circles, embers falling | 0.3 s / — | ~63% | Dodge out of circles |
| Ashstorm Pulse | 3 | Light (DoT) | 0.3 per s | Arena-wide, 5 s pulses every 20 s, except behind windbreaks | 1.5 s rising wind and grey vignette | 5.0 s | ~9% per s | Shelter behind windbreaks |
| Firestorm Descent | 3 | Ultimate | 2.4 | Arena-wide except windbreaks | 2.5 s screen-edge ember glow, scream then silence | 1.0 s / 3.0 s landed | ~72% | Shelter behind a windbreak; then punish the long landing |

Firestorm Descent is the highest damage share of any boss attack in the game and stays under the 75% cap ([[Boss Design Overview]]).

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Flight cycle (P1):** circles for 17 s, lands for 8 s; landing spot is near the highest-threat cluster.
- **Perch logic (P2):** perches on the pinnacle furthest from the most players; switches perch every 15 s or when 3+ players reach it via updrafts.
- **Ranged pressure:** while airborne it is targetable by Ranged companions and ranged player specials; melee damage needs landings, dives or updraft rides.
- **Rotation (P3):** Ashstorm Pulse every 20 s, Firestorm Descent every 45 s, Cinder Rain every 14 s.
- **Retreat:** at 900 s it rides a thermal back into the caldera (no rewards).

## 7. Multiplayer scaling

- Max HP: `170,000 × (1 + 0.45 × (N − 1))`: 399,500 (4), 705,500 (8), 1,317,500 (16, cap).
- Cinder Rain: +1 circle per 2 participants beyond the first (max 16).
- Credit: ≥ 2.5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 8.5; R3 a fixed-rarity egg (for example Legendary); R4 first-defeat trophy; R5 cosmetic (for example ember-feather wings for the avatar). Confirmed regardless: +20 PS on first credited defeat; counts toward the Starfall gate and toward the Aurora Crucible's "1 world boss defeated" requirement ([[Egg Merging Station]]).

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the nearer unlocked Waystone (Chime Pavilions or Ember Heart); contribution kept while the boss is alive.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Huge condor with dark plumage, ember-orange feather tips and a pale ruff; majestic, not menacing ([[Boss Art Direction]]) |
| Animation | Wide soaring loops, wing fold before Ember Dive, perch landing with wing flare ([[Animation - Boss Attacks]]) |
| VFX | Ember trails, ash cloud volumes with clear edges, heat shimmer above vents, Cinder Rain previews ([[VFX - Combat Effects]]) |
| Sound | Distant screams that cue phase changes, roaring thermals, silence before Firestorm Descent ([[Sound - Bosses]]) |
| Camera | Upward tilt assist while the boss is airborne ([[Camera Behaviour Guidelines]]) |

## 11. Test hooks

- Updraft lifts to perch height for 6 s and rejects client velocity changes.
- Windbreaks negate Ashstorm Pulse and Firestorm Descent.
- Firestorm Descent on a full-HP level 70 player leaves at least 25% HP.
- Players from Skyreach without Emberheart access can enter the arena.

## Related documents
- [[Boss Design Overview]]
- [[Region - Skyreach Peaks]]
- [[Region - Emberheart Caldera]]
- [[Boss AI]]
- [[Camera Behaviour Guidelines]]
- [[Test Cases - Bosses]]
