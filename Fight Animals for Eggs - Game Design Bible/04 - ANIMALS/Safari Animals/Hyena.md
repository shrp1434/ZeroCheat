---
title: Hyena
type: animal
name: Hyena
species: Crocuta crocuta
animal_id: ANM-018
rarity: Uncommon
family: Safari Animals
role: Skirmisher
habitat: Sunscorch Savanna
pool_class: Standard
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - safari-animals
  - skirmisher
  - sunscorch-savanna
---

# Hyena

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Hyena |
| Species | *Crocuta crocuta* |
| Rarity | Uncommon |
| Animal family | Safari Animals (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-018 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A pack scrapper that grows bolder with friends nearby and slows anything it bites.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 11.44% at P = 0.0, 10.99% at P = 0.3 (baseline), 10.06% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 2.418% per roll at baseline P = 0.3; 2.569% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 221 | |
| Damage (ATK per basic hit) | 20.8 | |
| Defence | 10.4 | 9.4% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 32.2 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.015 | Role target 1.015 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 663, ATK 23.4, DEF 10.4.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Sunscorch Savanna (×1.5) | 24 | 22 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Pack Laugh | Auto | 10 s | Cackles, gaining +10% damage per ally within 12 studs (the player counts; maximum +30%) for 6 s. During this time its basic attacks slow by 10% for 3 s. |

**Ability activation type:** Pack Laugh is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Hyena are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 221 | 20.8 | 10.4 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 239 | 22.5 | 11.2 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 256 | 24.1 | 12.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 274 | 25.8 | 12.9 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 292 | 27.5 | 13.7 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 309 | 29.1 | 14.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A sloped back (front legs longer) and round ears.

**Distinctive features:** Spotted pattern as decal clusters; stubby tail.

| Colour | Use |
|---|---|
| `#B49A6A` | Coat |
| `#3A2E22` | Spots |
| `#2A2A2A` | Muzzle |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-018 Hyena (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped (sloped back); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-018 in the [[Asset Register]] |

## Animation requirements

Signature motion: Loping gait, head-low prowl idle, cackle shake.

Required clips: idle (2 variants), walk, run, basic attack, Pack Laugh, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Pack Laugh effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Whooping laugh (pitch-varied), snapping bites. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Scales with a full team; sticky slows.
- **Weaknesses:** Weaker when separated; moderate health.

## Balance notes

- Power Index 1.015 against a Skirmisher target of 1.015 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Wolf]] · [[Lion]] · [[Meerkat]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
