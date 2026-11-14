---
title: Raid Eligibility and Offline Protection
type: spec
category: pvp-and-raiding
status: mixed
priority: P0
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - raids
  - eligibility
  - offline-protection
  - matchmaking
  - safeguards
---

# Raid Eligibility and Offline Protection

Who may raid whom, the precise meaning of "online", and what happens when the defender leaves during a raid.

> [!success] CONFIRMED
> **An offline base is never raidable** (D-024). Raiding is optional (D-024).

> [!warning] UNDECIDED
> - Raid matchmaking: who can raid whom ([[Open Questions#Q-029]]).
> - Raid opt-in mechanism (Q-207, new; options in [[Base Raiding System#Raid opt-in]]).

## Definition of "online"

> [!info] PROPOSED definition
> A defender is **online for raid purposes** at time *t* if, and only if, **all** of the following are true on the server that hosts their base:
> 1. Their `Player` object is present in `Players` on this server, and `Players.PlayerRemoving` has not fired for them.
> 2. Their profile is loaded and its session lock is held by this server ([[Save, Load and Recovery]]).
> 3. A client heartbeat from them was received within the last `OnlineHeartbeatTimeoutSeconds` (10 s *(new)*). The client sends a heartbeat every 2 s through a dedicated `RemoteEvent`.
> 4. They are not in an outbound teleport to another place or server.
> 5. The server is not shutting down (`game:BindToClose` has not fired).
>
> If any condition is false, the defender is **offline** and their base is **not raidable**. There is no grace period in the defender's disfavour: as soon as the server knows a condition is false, the base is treated as offline.

Consequences:
- Because bases are hosted by the owner's session server (PROPOSED, Q-209), an offline player's base is normally not loaded at all, so it cannot be targeted. The checks above also cover the edge cases: a player who is mid-departure, frozen, or teleporting.
- A defender who is AFK but still connected and heartbeating is **online**. AFK protection is the role of shields ([[Shield Mechanics]]), not of offline protection. Roblox's own idle disconnect (*unverified* exact timing) eventually makes such a player offline.

## Defender leaves mid-raid

When the server detects that the defender has become offline (any condition above) at time *T* during `Active` or `Breached`:

| Item | Rule (PROPOSED) |
|---|---|
| The raid | Immediately moves to `Resolving` with reason `DefenderOffline` ([[Raid Lifecycle and States]]). No theft action is accepted after *T*. |
| Eggs secured before *T* | Stay with the attacker. They were taken while the defender was online and are already committed. |
| An egg being carried at *T* | Returns to the defender's vault. |
| Animals held provisionally | Transferred only if the vault was breached **before** *T* (the raid is then successful, [[Base Raiding System#Definition of a successful raid]]). Otherwise returned. |
| Capture channel in progress at *T* | Cancelled; the animal is not captured. |
| Shield | The post-raid shield is applied to the defender's base as normal. |
| Attacker | No attacker cooldown if the raid was not successful; normal cooldown if it was. |

Rationale: this rule never lets a theft happen while the base is offline (honouring D-024) and gives no reason to "rage-quit": leaving stops further theft but does not undo what was already secured, exactly as if the attacker had extracted at *T*.

> [!danger] Edge case: heartbeat loss
> A defender whose connection degrades may stop heartbeating while their `Player` object remains. After 10 s the raid ends with `DefenderOffline`. This is deliberate: we would rather end a raid early than risk a theft from a player who could not defend. Log every such case for review ([[Raid Anti-Exploit Validation]]).

## Eligibility checklist

All checks run on the server in `Requested`. The attacker sees the first failing reason.

### Defender (target) must
| Check | Value | Status |
|---|---|---|
| Be online (definition above) | — | **CONFIRMED** principle, PROPOSED definition |
| Have opted into raiding | Q-207 | **UNDECIDED** mechanism |
| Have a built [[Module - Egg Vault]] | — | **PROPOSED** |
| Be at or above `RaidMinimumLevel` | 20 *(new)* | **PROPOSED** |
| Have no active shield | [[Shield Mechanics]] | **PROPOSED** |
| Not be in another raid or in `Aftermath` | — | **PROPOSED** |
| Have received fewer than `MaxRaidsReceivedPerDay` raids in the last 24 h | 3 *(new)* | **PROPOSED** |
| Not be inside a world boss or mini-boss arena while that boss is in combat | — | **PROPOSED** *(new)* |
| Be inside the attacker's matchmaking band | Q-029 | **UNDECIDED** |

### Attacker must
| Check | Value |
|---|---|
| Have opted into raiding (reciprocal, recommended under Q-207) | — |
| Be at or above `RaidMinimumLevel` | 20 *(new)* |
| Have a built Egg Vault with at least one free base storage slot | So stolen eggs have somewhere to go ([[Egg Theft Rules]]) |
| Have at least one free owned-animal slot | Working assumption 100 animals ([[Open Questions#Q-022]]); see [[Animal Theft Rules]] |
| Not be combat-tagged, in PvP, in a boss arena or in another raid | — |
| Be outside `AttackerRaidCooldownSeconds` since their last raid | 900 s *(new)* |
| Not have raided this defender within `PairRaidCooldownSeconds` | 86,400 s *(new)* |
| Have no active shield, or accept that starting a raid removes it | [[Shield Mechanics#Breaking a shield]] |

## Matchmaking (Q-029)

> [!warning] UNDECIDED (Q-029)
> Who can raid whom is undecided ([[Open Questions#Q-029]]). Options:

| Option | Rule | Pros | Cons |
|---|---|---|---|
| A. Level band | Attacker may raid defenders within ±10 levels | Easy to explain | Level ignores team rarity and base investment |
| B. Progression Score band | Within ±150 PS ([[Progression Score Specification]]) | Captures level, collection, bosses and base | Players cannot easily see PS; must be explained |
| C. Base progression band | Within ±25% of total module levels | Matches defences to offence weakly | A strong team with a weak base becomes a target magnet |
| D. Unrestricted with protection | Anyone opted-in, protected only by shields and caps | Most targets | Strong players farm weak ones |
| **E. B with an "upward" bonus (recommended)** | Within ±150 PS; raiding a defender with higher PS is always allowed up to +300 | Protects weaker players; rewards ambition | Slightly more complex |

**Recommendation (PROPOSED, unapproved): option E.** It is the only option that stops a high-progression player from targeting much weaker bases while still allowing underdog raids. The Raid Board shows only eligible bases, so players never see targets they cannot raid ([[UI - Raid Interface]]).

## New player protection (PROPOSED)
- Below `RaidMinimumLevel` (20) a player can neither raid nor be raided, whatever their opt-in setting. Level 20 is inside Emerald Canopy's range (canonical §5), after two mini-bosses.
- The first time a player reaches level 20, the raid opt-in is explained with a clear choice, defaulting to **not** opted in.

## Implementation notes
- Eligibility is a pure function of server state, evaluated in one frame, so it cannot change between check and start. The raid record is created in the same frame ([[Implementation - Raid Session Controller]]).
- Heartbeats are rate-limited (at most one accepted per second) to stop spam ([[Implementation - Rate Limiting]]).

```lua
-- Illustrative Luau, not tested in Roblox Studio.
local HEARTBEAT_TIMEOUT = 10

local function isOnlineForRaid(session, now: number): boolean
	return session.player.Parent ~= nil
		and not session.removing
		and session.profileLockHeld
		and (now - session.lastHeartbeat) <= HEARTBEAT_TIMEOUT
		and not session.teleportingOut
		and not ServerState.shuttingDown
end
```

## Test hooks
- `PlayerRemoving` during `Active`: raid ends within one frame with `DefenderOffline`; no theft accepted afterwards.
- Heartbeat stopped for 10.1 s: same outcome; 9.9 s: raid continues.
- Defender in a world boss arena in combat: Raid Board does not list them.
- Level 19 player cannot appear on any Raid Board.
- Cases in [[Test Cases - Raiding]].

## Related documents
- [[Base Raiding System]]
- [[Raid Lifecycle and States]]
- [[Raid Disconnection Handling]]
- [[Shield Mechanics]]
- [[Shared World and Player Sessions]]
- [[Disconnect Handling]]
- [[UI - Raid Interface]]
