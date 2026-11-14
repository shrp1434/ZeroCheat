---
title: UI - Main HUD
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - hud
  - combat
  - mobile-first
---

# UI - Main HUD

> [!info] PROPOSED
> Layout, sizes and bindings are **PROPOSED**. Combat values shown on the HUD (HP formula, special unlock levels, cooldowns) come from [[Canonical Proposed Values]] §4 and §13 and are also **PROPOSED**. The team lock rule (D-010) and team size of three (D-006) are **CONFIRMED**.

## Purpose

The HUD is the always-on layer during play. It must let a phone player fight in real time alongside three animals (D-005), read their own health and progress at a glance, see Cash and context (at base, team locked, PvP state), and reach every menu without covering combat. It hosts two sub-components documented separately: [[UI - Animal Team Display]] and [[UI - Player Strength Display]].

## Layout

Five anchored zones inside the safe area:

| Zone | Anchor | Contents |
|---|---|---|
| Player panel | Top-left | Health bar, level badge, XP bar, Strength chip |
| Team display | Left edge, below player panel | Three animal portraits with ability buttons ([[UI - Animal Team Display]]) |
| Context strip | Top-centre | Region name, base status chip, team lock chip, PvP chip, raid or boss overlay slot |
| Economy and menu | Top-right | Cash counter, notification bell, menu button |
| Action cluster | Bottom-right arc | Basic attack, three specials, dodge |

The bottom-left quarter is left empty on touch devices for the Roblox thumbstick.

## Hierarchy

1. Player health and the action cluster (survival and input).
2. Team display (the animals fight with you).
3. Context strip chips (lock, PvP, base status) — read when they change.
4. Cash, level and XP — progress, read between fights.
5. Menu button and notification bell.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Health bar | `Bar/Health` | "328 / 328" at level 20 (`100 + 12 × (Level − 1)`) | Ghost fill trails damage; low-health icon and vignette below 25% |
| Level badge | `Counter/Level` | "Lv 20" | Tap opens [[UI - Progression Interface]] |
| XP bar | `Bar/XP` | Current / next XP (`round(100 × L^1.6)`) | Pulses on gain; level-up toast |
| Strength chip | Chip | Strength icon + value | See [[UI - Player Strength Display]] |
| Region label | `TextLabel` | "Whisperwood Forest" | Fades after 4 s on entering a region; reappears on tap of the context strip |
| Base status chip | `Chip/Status` | "At base" / hidden | Visible only at own base; tap opens [[UI - Base Management]] |
| Team lock chip | `Chip/Locked` | Padlock + "Team locked" | Visible whenever away from own base; tap opens the explanation (D-010) |
| PvP chip | Chip | "PvP OFF" / "PvP ON" | Behaviour depends on activation method (**UNDECIDED**, [[Open Questions#Q-011]]); see [[UI - PvP Interface]] |
| Cash counter | `Counter/Currency` | "12.4K" | Counts up over 0.4 s on gain; full value on tap |
| Notification bell | `Btn/Icon` + badge | Unread count | Opens notification log ([[UI - Notifications]]) |
| Menu button | `Btn/Icon` | Grid icon | Opens the menu hub ([[UI Navigation Map]]) |
| Basic attack | `Btn/Combat` 96 × 96 | Fist / claw icon | Press for the 3-hit combo ([[Player Combat]]); hold repeats |
| Power Strike | `Btn/Combat` + `Radial/Cooldown` | Icon, 6 s cooldown | Unlocked at level 1 |
| Ground Slam | `Btn/Combat` + radial | Icon, 12 s cooldown | Shows `Chip/Locked` "Lv 10" until unlocked |
| Rally Cry | `Btn/Combat` + radial | Icon, 25 s cooldown | Shows `Chip/Locked` "Lv 25" until unlocked |
| Dodge | `Btn/Combat` + radial | Roll icon, 4 s cooldown | |
| Combat vignette | `ImageLabel` | Screen-edge tint | On low health and while in combat with a panel open |
| Command chip | Chip | "Team: attacking Boar" | Appears when a manual target command is active ([[UI - Animal Team Display]]) |

## Interactions

- **Combat:** press-to-fire for specials and dodge; a pressed special on cooldown plays a short shake and shows remaining seconds, never queues.
- **Locked special:** tapping shows a toast "Ground Slam unlocks at level 10".
- **Team lock chip:** tap opens `Modal/Info`: "Your team is locked while you are away from your base. Return to your base to change it." with a "Show route to base" action ([[Team Equipping and Base Lock Rule]]).
- **Menu button:** opens the menu hub panel; on PC also `M`.
- **Auto-hide:** in cut-scenes and reveals, the HUD hides with a 0.2 s fade; combat inputs are disabled while hidden.

## States

| State | Visible changes |
|---|---|
| Exploring | Full HUD; region label shown on entry |
| In combat (8 s combat tag) | Region label hidden, action cluster at full opacity, menu button dimmed (still usable) |
| At own base | Base status chip shown, team lock chip hidden |
| Away from base | Team lock chip shown |
| Boss fight | Boss bar occupies the context strip slot ([[UI - Boss Health Bar]]) |
| Raid (attacker or defender) | Raid counters occupy the context strip slot ([[UI - Raid Interface]]) |
| Player knocked out | Action cluster disabled, defeat overlay (penalties **UNDECIDED**, [[Open Questions#Q-014]]) |
| Panel open | HUD stays under the panel scrim; action cluster remains live on Large and TV, hidden behind full-screen panels on Compact |

## Empty states

- No animals equipped (new player before onboarding grants animals): team display shows three empty slots with "Hatch your first animals" linking to the onboarding step ([[New Player Onboarding]]).
- Zero Cash: counter shows "0"; no warning is shown, because zero Cash is normal.

## Error states

| Situation | Response |
|---|---|
| Special pressed but server rejects (cooldown desync) | Radial resyncs to the server value; no toast |
| Lost connection | `Modal/Critical` from the Critical layer; HUD inputs disabled |
| Player data still loading | HUD shows skeletons; combat inputs disabled until the profile loads |

## Loading states

On join, the HUD fades in only after the profile snapshot arrives. Until then, the Transition layer loading screen is shown ([[Save, Load and Recovery]]). Cash and level skeletons replace numbers if a late resync is pending.

## Mobile layout

- Action cluster: attack 96 × 96 at bottom-right with an 8-unit margin from the safe area; specials 64 × 64 on an arc above and left of it; dodge 64 × 64 to the left of attack.
- The Roblox default jump button also sits bottom-right on touch devices. The cluster is arranged around its default position rather than moving it, since repositioning `TouchGui` children is *unverified* and fragile.
- Team display is a vertical stack on the left edge between the player panel and the thumbstick area.
- Region label and toasts never overlap the top-bar inset from `GuiService:GetGuiInset()`.

## Desktop layout

- Action cluster becomes a horizontal hotbar at bottom-centre with key glyphs (`Q`, `E`, `R`, `F`), 56 × 56 slots; mouse click remains the basic attack.
- Team display moves to bottom-left, horizontal, next to the hotbar.
- Context strip and economy area unchanged.

> [!note] Console / gamepad
> TV layout uses the desktop arrangement at × 1.15 scale. Button glyphs swap to gamepad icons when `UserInputService.LastInputType` becomes a gamepad type. `DPadDown` opens the menu hub. No HUD element requires a cursor.

## Accessibility

- Health and cooldowns combine fill, number and icon; low health adds an icon, not only red.
- All HUD text has a `UIStroke` outline or backing plate for contrast over bright regions ([[UI Accessibility Standards]] §1).
- Camera shake and vignette intensity respect Settings toggles.
- Combat buttons can be enlarged with the HUD scale option (90–130%, **PROPOSED**) in [[UI - Settings]].

## Roblox implementation notes

```text
PlayerGui
└─ HUD (ScreenGui, DisplayOrder 10, ResetOnSpawn false, ZIndexBehavior Sibling)
   ├─ UIScale
   └─ SafeArea (Frame, sized from GuiService:GetGuiInset and ScreenInsets)
      ├─ PlayerPanel (Frame, UIListLayout vertical)
      │  ├─ HealthBar · LevelBadge · XPBar · StrengthChip
      ├─ TeamDisplay (see UI - Animal Team Display)
      ├─ ContextStrip (Frame, UIListLayout horizontal, centred)
      ├─ EconomyMenu (Frame, UIListLayout horizontal, right-aligned)
      └─ ActionCluster (Frame, absolute positions per breakpoint)
         └─ AttackButton, Special1-3, DodgeButton (ImageButton + UICorner + cooldown ImageLabel)
```

- Combat actions bind through `ContextActionService:BindActionAtPriority`; on-screen buttons call the same action handler so touch, keys and gamepad share one code path. The built-in `createTouchButton` option is not used.
- The client sends attack and special intents only; damage, cooldown authority and unlock checks are server-side ([[Implementation - Combat Damage Pipeline]]). The client predicts the cooldown radial and corrects to the server value.
- Base status and team lock come from server-set player attributes (illustrative names `AtOwnBase`, `TeamLocked`) observed with `GetAttributeChangedSignal`.
- Cash and XP update from the profile replication stream, never from client arithmetic.

## Wireframe

```text
+--------------------------------------------------------------------------------+
| [HP ██████████ 328/328]   Whisperwood Forest   [Team locked]  [PvP OFF]  12.4K  [!3] [≡] |
| [Lv 20][XP ████░░ 1,240/1,620]  [STR 55]                                        |
| +------+                                                                        |
| |Wolf  | [TAP]                                                                  |
| |██████|                                                                        |
| +------+                                                                        |
| |Fox   | [AUTO]                                                                 |
| |██████|                                                                        |
| +------+                                                                        |
| |Deer  | [TAP]                                              [R] [E]            |
| |██████|                                                 [Q]                   |
| +------+                                                       [ATTACK]        |
|   (thumbstick area)                                      [F]      (jump)        |
+--------------------------------------------------------------------------------+
```

## Related documents

- [[UI - Animal Team Display]] · [[UI - Player Strength Display]] · [[UI - Notifications]] · [[UI - Boss Health Bar]] · [[UI - Raid Interface]]
- [[Player Combat]] · [[Combat Feedback and Readability]] · [[Team Equipping and Base Lock Rule]]
- [[UI Design System]] · [[UI Navigation Map]] · [[UI Accessibility Standards]]
