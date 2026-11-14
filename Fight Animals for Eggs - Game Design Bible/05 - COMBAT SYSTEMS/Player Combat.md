---
title: Player Combat
type: system
category: combat
status: mixed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - player
  - controls
---

# Player Combat

The player character is a combatant, not a commander standing behind the team. This page specifies the player's attacks, specials, dodge and movement. The Strength statistic that powers them is in [[Player Strength]]; controls for commanding animals are in [[Targeting and Command System]].

> [!success] CONFIRMED
> The player fights alongside their animals in real time. The player has basic attacks and special moves, and special moves may have cooldowns (D-005). Player strength is separate from animal strength (D-007).

> [!info] PROPOSED
> All values below come from [[Canonical Proposed Values]] §4 and §13 unless flagged as a new local value.

## 1. Player combat statistics

| Stat | Formula | L1 | L10 | L25 | L50 | L90 |
|---|---|---:|---:|---:|---:|---:|
| HP | `100 + 12 × (L − 1)` | 100 | 208 | 388 | 688 | 1,168 |
| DEF | `5 + 0.5 × (L − 1)` | 5.0 | 9.5 | 17.0 | 29.5 | 49.5 |
| Damage reduction | `DEF / (DEF + 100)` | 4.8% | 8.7% | 14.5% | 22.8% | 33.1% |
| Base Strength | `10 + 2 × (L − 1)` | 10 | 28 | 58 | 108 | 188 |
| Walk speed | 16 studs/s | 16 | 16 | 16 | 16 | 16 |

Player attacks use **effective Strength** in place of ATK in the damage formula ([[Damage, Defence and Health Model]]).

## 2. Basic combo

| Hit | Multiplier | Timing | Notes |
|---|---:|---|---|
| 1 | Strength × 0.8 | 0.45 s | Light swipe; can be cancelled into dodge |
| 2 | Strength × 0.8 | 0.45 s | Light swipe; can be cancelled into dodge |
| 3 | Strength × 1.4 | 0.45 s | Finisher with a small knock-back on wild Commons and Uncommons only (PROPOSED local rule) |

- The combo resets after **1.2 s** without a basic attack input.
- A full combo deals **3.0 × Strength** in **1.35 s**: a theoretical sustained output of **2.22 × Strength per second** before defence.
- **Melee range (PROPOSED local value):** 7 studs in a 90° forward arc, single target (the nearest enemy in the arc, preferring the current focus target). Server tolerance +3 studs for latency ([[Multiplayer Combat Rules#Server authority and validation]]).
- **Input buffer (PROPOSED local value):** one queued basic attack accepted within the last 0.2 s of the current hit.
- **Movement while attacking (PROPOSED local value):** walk speed is reduced to 60% (9.6 studs/s) during a combo hit and restored immediately after.

## 3. Special moves

| Special | Effect | Cooldown | Unlock | Cast time (PROPOSED local) |
|---|---|---:|---|---|
| **Power Strike** | Strength × 3.0, single target | 6 s | Level 1 | 0.35 s wind-up, cannot move |
| **Ground Slam** | Strength × 2.0 to every enemy within 10 studs | 12 s | Level 10 | 0.5 s wind-up, ground decal shown to the player |
| **Rally Cry** | Team +15% damage for 6 s | 25 s | Level 25 | Instant; usable while moving |

Rules (PROPOSED):
- Specials are always **manual**. Cooldowns start when the effect resolves, not when the button is pressed.
- Specials are not affected by the 0.5 s global cooldown between **animal** manual abilities. They share a separate 0.25 s anti-mash lock with each other (new local value).
- **Rally Cry scope (interpretation, PROPOSED):** "team" means the player's three equipped animals. Whether the player is included is a tuning lever; the worked examples in [[Damage, Defence and Health Model]] exclude the player.
- Being stunned or knocked back cancels a wind-up; the cooldown is **not** consumed.

## 4. Dodge roll

| Property | Value |
|---|---|
| Distance | 12 studs in the movement direction (or backwards if stationary) |
| Invulnerability | 0.3 s from the start of the roll |
| Cooldown | 4 s |
| Cancels | Basic combo hits 1–2 and the Ground Slam wind-up (cancelling Ground Slam does not consume it) |

The dodge is the main skill expression in PvE. Boss telegraphs are timed so that a dodge started at the moment the telegraph appears always clears it (see [[Boss AI#Telegraph rules]]).

## 5. Movement in combat

- Walk speed 16 studs/s (Roblox default). Jumping is allowed but does not avoid ground attacks that are flagged as AoE.
- No sprint at launch (PROPOSED). Companions with higher MS (for example Skirmishers at ×1.30) arrive first, which reinforces their role.
- **Camera:** third-person follow; optional soft lock-on to the focus target ([[Camera Behaviour Guidelines]]).
- Swimming and climbing follow the region rules in [[Environmental Hazards]].

## 6. Inputs (summary)

Full input maps for PC, mobile and gamepad are in [[Targeting and Command System#Input mapping]]. Player actions:

| Action | PC | Mobile | Gamepad |
|---|---|---|---|
| Basic attack | Left mouse | Attack button | RT / R2 |
| Power Strike | E | Special button 1 | X / Square |
| Ground Slam | R | Special button 2 | Y / Triangle |
| Rally Cry | F | Special button 3 | RB / R1 |
| Dodge roll | Q | Dodge button | B / Circle |

## 7. Edge cases

| Case | Rule (PROPOSED) |
|---|---|
| Attacking from inside a safe zone | Not possible. Attack inputs are ignored in the hub and in the owner's base outside a raid. |
| Combo interrupted by being hit | Basic hits are not interrupted by ordinary hits (no flinch for the player in PvE). Controller stuns interrupt. |
| Special pressed during a stun | Discarded, not buffered. |
| Player attacks an enemy that another player is fighting | Allowed; contribution counts towards kill credit ([[Multiplayer Combat Rules]]). |
| Player attacks another player | No effect unless both are in a valid PvP context ([[PvP System]]). |

## 8. Test hooks
- Combo timing: three inputs at 0.45 s spacing produce exactly 3 damage events with multipliers 0.8 / 0.8 / 1.4.
- Combo reset: a 1.25 s pause restarts at hit 1.
- Dodge invulnerability: an attack landing 0.29 s after roll start deals 0; at 0.31 s it deals full damage.
- Special cooldowns are server-enforced: a forged remote within the cooldown is rejected and logged ([[Implementation - Rate Limiting]]).
- Cases live in [[Test Cases - Combat]].

## Related documents
- [[Player Strength]]
- [[Abilities and Cooldowns]]
- [[Targeting and Command System]]
- [[Damage, Defence and Health Model]]
- [[Animation - Player Attacks and Specials]]
- [[UI - Main HUD]]
- [[Player Progression and Levelling]]
- [[M04 - Player Combat]]
