---
title: UI and UX Index
type: index
category: ui
status: mixed
priority: P0
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - ux
  - index
---

# UI and UX Index

Everything the player sees and touches outside the 3D world: the HUD, every panel, modal and notification, and the rules that keep them consistent across **phone, tablet, PC and console**. The interface is designed mobile-first and is purely presentational: every outcome (rolls, hatches, purchases, raids) is decided and validated on the server ([[Server-Client Responsibilities]]).

## How to read this folder

1. Start with the [[UI Design System]]: components, spacing, touch targets, layers and the modal stack.
2. Use the [[UI Navigation Map]] to see how screens connect, which are available in each context (base, combat, raid) and the input bindings.
3. Check the [[UI Accessibility Standards]] before designing or reviewing any screen.
4. Each screen document follows the same structure: purpose, layout, hierarchy, elements, interactions, states (normal, empty, error, loading), mobile and desktop layouts with a console note, accessibility, Roblox implementation notes, a text wireframe and, where the interaction is complex, a Mermaid flow. New screens use [[Template - UI Screen]].

Colours, fonts and surface styling are owned by the art team: [[Colour Palette]], [[Typography]] and [[UI Visual Styling]].

## Foundations

| Document | What it covers |
|---|---|
| [[UI Design System]] | Component library (buttons, cards, rarity frames, tabs, modals, toasts, bars, counters), spacing scale, touch targets, z-order and modal stack |
| [[UI Navigation Map]] | Screen graph, entry points, availability by context, Back rules, input bindings for touch, keyboard and gamepad |
| [[UI Accessibility Standards]] | Contrast, text size, colour independence, motion and flashing, input alternatives, audio equivalents, test checklist |

## Screens

| Screen | One-line description |
|---|---|
| [[UI - Main HUD]] | Always-on combat and status layer: health, level, Cash, specials, dodge, menu access and the team lock indicator |
| [[UI - Player Strength Display]] | The player's own Strength (separate from animal strength, D-007) and its breakdown |
| [[UI - Animal Team Display]] | The three equipped animals in combat: health, manual versus automatic abilities (D-008) and target commands (D-009) |
| [[UI - Team Selection]] | Choosing exactly three animals, editable only at the player's own base (D-010), with a locked state elsewhere |
| [[UI - Animal Inventory]] | Grid of owned animals with filters, details, 3D preview and entry to ascension and team editing |
| [[UI - Animal Index Screen]] | Collection book of all 60 species: Undiscovered, Discovered, Owned and variants (D-029) |
| [[UI - Egg Rolling]] | Buying egg rolls with Cash, with the player's current actual odds shown before purchase (D-017, D-041) |
| [[UI - Egg Hatching]] | Selecting and hatching up to five eggs at once (D-016) with per-pool odds and the reveal |
| [[UI - Egg Storage]] | Backpack 10 and base storage 50, safe versus raidable eggs, transfers and full-capacity states |
| [[UI - Ascension]] | Consuming duplicates to ascend an animal while keeping the original (D-019) |
| [[UI - Egg Merging]] | Three same-rarity eggs into one of the next rarity at the Egg Merging Station (D-020) |
| [[UI - Base Management]] | Base overview: modules, storage, shield, guards and access to base-only actions |
| [[UI - Base Upgrades]] | Upgrading each module L1–L5 with costs, effects and the visual change preview |
| [[UI - Raid Interface]] | Attacker and defender raid flows, the "x / 3" animal counter and configurable egg counter |
| [[UI - PvP Interface]] | Opt-in PvP status and combat UI, built to support any activation method (Q-011) |
| [[UI - Boss Health Bar]] | Mini-boss and world-boss bars, phases, spawn announcements and contribution status |
| [[UI - Notifications]] | Toasts, banners, server announcements, the critical raid alert and the notification log |
| [[UI - Settings]] | Audio, graphics, controls, accessibility and gameplay preferences |
| [[UI - Progression Interface]] | Level and XP, unlocks, regions, bosses, base and index milestones |
| [[UI - Shop]] | Robux and Cash products with fair-monetisation rules; never sells Cash for Robux (D-044 proposed) |

## Status summary

> [!success] CONFIRMED rules reflected throughout
> Team of exactly 3, changeable only at base (D-006, D-010); manual and automatic abilities (D-008); auto-targeting with manual commands (D-009); odds shown before commit, never changed silently (D-017); independent hatches (D-018); hatch up to 5 (D-016); storage 10 + 50 with backpack eggs never stealable (D-021); max 3 animals stolen per raid (D-024); index distinguishes discovered from owned (D-029).

> [!warning] UNDECIDED items with UI impact
> Raid duration ([[Open Questions#Q-012]]), egg theft limit ([[Open Questions#Q-013]]), PvP activation ([[Open Questions#Q-011]]), defeat penalties ([[Open Questions#Q-014]]), boss rewards ([[Open Questions#Q-015]]), storage expansion currency and price ([[Open Questions#Q-009]], [[Open Questions#Q-010]]), animal storage cap ([[Open Questions#Q-022]]). New UI questions Q-501 to Q-510 are listed in the documents that raise them and are awaiting entry in [[Open Questions]].

## Related documents

- [[M18 - UI and UX]] · [[Client Controllers]] · [[Remote Communication Contract]]
- [[Art Direction Index]] · [[Sound - UI Feedback]] · [[Test Plan Matrix]]
