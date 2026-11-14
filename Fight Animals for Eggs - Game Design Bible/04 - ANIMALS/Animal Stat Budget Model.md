---
title: Animal Stat Budget Model
type: spec
category: animals
status: proposed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - animals
  - balancing
  - combat
---

# Animal Stat Budget Model

> [!info] PROPOSED ([[Decision Register|D-034]])
> This model explains why every animal has the statistics in the [[Animal Statistics Database]]. Values are not assigned by hand: each animal's stats come from three inputs (rarity, role and a small species tweak) and are checked with a Power Index.

## 1. Why a budget model

- **Coherence.** Two animals of the same rarity are roughly equally strong, but in different ways.
- **Readability.** Players learn that rarity means power and role means play style.
- **Maintainability.** New animals ([[Content Expansion Guidelines]]) can be added by choosing a rarity, a role and a tweak, then regenerating.
- **Auditability.** The Power Index gives one number that QA and designers can check.

## 2. Formula

```text
HP  = 200 × M(rarity) × Role.HP  × Tweak.HP
ATK = 20  × M(rarity) × Role.ATK × Tweak.ATK
DEF = 10  × M(rarity) × Role.DEF × Tweak.DEF
AS  = 1.00           × Role.AS  × Tweak.AS     (not scaled by rarity)
MS  = 16             × Role.MS  × Tweak.MS     (not scaled by rarity)
```

Attack speed and movement speed do not scale with rarity. A Secret animal should hit harder and survive longer than a Common one, but it should not move or attack so fast that it stops reading as the same species archetype. It also must not out-run the player (walk speed 16).

### Rarity tier multipliers

| Rarity | M | Step from previous |
|---|---:|---:|
| Common | 1.00 | — |
| Uncommon | 1.30 | ×1.30 |
| Rare | 1.70 | ×1.31 |
| Epic | 2.20 | ×1.29 |
| Legendary | 2.85 | ×1.30 |
| Mythical | 3.70 | ×1.30 |
| Secret | 4.80 | ×1.30 |

Each tier is about 1.27–1.31 times the previous one. A Secret is 4.8 times a Common, so an endgame team is roughly 5–7 times stronger than a starter team before ascension and base bonuses.

### Role multipliers

| Role | HP | ATK | DEF | AS | MS | Range | Role PI | Pays for |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| [[Animal Roles#Tank\|Tank]] | 1.55 | 0.70 | 1.60 | 0.85 | 0.90 | 5 | 0.986 | Taunts, damage reduction |
| [[Animal Roles#Bruiser\|Bruiser]] | 1.10 | 1.00 | 1.10 | 0.95 | 1.00 | 5 | 1.027 | Nothing; the baseline all-rounder |
| [[Animal Roles#Assassin\|Assassin]] | 0.75 | 1.45 | 0.70 | 1.05 | 1.20 | 5 | 1.054 | Fragility; must be protected |
| [[Animal Roles#Skirmisher\|Skirmisher]] | 0.85 | 0.80 | 0.80 | 1.55 | 1.30 | 5 | 1.017 | Low per-hit damage |
| [[Animal Roles#Ranged\|Ranged]] | 0.75 | 1.15 | 0.70 | 1.00 | 1.00 | 28 | 0.916 | Safety from range (PI below 1.0) |
| [[Animal Roles#Support\|Support]] | 1.00 | 0.65 | 1.00 | 1.00 | 1.00 | 18 | 0.806 | Heals and buffs (PI about 0.8) |
| [[Animal Roles#Controller\|Controller]] | 0.95 | 0.80 | 0.95 | 1.00 | 1.00 | 12 | 0.870 | Stuns, slows, pulls (PI about 0.87) |

## 3. Power Index

```text
Offence = ATK × AS                      (damage per second from basic attacks)
EHP     = HP × (1 + DEF / 100)          (effective HP under the reduction formula)
PI      = sqrt(Offence × EHP) / sqrt(ReferenceOffence × ReferenceEHP)
```

The reference is the role-neutral animal of the same rarity (HP 200·M, ATK 20·M, DEF 10·M, AS 1.0), so PI is comparable across rarities. A geometric mean is used because a fight's length is proportional to EHP ÷ enemy DPS: doubling either offence or survivability doubles the value of the other.

| Rule | Value |
|---|---|
| Pure combat roles (Tank, Bruiser, Assassin, Skirmisher) | PI ≈ 1.00 ± 0.08 |
| Ranged | PI ≈ 0.92 (range advantage) |
| Support | PI ≈ 0.81 (utility) |
| Controller | PI ≈ 0.87 (utility) |
| Species tweak tolerance | ±0.06 from the role PI |

## 4. Worked example: Tiger

Tiger is Epic (M = 2.20) and an Assassin (HP 0.75, ATK 1.45, DEF 0.70, AS 1.05):

- HP = 200 × 2.20 × 0.75 = **330**
- ATK = 20 × 2.20 × 1.45 = **63.8**
- DEF = 10 × 2.20 × 0.70 = **15.4** (13.3% reduction)
- AS = 1.05; MS = 16 × 1.20 = **19.2**
- PI = **1.039** (role target 1.039)

## 5. Species tweaks

Tweaks give individual animals a recognisable identity (for example, the Cheetah is faster than other Skirmishers) without breaking the budget. Each tweak trades one stat against another.

| Animal | Tweak | PI | Role target |
|---|---|---:|---:|
| [[Woodpecker]] | AS ×1.10, ATK ×0.92 | 1.023 | 1.017 |
| [[Cheetah]] | MS ×1.15, HP ×0.92 | 0.970 | 1.012 |
| [[Gorilla]] | ATK ×1.08, HP ×0.95 | 1.024 | 1.011 |
| [[Hippo]] | ATK ×1.10, MS ×0.90 | 1.060 | 1.011 |
| [[Elephant]] | HP ×1.08, AS ×0.92 | 1.019 | 1.022 |
| [[Peregrine Falcon]] | MS ×1.15, DEF ×0.90 | 0.994 | 1.004 |
| [[Woolly Mammoth]] | HP ×1.06, MS ×0.90 | 1.066 | 1.035 |
| [[Tyrannosaurus Rex]] | ATK ×1.08, MS ×0.92 | 1.079 | 1.039 |

Abilities are the main source of identity. They are written as a percentage of ATK, so they scale with rarity and ascension automatically ([[Animal Abilities Catalogue]]).

## 6. Ability budget guidelines

| Rarity band | Abilities | Typical single-target multiplier | Typical cooldown |
|---|---|---|---|
| Common, Uncommon | 1 (auto or manual) | 130–180% ATK | 8–18 s |
| Rare, Epic | 2 (one auto, one manual) | 150–260% ATK | 7–22 s |
| Legendary, Mythical, Secret | 2 plus a passive | 190–360% ATK | 7–24 s |

Crowd-control caps against normal enemies: area stuns and freezes at most 1.5 s; roots at most 2.0 s; single-target stuns at most 3.0 s (reserved for Secret signature abilities). After a stun the target is immune to stuns for 4 s, and all durations are halved on bosses ([[Damage, Defence and Health Model]], [[Boss AI]]).

## 7. Wild scaling

Wild animals use the same species stats with wild multipliers (HP ×2.0, ATK ×0.75) and the region multiplier ([[Canonical Proposed Values]] §4–§5). DEF is not region-scaled, because DEF/(DEF+100) would otherwise approach 100% reduction in late regions.

## 8. Tuning levers and risks

| Lever | Effect | Risk |
|---|---|---|
| Tier multiplier M | Rarity power gap | A large gap makes Commons useless late; a small gap makes rarity feel meaningless |
| Role multipliers | Role identity | Over-tuned Support can make fights trivial |
| Ability % of ATK | Burst and control | Stacked stuns lead to permanent lockdown; enforce diminishing returns |
| Region multiplier | Pacing of the world | Steep curves make old teams obsolete too quickly |

## Related documents

[[Animal Statistics Database]] · [[Animal Roles]] · [[Damage, Defence and Health Model]] · [[Balancing Methodology]] · [[Canonical Proposed Values]]
