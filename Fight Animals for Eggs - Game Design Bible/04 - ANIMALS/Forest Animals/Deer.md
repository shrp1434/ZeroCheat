---
title: Deer
type: animal
name: Deer
species: Cervus elaphus
animal_id: ANM-015
rarity: Uncommon
family: Forest Animals
role: Support
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - forest-animals
  - support
  - whisperwood-forest
---

# Deer

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Deer |
| Species | *Cervus elaphus* |
| Rarity | Uncommon |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-015 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A graceful forest guardian whose bounding spirit speeds and soothes the team.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

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

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 520, ATK 12.7, DEF 13.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Whisperwood Forest (×1.0) | 16 | 15 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Meadow Bound | Auto | 16 s | The team gains +20% move speed and heals 5% of max HP over 3 s. |

**Ability activation type:** Meadow Bound is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Deer are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 260 | 16.9 | 13.0 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 281 | 18.3 | 14.0 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 302 | 19.6 | 15.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 322 | 21.0 | 16.1 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 343 | 22.3 | 17.2 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 364 | 23.7 | 18.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Branching antlers (six tines) on a slender, long-legged frame.

**Distinctive features:** Ears flick independently; graceful head-up alert idle.

| Colour | Use |
|---|---|
| `#9A5B34` | Coat |
| `#E8D2B0` | Rump and throat |
| `#5E4630` | Antlers |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-015 Deer (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (cervid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-015 in the [[Asset Register]] |

## Animation requirements

Signature motion: Bounding gallop, grazing idle, antler-raise cast.

Required clips: idle (2 variants), walk, run, basic attack, Meadow Bound, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Meadow Bound effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Soft bleat; hoof patter on grass; chime on Meadow Bound. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Mobility for chasing and escaping; gentle sustained healing.
- **Weaknesses:** Low damage; heals are small in burst fights.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Rabbit]] · [[Fox]] · [[Mini-Boss - Bramblehorn]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
