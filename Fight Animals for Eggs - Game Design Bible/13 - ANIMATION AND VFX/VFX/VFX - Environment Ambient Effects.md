---
title: VFX - Environment Ambient Effects
type: asset-spec
category: vfx
status: mixed
priority: P1
owner: VFX Artist
last_updated: 2026-11-14
tags:
  - vfx
  - environment
  - ambience
  - regions
  - weather
---

# VFX - Environment Ambient Effects

Register VFX-200 to VFX-299: ambient effects per region and the hub, weather, water, wild spawn and rare-spawn effects, region gates, environmental hazard cues and interactable glints. Rules and budgets are in [[VFX Bible]]; region art in [[Environment Art Direction]] and [[Lighting Direction]].

> [!warning] UNDECIDED
> The world layout is **UNDECIDED** ([[Open Questions#Q-001]]). Region names and themes follow [[Canonical Proposed Values]] §5 (**PROPOSED**). If regions change, this register is re-themed; the budget rules stay.

> [!info] PROPOSED
> All effects and counts are **PROPOSED**.

---

## 1. Ambient budget rules

| Rule | Low | Medium | High |
|---|---:|---:|---:|
| Region ambient continuous emitters active (P3) | 6 | 12 | 20 |
| Camera-following weather emitters | 1 | 1 | 2 |
| Ambient Beams (god-rays, aurora, constellations) | 2 | 4 | 8 |
| Ambient culling distance | 80 studs | 120 studs | 160 studs |

- **Weather follows the camera:** snow, rain, ash and star motes come from one emitter on an invisible part that follows the camera (local space), covering a 60-stud box, instead of emitters placed across the map.
- **Placed emitters** (waterfalls, vents, fountains) are culled by distance and switched off when out of the camera frustum by the VFX controller's 2 Hz visibility pass.
- **Combat first:** when combat effects push the client over budget, P3 ambient effects are halved first, then disabled ([[VFX Bible]] §3.2).
- **No flashes:** no lightning flashes or strobing ambience anywhere (photosensitivity, [[VFX Bible]] §5).

---

## 2. Hub and regions

### 2.1 [[Hub - Hatchling Haven]]

| ID | Effect | Components | Placement |
|---|---|---|---|
| VFX-200 | Floating dandelion motes | Camera-following emitter, rate 6 | Whole hub |
| VFX-201 | Egg shrine fountain sparkle | Placed emitter, rate 8 | Around the egg shrine (shrine itself is VFX-300) |
| VFX-202 | Base portal swirl | Rotating Beam ring + sparkle emitter, rate 10 | Each base portal |

### 2.2 [[Region - Whisperwood Forest]]

| ID | Effect | Components |
|---|---|---|
| VFX-205 | Falling leaves | Camera-following, rate 5, low-poly leaf meshes as flipbook |
| VFX-206 | Fireflies | Placed in glades, rate 4, soft glow, only if [[Lighting Direction]] has dusk or night |
| VFX-207 | Sunbeam shafts | Static Beams through the canopy, 2–4 per glade |
| VFX-208 | Mushroom spore glow | Placed, rate 2 |

### 2.3 [[Region - Sunscorch Savanna]]

| ID | Effect | Components |
|---|---|---|
| VFX-210 | Horizon haze | Scrolling haze texture on distant billboard parts (no screen distortion) |
| VFX-211 | Dust devil | Placed spinning emitter, wanders along a spline, rate 20; cosmetic only |
| VFX-212 | Grass seed drift | Camera-following, rate 4 |

### 2.4 [[Region - Emerald Canopy]]

| ID | Effect | Components |
|---|---|---|
| VFX-215 | Leaf drips | Placed under large leaves, rate 3 |
| VFX-216 | Low mist | Large soft particles near the ground, rate 2, `LightEmission` 0 |
| VFX-217 | Butterflies | Placed, 3–5 mesh flappers per clearing (animated parts, not particles) |
| VFX-218 | Waterfall spray | Placed at waterfall bases, rate 25 (clamped by tier) |

### 2.5 [[Region - Coral Coast]]

| ID | Effect | Components |
|---|---|---|
| VFX-220 | Surf foam | Scrolling foam texture on shoreline strips + burst on wave break, rate 10 |
| VFX-221 | Bubble columns | Placed in reef pools, rate 6 |
| VFX-222 | Caustics | Scrolling caustic decal on shallow seabed parts |
| VFX-223 | Sea spray | Camera-following near the shore only, rate 4 |

### 2.6 [[Region - Frostfang Tundra]]

| ID | Effect | Components |
|---|---|---|
| VFX-225 | Snowfall | Camera-following, rate 20 (Low clamps to 20 anyway) |
| VFX-226 | Wind gusts | Short streak Trails crossing the view every 3–6 s |
| VFX-227 | Aurora | 2–8 sky Beams (tier) with slow texture scroll, colour shift over ≥ 8 s |
| VFX-228 | Ice sparkle | Placed on ice sheets, rate 3 |

### 2.7 [[Region - Skyreach Peaks]]

| ID | Effect | Components |
|---|---|---|
| VFX-230 | Cloud wisps | Large soft particles drifting below cliff edges, rate 2 |
| VFX-231 | Wind streaks | As VFX-226, faster |
| VFX-232 | Ridge snow plumes | Placed on ridgelines, rate 8 |

### 2.8 [[Region - Emberheart Caldera]]

| ID | Effect | Components |
|---|---|---|
| VFX-235 | Rising ember sparks | Camera-following, rate 8, warm orange, small |
| VFX-236 | Steam vents | Placed, periodic burst every 4 s, white steam (never green or toxic-looking) |
| VFX-237 | Lava glow pulse | `PointLight` pulse near lava (counts against light budget; static `SurfaceLight` on Low) |
| VFX-238 | Ash fall | Camera-following, rate 4, light grey |

Ember sparks must not use the boss telegraph hue `#FF5A36`; they are a yellower orange so danger stays unambiguous.

### 2.9 [[Region - Starfall Sanctuary]]

| ID | Effect | Components |
|---|---|---|
| VFX-240 | Floating star motes | Camera-following, rate 8 |
| VFX-241 | Constellation lines | Static sky Beams joining star parts |
| VFX-242 | Falling-star streaks | A streak Trail every 6–12 s across the sky |
| VFX-243 | Island underglow | Neon undersides + slow sparkle emitter per island, rate 3 |

Starfall motes are white-gold and must not resemble the Secret prismatic module, so the endgame region does not dilute the Secret tier's look.

---

## 3. Shared world effects

| ID | Effect | Components | Class | Notes |
|---|---|---|---|---|
| VFX-250 | Wild spawn poof | Region-themed puff (leaves, sand, petals, bubbles, snow, ember-sparks, stars), burst 12 | P2 | Plays as a wild animal respawns ([[Wild Animal Spawning and Respawn]]) |
| VFX-251 | Rare spawn beacon | Tall light column in the rarity colour, visible across the region, for Mythical and Secret wild spawn events | P0 while active | Pairs with the server announcement |
| VFX-252 | Region gate unlock | Barrier dissolves upward in sparkles; burst 40 | P1 | [[Region Unlock Progression]] |
| VFX-253 | Locked gate barrier | Soft shimmer wall with a lock glyph | P0 | Tells players where they cannot go yet |
| VFX-254 | Water entry splash | Splash burst 12 + ring decal | P2 | Players and land animals entering water |
| VFX-255 | Leash reset shimmer | Wild animal returning to its spawn with a soft heal shimmer | P2 | Leash range 60 studs ([[Canonical Proposed Values]] §4) |
| VFX-256 | Hazard warning decal | Ground decal in telegraph hue with a hazard glyph | P0 | [[Environmental Hazards]] |
| VFX-257 | Hazard active effect | Per hazard type: icy sheen, hot ground shimmer, sticky mud bubbles, gust lines | P0 | Gameplay-relevant; never culled within 120 studs |
| VFX-258 | Own base beacon | Faint column over the player's own base plot visible from the hub | P1 | Navigation aid |
| VFX-259 | Interactable glint | Small sparkle every 3 s on objects with a `ProximityPrompt` (shrine, station, vault) | P1 | Off while the prompt is visible |

IDs VFX-260 to VFX-299 are reserved.

---

## 4. Test hooks

- Each region on a Low tier phone with 8 players and 40 wild animals: ambient P3 emitters ≤ 6; frame time under 33 ms ([[Test Cases - Mobile Performance]]).
- Emberheart Caldera colour check: no ambient effect within ΔE 10 of the telegraph hue.
- Weather emitter follows the camera through a 100-stud teleport without a visible gap longer than 0.5 s.

---

## Related documents
- [[VFX Bible]]
- [[Environment Art Direction]]
- [[Lighting Direction]]
- [[World Overview and Map]]
- [[Environmental Hazards]]
- [[Wild Animal Spawning and Respawn]]
- [[Sound - Ambient World]]
