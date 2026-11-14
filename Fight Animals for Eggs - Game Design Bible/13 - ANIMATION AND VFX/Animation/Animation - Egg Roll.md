---
title: Animation - Egg Roll
type: asset-spec
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - eggs
  - egg-roll
  - rarity
  - compliance
---

# Animation - Egg Roll

The presentation of an egg roll: the shrine activation, the seven rarity reveal sequences, the ×5 roll layout, skip behaviour and the egg's flight into storage. The roll system itself is specified in [[Egg Roll System]]; egg models in [[Egg Art Direction]]; the broader egg animation overview in [[Egg Animations]].

> [!success] CONFIRMED
> The roll decides the egg's rarity (D-015). Seven rarities: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret (D-003). The actual odds are shown before the player commits and are never changed silently after purchase (D-017).

> [!danger] The result is decided before the animation starts
> The client sends the roll request with the displayed `oddsVersion` token (D-041, **PROPOSED**). The server validates, deducts the Cash, rolls, stores the egg and only then replies with the rarity. The client **starts the reveal only after receiving the server result**. Nothing the player does during the animation (skipping, leaving, disconnecting) can change the result, and a disconnect never loses the egg ([[Implementation - Egg Roll and Hatch Flow]]). The reveal follows the honesty rules in [[Animation Bible]] §6.

> [!info] PROPOSED
> Sequences, durations, frame splits, the ×5 layout and IDs are **PROPOSED**. Roll price (200 Cash) and the ×5 bulk roll (1,000 Cash) are from [[Canonical Proposed Values]] §7; the pricing model is **UNDECIDED** ([[Open Questions#Q-020]]).

---

## 1. Design of the escalation

Every reveal has the same four phases. Rarity changes the **length and intensity of the build** and the **size of the reveal**, never the result.

| Phase | Name | What happens | Rarity-dependent? |
|---|---|---|---|
| A | Intro | Shrine lights up; a neutral cream "mystery shell" egg descends into the cradle | No (0.6 s, all tiers) |
| B | Build | Neutral white pulses; one pulse per tier step (Common 1 … Secret 7); wobble and float grow | Length and pulse count only |
| C | Reveal | Shell cracks; the true rarity colour bursts out | Effect size |
| D | Present | Egg shown in its rarity model with label; flies to storage | Length and flourish |

**Why neutral pulses and not a colour ladder.** A ladder (grey → green → blue …) that stops at the true tier is honest under the Bible rule, but playtests of similar presentations tend to read the colours that *did not* appear as a near miss. Neutral white pulses make the build exciting without ever displaying a higher tier's colour. The colour appears once, at the true tier. The ladder is a rejected alternative, kept here for the record.

Only the Secret build darkens the scene into the night-sky key (`#1B1B2F`). Because no other tier ever shows it, the darkness is a true signal rather than a fake-out.

---

## 2. Durations

| Rarity | Colour key | Full length | Short length (after first viewing of that tier) | Build pulses | Status |
|---|---|---:|---:|---:|---|
| Common | `#9AA5B1` | **1.6 s** (48 f) | 0.8 s | 1 | **PROPOSED** |
| Uncommon | `#4CC26A` | **2.2 s** (66 f) | 1.0 s | 2 | **PROPOSED** |
| Rare | `#3D8BFF` | **2.8 s** (84 f) | 1.2 s | 3 | **PROPOSED** |
| Epic | `#A55BFF` | **3.6 s** (108 f) | 1.5 s | 4 | **PROPOSED** |
| Legendary | `#FFB020` | **4.6 s** (138 f) | 2.0 s | 5 | **PROPOSED** |
| Mythical | `#FF4D8D` | **5.8 s** (174 f) | 2.6 s | 6 | **PROPOSED** |
| Secret | `#1B1B2F` + prismatic | **7.0 s** (210 f) | 3.2 s | 7 | **PROPOSED** |

- "First viewing" is per player per tier, stored in the player profile ([[Schema - Player Profile]]). The first time a player rolls a given tier they see the full version; afterwards the short version plays by default, and the full version can be re-enabled in [[UI - Settings]].
- Skip (tap anywhere, after first viewing) jumps to phase D within 0.4 s (ANI-410). Skipping is a presentation choice only.
- With "Reduce motion", lengths are unchanged but spins, floats and camera pushes become static framing.

---

## 3. Asset table

| ID | Clip / sequence | Length | Priority | Status |
|---|---|---|---|---|
| ANI-400 | Phase A intro: shrine activation and egg descent | 0.6 s (18 f) | n/a (prop animation via `AnimationController` on the shrine rig) | **PROPOSED** |
| ANI-401 | Common reveal (phases B–D) | 1.0 s after intro | — | **PROPOSED** |
| ANI-402 | Uncommon reveal | 1.6 s | — | **PROPOSED** |
| ANI-403 | Rare reveal | 2.2 s | — | **PROPOSED** |
| ANI-404 | Epic reveal | 3.0 s | — | **PROPOSED** |
| ANI-405 | Legendary reveal | 4.0 s | — | **PROPOSED** |
| ANI-406 | Mythical reveal | 5.2 s | — | **PROPOSED** |
| ANI-407 | Secret reveal | 6.4 s | — | **PROPOSED** |
| ANI-408 | Roll ×5 layout controller (five cradles) | up to 7.8 s | — | **PROPOSED** |
| ANI-409 | Egg flight to storage | 0.5 s | — | **PROPOSED** |
| ANI-410 | Skip to result | 0.4 s | — | **PROPOSED** |
| ANI-411 | Player watch-and-react set (upper body: lean in, nod, clap, cheer) | 0.6–1.2 s | Action | **PROPOSED** |
| ANI-412 | Shrine idle loop | 4.0 s loop | — | **PROPOSED** |
| ANI-413 | Roll refused (insufficient Cash, storage full, stale odds) | 0.5 s | — | **PROPOSED** |

The egg itself is a prop rig (`HumanoidRootPart`, `ShellTop`, `ShellBottom`, `Glow` parts, `AnimationController`). Egg wobble, crack and float are keyframed on this rig; colour changes are material swaps driven by markers (`VFX` marker value `"RARITY_REVEAL"`).

---

## 4. Phase A — intro (ANI-400, all tiers, f0–17)

| Frames | Action | VFX | SFX |
|---|---|---|---|
| f0 | Shrine rune ring lights (cream white) | VFX-300 shrine glow ramps up | SFX-320 shrine activate |
| f0–11 | Mystery egg descends from 4 studs above the cradle along a soft beam | VFX-301 descent beam | |
| f12 | Egg lands in cradle; 3% squash via cradle pose (the egg part itself is not scaled) | Small dust of light | SFX-321 land |
| f13–17 | Two small wobbles (±6°) | | SFX-322 wobble tick |

**Camera:** on roll confirm the camera blends (0.3 s) to the roll framing: Scriptable camera 12 studs from the cradle, 20° elevation, FOV 55 ([[Camera Behaviour Guidelines]]). If the roll was made from a UI panel away from the shrine, the same sequence plays in the [[UI - Egg Rolling]] viewport instead and the world camera is untouched.

**Player:** if the player is at the shrine, their avatar plays ANI-411 "lean in" (upper body) from f0.

---

## 5. Reveal sequences (frame by frame, 30 fps, frame 0 = start of phase A)

### 5.1 Common — 1.6 s (ANI-401)

| Frames | Phase | Action |
|---|---|---|
| f0–17 | A | Intro |
| f18–23 | B | One pulse: soft white glow swells and fades (SFX-323 pulse 1); one wobble |
| f24 | C | Crack line appears across the shell (SFX-324 crack) |
| f26 | C | Shell top lifts 0.3 studs; Common slate-grey colour and the Common egg model swap in; VFX-111 small grey puff ring |
| f27–39 | D | Egg settles, rarity label "Common" appears in [[UI - Egg Rolling]]; MUS-31 Common stinger (0.6 s) |
| f40–47 | D | Egg flies to storage (ANI-409 begins at f40) |

### 5.2 Uncommon — 2.2 s (ANI-402)

| Frames | Phase | Action |
|---|---|---|
| f0–17 | A | Intro |
| f18–35 | B | Pulses at f20 and f30 (SFX-323 rising a whole tone each pulse); wobbles grow from ±6° to ±10° |
| f36 | C | Crack |
| f38 | C | Leaf-green colour, Uncommon model; VFX-112 green ring and four leaf-shaped sparks |
| f39–55 | D | Bounce, label, MUS-32 stinger |
| f56–65 | D | Flight to storage |

### 5.3 Rare — 2.8 s (ANI-403)

| Frames | Phase | Action |
|---|---|---|
| f0–17 | A | Intro |
| f18–47 | B | Pulses at f20, f30, f40; the egg lifts 0.2 studs off the cradle on pulse 3 |
| f48 | C | Crack, two lines |
| f50 | C | Sky-blue colour, Rare model; VFX-113 blue burst with 6 short light rays |
| f51–71 | D | Egg spins once (360° over 20 frames), label, MUS-33 stinger |
| f72–83 | D | Flight to storage |

### 5.4 Epic — 3.6 s (ANI-404)

| Frames | Phase | Action |
|---|---|---|
| f0–17 | A | Intro |
| f18 | B | Shrine rune ring brightens; ambient light around the shrine dims 15% (local client only) |
| f18–65 | B | Pulses at f20, f32, f44, f56; egg floats up to 0.6 studs by f56; wobble becomes a slow rock |
| f66–71 | C | Crack lines spread across the shell over 6 frames (SFX-324 with a sustain tail) |
| f72 | C | Violet colour, Epic model; VFX-114 violet burst, ring shockwave and orbiting motes |
| f73–95 | D | Egg spins twice, motes orbit; label; MUS-34 stinger |
| f96–107 | D | Flight to storage |

### 5.5 Legendary — 4.6 s (ANI-405)

| Frames | Phase | Action | Camera |
|---|---|---|---|
| f0–17 | A | Intro | Roll framing |
| f18–83 | B | Five pulses, accelerating: f20, f34, f46, f56, f64; egg rises to float at 1.0 stud by f60, slow rotation begins | Slow push-in from 12 to 9 studs over f18–83 |
| f84–89 | C | White light leaks through growing cracks (VFX-302 neutral) | Hold |
| f90 | C | **Gold** colour, Legendary model; VFX-115 gold burst, vertical light pillar 20 studs tall, gold ray fan | "Light" shake (unless reduce motion) |
| f91–125 | D | Egg spins with gold rays; label; MUS-35 Legendary stinger (2.0 s) | Hold, slight orbit 10° |
| f126–137 | D | Flight to storage | Blend back over 0.4 s |

### 5.6 Mythical — 5.8 s (ANI-406)

| Frames | Phase | Action | Camera |
|---|---|---|---|
| f0–17 | A | Intro | Roll framing |
| f18–107 | B | Six pulses (f20, f34, f48, f62, f76, f90); a white haze vignette closes in (screen-space, local only); egg floats to 1.5 studs and spins faster each pulse; shrine rune ring rises around the egg | Push-in to 8 studs |
| f108–113 | C | Cracks, neutral light leaks, egg shudders | Hold |
| f114 | C | **Magenta-rose** colour, Mythical model; VFX-116 burst, petal swirl, double ring shockwave | "Light" shake |
| f115–161 | D | Egg descends slowly in a spiral of petals; label; MUS-36 Mythical stinger (2.8 s) | 15° orbit |
| f162–173 | D | Flight to storage | Blend back |

### 5.7 Secret — 7.0 s (ANI-407)

| Frames | Phase | Action | Camera |
|---|---|---|---|
| f0–17 | A | Intro | Roll framing |
| f18–47 | B | Lights fade towards deep night `#1B1B2F` (local lighting override), stars appear around the shrine | Push-in begins |
| f48–131 | B | Seven pulses in total (f20, f34, f48, f62, f76, f96, f116), the last two slower; egg floats to 2.0 studs; a ring of seven small lights (one per rarity, all white) circles the egg | Push-in to 7 studs, slow orbit 20° |
| f132–143 | C | Cracks race across the shell; every star brightens | Hold |
| f144 | C | **Prismatic** reveal: Secret model in deep night with prismatic shimmer; VFX-117 prismatic burst, aurora ribbons (Beams), star shower | "Medium" shake (unless reduce motion) |
| f145–197 | D | Egg rotates slowly while the night lifts back to normal lighting; label; MUS-37 Secret stinger (3.5 s) | Slow pull-out |
| f198–209 | D | Flight to storage | Blend back |

---

## 6. Roll ×5 (ANI-408)

- Five cradles in a shallow arc in front of the shrine, 2.5 studs apart. The roll framing widens to FOV 65.
- **Intro:** the five mystery eggs descend with a 0.15 s stagger (left to right), landing f12, f16, f21, f25, f30.
- **Parallel reveals:** each egg then plays its own tier's phases B and C, starting at its own landing frame. Commons therefore crack first and the rarest egg cracks last. No egg's presentation is affected by the others.
- **Effects hierarchy:** only the highest-tier egg gets camera moves; others keep their bursts but at 60% particle rate.
- **Present:** when the last egg has revealed, all five are shown together for 0.6 s with labels, then fly to storage one after another (0.1 s stagger).
- **Total length** = the full length of the rarest egg's sequence + that egg's landing offset (0 to 0.6 s) + 0.6 s group present − its own 0.4 s flight (flights happen after the group present). Worst case (a Secret in the fifth cradle): 7.0 + 0.6 + 0.6 − 0.4 ≈ **7.8 s** full.
- **Skip** reveals all five at once.

---

## 7. Egg flight to storage (ANI-409)

0.5 s arc from the cradle to the backpack HUD icon (screen-space tween over the last 0.2 s) or, if the egg goes to base storage, to the base icon. Storage destination and full-storage rules are in [[Egg Storage]]. SFX-332 on arrival with a counter tick in the HUD.

## 8. Roll refused (ANI-413)

If the server refuses (insufficient Cash, storage full, stale `oddsVersion`), no egg appears. The shrine ring flickers twice and dims (0.5 s), SFX-334, and the UI shows the reason; for a stale token the UI re-displays the new odds ([[Randomised Reward Compliance]]).

---

## 9. Shared-world visibility

> [!warning] UNDECIDED (Q-703)
> Whether other players in the shared world see a player's roll reveals, and whether Mythical and Secret results are announced server-wide, is **UNDECIDED** (Q-703). Recommendation (**PROPOSED**): each player's reveal plays on a client-side cradle instance at the shrine, so up to 16 players can roll at once without queueing; other players see only a short coloured light column above the rolling player **after** the reveal completes. Server announcements are off until the owner decides.

---

## 10. Mobile performance considerations

| Item | Low | Medium | High |
|---|---|---|---|
| Reveal burst particle rate | 40% | 70% | 100% |
| Light pillar and aurora Beams | 1 Beam | 2 Beams | 4 Beams |
| Local lighting override (Epic dim, Secret night) | Colour-grade only (`ColorCorrectionEffect`) | Colour-grade + ambient | Full |
| ×5 roll secondary eggs | 40% particle rate | 60% | 60% |

Preload all seven egg models, their materials and the reveal VFX when the player enters the hub (`ContentProvider:PreloadAsync`), so the reveal never stalls on asset load. If an asset is not ready, the reveal waits in phase B (extra neutral pulses are **not** added; the build simply holds its last pulse) and logs a warning ([[Logging and Error Handling]]).

## 11. Test hooks

| Test | Expected |
|---|---|
| Force each rarity on a test server | Each sequence matches §5 frame splits within 1 frame |
| Inspect every frame of every non-Secret reveal | No colour of a higher tier, and no night-sky darkening, ever appears |
| Disconnect during phase B | On rejoin the egg is in storage; the reveal is offered again as a short replay from the inventory |
| ×5 roll with Common, Common, Rare, Common, Epic (Epic in cradle 5) | Reveals in order of tier length; total ≈ 3.6 + 0.6 + 0.6 − 0.4 = 4.4 s |
| Skip on first viewing of a tier | Not allowed; tap does nothing until phase D |

---

## Related documents
- [[Egg Roll System]]
- [[Egg Animations]]
- [[Egg Rarity System]]
- [[Randomised Reward Compliance]]
- [[UI - Egg Rolling]]
- [[Animation - Egg Hatch]]
- [[VFX - Rarity and Variant Effects]]
- [[Sound - Eggs]]
- [[Music Direction]]
- [[Camera Behaviour Guidelines]]
- [[Hub - Hatchling Haven]]
