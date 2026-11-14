---
title: UI - Boss Health Bar
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - bosses
  - combat
  - hud
---

# UI - Boss Health Bar

> [!success] CONFIRMED
> Mini-bosses and world bosses exist (D-012).

> [!info] PROPOSED
> World boss cadence and 2-minute pre-announcement, mini-boss 10-minute respawn, and reward eligibility once per player per spawn ([[Canonical Proposed Values]] §5). Bar design, phase markers and contribution indicator are **PROPOSED**.

> [!warning] UNDECIDED
> Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]). The UI shows no reward amounts until they are decided; the summary card reads from config.

## Purpose

Give every participant a shared, readable view of the boss fight: who the boss is, how much health remains, which phase it is in, and whether *this* player has contributed enough to be eligible for rewards. Announce world bosses before they spawn so players can travel to them.

## Layout

- Bar: top-centre in the CombatOverlay layer, replacing the region label slot of the context strip.
- Announcement: toast-style banner (Toasts layer) 2 minutes before a world boss.
- Reward summary: card after defeat.

## Hierarchy

1. Boss name and tier ("World Boss", "Mini-Boss").
2. Health remaining and phase.
3. Your contribution status.
4. Participants and timers.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Boss name | `type.title` | "Ironbark Colossus" | |
| Tier label | Chip | "World Boss" / "Mini-Boss" | Different frame ornaments per tier ([[Boss Art Direction]]) |
| Health bar | `Bar/Segmented` | Fill + ghost fill + percentage text | Phase markers at thresholds from boss config ([[Boss AI]]); the number of phases is not fixed by the UI |
| Phase label | Caption | "Phase 2" | Phase change plays a short shake (static flash-free under Reduced Flashing) |
| Status icons | Row | Boss buffs / shields / enrage icons, each with text tooltip | From boss state |
| Contribution indicator | Chip | "Reward eligible ✓" / "Deal more damage to qualify" | Server-evaluated against the threshold in [[Multiplayer Combat Rules]] and [[Boss Rewards]] |
| Participants | Caption | "12 fighting" | |
| Announcement banner | Toast (priority) | "Ironbark Colossus appears in 2:00 · Whisperwood–Savanna border" | "Show route" action; countdown text |
| Defeat card | `Modal/Info` (non-blocking variant) | "Ironbark Colossus defeated" + reward list from config | If Q-015 is unresolved in a build, card shows "Rewards: to be decided" in internal builds only |
| Already claimed | Chip | "Reward already claimed this spawn" | Once per player per spawn (**PROPOSED**) |

## Interactions

- The bar appears when the player enters the boss's engagement radius or deals damage, and hides 5 s after leaving or after defeat (**PROPOSED**).
- Tapping the bar (Compact) or hovering (Large) expands status icon descriptions.
- Announcement "Show route" highlights the way using the world map / compass (see [[World Overview and Map]]).

## States

| State | Display |
|---|---|
| Spawning soon | Announcement banner with countdown |
| Engaged, not eligible | Bar + "Deal more damage to qualify" |
| Engaged, eligible | Bar + "Reward eligible ✓" |
| Phase transition | Phase label update; marker passed |
| Boss leashed / reset | "Ironbark Colossus recovered" caption; bar refills ([[Boss AI]]) |
| Defeated | Defeat card |
| Player knocked out | Bar remains; contribution status kept; penalties per Q-014 |

## Empty states

No boss active and none announced: no bar. The Progression Interface shows boss history instead.

## Error states

If boss state stops replicating (streaming out), the bar shows "Boss out of range" and hides after 5 s. If the reward grant fails on the server, the defeat card shows "Reward is being processed" and a notification confirms later; the UI never shows a reward as granted before the server confirms it.

## Loading states

On entering the radius, the bar fades in with the current replicated health; no skeleton needed.

## Mobile layout

Bar width 70% of the safe area, 20 units high, with name above in `type.label`. Contribution chip under the bar on the right. Status icons limited to four, with "+2" overflow.

## Desktop layout

Bar 720 wide, 24 high; status icons and participants on one line under it.

> [!note] Console / gamepad
> No input needed. On TV the bar uses the × 1.15 scale and the announcement's "Show route" binds to `ButtonY` while the banner is visible.

## Accessibility

- Health percentage is shown as text.
- Phase markers are notches in the bar plus the phase label.
- Status icons carry text tooltips and are distinct shapes.
- Announcements have audio ([[Sound - Bosses]]) and visual forms.

## Roblox implementation notes

```text
CombatOverlay (ScreenGui, DisplayOrder 20)
└─ BossBar (Frame, AnchorPoint 0.5,0, top-centre within safe area)
   ├─ Name (TextLabel), Tier (Frame chip)
   ├─ Track (Frame + UICorner + UIStroke) → Ghost (Frame), Fill (Frame), Markers (Frame ×N)
   ├─ Percent (TextLabel)
   └─ Status (Frame, UIListLayout horizontal)
```

- Boss health replicates from the server ([[Service - BossService]]); tween the fill locally with `TweenService` between replicated values for smoothness. Phase thresholds come from boss config.
- Contribution eligibility is computed on the server and replicated per player; the client never estimates it from local damage numbers.
- With `StreamingEnabled`, the boss model may stream out; the bar binds to a server-replicated value object rather than the model so it stays accurate.

## Wireframe

```text
+--------------------------------------------------------------------------+
|                   WORLD BOSS · Ironbark Colossus · Phase 2                |
|            [██████████████████|░░░░░░░░|░░░░░░]  58%                       |
|            [🛡 Status A] [⇡ Status B]        12 fighting  [Reward eligible ✓] |
+--------------------------------------------------------------------------+

Announcement (toast layer):
+--------------------------------------------------------------+
| ⏱ Ironbark Colossus appears in 2:00                          |
|   Whisperwood–Savanna border              [ Show route ]     |
+--------------------------------------------------------------+
```

Status icon names in the wireframe are placeholders; real boss states are defined in each boss document such as [[World Boss - Ironbark Colossus]].

## Related documents

- [[Boss Design Overview]] · [[Boss AI]] · [[Boss Rewards]] · [[World Boss - Ironbark Colossus]] · [[World Boss - Thunderhoof]] · [[World Boss - Abyssal Leviathan]] · [[World Boss - Ashwing Condor]]
- [[UI - Main HUD]] · [[UI - Notifications]] · [[Sound - Bosses]] · [[Test Cases - Bosses]]
