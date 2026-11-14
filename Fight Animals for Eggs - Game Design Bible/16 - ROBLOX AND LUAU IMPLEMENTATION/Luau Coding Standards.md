---
title: Luau Coding Standards
type: standard
category: engineering
status: proposed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - luau
  - engineering
  - coding-standards
  - security
---

# Luau Coding Standards

> [!info] PROPOSED
> These standards are a team recommendation for all Luau written for *Fight Animals for Eggs*. They become binding once adopted in [[Definition of Done]]. Every code sample in this folder follows them and is **illustrative — not executed** in Roblox Studio.

The standards exist for three reasons: the game handles randomised rewards that must be provably fair ([[Randomised Reward Compliance]]), it moves valuable items between players during raids ([[Base Raiding System]]), and it is played on mobile where frame time is scarce ([[Performance Guidelines]]). Most rules below trace back to one of these.

## 1. Type checking

| Rule | Detail |
|---|---|
| `--!strict` everywhere | Every ModuleScript, Script and LocalScript starts with `--!strict`. `--!nonstrict` needs a comment explaining why and an owner. `--!nocheck` is forbidden outside generated code. |
| Export types from the owning module | `export type EggRecord = { ... }` lives beside the code that creates eggs. Consumers `require` the module for the type. |
| No `any` at module boundaries | Public functions take and return concrete types. `any` is allowed only immediately after a remote boundary, before validation narrows it ([[Implementation - Remote Validation Layer]]). |
| Narrow with `typeof` | Use `typeof(x) == "Vector3"` rather than `type(x)` for Roblox datatypes. |
| Optional values are explicit | `number?` and an explicit `nil` check. Never rely on a falsy `0`. |
| Freeze configuration | Config tables are wrapped with `table.freeze` (shallow) at load. Nested tables are frozen by a recursive helper ([[Configuration Modules]]). |

## 2. Naming

| Element | Convention | Example |
|---|---|---|
| Services (server singletons) | `PascalCase` + `Service` | `HatchService` |
| Controllers (client singletons) | `PascalCase` + `Controller` | `EggRollController` |
| Modules returning a class | `PascalCase` | `TokenBucket` |
| Functions, locals | `camelCase` | `computeEggWeights` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_HATCH_BATCH` |
| Types | `PascalCase` | `RarityName`, `ReasonCode` |
| Remotes | `Verb` + `Noun` for requests, `Noun` + `Event` for broadcasts | `RequestHatchEggs`, `CombatEvent` |
| Attributes | `PascalCase` string | `AnimalUid`, `OwnerUserId` |
| CollectionService tags | `PascalCase` | `WildAnimal`, `RaidableVault` |

Rarity identifiers are the seven canonical names exactly as written: `Common`, `Uncommon`, `Rare`, `Epic`, `Legendary`, `Mythical`, `Secret` ([[Egg Rarity System]]). Do not abbreviate them in data.

## 3. Server authority rules (non-negotiable)

> [!danger] Security baseline
> Breaking any rule in this section is a release blocker. See [[Security Architecture]] and [[Exploit Prevention]].

1. **The client sends intent, never outcomes.** A client may say "I want to hatch these three eggs" or "I swung at target 4012". It never says "I hatched a Tiger" or "I dealt 84 damage".
2. **Every remote handler validates type, shape and bounds before reading a field** ([[Implementation - Remote Validation Layer]]) and passes a rate limiter ([[Implementation - Rate Limiting]]).
3. **The server never trusts client-supplied odds, prices, positions of other entities, timestamps or counts.** Client timestamps may be logged for diagnostics only.
4. **All randomness that affects rewards runs on the server** with a `Random` object owned by the service ([[Implementation - Weighted Random Selection]]). `math.random` is not used for gameplay.
5. **Never call `RemoteFunction:InvokeClient`.** A client can hang or error the server thread. Server-to-client traffic uses `RemoteEvent` or `UnreliableRemoteEvent`.
6. **Secret configuration lives in `ServerStorage` or `ServerScriptService`.** Anything in `ReplicatedStorage` is readable by exploiters. The luck slopes and pool weights may stay hidden (D-017); only computed odds are sent ([[Implementation - Dynamic Luck Calculation]]).

## 4. Transactions and yielding

| Rule | Why |
|---|---|
| No yield between validation and mutation | Luau runs one thread at a time on a server actor. A yield (`task.wait`, any `...Async` call, `WaitForChild`) lets another request run and invalidate what you validated. This is the root cause of most duplication bugs ([[Data Consistency and Transactions]]). |
| Mutations go through the transaction helper | `Txn.run` snapshots, mutates, checks invariants and rolls back on failure ([[Implementation - Egg Roll and Hatch Flow#Transaction helper]]). |
| Saving happens after the transaction | The in-memory change is atomic; the DataStore write is a separate, retried step owned by [[Service - DataService]]. |
| Idempotency keys on every economy request | Retries and double-taps must not double-charge ([[Implementation - Egg Roll and Hatch Flow#Idempotency]]). |

## 5. Concurrency and scheduling

- Use the `task` library (`task.spawn`, `task.defer`, `task.delay`, `task.wait`, `task.cancel`). The legacy global `wait`, `spawn` and `delay` are forbidden.
- Long-running loops run from **one** scheduler per system connected to `RunService.Heartbeat`, not one loop per entity ([[Implementation - Animal AI State Machine#LOD scheduler]]).
- Any `...Async` call is wrapped in `pcall` and has a retry policy with back-off. Never retry inside a `Heartbeat` callback.
- Parallel Luau (`task.desynchronize`) is **PROPOSED for evaluation only** in the AI system after profiling; it must not touch player data.

## 6. Errors and logging

- Expected failures return a `ReasonCode` ([[Implementation - Remote Validation Layer#Reason codes]]); they are not errors.
- Unexpected failures use `error()` inside the service and are caught at the remote boundary, logged through [[Service - AnalyticsAndLoggingService]], and returned to the client as `INTERNAL_ERROR`.
- Never log a full player profile. Log UserId, request kind, reason code and the relevant IDs ([[Logging and Error Handling]]).

## 7. Performance

- Cache service and instance lookups at module load (`local Players = game:GetService("Players")`).
- Avoid creating closures or tables per frame in hot loops; reuse buffers.
- Use `buffer` for high-volume replication payloads ([[Replication Strategy]]).
- Use `os.clock()` for durations on the server and `workspace:GetServerTimeNow()` for client–server shared timelines.
- Profile with the MicroProfiler before optimising. Budgets live in [[Animal Scalability and Performance Budgets]].

## 8. Module layout template

```lua
--!strict
-- Illustrative — not executed
-- <ModuleName>: one-line purpose. Owner: <role>.

local ReplicatedStorage = game:GetService("ReplicatedStorage")

local Types = require(ReplicatedStorage.Shared.Types)

export type Thing = {
	id: string,
	value: number,
}

local MAX_THINGS = 10 -- PROPOSED, see Canonical Proposed Values

local Module = {}

local function helper(x: number): number
	return x * 2
end

function Module.doThing(input: Thing): (boolean, Types.ReasonCode?)
	if input.value <= 0 then
		return false, "INVALID_PAYLOAD"
	end
	return true, nil
end

return Module
```

## 9. Testing

| Practice | Detail |
|---|---|
| Pure core, thin shell | Probability, damage and validation logic are pure functions that take inputs (including a uniform random number) and return outputs. Services wrap them. |
| Unit tests | Run under a Luau test framework (TestEZ or Jest Lua are the common community and Roblox open-source options; choice is **PROPOSED** for [[M02 - Core Project Setup]]). |
| Statistical tests | Weighted selection and luck are tested against [[Statistical Testing of Probabilities]]. |
| Test hooks | Services expose `_testing` tables only when `RunService:IsStudio()` is true. They must not exist in live builds. |

## 10. Tooling (PROPOSED)

| Tool | Purpose |
|---|---|
| Rojo | File-system project sync, so code is reviewed in Git |
| StyLua | Formatting (tabs, 120 columns) |
| Selene | Linting (deny `wait`, `spawn`, `delay` globals) |
| luau-lsp | Editor type checking with `--!strict` |

These are widely used community tools; adoption is a [[M02 - Core Project Setup]] task.

## 11. Code review checklist

- [ ] `--!strict` present; no `any` leaking from a public function
- [ ] Remote handler validates and rate-limits before any other work
- [ ] No yield between validation and mutation
- [ ] Mutation uses `Txn.run`; idempotency key recorded
- [ ] Reward randomness uses the service `Random`, not `math.random`
- [ ] No hard-coded numbers that belong in [[Canonical Proposed Values]]
- [ ] Status of each rule noted (**CONFIRMED**/**PROPOSED**/**UNDECIDED**) in comments where it encodes a design rule
- [ ] Test added or updated

## Related documents
- [[Luau Implementation Index]]
- [[Module Patterns and Bootstrapping]]
- [[Configuration Modules]]
- [[Implementation - Remote Validation Layer]]
- [[Security Architecture]]
- [[Service Architecture]]
- [[Performance Guidelines]]
- [[Definition of Done]]
