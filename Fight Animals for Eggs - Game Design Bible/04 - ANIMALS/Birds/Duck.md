---
title: Duck
type: animal
name: Duck
species: Anas platyrhynchos
animal_id: ANM-006
rarity: Common
family: Birds
role: Support
habitat: Whisperwood Forest
pool_class: Standard
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - birds
  - support
  - whisperwood-forest
---

# Duck

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Duck |
| Species | *Anas platyrhynchos* |
| Rarity | Common |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-006 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Rainbow (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A cheerful healer that splashes allies back to health. The first Support most players own and a reminder that healing wins long fights.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 10.59% at P = 0.0, 10.20% at P = 0.3 (baseline), 9.398% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 6.633% per roll at baseline P = 0.3; 4.994% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 200 | |
| Damage (ATK per basic hit) | 13.0 | |
| Defence | 10.0 | 9.1% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 13.0 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 400, ATK 9.8, DEF 10.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Puddle Splash | Auto | 12 s | Splashes water around itself, healing all allies within 10 studs for 8% of their max HP. |

**Ability activation type:** Puddle Splash is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Duck are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 200 | 13.0 | 10.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 216 | 14.0 | 10.8 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 232 | 15.1 | 11.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 248 | 16.1 | 12.4 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 264 | 17.2 | 13.2 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 280 | 18.2 | 14.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A rounded body with a flat bill; the green mallard head is the identity colour.

**Distinctive features:** White neck ring, curled tail feather, waddle walk.

| Colour | Use |
|---|---|
| `#2F7D4F` | Head |
| `#C8B89A` | Body |
| `#F29B30` | Bill and feet |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-006 Duck (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (ground and short flight); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-006 in the [[Asset Register]] |

## Animation requirements

Signature motion: Waddle walk, flap-hop over obstacles, tail-wag idle, splash stomp cast.

Required clips: idle (2 variants), walk, run, basic attack, Puddle Splash, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Puddle Splash effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Quack (three variants); water splash on cast; wing flutter. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area heal suits clumped teams; low upkeep.
- **Weaknesses:** Very low damage; heal radius forces the team to stay close.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Flamingo]] · [[Penguin]] · [[Frog]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
