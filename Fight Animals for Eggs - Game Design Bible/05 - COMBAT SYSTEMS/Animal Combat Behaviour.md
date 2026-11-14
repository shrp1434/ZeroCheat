---
title: Animal Combat Behaviour
type: system
category: combat
status: mixed
priority: P0
owner: Gameplay Systems Architect
last_updated: 2026-11-14
tags:
  - combat
  - animals
  - ai
  - companions
---

# Animal Combat Behaviour

How the three equipped companions move, fight, protect the player, retreat and recover. Target choice is specified in [[Targeting and Command System]]; abilities in [[Abilities and Cooldowns]]; the formal state machine in [[Combat States and State Machine]].

> [!success] CONFIRMED
> - Exactly **three** equipped animals (D-006), changed only at the player's own base (D-010).
> - Animals auto-target nearby enemies; players can issue manual target commands (D-009).
> - Abilities are manual or automatic (D-008).

Everything else on this page is **PROPOSED**. Values not in [[Canonical Proposed Values]] are new local proposals and are marked *(new)*.

## 1. Design goals
1. Companions are **competent without input**: a player who never issues a command still sees sensible behaviour.
2. Companions **stay with the player**: they never wander off across the region chasing a target.
3. Roles **look different in motion**: Tanks step in front, Ranged and Supports hang back, Assassins flank.
4. Low-health companions **protect themselves** before being knocked out, so losses feel avoidable.

## 2. Follow and formation

Out of combat, each companion occupies a formation slot relative to the player's facing direction.

| Slot | Default occupant | Offset from player (right, up, back) in studs *(new)* |
|---|---|---|
| 1 | First equipped animal | (−5, 0, 4) left-rear |
| 2 | Second equipped animal | (5, 0, 4) right-rear |
| 3 | Third equipped animal | (0, 0, 7) rear |

- Slots are filled in team order. When combat starts, slots are re-assigned by role (below).
- Companions path with `PathfindingService` when the direct line is blocked and steer directly otherwise ([[Implementation - Animal AI State Machine]]).
- Catch-up: a companion more than 20 studs from its slot moves at 125% of its MS until it is within 6 studs *(new)*. Air-swimming aquatic animals follow the same rules (D-043, PROPOSED).

### Combat stance by role

| Role | Preferred position while engaging *(new)* | Stand-off distance |
|---|---|---|
| Tank | Between the player and the primary target | Melee (5 studs) |
| Bruiser | Beside the Tank, on the target's flank | Melee (5 studs) |
| Assassin | Behind the target (flank angle ≥ 120° from Tank) | Melee (5 studs) |
| Skirmisher | Orbits the target, repositions every 2–3 s | Melee (5 studs) |
| Ranged | Behind the player, line of sight to target | 20–28 studs |
| Support | Within 12 studs of the lowest-HP ally | 14–18 studs |
| Controller | Mid-line, within ability range of the target cluster | 10–12 studs |

Basic attack ranges are canonical (§3): melee 5, Ranged 28, Support 18, Controller 12.

## 3. Engage rules

| Rule | Value |
|---|---|
| Acquisition radius | Enemies within **30 studs of the player** *(new)* are candidates. Companions never acquire targets based on their own position, which prevents runaway chains. |
| Default behaviour | **Assist**: attack the player's focus target, anything attacking the player or a companion, then the best-scoring candidate ([[Targeting and Command System#Auto-target scoring]]). |
| Passive wildlife | Neutral or skittish wild animals that have not entered combat are **not** auto-engaged. The player must attack them or command an attack. This stops companions dragging the player into fights. |
| Bosses | Auto-engaged only once the player is in the boss arena and the boss is in combat. |
| Other players | Never targeted outside PvP or a raid. |

## 4. Leash to the player

| Condition | Response *(new)* |
|---|---|
| Companion is more than **45 studs** from the player | Drop target, switch to `Returning`, move to slot. The companion keeps its threat on the enemy table but stops attacking. |
| More than **90 studs** from the player, or path blocked for more than 4 s | Teleport to its slot with a short dissolve effect ([[VFX - Combat Effects]]). |
| Player enters a safe zone (hub, own base outside a raid) | All companions disengage and teleport to slots on arrival. |
| Player teleports (portal, respawn) | Companions travel with the player; they do not remain behind. |

The 45-stud soft leash is shorter than the wild animal leash (60 studs from spawn, canonical §4), so a player who walks away reliably pulls the team out before the wild animal resets.

## 5. Retreat when low

| Trigger | Behaviour *(new)* |
|---|---|
| HP ≤ **25%** of max | `Retreating`: move to the slot furthest from the current target, stop basic attacks, keep automatic **defensive or healing** abilities active, keep manual abilities available to the player. |
| Re-engage | When HP ≥ 50% (healing or Support), or when the player issues a direct attack command to that companion. |
| Tanks | Retreat threshold is **15%** instead of 25%, so the Tank holds aggro longer. |
| All three below threshold | Only the companion with the highest HP re-engages; this avoids a team that does nothing. |

Enemies may still chase a retreating companion; the retreat is about position and reduced exposure, not invulnerability.

## 6. Commands and stances
Players influence companions through commands, not stance micro-management. Commands (attack this target, regroup, hold) and their input are in [[Targeting and Command System#Command set]]. A command overrides auto-targeting for 8 s or until the target dies.

## Knock-out and recovery

At 0 HP a companion is **knocked out (KO)**. It plays a short collapse animation, becomes untargetable and non-colliding, and fades to a "spirit" marker at its last position before returning to the player as an icon on the team bar ([[UI - Animal Team Display]]).

> [!warning] UNDECIDED (Q-204)
> **Companion knock-out recovery rule.** The owner has not chosen how knocked-out companions come back. Options are below. The recommendation is a proposal only.

| Option | Rule | Pros | Cons |
|---|---|---|---|
| A. Timed field recovery | KO companion returns at 50% HP **30 s after the player's combat tag ends** | Simple; never strands a player; encourages pacing | Low tension |
| B. Base or hub only | KO companion returns only when the player visits their base or the hub | Strong tension; base visits matter | Punishing in a team-locked game (D-010); new players can end up fighting alone |
| C. Field revive | Player channels 3 s within 6 studs of the spirit marker; returns at 30% HP; 45 s per-companion cooldown | Player skill and agency | Cluttered in boss fights; vulnerable to griefing in PvP |
| **D. Hybrid (recommended)** | A + C: timed recovery after combat, plus an optional field revive during combat. Instant full recovery at the base or hub. | Never strands the player, rewards attention in long fights, keeps base visits useful | Two rules to teach |

**Recommendation (PROPOSED, unapproved):** option D. Values *(new)*: `CompanionRecoverySeconds` = 30, recovery HP 50%, field revive channel 3 s, revive HP 30%, `CompanionReviveCooldownSeconds` = 45, revive interrupted by damage to the player.

Further rules (PROPOSED):
- KO is **not** death: the animal is never lost, never damaged permanently and loses no ascension. Animal loss exists only through raid theft ([[Animal Theft Rules]]).
- In a raid, a knocked-out **defender** stays down for the rest of the raid and may be captured ([[Animal Theft Rules]]). Field revive is disabled for raid defenders.
- In PvP, KO companions recover at the end of the duel or match ([[PvP System]]).
- If the player is defeated, all companions are restored on respawn ([[Player Defeat and Penalties]]).

## 8. Out-of-combat regeneration
When the combat tag (8 s) expires, the player and active companions regenerate **10% of max HP per second** *(new)*. Regeneration stops immediately when a new combat tag is applied.

## 9. Performance notes
- Companion AI ticks at 10 Hz on the server, with movement interpolated on clients *(new)*; full budgets are in [[Animal Scalability and Performance Budgets]].
- 16 players × 3 companions = 48 companions per server at the canonical cap (§15). They are budgeted separately from the "≤ 60 wild animals with full AI" limit, so a full server can run up to 108 full-AI animals at once. See [[Wild Animal AI#Performance and simulation tiers]].
- Network ownership of companions stays with the server ([[Network Ownership]]).

## 10. Test hooks
- With no player input, a Common team clears a Whisperwood Forest wild Common in 4–9 s ([[Damage, Defence and Health Model]]).
- Walking 46 studs away from a fight makes every companion disengage within 0.5 s.
- A companion at 24% HP stops basic attacks and moves away; at 51% it re-engages.
- KO companion recovers 30 s after combat tag expiry, not 30 s after KO.
- Cases in [[Test Cases - Animal AI]].

## Related documents
- [[Targeting and Command System]]
- [[Abilities and Cooldowns]]
- [[Combat States and State Machine]]
- [[Animal Roles]]
- [[Team Equipping and Base Lock Rule]]
- [[Service - AnimalAIService]]
- [[Implementation - Animal AI State Machine]]
- [[Animation - Animal Locomotion]]
- [[Animation - Animal Defeat and Victory]]
