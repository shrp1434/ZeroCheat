---
title: Golden Eagle
type: animal
name: Golden Eagle
species: Aquila chrysaetos
animal_id: ANM-039
rarity: Epic
family: Birds
role: Skirmisher
habitat: Skyreach Peaks
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - birds
  - skirmisher
  - skyreach-peaks
---

# Golden Eagle

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Golden Eagle |
| Species | *Aquila chrysaetos* |
| Rarity | Epic |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Skyreach Peaks]] |
| Asset ID | ANM-039 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Diamond, Shadow, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A mountain raptor that dives from above and circles the battlefield picking off targets.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Epic Egg]]. Chance inside the Epic pool: 13.83% at P = 0.0, 13.33% at P = 0.3 (baseline), 12.30% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.4000% per roll at baseline P = 0.3; 0.6818% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Epic Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Skyreach Peaks]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 120 s. | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Diamond, Shadow, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 374 | |
| Damage (ATK per basic hit) | 35.2 | |
| Defence | 17.6 | 15.0% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 54.6 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.008 | Role target 1.008 ([[Animal Stat Budget Model]]) |

**Wild version in Skyreach Peaks** (region multiplier ×6.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 4,638, ATK 163.7, DEF 17.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Epic) | 50 | 45 |
| Defeated in Skyreach Peaks (×6.2) | 310 | 279 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Talon Strike | Auto | 7 s | Dives onto its target for 160% ATK. |
| Sky Circle | Manual | 16 s | Takes to the air for 4 s (melee cannot target it), striking a random enemy each second for 90% ATK. |

**Ability activation type:** Talon Strike is **auto**, Sky Circle is **manual**. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Golden Eagle are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 374 | 35.2 | 17.6 | 100% | Base appearance |
| A1 | 1 | 1 | 800 | 404 | 38.0 | 19.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 1,600 | 434 | 40.8 | 20.4 | 110% | Rarity-coloured eye glint |
| A3 | 2 | 4 | 2,400 | 464 | 43.6 | 21.8 | 115% | Soft rarity aura |
| A4 | 2 | 6 | 3,200 | 494 | 46.5 | 23.2 | 120% | Particle accents on movement |
| A5 | 3 | 9 | 4,000 | 524 | 49.3 | 24.6 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Broad wings (span 2.2 times body length) and a golden nape.

**Distinctive features:** Hooked beak; feathered legs.

| Colour | Use |
|---|---|
| `#5A3B1E` | Plumage |
| `#D9A441` | Nape |
| `#F2C14E` | Feet and cere |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-039 Golden Eagle (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (raptor, flight); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 3,500 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-039 in the [[Asset Register]] |

## Animation requirements

Signature motion: Ground hop, soaring flight cycle, stoop dive.

Required clips: idle (2 variants), walk, run, basic attack, Talon Strike, Sky Circle, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Talon Strike effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Sky Circle effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Epic) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

High whistled scream; wind rush on dives. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Evasive; reliable spread damage.
- **Weaknesses:** Damage is spread rather than focused.

## Balance notes

- Power Index 1.008 against a Skirmisher target of 1.008 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Epic animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Peregrine Falcon]] · [[Haast's Eagle]] · [[Owl]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Epic Egg]] · [[Region - Skyreach Peaks]] · [[Animal Combat Behaviour]] · [[Ascension System]]
