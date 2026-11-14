---
title: Tiger
type: animal
name: Tiger
species: Panthera tigris
animal_id: ANM-034
rarity: Epic
family: Big Cats
role: Assassin
habitat: Emerald Canopy
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - big-cats
  - assassin
  - emerald-canopy
---

# Tiger

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Tiger |
| Species | *Panthera tigris* |
| Rarity | Epic |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-034 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A striped apex hunter. It shreds targets with bleeding claws and chains ambush leaps when it secures a defeat.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 330 | |
| Damage (ATK per basic hit) | 63.8 | |
| Defence | 15.4 | 13.3% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 67.0 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.039 | Role target 1.039 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,452, ATK 105.3, DEF 15.4.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Emerald Canopy (×2.2) | 110 | 99 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Rending Claws | Auto | 8 s | Three claw swipes, each 80% ATK, applying a bleed of 30% ATK per second for 4 s. |
| Ambush Leap | Manual | 14 s | Leaps up to 24 studs for 250% ATK; if the target is defeated, this cooldown is reduced by 50%. |

**Ability activation type:** Rending Claws is **auto**, Ambush Leap is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Tiger are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 330 | 63.8 | 15.4 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 356 | 68.9 | 16.6 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 383 | 74.0 | 17.9 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 409 | 79.1 | 19.1 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 436 | 84.2 | 20.3 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 462 | 89.3 | 21.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Bold stripes and a white cheek ruff.

**Distinctive features:** Heavy forelimbs; tail held low while stalking.

| Colour | Use |
|---|---|
| `#F07F1E` | Coat |
| `#141414` | Stripes |
| `#FFF4E0` | Cheeks and belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-034 Tiger (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (felid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-034 in the [[Asset Register]] |

## Animation requirements

Signature motion: Powerful gallop, tail-flick stalk, claw-rake triple (frames 4, 9, 14 contact).

Required clips: idle (2 variants), walk, run, basic attack, Rending Claws, Ambush Leap, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Rending Claws effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Ambush Leap effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chuffing; full roar on the leap; tearing claw swishes. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Highest sustained Epic damage; snowballs in multi-enemy fights.
- **Weaknesses:** Fragile against Tanks with taunts and reflection.

## Balance notes

- Power Index 1.039 against a Assassin target of 1.039 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Leopard]] · [[Lion]] · [[Sabre-Tooth Tiger]] · [[Snow Leopard]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
