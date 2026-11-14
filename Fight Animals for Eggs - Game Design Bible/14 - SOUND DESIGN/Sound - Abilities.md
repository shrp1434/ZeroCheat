---
title: Sound - Abilities
type: asset-spec
category: audio
status: proposed
priority: P0
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - abilities
  - specials
  - combat
---

# Sound - Abilities

Sounds for the player specials (Power Strike, Ground Slam, Rally Cry, Dodge Roll) and for every animal ability archetype, with element and rarity layers (SFX-220 to SFX-269). Archetypes are defined in [[Animation - Animal Abilities]]; cooldown and ready cues are in [[Sound - UI Feedback]].

> [!success] CONFIRMED
> Special moves may have cooldowns (D-005). Animal abilities can be manual or automatic (D-008).

> [!info] PROPOSED
> All sounds and rules are **PROPOSED**. Gameplay values are from [[Canonical Proposed Values]] §4 and the [[Animal Abilities Catalogue]].

---

## 1. Construction of an ability sound

An ability sound = **archetype core** (fixed per archetype, teaches the shape of the move) + **element layer** (what it is made of) + optional **rarity accent** (Rare and above). Species vocals ([[Sound - Animal Vocalisations]]) may be added on the anticipation peak.

| Layer | Priority | Rule |
|---|---|---|
| Archetype core | V2 own team / V3 others | Always plays |
| Element layer | Same as core, −3 dB | Chosen by the ability's element in the catalogue |
| Rarity accent | Same as core, −9 dB | Rare and above; skipped on Low tier |
| Wild-cast telegraph | V1 if it targets the local player's area | Wild area abilities use the boss telegraph riser language, shortened ([[Sound - Bosses]]) |

Manual abilities additionally play the command whistle SFX-158 on input; automatic abilities do not.

---

## 2. Player specials

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-220 | Power Strike charge | Builds anticipation over the 12-frame charge | 0.35 s | Rising tone 400 Hz → 2 kHz + crackle | V2 own / V3 | S1 | ANI-223 f0 | 1 (tonal) | — |
| SFX-221 | Power Strike impact | Big single hit | 0.5 s | Body 80–250 Hz, crack 3–5 kHz, short tail | V2 / V3 | S2 | `Hit` "PS" | 3 | — |
| SFX-222 | Ground Slam wind-up | Crouch and leap | 0.5 s | Air rush rising | V2 / V3 | S1 | ANI-224 f0 | 2 | — |
| SFX-223 | Ground Slam impact | Area hit (10 studs) | 0.8 s | Boom 50–200 Hz, debris 1–4 kHz, ring tail | V2 / V3 | S2 | `Hit` "GS" | 3 | Boss slam lite layer |
| SFX-224 | Rally Cry swell | Gather | 0.3 s | Breath swell | V2 / V3 | S1 | ANI-225 f0 | 1 | — |
| SFX-225 | Rally Cry horn | Team buff (+15% damage for 6 s) announced | 1.0 s | Warm brass-like horn in a major fifth, 300 Hz–2 kHz | V2 own / V3 | S2 | ANI-225 f18 | 1 (tonal) | — |
| SFX-226 | Dodge Roll | Roll movement | 0.3 s | Cloth and air whoosh | V2 / V3 | S1 | ANI-226 f3 | 3 | Alias SFX-219 |
| SFX-227 | Rally Cry expiry | Buff ends | 0.3 s | Soft falling fifth | V3 | 2D own only | Buff end | 1 | Generic buff expiry for animal buffs at −6 dB |

SFX-228 and SFX-229 are reserved.

---

## 3. Archetype cores

| ID | Archetype | Core sound | Duration | Frequency | Spatial | Trigger | Variations |
|---|---|---|---|---|---|---|---|
| SFX-230 | Dash Strike | Short whoosh, sharp tail | 0.25 s | 400 Hz–4 kHz | S1 | Dash start f8 | 3 |
| SFX-231 | Pounce / Leap | Rising whoosh | 0.35 s | 300 Hz–3 kHz | S1 | Leap start f10 | 3 |
| SFX-232 | Charge | Snort at the tell, rolling rumble during the loop | 0.3 s + loop | 100 Hz–2 kHz | S2 | Tell f9, loop | 2 |
| SFX-233 | AoE Slam / Stomp | Thump with a ring tail; three size layers (small, medium, large) | 0.5–0.9 s | 60–400 Hz + ring 1–3 kHz | S2 | `Hit` f20 | 2 per size |
| SFX-234 | Channel Beam | Humming loop with start and stop tails | Loop | Tonal hum 300 Hz–2 kHz | S2 | `Release` / loop | 1 per element |
| SFX-235 | Heal Pulse | Soft major-third chime | 0.7 s | 800 Hz–4 kHz | S2 | `Cast` f12 | 2 |
| SFX-236 | Buff Call | Shimmer under the species call | 0.8 s | 2–8 kHz sparkle | S2 | `Cast` f10 | 2 |
| SFX-237 | Guard / Shell Up | Clamp-in thunk, low hum while held; release thunk (guard down) | 0.2 s + loop | 150 Hz–2 kHz | S1 | `Cast` f9 | 2 |
| SFX-238 | Taunt | Bold drum hit + vocal | 0.4 s | 80 Hz–2 kHz | S2 | `Cast` f12 | 2 |
| SFX-239 | Stun Burst | Twang burst with star tinkle tail | 0.5 s | 1–6 kHz | S2 | `Hit` f14 | 2 |
| SFX-240 | Tether Pull | Zip out, stretch, snap | 0.6 s | 500 Hz–4 kHz | S1 | `Release` f10 | 2 |
| SFX-241 | Zone Placement | Splat-settle, then a quiet zone loop | 0.3 s + loop | 200 Hz–3 kHz | S2 | `Cast` f13 | 2 |
| SFX-242 | Cone Breath / Spray | Inhale, then an element-textured spray loop | 0.5 s + loop | Element-dependent | S2 | In f0, loop f15 | 1 per element |
| SFX-243 | Burrow / Submerge | Dig or dive out, muffled travel rumble, burst in | 0.4 s + loop + 0.4 s | 80–800 Hz | S2 | Out f9, in f0 | 2 |
| SFX-244 | Call | Call ring chime + species call | 0.8 s | 1–4 kHz | S2 | `Cast` f18 | 1 |
| SFX-245 | Passive Proc | Tiny sparkle tick | 0.15 s | 3–7 kHz | S1 | `Cast` f3 | 3 |
| SFX-246 | Volley rhythm | Uses SFX-166 per release with a rising pitch pattern (+0, +2, +4 semitones) | — | — | S1 | `Release` f9, f15, f21 | — |
| SFX-247 | Guard down | Release thunk | 0.2 s | 150 Hz–1 kHz | S1 | Guard out | 2 |
| SFX-248 | Zone loop | Quiet hum while a zone persists | Loop | 200–800 Hz | S5 (Max 30) | While zone active | 1 per element |
| SFX-249 | Heal-over-time loop | Gentle shimmer on the target | Loop | 2–6 kHz, very quiet | S1 | While active | 1 |

---

## 4. Element layers

| ID | Element | Texture | Reuse |
|---|---|---|---|
| SFX-250 | Water | Splash, droplets, bubbling | Aquatic animals, Coast hazards |
| SFX-251 | Frost | Crystalline crackle, chime | Tundra animals |
| SFX-252 | Leaf | Rustle, flutter | Forest and Canopy animals |
| SFX-253 | Spark | Fizz, crackle (band-limited) | Electric Eel, sparks |
| SFX-254 | Wind | Gust, whoosh | Birds |
| SFX-255 | Ember-spark | Warm crackle (no roaring fire) | Caldera animals |
| SFX-256 | Bubble | Pops | Support orbs, Dolphin |
| SFX-257 | Petal | Soft flutter, chime | Display birds, Mythical accents |
| SFX-258 | Starlight | Bell shimmer (not the rarity intervals) | Starfall animals |
| SFX-259 | Earth | Gravel, thud | Stompers, burrowers |

## 5. Rarity accents

| ID | Rarity | Accent |
|---|---|---|
| SFX-260 | Rare | Thin bright ping on the cast |
| SFX-261 | Epic | Ping + short orbiting shimmer |
| SFX-262 | Legendary | Golden bell |
| SFX-263 | Mythical | Bell + petal flutter |
| SFX-264 | Secret | Prismatic chord shimmer |

SFX-265 to SFX-269 are reserved.

---

## 6. Overlap control

- At most 6 (Low 4) Abilities voices ([[Audio Mixing and Priority]]); own team first.
- Channel and spray loops: one per caster; a second loop from the same caster stops the first.
- Element layers are dropped first when the group is full; cores are kept.

## 7. Test hooks

- Every archetype recognisable with the element layer muted (core carries the meaning).
- Three Rally Cries from three players in one second: own horn at full, others at V3 levels, total voices within the cap.

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Animation - Animal Abilities]]
- [[Animation - Player Attacks and Specials]]
- [[Animal Abilities Catalogue]]
- [[Abilities and Cooldowns]]
- [[Sound - UI Feedback]]
- [[Sound - Combat Impacts]]
