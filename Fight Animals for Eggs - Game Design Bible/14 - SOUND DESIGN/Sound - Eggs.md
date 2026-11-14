---
title: Sound - Eggs
type: asset-spec
category: audio
status: mixed
priority: P0
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - eggs
  - egg-roll
  - hatching
  - merging
  - rarity
---

# Sound - Eggs

Sounds for egg rolls, hatches, merges and the Egg Merging Station (SFX-320 to SFX-369), and the rarity sound language shared with the music stingers MUS-31 to MUS-37 ([[Music Direction]]).

> [!success] CONFIRMED
> Seven rarities (D-003). Two-stage randomness: the roll decides rarity, the hatch picks the animal (D-015). Up to five eggs hatched at once (D-016). Merge 3 → 1 at an Egg Merging Station (D-020).

> [!danger] Honest audio
> Reveal sounds follow the same rule as the visuals ([[Animation Bible]] §6): during a roll build, no sound associated with a higher tier than the true result may play. Build pulses are neutral; a tier's own sound plays only at its reveal. Lengths never vary with spend or history ([[Randomised Reward Compliance]]).

> [!info] PROPOSED
> All sounds, musical intervals and rules are **PROPOSED**.

---

## 1. Rarity sound language

Each tier adds one musical element, so tiers are recognisable by ear and with the visuals off.

| Tier | Interval / harmony | Instrument colour | Tier layer duration | Sparkle band |
|---|---|---|---:|---|
| Common | Single note | Wooden marimba | 0.5 s | — |
| Uncommon | Rising major second | Marimba + soft flute | 0.7 s | — |
| Rare | Major-third arpeggio | Glockenspiel | 0.9 s | 4–6 kHz |
| Epic | Major triad with a suspended-fourth resolve | Celesta + string pad | 1.2 s | 4–8 kHz |
| Legendary | Full major chord with brass swell | Brass + bell | 1.6 s | 6–10 kHz |
| Mythical | Major chord with added ninth, harp glissando | Harp + choir pad ("ah") | 2.0 s | 6–10 kHz |
| Secret | Lydian chord (raised fourth), slow bloom | Music box + choir + soft deep swell | 2.5 s | Full shimmer |

The intervals are reserved: ambience, UI and other music never use these exact figures ([[Sound - Ambient World]] §3).

---

## 2. Egg roll ([[Animation - Egg Roll]])

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-320 | Shrine activate | Roll begins | 0.6 s | Soft drone swell + chime | V2 | 2D for the roller | Phase A f0 | 1 | — |
| SFX-321 | Egg land | Mystery egg lands in the cradle | 0.2 s | Wooden knock | V2 | 2D | f12 | 3 | Hatch pop landing |
| SFX-322 | Wobble tick | Anticipation | 0.1 s | Wood tick | V2 | 2D | Wobbles | 4 | — |
| SFX-323 | Build pulse | One per pulse (1 to 7) | 0.3 s | Soft neutral bell; pulse *n* plays scale degree *n* of a neutral pentatonic set (discrete notes, never a continuous rising sweep, which is reserved for danger) | V2 | 2D | Each pulse | 7 pitches | — |
| SFX-324 | Crack | Shell cracks | 0.3 s (Epic+ adds a 0.4 s sustain) | Crisp crackle 1–5 kHz | V2 | 2D | Phase C | 3 | Hatch crack |
| SFX-325 | Roll reveal — Common layer | Tier identity | 0.5 s | See §1 | V2 | 2D | Reveal frame | 1 | Merge output at −3 dB |
| SFX-326 | Roll reveal — Uncommon layer | | 0.7 s | | V2 | 2D | | 1 | |
| SFX-327 | Roll reveal — Rare layer | | 0.9 s | | V2 | 2D | | 1 | |
| SFX-328 | Roll reveal — Epic layer | | 1.2 s | | V2 | 2D | | 1 | |
| SFX-329 | Roll reveal — Legendary layer | | 1.6 s | | V1 | 2D | | 1 | |
| SFX-330 | Roll reveal — Mythical layer | | 2.0 s | | V1 | 2D | | 1 | |
| SFX-331 | Roll reveal — Secret layer | | 2.5 s | | V1 | 2D | | 1 | |
| SFX-332 | Storage arrival | Egg reaches backpack or base storage icon | 0.2 s | Soft pop + counter tick | V2 | 2D | Flight end | 2 | Merge, hatch collection |
| SFX-333 | Skip | Jump to result | 0.2 s | Quick whoosh | V2 | 2D | Skip | 1 | Hatch, merge, ascension skips |
| SFX-334 | Roll refused | No egg | 0.4 s | Soft falling two-note, muted | V2 | 2D | ANI-413 | 1 | — |

**Secret build:** the local night grade in phase B is accompanied by the music dropping out (not by an SFX), so the sound of the Secret build is silence plus pulses; no higher-tier sound is implied for other tiers.

**Roll ×5:** each egg plays its own crack and tier layer at its own reveal; only the highest tier's layer plays at full level, others at −6 dB; one stinger at the end ([[Audio Mixing and Priority]] §4).

---

## 3. Hatch ([[Animation - Egg Hatch]])

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-335 | Pop to stage | Egg moves to the stage | 0.3 s | Pop + whoosh | V2 | 2D | f0 | 2 | — |
| SFX-336 | Hatch wobble | Wobble build | 0.15 s | Wood knock pitched by rarity (Common lowest) | V2 | 2D | f12, f20, f28 | 3 per rarity pitch | — |
| SFX-337 | Crack build | Cracks spreading | 0.4 s | Crackle with rising density (not rising pitch) | V2 | 2D | f36 | 2 | — |
| SFX-338 | Shell burst | Burst | 0.4 s | Pop-crack + shell patter | V2 | 2D | f48 | 3 | Multi-hatch at −6 dB for non-centre eggs |
| SFX-339 | Hatch tier layer — Common | Rarity colour of the hatch | 0.5 s | §1 | V2 | 2D | f48 | 1 | Shares stems with SFX-325 |
| SFX-340 | Hatch tier layer — Uncommon | | 0.7 s | | V2 | 2D | | 1 | SFX-326 |
| SFX-341 | Hatch tier layer — Rare | | 0.9 s | | V2 | 2D | | 1 | SFX-327 |
| SFX-342 | Hatch tier layer — Epic | | 1.2 s | | V2 | 2D | | 1 | SFX-328 |
| SFX-343 | Hatch tier layer — Legendary | | 1.6 s | | V1 | 2D | | 1 | SFX-329 |
| SFX-344 | Hatch tier layer — Mythical | | 2.0 s | | V1 | 2D | | 1 | SFX-330 |
| SFX-345 | Hatch tier layer — Secret | | 2.5 s | | V1 | 2D | | 1 | SFX-331 |
| SFX-346 | New discovery chime | First time owning this species | 0.8 s | Bright rising three-note figure | V2 | 2D | f63 | 1 | Index screen "new" |
| SFX-347 | Duplicate tick | Duplicate hatched (positive: ascension progress) | 0.4 s | Warm double tick + small chime | V2 | 2D | f63 | 1 | Ascension progress UI |
| SFX-348 | Fly to collection | Animal sent to the collection | 0.3 s | Whoosh + pop | V2 | 2D | End | 2 | — |
| SFX-349 | Hatch refused | Not allowed (combat, base egg away from base) | 0.4 s | Muted thunk | V2 | 2D | ANI-429 | 1 | — |

The species hatch call ([[Sound - Animal Vocalisations]] event 5) plays at f66 in 2D.

---

## 4. Merge and the Egg Merging Station ([[Animation - Egg Merge]])

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-350 | Egg insert | Each input egg lands in the station | 0.15 s | Knock, material by station level | V2 | 2D for the merger | Insert | 3 per level | — |
| SFX-351 | Mechanism L1 — Twig Nest Press | Creak, rustle, wooden lever | Loop over the process phase | Wood 300 Hz–3 kHz | V2 | 2D (S2 for visitors) | Process | — | — |
| SFX-352 | Mechanism L2 — Stonebound Hatchery Forge | Bellows, stone hammer stamps | Loop | Stone 100 Hz–2 kHz | V2 | 2D / S2 | Process | — | Hammer stamps on beat |
| SFX-353 | Mechanism L3 — Crystal Incubator | Ring hum, crystal chimes | Loop | 800 Hz–6 kHz | V2 | 2D / S2 | Process | — | — |
| SFX-354 | Mechanism L4 — Aurora Crucible | Airy shimmer, orbit whooshes | Loop | Broadband shimmer | V2 | 2D / S2 | Process | — | — |
| SFX-355 | Mechanism L5 — Celestial Convergence Altar | Celestial chime bed, dial clicks, beam descent | Loop | Bells 1–8 kHz, low swell | V2 | 2D / S2 | Process | — | — |
| SFX-356 | Fusion | Flash moment | 0.5–1.0 s (longer for higher tiers) | Bright burst + whoosh | V2 | 2D | Fuse phase | 1 per tier length | — |
| SFX-357 | Output emerge | New egg appears; the output tier layer (SFX-325 to SFX-331) is added at −3 dB | 0.5 s + tier layer | Pop + tier | V2 (V1 for Legendary and above) | 2D | Emerge | 1 | — |
| SFX-358 | Station transformation | Upgrade rebuilds the station (D-020) | 3.0 s | Parts whoosh, assembly clunks in three waves, completion chord | V2 | 2D / S2 | ANI-473 to ANI-476 | 1 | Base upgrade grammar |
| SFX-359 | Merge refused | Station rejects eggs | 0.4 s | Bounce + muted two-note | V2 | 2D | ANI-477 | 1 | — |
| SFX-360 | Station idle L1 | Presence | Loop | Leaves, very quiet | V5 | S5 (Max 30) | Idle | — | — |
| SFX-361 | Station idle L2 | | Loop | Rune hum | V5 | S5 | Idle | — | — |
| SFX-362 | Station idle L3 | | Loop | Crystal ring | V5 | S5 | Idle | — | — |
| SFX-363 | Station idle L4 | | Loop | Aurora shimmer | V5 | S5 | Idle | — | — |
| SFX-364 | Station idle L5 | | Loop | Starry drone | V5 | S5 | Idle | — | — |
| SFX-365 | Station first build | Purchase reveal | 3.0 s | As SFX-358 with an extra opening flourish | V2 | 2D | ANI-478 | 1 | — |

SFX-366 to SFX-369 are reserved.

---

## 5. Test hooks

| Test | Expected |
|---|---|
| Record the audio of every non-Secret roll | No tier layer other than the true tier; no build sound differs from the neutral pulses |
| ×5 roll with two Epics | One Epic stinger; the other Epic's tier layer at −6 dB |
| Blindfolded listening test | Testers identify each tier from SFX-325 to SFX-331 with ≥ 90% accuracy |

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Music Direction]]
- [[Animation - Egg Roll]]
- [[Animation - Egg Hatch]]
- [[Animation - Egg Merge]]
- [[Egg Merging Station]]
- [[Randomised Reward Compliance]]
- [[UI - Egg Rolling]]
