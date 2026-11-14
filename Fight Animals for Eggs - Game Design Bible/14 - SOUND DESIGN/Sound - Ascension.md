---
title: Sound - Ascension
type: asset-spec
category: audio
status: mixed
priority: P1
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - ascension
  - progression
---

# Sound - Ascension

Sounds for the A1–A5 ascension ceremonies (SFX-370 to SFX-389) and the fanfares MUS-38 and MUS-39. The ceremony itself is in [[Animation - Ascension]].

> [!success] CONFIRMED
> Ascension consumes the required duplicates; the original animal is kept (D-019).

> [!info] PROPOSED
> Five levels A1–A5 (D-037; levels **UNDECIDED** [[Open Questions#Q-004]], duplicates [[Open Questions#Q-005]]). All sounds are **PROPOSED**.

---

## 1. Design intent

Duplicates are not lost; they become part of the original. The sound must feel like **joining**, not sacrifice: warm, rising, communal. No mournful tones, no "disappearing" whooshes that sound like loss.

The ceremony is a 2D personal presentation inside [[UI - Ascension]], so every sound here is 2D and routed to the Eggs and Ceremonies group ([[Audio Mixing and Priority]]), which ducks Music by 12 dB during the fanfare.

---

## 2. Register

| ID | Sound | Purpose | Duration | Frequency | Priority | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|
| SFX-370 | Ceremony open | Pedestal lights | 0.8 s | Soft swell + chime in the animal's rarity interval ([[Sound - Eggs]] §1) | V2 | Phase 1 f0 | 7 (one per rarity) | — |
| SFX-371 | Duplicate transform | A duplicate's happy pose turns into a light orb | 0.5 s | Bright rising two-note (discrete) + sparkle | V2 | Per duplicate | 3 | — |
| SFX-372 | Orb stream | Orb travelling to the original | 0.6 s per orb | Airy shimmer 2–6 kHz | V3 | Per orb | 2 | — |
| SFX-373 | Orb absorb | Orb joins the original; pitch steps up one scale degree per orb (1–5) | 0.3 s | Warm bell | V2 | Absorb frame | 5 pitches | — |
| SFX-374 | Rise swell | The original rises in its power-up pose | 0.6–1.0 s (by level) | String-pad swell | V2 | Phase 3 start | 1 | — |
| SFX-375 | Star ignite | The new star lights; pitch by star number (A1 lowest, A5 highest) | 0.5 s | Bell + sparkle | V2 | Star ignite frame | 5 pitches | Star row in UI |
| SFX-376 | Transform burst A1 | Coloured trim appears | 0.6 s | Light burst | V2 | Phase 4 | 1 | — |
| SFX-377 | Transform burst A2 | Eye glint | 0.7 s | Burst + glint ping | V2 | Phase 4 | 1 | — |
| SFX-378 | Transform burst A3 | Soft aura blooms | 0.9 s | Burst + warm bloom | V2 | Phase 4 | 1 | — |
| SFX-379 | Transform burst A4 | Particle accents burst out | 1.1 s | Burst + species element layer ([[Sound - Abilities]] §4) | V2 | Phase 4 | 1 | — |
| SFX-380 | Transform burst A5 | Crest and full aura | 1.6 s | Large burst, choir swell, crest "ring" | V1 | Phase 4 | 1 | — |
| SFX-381 | A5 shimmer tail | Persistent signature of a fully ascended animal | 0.6 s | Soft shimmer | V3 | A5 animal victory calls (layer at −12 dB) | 1 | [[Sound - Animal Vocalisations]] |
| SFX-382 | Stat gain ticks | Each stat line counting up in the present phase | 0.08 s per tick | Soft tick 2–4 kHz | V2 | UI count-up | 1 | UI counters |
| SFX-383 | Ascension refused | Missing duplicates or Cash | 0.4 s | Muted two-note | V2 | ANI-456 | 1 | Merge refused |
| SFX-384 | Skip | Jump to present | — | Alias of SFX-333 | V2 | Skip | — | — |

SFX-385 to SFX-389 are reserved.

## 3. Fanfares

| ID | Use | Length | Character |
|---|---|---:|---|
| MUS-38 | A1–A4 present phase | 2.0 s | Short brass and strings phrase in the animal's rarity harmony; resolves upward |
| MUS-39 | A5 present phase | 3.5 s | Fuller orchestration, choir, final held chord |

Both are specified in [[Music Direction]].

## 4. Timing map (A5 example, 6.5 s)

| Time (s) | Event | Sound |
|---:|---|---|
| 0.0 | Ceremony open | SFX-370 |
| 1.0–3.5 | Five duplicates transform and stream | SFX-371 ×5, SFX-372 ×5, SFX-373 rising 1–5 |
| 3.5 | Rise | SFX-374 |
| 4.3 | Star 5 ignites | SFX-375 (pitch 5) |
| 4.5 | Crest and full aura | SFX-380 |
| 5.5 | Present | MUS-38/39 (A5: MUS-39), SFX-382 ticks |

## 5. Test hooks

- A1 to A5 played back to back: star pitches rise strictly; no two levels share a transform burst.
- With Music at 0% in settings, the fanfares are silent but every SFX remains.

---

## Related documents
- [[Animation - Ascension]]
- [[Ascension System]]
- [[UI - Ascension]]
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Music Direction]]
- [[Sound - Eggs]]
