---
title: UI Accessibility Standards
type: spec
category: ui
status: proposed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - accessibility
  - standards
  - qa
---

# UI Accessibility Standards

The minimum accessibility bar for every screen in [[UI and UX Index]]. Each screen document has an *Accessibility* section that applies these standards and notes exceptions. A screen cannot pass [[Definition of Done]] while it breaks a **must** rule below.

> [!info] PROPOSED
> Every threshold on this page is a **PROPOSED** studio standard. It draws on widely used practice for readable contrast, motion safety and input flexibility, but none of it is a Roblox platform requirement unless stated. The audience for Roblox skews young and plays mostly on phones, so the floors are deliberately generous.

---

## 1. Visual readability

| Rule | Level | Standard |
|---|---|---|
| Text contrast | must | Body and label text ≥ 4.5 : 1 against its actual background (including over 3D world when on the HUD; use a backing plate or `UIStroke` outline) |
| Large text and icons | must | Text ≥ 24 reference units and essential icons ≥ 3 : 1 |
| Minimum text size (post-scale) | must | Compact 14, Large 16, TV 20. Captions may go to 12 on Compact only for non-essential detail |
| Text scale option | must | 100 / 115 / 130 / 150% in [[UI - Settings]]; layouts use `AutomaticSize` and `UITextSizeConstraint` so nothing clips at 150% |
| `TextScaled` | should not | Avoid on body text; it makes size unpredictable. Allowed for single-word counters inside fixed boxes with a `UITextSizeConstraint.MinTextSize` |
| Numbers in confirmations | must | Full number with thousands separators; no abbreviations at the point of commit |
| Type and colours | — | Defined in [[Typography]] and [[Colour Palette]]; this page only sets floors |

## 2. Colour independence

1. **Rarity** is always encoded three ways: colour token, ornament shape ([[UI Design System]] §4.3) and the rarity name (or its one-letter code on small cards).
2. **Safe versus raidable** eggs use icon + text chips ("Safe from raids", "Raidable"), never colour alone.
3. **Health and danger** use a fill plus an icon change at the low-health threshold (25%), not just a red tint.
4. **Odds tables** list the rarity name in text on every row.
5. **Colour-vision modes** (Protanopia, Deuteranopia, Tritanopia) swap the semantic tokens to alternative values supplied by [[Colour Palette]]. They never change shapes or text, so every rule above still holds.
6. **Enemy versus ally** highlights (`Highlight` instances, see [[Combat Feedback and Readability]]) use outline style differences as well as colour.

## 3. Motion, flashing and camera

| Rule | Level | Standard |
|---|---|---|
| Flash limit | must | No full-screen or large-area flash more than **3 times per second**; reveal flashes for Mythical and Secret eggs ([[Animation - Egg Hatch]]) are capped and use a fade-in, not a hard cut |
| Reduced Motion setting | must | Replaces slides, bounces and looping sheens with 0.1 s fades; shortens reveal sequences to a static card with the result |
| Reduce Flashing setting | must | Removes white flashes and strobing particles from UI reveals; separate from Reduced Motion |
| Camera shake | must | Toggle in Settings; default on at low intensity ([[Camera Behaviour Guidelines]]) |
| Skippable reveals | must | Hatch, roll, merge and ascension reveals are skippable after the first viewing ([[Canonical Proposed Values]] §7) |
| Auto-playing parallax | should not | No background parallax on panels |

## 4. Input flexibility

| Rule | Level | Standard |
|---|---|---|
| Touch targets | must | ≥ 44 × 44 post-scale, ≥ 8 gap ([[UI Design System]] §3.4) |
| Full gamepad navigation | must | Every panel is fully operable with `GuiService.SelectedObject`; visible focus ring; no pointer-only controls |
| Full keyboard operation on PC | should | All panels reachable by hotkey or `Tab`-style focus; mouse never mandatory except camera |
| Hold-to-confirm alternative | must | `Btn/HoldConfirm` can be switched to "tap twice to confirm" in Settings for players who cannot hold |
| Rebinding | must | Combat and menu actions rebindable except Roblox-reserved keys |
| Drag-and-drop alternative | must | Every drag (for example team slots) has a tap-to-select, tap-to-place alternative |
| Timing pressure | must | No UI decision is on a timer except where gameplay itself is timed (raids). Confirmation modals never time out; a stale `oddsVersion` triggers a re-confirm, never an automatic purchase |
| Haptics | may | Short `HapticService` pulses on rare reveals and damage taken; toggle in Settings (*unverified* support per device) |

## 5. Audio equivalents

Every gameplay-relevant sound has a visual equivalent, and every critical visual alert has an optional sound.

| Sound event | Visual equivalent |
|---|---|
| Raid alarm ([[Sound - Base and Raid Alerts]]) | Critical banner with icon and text, HUD base chip pulses |
| World boss spawn horn | Toast with countdown and region name |
| Ability ready chime | Cooldown radial completes and button brightens |
| Low-health heartbeat | Low-health icon on `Bar/Health` and screen-edge vignette |
| Rare spawn announcement | Server announcement toast |

Volume sliders per `SoundGroup` (Music, SFX, UI, Ambient, Alerts) live in [[UI - Settings]]; see [[Audio Mixing and Priority]].

## 6. Cognitive load and clarity

- One primary action per panel region. Secondary actions are visually quieter.
- Plain language, short sentences, no jargon in player-facing copy. Internal terms such as "oddsVersion" or "Progression Score" never appear on screen.
- Irreversible actions (consuming duplicates, merging, releasing an animal) name exactly what will be lost, with portraits, before the confirm button.
- Probability copy is factual. It must never suggest a result is "due", "close", or "building up" (D-018). See [[UI - Egg Rolling#Copy rules]].
- Locked features always explain *why* and *how to unlock* (for example the base team lock, D-010).

## 7. Localisation readiness

- All strings come from a string table keyed by ID; no text is hard-coded in instances. `LocalizationService` auto-translation is not relied on for odds, prices or rules copy (*unverified* quality).
- Layouts tolerate **+35%** text length (PROPOSED) without clipping, using `AutomaticSize` and wrapping.
- Numbers and percentages are formatted by one shared formatter so decimal separators can be localised later.

## 8. Platform limits to note

Roblox does not currently provide a general screen-reader pathway for experience UI (*unverified*; re-check before launch). The studio therefore compensates with high contrast, text scaling, icon + text labels and audio cues rather than claiming screen-reader support.

## 9. Test checklist (for [[Test Plan Matrix]])

| Check | How |
|---|---|
| Contrast | Screenshot each panel over the brightest and darkest region backgrounds; measure label contrast |
| 150% text | Enable largest text scale; open every panel on Compact; nothing clipped or overlapping |
| Colour-vision modes | Each mode: identify all seven rarities and safe/raidable eggs without colour cues |
| Gamepad-only pass | Complete roll → hatch → ascend → team change using only a controller |
| Touch reach | One-thumb use of combat controls on a 6-inch phone in landscape |
| Reduced Motion and Reduce Flashing | Every reveal has no slides, sheens or flashes |
| Hold alternative | Every hold-to-confirm completes with tap-twice |

## Related documents

- [[UI and UX Index]] · [[UI Design System]] · [[UI Navigation Map]] · [[UI - Settings]]
- [[Colour Palette]] · [[Typography]] · [[UI Visual Styling]] · [[Rarity Visual Language]]
- [[Combat Feedback and Readability]] · [[Sound - UI Feedback]] · [[Design Principles and Fairness Charter]]
