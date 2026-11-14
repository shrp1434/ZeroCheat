---
title: Implementation - Rate Limiting
type: implementation
category: security
status: mixed
priority: P0
owner: Security Engineer
last_updated: 2026-11-14
tags:
  - luau
  - security
  - networking
  - rate-limiting
---

# Implementation - Rate Limiting

Per-player token buckets protect every remote from spam, bound the server cost of hostile traffic, and feed a violation score used for anti-cheat responses. The limiter is the first stage of the gateway in [[Implementation - Remote Validation Layer]].

> [!info] PROPOSED
> Bucket parameters, violation weights, thresholds and actions are **PROPOSED** local values (listed for [[Canonical Proposed Values]]). Automated enforcement policy is **UNDECIDED** (Q-905). Code is **illustrative — not executed**.

## 1. Token bucket

Each bucket has a **capacity** C (burst size) and a **refill rate** R (tokens per second). A request costs one token. The bucket refills continuously:

`tokens = min(C, tokens + R × (now − lastRefill))`

A request is allowed if `tokens ≥ 1`, then `tokens −= 1`. Over a long window the sustained rate cannot exceed R; short bursts up to C are allowed, which matches human input (a quick double-tap, a combo string).

Each request is checked against **two** buckets: its category bucket and a global per-player bucket. Both must have a token.

## 2. Bucket parameters (PROPOSED)

| Bucket | Remotes | Capacity C | Refill R (/s) | Reasoning |
|---|---|---:|---:|---|
| `Quote` | `RequestOddsQuote` | 5 | 1.0 | UI requests a quote on opening the roll or hatch screen and on `STALE_ODDS` |
| `Economy` | `RequestRollEggs`, `RequestHatchEggs`, `RequestAscend`, `RequestMergeEggs` | 3 | 0.5 | Each action has a multi-second animation; 1 per 2 s sustained is generous |
| `Combat` | `CombatIntent` | 12 | 8 | Basic combo is 0.45 s per hit (≈2.2/s); specials and dodge add a few; 8/s leaves headroom for jitter bursts |
| `Ability` | `AbilityIntent` | 6 | 4 | Global ability cooldown 0.5 s (2/s) plus buffering |
| `Command` | `TargetCommand` | 8 | 4 | Players re-target often in boss fights |
| `Raid` | `RaidAction` | 10 | 5 | Claim attempts at the vault |
| `Team` | Team-change requests at base | 4 | 1 | |
| `UI` | Cosmetic and settings remotes | 10 | 2 | |
| `Global` | All remotes for a player | 60 | 30 | Absolute ceiling per player |

Tuning rule: a legitimate player on a high-latency mobile connection receiving buffered packets in a burst must never hit a limit in normal play. Telemetry on `RATE_LIMITED` per bucket is reviewed in [[M19 - Multiplayer Testing]].

## 3. Code

```lua
--!strict
-- Illustrative — not executed
-- ServerScriptService/Net/RateLimiter

local Players = game:GetService("Players")
local ServerStorage = game:GetService("ServerStorage")

local Config = require(ServerStorage.Config.RateLimitConfig)
--  RateLimitConfig (PROPOSED):
-- 	BUCKETS = {
-- 		Quote   = { capacity = 5,  refill = 1.0 },
-- 		Economy = { capacity = 3,  refill = 0.5 },
-- 		Combat  = { capacity = 12, refill = 8 },
-- 		Ability = { capacity = 6,  refill = 4 },
-- 		Command = { capacity = 8,  refill = 4 },
-- 		Raid    = { capacity = 10, refill = 5 },
-- 		Team    = { capacity = 4,  refill = 1 },
-- 		UI      = { capacity = 10, refill = 2 },
-- 	},
-- 	GLOBAL = { capacity = 60, refill = 30 },
-- 	VIOLATION_DECAY_PER_SECOND = 0.1,
-- 	THRESHOLD_LOG = 50,
-- 	THRESHOLD_KICK = 150,
-- 	DROPPED_REQUEST_WEIGHT = 1,

type Bucket = { tokens: number, last: number, capacity: number, refill: number }
type PlayerState = {
	buckets: { [string]: Bucket },
	global: Bucket,
	violation: number,
	violationAt: number,
	logged: boolean,
}

local state: { [Player]: PlayerState } = {}

local RateLimiter = {}

local function newBucket(spec: { capacity: number, refill: number }, now: number): Bucket
	return { tokens = spec.capacity, last = now, capacity = spec.capacity, refill = spec.refill }
end

-- Pure step function: exported for unit tests.
function RateLimiter.step(b: Bucket, now: number): boolean
	local elapsed = math.max(0, now - b.last) -- monotonic clock, but guard anyway
	b.tokens = math.min(b.capacity, b.tokens + elapsed * b.refill)
	b.last = now
	if b.tokens >= 1 then
		b.tokens -= 1
		return true
	end
	return false
end

local function get(player: Player): PlayerState
	local s = state[player]
	if s == nil then
		local now = os.clock()
		s = {
			buckets = {},
			global = newBucket(Config.GLOBAL, now),
			violation = 0,
			violationAt = now,
			logged = false,
		}
		state[player] = s
	end
	return s
end

function RateLimiter.consume(player: Player, bucketName: string): boolean
	local s = get(player)
	local now = os.clock()
	local spec = Config.BUCKETS[bucketName]
	assert(spec, "Unknown bucket " .. bucketName)
	local b = s.buckets[bucketName]
	if b == nil then
		b = newBucket(spec, now)
		s.buckets[bucketName] = b
	end
	-- Check global first without consuming twice on failure.
	local globalOk = RateLimiter.step(s.global, now)
	if not globalOk then
		RateLimiter.addViolation(player, "global_rate", Config.DROPPED_REQUEST_WEIGHT)
		return false
	end
	if not RateLimiter.step(b, now) then
		s.global.tokens = math.min(s.global.capacity, s.global.tokens + 1) -- refund global token
		RateLimiter.addViolation(player, "rate:" .. bucketName, Config.DROPPED_REQUEST_WEIGHT)
		return false
	end
	return true
end

function RateLimiter.addViolation(player: Player, kind: string, weight: number)
	local s = get(player)
	local now = os.clock()
	s.violation = math.max(0, s.violation - (now - s.violationAt) * Config.VIOLATION_DECAY_PER_SECOND)
	s.violationAt = now
	s.violation += weight

	if s.violation >= Config.THRESHOLD_LOG and not s.logged then
		s.logged = true
		local Registry = require(script.Parent.Parent.Registry) :: any
		Registry.get("AnalyticsAndLoggingService").security(player, "VIOLATION_THRESHOLD", kind, s.violation)
	end
	if s.violation >= Config.THRESHOLD_KICK then
		-- Enforcement policy UNDECIDED (Q-905). Kick is the strongest automated action proposed;
		-- bans are never automated.
		player:Kick("Connection closed due to unusual activity.")
	end
end

function RateLimiter.snapshot(player: Player): { violation: number }?
	local s = state[player]
	return if s then { violation = s.violation } else nil
end

Players.PlayerRemoving:Connect(function(p)
	state[p] = nil
end)

return RateLimiter
```

## Violation scoring

| Event | Weight | Status |
|---|---:|---|
| Request dropped by any bucket | 1 | **PROPOSED** |
| Schema failure (`INVALID_PAYLOAD`) | 5 | **PROPOSED** |
| Extra arguments on a remote (forged call) | 5 | **PROPOSED** |
| Cooldown or combo cadence violation | 2 | **PROPOSED** |
| Using a locked special | 5 | **PROPOSED** |
| Raid rule probe (backpack egg claim, non-defender claim) | 10 | **PROPOSED** |
| Raid claim on an undefeated defender | 5 | **PROPOSED** |
| Movement anomaly (from the movement validator, [[Exploit Prevention]]) | 3–10 | **PROPOSED** |
| Decay | −0.1 per second (−6 per minute) | **PROPOSED** |

| Threshold | Action | Status |
|---|---|---|
| ≥ 50 | Log once per session to [[Service - AnalyticsAndLoggingService]] with recent events; flag for review | **PROPOSED** |
| ≥ 150 | `Player:Kick` with a neutral message | **PROPOSED**; policy **UNDECIDED** (Q-905) |
| Any | Never an automated ban; bans are a human moderation decision | **PROPOSED** |

> [!warning] UNDECIDED (Q-905)
> Whether automated kicks are enabled at launch, or whether launch runs in log-only mode while thresholds are calibrated, is not decided. The recommendation is log-only during beta ([[M21 - Beta Testing]]), then kicks at launch with thresholds set from beta telemetry.

## 4. Worked example

A player with a fresh `Combat` bucket (12 tokens, 8/s) mashes attack at 20 inputs per second for 2 seconds:

- t = 0: 12 tokens. First 12 inputs (0.6 s) pass the limiter.
- During those 0.6 s the bucket refilled 4.8 tokens; inputs continue to pass at 8/s.
- Over 2 s: about 12 + 8 × 2 = 28 pass the limiter, 12 are dropped (violation +12, decaying).
- Of the 28 that pass, only those at least 0.40 s apart (0.45 s minus tolerance) produce basic hits ([[Implementation - Combat Damage Pipeline]]). About 5 hits land. Cadence violations add +2 each, but only when the client sends a hit intent faster than the combo window, which a correct client never does: the client should not send intents faster than its own combo timer.

The legitimate client therefore never accumulates violations; a macro does, and still gains nothing.

## 5. Server-originated rate limits

The server also limits itself:

| Resource | Limit | Owner |
|---|---|---|
| DataStore writes per player | ≤ 1 per 6 s, coalesced | [[Service - DataService]] |
| MemoryStore lock calls | Only at raid start and end | [[Implementation - Raid Session Controller]] |
| PathfindingService computations | ≤ 10 per second per server | [[Implementation - Animal AI State Machine]] |
| Unreliable state broadcasts | Fixed tick rates by LOD | [[Replication Strategy]] |

## 6. Test hooks

[[Test Cases - Exploit Prevention]]: bucket step function with synthetic clocks; burst then sustained rates; global refund; violation decay; threshold crossings call logging once; kick path behind a test flag; no state retained after `PlayerRemoving`.

## Related documents
- [[Implementation - Remote Validation Layer]]
- [[Exploit Prevention]]
- [[Security Architecture]]
- [[Threat Model]]
- [[Remote Communication Contract]]
- [[Service - AnalyticsAndLoggingService]]
- [[Test Cases - Exploit Prevention]]
