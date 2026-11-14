---
title: M19 - Multiplayer Testing
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - multiplayer
  - qa
  - security
milestone: M19
stage: 7
complexity: L
---

# M19 - Multiplayer Testing

> [!info] PROPOSED milestone
> Stage 7 · Size **L** · Critical path: **yes** · Exit gate: **G6 Beta ready**

## Objective

Prove the full game holds up in a full shared server (working assumption 16 players, [[Open Questions#Q-031]]) with every system running at once: combat, AI, bases, raids, bosses, rolls and persistence. M19 is a dedicated hardening milestone. It does not replace the multiplayer tests run inside each feature milestone; it runs them together, at scale, with deliberate failure injection and an internal red team.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Full-server soak test plan and scripts | QA | [[Test Plan Matrix]], [[Test Cases - Multiplayer]] |
| Failure injection: server shutdown, player crash, network drop during every transaction type | QA, Engineering | [[Disconnect Handling]], [[Data Consistency and Transactions]] |
| DataStore budget measurement under peak write patterns | Engineering | [[Service - DataService]], [[Save, Load and Recovery]] |
| Replication and bandwidth profile | Engineering | [[Replication Strategy]], [[Multiplayer Architecture]] |
| Latency sweep for combat and raids | Engineering, QA | [[Latency Handling]] |
| Internal red-team exploit pass against the threat model | Security | [[Threat Model]], [[Exploit Prevention]] |
| Item-count audit tool (detects duplication or loss) | Engineering | [[Data Validation and Migration]] |
| Defect triage and fixes | All | [[Bug Reporting and Severity]] |

## Dependencies

- **Upstream:** [[M15 - Base Raids]], [[M17 - Boss Encounters]].
- **Downstream:** [[M20 - Optimisation]].

## Complexity

**L.** Coordinating many testers and clients, building automation for failure injection, and fixing what it finds.

## Risks

| Risk | Why it matters here |
|---|---|
| R-023, R-024, R-025 (exploits and duplication) | Red-team pass is the main mitigation before beta. |
| R-016, R-017 (DataStore budgets, transfers) | Peak load and failure injection expose them. |
| R-018 (server cost) | First full-content, full-server measurement. |
| R-033 (QA capacity) | Multi-client tests need many people or automation. |

## Acceptance criteria

- [ ] A full-server soak with every system active completes without server errors that affect players.
- [ ] Failure injection on every transaction type (roll, hatch, ascension, merge, upgrade, raid theft, purchase) leaves every profile consistent; the item audit shows zero duplicates and zero losses.
- [ ] Peak DataStore usage stays inside documented budgets with headroom, with no throttled writes during the soak.
- [ ] Every confirmed raid rule still holds under latency and disconnection.
- [ ] The red-team pass finds no open high-severity exploit at the gate.
- [ ] Kill credit, boss eligibility and announcements behave correctly with a full server.

## Testing requirements

- [[Test Cases - Multiplayer]] (all).
- [[Test Cases - Raiding]] and [[Test Cases - PvP]] under latency and disconnection.
- [[Test Cases - Persistence]] with failure injection.
- [[Test Cases - Exploit Prevention]] (red-team pass).
- [[Test Cases - Bosses]] with a full server.

## Open questions

- [[Open Questions#Q-031]]: maximum players per server (measured capacity informs the decision).
- [[Open Questions#Q-012]] and [[Open Questions#Q-013]]: raid duration and theft limit (soak tests cover the range of candidate values; no value is chosen here).
- **UNDECIDED** (Q-1115): update rollout method (how servers move to a new version) affects how shutdown tests are scripted.

## Key vault documents
- [[Multiplayer and Security Index]] · [[Multiplayer Architecture]] · [[Shared World and Player Sessions]]
- [[Data Consistency and Transactions]] · [[Disconnect Handling]] · [[Threat Model]] · [[Security Architecture]]

## Related documents
- [[Development Roadmap]]
- [[M15 - Base Raids]]
- [[M20 - Optimisation]]
- [[QA Strategy]]
- [[Risk Register]]
