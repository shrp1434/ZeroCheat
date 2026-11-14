---
title: UI - Egg Storage
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - eggs
  - storage
  - raids
---

# UI - Egg Storage

> [!success] CONFIRMED
> - Storage starts at **Backpack 10 + Base 50 = 60** (D-021).
> - **Backpack eggs can never be stolen.** Base-stored eggs can be stolen during an eligible raid (D-021, D-024).
> - Extra space can be bought; the currency and pricing are **UNDECIDED** ([[Open Questions#Q-009]], [[Open Questions#Q-010]]).

> [!info] PROPOSED
> Expansion steps (+5 backpack ×3 to 25; +25 base ×6 to 200) are **PROPOSED** in [[Canonical Proposed Values]] §11. Transfers only at the base, the layout and the full-capacity behaviour are **PROPOSED**.

## Purpose

Show every egg the player owns, make the safety difference between the two stores impossible to miss, let the player move eggs between them at base, and route to hatching and merging. It is also where full-capacity problems are explained and resolved.

## Layout

Two side-by-side stores (Large) or two tabs (Compact):

- **Backpack** with a `Chip/Safe` header: "Safe from raids".
- **Base storage** (the [[Module - Egg Vault]]) with a `Chip/Raidable` header: "Can be stolen in raids".

A contextual action bar at the bottom shows Move, Hatch and Merge for the current selection.

## Hierarchy

1. Capacity counters for both stores.
2. Safety labels.
3. Egg grids grouped by rarity.
4. Action bar.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Backpack header | `Counter/Capacity` + `Chip/Safe` | "Backpack 7 / 10 · Safe from raids" | Info icon: "Eggs in your backpack can never be stolen." |
| Base header | `Counter/Capacity` + `Chip/Raidable` | "Base storage 31 / 50 · Raidable" | Info icon explains raids and shields, links to [[Shield Mechanics]] summary |
| Capacity bars | `Bar/Capacity` | Fill | Warning at 80%, "Full" at 100% |
| Egg grid (per store) | `ScrollingFrame` + `UIGridLayout` | `Card/Egg`, grouped by rarity, highest first | Multi-select by tap |
| Rarity group header | Row | "Rare ×4" | Tap selects all in group (respecting destination space) |
| Move to backpack | `Btn/Secondary` | "Move to backpack (safe)" | At base only; disabled if backpack full |
| Move to base | `Btn/Secondary` | "Move to base storage" | At base only; confirm modal warns the eggs become raidable |
| Hatch | `Btn/Primary` | "Hatch (3)" | Opens [[UI - Egg Hatching]] with selection (max 5) |
| Merge | `Btn/Secondary` | "Merge" | At base, with a station, opens [[UI - Egg Merging]] |
| Expand | `Btn/Ghost` | "Expand storage" | Hidden until Q-009 and Q-010 are decided; then opens the expansion offer |
| Get eggs | `Btn/Ghost` | "Get eggs" | Routes to the egg shrine |

## Interactions

- Selecting eggs from both stores at once is allowed for Hatch (subject to location rules) but Move acts on one direction at a time.
- **Move to base** shows `Modal/Confirm`: "These 3 eggs will be stored at your base, where raiders can steal them while you are online." Players can tick "Don't show again this session" (**PROPOSED**).
- **Move to backpack** needs no confirmation.
- Away from base, both grids are viewable but Move and Merge are disabled with "Return to your base to move eggs".

## States

| State | Display |
|---|---|
| Normal at base | Full controls |
| Away from base | View only for base storage (**PROPOSED**); backpack eggs can still be selected for hatching outside combat |
| Backpack full (10 / 10 or expanded max) | Backpack header in "Full" state; toast on reaching full; roll destination changes per Q-501 |
| Base storage full (50 / 50 or expanded max) | Base header "Full"; Move to base disabled; merge may be blocked (see [[UI - Egg Merging]]) |
| Both full | `Empty/Block`-style banner: "Egg storage full. Hatch or merge eggs to make space." with Hatch and Merge shortcuts |
| Own base under raid | Base grid shows a red "Raid in progress" banner; moves disabled (**PROPOSED**, Q-506) |
| Egg stolen | Stolen eggs vanish from the base grid with a short fade and a toast ([[UI - Raid Interface]]) |

## Empty states

- Both empty: "No eggs yet. Roll eggs at the egg shrine." + "Get eggs".
- Backpack empty only: "Your backpack is empty. Eggs here are safe from raids."
- Base empty only: "Base storage is empty."

## Error states

| Reason code (illustrative) | Copy |
|---|---|
| `NotAtOwnBase` | "Return to your base to move eggs." |
| `DestinationFull` | "Not enough space. Backpack 10 / 10." |
| `BaseUnderRaid` | "Your base is under raid. Egg moves are paused." |
| `EggNotFound` | "That egg is no longer in storage." (grid reconciles) |

## Loading states

Both headers show counters from the replicated inventory immediately; grids fill progressively. If inventory is not yet loaded, counters show skeletons and all actions are disabled.

## Mobile layout

Two tabs, "Backpack 7/10 · Safe" and "Base 31/50 · Raidable", each tab label carrying its chip icon. Action bar pinned at the bottom. Four-column grids.

## Desktop layout

Two columns side by side with the move buttons as arrows between them ("→ Base", "← Backpack"), action bar under both.

> [!note] Console / gamepad
> `ButtonL1`/`ButtonR1` switch store focus; `ButtonA` selects; `ButtonX` moves the selection to the other store; `ButtonY` hatches.

## Accessibility

- Safe versus raidable is shown with icon + text on headers, tabs and each egg card; never colour alone ([[UI Accessibility Standards]] §2).
- Capacity is written as "x / y" text and "Full".

## Roblox implementation notes

```text
Panels/EggStorage (Frame)
├─ Backpack (Frame) → Header (Counter, Chip), Grid (ScrollingFrame + UIGridLayout)
├─ Base (Frame) → Header, Grid
└─ ActionBar (Frame, UIListLayout horizontal)
```

- Inventory is server-owned ([[Schema - Egg Inventory]], [[Egg Storage]]); transfers send `MoveEggs(eggIds, toLocation, requestId)` and the server validates location (`AtOwnBase`), capacity, raid state and ownership as one transaction.
- Capacities are read from the server (including any purchased expansion), never hard-coded as 10 / 50 on the client.
- Egg cards are pooled; at most 60 cells at launch capacity, up to 225 with proposed maximum expansion, so virtualisation follows [[UI - Animal Inventory]].

## Wireframe

```text
+--------------------------------- Eggs -------------------------------------[X]+
| BACKPACK 7/10  [🛡 Safe from raids]   |   BASE STORAGE 31/50 [⚠ Raidable]     |
| [███████░░░]                          |   [██████░░░░]                         |
| Rare ×1   [R]                         |   Epic ×1   [E]                        |
| Unc ×2    [U][U]                      |   Rare ×4   [R][R][R][R]               |
| Common ×4 [C][C][C][C]                |   Unc ×9    [U][U][U][U][U]…           |
|                                       |   Common ×17 [C][C][C][C][C]…          |
|                 [← Backpack]  [→ Base]                                          |
| Selected 3      [ Merge ]   [ Hatch (3) ]                [Get eggs]           |
+-------------------------------------------------------------------------------+
```

## Related documents

- [[Egg Storage]] · [[Module - Egg Vault]] · [[Storage Expansion Economics]] · [[Egg Theft Rules]] · [[Schema - Egg Inventory]]
- [[UI - Egg Hatching]] · [[UI - Egg Merging]] · [[UI - Egg Rolling]] · [[UI - Raid Interface]] · [[UI - Shop]]
- [[Test Cases - Inventory and Storage]]
