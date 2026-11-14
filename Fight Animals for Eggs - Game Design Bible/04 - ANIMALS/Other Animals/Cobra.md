---
title: Cobra
type: animal
name: Cobra
species: Naja nigricollis
animal_id: ANM-020
rarity: Uncommon
family: Other Animals
role: Ranged
habitat: Sunscorch Savanna
pool_class: Standard
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - other-animals
  - ranged
  - sunscorch-savanna
---

# Cobra

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Cobra |
| Species | *Naja nigricollis* |
| Rarity | Uncommon |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-020 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A spitting cobra that weakens foes from range with lingering venom.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 195 | |
| Damage (ATK per basic hit) | 29.9 | |
| Defence | 9.1 | 8.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 29.9 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 24 studs | |
| Power Index | 0.913 | Role target 0.913 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 585, ATK 33.6, DEF 9.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Sunscorch Savanna (×1.5) | 24 | 22 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Venom Spit | Auto | 7 s | Spits at a target up to 24 studs away: 80% ATK plus poison dealing 60% ATK over 4 s; poisoned enemies deal -10% damage. |

**Ability activation type:** Venom Spit is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Cobra are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 195 | 29.9 | 9.1 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 211 | 32.3 | 9.8 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 226 | 34.7 | 10.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 242 | 37.1 | 11.3 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 257 | 39.5 | 12.0 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 273 | 41.9 | 12.7 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A spread hood rising from a coiled base.

**Distinctive features:** Forked tongue flick idle; the hood flares when attacking.

| Colour | Use |
|---|---|
| `#3A3A2E` | Scales |
| `#C9B26B` | Hood band |
| `#E6E0B8` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-020 Cobra (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Serpent; see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-020 in the [[Asset Register]] |

## Animation requirements

Signature motion: S-wave slither, hood-flare rise, spit recoil.

Required clips: idle (2 variants), walk, run, basic attack, Venom Spit, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Venom Spit effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Hiss (layered); wet spit; sizzle on poison ticks. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Damage over time plus a damage-down debuff.
- **Weaknesses:** Short range for a Ranged role; low health.

## Balance notes

- Power Index 0.913 against a Ranged target of 0.913 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Komodo Dragon]] · [[Titanoboa]] · [[Frog]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
