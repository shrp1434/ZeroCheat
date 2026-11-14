---
title: Kangaroo
type: animal
name: Kangaroo
species: Osphranter rufus
animal_id: ANM-027
rarity: Rare
family: Other Animals
role: Bruiser
habitat: Sunscorch Savanna
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - other-animals
  - bruiser
  - sunscorch-savanna
---

# Kangaroo

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Kangaroo |
| Species | *Osphranter rufus* |
| Rarity | Rare |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-027 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

An outback boxer. It jabs fast and finishes with a crushing double kick.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 374 | |
| Damage (ATK per basic hit) | 34.0 | |
| Defence | 18.7 | 15.8% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 32.3 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.030 | Role target 1.030 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,122, ATK 38.2, DEF 18.7.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Sunscorch Savanna (×1.5) | 42 | 38 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Jab Combo | Auto | 8 s | Two quick punches, each 70% ATK. |
| Haymaker Kick | Manual | 12 s | A balanced-on-tail double-foot kick for 200% ATK; knocks back 10 studs and stuns for 0.5 s. |

**Ability activation type:** Jab Combo is **auto**, Haymaker Kick is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Kangaroo are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 374 | 34.0 | 18.7 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 404 | 36.7 | 20.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 434 | 39.4 | 21.7 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 464 | 42.2 | 23.2 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 494 | 44.9 | 24.7 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 524 | 47.6 | 26.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Powerful hind feet, a thick tail and an upright stance.

**Distinctive features:** Boxing guard idle; ears swivel.

| Colour | Use |
|---|---|
| `#B8583A` | Coat |
| `#E9C9A8` | Chest |
| `#4A2A1E` | Paws |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-027 Kangaroo (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Hopper (large biped); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-027 in the [[Asset Register]] |

## Animation requirements

Signature motion: Pentapedal hop, boxing bounce idle, tail-plant kick.

Required clips: idle (2 variants), walk, run, basic attack, Jab Combo, Haymaker Kick, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Jab Combo effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Haymaker Kick effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Grunts and huffs; leather-like punch smacks; heavy kick impact. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Reliable damage plus a peel tool.
- **Weaknesses:** Knockback can push targets away from allies.

## Balance notes

- Power Index 1.030 against a Bruiser target of 1.030 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Rabbit]] · [[Goat]] · [[Gorilla]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
