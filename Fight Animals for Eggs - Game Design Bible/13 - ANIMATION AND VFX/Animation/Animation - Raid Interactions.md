---
title: Animation - Raid Interactions
type: asset-spec
category: animation
status: mixed
priority: P1
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - raids
  - theft
  - base-defence
  - pvp
---

# Animation - Raid Interactions

Alarm, raider entry, steal channels, egg and animal capture, carry, drop, return, secure, and the end-of-raid poses for both sides.

> [!success] CONFIRMED
> Raids are optional. Eggs stored in the base can be stolen; **backpack eggs can never be stolen**. A defending animal can be stolen **only after it has been knocked out**; undefeated defenders cannot be stolen. **Maximum three animals** stolen per successful raid. Offline bases cannot be raided (D-021, D-024).

> [!warning] UNDECIDED
> Raid duration ([[Open Questions#Q-012]]) and the egg theft limit ([[Open Questions#Q-013]]) are **UNDECIDED**; no animation here encodes them. What a stolen animal keeps is **UNDECIDED** ([[Open Questions#Q-025]]). Which animals defend is **UNDECIDED** ([[Open Questions#Q-033]]). Whether captured items must be physically carried out of the base before they count, or transfer when the capture completes, is **UNDECIDED** (Q-704). This document animates both options.

> [!info] PROPOSED
> All clips, durations, colours and the working channel times below are **PROPOSED**. Channel times are configuration values owned by [[Egg Theft Rules]] and [[Animal Theft Rules]]; the numbers here are prototype placeholders so animators can block the loops.

---

## 1. Readability rules for raids

| Rule | Why |
|---|---|
| Only things that are actually stealable get a steal prompt, outline or marker | The prompt is the player's truth source; a wrong prompt would teach the wrong rules |
| Undefeated defenders never show any steal layer | D-024 |
| Backpack eggs never appear in the base or in any steal UI | D-021 |
| Once three animals have been taken, no further animal prompt or outline is shown to that raider | D-024 cap |
| Raider colour amber `#FF8A3D`, defender colour red `#FF4D4D`, shield cyan `#5CE1FF` (all PROPOSED) | Consistent across HUD, outlines and world effects ([[UI - Raid Interface]]) |
| Theft is shown as gentle capture in a bubble, never as harm | D-026; captured animals look asleep and comfortable |

---

## 2. Asset table

| ID | Clip | Rig | Length | Priority | Status |
|---|---|---|---|---|---|
| ANI-520 | Alarm trigger (siren tower rises and spins up) | Defence Station prop | 1.2 s | — | **PROPOSED** |
| ANI-521 | Alarm loop (siren light rotation, bell swing) | Defence Station prop | 2.0 s loop | — | **PROPOSED** |
| ANI-522 | Raider boundary entry (step through the raid boundary shimmer) | Player R15 | 0.8 s | Action2 | **PROPOSED** |
| ANI-523 | Steal channel — egg (enter, loop, exit) | Player R15 | 0.4 s + loop + 0.3 s | Action2 | **PROPOSED** |
| ANI-524 | Steal channel — animal (enter, loop, exit) | Player R15 | 0.5 s + loop + 0.3 s | Action2 | **PROPOSED** |
| ANI-525 | Egg capture (egg lifts into a capture orb) | Orb prop | 0.6 s | — | **PROPOSED** |
| ANI-526 | Animal capture (orb envelops the KO'd defender) | Orb prop + defender rig | 1.0 s | Action4 on defender | **PROPOSED** |
| ANI-527 | Carry override (upper body; legs keep locomotion) | Player R15 | 1.0 s loop | Action | **PROPOSED** |
| ANI-528 | Drop (orb knocked out of the hands) | Player R15 + orb | 0.8 s | Action3 | **PROPOSED** |
| ANI-529 | Return (orb flies home to vault or pen) | Orb prop | 0.8 s | — | **PROPOSED** |
| ANI-530 | Secure (item counted for the raider) | Orb prop | 1.0 s | — | **PROPOSED** |
| ANI-531 | Channel interrupted | Player R15 | 0.4 s | Action3 | **PROPOSED** |
| ANI-532 | Raid success pose (raider) | Player R15 | 1.5 s | Action | **PROPOSED** |
| ANI-533 | Raid repelled pose (defender) | Player R15 | 1.5 s | Action | **PROPOSED** |
| ANI-534 | Guard alert (per class: head snap, warning call) | Animal rigs, `ANI-534/<class>` | 0.6 s | Action | **PROPOSED** |
| ANI-535 | Ground-wait loop (dropped orb waiting for pickup, Q-704 option B) | Orb prop | 2.0 s loop | — | **PROPOSED** |

IDs ANI-536 to ANI-549 are reserved.

### 2.1 Working channel times (prototype placeholders, PROPOSED)

| Channel | Working value | Owner of the real value |
|---|---|---|
| Steal one egg | 3.0 s | [[Egg Theft Rules]] |
| Capture one knocked-out animal | 5.0 s | [[Animal Theft Rules]] |

Loops are authored so any channel length from 1.5 s to 10 s looks correct.

---

## 3. Alarm

### 3.1 When it fires

The alarm marks the raid's start as defined in [[Raid Lifecycle and States]]. The defender is always online (offline bases cannot be raided), so the alarm is both an in-world signal at the base and a notification wherever the defender is ([[UI - Notifications]], [[Sound - Base and Raid Alerts]]).

### 3.2 ANI-520 Alarm trigger (36 f) and ANI-521 loop

| Frames | Action | VFX | SFX |
|---|---|---|---|
| f0–11 | Siren tower on the Defence Station rises 2 studs out of its housing | Dust | SFX-463 alarm start |
| f12–23 | Amber siren lamp begins rotating (0 → 360°/s) | VFX-350 rotating light cone (one `SpotLight` + Beam) | Siren swell |
| f24–35 | Bell swings (if the station level has one) | Base-wide amber tint pulse (`ColorCorrectionEffect` on clients inside the base boundary) | Bell |
| Loop (60 f) | Lamp rotates; bell swings every 2 s | Tint pulse every 2 s, low contrast | SFX-463 loop, ducked after 6 s (§8) |

Base guards play ANI-534 guard alert on the first loop.

**Camera:** none. The defender's camera is never taken over during a raid.

---

## 4. Raider entry (ANI-522, 48 f @60)

f0–11 raider braces at the boundary shimmer (VFX-351 boundary wall), f12–29 steps through with arms shielding the face, the shimmer ripples around the body, f30–47 lands in a ready crouch. SFX-465. The raid HUD appears ([[UI - Raid Interface]]).

---

## 5. Steal channels and capture

### 5.1 Egg steal — ANI-523 then ANI-525

Prompt: a `ProximityPrompt` on each stealable egg rack slot in the [[Module - Egg Vault]] (raider only, `HoldDuration` = the configured channel time). Because ProximityPrompt holds can be cancelled by the client, the server times the channel independently ([[Raid Anti-Exploit Validation]]).

| Frames (@60) | Raider | Egg and world | VFX | SFX |
|---|---|---|---|---|
| Enter f0–23 | Kneels at the rack, both hands reach to the egg | Egg wobbles | Progress ring VFX-352 appears around the egg at 0% | SFX-466 channel start |
| Loop (60 f) | Hands circle the egg, palms glowing amber; small shoulder shake every 30 f | Egg glows amber, wobble grows with progress | Ring fills with progress (driven by server-replicated progress, not by the clip) | SFX-466 loop, pitch rises with progress |
| Progress reaches 100% | — | — | — | — |
| ANI-525 f0–8 (@30) | Hands pull back | A capture orb forms around the egg | VFX-353 orb | SFX-468 capture pop |
| f9–17 | Stands | Orb lifts from the rack and floats into the raider's hands | Orb trail | |

The defender sees the same ring in defender red and a HUD warning "Egg being taken from your vault" with a pointer.

### 5.2 Animal capture — ANI-524 then ANI-526

Only available on knocked-out defenders that show the stealable outline ([[Animation - Animal Defeat and Victory]] §4.3) and only while the raid's animal count is below three.

| Frames (@60) | Raider | Defender (in KO loop) | VFX | SFX |
|---|---|---|---|---|
| Enter f0–29 | Steps to the animal, crouches, holds both hands out over it | KO loop continues | Ring VFX-352 appears on the ground around the animal | SFX-467 channel start |
| Loop (60 f) | Hands spread slowly as if inflating a bubble; amber glow grows | A translucent bubble forms over the animal, its size tracking progress | Ring fills with server progress | Bubble stretching loop, pitch rises |
| ANI-526 f0–9 (@30) | Hands lift | Bubble completes and seals with a soft shine | VFX-353 orb seal | SFX-469 capture |
| f10–19 | Stands | Bubble lifts 1 stud; the animal inside is swapped for a miniature proxy curled up asleep (a small, comfortable pose, not the KO pose) | | |
| f20–29 | Receives the orb | Orb shrinks to 1.5 studs and floats to the raider's hands | Orb trail | |

Shrinking uses a pre-built miniature proxy model rather than scaling the rig at runtime; `Model:ScaleTo` would also work but its cost on complex rigs is *unverified*.

The HUD shows the animal count, for example "Animals 2 / 3". After the third animal, prompts and outlines disappear for that raider.

### 5.3 ANI-531 Channel interrupted (24 f @60)

If the raider is hit by a defence, moves away, or the server cancels the channel: f0–5 hands snap back, f6–17 stumble half a step, f18–23 recover. The progress ring flashes and drains over 0.3 s (progress reset rules belong to the theft rules). SFX-474.

---

## 6. Carry, drop, return and secure

> [!warning] Depends on Q-704
> **Option A — transfer on capture.** The item counts for the raider as soon as the capture completes; the orb immediately plays ANI-530 secure and no carry is needed. **Option B — carry out.** The raider must carry the orb to the raid exit; while carrying, ANI-527 plays, and if the raider is defeated the orb drops (ANI-528). Both options are fully animated; neither is chosen here.

### 6.1 ANI-527 Carry override (60 f loop @60)

Upper body only (arms, `UpperTorso`, `Head`), so the player's locomotion continues underneath.

- Orb held in both hands in front of the chest; elbows bent at 80°.
- f0–29 orb bobs up 0.1 studs, f30–59 down. Head looks slightly down at the orb every other loop.
- Additional carried items (if carry rules allow more than one) are shown as small orbs orbiting the raider at 2 studs, not as extra hand poses.
- Any carry speed penalty is a gameplay value of the theft rules; the clip looks correct between 8 and 16 studs/s.
- Combat while carrying: attacks are blocked or allowed per the theft rules; if allowed, attack clips play and the orb tucks under one arm (variant `ANI-527/1H`).

### 6.2 ANI-528 Drop (48 f @60)

f0–5 raider is hit, the orb jumps out of the hands; f6–29 orb bounces twice on the ground (VFX-355 bounce puffs); raider staggers back. Then either ANI-529 return (if rules return dropped items immediately) or ANI-535 ground-wait loop (if rules allow pickup). SFX-471.

### 6.3 ANI-529 Return (24 f @30)

Orb rises 2 studs, then flies along an arc back to the vault rack or the pen; at arrival it pops (VFX-355) and the egg or animal reappears in place. For an animal, it reappears in its KO loop or recovered, per [[Animal Theft Rules]]. SFX-472.

### 6.4 ANI-530 Secure (30 f @30)

Orb glows amber, then bursts into sparkles (VFX-354 secure burst); an icon of the egg or animal flies to the raider's raid HUD tally. SFX-473. The victim's HUD shows the loss with a neutral, non-mocking message.

---

## 7. End of raid

| Outcome | Raider | Defender | Guards |
|---|---|---|---|
| Raid succeeds | ANI-532: fist pump and cheer (no taunting gestures, no pointing at the defender) | ANI-533 is not played; neutral idle | — |
| Raid repelled or fails | Neutral recovery to idle | ANI-533: arms-up relief cheer | Victory clips ([[Animation - Animal Defeat and Victory]]) |

End-of-raid banners and summaries are in [[UI - Raid Interface]]; compensation is in [[Raid Rewards and Defender Compensation]].

---

## 8. Sound and camera summary

| Event | Camera | Sound |
|---|---|---|
| Alarm | None | Alarm loop ducks by 9 dB after 6 s so the raid stays audible but not fatiguing; returns to full at each new steal start |
| Steal channel start | None | Defender gets a positional warning sound from the vault or pen direction |
| Capture complete | None | Short capture pop, audible within 40 studs |
| Carry | None | Soft orb hum loop on the carrier (others hear it within 30 studs, helping defenders find the carrier) |
| Secure | None | Raider-only confirmation; defender hears a neutral "item lost" cue |

Details and IDs: [[Sound - Base and Raid Alerts]].

## 9. Mobile performance considerations

- Progress rings are `SurfaceGui` or decal parts updated by one client loop from replicated progress values (at most 10 Hz), not particles.
- Stealable outlines are capped (nearest 6 with Highlights, the rest with icons only, see [[VFX Bible]]).
- Orbs are pooled; one orb prop per possible concurrent capture.
- The base-wide amber tint is a single `ColorCorrectionEffect`; on low quality it is replaced by HUD edge pulses.

## 10. Test hooks

| Test | Expected |
|---|---|
| Raid a base with eggs in the vault and eggs in the defender's backpack | Prompts on vault eggs only; nothing for backpack eggs |
| Attempt to capture a standing (not knocked-out) defender | No prompt, no outline, server rejects any forced request |
| Capture three animals | After the third, no animal prompt or outline for that raider |
| Interrupt a channel at 60% | ANI-531 plays; ring drains; server progress follows theft rules |
| Raider defeated while carrying (option B build) | Drop plays, then return or ground-wait per configuration |
| Offline base | No raid entry possible; no alarm ever plays |

---

## Related documents
- [[Base Raiding System]]
- [[Raid Lifecycle and States]]
- [[Egg Theft Rules]]
- [[Animal Theft Rules]]
- [[Raid Anti-Exploit Validation]]
- [[Raid Disconnection Handling]]
- [[UI - Raid Interface]]
- [[Animation - Animal Defeat and Victory]]
- [[Animation - Shield Activation]]
- [[Sound - Base and Raid Alerts]]
- [[Test Cases - Raiding]]
