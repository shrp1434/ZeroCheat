---
title: Gorilla
type: animal
name: Gorilla
species: Gorilla gorilla
animal_id: ANM-035
rarity: Epic
family: Other Animals
role: Tank
habitat: Emerald Canopy
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - other-animals
  - tank
  - emerald-canopy
---

# Gorilla

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Gorilla |
| Species | *Gorilla gorilla* |
| Rarity | Epic |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-035 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A silverback protector. It pounds its chest to draw every enemy in, then flattens them with a seismic slam.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 648 | |
| Damage (ATK per basic hit) | 33.3 | |
| Defence | 35.2 | 26.0% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 28.3 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.024 | Role target 1.011 ([[Animal Stat Budget Model]]) |

Species tweak applied: ATK ×1.08, HP ×0.95.

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,851, ATK 54.9, DEF 35.2.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Emerald Canopy (×2.2) | 110 | 99 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Chest Pound | Auto | 15 s | Taunts enemies within 12 studs for 3 s and gains +20% DEF for the duration. |
| Knuckle Quake | Manual | 14 s | Slams both fists down: 180% ATK within 10 studs and a 1 s stun. |

**Ability activation type:** Chest Pound is **auto**, Knuckle Quake is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Gorilla are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 648 | 33.3 | 35.2 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 700 | 35.9 | 38.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 752 | 38.6 | 40.8 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 803 | 41.2 | 43.6 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 855 | 43.9 | 46.5 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 907 | 46.6 | 49.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Huge forearms and a silver saddle on the back.

**Distinctive features:** Knuckle-walk stance; brow ridge.

| Colour | Use |
|---|---|
| `#2B2B2E` | Fur |
| `#A9A9B0` | Silver back |
| `#4A4A50` | Face and hands |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-035 Gorilla (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Biped primate (large, knuckle-walk); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-035 in the [[Asset Register]] |

## Animation requirements

Signature motion: Knuckle-walk, chest-pound idle variant, two-arm overhead slam.

Required clips: idle (2 variants), walk, run, basic attack, Chest Pound, Knuckle Quake, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Chest Pound effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Knuckle Quake effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chest-drum rhythm; deep hoots; ground-crack impact. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area taunt plus area stun; the most aggressive Tank.
- **Weaknesses:** Slightly lower health than other Tanks.

## Balance notes

- Power Index 1.024 against a Tank target of 1.011 (difference +0.013; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Monkey]] · [[Brown Bear]] · [[Kangaroo]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
