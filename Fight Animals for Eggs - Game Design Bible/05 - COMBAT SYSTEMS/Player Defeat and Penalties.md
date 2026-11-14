---
title: Player Defeat and Penalties
type: system
category: combat
status: mixed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - defeat
  - penalties
  - pvp
  - raids
---

# Player Defeat and Penalties

What happens when the player reaches 0 HP, for each type of battle.

> [!success] CONFIRMED
> The defeat penalty system is **mixed**: consequences differ by battle type (D-013).

> [!warning] UNDECIDED (Q-014)
> **The exact penalties are undecided** ([[Open Questions#Q-014]]). Every rule set below is an **unapproved PROPOSED** option list with a labelled recommendation. Nothing on this page may be implemented as final without an owner decision recorded in the [[Decision Register]].

## Principles behind every recommendation (PROPOSED)

1. **Defeat costs time, not possessions, in PvE.** No eggs, animals or ascension progress are lost outside base raids. Options that break this are listed only for completeness and are marked **not recommended**.
2. **Backpack eggs are never at risk** in any battle type (D-021).
3. **Animals are lost only through raid theft rules**: knocked out first, at most three per successful raid (D-024). See [[Animal Theft Rules]].
4. **Penalties scale with consent.** Wild fights happen constantly and must be forgiving; PvP and raids are opt-in and may carry more stakes.
5. **No penalty should push a player into a loop of repeated defeat** (for example, losing Cash needed to recover).

## Common defeat sequence (PROPOSED)

| Step | Rule *(new values)* |
|---|---|
| 1. 0 HP | Player enters `Defeated` (or `Downed` in world boss fights, see below). Companions disengage and become untargetable. |
| 2. Defeat screen | 5 s respawn delay (10 s at a world boss rally point) with a short "what hit you" summary ([[Combat Feedback and Readability]]). |
| 3. Respawn | Location depends on battle type. HP restored to 100%. |
| 4. Companions | All three companions are restored to full HP, including any that were knocked out. |
| 5. Spawn protection | 3 s invulnerability, ended early by attacking. |
| 6. Cooldowns | Player specials and animal abilities reset. |

## Rule set 1: ordinary wild encounters

> [!info] PROPOSED, unapproved (Q-014)

| Option | Rule | Pros | Cons |
|---|---|---|---|
| **W-A** | No material loss. Respawn at the region's nearest respawn point. | Friendly for a young audience; supports a free-to-play loop | Little tension |
| W-B | W-A plus a 60 s "Weary" debuff: −10% damage dealt | Mild tension; costs nothing permanent | Can snowball if the player re-engages immediately |
| W-C | Lose 5% of Cash on hand, capped at the Cash earned in the last 10 minutes | Real stakes | Punishes saving for egg rolls; feels bad on mobile disconnect-deaths; encourages hoarding before fights |
| W-D (**not recommended**) | Lose one random backpack egg | High stakes | Contradicts the spirit of D-021 (backpack is the safe store); would push players to keep eggs out of the backpack; deeply frustrating |

**Recommendation (PROPOSED, unapproved): W-A.**
Rationale: defeat in the wild already costs the walk back and the lost fight. Wild fights are the main Cash source (D-014), so any Cash penalty taxes the core loop. Respawn time and distance are enough to make positioning and dodging matter.

## Rule set 2: mini-boss encounters

> [!info] PROPOSED, unapproved (Q-014)

| Option | Rule | Pros | Cons |
|---|---|---|---|
| M-A | Respawn outside the arena entrance. The boss keeps fighting other participants; if nobody is left it resets ([[Boss AI]]). | Simple; co-operative | Solo players can retry instantly, so a fight can be "chipped" with repeated attempts (mitigated: bosses reset to full HP) |
| **M-B** | M-A plus a 30 s re-entry lockout after a **full wipe** only | Encourages learning the fight; stops spam retries; does not punish a player whose group is still fighting | One more timer to communicate |
| M-C | Entry fee in Cash, lost on defeat | Stakes | Taxes progression gates; harms players stuck on a gate |
| M-D | Lose a share of Cash on hand | Stakes | Same problems as W-C, worse at a progression gate |

**Recommendation (PROPOSED, unapproved): M-B.**
Rationale: mini-bosses gate region unlocks ([[Region Unlock Progression]]); a penalty that costs Cash would slow the players who are already stuck. A short lockout after a wipe gives a moment to reflect and prevents a server-visible retry spam.

## Rule set 3: world bosses

> [!info] PROPOSED, unapproved (Q-014)

| Option | Rule | Pros | Cons |
|---|---|---|---|
| **B-A** | **Downed** first: 15 s bleed-out, ally revive in 3 s (30% HP). If defeated, respawn at the event rally point after 10 s and rejoin. Contribution is kept. | Social; reviving is co-operative play | Slightly more complex |
| B-B | Defeated players cannot rejoin this spawn | Tension | Spawns are 45–60 min apart (canonical §5); losing a whole event to one mistake is harsh |
| B-C | Contribution decays by 25% per defeat | Rewards survival | Hard to explain; punishes Tanks most |

**Recommendation (PROPOSED, unapproved): B-A.**
Rationale: world bosses are social events. Revives create co-operative moments and the rally-point respawn keeps everyone involved. Reward eligibility already requires contribution ([[Boss AI#Participation and credit]]), so there is no free ride.

## Rule set 4: PvP

> [!info] PROPOSED, unapproved (Q-014). PvP activation is also **UNDECIDED** ([[Open Questions#Q-011]]).

| Option | Rule | Pros | Cons |
|---|---|---|---|
| **P-A** | No material loss. Loss counts in rating (where ratings exist). Respawn depends on context: duel ends with both restored on the spot; arena respawn at the arena; open-world PvP respawn at the region respawn point with 5 s PvP spawn protection. | No griefing incentive; easy to opt in | Lower stakes |
| P-B | Consensual Cash wagers on duels | Stakes for those who want them | Encourages scams and pressure on young players; policy review needed (*unverified*); not recommended at launch |
| P-C | Loser drops a share of Cash to the winner | Stakes | Rewards preying on weaker players; contradicts PvP safeguards in [[PvP System]] |
| P-D (**not recommended**) | Loser loses an egg or animal | Maximum stakes | Turns optional PvP into a raid without raid protections; breaks principle 1 |

**Recommendation (PROPOSED, unapproved): P-A.**
Rationale: PvP is optional (D-023). Material losses would discourage opting in and create griefing incentives. Rewards for winning come from the system, never from the loser ([[PvP System]]).

## Rule set 5: base raids

> [!info] PROPOSED, unapproved (Q-014). Raid duration is **UNDECIDED** ([[Open Questions#Q-012]]).

Raids are the **only** battle type where possessions can change hands, and only through [[Egg Theft Rules]] and [[Animal Theft Rules]]. Defeat itself never removes anything.

### Attacker defeated

| Option | Rule | Pros | Cons |
|---|---|---|---|
| **RA-A** | Defeat ends the attacker's raid. Eggs being carried (not yet delivered to the extraction point) drop and return to the vault. Items already secured stay secured. The raid resolves as described in [[Raid Lifecycle and States]]. The attacker respawns at the hub. | Clear, decisive defending | Short raids when the defence is strong |
| RA-B | One re-entry per raid after 10 s; carried eggs still drop | More attacker agency | Longer raids; more server state; more complex to explain |
| RA-C | Attacker also loses Cash | Deters raid spam | Cooldowns already do this; adds a currency drain to an optional mode |

**Recommendation (PROPOSED, unapproved): RA-A.** Defenders need a clear win condition, and "defeat the raider" is the most readable one.

### Defender defeated

| Option | Rule | Pros | Cons |
|---|---|---|---|
| **RD-A** | Respawn at the base's defender spawn after 5 s and keep defending. No extra loss. | Defending stays possible; nobody loses more for being outmatched | Weak defenders can be farmed for KOs (no reward attached to defender KOs, see [[Raid Rewards and Defender Compensation]]) |
| RD-B | Respawn after 15 s | Gives attackers a window | Feels helpless |
| RD-C | Defender defeat ends the raid as an attacker success | Short raids | Removes the defence; contradicts the "undefeated defenders cannot be stolen" spirit |

**Recommendation (PROPOSED, unapproved): RD-A.**

Defender **animals** that are knocked out stay down for the rest of the raid and may be captured ([[Animal Theft Rules]]). That is a theft rule, not a defeat penalty.

## Summary matrix (all PROPOSED, unapproved)

| Battle type | Recommended option | Material loss | Respawn |
|---|---|---|---|
| Wild | W-A | None | Region respawn point, 5 s |
| Mini-boss | M-B | None | Arena entrance; 30 s lockout after a full wipe |
| World boss | B-A | None | Downed then rally point, 10 s |
| PvP | P-A | None | Context-dependent |
| Raid (attacker) | RA-A | None from inventory; unsecured carried eggs return | Hub |
| Raid (defender) | RD-A | Only theft rules apply | Base defender spawn, 5 s |

## Implementation notes
- The rule set is chosen by the server from the battle context at the moment of defeat (`Wild`, `MiniBoss`, `WorldBoss`, `PvP`, `RaidAttacker`, `RaidDefender`). Store the choice as configuration so the owner's decision on Q-014 changes data, not code ([[Configuration Modules]]).
- Defeat events are logged for balancing: battle type, killer type, region, player level, time in fight ([[Service - AnalyticsAndLoggingService]]).

## Test hooks
- Wild defeat: Cash, backpack and base storage are byte-identical before and after.
- Raid attacker defeated while carrying an egg: the egg returns to the defender's vault and the attacker's inventory is unchanged.
- World boss: a downed player revived within 15 s keeps contribution.
- Cases in [[Test Cases - Combat]], [[Test Cases - PvP]] and [[Test Cases - Raiding]].

## Related documents
- [[Combat States and State Machine]]
- [[Boss AI]]
- [[PvP System]]
- [[Base Raiding System]]
- [[Raid Lifecycle and States]]
- [[Egg Theft Rules]]
- [[Animal Theft Rules]]
- [[Design Principles and Fairness Charter]]
- [[Open Questions]]
