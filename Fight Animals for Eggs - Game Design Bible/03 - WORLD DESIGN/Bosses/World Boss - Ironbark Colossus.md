---
title: World Boss - Ironbark Colossus
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - world-boss
  - whisperwood-forest
  - sunscorch-savanna
---

# World Boss - Ironbark Colossus

| Field | Value |
|---|---|
| Asset ID | BOS-09 |
| Type | World boss (3 phases) |
| Base animal | Ancient giant tortoise carrying a living forest on its shell |
| Location / arena | Rootfall Crossing, on the border of [[Region - Whisperwood Forest]] and [[Region - Sunscorch Savanna]] |
| Recommended level | 15 |
| Spawn cadence | Every 45 min per server, announced 2 min ahead (canonical) |
| Lifetime | Retreats after 900 s if undefeated (**PROPOSED**) |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Every 45 minutes the ground at Rootfall Crossing trembles and an impossibly old tortoise lumbers out of the stream, its shell a hill of oaks, moss and birds. Ironbark Colossus is most players' **first world boss** and first big group moment. It is slow and enormous; the challenge is reading stomps, finding the glowing **Heartwood Knots** (weak points) and splitting up roles when its shell-forest spawns Sapling Sentinels. It is the gentlest world boss and should feel like a festival as much as a fight.

## 2. Arena: Rootfall Crossing

- Wide stream-side meadow, **140 × 120 studs**, bounded by giant fallen roots (arena boundary).
- The Colossus is about **60 studs long and 30 studs tall**; players fight around its legs and shell rim.
- **Four Heartwood Knots** glow on its legs and shell rim (front-left, front-right, rear-left, rear-right). Knots take **+50% damage**; at most two are exposed at a time, rotating every 20 s.
- Fallen-log cover pieces (5) block Root Spike lines.
- Accessible from both regions; players who have not unlocked the Savanna can reach the arena from the Whisperwood side ([[Region Unlock Progression]]), since the arena volume belongs to the border, not to the Savanna (**PROPOSED**).

## 3. Stats (PROPOSED)

`HP = 200 × 120 × 1.5`, `ATK = 20 × 2.6 × 1.5`, `DEF = 10 × 4.5` (encounter multiplier E = 1.5, [[Boss Design Overview]]).

| Stat | Value |
|---|---:|
| Max HP (solo) | 36,000 |
| ATK | 78 |
| DEF | 45 (×3 = 135 while withdrawn) |
| Move speed | 6 studs/s |
| Lifetime | 900 s |

Target time-to-kill: about 5–6 min solo at level 15; about 2.5–3 min for 6 players.

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: The Wandering Hill | 100–66% | Stomps, Root Spikes, Shell Quake | At 66%: 2.5 s; birds burst from the shell-forest; saplings uproot themselves |
| 2: The Forest Wakes | 66–33% | Sapling Sentinels join | At 33%: 3.0 s; the Colossus withdraws into its shell |
| 3: Heartwood | 33–0% | Withdraw cycles, Log Fall, Earthshaker | — |

### 4.1 Withdraw cycle (phase 3)

Every 40 s the Colossus withdraws for 10 s: DEF ×3, no knots exposed, Log Fall rains from the shell. When it emerges, **all four knots** are exposed for 8 s (+50% damage), followed by Earthshaker.

## 5. Attack list

Damage percentages are of a level 15 player's max HP (268 HP, DEF 12); one SkillMultiplier point ≈ 26%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Stomp | 1–3 | Heavy | 1.8 | Circle 12 studs under a raised foot | 0.9 s red circle, foot lifts slowly | 0.3 s / 1.5 s | ~47% | Leave the circle; attack the planted leg |
| Shell Quake | 1–3 | Light | 0.9 | Ring 15–45 studs from the centre of the shell | 0.8 s orange ring, shell shudders | 0.4 s / 0.8 s | ~23% | Move inside 15 studs (under the shell rim) or outside 45 |
| Root Spike | 1–3 | Control | 0.7 | 3 lines 30 × 4 studs radiating toward targets | 1.0 s purple lines, roots bulge | 0.3 s / 0.6 s | ~18% + root 1.0 s | Sidestep or hide behind a log |
| Sapling Sentinels | 2, 3 | Adds | — | 3 stationary saplings (+1 per 3 extra participants), each fires seed pellets | 1.5 s sapling drop shadows | Live until destroyed (each 2% of scaled max HP) | Pellets ~12% per hit | Assign companions with target commands |
| Log Fall | 3 | Signature | 2.2 | 8 circles 7 studs around the shell | 1.5 s red circles, branches creak | 0.3 s / — | ~57% | Dodge out of circles |
| Earthshaker | 3 | Ultimate | 2.4 | Arena-wide except gold circles on the five fallen logs | 2.5 s ground cracks glowing red, deep groan | 1.0 s / 3.0 s | ~62% | Stand on a log (gold decal) |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Movement:** walks a slow loop through the meadow; turns to face the highest-threat cluster every 8 s.
- **Target selection:** threat for Root Spike; Stomp hits whoever stands under a foot, so it punishes clustering at one leg.
- **Knot rotation:** two knots exposed at a time, switching every 20 s, so groups must move around the boss.
- **Saplings:** placed at least 25 studs apart so a single area attack cannot clear them.
- **Retreat:** at 900 s it sinks back into the stream (no rewards); cadence timer restarts.

## 7. Multiplayer scaling

- Max HP: `36,000 × (1 + 0.45 × (N − 1))`: 84,600 (4), 149,400 (8), 279,000 (16, cap).
- Saplings: +1 per 3 participants beyond the first.
- Credit: ≥ 2.5% of current scaled max HP; damage to saplings and healing count.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 1.5; R3 a fixed-rarity egg (for example Uncommon or Rare); R4 first-defeat trophy; R5 cosmetic (for example a sapling base decoration). Confirmed regardless: +20 PS on first credited defeat; counts as one of the two different world bosses for the Starfall gate ([[Region Unlock Progression]]).

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the nearest Waystone (Grandfather Oak or Great Baobab, whichever the player has unlocked and is closer); contribution kept while the boss is alive.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Huge tortoise with bark-textured skin and a shell carrying oaks, moss, flowers and a small waterfall; shell trees are separate meshes for sway ([[Boss Art Direction]]) |
| Animation | Slow, weighty walk; foot lift before Stomp; head-and-legs withdraw for the shell cycle ([[Animation - Boss Attacks]]) |
| VFX | Glowing amber knots, root-bulge decals, falling leaves and birds on transitions ([[VFX - Combat Effects]]) |
| Sound | Deep wooden groans, birdsong from the shell that falls silent before Earthshaker ([[Sound - Bosses]]) |
| UI | World boss bar with participant count and knot indicators ([[UI - Boss Health Bar]]) |

## 11. Test hooks

- Spawn every 45 min with a 2 min announcement; retreat at 900 s.
- Knots take +50% damage; withdrawn DEF ×3 applied.
- 16 participants → max HP 279,000, current HP % preserved on each join.
- Players without Savanna access can enter the arena from Whisperwood.

## Related documents
- [[Boss Design Overview]]
- [[Region - Whisperwood Forest]]
- [[Region - Sunscorch Savanna]]
- [[Boss AI]]
- [[Multiplayer Combat Rules]]
- [[Test Cases - Bosses]]
