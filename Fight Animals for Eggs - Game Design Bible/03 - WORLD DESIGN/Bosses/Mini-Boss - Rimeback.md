---
title: Mini-Boss - Rimeback
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - frostfang-tundra
---

# Mini-Boss - Rimeback

| Field | Value |
|---|---|
| Asset ID | BOS-05 |
| Type | Mini-boss (2 phases) |
| Base animal | Giant polar bear whose back is armoured with glacier ice |
| Region / arena | [[Region - Frostfang Tundra]] / Glacier Maw |
| Recommended level | 48–54 |
| Gate role | Key for [[Region - Skyreach Peaks]] (with level 52) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Rimeback has slept in the Glacier Maw so long that the glacier grew onto it. Its back is a ridge of blue ice crystals that thicken into full armour when it is threatened. Its lesson: **focus fire**. In phase 2 Rimeback raises Rime Armour, and the fight stalls unless the player directs all three animals at the glowing rime plates with target commands ([[Targeting and Command System]]).

## 2. Arena: Glacier Maw

- Ice cavern, **70-stud radius**, translucent blue walls lit from outside.
- **Five ice pillars** at 30–45 studs from centre. During Glacial Collapse, the space directly under each pillar's overhang is safe.
- Icicles hang from the ceiling over marked zones; their shadows show where Icicle Drop lands.
- The floor is packed snow (no Thin Ice inside the arena).

## 3. Stats (PROPOSED)

`HP = 200 × 40 × 4.5`, `ATK = 20 × 2.3 × 4.5`, `DEF = 10 × 3.8`.

| Stat | Value |
|---|---:|
| Max HP (solo) | 36,000 |
| ATK | 207 |
| DEF | 38 (×2 = 76 while Rime Armour is up) |
| Move speed | 15 studs/s |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Sleeper Wakes | 100–50% | Claw combos, Ice Slam, Frost Breath, Icicle Drop | At 50%: 2.5 s; Rimeback rears and roars; ice spreads over its body |
| 2: Rime Armour | 50–0% | Armour cycles, Glacial Collapse | — |

### 4.1 Rime Armour cycle (phase 2)

1. Rimeback raises armour: DEF doubles; **4 rime plates** glow (shoulders, back, flank, hip). Each plate has HP equal to **3% of current scaled max HP** and takes normal damage.
2. Breaking all 4 plates shatters the armour: Rimeback is **stunned 4 s** and takes **+30% damage for 8 s**.
3. If plates are not broken within 25 s, the armour cracks off by itself with no stun or bonus, and Rimeback uses Glacial Collapse immediately.
4. Armour returns 20 s after it falls.

## 5. Attack list

Damage percentages are of a level 52 player's max HP (712 HP, DEF 30.5); one SkillMultiplier point ≈ 22.3%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Claw Combo | 1, 2 | Light | 0.8 ×2 | Cone 90°, 9 studs, two hits | 0.5 s orange cone, paws raise | 0.6 s / 0.6 s | ~18% per hit | Dodge after the first hit or step behind |
| Ice Slam | 1, 2 | Heavy | 1.9 | Circle 12 studs on self | 0.9 s red circle, rears onto hind legs | 0.3 s / 1.4 s | ~42% | Leave the circle; punish during recovery |
| Frost Breath | 1, 2 | Control | 0.6 per s for 2.5 s | Cone 45°, 20 studs | 1.0 s purple cone, frosty inhale | 2.5 s / 0.8 s | ~13% per s + Chilled (−30% attack speed 6 s) | Move out of the cone sideways |
| Icicle Drop | 1, 2 | Heavy | 1.8 | 4–6 circles 5 studs under marked icicles | 1.2 s red circles + icicle shadows | 0.2 s / — | ~40% | Watch the ceiling shadows |
| Rime Armour | 2 | Mechanic | — | Self | 1.5 s ice spreading, plates glow | 25 s window | DEF ×2 | Command all animals onto plates |
| Glacial Collapse | 2 | Ultimate | 2.4 | Arena-wide except under pillar overhangs | 2.5 s red cavern-wide glow, ceiling cracks | 1.0 s / 2.0 s | ~54% | Shelter under a pillar (gold decal) |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Target selection:** highest threat; Frost Breath prefers the largest cluster of companions.
- **Armour behaviour:** while armoured, Rimeback turns to keep its plated side away from the highest-threat target, so the group must spread or the player must reposition to expose plates.
- **Rotation (P2):** armour on a 20 s cooldown after it falls; Glacial Collapse every 35 s or immediately after an unbroken armour cycle.
- **Reset:** arena empty 10 s → full HP, armour cleared.

## 7. Multiplayer scaling

- Max HP: 36,000 solo; 50,400 (2); 79,200 (4); 136,800 (8, cap).
- Plates scale with max HP (3% each), so large groups do not trivialise the armour.
- With 5+ participants, a fifth plate appears (on the chest).
- Credit: ≥ 5% of current scaled max HP; plate damage counts.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 4.5; R3 a fixed-rarity egg (for example Epic); R4 first-defeat trophy; R5 cosmetic (for example a rime-crystal base decoration). Confirmed regardless: Skyreach gate key, +10 PS.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Aurora Stones Waystone; contribution kept until reset.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Massive white bear with a crystalline blue ice ridge; armour state adds plate meshes with emissive cores ([[Boss Art Direction]]) |
| Animation | Rear-up for Ice Slam, inhale for Frost Breath, heavy stagger loop when armour shatters ([[Animation - Boss Attacks]]) |
| VFX | Frost cone with clear edge, plate glow, shatter burst with ice shards, falling ice preview shadows ([[VFX - Combat Effects]]) |
| Sound | Deep huff idle, ice-crack cues for each plate, cavern rumble before Collapse ([[Sound - Bosses]]) |
| UI | Plate HP pips under the boss bar during the armour cycle ([[UI - Boss Health Bar]]) |

## 11. Test hooks

- Break 4 plates within 25 s → 4 s stun, +30% damage taken for 8 s.
- Fail to break → armour cracks off, Glacial Collapse follows.
- Plate HP equals 3% of scaled max HP for 1, 4 and 8 participants.
- Players under pillar overhangs take no Collapse damage.

## Related documents
- [[Boss Design Overview]]
- [[Region - Frostfang Tundra]]
- [[Targeting and Command System]]
- [[Boss AI]]
- [[Test Cases - Bosses]]
