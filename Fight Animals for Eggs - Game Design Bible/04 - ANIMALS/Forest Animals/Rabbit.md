---
title: Rabbit
type: animal
name: Rabbit
species: Oryctolagus cuniculus
animal_id: ANM-001
rarity: Common
family: Forest Animals
role: Skirmisher
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - forest-animals
  - skirmisher
  - whisperwood-forest
---

# Rabbit

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Rabbit |
| Species | *Oryctolagus cuniculus* |
| Rarity | Common |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-001 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

The first companion most players hatch. A twitchy, fast-hopping skirmisher that teaches new players to flank and reposition rather than stand still and trade hits.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 10.59% at P = 0.0, 10.20% at P = 0.3 (baseline), 9.398% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 6.633% per roll at baseline P = 0.3; 4.994% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 170 | |
| Damage (ATK per basic hit) | 16.0 | |
| Defence | 8.0 | 7.4% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 24.8 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.017 | Role target 1.017 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 340, ATK 12.0, DEF 8.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Burrow Dash | Auto | 8 s | Dashes up to 12 studs to the far side of its target and strikes for 140% ATK. Its next basic hit within 2 s deals +30% damage. |

**Ability activation type:** Burrow Dash is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Rabbit are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 170 | 16.0 | 8.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 184 | 17.3 | 8.6 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 197 | 18.6 | 9.3 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 211 | 19.8 | 9.9 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 224 | 21.1 | 10.6 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 238 | 22.4 | 11.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Two tall ears (35% of total height) make the silhouette unmistakable even at icon size.

**Distinctive features:** Spherical cotton tail, oversized hind feet, nose twitch blend on idle.

| Colour | Use |
|---|---|
| `#C9A27E` | Main fur |
| `#F3E6D8` | Belly and tail puff |
| `#E58FA0` | Inner ears and nose |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-001 Rabbit (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Hopper (small quadruped, bounding gait); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-001 in the [[Asset Register]] |

## Animation requirements

Signature motion: Bounding hop locomotion (two-beat), foot-thump alert idle, burrow-dip before the dash.

Required clips: idle (2 variants), walk, run, basic attack, Burrow Dash, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Burrow Dash effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Soft paw thumps, a short squeak on Burrow Dash, a rustling burrow whoosh. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Closes distance quickly; good at reaching enemy ranged units; Burrow Dash repositions it out of frontal cleaves.
- **Weaknesses:** Fragile; low per-hit damage; struggles against Tanks with damage reflection.

## Balance notes

- Power Index 1.017 against a Skirmisher target of 1.017 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Fox]] · [[Hedgehog]] · [[Squirrel]] · [[Kangaroo]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
