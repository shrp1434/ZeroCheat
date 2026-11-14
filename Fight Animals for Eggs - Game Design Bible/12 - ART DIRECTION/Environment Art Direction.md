---
title: Environment Art Direction
type: art-direction
category: art
status: mixed
priority: P0
owner: Environment Art Director
last_updated: 2026-11-14
tags:
  - art
  - environment
  - regions
  - world
  - performance
---

# Environment Art Direction

How the hub and the eight regions look: shared construction rules, the per-region visual identity (palette, terrain materials, landmarks, prop kits), navigation readability and performance budgets. **Region content (layout, encounters, spawns, unlocks) is owned by each region document and is not repeated here.** World layout itself is **UNDECIDED** ([[Open Questions#Q-001]]); the eight-region structure is **PROPOSED** (D-035).

> [!success] CONFIRMED
> One large shared world for solo and multiplayer play (D-025). Colourful, polished, no horror (D-026).

## 1. Principles

1. **Diorama clarity.** Each region reads as a hand-built set: a clear ground plane, a few big landmark shapes, mid-sized prop clusters and open combat clearings. No visual noise at ground level where animals fight.
2. **Combat clearings first.** Fighting happens in open spaces. Clearings are at least 40 × 40 studs with ground props no taller than 1.5 studs inside them, so the 60-stud leash area ([[Canonical Proposed Values]] §4) stays readable.
3. **Landmarks navigate.** Every region has one **hero landmark** visible from anywhere in the region (minimum 80 studs tall or on high ground) and 3–5 **secondary landmarks**. Players should navigate by landmarks, not the minimap.
4. **Environment sits behind animals.** Environment saturation is ≥ 15% lower than animals in the same view; environment never uses feedback colours from [[Colour Palette]].
5. **Friendly danger.** Hazards ([[Environmental Hazards]]) are visually honest (red-orange chevrons, Neon edges) but never frightening: no skulls, bones, cages, gore or haunted imagery.

## 2. Construction rules

| Topic | Rule (PROPOSED) |
|---|---|
| Ground | Roblox `Terrain` for ground masses, water and cliffs; MeshPart props on top |
| Grid | 4-stud snapping grid for constructed props (fences, bridges, ruins); natural props free-placed |
| Prop scale tiers | Small 0.5–2 studs; Medium 2–8; Large 8–25; Landmark 25+ |
| Prop polycount | Small ≤ 200 tris; Medium ≤ 800; Large ≤ 3,000; Hero landmark ≤ 15,000 (split into ≤ 6 MeshParts) |
| Foliage | Solid low-poly leaf clusters (no alpha cards by default); 3–5 tree variants per region, each with 2 colour swaps from the region atlas |
| Collision | `CollisionFidelity = Box` or `Hull` on props; decorative small props `CanCollide = false`, `CanQuery = false`, `CanTouch = false` |
| Shadows | `CastShadow = false` on small props and ground clutter |
| Streaming | `StreamingEnabled` with landmarks as persistent models where supported (`Model.ModelStreamingMode`), and `Model.LevelOfDetail = StreamingMesh` on hero landmarks so they show at distance (*unverified* behaviour detail) |
| Instance counts | ≤ 9,000 visible parts per region at full detail (PROPOSED); measured in [[M16 - World Design]] |

## 3. Region visual identities

Each row gives the art identity only. Palette hex values are in [[Colour Palette]]; lighting presets in [[Lighting Direction]].

| Region (content owner) | Visual hook | Terrain materials | Hero landmark brief | Signature props | Kit ID |
|---|---|---|---|---|---|
| [[Hub - Hatchling Haven]] | Sunny village square around a giant egg shrine; safe and celebratory | `Grass` (pastel MaterialVariant), `Cobblestone`, `Sandstone`, `Water` | The **Egg Shrine**: a tall sandstone and Marble tower cradling a huge glowing egg whose colour cycles through rarity keys (ENV-016) | Base portals (ENV-017), bunting, blossom trees, hatch pads | ENV-001 |
| [[Region - Whisperwood Forest]] | Warm afternoon woodland, mossy stones, giant friendly mushrooms | `LeafyGrass`, `Grass`, `Ground`, `Mud`, `Rock` | An ancient hollow oak with a glowing canopy, 110 studs | Mushroom clusters (`#F2A65A` caps), log bridges, fern beds, stone circles | ENV-002 |
| [[Region - Sunscorch Savanna]] | Golden-hour grassland, flat-topped trees, red-clay termite towers | `Grass` (gold colour), `Sand`, `Sandstone`, `Salt`, `Ground` | A huge baobab-like tree on a plateau, 95 studs | Acacia-style trees, termite mounds, watering holes, savanna rocks | ENV-003 |
| [[Region - Emerald Canopy]] | Layered jungle, god rays, vines, waterfalls | `LeafyGrass`, `Mud`, `Rock`, `Limestone`, `Water` | A temple-like waterfall cliff overgrown with orchids (no faces carved in stone), 120 studs | Buttress-root trees, hanging vines, giant leaves, stepping stones | ENV-004 |
| [[Region - Coral Coast]] | Bright midday beach, turquoise shallows, coral arches | `Sand`, `Sandstone`, `Rock`, `Water` | A coral arch and lighthouse on a sea stack, 90 studs | Palm clusters, coral heads, tide pools, wooden piers | ENV-005 |
| [[Region - Frostfang Tundra]] | Crisp morning snowfields, blue glaciers, ice caves with light | `Snow`, `Glacier`, `Ice`, `Rock`, `Slate` | A glacier wall with a frozen waterfall, 100 studs | Ice spires, snow-covered pines, igloo-like rocks, aurora arcs in the sky | ENV-006 |
| [[Region - Skyreach Peaks]] | Alpine heights above clouds, wind-swept meadows, rope bridges | `Granite`, `Rock`, `Grass`, `Snow`, `Slate` | The summit spire with a ring of standing stones, 160 studs | Rope bridges (WoodPlanks), plain wind banners in region colours, nests, cloud banks | ENV-007 |
| [[Region - Emberheart Caldera]] | Volcanic lost valley: lush ferns around glowing lava rivers, dusk light | `Basalt`, `CrackedLava`, `Ground`, `LeafyGrass`, `Rock` | A dormant volcano cone with a glowing crown, 150 studs | Giant ferns, basalt columns, lava crack meshes (Neon), geysers | ENV-008 |
| [[Region - Starfall Sanctuary]] | Celestial archipelago: floating islands, crystal trees, star-stone ruins under a bright night sky | `Slate` (star-stone variant), `Marble`, `Glacier` (crystal variant), `Grass` | A floating observatory ring with a falling-star waterfall, 140 studs | Crystal trees (`#8E9BFF` Glass leaves on SmoothPlastic trunks), floating rocks, starlight pools | ENV-009 |

> [!note] Cultural care
> Ruins, banners and shrines use original fictional motifs (eggs, paws, feathers, stars). Do not imitate real religious architecture, sacred symbols or specific real cultures' iconography.

## 4. Shared kits

| Kit ID | Kit | Contents | Notes |
|---|---|---|---|
| ENV-010 | Terrain material set | MaterialVariants and `SetMaterialColor` presets per region | Max 4 MaterialVariants per region ([[Material and Texture Direction]]) |
| ENV-011 | Skybox set | 9 cartoon skyboxes | No photographic skies |
| ENV-012 | Wild spawn dressing | Nests, burrows, dens and water spots that hint at species | Rarer spawn points get more elaborate dressing (Epic+ dens have a rarity-coloured trim stone); spawn rules in [[Wild Animal Spawning and Respawn]] |
| ENV-013 | Region gates | One gate per region border; locked state shows a closed barrier with a requirement icon | Unlock rules in [[Region Unlock Progression]] |
| ENV-014 | Mini-boss arena kit | Circular arena ring, 50–70 studs diameter, boundary posts, spectator-safe edge | Per-boss dressing in [[Boss Art Direction]] |
| ENV-015 | World boss arena and beacon | Large arena dressing and a light-pillar beacon (Beam) visible across the region during the 2-minute announcement ([[Canonical Proposed Values]] §5) | Beacon colour `social.boss` `#FF2E63` core with white outer beam |
| ENV-016 | Hub Egg Shrine | Hero landmark for the hub and egg rolling | Interacts with [[UI - Egg Rolling]] |
| ENV-017 | Base portals | Portal arches from the hub to player bases | One style, owner name plate above |
| ENV-018 | Base plot ground and borders | Plot ground tiles, borders, expansion markers | See [[Base Art Direction]] |
| ENV-019 | Wayfinding kit | Icon signposts, path edging, region-colour banners | Icon-only by default (Q-605) |
| ENV-020 | Hazard markers | Chevron decals, Neon edge strips, warning posts | Colours from [[Colour Palette]] feedback set; hazard rules in [[Environmental Hazards]] |
| ENV-021 | Water and shoreline kit | Shore rocks, foam meshes, reed beds | Used in Whisperwood, Canopy, Coast, Tundra |
| ENV-022 | World edge dressing | Soft boundaries (cliffs, clouds, sea mist) instead of invisible walls | |

## 5. Navigation and readability

| Cue | Treatment (PROPOSED) |
|---|---|
| Main paths | 6–8 studs wide, `Cobblestone` or `Ground` with 1-stud edging stones in the region's light tone |
| Path direction | Lanterns or crystal posts every 24 studs pointing towards the next landmark |
| Progression direction | The gate to the next region is visible from the hero landmark |
| Danger zones | Ground colour shifts towards the hazard palette 10 studs before the hazard begins |
| Interactables | White sparkle `ParticleEmitter` (Rate 2) plus a `ProximityPrompt`; never rely on colour alone |
| Rare spawn areas | Distinct dressing (ENV-012) so players learn "this den might hold something special" without the art implying changed odds; wild encounter rarity is not affected by luck (D-017) |

## 6. Ambient life and effects

Ambient effects (falling leaves, dust motes, snow, embers, star sparkles) are specified in [[VFX - Environment Ambient Effects]] and ambient sound in [[Sound - Ambient World]]. Art constraints:
- Ambient particles never exceed 30% opacity over a combat clearing.
- Ember particles in Emberheart Caldera use orange-to-cream colour sequences, never red-to-black ash (horror tone).
- Weather (snowfall, sand gusts, rain) is visual only unless [[Environmental Hazards]] says otherwise. Whether regions have weather states at all is **UNDECIDED** (Q-606).

## 7. Performance budget per region

| Budget | Value (PROPOSED) |
|---|---:|
| Visible triangles from environment, full detail | ≤ 400,000 |
| Unique MeshPart meshes per region | ≤ 120 |
| Region prop atlas | 1 × 256×256 |
| Hero landmark textures | ≤ 6 × 1,024 SurfaceAppearance sets |
| Dynamic local lights per streaming chunk | ≤ 8 |
| Ambient ParticleEmitters active near player | ≤ 12 |

These figures sit inside the frame-rate targets in [[Canonical Proposed Values]] §15. Profiling and sign-off happen in [[M16 - World Design]] and [[M20 - Optimisation]].

## 8. Review checklist per region

- [ ] Hero landmark visible from 90% of walkable area.
- [ ] Every combat clearing ≥ 40 × 40 studs and free of tall clutter.
- [ ] Lighting preset meets the readability floor ([[Lighting Direction]]).
- [ ] Region palette distinct from neighbours in a thumbnail test (screenshots at 128 px wide).
- [ ] No feedback colours or rarity keys used at full strength on props.
- [ ] Triangle and part budgets met.
- [ ] Tone check: nothing scary, gory, or culturally appropriative.

## Related documents
- [[Art Direction Index]]
- [[World Overview and Map]]
- [[World Design Index]]
- [[Lighting Direction]]
- [[Colour Palette]]
- [[Material and Texture Direction]]
- [[Boss Art Direction]]
- [[Base Art Direction]]
- [[Environmental Hazards]]
- [[VFX - Environment Ambient Effects]]
- [[Asset Register]]
