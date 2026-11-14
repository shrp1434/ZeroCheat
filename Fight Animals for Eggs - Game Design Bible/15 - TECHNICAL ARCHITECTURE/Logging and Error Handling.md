---
title: Logging and Error Handling
type: spec
category: technical-architecture
status: proposed
priority: P0
owner: Roblox Technical Architect
last_updated: 2026-11-14
tags:
  - technical-architecture
  - logging
  - error-handling
  - analytics
  - observability
---

# Logging and Error Handling

> [!info] PROPOSED
> Log format, categories, error codes and analytics events are **PROPOSED**. The implementation lives in [[Service - AnalyticsAndLoggingService]]. Code is illustrative Luau, not tested.

## Structured logs

Every log line is a table, not a formatted string. The logger serialises it once, at the sink.

```lua
--!strict
export type LogLevel = "Debug" | "Info" | "Warn" | "Error" | "Security"

export type LogEntry = {
	t: number,            -- workspace:GetServerTimeNow()
	level: LogLevel,
	scope: string,        -- service or system name, e.g. "Hatch"
	event: string,        -- snake_case event key, e.g. "hatch_committed"
	userId: number?,      -- Roblox user ID only; never display names or chat text
	jobId: string,        -- game.JobId, identifies the server
	build: string,        -- build version from Config, see Versioning and Changelog Policy
	data: { [string]: string | number | boolean }?,
	trace: string?,       -- only for Error level
}
```

| Rule | Detail |
|---|---|
| Keys, not prose | `event = "roll_rejected", data = { code = "E_STALE_ODDS" }`, never `"Roll was rejected because..."` |
| No personal data | User ID is the only player identifier. No display names, usernames, chat text, device identifiers or free-text input from players (client error text is truncated and kept server-side) |
| Flat data | `data` values are scalars; arrays are summarised (`count = 5`) |
| Bounded volume | Debug is off in live servers; Info is sampled for high-frequency events (combat at 1%) |
| One logger | Services call `Log:Scope("Name")`; no raw `print` or `warn` in committed code except in the boot path before the logger exists |

### Sinks

| Sink | Levels | Purpose |
|---|---|---|
| Output (`print` / `warn`) | Debug in Studio; Warn and above in live servers | Developer Console server log |
| In-memory ring buffer (last 500 entries per server, **PROPOSED**) | All | Attached to error reports; viewable by an admin debug panel |
| AnalyticsService | Analytics events only (see below) | Creator Hub analytics dashboards |
| Error aggregation key | Error and Security | Groups identical errors by `scope + event + first trace line` and counts per server per minute |

> [!warning] External log shipping
> Shipping logs to an external service over `HttpService` is possible but is **not** planned. If proposed later, it needs a privacy review and must never send personal data. Raise it as a new open question before building.

## Error categories

| Category | Examples | Handling | Player sees |
|---|---|---|---|
| **Validation** | Malformed payload, unknown ID, wrong count | Reject; `Info` log (sampled); no retry | Generic or specific error code |
| **Rule** | Not enough cash, not at base, storage full, team locked | Reject; `Info` log | Specific error code with guidance |
| **Staleness** | Stale odds, expired quote, `expectedLevel` mismatch | Reject; client refreshes and asks again | Refreshed screen; short notice |
| **Security** | Forged quote, rate abuse, impossible range, movement flags | Reject silently; `Security` log; suspicion score ([[Exploit Prevention]]) | Same message as Validation (no hint to exploiters) |
| **Platform** | DataStore throttling or outage, MarketplaceService error, PolicyService failure | Retry with backoff where safe; degrade feature; `Warn` then `Error` | "Saving delayed" banner or feature temporarily unavailable |
| **Internal** | A Luau error inside a handler | `xpcall` catches; transaction discarded; `Error` log with trace | `E_INTERNAL` with "please try again" |
| **Configuration** | A required value is `nil` (for example raid duration, Q-012) | Feature disabled at boot; `Warn` log `CONFIG_INCOMPLETE` | Feature hidden or "coming soon" |

### Retry policy for platform calls (PROPOSED)

| Call | Retries | Backoff | On final failure |
|---|---:|---|---|
| Profile load (`UpdateAsync`) | 5 | 1, 2, 4, 8, 16 s | Kick with a "data unavailable, please rejoin" message; **never** play on a default profile that would overwrite saved data |
| Autosave | 3 per cycle | 2, 4, 8 s | Keep dirty; retry next cycle; banner after 2 failed cycles |
| Final save on leave | 5 | 1 to 16 s, bounded by `BindToClose` time | `Error` log `save_lost_risk` |
| `PolicyService:GetPolicyInfoForPlayerAsync` | 3 | 1, 2, 4 s | Treat as most restrictive policy |
| `MarketplaceService.ProcessReceipt` grant | Handled by the platform calling again | — | Return `NotProcessedYet` |

Detail of save and recovery: [[Save, Load and Recovery]].

## Player-facing error codes

Error codes are stable strings shared in `ReplicatedStorage/Shared/ErrorCodes`. The client maps each to a localisation key. Messages below are proposed English copy ([[UI - Notifications]]).

| Code | Category | Raised by | Player message (PROPOSED) |
|---|---|---|---|
| `E_RATE_LIMITED` | Validation | Net | "Slow down a little." |
| `E_INVALID_PAYLOAD` | Validation / Security | Net | "Something went wrong. Please try again." |
| `E_NOT_READY` | Platform | All | "Your data is still loading." |
| `E_DATA_UNAVAILABLE` | Platform | DataService | "We could not load your data. Please rejoin." |
| `E_INTERNAL` | Internal | All | "Something went wrong. Please try again." |
| `E_FEATURE_DISABLED` | Configuration | All | "This feature is not available yet." |
| `E_INSUFFICIENT_CASH` | Rule | Economy, Egg, Merge, Ascension, Base | "You need more Cash." |
| `E_QUOTE_UNKNOWN` | Validation / Security | Egg, Hatch | "Something went wrong. Please try again." |
| `E_QUOTE_EXPIRED` | Staleness | Egg, Hatch | "Odds refreshed. Please check and confirm again." |
| `E_STALE_ODDS` | Staleness | Egg, Hatch | "Your odds have changed. Please check the new odds and confirm again." |
| `E_STALE_STATE` | Staleness | Ascension, Base, Merge | "This has already changed. Refreshing." |
| `E_STORAGE_FULL` | Rule | Egg, Merge | "Your egg storage is full." |
| `E_BACKPACK_FULL` | Rule | Egg | "Your backpack is full." |
| `E_ANIMAL_STORAGE_FULL` | Rule | Hatch | "You have no room for more animals." |
| `E_HATCH_LIMIT` | Validation | Hatch | "You can hatch up to 5 eggs at once." |
| `E_IN_COMBAT` | Rule | Hatch, Team, PvP | "You cannot do that during combat." |
| `E_NOT_AT_BASE` | Rule | Team, Egg, Merge, Base, Hatch | "Return to your base to do this." |
| `E_TEAM_LOCKED` | Rule | Team | "Your team is locked until you return to your base." |
| `E_TEAM_INVALID` | Validation | Team | "That team is not valid." |
| `E_NOT_OWNED` | Validation / Security | All | "You do not own that." |
| `E_ASSET_LOCKED` | Rule | Ascension, Merge, Egg, Team | "That item is busy right now." |
| `E_MAX_ASCENSION` | Rule | Ascension | "This animal is fully ascended." |
| `E_DUPLICATES_INVALID` | Validation | Ascension | "Those animals cannot be used for this ascension." |
| `E_STATION_REQUIRED` | Rule | Merge | "Buy an Egg Merging Station first." |
| `E_STATION_LEVEL` | Rule | Merge | "Upgrade your Egg Merging Station to merge these eggs." |
| `E_MERGE_INVALID` | Validation | Merge | "You need 3 eggs of the same rarity." |
| `E_MERGE_MAX_RARITY` | Rule | Merge | "Secret eggs cannot be merged." |
| `E_UPGRADE_GATE` | Rule | Base, Merge | "You have not met the requirement for this upgrade yet." |
| `E_MAX_LEVEL` | Rule | Base | "This is already at its highest level." |
| `E_LEVEL_LOCKED` | Rule | Combat, Progression | "Reach a higher level to unlock this." |
| `E_COOLDOWN` | Rule | Combat | (no message; cooldown UI only) |
| `E_OUT_OF_RANGE` | Rule | Combat, Raid | (no message; indicator only) |
| `E_PVP_DISABLED` | Rule | PvP | "PvP is not active." |
| `E_RAID_DISABLED` | Configuration | Raid | "Raids are not available yet." |
| `E_RAID_TARGET_OFFLINE` | Rule | Raid | "That base cannot be raided right now." |
| `E_RAID_SHIELDED` | Rule | Raid | "That base is protected by a shield." |
| `E_RAID_NOT_ELIGIBLE` | Rule | Raid | "You cannot raid that base." |
| `E_RAID_NOT_KNOCKED_OUT` | Rule | Raid | "Defeat this defender before taking it." |
| `E_RAID_ANIMAL_LIMIT` | Rule | Raid | "You have taken the maximum of 3 animals." |
| `E_RAID_EGG_LIMIT` | Rule | Raid | "You cannot carry any more eggs from this raid." |
| `E_RAID_NOT_STEALABLE` | Rule | Raid | "That cannot be stolen." |
| `E_PURCHASE_FAILED` | Platform | Economy | "The purchase could not be completed. You have not been charged." (only shown when the platform reports failure) |

Security-category rejections deliberately reuse the generic message so that an exploiter cannot tell which check caught them.

## Analytics events

> [!info] AnalyticsService method names
> Roblox's `AnalyticsService` documents `LogEconomyEvent`, `LogProgressionEvent` (with `LogProgressionStartEvent`, `LogProgressionCompleteEvent`, `LogProgressionFailEvent`), `LogFunnelStepEvent`, `LogOnboardingFunnelStepEvent` and `LogCustomEvent`. These names were checked against the Creator Hub engine reference during writing; exact parameter order, the `customFields` keys accepted and per-experience limits on custom event names are *unverified* and must be checked by [[Service - AnalyticsAndLoggingService]] before implementation. See [[Roblox API Reference Notes]].

| Event key | Method family | When | Fields |
|---|---|---|---|
| `cash_source` | Economy (source) | Every Cash credit | amount, ending balance, source (`WildDefeat`, `BossDefeat`, `Refund`, ...), region |
| `cash_sink` | Economy (sink) | Every Cash debit | amount, ending balance, sink (`EggRoll`, `MergeFee`, `AscensionFee`, `ModuleUpgrade`, `PlotExpansion`, `StationPurchase`) |
| `egg_rolled` | Custom | Each roll commit | count, rarities (counts), PS bucket (deciles), oddsVersion |
| `egg_hatched` | Custom | Each hatch commit | count, rarity per egg, species per egg, duplicate flag |
| `egg_merged` | Custom | Each merge | input rarity, station level |
| `animal_ascended` | Custom | Each ascension | rarity, new level, duplicates consumed |
| `team_changed` | Custom | Each team set | species count by role |
| `level_reached` | Progression (complete) | Level up | level |
| `region_unlocked` | Progression (complete) | Region unlock | region index |
| `boss_defeated` | Progression (complete) | Boss defeat with eligibility | boss ID, participants, duration |
| `player_defeated` | Progression (fail) | Player KO | battle type, region |
| `onboarding_step` | Onboarding funnel | Steps in [[New Player Onboarding]] | step, step name |
| `raid_started` / `raid_resolved` | Custom | Raid lifecycle | outcome, eggs stolen, animals stolen, duration |
| `pvp_toggled` | Custom | PvP participation change | new state |
| `purchase_granted` | Custom (Robux revenue is reported by the platform) | ProcessReceipt grant | product key |
| `perf_sample` | Custom (sampled 5% of players) | Every 60 s from `Telemetry/ClientMetrics` | fps bucket, memory bucket, quality tier, platform class |

Rules:
- Analytics events are emitted **after** a successful commit, never before.
- Probability analytics (`egg_rolled`, `egg_hatched`) feed [[Statistical Testing of Probabilities]] and live checks in [[Probability Balancing]]. They must record the `oddsVersion` so observed rates can be compared with the odds that were shown.
- Custom event names are a fixed list in `Config`; services cannot invent names at runtime.

## Alerts (PROPOSED)

| Alert | Condition | Action |
|---|---|---|
| Save failures | > 1% of saves failing over 5 min across servers | Investigate DataStore status; consider pausing high-value features |
| Internal errors | Any `scope + event` key above 20 per server per hour | Bug ticket at severity per [[Bug Reporting and Severity]] |
| Security spike | `security.*` events above 3× the 7-day baseline | Review recent build for a new exploit path |
| Odds drift | Observed rarity rate outside the 99.9% confidence interval for its oddsVersion over ≥ 100,000 rolls | P0 investigation (could be an RNG or weighting bug) |

## Related documents
- [[Technical Architecture Index]]
- [[Service - AnalyticsAndLoggingService]]
- [[Remote Communication Contract]]
- [[Save, Load and Recovery]]
- [[Exploit Prevention]]
- [[Statistical Testing of Probabilities]]
- [[Bug Reporting and Severity]]
- [[Roblox API Reference Notes]]
