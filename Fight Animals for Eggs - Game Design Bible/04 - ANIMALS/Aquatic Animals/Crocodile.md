---
title: Crocodile
type: animal
name: Crocodile
species: Crocodylus niloticus
animal_id: ANM-036
rarity: Epic
family: Aquatic Animals
role: Controller
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
  - aquatic-animals
  - controller
  - emerald-canopy
---

# Crocodile

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Crocodile |
| Species | *Crocodylus niloticus* |
| Rarity | Epic |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-036 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A patient river ambusher. It snaps at anything that comes close and drags single targets into a death roll.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

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

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,839, ATK 58.1, DEF 20.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Emerald Canopy (×2.2) | 110 | 99 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Ambush Snap | Auto | 10 s | When an enemy comes within 6 studs: a snap for 160% ATK and a 1 s root. |
| Death Roll | Manual | 16 s | Grabs its target and rolls for 2 s: the target is stunned and takes 260% ATK over the roll. Against bosses it deals damage only, without the stun. |

**Ability activation type:** Ambush Snap is **auto**, Death Roll is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Crocodile are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 418 | 35.2 | 20.9 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 451 | 38.0 | 22.6 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 485 | 40.8 | 24.2 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 518 | 43.6 | 25.9 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 552 | 46.5 | 27.6 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 585 | 49.3 | 29.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A long low snout, armoured scutes and a heavy tail.

**Distinctive features:** Scutes are extruded ridges along the back; the jaw opens 60 degrees.

| Colour | Use |
|---|---|
| `#4E6B3A` | Hide |
| `#A7B46E` | Belly |
| `#E8E2A0` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-036 Crocodile (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Low quadruped (reptile); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-036 in the [[Asset Register]] |

## Animation requirements

Signature motion: Belly crawl and high walk, jaw-open bask idle, full-body roll.

Required clips: idle (2 variants), walk, run, basic attack, Ambush Snap, Death Roll, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Ambush Snap effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Death Roll effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Hissing growl; heavy jaw clap; water churn on the roll. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Long hard disable; punishes melee rushers.
- **Weaknesses:** Slow; Death Roll locks the Crocodile in place too.

## Balance notes

- Power Index 0.868 against a Controller target of 0.868 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Komodo Dragon]] · [[Hippo]] · [[Frog]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
