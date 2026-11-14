---
title: Test Cases - Mobile Performance
type: test-cases
category: qa
status: proposed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - performance
  - mobile
  - optimisation
---

# Test Cases - Mobile Performance

Performance, memory, load-time and mobile usability test cases. System documents: [[Performance Guidelines]], [[Animal Scalability and Performance Budgets]], [[Replication Strategy]], [[UI Accessibility Standards]], [[VFX Bible]], [[Audio Mixing and Priority]].

> [!info] PROPOSED targets
> From [[Canonical Proposed Values]] §15: **60 FPS on a mid-range PC; 30 FPS minimum on a mid-range mobile device**; 16 players per server; ≤ 180 simulated wild animals. QA turns these into measurable pass criteria (all **PROPOSED**, introduced here):
> - **Mobile pass:** 95th-percentile frame time ≤ 33.3 ms over a 5-minute capture, and no single stall above 100 ms during gameplay (loading screens excluded).
> - **PC pass:** 95th-percentile frame time ≤ 16.7 ms over a 5-minute capture.
> - **Soak:** 60-minute session; median FPS in minute 55–60 is at least 90% of the median in minute 5–10; client memory in minute 55–60 is no more than 5% above minute 10 (no sustained leak).
> Memory, bandwidth and load-time budgets are owned by [[Performance Guidelines]] and referenced here as `B_mem`, `B_net` and `B_load`.

> [!warning] Reference devices UNDECIDED
> Which physical devices define "low-end", "mid-range" and "high-end" mobile is **UNDECIDED** (Q-1010). Until decided, QA keeps one device per tier from the test pool and records its model in every capture so results are comparable over time.

**Measurement.** Developer Console (memory and network tabs), MicroProfiler captures, and the QA-build frame-time logger that records per-frame times and writes p50 / p95 / p99 to the capture report. Each capture records device, graphics quality level, server player count and build number. Graphics quality is tested at the automatic setting and at the lowest manual level.

## 1. Gameplay scenarios

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MOB-001 | Hub with a full server | Mid-range mobile; 16 players in [[Hub - Hatchling Haven]] | 1) Idle and walk for 5 minutes. | Mobile pass criteria met. | P0 | performance | D-025 |
| TC-MOB-002 | Standard combat | Three companions; six wild enemies | 1) Fight for 5 minutes with abilities. | Mobile pass criteria met; ability VFX within the budget in [[VFX - Combat Effects]]. | P0 | performance | D-005 |
| TC-MOB-003 | Crowded region | 8 players with 24 companions in one region near the wild-animal cap | 1) Fight for 5 minutes. | Mobile pass; distant companions and wild animals use reduced animation and VFX LOD. | P0 | performance | D-025 |
| TC-MOB-004 | Region traversal with streaming | StreamingEnabled | 1) Travel through every unlocked region. | No stall above 100 ms during traversal; memory stays below `B_mem`; no missing collision. | P0 | performance | D-025 |
| TC-MOB-005 | Five-egg multi-hatch | Five eggs including Secret | 1) Multi-hatch. | Mobile pass during the 5.0 s presentation; particle counts reduced at low quality ([[Animation - Egg Hatch]]). | P0 | performance | D-016 |
| TC-MOB-006 | Single hatch and roll animations | — | 1) Roll ×5; hatch one. | Mobile pass. | P1 | performance | D-015 |
| TC-MOB-007 | Merge at station L5 | Celestial Convergence Altar | 1) Merge Mythical → Secret. | Mobile pass for the full animation. | P1 | performance | D-020 |
| TC-MOB-008 | Ascension to A5 | — | 1) Ascend and view the A5 aura on three equipped animals in combat. | Mobile pass; A5 auras use the budget in [[VFX - Rarity and Variant Effects]]. | P1 | performance | D-037 |
| TC-MOB-009 | Raid with defences | Defence Station L5; turrets; defenders | 1) Attack for 5 minutes. | Mobile pass for attacker and defender. | P0 | performance | D-024 |
| TC-MOB-010 | Mini-boss fight | Any mini-boss, 4 players | 1) Full fight. | Mobile pass. | P1 | performance | D-012 |
| TC-MOB-012 | World boss with a full server | 16 players, 48 companions | 1) Full fight. | Mobile pass at the lowest graphics level; at the automatic level p95 ≤ 33.3 ms or the VFX LOD drops automatically to reach it. | P0 | performance | D-012 |
| TC-MOB-013 | Rare-spawn announcement during a boss | Boss active; Mythical rare-spawn announced | 1) Observe. | No stall above 100 ms when the notification and its sound play. | P2 | performance | D-011 |

## 2. Base and UI scenarios

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MOB-020 | Fully upgraded neighbouring bases | 16 bases at plot stage 4 with all modules L5 | 1) Walk through the base area. | Mobile pass; base LOD per [[Base Art Direction]]. | P0 | performance | D-022 |
| TC-MOB-021 | Animal Index screen | All 60 species discovered | 1) Scroll through [[UI - Animal Index Screen]]. | Scrolling stays above 30 FPS; ViewportFrame previews are limited to the visible page; memory returns to within 5% of the pre-open value after closing. | P1 | performance | D-029 |
| TC-MOB-022 | Inventory with 100 animals | Working capacity reached | 1) Open, sort and filter [[UI - Animal Inventory]]. | Each action responds within one frame budget after the first open; no stall above 100 ms. | P1 | performance | Q-022 |
| TC-MOB-023 | Storage UI at maximum capacity | Base 200, backpack 25 | 1) Open [[UI - Egg Storage]]. | No stall above 100 ms; list virtualised. | P2 | performance | D-021 |

## 3. Pens display, if enabled

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MOB-030 | Displayed owned animals | Pens display enabled (Q-008) and several players with 100 animals | 1) Visit the base area. | Mobile pass. The number of displayed animals per base and their LOD follow [[Module - Animal Pens]]. If the target cannot be met, the result is reported to the owner as evidence for Q-008. | P1 | performance | Q-008 |

## 4. Soak, load and network

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MOB-040 | 60-minute soak | Mid-range mobile; normal play loop | 1) Play the core loop for 60 minutes. | Soak criteria met (FPS ≥ 90% of the early median; memory growth ≤ 5%). | P0 | performance | D-025 |
| TC-MOB-041 | Thermal throttling | Same as TC-MOB-040 in a warm room | 1) Record FPS over time. | Report the curve; if it fails the soak criterion, raise a bug with the capture. | P2 | performance | D-025 |
| TC-MOB-042 | Cold load time | App closed; mobile | 1) Launch and join. | Time to playable ≤ `B_load`; loading screen shows progress; `ContentProvider` preloading limited to essential assets. | P1 | performance | D-025 |
| TC-MOB-043 | Client receive bandwidth | Full server in a busy region | 1) Record network receive for 10 minutes. | Average ≤ `B_net`. | P1 | performance | D-025 |
| TC-MOB-044 | Background and resume | Mid-session | 1) Switch to another app for 60 s. 2) Return. | Session resumes or reconnects cleanly; no duplicated actions; state consistent. | P1 | edge | D-025 |
| TC-MOB-045 | Server heartbeat at capacity | 16 players, 180 wild animals | 1) Record server frame time for 30 minutes. | Within the server budget in [[Animal Scalability and Performance Budgets]]. | P0 | performance | D-025 |

## 5. Mobile usability

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-MOB-050 | Touch controls for combat | Phone | 1) Use basic attack, three specials, dodge and three animal abilities. | All reachable without covering the character; touch target sizes per [[UI Accessibility Standards]]; buttons bound through `ContextActionService` or the touch UI in [[UI - Main HUD]]. | P0 | functional | D-005 |
| TC-MOB-051 | Aspect ratios | Narrow phone, standard phone, tablet | 1) Open every main screen. | Layout correct using `UIScale` and `UIAspectRatioConstraint`; nothing clipped. | P1 | functional | D-025 |
| TC-MOB-052 | Safe areas and notches | Phone with a notch | 1) Inspect HUD edges. | No critical control inside unsafe screen areas (inset from `GuiService`). | P1 | functional | D-025 |
| TC-MOB-053 | Odds readable on small screens | Phone | 1) Open roll and hatch confirmation. | All seven odds rows readable without zooming (compliance, D-017). | P0 | functional | D-017 |
| TC-MOB-054 | Text size | Smallest supported phone | 1) Read body text and labels. | Minimum text size per [[Typography]]. | P2 | functional | D-025 |

## Related documents

- [[Test Cases - Multiplayer]]
- [[Test Cases - Bosses]]
- [[Test Cases - Animal AI]]
- [[Performance Guidelines]]
- [[Animal Scalability and Performance Budgets]]
- [[Replication Strategy]]
- [[UI Accessibility Standards]]
- [[VFX Bible]]
- [[M20 - Optimisation]]
