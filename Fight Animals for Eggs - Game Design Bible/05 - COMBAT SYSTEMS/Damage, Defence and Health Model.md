---
title: Damage, Defence and Health Model
type: spec
category: combat
status: proposed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - balancing
  - damage
  - formulas
---

# Damage, Defence and Health Model

The maths of combat: how damage is calculated, how defence and health work, how to balance them, and worked examples using the canonical tables.

> [!info] PROPOSED
> Every formula here comes from [[Canonical Proposed Values]] §3 and §4 and is a proposal, not a decision. Final animal statistics are **UNDECIDED** ([[Open Questions#Q-003]]). Values not on the canonical page are marked *(new)*.

## Core formulas

| Formula | Definition |
|---|---|
| Damage | `Damage = ATK × SkillMultiplier × (100 / (100 + DEF_target)) × Random(0.95, 1.05)` |
| Damage reduction | `DEF / (DEF + 100)`: 10 DEF = 9.1%, 50 DEF = 33.3%, 100 DEF = 50% |
| Effective HP | `EHP = HP × (1 + DEF / 100)` |
| Companion stat | `Reference × M(rarity) × RoleMultiplier × SpeciesTweak` (HP, ATK, DEF); AS and MS omit `M` |
| Wild animal stat | Companion stat of the same species × 2.0 (HP) or × 0.75 (ATK), then × region multiplier. DEF and AS are **not** region-scaled (interpretation of canonical §5, which scales HP and ATK only). |
| Player attacks | Effective Strength replaces ATK ([[Player Strength]]) |
| Critical hits | None at launch |

### Bonus stacking *(new)*
`FinalStat = SpeciesStat × (1 + 0.08 × AscensionLevel) × (1 + 0.04 × TrainingGroundsLevel)`

Bonuses from the same category add together; different categories multiply. Ascension and the [[Module - Training Grounds]] animal bonus are different categories. This stacking rule is new and must be confirmed on [[Canonical Proposed Values]].

### Damage pipeline order *(new)*
1. Base value: ATK (animals), effective Strength (player) or ability base.
2. × SkillMultiplier (basic hit, combo hit, ability percentage of ATK).
3. × (1 + sum of outgoing damage buffs), e.g. Rally Cry +0.15.
4. × (100 / (100 + DEF_target)).
5. × (1 − sum of incoming damage reductions on the target), capped at 60% total reduction.
6. × Random(0.95, 1.05), rolled on the server with a per-server `Random.new()` stream.
7. Round to the nearest integer, minimum 1.
8. Subtract from absorb shields first, then from HP.

The server runs this pipeline; the client only displays the result ([[Implementation - Combat Damage Pipeline]]).

## Health rules

| Rule | Value |
|---|---|
| In-combat regeneration | None. Healing comes only from abilities. |
| Out-of-combat regeneration | 10% max HP per second after the 8 s combat tag expires *(new)*, player and companions |
| Healing | Written as a percentage of the **target's** max HP (canonical §3) |
| Overheal | Not allowed; excess healing is discarded |
| Absorb shields | Written as a percentage of the target's max HP; expire after their duration; do not stack from the same source *(new)* |
| 0 HP | Wild animal: defeated. Companion: knocked out ([[Animal Combat Behaviour#Knock-out and recovery]]). Player: defeated ([[Player Defeat and Penalties]]). |

## Crowd control and status effects *(new)*

| Effect | Rule |
|---|---|
| Stun | Target cannot act. After a stun ends, the target is immune to stuns for 4 s. |
| Slow | Reduces MS by a percentage; the strongest slow applies, slows do not stack. Floor: 40% of base MS. |
| Knock-back | Displacement only. Mini-bosses and world bosses are immune. |
| Taunt | Forces the target to attack the taunter for the duration; bosses obey taunts at half duration. |
| Damage over time | Ticks once per second through the full pipeline (DEF applies to each tick). |
| Bosses | All CC durations × 0.5 on mini-bosses and world bosses. |

## Time-to-kill targets

These are the targets the balance must hit, measured for an **on-curve** player (see the next section) fighting **solo with their team**, with perfect uptime and no abilities. Abilities add roughly 15–30% to output in practice. All **PROPOSED** *(new)*.

| Encounter | Target TTK | Tank time-to-KO when focused | Player time-to-defeat when focused |
|---|---|---|---|
| Wild Common, any region | 4–7 s | ≥ 20 s | ≥ 10 s |
| Wild Uncommon | 5–8 s | ≥ 18 s | ≥ 9 s |
| Wild Rare | 7–11 s | ≥ 15 s | ≥ 8 s |
| Wild Epic | 10–15 s | ≥ 12 s | ≥ 7 s |
| Wild Legendary | 15–25 s | ≥ 10 s | ≥ 6 s |
| Wild Mythical (server event) | 25–45 s solo, 8–15 s in a group of 4 | ≥ 8 s | ≥ 5 s |
| Wild Secret (server event) | 40–75 s solo, 12–25 s in a group of 4 | ≥ 8 s | ≥ 5 s |
| Mini-boss | 60–120 s solo | Driven by telegraphs ([[Boss AI]]) | Driven by telegraphs |
| World boss | 180–300 s with 8 players | Driven by telegraphs | Driven by telegraphs |

How to use the bands:
- If TTK falls **below** the band, wild HP is too low or player/team damage too high. Adjust the region multiplier for HP or the damage source, not the rarity multiplier (which also drives eggs and collection value).
- If time-to-KO falls **below** the band, wild ATK is too high for that rarity. Prefer telegraphed burst attacks (avoidable) over higher basic-attack damage.
- Re-run the on-curve table whenever a canonical number changes. Automate it in the [[Balance Simulation Plan]].

## On-curve reference teams

An on-curve player has the team rarity, ascension and Training Grounds level the progression curve expects at the midpoint of each region. These assumptions are *(new)* and should be validated against [[Progression Bottleneck Analysis]]. Each team is role-neutral (Tank + Bruiser + Ranged, species tweak 1.00).

| Region | ×Region | Team rarity | Ascension | Training Grounds | Player level |
|---|---:|---|---:|---:|---:|
| [[Region - Whisperwood Forest\|Whisperwood Forest]] | 1.0 | Common | A0 | 0 | 5 |
| [[Region - Sunscorch Savanna\|Sunscorch Savanna]] | 1.5 | Uncommon | A1 | 1 | 14 |
| [[Region - Emerald Canopy\|Emerald Canopy]] | 2.2 | Rare | A1 | 2 | 24 |
| [[Region - Coral Coast\|Coral Coast]] | 3.2 | Epic | A2 | 3 | 35 |
| [[Region - Frostfang Tundra\|Frostfang Tundra]] | 4.5 | Epic | A3 | 3 | 47 |
| [[Region - Skyreach Peaks\|Skyreach Peaks]] | 6.2 | Legendary | A3 | 4 | 59 |
| [[Region - Emberheart Caldera\|Emberheart Caldera]] | 8.5 | Mythical | A4 | 5 | 72 |
| [[Region - Starfall Sanctuary\|Starfall Sanctuary]] | 11.5 | Mythical | A5 | 5 | 90 |

### Results against role-neutral wild reference animals

"C" is a wild Common reference (HP 400 × region, ATK 15 × region, DEF 10). "N" is a wild animal of the team's own rarity in that region.

| Region | Target | Wild HP | Wild ATK | Team animal DPS | Player DPS | Player share | TTK | Tank time-to-KO | Player time-to-defeat |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Whisperwood | C | 400 | 15.0 | 49 | 45 | 48% | 4.3 s | 24.0 s | 10.6 s |
| Savanna | C | 600 | 22.5 | 72 | 94 | 57% | 3.6 s | 24.8 s | 12.7 s |
| Savanna | N (Uncommon) | 780 | 29.2 | 70 | 91 | 57% | 4.9 s | 19.1 s | 9.8 s |
| Canopy | N (Rare) | 1,496 | 56.1 | 91 | 143 | 61% | 6.4 s | 14.4 s | 7.8 s |
| Coral Coast | C | 1,280 | 48.0 | 140 | 222 | 61% | 3.5 s | 26.9 s | 12.9 s |
| Coral Coast | N (Epic) | 2,816 | 105.6 | 126 | 200 | 61% | 8.6 s | 12.2 s | 5.9 s |
| Frostfang | N (Epic) | 3,960 | 148.5 | 135 | 262 | 66% | 10.0 s | 9.5 s | 5.6 s |
| Skyreach | N (Legendary) | 7,068 | 265.1 | 172 | 320 | 65% | 14.4 s | 7.9 s | 4.0 s |
| Emberheart | C | 3,400 | 127.5 | 287 | 470 | 62% | 4.5 s | 27.6 s | 10.5 s |
| Emberheart | N (Mythical) | 12,580 | 471.8 | 231 | 378 | 62% | 20.7 s | 7.5 s | 2.8 s |
| Starfall | C | 4,600 | 172.5 | 305 | 582 | 66% | 5.2 s | 22.3 s | 10.1 s |
| Starfall | N (Mythical) | 17,020 | 638.2 | 245 | 467 | 66% | 23.9 s | 6.0 s | 2.7 s |

Player DPS assumes continuous combos plus Power Strike on cooldown: `Strength × (3.0 / 1.35 + 3.0 / 6) × DEF factor`.

## Worked example 1: three Commons versus a wild Common in Whisperwood Forest

Team: [[Rabbit]] (Skirmisher), [[Hedgehog]] (Tank), [[Squirrel]] (Ranged), all Common A0, no Training Grounds, species tweak assumed 1.00 (real values in [[Animal Statistics Database]]). Enemy: a wild [[Boar]] (Common Bruiser) in Whisperwood Forest (×1.0).

**Stats**

| Unit | HP | ATK | DEF | AS |
|---|---:|---:|---:|---:|
| Rabbit | 200 × 0.85 = 170 | 20 × 0.80 = 16 | 10 × 0.80 = 8 | 1.55 |
| Hedgehog | 200 × 1.55 = 310 | 20 × 0.70 = 14 | 10 × 1.60 = 16 | 0.85 |
| Squirrel | 200 × 0.75 = 150 | 20 × 1.15 = 23 | 10 × 0.70 = 7 | 1.00 |
| Wild Boar | 200 × 1.10 × 2.0 = 440 | 20 × 1.00 × 0.75 = 15 | 10 × 1.10 = 11 | 0.95 |

**Outgoing damage** (Boar DEF factor = 100 / 111 = 0.901)

| Source | Damage per hit | DPS |
|---|---:|---:|
| Rabbit | 16 × 0.901 = 14.4 | 22.3 |
| Hedgehog | 14 × 0.901 = 12.6 | 10.7 |
| Squirrel | 23 × 0.901 = 20.7 | 20.7 |
| **Animals total** | | **53.8** |
| Player L1 (Strength 10): combo 7.2 / 7.2 / 12.6, Power Strike 27.0 | | 24.5 |
| Player L5 (Strength 18): combo 13.0 / 13.0 / 22.7, Power Strike 48.6 | | 44.2 |

**Time to kill:** animals alone 440 / 53.8 = **8.2 s**; with an L1 player **5.6 s**; with an L5 player **4.5 s**. All inside or near the 4–7 s band.

**Incoming damage** (Boar per hit, 0.95 hits/s)

| Target | Damage per hit | Time to KO |
|---|---:|---:|
| Hedgehog (DEF 16) | 15 × 100/116 = 12.9 | 25.2 s |
| Rabbit (DEF 8) | 13.9 | 12.9 s |
| Squirrel (DEF 7) | 14.0 | 11.3 s |
| Player L1 (HP 100, DEF 5) | 14.3 | 7.4 s |
| Player L5 (HP 148, DEF 7) | 14.0 | 11.1 s |

**Reading:** a level 1 player who stands still and lets the Boar hit them loses in 7.4 s, but the team kills the Boar in 5.6 s. The Boar only targets the player first if the player pulled it, and Hedgehog's Protect bonus ([[Targeting and Command System#Auto-target scoring]]) and threat ([[Wild Animal AI]]) pull it away. The fight is safe but not trivial, which is the intended onboarding feel ([[New Player Onboarding]]).

## Worked example 2: a mid-game team in Coral Coast

Team: [[Wolf]] (Rare Bruiser), [[Brown Bear]] (Rare Tank), [[Toucan]] (Rare Ranged), all A2, Training Grounds L3, player level 35 (effective Strength 78 × 1.15 = 89.7). Enemy: a wild [[Octopus]] (Rare Controller) in Coral Coast (×3.2).

| Unit | HP | ATK | DEF | DPS vs Octopus |
|---|---:|---:|---:|---:|
| Wolf | 485.9 | 44.2 | 24.3 | 36.1 |
| Brown Bear | 684.7 | 30.9 | 35.3 | 22.6 |
| Toucan | 331.3 | 50.8 | 15.5 | 43.7 |
| Player L35 | 508 | Strength 89.7 | 22.0 | 210.2 |
| Wild Octopus | 200 × 1.7 × 0.95 × 2 × 3.2 = 2,067 | 65.3 | 16.2 | — |

TTK = 2,067 / 312.7 = **6.6 s**, slightly under the 7–11 s Rare band, because the player supplies 67% of the damage. The Octopus deals 48.2 per hit to Brown Bear (14.2 s to KO) and 56.5 to Toucan (5.9 s to KO), so Toucan must stay at range, which its Ranged stance already does ([[Animal Combat Behaviour]]).

## Worked example 3: an endgame team in Starfall Sanctuary

Team: [[Mosasaurus]] (Secret Assassin), [[Tyrannosaurus Rex]] (Secret Bruiser), [[Woolly Mammoth]] (Mythical Tank), all A5, Training Grounds L5 (×1.40 × 1.20 = ×1.68). Player level 90, effective Strength 188 × 1.25 = 235.

| Unit | HP | ATK | DEF | AS |
|---|---:|---:|---:|---:|
| Mosasaurus | 1,209.6 | 233.9 | 56.4 | 1.05 |
| Tyrannosaurus Rex | 1,774.1 | 161.3 | 88.7 | 0.95 |
| Woolly Mammoth | 1,927.0 | 87.0 | 99.5 | 0.85 |
| Player L90 | 1,168 | Strength 235 | 49.5 | — |

**3a. Versus a wild Common reference spawn** (HP 4,600, ATK 172.5, DEF 10): animals 429.8 DPS, player 581.6 DPS, TTK **4.6 s**. Incoming per hit: Mammoth 86.5 (22.3 s to KO), Mosasaurus 110.3 (11.0 s), player 115.4 (10.1 s). Inside every band: the region multiplier works well for everyday spawns.

**3b. Versus a wild [[Megalodon]]** (Mythical Bruiser, Starfall native: HP 200 × 3.7 × 1.1 × 2 × 11.5 = 18,722; ATK 20 × 3.7 × 0.75 × 11.5 = 638.3; DEF 40.7): team 790.7 DPS, TTK **23.7 s** solo, **5.9 s** with four equal players. Incoming per hit: Mammoth 320.0 (**6.3 s** to KO), Mosasaurus 408.0 (3.1 s), player 426.9 (**2.9 s**).

## Balance findings

1. **Everyday spawns are on target in every region.** Wild Commons scaled by the region multiplier give 3.5–5.2 s TTK and 20–28 s Tank time-to-KO from Whisperwood to Starfall. No change recommended.
2. **The player's share of damage rises from 48% to 66%.** This works against the "team is the hero" pillar. **UNDECIDED** (Q-211); options are in [[Player Strength]].
3. **Native high-rarity wild animals hit too hard in late regions.** Tank time-to-KO falls to 6–8 s and player time-to-defeat to 2.7–4 s from Skyreach Peaks onwards. Because Mythical and Secret wild animals are announced server events (canonical §6), they should be designed as **group encounters**. **UNDECIDED** (Q-212). Options:
   - A. Keep the numbers; make most of their damage come from telegraphed, dodgeable attacks, with basic attacks at 50% of the formula *(new lever)*.
   - B. Apply the region multiplier to ATK with a softer exponent (`Region^0.75`: Starfall ATK ×6.24 instead of ×11.5, Mammoth time-to-KO 11.7 s).
   - C. Scale rare-spawn HP and ATK by the number of engaged players, as world bosses do ([[Boss AI#Participant scaling]]).
   - **Recommendation (PROPOSED, unapproved):** A + C. It keeps one canonical region multiplier, rewards dodging, and makes rare spawns social events.
4. **Mid-game Rares die slightly too fast (6.6 s against a 7–11 s band)** for the same reason as finding 2. Fixing finding 2 fixes this.

## Test hooks
- Unit test the pipeline with fixed variance (1.00): Rabbit vs wild Boar basic hit = 14 (14.41 rounded); Power Strike at Strength 10 vs DEF 11 = 27.
- DEF 0 target takes exactly `ATK × multiplier`; DEF 100 takes half.
- Variance distribution over 10,000 hits stays within [0.95, 1.05] and averages 1.00 ± 0.005.
- Incoming reduction cap: three 30% reductions produce 60%, not 90%.
- Cases in [[Test Cases - Combat]]; simulation in [[Balance Simulation Plan]].

## Related documents
- [[Canonical Proposed Values]]
- [[Animal Stat Budget Model]]
- [[Animal Statistics Database]]
- [[Player Strength]]
- [[Balancing Methodology]]
- [[Balance Simulation Plan]]
- [[Implementation - Combat Damage Pipeline]]
- [[Region Unlock Progression]]
