---
title: Sound Bible
type: guide
category: audio
status: proposed
priority: P0
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - sound-design
  - style-guide
  - spatialisation
---

# Sound Bible

The sonic identity, technical conventions, spatial profiles, priority scale, variation rules and ID allocation for every sound in *Fight Animals for Eggs*. Mixing, voice limits and ducking are in [[Audio Mixing and Priority]]; music in [[Music Direction]].

> [!info] PROPOSED
> Everything in this document is **PROPOSED** by the Sound Designer.

---

## 1. Sonic identity

| Pillar | Means | Rules out |
|---|---|---|
| **Bright and tactile** | Wooden knocks, soft thumps, chimes, plucks, bubbly pops; impacts that feel like toys colliding with weight | Realistic flesh impacts, bone cracks, gunshots |
| **Animal truth, softened** | Real species character (a lion's chest rumble, a duck's quack) recorded or designed with harsh edges rounded off | Screams, pain cries, distressed animal sounds, growls that read as horror |
| **Rarity you can hear** | Each rarity has its own interval and instrument colour, rising from Common to Secret ([[Sound - Eggs]]) | Identical "win" sounds for every tier |
| **Readable on a phone speaker** | Every gameplay-important sound has strong content between 500 Hz and 4 kHz | Information carried only by sub-bass |
| **Calm by default, intense on purpose** | Ambience and UI are gentle; tension rises only for telegraphs, bosses, raids and reveals | Constant high-energy noise |

### 1.1 Banned content

No meme sounds or internet audio references (no "vine boom", airhorns, "bruh", record scratches, laugh tracks, flatulence, recognisable viral clips), no licensed popular music, no voice memes, no crude or mocking sounds aimed at defeated players, no horror stingers, and no sound that imitates a real product, brand jingle or person. This follows the visual direction in D-026.

---

## 2. Technical conventions

| Item | Convention |
|---|---|
| Engine objects | `Sound` instances in pooled templates under `ReplicatedStorage/Audio/<SFX-###>`; grouped by `SoundGroup` under `SoundService` ([[Audio Mixing and Priority]]) |
| 2D versus 3D | A `Sound` parented to a `BasePart` or `Attachment` is positional (3D). A `Sound` parented to `SoundService` or a non-part container plays without position (2D). UI, music and stingers are 2D; world events are 3D |
| Spatial properties | `RollOffMode` (`Enum.RollOffMode.Inverse`, `Linear`, `InverseTapered`, `LinearSquare`), `RollOffMinDistance`, `RollOffMaxDistance` |
| Playback | `Volume`, `PlaybackSpeed` (pitch variation), `Looped`, `TimePosition` |
| Effects | `EqualizerSoundEffect`, `CompressorSoundEffect`, `ReverbSoundEffect`, `PitchShiftSoundEffect` on SoundGroups, not on individual sounds |
| Newer audio API | Roblox also offers an instance-based audio graph (`AudioPlayer`, `AudioEmitter`, `AudioListener` and related). Our design is expressed in `Sound`/`SoundGroup` terms; migrating is an engineering choice, and feature parity details are *unverified* |
| Asset ownership | Audio assets must be uploaded by, or usable by, the account or group that owns the experience; the exact permission rules are *unverified* and checked by the audio lead before each upload batch |
| Source format | 48 kHz, 24-bit WAV masters; uploaded as OGG or MP3 per Roblox's accepted formats |
| Peak level | Masters peak at −1 dBFS; perceived loudness is balanced by category reference levels in [[Audio Mixing and Priority]] |
| Naming | `SFX-###_<Category>_<Name>_v<n>`, e.g. `SFX-161_Combat_ClawSwipe_v3`; music `MUS-##_<Name>_<Stem>` ([[Asset Naming Conventions]]) |
| Who plays sounds | Clients play all cosmetic sounds from replicated events and animation markers ([[Animal Rig Standards]] §8); the server never plays world SFX directly except via replicated state |

---

## 3. Spatial profiles

Every 3D sound uses one of these profiles. Distances are in studs.

| Profile | RollOffMode | RollOffMinDistance | RollOffMaxDistance | Use |
|---|---|---:|---:|---|
| S1 Close | InverseTapered | 4 | 40 | Hits, small vocals, foley, footsteps |
| S2 Mid | InverseTapered | 8 | 80 | Abilities, larger vocals, projectiles, base props |
| S3 Far | InverseTapered | 15 | 200 | Boss attacks, boss roars, raid alarm at the base, shield events |
| S4 Region | Linear | 20 | 300 | Rare-spawn beacons, world boss announcements, region landmark loops |
| S5 Emitter bed | Linear | 10 | 60 | Placed ambience (waterfalls, vents, fountains) |
| 2D | — | — | — | UI, music, stingers, own reveal sequences, personal alerts |

`InverseTapered` is the default because it behaves like natural inverse falloff near the source but reaches silence at `RollOffMaxDistance`, which keeps far sounds from stacking. The exact curve shape of each mode is as documented by Roblox; fine-tuning per mode is checked in prototype.

---

## 4. Volume priority scale

Each sound has a priority used by voice stealing and ducking ([[Audio Mixing and Priority]]).

| Priority | Name | Examples | May be stolen by |
|---|---|---|---|
| V1 | Critical | Boss telegraph risers, raid alarm, steal warnings, rarity reveal stingers, shield break | Nothing |
| V2 | Important | Own player hits and specials, own team abilities, UI confirms, KO of own animal | V1 |
| V3 | Standard | Other players' combat, wild animal attacks, creature vocals | V1, V2 |
| V4 | Background | Foley, footsteps, idle vocals, prop idles | V1–V3 |
| V5 | Bed | Ambience beds, distant loops | Anything; ducked first |

---

## 5. Variation and repetition

| Rule | Value |
|---|---|
| Variants for frequently heard sounds (hits, footsteps, vocals) | 3–5 recorded or designed variants |
| Pitch randomisation | `PlaybackSpeed` × Random(0.95, 1.05) by default; ±3% for tonal sounds (chimes, stingers: none) |
| No immediate repeat | The same variant never plays twice in a row from the same source |
| Tonal sounds | Rarity chimes, UI confirms and stingers are never pitch-randomised (they carry musical meaning) |
| Long loops | Seamless, ≥ 20 s for beds, with at least 2 alternate beds per region to avoid recognisable cycles |

---

## 6. Frequency map

| Category | Core band | Transient band | Notes |
|---|---|---|---|
| Combat impacts | 120–500 Hz body | 2–5 kHz click | Body gives weight on headphones; click carries on phones |
| Telegraph risers | 600 Hz → 3 kHz sweep | — | Rising pitch means "danger coming" everywhere in the game |
| Creature vocals | 250 Hz–3 kHz | — | Large animals add 80–200 Hz chest layer, filtered on low-end speakers by design |
| UI | 1–6 kHz | short | Short (≤ 0.3 s), soft attack, never piercing above 8 kHz |
| Rarity chimes | Tier-dependent: low tiers mid register, high tiers add sparkle 6–10 kHz | — | See [[Sound - Eggs]] |
| Ambience | Broadband, high-cut above 10 kHz | — | Kept 12–18 dB below combat |
| Music | Full range | — | Ducked under V1 events |

---

## 7. ID allocation

| Range | Document |
|---|---|
| SFX-001 – SFX-099 | [[Sound - Animal Vocalisations]] |
| SFX-100 – SFX-149 | [[Sound - Ambient World]] |
| SFX-150 – SFX-219 | [[Sound - Combat Impacts]] (includes movement foley SFX-200–219) |
| SFX-220 – SFX-269 | [[Sound - Abilities]] (player specials and animal ability archetypes) |
| SFX-270 – SFX-319 | [[Sound - Bosses]] |
| SFX-320 – SFX-369 | [[Sound - Eggs]] (roll, hatch, merge, station) |
| SFX-370 – SFX-389 | [[Sound - Ascension]] |
| SFX-390 – SFX-439 | [[Sound - UI Feedback]] |
| SFX-440 – SFX-489 | [[Sound - Base and Raid Alerts]] |
| SFX-490 – SFX-599 | Reserved for live content ([[Content Expansion Guidelines]]) |
| MUS-01 – MUS-49 | [[Music Direction]] |

New sounds use [[Template - Sound]] and are registered in the [[Asset Register]].

### 7.1 Per-sound specification fields

Every sound row in the SFX documents states: **purpose**, **duration**, **frequency character**, **priority (V1–V5)**, **spatial profile (S1–S5 or 2D)**, **trigger**, **variations**, **reuse**. Cooldowns and voice limits come from the SoundGroup rules in [[Audio Mixing and Priority]] unless a row overrides them.

---

## 8. Accessibility

- Separate volume sliders for Music, Effects, Ambience and UI in [[UI - Settings]], mapped to SoundGroups.
- Every V1 sound has a visual equivalent (telegraph decal, HUD alert), so no information is audio-only ([[UI Accessibility Standards]]).
- "Reduce intense audio" option: lowers V1 stingers by 6 dB and removes sub-bass layers from boss sounds.

---

## Related documents
- [[Sound Design Index]]
- [[Audio Mixing and Priority]]
- [[Music Direction]]
- [[Animation Bible]]
- [[VFX Bible]]
- [[Template - Sound]]
- [[Asset Register]]
- [[UI - Settings]]
