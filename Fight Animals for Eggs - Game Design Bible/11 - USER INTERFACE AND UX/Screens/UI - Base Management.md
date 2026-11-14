---
title: UI - Base Management
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - base
  - modules
  - raids
---

# UI - Base Management

> [!success] CONFIRMED
> - Every player owns a personal modular base whose sections are upgraded individually (D-022).
> - The team can only be changed at the base (D-010).
> - Bases are protected by shields and physical defences; offline bases cannot be raided (D-024).

> [!info] PROPOSED
> Module list and costs ([[Canonical Proposed Values]] §12; availability **UNDECIDED** [[Open Questions#Q-007]]), the overview layout and the raid-status summary are **PROPOSED**.

## Purpose

The base's control room. One screen summarises every module, egg storage, defence and shield state, and gives one-tap access to the base-only actions (team, merging, upgrades, storage transfers).

## Layout

- Header: base name, plot stage, "At your base" or "Away" status.
- Protection strip: raid eligibility (online = raidable), shield status, defence summary.
- Module grid: one `Card/Module` per built or buildable module.
- Quick actions: Team, Eggs, Merge, Guards.
- Raid log: last raids on this base (summary).

## Hierarchy

1. Protection status (is my base at risk right now?).
2. Quick actions (the base-only things the player came here to do).
3. Module grid and upgrade availability.
4. Raid log.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Location status | Chip | "At your base" / "Away from base" | Away: base-only actions disabled with reason |
| Raid exposure | Chip + text | "Raidable while you're online" / "Protected: shield active" | Explains offline protection: "Your base can't be raided while you're offline." ([[Raid Eligibility and Offline Protection]]) |
| Shield status | `Bar/Progress` + text | Active with time remaining, or recharging, or none | Behaviour per [[Shield Mechanics]]; acquisition **UNDECIDED** ([[Open Questions#Q-030]]) |
| Defence summary | Row | Defence Station level, traps / turrets count, guards assigned | Links to Defence Station upgrades |
| Storage summary | `Counter/Capacity` ×2 | "Base storage 31 / 50 · Raidable", "Backpack 7 / 10 · Safe" | Opens [[UI - Egg Storage]] |
| Module cards | `Card/Module` | Name, level L0–L5, effect summary, next cost | Tap opens [[UI - Base Upgrades]] for that module |
| Plot stage | `Card/Module` | "Plot stage 2 / 4 · next 15,000 Cash" | Plot expansion ([[Base Layout and Plot Expansion]]) |
| Team button | `Btn/Primary` | "Team" | Opens [[UI - Team Selection]] |
| Merge button | `Btn/Secondary` | "Merge eggs" | Opens [[UI - Egg Merging]]; build offer if no station |
| Guards button | `Btn/Secondary` | "Guards" | Opens the guard assignment sheet; which animals defend is **UNDECIDED** ([[Open Questions#Q-033]]) |
| Raid log | List | "Raided 2 h ago · 4 eggs, 1 animal taken" | Opens summary; compensation per [[Raid Rewards and Defender Compensation]] |

### Guard assignment sheet

Because [[Open Questions#Q-033]] (and [[Open Questions#Q-035]] for the defender's own team) are undecided, the sheet is built as a configurable list of guard slots whose count comes from server config (driven by [[Module - Animal Pens]] level). If the decision is "equipped team only", the sheet is hidden and the Guards button becomes an explanation.

## Interactions

- Tap a module → [[UI - Base Upgrades]].
- Quick actions open their panels; Back returns here.
- Away from base: the screen is a read-only overview (**PROPOSED**), with "Show route to base".
- During a raid on this base: the protection strip becomes a red "Raid in progress" banner with raider count and a "Defend" route, and base actions lock per the Q-506 proposal.

## States

| State | Display |
|---|---|
| At base, idle | Full controls |
| Away | Read-only; actions disabled with reason |
| Shield active | Shield bar with remaining time |
| Under raid | Red banner (icon + text), live counters from [[UI - Raid Interface]] |
| Upgrade affordable | Module card shows an "Upgrade available" chip |
| Module unbuilt | Card shows "Build · cost" |

## Empty states

New base with no modules: module grid shows buildable cards with the first recommended one highlighted ("Start with Training Grounds to boost your Strength", **PROPOSED** onboarding hint per [[New Player Onboarding]]).

## Error states

| Situation | Copy |
|---|---|
| Base data failed to load | "Couldn't load your base." + Retry; base-only actions disabled |
| Action while away | "Return to your base to do this." |
| Action during raid | "Your base is under raid." |

## Loading states

Header and protection strip render first from replicated attributes; module grid uses skeleton cards until base data arrives ([[Schema - Base Data]]).

## Mobile layout

Protection strip at the top as a single tappable row (expands to details); quick actions as four large buttons (64 high) in a 2 × 2 grid; module grid in two columns below; raid log in a collapsible section.

## Desktop layout

Left column: protection strip, storage summary and quick actions. Right two-thirds: module grid (three columns) and raid log.

> [!note] Console / gamepad
> Focus starts on the Team quick action. `ButtonX` opens the raid log; modules are a standard selectable grid.

## Accessibility

- Raid danger uses icon + text + banner, not colour alone; the raid alert also has a sound ([[Sound - Base and Raid Alerts]]).
- Shield time remaining is shown as text ("Shield: 1 h 12 m").

## Roblox implementation notes

```text
Panels/BaseManagement (Frame)
├─ Header (Frame)
├─ ProtectionStrip (Frame) → RaidExposure, ShieldBar, DefenceSummary
├─ QuickActions (Frame, UIGridLayout 2x2 on Compact)
├─ Modules (ScrollingFrame + UIGridLayout) → Card/Module clones
└─ RaidLog (Frame, UIListLayout)
```

- All base state is server-owned ([[Service - BaseService]], [[Schema - Base Data]]). Location (`AtOwnBase`) and raid state are server attributes.
- Module cards read level and cost from server config so costs always match [[Base Upgrade System]].
- The screen performs no actions itself; it opens other panels that send intents.

## Wireframe

```text
+------------------------------- Your Base -------------------------------[X]+
| Sunny Burrow · Plot stage 2/4                 [At your base]                |
| [⚠ Raidable while you're online]  Shield: recharging  Defences: L2 · 3 guards|
|-----------------------------------------------------------------------------|
| [  Team  ]  [ Eggs 31/50 ]  [ Merge eggs ]  [ Guards ]                      |
|-----------------------------------------------------------------------------|
| +------------+ +------------+ +------------+ +------------+                 |
| |Training    | |Egg Vault   | |Defence     | |Shield Gen. |                 |
| |Grounds L3  | |L2          | |Station L2  | |L1          |                 |
| |Up: 23,438  | |Up: 9,375   | |Up: 12,500  | |Up: 6,250   |                 |
| +------------+ +------------+ +------------+ +------------+                 |
| +------------+ +------------+ +------------+ +------------+                 |
| |Mult. Shrine| |Trophy Hall | |Animal Pens | |Merge Stn   |                 |
| |Build 3,000 | |L1          | |L1          | |L1          |                 |
| +------------+ +------------+ +------------+ +------------+                 |
| Raid log: Raided 2 h ago · 4 eggs, 1 animal taken  [View]                   |
+-----------------------------------------------------------------------------+
```

Each card shows the cost of the **next** level from [[Canonical Proposed Values]] §12, e.g. Training Grounds L3 → L4 = 1,500 × 2.5³ = 23,438 Cash. The base name is placeholder text.

## Related documents

- [[Player Base System]] · [[Base Upgrade System]] · [[Base Defence Overview]] · [[Animal Guards and Base Defence AI]] · [[Shield Mechanics]]
- [[UI - Base Upgrades]] · [[UI - Team Selection]] · [[UI - Egg Storage]] · [[UI - Egg Merging]] · [[UI - Raid Interface]]
- [[Service - BaseService]] · [[Test Cases - Bases and Upgrades]]
