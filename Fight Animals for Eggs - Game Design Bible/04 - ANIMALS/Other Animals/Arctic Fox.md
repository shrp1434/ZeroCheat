---
title: Arctic Fox
type: animal
name: Arctic Fox
species: Vulpes lagopus
animal_id: ANM-033
rarity: Rare
family: Other Animals
role: Controller
habitat: Frostfang Tundra
pool_class: Elusive
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - rare
  - other-animals
  - controller
  - frostfang-tundra
---

# Arctic Fox

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Arctic Fox |
| Species | *Vulpes lagopus* |
| Rarity | Rare |
| Animal family | Other Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Frostfang Tundra]] |
| Asset ID | ANM-033 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A snow-white trickster whose bites chill enemies to a standstill. The rarest Rare.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Rare Egg]]. Chance inside the Rare pool: 2.552% at P = 0.0, 3.529% at P = 0.3 (baseline), 5.586% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.3176% per roll at baseline P = 0.3; 0.7562% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Rare Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Frostfang Tundra]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 60 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 323 | |
| Damage (ATK per basic hit) | 27.2 | |
| Defence | 16.1 | 13.9% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 27.2 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.869 | Role target 0.869 ([[Animal Stat Budget Model]]) |

**Wild version in Frostfang Tundra** (region multiplier ×4.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,907, ATK 91.8, DEF 16.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Rare) | 28 | 25 |
| Defeated in Frostfang Tundra (×4.5) | 126 | 112 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Frost Nip | Auto | 6 s | Its bite applies Chill (-25% move speed, 3 s); 3 Chill stacks freeze the target for 1 s. |
| Snow Veil | Manual | 20 s | Creates a snow flurry (radius 10, 5 s): enemy auto-targeting prefers units outside it, and ranged damage against allies inside is reduced by 30%. |

**Ability activation type:** Frost Nip is **auto**, Snow Veil is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Arctic Fox are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 323 | 27.2 | 16.1 | 100% | Base appearance |
| A1 | 1 | 1 | 400 | 349 | 29.4 | 17.4 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 800 | 375 | 31.6 | 18.7 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 1,200 | 401 | 33.7 | 20.0 | 115% | Soft rarity aura |
| A4 | 3 | 7 | 1,600 | 426 | 35.9 | 21.3 | 120% | Particle accents on movement |
| A5 | 3 | 10 | 2,000 | 452 | 38.1 | 22.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A small round-eared fox in a thick white coat.

**Distinctive features:** Fluffy tail wrapped around the body when idle.

| Colour | Use |
|---|---|
| `#F4F7FA` | Coat |
| `#BFD7EA` | Shading |
| `#2A2A2A` | Nose and eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-033 Arctic Fox (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (canid); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 2,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-033 in the [[Asset Register]] |

## Animation requirements

Signature motion: Light trot, mousing hop idle, snow-swirl cast.

Required clips: idle (2 variants), walk, run, basic attack, Frost Nip, Snow Veil, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Frost Nip effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Snow Veil effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Rare) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

High yips; crunching snow; wind gust on Snow Veil. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Freeze combos; protects allies against ranged damage.
- **Weaknesses:** Low damage; the freeze needs three hits.

## Balance notes

- Power Index 0.869 against a Controller target of 0.869 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Rare animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Fox]] · [[Snow Leopard]] · [[Wolf]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Rare Egg]] · [[Region - Frostfang Tundra]] · [[Animal Combat Behaviour]] · [[Ascension System]]
