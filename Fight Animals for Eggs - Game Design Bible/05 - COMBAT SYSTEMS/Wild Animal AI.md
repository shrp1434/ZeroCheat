---
title: Wild Animal AI
type: system
category: combat
status: mixed
priority: P0
owner: Gameplay Systems Architect
last_updated: 2026-11-14
tags:
  - combat
  - ai
  - wild-animals
  - performance
---

# Wild Animal AI

How wild animals notice, fight, chase, give up and reset. Spawning, spawn points and respawn timers are owned by [[Wild Animal Spawning and Respawn]]; the formal state machine is in [[Combat States and State Machine]].

> [!success] CONFIRMED
> Wild animals respawn, and rarer animals respawn more slowly (D-011). Hidden luck does **not** change wild encounter rarity (D-017).

> [!info] PROPOSED
> Temperaments, radii, threat rules and simulation tiers are proposals. Canonical values: wild HP ×2.0, ATK ×0.75, region multiplier on HP and ATK, leash 60 studs from spawn with reset to full HP, combat tag 8 s ([[Canonical Proposed Values]] §4–§6). Other values are marked *(new)*.

## Temperaments

Every wild species has one temperament, set in its spawn data. Defaults by role and rarity are below; individual animal documents may override them.

| Temperament | Behaviour | Aggro radius *(new)* | Default for |
|---|---|---:|---|
| **Skittish** | Flees when a player comes within its radius; fights back weakly only if cornered | 14 studs (flee) | Common Support animals (for example [[Duck]]) |
| **Neutral** | Ignores players until attacked, then fights | — | Most Commons and Uncommons |
| **Territorial** | Attacks players who enter its radius; gives up sooner (leash 40 studs instead of 60) | 18 studs | Most Rares and Epics; Tanks and Bruisers at any rarity |
| **Aggressive** | Attacks players who enter its radius and calls nearby same-species animals | 26 studs | Legendary and above; Assassins from Epic upwards |

Rules:
- Whisperwood Forest uses no Aggressive animals so that new players are never ambushed ([[New Player Onboarding]]).
- A player in the hub, their own base or within 3 s of a respawn is never aggroed.
- Aggro checks require line of sight within the radius; behind full cover the radius halves *(new)*.

## Threat and target choice

Wild animals use a per-enemy threat table instead of companion-style scoring.

| Source | Threat *(new)* |
|---|---|
| Damage dealt | 1 threat per point of damage |
| Tank companion damage | × 2.0 |
| Healing done to anyone the wild animal is fighting | 0.5 per point healed |
| Taunt | Sets the taunter to 150% of the current highest threat for the taunt's duration |
| First aggro (proximity) | 10 threat to the triggering player |

- The wild animal attacks the highest-threat target in reach.
- **Switch rule:** a melee wild animal switches only when a new target exceeds the current one by 30%; a ranged one by 10% *(new)*. This lets Tanks hold attention.
- Threat decays by 10% per second for any participant who is more than 30 studs away *(new)*.
- Threat tables are cleared on `Reset`.

## Chase, leash and reset

| Rule | Value |
|---|---|
| Chase speed | Species MS (canonical §3; not scaled by rarity or region) |
| Leash | 60 studs from spawn point (canonical §4); 40 studs for Territorial *(new)* |
| On leash | `Reset`: invulnerable, clears threat, walks back to spawn, restores full HP |
| Unreachable target | If no path to any threat-table entry for 3 s *(new)*, the animal enters `Reset`. Stops "pillar cheese" from ledges and water. |
| Ranged harassment from out of reach | Counted as unreachable; same response |
| Reward on reset | None. Contribution resets with the threat table. |

## Group behaviour

| Behaviour | Rule *(new)* |
|---|---|
| Pack call | Aggressive animals alert same-species animals within 12 studs, which join with 10 threat on the caller's target. |
| Herd scatter | Skittish animals within 10 studs of a fleeing animal also flee. |
| Pull limit | At most 4 wild animals can be in combat with one player at once; further animals stay in `Alert`. This keeps early regions forgiving and limits server load. |

## Wild animal abilities

- Uncommon and above may use one ability from their species kit ([[Animal Abilities Catalogue]]) at the automatic cooldown band ([[Abilities and Cooldowns]]).
- Every wild ability that deals more than 25% of the target's max HP must have a ground or body telegraph of at least **0.6 s** *(new)*. Mythical and Secret rare-spawn attacks use boss telegraph rules ([[Boss AI#Telegraph rules]]).
- Wild animals never use crowd control on the same target twice within 6 s *(new)*.

## Rarity flavour

| Rarity | AI difference *(new)* |
|---|---|
| Common, Uncommon | Basic attacks only (Common) or one simple ability (Uncommon). Short alert time. |
| Rare, Epic | One ability, uses role stance (Ranged keep distance, Assassins flank). |
| Legendary | Ability plus a single 50%-HP behaviour change (for example a speed burst). |
| Mythical, Secret | Server-announced rare spawns (canonical §6). Treated as small group encounters: participant scaling and telegraphs as in [[Boss AI]]. **UNDECIDED** how hard they should be (Q-212, see [[Damage, Defence and Health Model#Balance findings]]). |

## Performance and simulation tiers

Canonical budget (§15): **≤ 180 wild animals simulated per server, ≤ 60 with full AI near players.** Companions (up to 48 at the 16-player cap) are budgeted separately.

| Tier | Condition *(new)* | Simulation |
|---|---|---|
| Full | In combat, or a player within 80 studs | 10 Hz AI tick, pathfinding, full animation replication |
| Ambient | Nearest player 80–200 studs | 2 Hz, straight-line wander only, no pathfinding |
| Dormant | No player within 200 studs | Not simulated; respawn timers still run; model may be streamed out (StreamingEnabled) |

- If more than 60 animals qualify for Full, the furthest non-combat animals drop to Ambient.
- Pathfinding requests are throttled to 20 per second per server *(new)*; animals waiting for a path steer directly.
- Details in [[Animal Scalability and Performance Budgets]] and [[Performance Guidelines]].

## Implementation notes
- AI runs in [[Service - AnimalAIService]]; damage goes through [[Service - CombatService]]. The server owns every wild animal's physics ([[Network Ownership]]).
- Wild animal definitions are data: temperament, radius, ability ID and leash override per species ([[Configuration Modules]]).

## Test hooks
- A Neutral animal does not attack a player standing 1 stud away until hit.
- A Territorial animal resets at 40 studs from spawn; a Neutral one at 60.
- Standing on an unreachable rock and shooting triggers `Reset` after 3 s; no reward is granted.
- A fifth wild animal near a player in combat with four stays in `Alert`.
- Cases in [[Test Cases - Animal AI]].

## Related documents
- [[Wild Animal Spawning and Respawn]]
- [[Combat States and State Machine]]
- [[Boss AI]]
- [[Combat Rewards]]
- [[Animal Index]]
- [[Service - SpawnService]]
- [[Implementation - Animal AI State Machine]]
- [[Animal Scalability and Performance Budgets]]
