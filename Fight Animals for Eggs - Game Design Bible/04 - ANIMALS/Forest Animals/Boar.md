---
title: Boar
type: animal
name: Boar
species: Sus scrofa
animal_id: ANM-008
rarity: Common
family: Forest Animals
role: Bruiser
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Manual
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - forest-animals
  - bruiser
  - whisperwood-forest
---

# Boar

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Boar |
| Species | *Sus scrofa* |
| Rarity | Common |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-008 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A stubborn forest brawler that barrels through enemy lines. A dependable all-rounder for new teams.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 10.59% at P = 0.0, 10.20% at P = 0.3 (baseline), 9.398% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 6.633% per roll at baseline P = 0.3; 4.994% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 220 | |
| Damage (ATK per basic hit) | 20.0 | |
| Defence | 11.0 | 9.9% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 19.0 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.027 | Role target 1.027 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 440, ATK 15.0, DEF 11.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Tusk Charge | Manual | 12 s | Charges up to 18 studs in a straight line, dealing 150% ATK to every enemy hit and knocking them back 6 studs. |

**Ability activation type:** Tusk Charge is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Boar are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 220 | 20.0 | 11.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 238 | 21.6 | 11.9 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 255 | 23.2 | 12.8 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 273 | 24.8 | 13.6 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 290 | 26.4 | 14.5 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 308 | 28.0 | 15.4 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A wedge-shaped head with upturned tusks and a bristly mane ridge.

**Distinctive features:** Short legs, heavy shoulders, snout snuffle idle.

| Colour | Use |
|---|---|
| `#5C4033` | Coat |
| `#3B2A20` | Mane ridge |
| `#F1E9D2` | Tusks |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-008 Boar (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped; see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-008 in the [[Asset Register]] |

## Animation requirements

Signature motion: Trotting run, hoof-scrape wind-up before the charge, head-toss impact.

Required clips: idle (2 variants), walk, run, basic attack, Tusk Charge, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Tusk Charge effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Grunts and snorts; thundering hoof loop on charge; thud on impact. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Line damage and displacement; durable enough to front-line early.
- **Weaknesses:** Charge can overshoot into danger; no sustain.

## Balance notes

- Power Index 1.027 against a Bruiser target of 1.027 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Rhino]] · [[Goat]] · [[Hippo]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
