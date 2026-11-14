---
title: Dolphin
type: animal
name: Dolphin
species: Tursiops truncatus
animal_id: ANM-040
rarity: Epic
family: Aquatic Animals
role: Support
habitat: Coral Coast
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - aquatic-animals
  - support
  - coral-coast
---

# Dolphin

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Dolphin |
| Species | *Tursiops truncatus* |
| Rarity | Epic |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Coral Coast]] |
| Asset ID | ANM-040 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow, Neon, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A brilliant reef medic that heals the most injured ally and empowers the team with sonar.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Coral Coast]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Neon, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 440 | |
| Damage (ATK per basic hit) | 28.6 | |
| Defence | 22.0 | 18.0% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 28.6 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Coral Coast** (region multiplier ×3.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,816, ATK 68.6, DEF 22.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Coral Coast (×3.2) | 160 | 144 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Echo Song | Auto | 14 s | Heals the lowest-HP ally for 18% of max HP and removes one debuff. |
| Sonar Pulse | Manual | 18 s | Pulse (radius 14): reveals camouflaged enemies, deals 100% ATK, and gives the team +15% damage for 5 s. |

**Ability activation type:** Echo Song is **auto**, Sonar Pulse is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Dolphin are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 440 | 28.6 | 22.0 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 475 | 30.9 | 23.8 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 510 | 33.2 | 25.5 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 546 | 35.5 | 27.3 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 581 | 37.8 | 29.0 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 616 | 40.0 | 30.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A sleek body with a curved dorsal fin and a smiling beak.

**Distinctive features:** A water trail ribbon follows the tail fluke.

| Colour | Use |
|---|---|
| `#6FA8DC` | Back |
| `#CFE2F3` | Belly |
| `#3D6E99` | Fin edges |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-040 Dolphin (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 4,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-040 in the [[Asset Register]] |

## Animation requirements

Signature motion: Undulating air-swim, barrel-roll idle, sonar ring cast.

Required clips: idle (2 variants), walk, run, basic attack, Echo Song, Sonar Pulse, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Echo Song effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Sonar Pulse effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Clicks and whistles; sonar ping; bubbling heal. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Targeted heal plus a team damage buff.
- **Weaknesses:** Modest durability.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Orca]] · [[Blue Whale]] · [[Seal]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Coral Coast]] · [[Animal Combat Behaviour]] · [[Ascension System]]
