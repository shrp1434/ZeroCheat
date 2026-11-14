---
title: Giant Panda
type: animal
name: Giant Panda
species: Ailuropoda melanoleuca
animal_id: ANM-049
rarity: Legendary
family: Other Animals
role: Support
habitat: Skyreach Peaks
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - other-animals
  - support
  - skyreach-peaks
---

# Giant Panda

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Giant Panda |
| Species | *Ailuropoda melanoleuca* |
| Rarity | Legendary |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Skyreach Peaks]] |
| Asset ID | ANM-049 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Rainbow, Diamond (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A serene mountain guardian. It shares bamboo snacks to heal allies and rolls into battle when needed.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 8.186% at P = 0.0, 9.231% at P = 0.3 (baseline), 11.36% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0738% per roll at baseline P = 0.3; 0.1991% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Skyreach Peaks]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow, Diamond versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 570 | |
| Damage (ATK per basic hit) | 37.1 | |
| Defence | 28.5 | 22.2% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 37.1 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Skyreach Peaks** (region multiplier ×6.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 7,068, ATK 172.3, DEF 28.5.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Skyreach Peaks (×6.2) | 589 | 496 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Bamboo Snack | Auto | 16 s | Heals the lowest-HP ally for 22% of max HP and gives it +20% DEF for 4 s. |
| Rolling Tumble | Manual | 18 s | Rolls 14 studs: 150% ATK and knockback to enemies, then heals the team for 12% of max HP. |
| Calm Presence | Passive (always on) | — | The team regenerates 0.5% of max HP per second while in combat. |

**Ability activation type:** Bamboo Snack is **auto**, Rolling Tumble is **manual**; Calm Presence is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Giant Panda are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 570 | 37.1 | 28.5 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 616 | 40.0 | 30.8 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 661 | 43.0 | 33.1 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 707 | 45.9 | 35.3 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 752 | 48.9 | 37.6 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 798 | 51.9 | 39.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Black eye patches on a round white body.

**Distinctive features:** Sits to munch bamboo when idle.

| Colour | Use |
|---|---|
| `#F5F5F5` | Body |
| `#1A1A1A` | Limbs, ears and eye patches |
| `#7FB069` | Bamboo prop |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-049 Giant Panda (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (ursid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-049 in the [[Asset Register]] |

## Animation requirements

Signature motion: Rolling amble, bamboo-munch idle, forward somersault tumble.

Required clips: idle (2 variants), walk, run, basic attack, Bamboo Snack, Rolling Tumble, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Bamboo Snack effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rolling Tumble effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Bleats and squeaks; bamboo crunch; soft whump. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** The strongest sustain in the game.
- **Weaknesses:** Low damage.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Peacock]] · [[Brown Bear]] · [[Blue Whale]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Skyreach Peaks]] · [[Animal Combat Behaviour]] · [[Ascension System]]
