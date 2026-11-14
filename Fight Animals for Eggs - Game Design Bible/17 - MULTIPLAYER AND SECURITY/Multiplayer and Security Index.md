---
title: Multiplayer and Security Index
type: index
category: networking
status: mixed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - index
  - multiplayer
  - security
  - networking
---

# Multiplayer and Security Index

This folder explains how one shared world serves many players at once, how state moves between server and clients, how data stays consistent through disconnects and crashes, and how the game resists exploits. It builds on [[Technical Architecture Index]] and is implemented by the patterns in [[Luau Implementation Index]].

> [!success] CONFIRMED foundations
> One large shared world for solo and multiplayer play (D-025). Optional PvP and raids (D-023, D-024). Raids: base eggs stealable, backpack eggs never; only knocked-out defenders stealable; at most three animals per successful raid; offline bases never raidable.

> [!warning] UNDECIDED items that shape this folder
> Players per server ([[Open Questions#Q-031]], working assumption 16), PvP activation ([[Open Questions#Q-011]]), raid duration ([[Open Questions#Q-012]]), egg theft limit ([[Open Questions#Q-013]]), defeat penalties ([[Open Questions#Q-014]]), matchmaking ([[Open Questions#Q-029]]), shields ([[Open Questions#Q-030]]), and this folder's own questions Q-901 (same-server raids), Q-905 (automated enforcement), Q-906 (claims before defender disconnect) and Q-907 (same-pair raid cooldown).

## Orientation

- **Networking first:** [[Multiplayer Architecture]] → [[Shared World and Player Sessions]] → [[Replication Strategy]] → [[Network Ownership]] → [[Latency Handling]].
- **Data integrity:** [[Data Consistency and Transactions]] → [[Disconnect Handling]].
- **Scale:** [[Animal Scalability and Performance Budgets]].
- **Security:** [[Security Architecture]] → [[Exploit Prevention]] → [[Threat Model]].

## Documents

| Document | One-line description |
|---|---|
| [[Multiplayer Architecture]] | Topology, authority model, session contexts, combat synchronisation, boss, raid and PvP sessions |
| [[Shared World and Player Sessions]] | Join-to-leave lifecycle, base plots, interest management, density and social visibility |
| [[Replication Strategy]] | Channels, the two animal replication approaches evaluated, snapshot format, rates and interpolation |
| [[Network Ownership]] | Ownership rule per object class; `SetNetworkOwner(nil)` for AI animals; raid-specific rules |
| [[Latency Handling]] | Player-only prediction, server reconciliation, hit validation tolerances, lag compensation |
| [[Disconnect Handling]] | Outcome of every in-flight action on disconnect, crash or shutdown, including raids and bosses |
| [[Data Consistency and Transactions]] | Session locking with `UpdateAsync`, save budget, raid journal, receipts, cross-server locks |
| [[Animal Scalability and Performance Budgets]] | Entity census, AI LOD load, CPU, bandwidth per animal, culling and mobile budgets |
| [[Security Architecture]] | Principles, trust boundaries, defence in depth, secrets, logging and response policy |
| [[Exploit Prevention]] | Catalogue of movement, remote, combat, economy, odds, raid and alt-account exploits with controls |
| [[Threat Model]] | STRIDE table of 25 threats with ratings, mitigations and residual risk |

## Related documents
- [[Technical Architecture Index]]
- [[Luau Implementation Index]]
- [[PvP and Raiding Index]]
- [[Remote Communication Contract]]
- [[Server-Client Responsibilities]]
- [[QA and Testing Index]]
