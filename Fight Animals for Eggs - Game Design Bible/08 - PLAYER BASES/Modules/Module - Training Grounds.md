---
title: Module - Training Grounds
type: system
category: base
status: mixed
priority: P1
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - strength
  - progression
---

# Module - Training Grounds

**Asset ID:** MOD-05 (**PROPOSED**). **Slot:** flexible.

> [!success] CONFIRMED context
> Player strength is a statistic separate from animal strength (D-007). Base progression can contribute to strength and multipliers (D-022).

> [!info] PROPOSED
> +5% player Strength and +4% equipped animal stats per level ([[Canonical Proposed Values]] §12). At L5: **+25% player Strength** and **+20% equipped animal HP, ATK and DEF**.

> [!warning] UNDECIDED
> Whether the bonus also applies to base guards: **UNDECIDED** (Q-402). Module availability: **UNDECIDED** ([[Open Questions#Q-007]]).

## 1. Purpose

The base's combat-power module. It turns Cash into a permanent, account-wide power bonus that works everywhere, so a player who has stalled at a region gate has a reliable lever other than re-rolling for better animals ([[Progression Bottleneck Analysis]]).

## 2. Footprint and appearance

| Property | Proposal |
|---|---|
| Footprint | 30 × 30 studs inside a 32 × 32 slot |
| Height | 6 studs (L1) to 16 studs (L5 arena banners) |
| Appearance | An outdoor training yard: straw dummies, balance logs, hurdles, a sparring ring. Animals visibly train here only as cosmetic idle loops |
| Materials | Straw, rope and logs; then stone rings, brass bells, crystal targets, gold banners |

## 3. Upgrade levels

| Level | Cost (Cash) | Player Strength bonus | Equipped animal stat bonus (HP, ATK, DEF) | Visual change |
|---:|---:|---:|---:|---|
| L1 | 1,500 | +5% | +4% | Two straw dummies and a log hurdle |
| L2 | 3,750 | +10% | +8% | Balance beams, a bell post, sand floor |
| L3 | 9,375 | +15% | +12% | Stone sparring ring with brass rails |
| L4 | 23,438 | +20% | +16% | Obstacle course with a water jump, crystal targets |
| L5 | 58,594 | +25% | +20% | Champion's arena with gold banners and a podium |

Total: **96,657 Cash**.

### Stacking

- Player: `EffectiveStrength = BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)` (canonical §4). Additive with other Strength bonuses.
- Animals: applies to HP, ATK and DEF of the three equipped animals. Stacking order with ascension is **PROPOSED** as `Stat = BaseStat × (1 + AscensionBonus) × (1 + TrainingBonus)`; the authoritative pipeline is [[Damage, Defence and Health Model]]. See [[Progression Multipliers]] for the full stack.
- Attack speed and movement speed are not affected.

Worked example: a level 40 player has base Strength `10 + 2 × 39 = 88`. With L3 Training Grounds: `88 × 1.15 = 101.2`. A Rare Bruiser (ATK `20 × 1.70 × 1.00 = 34`) at A2 (+16%) with L3 grounds: `34 × 1.16 × 1.12 = 44.2` ATK.

## 4. Functionality

| Function | Proposal |
|---|---|
| Passive bonus | Applied whenever the player has the module; no need to be at the base |
| Practice dummy | One dummy reports damage numbers so players can test their team (owner only; no rewards) |
| Progression Score | Levels count towards the 44 base levels |

## 5. Dependencies

- Free slot; level cap `PlotStage + 1`.
- Values are read by [[Service - CombatService]] when building the player's and team's stat blocks; changes take effect immediately (combat stats are rebuilt on upgrade).

## 6. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.TrainingGrounds = { level, slot }` |
| Stat rebuild | `ProgressionService.Recalculate` triggers `CombatService.RebuildStats(player)` |
| Instances | `Plot_##.Modules.TrainingGrounds` with `PracticeDummy` (Humanoid with high HP, owner-only damage) |
| Streaming | Atomic module; decorative training loops are client-side animations |
| Anti-abuse | The practice dummy grants no Cash, XP or kill credit |

## 7. Animation and VFX

- Upgrade: dummies spring up, banners unfurl ([[Animation - Base Upgrades]]).
- Strength aura: when the bonus increases, a short flex animation on the player and a gold ripple ([[Animation - Player Attacks and Specials]]).
- Practice dummy: wobble on hit, floating damage numbers ([[Combat Feedback and Readability]]).

## 8. Raid interaction

| Situation | Behaviour |
|---|---|
| Owner defends | The owner's Strength and team bonuses apply as everywhere else |
| Guards | Q-402 (working assumption: no bonus) |
| Raider | Raiders use their own Training Grounds bonus |
| Module | Not stealable, not disabled |

## Related documents
- [[Player Strength]]
- [[Progression Multipliers]]
- [[Damage, Defence and Health Model]]
- [[Base Upgrade System]]
- [[Cost Tables]]
- [[Player Bases Index]]
