---
title: Sabre-Tooth Tiger
type: animal
name: Sabre-Tooth Tiger
species: Smilodon fatalis
animal_id: ANM-051
rarity: Mythical
family: Big Cats
role: Assassin
habitat: Emberheart Caldera
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P2
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - mythical
  - big-cats
  - assassin
  - emberheart-caldera
---

# Sabre-Tooth Tiger

> [!info] PROPOSED
> Everything on this page is a **PROPOSED** design for the launch roster ([[Decision Register|D-032]]). The final catalogue and statistics are **UNDECIDED** ([[Open Questions#Q-002]], [[Open Questions#Q-003]]). All numbers are derived from [[Canonical Proposed Values]] by the [[Animal Stat Budget Model]].

| Field | Value |
|---|---|
| Name | Sabre-Tooth Tiger |
| Species | *Smilodon fatalis* |
| Rarity | Mythical |
| Animal family | Big Cats (see [[Animal Families]]) |
| Combat role | Assassin (see [[Animal Roles]]) |
| Habitat | [[Region - Emberheart Caldera]] |
| Asset ID | ANM-051 |
| Hatch pool class | Standard (weight 10) |
| Eligible variants | Golden, Diamond, Shadow (see [[Animal Variants]]) |
| Production priority | P2 |

## Identity

An Ice Age predator returned from an ancient egg. It pierces armour and reappears behind the toughest enemy.

## Acquisition method

| Route | Details | Status |
|---|---|---|
| Hatching | Hatched from a [[Mythical Egg]]. Chance inside the Mythical pool: 23.64% at P = 0.0, 22.22% at P = 0.3 (baseline), 19.49% at P = 1.0 ([[Hatch Pool Tables]]). | **CONFIRMED** mechanism, **PROPOSED** odds |
| Per egg roll (combined) | 0.0400% per roll at baseline P = 0.3; 0.0849% per roll at P = 1.0 (egg rarity × pool share, before merging). | **PROPOSED** |
| Merging route | Merge three lower-rarity eggs into a Mythical Egg at the [[Egg Merging Station]], then hatch it. | | **CONFIRMED** mechanism |
| Wild encounter | Fought (not captured) in [[Region - Emberheart Caldera]]. A defeat registers it in the player's index ([[Animal Index Feature Specification]]). Respawn: 900 s window (25% rare-spawn chance, server announcement). | **CONFIRMED** (index), **PROPOSED** (timers) |
| Raid theft | Can be stolen from another player's base only after being knocked out while defending ([[Animal Theft Rules]]). | **CONFIRMED** rule |
| Variants | Acquisition of Golden, Diamond, Shadow versions is **UNDECIDED** ([[Open Questions#Q-006]]). | **UNDECIDED** |

## Combat statistics

Companion statistics at ascension 0, with no base bonuses applied:

| Stat | Value | Notes |
|---|---:|---|
| Health | 555 | |
| Damage (ATK per basic hit) | 107.3 | |
| Defence | 25.9 | 20.6% damage reduction |
| Attack speed | 1.05 hits/s | DPS from basic attacks ≈ 112.7 |
| Movement speed | 19.2 studs/s | Player walk speed is 16 |
| Basic attack range | 5 studs | |
| Power Index | 1.024 | Role target 1.024 ([[Animal Stat Budget Model]]) |

**Wild version in Emberheart Caldera** (region multiplier ×8.5; wild HP ×2.0, wild ATK ×0.75; DEF is not region-scaled): HP 9,435, ATK 684.0, DEF 25.9.

## Cash reward

| Context | Cash | XP |
|---|---:|---:|
| Base value (Mythical) | 190 | 150 |
| Defeated in Emberheart Caldera (×8.5) | 1,615 | 1,275 |

Cash bonuses from the [[Module - Multiplier Shrine]] and the [[Module - Trophy Hall]] apply on top ([[Wild Animal Cash Rewards]]). All values are **PROPOSED**.

## Abilities

| Ability | Activation | Cooldown | Effect |
|---|---|---:|---|
| Sabre Pierce | Auto | 8 s | Stabs for 230% ATK and reduces the target's DEF by 25% for 5 s. |
| Ice Age Ambush | Manual | 16 s | Vanishes for 1 s (untargetable), reappears behind the highest-HP enemy and strikes for 320% ATK. |
| Ancient Predator | Passive (always on) | — | +20% damage against targets above 70% HP. |

**Ability activation type:** Sabre Pierce is **auto**, Ice Age Ambush is **manual**; Ancient Predator is passive. Automatic abilities fire as soon as their cooldown is ready and a valid target is in range. Manual abilities are triggered from the team bar ([[UI - Animal Team Display]]). Both activation types are **CONFIRMED** to exist ([[Decision Register|D-008]]). Cooldown rules are in [[Abilities and Cooldowns]].

## Ascension progression

Duplicates of the Sabre-Tooth Tiger are consumed; the original is kept ([[Ascension System]]). Values follow [[Ascension Progression Table]] (**PROPOSED**, [[Open Questions#Q-004]], [[Open Questions#Q-005]]).

| Level | Duplicates for this step | Cumulative | Cash fee | HP | ATK | DEF | Ability effectiveness | Visual |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| A0 | — | 0 | — | 555 | 107.3 | 25.9 | 100% | Base appearance |
| A1 | 1 | 1 | 3,200 | 599 | 115.9 | 28.0 | 105% | Coloured trim on collar/markings |
| A2 | 1 | 2 | 6,400 | 644 | 124.5 | 30.0 | 110% | Rarity-coloured eye glint |
| A3 | 1 | 3 | 9,600 | 688 | 133.1 | 32.1 | 115% | Soft rarity aura |
| A4 | 1 | 4 | 12,800 | 733 | 141.6 | 34.2 | 120% | Particle accents on movement |
| A5 | 2 | 6 | 16,000 | 777 | 150.2 | 36.3 | 125% | Crest emblem and full aura |

## Visual design

**Silhouette:** Long sabre canines, a bobbed tail and powerful forelimbs.

**Distinctive features:** The fangs extend below the jaw line; a stocky, muscular build.

| Colour | Use |
|---|---|
| `#C99A5B` | Coat |
| `#7A5530` | Markings |
| `#F6EFDC` | Fangs |

Rarity presentation (frame, aura, nameplate colour) follows [[Rarity Visual Language]]. Variant treatments follow [[Variant Visual Treatments]].

> [!example] VISUAL REFERENCE PLACEHOLDER
> Concept turnaround for ANM-051 Sabre-Tooth Tiger (front, side, back, three-quarter) plus a silhouette test sheet. No artwork exists yet ([[Visual Reference Placeholders]]).

## Model requirements

| Requirement | Specification |
|---|---|
| Body plan and rig | Large quadruped (felid, powerful forelimbs); see [[Animal Rig Standards]] |
| Triangle budget (LOD0) | ≤ 6,000 triangles (PROPOSED by rarity); LOD1 50%, LOD2 20% |
| Construction | Low-poly flat-shaded MeshParts; colour via vertex colour or palette texture; no photographic textures ([[Animal Modelling Principles]]) |
| Silhouette test | Must be identifiable as a black silhouette at 64 px |
| Materials | Base: SmoothPlastic look; rarity and variant layers are applied at runtime ([[Material and Texture Direction]]) |
| Asset register | ANM-051 in the [[Asset Register]] |

## Animation requirements

Signature motion: Heavy stalking gait, fang-bare idle, vanish blink and pierce lunge.

Required clips: idle (2 variants), walk, run, basic attack, Sabre Pierce, Ice Age Ambush, hit reaction (light and heavy), knocked-out (the stealable state in raids), revive, victory, and a hatch reveal pose. Specifications: [[Animation - Animal Locomotion]], [[Animation - Animal Attacks and Hit Reactions]], [[Animation - Animal Abilities]], [[Animation - Animal Defeat and Victory]].

## VFX requirements

| Effect | Trigger | Notes |
|---|---|---|
| Sabre Pierce effect | Ability fires automatically | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Ice Age Ambush effect | Player activates the ability | Telegraph plus impact; respects mobile quality tiers ([[VFX - Combat Effects]]) |
| Rarity aura (Mythical) | Always on while equipped | [[VFX - Rarity and Variant Effects]] |
| Ascension accents | A3 and above | [[Animation - Ascension]] |

## Sound requirements

Deep, rasping roar; bone-crunch stab. Vocal guidelines: [[Sound - Animal Vocalisations]]. Ability audio: [[Sound - Abilities]].

## Strengths and weaknesses

- **Strengths:** Opens fights against Tanks and bosses.
- **Weaknesses:** Weaker at finishing low-HP targets.

## Balance notes

- Power Index 1.024 against a Assassin target of 1.024 (difference +0.000; tolerance ±0.06).
- Ability multipliers are written as % of ATK, so ability power scales with rarity automatically. Ascension adds up to +40% to stats and +25% to ability effectiveness.
- Compare with other Mythical animals in [[Animal Statistics Database]]. Tuning follows [[Balancing Methodology]].

## Related animals

[[Tiger]] · [[Woolly Mammoth]] · [[Mini-Boss - Cinderjaw]]

## Related documents

[[Animal Index]] · [[Animal Abilities Catalogue]] · [[Mythical Egg]] · [[Region - Emberheart Caldera]] · [[Animal Combat Behaviour]] · [[Ascension System]]
