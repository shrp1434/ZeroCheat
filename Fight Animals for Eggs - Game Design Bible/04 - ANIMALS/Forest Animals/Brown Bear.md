---
title: Brown Bear
type: animal
name: Brown Bear
species: Ursus arctos
animal_id: ANM-025
rarity: Rare
family: Forest Animals
role: Tank
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - forest-animals
  - tank
  - whisperwood-forest
---

# Brown Bear

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Brown Bear |
| Species | *Ursus arctos* |
| Rarity | Rare |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-025 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The heavyweight of the forest. It holds the line with sweeping mauls and a roar that pulls every enemy's attention.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 527 | |
| Damage (ATK per basic hit) | 23.8 | |
| Defence | 27.2 | 21.4% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 20.2 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.001 | Role target 1.001 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,054, ATK 17.8, DEF 27.2.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Whisperwood Forest (×1.0) | 28 | 25 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Maul | Auto | 9 s | Swipes in a 120-degree arc for 160% ATK. |
| Mighty Roar | Manual | 18 s | Taunts enemies within 12 studs for 3 s and gains 25% damage reduction for the duration. |

**Ability activation type:** Maul is **auto**, Mighty Roar is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Brown Bear are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 527 | 23.8 | 27.2 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 569 | 25.7 | 29.4 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 611 | 27.6 | 31.6 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 653 | 29.5 | 33.7 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 696 | 31.4 | 35.9 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 738 | 33.3 | 38.1 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A pronounced shoulder hump and a broad head.

**Distinctive features:** Rears onto hind legs for the roar; heavy paw plants.

| Colour | Use |
|---|---|
| `#6E4B2E` | Fur |
| `#4A3320` | Paws and muzzle |
| `#2B1E14` | Claws |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-025 Brown Bear (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (ursid, can rear); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-025 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heavy amble, rear-up roar, double-paw maul.

Required clips: idle (2 variants), walk, run, basic attack, Maul, Mighty Roar, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Maul effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Mighty Roar effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep roar; huffing breaths; heavy thuds. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area taunt plus cleave; the best early Tank.
- **Weaknesses:** Slow; moderate damage.

## Balance notes

- Power Index 1.001 against a Tank target of 1.001 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Wolf]] · [[Gorilla]] · [[Mini-Boss - Rimeback]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
