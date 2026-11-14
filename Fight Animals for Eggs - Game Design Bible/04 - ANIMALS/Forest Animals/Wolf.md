---
title: Wolf
type: animal
name: Wolf
species: Canis lupus
animal_id: ANM-024
rarity: Rare
family: Forest Animals
role: Bruiser
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
  - bruiser
  - whisperwood-forest
---

# Wolf

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Wolf |
| Species | *Canis lupus* |
| Rarity | Rare |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-024 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A pack leader that hits harder alongside allies and rallies the whole team with a howl.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

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

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 748, ATK 25.5, DEF 18.7.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Whisperwood Forest (×1.0) | 28 | 25 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Flank Bite | Auto | 7 s | Bites for 150% ATK; +25% damage if another ally is attacking the same target. |
| Pack Howl | Manual | 22 s | The team gains +20% damage and +10% move speed for 6 s. |

**Ability activation type:** Flank Bite is **auto**, Pack Howl is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Wolf are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 374 | 34.0 | 18.7 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 404 | 36.7 | 20.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 434 | 39.4 | 21.7 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 464 | 42.2 | 23.2 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 494 | 44.9 | 24.7 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 524 | 47.6 | 26.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A lean body, long snout and low bushy tail.

**Distinctive features:** Raised hackles in combat; ears pinned during charges.

| Colour | Use |
|---|---|
| `#7A7F87` | Coat |
| `#C9CDD2` | Underbelly |
| `#F2C14E` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-024 Wolf (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped (canid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-024 in the [[Asset Register]] |

## Animation requirements

Signature motion: Loping trot, sniff-circle idle, head-raised howl (16 frames).

Required clips: idle (2 variants), walk, run, basic attack, Flank Bite, Pack Howl, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Flank Bite effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Pack Howl effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Howl (long, the signature); growls; snapping bite. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team damage buff on demand; strong focus-fire partner.
- **Weaknesses:** Average durability; the howl's timing matters.

## Balance notes

- Power Index 1.030 against a Bruiser target of 1.030 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Fox]] · [[Hyena]] · [[Arctic Fox]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
