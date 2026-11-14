---
title: Base Art Direction
type: art-direction
category: art
status: mixed
priority: P0
owner: Environment Art Director
last_updated: 2026-11-14
tags:
  - art
  - base
  - modules
  - egg-merging-station
  - raids
---

# Base Art Direction

The look of player bases: the modular kit, the five-level upgrade ladder, each module's visual identity, the Egg Merging Station's five forms, Plot Expansion stages, and raid-state readability. Gameplay, costs and effects are owned by [[Player Base System]], [[Base Upgrade System]] and the module documents; plot layout by [[Base Layout and Plot Expansion]]. Module availability at launch is **UNDECIDED** ([[Open Questions#Q-007]]).

> [!success] CONFIRMED
> Every player has a modular base with individually upgradeable sections (D-022). The Egg Merging Station must be purchased, must be upgraded for higher rarities, and **physically changes appearance as it is upgraded** (D-020). Bases are protected by shields and physical defences; offline bases cannot be raided (D-024).

## 1. Principles

1. **Upgrades are visible from across the plot.** Each level changes silhouette (height, roof, crest), not just colour. A visitor must be able to tell an L5 module from an L2 at 60 studs.
2. **One identity colour per module.** Used on trims, banners, icons and UI so players learn "orange = Training Grounds" ([[UI Visual Styling]] module icons, UI-016).
3. **Pride without clutter.** Bases show progress (trophies, glowing stations, displayed animals) but keep clear walkways for raids and for the owner's team.
4. **Raid states are unmistakable.** Shield up, shield down and raid in progress each have a distinct, non-threatening look.

## 2. Module identity

| Asset ID | Module | Identity colour | Silhouette idea | Materials L1 → L5 |
|---|---|---|---|---|
| MOD-01 | [[Module - Animal Pens]] | `#7CC26B` leaf | Open paddocks with gates and a shaded shelter | Wood fences → stone walls → metal-trimmed enclosures → crystal water troughs → marble pavilion |
| MOD-02 | [[Module - Egg Vault]] | `#2EC4B6` teal | Rounded vault with egg racks visible through windows | WoodPlanks shed → Slate vault → DiamondPlate door → Glass dome → Marble and Foil treasury |
| MOD-03 | [[Module - Defence Station]] | `#E0604F` brick | Watchtower and barricade line | Wood palisade → Cobblestone walls → Metal turrets → Neon-trimmed emitters → crest-topped bastion |
| MOD-04 | [[Module - Shield Generator]] | `#5BB8FF` sky | Pylon with an orb that projects the ForceField dome | Wood frame with crystal → Slate pylon → Metal coils → Glass orb with Neon rings → floating rings and halo |
| MOD-05 | [[Module - Training Grounds]] | `#FF8A3D` orange | Sparring ring, dummies, weights | Straw dummies → stone ring → metal rigs → glowing target rings → arena with banners |
| MOD-06 | [[Module - Multiplier Shrine]] | `#B67CFF` lavender | Small shrine with a coin-like emblem (original fictional motif) | Wood shrine → stone shrine → Foil emblem → Glass and Neon emblem → floating emblem with light rays |
| MOD-07 | [[Module - Trophy Hall]] | `#E3A33B` bronze | Hall with plinths for 12 boss trophies | Wood hall → stone hall → Foil plinths → Glass cases → Marble hall with skylight |
| MOD-08 | [[Egg Merging Station]] | Per level (§4) | Station with three input sockets and one output cradle | See §4 |
| MOD-09 | Plot Expansion ([[Base Layout and Plot Expansion]]) | `#A3835B` soil | Ground tiles, borders and markers for each of 4 stages | See §5 |

Module footprints are set by [[Base Layout and Plot Expansion]]. Art snaps to a **4-stud grid** (PROPOSED) and keeps a 1-grid walkway margin on every side of each module.

## 3. The upgrade ladder (L1–L5)

Applies to MOD-01 to MOD-07. Costs and effects come from [[Canonical Proposed Values]] §12; this table is visual only.

| Level | Theme name (PROPOSED) | Material family | Silhouette change | Light and effects | Triangle budget per module |
|---:|---|---|---|---|---:|
| L1 | Timber | `Wood`, `WoodPlanks`, `Plastic` | Low, single storey | none | 2,500 |
| L2 | Stone | `Slate`, `Cobblestone`, `Brick` | +25% height, pitched roof or parapet | Identity-colour banners | 4,000 |
| L3 | Reinforced | `Metal`, `DiamondPlate` trims | Adds a tower, chimney or frame element | One small `PointLight` | 5,500 |
| L4 | Crystal | `Glass` panels, `Neon` trims (≤ 10% surface) | Adds a glowing crown element | Neon trims, slow particle accent | 7,000 |
| L5 | Celestial | `Marble`, `Foil` trims, `Neon`, ForceField sparkle | Tallest form with a floating crest | Crest glow, ambient motes (Rate ≤ 4) | 8,500 |

Upgrade transitions are animated (construction dust, scaffolding pop, reveal flash) per [[Animation - Base Upgrades]].

## 4. Egg Merging Station forms (MOD-08)

Names and gates are from [[Canonical Proposed Values]] §10 (**PROPOSED**, [[Open Questions#Q-019]]). The fact that the station changes appearance per upgrade is **CONFIRMED** (D-020).

| Level | Name | Visual brief | Materials | Accent colour | Socket glow per merge tier |
|---:|---|---|---|---|---|
| 1 | Twig Nest Press | A woven twig nest on a wooden press with a hand lever; three straw-lined sockets | `Wood`, `WoodPlanks`, `Grass` (straw) | `#C9A46A` | Common→Uncommon green, Uncommon→Rare blue |
| 2 | Stonebound Hatchery Forge | Stone anvil-forge with a warm coal glow under the cradle; no fire hazard look | `Slate`, `Basalt`, small `CrackedLava` inset, Neon coals | `#FF9F45` | Rare→Epic violet |
| 3 | Crystal Incubator | Glass incubation dome on a crystal base; cool cyan glow | `Glass`, `Ice`, `SmoothPlastic`, Neon cyan strips | `#5CE1FF` | Epic→Legendary gold |
| 4 | Aurora Crucible | Metal crucible with aurora ribbons (`Beam`, green-to-violet) rising above | `Foil`, `Metal`, `Neon` | `#6DF2A8` → `#C77DFF` | Legendary→Mythical rose |
| 5 | Celestial Convergence Altar | Marble altar with three floating rings converging on a star-lit cradle | `Marble`, `Foil`, `Neon`, ForceField halo | Secret prismatic set | Mythical→Secret prismatic |

Rules:
- Each station level is a **separate model**, swapped on upgrade, so every level reads as a new object.
- Sockets that are not yet unlocked at the current level show their target rarity colour at 20% with a lock icon, so players see what an upgrade enables.
- The output cradle is sized for a 3.2-stud Secret egg at every level ([[Egg Art Direction]]).

## 5. Plot Expansion stages (MOD-09)

Four stages ([[Canonical Proposed Values]] §12; costs **PROPOSED**). Visuals:

| Stage | Visual change |
|---:|---|
| 1 | Ground grows from a single grass pad to a bordered plot with stone corner markers |
| 2 | Adds path network and a second terrace; border becomes low stone wall |
| 3 | Adds a raised viewing platform and landscaping (trees, water feature) |
| 4 | Full estate border with tall gateposts and a name arch over the entrance (see note below on colours) |

> [!warning] UNDECIDED
> Whether players can personalise base colours, themes or decorations is **UNDECIDED** (Q-602). Until it is decided, stage 4 gateposts use the default `#A3835B` and module identity colours. No art should assume a personalisation system exists.

Locked expansion areas show a soft fenced boundary with a "build here" marker, not a fog wall.

## 6. Animals at the base

Whether owned animals are physically displayed in pens is **UNDECIDED** ([[Open Questions#Q-008]]). Art supports both options:
- **Display option:** pens show up to N animals with calm idles (N set by [[Animal Scalability and Performance Budgets]]); flyers perch, aquatic animals rest in a pool prop.
- **No-display option:** pens show species icons on plaques and ambient props.

Which animals defend during a raid is **UNDECIDED** ([[Open Questions#Q-033]], [[Open Questions#Q-035]]). Guard posts are modelled as neutral platforms that work for either answer.

## 7. Raid-state readability

Rules from [[Base Raiding System]] and [[Shield Mechanics]]; durations and limits remain **UNDECIDED** ([[Open Questions#Q-012]], [[Open Questions#Q-013]]).

| State | Visual (PROPOSED) |
|---|---|
| Owner offline (cannot be raided, CONFIRMED) | Base shown in a calm "sleeping" state: gate closed, soft blue ForceField shimmer at 85% transparency, moon icon on the portal plate |
| Shield active | ForceField dome `#6FD3FF`, `Material = ForceField`, slow surface ripple; Shield Generator orb bright |
| Shield recharging | Dome absent; generator orb pulses with progress ring |
| Raid in progress | Border posts show `social.raid.raider` `#FF7A2F` on raider-facing side and `social.raid.defender` `#3DA5FF` inside; no red flashing, no alarm lights that strobe faster than 2 Hz |
| Knocked-out defender | Defender lies in a dizzy pose with star swirl ([[Animation - Raid Interactions]]); a ground marker in `#FF7A2F` shows to the raider only when the animal becomes stealable under [[Animal Theft Rules]] |
| Raid over | Shield re-forms per [[Animation - Shield Activation]]; visual damage (scorch-free scuffs) clears within 5 s |

Physical defences (barricades, traps) must read as **toy-like contraptions**: springs, nets, foam bumpers, bubble turrets. No spikes, blades or blood.

## 8. Performance budget per base (PROPOSED)

With up to 16 bases in a server ([[Canonical Proposed Values]] §15):

| Budget | Value |
|---|---:|
| Triangles, fully upgraded base (all modules L5, stage 4) | ≤ 70,000 |
| MeshParts per base | ≤ 900 |
| Dynamic local lights per base | ≤ 3 |
| Particle emitters active per base | ≤ 10 |
| Physical eggs displayed in the Egg Vault | ≤ 14 representative eggs (up to two per rarity present), not one model per stored egg |

Distant bases stream out; each base model uses `Model.LevelOfDetail = StreamingMesh` so a simplified silhouette remains visible at distance (*unverified* behaviour detail).

## Related documents
- [[Art Direction Index]]
- [[Player Base System]]
- [[Base Layout and Plot Expansion]]
- [[Base Upgrade System]]
- [[Base Defence Overview]]
- [[Egg Merging Station]]
- [[Shield Mechanics]]
- [[Animation - Base Upgrades]]
- [[Material and Texture Direction]]
- [[Asset Register]]
