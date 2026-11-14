---
title: Peacock
type: animal
name: Peacock
species: Pavo cristatus
animal_id: ANM-030
rarity: Rare
family: Birds
role: Support
habitat: Emerald Canopy
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - birds
  - support
  - emerald-canopy
---

# Peacock

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Peacock |
| Species | *Pavo cristatus* |
| Rarity | Rare |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-030 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A dazzling showman that heals the team and stuns attackers with its display.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 6.197% at P = 0.0, 7.059% at P = 0.3 (baseline), 8.872% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.6353% per roll at baseline P = 0.3; 1.201% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 340 | |
| Damage (ATK per basic hit) | 22.1 | |
| Defence | 17.0 | 14.5% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 22.1 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,496, ATK 36.5, DEF 17.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Emerald Canopy (×2.2) | 62 | 55 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Radiant Plumage | Auto | 18 s | Heals the team for 10% of max HP. |
| Dazzling Display | Manual | 20 s | Fans its tail: enemies within 10 studs are charmed (stop attacking) for 1.5 s and allies gain +15% DEF for 5 s. |

**Ability activation type:** Radiant Plumage is **auto**, Dazzling Display is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Peacock are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 340 | 22.1 | 17.0 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 367 | 23.9 | 18.4 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 394 | 25.6 | 19.7 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 422 | 27.4 | 21.1 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 449 | 29.2 | 22.4 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 476 | 30.9 | 23.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A fan tail with eye-spots, closed into a long train when walking.

**Distinctive features:** The tail fan is a hinged set of 12 feather plates.

| Colour | Use |
|---|---|
| `#1F5FBF` | Neck |
| `#1FA37A` | Train |
| `#D4AF37` | Eye-spot rims |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-030 Peacock (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (ground, display tail); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-030 in the [[Asset Register]] |

## Animation requirements

Signature motion: Stately strut, tail-fan open (14 frames), shimmer shake.

Required clips: idle (2 variants), walk, run, basic attack, Radiant Plumage, Dazzling Display, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Radiant Plumage effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Dazzling Display effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Loud cry; rustling tail rattle on display. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Both healing and defensive control.
- **Weaknesses:** Low damage; both effects need it close to the fight.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Flamingo]] · [[Toucan]] · [[Giant Panda]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
