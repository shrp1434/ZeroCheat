---
title: Woodpecker
type: animal
name: Woodpecker
species: Dendrocopos major
animal_id: ANM-007
rarity: Common
family: Birds
role: Skirmisher
habitat: Whisperwood Forest
pool_class: Elusive
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - birds
  - skirmisher
  - whisperwood-forest
---

# Woodpecker

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Woodpecker |
| Species | *Dendrocopos major* |
| Rarity | Common |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Whisperwood Forest]] |
| Asset ID | ANM-007 |
| Hatch pool class | Elusive (weight 3) |
| Eligible variants | Golden, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A relentless drummer whose rapid pecks crack enemy armour. The hardest Common to hatch, and a favourite for players who like fast attack rhythms.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 2.225% at P = 0.0, 3.061% at P = 0.3 (baseline), 4.793% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 1.990% per roll at baseline P = 0.3; 2.547% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Whisperwood Forest]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 170 | |
| Damage (ATK per basic hit) | 14.7 | |
| Defence | 8.0 | 7.4% damage reduction |
| Attack speed | 1.71 hits/s | DPS from basic attacks ≈ 25.1 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.023 | Role target 1.017 ([[Animal Stat Budget Model]]) |

Species tweak applied: AS ×1.10, ATK ×0.92.

**Wild version in Whisperwood Forest** (region multiplier ×1.0; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 340, ATK 11.0, DEF 8.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Whisperwood Forest (×1.0) | 10 | 10 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Drill Peck | Auto | 9 s | Rapid five-peck combo on its target, each peck 45% ATK; the final peck reduces target DEF by 15% for 4 s. |

**Ability activation type:** Drill Peck is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Woodpecker are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 170 | 14.7 | 8.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 184 | 15.9 | 8.6 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 197 | 17.1 | 9.3 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 211 | 18.3 | 9.9 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 224 | 19.4 | 10.6 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 238 | 20.6 | 11.2 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A chisel beak and a red crown patch over a pied black-and-white body.

**Distinctive features:** Stiff tail used as a prop; clings vertically when idle near trees.

| Colour | Use |
|---|---|
| `#1E1E1E` | Back and wings |
| `#FFFFFF` | Wing bars and face |
| `#D7263D` | Crown and vent |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-007 Woodpecker (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (ground and flight); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-007 in the [[Asset Register]] |

## Animation requirements

Signature motion: Hop-step ground move, short flutter flight, head-blur drill (each peck 3 frames).

Required clips: idle (2 variants), walk, run, basic attack, Drill Peck, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Drill Peck effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Machine-gun drumming 'tok-tok-tok'; sharp 'kik' call. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Shreds armour for the whole team; very high attack speed.
- **Weaknesses:** Low health; melee range despite being a bird.

## Balance notes

- Power Index 1.023 against a Skirmisher target of 1.017 (difference +0.006; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Golden Eagle]] · [[Toucan]] · [[Squirrel]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Whisperwood Forest]] · [[Animal Combat Behaviour]] · [[Ascension System]]
