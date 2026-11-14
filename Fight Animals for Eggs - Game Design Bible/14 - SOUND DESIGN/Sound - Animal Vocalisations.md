---
title: Sound - Animal Vocalisations
type: asset-spec
category: audio
status: proposed
priority: P1
owner: Sound Designer
last_updated: 2026-11-14
tags:
  - audio
  - animals
  - vocalisations
  - creatures
---

# Sound - Animal Vocalisations

Vocal palettes for all 60 launch animals, built from 19 vocal families with five event types each (SFX-001 to SFX-095), plus per-species pitch and layer rules. Footsteps and movement foley are in [[Sound - Combat Impacts]]; ability layers in [[Sound - Abilities]].

> [!info] PROPOSED
> Families, events and mapping are **PROPOSED**. The roster is **PROPOSED** (D-032, [[Open Questions#Q-002]]); if a species changes, it is re-mapped to a family, not given a new palette.

---

## 1. Event types (shared by every family)

| Event | Purpose | Duration | Priority | Spatial | Trigger | Variations | Cooldown |
|---|---|---|---|---|---|---|---|
| 1 Idle call | Life and species identity | 0.4–1.5 s | V4 | S1 (small) / S2 (Large and up) | Random every 8–15 s while idle, not in combat | 3 | [[Audio Mixing and Priority]] §4 |
| 2 Attack effort | Sells the strike | 0.15–0.4 s | V3 (V2 for own team) | S1 / S2 | `SFX` marker on the attack's anticipation peak | 4 | Every 2nd attack for Skirmishers |
| 3 Hurt | Hit feedback (a huff, never a pain cry) | 0.15–0.3 s | V3 (V2 own team) | S1 / S2 | Damage event, with flinch or stagger | 4 | 0.6 s per animal |
| 4 KO / daze | Marks the knock-out; dazed and sleepy, not distressed | 0.8–1.4 s | V2 (own team and raid defenders), V3 others | S2 | KO entry f19 ([[Animation - Animal Defeat and Victory]]) | 2 | Once per KO |
| 5 Victory / hatch call | Pride and joy; also used at hatch reveal and showcase | 0.6–1.6 s | V2 (own) / V3 | S2, or 2D in hatch and ascension | Victory peak marker; hatch f66 | 3 | Once per event |

**Frequency rule for every family:** fundamental and formants sit in 250 Hz–3 kHz so they survive phone speakers. Large animals add a separate chest layer (80–200 Hz) that is a sub-sound in the same template and is skipped on the Low tier.

---

## 2. Family register

| Family | IDs (events 1–5) | Character | Frequency character | Reuse notes |
|---|---|---|---|---|
| F01 Small mammal | SFX-001–005 | Chitters, squeaks, soft chirrups, foot-thump (Rabbit) | 1–4 kHz, short | Squirrel and Meerkat chirps differ by pitch and rhythm only |
| F02 Canine and fox | SFX-006–010 | Yips, barks, playful growls, howl for victory | 400 Hz–2.5 kHz | Wolf howl is the family victory call; foxes use a yip variant |
| F03 Big cat | SFX-011–015 | Chuffs, purr-rumbles, short snarls, roar for victory | 150 Hz–2 kHz + chest | Cheetah uses chirps instead of roars (true to species) |
| F04 Ungulate | SFX-016–020 | Snorts, bleats, whinny-brays, grunts | 300 Hz–3 kHz | Boar grunts, Goat bleats, Zebra barks, Deer bleats |
| F05 Bear | SFX-021–025 | Huffs, moans, woofs | 120 Hz–1.5 kHz + chest | Panda uses softer bleats |
| F06 Pachyderm | SFX-026–030 | Trumpets, rumbles, snorts | 100 Hz–2 kHz + chest | Hippo uses honk-grunts; Rhino snorts |
| F07 Primate | SFX-031–035 | Hoots, chatters, chest-beat layer (Gorilla) | 300 Hz–3 kHz | Chest beat is foley-like and shared with the Buff Call ability |
| F08 Kangaroo | SFX-036–040 | Clucks, grunts, coughs | 300 Hz–2 kHz | Tail-thump foley layer on the attack effort |
| F09 Small bird | SFX-041–045 | Chirps, trills, rattles (Woodpecker drum, Toucan croak) | 2–6 kHz | Woodpecker drum doubles as its attack effort |
| F10 Waterfowl and display birds | SFX-046–050 | Quacks, honks, peacock call | 500 Hz–3 kHz | Peacock call is loud: idle call capped at once per 30 s |
| F11 Raptor | SFX-051–055 | Screeches (softened), hoots (Owl), kek calls (Falcon) | 1.5–5 kHz | Owl hoots are low and calm; no shrill screams |
| F12 Penguin | SFX-056–060 | Brays, squawks, flipper pats | 500 Hz–3 kHz | |
| F13 Reptile | SFX-061–065 | Hisses (shaped, not harsh), jaw clacks, low rumbles (Crocodile, Komodo) | Noise 2–6 kHz + 100–300 Hz rumble | Hiss is band-limited so it does not mask telegraph risers |
| F14 Frog | SFX-066–070 | Croaks, ribbits, tongue "thwip" | 400 Hz–2.5 kHz | Tongue thwip shared with the Tether Pull archetype for Frog |
| F15 Crustacean and cephalopod | SFX-071–075 | Non-vocal: clicks and claw clacks (Crab), bubble burbles and water swirls (Octopus, Giant Squid) | 1–5 kHz clicks; bubbles 300 Hz–2 kHz | No squelch or slime sounds |
| F16 Pinniped | SFX-076–080 | Barks (Seal), bellows (Walrus) | 200 Hz–2 kHz | |
| F17 Cetacean | SFX-081–085 | Clicks and whistles (Dolphin, Orca, Narwhal), long song phrases (Blue Whale) | 800 Hz–6 kHz whistles; Blue Whale song 100 Hz–1 kHz shifted up | Blue Whale song is pitched up to remain audible on phones |
| F18 Shark and eel | SFX-086–090 | Non-vocal: water-surge whooshes, jaw clacks, electric crackle (Electric Eel) | 200 Hz–4 kHz | Crackle layer reused for Eel ability zaps |
| F19 Prehistoric | SFX-091–095 | Designed calls: deep bellows and rumbles (T-Rex), wind-like pterosaur calls (Quetzalcoatlus), sea-roar surges (Mosasaurus) | 80 Hz–2.5 kHz + chest | Designed from real animal sources (birds, crocodilians, large mammals), not from monster libraries |

SFX-096 to SFX-099 are reserved.

---

## 3. Species mapping

Pitch offset in semitones is applied with `PlaybackSpeed` on top of the ±5% random variation. Default offsets by size band ([[Animal Rig Standards]] §5): Tiny +5, Small +3, Medium 0, Large −3, Colossal −5. Overrides are noted.

| Animal | Family | Pitch | Note |
|---|---|---:|---|
| [[Rabbit]] | F01 | +5 | Foot-thump idle |
| [[Squirrel]] | F01 | +5 | Rapid chatter |
| [[Hedgehog]] | F01 | +5 | Snuffles and huffs |
| [[Raccoon]] | F01 | +3 | Chirrs |
| [[Frog]] | F14 | +5 | Ribbit |
| [[Duck]] | F10 | +3 | Quack |
| [[Woodpecker]] | F09 | +3 | Drum |
| [[Boar]] | F04 | 0 | Grunts |
| [[Goat]] | F04 | 0 | Bleat |
| [[Meerkat]] | F01 | +5 | Alarm peeps |
| [[Zebra]] | F04 | 0 | Barking bray |
| [[Crab]] | F15 | +5 | Claw clacks |
| [[Fox]] | F02 | +3 | Yips |
| [[Owl]] | F11 | +2 | Hoots |
| [[Deer]] | F04 | +1 | Soft bleat |
| [[Badger]] | F01 | +2 | Growly chitter |
| [[Beaver]] | F01 | +3 | Tail slap layer |
| [[Hyena]] | F02 | 0 | Whoops (no laughing calls, to avoid a mocking tone) |
| [[Flamingo]] | F10 | +1 | Honks |
| [[Cobra]] | F13 | +2 | Hiss |
| [[Monkey]] | F07 | +3 | Hoots |
| [[Seal]] | F16 | +2 | Barks |
| [[Penguin]] | F12 | +3 | Brays |
| [[Wolf]] | F02 | 0 | Howl victory |
| [[Brown Bear]] | F05 | −3 | Huffs |
| [[Cheetah]] | F03 | +2 | Chirps (no roar) |
| [[Kangaroo]] | F08 | 0 | Clucks |
| [[Leopard]] | F03 | 0 | Sawing call |
| [[Toucan]] | F09 | +1 | Croak |
| [[Peacock]] | F10 | 0 | Display call |
| [[Octopus]] | F15 | 0 | Bubble burble |
| [[Walrus]] | F16 | −3 | Bellow |
| [[Arctic Fox]] | F02 | +4 | High yip |
| [[Tiger]] | F03 | −2 | Chuff greeting idle |
| [[Gorilla]] | F07 | −3 | Chest beat |
| [[Crocodile]] | F13 | −3 | Low rumble |
| [[Rhino]] | F06 | −2 | Snorts |
| [[Hippo]] | F06 | −3 | Honk-grunt |
| [[Golden Eagle]] | F11 | 0 | Softened scream |
| [[Dolphin]] | F17 | +2 | Whistles |
| [[Electric Eel]] | F18 | 0 | Crackle |
| [[Snow Leopard]] | F03 | +1 | Chuffs |
| [[Lion]] | F03 | −3 | Roar victory |
| [[Elephant]] | F06 | −3 | Trumpet |
| [[Great White Shark]] | F18 | −2 | Surge and clack |
| [[Orca]] | F17 | −1 | Calls |
| [[Narwhal]] | F17 | 0 | Clicks |
| [[Peregrine Falcon]] | F11 | +2 | Kek |
| [[Giant Panda]] | F05 | 0 | Bleats |
| [[Komodo Dragon]] | F13 | −2 | Hiss and rumble |
| [[Sabre-Tooth Tiger]] | F03 | −4 | Deep roar |
| [[Woolly Mammoth]] | F06 | −5 | Low trumpet |
| [[Megalodon]] | F18 | −5 | Deep surge |
| [[Haast's Eagle]] | F11 | −2 | Deep screech |
| [[Blue Whale]] | F17 | −5 (song pitched up first, see F17) | Song |
| [[Giant Squid]] | F15 | −4 | Deep burble |
| [[Mosasaurus]] | F19 | −4 | Sea-roar |
| [[Quetzalcoatlus]] | F19 | −1 | Wind call |
| [[Titanoboa]] | F13 | −5 | Deep hiss |
| [[Tyrannosaurus Rex]] | F19 | −5 | Bellow |

Rarity does not change the vocal palette. Ascension A5 adds a soft shimmer tail (SFX-381 layer at −12 dB) to the victory call only.

---

## 4. Worked example — Lion victory call (SFX-015 with −3 semitones)

| Field | Value |
|---|---|
| Purpose | Celebrate a won fight; also the hatch reveal call |
| Duration | 1.4 s (roar 0.9 s + chest rumble tail 0.5 s) |
| Frequency | Roar formants 300 Hz–2 kHz; chest layer 90–180 Hz (skipped on Low) |
| Priority | V2 for the owner's team, V3 for others |
| Spatial | S2: `InverseTapered`, `RollOffMinDistance` 8, `RollOffMaxDistance` 80; 2D during hatch and ascension |
| Trigger | Victory clip f15 marker; hatch f66 |
| Variations | 3 roars; no immediate repeat |
| Reuse | Shared with Sabre-Tooth Tiger at −4 semitones with an extra breathy layer |

---

## 5. Test hooks

- Listen test on a phone speaker at 50% volume: every family's idle call and hurt is identifiable.
- 20 animals of the same species idle together: at most one idle call every 2 s ([[Audio Mixing and Priority]]).
- KO vocal of an own-team animal is always audible over wild combat (V2 vs V3).

---

## Related documents
- [[Sound Bible]]
- [[Audio Mixing and Priority]]
- [[Animal Families]]
- [[Animal Index]]
- [[Animation - Animal Defeat and Victory]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[Sound - Combat Impacts]]
- [[Sound - Abilities]]
