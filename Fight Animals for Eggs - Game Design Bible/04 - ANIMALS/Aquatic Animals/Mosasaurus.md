---
title: Mosasaurus
type: animal
name: Mosasaurus
species: Mosasaurus hoffmannii
animal_id: ANM-057
rarity: Secret
family: Aquatic Animals
role: Assassin
habitat: Starfall Sanctuary
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - secret
  - aquatic-animals
  - assassin
  - starfall-sanctuary
---

# Mosasaurus

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Mosasaurus |
| Species | *Mosasaurus hoffmannii* |
| Rarity | Secret |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Starfall Sanctuary]] |
| Asset ID | ANM-057 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

A prehistoric sea tyrant. It devours disabled prey and erupts from below in a shockwave.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Secret Egg]]. Chance inside the Secret pool: 36.76% at P = 0.0, 34.48% at P = 0.3 (baseline), 30.12% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.00690% per roll at baseline P = 0.3; 0.0160% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Secret Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Starfall Sanctuary]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 2,700 s window (10% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 720 | |
| Damage (ATK per basic hit) | 139.2 | |
| Defence | 33.6 | 25.1% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 146.2 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.015 | Role target 1.015 ([[Animal Stat Budget Model]]) |

**Wild version in Starfall Sanctuary** (region multiplier ×11.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 16,560, ATK 1200.6, DEF 33.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Secret) | 400 | 300 |
| Defeated in Starfall Sanctuary (×11.5) | 4,600 | 3,450 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Jaws of the Deep | Auto | 7 s | Bites for 260% ATK and heals for 20% of the damage dealt. |
| Leviathan Breach | Manual | 16 s | Plunges and erupts: 360% ATK to its target, 150% ATK within 10 studs, and a 1.2 s knock-up. |
| Sea Tyrant | Passive (always on) | — | +25% damage against enemies under crowd control. |

**Ability activation type:** Jaws of the Deep is **auto**, Leviathan Breach is **manual**; Sea Tyrant is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Mosasaurus are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 720 | 139.2 | 33.6 | 100% | Base appearance |
| A1 | 1 | 1 | 6,400 | 778 | 150.3 | 36.3 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 12,800 | 835 | 161.5 | 39.0 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 19,200 | 893 | 172.6 | 41.7 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 25,600 | 950 | 183.7 | 44.4 | 120% | Particle accents on movement |
| A5 | 1 | 5 | 32,000 | 1,008 | 194.9 | 47.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A crocodilian head on a whale-like body, with four flippers and a tail fluke.

**Distinctive features:** A double-hinged jaw; scale plates in the low-poly facets.

| Colour | Use |
|---|---|
| `#2F5D62` | Back |
| `#A7D7C5` | Belly |
| `#E0F2E9` | Teeth |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-057 Mosasaurus (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim, prehistoric marine reptile); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 7,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-057 in the [[Asset Register]] |

## Animation requirements

Signature motion: Powerful tail-driven air-swim, jaw-snap idle, breach eruption.

Required clips: idle (2 variants), walk, run, basic attack, Jaws of the Deep, Leviathan Breach, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Jaws of the Deep effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Leviathan Breach effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Secret) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Reptilian bellow with a water reverb; a cavernous bite. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** The top single-target burst in the game; pairs with Controllers.
- **Weaknesses:** Fragile for a Secret.

## Balance notes

- Power Index 1.015 against a Assassin target of 1.015 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Secret animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Megalodon]] · [[Great White Shark]] · [[Giant Squid]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Secret Egg]] · [[Region - Starfall Sanctuary]] · [[Animal Combat Behaviour]] · [[Ascension System]]
