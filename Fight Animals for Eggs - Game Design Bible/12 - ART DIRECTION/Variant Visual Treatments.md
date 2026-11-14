---
title: Variant Visual Treatments
type: art-direction
category: art
status: mixed
priority: P1
owner: Technical Artist
last_updated: 2026-11-14
tags:
  - art
  - variants
  - materials
  - vfx
  - rarity
---

# Variant Visual Treatments

How the five special variants look: Golden (VAR-001), Diamond (VAR-002), Rainbow (VAR-003), Shadow (VAR-004) and Neon (VAR-005). Each variant is a **material set** applied to an existing animal model, plus a badge and a small particle set. Which species are eligible for which variants is owned by [[Animal Variants]] (**PROPOSED**). How variants are acquired is **UNDECIDED** ([[Open Questions#Q-006]]); whether they carry stat bonuses is **UNDECIDED** ([[Open Questions#Q-024]]). Nothing on this page assumes an answer to either.

> [!success] CONFIRMED
> Selected species have special variants; the owner's examples are Golden, Diamond, Rainbow, Shadow and Neon (D-028).

> [!warning] UNDECIDED
> Whether one animal can carry more than one variant at once (for example "Golden Shadow") is **UNDECIDED** (Q-608). This page specifies single variants only. If stacking is ever approved, a combination matrix must be designed; materials do not combine automatically.

## 1. Principles

1. **Same animal, new surface.** Variants never change mesh, proportions or silhouette, so the species still passes its silhouette test ([[Animal Modelling Principles]]).
2. **Variants do not borrow rarity signals.** No pips, no rarity frames, no rarity keys at full strength. A variant is shown with a corner badge (UI-008) and its material ([[Rarity Visual Language]] §5).
3. **Readable in every region.** Each variant must keep the animal's eyes, face and markings legible in all nine lighting presets ([[Lighting Direction]]).
4. **Friendly, always.** Shadow is "twilight", not evil. Neon is "glow-in-the-dark toy", not cyber-horror.
5. **Cheap enough for a full server.** Variant effects obey the particle caps below even when all 48 companions in a server are variants.

## 2. Treatment summary

| ID | Variant | Look in one line | Body colour values | Material approach | Particles | Badge |
|---|---|---|---|---|---|---|
| VAR-001 | Golden | Polished gold statue that is alive | Base `#FFC83D`, shade `#C98A12`, highlight `#FFF1B0` | Common–Rare: golden palette atlas + `Material = Foil` on accent parts only. Epic+: Golden SurfaceAppearance (MetalnessMap 1.0, Roughness 0.25) | 2 glints/s, star sparkle `#FFF1B0` | Gold coin emblem |
| VAR-002 | Diamond | Faceted crystal animal with sparkle | Base `#CFF4FF`, facet shade `#7FC8F0`, glint `#FFFFFF` | `Material = Glass`, `Transparency` 0.15, `Reflectance` 0.2 on Body; eyes, nose and mouth stay opaque SmoothPlastic. Low-end fallback: `Material = Ice`, opaque | 3 glints/s, 4-point star `#FFFFFF` | Cut-gem emblem |
| VAR-003 | Rainbow | Pastel rainbow bands flowing nose to tail | Bands `#FF8A8A`, `#FFC46B`, `#FFF07A`, `#8BE38B`, `#7FE0FF`, `#8AA8FF`, `#C49BFF` | Rainbow palette atlas (static bands mapped along body length); optional `Trail` in band colours on movement | Trail while moving; 2 pastel sparkles/s idle | Arc emblem |
| VAR-004 | Shadow | Twilight-coloured animal with a soft violet rim glow | Base `#2B2440`, mid `#3D3560`, markings `#6B5BB5`, rim `#9B7BFF`, eye glow `#CFC2FF` | Shadow palette atlas or SurfaceAppearance; `SmoothPlastic`; rim effect from a thin violet Neon accent strip (≤ 5% surface) along the back line | 3 soft violet wisps/s, `LightEmission` 0.3, rising (not trailing like smoke) | Crescent emblem |
| VAR-005 | Neon | Dark body with glowing marking lines | Body `#1A1D33`; glow pair `#39FFE0` + `#FF3DF2` (alternative pair `#B6FF3D` + `#3DA5FF` for species where pink clashes with natural markings) | Body SmoothPlastic with Neon-base atlas; markings on a **separate accent MeshPart** with `Material = Neon` (≤ 15% surface) | 1 pulse ring/2 s at feet | Glowing ring emblem |

All hex values are **PROPOSED** and live in [[Colour Palette]] if promoted to tokens.

## 3. Per-variant detail

### VAR-001 Golden
- Must look like **gold**, not like the Legendary rarity. The difference is metallic response (bright specular highlights, dark reflections) and sparkle, versus Legendary's flat `#FFB020` frame colour.
- Markings are preserved as darker gold `#C98A12` so the species remains identifiable (a Golden [[Tiger]] still shows stripes).
- Aura conflict rule: if the animal's rarity key shares the hue (Legendary), ascension auras switch to the rarity light tint ([[Rarity Visual Language]] §5).

### VAR-002 Diamond
- Glass on a skinned mesh shows interior faces when transparent. Production rule: Body mesh must be closed and back-face-clean; check under ShadowMap and on mobile. If artefacts appear, use `Transparency` 0 with a facet NormalMap (Epic+) or Ice material (Common–Rare).
- Eyes stay opaque and fully coloured so the animal looks alive, not hollow.
- Exact Glass rendering on MeshParts at low quality levels is *unverified*.

### VAR-003 Rainbow
- Static bands are the default. A runtime hue cycle (tweening `Color` on parts) is **not** used on animals, because it is expensive across many parts and fights the palette atlas.
- Rainbow pastels are lighter than the Secret prismatic set so a Rainbow animal never reads as Secret ([[Colour Palette]]).

### VAR-004 Shadow
- Banned: red or white glowing eyes, smoke that trails like ghosts, skulls, tattered edges. Eyes use the normal species eye with a `#CFC2FF` iris tint and the usual white highlight.
- Shadow animals in [[Region - Starfall Sanctuary]] and [[Region - Emberheart Caldera]] get their rim strip at full emission so they separate from dark grounds.
- Distinct from the Secret rarity: Shadow is violet and soft; Secret is deep navy with prismatic light. Shadow never uses prismatic colours.

### VAR-005 Neon
- Needs a **markings mesh**: every eligible species provides a separate `Accent` MeshPart that traces its natural markings (stripes, spots, wing bars, fins). Species with no natural markings get a standard "outline seam" pattern along spine and limbs.
- Neon coverage ≤ 15% so Bloom does not swallow the silhouette; tested under the lowest Bloom threshold (Starfall, 1.1).

## 4. Art-side eligibility constraints

[[Animal Variants]] decides which species get which variants. Art adds these production constraints; a species that cannot meet them should be flagged to the owner of that document rather than shipped with a broken look:

| Variant | Constraint |
|---|---|
| Golden | None beyond a clean UV layout |
| Diamond | Closed mesh; no thin overlapping shells (for example layered wing feathers) that break under Glass, or use the opaque fallback |
| Rainbow | Body length axis clear enough for bands (serpents and air-swimmers ideal; round species such as [[Hedgehog]] use radial bands) |
| Shadow | Species must have visible markings or facial features that survive a dark base; if not, add a lighter `#6B5BB5` muzzle and belly |
| Neon | Requires the `Accent` markings mesh (adds ~300–600 triangles, counted within the variant allowance below) |

Triangle allowance for variant accent meshes: **+15%** over the species budget (PROPOSED).

## 5. Implementation sketch

Variants are applied by swapping prepared instances, never by editing properties per frame. Illustrative only:

```lua
-- Illustrative Luau, not tested in Studio
-- VariantSets is a folder of prepared assets per variant ID, e.g. VariantSets["VAR-001"]
local function applyVariant(animalModel: Model, variantId: string, variantSets: Folder)
	local set = variantSets:FindFirstChild(variantId)
	if not set then return end
	local body = animalModel:FindFirstChild("Body") :: MeshPart
	local surface = set:FindFirstChild(animalModel:GetAttribute("AssetId"))
	if surface and surface:IsA("SurfaceAppearance") then
		local old = body:FindFirstChildOfClass("SurfaceAppearance")
		if old then old:Destroy() end
		surface:Clone().Parent = body
	elseif set:GetAttribute("AtlasTextureId") then
		body.TextureID = set:GetAttribute("AtlasTextureId")
	end
	if set:GetAttribute("BodyMaterial") then
		body.Material = Enum.Material[set:GetAttribute("BodyMaterial")]
	end
	animalModel:SetAttribute("VariantId", variantId)
end
```

The server owns which variant an animal has (data in [[Schema - Animal Collection]]); the client applies visuals. Whether `SurfaceAppearance` can be swapped at runtime by cloning in this way is *unverified* and is part of the look-dev checklist in [[Material and Texture Direction]].

## 6. Budgets (PROPOSED)

| Item | Cap |
|---|---|
| Variant particles per companion | ≤ 4 per second emission, ≤ 8 alive |
| Variant particles per wild animal | Same, and only within 80 studs of the camera |
| Variant `Trail` (Rainbow) | Local player's own animals and within 40 studs only |
| Variant atlases | 4 × 256×256 (Golden, Shadow, Neon base, Rainbow) |
| Variant SurfaceAppearance sets | One per eligible Epic+ species per variant; count depends on [[Animal Variants]] |

## 7. Test hooks

- Variant line-up scene: each variant on one animal of every body plan, in all nine lighting presets.
- Silhouette re-test: variant applied, silhouette unchanged (automated mesh-ID comparison).
- Confusion test: Golden vs Legendary card, Shadow vs Secret card, Rainbow vs Secret card; target zero confusion in a 5-person test.
- Performance: 48 companions all set to Diamond and Neon in one view, frame time recorded on the mobile reference device.

## Related documents
- [[Art Direction Index]]
- [[Animal Variants]]
- [[Rarity Visual Language]]
- [[Material and Texture Direction]]
- [[Colour Palette]]
- [[VFX - Rarity and Variant Effects]]
- [[Animal Modelling Principles]]
- [[Asset Register]]
