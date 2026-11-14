---
title: Seal
type: animal
name: Seal
species: Phoca vitulina
animal_id: ANM-022
rarity: Uncommon
family: Aquatic Animals
role: Controller
habitat: Coral Coast
pool_class: Scarce
ability_activation: Manual
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - aquatic-animals
  - controller
  - coral-coast
---

# Seal

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Seal |
| Species | *Phoca vitulina* |
| Rarity | Uncommon |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Coral Coast]] |
| Asset ID | ANM-022 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A playful bowling ball of the shore that slides through enemy groups and leaves them sluggish.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 5.835% at P = 0.0, 6.593% at P = 0.3 (baseline), 8.149% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.451% per roll at baseline P = 0.3; 2.081% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Coral Coast]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 247 | |
| Damage (ATK per basic hit) | 20.8 | |
| Defence | 12.3 | 11.0% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 20.8 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.869 | Role target 0.869 ([[Animal Stat Budget Model]]) |

**Wild version in Coral Coast** (region multiplier ×3.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,581, ATK 49.9, DEF 12.3.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Coral Coast (×3.2) | 51 | 48 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Belly Slide | Manual | 11 s | Slides forward 16 studs, dealing 100% ATK to enemies hit, knocking them back and slowing them by 40% for 2.5 s. |

**Ability activation type:** Belly Slide is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Seal are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 247 | 20.8 | 12.3 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 267 | 22.5 | 13.3 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 287 | 24.1 | 14.3 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 306 | 25.8 | 15.3 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 326 | 27.5 | 16.3 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 346 | 29.1 | 17.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A torpedo-shaped body with whiskers and big dark eyes.

**Distinctive features:** Flippers clap on happy idle; sheen material on the body.

| Colour | Use |
|---|---|
| `#8D99A6` | Body |
| `#5E6A75` | Spots |
| `#1A1A1A` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-022 Seal (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (flipper bound on land); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-022 in the [[Asset Register]] |

## Animation requirements

Signature motion: Galumphing bound on land, flipper clap idle, slide with a water trail.

Required clips: idle (2 variants), walk, run, basic attack, Belly Slide, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Belly Slide effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Barks; wet slide squeak; splash on impact. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Line displacement plus a heavy slow; disrupts packs.
- **Weaknesses:** Clumsy on land; long cooldown.

## Balance notes

- Power Index 0.869 against a Controller target of 0.869 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Walrus]] · [[Penguin]] · [[Orca]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Coral Coast]] · [[Animal Combat Behaviour]] · [[Ascension System]]
