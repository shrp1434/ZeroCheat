---
title: Ascension and Progression Index
type: index
category: progression
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - index
  - ascension
  - progression
---

# Ascension and Progression Index

Two kinds of progression live here. **Animal progression** is ascension: consuming duplicate animals to raise one animal's stars, stats and look. **Player progression** is levelling and the Progression Score that drives egg luck. Both feed the long-term goals at the end of this folder.

> [!success] CONFIRMED foundations
> Ascension consumes duplicates of the same animal and keeps the original (D-019). Duplicates exist because hatches are independent with no duplicate protection (D-018). Player strength is separate from animal strength (D-007). Progression improves egg and hatch odds but never wild encounters (D-017).

> [!info] PROPOSED framework
> Five ascension levels with duplicate counts by rarity (D-037; **UNDECIDED** [[Open Questions#Q-004]], [[Open Questions#Q-005]]); animals do not level individually (D-042; [[Open Questions#Q-021]]); Progression Score 0–1000 (D-036; **UNDECIDED** [[Open Questions#Q-017]]).

## Orientation

| Question | Go to |
|---|---|
| How does ascending work, step by step, including validation? | [[Ascension System]] |
| How many duplicates and how much Cash for each star? | [[Ascension Progression Table]] |
| How long does it take to max an animal, and is that reasonable? | [[Ascension Expected Value Analysis]] |
| How does the player level, and how fast? | [[Player Progression and Levelling]] |
| What exactly goes into the luck score? | [[Progression Score Specification]] |
| What do veterans do, and when do they run out of goals? | [[Long-Term Goals and Endgame]] |

## Documents in this folder

| Document | What it covers | Status |
|---|---|---|
| [[Ascension System]] | Design bible for ascension: UI flow, duplicate detection, selection, consumption, stat and ability scaling, visual tiers, confirmation, server validation, atomic transaction, save data | mixed |
| [[Ascension Progression Table]] | Per-rarity step tables, cumulative duplicates and fees, effective tier multipliers and the A4 crossover rule | proposed |
| [[Ascension Expected Value Analysis]] | Expected rolls, Cash and hours to A5 per rarity at P = 0.30 and P = 1.0, with and without merging; the cash-per-hour model; concerns and tuning options | proposed |
| [[Player Progression and Levelling]] | XP sources, XP curve, player stats by level, gates, time-to-level model and curve options | mixed |
| [[Progression Score Specification]] | PS inputs, weights, caps, data sources, recalculation triggers, worked profiles (PS 50 / 300 / 600 / 950), tuning levers | proposed |
| [[Long-Term Goals and Endgame]] | Goal ladder with time estimates, endgame loop, retention risks | mixed |

## Key numbers at a glance (PROPOSED)

| Item | Value |
|---|---|
| Ascension levels | A1–A5 |
| Copies to A5 (Common → Secret) | 16 / 14 / 11 / 10 / 8 / 7 / 6 |
| Stat gain per level | +8 % of base HP, ATK, DEF; +5 % ability effectiveness |
| Level cap | 100; 6,016,706 XP in total |
| PS profiles | Beginner 50, Intermediate 300, Advanced 600, Endgame 950 |
| Hardest A5 (Tyrannosaurus Rex) at P = 1.0 | ≈ 56 h with merging, ≈ 221 h direct (model) |

## New open questions raised in this folder

| ID | Topic |
|---|---|
| Q-303 | Whether variant copies count as duplicates for ascension, and whether a variant can be the kept target |
| Q-304 | Where ascension may be performed (own base only, or anywhere outside combat) |
| Q-305 | Disposal of surplus animals once ascension is complete or capacity is full |

These are pending addition to [[Open Questions]].

## Related folders
- [[Eggs and Hatching Index]]: where duplicates come from
- [[Combat Index]]: [[Player Strength]], [[Abilities and Cooldowns]]
- [[Data and Balancing Index]]: [[Canonical Proposed Values]], [[Balance Simulation Plan]]
- [[UI and UX Index]]: [[UI - Ascension]], [[UI - Progression Interface]]
- [[Technical Architecture Index]]: [[Service - AscensionService]], [[Service - ProgressionService]], [[Service - LuckService]]
- [[Vault Map]]
