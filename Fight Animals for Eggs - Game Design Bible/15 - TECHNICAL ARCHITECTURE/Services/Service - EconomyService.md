---
title: Service - EconomyService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - economy
  - cash
  - monetisation
---

# Service - EconomyService

> [!info] PROPOSED
> Layer **2**. Design is **PROPOSED**; code is illustrative Luau, not tested. Economy design: [[Economy Overview]], [[Cash Sources and Sinks]]. Schema: [[Schema - Economy]].

> [!success] CONFIRMED rules enforced here
> Defeating wild animals earns Cash, and Cash buys egg rolls (D-014). The game is fully playable without Robux (D-027).

## Responsibility

- Be the **ledger** for Cash: the only code that changes the Cash balance.
- Provide composable debit and credit helpers that run **inside** another service's `DataService:Mutate` call, so a purchase and its item grant commit together.
- Record lifetime sources and sinks for analytics and inflation monitoring ([[Inflation and Farming Exploit Risks]]).
- Own `MarketplaceService.ProcessReceipt` and developer-product grants (idempotent).
- Gate storage-expansion purchases behind the `StorageExpansion` feature flag until the currency and price are decided (**UNDECIDED**, [[Open Questions#Q-009]], [[Open Questions#Q-010]]).

It does **not** compute reward amounts. CombatService computes `BaseCash × RegionMultiplier × (1 + CashBonuses)` and calls `Credit` (this avoids a dependency cycle with BaseService; see [[Service Architecture#4. Dependency layers]]).

## Inputs

| Input | Source |
|---|---|
| `Credit` calls | CombatService (wild defeats, kill credit), BossService (if boss rewards include Cash; **UNDECIDED**, [[Open Questions#Q-015]]), refunds |
| `DebitInProfile` calls inside mutations | EggService (rolls), MergeService (fees), AscensionService (fees), BaseService (upgrades, plot expansion, station) |
| `MarketplaceService.ProcessReceipt` callbacks | Roblox |

## Outputs

| Output | Consumer |
|---|---|
| Profile `economy` section changes (replicated via DataService) | Client HUD |
| `CashChanged(player, newBalance, delta, reason)` signal | Analytics, quests in future |
| `cash_source` / `cash_sink` analytics | [[Service - AnalyticsAndLoggingService]] |
| `Shop/PurchaseGranted` remote | Client |

## Dependencies

[[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. MarketplaceService (Roblox).

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `CashChanged` | `(player, balance: number, delta: number, reason: string)` |
| Signal | `ProductGranted` | `(player, productKey: string, purchaseId: string)` |
| Remote S→C | `Shop/PurchaseGranted` | `{ productKey }` |

## Data structures

```lua
--!strict
export type EconomySection = {
	cash: number,               -- integer, >= 0
	lifetimeEarned: number,
	lifetimeSpent: number,
	sourceTotals: { [string]: number }, -- e.g. WildDefeat, BossDefeat, Refund
	sinkTotals: { [string]: number },   -- e.g. EggRoll, MergeFee, AscensionFee, ModuleUpgrade
	processedReceipts: { [string]: number }, -- PurchaseId -> os.time(), pruned after 90 days (PROPOSED)
}

export type CashSource = "WildDefeat" | "BossDefeat" | "Refund" | "Admin"
export type CashSink = "EggRoll" | "MergeFee" | "AscensionFee" | "ModuleUpgrade"
	| "PlotExpansion" | "StationPurchase" | "StorageExpansion"
```

Cash is always an integer. Fractional reward results are **floored** at the point of credit (**PROPOSED** rounding rule). Maximum balance (**PROPOSED**): 2^53 is the exact-integer limit of a Luau number; the service clamps at 1e15 and logs `economy.cap_reached`, which should never happen in normal play.

## Public API

```lua
--!strict
function EconomyService:GetCash(player: Player): number

-- Standalone credit (its own Mutate). Used for rewards.
function EconomyService:Credit(player: Player, amount: number, source: CashSource, meta: { [string]: any }?): boolean

-- Composable helpers: call ONLY inside DataService:Mutate with "economy" declared.
function EconomyService:CanAfford(data: ProfileData, amount: number): boolean
function EconomyService:DebitInProfile(data: ProfileData, amount: number, sink: CashSink): boolean
function EconomyService:CreditInProfile(data: ProfileData, amount: number, source: CashSource): ()

-- Developer products. Handlers are registered by product key at Start.
function EconomyService:RegisterProduct(productKey: string, productId: number,
	grant: (player: Player, data: ProfileData) -> boolean, sections: { string }): ()
```

Worked example (kill reward, values from [[Canonical Proposed Values]]): a Rare wild animal defeated in Sunscorch Savanna (region ×1.5) by a player with Multiplier Shrine L2 (+20%) and 3 unique boss trophies (+3%): `28 × 1.5 × (1 + 0.20 + 0.03) = 51.66` → **51 Cash** credited. Every contributor with ≥ 10% damage receives the full 51 (D-040).

## Receipt processing

```lua
--!strict
-- Illustrative Luau, not tested.
MarketplaceService.ProcessReceipt = function(receipt)
	local player = Players:GetPlayerByUserId(receipt.PlayerId)
	if not player or not Data:IsLoaded(player) then
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end
	local product = productsById[receipt.ProductId]
	if not product then
		Log:Error("unknown_product", player, { productId = receipt.ProductId })
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end

	local sections = table.clone(product.sections)
	table.insert(sections, "economy")
	local granted = Data:Mutate(player, "receipt", sections, function(data)
		if data.economy.processedReceipts[receipt.PurchaseId] then
			return true -- already granted earlier; idempotent
		end
		if not product.grant(player, data) then return false end
		data.economy.processedReceipts[receipt.PurchaseId] = os.time()
		return true
	end)
	if not granted then
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end
	Data:RequestPrioritySave(player, "receipt")
	return Enum.ProductPurchaseDecision.PurchaseGranted
end
```

> [!warning] Save-before-grant caveat
> Returning `PurchaseGranted` before the priority save completes means a server crash in that window could lose the grant while Roblox considers it delivered. The safer pattern is to save first and return `PurchaseGranted` only after the save succeeds. Which pattern to adopt is detailed in [[Data Consistency and Transactions]]; this service supports both because `RequestPrioritySave` returns a `SaveTicket` whose `Wait()` yields until the save finishes ([[Service - DataService#Public API]]). `ProcessReceipt` is allowed to yield.

> [!info] PROPOSED (D-044)
> No product grants Cash, directly or indirectly. Product grant functions must never call `CreditInProfile`; the `economy` section is declared only so the receipt ID can be recorded. A unit test runs every registered grant and asserts the Cash balance is unchanged. Whether any Robux product may ever grant Cash is **UNDECIDED** ([[Open Questions#Q-032]]).

## Error handling

| Case | Result |
|---|---|
| Debit larger than balance | `DebitInProfile` returns `false`; caller's mutation aborts; client gets `E_INSUFFICIENT_CASH` |
| Negative, non-integer or NaN amount | `assert` fails inside the mutation → sections restored → `E_INTERNAL`, `Error` log (this is a server bug, never client input) |
| Player left before receipt processed | `NotProcessedYet`; Roblox retries later |
| Unknown product ID | `NotProcessedYet` and `Error` log |

## Security requirements

- No remote accepts an amount of Cash. Clients cannot request credits.
- Every credit names a `CashSource`; the `Admin` source is usable only from Studio or by allow-listed user IDs in server config, and is logged at `Security` level.
- Inflation guard: if a player's Cash earned per minute exceeds 5× the expected rate for their region and level for 10 minutes (**PROPOSED**), log `security.farm_rate` for review ([[Inflation and Farming Exploit Risks]]). No automatic penalty.

## Testing requirements

| Test | Type |
|---|---|
| Debit then failed grant inside one mutation leaves Cash unchanged | Unit |
| Receipt processed twice with the same `PurchaseId` grants once | Unit |
| Receipt for an offline player returns `NotProcessedYet` | Unit |
| Floor rounding on rewards; no fractional Cash ever stored | Unit |
| Cash sources and sinks totals reconcile with `lifetimeEarned − lifetimeSpent = cash − startingCash` | Property test over random transaction sequences |
| Spam of every purchase remote cannot produce Cash | Exploit test ([[Test Cases - Exploit Prevention]]) |

## Related documents
- [[Technical Architecture Index]]
- [[Economy Overview]]
- [[Cash Sources and Sinks]]
- [[Wild Animal Cash Rewards]]
- [[Schema - Economy]]
- [[Monetisation Principles]]
- [[Roblox Monetisation Policy Requirements]]
- [[Storage Expansion Economics]]
- [[Service - CombatService]]
