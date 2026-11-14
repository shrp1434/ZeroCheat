---
title: Mini-Boss - Dustmane
type: boss
category: world-design
status: proposed
priority: P0
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - bosses
  - mini-boss
  - sunscorch-savanna
---

# Mini-Boss - Dustmane

| Field | Value |
|---|---|
| Asset ID | BOS-02 |
| Type | Mini-boss (2 phases) |
| Base animal | Elder lion with a mane of swirling dust |
| Region / arena | [[Region - Sunscorch Savanna]] / Sunstone Kopje summit |
| Recommended level | 16–20 |
| Gate role | Key for [[Region - Emerald Canopy]] (with level 18) |
| Respawn | 10 min after defeat, per server |
| Status | **PROPOSED** (rewards **UNDECIDED**, [[Open Questions#Q-015]]) |

## 1. Concept

Dustmane is an ancient, battle-scarred lion who rules the kopjes. His mane is a living swirl of sand that he can shake loose into blinding clouds. He is a boss-only creature, distinct from the hatchable [[Lion]]. His lesson: **your animals need you**. Dust Shake breaks companions' automatic targeting, so the player must re-issue manual target commands ([[Targeting and Command System]]) to keep damage flowing.

## 2. Arena: Sunstone Kopje summit

- Oval granite plateau, **80 × 60 studs**, with five rock pillars (4 studs wide) scattered across it.
- The pillars block Pounce line of sight and provide **safe zones** from King's Roar in phase 2.
- Edges are low ledges; falling off returns the player to the arena entrance ramp (still a participant within 20 s).
- Sand patches on the plateau show where Sandstorm Ring will be thickest (environmental storytelling, no damage on their own).

## 3. Stats (PROPOSED)

`HP = 200 × 34 × 1.5`, `ATK = 20 × 2.6 × 1.5`, `DEF = 10 × 3.0` ([[Boss Design Overview]]).

| Stat | Value |
|---|---:|
| Max HP (solo) | 10,200 |
| ATK | 78 |
| DEF | 30 |
| Move speed | 18 studs/s; Pounce leap 30 studs |
| Soft enrage | After 300 s: +10% ATK per 30 s, max +100% |

## 4. Phases

| Phase | HP range | Behaviour | Transition |
|---|---|---|---|
| 1: Pride Lord | 100–50% | Swipes, Pounces, Dust Shake | At 50%: 2.5 s roar; mane flares into a dust vortex; the sky dims orange |
| 2: Sandstorm | 50–0% | Adds Sandstorm Ring, Dust Wisps and King's Roar | — |

## 5. Attack list

Damage percentages are of a level 18 player's max HP (304 HP, DEF 13.5); one SkillMultiplier point ≈ 22.6%.

| Attack | Phase | Tier | Skill mult. | Shape | Telegraph | Active / recovery | Approx. damage | Counterplay |
|---|---|---|---:|---|---|---|---|---|
| Claw Swipe | 1, 2 | Light | 1.0 | Cone 100°, 8 studs | 0.5 s orange cone, paw raises | 0.25 s / 0.5 s | ~23% | Dodge or step aside |
| Pounce | 1, 2 | Heavy | 1.9 | Circle 8 studs at landing point (target's position at wind-up) | 0.9 s red landing circle, crouch and tail lash | 0.6 s / 1.0 s | ~43% | Move out; break line of sight with pillars |
| Dust Shake | 1, 2 | Control | 0.6 | Circle 14 studs on self | 1.0 s purple circle, mane bristles | 0.4 s / 0.8 s | ~14% + **Dust-blind** | Companions inside lose their target for 2 s; issue a new target command |
| Sandstorm Ring | 2 | Signature | 2.2 over 4 s | Ring: everything outside 12 studs from Dustmane | 1.5 s red outer ring with gold inner circle | 4.0 s / 1.0 s | ~50% total if standing outside | Move inside the gold circle, close to the boss |
| Dust Wisps | 2 | Adds | — | 2 sand lion silhouettes (+1 per 3 extra participants) | 1.5 s sand swirl at spawn | Wisps live 20 s or until destroyed (each 4% of boss max HP) | Wisp hits ~15% | Focus them with a target command |
| King's Roar | 2 | Ultimate | 2.4 | Arena-wide except behind pillars | 2.5 s red screen-edge glow, lion rears and inhales | 0.5 s / 2.0 s | ~54% + 10-stud knockback | Hide behind a pillar (gold shadow decal) |

## 6. AI behaviour summary

General system: [[Boss AI]].
- **Target selection:** highest threat; Pounce prefers a target at 15–30 studs.
- **Dust Shake** triggers when 2+ companions are within 14 studs, at most every 12 s, so it reliably interrupts companion auto-targeting.
- **P2 rotation:** Sandstorm Ring every 20 s; Dust Wisps every 25 s; King's Roar every 30 s, never within 5 s of Sandstorm Ring.
- **Wisps** are not animals: they cannot be discovered, captured or stolen, and grant no wild rewards.
- **Reset:** arena empty 10 s → full HP.

## 7. Multiplayer scaling

- Max HP: 10,200 solo; 14,280 (2); 22,440 (4); 38,760 (8, cap).
- Wisps: +1 per 3 participants beyond the first.
- Credit: ≥ 5% of current scaled max HP.

## 8. Rewards (UNDECIDED, Q-015)

> [!warning] UNDECIDED
> Options only ([[Boss Rewards]]): R1 Cash / R2 XP scaled by E = 1.5; R3 a fixed-rarity egg (for example Uncommon); R4 Trophy Hall trophy on first defeat; R5 cosmetic (for example a mane-dust trail). Confirmed regardless: Canopy gate key and +10 PS on first credited defeat.

## 9. Defeat penalties

[[Player Defeat and Penalties]] (**UNDECIDED**, [[Open Questions#Q-014]]). **PROPOSED:** respawn at the Great Baobab Waystone; contribution kept until reset.

## 10. Visual, animation, VFX and sound notes

| Area | Notes |
|---|---|
| Model | Broad-shouldered lion, scarred muzzle, mane built from layered sand-coloured planes that animate as swirling dust in P2 ([[Boss Art Direction]]) |
| Animation | Crouch and tail-lash before Pounce, full-body shake for Dust Shake, rear-and-inhale for King's Roar ([[Animation - Boss Attacks]]) |
| VFX | Dust cloud with readable edge, sand vortex ring with clearly visible gold safe circle, Wisps as translucent sand silhouettes ([[VFX - Combat Effects]]) |
| Sound | Low growl idle, rising inhale before Roar, sand hiss for Sandstorm Ring ([[Sound - Bosses]]) |
| Accessibility | Dust-blind status shown as an icon on companion portraits ([[UI - Animal Team Display]]) |

## 11. Test hooks

- Dust Shake on 3 companions → all lose target for 2.0 s; a manual command reassigns instantly.
- Player behind a pillar during King's Roar → no damage.
- Sandstorm Ring safe circle visible on mobile at minimum graphics quality.
- Wisp defeat → no Animal Index entry, no Cash.

## Related documents
- [[Boss Design Overview]]
- [[Region - Sunscorch Savanna]]
- [[Targeting and Command System]]
- [[Boss AI]]
- [[Test Cases - Bosses]]
