---
title: Rhino
type: animal
name: Rhino
species: Ceratotherium simum
animal_id: ANM-037
rarity: Epic
family: Safari Animals
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
  - epic
  - safari-animals
  - bruiser
  - sunscorch-savanna
---

# Rhino

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Rhino |
| Species | *Ceratotherium simum* |
| Rarity | Epic |
| Animal family | Safari Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-037 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

An armoured battering ram. It regenerates a protective shield and launches enemies with devastating charges.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 484 | |
| Damage (ATK per basic hit) | 44.0 | |
| Defence | 24.2 | 19.5% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 41.8 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.031 | Role target 1.031 ([[Animal Stat Budget Model]]) |

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,452, ATK 49.5, DEF 24.2.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Sunscorch Savanna (×1.5) | 75 | 68 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Armoured Hide | Auto | 10 s | Gains a shield equal to 12% of max HP (refreshed every 10 s). |
| Rampage Charge | Manual | 14 s | Charges 24 studs: 200% ATK to everything hit and a 1 s knock-up. |

**Ability activation type:** Armoured Hide is **auto**, Rampage Charge is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Rhino are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 484 | 44.0 | 24.2 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 523 | 47.5 | 26.1 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 561 | 51.0 | 28.1 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 600 | 54.6 | 30.0 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 639 | 58.1 | 31.9 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 678 | 61.6 | 33.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Two horns and plated hide.

**Distinctive features:** Low-slung head with a raised shoulder.

| Colour | Use |
|---|---|
| `#8A8A84` | Hide |
| `#6B6B65` | Plates |
| `#D8D2C0` | Horns |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-037 Rhino (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (heavy); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-037 in the [[Asset Register]] |

## Animation requirements

Signature motion: Trot to gallop, head-lowered paw-scrape (10 frames), horn-toss impact.

Required clips: idle (2 variants), walk, run, basic attack, Armoured Hide, Rampage Charge, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Armoured Hide effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rampage Charge effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Snorts; stampede rumble; armour clank on the shield refresh. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Durable damage dealer; reliable engage.
- **Weaknesses:** The charge is easy to dodge; poor against Ranged kiting.

## Balance notes

- Power Index 1.031 against a Bruiser target of 1.031 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Boar]] · [[Elephant]] · [[Hippo]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
