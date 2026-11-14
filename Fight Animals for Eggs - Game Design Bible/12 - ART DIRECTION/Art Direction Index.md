---
title: Art Direction Index
type: index
category: art
status: mixed
priority: P0
owner: Art Director
last_updated: 2026-11-14
tags:
  - art
  - index
  - navigation
---

# Art Direction Index

The art direction folder defines how *Fight Animals for Eggs* looks: style, colour, typography, UI skin, animal modelling, materials, lighting, environments, rarity signals, eggs, bases, bosses and variants. It is written for 3D artists, technical artists, UI artists, animators and the engineers who implement visuals.

> [!success] CONFIRMED — D-026
> Colourful, polished, low-poly animals with clear silhouettes. No horror, no "Italian brainrot", no meme animals.

Almost everything else in this folder is **PROPOSED** and will be tuned during look-development. Numbers that belong to gameplay (costs, stats, odds) are never defined here; they live in [[Canonical Proposed Values]].

## How to use this folder

1. Start with the [[Art Bible]]: style statement, tone rules, readability hierarchy and review gates.
2. Look up colours in [[Colour Palette]] before typing any hex value.
3. Use the specialist page for the asset you are making (table below).
4. Register every asset in the [[Asset Register]] and name it per [[Asset Naming Conventions]].
5. Request concept art through [[Visual Reference Placeholders]].

## Documents

| Document | What it covers |
|---|---|
| [[Art Bible]] | Top-level style statement, pillars, content safety rules, readability hierarchy, shape language and the six review gates |
| [[Colour Palette]] | Every colour token: rarity keys and tints, feedback, social, UI and region palettes, accessibility checks |
| [[Typography]] | Typefaces, type scale, outlines, number formatting and localisation rules for text |
| [[UI Visual Styling]] | Visual skin for panels, buttons, rarity card frames, icons, bars and world-space UI |
| [[Animal Modelling Principles]] | Scale classes, family proportions, body plans, triangle budgets, 64 px silhouette test and confusion groups |
| [[Material and Texture Direction]] | Enum.Material meanings, palette atlases, SurfaceAppearance rules and texture memory budgets |
| [[Lighting Direction]] | Lighting technology, per-region Lighting, Atmosphere and post-processing presets, readability floor, presentation lighting |
| [[Environment Art Direction]] | Construction rules, region visual identities, shared environment kits, navigation and environment budgets |
| [[Rarity Visual Language]] | The seven-step escalation ladder for frames, nameplates, wild animals and hatch reveals |
| [[Egg Art Direction]] | Shared principles for the seven egg models: silhouette ladder, materials and states |
| [[Base Art Direction]] | Module identities, the L1–L5 upgrade ladder, Egg Merging Station forms, Plot Expansion and raid-state visuals |
| [[Boss Art Direction]] | Boss scale, phase visuals, telegraph language and per-boss art hooks |
| [[Variant Visual Treatments]] | Golden, Diamond, Rainbow, Shadow and Neon material sets, constraints and budgets |

## Open questions raised by art direction

| ID | Question | Where discussed |
|---|---|---|
| Q-601 | Player avatar type and scale constraints | [[Art Bible]] |
| Q-602 | Base personalisation (colours, themes, decorations) | [[Base Art Direction]] |
| Q-603 | Day/night cycle versus fixed per-region time of day | [[Lighting Direction]] |
| Q-604 | Scale compression of colossal species as companions | [[Animal Modelling Principles]] |
| Q-605 | Whether in-world signage may contain text | [[Typography]], [[Environment Art Direction]] |
| Q-606 | Whether regions have weather states | [[Environment Art Direction]] |
| Q-607 | Whether the game provides its own reduced-effects setting | [[Lighting Direction]] |
| Q-608 | Whether one animal can carry more than one variant | [[Variant Visual Treatments]] |

All are **UNDECIDED**. Existing questions that most affect art: [[Open Questions#Q-002]] (roster), [[Open Questions#Q-006]] (variant acquisition), [[Open Questions#Q-008]] (pen display), [[Open Questions#Q-027]] (ancient lineage theme) and [[Open Questions#Q-028]] (aquatic movement on land).

## Neighbouring folders

- Animation, rigs and VFX: [[Animation and VFX Index]] ([[Animation Bible]], [[Animal Rig Standards]], [[VFX Bible]])
- Sound: [[Sound Design Index]]
- UI components and screens: [[UI and UX Index]]
- Asset catalogue: [[Assets Index]]

## Related documents
- [[Home]]
- [[Vault Map]]
- [[Assets Index]]
- [[Asset Register]]
- [[Decision Register]]
