---
title: Leopard
type: animal
name: Leopard
species: Panthera pardus
animal_id: ANM-028
rarity: Rare
family: Big Cats
role: Assassin
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
  - big-cats
  - assassin
  - emerald-canopy
---

# Leopard

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Leopard |
| Species | *Panthera pardus* |
| Rarity | Rare |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-028 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Shadow, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A stealthy canopy hunter that vanishes into the foliage and strikes from above.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 6.197% at P = 0.0, 7.059% at P = 0.3 (baseline), 8.872% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.6353% per roll at baseline P = 0.3; 1.201% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 255 | |
| Damage (ATK per basic hit) | 49.3 | |
| Defence | 11.9 | 10.6% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 51.8 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.045 | Role target 1.045 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,122, ATK 81.3, DEF 11.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Emerald Canopy (×2.2) | 62 | 55 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Rosette Camouflage | Auto | 10 s | If not attacked for 4 s, becomes camouflaged: ignored by enemy auto-targeting until it attacks. |
| Tree Ambush | Manual | 14 s | Leaps from up to 24 studs for 220% ATK and applies a bleed of 60% ATK over 3 s. |

**Ability activation type:** Rosette Camouflage is **auto**, Tree Ambush is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Leopard are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 255 | 49.3 | 11.9 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 275 | 53.2 | 12.9 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 296 | 57.2 | 13.8 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 316 | 61.1 | 14.8 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 337 | 65.1 | 15.7 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 357 | 69.0 | 16.7 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A muscular frame covered in rosettes.

**Distinctive features:** Camouflage uses a material transparency blend (0.6) plus a shimmer edge.

| Colour | Use |
|---|---|
| `#D9A441` | Coat |
| `#2B1F14` | Rosettes |
| `#F3E6C8` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-028 Leopard (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped (felid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-028 in the [[Asset Register]] |

## Animation requirements

Signature motion: Low stalk, tree-perch idle, pounce from height.

Required clips: idle (2 variants), walk, run, basic attack, Rosette Camouflage, Tree Ambush, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Rosette Camouflage effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Tree Ambush effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Rasping 'sawing' call; soft foliage rustle on camouflage. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Picks off isolated targets; hard to pin down.
- **Weaknesses:** Fragile when revealed.

## Balance notes

- Power Index 1.045 against a Assassin target of 1.045 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Tiger]] · [[Cheetah]] · [[Snow Leopard]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
