---
title: Sound - Bosses
type: asset-spec
category: audio
status: mixed
priority: P1
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - bosses
  - telegraphs
---

# Sound - Bosses

Boss telegraph language, attack sounds, intro, phase and defeat sounds, and one voice palette per boss (SFX-270 to SFX-319). Animation templates are in [[Animation - Boss Attacks]]; boss music in [[Music Direction]].

> [!success] CONFIRMED
> Mini-bosses and world bosses exist (D-012).

> [!info] PROPOSED
> All sounds and rules are **PROPOSED**. Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]); no sound implies a specific reward.

---

## 1. Telegraph language

The rising-pitch riser is the game's single "danger is coming" sound. It is never used for anything friendly and never appears in music or ambience ([[Sound Bible]] §6).

| Rule | Value |
|---|---|
| Riser shape | Starts at ~600 Hz, rises to ~3 kHz, ends exactly on the damage frame with a short "click" so the dodge moment is audible |
| Length-matched variants | SFX-271 is authored in five lengths: 0.8, 1.2, 1.5, 2.0 and 2.5 s, matching the telegraph minimums ([[Animation - Boss Attacks]] §1). Longer telegraphs pick the nearest shorter variant and pre-roll a quiet bed |
| Priority | V1 for players inside 1.5 × the attack radius; V3 beyond |
| Spatial | S3 (`InverseTapered`, Min 15, Max 200), emitted from the attack centre, not the boss body, so players hear where the danger lands |
| Ducking | Music −6 dB, Ambience −6 dB, Combat −3 dB during the riser ([[Audio Mixing and Priority]] §5) |
| Wild-cast area abilities | Use the 0.8 s variant at −6 dB ([[Sound - Abilities]]) |

---

## 2. Shared boss sound register

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-270 | Boss spawn announcement | Server-wide notice 2 min before a world boss spawn ([[Canonical Proposed Values]] §5) | 2.0 s | Distant horn chord | V2 | 2D | Announcement | 1 per world boss (pitch) | Rare-spawn beacon pairs with it |
| SFX-271 | Telegraph riser | Danger countdown | 0.8–2.5 s | 600 Hz → 3 kHz | V1 | S3 | Telegraph f0 | 5 lengths | Wild-cast abilities |
| SFX-272 | Slam impact | Circle attack lands | 1.0 s | Boom 40–200 Hz, debris 1–4 kHz | V1 in radius / V3 | S3 | Slam `Hit` | 3 | Quake pulse layer |
| SFX-273 | Sweep whoosh | Arc attack | 0.6 s | Heavy air 200 Hz–2 kHz | V2 / V3 | S3 | Sweep travel | 3 | — |
| SFX-274 | Charge run and impact | Line attack | Loop + 0.8 s | Rumble 50–300 Hz + impact | V2 / V3 | S3 | Charge loop | 2 | — |
| SFX-275 | Roar | Enrage or buff | 2.0 s | Per boss voice palette (§3) | V2 | S3 | Roar `Cast` | per boss | — |
| SFX-276 | Phase transition | New phase begins | 2.5 s | Rising whoosh + shockwave | V1 | S3 | ANI-333 f30 | 1 | — |
| SFX-277 | Breath or cone loop | Cone attack (wind, frost, ember sparks, spores) | Loop | Element textures from [[Sound - Abilities]] §4 at boss scale | V2 | S3 | `Release` | 1 per element | — |
| SFX-278 | Volley launch and incoming whistle | Targeted volley | 0.5 s + per-marker whistle ending on impact | 1–4 kHz whistle | V1 for the targeted player | S3 | Volley markers | 2 | — |
| SFX-279 | Quake rumble and pulse | Ring or donut attack | 2.0 s build + 0.8 s pulse | 30–150 Hz rumble (with a 500 Hz–2 kHz rattle for phones) | V1 | S3 | Quake | 1 | — |
| SFX-280 | Summon call | Helpers spawning | 1.5 s | Horn-like call + region texture | V2 | S3 | Summon `Cast` | 1 | — |
| SFX-281 | Ultimate charge bed | Ultimate telegraph (2.0–2.5 s) under the riser | 2.5 s | Swelling chord | V1 | S3 | Ultimate f15 | 1 | — |
| SFX-282 | Ultimate impact | Ultimate lands | 1.5 s | Full-range boom, long tail | V1 | S3 | Ultimate f75 | 1 | — |
| SFX-283 | Vulnerable ring | "Attack now" cue when the boss is staggered | 1.0 s | Bright bell 2–5 kHz | V2 | S3 | Stagger in | 1 | — |
| SFX-284 | Boss hurt | Damage feedback on the boss (rate-limited 1 per 0.8 s) | 0.4 s | Per boss voice | V3 | S3 | Damage | per boss | — |
| SFX-285 | Boss defeat | Victory moment | 3.0 s | Soft descending call + golden shimmer | V1 | S3 + 2D shimmer | ANI-334 f60 | per boss | — |
| SFX-286 | Intro arrival | Spawn reveal | 3.0 s | Arrival texture (ground rise, sky landing, water surge) + call | V2 | S3 | ANI-320 | per boss | — |
| SFX-287 | Enrage loop | Enraged state | Loop | Low pulsing growl bed, quiet | V3 | S3 | Enrage active | 1 | — |
| SFX-288 | Leash reset | Boss returns home and heals | 1.5 s | Soft rewind whoosh + heal chime | V3 | S3 | Leash return | 1 | — |
| SFX-289 | Boss footsteps | Weight | 0.3–0.5 s | 40–200 Hz + 1–3 kHz click | V3 | S3 | Foot markers | 3 per scale | — |
| SFX-290 | Flight dive whistle | Flying boss dive | 1.5 s | Descending whistle ending on impact | V1 for targeted area | S3 | ANI-336 | 1 | — |
| SFX-291 | Dive and resurface surge | Air-swim boss resurfacing | 1.2 s | Water surge 80 Hz–3 kHz | V1 for targeted area | S3 | ANI-337 | 1 | — |
| SFX-292 | Boss idle breath | Presence | Loop | Low breath | V4 | S3 | Idle | per boss | — |

SFX-293 to SFX-299 are reserved.

---

## 3. Boss voice palettes

Each boss has one palette ID covering its roar, hurt, intro call and defeat call. Palettes are designed from real animal sources of the boss's base animal, slowed and layered; no monster libraries, no screams.

| ID | Boss | Source direction |
|---|---|---|
| SFX-300 | [[Mini-Boss - Bramblehorn]] | Defined in the boss document's base animal; woody creaks layered in |
| SFX-301 | [[Mini-Boss - Dustmane]] | As above; dry dusty breath layer |
| SFX-302 | [[Mini-Boss - Vinecoil]] | As above; vine rustle layer |
| SFX-303 | [[Mini-Boss - Hammertide]] | As above; water surge layer |
| SFX-304 | [[Mini-Boss - Rimeback]] | As above; ice crackle layer |
| SFX-305 | [[Mini-Boss - Stormtalon]] | As above; wind layer |
| SFX-306 | [[Mini-Boss - Cinderjaw]] | As above; ember crackle layer |
| SFX-307 | [[Mini-Boss - Eclipse Panther]] | As above; starlight shimmer layer |
| SFX-308 | [[World Boss - Ironbark Colossus]] | Ancient tortoise: deep slow breaths, wood groans from the shell forest |
| SFX-309 | [[World Boss - Thunderhoof]] | Storm elephant: trumpet layered with rolling (non-flashing) thunder rumble |
| SFX-310 | [[World Boss - Abyssal Leviathan]] | Giant whale: song phrases pitched up for phones, deep water surges |
| SFX-311 | [[World Boss - Ashwing Condor]] | Ember-feathered condor: wing whumps, softened calls, warm crackle |

SFX-312 to SFX-319 are reserved for new bosses.

---

## 4. Mix during boss fights

- Bosses group: 6 voices (Low 4). V1 telegraphs never stolen.
- Up to 16 players' combat continues under the boss mix at Combat −12 dB; boss risers sit 9 dB above it.
- Boss music takes over from region music on the intro ([[Music Direction]]).

## 5. Test hooks

| Test | Expected |
|---|---|
| Telegraph riser vs damage frame | Riser click within 1 frame (33 ms) of the damage frame |
| Player outside 1.5 × radius | Riser at V3 level, no ducking |
| Five telegraphs at once (targeted volley) | All audible; Bosses group may exceed by one for V1 ([[Audio Mixing and Priority]] §3) |

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Animation - Boss Attacks]]
- [[Boss Design Overview]]
- [[Boss AI]]
- [[Music Direction]]
- [[UI - Boss Health Bar]]
