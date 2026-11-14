---
title: Egg Art Direction
type: art-direction
category: art
status: mixed
priority: P0
owner: Art Director
last_updated: 2026-11-14
tags:
  - art
  - eggs
  - rarity
  - modelling
---

# Egg Art Direction

The design principles shared by all seven egg models (EGG-01 to EGG-07): silhouette ladder, proportions, materials, state meshes and presentation rules. **Per-egg specifications (exact patterns, colours, effects and hatch choreography) are owned by the Egg Type documents:** [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]. Where those documents and this page disagree on a specific egg, the Egg Type document wins and this page should be updated.

> [!success] CONFIRMED
> Seven rarities (D-003). The roll decides egg rarity; the hatch picks an animal from that rarity's pool (D-015). Up to five eggs hatch at once (D-016). Three eggs of one rarity merge into one egg of the next rarity at an Egg Merging Station (D-020).

![[Seven Egg Silhouette Lineup.svg]]

## 1. Principles

1. **The egg is the rarity.** An egg's look must tell its rarity instantly, because in this game the egg's rarity is already decided at the roll ([[Egg Roll System]]). Eggs follow the ladder in [[Rarity Visual Language]]: colour → gradient → glow → motion → ornament → orbit → inversion.
2. **Silhouette changes every tier.** Each egg adds a silhouette feature so eggs are distinguishable as black shapes at 48 px in a 10-slot backpack grid ([[UI - Egg Storage]]).
3. **One base mesh family.** All eggs share an ovoid core so the hatch rig, crack states and storage racks work for every tier. Rarity is added with crowns, bands, shards and floating pieces.
4. **Precious, not creepy.** No veins, pulsing organic membranes, eyes inside eggs or creatures visible through the shell. Glow is clean light, never sickly.
5. **No hint of the animal inside.** Egg art never suggests which animal will hatch (no species silhouettes, spots or stripes that match a species), because every hatch is an independent draw from the pool ([[Independent Random Outcomes]]).

## 2. Proportions and scale (PROPOSED)

| Tier | Asset ID | Height (studs) | Height : width | Silhouette feature added | Triangles (all parts) |
|---|---|---:|---:|---|---:|
| Common | EGG-01 | 2.0 | 1.30 : 1 | Plain ovoid | 600 |
| Uncommon | EGG-02 | 2.1 | 1.30 : 1 | Raised band around the waist | 800 |
| Rare | EGG-03 | 2.2 | 1.32 : 1 | Band + gem stud on the front | 1,000 |
| Epic | EGG-04 | 2.4 | 1.34 : 1 | Crown of 3–5 crystal shards at the top | 1,400 |
| Legendary | EGG-05 | 2.6 | 1.35 : 1 | Filigree cage bands + crown points | 1,800 |
| Mythical | EGG-06 | 2.8 | 1.36 : 1 | Petal or fin flares at the base + one floating ring | 2,200 |
| Secret | EGG-07 | 3.2 | 1.40 : 1 | Floating shell shards orbiting a dark core | 2,600 |

Eggs sit on a flat base contact (bottom 6% of the ovoid flattened) so they rest stably in storage racks and on hatch pads. Pivot at the base centre.

## 3. Material escalation

| Tier | Shell material | Accent material | Texture |
|---|---|---|---|
| Common | `SmoothPlastic` | none | Shared egg atlas 256×256 (speckle swatches) |
| Uncommon | `SmoothPlastic` | `SmoothPlastic` band in light tint | Shared egg atlas |
| Rare | `SmoothPlastic` | `Glass` gem stud | Shared egg atlas |
| Epic | `SmoothPlastic` with SurfaceAppearance | `Glass` shards + small `Neon` cores | 512×512 set |
| Legendary | SurfaceAppearance (gloss) | `Foil` filigree bands | 512×512 set |
| Mythical | SurfaceAppearance (pearlescent via roughness map) | `Neon` ring + `Glass` flares | 512×512 set |
| Secret | SurfaceAppearance dark `#1B1B2F` with star speckle | `Glass` shards with prismatic `Neon` edges | 1,024×1,024 set |

Neon coverage stays under 15% of the visible egg surface ([[Material and Texture Direction]]).

## 4. Egg states

Every egg provides the same set of states so systems can treat eggs uniformly. Motion and timing are specified in [[Egg Animations]], [[Animation - Egg Roll]] and [[Animation - Egg Hatch]].

| State | Art requirement |
|---|---|
| Idle (storage, backpack preview) | Rest pose; Epic+ eggs have one looping accent (shard twinkle, ring rotation) that can be disabled in storage racks |
| Roll reveal | Egg appears on the Hub shrine pad; the roll outcome is already known to the server |
| Ready to hatch | Wobble; rarity key rim light |
| Crack stage 1 | Crack decal or crack mesh swap; light leaks in the rarity key |
| Crack stage 2 | Larger cracks; shell pieces lift 0.1 stud |
| Burst | Shell splits into 4–8 pre-cut shell pieces (separate MeshParts, `CanCollide = false`) that fade within 0.6 s |
| Merge input | Egg shrinks into the station ([[Animation - Egg Merge]]) |
| Merge output | New egg forms in the station, full-tier reveal at reduced intensity |

Pre-cut burst pieces are part of the egg model (named per [[Asset Naming Conventions]]) to avoid runtime mesh operations.

## 5. Placement contexts

| Context | Rules |
|---|---|
| Hub Egg Shrine ([[Hub - Hatchling Haven]]) | Rolled eggs appear on a lit pad; up to 5 pads for a ×5 roll |
| Backpack (10 slots, CONFIRMED) | UI icons only; renders from the egg portrait pipeline (UI-012) |
| Base storage (50 slots, CONFIRMED) | Physical display in the Egg Vault is designed in [[Base Art Direction]]; display density rules (how many physical eggs show) are **PROPOSED** there |
| Egg Merging Station | Three input sockets and one output cradle sized for the largest egg (Secret, 3.2 studs) |
| During a raid | Eggs in base storage may be stolen ([[Egg Theft Rules]]); visual marking of eggs a raider can interact with is defined with [[UI - Raid Interface]]. Backpack eggs are never stealable (CONFIRMED) and never appear in the base during a raid |

## 6. Odds and egg art

- The egg on the purchase or hatch screen is shown beside the **disclosed odds** ([[UI - Egg Rolling]], [[UI - Egg Hatching]]); egg art must never overlap or obscure the odds panel (D-017).
- Egg art does not change when the player's progression luck changes. Luck changes odds, which are displayed; it does not change how eggs look.

## 7. Edge cases

- **Secret eggs cannot be merged** (no tier above Secret, CONFIRMED). The station shows the Secret egg socket greyed out with a lock icon.
- **Five-egg hatch:** pads are spaced 4 studs apart so burst pieces do not overlap; the camera frames all five.
- **Event eggs** (if [[Seasonal and Limited-Time Events]] ever proposes them) must use one of the seven rarity ladders, not a new one.

## 8. Production notes

- Shared egg core mesh: `EGG-00_Core` (internal base mesh, not a shipped asset ID).
- Each egg ships as one `Model` with `Shell`, accent parts, `BurstPieces` folder and Attachments: `RimLight`, `CrackFX`, `BurstFX`, `OrbitRoot` (Mythical, Secret).
- Effects are attached to Attachments; their catalogue is in [[VFX Bible]].

## Related documents
- [[Art Direction Index]]
- [[Rarity Visual Language]]
- [[Egg System Overview]]
- [[Egg Animations]]
- [[Egg Merging Station]]
- [[Common Egg]] · [[Uncommon Egg]] · [[Rare Egg]] · [[Epic Egg]] · [[Legendary Egg]] · [[Mythical Egg]] · [[Secret Egg]]
- [[Asset Register]]
- [[Visual Reference Placeholders]]
