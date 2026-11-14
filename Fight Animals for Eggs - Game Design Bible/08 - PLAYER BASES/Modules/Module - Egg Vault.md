---
title: Module - Egg Vault
type: system
category: base
status: mixed
priority: P0
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - eggs
  - storage
  - raiding
---

# Module - Egg Vault

**Asset ID:** MOD-02 (**PROPOSED**). **Slot:** fixed, rear centre of the plot (does not use a flexible slot).

> [!success] CONFIRMED
> Base storage starts at **50** eggs (backpack 10, total **60**). Base-stored eggs can be stolen during an eligible raid. Backpack eggs can never be stolen. Extra space is purchasable; its currency and price are **UNDECIDED** ([[Open Questions#Q-009]], [[Open Questions#Q-010]]).

> [!warning] UNDECIDED
> - Egg theft limit per raid: **UNDECIDED** ([[Open Questions#Q-013]]). The vault never changes this limit.
> - Whether the 50 slots exist before the vault is built (the L0 Egg Crate interpretation): **UNDECIDED** (Q-409).

## 1. Purpose

The physical home of base-stored eggs. It shows the player's stash, provides the theft interaction point in raids and slows thieves down. **Vault levels change security and visuals only. Capacity expansion is a separate purchase** ([[Storage Expansion Economics]], [[Egg Storage]]).

## 2. Footprint and appearance

| Property | Proposal |
|---|---|
| Footprint | 24 × 24 studs, fixed at the rear centre, entrance facing the Base Core |
| Height | 6 studs (L0 crate) to 18 studs (L5 dome) |
| Appearance | A nest-themed treasure store: eggs are visible on shelves or in nests, glowing in their rarity colours ([[Rarity Visual Language]]) |
| Materials | L0 straw and crates; L1 timber; L2–L3 stone and brass; L4 crystal; L5 gold filigree dome |

### Egg display

Showing up to 200 individual egg models is unnecessary. The vault shows **one representative egg per rarity** held, with a stack height and a count badge; the full list is in [[UI - Egg Storage]]. This keeps the vault to ≤ 7 egg models (**PROPOSED**).

## 3. Upgrade levels

| Level | Name (PROPOSED) | Cost (Cash) | Theft channel multiplier (PROPOSED) | Extra security (PROPOSED) | Visual change |
|---:|---|---:|---:|---|---|
| L0 | Egg Crate | 0 (starter) | ×1.00 | None | Straw crates under a tarp |
| L1 | Timber Egg Store | 1,500 | ×1.10 | Door that raiders must open (1.0 s channel) | Log cabin with nest shelves |
| L2 | Stonebound Egg Store | 3,750 | ×1.20 | Owner alert when a raider enters the vault | Stone walls, iron-banded door |
| L3 | Brass-Lock Vault | 9,375 | ×1.35 | Vault seal: 6 s lockout after each successful egg theft | Brass dial door, lanterns |
| L4 | Crystal Vault | 23,438 | ×1.50 | Shimmer field: raider walk speed −20% inside the vault | Crystal panels, violet glow |
| L5 | Golden Nest Dome | 58,594 | ×1.75 | Guardian pulse: knock-back on the first channel start every 30 s | Gold dome with orbiting light motes |

Total L1–L5: **96,657 Cash**.

The **theft channel time** is `BaseEggChannel × VaultMultiplier × RarityFactor`. `BaseEggChannel` and `RarityFactor` are owned by [[Egg Theft Rules]] and must be configurable, because raid duration is **UNDECIDED** ([[Open Questions#Q-012]]).

> [!info] PROPOSED design intent
> The vault makes each theft slower and noisier. It never caps the number of eggs (Q-013) and never hides eggs. A max-level vault should roughly halve the eggs a raider can take in a given time compared with L0 when combined with guards and the perimeter ([[Base Defence Overview]]).

## 4. Functionality

| Function | Proposal |
|---|---|
| Storage | Holds base storage capacity (50 start, +25 per expansion step up to 200, **PROPOSED**; currency **UNDECIDED**) |
| Deposit and withdraw | Free and instant from inside the plot; blocked during an active raid on this base |
| Hatch from storage | Base-stored eggs hatch only at the base ([[Hatch System]]) |
| Merge input and output | The [[Egg Merging Station]] reads inputs from storage or backpack and writes output to storage |
| Progression Score | L1–L5 count towards the 44 base levels (L0 counts as 0) |

### Edge case: storage full

If base storage is full, a merge still succeeds because 3 inputs leave and 1 output arrives (net −2). Rolls cannot be sent to a full storage; they go to the backpack, and if both are full the roll is blocked before payment ([[Egg Roll System]]).

## 5. Dependencies

- None to build. Expansion steps are independent of vault level (**PROPOSED**).
- Level cap `PlotStage + 1` applies.

## 6. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.EggVault = { level }`; eggs live in the egg inventory ([[Schema - Egg Inventory]]), not in the module |
| Instances | `Plot_##.Modules.EggVault` with `Door` (ProximityPrompt), `Display` (7 egg anchors), `TheftPoint` attachment |
| Replication | Attribute `EggCounts` (JSON-free compact string such as `"12,4,2,1,0,0,0"`) updated on change; the client builds the display |
| Streaming | Atomic module streaming; display eggs are client-built |
| Security | The theft prompt is created by the server only for active raiders; every theft is re-validated by the raid session ([[Raid Anti-Exploit Validation]]) |

```lua
-- Illustrative Luau (not executed)
local VAULT_CHANNEL_MULT = { [0] = 1.00, 1.10, 1.20, 1.35, 1.50, 1.75 }

local function getEggTheftChannel(vaultLevel: number, rarityIndex: number, theftConfig): number
	local base = theftConfig.baseEggChannel      -- owned by Egg Theft Rules, configurable
	local rarityFactor = theftConfig.rarityFactor[rarityIndex]
	return base * VAULT_CHANNEL_MULT[vaultLevel] * rarityFactor
end
```

## 7. Animation and VFX

- Deposit: egg arcs from the player into its rarity nest with a soft chime ([[Sound - Eggs]]).
- Upgrade: the old shell "hatches" open and the new vault rises from inside (an egg metaphor; [[Animation - Base Upgrades]]).
- Raid: door alarm glow, red-to-amber light sweep when a raider is inside; vault seal (L3+) shows a closing iris ([[Animation - Raid Interactions]]).

## 8. Raid interaction

| Situation | Behaviour |
|---|---|
| Raider reaches the vault | Must open the door (L1+), then channel each egg theft |
| Channel interrupted by damage | Channel cancelled, progress lost (**PROPOSED**) |
| Owner deposits during a raid | Blocked. Eggs already in the backpack stay safe |
| Owner withdraws during a raid | Blocked, so a defender cannot "evacuate" the vault into the backpack at the last moment (**PROPOSED**) |
| Theft limit | Per [[Egg Theft Rules]] and **UNDECIDED** Q-013 |
| Module damage | None |

## Related documents
- [[Egg Storage]]
- [[Storage Expansion Economics]]
- [[Egg Theft Rules]]
- [[Base Defence Overview]]
- [[UI - Egg Storage]]
- [[Schema - Egg Inventory]]
- [[Cost Tables]]
- [[Player Bases Index]]
