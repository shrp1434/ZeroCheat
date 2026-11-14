---
title: Latency Handling
type: architecture
category: networking
status: mixed
priority: P0
owner: Multiplayer and Network Engineer
last_updated: 2026-11-14
tags:
  - multiplayer
  - networking
  - latency
  - combat
---

# Latency Handling

Real-time hybrid combat (D-005, **CONFIRMED**) must feel immediate on a 200 ms mobile connection without letting a high-latency player, or a client faking latency, gain an advantage. The approach: **predict only what belongs to the local player, confirm everything that affects anyone else on the server, and validate hits with bounded tolerances.**

> [!info] PROPOSED
> All tolerances and rates on this page are **PROPOSED** and appear in [[Implementation - Combat Damage Pipeline]]. Tune them in [[M19 - Multiplayer Testing]].

## 1. Latency assumptions

| Connection class | Round-trip time (assumed) | Target experience | Status |
|---|---|---|---|
| Good PC / Wi-Fi | 40–120 ms | Full quality | **PROPOSED** assumption |
| Typical mobile | 120–250 ms | Full quality, slightly later damage numbers | **PROPOSED** assumption |
| Poor mobile | 250–400 ms | Playable; hits near the edge of range may miss | **PROPOSED** assumption |
| Beyond 400 ms or heavy loss | — | Degraded; no compensation beyond caps | **PROPOSED** |

These are assumptions for design, not measurements. Replace them with telemetry from beta ([[M21 - Beta Testing]]).

## 2. What the client predicts (player-only presentation)

| Predicted locally, immediately on input | Why safe |
|---|---|
| Player swing and special animations | Purely visual; no state changes |
| Swing whoosh sound, trail VFX, camera nudge | Visual and audio feedback for the local player only ([[Combat Feedback and Readability]]) |
| Dodge roll movement | The character is client-owned anyway; server validates distance and cooldown |
| Cooldown ring on the pressed button | Corrected by server `CooldownSync` if rejected |
| Button press, haptics, UI states | UI only |
| Local footsteps, own companion follow smoothing | Visual |

| Never predicted; shown only after server confirmation | Why |
|---|---|
| Damage numbers and enemy HP bar changes | Must match the server; a predicted number that the server rejects teaches players to distrust the UI |
| Enemy hit reactions and knockback | Affect what other players see |
| Kills, rewards, Cash | Economy |
| Egg roll, hatch, merge, ascension results | Randomness and economy; client shows "rolling" animation lead-in, then reveals the server result |
| Raid claims | Show "claiming…" until the server responds |

## 3. Reconciliation

| Situation | Server says | Client action |
|---|---|---|
| Intent accepted, hit landed | `CombatEvent` | Show number and reaction on the target |
| Intent accepted, hit missed (out of range, dodged) | Nothing (or `CombatEvent` with miss flag if design wants "Miss" text) | Swing already played; nothing to undo |
| Intent rejected (cooldown not ready) | `CooldownSync { kind, readyAtServerTime }` | Reset the cooldown ring to the server value |
| Special locked (level) | `CooldownSync` with locked flag | Grey out the button |
| Odds changed | `OddsChanged` | Re-display odds ([[Implementation - Dynamic Luck Calculation]]) |
| Character position rejected by movement validator | Server corrects position (teleports back) | Character snaps; logged |

Because the client predicts only its own visuals, reconciliation never needs to rewind world state on the client.

## 4. Hit validation tolerances

The server evaluates a player's hit against where the target was when the player most likely saw it (lag compensation), with strict caps.

| Tolerance | Value | Applies to | Reasoning |
|---|---|---|---|
| Range tolerance | +3 studs plus target radius | Player basic, Power Strike, Ground Slam, companion manual abilities | Absorbs snapshot interpolation (100 ms) and movement jitter |
| Lag compensation rewind | min(ping, 0.25 s) | Target position for player hits | Caps the "hit from behind a wall" effect; a client faking high ping gains at most 0.25 s |
| Position history | Server stores each entity's position at 20 Hz for 1 s | All hittable entities | Enough for 0.25 s rewind with interpolation |
| Timing tolerance | 0.05 s early | Combo cadence and cooldowns | Server frame and network jitter |
| Dodge i-frame back-date | ≤ 0.1 s (half ping, capped) | Dodge against boss and wild attacks | Favours the dodger slightly without allowing late dodges to cancel landed hits |
| Line of sight | Raycast from the attacker's server position to the rewound target position | Power Strike, ranged specials | Prevents hits through walls |
| Boss telegraph lead | ≥ 0.8 s between telegraph and impact | Every dodgeable boss attack | Exceeds the 400 ms poor-connection RTT with margin |

> [!info] PROPOSED — whom to favour
> **Player → AI hits:** favour the attacker within caps (lag compensation), because the victim is AI and cannot feel cheated. **AI → player hits:** favour the defender slightly (i-frame back-date) so dodges that looked successful on screen usually count. **Player → player hits (PvP):** reduce rewind to 0.15 s and range tolerance to +2 studs, because both sides are human (values **PROPOSED**; PvP activation **UNDECIDED**, [[Open Questions#Q-011]]).

### Lag-compensated range check

```lua
--!strict
-- Illustrative — not executed
-- Position history ring buffer per entity; 20 Hz × 1 s = 20 samples.

export type History = { times: { number }, positions: { Vector3 }, head: number }

local SIZE = 20

local function record(h: History, t: number, p: Vector3)
	h.head = (h.head % SIZE) + 1
	h.times[h.head] = t
	h.positions[h.head] = p
end

local function sampleAt(h: History, t: number): Vector3?
	-- Find the two samples bracketing t and interpolate.
	local bestBefore, bestAfter = nil :: number?, nil :: number?
	for i = 1, SIZE do
		local ti = h.times[i]
		if ti then
			if ti <= t and (bestBefore == nil or ti > h.times[bestBefore]) then bestBefore = i end
			if ti >= t and (bestAfter == nil or ti < h.times[bestAfter]) then bestAfter = i end
		end
	end
	if bestBefore and bestAfter then
		local t0, t1 = h.times[bestBefore], h.times[bestAfter]
		local a = if t1 > t0 then (t - t0) / (t1 - t0) else 0
		return h.positions[bestBefore]:Lerp(h.positions[bestAfter], a)
	end
	return nil
end
```

## 5. Remote entities on screen

| Entity | Client technique | Delay | Status |
|---|---|---|---|
| Animals (Approach B) | Interpolation between snapshots ([[Replication Strategy]]) | 100 ms behind newest snapshot | **PROPOSED** |
| Other players' characters | Roblox default replication | Engine-defined (*unverified*) | — |
| Bosses | Interpolation or engine replication (per boss choice) | 100 ms | **PROPOSED** |
| Extrapolation | At most 0.2 s when snapshots stop, then hold | — | **PROPOSED** |

Consequence: a player sees animals about 100 ms plus half the RTT in the past. The lag-compensation rewind (capped at 0.25 s) covers this for typical connections.

## 6. Economy and UI actions

Economy actions are not latency-sensitive in the same way. The client:

1. Disables the confirm button on press (prevents double submission; idempotency key also protects).
2. Starts a neutral lead-in (egg wobble) that is identical for every outcome.
3. Reveals the result when the server responds. If the response takes longer than the lead-in, the wobble loops.
4. On timeout (10 s, **PROPOSED**), retries once with the **same** idempotency key, then shows an error.

This keeps the canonical instant-result model (canonical §7) while hiding latency ([[UI - Egg Hatching]]).

## 7. Measuring latency

- Server: `Player:GetNetworkPing()` (signature verified; unit assumed seconds, *unverified*), sampled every 2 s and smoothed (exponential moving average, α = 0.3, **PROPOSED**).
- A client claiming high ping cannot change the server's measurement. Rewind uses only the server-measured value.
- Telemetry: median and 95th percentile ping per platform reported to [[Service - AnalyticsAndLoggingService]].

## 8. Test hooks

[[Test Cases - Multiplayer]] and [[Test Cases - Combat]]: Studio network simulation at 0, 150, 300 and 500 ms; hit at range + 2.9 (accept) and + 3.5 (reject); rewind clamped at 0.25 s with simulated 600 ms; dodge 0.05 s and 0.15 s late against a boss slam; cooldown press 0.03 s early (accept) and 0.2 s early (reject + sync).

## Related documents
- [[Implementation - Combat Damage Pipeline]]
- [[Replication Strategy]]
- [[Multiplayer Architecture]]
- [[Multiplayer Combat Rules]]
- [[Combat Feedback and Readability]]
- [[Boss AI]]
- [[Exploit Prevention]]
