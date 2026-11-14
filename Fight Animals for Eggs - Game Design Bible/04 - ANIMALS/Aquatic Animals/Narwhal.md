---
title: Narwhal
type: animal
name: Narwhal
species: Monodon monoceros
animal_id: ANM-047
rarity: Legendary
family: Aquatic Animals
role: Ranged
habitat: Frostfang Tundra
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - aquatic-animals
  - ranged
  - frostfang-tundra
---

# Narwhal

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Narwhal |
| Species | *Monodon monoceros* |
| Rarity | Legendary |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Ranged (see [[Animal Roles]]) |
| Habitat | [[Region - Frostfang Tundra]] |
| Asset ID | ANM-047 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The unicorn of the sea. It launches piercing ice javelins along its spiral tusk's line of sight.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 8.186% at P = 0.0, 9.231% at P = 0.3 (baseline), 11.36% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0738% per roll at baseline P = 0.3; 0.1991% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Frostfang Tundra]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 428 | |
| Damage (ATK per basic hit) | 65.5 | |
| Defence | 19.9 | 16.6% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 65.5 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 32 studs | |
| Power Index | 0.897 | Role target 0.897 ([[Animal Stat Budget Model]]) |

**Wild version in Frostfang Tundra** (region multiplier ×4.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 3,848, ATK 221.2, DEF 19.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Frostfang Tundra (×4.5) | 428 | 360 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Tusk Javelin | Auto | 8 s | Throws an ice javelin along a 32-stud piercing line: 220% ATK. |
| Frost Lance Barrage | Manual | 18 s | Fires 5 ice lances over 2 s, each 90% ATK, applying Chill. |
| Spiral Tusk | Passive (always on) | — | Basic attacks pierce, hitting up to 2 enemies in a line. |

**Ability activation type:** Tusk Javelin is **auto**, Frost Lance Barrage is **manual**; Spiral Tusk is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Narwhal are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 428 | 65.5 | 19.9 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 462 | 70.8 | 21.5 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 496 | 76.0 | 23.1 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 530 | 81.3 | 24.7 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 564 | 86.5 | 26.3 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 598 | 91.8 | 27.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A long spiral tusk on a mottled grey body.

**Distinctive features:** The tusk carries a faint frost Trail when attacking.

| Colour | Use |
|---|---|
| `#9AA7B1` | Body |
| `#5B6670` | Mottling |
| `#F5F0E1` | Tusk |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-047 Narwhal (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 4,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-047 in the [[Asset Register]] |

## Animation requirements

Signature motion: Gentle air-swim, tusk-raise aim, recoil throw.

Required clips: idle (2 variants), walk, run, basic attack, Tusk Javelin, Frost Lance Barrage, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Tusk Javelin effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Frost Lance Barrage effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Crystalline ice whoosh; clicks; shattering impacts. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Longest range companion; line damage; Chill combos.
- **Weaknesses:** Fragile; lines need lined-up enemies.

## Balance notes

- Power Index 0.897 against a Ranged target of 0.897 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Orca]] · [[Snow Leopard]] · [[Arctic Fox]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Frostfang Tundra]] · [[Animal Combat Behaviour]] · [[Ascension System]]
