---
title: Squirrel
type: animal
name: Squirrel
species: Sciurus vulgaris
animal_id: ANM-002
rarity: Common
family: Forest Animals
role: Ranged
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
  - ranged
  - whisperwood-forest
---

# Squirrel

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Squirrel |
| Species | *Sciurus vulgaris* |
| Rarity | Common |
| Animal family | Forest Animals (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-002 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A tree-dwelling sharpshooter that pelts enemies with acorns. The earliest ranged animal and a lesson in keeping damage dealers behind a front line.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 10.59% at P = 0.0, 10.20% at P = 0.3 (baseline), 9.398% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 6.633% per roll at baseline P = 0.3; 4.994% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 150 | |
| Damage (ATK per basic hit) | 23.0 | |
| Defence | 7.0 | 6.5% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 23.0 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 28 studs | |
| Power Index | 0.916 | Role target 0.916 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 300, ATK 17.2, DEF 7.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Acorn Volley | Auto | 6 s | Throws three acorns in quick succession at its target (range 25 studs), each dealing 60% ATK. |

**Ability activation type:** Acorn Volley is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Squirrel are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 150 | 23.0 | 7.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 162 | 24.8 | 7.6 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 174 | 26.7 | 8.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 186 | 28.5 | 8.7 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 198 | 30.4 | 9.2 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 210 | 32.2 | 9.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A huge S-curved bushy tail as large as its body defines the silhouette.

**Distinctive features:** Tufted ears, cheek pouches that puff when throwing, acorn held in forepaws during idle.

| Colour | Use |
|---|---|
| `#B5562B` | Red-brown fur |
| `#F2E2C4` | Belly |
| `#6B3B1F` | Ear tufts |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-002 Squirrel (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (climber); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-002 in the [[Asset Register]] |

## Animation requirements

Signature motion: Scampering quick-step run, tail flick idle, overhand throw with a three-frame wind-up per acorn.

Required clips: idle (2 variants), walk, run, basic attack, Acorn Volley, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Acorn Volley effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chitter vocal, light 'tok' acorn impacts, tail rustle. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Safe, consistent ranged damage; good against slow Tanks and Controllers.
- **Weaknesses:** Very low health; collapses if Assassins or Skirmishers reach it.

## Balance notes

- Power Index 0.916 against a Ranged target of 0.916 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Rabbit]] · [[Toucan]] · [[Monkey]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
