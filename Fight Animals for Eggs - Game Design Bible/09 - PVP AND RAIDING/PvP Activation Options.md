---
title: PvP Activation Options
type: spec
category: pvp-and-raiding
status: undecided
priority: P1
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - pvp
  - options
  - open-question
---

# PvP Activation Options

How a player enters PvP. The owner has confirmed that PvP is optional (D-023) but has **not** chosen the method.

> [!warning] UNDECIDED (Q-011)
> The PvP activation method is **UNDECIDED** ([[Open Questions#Q-011]]). This page compares options and gives a **labelled, unapproved recommendation**. It must not be implemented as final until the owner records a decision in the [[Decision Register]]. Q-011 blocks the PvP prototype.

Whichever option is chosen, the shared rules in [[PvP System]] (damage scalar, safeguards, no material loss) apply.

## Evaluation criteria

| Criterion | Why it matters here |
|---|---|
| Consent clarity | PvP is optional (D-023); a player must never be surprised by PvP damage |
| Griefing resistance | Young audience ([[Target Audience and Player Motivations]]); shared world (D-025) |
| Engagement | Does PvP actually happen, or does the feature sit unused? |
| Fairness | Level and rarity gaps are large in this game ([[Damage, Defence and Health Model]]) |
| Build and test cost | Server-authoritative validation per option ([[Service - PvPService]]) |
| Fit with the shared PvE world | Must not disrupt farming, bosses or onboarding |

## Option A: opt-in toggle with cooldown

The player switches a "PvP On" flag (in settings or at a shrine in the hub). Flagged players can damage each other anywhere outside safe zones.

| Pros | Cons |
|---|---|
| Spontaneous encounters across the whole world | Flagged low-power players get hunted; needs level bands |
| Simple for players to understand | Interferes with PvE: a flagged player can be attacked mid-boss or mid-farm (mitigated by arena and boss exclusions) |
| Low content cost: no new spaces | Toggle abuse: switching on only to ambush, off to escape; needs a cooldown (300 s) and PvP tag (15 s) |
| | Fewest players will flag, so encounters may be rare on a 16-player server |

## Option B: arena zones

Dedicated arena areas (for example one in the hub's edge or one per region tier). Entering the arena is consent; PvP applies only inside.

| Pros | Cons |
|---|---|
| Clear consent: walking in is the opt-in | Needs arena content, matchmaking queue and UI |
| No interference with PvE | Little spontaneity |
| Easy to add matchmaking by Progression Score | With 16 players per server, queues may be thin; may need cross-server matchmaking (*unverified* feasibility; large cost) |
| Spectating and events are possible | |

## Option C: duel requests

A player targets another and sends a duel request; the other accepts. A duel ring appears around both.

| Pros | Cons |
|---|---|
| Strongest consent: each fight is accepted individually | Can be spammed (mitigated: block, request cooldowns) |
| Works on any server population | No "competitive ladder" by itself |
| Cheapest to build; no new spaces | Friends-only use; low discovery for players without friends online |
| Ideal for social play between friends | |

## Option D: PvP-enabled region

One region, or part of one, is always PvP (for example a contested zone with better rewards).

| Pros | Cons |
|---|---|
| High-stakes area with its own identity | Conflicts with the linear region unlock ([[Region Unlock Progression]]); if the region holds required content, PvP becomes mandatory, which breaks D-023 |
| Strong engagement among competitive players | Needs extra rewards to attract players, which pressures the economy ([[Inflation and Farming Exploit Risks]]) |
| | Highest griefing risk |

## Comparison

Scores are 1 (poor) to 5 (good) and are the team's judgement (PROPOSED).

| Criterion | A. Toggle | B. Arena | C. Duel | D. Region | A+B+C hybrid | **B+C hybrid** |
|---|---:|---:|---:|---:|---:|---:|
| Consent clarity | 3 | 5 | 5 | 2 | 4 | 5 |
| Griefing resistance | 2 | 5 | 5 | 1 | 3 | 5 |
| Engagement | 3 | 4 | 3 | 4 | 5 | 4 |
| Fairness (matchmaking possible) | 2 | 5 | 3 | 2 | 4 | 4 |
| Build and test cost (5 = cheapest) | 4 | 2 | 5 | 2 | 1 | 3 |
| Fit with shared PvE world | 2 | 5 | 5 | 2 | 3 | 5 |
| **Total** | 16 | 26 | 26 | 13 | 20 | **26** |

## Recommendation

> [!info] PROPOSED recommendation, unapproved (Q-011)
> **Duel requests at launch (C), with arena zones (B) as the first post-launch PvP feature, built on the same rules.** Do not ship an open-world toggle (A) or a PvP region (D) at launch.
>
> Rationale:
> 1. **Consent and safety:** both C and B need an explicit action per fight or per entry, so no player is surprised by PvP damage.
> 2. **Cheapest path to prove demand:** duels need no new spaces or queues. If duels are popular, arenas add matchmaking and ratings.
> 3. **No disruption to PvE:** boss fights, farming and onboarding stay untouched.
> 4. **Fairness:** duels show both players' level and team rarity before acceptance; arenas can match by Progression Score ([[PvP System#Matchmaking and fairness]]).
> 5. **Avoids D-023 risk:** a PvP region can make PvP effectively mandatory if it holds required content.

If the owner prefers more open PvP, the safest version of option A is a hub-only toggle with a 300 s cooldown, ±10 level bands, a 15 s PvP tag, no PvP in boss arenas and a level 15 minimum, as listed in [[PvP System#Safeguards]].

## What each option changes elsewhere

| Option | Affected documents |
|---|---|
| A | [[UI - Settings]], [[UI - PvP Interface]], [[Multiplayer Combat Rules]], [[Test Cases - PvP]] |
| B | [[World Overview and Map]], [[Hub - Hatchling Haven]], [[UI - PvP Interface]], [[Service - PvPService]] |
| C | [[UI - PvP Interface]], [[UI - Notifications]], [[Service - PvPService]] |
| D | [[World Overview and Map]], [[Region Unlock Progression]], [[Economy Overview]] |

## Related documents
- [[PvP System]]
- [[Open Questions]]
- [[Decision Register]]
- [[Design Principles and Fairness Charter]]
- [[Target Audience and Player Motivations]]
