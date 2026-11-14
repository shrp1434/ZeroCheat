---
title: M04 - Player Combat
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - combat
  - player-strength
milestone: M04
stage: 2
complexity: L
---

# M04 - Player Combat

> [!info] PROPOSED milestone
> Stage 2 · Size **L** · Critical path: **yes** (co-critical with M05) · Exit gate: **G2 Combat slice** (with M05, M06)

## Objective

Make the player a real combatant, as **CONFIRMED** by D-005 and D-007: basic attacks, special moves with cooldowns, and a Player Strength statistic separate from animal strength. Build the server-authoritative damage pipeline that animals and bosses will reuse, and the combat state machine for the player.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Three-hit basic combo, three specials and dodge roll at PROPOSED values | Engineering, Design | [[Player Combat]], [[Canonical Proposed Values#4. Combat values (PROPOSED)]] |
| Player Strength, HP and DEF from level | Engineering, Design | [[Player Strength]], [[Player Progression and Levelling]] |
| Damage pipeline: hit request, server validation, damage formula, application, feedback | Engineering | [[Implementation - Combat Damage Pipeline]], [[Damage, Defence and Health Model]] |
| Combat states, combat tag and cooldown tracking | Engineering | [[Combat States and State Machine]], [[Abilities and Cooldowns]] |
| Hit validation under latency (range, angle, timing tolerance) | Engineering | [[Latency Handling]] |
| Player attack and special animations | Animation | [[Animation - Player Attacks and Specials]] |
| Hit sparks, special VFX and impact sounds | VFX, Audio | [[VFX - Combat Effects]], [[Sound - Combat Impacts]] |
| Combat HUD: health, cooldowns, Player Strength readout | UI | [[UI - Main HUD]], [[UI - Player Strength Display]] |
| Defeat flow with configurable penalties (values **UNDECIDED**) | Engineering, Design | [[Player Defeat and Penalties]] |
| Training dummy and test arena | Design | [[Combat System Overview]] |

## Dependencies

- **Upstream:** [[M03 - Player Movement]].
- **Downstream:** [[M06 - Animal Combat]] (reuses the pipeline), [[M17 - Boss Encounters]] (through M06).

## Complexity

**L.** Responsive real-time combat with server authority is one of the hardest feel problems on Roblox. Latency tolerance, animation timing and server validation all interact.

## Risks

| Risk | Why it matters here |
|---|---|
| R-020 (latency and rejected hits) | Validation tolerances are tuned here first. |
| R-023 (remote exploitation) | Damage is never trusted from the client. |
| R-002 (readability) | Player VFX scale must leave room for three animals and other players. |

## Acceptance criteria

- [ ] The combo, specials and dodge behave as specified in [[Player Combat]], with values read from config.
- [ ] Cooldowns are enforced on the server; client display matches server state.
- [ ] The damage formula output matches hand-calculated values in [[Damage, Defence and Health Model]] within the PROPOSED random spread.
- [ ] Player Strength changes with level and with bonuses, and is shown separately from any animal statistic (D-007).
- [ ] Hits from a client with simulated added latency are accepted when legitimate and rejected when out of range.
- [ ] Defeat triggers the defeat flow; penalty values come from config and are labelled **UNDECIDED** in any UI copy until decided.

## Testing requirements

- [[Test Cases - Combat]]: combo timing, specials, cooldowns, damage formula, defeat flow.
- [[Test Cases - Exploit Prevention]]: forged hit requests, cooldown bypass, range spoofing.
- [[Test Cases - Mobile Performance]]: combat VFX on reference devices.

## Open questions

- [[Open Questions#Q-014]]: exact defeat penalties per battle type. Build with configurable values; no final numbers.
- [[Open Questions#Q-003]]: final statistics (player values are tuned alongside animal stats).
- **UNDECIDED** (Q-1110): platform priority affects the mobile special-move button layout.

## Key vault documents
- [[Combat System Overview]] · [[Player Combat]] · [[Player Strength]]
- [[Damage, Defence and Health Model]] · [[Abilities and Cooldowns]] · [[Combat States and State Machine]]
- [[Implementation - Combat Damage Pipeline]] · [[Service - CombatService]] · [[Combat Feedback and Readability]]

## Related documents
- [[Development Roadmap]]
- [[M03 - Player Movement]]
- [[M05 - Animal AI]]
- [[M06 - Animal Combat]]
- [[Risk Register]]
