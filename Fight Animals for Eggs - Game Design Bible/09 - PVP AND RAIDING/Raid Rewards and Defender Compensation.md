---
title: Raid Rewards and Defender Compensation
type: system
category: pvp-and-raiding
status: mixed
priority: P1
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - raids
  - rewards
  - compensation
  - economy
---

# Raid Rewards and Defender Compensation

What each side gains or keeps after a raid, and how a defender who loses something is supported. Economy-wide effects are owned by [[Economy Overview]] and [[Inflation and Farming Exploit Risks]].

> [!success] CONFIRMED
> Base eggs can be stolen; knocked-out defenders can be stolen, at most three per successful raid; offline bases cannot be raided (D-024). Backpack eggs are never stolen (D-021).

> [!warning] UNDECIDED
> - Egg theft limit ([[Open Questions#Q-013]]) and raid duration ([[Open Questions#Q-012]]) shape how much can be gained.
> - What stolen animals keep ([[Open Questions#Q-025]]).
> - Defender compensation model (Q-210, new): options below.

> [!info] PROPOSED
> Everything else is a proposal. New values are marked *(new)*.

## Attacker outcomes (PROPOSED)

| Outcome | Attacker receives |
|---|---|
| `Succeeded` | Every **secured** egg (already in their base storage) and up to **three** held animals ([[Animal Theft Rules]]). A raid record and raid statistics. |
| `Failed` | Nothing. No Cash cost; the attacker cooldown (900 s) applies. |
| `Cancelled` or `Voided` | Nothing beyond eggs that were securely committed before the event. |

Design choices:
- **No Cash is stolen** and no Cash is paid per knock-out or per structure destroyed *(new)*. Theft of eggs and animals is the reward; adding Cash would make raids the best farming method and pressure the wild-combat loop (D-014).
- Optional cosmetic raid trophies may be displayed in the [[Module - Trophy Hall]]; they give no stat or Cash bonus *(new)*. (Trophy Hall Cash bonuses are for boss trophies only, canonical §12.)

## Defender outcomes (PROPOSED)

### Defence win
A **defence win** is a raid that ends `Failed` with reason `AttackerDefeated` or `Timeout`, where the defender's guards, structures or the defender personally dealt damage to the attacker or their companions (the "resistance" check, [[Raid Anti-Exploit Validation#Collusion and alt-account defences]]).

| Reward | Value *(new)* |
|---|---|
| Defence-win Cash | `DefenceWinCash = 200 × RegionMultiplier` of the defender's highest unlocked region (for example 200 in Whisperwood Forest, 1,500 in Frostfang Tundra, 2,300 in Starfall Sanctuary), from the system, not from the attacker |
| Shield | Post-raid shield of 1,800 s ([[Shield Mechanics]]) |
| Repair | All structures restored free ([[Raid Lifecycle and States]]) |
| Record | Defence statistics on the base sign |

### After any raid that reached `Active`
- Post-raid shield (1,800 s after a failed raid, 3,600 s after a successful one).
- Free structure repair; knocked-out guards that were not captured recover.
- A raid summary listing exactly what was lost and when ([[UI - Notifications]]).

## Defender compensation for losses (Q-210)

> [!warning] UNDECIDED (Q-210)
> **Should defenders be compensated for stolen eggs and animals, and how?** Compensation softens loss for a mostly young audience but injects system-funded value, which can be farmed through collusion.

### Reference value used by the options *(new)*
`EggReferenceValue(r) = 200 × 3^r` Cash, where `r` is the rarity index (Common 0 to Secret 6). It is the egg-roll price (canonical §7) times the number of Common eggs that three-into-one merging (D-020) needs to build one egg of that rarity, ignoring merge fees.

| Rarity | Index | EggReferenceValue | 25% compensation |
|---|---:|---:|---:|
| Common | 0 | 200 | 50 |
| Uncommon | 1 | 600 | 150 |
| Rare | 2 | 1,800 | 450 |
| Epic | 3 | 5,400 | 1,350 |
| Legendary | 4 | 16,200 | 4,050 |
| Mythical | 5 | 48,600 | 12,150 |
| Secret | 6 | 145,800 | 36,450 |

### Options

| Option | Rule | Pros | Cons |
|---|---|---|---|
| C-A. None | Shield, repair and summary only | No inflation; theft has weight | Harsh for young players who lose a rare animal |
| **C-B. Partial Cash** | 25% of `EggReferenceValue` per stolen egg (by egg rarity) and per stolen animal (by animal rarity), from the system | Softens losses; readable | System Cash enters the economy; must be gated against collusion |
| C-C. Replacement egg | One free egg of the lowest stolen rarity, once per day | Feels generous | Creates eggs from nothing; interacts with odds disclosure (D-017) |
| C-D. Revenge raid | Defender may raid the attacker once within 24 h, ignoring the pair cooldown and matchmaking band, but not offline protection or shields | Satisfying; player-driven | Encourages feuds; harder to moderate |

**Recommendation (PROPOSED, unapproved): C-B,** paid only when the raid passes the resistance check and no collusion flag is raised, and capped by the existing `MaxRaidsReceivedPerDay` (3). Do not ship C-C or C-D at launch.

Rationale: partial Cash lets a defender rebuild towards what they lost (for example re-rolling or merging) without making loss meaningless. Paying 25% means compensation is always worth much less than the stolen item, so colluding pairs lose value overall: the attacker gains 100% of the item and the defender 25% back in Cash, but the item itself was already owned by the pair, so the net gain from a staged raid is 25% of the reference value per item. The resistance check, pair cooldown and pattern flags in [[Raid Anti-Exploit Validation]] are designed to stop that residual gain. The economy owner should still model it in [[Expected Value Calculations]].

> [!danger] Inflation check required
> Option C-B injects Cash. Before approval, [[Inflation and Farming Exploit Risks]] must estimate the worst-case Cash injected per player per day (three compensated raids with the maximum theft allowed by `MaxEggsStolenPerRaid` and three animals each). That estimate cannot be made until Q-013 is decided.

## Summary table

| Party | Succeeded | Failed (defence win) | Failed (no resistance) | Cancelled |
|---|---|---|---|---|
| Attacker | Secured eggs + up to 3 animals | Nothing; cooldown | Nothing; cooldown | Nothing |
| Defender | Shield 3,600 s, repair, compensation (if C-B approved) | Shield 1,800 s, repair, `DefenceWinCash` | Shield 1,800 s, repair | Nothing |

## Test hooks
- Defence win in Frostfang Tundra pays exactly 1,500 Cash (200 × 4.5) once.
- A failed raid in which no defender damage was dealt pays no defence-win Cash.
- With C-B enabled in a test build: a stolen Rare egg pays 450 Cash compensation; a flagged pair pays nothing.
- Attacker never receives Cash from a raid.
- Cases in [[Test Cases - Raiding]].

## Related documents
- [[Base Raiding System]]
- [[Egg Theft Rules]]
- [[Animal Theft Rules]]
- [[Shield Mechanics]]
- [[Raid Anti-Exploit Validation]]
- [[Cash Sources and Sinks]]
- [[Inflation and Farming Exploit Risks]]
- [[Expected Value Calculations]]
- [[Egg Merging]]
