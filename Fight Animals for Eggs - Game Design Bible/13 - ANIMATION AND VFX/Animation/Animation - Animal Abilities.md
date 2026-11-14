---
title: Animation - Animal Abilities
type: asset-spec
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - abilities
  - combat
  - archetypes
  - animals
---

# Animation - Animal Abilities

Animation archetypes for animal abilities. Every ability in the [[Animal Abilities Catalogue]] is assigned one archetype; the archetype fixes timing, phases, markers and presentation, and the species variant supplies poses.

> [!success] CONFIRMED
> Animal abilities can be manually or automatically activated, and both kinds exist (D-008).

> [!info] PROPOSED
> Archetypes, durations and frame splits are **PROPOSED**. Ability numbers (damage, radius, duration, cooldown) belong to the [[Animal Abilities Catalogue]] and [[Abilities and Cooldowns]]; this document never sets them. The global cooldown between manual animal abilities is 0.5 s ([[Canonical Proposed Values]] §4).

---

## 1. How archetypes are used

1. The catalogue entry for an ability names its archetype (for example "AoE Slam") and its gameplay parameters.
2. The variant clip is produced as `ANI-<archetype>/ANM-<animal>`, for example `ANI-263/ANM-044` for an [[Elephant]] stomp. Timing must match the archetype table exactly; only poses change.
3. The cast time (the moment the server applies the effect) is the archetype's `Hit`, `Release` or `Cast` frame, scaled by the same playback-speed rule as basic attacks only if the catalogue says the ability scales with attack speed (default: it does not).
4. Variable-length archetypes (channels, charges, guards) use `LoopStart` / `LoopEnd` markers. The client loops that segment while the server state persists.

### 1.1 Manual versus automatic presentation

| | Manual ability | Automatic ability |
|---|---|---|
| Who triggers | Player via [[UI - Animal Team Display]] or a key | Animal AI ([[Animal Combat Behaviour]]) |
| Clip | Same archetype clip | Same archetype clip |
| Extra feedback | **Command ring** VFX-030 (player colour) at `A_Root` for 0.25 s on start, plus SFX-158 command whistle, so the player sees the order was obeyed | None beyond the clip |
| Latency handling | The command ring plays immediately on input; the clip starts when the server state arrives | Clip starts with server state |
| Priority | `Action2` | `Action2` |

### 1.2 Wild animal versions

Wild animals use the same archetypes. Because players must be able to react, any wild-cast archetype that hits an area also shows a ground telegraph decal (VFX-040 circle, VFX-041 line or VFX-042 cone, scaled down from the boss versions) from the first frame of anticipation, and the wild anticipation is lengthened by **+0.3 s** (a slower variant of the same clip, played at speed `anticipationFrames / (anticipationFrames + 9)` during the anticipation segment only).

---

## 2. Archetype table

| ID | Archetype | Typical roles | Length @30 | Cast frame | Variable segment | Priority | Status |
|---|---|---|---|---|---|---|---|
| ANI-260 | Dash Strike | Assassin, Skirmisher | 24 f (0.8 s) | `Hit` f12 | — | Action2 | **PROPOSED** |
| ANI-261 | Pounce | Assassin, Bruiser | 30 f (1.0 s) | `Hit` f20 | — | Action2 | **PROPOSED** |
| ANI-262 | Charge | Tank, Bruiser | 15 f tell + loop + 9 f | `Hit` on impact | Charge run loop | Action2 | **PROPOSED** |
| ANI-263 | AoE Slam / Stomp | Tank, Bruiser, Controller | 36 f (1.2 s) | `Hit` f20 | — | Action2 | **PROPOSED** |
| ANI-264 | Projectile Volley | Ranged | 36 f (1.2 s) | `Release` f9, f15, f21 | — | Action2 | **PROPOSED** |
| ANI-265 | Channel Beam | Ranged, Support | 12 f in + loop + 9 f out | `Release` f12 | Beam loop | Action2 | **PROPOSED** |
| ANI-266 | Cone Breath / Spray | Ranged, Controller | 15 f in + loop + 9 f out | `Release` f15 | Spray loop | Action2 | **PROPOSED** |
| ANI-267 | Heal Pulse | Support | 30 f (1.0 s) | `Cast` f12 | — | Action2 | **PROPOSED** |
| ANI-268 | Buff Call (howl, roar, song, display) | Support, Bruiser | 36 f (1.2 s) | `Cast` f10 | — | Action2 | **PROPOSED** |
| ANI-269 | Guard / Shell Up | Tank | 9 f in + loop + 9 f out | `Cast` f9 | Guard hold | Action2 | **PROPOSED** |
| ANI-270 | Taunt | Tank | 24 f (0.8 s) | `Cast` f12 | — | Action2 | **PROPOSED** |
| ANI-271 | Stun Burst | Controller | 27 f (0.9 s) | `Hit` f14 | — | Action2 | **PROPOSED** |
| ANI-272 | Tether Pull | Controller | 30 f (1.0 s) | `Release` f10, pull f10–19 | — | Action2 | **PROPOSED** |
| ANI-273 | Zone Placement (slow field, trap) | Controller, Support | 27 f (0.9 s) | `Cast` f13 | — | Action2 | **PROPOSED** |
| ANI-274 | Call (decoy or helper) | Support, Controller | 36 f (1.2 s) | `Cast` f18 | — | Action2 | **PROPOSED** |
| ANI-275 | Burrow / Submerge Reposition | Skirmisher, Assassin | 15 f out + hidden + 15 f in | `Hit` on emerge f6 (optional) | Hidden travel | Action2 | **PROPOSED** |
| ANI-276 | Leap Reposition (evade) | Skirmisher | 21 f (0.7 s) | — | — | Action2 | **PROPOSED** |
| ANI-277 | Passive Proc Flourish | Any (automatic passives) | 9 f (0.3 s), upper body | `Cast` f3 | — | Action | **PROPOSED** |

IDs ANI-278 to ANI-299 are reserved for new archetypes; ANI-300 to ANI-319 for wild-only elite variants. Per-animal variants use the compound `ANI-2xx/ANM-0xx` form and do not consume new numbers.

---

## 3. Archetype specifications

Each block gives: start pose → sequence → end pose, movement, camera, VFX, sound, transitions and mobile notes. Frames are @30.

### 3.1 ANI-260 Dash Strike (24 f)

- **Start:** combat idle facing the target.
- f0–7: low crouch, body pulled back 0.2 studs, eyes locked (tell 0.27 s).
- f8–13: dash; the server moves the animal along a straight line to the target (distance from the catalogue). Body stretched long, legs extended.
- **f12 `Hit`:** passes through or stops at the target.
- f14–23: skid to a stop (2 frames of dust), turn back towards the target.
- **End:** combat idle.
- **VFX:** VFX-019 dash streak Trail f8–13; VFX-001 or VFX-002 on contact.
- **SFX:** SFX-230 dash whoosh at f8, impact from [[Sound - Combat Impacts]].
- **Camera:** none.
- **Mobile:** Trail lifetime 0.25 s; disabled for other players' animals at low quality.

### 3.2 ANI-261 Pounce (30 f)

- f0–9: coil (pelvis −0.3 studs), tail stiff, a 0.33 s tell.
- f10–19: airborne arc. The clip lifts the body to 1.5 studs at f15 via `Pelvis`; the server moves the root to the landing point over the same 10 frames.
- **f20 `Hit`:** lands on the target position, forepaws first. Hit-stop f20–21.
- f22–29: rebound and turn.
- **VFX:** VFX-025 landing dust ring at f20.
- **SFX:** SFX-231 leap whoosh f10; landing impact f20.

### 3.3 ANI-262 Charge

| Segment | Frames | Pose |
|---|---|---|
| Tell | f0–14 (0.5 s) | Front foot scrapes twice (f3, f9), head lowered, snort puff from `A_Mouth` at f9 |
| `LoopStart` | f15 | Charge run loop (class run cycle exaggerated: head down, horns or tusks forward) |
| Loop | f15–30 | Repeats while the server charge state lasts (distance / charge speed) |
| `LoopEnd` → impact | f31 | **`Hit`** on collision with the first target, or a skid if nothing is hit |
| Recovery | f32–40 | Head shake, back to combat idle |

- **VFX:** VFX-020 dust trail at the feet during the loop; for wild casters a line telegraph VFX-041 along the charge path during the tell.
- **SFX:** SFX-232 snort at f9, footfall loop, SFX-163 heavy impact.
- **Camera:** none for companions. A wild charge that hits the local player triggers the player's knockdown shake.

### 3.4 ANI-263 AoE Slam / Stomp (36 f)

| Frames | Pose |
|---|---|
| f0–8 | Rise: quadrupeds rear onto hind legs (pachyderms lift both front feet 1 stud), bipeds raise both arms |
| f9–17 | Peak hold (0.3 s): the readable tell |
| f18–19 | Drop |
| **f20** | **`Hit`**: impact; hit-stop f20–22 |
| f23–35 | Settle, shoulders heave once |

- **VFX:** VFX-023 impact ring sized to the catalogue radius; debris chunks only at medium and high quality.
- **SFX:** SFX-233 stomp, scaled by size band (Tiny animals play a lighter layer).
- **Camera:** none for companions. If the caster is a wild animal within 15 studs of the local player, "Light" shake.

### 3.5 ANI-264 Projectile Volley (36 f)

- f0–8: draw back, charge glow at `A_Mouth`.
- **f9, f15, f21 `Release`** "1", "2", "3": three projectiles. Each release is a 3-frame recoil (head snaps back 6°).
- f22–35: recover to aim pose.
- If the catalogue specifies a different projectile count, the variant clip adds or removes 6-frame release beats and the archetype length changes by 6 frames per beat.
- **VFX:** VFX-009 projectiles; impacts VFX-010.
- **SFX:** SFX-166 launch per release with ±6% pitch variation.

### 3.6 ANI-265 Channel Beam

- **In (12 f):** plant, head forward, charge glow.
- **`Release` f12 and `LoopStart`:** Beam VFX-022 from `A_Mouth` (or horn, beak) to the target's `A_Chest`.
- **Loop (24 f):** body trembles ±1°, head tracks the target (Neck yaw follows, capped at 45° before the whole body turns).
- **`LoopEnd` → Out (9 f):** beam cut, recoil, recover.
- **SFX:** SFX-234 channel hum loop (one per caster, voice-limited), start and stop tails.
- **Mobile:** one Beam per caster; Beam `Segments` 8 at low, 16 at high.

### 3.7 ANI-266 Cone Breath / Spray

- **In (15 f):** inhale; chest expands (Chest pitch up 8°), head pulls back.
- **`Release` f15:** cone VFX-021 (tinted by the ability's element: water, frost, wind, spark, petals; never fire-on-animals imagery that reads as burning creatures).
- **Loop (18 f):** head sweeps ±10° across the cone.
- **Out (9 f):** mouth closes, small cough-shake.
- **Wild casters:** cone telegraph VFX-042 during the inhale (+0.3 s).

### 3.8 ANI-267 Heal Pulse (30 f)

- f0–11: gather: body rises 0.1 studs, eyes close, glow builds at `A_Chest`.
- **f12 `Cast`:** pulse ring (VFX-011) expands from `A_Root`; healed allies show VFX-012 motes.
- f13–29: open eyes, gentle settle.
- **SFX:** SFX-235 heal chime (major third, soft attack).

### 3.9 ANI-268 Buff Call (36 f)

- f0–9: inhale, chest rises; wolves and canines lift the head, primates beat the chest (f4, f7), birds fan wings or tail (Peacock fan).
- **f10 `Cast`:** buff ring VFX-013 on allies.
- f10–27: hold the call pose (howl, roar, song).
- f28–35: settle.
- **SFX:** species call from [[Sound - Animal Vocalisations]] layered with SFX-236 buff shimmer.

### 3.10 ANI-269 Guard / Shell Up

- **In (9 f):** Hedgehog curls into a ball; Crab raises both claws in front of its face; Penguin and Walrus brace with lowered heads; large QL plant feet wide and lower head.
- **`Cast` f9 / `LoopStart`:** VFX-017 guard bubble or shimmer on the body.
- **Loop (30 f):** slight breathing; hits during the loop play a 3-frame shudder instead of a flinch.
- **Out (9 f):** uncurl or lower guard.
- **SFX:** SFX-237 guard up, SFX-176 hit-on-guard tink during the loop.

### 3.11 ANI-270 Taunt (24 f)

f0–5 chest out, f6–11 stomp or chest beat, **f12 `Cast`** taunt ring VFX-018, f12–17 roar pose, f18–23 settle. SFX-238.

### 3.12 ANI-271 Stun Burst (27 f)

f0–13 coil and charge (sparks gather), **f14 `Hit`** burst (VFX-023 tinted Controller teal), f15–26 recover. Stunned targets switch to their stun loop ([[Animation - Animal Attacks and Hit Reactions]]). SFX-239.

### 3.13 ANI-272 Tether Pull (30 f)

- f0–9: aim (head forward, body low).
- **f10 `Release`:** tether Beam VFX-016 reaches the target (tongue for [[Frog]], vine or water rope for others; never a hook or chain).
- f10–19: reel: head and chest pull back while the server displaces the target towards the caster.
- f20–29: tether snaps, recover.
- SFX-240 tether zip and snap.

### 3.14 ANI-273 Zone Placement (27 f)

f0–12 wind-up (spit, stomp or wing beat), **f13 `Cast`**: zone decal VFX-015 appears at the target point and stays for the zone's duration; f14–26 recover. SFX-241.

### 3.15 ANI-274 Call (36 f)

f0–17 call pose (head raised, mouth open), **f18 `Cast`**: VFX-026 call ring at the spawn point; any helper uses its own class locomotion; f19–35 settle. If the catalogue contains no call or decoy ability at launch, this archetype is not produced.

### 3.16 ANI-275 Burrow / Submerge Reposition

- **Out (15 f):** dig or dive pose; f9 VFX-024 puff (earth for land animals, a water ripple decal for AQ air-swimmers); f12 rig hidden.
- **Hidden travel:** the server moves the hidden animal; a moving ground ripple VFX-024 follows it so opponents can track it.
- **In (15 f):** f0 rig shown below ground level (-1 stud), f0–5 burst out, **f6 optional `Hit`** if the ability damages on emerge, f7–14 shake-off.

### 3.17 ANI-276 Leap Reposition (21 f)

f0–5 crouch, f6–15 arc (1.2 studs visual height), f16 land, f17–20 recover. VFX-025 landing dust. Used for evasive abilities; no damage frame.

### 3.18 ANI-277 Passive Proc Flourish (9 f, upper body)

For automatic passives that trigger on an event (for example on hit or at low health). f0–2 head flick, **f3 `Cast`**, f4–8 settle. A small proc spark at `A_Head`. Never interrupts the current action (priority `Action`, upper-body keys only). Rate-limited to one flourish per animal per 2 s.

---

## 4. Rarity escalation

Abilities of higher-rarity animals keep the same timing, but their VFX gain accents ([[VFX - Rarity and Variant Effects]]):

| Rarity | Ability VFX accent |
|---|---|
| Common, Uncommon | Base effect only |
| Rare, Epic | Base effect plus a rarity-coloured rim on rings and Beams |
| Legendary, Mythical | Plus a secondary sparkle layer (rate-capped by quality tier) |
| Secret | Plus the prismatic shimmer module VFX-161 |

---

## 5. Camera summary

Companion abilities never move or shake the local camera. Wild-cast area abilities may apply "Light" shake when they hit the local player. Boss abilities are covered in [[Animation - Boss Attacks]]. See [[Camera Behaviour Guidelines]].

## 6. Mobile performance considerations

- Maximum simultaneous ability VFX per client is capped by tier ([[VFX Bible]]); the local team's abilities always win the budget over other players'.
- Channel and spray loops are the most expensive archetypes. At low quality the spray cone uses one emitter at 50% rate and the Beam uses 8 segments.
- Burrow travel ripples are decals moved by one client loop for all burrowed animals.

## 7. Test hooks

| Test | Expected |
|---|---|
| Fire two manual abilities 0.3 s apart | Second is rejected by the 0.5 s global cooldown; no clip starts; UI shows the cooldown ([[Abilities and Cooldowns]]) |
| Manual ability with 200 ms latency | Command ring appears at once; clip starts on server state; cast frame aligns with the server cast time within one frame of the server time after the state arrives |
| Wild AoE ability | Telegraph decal visible from f0; anticipation at least 0.6 s (wild rule in [[Animation Bible]] §3) |
| Channel interrupted by a stun | Beam cut on the stun frame; stun loop plays |

---

## Related documents
- [[Animal Abilities Catalogue]]
- [[Abilities and Cooldowns]]
- [[Animal Combat Behaviour]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Animation - Boss Attacks]]
- [[VFX - Combat Effects]]
- [[VFX - Rarity and Variant Effects]]
- [[Sound - Abilities]]
- [[UI - Animal Team Display]]
