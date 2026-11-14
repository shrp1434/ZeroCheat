---
title: Snow Leopard
type: animal
name: Snow Leopard
species: Panthera uncia
animal_id: ANM-042
rarity: Epic
family: Big Cats
role: Controller
habitat: Skyreach Peaks
pool_class: Elusive
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - big-cats
  - controller
  - skyreach-peaks
---

# Snow Leopard

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Snow Leopard |
| Species | *Panthera uncia* |
| Rarity | Epic |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Skyreach Peaks]] |
| Asset ID | ANM-042 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A ghost of the peaks that freezes enemies with leaping avalanches. The rarest Epic.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 2.905% at P = 0.0, 4.000% at P = 0.3 (baseline), 6.273% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1200% per roll at baseline P = 0.3; 0.3477% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Skyreach Peaks]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 418 | |
| Damage (ATK per basic hit) | 35.2 | |
| Defence | 20.9 | 17.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 35.2 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.868 | Role target 0.868 ([[Animal Stat Budget Model]]) |

**Wild version in Skyreach Peaks** (region multiplier ×6.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 5,183, ATK 163.7, DEF 20.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Skyreach Peaks (×6.2) | 310 | 279 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Frost Pounce | Auto | 9 s | Pounces for 140% ATK and applies 2 Chill stacks (3 stacks freeze for 1 s). |
| Avalanche Leap | Manual | 18 s | Leaps high and lands in a 10-stud radius: 180% ATK and freezes enemies for 1.5 s (bosses: 50% slow instead). |

**Ability activation type:** Frost Pounce is **auto**, Avalanche Leap is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Snow Leopard are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 418 | 35.2 | 20.9 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 451 | 38.0 | 22.6 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 485 | 40.8 | 24.2 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 518 | 43.6 | 25.9 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 552 | 46.5 | 27.6 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 585 | 49.3 | 29.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A very long thick tail and smoky rosettes.

**Distinctive features:** Large paws; tail curled over the nose when resting.

| Colour | Use |
|---|---|
| `#D9DEE3` | Coat |
| `#6E7781` | Rosettes |
| `#9FC5E8` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-042 Snow Leopard (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Medium quadruped (felid, long tail); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-042 in the [[Asset Register]] |

## Animation requirements

Signature motion: Bounding run, tail-wrap idle, high leap with a snow-burst landing.

Required clips: idle (2 variants), walk, run, basic attack, Frost Pounce, Avalanche Leap, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Frost Pounce effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Avalanche Leap effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chuffing; snow crunch; avalanche rumble on landing. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area freeze; synergises with Chill from Arctic Fox and Narwhal.
- **Weaknesses:** Modest damage outside combos.

## Balance notes

- Power Index 0.868 against a Controller target of 0.868 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Leopard]] · [[Arctic Fox]] · [[Tiger]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Skyreach Peaks]] · [[Animal Combat Behaviour]] · [[Ascension System]]
