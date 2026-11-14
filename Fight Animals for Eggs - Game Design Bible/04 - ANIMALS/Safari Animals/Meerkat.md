---
title: Meerkat
type: animal
name: Meerkat
species: Suricata suricatta
animal_id: ANM-010
rarity: Common
family: Safari Animals
role: Support
habitat: Sunscorch Savanna
pool_class: Scarce
ability_activation: Auto
status: proposed
priority: P0
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - common
  - safari-animals
  - support
  - sunscorch-savanna
---

# Meerkat

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Meerkat |
| Species | *Suricata suricatta* |
| Rarity | Common |
| Animal family | Safari Animals (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-010 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Neon (see [[Animal Variants]]) |
| Production priority | P0 |

## Identity

A vigilant sentry that spots threats for the whole team. Its marks make every hit count.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Common Egg]]. Chance inside the Common pool: 5.403% at P = 0.0, 6.122% at P = 0.3 (baseline), 7.613% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 3.980% per roll at baseline P = 0.3; 4.045% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Common Egg at the [[Egg Merging Station]], then hatch it. | Not applicable to Common. | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 20 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Neon versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

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

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 600, ATK 14.6, DEF 10.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Common) | 10 | 10 |
| Defeated in Sunscorch Savanna (×1.5) | 15 | 15 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Lookout | Auto | 15 s | Stands sentry and marks up to 3 enemies within 30 studs for 5 s; the team deals +12% damage to marked enemies. |

**Ability activation type:** Lookout is **auto**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Meerkat are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 200 | 13.0 | 10.0 | 100% | Base appearance |
| A1 | 1 | 1 | 100 | 216 | 14.0 | 10.8 | 105% | Coloured trim on collar/markings |
| A2 | 2 | 3 | 200 | 232 | 15.1 | 11.6 | 110% | Rarity-coloured eye glint |
| A3 | 3 | 6 | 300 | 248 | 16.1 | 12.4 | 115% | Soft rarity aura |
| A4 | 4 | 10 | 400 | 264 | 17.2 | 13.2 | 120% | Particle accents on movement |
| A5 | 5 | 15 | 500 | 280 | 18.2 | 14.0 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** An upright posture with the tail used as a tripod.

**Distinctive features:** Dark eye patches, slim body, quick head turns.

| Colour | Use |
|---|---|
| `#C9A66B` | Coat |
| `#4A3A2A` | Eye patches and tail tip |
| `#E9D8B4` | Belly |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-010 Meerkat (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Small quadruped (stands upright); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 1,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-010 in the [[Asset Register]] |

## Animation requirements

Signature motion: Scurry run, stand-up sentry pose (blend), head-scan idle.

Required clips: idle (2 variants), walk, run, basic attack, Lookout, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Lookout effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Common) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Chirp alarms; a rising whistle on Lookout. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team-wide damage amplification; long range.
- **Weaknesses:** Fragile and weak alone; marks are wasted on scattered fights.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Common animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Hyena]] · [[Zebra]] · [[Monkey]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Common Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
