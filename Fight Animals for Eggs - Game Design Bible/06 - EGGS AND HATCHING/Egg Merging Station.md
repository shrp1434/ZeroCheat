---
title: Egg Merging Station
type: feature
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - eggs
  - merging
  - base
  - base-module
  - art
---

# Egg Merging Station

The Egg Merging Station is the base structure where players perform [[Egg Merging]]. It is bought, then upgraded through five levels. Each level unlocks a higher merge tier and **physically transforms** the structure, so a visitor can read a player's merging progress at a glance.

> [!success] CONFIRMED (D-020)
> Merging requires a purchased Egg Merging Station. It must be upgraded before it can merge higher rarities, and its appearance changes with every upgrade.

> [!info] PROPOSED (D-038)
> Five levels, names, costs, gates, fees, footprints and visual designs on this page. Final costs **UNDECIDED** ([[Open Questions#Q-019]]).

## 1. Levels, costs and gates

| Level | Name | Cost (Cash) | Extra gate | Merges unlocked | Merge fee (Cash) | Merge animation |
|---:|---|---:|---|---|---|---|
| 1 | Twig Nest Press | 2,500 | — | Common → Uncommon; Uncommon → Rare | 100; 300 | 2.5 s; 3.0 s |
| 2 | Stonebound Hatchery Forge | 15,000 | Region 2 unlocked | Rare → Epic | 900 | 3.5 s |
| 3 | Crystal Incubator | 60,000 | Region 4 unlocked | Epic → Legendary | 2,700 | 4.25 s |
| 4 | Aurora Crucible | 250,000 | Region 6 unlocked + 1 world boss defeated | Legendary → Mythical | 8,000 | 5.0 s |
| 5 | Celestial Convergence Altar | 1,000,000 | Region 8 unlocked | Mythical → Secret | 25,000 | 6.0 s |

Costs, gates and fees are canonical **PROPOSED** values. The per-tier animation lengths within the canonical 2.5–6 s range are **PROPOSED** here. Each level keeps all merges unlocked at lower levels. The station counts **5** module levels towards the PS base input ([[Progression Score Specification]]).

Gate references: [[Region - Sunscorch Savanna]] (Region 2), [[Region - Coral Coast]] (Region 4), [[Region - Skyreach Peaks]] (Region 6), [[Region - Starfall Sanctuary]] (Region 8); world bosses in [[Boss Design Overview]].

**Cost in play time (PROPOSED model from [[Ascension Expected Value Analysis#Cash-per-hour model]]).** Level 2 ≈ 1.5 h at intermediate income (9,821 Cash/h); level 4 ≈ 7.6 h at advanced income (33,034 Cash/h); level 5 ≈ 15 h at endgame income (67,068 Cash/h).

## 2. Physical appearance by level

All levels share one anchor point on the base plot and grow outward and upward. Footprints must fit the station slot defined in [[Base Layout and Plot Expansion]]; the footprints below are **PROPOSED** and must be validated against it. Visual language follows [[Base Art Direction]] and [[Rarity Visual Language]]: each level adopts the colour of the highest rarity it can *produce*.

| Level | Footprint × height (studs) | Silhouette | Materials (Enum.Material) | Emissive elements | Moving parts | Asset ID (PROPOSED) |
|---:|---|---|---|---|---|---|
| 1 Twig Nest Press | 6 × 6 × 5 | A woven twig nest on a tree stump with a wooden lever press above it | Wood, WoodPlanks, Fabric (hessian padding), Grass (moss tufts) | One small hanging lantern, Neon `#FFD27A` | Lever rocks down on merge; nest bobs gently on idle (2 s cycle) | MOD-08-L1 |
| 2 Stonebound Hatchery Forge | 10 × 10 × 8 | A round stone forge with a chimney and a basin, the nest now cradled in iron bands | Cobblestone, Slate, Metal (bands), CrackedLava (coal bed) | Glowing coal bed `#FF7A1A`, chimney ember particles; Uncommon-green and Rare-blue rune stones `#4CC26A` / `#3D8BFF` | Bellows pump; stone grinding wheel rotates 6 rpm idle, 30 rpm during merge | MOD-08-L2 |
| 3 Crystal Incubator | 12 × 12 × 11 | A marble plinth with a glass dome over the basin, flanked by four crystal pylons | Marble, Glass (dome), Glass + Neon (pylon cores), Metal (frame) | Violet pylon cores `#A55BFF`, soft PointLight inside the dome | A crystal ring orbits the dome; pylons pulse in sequence during merge | MOD-08-L3 |
| 4 Aurora Crucible | 14 × 14 × 14 | A gilded frame holding a floating crucible bowl, three levitating rings around it | Foil (gilding), Metal, Marble (base), Glass (bowl), Neon (ring inlays) | Gold ring inlays `#FFB020`; aurora ribbons (Beam) in teal `#3FE0C5`, gold and rose; Mythical-rose crucible glow `#FF4D8D` | Three rings rotate on different axes (8, 12, 16 s periods); crucible rises 1 stud during merge | MOD-08-L4 |
| 5 Celestial Convergence Altar | 18 × 18 × 20 | A stepped marble altar, floating platform segments around it, a column of light to the sky | Marble, Glass, ForceField (prismatic shell), Neon, Foil (trim) | Prismatic ForceField shell over a night core `#1B1B2F`; star motes (ParticleEmitter); vertical sky beam (Beam) visible from the neighbouring plots; all six lower rarity colours as orbiting motes | Floating segments drift and lock into place during merge; altar steps unfold; orbiting "planet" spheres circle on 20 s period | MOD-08-L5 |

**Readability rules (PROPOSED).**
- Every level must be identifiable at 60 studs by silhouette alone (nest → forge → dome → rings → altar with sky beam).
- Emissive parts total at most 15 % of visible surface area at L5 to stay inside [[Performance Guidelines]].
- Particle emitters: L1 0, L2 1, L3 2, L4 3, L5 4, each with `Rate` ≤ 20 at idle; emitters disable beyond 150 studs using a distance check, because StreamingEnabled alone does not throttle emitters (behaviour *unverified*).
- The L5 sky beam is the only station element visible from other plots, as a status signal.

The `MOD-08` IDs are **PROPOSED** pending the [[Asset Register]] (module IDs MOD-01 to MOD-07 are expected to cover the seven other modules).

## 3. Upgrade animations (summary)

Each upgrade plays a construction sequence. Full specification: [[Animation - Base Upgrades]]; the merge sequences themselves are in [[Animation - Egg Merge]].

| Upgrade | Duration (PROPOSED) | Beats |
|---|---|---|
| Purchase (L1) | 3 s | Twigs fly in and weave; lever drops into place; lantern lights |
| L1 → L2 | 4 s | Stones rise from the ground around the nest; iron bands clamp; coal bed ignites |
| L2 → L3 | 4.5 s | Forge cools to grey; marble plinth lifts it; glass dome lowers; pylons grow from the corners |
| L3 → L4 | 5 s | Dome dissolves into light; rings assemble one by one; crucible floats up; aurora ribbons unfurl |
| L4 → L5 | 6 s | Rings expand and become floating platforms; altar steps rise; sky beam fires upward; server-wide toast "Player X raised a Celestial Convergence Altar" (PROPOSED, opt-out in [[UI - Settings]]) |

Upgrade animations are presentation only. The level is committed on the server before the animation starts.

## 4. Interaction and UI

- A ProximityPrompt (`Merge eggs`, hold 0.3 s) opens [[UI - Egg Merging]] when the owner is within 10 studs. Visitors see `Inspect` instead, which shows the level name only.
- Upgrade is done through [[UI - Base Upgrades]], which shows cost, gate status and a preview of the next form.
- The station is **not** a raid target and stores no eggs; it cannot be damaged or disabled by raiders (**PROPOSED**).

## Server validation

Every merge and upgrade request is validated in [[Service - MergeService]] (merges) and [[Service - BaseService]] (upgrades) inside one atomic profile update ([[Implementation - Egg Merge Transaction]], [[Data Consistency and Transactions]]).

| Check | Applies to | Error code |
|---|---|---|
| Player is at own base, within prompt range of the station | Merge, upgrade | `NotAtStation` |
| Station owned and level ≥ required for the input tier | Merge | `StationLevel` |
| Exactly 3 distinct egg IDs, all owned, all same rarity, rarity < 6 | Merge | `BadInputs`, `MixedRarity`, `MaxRarity` |
| No input egg locked by another pending action | Merge | `EggLocked` |
| Cash ≥ fee (merge) or cost (upgrade) | Both | `InsufficientCash` |
| Gate satisfied (regions unlocked, world boss defeated), read from persisted progress | Upgrade | `GateNotMet` |
| Upgrade target = current level + 1, ≤ 5 | Upgrade | `BadLevel` |
| Not combat-tagged; own base not under active raid | Both | `InCombat`, `BaseUnderRaid` |
| `requestId` not already processed; per-player in-flight lock | Both | Cached result / `Busy` |
| Rate limit: 4 merge commits per second | Merge | `RateLimited` |

On upgrade success, the server invalidates the player's luck cache (module levels are a PS input) so the next odds request reflects the new PS.

## 5. Error handling (player-facing, PROPOSED copy)

| Code | Message |
|---|---|
| `StationLevel` | "Upgrade to the Crystal Incubator to merge Epic eggs." (names the required level) |
| `GateNotMet` | "Unlock Coral Coast to build the Crystal Incubator." |
| `InsufficientCash` | "You need 2,700 Cash to merge these eggs." |
| `MixedRarity` | "All three eggs must be the same rarity." |
| `MaxRarity` | "Secret is the highest rarity. Secret eggs cannot be merged." |
| `BaseUnderRaid` | "You can't merge while your base is being raided." |
| `EggLocked` | "One of these eggs is busy. Try again in a moment." |
| `SaveFailed` | "Something went wrong. Your eggs and Cash are unchanged." |

## Related documents
- [[Egg Merging]] · [[UI - Egg Merging]] · [[UI - Base Upgrades]]
- [[Animation - Egg Merge]] · [[Animation - Base Upgrades]] · [[Sound - Eggs]]
- [[Player Base System]] · [[Base Upgrade System]] · [[Base Layout and Plot Expansion]] · [[Base Art Direction]]
- [[Service - MergeService]] · [[Implementation - Egg Merge Transaction]] · [[Test Cases - Egg Merging]]
- [[Canonical Proposed Values]]
