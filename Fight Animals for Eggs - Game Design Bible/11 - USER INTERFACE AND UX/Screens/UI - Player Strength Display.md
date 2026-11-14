---
title: UI - Player Strength Display
type: ui-screen
category: ui
status: mixed
priority: P1
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - hud
  - player-strength
  - progression
---

# UI - Player Strength Display

> [!success] CONFIRMED
> Player strength is a statistic separate from animal strength (D-007).

> [!info] PROPOSED
> The Strength formula (`BaseStrength = 10 + 2 × (Level − 1)`, `Effective = BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)`, Training Grounds +5% per level) is **PROPOSED** in [[Canonical Proposed Values]] §4 and §12. The display design is **PROPOSED**.

## Purpose

Show the player's own Strength clearly and separately from their animals' power, and explain where it comes from so base upgrades and levelling feel meaningful. It has two parts: a HUD chip and a breakdown panel.

## Layout

- **HUD chip:** in the player panel, beside the level badge ([[UI - Main HUD]]).
- **Breakdown panel:** a side panel (Large) or bottom sheet (Compact) opened from the chip, with the effective value at the top, a contribution list, and a "What Strength affects" section.

## Hierarchy

1. Effective Strength (large numeric).
2. Contributions (level base, Training Grounds, other bonuses).
3. What Strength affects (attacks and specials).
4. How to increase it (links).

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Strength chip | Chip with icon | "STR 55" | Tap or hover opens the breakdown; pulses 0.3 s when the value changes |
| Effective value | `type.display` label | "55" with one decimal in a caption ("55.2") | Server value |
| Base row | List row | "Level 20 base: 48" | |
| Training Grounds row | List row | "Training Grounds L3: +15%" | Tap opens [[UI - Base Upgrades]] for that module (at base) or shows its location |
| Other bonuses rows | List rows | One row per active bonus source, if any | Hidden when none |
| Affects list | List | Basic combo (0.8 / 0.8 / 1.4 × Strength), Power Strike (3.0 ×), Ground Slam (2.0 ×) | Values from [[Player Combat]]; damage is before enemy defence |
| Separation note | Caption | "Strength powers your own attacks. Your animals' stats are shown on each animal." | Links to [[UI - Animal Inventory]] |
| Increase tips | `Btn/Ghost` list | "Level up", "Upgrade Training Grounds" | Navigation only |

## Worked example (PROPOSED values)

Level 20, Training Grounds level 3: `BaseStrength = 10 + 2 × 19 = 48`; `Effective = 48 × (1 + 0.15) = 55.2`. The chip shows **55** (rounded half-up, **PROPOSED** display rule); the breakdown shows 55.2. Power Strike row: `55.2 × 3.0 = 165.6` before defence.

> [!info] PROPOSED — no combined power number
> The UI never adds player Strength and animal stats into a single "total power" figure at launch. Keeping them visually separate reinforces D-007 and avoids implying a formula that does not exist. If a combined rating is wanted later, it needs its own design decision.

## Interactions

- Tap chip → breakdown opens; tap outside or Back closes.
- Tap a contribution row → navigates to its source (Progression or Base Upgrades).
- Value changes animate the number counting up over 0.4 s, with a "+7.2" delta caption for 2 s.

## States

| State | Display |
|---|---|
| Normal | Chip with value |
| Value increased | Pulse + delta caption |
| Temporary bonus active (if any exist) | Small up-arrow on chip; row shows remaining time |
| Knocked out | Chip dims with the rest of the player panel |

## Empty states

No bonus sources yet (new player): the breakdown shows only the level base row and the tip "Build Training Grounds at your base to increase Strength."

## Error states

If the breakdown request fails, the chip still shows the replicated effective value, and the panel shows "Breakdown unavailable right now" with a retry button. The chip value is never computed on the client.

## Loading states

The panel opens immediately with skeleton rows; the effective value (already replicated) is shown at once.

## Mobile layout

Chip 44 high (hit area), within the player panel. Breakdown is a bottom sheet covering 60% of the height, dismissible by swipe-down or the close button.

## Desktop layout

Hovering the chip shows a compact tooltip with the three main numbers; clicking opens a right-side panel 420 wide.

> [!note] Console / gamepad
> The chip is reachable from the menu hub ("Progress" → Strength section) because HUD chips are not in the gamepad focus path during combat.

## Accessibility

- Value always shown as text, never only as a bar.
- Delta captions persist 2 s and also appear in the notification log for players who miss them.
- Text scales per [[UI Accessibility Standards]].

## Roblox implementation notes

- Chip: `TextButton` with `UICorner`, `UIStroke`, icon `ImageLabel`; lives in `HUD/SafeArea/PlayerPanel`.
- Breakdown: `Panels/StrengthBreakdown` (`Frame` + `ScrollingFrame` + `UIListLayout`).
- Effective Strength replicates as a server-set attribute or profile field; the breakdown rows come from a read-only RemoteFunction (illustrative `GetStrengthBreakdown`, see [[Remote Communication Contract]]). Display-only: no client value feeds combat.

## Wireframe

```text
+------------------------------- Strength ---------------------[X]+
|                 STRENGTH   55   (55.2)                          |
|-----------------------------------------------------------------|
|  Level 20 base ............................................ 48   |
|  Training Grounds L3 ...................................... +15% |
|-----------------------------------------------------------------|
|  What Strength affects                                          |
|   Basic combo   44.2 / 44.2 / 77.3                              |
|   Power Strike  165.6     Ground Slam  110.4 (area)             |
|-----------------------------------------------------------------|
|  Strength powers your own attacks. Animal stats are separate.   |
|  [Level up ›]   [Upgrade Training Grounds ›]                    |
+-----------------------------------------------------------------+
```

## Related documents

- [[Player Strength]] · [[Player Combat]] · [[Module - Training Grounds]] · [[Player Progression and Levelling]]
- [[UI - Main HUD]] · [[UI - Progression Interface]] · [[UI - Base Upgrades]]
