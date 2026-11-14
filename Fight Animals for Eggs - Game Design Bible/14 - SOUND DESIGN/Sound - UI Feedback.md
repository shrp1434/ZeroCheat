---
title: Sound - UI Feedback
type: asset-spec
category: audio
status: mixed
priority: P0
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - ui
  - feedback
  - accessibility
---

# Sound - UI Feedback

Interface sounds: navigation, confirmations, errors, currency, cooldowns, progression, index, team, odds disclosure and shop (SFX-390 to SFX-439). Visual UI rules are in [[UI Design System]].

> [!info] PROPOSED
> All sounds and rules are **PROPOSED**.

---

## 1. UI sound rules

| Rule | Value |
|---|---|
| Spatial | All 2D, UI SoundGroup (−10 dB reference, 4 voices) |
| Length | ≤ 0.3 s for navigation; ≤ 1.0 s for milestones |
| Tone | Soft attack, rounded wooden and glassy timbres matching the bright, tactile identity ([[Sound Bible]]) |
| Pitch | Never randomised (tonal meaning) |
| Frequency | 1–6 kHz core, nothing piercing above 8 kHz |
| Errors | Muted and low, never harsh buzzers; errors must not sound like punishment |
| Repeats | Hover limited to one per 0.08 s; Cash ticks aggregated ([[Audio Mixing and Priority]] §4) |
| Purchases with Robux | Neutral confirmation; no celebratory fanfare that is louder than earned rewards ([[Monetisation Principles]]) |

---

## 2. Register

| ID | Sound | Purpose | Duration | Frequency | Priority | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|
| SFX-390 | Tap primary | Primary button press | 0.08 s | Wood tap 1–3 kHz | V2 | Button activated | 1 | — |
| SFX-391 | Tap secondary / back | Back, cancel | 0.08 s | Lower wood tap | V2 | Button activated | 1 | — |
| SFX-392 | Hover (pointer devices) | Focus feedback | 0.05 s | Very soft tick | V4 | Hover or gamepad focus | 1 | — |
| SFX-393 | Tab switch | Navigation | 0.1 s | Paper-slide tick | V2 | Tab change | 1 | — |
| SFX-394 | Panel open | Screen appears | 0.2 s | Rising soft whoosh (short, not a danger sweep: 0.2 s, 1–2 kHz only) | V2 | Panel open | 1 | — |
| SFX-395 | Panel close | Screen closes | 0.15 s | Falling soft whoosh | V2 | Panel close | 1 | — |
| SFX-396 | Toggle on | Setting enabled | 0.08 s | Up click | V2 | Toggle | 1 | — |
| SFX-397 | Toggle off | Setting disabled | 0.08 s | Down click | V2 | Toggle | 1 | — |
| SFX-398 | Slider tick | Volume and value sliders | 0.03 s | Tiny tick | V3 | Every 10% step | 1 | — |
| SFX-399 | Unavailable | Action not possible (locked, insufficient Cash) | 0.2 s | Muted low two-note | V2 | Refusals | 1 | Generic refusals across systems |
| SFX-400 | Cash spend confirm | Purchase with Cash (rolls, upgrades, fees) | 0.3 s | Coin drop + soft chime | V2 | Server confirm | 1 | — |
| SFX-401 | Cash gain tick | Cash added (aggregated) | 0.1 s | Coin tick, pitch +1 semitone per aggregated pickup up to +5 | V3 | Reward events | 1 (pitch steps) | Combat rewards |
| SFX-402 | Cash big gain | Large reward (boss or milestone) | 0.6 s | Coin cascade | V2 | Large reward events | 1 | — |
| SFX-403 | Notification (soft) | Informational toast | 0.2 s | Glass ping | V3 | [[UI - Notifications]] | 1 | — |
| SFX-404 | Notification (important) | Needs attention (not raid alarm) | 0.4 s | Two-note glass ping | V2 | Important toasts | 1 | — |
| SFX-405 | Special ready | A player special's cooldown has ended | 0.2 s | Bright ping, one per special (three pitches: Power Strike, Ground Slam, Rally Cry) | V2 | Cooldown end | 3 pitches | — |
| SFX-406 | Animal ability ready | A manual animal ability is ready | 0.2 s | Soft paw-pad ping; pitch by team slot 1–3 | V2 | Cooldown end | 3 pitches | — |
| SFX-407 | Cooldown fizzle | Pressed while on cooldown | 0.15 s | Dull tick | V3 | Input during cooldown (ANI-234) | 1 | — |
| SFX-408 | Level up jingle | Player level up | 1.2 s | Rising major arpeggio in a register distinct from the rarity language | V1 (out of combat) / V2 (in combat, −6 dB) | Level up | 1 | [[Player Progression and Levelling]] |
| SFX-409 | XP tick | XP gained (aggregated like Cash) | 0.08 s | Soft sparkle tick | V4 | XP events | 1 | — |
| SFX-410 | Index registered | A wild animal species registered as discovered after defeat (D-029) | 0.6 s | Page-turn + chime | V2 | Index update | 1 | [[Animal Index Feature Specification]] |
| SFX-411 | Index milestone | Discovery milestone | 1.0 s | Page flourish + chord | V2 | Milestone | 1 | — |
| SFX-412 | Team slot equip | Animal placed in a team slot at the base | 0.3 s | Satisfying click + species call snippet at −9 dB | V2 | [[UI - Team Selection]] | 1 | — |
| SFX-413 | Team locked notice | Attempted team change away from the base (D-010) | 0.3 s | Soft lock click | V2 | Refusal | 1 | — |
| SFX-414 | Odds updated | Displayed odds changed before confirmation (stale `oddsVersion`, D-041) | 0.4 s | Neutral attention two-note | V2 | UI re-displays new odds ([[Randomised Reward Compliance]]) | 1 | — |
| SFX-415 | Odds panel open | Odds disclosure panel shown before a roll or hatch | 0.2 s | Paper unfold | V2 | Panel open | 1 | — |
| SFX-416 | Drag pick-up | Drag an egg or animal | 0.08 s | Lift click | V3 | Drag start | 1 | — |
| SFX-417 | Drop | Drop into a slot | 0.1 s | Place click | V3 | Drop | 1 | — |
| SFX-418 | Storage full warning | Backpack or base storage full ([[Egg Storage]]) | 0.4 s | Muted three-note | V2 | Full state | 1 | — |
| SFX-419 | Storage expanded | Capacity increased (method **UNDECIDED**, [[Open Questions#Q-009]]) | 0.6 s | Unfolding chime | V2 | Expansion | 1 | — |
| SFX-420 | Goal complete | Generic milestone banner | 0.8 s | Short chord | V2 | Banners | 1 | — |
| SFX-421 | Region unlocked banner | UI side of a region unlock | 1.0 s | Chord + drum | V2 | Banner | 1 | World SFX-147 |
| SFX-422 | Boss bar appear | Boss health bar slides in | 0.4 s | Low drum + whoosh | V2 | [[UI - Boss Health Bar]] | 1 | — |
| SFX-423 | PvP status change | PvP status toggled (activation method **UNDECIDED**, [[Open Questions#Q-011]]) | 0.4 s | Neutral two-tone | V2 | Status change | 2 (on, off) | — |
| SFX-424 | Shop purchase complete | Robux purchase confirmed via `ProcessReceipt` | 0.4 s | Neutral confirm (quieter than earned rewards) | V2 | Receipt processed | 1 | — |
| SFX-425 | Shop purchase cancelled | Prompt closed without purchase | 0.15 s | Soft close | V3 | Prompt closed | 1 | — |
| SFX-426 | Countdown tick | Generic countdowns (shield expiry for the owner, event timers) | 0.08 s | Clock tick | V2 | Each second of the last 10 s | 1 | Shield warning |
| SFX-427 | Countdown final | Countdown reaches zero | 0.3 s | Soft gong-like tone | V2 | Zero | 1 | — |

SFX-428 to SFX-439 are reserved.

---

## 3. Accessibility

- Every UI sound has a visual state change; none carries unique information.
- The UI slider in [[UI - Settings]] controls this group independently.
- "Reduce intense audio" lowers SFX-408 and SFX-402 by 6 dB.

## 4. Test hooks

- Rapidly hover 20 buttons in 1 s on PC: at most 12 hover sounds.
- Pick up 15 Cash drops in 0.25 s: one aggregated tick at +5 semitones.
- Purchase a Robux product: SFX-424 peak is at least 3 dB quieter than SFX-402.

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[UI Design System]]
- [[UI - Main HUD]]
- [[UI - Notifications]]
- [[UI - Shop]]
- [[UI Accessibility Standards]]
- [[Randomised Reward Compliance]]
