---
title: Sound - Ambient World
type: asset-spec
category: audio
status: mixed
priority: P1
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - ambience
  - regions
  - world
---

# Sound - Ambient World

Ambience beds, placed emitters and world event sounds for the hub and the eight regions (SFX-100 to SFX-149). Visual counterparts are in [[VFX - Environment Ambient Effects]]; music is in [[Music Direction]].

> [!warning] UNDECIDED
> The world layout is **UNDECIDED** ([[Open Questions#Q-001]]); regions follow [[Canonical Proposed Values]] §5 (**PROPOSED**).

> [!info] PROPOSED
> All sounds, levels and rules are **PROPOSED**.

---

## 1. How ambience is built

| Layer | Spatial | Priority | Rule |
|---|---|---|---|
| Region bed (stereo loop, ≥ 40 s) | 2D | V5 | Two alternate beds per region, crossfaded every 3–5 minutes; region transitions crossfade over 3 s at region boundaries |
| Placed emitters (waterfalls, vents, surf) | S5 (`Linear`, Min 10, Max 60) | V5 | Max 4 audible at once (Ambience voice limit); nearest wins |
| Random one-shots (gusts, creaks) | 3D at a random point 20–40 studs from the listener | V4 | One every 6–14 s per region |
| Event sounds (spawns, gates, hazards) | S1–S4 | V2–V4 | Per row below |

Beds are high-cut above 10 kHz and kept 12–18 dB below combat so fights stay readable ([[Audio Mixing and Priority]]). No animal calls are baked into beds: creature sounds come only from real animals in the world, so players never hear an animal that is not there.

---

## 2. Register

| ID | Sound | Area | Purpose | Duration | Frequency character | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|---|
| SFX-100 | Hub bed A (gentle breeze, distant chimes) | [[Hub - Hatchling Haven]] | Safe, welcoming | 60 s loop | Warm mids, soft highs | V5 | 2D | In hub | — | — |
| SFX-101 | Hub bed B | Hub | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-102 | Egg shrine hum | Hub | Landmark | 12 s loop | Soft drone 200–800 Hz + shimmer | V5 | S5 | Always | — | Also under roll intro |
| SFX-103 | Fountain | Hub | Spot detail | 20 s loop | Broadband water | V5 | S5 | Always | — | Reused in Canopy pools at −3 dB |
| SFX-104 | Base portal hum | Hub | Landmark, guides players to portals | 8 s loop | 300 Hz–2 kHz whoosh-drone | V5 | S5 | Always | — | — |
| SFX-105 | Whisperwood bed (leaves, light wind) | [[Region - Whisperwood Forest]] | Temperate forest mood | 60 s loop | Broadband rustle | V5 | 2D | In region | — | — |
| SFX-106 | Whisperwood bed alt (stream nearby feel) | Whisperwood | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-107 | Stream | Whisperwood | Spot | 20 s loop | Bubbling water | V5 | S5 | Placed | — | Canopy, Peaks meltwater |
| SFX-108 | Leaf gust | Whisperwood | Life | 1.5–2.5 s | Rustle | V4 | 3D random | Random | 4 | Canopy at −3 semitones |
| SFX-110 | Savanna bed (warm wind, grass) | [[Region - Sunscorch Savanna]] | Open plain | 60 s loop | Airy, light highs | V5 | 2D | In region | — | — |
| SFX-111 | Savanna bed alt | Savanna | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-112 | Dust devil whoosh | Savanna | Spot | 4 s loop | Swirling noise | V4 | S2 | Follows VFX-211 | 2 | — |
| SFX-113 | Hazard warning cue (generic) | All | Gameplay: hazard about to activate | 0.6 s | Rising two-note, 1–3 kHz | **V2** | S2 | With VFX-256 | 1 (consistent meaning) | Shared by all hazards ([[Environmental Hazards]]) |
| SFX-115 | Canopy bed (humid air, drips, distant water) | [[Region - Emerald Canopy]] | Jungle | 60 s loop | Dense mids | V5 | 2D | In region | — | — |
| SFX-116 | Canopy rain bed | Canopy | Weather variant | 60 s loop | Rain hiss, high-cut | V5 | 2D | Weather state | — | — |
| SFX-117 | Waterfall | Canopy | Landmark | 20 s loop | Broadband roar, low-cut | V5 | S5 (Max 80 override) | Placed | — | Peaks, Caldera (cooled pools) |
| SFX-118 | Leaf drips | Canopy | Detail | 0.2 s | Plinks 1–3 kHz | V4 | 3D random | Random | 5 | — |
| SFX-120 | Coast bed (waves, sea air) | [[Region - Coral Coast]] | Shoreline | 60 s loop | Surf wash | V5 | 2D | In region | — | — |
| SFX-121 | Coast bed alt (calmer reef) | Coast | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-122 | Wave break | Coast | Spot | 3 s | Low surge + hiss | V4 | S5 | With VFX-220 | 4 | — |
| SFX-123 | Bubble column | Coast | Spot | 6 s loop | Bubbles 300 Hz–2 kHz | V5 | S5 | Placed | — | Octopus idle layer |
| SFX-125 | Tundra bed (cold wind) | [[Region - Frostfang Tundra]] | Arctic | 60 s loop | Thin highs, low hum | V5 | 2D | In region | — | — |
| SFX-126 | Blizzard bed | Tundra | Weather variant | 60 s loop | Dense wind | V5 | 2D | Weather state | — | — |
| SFX-127 | Ice creak | Tundra | Detail | 1–2 s | 200–800 Hz groan, softened | V4 | 3D random | Random | 4 | — |
| SFX-128 | Wind gust | Tundra, Peaks | Life | 2–3 s | Whoosh | V4 | 3D random | Random | 4 | Peaks at +2 semitones |
| SFX-130 | Peaks bed (high wind, open air) | [[Region - Skyreach Peaks]] | Altitude | 60 s loop | Airy | V5 | 2D | In region | — | — |
| SFX-131 | Peaks bed alt | Peaks | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-132 | Ridge wind | Peaks | Spot | 10 s loop | Whistling 800 Hz–3 kHz | V5 | S5 | Placed | — | — |
| SFX-133 | Hazard active loop (generic bed under any active hazard) | All | Gameplay | 4 s loop | Per hazard: crackle, wind, bubbling | **V3** | S2 | While VFX-257 is active | 1 per hazard type | — |
| SFX-135 | Caldera bed (warm rumble, crackle) | [[Region - Emberheart Caldera]] | Volcanic lost valley | 60 s loop | 60–300 Hz rumble + crackle | V5 | 2D | In region | — | — |
| SFX-136 | Caldera bed alt | Caldera | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-137 | Steam vent burst | Caldera | Spot | 1.5 s | Hiss 2–6 kHz, soft | V4 | S5 | With VFX-236 (every 4 s) | 3 | — |
| SFX-138 | Lava bubble | Caldera | Spot | 0.8 s | Low blorp, gentle | V5 | S5 | Placed | 4 | — |
| SFX-140 | Starfall bed (celestial drone, soft chimes) | [[Region - Starfall Sanctuary]] | Endgame wonder | 60 s loop | Pads, airy highs | V5 | 2D | In region | — | — |
| SFX-141 | Starfall bed alt | Starfall | Variety | 60 s loop | Same | V5 | 2D | Alternate | — | — |
| SFX-142 | Star chime | Starfall | Detail | 1.5 s | Bell 1–6 kHz (pentatonic, never the rarity intervals) | V4 | 3D random | Random | 5 | — |
| SFX-143 | Falling-star whoosh | Starfall | Detail | 1.2 s | Descending whoosh | V4 | 2D, panned | With VFX-242 | 3 | — |
| SFX-145 | Wild spawn poof | All | Feedback | 0.4 s | Soft pop + region texture | V4 | S1 | With VFX-250 | 3 per region texture | — |
| SFX-146 | Rare-spawn beacon | All | Gameplay: Mythical or Secret wild spawn event | 6 s loop | Shimmering drone in the rarity's interval | **V2** | S4 | With VFX-251 and the server announcement | 2 (Mythical, Secret) | — |
| SFX-147 | Region gate unlock | All | Milestone | 2.5 s | Rising chord, stone grind | V2 | 2D for the unlocker; S3 for others | [[Region Unlock Progression]] | 1 | — |
| SFX-148 | Locked gate hum | All | Boundary cue | 6 s loop | Low hum 150–600 Hz | V5 | S5 | Near locked gates | — | — |
| SFX-149 | Water entry splash | All | Feedback | 0.5 s | Splash | V4 | S1 | With VFX-254 | 4 | — |

IDs SFX-109, 114, 119, 124, 129, 134, 139 and 144 are reserved for additional region details found in production.

---

## 3. Rules that protect readability

1. Region beds never contain rising pitch sweeps (the telegraph language, [[Sound Bible]] §6).
2. Star chimes in Starfall Sanctuary use a pentatonic set that never matches the rarity reveal intervals ([[Sound - Eggs]]).
3. Hazard cues SFX-113 and SFX-133 are the same sound everywhere, so the meaning is learnt once.
4. Ambience ducks under all V1 events ([[Audio Mixing and Priority]] §5).

## 4. Mobile considerations

- Beds are the only long assets loaded per region; they are preloaded during the region transition.
- On the Low tier only one bed and two placed emitters play.

## 5. Test hooks

- Walk across every region boundary: bed crossfade 3 s, no gap, no double bed after 10 crossings.
- In Coral Coast, place 10 surf emitters: at most 4 audible.

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[VFX - Environment Ambient Effects]]
- [[World Overview and Map]]
- [[Environmental Hazards]]
- [[Music Direction]]
