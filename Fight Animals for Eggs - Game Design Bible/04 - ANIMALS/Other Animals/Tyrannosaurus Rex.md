---
title: Tyrannosaurus Rex
type: animal
name: Tyrannosaurus Rex
species: Tyrannosaurus rex
animal_id: ANM-060
rarity: Secret
family: Other Animals
role: Bruiser
habitat: Emberheart Caldera
pool_class: Elusive
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - secret
  - other-animals
  - bruiser
  - emberheart-caldera
---

# Tyrannosaurus Rex

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Tyrannosaurus Rex |
| Species | *Tyrannosaurus rex* |
| Rarity | Secret |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Bruiser (see [[Animal Roles]]) |
| Habitat | [[Region - Emberheart Caldera]] |
| Asset ID | ANM-060 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

The tyrant lizard king. Its roar shakes the ground, empowers its team and makes enemies falter. The rarest animal in the game.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Secret Egg]]. Chance inside the Secret pool: 7.721% at P = 0.0, 10.34% at P = 0.3 (baseline), 15.36% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.00207% per roll at baseline P = 0.3; 0.00814% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Secret Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emberheart Caldera]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 2,700 s window (10% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 1,056 | |
| Damage (ATK per basic hit) | 103.7 | |
| Defence | 52.8 | 34.6% damage reduction |
| Attack speed | 0.95 hits/s | DPS from basic attacks ≈ 98.5 |
| Movement speed | 14.7 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.079 | Role target 1.039 ([[Animal Stat Budget Model]]) |

Species tweak applied: ATK ×1.08, MS ×0.92.

**Wild version in Emberheart Caldera** (region multiplier ×8.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 17,952, ATK 661.0, DEF 52.8.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Secret) | 400 | 300 |
| Defeated in Emberheart Caldera (×8.5) | 3,400 | 2,550 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Bone-Crush Bite | Auto | 8 s | Bites for 280% ATK and reduces the target's DEF by 30% for 5 s. |
| Earthshaker Roar | Manual | 22 s | Roars and stomps (radius 18): 220% ATK, a 1.5 s stun (0.5 s on bosses), and the team gains +20% damage for 6 s. |
| Tyrant King | Passive (always on) | — | Enemies within 12 studs deal -10% damage. |

**Ability activation type:** Bone-Crush Bite is **auto**, Earthshaker Roar is **manual**; Tyrant King is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Tyrannosaurus Rex are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 1,056 | 103.7 | 52.8 | 100% | Base appearance |
| A1 | 1 | 1 | 6,400 | 1,140 | 112.0 | 57.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 12,800 | 1,225 | 120.3 | 61.2 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 19,200 | 1,309 | 128.6 | 65.5 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 25,600 | 1,394 | 136.9 | 69.7 | 120% | Particle accents on movement |
| A5 | 1 | 5 | 32,000 | 1,478 | 145.2 | 73.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A huge head, tiny arms and a counterbalancing tail.

**Distinctive features:** A forward-leaning stance with the tail held level; companion scale capped (see the modelling principles).

| Colour | Use |
|---|---|
| `#5E6B3A` | Scales |
| `#A3A36B` | Stripes |
| `#E8D9A8` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-060 Tyrannosaurus Rex (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large biped (prehistoric theropod); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 7,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-060 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heavy stalking walk with head bob, sniff idle, roar with a head-sweep (24 frames).

Required clips: idle (2 variants), walk, run, basic attack, Bone-Crush Bite, Earthshaker Roar, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Bone-Crush Bite effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Earthshaker Roar effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Secret) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

The game's signature roar, layered low; earth-shaking footfalls. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Elite all-round damage and team buffs.
- **Weaknesses:** Slower movement; a large target.

## Balance notes

- Power Index 1.079 against a Bruiser target of 1.039 (difference +0.041; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Secret animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Titanoboa]] · [[Megalodon]] · [[Mini-Boss - Cinderjaw]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Secret Egg]] · [[Region - Emberheart Caldera]] · [[Animal Combat Behaviour]] · [[Ascension System]]
