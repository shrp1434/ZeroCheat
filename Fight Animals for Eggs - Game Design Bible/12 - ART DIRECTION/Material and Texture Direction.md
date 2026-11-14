---
title: Material and Texture Direction
type: art-direction
category: art
status: proposed
priority: P0
owner: Technical Artist
last_updated: 2026-11-14
tags:
  - art
  - materials
  - textures
  - surface-appearance
  - performance
---

# Material and Texture Direction

Which Roblox materials to use for what, how textures are authored and sized, when `SurfaceAppearance` is allowed, and the texture-memory budget. All values are **PROPOSED**. Colour values come from [[Colour Palette]].

## 1. Principles

1. **Material carries meaning.** Players learn that Neon means energy or danger, Glass and Ice mean crystal or cold, Foil means precious, ForceField means protection. Do not use these materials decoratively against their meaning.
2. **Colour comes from palette atlases, not photos.** No photographic, scanned or stock textures anywhere ([[Art Bible]]).
3. **Share everything that can be shared.** One palette atlas serves every Common–Rare animal; one terrain material set serves every region.
4. **Texture budget follows rarity.** Rarer animals get richer surfaces, which is also a rarity signal ([[Rarity Visual Language]]).

## 2. Enum.Material usage table

| `Enum.Material` | Allowed on | Meaning and typical use | Notes |
|---|---|---|---|
| `SmoothPlastic` | Animals, props, base modules, UI-in-world | **Default** for everything stylised | Clean flat shading; cheapest to read |
| `Plastic` | Props, base L1 parts | Slightly textured toy surfaces | Use where SmoothPlastic looks too sterile at close range |
| `Neon` | Accent MeshParts only (≤ 15% of an asset's visible surface) | Energy, magic, telegraphs, lava cracks, Neon variant | Drives Bloom; never on large flat areas |
| `Glass` | Diamond variant, crystal props, Merging Station L3 | Crystal, precious transparency | Keep `Transparency` 0.1–0.3; check refraction cost on mobile |
| `ForceField` | Shields, raid barriers, boss invulnerability, spawn protection | Protection | Never on animals except a boss's invulnerable phase |
| `Foil` | Golden accents, Trophy Hall, Merging Station L4–L5 trims | Precious metal | Use small areas; strong specular |
| `Metal` / `DiamondPlate` | Defence Station, base L3 reinforcement | Engineering, defence | DiamondPlate only on floors and plates |
| `Wood` / `WoodPlanks` | Base L1, Whisperwood props, Twig Nest Press | Natural, starter | WoodPlanks for constructed items, Wood for natural logs |
| `Slate` / `Cobblestone` / `Brick` | Base L2, ruins, Hub paving | Stone, sturdy | Cobblestone for paths |
| `Marble` | Hub shrine, Celestial Convergence Altar, Starfall ruins | Sacred, celestial | Pair with Foil trims |
| `Granite` / `Rock` | Skyreach Peaks, cliff props | Mountain stone | |
| `Grass` / `LeafyGrass` | Terrain and prop tops | Living ground | LeafyGrass for Whisperwood and Emerald Canopy |
| `Sand` / `Sandstone` | Coral Coast, Sunscorch Savanna | Beach, dry rock | |
| `Ice` / `Glacier` / `Snow` | Frostfang Tundra, Crystal Incubator, Diamond low-end fallback | Cold | Ice for thin props, Glacier for terrain masses |
| `Basalt` / `CrackedLava` | Emberheart Caldera | Volcanic | CrackedLava for terrain; separate Neon crack meshes for glow |
| `Salt` / `Limestone` | Savanna flats, coastal cliffs | Pale mineral ground | |
| `Mud` / `Ground` | Paths, riverbanks | Worn ground | Keep saturation low |
| `Fabric` | Banners, tents in the Hub | Cloth | |
| `Pebble` | Riverbeds, garden borders | Detail ground | |

Banned on animals: `Concrete`, `Asphalt`, `CorrodedMetal` (wrong tone for creatures). `CorrodedMetal` is also banned on all props as it reads as decay and horror.

Custom looks for environment materials use `MaterialService` with `MaterialVariant` instances (for example a pastel `Grass` variant for the Hub). Each region may add at most **4** MaterialVariants (PROPOSED). MaterialVariant texture sets are 1,024×1,024 at most and are shared across regions where possible.

## 3. Animal surfaces by rarity

| Rarity | Surface method | Texture maps | Size | Notes |
|---|---|---|---|---|
| Common, Uncommon, Rare | `MeshPart.TextureID` = shared palette atlas; Material `SmoothPlastic` | Colour only | 256×256 (one atlas for all) | UV islands snap to flat swatches and gradient strips |
| Epic | `SurfaceAppearance` per species | ColorMap; optional NormalMap | 512×512 | Soft hand-painted gradients, painted markings |
| Legendary | `SurfaceAppearance` per species | ColorMap + NormalMap | 512×512 | Normal map adds faceted fur or feather grooves |
| Mythical | `SurfaceAppearance` per species | ColorMap + NormalMap + RoughnessMap | 1,024×1,024 | Roughness picks out horns, claws, shells |
| Secret | `SurfaceAppearance` per species | ColorMap + NormalMap + RoughnessMap + MetalnessMap | 1,024×1,024 | Metalness used only for small "ancient" inlays |

### The shared palette atlas (`ANM-000_PaletteAtlas_AT`)

- 256×256 px, divided into a 16 × 16 grid of 16 px swatches.
- Rows 0–9: flat colours grouped by hue family (browns, oranges, yellows, greens, blues, purples, pinks, greys, creams, near-darks).
- Rows 10–13: vertical gradient strips (top light, bottom dark) for soft shading on bellies and muzzles.
- Row 14: rarity trim swatches using the seven rarity keys from [[Colour Palette]] (used by ascension A1 trim).
- Row 15: reserved for eye whites, highlight white `#FFFFFF`, pupil `#1B1B2F`, nose `#3A2A33`, teeth `#F5EFE0`.
- Adding a colour requires Art Director approval and a palette-atlas version bump ([[Asset Naming Conventions]]).

Variant atlases (Golden, Shadow, Neon base, Rainbow bands) are separate 256×256 atlases with **the same grid layout**, so a variant can swap `TextureID` without changing UVs ([[Variant Visual Treatments]]).

> [!note] Look-dev verification needed
> The following platform behaviours must be checked in Studio before production and are *unverified* here:
> - Whether `MeshPart.Color` tints a mesh that has a `TextureID`, and how `Material` affects shading when a `TextureID` is present.
> - How `SurfaceAppearance` interacts with `MeshPart.Material` for Neon and Glass (expected: SurfaceAppearance overrides the material's look; Neon parts therefore stay separate MeshParts without SurfaceAppearance).
> - Whether `SurfaceAppearance` properties can be changed at runtime (assumed **not**; variants are prepared as separate SurfaceAppearance instances and swapped by cloning).

## 4. Environment textures

| Asset type | Method | Max size | Notes |
|---|---|---|---|
| Terrain | `Terrain` materials with `Terrain:SetMaterialColor` per region preset, plus MaterialVariants | 1,024 | Colour presets from [[Colour Palette]] region table |
| Hero landmarks | MeshPart + `SurfaceAppearance` | 1,024 | ≤ 6 hero landmarks per region |
| Standard props | MeshPart + region palette atlas (256×256 per region) | 256 | Same atlas method as animals |
| Foliage cards | MeshPart with alpha `TextureID` | 512 | Avoid; prefer solid low-poly leaf clusters |
| Decals and signage | `Decal` / `Texture` | 512 | Icon-only by default (Q-605) |
| Water | Terrain water; `Terrain.WaterColor` per region | — | Coral Coast `#3FC6D9`, Frostfang `#4FB0C6` |

## 5. UI textures

| Asset | Source size | Format |
|---|---|---|
| Icons (UI-004 to UI-008, UI-016, UI-021) | 256×256 or 512×512 | PNG, transparent |
| Card ornaments (UI-001) | 128×128 corner pieces | PNG |
| Animal portraits (UI-013) | 512×512 render, displayed ≤ 256 | PNG, transparent |
| Loading screen and key art (UI-020, UI-022) | 1,024×1,024 (largest safe upload size, *unverified* current limit) | PNG |

## 6. Texture memory budget

| Category | Budget (PROPOSED) | Calculation basis |
|---|---:|---|
| Animal palette atlases (base + 4 variant) | ≈ 1.3 MB | 5 × 256² × 4 bytes, uncompressed |
| Epic + Legendary animal SurfaceAppearance (17 species × 2 maps × 512²) | ≈ 36 MB | Upper bound if all on screen; usually far less |
| Mythical + Secret SurfaceAppearance (10 species × 3–4 maps × 1,024²) | ≈ 150 MB upper bound | Streaming means only a few are ever resident |
| Per-region environment set | ≤ 48 MB | Terrain variants + hero landmarks + prop atlas |
| UI | ≤ 24 MB | Icons, ornaments, portraits on screen |

These are uncompressed planning figures; GPU compression on device will reduce them (exact compression *unverified*). The key rule is **residency**: no more than one region's environment set plus the Hub set should be resident at once, using `StreamingEnabled` ([[Performance Guidelines]]).

## 7. Base and boss materials

- Base modules escalate material by upgrade level (Wood → Slate → Metal → Glass/Neon → Marble/Foil); the ladder is defined in [[Base Art Direction]].
- Bosses use 1,024 SurfaceAppearance sets plus Neon accent parts for phase changes ([[Boss Art Direction]]).
- Eggs follow the material escalation in [[Egg Art Direction]].

## 8. Review checklist

- [ ] No photographic or stock textures; every texture hand-authored or rendered from our own models.
- [ ] Material choice matches the meaning table in §2.
- [ ] Neon coverage ≤ 15% of visible surface; checked with Bloom on.
- [ ] Common–Rare animals use only the shared atlas (no per-species textures).
- [ ] Texture sizes match §3 and §5.
- [ ] Names follow [[Asset Naming Conventions]].

## Related documents
- [[Art Direction Index]]
- [[Colour Palette]]
- [[Animal Modelling Principles]]
- [[Variant Visual Treatments]]
- [[Lighting Direction]]
- [[Environment Art Direction]]
- [[Performance Guidelines]]
- [[Asset Register]]
