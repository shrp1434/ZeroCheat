---
title: Animation - Base Upgrades
type: asset-spec
category: animation
status: mixed
priority: P1
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - base
  - upgrades
  - modules
  - defence
---

# Animation - Base Upgrades

Construction and level-up animation for every base module, plot expansion, module idle loops and the physical defence props (turrets, barricades, traps) that the Defence Station adds.

> [!success] CONFIRMED
> Every player has a modular base and each section is upgraded separately (D-022). Bases are protected by shields and physical defences (D-024).

> [!info] PROPOSED
> Module list and levels L1–L5 come from [[Canonical Proposed Values]] §12 (availability **UNDECIDED**, [[Open Questions#Q-007]]). Whether upgrades are instant or timed belongs to [[Base Upgrade System]]; this document supports both through a construction loop. Durations, frame splits and IDs are **PROPOSED**. Module appearance per level is owned by [[Base Art Direction]].

---

## 1. Upgrade grammar

Every module upgrade uses the same five beats so players learn them once:

| Beat | Purpose | Visual |
|---|---|---|
| 1 Mark | Shows which module is changing | Ground ring in Cash gold around the module footprint |
| 2 Scaffold | "Work is happening" | Low-poly scaffolding and crates pop up around the module |
| 3 Build | Rhythm of construction | Hammer-strike flashes and dust puffs on a beat; in timed upgrades this beat loops |
| 4 Reveal | The new level appears | Scaffolding drops away; new model swapped in under a burst |
| 5 Show-off | Reward | Level trim glows, banner in [[UI - Base Upgrades]] |

| Level | Length (full) | Short (after first viewing of that level) | Hammer beats | Status |
|---|---:|---:|---:|---|
| L1 construction | **2.4 s** (72 f) | 1.2 s | 3 | **PROPOSED** |
| L2 | **2.8 s** (84 f) | 1.2 s | 3 | **PROPOSED** |
| L3 | **3.2 s** (96 f) | 1.4 s | 4 | **PROPOSED** |
| L4 | **3.6 s** (108 f) | 1.5 s | 4 | **PROPOSED** |
| L5 (max) | **4.0 s** (120 f) | 1.6 s | 5 | **PROPOSED** |

---

## 2. Asset table

| ID | Clip / sequence | Length | Status |
|---|---|---|---|
| ANI-480 | Construction (L1) sequence controller, with `LoopStart`/`LoopEnd` around the build beat for timed builds | 2.4 s + loop | **PROPOSED** |
| ANI-481 | Upgrade to L2 | 2.8 s | **PROPOSED** |
| ANI-482 | Upgrade to L3 | 3.2 s | **PROPOSED** |
| ANI-483 | Upgrade to L4 | 3.6 s | **PROPOSED** |
| ANI-484 | Upgrade to L5 | 4.0 s | **PROPOSED** |
| ANI-485 | Idle loop — [[Module - Animal Pens]] (gate sway, water trough ripple) | 5.0 s | **PROPOSED** |
| ANI-486 | Idle loop — [[Module - Egg Vault]] (vault door seal pulse, egg racks glint) | 4.0 s | **PROPOSED** |
| ANI-487 | Idle loop — [[Module - Defence Station]] (lookout flag, turret scan) | 4.0 s | **PROPOSED** |
| ANI-488 | Idle loop — [[Module - Shield Generator]] (rotor spin, see [[Animation - Shield Activation]]) | 3.0 s | **PROPOSED** |
| ANI-489 | Idle loop — [[Module - Training Grounds]] (punching post wobble, dummy spin) | 4.0 s | **PROPOSED** |
| ANI-490 | Idle loop — [[Module - Multiplier Shrine]] (coin motes orbit) | 6.0 s | **PROPOSED** |
| ANI-491 | Idle loop — [[Module - Trophy Hall]] (banner sway, trophy pedestal light) | 6.0 s | **PROPOSED** |
| ANI-492 | Plot expansion (fence and ground extend) | 3.0 s | **PROPOSED** |
| ANI-493 | Upgrade refused (insufficient Cash, prerequisites, raid in progress) | 0.5 s | **PROPOSED** |
| ANI-494 | Turret idle scan, acquire and fire set | 4.0 s loop; 0.3 s acquire; 0.5 s fire | **PROPOSED** |
| ANI-495 | Barricade raise and lower | 0.8 s / 0.6 s | **PROPOSED** |
| ANI-496 | Trap arm and trigger | 0.4 s / 0.6 s | **PROPOSED** |
| ANI-497 | Trophy placement (a boss trophy appears on a pedestal) | 2.0 s | **PROPOSED** |

ANI-498 and ANI-499 are reserved. The [[Egg Merging Station]] has its own transformations in [[Animation - Egg Merge]].

---

## 3. Frame-by-frame examples

### 3.1 L2 upgrade (ANI-481, 84 f, 2.8 s)

| Frames | Beat | Module | VFX | SFX | Camera |
|---|---|---|---|---|---|
| f0–8 | Mark | Module glows faintly | Gold ground ring draws around the footprint (VFX-330 ring stage) | SFX-440 construction start | Optional spotlight framing (§4) |
| f9–20 | Scaffold | Scaffold poles rise from the ground (3 waves at f9, f13, f17), two crates drop in (f15, f19) | Dust puffs per wave | Wood clunks (SFX-442 one-shot variants) | Hold |
| f21–50 | Build | Hammer flashes at f24, f34, f44 (each: 2-frame white flash on a random scaffold node, 6-frame dust) | VFX-330 sparkles | SFX-441 hammer hit (four variations, no repeats in a row) | Hold |
| f51–56 | Reveal | Scaffold collapses outward and fades; old model swapped for the L2 model at f53 under the flash | VFX-331 complete burst | Whoosh | Micro push-in 0.5 stud |
| f57–70 | Reveal | New parts settle with a 3% overshoot (parts animated on the module rig) | Debris settles | | Hold |
| f71–83 | Show-off | Level trim lights up from the base to the top over 12 frames | VFX-332 level trim glow | SFX-444 L2 complete layer | Blend out from f76 |

### 3.2 L5 upgrade (ANI-484, 120 f, 4.0 s)

| Frames | Beat | Detail |
|---|---|---|
| f0–11 | Mark | Gold ring draws, then a second ring; module lifts 0.2 studs |
| f12–29 | Scaffold | Taller, golden scaffolding in 4 waves |
| f30–79 | Build | Five hammer beats at f33, f43, f53, f63, f73, the last one larger (VFX-331 mini-burst) |
| f80–89 | Reveal | Scaffold bursts into gold sparks; L5 model swaps at f84 under a light pillar |
| f90–104 | Reveal | Crown or roof piece descends onto the module (the L5 signature detail from [[Base Art Direction]]), lands f100 with dust |
| f105–119 | Show-off | Full trim glow, small confetti VFX-037, SFX-447 L5 complete fanfare layer |

### 3.3 Timed upgrades (if [[Base Upgrade System]] uses build timers)

The controller plays beats 1–2, then loops the build beat (30 f loop, one hammer beat per loop) until the server marks the upgrade complete, then plays beats 4–5. While looping, hammer beats are reduced to one every 2 s and their sound is quiet (−12 dB) so a base with several builds is not noisy. A floating progress sign above the module shows the remaining time (UI element, not animated geometry).

---

## 4. Camera behaviour

| Situation | Camera |
|---|---|
| Player at the module (within 40 studs) and not combat-tagged, upgrade started from the module prompt | "Spotlight" framing: Scriptable camera 0.3 s blend to a 3/4 view at 2.5 × the module height, holds for the sequence, blends back 0.4 s. Skippable by moving the thumbstick or pressing any movement key ([[Camera Behaviour Guidelines]]) |
| Upgrade started from the base menu elsewhere | No camera change; sequence plays where the module is |
| A raid is in progress at the base | Upgrades are refused by the server or allowed per [[Base Upgrade System]]; never a camera takeover during a raid |
| Visitors or raiders watching | No camera change for them |

---

## 5. Defence props

### 5.1 ANI-494 Turret set

Turrets are friendly-looking contraptions (berry launchers, bubble blowers, net throwers) in keeping with the art direction; never realistic guns ([[Base Art Direction]]).

| Clip | Frames (@30) | Motion |
|---|---|---|
| Idle scan (120 f loop) | f0–59 rotate +45°, f60–119 rotate back; head bobs | Slow, readable |
| Acquire (9 f) | Snaps to target over 4 frames, 2-frame overshoot, settle | Tells the raider "you are being targeted" |
| Fire (15 f) | f0–1 compress, **f2 `Release`**, f3–6 recoil, f7–14 return | Projectile VFX-333 muzzle puff |
| Cooldown | Holds facing until the next shot (rate from [[Base Defence Overview]]) | |

### 5.2 ANI-495 Barricade

Raise (24 f): f0–5 ground cracks open (decal), f6–17 barricade rises with a 0.2-stud overshoot at f15, f18–23 settles with dust VFX-335. Lower (18 f): reverse, faster.

### 5.3 ANI-496 Trap

Arm (12 f): trap pad sinks flush with the ground and its rim light turns on. Trigger (18 f): f0–2 snap, f3 effect (sticky slow puddle or net pop, VFX-334), f4–17 reset. Effects follow [[Base Defence Overview]]; the animation never implies harm beyond slowing or holding.

---

## 6. Plot expansion (ANI-492, 90 f)

f0–14 fence posts at the new boundary glow; f15–44 ground tiles unfold outward in a wave from the old edge (terrain reveal via `Part` panels, not terrain writes); f45–74 fence segments hop to the new boundary one by one; f75–89 new empty module slots show a pulsing build marker. SFX-448.

## 7. Trophy placement (ANI-497, 60 f)

f0–19 pedestal light turns on, f20–39 trophy (a miniature of the boss) descends rotating, f40–49 lands with a ring of light, f50–59 banner unfurls. SFX-454. Trophy Cash bonus feedback is UI only ([[Module - Trophy Hall]]).

## 8. Mobile performance considerations

| Item | Rule |
|---|---|
| Module idle loops | Play only for modules within 60 studs of the camera; beyond that, hold pose |
| Visiting other bases | Idle loops at A1 (reduced) for every base except the player's own |
| Scaffolding | Pooled prop set (one per client) reused for every upgrade |
| Turrets | Idle scan only while a raid is active or the camera is within 40 studs |
| Highlight use | None; trim glow uses `Neon` material swaps, not Highlights |

## 9. Test hooks

| Test | Expected |
|---|---|
| Upgrade each module L1 → L5 | Five distinct beats; lengths 2.4 / 2.8 / 3.2 / 3.6 / 4.0 s |
| Two upgrades started 0.5 s apart | Both play; only the first takes the camera |
| Timed build (if enabled) left for 10 minutes | Build loop continues quietly; no audio fatigue (−12 dB, 2 s beat) |
| Upgrade refused | ANI-493 shake, SFX-449, no model change |

---

## Related documents
- [[Base Upgrade System]]
- [[Player Base System]]
- [[Base Art Direction]]
- [[Base Defence Overview]]
- [[UI - Base Upgrades]]
- [[Animation - Egg Merge]]
- [[Animation - Shield Activation]]
- [[VFX Bible]]
- [[Sound - Base and Raid Alerts]]
