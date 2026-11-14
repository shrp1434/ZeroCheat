---
title: Target Audience and Player Motivations
type: vision
category: game-vision
status: proposed
priority: P1
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - vision
  - audience
  - player-motivation
---

# Target Audience and Player Motivations

> [!info] PROPOSED
> Everything in this document is a direction-team proposal. No external market research has been commissioned or is cited here. Audience segments are design hypotheses to be tested in [[M21 - Beta Testing]] using our own analytics ([[Service - AnalyticsAndLoggingService]]).

## 1. Who we are building for

*Fight Animals for Eggs* targets the broad Roblox audience that already enjoys collecting, hatching and fighting games, and gives them something those games usually lack: **hands-on combat in which the player fights alongside their collection**, and **luck that is explained honestly**.

| Dimension | Proposal | Design consequence |
|---|---|---|
| Platform mix | PC, mobile and console players on Roblox. Mobile is assumed to be a large share. | Touch-first controls, one-thumb basic attack, readable at phone size ([[UI Accessibility Standards]]), 30 FPS minimum on mid-range mobile ([[Canonical Proposed Values#15. Server and performance targets (PROPOSED)]]). |
| Age | A wide range, including younger players. | Plain language, no gore, no horror (D-026), strict compliance for paid random items ([[Roblox Monetisation Policy Requirements]]), parental-trust friendly fairness rules ([[Design Principles and Fairness Charter]]). |
| Session length | Short mobile sessions (5–15 min) through long PC sessions (60+ min). | Every 5-minute slice must produce progress (Cash, XP, an index entry); long sessions need region, boss and base goals ([[Session Flow and Player Journey]]). |
| Social context | Solo players, friend groups, and strangers sharing a server. | Shared kill credit (D-040 **PROPOSED**), world bosses that scale with participants, optional PvP (D-023). |
| Spending | The majority of players are expected never to spend. | Fully playable without Robux (D-027). See [[Free-to-Play Experience]]. |

## 2. Player motivation segments

These segments overlap. Most players combine two or three. Each segment lists the systems that must satisfy it.

| Segment | Core desire | Key systems | Risk if neglected |
|---|---|---|---|
| **Collectors** | Fill the index, own every species and variant. | [[Animal Index Feature Specification]], [[Animal Collection System]], [[Animal Variants]], [[Hatch System]] | Collection feels padded or unreachable; Secret animals feel fake. |
| **Fighters** | Master combat, beat bosses, optimise a team. | [[Player Combat]], [[Targeting and Command System]], [[Boss Design Overview]], [[Team Equipping and Base Lock Rule]] | Combat becomes auto-play; bosses become stat checks. |
| **Builders** | Grow and customise a base that looks impressive. | [[Player Base System]], [[Base Upgrade System]], [[Egg Merging Station]] | Base is a menu, not a place. |
| **Explorers** | See new places, find secrets and rare spawns. | [[World Overview and Map]], the region documents, [[Wild Animal Spawning and Respawn]] | Regions feel like reskinned arenas. |
| **Competitors** | Test themselves against other players. | [[PvP System]], [[Base Raiding System]] | Raids feel punishing or exploit-ridden; non-competitors feel hunted. |
| **Socialisers** | Play with friends, show off pulls and bases. | Shared world (D-025), world bosses, hatch presentation ([[Egg Animations]]) | The world feels empty or hostile. |

### 2.1 Motivation to system matrix

| System | Collectors | Fighters | Builders | Explorers | Competitors | Socialisers |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| Wild combat | ● | ●●● | ○ | ●● | ● | ● |
| Animal Index | ●●● | ○ | ○ | ●● | ○ | ● |
| Egg rolls and hatching | ●●● | ● | ○ | ○ | ● | ●● |
| Ascension | ●● | ●●● | ○ | ○ | ●● | ● |
| Egg merging | ●● | ○ | ●● | ○ | ● | ○ |
| Base modules | ● | ●● | ●●● | ○ | ●● | ●● |
| Bosses | ● | ●●● | ○ | ●● | ● | ●●● |
| Region unlocks | ●● | ●● | ○ | ●●● | ○ | ● |
| PvP and raids | ○ | ●● | ● | ○ | ●●● | ● |

●●● primary driver · ●● strong · ● minor · ○ negligible

## 3. Motivations by stage of play

| Stage | Typical level | Dominant motivation | What must be visible |
|---|---|---|---|
| First 10 minutes | 1–3 | Novelty, clarity | One clear objective at a time ([[New Player Onboarding]]) |
| First session | 1–6 | First hatch, first team of three | Cash-to-roll progress bar; odds panel on first roll |
| First week | 6–30 | Region unlocks, first Epic, base growth | Next gate requirement; next module upgrade cost |
| First month | 30–65 | Ascension goals, world bosses, merging | Duplicate counters, boss timers, station level |
| Long term | 65–100 | Secret animals, variants, index completion, rivalry | Index completion, rare-spawn announcements, raid history |

## 4. Design guardrails derived from the audience

1. **Readability beats realism.** Silhouette, colour and telegraph clarity come before anatomical detail ([[Animal Modelling Principles]], [[Combat Feedback and Readability]]).
2. **No hidden loss.** Anything a player can lose (eggs in base storage, knocked-out defenders during a raid) is shown before they opt in. See [[Design Principles and Fairness Charter]].
3. **Odds in plain words.** The odds panel shows percentages and a plain-language line such as "About 1 in 125 rolls" ([[UI - Egg Rolling]]).
4. **Respect short sessions.** No mandatory waits are proposed for hatching or merging at launch (hatch timing is **UNDECIDED**, [[Open Questions#Q-023]]; merge timing is **UNDECIDED**, [[Open Questions#Q-034]]).
5. **Accessibility from day one.** Colour-blind-safe rarity cues (shape and pattern as well as colour) and reduced-flash options ([[UI Accessibility Standards]], [[Rarity Visual Language]]).

## 5. Hypotheses to validate in beta

| ID | Hypothesis | Signal |
|---|---|---|
| H1 | Players understand the hybrid combat within the first fight. | Player deals a share of team damage above a threshold in the first five kills |
| H2 | The base lock adds strategy rather than frustration. | Rate of "return to base to change team" versus quitting after a lost fight |
| H3 | Honest odds disclosure increases trust. | Odds-related support contacts and survey responses |
| H4 | Optional raids attract Competitors without driving away others. | Retention of players who never opt into raids versus those who do |
| H5 | The region ladder provides a clear medium-term goal. | Time-to-gate distribution per region ([[Region Unlock Progression]]) |

## Related documents
- [[Game Vision Index]]
- [[Vision Statement and Pillars]]
- [[Unique Selling Points and Identity]]
- [[Session Flow and Player Journey]]
- [[Free-to-Play Experience]]
- [[Design Principles and Fairness Charter]]
