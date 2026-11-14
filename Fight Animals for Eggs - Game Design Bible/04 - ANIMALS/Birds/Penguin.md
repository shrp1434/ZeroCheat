---
title: Penguin
type: animal
name: Penguin
species: Aptenodytes forsteri
animal_id: ANM-023
rarity: Uncommon
family: Birds
role: Tank
habitat: Frostfang Tundra
pool_class: Elusive
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - uncommon
  - birds
  - tank
  - frostfang-tundra
---

# Penguin

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Penguin |
| Species | *Aptenodytes forsteri* |
| Rarity | Uncommon |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Frostfang Tundra]] |
| Asset ID | ANM-023 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

An emperor of the ice whose huddle shelters the whole team. The rarest Uncommon.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Uncommon Egg]]. Chance inside the Uncommon pool: 2.403% at P = 0.0, 3.297% at P = 0.3 (baseline), 5.131% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.7253% per roll at baseline P = 0.3; 1.310% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Uncommon Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Frostfang Tundra]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 35 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 403 | |
| Damage (ATK per basic hit) | 18.2 | |
| Defence | 20.8 | 17.2% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 15.5 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.993 | Role target 0.993 ([[Animal Stat Budget Model]]) |

**Wild version in Frostfang Tundra** (region multiplier ×4.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 3,627, ATK 61.4, DEF 20.8.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Uncommon) | 16 | 15 |
| Defeated in Frostfang Tundra (×4.5) | 72 | 68 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Huddle | Auto | 18 s | For 5 s, allies within 8 studs take -20% damage, and the Penguin taunts adjacent enemies. |

**Ability activation type:** Huddle is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Penguin are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 403 | 18.2 | 20.8 | 100% | Base appearance |
| A1 | 1 | 1 | 200 | 435 | 19.7 | 22.5 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 400 | 467 | 21.1 | 24.1 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 600 | 500 | 22.6 | 25.8 | 115% | Soft rarity aura |
| A4 | 3 | 9 | 800 | 532 | 24.0 | 27.5 | 120% | Particle accents on movement |
| A5 | 4 | 13 | 1,000 | 564 | 25.5 | 29.1 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** An upright tuxedo body with yellow ear patches.

**Distinctive features:** Flipper wobble when walking; belly-slide locomotion over ice.

| Colour | Use |
|---|---|
| `#1C1C24` | Back |
| `#FFFFFF` | Front |
| `#F5C542` | Ear patches |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-023 Penguin (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (flightless, upright); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-023 in the [[Asset Register]] |

## Animation requirements

Signature motion: Waddle, belly-slide on ice surfaces, flipper-flap idle, huddle squat.

Required clips: idle (2 variants), walk, run, basic attack, Huddle, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Huddle effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Uncommon) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Trumpeting call; padding footsteps; whoosh on belly slide. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team-wide damage reduction; reliable automatic trigger.
- **Weaknesses:** Slow; low damage.

## Balance notes

- Power Index 0.993 against a Tank target of 0.993 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Uncommon animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Duck]] · [[Seal]] · [[Walrus]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Uncommon Egg]] · [[Region - Frostfang Tundra]] · [[Animal Combat Behaviour]] · [[Ascension System]]
