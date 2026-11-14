---
title: Uncommon Egg
type: egg
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - uncommon
  - art
---

# Uncommon Egg

A fresh leaf-green egg with a band of embossed leaves and a two-leaf sprout on top. It signals "something growing": the first step up the ladder.

| Property | Value | Status |
|---|---|---|
| Rarity | Uncommon (index 1 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-02 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#4CC26A` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 22 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 4.5 | Derived |
| Expected rolls via full merging (P = 0.30) | 2.3 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 3 | Derived (3^1) |
| Pool size | 11 animals | **PROPOSED** (D-030) |
| Model height | 2.1 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Oval with a small two-leaf sprout on the crown. The sprout is the first silhouette break in the set.

**Surface and detail.** Glossy leaf-green shell with a raised band of overlapping leaves around the middle and a pale cream belly below the band. The sprout sways gently on idle (a 2.5 s sine rotation of ±8°). No emissive parts.

**Distinctiveness rule.** Only egg with a plant sprout and leaf band. Green alone never identifies it: the sprout does. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Shell | `#4CC26A` | Rarity colour key |
| Leaf band | `#2E8B47` | Deep leaf |
| Sprout | `#8BE07A` | Bright new growth |
| Belly | `#F1F6E4` | Cream |
| Stem | `#7A5A3A` | Small wooden stem |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Shell | SmoothPlastic | Reflectance 0.05 |
| Leaf band | Plastic | Embossed geometry, not a decal |
| Sprout leaves | SmoothPlastic | Two thin wedge parts or one mesh |
| Stem | Wood | Tiny cylinder |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: none (motion comes from the sprout). Roll settle: 6 drifting leaves. Hatch: 12-leaf burst with 6 small green sparkles (`#B8F5A8`). Budget: ≤ 25 particles. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Knock with a leafy rustle layer; a twig-snap crack; reveal chime one step higher than Common.

## Rolling animation (PROPOSED)

Snaps to green; the sprout springs up from flat, followed by a leaf flurry. Settle 0.6 s. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Wobbles shake the sprout; the leaf band splits along its seam; the top half lifts away like a seed husk. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 22 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Fox]] | Assassin | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Owl]] | Controller | Birds | Whisperwood Forest | Scarce | 6 | 6 / 91 = 6.593 % | 1.451 % (1 in 69) |
| [[Deer]] | Support | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Badger]] | Bruiser | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Beaver]] | Tank | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Hyena]] | Skirmisher | Safari Animals | Sunscorch Savanna | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Flamingo]] | Support | Birds | Sunscorch Savanna | Scarce | 6 | 6 / 91 = 6.593 % | 1.451 % (1 in 69) |
| [[Cobra]] | Ranged | Other Animals | Sunscorch Savanna | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Monkey]] | Skirmisher | Other Animals | Emerald Canopy | Standard | 10 | 10 / 91 = 10.989 % | 2.418 % (1 in 41) |
| [[Seal]] | Controller | Aquatic Animals | Coral Coast | Scarce | 6 | 6 / 91 = 6.593 % | 1.451 % (1 in 69) |
| [[Penguin]] | Tank | Birds | Frostfang Tundra | Elusive | 3 | 3 / 91 = 3.297 % | 0.7253 % (1 in 138) |
| **Total** | | | | 7 Standard + 3 Scarce + 1 Elusive | **91** | **100.000 %** | 22 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 11.442 % | see table | 10.060 % |
| Scarce | 5.835 % | see table | 8.149 % |
| Elusive | 2.403 % | see table | 5.131 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Common Egg]] → 1 Uncommon egg at the Twig Nest Press (station level 1), fee 100 Cash (**PROPOSED**). |
| Merge out | 3 × Uncommon egg → 1 [[Rare Egg]] at the Twig Nest Press (station level 1), fee 300 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-02 | Uncommon Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
