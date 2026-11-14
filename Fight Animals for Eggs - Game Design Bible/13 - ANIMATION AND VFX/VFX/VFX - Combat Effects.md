---
title: VFX - Combat Effects
type: asset-spec
category: vfx
status: proposed
priority: P0
owner: VFX Artist
last_updated: 2026-11-14
tags:
  - vfx
  - combat
  - telegraphs
  - abilities
---

# VFX - Combat Effects

Register VFX-001 to VFX-099: hits, player specials, projectiles, ability archetype effects, status effects, defeat and KO effects, boss telegraphs and locomotion effects. Rules, tiers and budgets are in [[VFX Bible]]; damage numbers and hit-confirm UI are in [[Combat Feedback and Readability]].

> [!info] PROPOSED
> All effects, counts and timings are **PROPOSED**. Gameplay sizes (Ground Slam 10 studs, ability radii) come from [[Canonical Proposed Values]] §4 and the [[Animal Abilities Catalogue]]; effects are scaled to them, never the reverse.

Columns: **Rate / burst** is the authored value; the controller clamps it to the tier cap (20 / 40 / 80 per second continuous; 12 / 24 / 48 per burst). **Class** is the priority class from [[VFX Bible]] §3.2.

---

## 1. Hits and player attacks

| ID | Effect | Components | Rate / burst | Lifetime | Attach | Class | Used by |
|---|---|---|---|---|---|---|---|
| VFX-001 | Basic hit spark | Triangular spark burst, white core, attacker-role tint rim | Burst 8 | 0.25 s | Target `A_Chest` | P1 own, P2 others | All basic attacks |
| VFX-002 | Heavy hit burst | Spark burst + ring flash decal | Burst 16 | 0.35 s | Target `A_Chest` | P1 / P2 | Tank hits, finishers, stagger hits |
| VFX-003 | Player hand trail | `Trail` on each hand, white to transparent, `Lifetime` 0.15 | — | 0.15 s | Hand attachments | P1 / P2 | Combo hits 1–2 |
| VFX-004 | Finisher charge and burst | Hand glow emitter (charge), burst + small shockwave ring on contact | Rate 30 charge; burst 20 | 0.4 s | Hands, target | P1 / P2 | Combo hit 3 |
| VFX-005 | Power Strike | Charge: 12-frame growing orb at the fist (rate 40); impact: shockwave ring 4 studs, burst 24, `PointLight` pulse 0.2 s (not on Low) | Rate 40; burst 24 | 0.75 s total | Right hand, target | P1 / P2 | [[Animation - Player Attacks and Specials]] |
| VFX-006 | Ground Slam | Ground ring decal expanding to **exactly 10 studs** over 0.4 s, dust burst, 6–12 low-poly debris chunks (Medium and High only) | Burst 30 dust | 0.8 s | Player `A_Root` equivalent (root, ground level) | P1 / P2 | Ground Slam |
| VFX-007 | Rally Cry | Golden ring pulse from the player reaching each companion, then rising gold motes on each companion for the buff duration (6 s) | Rate 6 per companion | 6 s | Player root; companions `A_Aura` | P1 / P2 | Rally Cry |
| VFX-008 | Dodge Roll | Dust puff at start and end; faint afterimage `Trail` on the torso | Burst 8 ×2 | 0.45 s | Player root and torso | P1 / P2 | Dodge Roll |

---

## 2. Projectiles

| ID | Effect | Components | Rate / burst | Lifetime | Class | Notes |
|---|---|---|---|---|---|---|
| VFX-009 | Basic projectile | Charge stage (small glow at `A_Mouth` or `A_Strike*`), projectile body (low-poly gem, acorn, water bolt, spark orb per species) with a `Trail` | Charge rate 20 | Travel time at 70 studs/s (max 0.4 s for 28 studs) | P1 / P2 | Tint: Ranged white-gold, Support mint, Controller teal. Body model per species is a variant `VFX-009/ANM-0xx` |
| VFX-010 | Projectile impact | Puff + 6 sparks, projectile tint | Burst 10 | 0.3 s | P1 / P2 | |

Projectile visuals are spawned on the client from the `Release` marker and travel along the same line the server uses; if the server reports a hit earlier (target moved into it), the visual snaps to the impact point.

---

## 3. Ability archetype effects

Archetypes are defined in [[Animation - Animal Abilities]]. Each effect is tinted by the ability's element and gains rarity accents ([[VFX - Rarity and Variant Effects]] §5).

| ID | Effect | Components | Rate / burst | Class |
|---|---|---|---|---|
| VFX-011 | Heal pulse | Mint ring decal expanding to the heal radius over 0.4 s, cross-shaped motes | Burst 16 | P1 / P2 |
| VFX-012 | Heal received | 6 mint cross motes rising from `A_Chest` | Burst 6 | P1 / P2 |
| VFX-013 | Buff applied | Gold ring at `A_Aura`, upward motes for 1 s, then a faint persistent rim for the buff duration | Burst 10; rate 3 | P1 / P2 |
| VFX-014 | Stun stars | 3 yellow star parts orbiting `A_Head` (parts, not particles; cheap and readable) | — | **P0** |
| VFX-015 | Zone decal (slow field, trap) | Ground decal at the zone radius, lilac drips at the edge | Rate 8 | **P0** for wild or enemy zones, P1 own |
| VFX-016 | Tether | `Beam` from caster `A_Mouth` to target `A_Chest`, element-textured, snap burst at the end | Burst 6 on snap | P1 / P2 |
| VFX-017 | Guard bubble | Transparent shell mesh with element rim (spikes for Hedgehog, shell sheen for Crab), hit shimmer | Burst 4 per hit | P1 / P2 |
| VFX-018 | Taunt ring | Pulsing ring at the taunt radius, 2 pulses | Burst 0 (decal) | P1 / P2 |
| VFX-019 | Dash streak | `Trail` on `A_Strike*` and body, lifetime 0.25 | — | P1 / P2 |
| VFX-020 | Charge dust trail | Dust emitter at the feet during the charge loop | Rate 30 | P1 / P2 |
| VFX-021 | Cone spray | Directional emitter with `SpreadAngle` matching the cone; element texture (water, frost, wind, spark, petal) | Rate 60 (clamped by tier) | P1 / P2 |
| VFX-022 | Channel beam | `Beam` with scrolling texture, core and rim, impact sparkle at the target | Rate 10 at target | P1 / P2 |
| VFX-023 | Area impact ring | Ring decal sized to the radius, burst at the centre, debris on Medium and High | Burst 20 | P1 / P2 (wild-cast: preceded by VFX-040) |
| VFX-024 | Burrow and submerge | Puff on exit and entry; moving ripple decal while hidden (earth for land, water-ring for air-swimmers) | Burst 10 | **P0** while hidden (opponents must track it) |
| VFX-025 | Landing dust ring | Dust ring at `A_Root` | Burst 12 | P1 / P2 |
| VFX-026 | Call ring | Spawn ring with region-themed swirl | Burst 12 | P1 / P2 |

---

## 4. Targeting, damage, defeat and progression

| ID | Effect | Components | Class | Notes |
|---|---|---|---|---|
| VFX-030 | Target command ring | Ground ring in the player's team colour, shrinks onto the target over 0.25 s; also the manual-ability command ring | **P0** | [[Targeting and Command System]] |
| VFX-031 | Team target indicator | Small chevron above the local team's current target | **P0** | One per local team target |
| VFX-032 | Damage flash | `Highlight` `FillColor` white, `FillTransparency` 0.5 → 1 over 0.1 s; fallback when the Highlight budget is full: brief white `PointLight` (High) or nothing | P1 | One reserve slot for the local player |
| VFX-033 | Wild defeat dissolve | Upward sparkles in the animal's rarity colour, `Emit` from a pooled emitter | P2 | [[Animation - Animal Defeat and Victory]] |
| VFX-034 | KO stars | 4 star parts orbiting over `A_Head`, slower than stun stars, plus a "Zz" sprite | **P0** | KO state |
| VFX-035 | Recover and respawn shimmer | Sparkle column 1 s | P1 | KO recovery, player respawn |
| VFX-036 | Recall swirl | Leaf-or-sparkle swirl at `A_Root` for catch-up teleports | P2 | [[Animation - Animal Locomotion]] |
| VFX-037 | Victory confetti | 20 low-poly confetti pieces; skipped on Low | P3 | Victory poses |
| VFX-038 | Player level-up | Ring + rising rays, 1.2 s | P1 | [[Player Progression and Levelling]] |
| VFX-039 | Cash pickup sparkle | Gold sparkle at the defeated animal, then a screen-space coin stream to the Cash counter | P1 | [[Combat Rewards]] |

---

## 5. Boss and wild telegraphs

All telegraphs are **P0**: exempt from caps, never culled within 200 studs. Fill timing equals the attack's telegraph ([[Animation - Boss Attacks]]).

| ID | Effect | Components | Notes |
|---|---|---|---|
| VFX-040 | Circle telegraph | Flat part with a `SurfaceGui` ring and radial fill in `#FF5A36`, rim darker; fill 0 → 100% over the telegraph | Hatched pattern added in colour-blind mode |
| VFX-041 | Line telegraph | Rectangle decal along the path with a fill sweeping from the caster to the end | Width = hit width |
| VFX-042 | Cone or arc telegraph | Sector decal; fill from the apex outward | Angle = hit angle |
| VFX-043 | Targeted marker | Small circle under a targeted player, fill 1.5 s, static position | Max 8 per client |
| VFX-044 | Safe zone marker | Cool-blue `#7FD3FF` ring with a gentle upward shimmer (rate 6) | Shown with ultimates and quakes |
| VFX-045 | Enrage aura | Red-orange rim emitter on the boss (rate 20), distinct from the telegraph fill by texture (flame-free heat shimmer) | |
| VFX-046 | Phase transition shockwave | Large ring + dust burst; cosmetic push | |
| VFX-047 | Vulnerable sparkle | White-gold sparkles orbiting the boss weak point (rate 12) | Tells players "attack now" |
| VFX-048 | Boss spawn pillar | Tall light pillar visible across the region, 2 min before spawn per the cadence in [[Canonical Proposed Values]] §5 | P0 only for the announcement period |
| VFX-049 | Boss defeat burst | Golden burst, rays, sparkle dissolve over 1 s | |
| VFX-050 | Summon spawn swirl | Region-themed swirl (leaf, sand, ice, ember-spark, starlight) at each helper spawn point during the summon telegraph | |

---

## 6. Locomotion effects

| ID | Effect | Components | Class | Notes |
|---|---|---|---|---|
| VFX-060 | Footstep dust | Small puff at the foot attachment on foot markers; Medium size band and up, A0 only; surface-tinted (grass green-brown, sand, snow, ash) | P3 (own team P1) | [[Animation - Animal Locomotion]] |
| VFX-061 | Air-swim water trail | `Trail` on `A_Tail` (blue-white, lifetime 0.4) + droplet emitter (rate 6) | P3 (own team P1) | D-043 (**PROPOSED**), [[Open Questions#Q-028]] |
| VFX-062 | Wing gust | Dust ring on take-off and landing | P3 | Birds |
| VFX-063 | Slither and slide spray | Dust (serpents) or snow and sand spray (Penguin slide) | P3 | |
| VFX-064 | Air-swim dip splash | Water-ring decal and 8 droplets when an air-swimmer dips | P3 | |

IDs VFX-065 to VFX-099 are reserved.

---

## 7. Worked budget example

A 3-player group fights a world boss on a Medium-tier phone: 3 players × (player + 3 companions) = 12 combatants, plus 4 summoned helpers and the boss.

| Source | Continuous emitters | Beams | Trails | Highlights |
|---|---:|---:|---:|---:|
| Boss telegraphs (P0, decals) | 0 | 0 | 0 | 0 |
| Enrage aura + vulnerable sparkle | 2 | 0 | 0 | 0 |
| Rally Cry motes on 9 companions (others' at half rate) | 9 | 0 | 0 | 0 |
| Two channel beams | 2 | 2 | 0 | 0 |
| Air-swim trails on 2 aquatic companions | 2 | 0 | 2 | 0 |
| Player hand trails (local + 2 others) | 0 | 0 | 6 | 0 |
| Damage flash (local) | 0 | 0 | 0 | 1 |
| Ambient region effects (P3) | 10 | 2 | 0 | 0 |
| **Total** | **25** (cap 50) | **4** (cap 16) | **8** (cap 14) | **1** (cap 8) |

Within budget; if a fourth player joined, P3 ambient effects are halved first.

## 8. Test hooks

- Spawn every combat effect at once on a Low tier device: the controller must clamp all rates and keep frame time under 33 ms ([[Test Cases - Mobile Performance]]).
- Ground Slam ring radius equals 10 studs ±0.25 at full expansion.
- Telegraph fill completes on the damage frame ±1 frame at 30 FPS.

---

## Related documents
- [[VFX Bible]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Animation - Animal Abilities]]
- [[Animation - Player Attacks and Specials]]
- [[Animation - Boss Attacks]]
- [[Combat Feedback and Readability]]
- [[Sound - Combat Impacts]]
