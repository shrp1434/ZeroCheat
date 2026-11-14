---
title: Risk Register
type: register
category: roadmap
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - risk
  - production
  - governance
---

# Risk Register

The live list of project risks for *Fight Animals for Eggs*. Each risk has an ID, a likelihood and impact score, a mitigation, an owner and a **trigger** (the observable signal that the risk is turning into an issue). Milestone documents cite risks by ID. The staged plan they belong to is in [[Development Roadmap]].

> [!info] PROPOSED — scoring model
> Likelihood (L) and Impact (I) are each scored 1–5. **Score = L × I.** Bands: **1–6 Low**, **8–12 Medium**, **15–25 High**. High risks are reviewed at every stage gate and whenever their trigger fires. This scale is a local **PROPOSED** production convention, not a game value.

| Score | Likelihood meaning | Impact meaning |
|---:|---|---|
| 1 | Very unlikely in this project | Cosmetic; no player or schedule effect |
| 2 | Unlikely | Minor rework inside one milestone |
| 3 | Plausible | Milestone slips or a feature is weakened |
| 4 | Likely | A stage gate fails, or players are visibly harmed |
| 5 | Expected without action | Launch blocked, data loss, policy breach or loss of player trust |

## How to use this register

1. **Add** a risk when anyone can name a trigger for it. Use the next free `R-` ID. Never reuse IDs.
2. **Review** at every stage gate in [[Development Roadmap#Stage gates]]. Re-score; record closed risks under [[#Closed and retired risks]] with the reason.
3. **Escalate** to the project owner any High risk whose mitigation needs an owner decision. Most of those map to an open question in [[Open Questions]].
4. **Link** the risk ID from the milestone that carries the mitigation work.

---

## Design risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-001 | The core loop (fight → cash → roll → hatch → ascend) feels grindy once the novelty of the first hatches wears off. | 3 | 5 | 15 | Combat-slice and core-loop playtests at gates G2 and G3. Run the [[Balance Simulation Plan]] and [[Progression Bottleneck Analysis]] before beta. Keep merging as a deterministic route alongside random rolls. | Lead Game Designer | Playtesters stop between region 1 and region 2, or describe rolling as "the only thing to do". |
| R-002 | Hybrid real-time combat (player plus three animals, in a shared world) becomes visually unreadable. | 4 | 4 | 16 | Readability rules in [[Combat Feedback and Readability]]; priority tiers in [[Audio Mixing and Priority]]; VFX budgets in [[VFX Bible]]. Test in crowded servers during [[M19 - Multiplayer Testing]]. | Combat Designer | Testers cannot identify which enemy is attacking them, or which animal is theirs, in a fight with 3+ players. |
| R-003 | The **CONFIRMED** team lock (team changes only at the player's own base, D-010) frustrates players who leave with the wrong team. | 3 | 3 | 9 | Clear pre-departure team check in [[UI - Team Selection]]; fast base travel from [[Hub - Hatchling Haven]]. The rule itself is not changed without the owner. | Lead Game Designer | Repeated base round-trips per session in telemetry; complaints in playtests. |
| R-004 | Optional raids feel mandatory or punishing; theft drives defenders to quit. | 3 | 5 | 15 | Use the **CONFIRMED** protections (offline immunity, backpack safety, undefeated defenders unstealable, three-animal cap) and the proposed shields and compensation in [[Raid Rewards and Defender Compensation]]. Matchmaking bands ([[Open Questions#Q-029]]). | PvP Designer | Raided players' return rate falls clearly below non-raided players' in beta cohorts. |
| R-005 | Fully independent hatches (no pity, D-018 **CONFIRMED**) create long bad-luck streaks that players read as rigged. | 4 | 3 | 12 | Accurate odds disclosure; merging as a guaranteed path; ascension gives duplicates value; [[Statistical Testing of Probabilities]] evidence available to support staff. | Economy and Progression Designer | Support or community reports alleging manipulated odds. |
| R-006 | Eight regions and twelve bosses exceed what the loop needs, diluting each area. | 3 | 3 | 9 | Region list remains **UNDECIDED** ([[Open Questions#Q-001]]); cut line agreed in pre-production (**UNDECIDED** (Q-1103)). | Lead Game Designer | Greybox regions in [[M16 - World Design]] lack distinct activities. |

## Economy risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-007 | Cash inflation from shared kill credit (D-040) combined with late region multipliers (up to ×11.5) and stacking base bonuses. | 4 | 4 | 16 | Model cash per hour per region in [[Expected Value Calculations]]; sinks in [[Cash Sources and Sinks]]; farming analysis in [[Inflation and Farming Exploit Risks]]. Economy telemetry from [[M21 - Beta Testing]]. | Economy and Progression Designer | Observed cash per hour exceeds the modelled band for a region in beta. |
| R-008 | Late-game costs (station levels 4–5, module L5) create a wall where players stop progressing. | 3 | 4 | 12 | [[Progression Bottleneck Analysis]]; tune via [[Balance Update Process]]. Costs stay **PROPOSED** ([[Open Questions#Q-019]]). | Economy and Progression Designer | Large share of beta players stalled at the same station level. |
| R-009 | Multi-account farming feeds a main account through raids or shared kill credit. | 3 | 4 | 12 | Raid eligibility rules in [[Raid Eligibility and Offline Protection]]; detection in [[Raid Anti-Exploit Validation]]; telemetry flags in [[Service - AnalyticsAndLoggingService]]. | Security Engineer | Repeated raids between the same account pair, or one-sided kill credit patterns. |
| R-010 | Egg storage (60 total) frustrates hoarding while expansion currency and price are **UNDECIDED** ([[Open Questions#Q-009]], [[Open Questions#Q-010]]). | 3 | 3 | 9 | Merging frees capacity; storage UI warns before rolls; decision required before beta. | Economy and Progression Designer | Players blocked from rolling by full storage more than occasionally in playtests. |

## Compliance risks

> [!danger] Compliance
> Odds disclosure is a **CONFIRMED** principle (D-017): actual odds are shown before the player commits and never change silently after purchase. Any risk in this section scoring 10 or more is treated as High regardless of its score.

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-011 | Displayed odds differ from the odds the server uses (stale cache, rounding, wrong progression score). | 2 | 5 | 10 | Server-issued `oddsVersion` tokens (D-041); automated parity check between disclosed table and server table on every build; [[Statistical Testing of Probabilities]]; release checklist in [[Versioning and Changelog Policy]]. | Lead Engineer | Any parity-check failure, or any player report with a screenshot that disagrees with server logs. |
| R-012 | A Robux product grants Cash, eggs or luck directly or indirectly, turning egg rolls into paid random items that need restriction handling. | 3 | 5 | 15 | D-044 (**PROPOSED**: no Robux for Cash); [[Open Questions#Q-032]] resolved before launch; `PolicyService:GetPolicyInfoForPlayerAsync` checks for `ArePaidRandomItemsRestricted` designed in [[Roblox Monetisation Policy Requirements]]. | Monetisation Lead | Any proposed product in [[Monetisation Product Concepts]] that touches Cash, eggs, rolls or odds. |
| R-013 | A content update adds an animal to a hatch pool without re-normalising, re-verifying and re-disclosing the pool. | 2 | 5 | 10 | Mandatory rules in [[Content Expansion Guidelines#Adding an animal without breaking hatch pools]]; odds-table version bump; release checklist gate. | Live Operations Director | Pool sum check fails in CI, or a release candidate has a pool change without a new odds-table version. |
| R-014 | Theft, combat or creature depiction conflicts with platform standards or the experience's content rating. | 2 | 4 | 8 | Visual direction D-026 (no horror); review against Community Standards and content rating guidance ([[Roblox Platform References]]); questionnaire answers **UNDECIDED** (Q-1116). | Art Director | Moderation flag, rating questionnaire uncertainty, or reviewer concern in beta. |
| R-015 | Monetisation is perceived as pay-to-win, contradicting D-027. | 2 | 4 | 8 | [[Monetisation Principles]]; [[Free-to-Play Experience]] audit at beta; no paid power in PvP or raids. | Monetisation Lead | Community feedback or beta surveys naming purchases as necessary. |

## Technical risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-016 | DataStore request budgets are exhausted at peak (autosave, raids, purchases, shutdown). | 3 | 5 | 15 | Budget-aware write scheduling in [[Service - DataService]]; session locking and retry policy in [[Save, Load and Recovery]]; load tests in [[M19 - Multiplayer Testing]]. | Lead Engineer | Throttling warnings in logs, or queued writes during soak tests. |
| R-017 | Cross-player transfers (raid theft of eggs and animals) duplicate or lose items when a server or client fails mid-transaction. | 3 | 5 | 15 | Transaction design in [[Data Consistency and Transactions]] and [[Implementation - Raid Session Controller]]; disconnect matrix in [[Raid Disconnection Handling]]. | Lead Engineer | Any reconciliation mismatch between attacker and defender records in tests. |
| R-018 | Server simulation cost: up to 180 wild animals plus 16 players × 3 companions (PROPOSED budgets) exceeds frame budget. | 4 | 4 | 16 | [[Animal Scalability and Performance Budgets]]; AI LOD; [[M20 - Optimisation]]. Server size stays **UNDECIDED** ([[Open Questions#Q-031]]). | Lead Engineer | Server heartbeat below target in a full-server soak. |
| R-019 | Mobile clients miss the PROPOSED 30 FPS minimum, or run out of memory, in busy areas. | 3 | 4 | 12 | Polygon, texture and VFX budgets in [[Performance Guidelines]]; StreamingEnabled; [[Test Cases - Mobile Performance]] from M03 onwards. | Technical Artist | Device-lab captures below target on a reference mid-range phone. |
| R-020 | Latency makes real-time combat feel unresponsive, or server-authoritative hit validation rejects legitimate hits. | 3 | 4 | 12 | Client prediction and server validation rules in [[Latency Handling]] and [[Implementation - Combat Damage Pipeline]]. | Lead Engineer | Rejected-hit rate rises with ping in test logs; testers report "ghost hits". |
| R-021 | Pathfinding for many animals is too expensive or unreliable on complex terrain. | 3 | 3 | 9 | Steering for short ranges, pathfinding only when needed ([[Implementation - Animal AI State Machine]]); navigation-friendly level design in [[M16 - World Design]]. | AI Engineer | Animals stuck or path requests queuing in AI profiling. |
| R-022 | A server-shutdown or update rollout interrupts transactions (roll, hatch, merge, ascension). | 3 | 4 | 12 | `game:BindToClose` flush; idempotent transactions; rollout method **UNDECIDED** (Q-1115). | Lead Engineer | Any lost or duplicated item after a forced shutdown test. |

## Security risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-023 | Exploiters abuse remotes: fake hits, speed or teleport, free rolls, out-of-range interactions. | 5 | 5 | 25 | Server authority ([[Server-Client Responsibilities]]); [[Implementation - Remote Validation Layer]]; [[Implementation - Rate Limiting]]; [[Threat Model]]; [[Test Cases - Exploit Prevention]] every milestone. | Security Engineer | Any validation bypass in internal red-team tests, or anomaly alerts after launch. |
| R-024 | Raid exploits: leaving to avoid loss, exceeding the three-animal cap, stealing undefeated defenders or backpack eggs. | 4 | 5 | 20 | Server-side theft rules in [[Egg Theft Rules]] and [[Animal Theft Rules]]; [[Raid Anti-Exploit Validation]]; [[Raid Disconnection Handling]]. | Security Engineer | Any test in [[Test Cases - Raiding]] that violates a **CONFIRMED** theft rule. |
| R-025 | Item duplication through interrupted merge or ascension transactions. | 3 | 5 | 15 | [[Implementation - Egg Merge Transaction]], [[Implementation - Ascension Transaction]]; duplicate-ID audits in [[Data Validation and Migration]]. | Lead Engineer | Item count audit shows more items than issued. |
| R-026 | No channel for players to report exploits privately, so exploits spread publicly first. | 3 | 3 | 9 | Exploit-reporting route **UNDECIDED** (Q-1119); support macros in [[Bug Reporting and Severity]]. | Live Operations Director | Exploit videos appear before internal reports. |

## Scope risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-027 | Sixty animals (**CONFIRMED** target) with rigs, animations, variants and audio exceed art and audio capacity. | 4 | 5 | 20 | Shared rigs per body plan ([[Animal Rig Standards]]); modular animation sets; variants as material sets ([[Variant Visual Treatments]]); production tracking in [[Asset Register]]. | Art Director | Per-animal throughput in [[M16 - World Design]] falls below the rate needed to finish the roster before [[M21 - Beta Testing]]. |
| R-028 | Feature creep: systems not in the owner brief (trading, per-animal levelling, extra currencies) enter scope. | 3 | 3 | 9 | D-042 and D-045 (**PROPOSED**); every new system needs a Decision Register entry; [[Definition of Done]]. | Production Manager | Backlog items with no link to a decision or brief item. |
| R-029 | Owner decisions on blocking questions arrive after the gate that needs them. | 4 | 4 | 16 | Decision schedule per gate in [[Development Roadmap#Decisions needed per gate]]; configurable values for every **UNDECIDED** number. | Production Manager | A gate review opens with a blocking question unresolved. |
| R-030 | Launch scope has no agreed cut line, so a slip in one area delays everything. | 3 | 4 | 12 | Cut line **UNDECIDED** (Q-1103); [[Scope and Launch Targets]]. | Production Manager | Critical-path milestone exceeds its size class by a full step. |

## Team risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-031 | Key-person dependency: one engineer owns persistence and raid transactions. | 3 | 4 | 12 | Pairing and code review on data code ([[Luau Coding Standards]]); documented services; staffing **UNDECIDED** (Q-1101). | Lead Engineer | Only one person can explain a data-layer change in review. |
| R-032 | Documentation drifts from implementation and from [[Canonical Proposed Values]]. | 3 | 3 | 9 | Single source for numbers; config modules generated from the canonical page ([[Configuration Modules]]); vault link check before each gate. | Technical Documentation Architect | Code constants differ from the canonical page in review. |
| R-033 | QA capacity is insufficient for statistical odds tests and multi-client tests. | 3 | 4 | 12 | Automated sampling harness ([[Statistical Testing of Probabilities]]); [[Test Plan Matrix]] prioritisation; early test-server scheduling. | QA Lead | Test Plan Matrix rows marked "not run" at a gate. |
| R-034 | Overwork near beta and launch. | 3 | 4 | 12 | Relative sizing and critical-path visibility; cut line agreed in advance; no date promises without capacity estimates. | Production Manager | Repeated overtime requests; defect injection rises. |

## Live operations risks

| ID | Risk | L | I | Score | Mitigation | Owner | Trigger |
|---|---|---:|---:|---:|---|---|---|
| R-035 | The game depends on a constant release treadmill to retain players. | 3 | 4 | 12 | Evergreen loop design in [[Live Operations Framework#Evergreen principle]]; cadence **UNDECIDED** (Q-1104). | Live Operations Director | Engagement drops sharply in weeks with no update. |
| R-036 | Hotfix path is too slow for a critical exploit or data bug after launch. | 3 | 5 | 15 | Hotfix lane in [[Content Update Pipeline#Hotfix lane]]; kill switches in config. | Live Operations Director | A critical bug remains live longer than the hotfix target in [[Live Operations Framework]]. |
| R-037 | Limited-time content creates FOMO backlash or breaks the "fully playable without Robux" principle. | 2 | 4 | 8 | Rules in [[Seasonal and Limited-Time Events]]; permanence **UNDECIDED** (Q-1105). | Live Operations Director | Event feedback dominated by "missed forever" complaints. |
| R-038 | A balance nerf to ascended animals destroys trust in long-term investment. | 3 | 4 | 12 | Change limits and communication rules in [[Balance Update Process]]; compensation policy **UNDECIDED** (Q-1107). | Economy and Progression Designer | Negative sentiment after a balance patch focused on one animal. |

---

## Top risks (High band)

| Rank | ID | Score | Milestones carrying mitigation |
|---:|---|---:|---|
| 1 | R-023 | 25 | Every milestone; hardened in [[M19 - Multiplayer Testing]] |
| 2 | R-024 | 20 | [[M15 - Base Raids]] |
| 3 | R-027 | 20 | [[M16 - World Design]] |
| 4 | R-002 | 16 | [[M06 - Animal Combat]], [[M19 - Multiplayer Testing]] |
| 5 | R-007 | 16 | [[M08 - Egg Rolling]], [[M21 - Beta Testing]] |
| 6 | R-018 | 16 | [[M05 - Animal AI]], [[M20 - Optimisation]] |
| 7 | R-029 | 16 | [[M01 - Pre-production]], every gate |
| 8 | R-001, R-004, R-012, R-016, R-017, R-025, R-036 | 15 | See each risk |

Compliance risks R-011 and R-013 are High by rule despite a score of 10.

## Closed and retired risks

None yet. When a risk closes, move its row here with the gate at which it closed and the evidence.

## Related documents
- [[Development Roadmap]]
- [[Roadmap Index]]
- [[Open Questions]]
- [[Decision Register]]
- [[Threat Model]]
- [[Randomised Reward Compliance]]
- [[Inflation and Farming Exploit Risks]]
- [[Live Operations Framework]]
- [[QA Strategy]]
