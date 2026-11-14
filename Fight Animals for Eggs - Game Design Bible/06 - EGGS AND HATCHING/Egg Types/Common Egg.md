---
title: Common Egg
type: egg
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - common
  - art
---

# Common Egg

The everyday egg: a smooth, speckled, slate-grey oval. It is deliberately plain so that every rarer egg reads as an upgrade. About two of every three rolls at baseline produce one.

| Property | Value | Status |
|---|---|---|
| Rarity | Common (index 0 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-01 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#9AA5B1` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 65 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 1.5 | Derived |
| Expected rolls via full merging (P = 0.30) | 1.5 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 1 | Derived (3^0) |
| Pool size | 12 animals | **PROPOSED** (D-030) |
| Model height | 2.0 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Classic smooth oval with no attachments. The plainest silhouette in the set and the reference shape every other egg modifies.

**Surface and detail.** A matte slate-grey shell with irregular cream speckles concentrated towards the top, and one thin darker band a third of the way up. A soft painted-on highlight keeps it friendly rather than dull. No glow, no transparency, no moving parts.

**Distinctiveness rule.** The only egg with no attachments, glow or motion. If a future egg looks this plain, it must be Common. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Shell | `#9AA5B1` | Rarity colour key |
| Speckles | `#E8E1D3` | Warm cream |
| Band | `#6B7682` | Darker slate |
| Shadow tint | `#4A525C` | Painted ambient occlusion at the base |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Shell | SmoothPlastic | Reflectance 0 |
| Band | Plastic | Slight texture contrast with the shell |
| Speckles | SmoothPlastic | Texture or decal on the shell mesh, not separate parts |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: none. Roll settle: a small grey dust puff (8 particles, `#C9CED4`). Hatch: 10 shell chips (mesh particles or small parts with TweenService) plus a dust ring. Budget: ≤ 20 particles total. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Soft wooden knock on each wobble; dry crack; a light "pop" and short two-note chime on reveal. Lowest pitch register of the seven eggs ([[Sound - Eggs]]).

## Rolling animation (PROPOSED)

Rises from the shrine bowl, spins neutral white, snaps to grey with a single small bounce and dust puff. Settle 0.6 s. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Three wobbles of increasing amplitude, a zig-zag crack around the upper third, then the top cap pops off and the animal hops out. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 65 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Rabbit]] | Skirmisher | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Squirrel]] | Ranged | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Hedgehog]] | Tank | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Raccoon]] | Assassin | Forest Animals | Whisperwood Forest | Scarce | 6 | 6 / 98 = 6.122 % | 3.98 % (1 in 25) |
| [[Frog]] | Controller | Other Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Duck]] | Support | Birds | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Woodpecker]] | Skirmisher | Birds | Whisperwood Forest | Elusive | 3 | 3 / 98 = 3.061 % | 1.99 % (1 in 50) |
| [[Boar]] | Bruiser | Forest Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Goat]] | Bruiser | Other Animals | Whisperwood Forest | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Meerkat]] | Support | Safari Animals | Sunscorch Savanna | Scarce | 6 | 6 / 98 = 6.122 % | 3.98 % (1 in 25) |
| [[Zebra]] | Controller | Safari Animals | Sunscorch Savanna | Standard | 10 | 10 / 98 = 10.204 % | 6.633 % (1 in 15) |
| [[Crab]] | Tank | Aquatic Animals | Coral Coast | Elusive | 3 | 3 / 98 = 3.061 % | 1.99 % (1 in 50) |
| **Total** | | | | 8 Standard + 2 Scarce + 2 Elusive | **98** | **100.000 %** | 65 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 10.593 % | see table | 9.398 % |
| Scarce | 5.403 % | see table | 7.613 % |
| Elusive | 2.225 % | see table | 4.793 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | None. Common eggs come only from rolls (and from raids, as stolen eggs). |
| Merge out | 3 × Common egg → 1 [[Uncommon Egg]] at the Twig Nest Press (station level 1), fee 100 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-01 | Common Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
