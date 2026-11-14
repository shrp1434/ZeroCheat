---
title: Animation - Animal Defeat and Victory
type: asset-spec
category: animation
status: mixed
priority: P0
owner: Animation Director
last_updated: 2026-11-14
tags:
  - animation
  - defeat
  - knock-out
  - victory
  - raids
  - animals
---

# Animation - Animal Defeat and Victory

Wild-animal defeat, the knock-out (KO) state for companions and raid defenders, KO recovery, victory poses and the showcase pose used by hatching, ascension and the index.

> [!success] CONFIRMED
> A defending animal can be stolen **only after it has been knocked out**; undefeated defenders can never be stolen; at most **three** animals are stolen per successful raid (D-024). The KO pose specified here is therefore a gameplay-critical readability signal, not decoration.

> [!info] PROPOSED
> All clips, durations and visual rules here are **PROPOSED**. How long a KO lasts, whether a KO'd companion revives in the field, and the defeat penalties are owned by [[Combat States and State Machine]] and [[Player Defeat and Penalties]] (penalties **UNDECIDED**, [[Open Questions#Q-014]]). Whether a knocked-out raid defender can recover during a raid is **UNDECIDED** (Q-701).

---

## 1. Asset table

| Class | Wild defeat | KO entry + loop | KO recovery | Victory | Showcase |
|---|---|---|---|---|---|
| QS | ANI-180 | ANI-187 | ANI-194 | ANI-201 | ANI-208 |
| QL | ANI-181 | ANI-188 | ANI-195 | ANI-202 | ANI-209 |
| BP | ANI-182 | ANI-189 | ANI-196 | ANI-203 | ANI-210 |
| BD | ANI-183 | ANI-190 | ANI-197 | ANI-204 | ANI-211 |
| SP | ANI-184 | ANI-191 | ANI-198 | ANI-205 | ANI-212 |
| AQ | ANI-185 | ANI-192 | ANI-199 | ANI-206 | ANI-213 |
| PB | ANI-186 | ANI-193 | ANI-200 | ANI-207 | ANI-214 |

| Clip family | Duration | Priority | Loop | Status |
|---|---|---|---|---|
| Wild defeat | 1.2 s (36 f) + 0.3 s dissolve | Action4 | No | **PROPOSED** |
| KO entry | 0.8 s (24 f) | Action4 | No | **PROPOSED** |
| KO loop | 2.0 s (60 f) | Action4 | Yes | **PROPOSED** |
| KO recovery | 1.0 s (30 f) | Action4 → Idle | No | **PROPOSED** |
| Victory | 1.5 s (45 f) | Action | No | **PROPOSED** |
| Showcase | 2.0 s (60 f), key pose held from f20 | Action4 | Hold on last frame | **PROPOSED** |

IDs ANI-215 to ANI-219 are reserved.

---

## 2. The three "down" states must never be confused

| State | Who | Pose | Eyes | Duration | Marker | Can be stolen |
|---|---|---|---|---|---|---|
| Stunned | Any | **Standing**, swaying | Swirl | Seconds | Dizzy stars VFX-014 | No |
| Wild defeat | Wild animals | Collapses then **dissolves** | Closed | 1.5 s then gone | Sparkle dissolve VFX-033 | Not applicable |
| **Knocked out** | Companions, guards, raid defenders | **Lying on side, still present** | Swirl, then closed in the loop | Until revived or the raid ends | KO stars VFX-034; in a raid, plus the stealable marker VFX-357 | **Only in an eligible raid, by the raider** |

Production rules:
1. No idle, fidget, emote or sleep animation anywhere in the game may show an animal lying on its side. Pens use sitting or curled-up rests only. This keeps "lying on side" exclusive to KO.
2. The KO loop never fully stops moving: a slow breath and a twitching ear or tail show the animal is dazed, not hurt.
3. No limp ragdolls, no closed-eye stillness without the dizzy stars, no tears or injuries (D-026).

---

## 3. Wild defeat (ANI-180 to ANI-186)

Example QL (ANI-181), 36 frames:

| Frames | Action |
|---|---|
| f0 | Final hit received; 2-frame hit-stop (f0–1) |
| f2–8 | Head thrown back 15°, legs buckle at the hind first |
| f9–16 | Slumps onto its side (90° roll), dust VFX-025 at f14 |
| f17–24 | Small bounce settle, eyes close |
| f25–35 | Holds; at f28 the sparkle dissolve VFX-033 starts at `A_Root` and rises |
| +0.3 s | Rig made transparent over 0.3 s and returned to the pool; cash and XP pickup feedback follows ([[Combat Rewards]]) |

- **Sound:** wild defeat poof SFX-173 at f28; species KO vocal from [[Sound - Animal Vocalisations]] at f2.
- **Camera:** none.
- **Class differences:** birds in flight spiral down 1.5 turns before landing; AQ animals roll belly-up slowly and sink to ground hover height 0.5; serpents uncoil and flatten; small QS hop once and flop.
- **Mobile:** at LOD A2 the clip is skipped and only the dissolve plays.

---

## 4. Knock-out (ANI-187 to ANI-193)

### 4.1 KO entry (24 f) — QL example (ANI-188)

| Frames | Action |
|---|---|
| f0–1 | Hit-stop on the final hit |
| f2–6 | Big stagger back; eyes switch to swirl decal |
| f7–10 | Wobbles in place (two head circles) |
| f11–18 | Sits back, then rolls onto its side (left side by default; right side if the hit came from the left) |
| f19–23 | Settles; KO stars VFX-034 appear over `A_Head`; KO vocal SFX from the species palette |

### 4.2 KO loop (60 f)

- Chest rises 0.05 studs on a 60-frame breath.
- Ear (or tail, fin, crest) twitch at f20 and f45.
- Eyes stay as swirls for the first loop, then switch to closed with a periodic swirl blink every 3 s so a viewer arriving late still reads "dazed".
- KO stars orbit at 0.5 rotations per second.

### 4.3 Raid defender KO — the stealable state

When a defender is knocked out during an eligible raid ([[Animal Theft Rules]]), it plays the same KO entry and loop, and the client **of the raider** adds the stealable presentation:

| Layer | Spec | Seen by |
|---|---|---|
| Pose | Standard KO loop (§4.2) | Everyone |
| Stealable outline | VFX-357: `Highlight` with outline only, colour raid amber `#FF8A3D` (PROPOSED), `OutlineTransparency` pulsing 0.0 ↔ 0.4 every 1.0 s | Raider and raid allies |
| Overhead marker | Paw-and-hand icon billboard at `A_Overhead`, bobbing 0.2 studs | Raider and raid allies |
| Defender view | Same Highlight in defender red `#FF4D4D` (PROPOSED) with a shield-crack icon: "This animal can be taken" | Defender |
| Prompt | `ProximityPrompt` (raider only) that starts the capture channel ([[Animation - Raid Interactions]]) | Raider |
| Steal cap | When the raid has already taken three animals (the confirmed maximum), the outline and prompt are not shown to the raider at all | Raider |

Undefeated defenders never show any of these layers. QA must verify that no outline, icon or prompt appears on a standing defender ([[Test Cases - Raiding]]).

### 4.4 KO recovery (30 f)

| Frames | Action |
|---|---|
| f0–5 | Eyes open (swirl blink), head lifts |
| f6–14 | Rolls upright onto feet (birds: hop up and flap; AQ: re-level and rise to hover height; serpents: re-coil) |
| f15–22 | Whole-body shake-off, KO stars pop (VFX-035 recover shimmer) |
| f23–29 | Into combat idle (if a target is near) or idle |

- **Sound:** SFX-175 recover chime at f15.
- **Transition:** fade 0.2 s to Idle or the class combat idle.

---

## 5. Victory (ANI-201 to ANI-207)

### 5.1 When victory plays

| Trigger | Who plays it | Rule |
|---|---|---|
| The local player's combat tag ends (8 s without damage, [[Canonical Proposed Values]] §4) and the team defeated at least one enemy | The three companions | Staggered: companion 1 at 0 s, 2 at 0.15 s, 3 at 0.30 s |
| Mini-boss or world boss defeated | Every participating player's companions | Plays 1.0 s after the boss defeat burst |
| A raid ends successfully (raider side) or a raid is repelled (defender side) | The winner's team and guards | Raider team plays it at the raid exit; defender guards play it in place |
| Hatch, ascension, merge | Not used; these use the showcase pose | |

Victory never plays while any enemy within 30 studs is still targeting the team, and never in PvP while the opponent is in its KO loop (no gloating over a downed player, see [[PvP System]]).

### 5.2 QL victory example (ANI-202, 45 f)

| Frames | Action |
|---|---|
| f0–8 | Rises tall, chest out, head up 20° |
| f9–14 | Feline: one big stretch with front legs forward; Canine: howl pose; Ungulate: rear on hind legs; Pachyderm: trunk raise; Sprawler: tail sweep and jaw clap |
| f15 | Peak pose (held 4 frames, f15–18), `SFX` marker fires the species victory call |
| f19–34 | Tail wag or head shake, small hop for lighter species |
| f35–44 | Back to idle |

- **VFX:** VFX-037 small confetti burst at `A_Overhead` on f15, A0 only, skipped at low quality.
- **Camera:** none during normal play; after a boss defeat, see [[Camera Behaviour Guidelines]] (optional short orbit, off by default in PvP and raids).

---

## 6. Showcase (ANI-208 to ANI-214)

The showcase is the "hero pose" used whenever an animal is presented: hatch reveal ([[Animation - Egg Hatch]]), ascension ([[Animation - Ascension]]), [[UI - Animal Index Screen]] previews and team selection.

| Frames | Action |
|---|---|
| f0–4 | Pop-in anticipation: body crouched, facing camera 25° off-axis |
| f5–12 | Spring up into the hero pose (role flavour: Tanks plant wide, Assassins low and coiled, Skirmishers mid-hop, Ranged and Support head high, Controllers side-on twist) |
| f13–19 | Settle with a 3% overshoot |
| f20 | **Key pose** — the frame used for hatch and ascension timings and for still thumbnails |
| f20–59 | Breathing hold with one blink at f40 |

- **Sound:** species victory or hatch call at f8 (driven by the hatch or ascension sequence, not by the clip, so it can be re-timed).
- **ViewportFrame use:** for UI previews the rig is placed inside a `WorldModel` in a `ViewportFrame` so the Animator runs; animations inside ViewportFrames are *unverified* on low-end devices and are a prototype check ([[UI - Animal Inventory]]).

---

## 7. Mobile performance considerations

- KO loops are cheap (few keys) but long-lived: in a raid there may be many KO'd guards. KO loops drop to LOD A1 beyond 30 studs (no twitch keys).
- Stealable Highlights count against the Highlight budget ([[VFX Bible]]). The raider client shows Highlights on the nearest 6 stealable defenders and an icon-only marker on the rest.
- Wild defeat dissolves use `ParticleEmitter:Emit` bursts from a pooled emitter, not a new instance per defeat.

## 8. Test hooks

| Test | Expected |
|---|---|
| Knock out a defender during an eligible raid | KO pose, stealable outline and prompt appear for the raider within 0.2 s of the server KO state |
| Damage but do not knock out a defender | No stealable layer ever appears |
| Raid has stolen three animals | Further KO'd defenders show the KO pose but no outline and no prompt |
| Screenshot test of all 7 KO loops beside the 7 stun loops | Reviewers identify KO versus stun correctly 100% of the time at 40 studs on a phone |
| Victory during an active fight | Never plays |

---

## Related documents
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Animation - Raid Interactions]]
- [[Animation - Egg Hatch]]
- [[Animal Theft Rules]]
- [[Raid Lifecycle and States]]
- [[Combat States and State Machine]]
- [[Player Defeat and Penalties]]
- [[Combat Feedback and Readability]]
- [[VFX - Combat Effects]]
- [[Sound - Animal Vocalisations]]
