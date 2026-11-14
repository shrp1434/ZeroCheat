---
title: Frog
type: animal
name: Frog
species: Rana temporaria
animal_id: ANM-005
rarity: Common
family: Other Animals
role: Controller
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
  - other-animals
  - controller
  - whisperwood-forest
---

# Frog

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Frog |
| Species | *Rana temporaria* |
| Rarity | Common |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-005 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A pond-side wrangler whose tongue drags enemies out of position. It is the simplest introduction to crowd control.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 10.59% at P = 0.0, 10.20% at P = 0.3 (baseline), 9.398% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 6.633% per roll at baseline P = 0.3; 4.994% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 190 | |
| Damage (ATK per basic hit) | 16.0 | |
| Defence | 9.5 | 8.7% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 16.0 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.870 | Role target 0.870 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 380, ATK 12.0, DEF 9.5.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Sticky Tongue | Manual | 10 s | Lashes a target up to 14 studs away, pulls it 8 studs towards the Frog and roots it for 1 s. Bosses are rooted but not pulled. |

**Ability activation type:** Sticky Tongue is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Frog are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 190 | 16.0 | 9.5 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 205 | 17.3 | 10.3 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 220 | 18.6 | 11.0 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 236 | 19.8 | 11.8 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 251 | 21.1 | 12.5 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 266 | 22.4 | 13.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A wide crouched body with bulging top-mounted eyes.

**Distinctive features:** Wide mouth line, throat sac puff idle, long folded hind legs.

| Colour | Use |
|---|---|
| `#5BAE4A` | Skin |
| `#F3E15B` | Belly |
| `#2E6B2A` | Spots |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-005 Frog (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Hopper (amphibian); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-005 in the [[Asset Register]] |

## Animation requirements

Signature motion: Leap-and-land locomotion, throat puff idle, tongue lash (tongue is a stretched Beam/part).

Required clips: idle (2 variants), walk, run, basic attack, Sticky Tongue, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Sticky Tongue effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Ribbit vocal; wet 'thwap' tongue; soft splat on landing. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Pulls ranged enemies into melee; peels attackers off the player.
- **Weaknesses:** Low damage and health; one control tool with a long cooldown.

## Balance notes

- Power Index 0.870 against a Controller target of 0.870 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Duck]] · [[Crocodile]] · [[Cobra]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
