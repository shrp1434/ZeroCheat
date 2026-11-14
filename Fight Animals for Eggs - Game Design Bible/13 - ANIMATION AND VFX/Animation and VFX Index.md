---
title: Animation and VFX Index
type: index
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - index
  - animation
  - vfx
---

# Animation and VFX Index

Everything that moves or glows in *Fight Animals for Eggs*: rig standards, animation sets, camera rules and visual effects. Start with the [[Animation Bible]] (timing language, priorities, LOD, honesty rules for reward reveals) and [[Animal Rig Standards]] (the seven rig classes every animal belongs to), then go to the set you are producing.

> [!info] Status
> Contents are **PROPOSED** unless they restate a **CONFIRMED** owner decision from the [[Decision Register]]. Gameplay numbers come from [[Canonical Proposed Values]]; this folder adds presentation values only.

## Foundations

| Document | What it covers |
|---|---|
| [[Animation Bible]] | Style pillars, 30/60 fps conventions, timing phases, playback authority, transitions, LOD and mobile budgets, reward-reveal honesty, ANI ID allocation |
| [[Animal Rig Standards]] | Motor6D rigs per body plan, joint and attachment names, roster-to-rig mapping, animation priorities, keyframe markers |
| [[Camera Behaviour Guidelines]] | Gameplay camera, shake and FOV-punch profiles, cinematic modes and when the camera may never be taken |

## Animation sets (`Animation/`)

| Document | What it covers |
|---|---|
| [[Animation - Animal Locomotion]] | Idle, walk, run, jump, flight, slither and air-swim sets for all seven rig classes (ANI-001–099) |
| [[Animation - Animal Attacks and Hit Reactions]] | Role timing templates, 29 basic attack clips, flinch, stagger, knockback and stun (ANI-100–179) |
| [[Animation - Animal Defeat and Victory]] | Wild defeat, the knock-out pose that marks raid defenders as stealable, recovery, victory and showcase (ANI-180–219) |
| [[Animation - Player Attacks and Specials]] | Three-hit combo, Power Strike, Ground Slam, Rally Cry, Dodge Roll, player reactions (ANI-220–259) |
| [[Animation - Animal Abilities]] | Eighteen ability archetypes, manual versus automatic presentation (ANI-260–319) |
| [[Animation - Boss Attacks]] | Telegraph minimums, boss templates, intro, phases and defeat (ANI-320–399) |
| [[Animation - Egg Roll]] | Seven rarity reveal sequences (1.6–7.0 s), ×5 roll, skip and refusal (ANI-400–419) |
| [[Animation - Egg Hatch]] | Single 3.5 s hatch and 5.0 s multi-hatch with the five-egg layout (ANI-420–439) |
| [[Animation - Ascension]] | A1–A5 ceremonies with duplicates becoming light (ANI-440–459) |
| [[Animation - Egg Merge]] | 3 → 1 merges by tier and station level, station idles and transformations (ANI-460–479) |
| [[Animation - Base Upgrades]] | Module construction and upgrades L1–L5, module idles, turrets, barricades, traps (ANI-480–499) |
| [[Animation - Shield Activation]] | Generator spin-up, dome raise, idle, ripple, expiry warning, collapse, break (ANI-500–519) |
| [[Animation - Raid Interactions]] | Alarm, steal channels, egg and animal capture, carry, drop, return, secure (ANI-520–549) |

## Visual effects (`VFX/`)

| Document | What it covers |
|---|---|
| [[VFX Bible]] | Style, colour language, low/medium/high quality tiers with emitter rate caps, Beam/Trail/Highlight/light budgets, photosensitivity, system effects register (VFX-300–399) |
| [[VFX - Combat Effects]] | Hits, specials, projectiles, ability effects, status, KO and telegraphs (VFX-001–099) |
| [[VFX - Rarity and Variant Effects]] | Per-rarity escalation for eggs, reveals and companions; ascension tiers; variants (VFX-100–199) |
| [[VFX - Environment Ambient Effects]] | Hub and region ambience, weather, spawns, gates, hazards (VFX-200–299) |

## Key cross-cutting rules

1. Server decides, client dramatises: animations never imply a result different from the server's ([[Animation Bible]] §6).
2. The knock-out pose (lying on the side) is exclusive to KO, because it marks raid defenders as stealable ([[Animation - Animal Defeat and Victory]]).
3. Boss telegraphs are at least 0.8 s and their decals match the true hit area ([[Animation - Boss Attacks]]).
4. Low, medium and high quality tiers are shared by animation LOD and VFX budgets ([[VFX Bible]]).

## Related documents
- [[Art Direction Index]]
- [[Sound Design Index]]
- [[Asset Register]]
- [[Template - Animation]]
- [[Template - VFX]]
- [[Performance Guidelines]]
