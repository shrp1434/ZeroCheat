---
title: Animal Rig Standards
type: standard
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - rigging
  - motor6d
  - animals
  - technical-art
---

# Animal Rig Standards

This standard defines how every animal, companion, wild animal and boss is rigged so that animations, VFX attachments and code can be shared across the 60-animal launch roster. It is binding for modellers ([[Animal Modelling Principles]]), animators ([[Animation Bible]]) and engineers ([[Client Controllers]]).

> [!info] PROPOSED
> Everything in this document is **PROPOSED** by the Animation Director. Rig classes, joint names, budgets and priority mapping can be used for prototyping immediately. The roster itself is **PROPOSED** (D-032, [[Open Questions#Q-002]]); if species change, the rig class table in §4 is updated, not the standard.

---

## 1. Principles

1. **Seven rig classes, not sixty rigs.** Every animal belongs to exactly one rig class. All animals in a class share part names, joint names and attachment names, so one animation can be retargeted across the class by re-uploading against a proportion-matched rig.
2. **Motor6D rigid-part rigs.** The low-poly art style ([[Art Bible]], D-026) uses separate rigid mesh parts joined by `Motor6D`. No skinned meshes at launch. This keeps the rigs cheap on mobile, readable in the Roblox Animation Editor, and avoids bone-weight artefacts on faceted geometry.
3. **No Humanoid on animals.** Animals use an `AnimationController` with a child `Animator`. A `Humanoid` brings state machines, physics and name-plate behaviour the game does not need and costs more per instance (we expect up to 180 simulated wild animals per server; see [[Animal Scalability and Performance Budgets]]). Movement is driven by [[Service - AnimalAIService]], not by Humanoid physics.
4. **Gameplay never reads the rig.** Hitboxes, ranges and damage timing come from configuration ([[Configuration Modules]]), not from part positions or animation markers. Markers drive client cosmetics only (§7).

---

## 2. Required model structure

```text
Model "ANM-034_Tiger"          (PrimaryPart = HumanoidRootPart)
├── HumanoidRootPart          invisible, Anchored = false, CanCollide = false, Massless = false
├── AnimationController
│   └── Animator
├── Pelvis                    (contains Motor6D "J_Pelvis": Part0 = HumanoidRootPart)
├── Spine                     (contains Motor6D "J_Spine":  Part0 = Pelvis)
├── ...                       (one Motor6D per child part, inside the child part)
├── Hitbox                    invisible box, CanCollide = false, CanQuery = true, not jointed by Motor6D (WeldConstraint to HumanoidRootPart)
└── Attachments live inside the parts listed in §6
```

| Rule | Requirement |
|---|---|
| Root part name | `HumanoidRootPart`. The name is kept for compatibility with the Roblox Animation Editor and rig tooling even though there is no Humanoid. |
| Root size | Box covering the animal's ground footprint; height equals shoulder height. Used by the AI mover and by camera framing. |
| Forward axis | Model faces −Z (the root's `LookVector`). Y is up. |
| Bind pose | Neutral standing pose, feet on the ground plane at Y = root bottom. Not a T-pose. All Motor6D `Transform` values are identity in bind pose. |
| Motor6D placement | Inside the **child** part, named `J_<ChildPartName>`. Part0 = parent, Part1 = child. |
| Part naming | PascalCase. Sides use the suffix `L` / `R` (animal's own left/right). Chains use numeric suffixes from root outwards: `Tail1`, `Tail2`, `Tail3`. |
| Cosmetic parts | Rarity trims, variant overlays and ascension crests ([[Variant Visual Treatments]]) attach with `WeldConstraint` to the part they decorate. Never add a Motor6D for a cosmetic. |
| Collisions | Every visual part: `CanCollide = false`, `CanTouch = false`, `CanQuery = false`. Only `Hitbox` is queryable. |
| Animation ownership | Animation assets must be uploaded by the group that owns the experience; animations owned by another account do not play in the live game. |

---

## 3. Rig classes and joint lists

### 3.1 Summary

| Class code | Body plan | Motor6D budget | Parts (typical) | Notes |
|---|---|---:|---:|---|
| QS | Quadruped small | ≤ 18 | 15–19 | Two-segment legs allowed |
| QL | Quadruped large | ≤ 26 | 22–27 | Three-segment legs; gait profiles in §4.2 |
| BP | Biped primate | ≤ 22 | 20–23 | Long arms reach the ground for knuckle gait |
| BD | Bird (ground and flight) | ≤ 22 | 18–23 | Three-segment wings |
| SP | Serpent | ≤ 12 | 11–13 | Eight-segment body chain |
| AQ | Aquatic air-swim | ≤ 16 | 12–17 | Flipper or tentacle sub-layouts |
| PB | Prehistoric large biped | ≤ 24 | 22–25 | Heavy tail counterbalance; also the hopper sub-layout |
| BOSS | Boss scale (any plan) | ≤ 40 | — | Class layout of its base animal plus extra break-off and armour parts |

### 3.2 QS — Quadruped small

`HumanoidRootPart → Pelvis → Spine → Chest → Neck → Head → Jaw`, plus `EarL`, `EarR` (on Head), `Tail1 → Tail2`, and four legs: `FrontUpperLegL → FrontFootL`, `FrontUpperLegR → FrontFootR`, `HindUpperLegL → HindFootL`, `HindUpperLegR → HindFootR`.

- Optional: `Tail3`, `FrontLowerLeg*`, `HindLowerLeg*` (counts against the 18 budget).
- **Crab sub-layout (QS-C):** `Chest` holds `ClawL`, `ClawR` (each with `ClawPincer*`) and three leg pairs `LegA*`, `LegB*`, `LegC*` (single segment). `Spine`, `Neck` and `Tail*` are omitted. Eye stalks are cosmetic parts welded to `Head`.

### 3.3 QL — Quadruped large

As QS, plus `Spine2` between `Spine` and `Chest`, three-segment legs (`UpperLeg`, `LowerLeg`, `Foot`), and `Tail3`. Optional: `Trunk1 → Trunk2 → Trunk3` (Elephant, Woolly Mammoth), `HornBase` (Rhino, cosmetic otherwise), `Mane` (Lion, single joint for secondary motion).

### 3.4 BP — Biped primate

`HumanoidRootPart → Pelvis → Spine → Chest → Neck → Head → Jaw`, `ShoulderL → UpperArmL → LowerArmL → HandL` (and R), `UpperLegL → LowerLegL → FootL` (and R), `Tail1 → Tail2` (Monkey only). Arm length must let `HandL/R` touch the ground with `Chest` pitched 35° forward, for the knuckle-walk gait.

### 3.5 BD — Bird

`HumanoidRootPart → Pelvis → Body → Neck1 → Neck2 → Head → BeakUpper, BeakLower`, `WingInnerL → WingOuterL → WingTipL` (and R), `UpperLegL → LowerLegL → FootL` (and R), `TailFan`. Long-necked birds (Flamingo) add `Neck3`. **Pterosaur sub-layout (BD-P, Quetzalcoatlus):** wings also act as forelimbs; `WingOuter*` carries an attachment `A_WingHand*` that plants on the ground during the quad-walk.

### 3.6 SP — Serpent

`HumanoidRootPart → Seg1 → Seg2 → … → Seg8 → TailTip`, `Seg1 → Neck → Head → Jaw`, optional `Hood` (Cobra). The chain runs from the root (mid-body) both forwards (Neck/Head) and backwards (Seg2–Seg8), so the body can coil around the root. Titanoboa uses the same chain scaled up; do not add segments.

### 3.7 AQ — Aquatic air-swim

Default fish and cetacean layout: `HumanoidRootPart → Body → Head → Jaw`, `Body → Tail1 → Tail2 → Fluke`, `FinL`, `FinR` (pectoral), `DorsalFin` (cosmetic or single joint), optional `Horn` (Narwhal).

- **Pinniped sub-layout (AQ-PN, Seal, Walrus):** adds `FrontFlipperL/R` and `HindFlipperL/R`; `Tusks` (Walrus) are welded to `Head`.
- **Cephalopod sub-layout (AQ-CE, Octopus, Giant Squid):** `Body → Mantle`, `Body → Head`, and arms `ArmA1 → ArmA2` to `ArmH1 → ArmH2` (8 arms × 2 segments = 16; the two Giant Squid feeding tentacles are cosmetic extensions welded to `ArmA2` and `ArmB2`). This sub-layout is permitted 18 Motor6Ds.

The air-swim body plan follows D-043 (**PROPOSED**); how aquatic animals move on land is **UNDECIDED** ([[Open Questions#Q-028]]). The rig supports both outcomes: the AQ-PN layout can also drive a ground "flop" gait if Q-028 resolves to ground movement.

### 3.8 PB — Prehistoric large biped

`HumanoidRootPart → Pelvis → Spine → Chest → Neck → Head → Jaw`, `ArmL → HandL` (and R, short), `UpperLegL → LowerLegL → AnkleL → FootL` (and R; digitigrade), `Tail1 → Tail2 → Tail3 → Tail4`. **Hopper sub-layout (PB-H, Kangaroo):** same names, `Arm*` gains `LowerArm*`, and `Tail*` is reduced to three segments; the tail acts as a fifth limb during the idle prop.

---

## 4. Roster assignment

### 4.1 Animals per class (PROPOSED)

| Class | Count | Animals |
|---|---:|---|
| QS | 11 | [[Rabbit]], [[Squirrel]], [[Hedgehog]], [[Raccoon]], [[Frog]], [[Meerkat]], [[Fox]], [[Badger]], [[Beaver]], [[Arctic Fox]], [[Crab]] (QS-C) |
| QL | 20 | [[Boar]], [[Goat]], [[Zebra]], [[Deer]], [[Hyena]], [[Wolf]], [[Brown Bear]], [[Cheetah]], [[Leopard]], [[Tiger]], [[Snow Leopard]], [[Lion]], [[Sabre-Tooth Tiger]], [[Rhino]], [[Hippo]], [[Elephant]], [[Giant Panda]], [[Woolly Mammoth]], [[Crocodile]], [[Komodo Dragon]] |
| BP | 2 | [[Monkey]], [[Gorilla]] |
| BD | 11 | [[Duck]], [[Woodpecker]], [[Owl]], [[Flamingo]], [[Penguin]], [[Toucan]], [[Peacock]], [[Golden Eagle]], [[Peregrine Falcon]], [[Haast's Eagle]], [[Quetzalcoatlus]] (BD-P) |
| SP | 3 | [[Cobra]], [[Titanoboa]], [[Electric Eel]] (air-swim serpent) |
| AQ | 11 | [[Seal]] (AQ-PN), [[Walrus]] (AQ-PN), [[Octopus]] (AQ-CE), [[Giant Squid]] (AQ-CE), [[Dolphin]], [[Great White Shark]], [[Orca]], [[Narwhal]], [[Megalodon]], [[Blue Whale]], [[Mosasaurus]] |
| PB | 2 | [[Tyrannosaurus Rex]], [[Kangaroo]] (PB-H) |
| **Total** | **60** | |

[[Crab]] and [[Crocodile]] belong to the Aquatic Animals family ([[Animal Families]]) but walk natively, so they use land rigs rather than air-swim.

### 4.2 QL gait profiles

One QL skeleton, six gait profiles. A profile changes the locomotion clips only ([[Animation - Animal Locomotion]]); attack, hit and defeat clips stay class-wide.

| Profile | Animals | Character |
|---|---|---|
| Feline | Cheetah, Leopard, Tiger, Snow Leopard, Lion, Sabre-Tooth Tiger | Flexible spine, rotary gallop, low head carriage |
| Canine | Wolf, Hyena | Transverse gallop, level back, tail as counterbalance |
| Ungulate | Boar, Goat, Zebra, Deer | Stiff back, bouncing gait, high head |
| Plantigrade | Brown Bear, Giant Panda | Rolling shoulders, heavy forefoot plant |
| Pachyderm | Rhino, Hippo, Elephant, Woolly Mammoth | Amble instead of gallop; never all four feet off the ground |
| Sprawler | Crocodile, Komodo Dragon | Legs out to the side, lateral spine wave, belly close to ground |

### 4.3 Bosses

World bosses use the rig class of their base animal at boss scale ([[Boss Art Direction]]): [[World Boss - Ironbark Colossus]] (QL-Pachyderm profile, tortoise shell parts), [[World Boss - Thunderhoof]] (QL-Pachyderm), [[World Boss - Abyssal Leviathan]] (AQ), [[World Boss - Ashwing Condor]] (BD). Mini-boss rig classes are set in each boss document. Boss rigs may add up to 14 extra Motor6Ds for armour plates, break-off parts and phase-change pieces (BOSS budget ≤ 40).

---

## 5. Scale and proportion

| Size band | Applies to | Root height (studs) | Notes |
|---|---|---:|---|
| Tiny | Frog, Hedgehog, Crab, Squirrel, Meerkat, Rabbit | 1.2–1.8 | Head enlarged 15% for readability |
| Small | Other QS, small birds, Cobra | 1.8–2.6 | |
| Medium | Most QL, BP, large birds, PB-H | 2.6–4.5 | |
| Large | Pachyderms, PB, large AQ, Titanoboa | 4.5–7.0 | |
| Colossal (companion) | Blue Whale, Megalodon, Woolly Mammoth | 7.0–9.0 | Companion scale is clamped so three animals and the player fit in the camera ([[Camera Behaviour Guidelines]]) |
| Boss | Bosses | 12–40 | |

These bands are **PROPOSED** and owned jointly with [[Animal Modelling Principles]]. Real-world size ratios are compressed on purpose: a companion Blue Whale must not block the screen.

---

## 6. Attachments (VFX and SFX anchors)

Every rig must provide these `Attachment` instances, named exactly as below. VFX ([[VFX Bible]]) and SFX ([[Sound Bible]]) spawn on attachments, never on raw part positions.

| Attachment | Parent part | Use |
|---|---|---|
| `A_Root` | HumanoidRootPart, at ground level | Ground decals, auras, shadows, footstep dust for small animals |
| `A_Chest` | Chest / Body / Seg1 | Hit sparks received, heal motes, Highlight anchor |
| `A_Head` | Head | Status icons (stun stars), vocal sound emitter |
| `A_Overhead` | HumanoidRootPart, 1 stud above the tallest point | Name tags, KO and stealable markers ([[Animation - Raid Interactions]]) |
| `A_Mouth` | Jaw / BeakLower / Head | Breath, spit, roar and projectile origin |
| `A_StrikeL`, `A_StrikeR` | Front feet, hands, claws, wing tips, tail tip or fluke | Strike trails and hit-spark origin |
| `A_FootFL/FR/HL/HR` | Feet (quadrupeds), `A_FootL/R` (bipeds, birds) | Footstep markers for large animals (dust and sound) |
| `A_Tail` | Last tail segment | Trails, air-swim water trail (D-043) |
| `A_Aura` | HumanoidRootPart centre | Rarity and ascension auras ([[VFX - Rarity and Variant Effects]]) |

---

## 7. Animation priorities

Roblox `AnimationTrack.Priority` uses the `Enum.AnimationPriority` values **Core, Idle, Movement, Action, Action2, Action3, Action4** (lowest to highest). A higher-priority track overrides lower ones on every joint it keys; joints it does not key fall through to lower-priority tracks. We exploit this for partial-body layering.

| Priority | Used for | Examples | Keys which joints |
|---|---|---|---|
| Core | Safety fallback only | Bind-pose hold loaded on spawn | All |
| Idle | Idle loops and fidgets | ANI-001, ANI-002 | All |
| Movement | Locomotion loops | Walk, run, flap, swim | All |
| Action | Basic attacks, light flinch, emotes, command acknowledgements | ANI-100 to ANI-139 | All, or upper body only for "attack while moving" clips |
| Action2 | Abilities (manual and automatic) | ANI-260 archetypes | All |
| Action3 | Crowd control and heavy reactions | Stagger, knockback, stun loop | All |
| Action4 | Absolute overrides | KO, wild defeat, capture, showcase in hatch and ascension | All |

Rules:
1. A clip's priority is set in the asset and re-asserted in code (`track.Priority = ...`) when loaded, so a mis-exported asset cannot break layering.
2. Locomotion keeps playing under actions. Quadruped attacks key the whole body (they plant to strike), so the animal stops moving for the clip's commit window; the AI mover respects this through the `Rooted` window in configuration ([[Animation - Animal Attacks and Hit Reactions]]).
3. Only one track per priority level may be at full weight on a rig at a time. Starting a new clip at a level stops the previous one with a 0.08 s fade.
4. Standard fade times: Idle and Movement 0.2 s; Action 0.08 s; Action2 0.1 s; Action3 0.05 s; Action4 0.15 s.

---

## 8. Keyframe markers

Markers are `KeyframeMarker` events authored in the Animation Editor and read on the client with `AnimationTrack:GetMarkerReachedSignal(name)`, whose handler receives the marker's `Value` string.

| Marker name | Value format | Meaning | Consumed by |
|---|---|---|---|
| `Hit` | `"<index>"` e.g. `"1"` | Contact frame of a strike | Client: hit spark VFX, impact SFX, camera micro-shake (local player only) |
| `Release` | `"<index>"` | Projectile or beam leaves `A_Mouth` / `A_Strike*` | Client: projectile visual spawn |
| `FootL`, `FootR`, `FootFL`, `FootFR`, `FootHL`, `FootHR` | empty | Foot plant | Client: footstep SFX and dust (Medium size band and up only) |
| `VFX` | VFX asset ID, e.g. `"VFX-006"` | Spawn a cosmetic effect | Client VFX controller |
| `SFX` | SFX asset ID, e.g. `"SFX-231"` | Play a one-shot | Client sound controller |
| `CancelOpen` | empty | From here the clip may be cancelled into the next action | Client input buffer (player only) |
| `Commit` | empty | From here the action can no longer be cancelled | Client input buffer (player only) |
| `LoopStart`, `LoopEnd` | empty | Segment to loop while a server state persists (channels, KO) | Client animation controller |

> [!danger] Authority rule
> Markers are **cosmetic**. The server never waits for a marker and never trusts a client-reported marker time. Every gameplay-relevant time (hit time, release time, invulnerability window) is stored in configuration next to the animation ID and is the value the server uses ([[Implementation - Combat Damage Pipeline]], [[Exploit Prevention]]). The animator's job is to put the `Hit` marker on the same frame the configuration specifies; QA checks that they match (§10).

---

## 9. Runtime setup (illustrative Luau)

```lua
-- Illustrative Luau, not tested in Studio.
local AnimationRegistry = require(ReplicatedStorage.Config.AnimationRegistry)

local function loadClassTracks(model: Model, classCode: string)
	local animator = model.AnimationController.Animator
	local tracks = {}
	for key, entry in AnimationRegistry[classCode] do
		local anim = Instance.new("Animation")
		anim.AnimationId = entry.assetId
		local track = animator:LoadAnimation(anim)
		track.Priority = entry.priority      -- Enum.AnimationPriority.*
		track.Looped = entry.looped
		tracks[key] = track
	end
	return tracks
end

-- Cosmetic hook: hit spark on the authored contact frame
tracks.AttackBasic:GetMarkerReachedSignal("Hit"):Connect(function(value)
	VfxController.burst("VFX-001", model.Chest.A_StrikeR)
end)
```

Animation playback for animals is done **on each client** from replicated state attributes (for example `AnimState = "Attack"`, `AnimSeq = 412`), not by the server calling `Play`. This avoids replicating track state for up to 180 animals and lets each client apply its own distance-based level of detail ([[Animation Bible]] §8, [[Replication Strategy]]). Whether client-played animations on server-owned models behave identically on every device is *unverified* and is a prototype test item (M05).

---

## 10. Validation checklist (rig sign-off)

| # | Check | Method |
|---:|---|---|
| 1 | Root named `HumanoidRootPart`, set as `PrimaryPart` | Studio script `RigLint` (to be written, see [[Luau Coding Standards]]) |
| 2 | Motor6D count within class budget | RigLint |
| 3 | Every Motor6D named `J_<Child>` and inside its child part | RigLint |
| 4 | All §6 attachments present | RigLint |
| 5 | Visual parts non-collidable and non-queryable; one `Hitbox` | RigLint |
| 6 | Class walk cycle plays without foot sliding at authored speed | Visual review |
| 7 | `Hit` marker frame equals configured hit time ±1 frame | Automated test in [[Test Cases - Animal AI]] |
| 8 | Rig renders with all class clips in the Animation Editor | Animator review |

---

## Related documents
- [[Animation Bible]]
- [[Animation and VFX Index]]
- [[Animation - Animal Locomotion]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Animal Modelling Principles]]
- [[Animal Families]]
- [[Animal Roles]]
- [[Animal Scalability and Performance Budgets]]
- [[VFX Bible]]
- [[Asset Naming Conventions]]
- [[Asset Register]]
