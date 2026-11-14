---
title: Secret Egg
type: egg
category: eggs
status: mixed
priority: P1
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - secret
  - art
---

# Secret Egg

The rarest egg is not a whole egg at all: four night-dark shell segments float apart around a blazing prismatic core, each segment holding a tiny starfield. It must be unmistakable from across the hub.

| Property | Value | Status |
|---|---|---|
| Rarity | Secret (index 6 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-07 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#1B1B2F` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 0.02 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 5,000 | Derived |
| Expected rolls via full merging (P = 0.30) | 175 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 729 | Derived (3^6) |
| Pool size | 4 animals | **PROPOSED** (D-030) |
| Model height | 3.0 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** A split egg: four curved shell segments hovering a short distance from a bright core, slowly drifting apart and back together (6 s cycle). No other egg breaks its outline this way.

**Surface and detail.** Deep night-blue segments, glossy and slightly transparent, with drifting stars inside. Between them a white-hot core cycles slowly through the six lower rarity colours, so the Secret egg literally contains the whole ladder. A faint distortion ring and prismatic shimmer surround it.

**Distinctiveness rule.** Only split-shell egg, the only one with an inner starfield and a colour-cycling core. Its dark key colour makes it the only egg that is darker than its surroundings. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Segments | `#1B1B2F` | Rarity colour key |
| Segment edges | `#2C2C4A` | Lighter night |
| Stars | `#F5F7FF` | Inner starfield |
| Core | `#FFFFFF` | Emissive base |
| Prismatic cycle | `#9AA5B1 → #4CC26A → #3D8BFF → #A55BFF → #FFB020 → #FF4D8D` | Core and seam colour cycle, 12 s loop |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Segments | Glass | Transparency 0.2, Reflectance 0.3 |
| Segment backing | SmoothPlastic | Dark inner layer so stars read |
| Core and seams | Neon | Colour tweened with TweenService |
| Aura | ForceField | Prismatic shimmer shell |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: inner starfield (ParticleEmitter with LockedToPart, 12 per second), Beams linking the segments, 6 orbiting motes in the six lower rarity colours. Roll settle: prismatic flash with a soft screen vignette. Hatch: starfield burst filling the screen edges. Budget: ≤ 80 particles plus 4 Beams; mobile halves the rates. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Sub-bass drone with crystalline shimmer on idle (3D, short roll-off); on hatch, rising layers, then a 0.5 s silence before the reveal hit and choir ([[Sound - Eggs]]).

## Rolling animation (PROPOSED)

Neutral egg freezes mid-spin, then splits into four segments revealing the core; prismatic flash. Settle 3.0 s. Server-wide toast if not opted out. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Segments orbit faster and tighter with each wobble; the core brightens through all six colours; a beat of silence; the segments fly outward and the animal emerges from the core; 90° camera orbit. 3.5 s single, always offered unskipped by default. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 0.02 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Mosasaurus]] | Assassin | Aquatic Animals | Starfall Sanctuary | Standard | 10 | 10 / 29 = 34.483 % | 0.006897 % (1 in 14,500) |
| [[Quetzalcoatlus]] | Ranged | Other Animals | Starfall Sanctuary | Standard | 10 | 10 / 29 = 34.483 % | 0.006897 % (1 in 14,500) |
| [[Titanoboa]] | Controller | Other Animals | Emberheart Caldera | Scarce | 6 | 6 / 29 = 20.690 % | 0.004138 % (1 in 24,167) |
| [[Tyrannosaurus Rex]] | Bruiser | Other Animals | Emberheart Caldera | Elusive | 3 | 3 / 29 = 10.345 % | 0.002069 % (1 in 48,333) |
| **Total** | | | | 2 Standard + 1 Scarce + 1 Elusive | **29** | **100.000 %** | 0.02 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 36.765 % | see table | 30.120 % |
| Scarce | 18.750 % | see table | 24.398 % |
| Elusive | 7.721 % | see table | 15.361 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Mythical Egg]] → 1 Secret egg at the Celestial Convergence Altar (station level 5), fee 25,000 Cash (**PROPOSED**). |
| Merge out | None. Secret is the highest rarity; Secret eggs cannot be merged (**CONFIRMED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-07 | Secret Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
