---
title: Asset Naming Conventions
type: spec
category: assets
status: mixed
priority: P0
owner: Technical Artist
last_updated: 2026-11-14
tags:
  - assets
  - naming
  - pipeline
  - roblox
---

# Asset Naming Conventions

How art assets are identified and named: asset IDs, source files, exported files, Roblox upload names, Studio instance names, attributes and versioning. The ID prefixes themselves are set in `CLAUDE.md` §9 (vault rules); everything else here is **PROPOSED**. Where assets sit in the Roblox place hierarchy is owned by [[Roblox Project Hierarchy]].

## 1. Asset IDs

| Prefix | Class | Format | Range at launch | Allocated in |
|---|---|---|---|---|
| ANM | Animal models | `ANM-###` | ANM-001 to ANM-060 (catalogue order) | [[Asset Register]] |
| VAR | Variant material sets | `VAR-###` | VAR-001 to VAR-005 | [[Asset Register]] |
| BOS | Boss models | `BOS-##` | BOS-01 to BOS-12 | [[Asset Register]] |
| EGG | Egg models | `EGG-##` | EGG-01 to EGG-07 | [[Asset Register]] |
| ENV | Environment kits and props | `ENV-###` | ENV-001 to ENV-022 | [[Asset Register]] |
| MOD | Base module models | `MOD-##` | MOD-01 to MOD-09 | [[Asset Register]] |
| UI | UI assets | `UI-###` | UI-001 to UI-022 | [[Asset Register]] |
| ANI | Animations | `ANI-###` | Owned by [[Animation Bible]] | [[Animation Bible]] |
| VFX | Visual effects | `VFX-###` | Owned by [[VFX Bible]] | [[VFX Bible]] |
| SFX | Sound effects | `SFX-###` | Owned by [[Sound Bible]] | [[Sound Bible]] |
| MUS | Music | `MUS-##` | Owned by [[Music Direction]] | [[Music Direction]] |

Rules:
1. IDs are permanent. A cut asset keeps its ID, marked "cut" in the register; the ID is never reused.
2. ANM numbers follow the canonical roster order in [[Canonical Proposed Values]] §2. If the roster changes before production locks (D-032 is **PROPOSED**), renumbering is done once, recorded in the [[Changelog]], and all references are updated in the same change.
3. Sub-assets extend the parent ID with an underscore suffix (never a new ID): `ANM-034_Body`, `BOS-07_Trophy`, `MOD-08_L3`.
4. Composite assets join IDs with a hyphen: a Golden Tiger material set is `ANM-034-VAR-001`.

## 2. Name grammar

```
<AssetID>_<PascalName>[_<Part>][_<Variant>][_<LOD>][_<MapType>][_v<NN>].<ext>
```

| Token | Values | Example |
|---|---|---|
| `AssetID` | From §1 | `ANM-034` |
| `PascalName` | Species or asset name, PascalCase, ASCII only, no spaces or apostrophes | `Tiger`, `HaastsEagle`, `SabreToothTiger`, `GreatWhiteShark` |
| `Part` | `Body`, `Accent`, `Horn`, `Shell`, `Eyes`, `BurstPieces`, `L1`–`L5`, `Stage1`–`Stage4`, `Trophy` | `Body` |
| `Variant` | `VAR001`–`VAR005` (no hyphen inside file tokens) | `VAR001` |
| `LOD` | `LOD0`, `LOD1` (only if a manual LOD is ever made) | `LOD0` |
| `MapType` | `CM` colour, `NM` normal, `RM` roughness, `MM` metalness, `AT` palette atlas | `CM` |
| `v<NN>` | Two-digit source version | `v03` |

Worked examples:

| Asset | File name |
|---|---|
| Tiger source scene | `ANM-034_Tiger_v03.blend` |
| Tiger body export | `ANM-034_Tiger_Body_LOD0.fbx` |
| Tiger colour map | `ANM-034_Tiger_CM_v02.png` |
| Golden Tiger colour map | `ANM-034_Tiger_VAR001_CM_v01.png` |
| Haast's Eagle body | `ANM-054_HaastsEagle_Body_LOD0.fbx` |
| Crystal Incubator (station L3) | `MOD-08_EggMergingStation_L3_v01.fbx` |
| Secret Egg burst pieces | `EGG-07_SecretEgg_BurstPieces_v01.fbx` |
| Cinderjaw trophy | `BOS-07_Cinderjaw_Trophy_v01.fbx` |
| Shared animal palette atlas | `ANM-000_PaletteAtlas_AT_v04.png` (ANM-000 is reserved for shared animal resources, not a model) |
| Golden palette atlas | `VAR-001_Golden_AT_v01.png` |
| Emberheart prop atlas | `ENV-008_EmberheartCaldera_AT_v02.png` |
| Rarity frame corner, Legendary | `UI-001_RarityFrame_Legendary_Corner_v01.png` |

Reserved shared IDs: `ANM-000` (shared animal resources), `EGG-00` (shared egg core mesh), `ENV-000` (shared world resources). They never appear as playable or placeable assets.

## 3. Roblox upload names

Uploaded assets (meshes, images) are named with a project prefix so they are searchable in the creator inventory:

```
FAFE_<AssetID>_<PascalName>[_<Part>][_<Variant>][_<MapType>]
```

Example: `FAFE_ANM-034_Tiger_Body`, `FAFE_ANM-034_Tiger_VAR001_CM`. Upload names do not carry the version; the version lives in the source file name and in the `AssetVersion` attribute (§5).

## 4. Studio instance names

| Instance | Name | Example |
|---|---|---|
| Animal `Model` | `<PascalName>` | `Tiger` |
| Skinned body `MeshPart` | `Body` | `Body` |
| Rigid accent parts | Part token | `Horn`, `Accent`, `Shell` |
| Hitbox parts | Defined by [[Animal Rig Standards]] | — |
| Attachments for effects | `AuraRoot`, `EyeGlint_L`, `EyeGlint_R`, `Crest`, `RimLight`, `CrackFX`, `BurstFX`, `OrbitRoot`, `TrailTop`, `TrailBottom` | `AuraRoot` |
| Egg `Model` | `<PascalName>` | `LegendaryEgg` |
| Module level models | `<PascalName>_L<n>` | `ShieldGenerator_L4` |
| Lighting effect instances | `Region<Effect>` for presets, `<Moment><Effect>` for presentations | `RegionBloom`, `HatchColorCorrection`, `BossColorCorrection` |
| Variant set folders | `<VariantID>` | `VAR-003` |

Names are ASCII PascalCase with no spaces, so they can be used safely in code paths. Display names shown to players (for example "Haast's Eagle") come from data and localisation, never from instance names.

## 5. Attributes and tags

Every top-level asset `Model` carries these attributes (set by the import tool, checked by the validator in §7):

| Attribute | Type | Example | Purpose |
|---|---|---|---|
| `AssetId` | string | `"ANM-034"` | Links instance to the register |
| `AssetVersion` | number | `3` | Matches the source file version |
| `BodyPlan` | string | `"QDR"` | Animals only ([[Animal Modelling Principles]]) |
| `SizeClass` | string | `"L"` | Animals only |
| `TriBudget` | number | `4000` | Used by automated budget checks |
| `VariantId` | string | `""` or `"VAR-001"` | Set at runtime when a variant is applied |

CollectionService tags (PascalCase): `AnimalModel`, `EggModel`, `BossModel`, `BaseModule`, `EnvHeroLandmark`, `EnvProp`, `RarityAuraHost`. Gameplay tags are owned by the engineering documents ([[Roblox Project Hierarchy]]); art tags must not collide with them.

## 6. Source folder structure (art repository)

```
Art/
  Source/
    Animals/ANM-034_Tiger/      ANM-034_Tiger_v03.blend, textures/, renders/
    Eggs/EGG-05_LegendaryEgg/
    Bosses/BOS-09_IronbarkColossus/
    Modules/MOD-08_EggMergingStation/
    Environment/ENV-008_EmberheartCaldera/
    UI/UI-001_RarityFrame/
    Variants/VAR-002_Diamond/
  Export/                        mirrors Source; only export files
  Reference/                     concept art produced from Visual Reference Placeholders briefs
```

No stock imagery is stored in `Reference/`. Concept art produced in-house or commissioned under contract is the only reference material ([[Visual Reference Placeholders]]).

## 7. Validation

Illustrative only; not tested in Studio.

```lua
-- Illustrative Luau, not tested in Studio
local CollectionService = game:GetService("CollectionService")
local ID_PATTERNS = {
	"^ANM%-%d%d%d$", "^VAR%-%d%d%d$", "^BOS%-%d%d$", "^EGG%-%d%d$",
	"^ENV%-%d%d%d$", "^MOD%-%d%d$", "^UI%-%d%d%d$",
}
local function isValidId(id: string): boolean
	for _, pattern in ID_PATTERNS do
		if string.match(id, pattern) then return true end
	end
	return false
end

for _, model in CollectionService:GetTagged("AnimalModel") do
	local id = model:GetAttribute("AssetId")
	if typeof(id) ~= "string" or not isValidId(id) then
		warn("Missing or invalid AssetId", model:GetFullName())
	end
	if not model:FindFirstChild("Body") then
		warn("Animal model has no Body MeshPart", model:GetFullName())
	end
end
```

Pre-commit checks on source files (pipeline tooling, not Luau): file name matches the grammar in §2; version increments; texture sizes match [[Material and Texture Direction]].

## Related documents
- [[Assets Index]]
- [[Asset Register]]
- [[Visual Reference Placeholders]]
- [[Roblox Project Hierarchy]]
- [[Animal Rig Standards]]
- [[Material and Texture Direction]]
- [[Art Direction Index]]
