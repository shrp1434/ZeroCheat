---
title: Quetzalcoatlus
type: animal
name: Quetzalcoatlus
species: Quetzalcoatlus northropi
animal_id: ANM-058
rarity: Secret
family: Other Animals
role: Ranged
habitat: Starfall Sanctuary
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - secret
  - other-animals
  - ranged
  - starfall-sanctuary
---

# Quetzalcoatlus

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Quetzalcoatlus |
| Species | *Quetzalcoatlus northropi* |
| Rarity | Secret |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Starfall Sanctuary]] |
| Asset ID | ANM-058 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

A pterosaur as tall as a giraffe. It controls the battlefield with storms of wind from its colossal wings.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Secret Egg]]. Chance inside the Secret pool: 36.76% at P = 0.0, 34.48% at P = 0.3 (baseline), 30.12% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.00690% per roll at baseline P = 0.3; 0.0160% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Secret Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Starfall Sanctuary]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 2,700 s window (10% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 720 | |
| Damage (ATK per basic hit) | 110.4 | |
| Defence | 33.6 | 25.1% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 110.4 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 32 studs | |
| Power Index | 0.882 | Role target 0.882 ([[Animal Stat Budget Model]]) |

**Wild version in Starfall Sanctuary** (region multiplier ×11.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 16,560, ATK 952.2, DEF 33.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Secret) | 400 | 300 |
| Defeated in Starfall Sanctuary (×11.5) | 4,600 | 3,450 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Gale Wingbeat | Auto | 8 s | A cone of wind (28 studs): 180% ATK and 8-stud knockback. |
| Stormfront Glide | Manual | 18 s | Glides along a 30-stud line, dropping 5 gusts that each deal 140% ATK and slow by 30%. |
| Sky Giant | Passive (always on) | — | Immune to knockback; attacks from 32 studs. |

**Ability activation type:** Gale Wingbeat is **auto**, Stormfront Glide is **manual**; Sky Giant is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Quetzalcoatlus are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 720 | 110.4 | 33.6 | 100% | Base appearance |
| A1 | 1 | 1 | 6,400 | 778 | 119.2 | 36.3 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 12,800 | 835 | 128.1 | 39.0 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 19,200 | 893 | 136.9 | 41.7 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 25,600 | 950 | 145.7 | 44.4 | 120% | Particle accents on movement |
| A5 | 1 | 5 | 32,000 | 1,008 | 154.6 | 47.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A giraffe-tall neck, a huge beak and a crest.

**Distinctive features:** Walks on folded wings; the wing membrane uses a translucent material.

| Colour | Use |
|---|---|
| `#C46A3A` | Crest |
| `#F1D5B0` | Body |
| `#3B2F2F` | Wing membrane |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-058 Quetzalcoatlus (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Pterosaur (flight and quadrupedal walk); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 7,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-058 in the [[Asset Register]] |

## Animation requirements

Signature motion: Quadrupedal wing-walk, launch hop, slow soaring flaps.

Required clips: idle (2 variants), walk, run, basic attack, Gale Wingbeat, Stormfront Glide, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Gale Wingbeat effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Stormfront Glide effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Secret) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep, croaking call; heavy whooshing wingbeats; gale howl. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Longest-range area damage; knockback zoning.
- **Weaknesses:** Knockback can scatter enemies away from melee allies.

## Balance notes

- Power Index 0.882 against a Ranged target of 0.882 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Secret animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Haast's Eagle]] · [[World Boss - Ashwing Condor]] · [[Narwhal]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Secret Egg]] · [[Region - Starfall Sanctuary]] · [[Animal Combat Behaviour]] · [[Ascension System]]
