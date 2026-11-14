---
title: UI - Progression Interface
type: ui-screen
category: ui
status: mixed
priority: P1
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - progression
  - levelling
  - regions
  - goals
---

# UI - Progression Interface

> [!success] CONFIRMED
> Hidden progression luck improves egg-rarity and hatch odds; the formula may stay hidden (D-017). Bosses exist (D-012). Base progression can contribute to progression (D-022).

> [!info] PROPOSED
> Level cap 100, `XP(L) = round(100 × L^1.6)`, special unlocks at L1 / L10 / L25 ([[Canonical Proposed Values]] §13); region unlock requirements (§5, world layout **UNDECIDED** [[Open Questions#Q-001]]); Progression Score inputs (§8, formula **UNDECIDED** [[Open Questions#Q-017]]). Layout and milestone presentation are **PROPOSED**.

## Purpose

A single "where am I and what's next" screen: player level and XP, what the next levels unlock, which regions are open and what the next one needs, bosses defeated, base progress and collection progress. It turns long-term goals ([[Long-Term Goals and Endgame]]) into visible next steps.

## Layout

Tabs: **Overview · Regions · Bosses · Base · Collection**. Overview is a dashboard of the next goal in each area.

## Hierarchy

1. Level and XP.
2. Next unlock (special move or region).
3. Per-area progress cards.
4. Detail tabs.

## Elements

| Element | Tab | Type | Content | Behaviour |
|---|---|---|---|---|
| Level and XP | Overview | `Counter/Level` + `Bar/XP` | "Level 20 · 4,210 / 12,068 XP" | XP needed for L20 → L21 is `round(100 × 20^1.6) = 12,068` |
| Next special | Overview | Card | "Rally Cry unlocks at level 25" | Locked icon + level |
| Strength | Overview | Chip | "Strength 55" | Opens [[UI - Player Strength Display]] |
| Next region | Overview, Regions | Card | "Emerald Canopy: reach level 18 and defeat Dustmane" | Checklist with ticks |
| Region list | Regions | List of 8 + hub | Name, recommended levels, unlocked / locked, requirements | From [[Region Unlock Progression]] |
| Boss list | Bosses | Grid | 8 mini-bosses, 4 world bosses: defeated ✓ / not yet | Shows next world boss spawn time if known |
| Base progress | Base | `Bar/Progress` | "Module levels 14 / 44" | 44 from [[Canonical Proposed Values]] §12 |
| Collection | Collection | Counters | "Discovered 23 / 60 · Owned 17 / 60" | Opens [[UI - Animal Index Screen]] |
| Luck note | Overview | Caption + info icon | "Levelling up, discovering animals, defeating bosses, unlocking regions and upgrading your base all improve your egg odds." | Info opens current odds (read-only) via the egg odds view |

### Showing luck without the formula

> [!warning] UNDECIDED (Q-505)
> Whether the numeric Progression Score (0–1000) is shown to players. **PROPOSED** UI working assumption: do **not** show the number or the formula (D-017 allows it to stay hidden). Instead show (a) the list of activities that improve odds, and (b) a read-only view of the player's **current actual odds**, identical to the table in [[UI - Egg Rolling]]. Players always see the truth that matters: their odds.

The luck note must never imply that rolling or failing improves odds (see [[UI - Egg Rolling#Copy rules]]).

## Interactions

- Tap any card → its tab or the owning screen (Index, Strength, Base Upgrades).
- Region card "Show route" for unlocked regions.
- Boss card "Show route" when a boss is active.

## States

| State | Display |
|---|---|
| Level up just happened | Overview header celebrates (static under Reduced Motion) |
| Max level (100) | XP bar replaced with "Max level" |
| All regions unlocked | Regions tab header "All regions unlocked" |
| Requirement newly met | Tick animates; toast via [[UI - Notifications]] |

## Empty states

New player: Overview shows only Level 1, "Power Strike unlocked", the first region and the first mini-boss ([[Mini-Boss - Bramblehorn]]), plus "Defeat wild animals to earn XP and Cash."

## Error states

If the progression snapshot fails: "Couldn't load your progress" + Retry. Never show zeroed progress as if it were real.

## Loading states

Level and XP from replicated profile appear immediately; other tabs show skeleton rows until their data arrives.

## Mobile layout

Overview as a vertical stack of cards (one column); tabs as a scrolling bar; region and boss lists one per row.

## Desktop layout

Overview as a 2 × 3 card grid; tabs along the top; Regions tab shows a schematic map strip on the left and the list on the right (map art per [[World Overview and Map]]).

> [!note] Console / gamepad
> Cards are selectable; `ButtonL1`/`ButtonR1` switch tabs.

## Accessibility

- Locked / unlocked uses padlock / tick icons with text.
- XP shown as numbers, not only a bar.

## Roblox implementation notes

```text
Panels/Progression (Frame)
├─ Tabs (Frame, UIListLayout)
└─ Pages → Overview (UIGridLayout of cards), Regions (ScrollingFrame + UIListLayout), Bosses (UIGridLayout), Base, Collection
```

- All values are read from server-replicated profile data ([[Service - ProgressionService]], [[Schema - Player Progression]], [[Schema - Unlocks and Boss Progress]]). The client never derives unlocks itself; requirement ticks come from the server.
- The odds view reuses the Egg Rolling odds table component in read-only mode, fed by the same quote call.

## Wireframe

```text
+----------------------------- Progress ----------------------------------[X]+
| [Overview●] [Regions] [Bosses] [Base] [Collection]                          |
|-----------------------------------------------------------------------------|
| Level 20   [████░░░░░░░░] 4,210 / 12,068 XP      Strength 55 ›              |
| +----------------------+ +-----------------------+ +----------------------+ |
| | Next special         | | Next region           | | Collection           | |
| | Rally Cry at Lv 25   | | Emerald Canopy        | | Discovered 23/60     | |
| | 🔒                    | | ✓ Level 18  ✗ Dustmane| | Owned 17/60          | |
| +----------------------+ +-----------------------+ +----------------------+ |
| +----------------------+ +-----------------------+                          |
| | Bosses 3/12          | | Base 14/44 levels     |                          |
| +----------------------+ +-----------------------+                          |
| (i) Levelling, discoveries, bosses, regions and base upgrades improve your   |
|     egg odds.  [See my current odds]                                         |
+-----------------------------------------------------------------------------+
```

## Related documents

- [[Player Progression and Levelling]] · [[Progression Score Specification]] · [[Dynamic Progression Luck]] · [[Region Unlock Progression]] · [[Long-Term Goals and Endgame]]
- [[UI - Player Strength Display]] · [[UI - Animal Index Screen]] · [[UI - Egg Rolling]] · [[UI - Boss Health Bar]]
- [[Service - ProgressionService]] · [[Schema - Player Progression]]
