---
title: Storage Expansion Economics
type: analysis
category: economy
status: undecided
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - storage
  - eggs
  - monetisation
---

# Storage Expansion Economics

Analysis of how extra egg storage could be sold. **No currency and no price is decided here.**

> [!success] CONFIRMED
> Storage starts at backpack **10** + base **50** = **60**. Backpack eggs can never be stolen. Extra space is purchasable (D-021).

> [!warning] UNDECIDED
> - Expansion **currency**: **UNDECIDED** ([[Open Questions#Q-009]]).
> - Expansion **price**: **UNDECIDED** ([[Open Questions#Q-010]]).
> - The step sizes (+5 backpack ×3 to 25, +25 base ×6 to 200) are **PROPOSED** ([[Canonical Proposed Values]] §11).

## 1. What a slot is worth

| Value driver | Backpack slot | Base slot |
|---|---|---|
| Theft protection | **Total**: never stealable | None: stealable in an eligible raid |
| Where eggs can hatch | Anywhere outside combat | Only at the base |
| Merge throughput | Holds merge inputs while away | Holds the bulk of merge inputs and outputs |
| Late-game roll throughput | Small | Large: 312 rolls per hour at Starfall Sanctuary fill 60 slots in ~12 minutes |
| Raid exposure | Reduces it | **Increases** it (more eggs at risk) |

> [!danger] Fairness risk: backpack slots are protection
> Because backpack eggs are never stealable, every extra backpack slot is permanent theft protection. Selling backpack slots for Robux would let paying players shield more eggs from raids, which is a pay-to-win effect in PvP and conflicts with the spirit of D-027 ([[Monetisation Principles]]).

### Do players need more than 60?

- **Early (Regions 1–3):** rarely. Income is 25–66 rolls per hour and merging consumes eggs. 60 is enough.
- **Mid (Regions 4–6):** sometimes, when saving eggs for a station upgrade that unlocks the next merge tier (for example banking Epics before the Crystal Incubator).
- **Late (Regions 7–8):** yes, for throughput. Merging a full Secret chain needs only a few slots at a time if done continuously, but hatching sessions, saving for ascension targets and batching merges all want space.

Conclusion: storage is a **mid-to-late convenience and throughput** item, not an essential gate, provided merging and hatching stay fast.

## 2. Currency options for Q-009

| Option | Description | F2P fairness | Revenue | Raid fairness | Compliance | Complexity |
|---|---|---|---|---|---|---|
| A. Cash only | Every step is bought with Cash | Full | None | Full | No impact | Low |
| B. Robux only | Every step costs Robux | Poor: a core capacity becomes paid | Medium | Poor for backpack (paid protection) | No paid-random impact (storage is not random), but a functional advantage sold | Low |
| C. Mixed: Cash or Robux per step | Each step can be bought with either | Good if Cash prices are reachable | Low–medium | Backpack still purchasable for Robux | As B for the Robux path | Medium (two prices) |
| D. Progression-unlocked | Steps unlock at milestones (region unlocks, station levels) for free or for Cash | Full | None | Full | No impact | Low |
| E. Hybrid D + A | Steps unlock at milestones **and** cost Cash | Full | None | Full | No impact | Low |
| F. Split by location | Backpack via D/E only; base storage via A or C | Good | Low | Backpack protected from Robux | As C for base | Medium |

> [!info] PROPOSED recommendation (labelled, not a decision)
> **Option E for both locations**: each step unlocks at a progression milestone and then costs Cash. If the owner wants a Robux path, use **Option F**: Robux may only buy **base** storage steps that are also available for Cash, never backpack steps. Final decision: **UNDECIDED** ([[Open Questions#Q-009]], [[Open Questions#Q-010]]).

## 3. Illustrative price ladders (for modelling only)

> [!warning] Illustrative only
> The ladders below exist so the [[Balance Simulation Plan]] can run. They are **not** proposed prices and must not appear in builds or UI until Q-010 is decided.

**Model M-1 (Cash, milestone-gated, ≈ 1–1.5 hours of income at the gate region):**

| Step | Backpack (+5) gate | Backpack illustrative Cash | Base (+25) gate | Base illustrative Cash |
|---:|---|---:|---|---:|
| 1 | Region 2 unlocked | 12,500 | Region 2 unlocked | 8,000 |
| 2 | Region 4 unlocked | 30,000 | Region 3 unlocked | 13,000 |
| 3 | Region 6 unlocked | 55,000 | Region 4 unlocked | 19,000 |
| 4 | — | — | Region 5 unlocked | 27,000 |
| 5 | — | — | Region 6 unlocked | 38,000 |
| 6 | — | — | Region 7 unlocked | 48,000 |
| **Total** | | **97,500** | | **153,000** |

At M-1 the full expansion (250,500 Cash) would be ~11% of the full-base cost, which keeps storage a secondary sink.

**Model M-2 (Robux path for base storage only, Option F):** a single PROPOSED-for-modelling price point per base step in the 49–99 Robux range. This is listed only so the Monetisation Designer can model conversion. It is subject to the same **UNDECIDED** status.

## 4. Interaction with other systems

| System | Interaction |
|---|---|
| [[Egg Theft Rules]] | Larger base storage means more eggs at risk; the theft limit (**UNDECIDED** [[Open Questions#Q-013]]) caps losses per raid regardless of capacity |
| [[Module - Egg Vault]] | Vault levels do not change capacity |
| [[Egg Merging Station]] | Output always goes to base storage; merges always net-free two slots |
| [[Egg Pricing]] | Rolls are blocked before payment when storage is full |
| [[Roblox Monetisation Policy Requirements]] | A Robux storage purchase is a deterministic item, not a paid random item |

## 5. Technical notes

- Capacity is stored as step counts (`backpackSteps`, `baseSteps`) in [[Schema - Egg Inventory]], and capacity is derived: `10 + 5 × backpackSteps`, `50 + 25 × baseSteps`.
- Any Robux path uses MarketplaceService developer products with an idempotent ProcessReceipt handler that records the purchase ID before granting ([[Roblox Monetisation Policy Requirements]]).
- Reducing capacity in a future update must never delete eggs; over-capacity eggs stay until used (**PROPOSED** rule, [[Data Validation and Migration]]).

## Related documents
- [[Egg Storage]]
- [[Module - Egg Vault]]
- [[Cost Tables]]
- [[Monetisation Principles]]
- [[Monetisation Product Concepts]]
- [[UI - Egg Storage]]
- [[Economy and Monetisation Index]]
