---
title: Titanoboa
type: animal
name: Titanoboa
species: Titanoboa cerrejonensis
animal_id: ANM-059
rarity: Secret
family: Other Animals
role: Controller
habitat: Emberheart Caldera
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - secret
  - other-animals
  - controller
  - emberheart-caldera
---

# Titanoboa

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Titanoboa |
| Species | *Titanoboa cerrejonensis* |
| Rarity | Secret |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Emberheart Caldera]] |
| Asset ID | ANM-059 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

The largest snake ever discovered. It coils around its prey and crushes the life out of it.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Secret Egg]]. Chance inside the Secret pool: 18.75% at P = 0.0, 20.69% at P = 0.3 (baseline), 24.40% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.00414% per roll at baseline P = 0.3; 0.0129% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Secret Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emberheart Caldera]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 2,700 s window (10% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 912 | |
| Damage (ATK per basic hit) | 76.8 | |
| Defence | 45.6 | 31.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 76.8 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.865 | Role target 0.865 ([[Animal Stat Budget Model]]) |

**Wild version in Emberheart Caldera** (region multiplier ×8.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 15,504, ATK 489.6, DEF 45.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Secret) | 400 | 300 |
| Defeated in Emberheart Caldera (×8.5) | 3,400 | 2,550 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Coil Strike | Auto | 9 s | Strikes for 180% ATK and roots for 1.2 s. |
| Crushing Embrace | Manual | 20 s | Coils around its target for 3 s (stun; bosses: 50% slow instead), dealing 400% ATK over the duration; nearby enemies within 8 studs are knocked back. |
| Constrictor | Passive (always on) | — | Deals 40% ATK per second to enemies it has rooted. |

**Ability activation type:** Coil Strike is **auto**, Crushing Embrace is **manual**; Constrictor is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Titanoboa are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 912 | 76.8 | 45.6 | 100% | Base appearance |
| A1 | 1 | 1 | 6,400 | 985 | 82.9 | 49.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 12,800 | 1,058 | 89.1 | 52.9 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 19,200 | 1,131 | 95.2 | 56.5 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 25,600 | 1,204 | 101.4 | 60.2 | 120% | Particle accents on movement |
| A5 | 1 | 5 | 32,000 | 1,277 | 107.5 | 63.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A massive olive body with dark saddles.

**Distinctive features:** Body built from 12 segments for coiling; the head is a broad wedge.

| Colour | Use |
|---|---|
| `#556B2F` | Scales |
| `#2F3A1F` | Saddles |
| `#C9C27A` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-059 Titanoboa (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Serpent (giant); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 8,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-059 in the [[Asset Register]] |

## Animation requirements

Signature motion: Rectilinear slither, coil-rest idle, wrap-around crush (segments follow a spline).

Required clips: idle (2 variants), walk, run, basic attack, Coil Strike, Crushing Embrace, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Coil Strike effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Crushing Embrace effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Secret) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep hiss; scale grinding; creaking constriction. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** The longest single-target disable.
- **Weaknesses:** Weaker against groups.

## Balance notes

- Power Index 0.865 against a Controller target of 0.865 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Secret animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Cobra]] · [[Komodo Dragon]] · [[Mini-Boss - Vinecoil]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Secret Egg]] · [[Region - Emberheart Caldera]] · [[Animal Combat Behaviour]] · [[Ascension System]]
