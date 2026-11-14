---
title: Sound - Combat Impacts
type: asset-spec
category: audio
status: proposed
priority: P0
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - combat
  - impacts
  - foley
---

# Sound - Combat Impacts

Player swings and hits, animal basic hits, projectiles, status sounds, defeat and KO, and movement foley (SFX-150 to SFX-219). Player specials and ability archetypes are in [[Sound - Abilities]]; vocals in [[Sound - Animal Vocalisations]].

> [!info] PROPOSED
> All sounds and rules are **PROPOSED**. Timings follow the animation documents ([[Animation - Player Attacks and Specials]], [[Animation - Animal Attacks and Hit Reactions]]).

---

## 1. Impact design rules

- **Two layers:** a body (120–500 Hz, gives weight) and a transient (2–5 kHz, carries on phone speakers). The transient is what players hear on mobile; it must be distinct per impact family.
- **Toy-like, not flesh:** wooden thocks, padded thumps, rubbery boinks, leafy swishes. No bone cracks, no wet hits, no cries.
- **Own hits louder than others':** the local player and their companions route to PlayerCombat (−6 dB); everyone else to Combat (−12 dB) ([[Audio Mixing and Priority]]).
- **Triggered on the client** by the `Hit` marker for cosmetic sync, but suppressed if the server's damage event does not arrive within 0.25 s (a predicted swing that the server rejected plays its whoosh but no impact).

---

## 2. Player attacks and reactions

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-150 | Swing whoosh (light) | Combo hits 1–2 wind-up | 0.15 s | 400 Hz–3 kHz air | V2 own / V3 | S1 | Strike start (f8, f9 @60) | 4 | Hit 2 pitched +5% |
| SFX-151 | Swing whoosh (heavy) | Finisher | 0.25 s | 200 Hz–2 kHz | V2 / V3 | S1 | Finisher f13 | 3 | — |
| SFX-152 | Hit impact (light) | Combo hits 1–2 contact | 0.12 s | Thock body 200–400 Hz + click 3 kHz | V2 / V3 | S1 | `Hit` marker | 5 | — |
| SFX-153 | Hit impact (finisher) | Hit 3 contact | 0.3 s | Body 120–300 Hz + bright crack 4 kHz | V2 / V3 | S1 | `Hit` "3" | 3 | Ability heavy hits at −3 dB |
| SFX-154 | Player hit taken | Feedback when the local player is damaged | 0.15 s | Padded thump 150–500 Hz + soft "puff" | V2 (own only) | 2D for self, S1 for others at −6 dB | Damage event | 4 | — |
| SFX-155 | Player knockdown | Heavy hit lands the player | 0.4 s | Thud + dust | V2 | 2D self / S1 | ANI-230 f11 | 2 | — |
| SFX-156 | Player defeated | Neutral downed cue (penalties **UNDECIDED**, [[Open Questions#Q-014]]) | 1.0 s | Soft descending three-note mallet | V2 | 2D self only | Defeat state | 1 | — |
| SFX-157 | Player respawn / revive | Return to play | 1.0 s | Rising shimmer | V2 | 2D self / S1 | ANI-232 | 1 | KO recovery at −6 dB |
| SFX-158 | Command whistle | Manual target or manual ability order confirmed | 0.2 s | Two-note whistle 1.5–3 kHz | V2 | 2D | On command input ([[Targeting and Command System]]) | 2 | — |

SFX-159 is reserved.

---

## 3. Animal basic hits, projectiles and status

| ID | Sound | Purpose | Duration | Frequency | Priority | Spatial | Trigger | Variations | Reuse |
|---|---|---|---|---|---|---|---|---|---|
| SFX-160 | Blunt hit (bump, headbutt, slam) | Tank and Bruiser basic contacts | 0.15 s | Thump 120–400 Hz + knock 2.5 kHz | V2 own / V3 | S1 | `Hit` marker | 5 | Size band shifts pitch (−3 to +4 semitones) |
| SFX-161 | Swipe hit (claw, paw, wing) | Assassin and Skirmisher contacts | 0.12 s | Swish 1–4 kHz + soft thock | V2 / V3 | S1 | `Hit` | 5 | — |
| SFX-162 | Snap hit (jaw clack) | Bite-style contacts; a wooden clack, not a bite into flesh | 0.1 s | Clack 1.5–4 kHz | V2 / V3 | S1 | `Hit` | 4 | — |
| SFX-163 | Heavy impact | Staggers, Tank hits on large targets, knockback landings | 0.35 s | Deep thump 80–250 Hz + crack 3 kHz | V2 / V3 | S2 | Stagger, heavy contacts | 3 | Boss slams layer |
| SFX-164 | Peck and talon tick | Bird contacts | 0.08 s | Tick 3–6 kHz | V2 / V3 | S1 | `Hit` | 4 | Woodpecker drum overlay |
| SFX-165 | Water slap | Aquatic contacts | 0.15 s | Splash slap 300 Hz–3 kHz | V2 / V3 | S1 | `Hit` | 4 | — |
| SFX-166 | Projectile launch | Ranged and Support releases | 0.12 s | Pop 500 Hz–2 kHz | V2 / V3 | S1 | `Release` marker | 4 | Volley ±6% pitch per shot |
| SFX-167 | Projectile travel | Fly-by for projectiles passing within 6 studs of the listener | 0.3 s | Whistle 1–3 kHz | V4 | S1 | Fly-by test | 2 | — |
| SFX-168 | Projectile impact | Projectile hits | 0.15 s | Soft splat-pop | V2 / V3 | S1 | Impact | 4 | Element variants (water, spark, leaf) |
| SFX-169 | Support orb impact | Support basic hits | 0.2 s | Chime-thud | V3 | S1 | Impact | 3 | — |
| SFX-170 | Zap impact | Electric Eel and spark elements | 0.15 s | Crackle 2–6 kHz, band-limited | V3 | S1 | Impact | 3 | Eel vocal crackle |
| SFX-171 | Stun twinkle loop | Stunned target | Loop 1.0 s | Tinkling 3–7 kHz, quiet | V3 (V2 if own) | S1 | Stun state | 1 | KO stars at −6 dB |
| SFX-172 | Knockback whoosh | A body flung by knockback | 0.3 s | Whoosh 300 Hz–2 kHz | V3 | S1 | Knockback start | 2 | — |
| SFX-173 | Wild defeat poof | Wild animal dissolves | 0.6 s | Soft pop + sparkle | V3 | S1 | ANI-18x f28 | 3 | — |
| SFX-174 | Companion KO thump | Own or guard animal knocked out | 0.5 s | Padded thump + daze wobble | V2 own / V3 | S2 | KO entry f19 | 2 | Raid defenders (V2 for the defender) |
| SFX-175 | KO recover chime | Animal gets up | 0.6 s | Rising chime | V3 | S1 | Recovery f15 | 1 | — |
| SFX-176 | Hit on guard | A hit absorbed by a guard ability | 0.12 s | Tink 2–4 kHz | V3 | S1 | Guard loop hit | 3 | Shield ripples at −3 dB |
| SFX-177 | Blocked / invulnerable | A hit negated by Dodge Roll invulnerability or immunity | 0.15 s | Clean tink + air | V2 | S1 | Server "negated" result | 2 | — |
| SFX-178 | Combat enter cue | Subtle cue when the player enters combat (combat tag starts) | 0.3 s | Low soft drum | V3 | 2D | Combat tag starts | 1 | — |
| SFX-179 | Combat exit cue | Combat tag ends (8 s, [[Canonical Proposed Values]] §4) | 0.4 s | Relieved soft chord | V4 | 2D | Tag ends | 1 | — |

SFX-180 to SFX-199 are reserved.

---

## 4. Movement foley

Triggered by foot markers ([[Animation - Animal Locomotion]]) at LOD A0 only; routed to Foley (V4).

| ID | Sound | Used by | Duration | Frequency | Spatial | Variations | Surface variants |
|---|---|---|---|---|---|---|---|
| SFX-200 | Tiny patter | Tiny band (not marker-driven: a 0.5 s pattering loop while moving) | Loop | 2–5 kHz | S1 (Max 20 override) | 2 | Grass, sand, snow, stone |
| SFX-201 | Small paw | Small band | 0.08 s | 1–3 kHz | S1 | 4 | Same |
| SFX-202 | Medium paw | Felines, canines, bears | 0.12 s | 300 Hz–2 kHz | S1 | 4 | Same |
| SFX-203 | Hoof | Ungulates | 0.1 s | Clop 800 Hz–3 kHz | S1 | 4 | Same |
| SFX-204 | Heavy pad | Large plantigrades, Gorilla knuckles | 0.15 s | 150–800 Hz | S1 | 4 | Same |
| SFX-205 | Pachyderm thud | Elephant, Rhino, Hippo, Mammoth, Colossus-scale companions | 0.25 s | 60–300 Hz + dust | S2 | 3 | Same |
| SFX-206 | Prehistoric stomp | T-Rex | 0.3 s | 50–250 Hz + click | S2 | 3 | Same |
| SFX-207 | Bird hop step | Ground birds | 0.06 s | 2–4 kHz | S1 | 3 | — |
| SFX-208 | Wing flap (small) | Small birds | 0.15 s | Flutter 500 Hz–3 kHz | S1 | 3 | — |
| SFX-209 | Wing flap (large) | Raptors, Quetzalcoatlus | 0.3 s | Whump 150 Hz–1.5 kHz | S2 | 3 | — |
| SFX-210 | Slither scrape | Serpents (loop, volume by speed) | Loop | Noise 1–4 kHz, soft | S1 | 2 | Sand, grass |
| SFX-211 | Air-swim swish | Air-swimming aquatic animals (loop, D-043) | Loop | Watery swish 300 Hz–3 kHz | S1 | 2 | — |
| SFX-212 | Crab scuttle | Crab | Loop | Clicks 2–5 kHz | S1 | 2 | — |
| SFX-213 | Hop landing | Rabbit, Frog, Kangaroo | 0.1 s | Soft thump | S1 | 3 | Same |
| SFX-214 | Belly slide | Penguin | Loop | Shush 1–5 kHz | S1 | 1 | Snow, sand |
| SFX-215 | Jump take-off | All | 0.1 s | Push | S1 | 2 | — |
| SFX-216 | Landing | All, knockback landings | 0.15 s | Thump | S1 | 3 | Same |
| SFX-217 | Player footsteps | Player avatars (replacing default footsteps only if engineering chooses to, see note) | 0.08 s | 500 Hz–3 kHz | S1 | 4 | Same |
| SFX-218 | Catch-up swirl | Companion catch-up out and in | 0.4 s | Whoosh + sparkle | S1 | 1 | — |
| SFX-219 | Dodge roll cloth (alias of SFX-226) | Kept for foley grouping | — | — | — | — | — |

Note on SFX-217: Roblox characters have default footstep sounds; whether to replace them is an engineering decision for [[Client Controllers]]. If replaced, surface detection uses the material under the character.

---

## 5. Test hooks

| Test | Expected |
|---|---|
| Server rejects a predicted Power Strike | Whoosh plays, no impact sound |
| 30 wild hits in 1 s on one target | Merged impacts, Combat group cap respected |
| Phone speaker test | Every impact family distinguishable at 50% volume by its transient |

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Sound - Abilities]]
- [[Sound - Animal Vocalisations]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Animation - Player Attacks and Specials]]
- [[Combat Feedback and Readability]]
