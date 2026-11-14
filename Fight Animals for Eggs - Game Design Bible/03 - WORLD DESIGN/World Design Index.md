---
title: World Design Index
type: index
category: world-design
status: mixed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - index
  - world
  - regions
  - bosses
---

# World Design Index

This folder defines the shared world (D-025): the hub, eight habitat regions, how regions unlock, how wild animals spawn, the hazards that make each region play differently, and the twelve bosses.

> [!warning] UNDECIDED (Q-001)
> The world layout is **not approved** ([[Open Questions#Q-001]]). Every region, adjacency, size and landmark here is part of a **PROPOSED** hybrid world (D-035 **PROPOSED**). Start with [[World Overview and Map]].

**Orientation:** read [[World Overview and Map]] for the big picture, [[Region Unlock Progression]] for pacing, and [[Wild Animal Spawning and Respawn]] before touching any spawn data. Each region document follows the same structure (theme, palette, sub-zones, animals, difficulty, bosses, exploration, gates, hazards, performance, asset IDs, test hooks). Boss documents share the rules in [[Boss Design Overview]].

## World systems

| Document | One-line description |
|---|---|
| [[World Overview and Map]] | The proposed hybrid ring world, adjacency diagram, footprints, shared-world rules and ENV-### allocation. |
| [[Hub - Hatchling Haven]] | The safe central hub: Egg Shrine, base portals, Waystone Ring, World Boss Board. |
| [[Region Unlock Progression]] | Gate requirements (level + boss), unlock flow, barrier behaviour and pacing estimates. |
| [[Wild Animal Spawning and Respawn]] | Spawn points, caps per region, respawn by rarity, rare-spawn events, LOD and leash; luck never affects wild rarity. |
| [[Environmental Hazards]] | Global hazard rules and the HZ-01 to HZ-20 catalogue. |

## Regions

| # | Document | Multiplier | One-line description |
|---:|---|---:|---|
| 1 | [[Region - Whisperwood Forest]] | ×1.0 | Starter woodland with 16 home species and the Grandfather Oak. |
| 2 | [[Region - Sunscorch Savanna]] | ×1.5 | Open grassland, first Epic and Legendary wild animals, Thunderhoof's storm. |
| 3 | [[Region - Emerald Canopy]] | ×2.2 | Three-layer vertical jungle with four Epic points. |
| 4 | [[Region - Coral Coast]] | ×3.2 | Beaches, tide flats and reef; the tide moves on a timer. |
| 5 | [[Region - Frostfang Tundra]] | ×4.5 | Arctic steppe and sea ice; first Mythical rare spawn. |
| 6 | [[Region - Skyreach Peaks]] | ×6.2 | Vertical mountain climb; the birds' region. |
| 7 | [[Region - Emberheart Caldera]] | ×8.5 | Volcanic lost valley; two Secret rare spawns. |
| 8 | [[Region - Starfall Sanctuary]] | ×11.5 | Celestial endgame archipelago; five rare-spawn species. |

## Bosses

| Document | One-line description |
|---|---|
| [[Boss Design Overview]] | Roster, stat formula, scaling, credit, telegraph standard, phase framework, reward options. |
| [[Mini-Boss - Bramblehorn]] | Bramble-antlered stag; first boss; bait charges into stumps. |
| [[Mini-Boss - Dustmane]] | Elder lion; Dust Shake forces manual target commands. |
| [[Mini-Boss - Vinecoil]] | Vine-wrapped python; grabs and rescues. |
| [[Mini-Boss - Hammertide]] | Hammerhead shark; jetties and surge timing. |
| [[Mini-Boss - Rimeback]] | Ice-armoured polar bear; focus-fire rime plates. |
| [[Mini-Boss - Stormtalon]] | Storm eagle; perch and hover cycle, edge awareness. |
| [[Mini-Boss - Cinderjaw]] | Ember crocodile; sinking islands in a lava lake. |
| [[Mini-Boss - Eclipse Panther]] | Celestial panther; three phases, clones and total eclipse. |
| [[World Boss - Ironbark Colossus]] | Forest-shelled tortoise; first world boss, weak-point knots. |
| [[World Boss - Thunderhoof]] | Storm elephant; chain lightning and totems. |
| [[World Boss - Abyssal Leviathan]] | Giant whale; platform fight with rest windows and flooding. |
| [[World Boss - Ashwing Condor]] | Ember condor; thermals carry players to its perches. |

## Open questions raised here

Q-107 (party access to locked regions), pending entry in [[Open Questions]]. Existing questions most relevant to this folder: [[Open Questions#Q-001]], [[Open Questions#Q-014]], [[Open Questions#Q-015]], [[Open Questions#Q-028]], [[Open Questions#Q-031]].

## Where to go next
- [[Game Vision Index]] · [[Core Gameplay Index]] · [[Environment Art Direction]] · [[M16 - World Design]] · [[M17 - Boss Encounters]]
