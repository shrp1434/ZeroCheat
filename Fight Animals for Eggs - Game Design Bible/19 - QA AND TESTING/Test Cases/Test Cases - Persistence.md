---
title: Test Cases - Persistence
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - persistence
  - datastore
  - data-integrity
---

# Test Cases - Persistence

Test cases for saving, loading, session locking, failure recovery, schema migration, cross-player transactions and purchase receipts. System documents: [[Save, Load and Recovery]], [[Data Architecture Overview]], [[Data Validation and Migration]], [[Data Consistency and Transactions]], [[Service - DataService]], and the schemas ([[Schema - Player Profile]], [[Schema - Egg Inventory]], [[Schema - Animal Collection]], [[Schema - Base Data]], [[Schema - Economy]]).

> [!danger] Data loss is a launch blocker
> Every P0 case here is in the release regression. A failure that loses or duplicates player items is severity S1 ([[Bug Reporting and Severity]]).

> [!info] PROPOSED
> Autosave interval, retry counts, back-off and session-lock timeout are configuration values owned by [[Save, Load and Recovery]]; tests refer to them symbolically (`T_autosave`, `N_retry`, `T_lock`). The Cash ceiling `MAX_CASH` = 10^15 is a **PROPOSED** QA value introduced here (below 2^53, the largest range in which Luau numbers represent every integer exactly) and must be confirmed in [[Canonical Proposed Values]].

**Fixtures.** The DataStore test double supports `QA_InjectDataStoreError(op, count)`, `QA_InjectLatency(op, ms)`, `QA_SetBudget(requestType, n)`, `QA_KillServer()`, `QA_KillServerBetweenWrites()`, `QA_LoadFixtureProfile(name)` (for old-schema and corrupt profiles). All tests run in the QA test experience, whose DataStores are separate from production.

## 1. Save and load

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-001 | New profile defaults | Never-played account | 1) Join. | Profile created with schema defaults: backpack 10, base 50, Cash per [[Schema - Economy]], empty collection or starter rules per [[New Player Onboarding]], current schema version. | P0 | functional | D-021 |
| TC-PER-002 | Full round trip | Profile with eggs of every rarity, 100 animals with mixed ascension, upgraded base, station L3, index progress | 1) Leave. 2) Rejoin on another server. | Every field identical, including instance IDs, ascension levels, variants, equipped team, storage expansions and ledger totals. | P0 | functional | D-019, D-021, D-022 |
| TC-PER-003 | Save on leave | Changes made in session | 1) Leave via `Players.PlayerRemoving`. 2) Read DataStore directly. | Latest state saved once with `UpdateAsync`. | P0 | functional | D-025 |
| TC-PER-004 | Autosave | Session active | 1) Make a change. 2) Wait `T_autosave`. 3) `QA_KillServer()`. 4) Rejoin. | Changes made before the last autosave are present. Loss window is at most `T_autosave`, except for transactions saved immediately (purchases, raid settlement). | P0 | functional | D-025 |
| TC-PER-005 | Writes use UpdateAsync | Code review and log inspection | 1) Inspect `DataService` writes. | Profile writes use `UpdateAsync` with a version or lock check, never a blind `SetAsync` over existing data. | P0 | security | D-025 |
| TC-PER-006 | Save on shutdown | 16 players | 1) Shut down the server. | All 16 saved via `game:BindToClose` (TC-MP-007). | P0 | edge | D-025 |
| TC-PER-007 | Maximum-size profile | Every container at its PROPOSED maximum (backpack 25, base 200, 100 animals at working capacity, all modules L5, full index) | 1) Save. 2) Measure the serialised size. | Well below the DataStore per-key value limit stated in [[Roblox API Reference Notes]] (*unverified* value; QA records the measured size per schema version). | P1 | performance | D-021 |

## 2. Failure handling

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-010 | DataStore failure mid-save | `QA_InjectDataStoreError("UpdateAsync", N_retry − 1)` | 1) Trigger a save. | Retries with back-off and succeeds; player sees nothing; in-memory state kept; log shows retries. | P0 | edge | D-025 |
| TC-PER-011 | Persistent save failure | Error injected for every attempt | 1) Trigger a save. 2) Player continues playing. 3) Player leaves. | In-memory state retained; saves retried on later autosaves and on leave; a "saving problem" notice per [[Save, Load and Recovery]] if configured; error logged with severity. No partial overwrite of the stored profile. | P0 | edge | D-025 |
| TC-PER-012 | Load failure must not create a blank profile | Load error injected for an existing player | 1) Player joins. | The server never treats the player as new and never saves defaults over the stored profile. The player is retried and, if still failing, removed with a "try again" message. | P0 | edge | D-025 |
| TC-PER-013 | Request budget exhaustion | `QA_SetBudget` near zero | 1) Trigger many saves. | Saves are queued and prioritised (leave and transaction saves first); no save is dropped silently. Budget read via `DataStoreService:GetRequestBudgetForRequestType`. | P1 | edge | D-025 |
| TC-PER-014 | Slow DataStore | `QA_InjectLatency` several seconds | 1) Join; roll; leave. | Join shows loading state; gameplay waits for load; leave save completes. | P1 | performance | D-025 |

## 3. Session locking

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-020 | Quick rejoin on another server | Player leaves server 1, joins server 2 at once | 1) Observe load on server 2. | Server 2 waits until server 1 released the lock (or the lock expires) before loading; loaded data includes server 1's final save. | P0 | edge | D-025 |
| TC-PER-021 | Stale lock after a crash | Server 1 crashed holding the lock | 1) Player joins server 2. | Lock treated as stale after `T_lock`; profile loads; no data from before the crash's last save is lost. | P0 | edge | D-025 |
| TC-PER-022 | Rejoining another server mid-raid | Player was in a raid on server 1 | 1) Rejoin on server 2. | See TC-RAID-045: raid ended, committed transfers present, lock respected. | P0 | edge | D-024 |

## 4. Schema and validation

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-030 | Migration from the previous schema | `QA_LoadFixtureProfile("schema_prev")` | 1) Load. | Migrated to the current version; every item preserved; migration logged once. | P0 | functional | D-025 |
| TC-PER-031 | Profile from a newer schema | Profile saved by a newer build (rollback scenario) | 1) Load on the older build. | Loaded read-only or the player is asked to rejoin later; the newer data is never overwritten by the older build. | P0 | edge | D-025 |
| TC-PER-032 | Corrupt or invalid fields | Missing fields, wrong types, negative counts, unknown animal IDs | 1) Load each fixture. | Validation repairs or quarantines per [[Data Validation and Migration]]; nothing crashes; repairs are logged for support. | P1 | edge | D-025 |
| TC-PER-033 | Cash is a non-negative integer | Many fractional multiplier sources | 1) Earn rewards with Shrine and Trophy bonuses for 30 minutes. 2) Inspect stored Cash. | Stored Cash is an integer after every operation (rounding rule per [[Wild Animal Cash Rewards]]); never negative. | P0 | edge | D-014 |
| TC-PER-034 | Integer overflow on Cash | Cash set to `MAX_CASH − 5` | 1) Earn a reward of 100. 2) Try to earn more. | Cash clamps at `MAX_CASH`; never wraps, becomes negative, loses integer precision or turns into `inf`/NaN. The excess is logged. A spend from `MAX_CASH` works normally. | P0 | edge | D-014 |
| TC-PER-035 | Duplicate instance IDs in stored data | Fixture with two animals sharing one ID | 1) Load. | Detected; one is re-keyed or quarantined per [[Data Validation and Migration]]; no crash; logged as a data-integrity alert. | P1 | edge | D-019 |

## 5. Transactions and purchases

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-040 | Purchase receipt processed once | A developer product exists (for example from [[Monetisation Product Concepts]]) | 1) Buy. 2) Simulate `MarketplaceService.ProcessReceipt` being called again with the same `PurchaseId`. | Item granted once; the callback returns `PurchaseGranted` only after the grant is saved; the purchase ID is recorded in the profile to make repeats idempotent. | P0 | security | D-027 |
| TC-PER-041 | Receipt during save failure | Save errors injected | 1) Buy. | Callback returns `NotProcessedYet`; the grant is retried on the next receipt call; never granted without being saved, never lost. | P0 | edge | D-027 |
| TC-PER-042 | Cross-profile transfer (raid theft) | Attacker and defender profiles | 1) Settle a theft. 2) `QA_KillServerBetweenWrites()` variant. | Item ends in exactly one profile after recovery (TC-RAID-044). | P0 | edge | D-024 |
| TC-PER-043 | Local transactions are atomic | Roll, hatch, merge, ascension, upgrade | 1) Kill the server at each internal stage of each transaction. | Every transaction is all-or-nothing after reload (INV-01 to INV-03). | P0 | edge | D-019, D-020 |

## 6. Environment separation

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PER-050 | Test data never reaches production | QA build | 1) Use QA hooks (grant Cash). 2) Inspect production DataStores. | Production unaffected; QA experience uses separate DataStores. | P0 | security | D-027 |
| TC-PER-051 | Recovery tooling | A support request to restore a profile | 1) Restore from a previous saved version using the procedure in [[Save, Load and Recovery]]. | Procedure works on the test experience; restored profile passes validation. | P2 | functional | D-025 |

## Related documents

- [[Test Cases - Raiding]]
- [[Test Cases - Multiplayer]]
- [[Test Cases - Exploit Prevention]]
- [[Save, Load and Recovery]]
- [[Data Architecture Overview]]
- [[Data Validation and Migration]]
- [[Data Consistency and Transactions]]
- [[Service - DataService]]
- [[Roblox API Reference Notes]]
