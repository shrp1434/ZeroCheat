---
title: Orca
type: animal
name: Orca
species: Orcinus orca
animal_id: ANM-046
rarity: Legendary
family: Aquatic Animals
role: Controller
habitat: Frostfang Tundra
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - aquatic-animals
  - controller
  - frostfang-tundra
---

# Orca

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Orca |
| Species | *Orcinus orca* |
| Rarity | Legendary |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Frostfang Tundra]] |
| Asset ID | ANM-046 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

An intelligent pod hunter. It stuns, launches and slows enemies so the whole team can pile on.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 16.05% at P = 0.0, 15.38% at P = 0.3 (baseline), 14.03% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1231% per roll at baseline P = 0.3; 0.2458% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Frostfang Tundra]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 542 | |
| Damage (ATK per basic hit) | 45.6 | |
| Defence | 27.1 | 21.3% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 45.6 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.867 | Role target 0.867 ([[Animal Stat Budget Model]]) |

**Wild version in Frostfang Tundra** (region multiplier ×4.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 4,874, ATK 153.9, DEF 27.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Frostfang Tundra (×4.5) | 428 | 360 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Tail Slap | Auto | 9 s | Slaps for 150% ATK and stuns for 0.8 s. |
| Tidal Breach | Manual | 18 s | A wave along a 20-stud line: 200% ATK, a 1.2 s knock-up and a 30% slow. |
| Pod Tactics | Passive (always on) | — | Enemies under crowd control take +15% damage from the team. |

**Ability activation type:** Tail Slap is **auto**, Tidal Breach is **manual**; Pod Tactics is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Orca are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 542 | 45.6 | 27.1 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 585 | 49.2 | 29.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 628 | 52.9 | 31.4 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 671 | 56.5 | 33.6 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 715 | 60.2 | 35.7 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 758 | 63.8 | 37.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A black-and-white pattern with an eye patch and a tall dorsal fin.

**Distinctive features:** High-contrast pattern readable at any distance.

| Colour | Use |
|---|---|
| `#111111` | Back |
| `#FFFFFF` | Belly and eye patch |
| `#CFD8DC` | Saddle |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-046 Orca (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 4,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-046 in the [[Asset Register]] |

## Animation requirements

Signature motion: Powerful air-swim, spy-hop idle, tail-slap spin.

Required clips: idle (2 variants), walk, run, basic attack, Tail Slap, Tidal Breach, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Tail Slap effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Tidal Breach effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Whistles and calls; slap crack; wave crash. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** The best team amplifier among Controllers.
- **Weaknesses:** Its own damage is modest.

## Balance notes

- Power Index 0.867 against a Controller target of 0.867 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Dolphin]] · [[Narwhal]] · [[Seal]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Frostfang Tundra]] · [[Animal Combat Behaviour]] · [[Ascension System]]
