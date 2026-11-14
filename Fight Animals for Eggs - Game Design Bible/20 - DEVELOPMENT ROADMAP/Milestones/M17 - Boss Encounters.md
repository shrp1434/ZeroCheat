---
title: M17 - Boss Encounters
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - bosses
milestone: M17
stage: 6
complexity: L
---

# M17 - Boss Encounters

> [!info] PROPOSED milestone
> Stage 6 · Size **L** · Critical path: no (12 units of slack) · Exit gate: **G5 Feature complete**

## Objective

Deliver the **CONFIRMED** mini-bosses and world bosses (D-012). The PROPOSED set is eight mini-bosses (one per region) and four world bosses with server-wide scheduling and announcements. Boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]); they are built as config-driven reward tables with placeholder entries that are clearly labelled as not final.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Boss AI framework: phases, telegraphs, threat handling, multiplayer scaling | Engineering, Design | [[Boss AI]], [[Boss Design Overview]], [[Service - BossService]] |
| Eight mini-bosses | Design, Art | [[Mini-Boss - Bramblehorn]], [[Mini-Boss - Dustmane]], [[Mini-Boss - Vinecoil]], [[Mini-Boss - Hammertide]], [[Mini-Boss - Rimeback]], [[Mini-Boss - Stormtalon]], [[Mini-Boss - Cinderjaw]], [[Mini-Boss - Eclipse Panther]] |
| Four world bosses with spawn schedule and announcement | Design, Engineering | [[World Boss - Ironbark Colossus]], [[World Boss - Thunderhoof]], [[World Boss - Abyssal Leviathan]], [[World Boss - Ashwing Condor]] |
| Reward eligibility (once per player per spawn, PROPOSED) and config reward tables | Engineering, Economy | [[Boss Rewards]] |
| Boss progress tracking for unlocks and Progression Score | Engineering | [[Schema - Unlocks and Boss Progress]] |
| Boss health bar | UI | [[UI - Boss Health Bar]] |
| Boss models (BOS-##), attack animations, VFX | Art, Animation | [[Boss Art Direction]], [[Animation - Boss Attacks]] |
| Boss sound and music | Audio | [[Sound - Bosses]], [[Music Direction]] |

## Dependencies

- **Upstream:** [[M06 - Animal Combat]] (combat and rewards), [[M16 - World Design]] (arenas and region gates).
- **Downstream:** [[M18 - UI and UX]], [[M19 - Multiplayer Testing]].

## Complexity

**L.** Twelve distinct encounters on a shared framework, multiplayer scaling, and server-wide scheduling.

## Risks

| Risk | Why it matters here |
|---|---|
| R-002 (readability) | Boss telegraphs must read through many players' VFX. |
| R-007 (inflation) | Boss rewards are a large single-event income. |
| R-018 (server cost) | World boss fights concentrate many players and animals. |
| R-029 (decision latency) | Rewards block beta. |

## Acceptance criteria

- [ ] Every boss is defeatable solo or in a group at its recommended level, according to its document.
- [ ] Every boss attack has a readable telegraph tested in a crowded server.
- [ ] World bosses spawn on their configured cadence and announce ahead of time.
- [ ] Reward eligibility is enforced once per player per spawn; reward contents come from config and are marked as placeholders until [[Open Questions#Q-015]] is decided.
- [ ] Boss defeats update unlocks and the Progression Score.
- [ ] Leash and reset behaviour prevents boss abuse from safe spots.

## Testing requirements

- [[Test Cases - Bosses]]: phases, telegraphs, rewards eligibility, scheduling, reset.
- [[Test Cases - Multiplayer]]: group scaling, kill credit, announcements.
- [[Test Cases - Combat]]: boss damage and defeat penalties.
- [[Test Cases - Mobile Performance]]: world boss fights with a full server.

## Open questions

- [[Open Questions#Q-015]]: exact boss rewards.
- [[Open Questions#Q-014]]: defeat penalties in boss fights.
- [[Open Questions#Q-001]]: world layout determines boss locations.

## Key vault documents
- [[Boss Design Overview]] · [[Boss AI]] · [[Boss Rewards]] · [[Service - BossService]]
- [[Boss Art Direction]] · [[Animation - Boss Attacks]] · [[Sound - Bosses]] · [[UI - Boss Health Bar]]

## Related documents
- [[Development Roadmap]]
- [[M06 - Animal Combat]]
- [[M16 - World Design]]
- [[M19 - Multiplayer Testing]]
- [[World Design Index]]
