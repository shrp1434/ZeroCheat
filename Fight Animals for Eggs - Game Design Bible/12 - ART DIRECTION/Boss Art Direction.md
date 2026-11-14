---
title: Boss Art Direction
type: art-direction
category: art
status: mixed
priority: P1
owner: Character Art Director
last_updated: 2026-11-14
tags:
  - art
  - bosses
  - telegraphs
  - modelling
  - readability
---

# Boss Art Direction

Visual rules for the 8 mini-bosses and 4 world bosses (BOS-01 to BOS-12): scale, silhouette, materials, phase visuals, telegraph language and budgets. Each boss's species, mechanics, phases and lore are owned by its boss document and by [[Boss Design Overview]] and [[Boss AI]]. Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]).

> [!success] CONFIRMED
> Mini-bosses and world bosses exist (D-012). No horror (D-026).

## 1. Principles

1. **Big, proud, readable.** Bosses are larger, more ornamented versions of the game's animal style, never monsters. They keep friendly-style eyes with highlights; aggression is shown with brows, posture and armour, not with gore or glowing red eyes.
2. **A boss is a landmark.** A world boss must be recognisable as a silhouette from 150 studs; a mini-boss from 80 studs.
3. **The region is in the boss.** Each boss borrows its region's palette and materials ([[Environment Art Direction]]) and adds one region-element feature (bark, dust, vines, tide, frost, storm, embers, starlight).
4. **Telegraphs beat spectacle.** Boss attack telegraphs follow the [[Colour Palette]] feedback colours and are always more visible than the boss's own ambient effects.

## 2. Scale and budgets (PROPOSED)

| Class | Longest axis (studs) | Triangles (all parts) | MeshParts | Texture set | Persistent particles |
|---|---:|---:|---:|---|---:|
| Mini-boss | 10–16 | 12,000 | ≤ 10 | SurfaceAppearance 1,024 (Color, Normal, Roughness) | ≤ 40 |
| World boss | 30–60 | 30,000 | ≤ 16 | 2 × 1,024 sets | ≤ 80 |

Bosses use `CollisionFidelity = Box` on visual parts; hit volumes and weak-point parts are defined by [[Boss AI]] and [[Animal Rig Standards]].

## 3. Phase visuals

Phase thresholds and behaviours belong to [[Boss AI]]; art provides a standard set of visual states:

| State | Visual (PROPOSED) |
|---|---|
| Idle / patrol | Base look; slow region-element ambient (falling leaves, dust, frost) |
| Engaged | Accent Neon parts brighten from 0% to 60% emission look; nameplate crown appears |
| Phase 2 | Armour or feature change: an accent part swaps (for example, bark plates open to reveal glowing sap lines); Neon accents to 100% |
| Enraged / final phase (if used) | Colour temperature shifts warmer on accents; added orbiting particles; **no** red full-body tint |
| Invulnerable window (if used) | `ForceField` material shell part fades in; clearly "can't hurt now" |
| Staggered / weak point open | Weak-point part pulses `#FFF35C` (same as manual target colour, signalling "hit here") |
| Defeated | Dizzy-star swirl and sit or lie down, then fades with sparkles. No death animation with bodies left behind ([[Animation - Boss Attacks]]) |

## 4. Telegraph language

| Telegraph | Shape | Colour | Timing cue |
|---|---|---|---|
| Light attack area | Circle or cone ground decal | Fill `#FF4B3E` 65% transparent, edge opaque | Edge fills inward over the wind-up |
| Heavy attack | Same shape, double edge | Edge `#FF2E63`, inner pulse `#FFD23F` | Two pulses, then strike |
| Line / charge | Long rectangle decal + arrow chevrons | `#FF4B3E` | Chevrons move towards the end point |
| Summon or add spawn | Small circles at spawn points | `#FFD23F` | Ring shrinks to centre |
| Safe zone | Circle | `#3DD6FF` with white edge | Static while active |

Telegraph decals must stay visible over every region's ground; checked against the readability floor in [[Lighting Direction]]. Wind-up durations are design values in [[Boss AI]].

## 5. Boss briefs

Species and mechanics are taken from each boss document. For mini-bosses, this table gives only the **art hook implied by the name and region**; if the boss document specifies otherwise, it wins.

| ID | Boss | Region | Art hook | Palette anchors | Key materials |
|---|---|---|---|---|---|
| BOS-01 | [[Mini-Boss - Bramblehorn]] | [[Region - Whisperwood Forest\|Whisperwood Forest]] | Large antlers or horns grown through with friendly bramble vines and blossoms | `#7A5A3C`, `#5FAF4E`, accent `#F2A65A` | SmoothPlastic, Wood accents, Neon blossom cores |
| BOS-02 | [[Mini-Boss - Dustmane]] | [[Region - Sunscorch Savanna\|Sunscorch Savanna]] | Huge flowing mane that sheds golden dust swirls | `#D9A35F`, `#D8C26A`, accent `#C2553A` | SmoothPlastic, Sand-tinted SurfaceAppearance, dust particles |
| BOS-03 | [[Mini-Boss - Vinecoil]] | [[Region - Emerald Canopy\|Emerald Canopy]] | Long coiling body wrapped in vines and orchid blooms | `#2FA86A`, `#4E3B2A`, accent `#FF7A3D` | SmoothPlastic, LeafyGrass-tinted accents |
| BOS-04 | [[Mini-Boss - Hammertide]] | [[Region - Coral Coast\|Coral Coast]] | Broad hammer-shaped head mass with coral crust and tidal water arcs | `#3FC6D9`, `#F2E2B8`, accent `#FF7F6B` | SmoothPlastic, coral accent parts, water-trail VFX |
| BOS-05 | [[Mini-Boss - Rimeback]] | [[Region - Frostfang Tundra\|Frostfang Tundra]] | Back covered in rime-ice plates and icicle ridges | `#EEF4FA`, `#9CC9E8`, accent `#4FB0C6` | SmoothPlastic, Ice and Glass plates |
| BOS-06 | [[Mini-Boss - Stormtalon]] | [[Region - Skyreach Peaks\|Skyreach Peaks]] | Oversized talons and wings trailing small storm clouds and light arcs | `#8A8F9E`, `#F4F1E8`, accent `#5CE1FF` | SmoothPlastic, Neon lightning strips, cloud particles |
| BOS-07 | [[Mini-Boss - Cinderjaw]] | [[Region - Emberheart Caldera\|Emberheart Caldera]] | Heavy jaw with basalt armour and glowing ember seams (warm orange, not blood red) | `#3E3433`, `#6B8F3A`, accent `#FF8A2B` | Basalt-look SurfaceAppearance, Neon seams |
| BOS-08 | [[Mini-Boss - Eclipse Panther]] | [[Region - Starfall Sanctuary\|Starfall Sanctuary]] | Sleek panther with a crescent-moon crest and a star-speckled coat; the "eclipse" is a halo ring | `#3B3F7A`, `#8E9BFF`, accent `#FFE38A` | SmoothPlastic, Neon halo, star particles |
| BOS-09 | [[World Boss - Ironbark Colossus]] | Whisperwood–Savanna border | Ancient tortoise carrying a living forest on its shell (trees, a waterfall, birds' nests) | `#7A5A3C`, `#5FAF4E`, shell `#8A6E4E` | Wood, LeafyGrass-tinted, Rock |
| BOS-10 | [[World Boss - Thunderhoof]] | Sunscorch Savanna | Colossal storm elephant; storm clouds around the ears, lightning-patterned tusks | `#8F95A8`, `#F4D9A6`, accent `#5CE1FF` | SmoothPlastic, Neon lightning, cloud VFX |
| BOS-11 | [[World Boss - Abyssal Leviathan]] | Coral Coast | Giant whale with bioluminescent spots and barnacle-coral clusters; "abyssal" shown with deep blues, not darkness or dread | `#1F4E7A`, `#3FC6D9`, glow `#7DF9FF` | SmoothPlastic, Neon spots, water-trail VFX |
| BOS-12 | [[World Boss - Ashwing Condor]] | Emberheart Caldera / Skyreach Peaks rim | Giant condor with ember-tipped feathers and a heat-shimmer trail | `#3E3433`, `#F4F1E8`, accent `#FF8A2B` | SmoothPlastic, Neon feather tips, ember particles |

Base animals for BOS-09 to BOS-12 are from [[Canonical Proposed Values]] §5. Each boss must pass a silhouette test against the companion animal it most resembles (for example Thunderhoof against [[Elephant]] and [[Woolly Mammoth]]) so that no boss looks like a scaled-up companion.

## 6. Announcements and arenas

- World boss announcements (2 minutes ahead, [[Canonical Proposed Values]] §5) use the ENV-015 light-pillar beacon and a server banner styled per [[UI - Notifications]].
- Mini-boss arenas use ENV-014 with boss-specific dressing (bramble thickets, dust rings, vine walls, tide pools, ice ridges, cloud platforms, basalt columns, star circles).
- Boss health bars are styled in [[UI Visual Styling]] and specified in [[UI - Boss Health Bar]].

## 7. Trophies

Each boss has a trophy model for the Trophy Hall (MOD-07, [[Module - Trophy Hall]]): a 2–3 stud stylised statuette of the boss on a plinth in the boss's accent colour, ≤ 1,500 triangles, shared plinth mesh. Trophies are cosmetic representations; their cash bonus is in [[Canonical Proposed Values]] §12.

## Related documents
- [[Art Direction Index]]
- [[Boss Design Overview]]
- [[Boss AI]]
- [[Animation - Boss Attacks]]
- [[Sound - Bosses]]
- [[Environment Art Direction]]
- [[Colour Palette]]
- [[Lighting Direction]]
- [[Asset Register]]
- [[Visual Reference Placeholders]]
