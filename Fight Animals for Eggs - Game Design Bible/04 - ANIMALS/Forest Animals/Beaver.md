---
title: Beaver
type: animal
name: Beaver
species: Castor canadensis
animal_id: ANM-017
rarity: Uncommon
family: Forest Animals
role: Tank
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
  - tank
  - whisperwood-forest
---

# Beaver

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Beaver |
| Species | *Castor canadensis* |
| Rarity | Uncommon |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-017 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

An engineer that throws up log walls to block projectiles and stall chasing enemies.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 403 | |
| Damage (ATK per basic hit) | 18.2 | |
| Defence | 20.8 | 17.2% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 15.5 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.993 | Role target 0.993 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 806, ATK 13.6, DEF 20.8.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Whisperwood Forest (×1.0) | 16 | 15 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Dam Wall | Manual | 18 s | Builds a 10-stud-wide log wall in front of itself for 4 s that blocks projectiles and enemy movement; the wall has 30% of the Beaver's max HP. |

**Ability activation type:** Dam Wall is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Beaver are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 403 | 18.2 | 20.8 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 435 | 19.7 | 22.5 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 467 | 21.1 | 24.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 500 | 22.6 | 25.8 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 532 | 24.0 | 27.5 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 564 | 25.5 | 29.1 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A flat paddle tail and big orange incisors.

**Distinctive features:** Rounded body, tiny ears, gnawing idle.

| Colour | Use |
|---|---|
| `#7B4A2A` | Fur |
| `#3E2A1C` | Tail |
| `#F2A541` | Teeth |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-017 Beaver (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (stocky); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-017 in the [[Asset Register]] |

## Animation requirements

Signature motion: Waddle, tail-slap alert, log-stack build (3 logs pop in over 10 frames).

Required clips: idle (2 variants), walk, run, basic attack, Dam Wall, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Dam Wall effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chattering; wood creak and thunk as the logs land; tail slap. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Hard counter to Ranged enemies; zone control.
- **Weaknesses:** The wall can block allies' melee paths; low damage.

## Balance notes

- Power Index 0.993 against a Tank target of 0.993 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Hedgehog]] · [[Badger]] · [[Walrus]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
