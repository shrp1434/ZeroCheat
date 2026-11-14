---
title: Hippo
type: animal
name: Hippo
species: Hippopotamus amphibius
animal_id: ANM-038
rarity: Epic
family: Safari Animals
role: Tank
habitat: Sunscorch Savanna
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - safari-animals
  - tank
  - sunscorch-savanna
---

# Hippo

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Hippo |
| Species | *Hippopotamus amphibius* |
| Rarity | Epic |
| Animal family | Safari Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-038 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Rainbow, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A river heavyweight that is far more dangerous than it looks. Its yawn intimidates, and its surging charge heals allies in its wake.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 7.054% at P = 0.0, 8.000% at P = 0.3 (baseline), 9.963% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.2400% per roll at baseline P = 0.3; 0.5522% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 682 | |
| Damage (ATK per basic hit) | 33.9 | |
| Defence | 35.2 | 26.0% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 28.8 |
| Movement speed | 13.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.060 | Role target 1.011 ([[Animal Stat Budget Model]]) |

Species tweak applied: ATK ×1.10, MS ×0.90.

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,046, ATK 38.1, DEF 35.2.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Sunscorch Savanna (×1.5) | 75 | 68 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Territorial Yawn | Auto | 12 s | A gaping yawn that taunts the nearest 3 enemies for 2.5 s and reduces their damage by 15%. |
| River Surge | Manual | 18 s | Charges in a water wave (18 studs): 170% ATK and knockback to enemies; allies touched by the wave heal 6% of max HP. |

**Ability activation type:** Territorial Yawn is **auto**, River Surge is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Hippo are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 682 | 33.9 | 35.2 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 737 | 36.6 | 38.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 791 | 39.3 | 40.8 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 846 | 42.0 | 43.6 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 900 | 44.7 | 46.5 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 955 | 47.4 | 49.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A barrel body, an enormous jaw and tiny ears.

**Distinctive features:** The jaw opens to 120 degrees for the yawn; ear wiggle idle.

| Colour | Use |
|---|---|
| `#7D6A8A` | Skin (purple-grey) |
| `#E8A6A0` | Mouth and skin folds |
| `#F1E9D2` | Tusks |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-038 Hippo (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (heavy); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-038 in the [[Asset Register]] |

## Animation requirements

Signature motion: Ponderous trot, ear-wiggle idle, yawn (20 frames), surge charge.

Required clips: idle (2 variants), walk, run, basic attack, Territorial Yawn, River Surge, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Territorial Yawn effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| River Surge effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Wheezing honk; booming yawn; rushing water. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Tank with heals; strong in packed fights.
- **Weaknesses:** The slowest Epic.

## Balance notes

- Power Index 1.060 against a Tank target of 1.011 (difference +0.049; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Rhino]] · [[Crocodile]] · [[Elephant]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
