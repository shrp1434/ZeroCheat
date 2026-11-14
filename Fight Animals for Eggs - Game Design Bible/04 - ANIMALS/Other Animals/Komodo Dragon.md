---
title: Komodo Dragon
type: animal
name: Komodo Dragon
species: Varanus komodoensis
animal_id: ANM-050
rarity: Legendary
family: Other Animals
role: Controller
habitat: Emberheart Caldera
pool_class: Elusive
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - other-animals
  - controller
  - emberheart-caldera
---

# Komodo Dragon

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Komodo Dragon |
| Species | *Varanus komodoensis* |
| Rarity | Legendary |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Emberheart Caldera]] |
| Asset ID | ANM-050 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A venomous giant lizard. It stacks venom until its prey is paralysed. The rarest Legendary.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 3.371% at P = 0.0, 4.615% at P = 0.3 (baseline), 7.153% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0369% per roll at baseline P = 0.3; 0.1254% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emberheart Caldera]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 542 | |
| Damage (ATK per basic hit) | 45.6 | |
| Defence | 27.1 | 21.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 45.6 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.867 | Role target 0.867 ([[Animal Stat Budget Model]]) |

**Wild version in Emberheart Caldera** (region multiplier ×8.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 9,206, ATK 290.7, DEF 27.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Emberheart Caldera (×8.5) | 808 | 680 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Toxic Bite | Auto | 9 s | Bites for 160% ATK and applies 3 venom stacks. |
| Paralysing Bite | Manual | 16 s | Lunges 16 studs and bites for 140% ATK; if the target has 4 or more venom stacks, it is stunned for 1.5 s. |
| Venomous Saliva | Passive (always on) | — | Basic attacks apply 1 venom stack (maximum 5); each stack deals 15% ATK per second and reduces healing received by 5%. |

**Ability activation type:** Toxic Bite is **auto**, Paralysing Bite is **manual**; Venomous Saliva is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Komodo Dragon are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 542 | 45.6 | 27.1 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 585 | 49.2 | 29.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 628 | 52.9 | 31.4 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 671 | 56.5 | 33.6 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 715 | 60.2 | 35.7 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 758 | 63.8 | 37.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Armoured scales, a heavy tail and a forked yellow tongue.

**Distinctive features:** Splayed legs; head sways while tasting the air.

| Colour | Use |
|---|---|
| `#5F5A47` | Scales |
| `#8B8457` | Highlights |
| `#E8C547` | Tongue |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-050 Komodo Dragon (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Low quadruped (reptile); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-050 in the [[Asset Register]] |

## Animation requirements

Signature motion: Swaggering sway walk, tongue-flick idle, lunge.

Required clips: idle (2 variants), walk, run, basic attack, Toxic Bite, Paralysing Bite, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Toxic Bite effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Paralysing Bite effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Hissing; a wet venom bite; scales scraping. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Strong against healing enemies; a powerful stun once stacked.
- **Weaknesses:** Slow to ramp up.

## Balance notes

- Power Index 0.867 against a Controller target of 0.867 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Crocodile]] · [[Cobra]] · [[Titanoboa]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Emberheart Caldera]] · [[Animal Combat Behaviour]] · [[Ascension System]]
