---
title: Schema - Player Profile
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - persistence
  - player-profile
---

# Schema - Player Profile

## Purpose

The root document stored under `PlayerProfile_v1 / u_<UserId>`. It wraps every other section in a storage envelope that carries the session lock and save revision, and it holds the few fields that belong to no single gameplay system: identity, timestamps, settings, moderation flags and the transaction bookkeeping used for idempotency. Layout and locking are explained in [[Data Architecture Overview]].

> [!info] PROPOSED
> All fields, defaults and limits are **PROPOSED**. Code is illustrative Luau and has not been executed.

## Envelope fields (`meta`)

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `meta.formatVersion` | `number` | Required | `1` | Integer = 1 | Envelope format, not schema version |
| `meta.revision` | `number` | Required | `0` | Integer ≥ 0, increases by 1 per save | Used by restore tooling and ledgers |
| `meta.session` | `SessionLock?` | Optional | `nil` | If present: `jobId` non-empty string, `placeId` integer, `lockedAt` ≤ `heartbeatAt` | `nil` means unlocked |
| `meta.lastSavedAt` | `number` | Required | creation time | Unix seconds | |
| `meta.lastSavedBy` | `string` | Required | `""` | String ≤ 64 characters | JobId of the last writer |
| `meta.restoredFrom` | `string?` | Optional | `nil` | ≤ 128 characters | Set only by restore tooling |

## Data root fields (`data`)

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `schemaVersion` | `number` | Required | `CURRENT_SCHEMA_VERSION` | Integer 1 … current | [[Data Validation and Migration]] |
| `userId` | `number` | Required | `player.UserId` | Positive integer equal to the key's user | Mismatch is a hard failure |
| `createdAt` | `number` | Required | `os.time()` at first join | Unix seconds, ≤ now | |
| `lastLoginAt` | `number` | Required | `os.time()` | ≥ `createdAt` | Updated on each claim |
| `loginCount` | `number` | Required | `1` | Integer ≥ 1 | Analytics only |
| `playtimeSeconds` | `number` | Required | `0` | Integer ≥ 0 | Accumulated on each save |
| `settings` | `Settings` | Required | see constructor | Known keys only; volumes 0–1 | Player preferences ([[UI - Settings]]) |
| `flags` | `ProfileFlags` | Required | all `false` | Booleans | Support and moderation markers |
| `pending` | `{ [string]: PendingTx }` | Required | `{}` | ≤ 16 entries; keys are transaction IDs | Open transactions. Intra-profile entries are cleared on load. |
| `appliedTx` | `{ string }` | Required | `{}` | ≤ 50 strings, newest last | Ring of applied cross-profile and inbox transaction IDs, for idempotency |
| `progression` | `PlayerProgression` | Required | constructor | [[Schema - Player Progression]] | |
| `animals` | `AnimalCollection` | Required | constructor | [[Schema - Animal Collection]] | |
| `team` | `EquippedTeam` | Required | constructor | [[Schema - Equipped Team]] | |
| `eggs` | `EggInventory` | Required | constructor | [[Schema - Egg Inventory]] | |
| `base` | `BaseData` | Required | constructor | [[Schema - Base Data]] | |
| `economy` | `Economy` | Required | constructor | [[Schema - Economy]] | |
| `unlocks` | `UnlocksAndBossProgress` | Required | constructor | [[Schema - Unlocks and Boss Progress]] | |
| `index` | `DiscoveryIndex` | Required | constructor | [[Schema - Discovery Index]] | |
| `_unknown` | `{ [string]: any }?` | Optional | `nil` | Any | Keys the validator did not recognise, preserved for review |

`Settings`: `musicVolume` (0.8), `sfxVolume` (0.8), `reducedMotion` (`false`), `skipSeenHatchAnimations` (`false`), `showDamageNumbers` (`true`). Settings that are device-specific (graphics quality) are not stored here.

`ProfileFlags`: `needsReview` (validator soft failure), `restorePending` (mass rollback gate), `testAccount` (excluded from analytics).

`PendingTx`: `kind` (`"merge" | "ascension" | "hatch" | "raid" | "inbox"`), `startedAt` (Unix seconds), `refs` (list of instance IDs touched).

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type SessionLock = { jobId: string, placeId: number, lockedAt: number, heartbeatAt: number }

export type ProfileMeta = {
	formatVersion: number,
	revision: number,
	session: SessionLock?,
	lastSavedAt: number,
	lastSavedBy: string,
	restoredFrom: string?,
}

export type Settings = {
	musicVolume: number,
	sfxVolume: number,
	reducedMotion: boolean,
	skipSeenHatchAnimations: boolean,
	showDamageNumbers: boolean,
}

export type PendingTx = {
	kind: "merge" | "ascension" | "hatch" | "raid" | "inbox",
	startedAt: number,
	refs: { string },
}

export type PlayerProfile = {
	schemaVersion: number,
	userId: number,
	createdAt: number,
	lastLoginAt: number,
	loginCount: number,
	playtimeSeconds: number,
	settings: Settings,
	flags: { needsReview: boolean, restorePending: boolean, testAccount: boolean },
	pending: { [string]: PendingTx },
	appliedTx: { string },
	progression: PlayerProgression,
	animals: AnimalCollection,
	team: EquippedTeam,
	eggs: EggInventory,
	base: BaseData,
	economy: Economy,
	unlocks: UnlocksAndBossProgress,
	index: DiscoveryIndex,
	_unknown: { [string]: any }?,
}

export type ProfileEnvelope = { meta: ProfileMeta, data: PlayerProfile }

local function newPlayerProfile(userId: number, now: number): PlayerProfile
	return {
		schemaVersion = CURRENT_SCHEMA_VERSION,
		userId = userId,
		createdAt = now,
		lastLoginAt = now,
		loginCount = 1,
		playtimeSeconds = 0,
		settings = {
			musicVolume = 0.8,
			sfxVolume = 0.8,
			reducedMotion = false,
			skipSeenHatchAnimations = false,
			showDamageNumbers = true,
		},
		flags = { needsReview = false, restorePending = false, testAccount = false },
		pending = {},
		appliedTx = {},
		progression = Progression.new(),
		animals = AnimalCollection.new(),
		team = EquippedTeam.new(),
		eggs = EggInventory.new(),
		base = BaseData.new(now),
		economy = Economy.new(),
		unlocks = Unlocks.new(now),
		index = DiscoveryIndex.new(),
	}
end
```

## Invariants

1. `data.userId` equals the numeric part of the key. A mismatch is a hard failure (never "repair" it to match).
2. `schemaVersion` ≤ the running server's `CURRENT_SCHEMA_VERSION`, otherwise the profile is not loaded ([[Data Validation and Migration]] rule H3).
3. Every instance ID is unique across `animals.instances` and `eggs.instances`.
4. Every ID in a `pending[...].refs` list exists in the profile, and the referenced instance's `pendingTx` equals that transaction ID.
5. `appliedTx` holds at most 50 entries. Adding a 51st drops the oldest.
6. `meta.session` is written only through `UpdateAsync` by DataService.
7. The profile never stores derived values listed in [[Data Architecture Overview]] §1 (P3).

## Migration notes

- Adding a new top-level section (for example a future quest log) is a migration that inserts the section's constructor output.
- `settings` keys are additive. Removing a setting deletes its key in a migration rather than leaving it in `_unknown`.
- Retention and erasure rules for the side stores this profile references are **UNDECIDED** (Q-955).

## Size estimate

The root and envelope, excluding sections, are about 0.8 KiB. A complete profile is 21–121 KiB for realistic shapes ([[Data Architecture Overview]] §8), well under the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Data Architecture Overview]]
- [[Data Validation and Migration]]
- [[Save, Load and Recovery]]
- [[Service - DataService]]
- [[Template - Data Schema]]
- [[Data and Balancing Index]]
