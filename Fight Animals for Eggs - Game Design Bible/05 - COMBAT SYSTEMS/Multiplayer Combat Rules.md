---
title: Multiplayer Combat Rules
type: system
category: combat
status: mixed
priority: P0
owner: Gameplay Systems Architect
last_updated: 2026-11-14
tags:
  - combat
  - multiplayer
  - networking
  - security
---

# Multiplayer Combat Rules

How combat behaves when many players share one world: who can hurt whom, how shared enemies are credited, and what the server checks. Network architecture is owned by [[Multiplayer Architecture]]; this page states the combat rules that architecture must enforce.

> [!success] CONFIRMED
> - One large shared world that supports single-player and multiplayer play (D-025).
> - PvP is optional (D-023). Raiding is optional (D-024).

> [!info] PROPOSED
> Shared kill credit (D-040), server cap of 16 players ([[Open Questions#Q-031]]) and the combat values in [[Canonical Proposed Values]] are proposals. New values are marked *(new)*.

## Hostility matrix

Who can damage whom. Anything not marked "Yes" is blocked on the server, regardless of what the client sends.

| Context | Wild animals and bosses | Own companions | Other players | Other players' companions | Base structures and guards |
|---|---|---|---|---|---|
| PvE (default) | Yes | No | No | No | No |
| PvP (valid pairing, see [[PvP System]]) | Yes | No | Yes, opponent only | Yes, opponent's only | No |
| Raid, attacker | No wild animals inside a base | No | Defender only | Defender's guards only | Yes, the target base only |
| Raid, defender | No wild animals inside a base | No | Attacker only | Attacker's companions only | Never their own |
| Safe zone (hub, own base outside a raid) | No | No | No | No | No |

Rules:
- **No friendly fire** in PvE. Area attacks (Ground Slam, area abilities) only affect valid hostile targets.
- **Collision:** companions do not collide with other players or other players' companions *(new)*, to stop body-blocking and griefing in narrow paths. Implemented with collision groups (*unverified* configuration details; see [[Network Ownership]]).
- **Third parties cannot interfere with raids or duels.** Non-participants cannot enter a base under raid ([[Base Raiding System]]) and cannot damage duel participants.

## Sharing wild animals

| Rule | Value |
|---|---|
| Ownership | None. Any player may attack any wild animal; nobody "tags" it exclusively. |
| Kill credit | Full reward to every player with ≥ 10% of max HP contributed (D-040, PROPOSED; [[Combat Rewards]]). |
| Threat | One shared threat table per wild animal ([[Wild Animal AI]]). |
| Pull limit | At most 4 wild animals in combat with one player at a time *(new)*. |
| Scaling | Wild animals are **not** scaled by nearby player count; groups simply kill faster. Bosses and rare spawns scale ([[Boss AI#Participant scaling]]). |

### Training (dragging enemies onto others)
Dragging aggressive animals onto another player is limited by the 60-stud spawn leash (40 for Territorial animals) and by threat decay beyond 30 studs. A wild animal never switches to a player who has not damaged it or entered its aggro radius.

## Support effects across players *(new)*

| Effect | Applies to |
|---|---|
| Heals, shields and buffs from companions | The owner and the owner's companions only, at launch |
| Rally Cry | The caster's own team only ([[Player Combat]]) |
| Field revive of a downed player (boss fights) | Any player can revive any other player |

Cross-player healing is a candidate for a later group or party feature. Restricting it at launch removes an exploit vector (healing a raider from outside the base, or feeding contribution).

## Server authority and validation

Clients send **intents**; the server resolves outcomes ([[Server-Client Responsibilities]], [[Remote Communication Contract]]).

| Intent (client → server) | Server checks *(new tolerances)* |
|---|---|
| `Attack(seq)` | Player state allows attacking; time since last hit ≥ 0.45 s × 0.9; target in arc and within 7 + 3 studs of the server-side position |
| `Special(id, targetId or point)` | Unlocked by level; cooldown expired on the server clock; range + 3 studs; not stunned |
| `Dodge(direction)` | Cooldown 4 s; direction normalised; displacement applied by the server-validated movement |
| `Command(kind, targetId, slot)` | Target eligible and within 40 studs; ≤ 4 commands per second |
| `UseAbility(slot, target, requestId)` | Companion alive and not stunned; ability exists on species; cooldown; 0.5 s team GCD; range |

General rules:
1. **Damage is never sent by the client.** The client never sends amounts, HP or reward values.
2. **Positions:** the server uses its own replicated position of the player. If the server sees movement faster than walk speed × 1.5 sustained for 1 s (outside dodges and teleports), the player is flagged and pulled back ([[Exploit Prevention]]).
3. **Rate limits:** attack intents above 110% of the nominal rate over a 2 s window are dropped and counted; repeated violations escalate ([[Implementation - Rate Limiting]]).
4. **No lag compensation by rewind at launch.** Range tolerance (+3 studs) covers typical latency. Revisit after [[M19 - Multiplayer Testing]] ([[Latency Handling]]).
5. **Idempotency:** every request carries a sequence number or request ID; duplicates are ignored.
6. **Remotes:** intents use `RemoteEvent`. Purely cosmetic broadcasts (hit sparks for distant players) may use `UnreliableRemoteEvent` *(per Roblox documentation; delivery is not guaranteed by design)*.

### Illustrative attack validation

```lua
-- Illustrative Luau, not tested in Roblox Studio.
local MELEE_RANGE, RANGE_TOLERANCE = 7, 3
local MIN_HIT_INTERVAL = 0.45 * 0.9

local function validateAttack(state, target, now: number): (boolean, string?)
	if not state.canAttack then return false, "State" end
	if now - state.lastHitTime < MIN_HIT_INTERVAL then return false, "Rate" end
	if not Hostility.canDamage(state.player, target) then return false, "Hostility" end
	local distance = (target.position - state.serverPosition).Magnitude
	if distance > MELEE_RANGE + RANGE_TOLERANCE then return false, "Range" end
	return true
end
```

## Replication budget *(new)*
- Damage events are sent at most 10 times per second per client and only for actors within 150 studs; farther actors receive HP bar updates at 2 Hz.
- Damage numbers for other players' hits are hidden by default to reduce clutter ([[Combat Feedback and Readability]]).
- See [[Replication Strategy]] and [[Animal Scalability and Performance Budgets]].

## Leaving and disconnecting during combat

| Situation | Rule (PROPOSED) |
|---|---|
| Player leaves during a wild fight | Character and companions removed; the wild animal re-evaluates threat. No penalty. |
| Player leaves during a boss fight | Contribution for that spawn is lost (bosses are per-server). Boss HP is not scaled down. |
| Player leaves while PvP-tagged | Counts as a loss for rating only; no material loss ([[PvP System]]). |
| Player leaves during a raid | See [[Raid Disconnection Handling]]. |

General disconnect handling (saving, session locks) is owned by [[Disconnect Handling]].

## Test hooks
- Ground Slam next to another player's companion deals 0 damage to it in PvE.
- Forged `Attack` 30 studs from the target is rejected with reason `Range`.
- 20 attack intents per second produce at most the nominal number of hits.
- Two players at 50% each on a wild Epic both receive full Cash.
- Cases in [[Test Cases - Multiplayer]] and [[Test Cases - Exploit Prevention]].

## Related documents
- [[Multiplayer Architecture]]
- [[Shared World and Player Sessions]]
- [[Server-Client Responsibilities]]
- [[Implementation - Remote Validation Layer]]
- [[Combat Rewards]]
- [[PvP System]]
- [[Base Raiding System]]
- [[Threat Model]]
