---
title: Blue Whale
type: animal
name: Blue Whale
species: Balaenoptera musculus
animal_id: ANM-055
rarity: Mythical
family: Aquatic Animals
role: Support
habitat: Starfall Sanctuary
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - mythical
  - aquatic-animals
  - support
  - starfall-sanctuary
---

# Blue Whale

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Blue Whale |
| Species | *Balaenoptera musculus* |
| Rarity | Mythical |
| Animal family | Aquatic Animals (see [[Animal Families]]) |
| Combat role | Support (see [[Animal Roles]]) |
| Habitat | [[Region - Starfall Sanctuary]] |
| Asset ID | ANM-055 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

The largest animal ever to live, scaled to companion size. Its song heals and its currents carry the team.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Mythical Egg]]. Chance inside the Mythical pool: 12.06% at P = 0.0, 13.33% at P = 0.3 (baseline), 15.79% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0240% per roll at baseline P = 0.3; 0.0688% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Mythical Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Starfall Sanctuary]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 900 s window (25% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 740 | |
| Damage (ATK per basic hit) | 48.1 | |
| Defence | 37.0 | 27.0% damage reduction |
| Attack speed | 1.00 hits/s | DPS from basic attacks ≈ 48.1 |
| Movement speed | 16.0 studs/s | Player walk speed is 16 |
| Basic attack range | 18 studs | |
| Power Index | 0.806 | Role target 0.806 ([[Animal Stat Budget Model]]) |

**Wild version in Starfall Sanctuary** (region multiplier ×11.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 17,020, ATK 414.9, DEF 37.0.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Mythical) | 190 | 150 |
| Defeated in Starfall Sanctuary (×11.5) | 2,185 | 1,725 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Whale Song | Auto | 15 s | Heals the team for 14% of max HP and removes one debuff from each ally. |
| Deep Current | Manual | 22 s | Summons a current for 5 s: allies inside gain +30% move speed and heal 3% of max HP per second; enemies inside are slowed by 25%. |
| Ocean Lullaby | Passive (always on) | — | The team gains +10% max HP. |

**Ability activation type:** Whale Song is **auto**, Deep Current is **manual**; Ocean Lullaby is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Blue Whale are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 740 | 48.1 | 37.0 | 100% | Base appearance |
| A1 | 1 | 1 | 3,200 | 799 | 51.9 | 40.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 6,400 | 858 | 55.8 | 42.9 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 9,600 | 918 | 59.6 | 45.9 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 12,800 | 977 | 63.5 | 48.8 | 120% | Particle accents on movement |
| A5 | 2 | 6 | 16,000 | 1,036 | 67.3 | 51.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** A long, mottled blue-grey body with throat pleats.

**Distinctive features:** Companion scale capped at 2.0 times a Dolphin; a slow, graceful swim.

| Colour | Use |
|---|---|
| `#5D7FA3` | Body |
| `#A9C1D9` | Mottling |
| `#3E5A78` | Fins |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-055 Blue Whale (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Aquatic (air-swim, huge); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 6,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-055 in the [[Asset Register]] |

## Animation requirements

Signature motion: Very slow sinusoidal air-swim, blowhole spout idle, song (head-up, 24 frames).

Required clips: idle (2 variants), walk, run, basic attack, Whale Song, Deep Current, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Whale Song effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Deep Current effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Mythical) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Long, low whale song; spout hiss. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Team-wide healing and mobility.
- **Weaknesses:** Low damage.

## Balance notes

- Power Index 0.806 against a Support target of 0.806 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Mythical animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Dolphin]] · [[Giant Panda]] · [[World Boss - Abyssal Leviathan]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Mythical Egg]] · [[Region - Starfall Sanctuary]] · [[Animal Combat Behaviour]] · [[Ascension System]]
