---
title: World Boss - Abyssal Leviathan
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - world-boss
  - coral-coast
  - aquatic
---

# World Boss - Abyssal Leviathan

| Field | Value |
|---|---|
| Asset ID | BOS-11 |
| Type | World boss (3 phases) |
| Base animal | Giant whale with bioluminescent markings |
| Location / arena | Leviathan's Maw, [[Region - Coral Coast]] |
| Recommended level | 45 |
| Spawn cadence | Every 55 min per server, announced 2 min ahead (canonical) |
| Lifetime | Retreats after 900 s if undefeated (**PROPOSED**) |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Leviathan's Maw is a deep, perfectly round bay ringed by reef platforms. Every 55 minutes the water darkens, glowing patterns rise from the depths, and a whale larger than any ship surfaces. The Abyssal Leviathan is a boss-only creature, distinct from the hatchable [[Blue Whale]]. Its fight is a **platform fight**: players stand on the reef ring and strike when the Leviathan **rests on the reef** or **breaches**, exposing glowing weak spots. Its lesson: **timing windows and terrain loss**. Platforms flood in phase 3.

## 2. Arena: Leviathan's Maw

- Circular bay, **diameter 160 studs**; the deep centre (100 studs) is boss-only water.
- **Eight reef platforms** (18 × 14 studs) ring the bay, linked by coral bridges (6 studs wide). Two platforms are **high reefs** (6 studs above the rest).
- **Rest windows:** every 20 s the Leviathan surfaces beside a platform (telegraphed by a glowing ring in the water 2 s ahead) and rests its head on the reef for **6 s**, letting melee players and companions hit it at +25% damage.
- **Breach:** in phases 2–3 it leaps across the bay; on landing it floats for 4 s with **four bioluminescent weak spots** exposed (+50% damage).
- Aquatic movement is **UNDECIDED** ([[Open Questions#Q-028]]); aquatic companions use the D-043 **PROPOSED** air-swim and may fight from the water's edge.

## 3. Stats (PROPOSED)

`HP = 200 × 125 × 4.5`, `ATK = 20 × 2.5 × 4.5`, `DEF = 10 × 3.6` (E = 4.5).

| Stat | Value |
|---|---:|
| Max HP (solo) | 112,500 |
| ATK | 225 |
| DEF | 36 |
| Move speed | 18 studs/s in water |
| Lifetime | 900 s |

Target time-to-kill: about 5 min solo with good window use at level 45; 2–3 min for 6 players.

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: The Surfacing | 100–66% | Rest windows, Tail Slap, Bubble Barrage, Tidal Swell | At 66%: 2.5 s; whale song; markings brighten |
| 2: Abyss Song | 66–33% | Breaches, Abyss Song pulls | At 33%: 3.0 s; a maelstrom forms in the centre |
| 3: Maelstrom | 33–0% | Platforms flood one at a time; Leviathan's Dive | — |

### 4.1 Flooding (phase 3)

Every 30 s one low platform floods over 5 s (telegraphed by rising foam), becoming knee-deep water with −25% move speed and no Rest windows beside it. Up to four platforms flood; the two high reefs and two low platforms always remain.

## 5. Attack list

Damage percentages are of a level 45 player's max HP (628 HP, DEF 27); one SkillMultiplier point ≈ 28.2%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Bubble Barrage | 1–3 | Light | 0.9 | 6 circles 5 studs across platforms | 0.7 s orange circles, bubbles rising | 0.3 s / — | ~25% | Step out of circles |
| Tail Slap | 1–3 | Heavy | 1.8 | Line 30 × 10 studs across one platform | 0.9 s red line, tail flukes rise | 0.4 s / 1.0 s | ~51% | Move to the platform's other half |
| Tidal Swell | 1–3 | Signature | 2.1 | Wave across all low platforms | 1.5 s red foam line at the bay edge | 1.0 s / 1.0 s | ~59% + knockback 8 studs | Stand on a high reef (gold decal) or dodge roll through |
| Abyss Song | 2, 3 | Control | 0.4 per s | Arena-wide pull toward the bay centre, 3 studs/s for 4 s | 1.0 s purple ripples, low song | 4.0 s / 1.0 s | ~11% per s if in water | Hold position at a coral anchor (gold post on each platform negates the pull) |
| Breach | 2, 3 | Heavy | 1.9 | Circle 16 studs at the landing point on the water's edge | 1.5 s red circle, water bulges | 0.5 s / 4 s floating (weak spots exposed) | ~54% | Leave the landing circle, then hit weak spots |
| Leviathan's Dive | 3 | Ultimate | 2.4 | Arena-wide except high reefs | 2.5 s whole-bay glow, whale song rises then stops | 1.5 s / 3.0 s | ~68% | Be on a high reef |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Rest choice:** rests beside the platform with the **fewest** players, spreading the group's attention around the ring.
- **Target selection:** Tail Slap targets the platform with the most players; Breach targets the far side of the bay from its current position.
- **Abyss Song** always precedes Tidal Swell by at least 6 s, never overlaps it.
- **Rotation (P3):** flooding every 30 s; Leviathan's Dive every 45 s.
- **Retreat:** at 900 s it sinks into the deep with a final song (no rewards).

## 7. Multiplayer scaling

- Max HP: `112,500 × (1 + 0.45 × (N − 1))`: 264,375 (4), 466,875 (8), 871,875 (16, cap).
- With 9+ participants it rests beside two platforms at once (head and tail), doubling windows.
- Credit: ≥ 2.5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 4.5; R3 a fixed-rarity egg (for example Epic or Legendary); R4 first-defeat trophy; R5 cosmetic (for example a bioluminescent base fountain). Confirmed regardless: +20 PS on first credited defeat; counts toward the Starfall gate.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Lantern Stack Waystone; contribution kept while the boss is alive.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Enormous dark-blue whale with cyan bioluminescent stripes and barnacle clusters; weak spots are bright pulsing patches ([[Boss Art Direction]]) |
| Animation | Slow surfacing roll, head-rest on reef, full-body breach arc ([[Animation - Boss Attacks]]) |
| VFX | Water glow ring before surfacing, foam lines, maelstrom spiral, splash on breach landing ([[VFX - Combat Effects]]) |
| Sound | Whale song as a telegraph language (rising for Abyss Song, silence before Dive), deep water booms ([[Sound - Bosses]]) |
| Performance | The model is the largest in the game; requires LOD meshes and preloading on announcement ([[Animal Scalability and Performance Budgets]]) |

## 11. Test hooks

- Rest windows rotate to the least-populated platform.
- Coral anchors fully negate Abyss Song pull.
- High reefs never flood; at least four platforms always remain.
- Weak spots take +50% damage only during the 4 s float.

## Related documents
- [[Boss Design Overview]]
- [[Region - Coral Coast]]
- [[Boss AI]]
- [[Multiplayer Combat Rules]]
- [[Test Cases - Bosses]]
