---
title: Great White Shark
type: animal
name: Great White Shark
species: Carcharodon carcharias
animal_id: ANM-045
rarity: Legendary
family: Aquatic Animals
role: Assassin
habitat: Coral Coast
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
  - assassin
  - coral-coast
---

# Great White Shark

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Great White Shark |
| Species | *Carcharodon carcharias* |
| Rarity | Legendary |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Coral Coast]] |
| Asset ID | ANM-045 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow, Neon (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

The ocean's perfect predator. It frenzies on wounded targets and erupts from below without warning.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 16.05% at P = 0.0, 15.38% at P = 0.3 (baseline), 14.03% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1231% per roll at baseline P = 0.3; 0.2458% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Coral Coast]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 428 | |
| Damage (ATK per basic hit) | 82.6 | |
| Defence | 19.9 | 16.6% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 86.8 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.032 | Role target 1.032 ([[Animal Stat Budget Model]]) |

**Wild version in Coral Coast** (region multiplier ×3.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,736, ATK 198.4, DEF 19.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Coral Coast (×3.2) | 304 | 256 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Frenzy Bite | Auto | 7 s | Bites for 200% ATK and heals for 25% of the damage dealt. |
| Breach | Manual | 15 s | Dives and erupts under its target: 280% ATK and a 1 s knock-up. |
| Blood in the Water | Passive (always on) | — | +30% damage against targets below 50% HP. |

**Ability activation type:** Frenzy Bite is **auto**, Breach is **manual**; Blood in the Water is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Great White Shark are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 428 | 82.6 | 19.9 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 462 | 89.3 | 21.5 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 496 | 95.9 | 23.1 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 530 | 102.5 | 24.7 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 564 | 109.1 | 26.3 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 598 | 115.7 | 27.9 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A torpedo body with a triangular dorsal fin and a sharp countershading line.

**Distinctive features:** Rows of teeth as one mesh; gill slits as decals.

| Colour | Use |
|---|---|
| `#7A8B99` | Back |
| `#F2F2F2` | Belly |
| `#2A2A2A` | Eyes |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-045 Great White Shark (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-045 in the [[Asset Register]] |

## Animation requirements

Signature motion: Side-to-side tail air-swim, slow circling idle, breach eruption.

Required clips: idle (2 variants), walk, run, basic attack, Frenzy Bite, Breach, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Frenzy Bite effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Breach effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Low bass rumble rather than a voice; jaw crunch; water surge. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Self-sustaining burst; brutal finisher.
- **Weaknesses:** Fragile when focused early.

## Balance notes

- Power Index 1.032 against a Assassin target of 1.032 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Megalodon]] · [[Mosasaurus]] · [[Mini-Boss - Hammertide]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Coral Coast]] · [[Animal Combat Behaviour]] · [[Ascension System]]
