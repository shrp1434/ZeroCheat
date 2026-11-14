---
title: Mythical Egg
type: egg
category: eggs
status: mixed
priority: P1
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - egg-type
  - mythical
  - art
---

# Mythical Egg

An ancient rose-marble egg carved with glowing spiral runes, levitating inside a faint shimmering shell while three stone fragments orbit it. It feels old and powerful.

| Property | Value | Status |
|---|---|---|
| Rarity | Mythical (index 5 of 0–6) | **CONFIRMED** tier (D-003) |
| Asset ID | EGG-06 | **PROPOSED** ([[Asset Register]]) |
| Colour key | `#FF4D8D` | **PROPOSED** |
| Baseline roll odds (P = 0.30) | 0.18 % | **PROPOSED** (D-031); final **UNDECIDED** ([[Open Questions#Q-016]]) |
| Expected direct rolls for one (P = 0.30) | 556 | Derived |
| Expected rolls via full merging (P = 0.30) | 60.5 | Derived, see [[Egg Merging#Merge shortcut analysis]] |
| Value in Common-equivalents | 243 | Derived (3^5) |
| Pool size | 6 animals | **PROPOSED** (D-030) |
| Model height | 2.8 studs | **PROPOSED** |

Odds at other progression levels: [[Dynamic Luck Probability Tables]]. Template: [[Template - Egg]].

## Visual appearance

**Silhouette.** Levitating oval (0.5 studs above its rest point) with three orbiting stone fragments. The orbit makes it read as Mythical even in silhouette.

**Surface and detail.** Rose-magenta marble shell with carved spiral runes that glow along their grooves. Three dark stone fragments, each carrying one rune, orbit on tilted paths. A faint shimmering outer shell wraps the egg. Petals and embers drift upward.

**Distinctiveness rule.** Only levitating egg with orbiting fragments, and the only Marble egg. The rune theme supports the ancient lineage proposal ([[Open Questions#Q-027]]) but does not depend on it. Shared egg rules (scale steps, readability at distance, accessibility cues) are in [[Egg Art Direction]] and [[Rarity Visual Language]].

## Colour palette (PROPOSED)

| Element | Hex | Notes |
|---|---|---|
| Shell | `#FF4D8D` | Rarity colour key |
| Rose quartz veins | `#FFB3CC` | Marble veining |
| Runes | `#FF8FB8` | Emissive |
| Stone fragments | `#5B4A52` | Dark stone |
| Deep rose | `#8A1E4A` | Base gradient |

Palette harmonises with the master [[Colour Palette]].

## Materials (PROPOSED)

| Part | Enum.Material | Settings |
|---|---|---|
| Shell | Marble | Tinted rose, Reflectance 0.1 |
| Runes | Neon | Inset in carved grooves |
| Stone fragments | Slate | Three small parts on an orbit attachment |
| Outer shimmer | ForceField | Transparency 0.6, slightly larger than the shell |

Material guidance: [[Material and Texture Direction]].

## Particle effects (PROPOSED)

Idle: 10 petals and embers per second; Trails on the three fragments. Roll settle: rune flare. Hatch: runes ignite in sequence, fragments slam into the shell, petal and ember storm. Budget: ≤ 60 particles plus 3 Trails. Effect specifications live in [[VFX - Rarity and Variant Effects]].

## Sound (PROPOSED)

Low choir pad under a stone grind on each wobble; rune "ignite" tones; choir swell on reveal.

## Rolling animation (PROPOSED)

Snaps to rose; runes trace themselves; fragments break off the shell and begin orbiting; egg lifts into levitation. Settle 2.0 s. Shared roll beats: [[Egg Animations]] and [[Animation - Egg Roll]].

## Hatching animation (PROPOSED)

Fragments orbit faster with each wobble; runes light one by one; fragments strike the shell and it splits along the rune lines; camera push-in and 30° orbit. 3.5 s single. In a multi-hatch (5.0 s), this egg cracks in ascending rarity order with the others. Detail: [[Animation - Egg Hatch]].

## Animal pool and probability table

Baseline in-pool odds = class weight / pool total (Standard 10, Scarce 6, Elusive 3; [[Canonical Proposed Values]] §2 and §7). "Chance per roll" multiplies the 0.18 % egg odds by the in-pool odds. All values **PROPOSED**; final pools **UNDECIDED** ([[Open Questions#Q-018]]).

| Animal | Role | Family | Home region | Pool class | Weight | Baseline in-pool odds | Chance per roll at P = 0.30 |
|---|---|---|---|---|---:|---:|---|
| [[Sabre-Tooth Tiger]] | Assassin | Big Cats | Emberheart Caldera | Standard | 10 | 10 / 45 = 22.222 % | 0.04 % (1 in 2,500) |
| [[Woolly Mammoth]] | Tank | Other Animals | Frostfang Tundra | Standard | 10 | 10 / 45 = 22.222 % | 0.04 % (1 in 2,500) |
| [[Megalodon]] | Bruiser | Aquatic Animals | Starfall Sanctuary | Standard | 10 | 10 / 45 = 22.222 % | 0.04 % (1 in 2,500) |
| [[Haast's Eagle]] | Skirmisher | Birds | Skyreach Peaks | Scarce | 6 | 6 / 45 = 13.333 % | 0.024 % (1 in 4,167) |
| [[Blue Whale]] | Support | Aquatic Animals | Starfall Sanctuary | Scarce | 6 | 6 / 45 = 13.333 % | 0.024 % (1 in 4,167) |
| [[Giant Squid]] | Controller | Aquatic Animals | Starfall Sanctuary | Elusive | 3 | 3 / 45 = 6.667 % | 0.012 % (1 in 8,333) |
| **Total** | | | | 3 Standard + 2 Scarce + 1 Elusive | **45** | **100.000 %** | 0.18 % |

Sum check: the exact in-pool values sum to **100 %** (rounded values may differ in the last decimal).

**Effect of luck on this pool** (per animal, by class; full tables in [[Hatch Pool Tables]]):

| Class | P = 0 | P = 0.30 | P = 1.0 |
|---|---:|---:|---:|
| Standard | 23.641 % | see table | 19.493 % |
| Scarce | 12.057 % | see table | 15.789 % |
| Elusive | 4.965 % | see table | 9.942 % |

## Merge in and out

| Direction | Rule |
|---|---|
| Merge in | 3 × [[Legendary Egg]] → 1 Mythical egg at the Aurora Crucible (station level 4), fee 8,000 Cash (**PROPOSED**). |
| Merge out | 3 × Mythical egg → 1 [[Secret Egg]] at the Celestial Convergence Altar (station level 5), fee 25,000 Cash (**PROPOSED**). |

Rules and balance: [[Egg Merging]] and [[Egg Merging Station]].

## Asset IDs

| ID | Asset | Status |
|---|---|---|
| EGG-06 | Mythical Egg model (shell and attachments) | **PROPOSED** |

Particle, sound and animation IDs (VFX-, SFX-, ANI-) are assigned in the [[Asset Register]].

## Related documents
- [[Eggs and Hatching Index]] · [[Egg Rarity System]] · [[Hatch Pool Tables]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Secret Egg]]
- [[Egg Art Direction]] · [[Egg Animations]] · [[Sound - Eggs]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]]
