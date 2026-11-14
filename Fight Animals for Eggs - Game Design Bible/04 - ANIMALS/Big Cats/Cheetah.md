---
title: Cheetah
type: animal
name: Cheetah
species: Acinonyx jubatus
animal_id: ANM-026
rarity: Rare
family: Big Cats
role: Skirmisher
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
  - big-cats
  - skirmisher
  - sunscorch-savanna
---

# Cheetah

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Cheetah |
| Species | *Acinonyx jubatus* |
| Rarity | Rare |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-026 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The fastest land animal: a sprinter that runs targets down and punishes anything trying to flee.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 266 | |
| Damage (ATK per basic hit) | 27.2 | |
| Defence | 13.6 | 12.0% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 42.2 |
| Movement speed | 23.9 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.970 | Role target 1.012 ([[Animal Stat Budget Model]]) |

Species tweak applied: MS ×1.15, HP ×0.92.

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 798, ATK 30.6, DEF 13.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Sunscorch Savanna (×1.5) | 42 | 38 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Chase Down | Auto | 8 s | A three-hit flurry, each hit 60% ATK; hits on moving targets deal +40%. |
| Sprint | Manual | 15 s | Gains +80% move speed and +30% attack speed for 4 s. |

**Ability activation type:** Chase Down is **auto**, Sprint is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Cheetah are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 266 | 27.2 | 13.6 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 287 | 29.4 | 14.7 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 308 | 31.6 | 15.8 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 330 | 33.7 | 16.9 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 351 | 35.9 | 18.0 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 372 | 38.1 | 19.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A slender frame, small head and black tear marks.

**Distinctive features:** Long tail used for balance in turns; deep chest.

| Colour | Use |
|---|---|
| `#E8B25A` | Coat |
| `#1A1A1A` | Spots and tear marks |
| `#F7F0E0` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-026 Cheetah (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped (felid, slender); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-026 in the [[Asset Register]] |

## Animation requirements

Signature motion: Rotary gallop with full spine flex, crouch-stalk idle, Sprint speed-line trail.

Required clips: idle (2 variants), walk, run, basic attack, Chase Down, Sprint, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Chase Down effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Sprint effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chirp and purr (not roars); rapid paw drum; air rush on Sprint. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Unmatched speed; counters kiting enemies.
- **Weaknesses:** Low health for a Rare; little sustained damage outside Sprint.

## Balance notes

- Power Index 0.970 against a Skirmisher target of 1.012 (difference -0.041; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Leopard]] · [[Lion]] · [[Peregrine Falcon]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
