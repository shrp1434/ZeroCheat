---
title: Crab
type: animal
name: Crab
species: Carcinus maenas
animal_id: ANM-012
rarity: Common
family: Aquatic Animals
role: Tank
habitat: Coral Coast
pool_class: Elusive
ability_activation: Manual
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - aquatic-animals
  - tank
  - coral-coast
---

# Crab

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Crab |
| Species | *Carcinus maenas* |
| Rarity | Common |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Coral Coast]] |
| Asset ID | ANM-012 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A sideways-scuttling shield that protects whoever stands behind it. The rarest Common, found on the coast.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 2.225% at P = 0.0, 3.061% at P = 0.3 (baseline), 4.793% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.990% per roll at baseline P = 0.3; 2.547% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Coral Coast]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 310 | |
| Damage (ATK per basic hit) | 14.0 | |
| Defence | 16.0 | 13.8% damage reduction |
| Attack speed | 0.85 hits/s | DPS from basic attacks ≈ 11.9 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.986 | Role target 0.986 ([[Animal Stat Budget Model]]) |

**Wild version in Coral Coast** (region multiplier ×3.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,984, ATK 33.6, DEF 16.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Coral Coast (×3.2) | 32 | 32 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Shell Guard | Manual | 16 s | Raises its claws for 4 s: blocks 70% of frontal damage, and allies within 4 studs behind it take -30% damage. |

**Ability activation type:** Shell Guard is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Crab are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 310 | 14.0 | 16.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 335 | 15.1 | 17.3 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 360 | 16.2 | 18.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 384 | 17.4 | 19.8 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 409 | 18.5 | 21.1 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 434 | 19.6 | 22.4 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A wide flat shell and one oversized claw: an asymmetric, readable profile.

**Distinctive features:** Stalk eyes that swivel independently; bubble idle.

| Colour | Use |
|---|---|
| `#E2553A` | Shell |
| `#F4A261` | Legs |
| `#FFF1E0` | Claw tips |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-012 Crab (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Crustacean (six legs, sideways walk); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-012 in the [[Asset Register]] |

## Animation requirements

Signature motion: Sideways scuttle, claw-snap idle, guard-raise pose.

Required clips: idle (2 variants), walk, run, basic attack, Shell Guard, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Shell Guard effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Clicky leg patter; claw snap; hollow shell 'tock' on blocked hits. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Directional protection for Ranged partners; strong against frontal attackers.
- **Weaknesses:** Weak against flanking Assassins; slow.

## Balance notes

- Power Index 0.986 against a Tank target of 0.986 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Hedgehog]] · [[Octopus]] · [[Walrus]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Coral Coast]] · [[Animal Combat Behaviour]] · [[Ascension System]]
