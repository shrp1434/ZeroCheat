---
title: Core Gameplay Index
type: index
category: core-gameplay
status: mixed
priority: P0
owner: Senior Game Designer
last_updated: 2026-11-14
tags:
  - index
  - core-gameplay
---

# Core Gameplay Index

This folder defines **what the player does, minute to minute and month to month**, and the cross-cutting rules that hold the systems together: the loop, the session shape, the collection, the discovery index, the team lock and onboarding. Detailed systems (combat, eggs, bases, raids) have their own folders; this folder links them into one experience.

Read [[Core Gameplay Loop]] first, then [[Team Equipping and Base Lock Rule]], which is the most implementation-sensitive rule in this folder.

## Documents

| Document | One-line description | Status |
|---|---|---|
| [[Core Gameplay Loop]] | The confirmed loop (D-002) expanded into 16 steps, with full, short, mid and long loop diagrams and a bottleneck summary. | mixed |
| [[Session Flow and Player Journey]] | Session beats, the first 45 minutes, journey stages from Hatchling to Legend, solo and group journeys. | **PROPOSED** |
| [[Animal Collection System]] | Ownership model, instances and duplicates, animal storage (Q-022), relationship to ascension, teams and raids. | mixed |
| [[Animal Index Feature Specification]] | The in-game discovery index: states, data, hatched-before-discovered handling, server validation, edge cases. | mixed |
| [[Team Equipping and Base Lock Rule]] | Exact semantics of the three-slot team and the base lock, boundary definition, edge cases and server enforcement. | mixed |
| [[New Player Onboarding]] | The 15-minute FTUE, starter animal options, honest odds teaching and just-in-time tutorials. | mixed |

## Key decisions used in this folder

D-002 (loop), D-006 (team of three), D-010 (base lock), D-015 (two-stage randomness), D-017 (disclosed luck), D-018 (independent hatches), D-019 (ascension), D-021 (egg storage), D-024 (raid theft rules), D-029 (index). See [[Decision Register]].

## Open questions raised here

Q-101 (partial teams), Q-102 (starter animal), Q-103 (duplicate species in a team), Q-104 (PS discovery credit for hatched animals), Q-105 (raider animal storage full), Q-106 (variants and ascension). These are pending entry in [[Open Questions]].

## Where to go next
- Vision: [[Game Vision Index]]
- World: [[World Design Index]]
- Systems: [[Combat Index]], [[Eggs and Hatching Index]], [[Ascension and Progression Index]], [[Player Bases Index]], [[PvP and Raiding Index]]
