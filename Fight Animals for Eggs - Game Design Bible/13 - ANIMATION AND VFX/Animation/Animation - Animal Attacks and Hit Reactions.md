---
title: Animation - Animal Attacks and Hit Reactions
type: asset-spec
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - combat
  - attacks
  - hit-reactions
  - animals
---

# Animation - Animal Attacks and Hit Reactions

Basic attack clips for every role on every rig class, and the four hit-reaction tiers. Used by companions, wild animals and base guards. Abilities are in [[Animation - Animal Abilities]]; knock-outs in [[Animation - Animal Defeat and Victory]].

> [!success] CONFIRMED context
> The player and their animals fight together in real time (D-005). Animals auto-target nearby enemies and accept manual target commands (D-009).

> [!info] PROPOSED
> Timings are derived from the role attack-speed multipliers in [[Canonical Proposed Values]] §3. Frame splits, clip IDs, projectile speed and hit-reaction thresholds are **PROPOSED**.

---

## 1. Role timing templates

The basic attack interval is `1 / AS`. Each role has one timing template; every rig class implements it with its own poses. "Hit time" is the value stored in configuration and used by the server ([[Animal Rig Standards]] §8).

| Role | Role AS | Interval (s) | Clip length (frames @30) | Anticipation | Strike | Contact (`Hit`) | Hit time (s) | Rooted window | Range (studs) |
|---|---:|---:|---:|---|---|---:|---:|---|---:|
| Tank | 0.85 | 1.18 | 35 | f0–13 | f14–16 | **f15** | 0.50 | f0–18 | 5 |
| Bruiser | 0.95 | 1.05 | 32 | f0–9 | f10–12 | **f11** | 0.37 | f0–14 | 5 |
| Assassin | 1.05 | 0.95 | 29 | f0–5 | f6–8 | **f7** | 0.23 | f0–10 | 5 |
| Skirmisher | 1.55 | 0.65 | 19 | f0–3 | f4–5 | **f5** | 0.17 | f0–7 | 5 |
| Ranged | 1.00 | 1.00 | 30 | f0–8 | f9 | **f9** (`Release`) | 0.30 + travel | f0–11 | 28 |
| Support | 1.00 | 1.00 | 30 | f0–10 | f11 | **f11** (`Release`) | 0.37 + travel | f0–13 | 18 |
| Controller | 1.00 | 1.00 | 30 | f0–9 | f10–12 | **f11** | 0.37 | f0–14 | 12 |

- **Rooted window:** the AI mover holds the animal in place for these frames so strikes plant convincingly. After it, the animal may reposition during recovery.
- **Projectiles (PROPOSED):** basic projectiles travel at **70 studs/s** in a straight line; damage is applied by the server at `releaseTime + distance / 70`. At the 28-stud Ranged maximum that is 0.70 s after the attack starts.
- **Species attack speed:** the clip is time-scaled to the species interval with the 0.85–1.20 clamp from [[Animation Bible]] §3.1. Hit time scales with it, and configuration stores the scaled value per species.

### 1.1 Frame-by-frame templates

**Tank (35 f).** f0–5 weight shifts back onto hind legs (or tail, or rear segments), head lowers 15°. f6–13 hold-and-coil: the body compresses 0.15 studs and the front of the body rises (the readable "big hit coming" pose). f14 drives forward. **f15 contact**, 2-frame hit-stop (f15–16 identical). f17–24 push-through and settle, overshooting 0.05 studs. f25–34 ease back into combat idle.

**Bruiser (32 f).** f0–4 head and shoulders pull back 10°. f5–9 front limb or head raised to strike height. f10 snaps forward. **f11 contact**, hit-stop f11–12. f13–20 follow-through (body rotates 10° past the target line). f21–31 recover.

**Assassin (29 f).** f0–5 low crouch, eyes fixed, the shortest tell of any melee role (0.2 s). f6 explosive lunge (visual pelvis forward 0.6 studs by joint pose). **f7 contact**, no hit-stop (assassins feel slick, not heavy). f8–14 spring back (pelvis returns), f15–28 prowling recovery with a slight sidestep that the AI may follow with real movement.

**Skirmisher (19 f, alternating A and B variants).** f0–3 quick hop or wind-up. f4 strike. **f5 contact**. f6–18 bounce away. The AI plays variant A and B alternately so rapid repeats do not look identical.

**Ranged (30 f).** f0–8 draw back: head and chest pull back 12°, `A_Mouth` or `A_StrikeR` charge glow (VFX-009 charge stage) from f3. **f9 `Release`**: the projectile visual spawns on the client. f10–14 recoil 5°, f15–29 return to aim pose.

**Support (30 f).** f0–10 gather: body rises 0.1 studs, a soft glow builds at `A_Chest` (VFX-009 tinted Support green). **f11 `Release`** of a slower, larger orb (same 70 studs/s). f12–29 settle with a small nod.

**Controller (30 f).** f0–9 wind-up with a sideways body coil (the tell is a twist, not a rear-back, so Controllers read differently from Bruisers). f10 strike. **f11 contact** (lunge, tongue, tail whip or kick depending on species). f12–13 hold. f14–29 recover.

---

## 2. Attack clips per rig class

Species-specific pose changes are made as `ANI-1xx/ANM-0xx` variants with unchanged timing ([[Animation Bible]] §2). Ability-specific attacks belong to the [[Animal Abilities Catalogue]], not here.

| ID | Class | Role | Animals using it | Pose language | Status |
|---|---|---|---|---|---|
| ANI-100 | QS | Tank | Hedgehog, Beaver, Crab | Hedgehog: rolls forward into a spiky shoulder bump. Beaver: tail slap down. Crab: claw pinch from both claws | **PROPOSED** |
| ANI-101 | QS | Bruiser | Badger | Forepaw double swipe, then head butt on contact | **PROPOSED** |
| ANI-102 | QS | Assassin | Raccoon, Fox | Low pounce, forepaw swipe at the target's flank | **PROPOSED** |
| ANI-103 | QS | Skirmisher | Rabbit | A: hind-leg kick turning away. B: hop-in head bonk | **PROPOSED** |
| ANI-104 | QS | Ranged | Squirrel | Sits up, throws from forepaws over the head | **PROPOSED** |
| ANI-105 | QS | Support | Meerkat | Upright, chirp gesture releasing a spark orb | **PROPOSED** |
| ANI-106 | QS | Controller | Frog, Arctic Fox | Frog: tongue flick (Jaw open, `A_Mouth` Beam stretch). Arctic Fox: pounce-dive from height into the target | **PROPOSED** |
| ANI-107 | QL | Tank | Brown Bear, Hippo, Elephant, Woolly Mammoth | Rear on hind legs (bear), wide-jaw shove (hippo), forefoot stomp with trunk raise (pachyderms) | **PROPOSED** |
| ANI-108 | QL | Bruiser | Boar, Goat, Wolf, Lion, Rhino | Head-down butt or charge-bite; Lion: forepaw swipe plus bite | **PROPOSED** |
| ANI-109 | QL | Assassin | Leopard, Tiger, Sabre-Tooth Tiger | Crouch-pounce, two-paw swipe, land past the target | **PROPOSED** |
| ANI-110 | QL | Skirmisher | Hyena, Cheetah | Dart in, nip, dart out (A left side, B right side) | **PROPOSED** |
| ANI-111 | QL | Support | Deer, Giant Panda | Deer: antler toss releasing a leaf-light orb. Panda: seated two-paw push | **PROPOSED** |
| ANI-112 | QL | Controller | Zebra, Snow Leopard, Crocodile, Komodo Dragon | Zebra: double hind-leg buck (turns away first). Snow Leopard: tail-whip swipe. Crocodile and Komodo: sideways head swing | **PROPOSED** |
| ANI-113 | BP | Tank | Gorilla | Double-fist ground pound in front of the body | **PROPOSED** |
| ANI-114 | BP | Skirmisher | Monkey | Swinging kick (A) and two-hand slap (B) | **PROPOSED** |
| ANI-115 | BD | Tank | Penguin | Belly bump forward, flippers spread | **PROPOSED** |
| ANI-116 | BD | Skirmisher | Woodpecker, Golden Eagle, Peregrine Falcon, Haast's Eagle | From hover: tuck, dive 1.5 studs (visual), talon or beak strike, climb back | **PROPOSED** |
| ANI-117 | BD | Ranged | Toucan, Quetzalcoatlus | Head pull-back and beak flick releasing a projectile | **PROPOSED** |
| ANI-118 | BD | Support | Duck, Flamingo, Peacock | Wing flourish releasing an orb; Peacock fans the tail on f3–11 | **PROPOSED** |
| ANI-119 | BD | Controller | Owl | Silent wing-sweep from hover, talons forward | **PROPOSED** |
| ANI-120 | SP | Ranged | Cobra, Electric Eel | Cobra: hood flare and spit. Eel: body arc and zap from `A_Mouth` | **PROPOSED** |
| ANI-121 | SP | Controller | Titanoboa | Coil, lunge, body-bump with the front third of the body | **PROPOSED** |
| ANI-122 | AQ | Tank | Walrus | Rears up from hover, tusk-led belly slam | **PROPOSED** |
| ANI-123 | AQ | Bruiser | Megalodon | Wide jaw lunge with a tail kick on recovery | **PROPOSED** |
| ANI-124 | AQ | Assassin | Great White Shark, Mosasaurus | Circle 30° off-line in anticipation, then snap-bite on the turn | **PROPOSED** |
| ANI-125 | AQ | Ranged | Narwhal | Horn point and water-bolt release from `A_Mouth` (horn tip carries the charge glow) | **PROPOSED** |
| ANI-126 | AQ | Support | Dolphin, Blue Whale | Dolphin: flip and click releasing a bubble orb. Blue Whale: slow roll and spout orb | **PROPOSED** |
| ANI-127 | AQ | Controller | Seal, Octopus, Orca, Giant Squid | Seal: flipper slap. Octopus and Squid: two-arm sweep (no grab). Orca: tail slap with spray | **PROPOSED** |
| ANI-128 | PB | Bruiser | Tyrannosaurus Rex, Kangaroo | T-Rex: head-down, jaw snap with a tail swing on recovery. Kangaroo: tail-propped double kick | **PROPOSED** |

IDs ANI-129 to ANI-139 are reserved (for example for an upper-body "attack while moving" set if playtests need one).

### 2.1 Worked example — Tiger basic attack (ANI-109/ANM-034)

[[Tiger]] is an Epic Assassin. Its species AS from the [[Animal Statistics Database]] gives an interval near 0.95 s, so playback speed is close to 1.0.

| Frames | Body | VFX / SFX | Camera |
|---|---|---|---|
| f0–5 | Chest drops 0.3 studs, hind legs coil, tail stiffens straight back | Faint dust at `A_FootHL` (A0 only) | None |
| f6 | Hind legs extend fully; forepaws reach | VFX-019 dash streak Trail on both `A_Strike*` | None |
| f7 `Hit` | Both forepaws cross through the target's chest height | VFX-001 hit spark at target `A_Chest`; SFX-161 claw swipe impact | Local player: none (companions never shake the camera) |
| f8–14 | Lands past the target line, spins 140° to face it | Trail fades over 6 frames | None |
| f15–28 | Low prowl recovery into combat idle | None | None |

Transition: f28 → ANI-030 combat idle (0.2 s fade), or straight into the next ANI-109 if the AI attacks again.

---

## 3. Hit reactions

Four tiers. Which tier plays is decided by the client from the server's damage event and the target's server combat state ([[Combat States and State Machine]]).

| Tier | Trigger (PROPOSED) | Server effect | Priority | Plays when |
|---|---|---|---|---|
| Flinch | Any damage | None (cosmetic) | Action | Only if no Action or Action2 clip is playing; otherwise a Highlight flash only (VFX-032) |
| Stagger | A single hit of ≥ 15% of the target's max HP, or a player combo finisher | None (cosmetic) | Action | Same as flinch: never interrupts an attack or ability |
| Knockback | Server applies a `KnockedBack` state (for example Ground Slam, boss slams, some abilities) | Displacement and action lockout per the source | Action3 | Always |
| Stun | Server applies `Stunned` (Controller effects) | No actions for the stun duration | Action3 | Always; loops for the duration |

> [!info] Why cosmetic reactions never interrupt
> The server keeps executing an animal's attack even if it was hit. If the client played a stagger over the attack, the damage would appear to come from an animal that is visibly reeling. So cosmetic reactions yield to actions, and only server states (knockback, stun) override them.

### 3.1 Hit reaction clips

| Class | Flinch | Stagger | Knockback and get-up | Stun loop |
|---|---|---|---|---|
| QS | ANI-140 | ANI-147 | ANI-154 | ANI-161 |
| QL | ANI-141 | ANI-148 | ANI-155 | ANI-162 |
| BP | ANI-142 | ANI-149 | ANI-156 | ANI-163 |
| BD | ANI-143 | ANI-150 | ANI-157 | ANI-164 |
| SP | ANI-144 | ANI-151 | ANI-158 | ANI-165 |
| AQ | ANI-145 | ANI-152 | ANI-159 | ANI-166 |
| PB | ANI-146 | ANI-153 | ANI-160 | ANI-167 |

All are **PROPOSED**. IDs ANI-168 to ANI-179 are reserved.

### 3.2 Flinch (8 f, 0.27 s)

- **Start pose:** whatever idle or locomotion pose is current (the flinch keys only Spine, Chest, Neck and Head, so legs keep walking underneath).
- f0: no change (the damage number appears this frame).
- f1–2: chest and head snap 10° away from the hit direction (the client picks a front, left or right variant from the hit vector).
- f3–7: ease back over 5 frames with a 2° overshoot.
- **VFX:** VFX-032 white Highlight flash, 0.1 s; VFX-001 on the attacker's side.
- **SFX:** creature hurt vocal SFX from [[Sound - Animal Vocalisations]] (at most one per animal per 0.6 s).

### 3.3 Stagger (15 f, 0.5 s)

- f0–2: whole body pushed back 0.25 studs (by joint pose), head 20° up and away.
- f3–6: one step back on the front legs (quadrupeds) or a stumble on one foot (bipeds); birds lose 0.5 studs of altitude.
- f7–10: head shake (±12° twice).
- f11–14: settle into combat idle.
- **SFX:** SFX-163 heavy impact on f0 and a louder hurt vocal.

### 3.4 Knockback and get-up (QL example, 30 f + get-up 18 f)

Displacement distance and direction are set by the source and applied by the server mover. The clip only provides the body.

| Frames | Pose |
|---|---|
| f0–2 | Body lifts 0.4 studs (visual), legs fold, head thrown back |
| f3–12 | Airborne tumble: one 90° roll onto the side by f12 (never upside down, no limp limbs) |
| f13 | Side contact with ground, dust VFX-025 at `A_Root`, SFX-216 |
| f14–29 | Slide and settle on the side; legs paddle once (f20–24) |
| get-up f0–8 | Roll back upright onto the feet |
| get-up f9–17 | Shake-off (whole body twist ±15°), into combat idle |

If the server's knockback lockout is shorter than 1.6 s, the get-up starts early: `getUpStart = lockout − 0.6 s`, never earlier than f13. Birds in flight tumble in the air and recover altitude instead of landing; AQ animals spin 360° on their long axis and re-level; serpents flip their front third and re-coil.

### 3.5 Stun loop (24 f loop)

- **Entry (6 f):** head droops 15°, eyes switch to the swirl decal (a texture swap on the eye part, see [[Animal Modelling Principles]]).
- **Loop:** body sways in a slow circle (head traces a 0.2-stud circle every 24 frames); legs stay planted.
- **Exit (8 f):** head shake, eyes reset, back to combat idle.
- **VFX:** VFX-014 dizzy stars orbiting `A_Head` for the stun duration.
- **SFX:** SFX-171 stun twinkle loop (one per stunned target, voice-limited).

The swirl-eye look is also used by the KO pose. To keep the KO pose unmistakable, the stun loop keeps the animal **standing**; the KO pose is always **lying down** ([[Animation - Animal Defeat and Victory]]).

---

## 4. Camera behaviour

| Event | Camera |
|---|---|
| Companion basic attacks | None |
| Companion hit reactions | None |
| Local player's companion knocked back by a boss | None (the boss slam already shakes, see [[Animation - Boss Attacks]]) |
| Local player hit | Covered in [[Animation - Player Attacks and Specials]] |

---

## 5. Mobile performance considerations

- Attack clips are loaded per rig on spawn; wild animals of one species share Animation instances but each rig has its own tracks ([[Animal Rig Standards]] §9).
- At LOD A2 (120–200 studs) attacks are replaced with a generic 9-frame lunge, and hit reactions are skipped.
- Highlight flashes (VFX-032) are budgeted ([[VFX Bible]]): beyond the budget the flash falls back to a brief white `PointLight` pulse or is skipped.
- Hurt vocals obey per-animal cooldowns and the Creature SoundGroup voice cap ([[Audio Mixing and Priority]]).

## 6. Test hooks

| Test | Expected |
|---|---|
| Measure `Hit` marker time vs configured hit time for all 29 attack clips at playback speeds 0.85, 1.0 and 1.2 | Within 1 frame (33 ms) |
| Hit an animal mid-attack | Attack completes; Highlight flash only |
| Apply a 0.8 s knockback | Get-up begins at 0.2 s after f13 (clamped), animal can act at 0.8 s |
| 10 animals stunned at once on a low-tier phone | Stun loop and stars run; no more than the voice cap of stun SFX audible |

---

## Related documents
- [[Animation Bible]]
- [[Animal Rig Standards]]
- [[Animation - Animal Locomotion]]
- [[Animation - Animal Abilities]]
- [[Animation - Animal Defeat and Victory]]
- [[Animal Roles]]
- [[Animal Combat Behaviour]]
- [[Combat Feedback and Readability]]
- [[Damage, Defence and Health Model]]
- [[VFX - Combat Effects]]
- [[Sound - Combat Impacts]]
