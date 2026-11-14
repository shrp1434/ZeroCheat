---
title: PvP System
type: system
category: pvp-and-raiding
status: mixed
priority: P1
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - pvp
  - combat
  - safeguards
  - matchmaking
---

# PvP System

The rules that apply to every player-versus-player fight, whichever activation method the owner chooses. Base raids are a separate mode with their own rules ([[Base Raiding System]]).

> [!success] CONFIRMED
> PvP is **optional**. Players choose whether to take part (D-023).

> [!warning] UNDECIDED
> - **How PvP is activated** is undecided ([[Open Questions#Q-011]]). Options and a labelled recommendation are in [[PvP Activation Options]].
> - PvP defeat consequences are part of [[Open Questions#Q-014]]; see [[Player Defeat and Penalties]].
> - PvP reward type (Q-203, new): see Rewards below.

> [!info] PROPOSED
> Everything else on this page is a proposal. New values are marked *(new)*.

## Core rules

| Rule | Value |
|---|---|
| Participants | Each player fights with their three equipped companions (D-006). The team lock still applies (D-010). |
| Consent | No player can be damaged by another player without having opted in through the chosen activation method. |
| Targets | Only the opponent(s) and their companions ([[Multiplayer Combat Rules#Hostility matrix]]). |
| Damage formula | The normal pipeline ([[Damage, Defence and Health Model]]) × **PvP damage scalar 0.5** *(new)* on all damage to players and their companions. |
| Crowd control vs players | Durations × 0.5; stun immunity 4 s after a stun; knock-backs at 50% distance *(new)* |
| Knocked-out companions | Stay out until the fight ends; restored afterwards. Never stealable in PvP. |
| Material loss | None (recommended option P-A in [[Player Defeat and Penalties]], unapproved) |
| PvP tag | 15 s *(new)*, longer than the PvE combat tag (8 s), so players cannot step out of PvP mid-exchange |

### Why a 0.5 damage scalar
In PvE the player's time-to-defeat against a same-rarity threat is 5–11 s ([[Damage, Defence and Health Model#On-curve reference teams]]). Player-plus-team against player-plus-team without a scalar would end fights in 2–4 s, too fast to dodge or react. The scalar targets a **PvP time-to-defeat of 12–25 s** *(new)* for evenly matched players.

## Encounter design

| Format | Players | Win condition *(new)* | Where |
|---|---|---|---|
| Duel | 1 v 1 | First player defeated loses; animals KO'd do not end the duel | Wherever both accept; a 40-stud duel ring appears |
| Arena skirmish | 1 v 1 or 2 v 2 | Best of three rounds; round ends when a side's players are all defeated | Arena zone ([[PvP Activation Options]]) |
| Open-world PvP | Free-for-all among flagged players | No formal win; defeat ends the encounter | Only if a toggle or region option is chosen |

Duel and arena rules (PROPOSED):
- Countdown 3 s, both sides at full HP, cooldowns reset.
- Wild animals cannot enter the duel ring; wild animals already in combat with a duellist keep fighting them (no exploit: the wild animal is not a weapon, it only attacks those it has threat on).
- Leaving the duel ring for more than 5 s forfeits.

## Matchmaking and fairness

| Mechanism | Rule *(new)* |
|---|---|
| Arena queue band | Match by Progression Score ([[Progression Score Specification]]) within ±100 points, widening by 25 points every 15 s up to ±200 |
| Duels | Any level gap allowed, because both players consent. The request shows both players' level and team rarity before acceptance. |
| Open-world PvP | Only players within ±10 levels can damage each other |
| No stat normalisation | At launch, teams fight with real stats. Normalised ranked modes are a post-launch option. |

## Rewards

> [!warning] UNDECIDED (Q-203)
> **What does winning PvP give?** Options:
> 1. Cosmetic rewards and a visible rating only.
> 2. A small Cash reward from the system (never from the loser), capped per day.
> 3. A separate PvP currency for cosmetics.
>
> **Recommendation (PROPOSED, unapproved):** option 1 plus a daily-capped option 2. Rewards never come from the loser, so there is no reason to prey on weaker players. Suggested cap: 5 rewarded wins per day, each worth the Cash of 10 wild Commons in the winner's highest unlocked region *(new)*.

Anti-farming for any reward *(new)*:
- The same pair of players can generate at most 3 rewarded results per hour.
- A win counts only if the loser dealt at least 10% of the winner's max HP (stops "stand still" win trading).
- Rewards and ratings are server-side and logged ([[Service - PvPService]]).

## Safeguards

| Safeguard | Rule *(new)* |
|---|---|
| New player protection | Players below level 15 cannot enable open-world PvP or enter the arena queue, and cannot be targeted. They can still accept duels. |
| Level bands | Open-world: ±10 levels. Arena: Progression Score band. |
| Spawn protection | 5 s invulnerability after respawning from a PvP defeat, ended early by attacking. A player defeated by the same opponent twice within 2 minutes becomes immune to that opponent for 5 minutes. |
| Toggle cooldown | If a toggle exists: 300 s between changes; cannot switch off while PvP-tagged. |
| Combat-log rule | Leaving the game while PvP-tagged records a loss for rating purposes only. No item, Cash, egg or animal loss. Repeated combat-logging (3 times in 24 h) blocks arena queueing for 30 minutes. |
| Safe zones | No PvP in the hub, at a player's own base (outside raids), or in boss arenas during a boss fight. |
| Harassment | Block a player to prevent duel requests from them; repeated declined requests (3 in 5 minutes) mute that requester for 10 minutes. Chat moderation uses Roblox systems ([[Security Architecture]]). |
| Boss fights | PvP damage is disabled inside boss arenas so groups cannot be sabotaged. |

## Interaction with raids
PvP and raids are separate opt-ins. Enabling PvP does not make a base raidable; opting into raids does not enable open-world PvP (raid opt-in is Q-207, see [[Raid Eligibility and Offline Protection]]).

## Data and services
- [[Service - PvPService]] owns pairing, tags, ring zones and results. Damage goes through [[Service - CombatService]] with a `PvP` context flag.
- Rating and records are stored with the player profile ([[Schema - Player Profile]]).

## Test hooks
- A level 14 player cannot be damaged in open-world PvP by anyone.
- A forged damage request against a non-consenting player is rejected with reason `Hostility`.
- Duel of identical builds lasts 12–25 s in a bot simulation.
- Leaving while PvP-tagged leaves inventory unchanged and records one loss.
- Cases in [[Test Cases - PvP]].

## Related documents
- [[PvP Activation Options]]
- [[Multiplayer Combat Rules]]
- [[Player Defeat and Penalties]]
- [[UI - PvP Interface]]
- [[Service - PvPService]]
- [[Design Principles and Fairness Charter]]
- [[Test Cases - PvP]]
