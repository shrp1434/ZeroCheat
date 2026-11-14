---
title: Elephant
type: animal
name: Elephant
species: Loxodonta africana
animal_id: ANM-044
rarity: Legendary
family: Safari Animals
role: Tank
habitat: Sunscorch Savanna
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - legendary
  - safari-animals
  - tank
  - sunscorch-savanna
---

# Elephant

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Elephant |
| Species | *Loxodonta africana* |
| Rarity | Legendary |
| Animal family | Safari Animals (see [[Animal Families]]) |
| Combat role | Tank (see [[Animal Roles]]) |
| Habitat | [[Region - Sunscorch Savanna]] |
| Asset ID | ANM-044 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Rainbow (see [[Animal Variants]]) |
| Production priority | P1 |

## Identity

A living fortress. It sweeps enemies aside with its trunk and stuns entire groups with a trumpeting quake.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Legendary Egg]]. Chance inside the Legendary pool: 16.05% at P = 0.0, 15.38% at P = 0.3 (baseline), 14.03% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.1231% per roll at baseline P = 0.3; 0.2458% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Legendary Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Sunscorch Savanna]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 300 s (50% spawn chance per window). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Rainbow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 954 | |
| Damage (ATK per basic hit) | 39.9 | |
| Defence | 45.6 | 31.3% damage reduction |
| Attack speed | 0.78 hits/s | DPS from basic attacks ≈ 31.2 |
| Movement speed | 14.4 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.019 | Role target 1.022 ([[Animal Stat Budget Model]]) |

Species tweak applied: HP ×1.08, AS ×0.92.

**Wild version in Sunscorch Savanna** (region multiplier ×1.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 2,863, ATK 44.9, DEF 45.6.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Legendary) | 95 | 80 |
| Defeated in Sunscorch Savanna (×1.5) | 142 | 120 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Trunk Sweep | Auto | 10 s | Sweeps a 180-degree arc for 160% ATK and knocks enemies back. |
| Trumpet Quake | Manual | 20 s | Trumpets and stomps: 200% ATK within 14 studs, a 1.2 s stun and a 3 s taunt. |
| Thick Hide | Passive (always on) | — | Takes -15% damage from abilities. |

**Ability activation type:** Trunk Sweep is **auto**, Trumpet Quake is **manual**; Thick Hide is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Elephant are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 954 | 39.9 | 45.6 | 100% | Base appearance |
| A1 | 1 | 1 | 1,600 | 1,031 | 43.1 | 49.2 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 3,200 | 1,107 | 46.3 | 52.9 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 4,800 | 1,183 | 49.5 | 56.5 | 115% | Soft rarity aura |
| A4 | 2 | 5 | 6,400 | 1,260 | 52.7 | 60.2 | 120% | Particle accents on movement |
| A5 | 2 | 7 | 8,000 | 1,336 | 55.9 | 63.8 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Huge ears, tusks and a trunk.

**Distinctive features:** The trunk is a 5-bone chain; ears flap as a secondary motion.

| Colour | Use |
|---|---|
| `#8E8E93` | Skin |
| `#F1E9D2` | Tusks |
| `#6F6F75` | Wrinkle shading |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-044 Elephant (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (proboscidean); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 5,000 triangles (PROPOSED by rarity; +20% for the XL size class); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-044 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heavy walk, ear-flap idle, rear-and-stomp quake.

Required clips: idle (2 variants), walk, run, basic attack, Trunk Sweep, Trumpet Quake, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Trunk Sweep effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Trumpet Quake effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Legendary) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Trumpet blast; low rumble vocal; ground thud. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** The most durable companion; area stun and taunt.
- **Weaknesses:** Slow attack speed; little single-target damage.

## Balance notes

- Power Index 1.019 against a Tank target of 1.022 (difference -0.003; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Legendary animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Woolly Mammoth]] · [[Rhino]] · [[World Boss - Thunderhoof]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Legendary Egg]] · [[Region - Sunscorch Savanna]] · [[Animal Combat Behaviour]] · [[Ascension System]]
