---
title: Epic Egg
type: egg
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - epic
  - art
---

# Epic Egg

A violet egg breaking out in crystals: five glassy shards jut from the shell and a network of glowing cracks runs between them. The first egg that emits light.

| Property | Value | Status |
|---|---|---|
| Rarity | Epic (index 3 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-04 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#A55BFF` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 3 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 33.3 | Derived |
| Expected rolls via full merging (P = 0.30) | 9.2 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 27 | Derived (3^3) |
| Pool size | 9 animals | **PROPOSED** (D-030) |
| Model height | 2.4 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Oval with five crystal shards of different lengths protruding at angles from the upper half, plus one small crystal orbiting it.

**Surface and detail.** Deep violet shell veined with thin luminous cracks. Pale lilac crystal shards emerge from the cracks. A thumb-sized crystal orbits the egg every 4 s. The egg bobs and occasionally pulses its cracks (every 3 s).

**Distinctiveness rule.** Only egg with protruding crystals and the first with Neon. Purple alone never identifies it: the crystals do. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Shell | `#A55BFF` | Rarity colour key |
| Crystal shards | `#D9B8FF` | Pale lilac |
| Glowing cracks | `#E7C6FF` | Emissive |
| Deep shell | `#5A2A9E` | Lower shell gradient |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Shell | SmoothPlastic | Reflectance 0.1 |
| Crystal shards | Glass | Transparency 0.15, Reflectance 0.2 |
| Cracks | Neon | Thin inset parts or mesh, first Neon use in the set |
| Orbiting crystal | Glass | Same as shards |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: 4 violet sparks per second around the shards. Roll settle: violet spark ring. Hatch: crystal shatter (shard particles), a brief violet Highlight outline flash on the animal. Budget: ≤ 40 particles. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Crystal ring on wobble; resonant hum rising under the crack; shatter with a sustained crystalline tail on reveal.

## Rolling animation (PROPOSED)

Snaps to violet; shards grow out of the shell (0.4 s scale tween); orbiting crystal launches. Settle 1.0 s. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Cracks brighten with each wobble; shards shatter outward one by one; the shell falls away in violet light; camera push-in. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 3 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Tiger]] | Assassin | Big Cats | Emerald Canopy | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Gorilla]] | Tank | Other Animals | Emerald Canopy | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Crocodile]] | Controller | Aquatic Animals | Emerald Canopy | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Rhino]] | Bruiser | Safari Animals | Sunscorch Savanna | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Hippo]] | Tank | Safari Animals | Sunscorch Savanna | Scarce | 6 | 6 / 75 = 8.000 % | 0.24 % (1 in 417) |
| [[Golden Eagle]] | Skirmisher | Birds | Skyreach Peaks | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Dolphin]] | Support | Aquatic Animals | Coral Coast | Standard | 10 | 10 / 75 = 13.333 % | 0.4 % (1 in 250) |
| [[Electric Eel]] | Ranged | Aquatic Animals | Emerald Canopy | Scarce | 6 | 6 / 75 = 8.000 % | 0.24 % (1 in 417) |
| [[Snow Leopard]] | Controller | Big Cats | Skyreach Peaks | Elusive | 3 | 3 / 75 = 4.000 % | 0.12 % (1 in 833) |
| **Total** | | | | 6 Standard + 2 Scarce + 1 Elusive | **75** | **100.000 %** | 3 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 13.831 % | see table | 12.300 % |
| Scarce | 7.054 % | see table | 9.963 % |
| Elusive | 2.905 % | see table | 6.273 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Rare Egg]] → 1 Epic egg at the Stonebound Hatchery Forge (station level 2), fee 900 Cash (**PROPOSED**). |
| Merge out | 3 × Epic egg → 1 [[Legendary Egg]] at the Crystal Incubator (station level 3), fee 2,700 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-04 | Epic Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
