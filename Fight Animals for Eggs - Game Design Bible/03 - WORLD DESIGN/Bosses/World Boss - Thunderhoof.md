---
title: World Boss - Thunderhoof
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - world-boss
  - sunscorch-savanna
---

# World Boss - Thunderhoof

| Field | Value |
|---|---|
| Asset ID | BOS-10 |
| Type | World boss (3 phases) |
| Base animal | Colossal elephant crackling with storm energy |
| Location / arena | Thunderflats, [[Region - Sunscorch Savanna]] |
| Recommended level | 30 |
| Spawn cadence | Every 50 min per server, announced 2 min ahead (canonical) |
| Lifetime | Retreats after 900 s if undefeated (**PROPOSED**) |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

The storm over Thunderflats never breaks, and every 50 minutes it walks. Thunderhoof is an elephant the size of a hill, tusks arcing with lightning, ears like storm clouds. It is a **returning-player** world boss: recommended level 30, well above the Savanna's band, so players come back after unlocking the Canopy. Its lesson for groups: **spread out and control the field**. Its lightning chains between players who stand together, and Storm Totems must be destroyed before they overcharge.

## 2. Arena: Thunderflats

- Cracked salt pan, **160 × 140 studs**, with low rock ridges at the edges (arena boundary).
- Puddles appear in phase 3 (Monsoon); standing in a puddle when lightning strikes nearby doubles Trunk Lightning chaining range (shown by a blue shimmer on puddles).
- No hard cover; four low stone cairns serve as **gold safe zones** for Sky Splitter.

## 3. Stats (PROPOSED)

`HP = 200 × 110 × 2.2`, `ATK = 20 × 3.0 × 2.2`, `DEF = 10 × 4.0` (E = 2.2).

| Stat | Value |
|---|---:|
| Max HP (solo) | 48,400 |
| ATK | 132 |
| DEF | 40 |
| Move speed | 10 studs/s; Stampede Charge 45 studs/s |
| Lifetime | 900 s |

Target time-to-kill: about 5 min solo at level 30; 2–3 min for 6 players.

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Rolling Thunder | 100–66% | Trunk Lash, Thunderclap Stomp, Stampede Charge | At 66%: 2.5 s; trumpet blast; three Storm Totems rise |
| 2: Storm Totems | 66–33% | Totems charge and strike; Trunk Lightning | At 33%: 3.0 s; the sky opens into rain; puddles form |
| 3: Monsoon | 33–0% | Puddle conduction, Sky Splitter every 40 s | — |

## 5. Attack list

Damage percentages are of a level 30 player's max HP (448 HP, DEF 19.5); one SkillMultiplier point ≈ 24.7%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Trunk Lash | 1–3 | Light | 1.0 | Cone 90°, 14 studs | 0.6 s orange cone, trunk curls back | 0.3 s / 0.6 s | ~25% | Dodge or step behind the front legs |
| Thunderclap Stomp | 1–3 | Heavy | 1.8 | Circle 10 studs + ring 10–25 studs 0.6 s later | 0.9 s red circle, then orange ring | 0.3 s + 0.3 s / 1.2 s | ~44% (circle) / ~22% (ring) | Leave the circle, then roll through the ring |
| Stampede Charge | 1–3 | Heavy | 2.0 | Line 80 × 12 studs | 1.2 s red line, three hoof scrapes and trumpet | 1.8 s / 2.0 s (stunned 2 s if it hits an arena ridge) | ~49% | Sidestep; bait it into a ridge |
| Trunk Lightning | 2, 3 | Control | 0.8 | Bolt on the highest-threat target, chains to anyone within 8 studs (16 in puddles), max 5 jumps | 1.0 s purple crackle around the target | instant / 0.8 s | ~20% + 0.5 s stun per hit | Spread out; stay out of puddles |
| Storm Totems | 2, 3 | Adds | — | 3 totems (+1 per 3 extra participants); each charges for 20 s, then strikes a 10-stud circle every 6 s | 1.5 s rising totem; charge bar visible | Each totem has 2% of scaled max HP | Strike ~40% | Destroy totems before they finish charging |
| Sky Splitter | 3 | Ultimate | 2.4 | Arena-wide except gold circles at the 4 cairns | 2.5 s sky flash (reduced-flash alternative), rising thunder | 1.0 s / 3.0 s | ~59% | Stand at a cairn |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Movement:** wanders the salt pan; faces the largest cluster when using Trunk Lightning.
- **Charge targeting:** the player furthest from Thunderhoof within 80 studs; ridge stuns reward baiting.
- **Totem placement:** at least 40 studs apart and 30 studs from the boss, forcing the group to split.
- **Rotation (P3):** Trunk Lightning every 8 s, Sky Splitter every 40 s.
- **Retreat:** at 900 s, it walks into the storm and fades (no rewards).

## 7. Multiplayer scaling

- Max HP: `48,400 × (1 + 0.45 × (N − 1))`: 113,740 (4), 200,860 (8), 375,100 (16, cap).
- Totems: +1 per 3 participants beyond the first.
- Credit: ≥ 2.5% of current scaled max HP; totem damage counts.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 2.2; R3 a fixed-rarity egg (for example Rare or Epic); R4 first-defeat trophy; R5 cosmetic (for example a storm-cloud base banner). Confirmed regardless: +20 PS on first credited defeat; counts toward the Starfall gate.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Great Baobab Waystone; contribution kept while the boss is alive.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Massive grey-blue elephant, cloud-like ears, tusks with glowing cyan veins; distinct from the hatchable [[Elephant]] in scale and storm features ([[Boss Art Direction]]) |
| Animation | Trunk curl before Lash, hoof scrapes before Stampede, rear-up for Thunderclap ([[Animation - Boss Attacks]]) |
| VFX | Chain lightning with clearly visible jump arcs, rain overlay in P3, puddle shimmer ([[VFX - Combat Effects]]) |
| Sound | Trumpeting calls, rolling thunder that rises before Sky Splitter, crackle loops on totems ([[Sound - Bosses]]) |
| Accessibility | Sky Splitter has a non-flashing red vignette alternative |

## 11. Test hooks

- Trunk Lightning chain range doubles in puddles; max 5 jumps.
- Stampede into a ridge → 2 s stun.
- Totem left alive past 20 s begins striking every 6 s.
- 50-minute cadence; overlaps with other world bosses handled without exceeding the 12-boss budget ([[Wild Animal Spawning and Respawn]]).

## Related documents
- [[Boss Design Overview]]
- [[Region - Sunscorch Savanna]]
- [[Boss AI]]
- [[Multiplayer Combat Rules]]
- [[Test Cases - Bosses]]
