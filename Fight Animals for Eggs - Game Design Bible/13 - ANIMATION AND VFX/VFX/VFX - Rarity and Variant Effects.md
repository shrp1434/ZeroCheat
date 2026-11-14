---
title: VFX - Rarity and Variant Effects
type: asset-spec
category: vfx
status: mixed
priority: P0
owner: VFX Artist
last_updated: 2026-11-14
tags:
  - vfx
  - rarity
  - variants
  - ascension
  - eggs
---

# VFX - Rarity and Variant Effects

Register VFX-100 to VFX-199: per-rarity escalation for eggs, roll reveals, hatch reveals, companion markers and ability accents; ascension visual tiers; variant effects; and the shared prismatic module. The visual language this implements is defined in [[Rarity Visual Language]] and [[Variant Visual Treatments]]; rules and budgets are in [[VFX Bible]].

> [!success] CONFIRMED
> Seven rarities in order: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret (D-003). Special variants exist, for example Golden, Diamond, Rainbow, Shadow and Neon (D-028).

> [!warning] UNDECIDED
> Variant acquisition is **UNDECIDED** ([[Open Questions#Q-006]]); whether variants have stat bonuses is **UNDECIDED** ([[Open Questions#Q-024]]). Variant effects below are purely visual and must not suggest extra power.

> [!info] PROPOSED
> Colour keys come from [[Canonical Proposed Values]] §1; ascension visual tiers from §9. Every effect, count and shape here is **PROPOSED**.

---

## 1. Escalation ladder

Each tier adds one new **shape** on top of the previous tier's vocabulary, so tiers are recognisable without colour.

| Tier | Colour | Signature shape | Motion | Light |
|---|---|---|---|---|
| Common | `#9AA5B1` | Soft round puff | Gentle | None |
| Uncommon | `#4CC26A` | Leaf sparks | Fluttering | None |
| Rare | `#3D8BFF` | Straight light rays | Radiating | Small glow |
| Epic | `#A55BFF` | Orbiting motes | Circling | Glow |
| Legendary | `#FFB020` | Vertical light pillar | Rising | PointLight (Medium and High) |
| Mythical | `#FF4D8D` | Petal spiral | Spiralling | PointLight |
| Secret | `#1B1B2F` + prismatic | Prism shards, aurora ribbons, stars | Shimmering colour shift | PointLight + local night grade |

---

## 2. Egg idle auras (VFX-101 to VFX-107)

On egg models in storage displays, the hatch stage and the vault racks ([[Egg Art Direction]]).

| ID | Tier | Components | Rate (authored) | Class |
|---|---|---|---|---|
| VFX-101 | Common | None (material only) | — | P3 |
| VFX-102 | Uncommon | 1 emitter, occasional leaf spark | 2 | P3 |
| VFX-103 | Rare | Faint rim glow (Neon shell band), 1 emitter of tiny rays | 3 | P3 |
| VFX-104 | Epic | 3 orbiting mote parts (no particles) | — | P3 |
| VFX-105 | Legendary | Gold sparkle emitter + short upward glow | 5 | P3 |
| VFX-106 | Mythical | Petal emitter, slow spiral | 5 | P3 |
| VFX-107 | Secret | VFX-161 prismatic module + 4 star parts | 6 | P3 |

Vault racks with many eggs: only the 10 nearest eggs to the camera run particle auras; the rest use material and Neon bands only.

## 3. Roll reveal bursts (VFX-111 to VFX-117)

Used at phase C of each reveal in [[Animation - Egg Roll]]. Builds before the reveal use neutral white only (VFX-302 neutral); a tier's colour first appears in its own burst.

| ID | Tier | Burst | Extras | Low / Medium / High particle scale |
|---|---|---|---|---|
| VFX-111 | Common | Grey puff ring, 12 particles | — | 40 / 70 / 100% |
| VFX-112 | Uncommon | Green ring + 4 leaf sparks | — | same |
| VFX-113 | Rare | Blue burst + 6 rays (Beams, 0.5 s) | — | same |
| VFX-114 | Epic | Violet burst + ring shockwave + 8 orbiting motes for 1.5 s | — | same |
| VFX-115 | Legendary | Gold burst + 20-stud light pillar (1 Beam) + ray fan | PointLight 1.5 s (Medium and High) | same; pillar always shown |
| VFX-116 | Mythical | Magenta-rose burst + petal spiral + double ring | PointLight | same |
| VFX-117 | Secret | Prismatic burst + aurora ribbons (1/2/4 Beams by tier) + star shower | Local night grade during build (Animation - Egg Roll §5.7) | same |

## 4. Hatch reveal bursts (VFX-121 to VFX-127)

Used at the burst beat in [[Animation - Egg Hatch]]. The egg's rarity is already known, so these may use the tier colour throughout.

| ID | Tier | Effect |
|---|---|---|
| VFX-121 | Common | Shell burst puff in grey |
| VFX-122 | Uncommon | Puff + leaf sparks |
| VFX-123 | Rare | Puff + 6 rays |
| VFX-124 | Epic | Rays + motes orbiting the hatched animal for 1 s |
| VFX-125 | Legendary | Pillar + rays |
| VFX-126 | Mythical | Pillar + petal spiral around the animal |
| VFX-127 | Secret | 0.3 s local night flash, prismatic burst, aurora ribbons |

In a multi-hatch, only the centre (highest) egg plays its full effect; others play at 60% particle scale without Beams.

---

## 5. Companion rarity markers and ability accents (VFX-131 to VFX-137)

Persistent markers on animals in the world help players read their own and others' teams at a glance. They are deliberately subtle so combat effects stay readable.

| ID | Tier | Persistent marker (on `A_Aura`) | Ability accent (added to the archetype effect) |
|---|---|---|---|
| VFX-131 | Common | None | None |
| VFX-132 | Uncommon | None | None |
| VFX-133 | Rare | Thin ground ring decal under the animal, 30% opacity | Rarity-coloured rim on rings and Beams |
| VFX-134 | Epic | Ring + 2 slow orbiting motes | Rim |
| VFX-135 | Legendary | Ring + faint upward gold sparkle (rate 3) | Rim + secondary sparkle layer |
| VFX-136 | Mythical | Ring + occasional petal (rate 2) | Rim + petal layer |
| VFX-137 | Secret | Ring + VFX-161 prismatic module at low rate | Rim + prismatic shimmer |

Wild animals show the same markers so players can spot a rare wild spawn; Mythical and Secret wild spawns are also announced to the server ([[Wild Animal Spawning and Respawn]]).

---

## 6. Ascension visual tiers (VFX-141 to VFX-145)

From [[Canonical Proposed Values]] §9. These are persistent on the animal everywhere it appears (world, pens, UI previews).

| ID | Level | Visual | Implementation | Class |
|---|---|---|---|---|
| VFX-141 | A1 | Coloured trim | Material and colour swap on designated trim parts (collar, bands, fin edges); no particles | P3 |
| VFX-142 | A2 | Rarity-coloured eye glint | Emissive eye decal in the rarity colour; a 4-frame sparkle every 6 s | P3 |
| VFX-143 | A3 | Soft aura | Low-opacity glow shell (scaled transparent mesh, `Neon` at 0.9 transparency) around the body | P3 |
| VFX-144 | A4 | Particle accents | Species-themed motes (leaves, snowflakes, bubbles, sparks, feathers) orbiting at rate 4 | P3 (own team P1) |
| VFX-145 | A5 | Crest and full aura | Crest parts welded to `Head` (model asset) + aura shell at higher opacity + accent motes at rate 6 | P3 (own team P1) |

### 6.1 Stacking rule

Rarity markers and ascension effects combine without doubling the particle load:

- Ground ring: use the rarity ring (VFX-133 to VFX-137); ascension does not add another ring.
- Particles: an animal runs **at most one** continuous particle layer: the stronger of its rarity marker and its A4/A5 accents. Secret animals at A4+ blend the prismatic module into the accent motes' colour instead of adding an emitter.
- Variants (§7) replace the rarity marker's particle layer with the variant's layer, keeping the ring.

---

## 7. Variant effects (VFX-151 to VFX-155)

Material sets are owned by [[Variant Visual Treatments]] (VAR-series assets). The VFX layer adds a small amount of motion so variants are noticeable but never louder than a Legendary marker.

| ID | Variant | Material (owned elsewhere) | VFX layer | Rate | Notes |
|---|---|---|---|---|---|
| VFX-151 | Golden | Metallic gold | Glint sparkles travelling along the silhouette | 3 | Must not use the Legendary pillar shape |
| VFX-152 | Diamond | Faceted crystal | Refraction glints (white and pale blue) | 3 | |
| VFX-153 | Rainbow | Hue-banded | Short hue-cycling `Trail` on `A_Tail` when moving | — | Hue cycle ≥ 4 s per loop (not strobing) |
| VFX-154 | Shadow | Deep indigo with soft edges | Slow drifting dusk wisps, violet rims | 2 | Calm "twilight" mood, not spooky; no skulls, no eyes in the dark (D-026) |
| VFX-155 | Neon | Bright emissive bands | Gentle pulse on the bands (material transparency 0.0 ↔ 0.2 over 2 s) | — | No Highlight (budget) |

---

## 8. Shared modules and screen effects

| ID | Effect | Use |
|---|---|---|
| VFX-160 | New-discovery sparkle | Ring of white-gold stars around a newly owned species at hatch (the "New" beat) |
| VFX-161 | Prismatic shimmer module | Reusable emitter group with colour-shifting `ColorSequence`, used by every Secret effect |
| VFX-170 to VFX-176 | Reveal screen vignettes, Common to Secret | Screen-space frame tint at reveal moments in [[UI - Egg Rolling]] and [[UI - Egg Hatching]]; peak opacity ≤ 40%; Secret uses a prismatic edge, not a full-screen flash |

IDs VFX-177 to VFX-199 are reserved.

---

## 9. Budgets for persistent effects

| Population | Low | Medium | High |
|---|---|---|---|
| Local player's 3 companions | Full markers and A4/A5 accents at Low cap | Full | Full |
| Other players' companions within 40 studs | Ring only | Ring + half-rate particles | Full |
| Beyond 40 studs | Nothing | Ring only | Ring only |
| Pen animals (if displayed, [[Open Questions#Q-008]]) | Ring only | Ring only, accents on the nearest 3 | Ring, accents on the nearest 6 |
| Wild animals | Rare and above: ring only | Ring + Legendary+ particles | Full |

## 10. Test hooks

- Screenshot every tier's roll and hatch reveal in greyscale: each must still be identifiable by shape.
- Inspect all non-Secret roll builds: no tier colour or night grade before phase C ([[Animation - Egg Roll]]).
- A5 Secret Rainbow-variant animal: exactly one continuous particle layer active.
- Rainbow hue cycle and Neon pulse: no luminance change faster than 3 per second ([[VFX Bible]] §5).

---

## Related documents
- [[VFX Bible]]
- [[Rarity Visual Language]]
- [[Variant Visual Treatments]]
- [[Animal Variants]]
- [[Egg Art Direction]]
- [[Animation - Egg Roll]]
- [[Animation - Egg Hatch]]
- [[Animation - Ascension]]
- [[Animation - Animal Abilities]]
