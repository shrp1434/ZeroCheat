---
title: Peregrine Falcon
type: animal
name: Peregrine Falcon
species: Falco peregrinus
animal_id: ANM-048
rarity: Legendary
family: Birds
role: Skirmisher
habitat: Skyreach Peaks
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - birds
  - skirmisher
  - skyreach-peaks
---

# Peregrine Falcon

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Peregrine Falcon |
| Species | *Falco peregrinus* |
| Rarity | Legendary |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Skyreach Peaks]] |
| Asset ID | ANM-048 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The fastest animal on Earth. It opens every fight with a devastating high-speed stoop.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 16.05% at P = 0.0, 15.38% at P = 0.3 (baseline), 14.03% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1231% per roll at baseline P = 0.3; 0.2458% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Skyreach Peaks]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 484 | |
| Damage (ATK per basic hit) | 45.6 | |
| Defence | 20.5 | 17.0% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 70.7 |
| Movement speed | 23.9 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.994 | Role target 1.004 ([[Animal Stat Budget Model]]) |

Species tweak applied: MS ×1.15, DEF ×0.90.

**Wild version in Skyreach Peaks** (region multiplier ×6.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 6,008, ATK 212.0, DEF 20.5.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Skyreach Peaks (×6.2) | 589 | 496 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Raking Talons | Auto | 7 s | Four rapid strikes, each 60% ATK. |
| Sonic Stoop | Manual | 15 s | Climbs, then dives at triple speed: 300% ATK and a small 5-stud area hit. |
| Stoop | Passive (always on) | — | Its first attack after 3 s out of combat deals +100% damage. |

**Ability activation type:** Raking Talons is **auto**, Sonic Stoop is **manual**; Stoop is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Peregrine Falcon are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 484 | 45.6 | 20.5 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 523 | 49.2 | 22.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 562 | 52.9 | 23.8 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 601 | 56.5 | 25.4 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 640 | 60.2 | 27.1 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 678 | 63.8 | 28.7 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A slate-blue back, pointed wings and a black 'moustache' mark.

**Distinctive features:** A compact, aerodynamic silhouette with swept wings.

| Colour | Use |
|---|---|
| `#4F5D75` | Back |
| `#F2EFE9` | Chest barring |
| `#F2C14E` | Feet and eye ring |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-048 Peregrine Falcon (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (raptor, flight); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-048 in the [[Asset Register]] |

## Animation requirements

Signature motion: Rapid wingbeats, perch idle, vertical climb and tuck-dive.

Required clips: idle (2 variants), walk, run, basic attack, Raking Talons, Sonic Stoop, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Raking Talons effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Sonic Stoop effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Sharp 'kak-kak' call; sonic whoosh crescendo on the stoop. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Huge opening burst; speed.
- **Weaknesses:** Lower defence; weaker in long fights.

## Balance notes

- Power Index 0.994 against a Skirmisher target of 1.004 (difference -0.009; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Golden Eagle]] · [[Cheetah]] · [[Haast's Eagle]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Skyreach Peaks]] · [[Animal Combat Behaviour]] · [[Ascension System]]
