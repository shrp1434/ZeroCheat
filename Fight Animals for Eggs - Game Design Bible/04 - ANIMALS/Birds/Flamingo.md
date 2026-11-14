---
title: Flamingo
type: animal
name: Flamingo
species: Phoenicopterus roseus
animal_id: ANM-019
rarity: Uncommon
family: Birds
role: Support
habitat: Sunscorch Savanna
pool_class: Scarce
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - birds
  - support
  - sunscorch-savanna
---

# Flamingo

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Flamingo |
| Species | *Phoenicopterus roseus* |
| Rarity | Uncommon |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-019 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Rainbow, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A poised dancer whose rhythmic rally quickens the team's strikes.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 5.835% at P = 0.0, 6.593% at P = 0.3 (baseline), 8.149% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.451% per roll at baseline P = 0.3; 2.081% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 260 | |
| Damage (ATK per basic hit) | 16.9 | |
| Defence | 13.0 | 11.5% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 16.9 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 780, ATK 19.0, DEF 13.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Sunscorch Savanna (×1.5) | 24 | 22 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Flock Rally | Auto | 14 s | The team gains +15% attack speed for 6 s. |

**Ability activation type:** Flock Rally is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Flamingo are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 260 | 16.9 | 13.0 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 281 | 18.3 | 14.0 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 302 | 19.6 | 15.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 322 | 21.0 | 16.1 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 343 | 22.3 | 17.2 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 364 | 23.7 | 18.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** An S-curved neck and a one-legged stance.

**Distinctive features:** Bent bill, long thin legs (capsule parts), elegant wing fan on cast.

| Colour | Use |
|---|---|
| `#FF7FA8` | Plumage |
| `#FFB3C9` | Highlights |
| `#1A1A1A` | Bill tip |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-019 Flamingo (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (wader, long legs); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-019 in the [[Asset Register]] |

## Animation requirements

Signature motion: High-step walk, one-leg idle, wing-fan dance cast (12 frames).

Required clips: idle (2 variants), walk, run, basic attack, Flock Rally, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Flock Rally effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Honking call; light rhythmic wing beats on Flock Rally. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Boosts every damage dealer; pairs with Skirmishers.
- **Weaknesses:** Fragile; no healing.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Duck]] · [[Peacock]] · [[Toucan]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
