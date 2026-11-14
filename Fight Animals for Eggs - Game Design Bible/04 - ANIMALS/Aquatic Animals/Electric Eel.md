---
title: Electric Eel
type: animal
name: Electric Eel
species: Electrophorus electricus
animal_id: ANM-041
rarity: Epic
family: Aquatic Animals
role: Ranged
habitat: Emerald Canopy
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - aquatic-animals
  - ranged
  - emerald-canopy
---

# Electric Eel

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Electric Eel |
| Species | *Electrophorus electricus* |
| Rarity | Epic |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Emerald Canopy]] |
| Asset ID | ANM-041 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Neon, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A living battery from the jungle rivers. Its lightning chains between enemies.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 7.054% at P = 0.0, 8.000% at P = 0.3 (baseline), 9.963% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.2400% per roll at baseline P = 0.3; 0.5522% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emerald Canopy]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 330 | |
| Damage (ATK per basic hit) | 50.6 | |
| Defence | 15.4 | 13.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 50.6 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 28 studs | |
| Power Index | 0.903 | Role target 0.903 ([[Animal Stat Budget Model]]) |

**Wild version in Emerald Canopy** (region multiplier ×2.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 1,452, ATK 83.5, DEF 15.4.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Emerald Canopy (×2.2) | 110 | 99 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Chain Shock | Auto | 8 s | Lightning strikes its target and chains to 2 more enemies within 10 studs: 110% / 70% / 50% ATK. |
| Overcharge | Manual | 18 s | For 4 s its basic attacks chain to one extra enemy, and the first hit each second stuns for 0.4 s. |

**Ability activation type:** Chain Shock is **auto**, Overcharge is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Electric Eel are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 330 | 50.6 | 15.4 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 356 | 54.6 | 16.6 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 383 | 58.7 | 17.9 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 409 | 62.7 | 19.1 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 436 | 66.8 | 20.3 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 462 | 70.8 | 21.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A long eel body with glowing yellow underside lines.

**Distinctive features:** Glow lines pulse with the ability cooldown state.

| Colour | Use |
|---|---|
| `#2E3B2F` | Body |
| `#F7E23B` | Glow lines (Neon material) |
| `#C9A227` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-041 Electric Eel (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Serpent (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-041 in the [[Asset Register]] |

## Animation requirements

Signature motion: Serpentine air-swim, coil idle, discharge arch.

Required clips: idle (2 variants), walk, run, basic attack, Chain Shock, Overcharge, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Chain Shock effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Overcharge effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Electrical crackle loop; zap chains; buzzing overcharge hum. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Chain damage; mini-stuns.
- **Weaknesses:** Fragile; the chain needs clustered enemies.

## Balance notes

- Power Index 0.903 against a Ranged target of 0.903 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Octopus]] · [[Cobra]] · [[Titanoboa]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Emerald Canopy]] · [[Animal Combat Behaviour]] · [[Ascension System]]
