---
title: Monkey
type: animal
name: Monkey
species: Cebus capucinus
animal_id: ANM-021
rarity: Uncommon
family: Other Animals
role: Skirmisher
habitat: Emerald Canopy
pool_class: Standard
ability_activation: Manual
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - other-animals
  - skirmisher
  - emerald-canopy
---

# Monkey

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Monkey |
| Species | *Cebus capucinus* |
| Rarity | Uncommon |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-021 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

An acrobatic canopy prankster that swings into fights and flurries its targets.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 221 | |
| Damage (ATK per basic hit) | 20.8 | |
| Defence | 10.4 | 9.4% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 32.2 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.015 | Role target 1.015 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 972, ATK 34.3, DEF 10.4.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Emerald Canopy (×2.2) | 35 | 33 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Vine Swing | Manual | 10 s | Swings to a target within 22 studs, strikes for 120% ATK and gains +40% attack speed for 4 s. |

**Ability activation type:** Vine Swing is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Monkey are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 221 | 20.8 | 10.4 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 239 | 22.5 | 11.2 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 256 | 24.1 | 12.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 274 | 25.8 | 12.9 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 292 | 27.5 | 13.7 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 309 | 29.1 | 14.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A long curling tail and a pale face framed by dark fur.

**Distinctive features:** Prehensile tail used in idle hangs; expressive brows.

| Colour | Use |
|---|---|
| `#3B2A1E` | Body fur |
| `#F0E3CF` | Face and chest |
| `#E0B48A` | Hands and feet |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-021 Monkey (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Biped primate (small); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-021 in the [[Asset Register]] |

## Animation requirements

Signature motion: Quadrupedal knuckle-bound run, tail-hang idle, swing arc (vine is a Beam).

Required clips: idle (2 variants), walk, run, basic attack, Vine Swing, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Vine Swing effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chatter and hoots; a rope-creak swing; rapid slaps. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Mobile; high burst attack speed.
- **Weaknesses:** Low defence; Vine Swing can leave it isolated.

## Balance notes

- Power Index 1.015 against a Skirmisher target of 1.015 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Gorilla]] · [[Toucan]] · [[Squirrel]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
