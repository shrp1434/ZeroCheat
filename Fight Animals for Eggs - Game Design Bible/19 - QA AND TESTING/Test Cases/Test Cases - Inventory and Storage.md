---
title: Test Cases - Inventory and Storage
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - inventory
  - storage
  - team
---

# Test Cases - Inventory and Storage

Test cases for egg storage (backpack and base), storage expansion, the owned-animal collection and team equipping with the base lock rule. System documents: [[Egg Storage]], [[Storage Expansion Economics]], [[Animal Collection System]], [[Team Equipping and Base Lock Rule]], [[Schema - Egg Inventory]], [[Schema - Animal Collection]], [[Schema - Equipped Team]].

> [!success] CONFIRMED rules under test
> Backpack 10 + base 50 = 60 at start; backpack eggs can never be stolen; extra space can be bought (D-021). Team of exactly three (D-006). Team changes only at the player's own base and stays locked after leaving until the player returns (D-010).

> [!warning] UNDECIDED parameters (tested generically)
> Expansion currency `C_exp` ([[Open Questions#Q-009]]) and price `P_exp(step)` ([[Open Questions#Q-010]]) are read from configuration; tests assert behaviour, not values. Owned-animal capacity `N_animals` is **UNDECIDED** ([[Open Questions#Q-022]]; working assumption 100). Team rule for players who own fewer than three animals: **UNDECIDED** (Q-1002).

> [!info] PROPOSED values used
> Expansion steps: backpack +5 × 3 (max 25), base +25 × 6 (max 200) ([[Canonical Proposed Values]] §11).

**Fixtures.** `QA_FillStorage(container, count, rarity)`, `QA_SetExpansionStep(container, step)`, `QA_SetOwnedAnimals(list)`, `QA_TeleportToBase()`, `QA_TeleportToRegion(name)`, `QA_SetConfig(key, value)`.

## 1. Egg storage

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-INV-001 | Starting capacity | New profile | 1) Open storage UI. 2) Query server profile. | Backpack 0/10, base 0/50, total capacity 60. UI and server agree. | P0 | functional | D-021 |
| TC-INV-002 | Fill the backpack | Backpack 9/10 | 1) Receive one egg. 2) Receive another. | First goes to backpack (10/10). Second follows the destination rule in [[Egg Storage]]; the backpack never shows 11/10 (INV-06). | P0 | edge | D-021 |
| TC-INV-003 | Move egg backpack → base | At own base; backpack 5; base 10/50 | 1) Move one egg to base storage. | Backpack 4, base 11. Egg identity and rarity unchanged. | P0 | functional | D-021 |
| TC-INV-004 | Move egg base → backpack | At own base; base 11; backpack 4/10 | 1) Move one egg to the backpack. | Base 10, backpack 5; the egg is now unstealable (INV-07). | P0 | functional | D-021 |
| TC-INV-005 | Move into a full container | Backpack 10/10 | 1) Try to move a base egg to the backpack. | Rejected `container_full`; nothing moves. | P0 | negative | D-021 |
| TC-INV-006 | Transfer location rule | Player away from base | 1) Try to move eggs between backpack and base storage. | Behaviour follows [[Egg Storage]] (**PROPOSED**: transfers only at the player's own base); a crafted request from elsewhere is rejected. | P1 | negative | D-021 |
| TC-INV-007 | Backpack eggs are flagged unstealable | Eggs of every rarity in the backpack | 1) Inspect the raid-visible inventory of this player from a raider's client. | No backpack egg is replicated or targetable during a raid (see TC-RAID-021). | P0 | security | D-021 |
| TC-INV-008 | Transfer during an active raid on own base | Raid in progress against the player | 1) Defender moves a base egg into the backpack. | **PROPOSED**: base-to-backpack transfers are rejected during a raid against the base (prevents "rescue" exploits). If [[Egg Theft Rules]] chooses otherwise, the transfer and any theft of the same egg are mutually exclusive (exactly one commits). | P0 | edge | D-024 |
| TC-INV-009 | Conservation under random operations | QA build | 1) Run a scripted sequence of 1,000 random rolls, moves, hatches and merges. | INV-01 and INV-06 hold after every step; final counts equal the ledger. | P0 | functional | D-021 |

## 2. Storage expansion

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-INV-020 | Backpack expansion steps | Configured `C_exp`, `P_exp(1..3)`; enough of `C_exp` | 1) Buy step 1, 2, 3. 2) Try step 4. | Capacity 15, 20, 25. Step 4 rejected `max_capacity`. Each purchase deducts exactly `P_exp(step)` of `C_exp` once. | P0 | functional | D-021, Q-009, Q-010 |
| TC-INV-021 | Base storage expansion steps | As above for base | 1) Buy steps 1–6. 2) Try step 7. | Capacity 75, 100, 125, 150, 175, 200; step 7 rejected. | P0 | functional | D-021, Q-009, Q-010 |
| TC-INV-022 | Insufficient balance for expansion | Balance of `C_exp` = `P_exp(step) − 1` | 1) Attempt purchase. | Rejected; capacity and balance unchanged. | P0 | negative | Q-010 |
| TC-INV-023 | Exactly enough balance | Balance = `P_exp(step)` | 1) Purchase. | Succeeds; balance 0. | P1 | edge | Q-010 |
| TC-INV-024 | Robux expansion branch (only if Q-009 chooses Robux) | Developer product configured | 1) Purchase. 2) Simulate `ProcessReceipt` being called twice for the same purchase ID. | Capacity granted exactly once; receipt answered `PurchaseGranted` only after the profile save succeeds ([[Test Cases - Persistence]] TC-PER-040). | P0 | security | D-027, Q-009 |
| TC-INV-025 | Cash expansion branch (only if Q-009 chooses Cash) | Cash ≥ price | 1) Purchase. | Cash ledger entry `storage_expansion` with the configured price; no Robux path. | P1 | functional | Q-009 |
| TC-INV-026 | Expansion is not a pay-to-win gate | Any configuration | 1) Review: can a non-paying player reach every capacity step? | Free path exists to the base capacities required for normal play (D-027). If a step is Robux-only, the owner has approved it in the [[Decision Register]]. | P1 | functional | D-027 |
| TC-INV-027 | Expansion persists | Bought steps | 1) Rejoin on another server. | Capacity identical. | P0 | functional | D-021 |
| TC-INV-028 | Expanded base capacity raises stealable volume only for base | Base 200 | 1) Inspect raid-visible eggs. | Only base storage eggs are raid-visible; egg theft per raid is still capped at `L_egg` ([[Open Questions#Q-013]]). | P1 | functional | D-024 |

## 3. Owned-animal collection

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-INV-040 | Animal capacity limit | Owned = `N_animals` | 1) Attempt to hatch. | Rejected before egg consumption (see TC-EGG-063). | P0 | edge | Q-022 |
| TC-INV-041 | Animal instance identity | Two copies of the same species | 1) Inspect collection. | Each copy has a unique instance ID, its own ascension level and variant flag; copies are distinguishable in the UI. | P0 | functional | D-019 |
| TC-INV-042 | Collection UI matches server | 100 animals owned | 1) Scroll, sort and filter. | Counts and properties match the server profile; sorting by rarity, ascension and species works. | P2 | functional | D-019 |
| TC-INV-043 | Owned vs discovered in index | Species discovered but not owned; another owned | 1) Open [[UI - Animal Index Screen]]. | Two distinct visual states (D-029). | P1 | functional | D-029 |

## 4. Team equipping and the base lock rule

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-INV-060 | Equip three animals at base | At own base; ≥ 3 owned | 1) Choose three. 2) Confirm. | Team of exactly 3 saved; companions spawn with the player. | P0 | functional | D-006, D-010 |
| TC-INV-061 | Team of four | At own base | 1) Try to select a fourth in UI. 2) Send a crafted request with 4 IDs. | UI caps at three. Request rejected `invalid_team_size`; previous team unchanged. | P0 | negative | D-006 |
| TC-INV-062 | Team of two when three or more are owned | At own base; ≥ 3 owned | 1) Send a request with 2 IDs. | **PROPOSED**: rejected `invalid_team_size`; previous team unchanged (team is exactly three). | P0 | negative | D-006 |
| TC-INV-063 | Player who owns fewer than three animals | New player owning 1–2 animals | 1) Open team UI. | Behaviour per the Q-1002 outcome. Until decided, **PROPOSED** working assumption: every owned animal is equipped and the remaining slots show an empty state prompting the player to hatch more. INV-04 is relaxed only for this case. | P1 | edge | D-006 |
| TC-INV-064 | Change team away from base | Player in a region | 1) Open team UI. 2) Send a crafted equip request. | UI shows "Return to your base to change your team". Request rejected `not_at_base`; team unchanged (INV-05). | P0 | negative | D-010 |
| TC-INV-065 | Team locked after leaving, until return | Team A equipped | 1) Leave base. 2) Return. 3) Change to team B. | Step 1 locks; step 3 allowed and saved. | P0 | functional | D-010 |
| TC-INV-066 | Leaving the base mid-selection | Team UI open with a pending (unconfirmed) selection | 1) Walk out of the base boundary before confirming. 2) Try to confirm. | UI closes or confirm is disabled at the boundary; pending selection discarded; the last committed team remains. A confirm that reaches the server after exit is rejected `not_at_base`. No partial team. | P0 | edge | D-010 |
| TC-INV-067 | Confirm on the boundary in the same frame | Pending selection; player on the boundary line | 1) Confirm while crossing. | The server's position check at commit time decides; result is either the full new team or the old team, never a mix. | P1 | edge | D-010 |
| TC-INV-068 | Team change at another player's base | Inside someone else's base | 1) Attempt change. | Rejected `not_own_base`. | P0 | negative | D-010 |
| TC-INV-069 | Same animal instance twice | At base | 1) Request `[A, A, B]`. | Rejected `duplicate_animal`. | P0 | security | D-006 |
| TC-INV-070 | Two copies of the same species | Owns two instances of one species | 1) Equip both plus one other. | **PROPOSED**: accepted (no confirmed rule forbids it). If [[Team Equipping and Base Lock Rule]] adds a uniqueness rule, this case changes to rejected. | P2 | edge | D-006 |
| TC-INV-071 | Equip an animal not owned | Another player's instance ID | 1) Send equip request. | Rejected `not_owned`; security log entry. | P0 | security | D-006 |
| TC-INV-072 | Team change via respawn or teleport | Defeated in a region | 1) Respawn. 2) If respawn places the player at base, change team. | Change allowed only if the server considers the player inside their own base boundary at commit time. | P1 | edge | D-010 |
| TC-INV-073 | Team after an equipped animal is stolen | Raid stole a knocked-out equipped animal | 1) Defender inspects team. | Team never references an animal the defender no longer owns (INV-04). Slot handling per the Q-025 outcome; see TC-RAID-036. | P0 | edge | D-024, Q-025 |
| TC-INV-074 | Team persists | Team equipped | 1) Rejoin. | Same three instances equipped. | P0 | functional | D-006 |

## Related documents

- [[Test Cases - Egg Rolls and Hatching]]
- [[Test Cases - Egg Merging]]
- [[Test Cases - Raiding]]
- [[Test Cases - Persistence]]
- [[Egg Storage]]
- [[Storage Expansion Economics]]
- [[Animal Collection System]]
- [[Team Equipping and Base Lock Rule]]
- [[Service - TeamService]]
- [[UI - Egg Storage]]
- [[UI - Team Selection]]
- [[UI - Animal Inventory]]
