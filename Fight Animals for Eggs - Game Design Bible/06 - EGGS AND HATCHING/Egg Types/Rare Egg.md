---
title: Rare Egg
type: egg
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - rare
  - art
---

# Rare Egg

A faceted, gem-cut egg in sky blue with water-ripple bands and a clear glass ring at its equator. It is the first egg with transparency and idle motion.

| Property | Value | Status |
|---|---|---|
| Rarity | Rare (index 2 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-03 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#3D8BFF` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 9 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 11.1 | Derived |
| Expected rolls via full merging (P = 0.30) | 4.3 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 9 | Derived (3^2) |
| Pool size | 10 animals | **PROPOSED** (D-030) |
| Model height | 2.2 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Low-poly faceted oval (about 24 flat facets), like a cut stone. The facets catch light and make it read as "crafted" rather than natural.

**Surface and detail.** Sky-blue facets, alternating with lighter ripple bands that suggest water. A clear glass ring circles the equator with tiny bubbles inside. The egg bobs slowly (0.15 studs, 3 s period).

**Distinctiveness rule.** Only faceted egg and the only one with a glass equator ring. First rarity with idle motion. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Facets | `#3D8BFF` | Rarity colour key |
| Ripple bands | `#9CC8FF` | Light sky |
| Deep facets | `#1F4FA8` | Shadow-side facets |
| Highlights | `#EAF4FF` | Specular accents |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Facets | SmoothPlastic | Reflectance 0.15 |
| Equator ring | Glass | Transparency 0.35 |
| Bubbles in ring | SmoothPlastic | Tiny white spheres, Transparency 0.2 |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: 2 rising bubbles per second. Roll settle: bubble sparkle ring. Hatch: water-ring shockwave (expanding Glass torus via TweenService) and a 20-bubble burst. Budget: ≤ 30 particles. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Glass chime on wobble; watery "bloop" crack; reveal arpeggio of three notes ([[Sound - Eggs]]).

## Rolling animation (PROPOSED)

Snaps to blue as facets "click" into place one band at a time (0.3 s), then a bubble ring. Settle 0.8 s. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Facets flash in sequence; the glass ring cracks first, then the shell splits along facet edges into large flat shards; slight camera push-in. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 9 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Wolf]] | Bruiser | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Brown Bear]] | Tank | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Cheetah]] | Skirmisher | Big Cats | Sunscorch Savanna | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Kangaroo]] | Bruiser | Other Animals | Sunscorch Savanna | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Leopard]] | Assassin | Big Cats | Emerald Canopy | Scarce | 6 | 6 / 85 = 7.059 % | 0.6353 % (1 in 157) |
| [[Toucan]] | Ranged | Birds | Emerald Canopy | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Peacock]] | Support | Birds | Emerald Canopy | Scarce | 6 | 6 / 85 = 7.059 % | 0.6353 % (1 in 157) |
| [[Octopus]] | Controller | Aquatic Animals | Coral Coast | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Walrus]] | Tank | Aquatic Animals | Frostfang Tundra | Standard | 10 | 10 / 85 = 11.765 % | 1.059 % (1 in 94) |
| [[Arctic Fox]] | Controller | Other Animals | Frostfang Tundra | Elusive | 3 | 3 / 85 = 3.529 % | 0.3176 % (1 in 315) |
| **Total** | | | | 7 Standard + 2 Scarce + 1 Elusive | **85** | **100.000 %** | 9 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 12.151 % | see table | 10.953 % |
| Scarce | 6.197 % | see table | 8.872 % |
| Elusive | 2.552 % | see table | 5.586 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Uncommon Egg]] → 1 Rare egg at the Twig Nest Press (station level 1), fee 300 Cash (**PROPOSED**). |
| Merge out | 3 × Rare egg → 1 [[Epic Egg]] at the Stonebound Hatchery Forge (station level 2), fee 900 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-03 | Rare Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
