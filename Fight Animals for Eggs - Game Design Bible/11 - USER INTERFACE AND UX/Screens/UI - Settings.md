---
title: UI - Settings
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - settings
  - accessibility
  - controls
  - audio
---

# UI - Settings

> [!info] PROPOSED
> All settings, defaults and groupings are **PROPOSED**. Accessibility settings implement [[UI Accessibility Standards]]; audio groups follow [[Audio Mixing and Priority]].

> [!warning] UNDECIDED
> A PvP setting appears here only if the PvP activation method ([[Open Questions#Q-011]]) is a menu toggle.

## Purpose

Let each player tune audio, visuals, controls, accessibility and gameplay comfort, with changes previewed live and saved to their profile so they follow them across devices (except device-specific graphics options).

## Layout

Tabbed panel: **Gameplay · Controls · Audio · Graphics · Accessibility · Notifications · Account**. Each tab is a vertical list of setting rows; a "Reset tab to defaults" button at the bottom.

## Hierarchy

1. Tab bar.
2. Setting rows (label, current value, control).
3. Live preview where relevant (text size, colour mode, HUD scale).
4. Reset.

## Elements

| Tab | Setting | Control | Default | Saved where |
|---|---|---|---|---|
| Gameplay | Skip hatch / roll / merge / ascension reveals after first viewing | Toggle | Off | Profile |
| Gameplay | Confirm every single roll | Toggle | Off | Profile |
| Gameplay | Show damage numbers | Toggle | On | Profile |
| Gameplay | Auto-select duplicates for ascension | Toggle | On | Profile |
| Gameplay | PvP (only if Q-011 picks a toggle) | Toggle | per decision | Server |
| Controls | Key bindings (PC) | Rebind list | [[UI Navigation Map]] §5 | Profile |
| Controls | Gamepad bindings | Rebind list | [[UI Navigation Map]] §5 | Profile |
| Controls | Touch layout | "Edit HUD" mode (drag action buttons within safe zones) | Default layout | Device |
| Controls | Camera sensitivity | Slider 0.5–2.0 | 1.0 | Profile |
| Controls | Haptics | Toggle | On | Device |
| Audio | Master, Music, SFX, UI, Ambient, Alerts | Sliders 0–100 | 80 / 60 / 80 / 70 / 60 / 100 | Profile |
| Graphics | Effects density (our VFX only) | Low / Medium / High | Auto by device | Device |
| Graphics | 3D previews in menus | On / Static only | Auto (Static on low-memory devices) | Device |
| Graphics | Camera shake | Off / Low / Full | Low | Profile |
| Accessibility | Text size | 100 / 115 / 130 / 150% | 100% | Profile |
| Accessibility | HUD scale | 90–130% | 100% | Device |
| Accessibility | Colour-vision mode | Off / Protanopia / Deuteranopia / Tritanopia | Off | Profile |
| Accessibility | Reduced Motion | Toggle | Off | Profile |
| Accessibility | Reduce Flashing | Toggle | Off | Profile |
| Accessibility | Hold-to-confirm style | Hold / Tap twice | Hold | Profile |
| Accessibility | Toast duration | Normal / Long (+50%) | Normal | Profile |
| Notifications | Per-category toggles (discoveries, level, boss announcements, rare spawns, storage) | Toggles | On | Profile |
| Notifications | Raid alert sound | Slider | 100 | Profile (banner can't be disabled) |
| Account | Language | Dropdown | Roblox locale | Profile |
| Account | Restore purchases | Button | — | Re-checks passes with `UserOwnsGamePassAsync` |
| Account | Player ID / support code | Read-only text | — | For bug reports ([[Bug Reporting and Severity]]) |

Roblox's own graphics quality, volume and camera settings in the Roblox menu are not duplicated; the tab explains "Overall graphics quality is set in the Roblox menu." (Roblox menu behaviour *unverified* per platform.)

## Interactions

- Changes apply immediately with live preview; no Save button. Profile-saved settings are sent to the server in a debounced batch (2 s after the last change, **PROPOSED**).
- Rebinding: select action → "Press a key / button" → conflict check → if conflict, `Modal/Confirm` "Swap with Ground Slam?".
- Reserved keys (Roblox `Escape`, system buttons) cannot be bound; the prompt says so.
- "Reset tab to defaults" asks for confirmation.

## States

| State | Display |
|---|---|
| Normal | Rows |
| Rebinding | Row highlighted, "Press a key…" with 5 s timeout and Cancel |
| Saving | Small "Saving…" caption in the header, then "Saved" |
| Save failed | "Settings saved on this device only. We'll retry." |
| Setting not available on device | Row disabled with reason (for example haptics on PC) |

## Empty states

None; every tab always has rows.

## Error states

| Situation | Copy |
|---|---|
| Profile save failed | "Couldn't save to your account. Changes are kept for this session." |
| Binding conflict with reserved key | "This key is reserved by Roblox." |
| Restore purchases found nothing | "No purchases to restore." |

## Loading states

Settings apply from the profile snapshot on join, before the HUD appears, so text size and colour mode are correct from the first frame. Device-only settings load from a local cache if available, else defaults.

## Mobile layout

Tabs as a horizontal scrolling bar; rows 56 high with toggles at the right edge; sliders full width under labels. "Edit HUD" opens a full-screen overlay with draggable action buttons constrained to the safe area and to positions that keep the 8-unit gap.

## Desktop layout

Vertical tab list on the left, rows on the right; sliders 320 wide.

> [!note] Console / gamepad
> `ButtonL1`/`ButtonR1` switch tabs; D-pad left/right adjusts sliders and cycles dropdowns; `ButtonX` resets the focused setting.

## Accessibility

- This screen is itself fully usable at 150% text, in every colour mode, and by gamepad only.
- Colour-vision mode preview shows all seven rarity frames and the safe / raidable chips.
- Text size changes re-flow the Settings panel live, so players see the effect immediately.

## Roblox implementation notes

```text
Panels/Settings (Frame)
├─ Tabs (Frame, UIListLayout)
└─ Pages (Frame, UIPageLayout or visibility) → Rows (ScrollingFrame + UIListLayout)
```

- Text size is applied by a single `SettingsController` that sets a multiplier read by every text component (with `UITextSizeConstraint` bounds); HUD scale multiplies the HUD `UIScale`.
- Volume sliders set `SoundGroup.Volume` for each group in `SoundService`.
- Rebinding rebinds `ContextActionService` actions with the stored key; on-screen glyphs update via the same table.
- Profile-saved settings validate on the server (type and range) before persisting ([[Schema - Player Profile]]).

## Wireframe

```text
+-------------------------------- Settings --------------------------------[X]+
| [Gameplay] [Controls] [Audio] [Graphics] [Accessibility●] [Notif.] [Account] |
|------------------------------------------------------------------------------|
| Text size                 ( 100% | 115% | 130% | 150% )                       |
| HUD scale                 [-----●-----] 100%                                 |
| Colour-vision mode        [ Off ▾ ]   Preview: [C][U][R][E][L][M][S] Safe/Raid |
| Reduced Motion            [ off ]                                            |
| Reduce Flashing           [ off ]                                            |
| Hold-to-confirm style     ( Hold | Tap twice )                                |
| Toast duration            ( Normal | Long )                                  |
|                                              [ Reset tab to defaults ]       |
+------------------------------------------------------------------------------+
```

## Related documents

- [[UI Accessibility Standards]] · [[UI Navigation Map]] · [[UI Design System]] · [[UI - Notifications]]
- [[Audio Mixing and Priority]] · [[Camera Behaviour Guidelines]] · [[Schema - Player Profile]] · [[Colour Palette]]
