---
title: UI Visual Styling
type: art-direction
category: art
status: proposed
priority: P0
owner: UI Art Lead
last_updated: 2026-11-14
tags:
  - art
  - ui
  - styling
  - rarity
  - icons
---

# UI Visual Styling

The visual skin of the interface: panels, buttons, cards, frames, icons, bars and world-space UI. [[UI Design System]] owns components, layout, spacing and navigation; [[Typography]] owns text; [[Colour Palette]] owns the hex values used here. All values are **PROPOSED**.

## 1. Style summary

**Chunky, tactile, bright.** Panels are dark navy slabs with rounded corners and a thick outer stroke; buttons look pressable with a visible bottom bevel; rarity frames are the most decorated element on any screen. The UI should feel like the same toy-box world as the animals ([[Art Bible]]), not a flat productivity app.

## 2. Panels and surfaces

Built from standard GUI objects (`Frame`, `UICorner`, `UIStroke`, `UIGradient`, `UIPadding`) so that nothing depends on large 9-slice textures.

| Element | Fill | `UICorner` | `UIStroke` | Gradient | Other |
|---|---|---|---|---|---|
| Modal panel | `ui.panel.base` `#20264A` | 18 px | 4 px `#0D1126` | Top-to-bottom `#2A3160` → `#20264A` | 2 px inner top line `#4A57A3` (separate Frame) |
| Card / list row | `ui.panel.raised` `#2C3566` | 12 px | 2 px `#0D1126` | none | Hover: stroke → `#FFFFFF` 2 px |
| Tooltip | `#141A33` at 8% transparency | 10 px | 2 px `#4A57A3` | none | Max width 360 px ref |
| Overlay backdrop | `ui.bg.deep` `#141A33` at 25% transparency | — | — | — | Blur via `BlurEffect` Size 12 in Lighting while a full-screen modal is open |
| Toast ([[UI - Notifications]]) | `#20264A` | 14 px | 3 px category colour | none | Left icon chip 48 px |

Corner radii scale with `UIScale`. Minimum touch target for any interactive element is defined in [[UI Accessibility Standards]]; styling never makes a target look smaller than its hit area.

## 3. Buttons

| Type | Face colour | Bevel (bottom 6 px) | Stroke | Label | Pressed state |
|---|---|---|---|---|---|
| Primary (Roll, Hatch, Equip, Confirm) | `#27C7A8` | `#168A74` | 3 px `#0D1126` | `type.button`, white, 2 px stroke `#0D3B33` | Face moves down 4 px, bevel shrinks to 2 px, 0.06 s |
| Secondary | `#5B6BFF` | `#3B47C2` | 3 px `#0D1126` | White | As primary |
| Danger (Cancel, Close) | `#FF5470` | `#C2304A` | 3 px `#0D1126` | White | As primary |
| Robux purchase | `#F2F4F7` | `#B9C1D0` | 3 px `#0D1126` | `#1B1B2F`, with Robux glyph | As primary |
| Disabled | `#4A5070` | `#343A57` | 3 px `#0D1126` | `#8C92B3` | No movement |
| Icon button (round) | `#2C3566` | none | 3 px `#0D1126` | Icon 60% of diameter | Scale 0.92 |

The Robux button is deliberately pale and plain compared with Cash actions so players always know when real money is involved ([[Monetisation Principles]], [[Roblox Monetisation Policy Requirements]]). Never animate a Robux button with rarity shimmer or pulsing glows.

## 4. Rarity frames for animal and egg cards

Frames are the main UI carrier of rarity. Escalation follows [[Rarity Visual Language]]; this table is the UI implementation.

| Tier | Frame stroke | Card background gradient | Corner ornaments | Animated element | Pips |
|---|---|---|---|---|---|
| Common | 3 px `#9AA5B1` | `#3A4250` → `#2C3566` | none | none | 1 |
| Uncommon | 3 px `#4CC26A` | `#2E6B45` → `#2C3566` | none | none | 2 |
| Rare | 4 px `#3D8BFF` | `#244C8F` → `#2C3566` | small corner notches | none | 3 |
| Epic | 4 px `#A55BFF` | `#5A2F99` → `#2C3566` | corner gems | slow diagonal sheen (`UIGradient` Offset sweep, 3.0 s loop) | 4 |
| Legendary | 5 px `#FFB020` + 1 px inner `#FFE2A3` | `#8F5A00` → `#3A2A10` | gold corner filigree (ImageLabel, 128 px source) | sheen 2.0 s loop + slow glow pulse behind card | 5 |
| Mythical | 5 px `#FF4D8D` + 1 px inner `#FFC2D8` | `#8F1F4A` → `#2C1530` | petal ornaments | sheen 1.6 s + orbiting spark (1 small ImageLabel) | 6 |
| Secret | 5 px prismatic `UIGradient` (Rotation animated, 4.0 s per turn) | `#1B1B2F` with star-speck image overlay | star crest top-centre | prismatic rotation + twinkle | 7 |

Rules:
- Animated frames update via `RunService.RenderStepped` or `TweenService` only while the card is visible on screen; inventories with many cards animate at most **12** Epic-or-higher frames at once (PROPOSED), the rest show the static first frame.
- Variant badges ([[Variant Visual Treatments]]) sit in the top-right corner chip and never replace the rarity frame.
- Ascension stars (A1–A5, [[Ascension System]]) sit along the bottom edge in `#FFE066` with `#1B1B2F` stroke.

## 5. Iconography

| Set | Asset ID | Count | Style | Source size | Display sizes |
|---|---|---:|---|---|---|
| Currency icons | UI-004 | 3+ (Cash, Robux glyph from platform, XP) | Chunky, 2-tone with 4 px dark outline | 512×512 | 24, 32, 48 |
| Role icons | UI-005 | 7 | Silhouette glyph in rounded square | 256×256 | 24, 40 |
| Family icons | UI-006 | 6 | Animal-head silhouette | 256×256 | 24, 40 |
| Rarity pips and badges | UI-007 | 7 | Pips: filled circles; badge: frame shape per tier | 128×128 | 12–32 |
| Variant badges | UI-008 | 5 | Small emblem matching material | 256×256 | 24, 32 |
| Module icons | UI-016 | 9 | Module identity colour from [[Base Art Direction]] | 256×256 | 40, 64 |
| Map and region icons | UI-021 | 9 | Landmark silhouette | 256×256 | 32, 64 |

Icon rules: one light source from the top-left; outline 4 px at 256 px source (scaled proportionally); no text inside icons; no gradients with more than three stops; legible at 24 px. Animal portraits (UI-013) are rendered in-engine with a fixed portrait rig: three-quarter view facing left, camera FOV 30°, key light from top-left, rarity-tinted rim light. Portrait backgrounds are transparent; the card supplies the rarity background.

## 6. Bars and meters

| Bar | Fill | Background | Edge | Special states |
|---|---|---|---|---|
| Player HP ([[UI - Main HUD]]) | `#5CFF9D` → `#2FBF6A` gradient | `#0D1126` | 3 px `#0D1126`, 8 px corner | Below 30%: fill shifts to `#FFC93C`, below 15% to `#FF5A4E` with pulse |
| Companion HP ([[UI - Animal Team Display]]) | Same as player, 60% height | `#0D1126` | 2 px | Knocked-out: greyscale portrait plus dashed `#FF5A4E` ring |
| Ability cooldown | Radial sweep `#000000` at 45% transparency over icon | — | — | Ready: 0.2 s white flash on ring |
| Boss HP ([[UI - Boss Health Bar]]) | `#FF2E63` → `#FF7A59` | `#1B1B2F` | 4 px `#0D1126` + crown cap | Phase markers as white ticks; damage chip trail `#FFE066` |
| Shield ([[UI - Raid Interface]]) | `#7FD8FF` hatched pattern | `#0D1126` | 3 px | Recharging: animated diagonal stripes |
| XP | `#5B6BFF` → `#9AA8FF` | `#0D1126` | 2 px | Level-up: full-bar flash to `#FFFFFF` |

## 7. World-space UI

| Element | Container | Size and distance | Style |
|---|---|---|---|
| Animal nameplate | `BillboardGui`, `AlwaysOnTop = false` | 160×40 ref px; `MaxDistance` 80 studs (PROPOSED) | Name + rarity pips on a `#1B1B2F` 35% plate; own animals add a `#FFE066` ring |
| Wild HP bar | `BillboardGui` | Appears when damaged or targeted; fades after 4 s | 100×10, colours per §6 |
| Manual target marker | Ground decal + `BillboardGui` chevron | Visible to the commanding player only | `#FFF35C`, bobbing 0.6 s |
| Interaction prompt | `ProximityPrompt` with custom style | Platform default distance unless a design doc overrides | Primary-button styling; key glyph in a white rounded square |
| Damage numbers | `BillboardGui` pool | Max 24 concurrent per client (PROPOSED) | [[Typography]] `type.world.damage`; pop-up 0.15 s, drift 0.8 s, fade 0.25 s |

Use `ProximityPrompt.Style = Custom` only if the custom prompt meets the same accessibility rules as the default.

## 8. Motion style for UI

| Event | Motion (PROPOSED) |
|---|---|
| Panel open | Scale 0.9→1.0 and fade 0→1 in 0.18 s, `Enum.EasingStyle.Back`, Out |
| Panel close | Scale 1.0→0.95 and fade out in 0.12 s, Quad, In |
| Button hover | Scale 1.0→1.04 in 0.08 s |
| Currency gain | Counter rolls up over 0.4 s; icon bounce 1.0→1.2→1.0 |
| Rarity reveal | Owned by [[Animation - Egg Hatch]] and [[Rarity Visual Language]] |

Respect reduced-motion settings from [[UI - Settings]]: replace scale animations with fades and stop looping sheens.

## 9. Odds and purchase screens

Because odds disclosure is a **CONFIRMED** requirement (D-017), the odds panel on [[UI - Egg Rolling]] and [[UI - Egg Hatching]] follows strict styling:
- Plain `ui.panel.raised` background, no animated elements behind numbers.
- Each rarity row: rarity badge (pips + colour), rarity name, percentage. All rows the same height and font size; rare outcomes are not visually enlarged or highlighted to look more likely.
- The "Confirm" button is a primary button; no countdown timers or flashing urgency effects.

## Related documents
- [[Art Direction Index]]
- [[UI Design System]]
- [[Typography]]
- [[Colour Palette]]
- [[Rarity Visual Language]]
- [[UI Accessibility Standards]]
- [[UI and UX Index]]
- [[Asset Register]]
