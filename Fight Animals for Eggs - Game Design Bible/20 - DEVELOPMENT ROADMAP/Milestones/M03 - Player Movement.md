---
title: M03 - Player Movement
type: milestone
category: roadmap
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - movement
  - input
milestone: M03
stage: 1
complexity: S
---

# M03 - Player Movement

> [!info] PROPOSED milestone
> Stage 1 · Size **S** · Critical path: **yes** · Exit gate: **G1 Technical foundation** (with M02)

## Objective

Give the player a responsive, readable avatar controller on PC, mobile and gamepad, with a camera that supports combat against groups and a greybox test area. Movement uses the Roblox Humanoid with the PROPOSED default walk speed of 16 studs per second ([[Canonical Proposed Values#4. Combat values (PROPOSED)]]). The dodge roll is specified in [[Player Combat]] but is built in [[M04 - Player Combat]], because it shares the combat input layer.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Input layer for keyboard and mouse, touch and gamepad using ContextActionService and UserInputService | Engineering | [[Client Controllers]] |
| Camera controller for exploration and combat | Engineering, Design | [[Camera Behaviour Guidelines]] |
| Player locomotion animation set (idle, walk, run, jump, fall, land) | Animation | [[Animation Bible]] |
| Server-side movement sanity checks (speed and teleport detection) | Engineering, Security | [[Exploit Prevention]] |
| Greybox test region and hub stub | Design, Art | [[World Overview and Map]] |
| Mobile control layout draft | UI | [[UI - Main HUD]], [[UI Accessibility Standards]] |
| Footstep and movement sounds, placeholder | Audio | [[Sound Bible]] |

## Dependencies

- **Upstream:** [[M02 - Core Project Setup]].
- **Downstream:** [[M04 - Player Combat]], [[M05 - Animal AI]] (needs a moving target to follow and chase), [[M16 - World Design]] (greybox scale and traversal metrics).

## Complexity

**S.** Uses standard Roblox character movement. The work is feel tuning, multi-device input and the camera.

## Risks

| Risk | Why it matters here |
|---|---|
| R-019 (mobile performance) | Mobile frame time is measured from this milestone onwards. |
| R-023 (exploits) | Speed and teleport checks must not punish legitimate high-latency players. |
| R-003 (team lock friction) | Traversal speed and base travel shape how costly a base round-trip feels. |

## Acceptance criteria

- [ ] The player can move, jump and look on keyboard and mouse, touch and gamepad, with no input dead ends.
- [ ] The camera never clips into terrain in the greybox and keeps the player readable at combat distances.
- [ ] Server speed checks flag simulated speed hacks in tests and do not flag a player on a throttled connection.
- [ ] Mobile controls do not overlap one another on the smallest supported screen.
- [ ] The reference mid-range phone holds the PROPOSED 30 FPS minimum in the greybox.

## Testing requirements

- [[Test Cases - Mobile Performance]]: frame rate and touch layout on reference devices.
- [[Test Cases - Multiplayer]]: movement replication between two or more clients.
- [[Test Cases - Exploit Prevention]]: speed and teleport detection.

## Open questions

- **UNDECIDED** (Q-1110): primary platform priority (mobile, PC, console) for controls and optimisation. Working assumption: mobile and PC equally, gamepad supported.
- [[Open Questions#Q-001]]: world scale depends on layout; use greybox metrics only.

## Key vault documents
- [[Client Controllers]] · [[Camera Behaviour Guidelines]] · [[Player Combat]]
- [[UI Accessibility Standards]] · [[Performance Guidelines]] · [[Exploit Prevention]]

## Related documents
- [[Development Roadmap]]
- [[M02 - Core Project Setup]]
- [[M04 - Player Combat]]
- [[M05 - Animal AI]]
- [[M16 - World Design]]
