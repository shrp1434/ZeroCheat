---
title: Walrus
type: animal
name: Walrus
species: Odobenus rosmarus
animal_id: ANM-032
rarity: Rare
family: Aquatic Animals
role: Tank
habitat: Frostfang Tundra
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
  - tank
  - frostfang-tundra
---

# Walrus

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Walrus |
| Species | *Odobenus rosmarus* |
| Rarity | Rare |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Frostfang Tundra]] |
| Asset ID | ANM-032 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A tusked guardian of the ice that slams the ground and shields its allies with floes.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Frostfang Tundra]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

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

**Wild version in Frostfang Tundra** (region multiplier ×4.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 4,743, ATK 80.3, DEF 27.2.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Frostfang Tundra (×4.5) | 126 | 112 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Tusk Slam | Auto | 10 s | Slams its tusks down: 140% ATK in a 6-stud radius and a 20% slow. |
| Ice Floe Shield | Manual | 20 s | Gives each ally a shield equal to 15% of the Walrus's max HP for 5 s. |

**Ability activation type:** Tusk Slam is **auto**, Ice Floe Shield is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Walrus are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 527 | 23.8 | 27.2 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 569 | 25.7 | 29.4 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 611 | 27.6 | 31.6 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 653 | 29.5 | 33.7 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 696 | 31.4 | 35.9 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 738 | 33.3 | 38.1 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Huge tusks and a whiskered moustache on a blubbery body.

**Distinctive features:** Skin folds modelled as two stacked rings.

| Colour | Use |
|---|---|
| `#8B6B5C` | Skin |
| `#F1E9D2` | Tusks |
| `#C9A894` | Whiskers |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-032 Walrus (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (flipper bound on land); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-032 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heaving bound, tusk-rest idle, rear-and-slam.

Required clips: idle (2 variants), walk, run, basic attack, Tusk Slam, Ice Floe Shield, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Tusk Slam effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Ice Floe Shield effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep bellow; wet slap; cracking ice on shield. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team shields; area slow.
- **Weaknesses:** Very slow on land.

## Balance notes

- Power Index 1.001 against a Tank target of 1.001 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Seal]] · [[Penguin]] · [[Woolly Mammoth]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Frostfang Tundra]] · [[Animal Combat Behaviour]] · [[Ascension System]]
