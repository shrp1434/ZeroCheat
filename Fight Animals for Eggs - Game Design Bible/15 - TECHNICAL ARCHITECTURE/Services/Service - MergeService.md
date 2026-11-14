---
title: Service - MergeService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - eggs
  - merging
  - transactions
---

# Service - MergeService

> [!info] PROPOSED
> Layer **6**. Design is **PROPOSED**; code is illustrative Luau, not tested. Design: [[Egg Merging]], [[Egg Merging Station]]. Transaction detail: [[Implementation - Egg Merge Transaction]]. Station levels, costs, fees and gates are **PROPOSED** and final costs **UNDECIDED** ([[Open Questions#Q-019]]).

> [!success] CONFIRMED rules enforced here (D-020)
> Three eggs of one rarity make one egg of the next rarity. Merging needs a purchased **Egg Merging Station**, which must be upgraded before it can merge higher rarities. Secret eggs cannot be merged further (no rarity above Secret).

## Responsibility

- Validate and commit merges: exactly **3** eggs of the same rarity → **1** egg of the next rarity.
- Check the player owns an Egg Merging Station at a level that unlocks that merge tier, and charge the tier's Cash fee.
- Require the player to be at their own base.
- Place the output egg in base storage (with the fallback below).

It does **not** sell or upgrade the station; purchase and upgrades are base modules handled by [[Service - BaseService]], which also swaps the station's physical model per level.

## Inputs

| Input | Source |
|---|---|
| `Merge/RequestMerge` | Client |
| Station level, `IsAtOwnBase` | [[Service - BaseService]] |
| Egg records and helpers | [[Service - EggService]] |
| Fee debit | [[Service - EconomyService]] |
| Locks | `Systems/AssetLocks` |

## Outputs

| Output | Consumer |
|---|---|
| `eggs`, `economy` changes | Client via deltas |
| `EggsMerged(player, fromRarity, outputEgg)` signal | Analytics, station VFX trigger on clients via `Notify/Toast` code |
| `egg_merged`, `cash_sink` analytics | AnalyticsAndLoggingService |

## Dependencies

[[Service - EggService]], [[Service - BaseService]], [[Service - EconomyService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `AssetLocks`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `EggsMerged` | `(player, fromRarity: Rarity, output: EggRecord)` |
| Remote | `Merge/RequestMerge` | [[Remote Communication Contract#2.5 Ascension, merging, base, team]] |

## Data structures

```lua
--!strict
export type MergeTier = { from: Rarity, to: Rarity, stationLevel: number, fee: number }

-- Mirrors Canonical Proposed Values §10 (PROPOSED, Q-019)
local TIERS: { [Rarity]: MergeTier } = {
	Common    = { from = "Common",    to = "Uncommon",  stationLevel = 1, fee = 100 },
	Uncommon  = { from = "Uncommon",  to = "Rare",      stationLevel = 1, fee = 300 },
	Rare      = { from = "Rare",      to = "Epic",      stationLevel = 2, fee = 900 },
	Epic      = { from = "Epic",      to = "Legendary", stationLevel = 3, fee = 2700 },
	Legendary = { from = "Legendary", to = "Mythical",  stationLevel = 4, fee = 8000 },
	Mythical  = { from = "Mythical",  to = "Secret",    stationLevel = 5, fee = 25000 },
	-- Secret: no entry. Merging Secret eggs is impossible (CONFIRMED).
}
local INPUT_COUNT = 3 -- CONFIRMED
```

## Output placement

The canonical rule is that the output egg goes to **base storage** and that total capacity always frees by two. One edge case is not covered: if all three inputs came from the backpack and base storage is full, there is no base slot for the output.

> [!info] PROPOSED handling of the full-base edge case
> Place the output in base storage when a slot is free after removing the inputs; otherwise place it in the backpack slot freed by an input. The player is told where the egg went. This keeps "merging always succeeds when the inputs are valid" true. Flagged to the lead for [[Egg Merging]].

## Public API

```lua
--!strict
function MergeService:GetAvailableTiers(player: Player): { MergeTier }
function MergeService:HandleRequestMerge(player: Player, p: { eggIds: { string } }): Result<{ egg: EggRecord }>
```

## Validation order

| # | Check | Code |
|---:|---|---|
| 1 | Exactly 3 distinct egg IDs | `E_MERGE_INVALID` |
| 2 | Player at own base | `E_NOT_AT_BASE` |
| 3 | All 3 owned | `E_NOT_OWNED` |
| 4 | None locked (open hatch quote, raid lock Q-808) | `E_ASSET_LOCKED` |
| 5 | All the same rarity | `E_MERGE_INVALID` |
| 6 | Rarity is not Secret | `E_MERGE_MAX_RARITY` |
| 7 | Station owned | `E_STATION_REQUIRED` |
| 8 | Station level ≥ tier requirement | `E_STATION_LEVEL` |
| 9 | Cash ≥ fee | `E_INSUFFICIENT_CASH` |

Then one `Mutate` over `{ "eggs", "economy" }`: remove the 3 inputs, debit the fee, add the output egg (source `Merge`). Presentation (2.5–6 s animation by tier) starts on the client after the response; there is no wait timer (timed merging is **UNDECIDED**, [[Open Questions#Q-034]]).

Worked example: three Rare eggs with a Level 2 Stonebound Hatchery Forge and 5,000 Cash → one Epic egg, Cash 4,100 (fee 900). With a Level 1 Twig Nest Press the same request returns `E_STATION_LEVEL`.

## Error handling

All failures before the commit return the code from the table and change nothing. A failure inside the commit restores the declared sections and returns `E_INTERNAL` (`Error` log). Merges are not quoted because they are deterministic; there are no odds to disclose.

## Security requirements

- The client sends egg IDs only. Rarities, tier, fee and output rarity are derived from server records and config.
- Station level is read from BaseService, never from the client.
- Inputs, fee and output are one transaction; no merge can consume eggs without producing the output.
- During an active raid on the player's base, base-stored eggs are locked (**UNDECIDED** policy Q-808), so merging cannot be used to move eggs out of reach.

## Testing requirements

| Test | Type |
|---|---|
| Every tier at the exact required station level succeeds; one level below fails | Unit |
| 2 or 4 eggs rejected; 3 eggs of mixed rarity rejected | Unit |
| 3 Secret eggs rejected | Unit |
| Merge away from base rejected | Unit |
| Same 3 egg IDs submitted twice: second fails with `E_NOT_OWNED` | Unit |
| Full base + 3 backpack inputs: output lands in backpack | Unit |
| Capacity after merge = capacity before − 2 eggs | Property test |

Full list: [[Test Cases - Egg Merging]].

## Related documents
- [[Technical Architecture Index]]
- [[Egg Merging]]
- [[Egg Merging Station]]
- [[Implementation - Egg Merge Transaction]]
- [[Service - EggService]]
- [[Service - BaseService]]
- [[UI - Egg Merging]]
- [[Animation - Egg Merge]]
- [[Test Cases - Egg Merging]]
