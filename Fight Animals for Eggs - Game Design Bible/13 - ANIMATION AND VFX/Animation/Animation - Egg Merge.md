---
title: Animation - Egg Merge
type: asset-spec
category: animation
status: mixed
priority: P1
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - eggs
  - merging
  - egg-merging-station
  - base
---

# Animation - Egg Merge

The 3 → 1 egg merge presentation at the Egg Merging Station, how it differs by station level and merge tier, the station idle loops and the station's physical transformation on each upgrade.

> [!success] CONFIRMED
> Three eggs of one rarity make one egg of the next rarity. Merging needs a purchased Egg Merging Station, which must be upgraded before it can merge higher rarities and **physically changes appearance** as it is upgraded. Secret eggs cannot be merged further (D-020).

> [!info] PROPOSED
> Station names, levels, gates and fees are from [[Canonical Proposed Values]] §10 (**PROPOSED**, final costs [[Open Questions#Q-019]]). Merge presentation is 2.5–6 s by tier with no wait timer; timers are the alternative under [[Open Questions#Q-034]]. Frame splits, mechanism designs and IDs here are **PROPOSED**.

---

## 1. Two axes: station level and merge tier

- **Merge tier** sets the **length** of the sequence and the output egg's reveal.
- **Station level** sets the **mechanism** (what the station physically does) and its look. A level 5 station merging Commons uses the level 5 mechanism at the Common→Uncommon length.

The merge outcome is deterministic (always the next rarity), so the output colour may be shown from the start; there is no reveal suspense to protect, and no randomness to disclose.

| Merge tier | Minimum station level | Length (full) | Short (after first viewing) | Status |
|---|---:|---:|---:|---|
| Common → Uncommon | 1 | **2.5 s** (75 f) | 1.2 s | **PROPOSED** |
| Uncommon → Rare | 1 | **3.0 s** (90 f) | 1.3 s | **PROPOSED** |
| Rare → Epic | 2 | **3.5 s** (105 f) | 1.5 s | **PROPOSED** |
| Epic → Legendary | 3 | **4.25 s** (128 f) | 1.8 s | **PROPOSED** |
| Legendary → Mythical | 4 | **5.0 s** (150 f) | 2.1 s | **PROPOSED** |
| Mythical → Secret | 5 | **6.0 s** (180 f) | 2.5 s | **PROPOSED** |

| Station level | Name | Mechanism (PROPOSED) | Palette |
|---:|---|---|---|
| 1 | Twig Nest Press | A woven twig nest; a wooden lever-press closes a leaf lid over the eggs; leaves swirl | Warm wood, moss green |
| 2 | Stonebound Hatchery Forge | Stone basin with bellows; warm glowing runes; a stone hammer stamps three times | Granite, amber glow |
| 3 | Crystal Incubator | A crystal pod; three crystal rings rotate around the eggs; light refracts into rainbows | Ice blue, clear crystal |
| 4 | Aurora Crucible | A floating crucible; eggs orbit it inside aurora ribbons, then drop in | Teal, violet, aurora green |
| 5 | Celestial Convergence Altar | Star altar; constellation lines connect the eggs; a celestial beam fuses them | Night blue, starlight gold |

---

## 2. Asset table

| ID | Clip / sequence | Length | Status |
|---|---|---|---|
| ANI-460 | Insert: three eggs fly from storage to the station's input slots | 0.6 s | **PROPOSED** |
| ANI-461 | Merge sequence Common → Uncommon | 2.5 s | **PROPOSED** |
| ANI-462 | Merge sequence Uncommon → Rare | 3.0 s | **PROPOSED** |
| ANI-463 | Merge sequence Rare → Epic | 3.5 s | **PROPOSED** |
| ANI-464 | Merge sequence Epic → Legendary | 4.25 s | **PROPOSED** |
| ANI-465 | Merge sequence Legendary → Mythical | 5.0 s | **PROPOSED** |
| ANI-466 | Merge sequence Mythical → Secret | 6.0 s | **PROPOSED** |
| ANI-467 | Output emerge and flight to base storage | 0.8 s (inside the sequence length) | **PROPOSED** |
| ANI-468 to ANI-472 | Station idle loops, levels 1–5 | 4.0–6.0 s loops | **PROPOSED** |
| ANI-473 to ANI-476 | Station upgrade transformations L1→L2, L2→L3, L3→L4, L4→L5 | 3.0 s each | **PROPOSED** |
| ANI-477 | Merge refused (wrong count, mixed rarities, station level too low, Secret selected) | 0.5 s | **PROPOSED** |
| ANI-478 | Station first build (purchase) reveal | 3.0 s | **PROPOSED** |

ANI-479 is reserved. Each station level is a separate prop rig (`MOD`-series model in [[Base Art Direction]]) with its own `AnimationController`; the merge sequences ANI-461 to ANI-466 are **controllers** that time the level's mechanism clips (`ANI-46x/L<level>` variants) to the tier length.

---

## 3. Phase structure

| Phase | C→U (75 f) | U→R (90 f) | R→E (105 f) | E→L (128 f) | L→M (150 f) | M→S (180 f) |
|---|---|---|---|---|---|---|
| 1 Insert (ANI-460) | f0–17 | f0–17 | f0–17 | f0–17 | f0–17 | f0–17 |
| 2 Process (mechanism) | f18–44 | f18–56 | f18–68 | f18–86 | f18–104 | f18–128 |
| 3 Fuse (flash) | f45–50 | f57–62 | f69–75 | f87–94 | f105–113 | f129–140 |
| 4 Emerge (output reveal) | f51–62 | f63–77 | f76–91 | f95–112 | f114–134 | f141–164 |
| 5 Store (flight) | f63–74 | f78–89 | f92–104 | f113–127 | f135–149 | f165–179 |

---

## 4. Frame-by-frame examples

### 4.1 Common → Uncommon at a level 1 Twig Nest Press (75 f, 2.5 s)

| Frames | Station | Eggs | VFX | SFX | Camera |
|---|---|---|---|---|---|
| f0–17 | Nest rustles open (lid lifts 30°) | Three Common eggs arc in from the HUD storage icon, landing in the nest at f8, f11, f14 | Grey trails | SFX-350 insert ticks ×3 | Scriptable 14 studs, 20° elevation, FOV 50 (blend 0.3 s) |
| f18–29 | Lever pulls down; leaf lid closes over the eggs (lid fully closed f26) | Hidden | Leaf swirl VFX-320 intensifies | SFX-351 L1 mechanism (creak, rustle) | Hold |
| f30–44 | Nest rocks ±5° twice; light leaks through gaps | Hidden | Grey light leaks shifting to green at f38 | Rhythmic creak | Push-in 1 stud |
| f45–50 | Lid bursts open | — | VFX-327 fusion flash (green) | SFX-356 fusion | Hold |
| f51–62 | — | One Uncommon egg rises from the nest, spins once, settles | VFX-328 emerge, green sparks | SFX-357 emerge + Uncommon tier layer (hatch layer reused at −3 dB) | Hold |
| f63–74 | Lid resets | Egg flies to base storage (ANI-467 arc) | Trail | SFX-332 storage arrival | Blend out from f68 |

### 4.2 Mythical → Secret at a level 5 Celestial Convergence Altar (180 f, 6.0 s)

| Frames | Station | Eggs | VFX | SFX | Camera |
|---|---|---|---|---|---|
| f0–17 | Altar's star dial wakes; local lighting dims 20% | Three Mythical eggs float in onto three star points | Magenta trails | SFX-350 ×3 | Blend in, 16 studs, FOV 55 |
| f18–47 | Constellation lines (Beams) draw between the three eggs, forming a triangle | Eggs rise 1 stud and begin orbiting the altar centre | VFX-324 starfield idle intensifies | SFX-355 L5 mechanism (celestial chime bed) | Slow orbit 15° |
| f48–89 | Dial rotates 120°, then another 120° | Orbit accelerates; eggs pulse in sequence | Starlight motes | Chimes rise in pitch every 14 frames | Push-in to 12 studs |
| f90–128 | Celestial beam descends from above onto the altar centre | Eggs spiral into the beam and vanish one by one (f100, f112, f124) | Beam widens; scene fades towards night `#1B1B2F` (the output is known to be Secret, so this cue is honest) | Swell | Hold |
| f129–140 | Beam collapses to a point | — | VFX-327 fusion flash (prismatic) | SFX-356 fusion (long) | "Light" shake (none with reduce motion) |
| f141–164 | Altar opens | Secret egg descends out of the point, rotating; prismatic shimmer | VFX-328 + VFX-161 prismatic module | SFX-357 + Secret tier layer; MUS-37 Secret stinger (merge edit) | Slow pull-out |
| f165–179 | Dial resets; lighting returns | Egg flies to base storage | Trail | SFX-332 | Blend out |

### 4.3 Mechanism beats per level (process phase)

| Level | Beat pattern within the process phase |
|---:|---|
| 1 | Lid closes at 30% of the phase; two rocks at 50% and 75% |
| 2 | Bellows pump at 0%, 25%, 50%; hammer stamps at 60%, 75%, 90% (each stamp: 3-frame strike, 2-frame hold) |
| 3 | Rings start rotating at 0%; speed doubles at 50%; rainbow refraction peaks at 90% |
| 4 | Eggs orbit from 0%; aurora ribbons wrap at 40%; eggs drop into the crucible at 70%, 80%, 90% |
| 5 | Lines draw at 0–25%; dial turns at 25–60%; beam descends at 60–100% |

Because the beats are percentages, every level fits every tier length it can perform.

---

## 5. Station idle loops (ANI-468 to ANI-472)

| ID | Level | Loop | Motion |
|---|---:|---|---|
| ANI-468 | 1 | 4.0 s | Nest lid breathes 2°; one leaf falls every loop |
| ANI-469 | 2 | 4.0 s | Bellows rest; rune glow pulses; occasional spark at 2.5 s |
| ANI-470 | 3 | 5.0 s | Rings turn at 10°/s; crystal shimmer |
| ANI-471 | 4 | 5.0 s | Crucible floats ±0.2 studs; aurora ribbons drift |
| ANI-472 | 5 | 6.0 s | Dial turns slowly; star motes rise; constellation flickers |

Idle loops stop animating (hold last pose) when the camera is more than 60 studs away, and run only while the base is streamed in.

---

## 6. Station upgrade transformations (ANI-473 to ANI-476)

Each upgrade physically rebuilds the station (D-020). 3.0 s (90 f), in place:

| Frames | Beat |
|---|---|
| f0–14 | Current station glows and lifts 0.5 studs; construction sparkles VFX-330 |
| f15–29 | Station parts separate and spin outward (parts animated by the old rig) |
| f30–44 | Flash VFX-325; the old model is swapped for the new level's model, parts collapsed at the centre |
| f45–74 | New parts fly into place in three waves (base, body, crown), each wave with a landing tick |
| f75–89 | New idle loop starts; level banner in [[UI - Base Upgrades]] |

SFX-358. Camera: if the player triggered the upgrade from the station, the same Scriptable framing as a merge is used; if triggered from the base menu elsewhere, no camera change and the sequence plays in the background. See [[Animation - Base Upgrades]] for the module upgrade grammar this follows.

---

## 7. Refusal (ANI-477)

The station rejects the eggs: the input slots shake twice and the eggs bounce back to storage (0.5 s), SFX-359. Causes include fewer than three eggs, mixed rarities, a station level too low for the tier, or a Secret egg selected (no rarity above Secret). The UI states the cause ([[UI - Egg Merging]]).

## 8. Mobile performance considerations

- One station per base; idle loop keys are sparse (≤ 1 key per joint per 6 frames).
- Level 4 and 5 Beams: 3 Beams at low quality, 6 at high.
- Lighting dim in the L5 sequence uses a `ColorCorrectionEffect` on low quality instead of changing `Lighting` properties.
- The merge camera is skipped if the player is in combat-tagged state (merging is a base activity and should not happen in combat, but the guard is cheap).

## 9. Test hooks

| Test | Expected |
|---|---|
| All six tiers on a level 5 station | Lengths 2.5 / 3.0 / 3.5 / 4.25 / 5.0 / 6.0 s; L5 mechanism beats at the percentages in §4.3 |
| Rare → Epic on a level 1 station | Refused (ANI-477) |
| Merge with a full base storage | Allowed: capacity frees by two because three eggs leave and one enters ([[Egg Storage]]) |
| Upgrade the station during an active raid on the base | Behaviour follows [[Base Upgrade System]]; animation plays only if the upgrade is accepted |

---

## Related documents
- [[Egg Merging]]
- [[Egg Merging Station]]
- [[UI - Egg Merging]]
- [[Implementation - Egg Merge Transaction]]
- [[Animation - Base Upgrades]]
- [[Animation - Egg Roll]]
- [[Base Art Direction]]
- [[VFX Bible]]
- [[Sound - Eggs]]
