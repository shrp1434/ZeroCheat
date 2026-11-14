---
title: Test Cases - PvP
type: test-cases
category: qa
status: mixed
priority: P1
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - pvp
  - combat
---

# Test Cases - PvP

Test cases for optional player-versus-player combat outside raids. System documents: [[PvP System]], [[PvP Activation Options]], [[Multiplayer Combat Rules]], [[Service - PvPService]], [[UI - PvP Interface]]. Raids are covered in [[Test Cases - Raiding]].

> [!success] CONFIRMED rules under test
> PvP is optional; players choose whether to take part (D-023). Combat is real-time with the player and three animals (D-005, D-006). The team is locked away from base (D-010). Defeat penalties vary by battle type and are **UNDECIDED** (D-013).

> [!warning] UNDECIDED: PvP activation method ([[Open Questions#Q-011]])
> The options are documented in [[PvP Activation Options]]. Every case below tests the **server-side PvP state** (`PvPEnabled` for a player, or a PvP zone flag), not a particular activation method. When the owner decides Q-011, QA adds activation-specific cases (TC-PVP-001 to 004 are the placeholders) without changing the rest. PvP penalties ([[Open Questions#Q-014]]) are tested as configuration.

**Fixtures.** `QA_SetPvPState(player, enabled)`, `QA_ForceCombatTag(player, s)`, `QA_SetConfig("PvPPenalty", row)`, network simulation for latency.

## 1. Activation and consent

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PVP-001 | PvP is off by default | New player | 1) Join. 2) Read server PvP state. | `PvPEnabled = false` (or not in a PvP zone) for every new player, whatever the Q-011 method. | P0 | functional | D-023 |
| TC-PVP-002 | Enabling PvP requires the player's own action | Q-011 method implemented | 1) Enable via the chosen method. | State becomes enabled only after the player's explicit action; never enabled by another player, a party leader or a timer. | P0 | functional | D-023 |
| TC-PVP-003 | Disabling PvP | PvP enabled; not combat-tagged | 1) Disable. | State becomes disabled per the Q-011 method's rules. | P1 | functional | D-023 |
| TC-PVP-004 | Disabling PvP while in combat | PvP enabled; combat-tagged by a player | 1) Try to disable. | **PROPOSED**: blocked until the 8 s combat tag expires (prevents escaping a fight); the UI shows the countdown. | P1 | edge | D-023 |
| TC-PVP-005 | Clear PvP indicators | Mixed PvP states nearby | 1) Observe other players. | Each player's PvP state is clearly visible ([[UI - PvP Interface]], [[UI Accessibility Standards]]: not by colour alone). | P1 | functional | D-023 |

## 2. Damage legality

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PVP-010 | Non-PvP player cannot be harmed | A PvP on, B PvP off | 1) A attacks B with basic attacks, specials and commands A's animals at B. | B and B's animals take no damage; commands on B are rejected; A's animals never auto-target B. | P0 | functional | D-023 |
| TC-PVP-011 | Non-PvP player cannot harm PvP players | A PvP off, B PvP on | 1) A attacks B. | No damage either way (**PROPOSED**: PvP damage needs both players enabled). | P0 | functional | D-023 |
| TC-PVP-012 | Both PvP enabled | A and B PvP on | 1) Fight. | Damage follows the same formula as PvE (or a PvP modifier if one is defined in [[PvP System]]); both teams' animals engage. | P0 | functional | D-005 |
| TC-PVP-013 | Area attacks respect legality | A PvP on; B PvP on; C PvP off; all within 10 studs | 1) A uses Ground Slam. | B takes damage; C takes none. | P0 | edge | D-023 |
| TC-PVP-014 | PvP in the safe hub | Both PvP on, inside [[Hub - Hatchling Haven]] | 1) Attack. | No damage. | P1 | edge | D-025 |
| TC-PVP-015 | Crafted damage against a non-PvP player | Exploit client | 1) Fire hit requests targeting a non-PvP player. | Rejected; security log (TC-EXP-030). | P0 | security | D-023 |
| TC-PVP-016 | State change mid-fight | A and B fighting | 1) B's PvP state becomes disabled (after the tag expires). | From that moment no PvP damage applies; in-flight projectiles resolve against the new state. | P1 | edge | D-023 |

## 3. Outcomes and penalties

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PVP-020 | PvP defeat penalty from configuration | Penalty row for PvP configured (Q-014) | 1) B defeats A. | The configured PvP penalty applies exactly once to A; nothing else changes. With a "none" row, nothing changes. | P0 | functional | D-013 |
| TC-PVP-021 | PvP never steals items | Any PvP defeat | 1) Compare inventories before and after. | No eggs or animals move between players in PvP (theft exists only in raids, D-024); INV-01 and INV-02 hold. | P0 | functional | D-024 |
| TC-PVP-022 | PvP rewards | PvP reward configuration per [[PvP System]] | 1) Defeat an opponent. | Reward (if any) granted exactly once; repeated defeats of the same opponent follow the configured anti-farming rule. | P1 | functional | D-023 |
| TC-PVP-023 | Disconnect during PvP | A and B fighting | 1) A disconnects. | A's character is removed per [[Disconnect Handling]]; any combat-logging rule applies the configured penalty (Q-014); B receives no duplicate reward. | P1 | edge | D-013 |
| TC-PVP-024 | Team stays locked | PvP fight in a region | 1) Try to change team. | Rejected `not_at_base` (D-010). | P1 | negative | D-010 |

## 4. Fairness under network conditions

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-PVP-030 | Hit validation with unequal latency | A at 50 ms, B at 250 ms | 1) Duel for 3 minutes. | Hits are validated with the lag tolerance in [[Latency Handling]]; neither player lands hits from clearly impossible positions. | P1 | performance | D-005 |
| TC-PVP-031 | Dodge invulnerability in PvP | A dodges B's Power Strike | 1) Time the dodge. | Server applies the 0.3 s invulnerability using server time; result consistent on both clients after reconciliation. | P2 | edge | D-005 |

## Related documents

- [[Test Cases - Combat]]
- [[Test Cases - Raiding]]
- [[Test Cases - Exploit Prevention]]
- [[PvP System]]
- [[PvP Activation Options]]
- [[Multiplayer Combat Rules]]
- [[Player Defeat and Penalties]]
- [[Service - PvPService]]
- [[UI - PvP Interface]]
