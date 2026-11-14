---
title: "Haast's Eagle"
type: animal
name: "Haast's Eagle"
species: Hieraaetus moorei
animal_id: ANM-054
rarity: Mythical
family: Birds
role: Skirmisher
habitat: Skyreach Peaks
pool_class: Scarce
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - mythical
  - birds
  - skirmisher
  - skyreach-peaks
---

# Haast's Eagle

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Haast's Eagle |
| Species | *Hieraaetus moorei* |
| Rarity | Mythical |
| Animal family | Birds (see [[Animal Families]]) |
| Combat role | Skirmisher (see [[Animal Roles]]) |
| Habitat | [[Region - Skyreach Peaks]] |
| Asset ID | ANM-054 |
| Hatch pool class | Scarce (weight 6) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

The largest eagle ever recorded. Its enormous talons crush targets and splash damage across a whole group.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Mythical Egg]]. Chance inside the Mythical pool: 12.06% at P = 0.0, 13.33% at P = 0.3 (baseline), 15.79% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0240% per roll at baseline P = 0.3; 0.0688% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Mythical Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Skyreach Peaks]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 900 s window (25% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 629 | |
| Damage (ATK per basic hit) | 59.2 | |
| Defence | 29.6 | 22.8% damage reduction |
| Attack speed | 1.55 hits/s | DPS from basic attacks ≈ 91.8 |
| Movement speed | 20.8 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 0.999 | Role target 0.999 ([[Animal Stat Budget Model]]) |

**Wild version in Skyreach Peaks** (region multiplier ×6.2; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 7,800, ATK 275.3, DEF 29.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Mythical) | 190 | 150 |
| Defeated in Skyreach Peaks (×6.2) | 1,178 | 930 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Crushing Talons | Auto | 8 s | Strikes for 200% ATK and stuns for 0.6 s. |
| Moa Hunter Dive | Manual | 16 s | Dives from height: 320% ATK to its target and 50% splash damage within 8 studs. |
| Giant Wingspan | Passive (always on) | — | Its attacks also hit one extra enemy within 6 studs for 40% damage. |

**Ability activation type:** Crushing Talons is **auto**, Moa Hunter Dive is **manual**; Giant Wingspan is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Haast's Eagle are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 629 | 59.2 | 29.6 | 100% | Base appearance |
| A1 | 1 | 1 | 3,200 | 679 | 63.9 | 32.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 6,400 | 730 | 68.7 | 34.3 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 9,600 | 780 | 73.4 | 36.7 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 12,800 | 830 | 78.1 | 39.1 | 120% | Particle accents on movement |
| A5 | 2 | 6 | 16,000 | 881 | 82.9 | 41.4 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Huge talons, broad wings and dark plumage with a pale head band.

**Distinctive features:** A wingspan 2.6 times body length; a heavy hooked beak.

| Colour | Use |
|---|---|
| `#3B2B22` | Plumage |
| `#C7B39A` | Head band |
| `#F2C14E` | Talons |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-054 Haast's Eagle (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Bird (raptor, flight, large); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 6,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-054 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heavy flapping, ledge-perch idle, steep dive.

Required clips: idle (2 variants), walk, run, basic attack, Crushing Talons, Moa Hunter Dive, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Crushing Talons effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Moa Hunter Dive effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Mythical) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep, raw scream; massive wing beats. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Area burst; stuns.
- **Weaknesses:** Long cooldowns.

## Balance notes

- Power Index 0.999 against a Skirmisher target of 0.999 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Mythical animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Golden Eagle]] · [[Peregrine Falcon]] · [[Mini-Boss - Stormtalon]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Mythical Egg]] · [[Region - Skyreach Peaks]] · [[Animal Combat Behaviour]] · [[Ascension System]]
