---
title: Colour Palette
type: art-direction
category: art
status: mixed
priority: P0
owner: Art Director
last_updated: 2026-11-14
tags:
  - art
  - colour
  - palette
  - rarity
  - accessibility
---

# Colour Palette

The master list of colours used by models, environments, VFX and UI. Every hex value an artist or engineer types should come from this page. Rarity colour keys are inherited from [[Canonical Proposed Values]] §1 and are not redefined here; everything else on this page is **PROPOSED** by the Art Director unless marked otherwise.

> [!success] CONFIRMED
> The visual direction is colourful, polished and low-poly, with clear silhouettes, and contains no horror, "Italian brainrot" or meme animals (D-026, [[Decision Register]]). Seven rarities exist (D-003).

> [!info] PROPOSED
> All hex values below except the rarity keys are proposals for look-development. They are tuned for sRGB displays and for the lighting in [[Lighting Direction]]. Change a value here, never locally in another document.

![[Rarity Colour Swatch Sheet.svg]]

## Colour principles

1. **Saturated but not neon by default.** Base albedo colours sit between 55% and 85% saturation and between 45% and 90% value (HSV). Pure Neon-material colour is reserved for accents, telegraphs and specific variants ([[Variant Visual Treatments]]).
2. **Value before hue.** Every animal, prop and UI element must read correctly in greyscale. Hue is a second channel, never the only one ([[UI Accessibility Standards]]).
3. **Rarity owns its key colour.** The seven rarity keys are used at full strength only for rarity-carrying elements (frames, nameplates, egg trims, hatch effects). Environments and base modules use desaturated or shifted neighbours so that rarity never gets lost in scenery.
4. **Warm = player side, cool = information, red-orange = danger.** Feedback colours follow this rule everywhere (see [[Colour Palette#Feedback and combat colours]]).
5. **No black, no blood.** The darkest colour on any model is `#1B1B2F` (the Secret key) or region shadow tones; true `#000000` is used only for silhouette tests. Red is never used as a liquid, splatter or wound colour.

## Rarity colours

Canonical keys from [[Canonical Proposed Values]] §1 (**PROPOSED** values for **CONFIRMED** tiers). The supporting tints are **PROPOSED** here.

| Index | Rarity | Key (canonical) | Dark shade | Light tint | Glow (for Neon/Bloom) | Text on key | Pip count |
|---:|---|---|---|---|---|---|---:|
| 0 | Common | `#9AA5B1` | `#5E6873` | `#D5DCE3` | none | `#1B1B2F` | 1 |
| 1 | Uncommon | `#4CC26A` | `#2E8445` | `#B5EBC2` | `#7BFF9C` | `#10351C` | 2 |
| 2 | Rare | `#3D8BFF` | `#1F5BC2` | `#B3D3FF` | `#7DB6FF` | `#FFFFFF` | 3 |
| 3 | Epic | `#A55BFF` | `#6E2FC9` | `#DCC2FF` | `#C69BFF` | `#FFFFFF` | 4 |
| 4 | Legendary | `#FFB020` | `#C27A00` | `#FFE2A3` | `#FFD36B` | `#3A2400` | 5 |
| 5 | Mythical | `#FF4D8D` | `#C2245E` | `#FFC2D8` | `#FF8AB6` | `#FFFFFF` | 6 |
| 6 | Secret | `#1B1B2F` + prismatic | `#0E0E1C` | `#3A3A5C` | prismatic set below | `#FFFFFF` | 7 |

**Secret prismatic shimmer set (PROPOSED).** Used as `UIGradient` or `ColorSequence` keypoints, always over the `#1B1B2F` base, never as a flat fill:

| Keypoint | 0.00 | 0.17 | 0.33 | 0.50 | 0.67 | 0.83 | 1.00 |
|---|---|---|---|---|---|---|---|
| Colour | `#FF6B9E` | `#FFB84D` | `#FFF27A` | `#6DF2A8` | `#5CE1FF` | `#7A8CFF` | `#C77DFF` |

The prismatic set is deliberately lighter and pinker than the [[Variant Visual Treatments|Rainbow variant]] bands so that a Secret frame and a Rainbow animal are never confused.

> [!warning] Colour collisions to manage
> - **Legendary gold `#FFB020` vs Golden variant** (`VAR-001`). Golden animals use metallic response and sparkle rather than a flat hue; rarity is shown by the frame, not the body ([[Variant Visual Treatments]]).
> - **Secret `#1B1B2F` vs Shadow variant** (`VAR-004`). Shadow uses violet rim tones `#9B7BFF`; Secret uses the prismatic set. Neither may borrow the other's accent.
> - **Uncommon `#4CC26A` vs foliage** in [[Region - Whisperwood Forest]] and [[Region - Emerald Canopy]]. World nameplates always sit on a dark backing plate (`#1B1B2F` at 35% transparency).
> - **Common `#9AA5B1` vs snow and rock** in [[Region - Frostfang Tundra]] and [[Region - Skyreach Peaks]]. Same backing-plate rule; Common pips get a 1 px `#1B1B2F` stroke.

## Feedback and combat colours

These colours carry gameplay meaning and must never be used decoratively. Owned here; their use in effects is specified in [[VFX Bible]] and [[Combat Feedback and Readability]].

| Token | Hex | Meaning | Typical carrier |
|---|---|---|---|
| `fb.damage.dealt.player` | `#FFFFFF` | Damage the local player dealt | Damage number, stroke `#1B1B2F` |
| `fb.damage.dealt.team` | `#FFE066` | Damage the local player's animals dealt | Damage number |
| `fb.damage.taken` | `#FF5A4E` | Damage the local player or their animals took | Damage number, screen-edge pulse |
| `fb.heal` | `#5CFF9D` | Healing received | Number, plus-sign particles |
| `fb.shield` | `#7FD8FF` | Damage absorbed, shield active | Bar overlay, bubble |
| `fb.control` | `#FFD23F` | Stun, slow, root and other control states | Status icon ring, swirl particles |
| `fb.dot` | `#FF8A3D` | Damage-over-time state | Status icon ring |
| `fb.buff` | `#6CF0C2` | Positive status | Up-arrow icon |
| `fb.debuff` | `#C07BFF` | Negative non-control status | Down-arrow icon |
| `fb.telegraph.enemy` | `#FF4B3E` | Enemy attack area (fill 65% transparent, edge opaque) | Ground decal, Beam |
| `fb.telegraph.boss` | `#FF2E63` edge, `#FFD23F` inner pulse | Boss heavy attack | Ground decal, two-stage |
| `fb.telegraph.friendly` | `#3DD6FF` | Own team's area ability | Ground decal |
| `fb.target.manual` | `#FFF35C` | Manual target command marker ([[Targeting and Command System]]) | Reticle, ring |
| `fb.selection` | `#FFFFFF` | Hover or selection outline | Highlight OutlineColor |

## Social and faction colours

| Token | Hex | Meaning |
|---|---|---|
| `social.self` | `#FFE066` | Local player's own name and animals' nameplate ring |
| `social.ally` | `#3DD6FF` | Party member or friendly player |
| `social.neutral` | `#E6E9F0` | Other players in the shared world, PvP off |
| `social.pvp.hostile` | `#FF6B3D` | Player who is a valid PvP target ([[PvP System]]) |
| `social.raid.defender` | `#3DA5FF` | Defender side during a raid ([[Base Raiding System]]) |
| `social.raid.raider` | `#FF7A2F` | Raider side during a raid |
| `social.wild` | `#F5F0E6` | Wild animal nameplate base (rarity pip shows tier) |
| `social.boss` | `#FF2E63` | Boss nameplate crown and health bar edge |

## UI palette

The skin used by [[UI Visual Styling]]. Layout, components and spacing are owned by [[UI Design System]].

| Token | Hex | Use |
|---|---|---|
| `ui.bg.deep` | `#141A33` | Full-screen overlays (75% opacity) |
| `ui.panel.base` | `#20264A` | Panel body |
| `ui.panel.raised` | `#2C3566` | Cards, list rows |
| `ui.panel.stroke` | `#0D1126` | Panel outer stroke |
| `ui.panel.highlight` | `#4A57A3` | Top bevel line, focus ring base |
| `ui.text.primary` | `#FFFFFF` | Body text on dark |
| `ui.text.secondary` | `#B9C1E6` | Captions, labels |
| `ui.text.disabled` | `#6B739C` | Disabled text |
| `ui.text.ondark.stroke` | `#1B1B2F` | UIStroke for display text |
| `ui.action.primary` | `#27C7A8` | Confirm, Hatch, Roll, Equip |
| `ui.action.primary.dark` | `#168A74` | Primary button bottom bevel |
| `ui.action.secondary` | `#5B6BFF` | Navigation, info |
| `ui.action.danger` | `#FF5470` | Close, cancel, destructive |
| `ui.action.robux` | `#F2F4F7` button with `#1B1B2F` text | Any Robux purchase button (kept visually distinct from Cash) |
| `ui.currency.cash` | `#8CE05A` | Cash icon and counters |
| `ui.currency.cash.dark` | `#4E9A2B` | Cash icon shade |
| `ui.warning` | `#FFC93C` | Warnings, "odds changed" notices |
| `ui.locked` | `#7A809E` | Locked content tint |

Robux pricing must never borrow the Cash green or any rarity colour, so that a player can always tell at a glance whether an action spends Robux ([[Monetisation Principles]]).

## Region palettes

Five anchor colours per region: ground, foliage or main surface, accent, sky tint, shadow tint. The sky tint is used as `Atmosphere.Color`; the shadow tint sets the hue family for `Ambient` and `OutdoorAmbient`, whose exact (lighter) values are in [[Lighting Direction]] so that every region meets the readability floor. Region content (layout, encounters) is owned by each region document.

| Region | Ground | Main surface | Accent | Sky tint | Shadow tint |
|---|---|---|---|---|---|
| [[Hub - Hatchling Haven]] | `#E8D9B5` warm sandstone | `#8FD16B` lawn | `#FF9EC4` blossom | `#C7D9F2` | `#6E6A80` |
| [[Region - Whisperwood Forest]] | `#7A5A3C` loam | `#5FAF4E` leaf | `#F2A65A` mushroom orange | `#CFE3C2` | `#4F6B55` |
| [[Region - Sunscorch Savanna]] | `#D9A35F` dry earth | `#D8C26A` grass gold | `#C2553A` termite red-clay | `#F4D9A6` | `#7E5E44` |
| [[Region - Emerald Canopy]] | `#4E3B2A` humus | `#2FA86A` jungle green | `#FF7A3D` orchid orange | `#BFE8C8` | `#2F5E48` |
| [[Region - Coral Coast]] | `#F2E2B8` sand | `#3FC6D9` shallow water | `#FF7F6B` coral | `#CDEFFF` | `#5B86A3` |
| [[Region - Frostfang Tundra]] | `#EEF4FA` snow | `#9CC9E8` glacier | `#4FB0C6` deep ice | `#DDEBFA` | `#7088AD` |
| [[Region - Skyreach Peaks]] | `#8A8F9E` granite | `#7FB86A` alpine meadow | `#F4F1E8` cloud white | `#D6E2FF` | `#5D6A93` |
| [[Region - Emberheart Caldera]] | `#3E3433` basalt | `#6B8F3A` lost-valley fern | `#FF8A2B` lava glow | `#E8A27A` | `#5A3A36` |
| [[Region - Starfall Sanctuary]] | `#3B3F7A` star-stone | `#8E9BFF` crystal | `#FFE38A` starlight | `#8C8CE0` | `#3E3F7A` |

Rule: a region's accent colour may match a rarity key's hue family but must differ by at least 15° of hue or 20% of value from that key. Emberheart's lava `#FF8A2B` is checked against Legendary `#FFB020` (hue difference about 12°, below the 15° rule, so **lava glow uses Neon only on cracks, never on large flat areas** to keep the difference clear).

## Palette for animal models

Animal colours are species-specific and live in each animal document (for example [[Tiger]]). The palette rules that apply to all of them:

| Rule | Value (PROPOSED) |
|---|---|
| Maximum distinct albedo colours per Common–Rare animal | 6 (from the shared palette atlas, see [[Material and Texture Direction]]) |
| Maximum distinct albedo colours per Epic–Secret animal | 9 |
| Eye colour | Iris from species doc; pupil `#1B1B2F`; highlight `#FFFFFF` (always present, friendly read) |
| Nose, mouth interior | `#3A2A33` (never pure black, never red-wet) |
| Teeth and claws | `#F5EFE0` |
| Rarity trim (from ascension A1, see [[Ascension System]]) | Rarity key at 100% on a trim strip ≤ 8% of visible surface |

## Accessibility checks

| Check | Requirement (PROPOSED) |
|---|---|
| Text contrast | ≥ 4.5:1 for body text, ≥ 3:1 for display text ≥ 24 px, measured against the panel colour it sits on |
| Rarity identification | Never colour alone: tier pips (1–7) and frame shape also differ ([[Rarity Visual Language]]) |
| Colour-vision simulation | Rarity sheet and feedback colours reviewed under deuteranopia, protanopia and tritanopia simulation before sign-off |
| Telegraphs | Enemy telegraphs pair `#FF4B3E` with an animated edge pulse so they read without hue |

See [[UI Accessibility Standards]] for the full accessibility standard.

## Related documents
- [[Art Direction Index]]
- [[Art Bible]]
- [[Rarity Visual Language]]
- [[UI Visual Styling]]
- [[Lighting Direction]]
- [[Variant Visual Treatments]]
- [[Canonical Proposed Values]]
- [[UI Accessibility Standards]]
- [[Visual Reference Placeholders]]
