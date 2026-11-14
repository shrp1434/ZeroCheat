---
title: Schema - Economy
type: data-schema
category: data
status: mixed
priority: P0
owner: Data Architect
last_updated: 2026-11-14
tags:
  - data
  - schema
  - economy
  - monetisation
---

# Schema - Economy

## Purpose

Stores the player's Cash balance, lifetime earning and spending counters by category, and the ring of processed Robux purchase receipts that makes `ProcessReceipt` idempotent. Economy rules are owned by [[Economy Overview]] and [[Cash Sources and Sinks]]. The purchase flow is in [[Save, Load and Recovery]].

> [!success] CONFIRMED
> Cash comes from defeating wild animals and buys egg rolls (D-014). The game must be fully playable without Robux (D-027).

> [!info] PROPOSED
> Cash is never sold for Robux (D-044), so this schema has no "premium Cash" path. If storage expansion is ever priced in a second currency ([[Open Questions#Q-009]]), that currency is added here by a migration. No such currency is assumed.

## Field table

| Field | Luau type | Required | Default | Validation | Notes |
|---|---|---|---|---|---|
| `cash` | `number` | Required | `0` | Integer, 0 ≤ cash ≤ 10^15 | Cap (PROPOSED) keeps values exact in a double (2^53 ≈ 9.0 × 10^15). Above the cap is a soft failure: clamp and flag for review. |
| `lifetime.earned` | `{ [string]: number }` | Required | `{}` | Keys from the source list below; integers ≥ 0 | Lifetime Cash earned by source |
| `lifetime.spent` | `{ [string]: number }` | Required | `{}` | Keys from the sink list below; integers ≥ 0 | Lifetime Cash spent by sink |
| `receipts` | `{ ReceiptRecord }` | Required | `{}` | ≤ 100 entries, newest last; unique `purchaseId` | Ring of the last 100 processed developer-product receipts |
| `robuxSpentTotal` | `number` | Required | `0` | Integer ≥ 0 | From `ReceiptInfo.CurrencySpent`; used for analytics and spend-awareness features only, never for gameplay odds |
| `lastCashChangeAt` | `number?` | Optional | `nil` | Unix seconds | Analytics |

Source keys (PROPOSED): `wild`, `boss`, `raid`, `event`, `refund`, `support`. Sink keys (PROPOSED): `roll`, `merge`, `ascension`, `module`, `station`, `plot`, `storage`, `other`. New keys need only a config change.

`ReceiptRecord`: `purchaseId` (string as provided by `ReceiptInfo.PurchaseId`), `productId` (integer), `at` (Unix seconds).

### Derived values (never stored)

| Value | Formula | Source |
|---|---|---|
| Cash per wild defeat | `BaseCash × RegionMultiplier × (1 + CashBonuses)` | [[Canonical Proposed Values]] §6; bonuses from [[Schema - Base Data]] |
| Net Cash balance check | `Σ earned − Σ spent` | Validation (see invariant 3) |

## Illustrative Luau type definition and constructor

```lua
-- Illustrative Luau, not executed.
export type ReceiptRecord = { purchaseId: string, productId: number, at: number }

export type Economy = {
	cash: number,
	lifetime: { earned: { [string]: number }, spent: { [string]: number } },
	receipts: { ReceiptRecord },
	robuxSpentTotal: number,
	lastCashChangeAt: number?,
}

local CASH_CAP = 1e15 -- PROPOSED
local RECEIPT_RING = 100 -- PROPOSED

local function newEconomy(): Economy
	return {
		cash = 0,
		lifetime = { earned = {}, spent = {} },
		receipts = {},
		robuxSpentTotal = 0,
		lastCashChangeAt = nil,
	}
end

-- All Cash changes go through these two functions so lifetime counters stay consistent.
local function addCash(economy: Economy, amount: number, source: string, now: number)
	assert(amount >= 0 and amount % 1 == 0, "invalid amount")
	economy.cash = math.min(economy.cash + amount, CASH_CAP)
	economy.lifetime.earned[source] = (economy.lifetime.earned[source] or 0) + amount
	economy.lastCashChangeAt = now
end

local function trySpend(economy: Economy, amount: number, sink: string, now: number): boolean
	assert(amount >= 0 and amount % 1 == 0, "invalid amount")
	if economy.cash < amount then
		return false
	end
	economy.cash -= amount
	economy.lifetime.spent[sink] = (economy.lifetime.spent[sink] or 0) + amount
	economy.lastCashChangeAt = now
	return true
end

local function hasReceipt(economy: Economy, purchaseId: string): boolean
	for _, record in economy.receipts do
		if record.purchaseId == purchaseId then return true end
	end
	return false
end

local function recordReceipt(economy: Economy, purchaseId: string, productId: number, now: number)
	table.insert(economy.receipts, { purchaseId = purchaseId, productId = productId, at = now })
	if #economy.receipts > RECEIPT_RING then
		table.remove(economy.receipts, 1)
	end
end
```

## Invariants

1. `cash` is a non-negative integer, never above `CASH_CAP`.
2. Every Cash change goes through `addCash` or `trySpend`. Spending checks the balance and deducts in the same synchronous block as the purchase it pays for (no yield between check and commit).
3. `cash ≤ Σ lifetime.earned − Σ lifetime.spent` (it is lower only when the cap clamped earnings). A balance above that bound is a strong exploit or corruption signal: soft failure, flag for review, and alert.
4. `receipts` has unique `purchaseId` values and at most 100 entries. A receipt ID is recorded in the **same** in-memory change as its grant.
5. No field in this schema influences egg or hatch odds. Robux spend in particular must never feed luck ([[Randomised Reward Compliance]], D-017).

> [!danger] Receipt ring size
> The ring must be large enough that Roblox never retries a receipt older than the oldest entry still held. Receipts are retried until granted (*unverified* exact retry policy), and the ring only holds receipts that were granted, so 100 entries is generous for any realistic purchase rate. The `PurchaseLedger_v1` store keeps the complete history for support.

## Migration notes

- Adding a currency: new field with default `0`, a schema bump, new source and sink keys. Update [[Cost Tables]] and [[Storage Expansion Economics]].
- If the cap is lowered, players above it are clamped only by an explicit migration with live-ops sign-off, never by the validator alone.

## Size estimate

About 0.5 KiB plus about 60 bytes per receipt record; a full ring of 100 ≈ 6.5 KiB. Negligible against the 4 MB per-key limit (*unverified — verify before use*).

## Related documents
- [[Economy Overview]]
- [[Cash Sources and Sinks]]
- [[Service - EconomyService]]
- [[Monetisation Product Concepts]]
- [[Roblox Monetisation Policy Requirements]]
- [[Inflation and Farming Exploit Risks]]
- [[Save, Load and Recovery]]
- [[Data and Balancing Index]]
