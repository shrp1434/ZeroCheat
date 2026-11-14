---
title: Megalodon
type: animal
name: Megalodon
species: Otodus megalodon
animal_id: ANM-053
rarity: Mythical
family: Aquatic Animals
role: Bruiser
habitat: Starfall Sanctuary
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - mythical
  - aquatic-animals
  - bruiser
  - starfall-sanctuary
---

# Megalodon

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Megalodon |
| Species | *Otodus megalodon* |
| Rarity | Mythical |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Starfall Sanctuary]] |
| Asset ID | ANM-053 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

The largest shark that ever lived. Every defeat feeds it, and its maw drags enemies into a crushing bite.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Mythical Egg]]. Chance inside the Mythical pool: 23.64% at P = 0.0, 22.22% at P = 0.3 (baseline), 19.49% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0400% per roll at baseline P = 0.3; 0.0849% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Mythical Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Starfall Sanctuary]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 900 s window (25% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 814 | |
| Damage (ATK per basic hit) | 74.0 | |
| Defence | 40.7 | 28.9% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 70.3 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.036 | Role target 1.036 ([[Animal Stat Budget Model]]) |

**Wild version in Starfall Sanctuary** (region multiplier ×11.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 18,722, ATK 638.2, DEF 40.7.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Mythical) | 190 | 150 |
| Defeated in Starfall Sanctuary (×11.5) | 2,185 | 1,725 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Crushing Bite | Auto | 8 s | Bites for 210% ATK and reduces the target's DEF by 20% for 4 s. |
| Abyssal Maw | Manual | 18 s | Lunges 20 studs and bites everything in a cone for 260% ATK, pulling enemies 6 studs towards it. |
| Apex Appetite | Passive (always on) | — | Heals 3% of max HP whenever the team defeats an enemy. |

**Ability activation type:** Crushing Bite is **auto**, Abyssal Maw is **manual**; Apex Appetite is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Megalodon are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 814 | 74.0 | 40.7 | 100% | Base appearance |
| A1 | 1 | 1 | 3,200 | 879 | 79.9 | 44.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 6,400 | 944 | 85.8 | 47.2 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 9,600 | 1,009 | 91.8 | 50.5 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 12,800 | 1,074 | 97.7 | 53.7 | 120% | Particle accents on movement |
| A5 | 2 | 6 | 16,000 | 1,140 | 103.6 | 57.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A massive jaw on a scarred grey body with small eyes.

**Distinctive features:** Companion scale capped at 1.6 times a Great White (see the modelling principles).

| Colour | Use |
|---|---|
| `#4F5B66` | Back |
| `#DADFE3` | Belly |
| `#F4F1E8` | Teeth |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-053 Megalodon (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim, large); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 6,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-053 in the [[Asset Register]] |

## Animation requirements

Signature motion: Slow, heavy air-swim, jaw-flex idle, lunge bite.

Required clips: idle (2 variants), walk, run, basic attack, Crushing Bite, Abyssal Maw, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Crushing Bite effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Abyssal Maw effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Mythical) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Sub-bass rumble; cavernous bite. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Sustained brawling; group pull.
- **Weaknesses:** A large hitbox.

## Balance notes

- Power Index 1.036 against a Bruiser target of 1.036 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Mythical animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Great White Shark]] · [[Mosasaurus]] · [[World Boss - Abyssal Leviathan]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Mythical Egg]] · [[Region - Starfall Sanctuary]] · [[Animal Combat Behaviour]] · [[Ascension System]]
