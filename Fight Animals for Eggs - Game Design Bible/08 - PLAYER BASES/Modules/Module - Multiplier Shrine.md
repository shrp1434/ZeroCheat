---
title: Module - Multiplier Shrine
type: system
category: base
status: proposed
priority: P1
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - economy
  - multipliers
---

# Module - Multiplier Shrine

**Asset ID:** MOD-06 (**PROPOSED**). **Slot:** flexible.

> [!info] PROPOSED
> +10% Cash per level ([[Canonical Proposed Values]] §12). At L5: **+50% Cash**. Module availability is **UNDECIDED** ([[Open Questions#Q-007]]).

## 1. Purpose

The base's income module and the clearest early investment. It is how base progression "contributes to multipliers" (D-022). It is also the most expensive module (base cost 3,000), because every point of Cash bonus compounds into every other purchase.

## 2. Footprint and appearance

| Property | Proposal |
|---|---|
| Footprint | 16 × 16 studs, 8 tall (L1) to 22 tall (L5) |
| Appearance | A stone cairn with an offering bowl that grows into a golden sun shrine; coins and leaves drift upward from the bowl |
| Materials | Rough stone, moss, then carved stone, brass bowls, crystal lenses, gold leaf |

## 3. Upgrade levels

| Level | Cost (Cash) | Cash bonus | Payback at Region 1 income | Payback at Region 4 income | Visual change |
|---:|---:|---:|---:|---:|---|
| L1 | 3,000 | +10% | 5.9 h | 1.6 h | Mossy cairn with a clay bowl |
| L2 | 7,500 | +20% | 14.7 h | 3.9 h | Carved stone, two brass braziers |
| L3 | 18,750 | +30% | 36.9 h | 9.7 h | Crystal lens focusing a sunbeam into the bowl |
| L4 | 46,875 | +40% | 92.2 h | 24.4 h | Tiered terraces, floating coin ring |
| L5 | 117,188 | +50% | 230.4 h | 60.9 h | Golden sun disc with a slow-orbiting coin halo |

Total: **193,313 Cash**. Payback = level cost ÷ (10% of raw hourly income); income assumptions are in [[Wild Animal Cash Rewards]]. At Starfall Sanctuary income the L5 step pays back in about 19 hours.

### Stacking

`Cash = BaseCash × RegionMultiplier × (1 + CashBonuses)`. The shrine's bonus is **additive** with the [[Module - Trophy Hall]] bonus (max +12%) inside `CashBonuses`. Maximum base-derived cash bonus: **+62%**. See [[Progression Multipliers]].

> [!info] PROPOSED scope of the bonus
> Applies to Cash from defeating wild animals, mini-bosses and world bosses. Does **not** apply to raid rewards, refunds, compensation or any future event grants. This keeps the bonus from amplifying raid feeding (see [[Inflation and Farming Exploit Risks]]).

## 4. Functionality

| Function | Proposal |
|---|---|
| Passive bonus | Always on, wherever the player is |
| Readout | The shrine shows the player's current total Cash multiplier on a floating plaque |
| Progression Score | Levels count towards the 44 base levels |

## 5. Dependencies

- Free slot; level cap `PlotStage + 1`. Because L2 needs Stage 1 (5,000), the realistic early sequence is Shrine L1 → Plot Stage 1 → Shrine L2 (see [[Progression Bottleneck Analysis]]).

## 6. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.MultiplierShrine = { level, slot }` |
| Effect | [[Service - EconomyService]] reads a cached `cashBonus` per player, rebuilt on upgrade, trophy change or config change |
| Instances | `Plot_##.Modules.MultiplierShrine` with `Plaque` (SurfaceGui text set by the client from an attribute) |
| Streaming | Atomic module; coin particles are a client ParticleEmitter enabled only when within 80 studs |

```lua
-- Illustrative Luau (not executed)
local function computeCashBonus(base): number
	local shrine = (base.modules.MultiplierShrine and base.modules.MultiplierShrine.level) or 0
	local trophies = math.min(#base.displayedTrophies, 12)
	return 0.10 * shrine + 0.01 * trophies -- additive, max 0.62
end

local function cashForKill(baseCash: number, regionMult: number, bonus: number): number
	return math.floor(baseCash * regionMult * (1 + bonus) + 0.5)
end
```

## 7. Animation and VFX

- Upgrade: the shrine rises in tiers, each tier landing with a coin chime ([[Animation - Base Upgrades]], [[Sound - UI Feedback]]).
- Ambient: coins drift up and fade; at L5 a soft god-ray ([[VFX - Environment Ambient Effects]]).
- Kill feedback in the world: Cash pop-ups show the bonus as a second gold number (for example "+28 +14") so the shrine's value is felt in play ([[Combat Feedback and Readability]]).

## 8. Raid interaction

None. The shrine cannot be stolen, damaged or disabled, and raids do not affect the bonus (**PROPOSED**; Q-403 covers temporary disabling in general).

## Related documents
- [[Progression Multipliers]]
- [[Cash Sources and Sinks]]
- [[Wild Animal Cash Rewards]]
- [[Module - Trophy Hall]]
- [[Cost Tables]]
- [[Player Bases Index]]
