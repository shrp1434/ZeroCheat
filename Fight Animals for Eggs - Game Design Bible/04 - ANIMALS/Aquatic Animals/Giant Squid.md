---
title: Giant Squid
type: animal
name: Giant Squid
species: Architeuthis dux
animal_id: ANM-056
rarity: Mythical
family: Aquatic Animals
role: Controller
habitat: Starfall Sanctuary
pool_class: Elusive
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - mythical
  - aquatic-animals
  - controller
  - starfall-sanctuary
---

# Giant Squid

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Giant Squid |
| Species | *Architeuthis dux* |
| Rarity | Mythical |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Controller (see [[Animal Roles]]) |
| Habitat | [[Region - Starfall Sanctuary]] |
| Asset ID | ANM-056 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Neon, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

A deep-sea titan that smothers groups in darkness and binds several enemies at once. The rarest Mythical.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Mythical Egg]]. Chance inside the Mythical pool: 4.965% at P = 0.0, 6.667% at P = 0.3 (baseline), 9.942% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0120% per roll at baseline P = 0.3; 0.0433% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Mythical Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Starfall Sanctuary]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 900 s window (25% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 703 | |
| Damage (ATK per basic hit) | 59.2 | |
| Defence | 35.1 | 26.0% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 59.2 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 12 studs | |
| Power Index | 0.866 | Role target 0.866 ([[Animal Stat Budget Model]]) |

**Wild version in Starfall Sanctuary** (region multiplier ×11.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 16,169, ATK 510.6, DEF 35.1.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Mythical) | 190 | 150 |
| Defeated in Starfall Sanctuary (×11.5) | 2,185 | 1,725 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Ink Darkness | Auto | 12 s | An ink zone (radius 10, 4 s) silences enemies inside it. |
| Kraken Coil | Manual | 18 s | Binds up to 3 enemies within 12 studs for 2 s, dealing 120% ATK to each over the duration. |
| Abyssal Reach | Passive (always on) | — | Its crowd-control durations are increased by 20%. |

**Ability activation type:** Ink Darkness is **auto**, Kraken Coil is **manual**; Abyssal Reach is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Giant Squid are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 703 | 59.2 | 35.1 | 100% | Base appearance |
| A1 | 1 | 1 | 3,200 | 759 | 63.9 | 38.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 6,400 | 815 | 68.7 | 40.8 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 9,600 | 872 | 73.4 | 43.6 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 12,800 | 928 | 78.1 | 46.4 | 120% | Particle accents on movement |
| A5 | 2 | 6 | 16,000 | 984 | 82.9 | 49.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Long arms, two longer feeding tentacles and a huge eye.

**Distinctive features:** A bioluminescent rim (Neon material dots) along the mantle.

| Colour | Use |
|---|---|
| `#B23A48` | Skin |
| `#F4C7C3` | Suckers |
| `#F9E79F` | Eye |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-056 Giant Squid (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Cephalopod (air-swim, large); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 6,500 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-056 in the [[Asset Register]] |

## Animation requirements

Signature motion: Jet pulse air-swim, slow arm-curl idle, triple-coil grab.

Required clips: idle (2 variants), walk, run, basic attack, Ink Darkness, Kraken Coil, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Ink Darkness effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Kraken Coil effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Mythical) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep, gurgling pressure sounds; wet coil squeezes. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Multi-target control.
- **Weaknesses:** Low personal damage.

## Balance notes

- Power Index 0.866 against a Controller target of 0.866 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Mythical animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Octopus]] · [[Orca]] · [[Megalodon]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Mythical Egg]] · [[Region - Starfall Sanctuary]] · [[Animal Combat Behaviour]] · [[Ascension System]]
