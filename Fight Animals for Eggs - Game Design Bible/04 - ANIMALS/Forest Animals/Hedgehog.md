---
title: Hedgehog
type: animal
name: Hedgehog
species: Erinaceus europaeus
animal_id: ANM-003
rarity: Common
family: Forest Animals
role: Tank
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
  - tank
  - whisperwood-forest
---

# Hedgehog

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Hedgehog |
| Species | *Erinaceus europaeus* |
| Rarity | Common |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-003 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A pocket-sized fortress. The first Tank most players meet, it shows how taunts and damage reflection protect fragile teammates.

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
| Health | 310 | |
| Damage (ATK per basic hit) | 14.0 | |
| Defence | 16.0 | 13.8% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 11.9 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.986 | Role target 0.986 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 620, ATK 10.5, DEF 16.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Spine Curl | Manual | 14 s | Curls into a spiked ball for 3 s: takes -60% damage, reflects 20% of melee damage received, and taunts enemies that strike it. |

**Ability activation type:** Spine Curl is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Hedgehog are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 310 | 14.0 | 16.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 335 | 15.1 | 17.3 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 360 | 16.2 | 18.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 384 | 17.4 | 19.8 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 409 | 18.5 | 21.1 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 434 | 19.6 | 22.4 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A dome of low-poly spine cones over a small pointed snout.

**Distinctive features:** Spine cones grouped in 3-4 flat-shaded clusters to stay within budget; curl pose is a separate silhouette.

| Colour | Use |
|---|---|
| `#6B4F3A` | Spines |
| `#D9C2A0` | Face and belly |
| `#2B2B2B` | Nose and eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-003 Hedgehog (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (low body); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-003 in the [[Asset Register]] |

## Animation requirements

Signature motion: Quick shuffling trot, sniff idle, roll-up transition (8 frames) into a rolling-ball state.

Required clips: idle (2 variants), walk, run, basic attack, Spine Curl, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Spine Curl effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Tiny huffs and snuffles; a bristling 'shk' on curl; thin metallic ping on reflected hits. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Turns enemy aggression against itself; excellent with Ranged and Support partners.
- **Weaknesses:** Low damage; Spine Curl is manual and wasted if mistimed.

## Balance notes

- Power Index 0.986 against a Tank target of 0.986 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Crab]] · [[Penguin]] · [[Rabbit]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
