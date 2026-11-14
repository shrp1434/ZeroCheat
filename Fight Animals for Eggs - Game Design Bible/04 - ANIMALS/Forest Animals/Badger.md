---
title: Badger
type: animal
name: Badger
species: Meles meles
animal_id: ANM-016
rarity: Uncommon
family: Forest Animals
role: Bruiser
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Manual
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - forest-animals
  - bruiser
  - whisperwood-forest
---

# Badger

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Badger |
| Species | *Meles meles* |
| Rarity | Uncommon |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-016 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A fearless digger that ambushes from below. Stocky and tough, it punches above its size.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 286 | |
| Damage (ATK per basic hit) | 26.0 | |
| Defence | 14.3 | 12.5% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 24.7 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.028 | Role target 1.028 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 572, ATK 19.5, DEF 14.3.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Whisperwood Forest (×1.0) | 16 | 15 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Burrow Ambush | Manual | 12 s | Burrows (untargetable for 1 s), then erupts beneath its target for 160% ATK and knocks it up for 0.8 s. |

**Ability activation type:** Burrow Ambush is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Badger are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 286 | 26.0 | 14.3 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 309 | 28.1 | 15.4 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 332 | 30.2 | 16.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 355 | 32.2 | 17.7 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 378 | 34.3 | 18.9 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 400 | 36.4 | 20.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A low, stocky body and a bold black-and-white face stripe.

**Distinctive features:** Large digging claws, short tail.

| Colour | Use |
|---|---|
| `#8E8E8E` | Body |
| `#111111` | Face stripes |
| `#FFFFFF` | Face blaze |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-016 Badger (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (stocky, digger); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-016 in the [[Asset Register]] |

## Animation requirements

Signature motion: Waddling trot, dig-in transition, eruption pop with debris.

Required clips: idle (2 variants), walk, run, basic attack, Burrow Ambush, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Burrow Ambush effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Low growls; soil crunch while burrowing; earthy burst. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Dodges a hit with the burrow, then disables.
- **Weaknesses:** Short range; average defence.

## Balance notes

- Power Index 1.028 against a Bruiser target of 1.028 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Boar]] · [[Raccoon]] · [[Wolf]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
