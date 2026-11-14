---
title: Animal Modelling Principles
type: art-direction
category: art
status: mixed
priority: P0
owner: Character Art Director
last_updated: 2026-11-14
tags:
  - art
  - animals
  - modelling
  - silhouettes
  - performance
---

# Animal Modelling Principles

How every one of the 60 launch animals is modelled: proportions per family, scale classes, triangle budgets, mesh structure, silhouette rules and the confusion groups that need special care. Species-specific design (colours, markings, personality) lives in each animal document, for example [[Tiger]]. Rig and skinning rules live in [[Animal Rig Standards]].

> [!success] CONFIRMED
> 60-animal launch target (D-004). Low-poly, colourful animals with clear silhouettes; no horror, brainrot or meme animals (D-026). Team size is three (D-006).

> [!info] PROPOSED
> Every number on this page (proportions, budgets, sizes) is a proposal for production. The launch roster itself is **PROPOSED** (D-032, [[Open Questions#Q-002]]).

## 1. Core rules

1. **One signature feature, exaggerated.** Each species has one or two "anchor" features that are enlarged 20–40% beyond natural proportion (Elephant ears, Rhino horn, Toucan beak, Peacock tail). The anchor must survive the silhouette test on its own.
2. **Faceted, not blocky.** Silhouette edges get one bevel loop; interior surfaces use large flat facets. Target average facet size: 4–8% of body length.
3. **Friendly faces.** Eyes are large (see §3), round, with a separate highlight. Mouths are closed at rest. No visible tongue or teeth at idle.
4. **Grounded stance.** Feet or contact points are wide enough to read stable. Bodies keep a low centre of mass for Tanks and Bruisers.
5. **No fine detail below 0.15 studs.** Anything smaller than 0.15 studs is painted, not modelled (whiskers, claws, individual feathers).

## 2. Scale classes

Scale is measured as the longest axis of the companion model in its idle pose, against a 5-stud reference player avatar. Wild animals of the same species use the same model and the same scale. Bosses use separate models ([[Boss Art Direction]]).

| Class | Longest axis (studs) | Shoulder or head height vs player | Examples |
|---|---|---|---|
| XS | 1.5–2.2 | knee height | Rabbit, Squirrel, Frog, Duck, Crab, Meerkat |
| S | 2.2–3.2 | thigh to hip | Fox, Owl, Raccoon, Penguin, Arctic Fox, Cobra (coiled) |
| M | 3.2–4.6 | hip to waist | Wolf, Deer, Cheetah, Zebra, Dolphin, Golden Eagle |
| L | 4.6–6.5 | waist to chest | Tiger, Brown Bear, Rhino, Hippo, Lion, Great White Shark |
| XL | 6.5–9.0 (hard cap) | chest to head | Elephant, Orca, Woolly Mammoth, Tyrannosaurus Rex, Blue Whale |

**Companion size cap: 9.0 studs on the longest axis (PROPOSED).** Colossal species (Blue Whale, Megalodon, Giant Squid, Mosasaurus, Titanoboa, Quetzalcoatlus) are compressed to the cap so that three companions and the player fit on screen and in base pens. Compression keeps proportions; the species still reads as "the biggest thing in my team". Owner acceptance of scale compression is **UNDECIDED** (Q-604). Each species' class is listed in the [[Asset Register]].

## 3. Proportions by family

Ratios are **head length : body length** (nose tip to back of head, versus back of head to rump, tail excluded) for quadrupeds, reptiles and aquatic animals, and **head height : total standing height** for birds and upright animals. Lower rarities lean cuter (bigger heads); higher rarities lean heroic (smaller heads, larger shoulders or wings).

| Family ([[Animal Families]]) | Head ratio Common–Rare | Head ratio Epic–Secret | Eye height as % of head height | Leg length as % of shoulder height | Notes |
|---|---|---|---:|---:|---|
| Forest Animals (11) | 1 : 1.8 | 1 : 2.4 | 18–22% | 35–45% | Cutest family; rounded cheeks; tails enlarged ~25% |
| Big Cats (6) | 1 : 2.4 (Cheetah, Leopard) | 1 : 2.8 | 14–17% | 45–55% | Broad muzzles; paws 1.3× natural; manes and ruffs as anchors |
| Safari Animals (6) | 1 : 2.2 | 1 : 2.8 | 12–15% | 40–50% | Heavy barrel bodies; horns, trunks and ears exaggerated |
| Aquatic Animals (14) | 1 : 2.0 | 1 : 2.6 | 12–16% | n/a (fins 1.2× natural) | Smooth sweeping forms; fins and tails as anchors |
| Birds (10) | 1 : 2.6 (head : height) | 1 : 3.2 | 22–28% | 20–35% | Large heads and beaks; wings fold to readable shapes at rest |
| Other Animals (13) | 1 : 2.0 | 1 : 2.6 | 14–20% | varies by body plan | Mixed plans; follow the closest family above |

Worked example: [[Wolf]] (Rare, Forest Animals) uses the Common–Rare forest ratio 1 : 1.8 but is pushed to 1 : 2.0 because Wolf is the forest family's first "heroic" animal and must not look like an enlarged Fox. [[Brown Bear]] (Rare) keeps 1 : 1.8 to stay approachable.

## 4. Body plans

Body plans group animals by skeleton and mesh structure. The rig details for each are owned by [[Animal Rig Standards]]; the codes here are art-side groupings used in the [[Asset Register]].

| Code | Body plan | Species (roster numbers from [[Canonical Proposed Values]] §2) |
|---|---|---|
| QDR | Quadruped (mammal) | 2, 3, 4, 8, 9, 11, 13, 15, 16, 17, 18, 24, 25, 26, 28, 33, 34, 37, 38, 42, 43, 44, 49, 51, 52 |
| HOP | Hopper | 1 Rabbit, 5 Frog, 27 Kangaroo |
| UPR | Upright small mammal | 10 Meerkat |
| PRM | Primate | 21 Monkey, 35 Gorilla |
| BGD | Ground bird | 6 Duck, 19 Flamingo, 23 Penguin, 30 Peacock |
| BFL | Flying bird or pterosaur | 7 Woodpecker, 14 Owl, 29 Toucan, 39 Golden Eagle, 48 Peregrine Falcon, 54 Haast's Eagle, 58 Quetzalcoatlus |
| SRP | Serpentine | 20 Cobra, 41 Electric Eel, 59 Titanoboa |
| SPR | Sprawling reptile | 36 Crocodile, 50 Komodo Dragon |
| THR | Bipedal theropod | 60 Tyrannosaurus Rex |
| PIN | Pinniped | 22 Seal, 32 Walrus |
| SWM | Air-swimmer (fish, cetacean, marine reptile) | 40 Dolphin, 45 Great White Shark, 46 Orca, 47 Narwhal, 53 Megalodon, 55 Blue Whale, 57 Mosasaurus |
| CEP | Cephalopod | 31 Octopus, 56 Giant Squid |
| ART | Arthropod walker | 12 Crab |

Air-swimmers and pinnipeds follow the **PROPOSED** air-swim convention (D-043): they hover 0.6–1.2 studs above ground with a water-trail effect from [[VFX Bible]]. How aquatic animals move on land is **UNDECIDED** ([[Open Questions#Q-028]]); pinnipeds are therefore modelled so that both a floating swim cycle and a ground "flipper crawl" are possible without remodelling (belly flat enough to rest on the ground).

## 5. Triangle and part budgets

Budgets are for the LOD0 companion model, excluding VFX and attached rarity or ascension accessories.

| Rarity | Triangles (LOD0) | XL class allowance | MeshParts max | Bones max | Texture set |
|---|---:|---:|---:|---:|---|
| Common | 2,000 | +20% | 3 | 24 | Shared palette atlas 256×256 |
| Uncommon | 2,500 | +20% | 3 | 26 | Shared palette atlas 256×256 |
| Rare | 3,000 | +20% | 4 | 30 | Shared palette atlas 256×256 |
| Epic | 4,000 | +20% | 4 | 34 | SurfaceAppearance 512×512 ColorMap (+ optional NormalMap) |
| Legendary | 5,000 | +20% | 5 | 40 | SurfaceAppearance 512×512 ColorMap + NormalMap |
| Mythical | 6,500 | +20% | 5 | 46 | SurfaceAppearance 1,024×1,024 ColorMap + NormalMap + RoughnessMap |
| Secret | 8,000 | +20% | 6 | 52 | SurfaceAppearance 1,024×1,024 full set |

MeshPart structure:
- **Part 1: `Body`**: one skinned MeshPart containing all deforming geometry.
- **Parts 2+: rigid accents**: horns, shells, tusks, armour plates, or any area that needs a different `Material` (for example a Neon stripe on [[Electric Eel]]). `Material` is per MeshPart, so any surface that needs Neon, Glass or ForceField must be its own part.
- Eyes are part of `Body` unless a variant needs them as separate parts (Diamond eyes stay opaque, see [[Variant Visual Treatments]]).
- `CollisionFidelity = Box` for every animal part; gameplay hitboxes are separate invisible parts defined in [[Animal Rig Standards]]. `RenderFidelity = Automatic`. `CastShadow = true` on `Body` only.

**Scene budget check (PROPOSED, to be validated in [[M20 - Optimisation]]):** 16 players × 3 companions at an average of 3,600 triangles ≈ 173,000; 60 fully simulated wild animals near players at an average of 2,900 ≈ 174,000. Animals therefore stay under about **350,000 triangles** on screen in the worst case before streaming and culling. Final scene budgets are owned by [[Animal Scalability and Performance Budgets]] and [[Performance Guidelines]].

Level of detail: Roblox reduces mesh detail automatically with `RenderFidelity = Automatic` (exact behaviour *unverified*). No hand-made LOD meshes are planned at launch; if profiling shows a need, a LOD1 at 40% triangles is the fallback.

## 6. Silhouette rules

Every animal must be identifiable as a **solid black silhouette at 64 × 64 px** in two views: side profile and three-quarter front. Test procedure:

1. Render the idle pose with an unlit black material on a white background at 512 px, then downscale to 64 px.
2. Show the sheet to three reviewers who did not make the model, mixed with every other animal in its confusion group.
3. Pass: all three name the species correctly within 2 seconds. Fail on any miss.
4. Repeat for the main attack pose: the silhouette must stay readable mid-action.

**Negative space rules:** at least one clear gap between legs in side view for all quadrupeds; tails and ears must break the body outline; birds at rest must show beak and leg separation.

### Confusion groups

| Group | Members | Differentiating anchors (silhouette only) |
|---|---|---|
| Small cats and big cats | Cheetah, Leopard, Snow Leopard, Tiger, Lion, Sabre-Tooth Tiger | Cheetah: tall thin legs, small head, deep chest. Leopard: low, long body, tail held in an S-curve. Snow Leopard: very thick tail 1.4× body width, rounded fluffy outline. Tiger: heavy shoulders, cheek ruff. Lion: mane doubles head width. Sabre-Tooth: short bobbed tail, sabre teeth visible in profile as a downward wedge (the one exception to "no teeth at rest", rounded tips only) |
| Canids | Fox, Arctic Fox, Wolf | Fox: huge brush tail ≥ body length, tall ears. Arctic Fox: round compact body, small rounded ears, fluffy tail curled to side. Wolf: longer legs, neck ruff, tail held straight |
| Raptors | Golden Eagle, Peregrine Falcon, Haast's Eagle | Golden Eagle: broad rectangular wings, feathered "trousers". Peregrine: pointed swept wings, compact. Haast's Eagle: oversized hooked beak and talons, crest |
| Sharks and marine reptiles | Great White Shark, Megalodon, Mosasaurus | Great White: classic triangle dorsal, conical snout. Megalodon: blunter, much deeper body, double-height dorsal. Mosasaurus: four paddle flippers, long jaw, tail fluke |
| Whales and dolphins | Dolphin, Orca, Narwhal, Blue Whale | Dolphin: long beak, curved dorsal. Orca: tall straight dorsal. Narwhal: tusk ≥ 40% body length. Blue Whale: tiny dorsal, very long flat head, throat grooves |
| Serpents | Cobra, Titanoboa, Electric Eel | Cobra: raised hood. Titanoboa: very thick body, coiled stack. Electric Eel: long ventral fin ribbon, floating |
| Reptile sprawlers | Crocodile, Komodo Dragon | Crocodile: flat long snout, ridged back, tail-heavy. Komodo: shorter deeper head, raised gait, forked tongue flick in idle |
| Heavy grazers | Rhino, Hippo, Elephant, Woolly Mammoth | Rhino: double horn. Hippo: wide square muzzle, short legs. Elephant: ears + trunk. Mammoth: domed head, curved tusks, shaggy hump |
| Bears | Brown Bear, Giant Panda | Brown Bear: shoulder hump, longer muzzle. Panda: round ears, rounder head, shorter muzzle |
| Rodent-like smalls | Squirrel, Rabbit, Meerkat, Hedgehog | Squirrel: S-curved tail over back. Rabbit: long ears. Meerkat: upright stance. Hedgehog: spiky dome outline |

Colour does not count in the silhouette test. If an animal fails, change shape, not paint.

## 7. Topology and export checklist

| Item | Rule (PROPOSED) |
|---|---|
| Up axis and facing | Y up, model faces −Z in Studio after import |
| Origin | Pivot at ground contact centre for walkers; at the hover rest point for air-swimmers and flyers (see [[Animal Rig Standards]]) |
| Units | 1 Blender unit = 1 stud at export (verify importer scale in M02) |
| Normals | Flat-shaded facets on body; smoothing groups only on eyes, noses and highlights |
| N-gons | Triangulate before export |
| UVs | Common–Rare: UV islands snapped to swatches on the shared palette atlas. Epic+: one 0–1 UV set, ≥ 85% space usage |
| Naming | Per [[Asset Naming Conventions]] (`ANM-034_Tiger_Body` etc.) |
| Mesh limits | Stay well below the platform's per-mesh triangle limit (current limit *unverified*; check before production) |

## 8. Rarity and ascension layers on the model

The base model never changes with rarity: rarity is a property of the species. Layers added on top:
- **Ascension A1–A5** visual tiers from [[Canonical Proposed Values]] §9 (trim, eye glint, aura, particle accents, crest). Models must provide: a trim UV region or trim MeshPart, an `EyeGlint` Attachment per eye, an `AuraRoot` Attachment at the centre of mass and a `Crest` Attachment on the head top. Effects themselves are in [[VFX - Rarity and Variant Effects]].
- **Variants** swap material sets ([[Variant Visual Treatments]]).
- **Rarity world signals** (nameplate pips, wild ground rings) are separate from the model ([[Rarity Visual Language]]).

## 9. Edge cases

- **Flying animals in pens and at rest** must have a perched or grounded idle (no permanent hover) so base displays look calm ([[Module - Animal Pens]], display rule [[Open Questions#Q-008]]).
- **Multi-limb animals** (Octopus, Giant Squid, Crab) cap arm or leg counts for budget: Octopus and Giant Squid keep 8 arms (squid tentacles merged into the arm silhouette, 2 longer arms), Crab keeps 8 legs as 4 rigid pairs.
- **Stolen animals** keep their model unchanged; what else they keep is **UNDECIDED** ([[Open Questions#Q-025]]).

## Related documents
- [[Art Direction Index]]
- [[Art Bible]]
- [[Animal Rig Standards]]
- [[Material and Texture Direction]]
- [[Rarity Visual Language]]
- [[Variant Visual Treatments]]
- [[Animal Families]]
- [[Animal Index]]
- [[Asset Register]]
- [[Animal Scalability and Performance Budgets]]
- [[Visual Reference Placeholders]]
