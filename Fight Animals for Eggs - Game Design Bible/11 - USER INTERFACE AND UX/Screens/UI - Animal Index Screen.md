---
title: UI - Animal Index Screen
type: ui-screen
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - index
  - collection
  - discovery
  - variants
---

# UI - Animal Index Screen

> [!success] CONFIRMED
> - Defeating wild animals registers them in the index, and the index distinguishes **discovered** animals from **owned** animals (D-029).
> - Special variants exist for selected species (D-028); how they are obtained is **UNDECIDED** ([[Open Questions#Q-006]]).
> - Launch target of 60 animals (D-004).

> [!info] PROPOSED
> The four-state presentation, what is revealed at each state, the hint rules and the layout are **PROPOSED**. Index behaviour is specified in [[Animal Index Feature Specification]].

## Purpose

A collection book of every species. It gives players long-term goals (find, then own, then collect variants), shows where to look, and feeds their sense of progress. Unique discoveries also count towards the Progression Score ([[Progression Score Specification]]), but the screen never shows that score (Q-505).

## Discovery states

| State | Trigger | Card shows | Detail shows |
|---|---|---|---|
| **Undiscovered** | Never defeated or owned | Dark silhouette, "???", rarity ornament, catalogue number | Rarity, and home region **only if that region is unlocked** (**PROPOSED** hint rule) |
| **Discovered** | Defeated in the wild (D-029) | Full-colour portrait, name, `Chip` "Discovered" | Name, family, role, home region, rarity, description; "Not owned yet — appears in [Rarity] eggs" |
| **Owned** | At least one instance owned (hatching also marks as discovered, **PROPOSED**) | Portrait, name, `Chip` "Owned ×n", highest ascension stars | Everything above + owned count, highest ascension, "View in Animals" |
| **Variants** | Per variant, per species | Row of variant chips under the card (Owned / Seen / Unknown) | Variant gallery with each eligible variant in one of three sub-states |

Variant sub-states (**PROPOSED**): *Unknown* (grey chip with "?"), *Seen* (encountered but not owned, outlined chip), *Owned* (filled chip). Whether variants can be "seen" at all depends on how they are acquired (Q-006); if they cannot, the Seen state is simply never used.

> [!info] PROPOSED — Secret silhouettes
> Secret-tier undiscovered entries show a generic "?" egg silhouette rather than the animal's outline, to preserve surprise. Rarity is still shown.

## Layout

- Header: completion counters, filters.
- Body: grid of `Card/IndexEntry` in catalogue order (1–60), grouped by family or region on demand.
- Detail: side panel or sheet.

## Hierarchy

1. Completion counters ("Discovered 23 / 60 · Owned 17 / 60").
2. The grid and each entry's state.
3. Detail with hints and links.
4. Filters and grouping.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| Completion counters | `Counter/Capacity` ×2 + `Bar/Capacity` ×2 | Discovered x / 60, Owned x / 60 | Total read from config (60 at launch) |
| Variant counter | Counter | "Variants owned 2 / n" | n = eligible variants in [[Animal Variants]] |
| Group by | Tabs | All · Family · Region · Rarity | `Tab/Bar` |
| State filter | Chips | Undiscovered · Discovered · Owned · Has variants | Multi-select |
| Index card | `Card/IndexEntry` | See discovery states | Tap opens detail |
| Detail: art | `Preview/3D` (owned or discovered) or silhouette image | Rotatable for owned | Static image for discovered on Compact to save frame rate |
| Detail: facts | Text block | Family, role, region, rarity | Links to the species page are internal only (not player-facing) |
| Detail: where to find | Row | Region name + "Wild" and/or "[Rarity] eggs" | Region shown as locked text if not unlocked |
| Detail: variant gallery | Row of chips | Variant names (e.g. Golden, Diamond) and sub-state | Tap a chip for its art if owned |
| New discovery badge | `Chip/New` | "NEW" | Clears when the entry is viewed |

## Interactions

- Defeating a new species triggers a toast "New animal discovered: Boar" with "View in Index" ([[UI - Notifications]]).
- Tapping a discovered-but-not-owned entry offers "Find eggs" (route to the egg shrine) — copy stays factual: "Boar can hatch from Common eggs." It never suggests the next egg is more likely to contain it (D-018).
- Owned entry → "View in Animals" opens [[UI - Animal Inventory]] filtered to that species.

## States

| State | Display |
|---|---|
| Normal | Grid |
| New discoveries unviewed | Badge count on the menu entry and on the group tab |
| 100% discovered / owned | Celebration banner (static under Reduced Motion) |

## Empty states

A new player with no discoveries sees all 60 cards as Undiscovered plus a tip: "Defeat wild animals to discover them." The grid is never empty, because all species always have a card.

## Error states

If the discovery index fails to load, show "Couldn't load your Index" with Retry; never show all entries as undiscovered by mistake (a failed load must not look like lost progress).

## Loading states

Card layout (60 cells) renders immediately with silhouettes as skeletons; states fill in when the discovery snapshot arrives ([[Schema - Discovery Index]]).

## Mobile layout

Five columns at Compact reference width; variant chips collapse to a single "+2 variants" chip. Detail is a full-height sheet.

## Desktop layout

Eight columns; detail panel on the right; hover tooltip shows state and region.

> [!note] Console / gamepad
> `ButtonL1`/`ButtonR1` change grouping tabs; `ButtonX` opens the state filter; grid uses standard selection.

## Accessibility

- Each state is identified by text chip **and** treatment (silhouette, colour, filled versus outlined), not by saturation alone.
- Counters are text.
- Variant sub-states use chip shape (outlined versus filled) and a text label.

## Roblox implementation notes

```text
Panels/AnimalIndex (Frame)
├─ Header → Counters, GroupTabs (UIListLayout), StateFilter
├─ Grid (ScrollingFrame + UIGridLayout + UIAspectRatioConstraint)
└─ Detail (Frame) → Art (ImageLabel or ViewportFrame), Facts, VariantRow (UIListLayout horizontal)
```

- Discovery state is server-owned ([[Service - IndexService]]); the client never marks an entry discovered from a local kill event. A discovery toast appears only after the server confirms the registration.
- Undiscovered entries must not leak names: the client receives only catalogue number, rarity and (if unlocked) region for undiscovered species. Names and art IDs for undiscovered species are not sent (**PROPOSED** anti-datamining measure; full secrecy is impossible because assets ship with the game).

## Wireframe

```text
+------------------------------- Animal Index -------------------------------[X]+
| Discovered 23/60 [██████░░░░]   Owned 17/60 [████░░░░░░]   Variants 2/n      |
| [All] [Family] [Region] [Rarity]          Show: [Undisc][Disc][Owned][Var]    |
|-------------------------------------------------------------------------------|
| #01 Rabbit  #02 Squirrel #03 Hedgehog #04 ???      #05 Frog                    |
| Owned ×3    Owned ×1     Discovered   (silhouette) Owned ×2                    |
| [G][?]      [?]          [?]          Common       [S]                         |
| #06 Duck    #07 ???      #08 Boar     #09 Goat     #10 ???                     |
| Discovered  (silhouette) NEW Disc.    Owned ×1     (silhouette)                |
|-------------------------------------------------------------------------------|
| Detail: Boar · Common · Bruiser · Whisperwood Forest                           |
| Discovered. Not owned yet. Can hatch from Common eggs.   [Find eggs]           |
+-------------------------------------------------------------------------------+
  [G] owned variant   [?] unknown variant   [S] seen variant
```

## Related documents

- [[Animal Index Feature Specification]] · [[Animal Index]] · [[Animal Variants]] · [[Schema - Discovery Index]] · [[Service - IndexService]]
- [[UI - Animal Inventory]] · [[UI - Egg Rolling]] · [[UI - Notifications]] · [[Variant Visual Treatments]]
