---
title: Lion
type: animal
name: Lion
species: Panthera leo
animal_id: ANM-043
rarity: Legendary
family: Big Cats
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
  - legendary
  - big-cats
  - bruiser
  - sunscorch-savanna
---

# Lion

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Lion |
| Species | *Panthera leo* |
| Rarity | Legendary |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-043 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The king of the savanna. It strengthens its pride and terrifies enemies with a thunderous roar.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 16.05% at P = 0.0, 15.38% at P = 0.3 (baseline), 14.03% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1231% per roll at baseline P = 0.3; 0.2458% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 627 | |
| Damage (ATK per basic hit) | 57.0 | |
| Defence | 31.4 | 23.9% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 54.1 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.034 | Role target 1.034 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,881, ATK 64.1, DEF 31.4.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Sunscorch Savanna (×1.5) | 142 | 120 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Royal Swipe | Auto | 8 s | Swipes in an arc for 190% ATK and slows by 20% for 2 s. |
| King's Roar | Manual | 24 s | Enemies within 16 studs are feared (flee) for 1.5 s; the team gains +25% damage for 6 s. |
| Pride Leader | Passive (always on) | — | While the Lion is equipped, the other two team animals gain +8% ATK. |

**Ability activation type:** Royal Swipe is **auto**, King's Roar is **manual**; Pride Leader is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Lion are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 627 | 57.0 | 31.4 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 677 | 61.6 | 33.9 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 727 | 66.1 | 36.4 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 777 | 70.7 | 38.9 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 828 | 75.2 | 41.4 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 878 | 79.8 | 43.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A large mane framing the head and a tufted tail.

**Distinctive features:** The mane is layered in 3 shells for a bold low-poly shape.

| Colour | Use |
|---|---|
| `#D9A441` | Coat |
| `#8B4513` | Mane |
| `#3B2A1E` | Tail tuft |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-043 Lion (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (felid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-043 in the [[Asset Register]] |

## Animation requirements

Signature motion: Regal walk, mane-shake idle, roar with the head thrown forward (18 frames).

Required clips: idle (2 variants), walk, run, basic attack, Royal Swipe, King's Roar, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Royal Swipe effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| King's Roar effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Iconic roar (the heaviest companion vocal); grunting calls. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team-wide offensive buffs; area fear.
- **Weaknesses:** Its passive value drops if team animals are knocked out.

## Balance notes

- Power Index 1.034 against a Bruiser target of 1.034 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Tiger]] · [[Hyena]] · [[Mini-Boss - Dustmane]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
