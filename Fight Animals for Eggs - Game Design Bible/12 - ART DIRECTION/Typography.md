---
title: Typography
type: art-direction
category: art
status: proposed
priority: P1
owner: UI Art Lead
last_updated: 2026-11-14
tags:
  - art
  - ui
  - typography
  - fonts
  - localisation
---

# Typography

Font choices, type scale, outline rules and number styling for all on-screen and in-world text. Screen layouts and component behaviour are owned by [[UI Design System]]; this page owns how text looks. All values are **PROPOSED**.

## 1. Typeface roles

| Role | Typeface | How it is set in Roblox | Weights used | Where |
|---|---|---|---|---|
| Display | Fredoka One | `Enum.Font.FredokaOne` | Regular (the face is already heavy) | Titles, rarity reveals, hatch result names, big numbers, button labels |
| Body / UI | Builder Sans | `Font.new("rbxasset://fonts/families/BuilderSans.json", Enum.FontWeight.Medium)` *(asset path unverified)* | Medium, Bold, ExtraBold | Body copy, odds tables, stats, settings, tooltips |
| Fallback body | Gotham SSm | `Enum.Font.GothamMedium` / `Enum.Font.GothamBold` | Medium, Bold | Used if Builder Sans renders incorrectly on a target device in look-dev |
| Accent (sparingly) | Luckiest Guy | `Enum.Font.LuckiestGuy` | Regular | Boss names on the [[UI - Boss Health Bar]], region title cards, event banners |

Rules:
- Never more than two typefaces on one screen (Display plus Body). Accent replaces Display where used; it never appears with Display.
- No script, horror or "grunge" fonts anywhere (D-026). No fonts that imitate meme captions (for example heavy white caps with black outline used as a joke format).
- Platform fonts only. No custom font uploads are planned; if Roblox font availability changes, the fallback row applies.

> [!note] Verification
> Roblox's font catalogue and family asset paths change over time. The `Font.new` family paths above are *unverified* and must be checked in Studio during [[M02 - Core Project Setup]]. `Enum.Font` names are listed for readability; the implementation should prefer `Font` objects (`TextLabel.FontFace`) so weights can be set.

## 2. Type scale

Sizes are in pixels at the reference resolution of 1920×1080. A root `UIScale` adapts them per device ([[UI Design System]]). Minimums apply after scaling.

| Token | Face | Size (ref) | Minimum after scaling | Line height | Use |
|---|---|---:|---:|---:|---|
| `type.hero` | Fredoka One | 72 | 40 | 1.0 | Hatch reveal name, "LEGENDARY!" banner |
| `type.h1` | Fredoka One | 48 | 28 | 1.05 | Screen titles |
| `type.h2` | Fredoka One | 34 | 22 | 1.1 | Panel titles, card names |
| `type.h3` | Builder Sans ExtraBold | 26 | 18 | 1.15 | Section headers, button labels (long) |
| `type.button` | Fredoka One | 28 | 18 | 1.0 | Primary and secondary buttons |
| `type.body` | Builder Sans Medium | 20 | 14 | 1.3 | Descriptions, tooltips |
| `type.body.strong` | Builder Sans Bold | 20 | 14 | 1.3 | Values inside body text |
| `type.caption` | Builder Sans Medium | 16 | 12 | 1.25 | Labels, footnotes |
| `type.number.hud` | Fredoka One | 32 | 20 | 1.0 | Cash counter, level |
| `type.number.odds` | Builder Sans Bold | 22 | 14 | 1.2 | Odds percentages ([[UI - Egg Rolling]]) |
| `type.world.name` | Builder Sans Bold | 18 | 14 | 1.0 | BillboardGui nameplates |
| `type.world.damage` | Fredoka One | 30 | 22 | 1.0 | Damage and heal numbers |

Body text is never set below 14 px on any device and captions never below 12 px. Use `TextScaled` only together with `UITextSizeConstraint` so that `MinTextSize` and `MaxTextSize` enforce these limits.

> [!danger] Odds disclosure legibility
> Displayed odds are a **CONFIRMED** requirement (D-017). Odds percentages use `type.number.odds` and are never shrunk below 14 px, never placed over animated backgrounds, and never set in the Accent face. Low-probability values (for example 0.02%) must show all significant digits ([[Randomised Reward Compliance]]).

## 3. Outlines, shadows and colour

Text over 3D scenes needs an outline. Text on panels does not.

| Context | Fill | `UIStroke` colour | Stroke thickness (ref px) | Notes |
|---|---|---|---:|---|
| Display text over scene | `#FFFFFF` | `#1B1B2F` | 3 | `UIStroke.ApplyStrokeMode = Contextual` |
| Display text on panel | `#FFFFFF` | none | 0 | Use a 2 px drop shadow label at `#0D1126`, offset (0, 3) |
| Body on panel | `#FFFFFF` or `#B9C1E6` | none | 0 | |
| Rarity name | Rarity key from [[Colour Palette]] | Rarity dark shade | 2.5 | Secret uses a prismatic `UIGradient` on fill over `#FFFFFF` |
| Damage numbers | Feedback colours | `#1B1B2F` | 2.5 | See [[Combat Feedback and Readability]] |
| World nameplate | `#F5F0E6` | `#1B1B2F` | 2 | Rarity pips beside, not inside, the name |

Stroke thickness scales with `UIScale`. On screens below 720 px tall, reduce strokes by 0.5 px but never below 1.5 px for scene text.

## 4. Numbers

| Rule | Example |
|---|---|
| Large values abbreviate with one decimal from 10,000 | `12.5K`, `3.4M`, `1.0B` |
| Below 10,000 use a thin-space or comma separator per locale | `2,500` |
| Prices always show the currency icon to the left of the number | Cash icon + `200` |
| Percentages: show up to the first two significant digits after the decimal point, never round a non-zero chance to `0%` | `0.02%`, `0.18%`, `65%` |
| Counters that change rapidly sit in a fixed-width frame so the layout does not jitter | Cash counter |
| Stat comparisons use `fb.buff` and `fb.debuff` colours plus ▲ ▼ glyphs | `ATK 46 ▲` |

The exact abbreviation thresholds are a UI rule; if [[UI Design System]] defines different ones, it takes precedence and this table should be updated.

## 5. Localisation

- No text is baked into images, textures or meshes. All text uses `TextLabel` or `TextButton` so Roblox translation tooling can reach it.
- Every text container allows **30% expansion** without clipping (German and Portuguese are the planning cases).
- In-world signage defaults to icons. Whether in-world text signs are allowed at all is **UNDECIDED** (Q-605).
- Rarity names and animal names are proper nouns in English in the data, but are still routed through localisation.

## 6. Hatch and reveal typography

| Moment | Treatment |
|---|---|
| Rarity banner (Common–Epic) | `type.hero`, rarity key fill, scale-in 0.85→1.0 over 0.2 s |
| Rarity banner (Legendary–Mythical) | As above plus 4 px stroke and an animated `UIGradient` sheen sweep |
| Rarity banner (Secret) | Fill `#FFFFFF` with prismatic `UIGradient` rotation, stroke `#0E0E1C`, letter-by-letter reveal 40 ms per letter |
| Animal name | `type.h1`, white, under the banner |
| "NEW" tag (first time owned) | `type.caption` in a `ui.warning` pill. This is a display label only; it never implies changed odds (D-018) |

Motion timings belong to [[Animation - Egg Hatch]]; the colours belong to [[Rarity Visual Language]].

## 7. Test hooks

- Typography sheet screen in a debug place renders every token at 1080p, 720p and a 390×844 mobile viewport.
- Automated check: walk all `TextLabel` instances under `PlayerGui` and flag any with `TextSize` < 14 (body) or `FontFace` outside the approved list. Illustrative only:

```lua
-- Illustrative Luau, not tested in Studio
local APPROVED = { FredokaOne = true, BuilderSans = true, GothamSSm = true, LuckiestGuy = true }
local function auditText(root: Instance)
	for _, inst in root:GetDescendants() do
		if inst:IsA("TextLabel") or inst:IsA("TextButton") then
			local family = string.match(inst.FontFace.Family, "families/(%w+)%.json")
			if family and not APPROVED[family] then
				warn("Unapproved font", inst:GetFullName(), family)
			end
			if not inst.TextScaled and inst.TextSize < 12 then
				warn("Text below minimum", inst:GetFullName(), inst.TextSize)
			end
		end
	end
end
```

## Related documents
- [[Art Direction Index]]
- [[UI Visual Styling]]
- [[UI Design System]]
- [[UI Accessibility Standards]]
- [[Colour Palette]]
- [[Rarity Visual Language]]
- [[Randomised Reward Compliance]]
