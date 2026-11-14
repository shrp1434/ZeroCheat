---
title: Mini-Boss - Vinecoil
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - emerald-canopy
---

# Mini-Boss - Vinecoil

| Field | Value |
|---|---|
| Asset ID | BOS-03 |
| Type | Mini-boss (2 phases) |
| Base animal | Giant python wrapped in living jungle vines |
| Region / arena | [[Region - Emerald Canopy]] / Strangler's Cenote |
| Recommended level | 26–30 |
| Gate role | Key for [[Region - Coral Coast]] (with level 28) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Vinecoil is a colossal python so old that the jungle has grown over it; vines and orchids sprout from its scales and it moves through the cenote's hanging vines as if they were part of its body. Pythons constrict rather than envenom, so Vinecoil's danger is **grabs and positioning**. Its lesson: **protect each other**. Constrict holds a player or companion, and allies (or the player's own animals, by command) free them by damaging the coils.

## 2. Arena: Strangler's Cenote

- Circular sinkhole floor, **60-stud radius**, open to the sky; walls covered in vines.
- A shallow central pool (1 stud deep, no movement penalty) and **four vine pillars** at 35 studs from centre.
- In phase 2 Vinecoil can enter a pillar and emerge from another; the destination pillar shakes and sheds leaves as a telegraph.
- The cenote rim is outside the arena; the only entrance is a root ramp from the Riverwild Floor.

## 3. Stats (PROPOSED)

`HP = 200 × 35 × 2.2`, `ATK = 20 × 2.3 × 2.2`, `DEF = 10 × 2.8`.

| Stat | Value |
|---|---:|
| Max HP (solo) | 15,400 |
| ATK | 101 |
| DEF | 28 |
| Move speed | 16 studs/s; Coil Lunge 45 studs/s |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Coiled Hunter | 100–50% | Sweeps, lunges, Constrict | At 50%: 2.5 s; Vinecoil rears and vanishes into a pillar; the cenote's vines start to sway |
| 2: The Living Vine | 50–0% | Pillar travel, Vine Lash, Canopy Shake, Strangler's Embrace | — |

## 5. Attack list

Damage percentages are of a level 28 player's max HP (424 HP, DEF 18.5); one SkillMultiplier point ≈ 20%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Tail Sweep | 1, 2 | Light | 1.0 | Arc 270° behind and beside, 12 studs | 0.6 s orange arc, tail lifts | 0.4 s / 0.6 s | ~20% | Stay in front or dodge through |
| Coil Lunge | 1, 2 | Heavy | 1.9 | Line 30 × 5 studs | 0.9 s red line, body coils back | 0.5 s / 1.2 s | ~38% | Sidestep |
| Constrict | 1, 2 | Control | 0.4 per s for up to 3 s | Grab on one target (player or companion) within 10 studs | 1.0 s purple circle on the target, head sways | Hold up to 3 s; release early when allies deal 3% of boss max HP to the coils | ~8% per s + hold | Dodge the grab; allies or companions (by command) attack the coils; the held player taps to struggle (each tap −0.1 s) |
| Vine Lash | 2 | Light | 1.1 | 2 lines from pillars across the arena | 0.8 s orange lines, vines pulled taut | 0.3 s / 0.5 s | ~22% | Step off the lines |
| Pillar Emergence | 2 | Heavy | 1.8 | Circle 10 studs at the destination pillar | 1.5 s pillar shakes, leaves fall | 0.4 s / 1.0 s | ~36% | Move away from the shaking pillar |
| Canopy Shake | 2 | Signature | 2.2 | 6 circles 6 studs (falling branches) | 1.5 s red circles with falling-leaf preview | 0.3 s / 0.8 s | ~44% | Dodge out of circles |
| Strangler's Embrace | 2 | Ultimate | 2.4 | Arena-wide closing ring from the wall inwards, ending 10 studs from centre | 2.5 s red ring at the wall with gold central pool | 3.0 s sweep / 2.0 s | ~48% | Gather in the gold central pool |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Constrict targeting:** prefers a target that is not the current highest-threat target, so the "tank" is rarely held; companions can be grabbed, which teaches players to command others to free them.
- **Pillar travel (P2):** every 15–20 s Vinecoil enters the nearest pillar and emerges from the pillar furthest from the current highest-threat target.
- **Rotation (P2):** Vine Lash every 8 s, Canopy Shake every 18 s, Strangler's Embrace every 35 s.
- **Reset:** arena empty 10 s → full HP, returns to the pool.

## 7. Multiplayer scaling

- Max HP: 15,400 solo; 21,560 (2); 33,880 (4); 58,520 (8, cap).
- Constrict can hold up to 2 targets at once with 5+ participants (**PROPOSED**).
- Credit: ≥ 5% of current scaled max HP; damage to coils counts.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 2.2; R3 a fixed-rarity egg (for example Rare); R4 first-defeat trophy; R5 cosmetic (for example an orchid crown). Confirmed regardless: Coral Coast gate key, +10 PS.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Giant Kapok Waystone; contribution kept until reset.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Long segmented python (bone-chain rig, see [[Animal Rig Standards]]), moss-green with vine wraps and orchid accents; readable head silhouette at all times |
| Animation | Coil-back before Lunge, swaying head before Constrict, pillar-merge dissolve into vines ([[Animation - Boss Attacks]]) |
| VFX | Leaf bursts on emergence, vine-tension glow on Lash lines, gold glow on the central pool during Embrace ([[VFX - Combat Effects]]) |
| Sound | Scale rustle loop, creaking vines, low hiss before Constrict ([[Sound - Bosses]]) |
| UI | Held state shows a struggle prompt and a coil HP bar ([[UI - Boss Health Bar]]) |

## 11. Test hooks

- Constrict on a companion; player commands two animals to attack the coils → release before 3 s.
- Held player on mobile can struggle with taps; release by 3.0 s at the latest.
- Strangler's Embrace safe zone fits 8 players and 24 companions.
- Pillar Emergence telegraph ≥ 1.35 s on a 150 ms latency client.

## Related documents
- [[Boss Design Overview]]
- [[Region - Emerald Canopy]]
- [[Targeting and Command System]]
- [[Boss AI]]
- [[Test Cases - Bosses]]
