---
title: Raccoon
type: animal
name: Raccoon
species: Procyon lotor
animal_id: ANM-004
rarity: Common
family: Forest Animals
role: Assassin
habitat: Whisperwood Forest
pool_class: Scarce
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - forest-animals
  - assassin
  - whisperwood-forest
---

# Raccoon

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Raccoon |
| Species | *Procyon lotor* |
| Rarity | Common |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-004 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A masked opportunist that strikes enemies who are distracted by someone else. It rewards players who let their Tank hold attention.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 5.403% at P = 0.0, 6.122% at P = 0.3 (baseline), 7.613% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 3.980% per roll at baseline P = 0.3; 4.045% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 150 | |
| Damage (ATK per basic hit) | 29.0 | |
| Defence | 7.0 | 6.5% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 30.5 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.054 | Role target 1.054 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 300, ATK 21.8, DEF 7.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Midnight Swipe | Auto | 9 s | Slips behind its target and strikes for 180% ATK; +50% damage if the target is currently attacking a different unit. |

**Ability activation type:** Midnight Swipe is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Raccoon are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 150 | 29.0 | 7.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 162 | 31.3 | 7.6 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 174 | 33.6 | 8.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 186 | 36.0 | 8.7 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 198 | 38.3 | 9.2 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 210 | 40.6 | 9.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A banded tail (five rings) and a black eye mask read clearly at a distance.

**Distinctive features:** Dexterous forepaws, slight hunch, curious head tilt idle.

| Colour | Use |
|---|---|
| `#7E7E86` | Grey coat |
| `#2A2A30` | Mask and tail rings |
| `#E8E8EC` | Muzzle |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-004 Raccoon (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped; see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-004 in the [[Asset Register]] |

## Animation requirements

Signature motion: Sneaking low run, paw-rub idle, two-frame vanish blur before the swipe.

Required clips: idle (2 variants), walk, run, basic attack, Midnight Swipe, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Midnight Swipe effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chirring trill; swish-and-scratch on the swipe. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** High burst on distracted targets; excellent cleanup.
- **Weaknesses:** Fragile; weak when it is the only target.

## Balance notes

- Power Index 1.054 against a Assassin target of 1.054 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Fox]] · [[Badger]] · [[Leopard]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
