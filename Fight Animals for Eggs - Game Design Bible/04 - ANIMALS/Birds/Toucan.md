---
title: Toucan
type: animal
name: Toucan
species: Ramphastos toco
animal_id: ANM-029
rarity: Rare
family: Birds
role: Ranged
habitat: Emerald Canopy
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - birds
  - ranged
  - emerald-canopy
---

# Toucan

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Toucan |
| Species | *Ramphastos toco* |
| Rarity | Rare |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-029 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A vivid canopy gunner that sprays seeds and exposes hidden enemies with its bright beak.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 12.15% at P = 0.0, 11.76% at P = 0.3 (baseline), 10.95% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.059% per roll at baseline P = 0.3; 1.483% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 255 | |
| Damage (ATK per basic hit) | 39.1 | |
| Defence | 11.9 | 10.6% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 39.1 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 26 studs | |
| Power Index | 0.908 | Role target 0.908 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,122, ATK 64.5, DEF 11.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Emerald Canopy (×2.2) | 62 | 55 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Seed Barrage | Auto | 7 s | Fires a cone of five seeds (range 26 studs), each 50% ATK. |
| Bright Beak Flare | Manual | 16 s | Reveals camouflaged enemies within 20 studs and reduces its target's DEF by 20% for 5 s. |

**Ability activation type:** Seed Barrage is **auto**, Bright Beak Flare is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Toucan are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 255 | 39.1 | 11.9 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 275 | 42.2 | 12.9 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 296 | 45.4 | 13.8 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 316 | 48.5 | 14.8 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 337 | 51.6 | 15.7 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 357 | 54.7 | 16.7 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A huge orange bill (40% of its body length).

**Distinctive features:** Hops between perches; bill tilts to aim.

| Colour | Use |
|---|---|
| `#111111` | Plumage |
| `#FF8C1A` | Bill |
| `#FFFFFF` | Throat |
| `#3FA7D6` | Eye ring |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-029 Toucan (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (ground and flight); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-029 in the [[Asset Register]] |

## Animation requirements

Signature motion: Bouncy hop, short flight, bill-flick barrage.

Required clips: idle (2 variants), walk, run, basic attack, Seed Barrage, Bright Beak Flare, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Seed Barrage effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Bright Beak Flare effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Croaking call; popcorn-like seed volley; bright flare chime. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Counters stealth; area ranged damage.
- **Weaknesses:** Low health; the cone falls off at range.

## Balance notes

- Power Index 0.908 against a Ranged target of 0.908 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Squirrel]] · [[Peacock]] · [[Leopard]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
