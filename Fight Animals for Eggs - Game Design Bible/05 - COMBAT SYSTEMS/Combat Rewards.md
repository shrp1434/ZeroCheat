---
title: Combat Rewards
type: system
category: combat
status: mixed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - rewards
  - economy
  - cash
---

# Combat Rewards

What players earn from fighting, who earns it, and when. The wider economy (sinks, inflation, pricing) is owned by [[Economy Overview]] and [[Wild Animal Cash Rewards]]; this page defines the combat side of the hand-off.

> [!success] CONFIRMED
> - Defeating wild animals earns Cash; Cash buys egg rolls (D-014).
> - Defeating wild animals registers them in the index, which distinguishes discovered from owned (D-029).

> [!warning] UNDECIDED
> - Boss rewards ([[Open Questions#Q-015]]).
> - Whether wild animals drop eggs directly (Q-202, new).

> [!info] PROPOSED
> Formulas and values from [[Canonical Proposed Values]] §5–§6 and D-040. New values are marked *(new)*.

## Reward types from combat

| Reward | Source | Status |
|---|---|---|
| Cash | Wild animal defeats | **CONFIRMED** source; amounts **PROPOSED** |
| Player XP | Wild animal defeats; bosses (amount part of Q-015) | **PROPOSED** |
| Index discovery | First defeat of a species (D-029) | **CONFIRMED** |
| Progression Score | Indirect: level, discoveries, unique boss defeats ([[Progression Score Specification]]) | **PROPOSED** |
| Boss rewards | Mini-bosses, world bosses | **UNDECIDED** (Q-015) |
| Animal XP | None. Animals do not level individually (D-042) | **PROPOSED** ([[Open Questions#Q-021]]) |

## Cash and XP formulas

```
Cash = BaseCash(rarity) × RegionMultiplier × (1 + CashBonuses)
XP   = BaseXP(rarity)   × RegionMultiplier
```

| Rarity | Base Cash | Base XP | Respawn |
|---|---:|---:|---|
| Common | 10 | 10 | 20 s |
| Uncommon | 16 | 15 | 35 s |
| Rare | 28 | 25 | 60 s |
| Epic | 50 | 45 | 120 s |
| Legendary | 95 | 80 | 300 s, 50% chance per window |
| Mythical | 190 | 150 | 900 s window, 25% chance, announced |
| Secret | 400 | 300 | 2,700 s window, 10% chance, announced |

`CashBonuses` (additive): [[Module - Multiplier Shrine]] +10% per level (max +50%) and [[Module - Trophy Hall]] +1% per unique boss trophy (max +12%). Full list in [[Progression Multipliers]].

### Examples

| Defeat | Calculation | Cash | XP |
|---|---|---:|---:|
| Wild Common, Whisperwood, no bonuses | 10 × 1.0 × 1.00 | 10 | 10 |
| Wild Rare, Coral Coast, Shrine L3 | 28 × 3.2 × 1.30 = 116.48 | 116 | 80 |
| Wild Common, Starfall, Shrine L5 + 12 trophies | 10 × 11.5 × 1.62 = 186.3 | 186 | 115 |
| Wild Mythical, Starfall, Shrine L5 + 12 trophies | 190 × 11.5 × 1.62 = 3,539.7 | 3,539 | 1,725 |

Rounding: Cash is rounded down to an integer at award time *(new)*.

### Earning pace (illustrative)
With worked example 1 in [[Damage, Defence and Health Model]] (TTK 4.5 s) and about 6 s of travel between spawns *(assumption)*, a new player defeats about 5.7 wild Commons per minute: **≈ 57 Cash/min**, one 200-Cash egg roll every **≈ 3.5 min**. An endgame player farming Starfall Commons (TTK 4.6 s, same travel) earns about **1,050 Cash/min** with full bonuses. These figures feed [[Expected Value Calculations]] and [[Progression Bottleneck Analysis]]; the economy owner validates them.

## Kill credit (D-040, PROPOSED)

- Every player who dealt **at least 10% of the target's max HP**, directly or through their animals, within the combat-tag window, receives the **full** reward.
- Damage from a player's companions counts as that player's damage.
- Healing and tanking do not count for wild animal credit (they do for world bosses; see [[Boss AI#Participation and credit]]).
- Damage dealt before the animal reset (leash) is discarded.
- Up to 10 players can qualify for one wild animal (10 × 10%). In practice it is rarely more than 3–4.

Full multiplayer rules, including anti-abuse, are in [[Multiplayer Combat Rules]].

## Index registration
- A species is registered as **discovered** for every player who earns kill credit on it (D-029).
- Boss adds count for discovery but give no Cash or XP ([[Boss AI]]).
- Discovery adds to the Progression Score (3 points per species, canonical §8). The [[Animal Index Feature Specification]] owns the display.

## What gives no reward *(new)*

| Case | Reason |
|---|---|
| Wild animal that reset | Anti-farming; damage is discarded on reset |
| Boss adds | Prevents stalling bosses to farm |
| Damage from outside a boss arena | Anti-cheese ([[Boss AI]]) |
| Defeating players in PvP | Rewards come from the PvP reward table, never from the loser ([[PvP System]]) |
| Knocking out raid defenders | Theft is the raid reward; no Cash per KO ([[Raid Rewards and Defender Compensation]]) |

## Boss rewards

> [!warning] UNDECIDED (Q-015)
> What mini-bosses and world bosses award is undecided. Combat guarantees only the delivery rules: once per eligible player per spawn (canonical §5), eligibility as in [[Boss AI#Participation and credit]], and a unique-boss defeat counts for the Progression Score (10 points per mini-boss, 20 per world boss, canonical §8). Options are documented in [[Boss Rewards]].

## Egg drops from wild animals

> [!warning] UNDECIDED (Q-202)
> **Should wild animals ever drop eggs directly?** The confirmed loop is Cash → egg roll (D-014). Options: (1) Cash only (current proposal); (2) rare Common-egg drops from wild Commons; (3) egg drops only from Mythical and Secret rare spawns. Drops would affect storage pressure ([[Egg Storage]]), raid stakes and odds disclosure (D-017). **Recommendation (PROPOSED, unapproved):** option 1 at launch; it keeps one clear path to eggs with disclosed odds.

## Delivery and integrity
- Rewards are granted by the server in [[Service - EconomyService]] when `CombatService` emits a `Defeated` event with a unique defeat ID. Grants are idempotent on that ID ([[Data Consistency and Transactions]]).
- Rate sanity check: if a player's Cash per minute exceeds 3 × the theoretical maximum for their region and bonuses, flag for review *(new)* ([[Inflation and Farming Exploit Risks]]).
- Feedback: floating "+Cash" text and an XP tick on the HUD ([[Combat Feedback and Readability]]).

## Test hooks
- Two players each deal 15%: both receive full Cash. A third who dealt 9% receives nothing.
- Wild Rare in Coral Coast with Shrine L3 awards exactly 116 Cash (116.48 rounded down).
- A defeat event replayed twice grants once.
- Cases in [[Test Cases - Combat]] and [[Test Cases - Multiplayer]].

## Related documents
- [[Wild Animal Cash Rewards]]
- [[Cash Sources and Sinks]]
- [[Boss Rewards]]
- [[Multiplayer Combat Rules]]
- [[Animal Index Feature Specification]]
- [[Inflation and Farming Exploit Risks]]
- [[Service - EconomyService]]
