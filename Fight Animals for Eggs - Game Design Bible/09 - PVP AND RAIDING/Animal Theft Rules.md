---
title: Animal Theft Rules
type: system
category: pvp-and-raiding
status: mixed
priority: P0
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - raids
  - animals
  - theft
  - capture
---

# Animal Theft Rules

How defending animals can be captured in a raid, the confirmed three-animal cap, and what happens to a captured animal.

> [!success] CONFIRMED (D-024)
> - A defending animal can be stolen **only after it has been knocked out**.
> - **Undefeated defenders cannot be stolen.**
> - **Maximum THREE animals** stolen per **successful** raid.
> - Offline bases cannot be raided.

> [!warning] UNDECIDED
> - What a stolen animal keeps (ascension level, variant) and what happens to the victim's equipped team ([[Open Questions#Q-025]]). Blocks the raid prototype.
> - Which animals defend a base ([[Open Questions#Q-033]]) and whether the defender's own team joins ([[Open Questions#Q-035]]).
> - Minimum-roster protection (Q-206, new).

## Successful raid (reference)

A raid is successful only if the attacker breached the Vault Lock while the defender was online, and the server committed the outcome without voiding it. Full definition: [[Base Raiding System#Definition of a successful raid]]. Animals are transferred **only** from successful raids.

## Which animals can be captured (PROPOSED)

An animal is capturable if, and only if, all of these are true on the server:
1. It is owned by the defender and is **assigned as a defender in this raid** (the set fixed at `Warning`; which animals that includes is Q-033, see [[Animal Guards and Base Defence AI]]).
2. It was **knocked out during this raid** (server-recorded KO event with this raid's ID). An animal that was already knocked out before the raid, or never fought, cannot be captured.
3. It is still knocked out (not rescued; see below).
4. It is not protected by minimum-roster protection (Q-206).
5. It has not been marked "recently stolen" within the last 24 h *(new)*: animals stolen in a previous raid cannot be assigned to guard duty for 24 h, which prevents immediate ping-pong theft.

An animal that is not knocked out can never be captured, whatever its HP.

## Capture flow (PROPOSED)

| Step | Rule *(new values)* |
|---|---|
| 1. Knock-out | Guard reaches 0 HP and collapses into a glowing capture marker at its position ([[Animation - Raid Interactions]]). It stays down for the rest of the raid. Field revive is disabled for raid defenders ([[Animal Combat Behaviour#Knock-out and recovery]]). |
| 2. Channel | Attacker holds a `ProximityPrompt` within 6 studs for `AnimalCaptureChannelSeconds` = 3. Taking damage or moving more than 6 studs away cancels it. |
| 3. Hold | On completion the animal enters the raid's **hold**: removed from the field, shown to both players as held. Captures are possible in `Active` and `Breached`. |
| 4. Resolve | In `Resolving`, if the raid is `Succeeded`, every held animal (at most 3) is transferred to the attacker in one transaction. If not, every held animal returns to the defender. |

### Defender counterplay: rescue *(new)*
The defender can channel 3 s on a knocked-out guard to **rescue** it. A rescued guard is sent back to the pens, cannot fight again this raid and cannot be captured. Rescue is the defender's way to protect a valuable animal after it falls.

### The cap
- `MaxAnimalsStolenPerRaid` = **3** (**CONFIRMED**). The hold cannot contain more than three animals; a fourth capture channel cannot start.
- The cap is per raid and per successful outcome, not per attacker per day. Daily protection comes from `MaxRaidsReceivedPerDay` and the pair cooldown ([[Raid Eligibility and Offline Protection]]).

### Capacity
The attacker needs a free owned-animal slot for each capture. Owned-animal capacity is **UNDECIDED** ([[Open Questions#Q-022]]; working assumption 100). If the attacker is full, the capture channel cannot start (`AnimalStorageFull`).

## What a stolen animal keeps (Q-025)

> [!warning] UNDECIDED (Q-025)
> Options for **ascension level**:
> 1. Kept in full: the animal is transferred exactly as it is.
> 2. Reset to A0 for the new owner; the consumed duplicates are lost.
> 3. Ascended animals (A1 and above) cannot be captured.
>
> Options for **variant**: kept, or reverted to the base form.
>
> Options for the **victim's equipped team** (only relevant if equipped animals can defend, Q-033 and Q-035):
> 1. Equipped animals are never capturable, even if they help defend.
> 2. They are capturable; the empty team slot can be refilled only at the base (D-010).
>
> **Recommendation (PROPOSED, unapproved):** ascension and variant are **kept** (option 1, since the animal really changes hands and a stolen animal should be worth having), combined with **dedicated guards chosen by the defender** under Q-033 and **equipped animals never capturable**. The defender then controls exactly which animals are at risk, which is the fairest way to make full transfer acceptable.

If an equipped animal is ever stolen (only possible if the owner chooses the alternative), the empty slot can be filled only at the player's base (D-010); the defender is prompted to do so in `Aftermath`.

## Minimum-roster protection

> [!warning] UNDECIDED (Q-206)
> **Should a defender always keep a minimum number of owned animals?** Option: captures that would leave the defender with fewer than three owned animals are refused, so they can always field a full team of three (D-006). Alternatives: no protection; protect the defender's single highest-rarity animal. **Recommendation (PROPOSED, unapproved):** minimum of three owned animals, matching the confirmed team size.

## Index and collection effects (PROPOSED)
- The attacker's index marks the species **owned** (and discovered, if new) (D-029).
- The victim's index keeps the species **discovered**. It shows **owned** only if they still hold another copy ([[Animal Index Feature Specification]]).
- Transfers are journalled with raid ID and transaction ID ([[Raid Anti-Exploit Validation]]).

## Test hooks
- Capture attempt on a guard at 1 HP: rejected (`NotKnockedOut`).
- Capture of a guard knocked out before the raid started: rejected (`NotKnockedOutThisRaid`).
- Fourth capture channel: cannot start (`AnimalCapReached`).
- Raid with three held animals ends `Failed` (no breach): all three return to the defender.
- Defender rescues a knocked-out guard: subsequent capture attempts rejected.
- Cases in [[Test Cases - Raiding]].

## Related documents
- [[Base Raiding System]]
- [[Animal Guards and Base Defence AI]]
- [[Module - Animal Pens]]
- [[Animal Collection System]]
- [[Team Equipping and Base Lock Rule]]
- [[Raid Anti-Exploit Validation]]
- [[Schema - Animal Collection]]
- [[Ascension System]]
