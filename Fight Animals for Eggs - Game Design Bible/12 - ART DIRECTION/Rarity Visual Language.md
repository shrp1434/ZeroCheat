---
title: Rarity Visual Language
type: art-direction
category: art
status: mixed
priority: P0
owner: Art Director
last_updated: 2026-11-14
tags:
  - art
  - rarity
  - vfx
  - ui
  - accessibility
---

# Rarity Visual Language

The fixed, learnable escalation that tells a player how rare something is: colour key, pip count, frame shape, glow, particles, motion and reveal intensity. It applies to animals, eggs, cards, nameplates and hatch moments. Colour keys are canonical ([[Canonical Proposed Values]] §1); the escalation rules are **PROPOSED** here. Effect implementation (emitters, IDs, budgets in detail) lives in [[VFX - Rarity and Variant Effects]] and the [[VFX Bible]].

> [!success] CONFIRMED
> Seven rarities in this order: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret (D-003). Rarity must be readable (D-026 direction).

![[Rarity Colour Swatch Sheet.svg]]

## 1. The escalation rule

Each tier adds **exactly one new kind of signal** on top of the previous tier, so players learn the ladder without reading labels.

| Tier | Key | New signal introduced at this tier | Cumulative signals |
|---|---|---|---|
| Common | `#9AA5B1` | Colour key + 1 pip | Colour |
| Uncommon | `#4CC26A` | Gradient fill on frames | Colour, gradient |
| Rare | `#3D8BFF` | Soft **glow** (outer glow on cards, ground ring on wild animals) | + glow |
| Epic | `#A55BFF` | **Motion** (animated sheen, rising motes) | + motion |
| Legendary | `#FFB020` | **Ornament** (filigree frame, light pillar on reveal, server announcement) | + ornament |
| Mythical | `#FF4D8D` | **Orbit** (particles that circle the subject; double frame) | + orbit |
| Secret | `#1B1B2F` + prismatic | **Inversion** (dark base with prismatic light, star field, unique reveal) | + inversion |

Secret is the only tier with a dark base. That inversion is the signal: it must never be imitated by any other tier, event, variant or monetised cosmetic.

## 2. Shape and pip coding (colour-independent)

Rarity is never conveyed by colour alone ([[UI Accessibility Standards]]).

| Tier | Pips | Badge shape | Frame corner |
|---|---:|---|---|
| Common | 1 | Circle | Plain rounded |
| Uncommon | 2 | Rounded square | Plain rounded |
| Rare | 3 | Diamond | Notched |
| Epic | 4 | Hexagon | Gem studs |
| Legendary | 5 | Shield with crown points | Filigree |
| Mythical | 6 | Six-petal rosette | Petals |
| Secret | 7 | Eight-point star | Star crest |

## 3. Escalation by surface

### 3.1 UI cards and frames
Implemented as specified in [[UI Visual Styling]] (frame strokes, gradients, ornaments and animated sheens per tier).

### 3.2 World nameplates (companions and wild animals)

| Tier | Nameplate | Wild animal ground ring | Wild ambient effect |
|---|---|---|---|
| Common | Name + 1 grey pip | none | none |
| Uncommon | + 2 green pips | none | none |
| Rare | + 3 blue pips, pip glow | Faint ring decal 4 studs, 70% transparent | none |
| Epic | + 4 violet pips | Ring 5 studs, 55% transparent, slow pulse 2 s | 6 rising motes/s |
| Legendary | + 5 gold pips, crown icon | Ring 6 studs, 45% transparent, pulse 1.6 s | 10 motes/s + soft `PointLight` Range 8 |
| Mythical | + 6 rose pips, crown | Double ring 7 studs, rotating | 8 orbiting sparks/s + light Range 10 |
| Secret | + 7 prismatic pips, star crest | Star-field ring 8 studs, prismatic edge | 6 star particles/s + prismatic shimmer; light Range 10 |

Wild animals show rarity so players can spot targets. **Companions do not show a rarity aura by default**: their rarity shows on the nameplate and in UI, while their in-world glow comes from ascension visual tiers (A1 trim to A5 crest and full aura, [[Canonical Proposed Values]] §9), which use the animal's rarity key. This keeps 48 companions from flooding a busy server with light.

### 3.3 Hatch reveal

The hatch result is decided on the server before the animation starts ([[Hatch System]]); the reveal only presents it. Visual intensity escalates as follows (timing and choreography belong to [[Animation - Egg Hatch]]; sound to [[Sound - Eggs]]):

| Tier | Burst particles | Light | Camera | Screen | Announcement |
|---|---:|---|---|---|---|
| Common | 16 dust puffs | none | static | none | none |
| Uncommon | 24 leaf confetti | rim light in key | static | none | none |
| Rare | 32 sparkles + light beam | `PointLight` Range 10 | slight push-in | 8% key-colour flash | none |
| Epic | 40 sparkles + shockwave ring | Range 12 | push-in + 2° tilt | 12% flash | none |
| Legendary | 48 + light pillar + sun-ray burst | Range 14, Bloom boost | push-in, slow orbit | 15% flash, gold vignette | Server banner ([[UI - Notifications]]) |
| Mythical | 56 + petal storm + orbiting sparks | Range 16 | orbit 90° | 18% flash, rose vignette | Server banner |
| Secret | 64 star particles + prismatic burst after a 0.4 s blackout | Range 18 | orbit 180° | dim to `#1B1B2F`, then prismatic wash | Server-wide banner |

Rules:
- **Reveal honesty.** The egg's appearance shows only the egg's rarity, which the player already knows. There is no "fake-out" sequence where an egg pretends to be rarer and then downgrades. Mid-animation tier "upgrades" are not used because hatch outcomes come from the egg's rarity pool only ([[Independent Random Outcomes]]).
- **Multi-hatch (up to 5, CONFIRMED D-016):** all eggs reveal together; the reveal intensity is that of the highest tier present, and each egg plays its own tier burst at 60% particle count.
- **Skip:** after the first viewing, skipping jumps straight to the result card with its full frame treatment ([[Canonical Proposed Values]] §7).

### 3.4 Eggs
Egg shells follow the same ladder (colour → gradient → glow → motion → ornament → orbit → inversion). See [[Egg Art Direction]].

## 4. Particle and light budgets per tier

| Tier | Max persistent particles per wild animal | Max emitters | Highlight instance allowed? |
|---|---:|---:|---|
| Common–Uncommon | 0 | 0 | No |
| Rare | 0 (ring decal only) | 0 | No |
| Epic | 12 | 1 | No |
| Legendary | 20 | 2 | No |
| Mythical | 24 | 2 | Only during hatch reveal |
| Secret | 24 | 3 | Only during hatch reveal |

`Highlight` instances are expensive and limited in number per client (a platform cap exists; the exact figure is *unverified*). Reserve them for: the local player's current manual target, hatch reveals, and UI previews.

Distance rules: wild rarity effects switch off beyond 120 studs from the camera; nameplates beyond 80 studs ([[UI Visual Styling]]).

## 5. Interaction with variants and ascension

| Layer | Carries | Never carries |
|---|---|---|
| Rarity | Frame, pips, badge, wild ring, hatch reveal | Body material |
| Variant ([[Variant Visual Treatments]]) | Body material and colour, a variant badge, a small variant particle set | Rarity colour keys at full strength, pips |
| Ascension ([[Ascension System]]) | Trim, eye glint, aura, accents, crest in the rarity key | Variant materials |

Worked example: a Golden [[Lion]] (Legendary) at A3. The body uses the Golden material set (VAR-001). The nameplate shows 5 gold pips and the crown. A soft aura in Legendary `#FFB020` comes from A3. To stop the Golden body and the gold aura merging into one blob, the aura uses the Legendary **light tint** `#FFE2A3` with 70% transparency when the variant is Golden. This substitution rule (variant shares the rarity hue → aura uses the light tint) applies to every such pairing.

## 6. Edge cases

- **Secret in dark regions:** Starfall Sanctuary's palette is close to `#1B1B2F`. Secret wild animals there get a prismatic edge ring at 100% opacity rather than 70%.
- **Common animals near snow:** nameplate backing plate is mandatory ([[Colour Palette]]).
- **Live events** may not introduce an eighth tier look; event items reuse the seven tiers.
- **Monetised cosmetics** (if any are ever proposed) may not use the rarity escalation signals, so that bought items are never mistaken for rare drops ([[Monetisation Principles]]).

## 7. Test hooks

- "Rarity line-up" debug scene: one wild animal of each tier side by side in every region preset; capture at 1080p and mobile.
- Colour-vision simulation pass on the swatch sheet and the line-up.
- Blind test: 5 players who have not seen the game rank seven unlabelled cards by rarity; target ≥ 80% correct ordering after one explanation screen.

## Related documents
- [[Art Direction Index]]
- [[Colour Palette]]
- [[UI Visual Styling]]
- [[Egg Art Direction]]
- [[Variant Visual Treatments]]
- [[VFX - Rarity and Variant Effects]]
- [[Egg Rarity System]]
- [[Animation - Egg Hatch]]
- [[UI Accessibility Standards]]
- [[Canonical Proposed Values]]
