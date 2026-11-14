---
title: Legendary Egg
type: egg
category: eggs
status: mixed
priority: P1
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - legendary
  - art
---

# Legendary Egg

A regal gold egg wrapped in gilded filigree, crowned with six short spikes and topped by a rotating halo of light. It should feel like a trophy.

| Property | Value | Status |
|---|---|---|
| Rarity | Legendary (index 4 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-05 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#FFB020` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 0.8 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 125 | Derived |
| Expected rolls via full merging (P = 0.30) | 22.6 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 81 | Derived (3^4) |
| Pool size | 8 animals | **PROPOSED** (D-030) |
| Model height | 2.6 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Oval with a six-point crown on top and a floating halo ring above the crown. Taller than the lower eggs.

**Surface and detail.** Warm gold shell with raised gilded filigree bands in a sunburst pattern. A short crown sits on top, and a thin glowing halo rotates slowly above it. Two faint light rays sweep slowly around the egg like a lighthouse.

**Distinctiveness rule.** Only egg with a crown and halo, and the only one using Foil. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Shell | `#FFB020` | Rarity colour key |
| Gilt filigree | `#FFD66B` | Bright gold |
| Deep amber | `#B86E00` | Recesses |
| Halo | `#FFF1B3` | Emissive |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Shell | SmoothPlastic | Reflectance 0.15 |
| Filigree and crown | Foil | Metallic highlight |
| Halo | Neon | Thin torus, rotates 1 turn per 6 s |
| Crown tips | Metal | Small contrasting points |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: 8 glitter motes per second; two Beam rays rotating. Roll settle: golden ray burst. Hatch: sunburst (radial Beams), glitter fountain, warm light flash. No coin imagery (avoids gambling associations). Budget: ≤ 50 particles plus 2 Beams. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Bell-like knock; brass swell under the crack; full fanfare chord on reveal ([[Sound - Eggs]]).

## Rolling animation (PROPOSED)

Snaps to gold; filigree draws itself across the shell (0.5 s); crown rises; halo ignites. Settle 1.5 s with a 0.5 s hold in bulk rolls. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Halo spins faster with each wobble; filigree glows; the shell opens like petals from the crown downward; sunburst; small camera shake. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 0.8 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Lion]] | Bruiser | Big Cats | Sunscorch Savanna | Standard | 10 | 10 / 65 = 15.385 % | 0.1231 % (1 in 812) |
| [[Elephant]] | Tank | Safari Animals | Sunscorch Savanna | Standard | 10 | 10 / 65 = 15.385 % | 0.1231 % (1 in 812) |
| [[Great White Shark]] | Assassin | Aquatic Animals | Coral Coast | Standard | 10 | 10 / 65 = 15.385 % | 0.1231 % (1 in 812) |
| [[Orca]] | Controller | Aquatic Animals | Frostfang Tundra | Standard | 10 | 10 / 65 = 15.385 % | 0.1231 % (1 in 812) |
| [[Narwhal]] | Ranged | Aquatic Animals | Frostfang Tundra | Scarce | 6 | 6 / 65 = 9.231 % | 0.07385 % (1 in 1,354) |
| [[Peregrine Falcon]] | Skirmisher | Birds | Skyreach Peaks | Standard | 10 | 10 / 65 = 15.385 % | 0.1231 % (1 in 812) |
| [[Giant Panda]] | Support | Other Animals | Skyreach Peaks | Scarce | 6 | 6 / 65 = 9.231 % | 0.07385 % (1 in 1,354) |
| [[Komodo Dragon]] | Controller | Other Animals | Emberheart Caldera | Elusive | 3 | 3 / 65 = 4.615 % | 0.03692 % (1 in 2,708) |
| **Total** | | | | 5 Standard + 2 Scarce + 1 Elusive | **65** | **100.000 %** | 0.8 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 16.051 % | see table | 14.025 % |
| Scarce | 8.186 % | see table | 11.360 % |
| Elusive | 3.371 % | see table | 7.153 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Epic Egg]] → 1 Legendary egg at the Crystal Incubator (station level 3), fee 2,700 Cash (**PROPOSED**). |
| Merge out | 3 × Legendary egg → 1 [[Mythical Egg]] at the Aurora Crucible (station level 4), fee 8,000 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-05 | Legendary Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
