---
title: Service - AnalyticsAndLoggingService
type: technical-service
category: technical-architecture
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - logging
  - analytics
  - observability
---

# Service - AnalyticsAndLoggingService

> [!info] PROPOSED
> Layer **0**: every other service may depend on it; it depends on nothing but Roblox. Design is **PROPOSED**; code is illustrative Luau, not tested. The log format, error categories, error codes and analytics event list are defined in [[Logging and Error Handling]]; this page is the service that implements them.

## Responsibility

- Provide scoped, structured loggers (`Log:Scope("Hatch")`) with levels Debug, Info, Warn, Error and Security.
- Keep an in-memory ring buffer (last 500 entries per server) for error context.
- Aggregate repeated errors by key and count them per minute.
- Maintain a per-player **suspicion score** from `Security` events, used for review and by [[Exploit Prevention]] (never for automatic bans by itself).
- Emit **analytics events** through Roblox `AnalyticsService`, using only the fixed event list.
- Receive client telemetry (`Telemetry/ClientError`, `Telemetry/ClientMetrics`, `Telemetry/UIFunnel`), validate it and fold it into logs and analytics.

## Inputs

| Input | Source |
|---|---|
| Log calls | Every service and system |
| `Event(name, player, fields)` analytics calls | Owning services after commits |
| `Telemetry/*` remotes | Clients |

## Outputs

| Output | Consumer |
|---|---|
| Developer Console output (Warn and above in live servers) | Engineers |
| `AnalyticsService` calls | Creator Hub analytics |
| `SuspicionChanged(player, score)` signal | [[Exploit Prevention]] tooling, admin panel |
| Ring buffer snapshots | Admin debug panel, error reports |

## Dependencies

None (layer 0). Roblox: `AnalyticsService`, `RunService` (for `IsStudio`).

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `SuspicionChanged` | `(player, score: number, reason: string)` |
| Signal | `ErrorBurst` | `(key: string, countPerMinute: number)` |
| Remotes C→S | `Telemetry/ClientError`, `Telemetry/ClientMetrics` (unreliable), `Telemetry/UIFunnel` | [[Remote Communication Contract#2.7 Progression, index, shop, telemetry]] |

## Data structures

```lua
--!strict
export type Logger = {
	Debug: (self: Logger, event: string, player: Player?, data: { [string]: any }?) -> (),
	Info: (self: Logger, event: string, player: Player?, data: { [string]: any }?) -> (),
	Warn: (self: Logger, event: string, player: Player?, data: { [string]: any }?) -> (),
	Error: (self: Logger, event: string, player: Player?, data: { [string]: any }?) -> (),
	Security: (self: Logger, event: string, player: Player?, data: { [string]: any }?) -> (),
	Event: (self: Logger, analyticsKey: string, player: Player, fields: { [string]: any }?) -> (),
}

export type SuspicionRecord = {
	score: number,                     -- decays by 1 point per minute (PROPOSED)
	recent: { { event: string, at: number } }, -- last 20
}
```

**PROPOSED values introduced here:** ring buffer 500 entries; suspicion weights `invalid_payload` 1, `quote_unknown` 3, `range_violation` 5, `rate_abuse` 2, `movement_flag` 5; review threshold 50; decay 1 point per minute; Info sampling 1% for combat events.

## Public API

```lua
--!strict
function AnalyticsAndLoggingService:Scope(name: string): Logger
function AnalyticsAndLoggingService:GetRecent(count: number): { LogEntry }
function AnalyticsAndLoggingService:GetSuspicion(player: Player): number
function AnalyticsAndLoggingService:SetSampling(scope: string, level: string, rate: number): ()
```

## Analytics adapter

```lua
--!strict
-- Illustrative Luau, not tested. AnalyticsService method names were checked against the
-- engine reference while writing; parameter details and limits are *unverified*.
local AnalyticsService = game:GetService("AnalyticsService")

local ECONOMY_KEYS = { cash_source = true, cash_sink = true }

local function emit(key: string, player: Player, f: { [string]: any })
	if not EventCatalogue[key] then
		Log:Warn("analytics_unknown_event", player, { key = key })
		return
	end
	local ok, err = pcall(function()
		if ECONOMY_KEYS[key] then
			AnalyticsService:LogEconomyEvent(
				player,
				if key == "cash_source" then Enum.AnalyticsEconomyFlowType.Source else Enum.AnalyticsEconomyFlowType.Sink,
				"Cash", f.amount, f.endingBalance, f.transactionType, f.itemSku
			)
		elseif EventCatalogue[key].kind == "ProgressionComplete" then
			AnalyticsService:LogProgressionCompleteEvent(player, EventCatalogue[key].path, f.level)
		elseif EventCatalogue[key].kind == "Onboarding" then
			AnalyticsService:LogOnboardingFunnelStepEvent(player, f.step, f.stepName)
		else
			AnalyticsService:LogCustomEvent(player, key, f.value or 1)
		end
	end)
	if not ok then
		Log:Warn("analytics_failed", player, { key = key, err = tostring(err) })
	end
end
```

Analytics failures never affect gameplay: every call is wrapped in `pcall` and is fire-and-forget. Analytics is called only after a successful commit.

## Error handling

| Case | Behaviour |
|---|---|
| `AnalyticsService` call errors | Logged at `Warn`, sampled; gameplay unaffected |
| Unknown event key | Dropped, `Warn` once per key per server |
| Client telemetry malformed or oversized | Dropped silently; counts towards `invalid_payload` suspicion only if repeated |
| Logger itself errors | Falls back to `warn()`; never throws into the caller |

## Security requirements

- **No personal data**: only `UserId` identifies a player. No display names, usernames, chat text or free text from other players is logged. Client error text is truncated (200 characters for messages, 500 for stacks) and stays server-side.
- Client telemetry is untrusted. It is used for diagnostics and analytics only and can never change game state.
- Suspicion scores are advisory. Any enforcement action follows the process in [[Exploit Prevention]] and [[Security Architecture]].
- Analytics custom event names are a fixed catalogue in config; services cannot create names dynamically (prevents unbounded cardinality and accidental data leaks).

## Testing requirements

| Test | Type |
|---|---|
| Logger never throws, even with cyclic or non-serialisable data | Unit |
| Ring buffer keeps exactly the last 500 entries | Unit |
| Unknown analytics key is dropped and warned once | Unit |
| `AnalyticsService` stub that errors does not break a hatch transaction | Integration |
| Telemetry spam beyond the rate limit is dropped | Exploit test |
| Logs contain no display names (grep test over a recorded session) | Integration |

## Related documents
- [[Technical Architecture Index]]
- [[Logging and Error Handling]]
- [[Exploit Prevention]]
- [[Security Architecture]]
- [[Statistical Testing of Probabilities]]
- [[Roblox API Reference Notes]]
- [[Bug Reporting and Severity]]
