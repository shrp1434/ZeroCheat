---
title: UI - Animal Inventory
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - inventory
  - animals
  - collection
---

# UI - Animal Inventory

> [!warning] UNDECIDED
> Owned-animal storage capacity is **UNDECIDED** ([[Open Questions#Q-022]]); the UI uses the prototyping working assumption of **100** from [[Canonical Proposed Values]] §7 and reads the real cap from server config. Whether animals can be released is **UNDECIDED** (Q-509).

> [!info] PROPOSED
> Layout, filters, sort orders, the stack view and the detail panel are **PROPOSED**.

## Purpose

The player's collection of owned animal *instances*: browse, compare, inspect and act on them. It is the entry point to [[UI - Ascension]] and, at base, to [[UI - Team Selection]]. It is different from the [[UI - Animal Index Screen]], which is a catalogue of species (discovered versus owned).

## Layout

- Header: title, capacity counter, search, filter and sort controls, Stack toggle.
- Body: grid of `Card/Animal`.
- Detail: right-side panel (Large) or full-height sheet (Compact) with 3D preview, stats, ability and actions.

## Hierarchy

1. Grid of animals (rarity frames make value scannable).
2. Capacity counter (warns before a hatch would overflow).
3. Detail panel actions (Ascend, Edit team).
4. Filters and sort.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Capacity counter | `Counter/Capacity` + `Bar/Capacity` | "Animals 74 / 100" | Warning at 80%, "Full" at 100% |
| Search | `TextBox` | Species name | Filters as the player types (debounced 0.2 s) |
| Filters | `Btn/Icon` → sheet | Rarity, role, family, region, ascension level, variant, equipped, guard, favourite | Active filter count badge |
| Sort | Dropdown | Rarity (default, high first), ascension, newest, name, species | Remembered per player in settings |
| Stack toggle | Toggle | "Group duplicates" | Stack view shows one card per species with "×4" count — useful for ascension planning |
| Animal card | `Card/Animal` | Portrait, name, rarity, role, stars, chips | Tap opens detail |
| Detail: 3D preview | `Preview/3D` | Idle animation, rotate by drag / right stick | One animated viewport |
| Detail: stats | Table | HP, ATK, DEF, attack speed, move speed (from [[Animal Statistics Database]] with ascension bonus applied by the server) | Ascension bonus shown as "+16%" beside base |
| Detail: ability | Row | Ability icon, name, `Chip/Manual` or `Chip/Auto`, cooldown, description | From [[Animal Abilities Catalogue]] |
| Detail: variant | Chip | "Golden" etc. if a variant | Per [[Animal Variants]] |
| Detail: duplicates | Caption | "You own 3 more Wolves" | Links to Ascension |
| Ascend | `Btn/Primary` | "Ascend (A2 → A3)" | Opens [[UI - Ascension]]; disabled with reason at A5 |
| Edit team | `Btn/Secondary` | "Edit team" | Opens Team Selection (locked view away from base) |
| Favourite | `Btn/Icon` | Heart | Favourites cannot be selected as ascension fodder (**PROPOSED**) |
| Release | `Btn/Danger` | "Release" | Hidden unless Q-509 approves releasing |

## Interactions

- Tap card → detail. Swipe left/right in the detail sheet (Compact) or `ButtonL1`/`ButtonR1` moves to the previous/next animal in the current sort.
- Long-press card → quick actions (Favourite, Ascend, Compare).
- Compare (**PROPOSED**): select two animals to see stats side by side.
- Equipped and guard animals show chips; tapping Ascend on an equipped animal is allowed (the animal is the *target*, not the fodder).

> [!warning] UNDECIDED (Q-509)
> Whether players can release (delete) owned animals to free storage, and what, if anything, they receive. Without a release action, a full collection can only be reduced through ascension. The UI reserves a `Btn/Danger` slot that requires a hold-to-confirm and names the animal, rarity and ascension level being released.

## States

| State | Display |
|---|---|
| Normal | Grid + header |
| Near capacity (≥ 80%) | Capacity bar warning; toast when crossing 80% |
| Full | "Full" label; hatching is blocked with reason in [[UI - Egg Hatching]] (Q-508) |
| Detail open | Grid dims (Large) or is covered (Compact) |
| In combat | View only; actions disabled with reason |
| Animal just hatched | `Chip/New` on first-owned species until viewed |

## Empty states

- No animals: `Empty/Block` "You don't own any animals yet. Hatch eggs to start your collection." with "Go to eggs".
- Filters exclude everything: "No animals match" + "Clear filters".

## Error states

| Situation | Copy |
|---|---|
| Collection page failed to load | "Couldn't load your animals. Try again." + Retry |
| Animal removed while detail open (for example stolen in a raid, [[Animal Theft Rules]]) | Detail closes; toast "Wolf is no longer in your collection" |
| Action rejected (in combat) | "Finish combat first" |

## Loading states

Grid loads in pages of 40 (**PROPOSED**) with skeleton cards. Portraits load through `ContentProvider:PreloadAsync` for the visible page; off-screen portraits load on scroll.

## Mobile layout

Four-column grid at Compact reference width, header controls collapsed into one filter button plus sort. Detail is a full-height sheet with the preview at the top 40% and actions pinned at the bottom.

## Desktop layout

Six-to-eight-column grid on the left 62%, persistent detail panel on the right 38%. Hover shows a stat tooltip.

> [!note] Console / gamepad
> Grid cells are `Selectable`; `ButtonA` opens detail, `ButtonX` filters, `ButtonY` toggles Stack view, right stick rotates the 3D preview.

## Accessibility

- Rarity is readable by ornament and letter code on cards and by name in detail.
- Stats use text values; bars are optional extras.
- Hold-to-confirm for Release (if it ships) has the tap-twice alternative.

## Roblox implementation notes

```text
Panels/AnimalInventory (Frame)
├─ Header (Frame, UIListLayout horizontal) → Capacity, Search (TextBox), FilterButton, SortButton, StackToggle
├─ Grid (ScrollingFrame, AutomaticCanvasSize Y, UIGridLayout, UIPadding)
│  └─ Card template clones (ImageButton + UIAspectRatioConstraint 0.82 + UICorner + UIStroke)
└─ Detail (Frame) → Preview (ViewportFrame + WorldModel), Stats (UIListLayout), Actions
```

- Grid cells are **virtualised** (**PROPOSED**): only visible rows plus one buffer row are instantiated; the rest are recycled on `CanvasPosition` change, so 100+ animals stay smooth on mobile.
- The collection is server-owned ([[Schema - Animal Collection]], [[Animal Collection System]]); the client renders a replicated read-only view. Stats displayed come from the server so ascension and base bonuses match combat exactly.
- Portraits are pre-rendered images (UI-### assets in the [[Asset Register]]), not one `ViewportFrame` per card.

## Wireframe

```text
+-------------------------------- Animals -------------------------------[X]+
| Animals 74/100 [████████░░]  [Search____] [Filters(2)] [Sort: Rarity▾] [Stack]|
|------------------------------------------------------+---------------------|
| +------+ +------+ +------+ +------+                  |  (3D Wolf preview)  |
| |Tiger | |Wolf E| |Wolf  | |Owl   |                  |  Wolf  · Rare · ★★  |
| |Epic★ | |Rare★★| |Rare  | |Unc   |                  |  Bruiser · Forest   |
| +------+ +------+ +------+ +------+                  |  HP 434 (+16%)      |
| +------+ +------+ +------+ +------+                  |  ATK 39  DEF 22     |
| |Fox   | |Boar  | |Rabbit| |Crab  |                  |  Ability [TAP] …    |
| |Unc   | |Com   | |Com N | |Com   |                  |  You own 3 more     |
| +------+ +------+ +------+ +------+                  |  [ Ascend A2→A3 ]   |
|                                                      |  [ Edit team ]  [♥] |
+------------------------------------------------------+---------------------+
 E = Equipped   N = NEW   ★ = ascension level
```

Wireframe stats are Wolf (Rare Bruiser) at A2 from the [[Canonical Proposed Values]] §3 formula before its species tweak (HP 200 × 1.70 × 1.10 = 374, +16% = 434); real values come from [[Animal Statistics Database]].

## Related documents

- [[Animal Collection System]] · [[Schema - Animal Collection]] · [[Animal Statistics Database]] · [[Animal Abilities Catalogue]]
- [[UI - Ascension]] · [[UI - Team Selection]] · [[UI - Animal Index Screen]] · [[UI - Egg Hatching]]
- [[Test Cases - Inventory and Storage]]
