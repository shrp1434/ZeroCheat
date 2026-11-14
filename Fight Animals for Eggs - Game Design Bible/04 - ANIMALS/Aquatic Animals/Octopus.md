---
title: Octopus
type: animal
name: Octopus
species: Octopus vulgaris
animal_id: ANM-031
rarity: Rare
family: Aquatic Animals
role: Controller
habitat: Coral Coast
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - aquatic-animals
  - controller
  - coral-coast
---

# Octopus

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Octopus |
| Species | *Octopus vulgaris* |
| Rarity | Rare |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Coral Coast]] |
| Asset ID | ANM-031 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Neon, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A clever reef escape artist that blinds groups with ink and pins single targets in its arms.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Coral Coast]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 323 | |
| Damage (ATK per basic hit) | 27.2 | |
| Defence | 16.1 | 13.9% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 27.2 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.869 | Role target 0.869 ([[Animal Stat Budget Model]]) |

**Wild version in Coral Coast** (region multiplier ×3.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,067, ATK 65.3, DEF 16.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Coral Coast (×3.2) | 90 | 80 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Ink Cloud | Auto | 12 s | Releases an ink cloud (radius 8, 4 s): enemies inside attack 30% slower and cannot target units more than 6 studs away. |
| Tentacle Bind | Manual | 14 s | Roots its target for 2 s and deals 120% ATK over the duration. |

**Ability activation type:** Ink Cloud is **auto**, Tentacle Bind is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Octopus are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 323 | 27.2 | 16.1 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 349 | 29.4 | 17.4 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 375 | 31.6 | 18.7 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 401 | 33.7 | 20.0 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 426 | 35.9 | 21.3 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 452 | 38.1 | 22.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A bulbous mantle with eight curling arms.

**Distinctive features:** Arms animated with a 3-bone chain each; colour pulse when casting.

| Colour | Use |
|---|---|
| `#C2475A` | Skin |
| `#F28C9B` | Suckers |
| `#F5D76E` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-031 Octopus (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Cephalopod (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-031 in the [[Asset Register]] |

## Animation requirements

Signature motion: Air-swim jet pulses, curling-arm idle, ink burst.

Required clips: idle (2 variants), walk, run, basic attack, Ink Cloud, Tentacle Bind, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Ink Cloud effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Tentacle Bind effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Bubbly squelch; ink 'poof'; suction pops. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area and single-target control; disrupts Ranged enemies.
- **Weaknesses:** Low damage; fragile.

## Balance notes

- Power Index 0.869 against a Controller target of 0.869 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Giant Squid]] · [[Crab]] · [[Electric Eel]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Coral Coast]] · [[Animal Combat Behaviour]] · [[Ascension System]]
