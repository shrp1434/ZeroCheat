---
title: Boss Rewards
type: analysis
category: economy
status: undecided
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - economy
  - bosses
  - rewards
---

# Boss Rewards

> [!warning] UNDECIDED
> Exact boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]). This page lists option sets, guardrails and a **labelled recommendation**. No option here is final, and no number here may ship without an owner decision.

> [!success] CONFIRMED context
> Mini-bosses and world bosses exist (D-012). Defeat penalties are mixed by battle type and their values are **UNDECIDED** ([[Open Questions#Q-014]]).

**Spawn context (PROPOSED, [[Canonical Proposed Values]] §5):** mini-bosses respawn every 10 minutes per server; reward eligibility is once per player per spawn. World bosses appear every 45–60 minutes per server, announced 2 minutes ahead. Boss design is in [[Boss Design Overview]].

## 1. Guardrails any option must meet (PROPOSED)

1. **No camping dominance.** A player who kills every mini-boss spawn in their region for an hour must not earn more than **+30%** Cash compared with an hour of ordinary farming in the same region.
2. **First kills matter most.** The biggest reward should come from the first defeat of each boss, because that is a progression milestone (region gates, Progression Score, Trophy Hall).
3. **No Robux interaction.** Boss rewards are never sold, boosted or skipped with Robux.
4. **Free random rewards still need disclosure.** If a reward includes an egg, its hatch odds are shown before the hatch as for any egg (D-017). If a reward includes a roll, the roll's odds are shown before the reward is claimed.
5. **Group-safe credit.** The canonical 10% damage threshold (D-040) cannot be met by more than 10 players at once. For bosses a lower threshold is needed (see §4).

## 2. Option sets

| Option | First defeat | Repeat defeats | Pros | Cons |
|---|---|---|---|---|
| A. Cash only | Cash | Cash | Simplest; feeds the single currency | Bosses feel like big wild animals; weak milestone |
| B. Cash + guaranteed egg | Cash + egg of a fixed rarity | Cash + chance of an egg | Strong excitement; fits the egg fantasy | Egg drops compete with rolls and merges; must be tuned with [[Expected Value Calculations]] |
| C. Cash + boss tokens | Cash + tokens | Cash + tokens | Tokens can buy boss cosmetics or decor; flexible for live ops | Second currency to explain and secure |
| D. Trophy + one-time bonus | Trophy for the [[Module - Trophy Hall]] + Cash bonus | Cash only | Clean milestone; feeds a CONFIRMED-style "base contributes to multipliers" loop | Repeats are plain |
| E. Cosmetic drop table | Cash + chance of a boss cosmetic | Same | Long-tail collection goal | Free random cosmetics need disclosure; content cost |

### Modelling values (for simulation only)

| Item | Modelling value | Derivation |
|---|---|---|
| Mini-boss Cash per defeat | `375 × RegionMultiplier` of its home region | 6 defeats per hour ≤ 45% of an hour's farming, so camping stays within +30% (§1.1) |
| World boss Cash per defeat | `1,000 × BandMultiplier` | ≈ 10 minutes of farming at the boss's recommended-level region |

| Boss | Home or band | Multiplier | Modelling Cash |
|---|---|---:|---:|
| [[Mini-Boss - Bramblehorn]] | Region 1 | 1.0 | 375 |
| [[Mini-Boss - Dustmane]] | Region 2 | 1.5 | 563 |
| [[Mini-Boss - Vinecoil]] | Region 3 | 2.2 | 825 |
| [[Mini-Boss - Hammertide]] | Region 4 | 3.2 | 1,200 |
| [[Mini-Boss - Rimeback]] | Region 5 | 4.5 | 1,688 |
| [[Mini-Boss - Stormtalon]] | Region 6 | 6.2 | 2,325 |
| [[Mini-Boss - Cinderjaw]] | Region 7 | 8.5 | 3,188 |
| [[Mini-Boss - Eclipse Panther]] | Region 8 | 11.5 | 4,313 |
| [[World Boss - Ironbark Colossus]] | Level 15 → Region 2 band | 1.5 | 1,500 |
| [[World Boss - Thunderhoof]] | Level 30 → Region 4 band | 3.2 | 3,200 |
| [[World Boss - Abyssal Leviathan]] | Level 45 → Region 5 band | 4.5 | 4,500 |
| [[World Boss - Ashwing Condor]] | Level 70 → Region 7 band | 8.5 | 8,500 |

Camping check (Region 1, modelling values): 6 Bramblehorn defeats (≈ 9 minutes of fighting) = 2,250 Cash, plus 51 minutes of farming ≈ 4,323, total ≈ 6,573 versus 5,086 for pure farming: **+29%**, inside the guardrail.

## 3. Recommendation (labelled PROPOSED, not a decision)

> [!info] PROPOSED recommendation: D + A, with a first-kill egg from B
> - **First defeat of each unique boss:** trophy (feeds the [[Module - Trophy Hall]]), a guaranteed egg, and Cash at 3× the repeat value.
>   - Mini-boss egg rarity: Rare (Regions 1–3), Epic (Regions 4–6), Legendary (Regions 7–8).
>   - World boss egg rarity: one tier above the mini-boss of its band.
> - **Repeat defeats:** Cash at the modelling scale above. World bosses additionally grant one free egg roll at the player's current disclosed odds.
> - **No boss tokens at launch** (avoids a second currency); revisit for live events ([[Seasonal and Limited-Time Events]]).
>
> Total first-kill value across all 12 bosses is modest relative to the economy (3 × 32,177 ≈ 96,500 Cash plus 12 eggs) but highly visible. Final decision: **UNDECIDED** ([[Open Questions#Q-015]]).

## 4. Credit and eligibility

| Rule | Proposal |
|---|---|
| Contribution threshold | Bosses use **2% of max HP** or **20 s of active combat within range** (whichever comes first), not 10%, so up to 16 players can all qualify (**PROPOSED** variation of D-040) |
| Once per spawn | Server-side set of UserIds per spawn instance |
| First-kill tracking | `unlocks.bossesDefeated[bossId] = timestamp` in [[Schema - Unlocks and Boss Progress]] |
| Server hopping for world bosses | Eligibility for world boss repeat rewards limited to one claim per boss per real-time spawn window across servers (MemoryStoreService key per user and boss, **PROPOSED**) |
| Defeat during the fight | Player remains eligible if they contributed before defeat; penalties per [[Player Defeat and Penalties]] |

```lua
-- Illustrative Luau (not executed)
local function isBossRewardEligible(boss, player: Player): boolean
	local record = boss.contributions[player.UserId]
	if not record then return false end
	local hpShare = record.damage / boss.maxHp
	return hpShare >= 0.02 or record.activeSeconds >= 20
end
```

## 5. Interactions

| System | Interaction |
|---|---|
| [[Progression Score Specification]] | Unique boss defeats already add PS (10 per mini-boss, 20 per world boss) |
| [[Region Unlock Progression]] | Mini-boss defeats gate regions; the reward must never be required for anything except the gate itself |
| [[Module - Multiplier Shrine]] | Shrine bonus applies to boss Cash (**PROPOSED**) |
| [[Inflation and Farming Exploit Risks]] | Camping, hopping and alt-assist risks |

## Related documents
- [[Boss Design Overview]]
- [[Combat Rewards]]
- [[Module - Trophy Hall]]
- [[Cash Sources and Sinks]]
- [[Expected Value Calculations]]
- [[Test Cases - Bosses]]
- [[Economy and Monetisation Index]]
