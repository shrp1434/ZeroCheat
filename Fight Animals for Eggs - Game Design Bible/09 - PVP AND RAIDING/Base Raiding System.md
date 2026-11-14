---
title: Base Raiding System
type: system
category: pvp-and-raiding
status: mixed
priority: P0
owner: PvP / Raid Designer
last_updated: 2026-11-14
tags:
  - raids
  - base
  - theft
  - pvp
---

# Base Raiding System

The overview of base raids: who takes part, what the attacker is trying to do, how the base defends itself, what can be stolen, and what makes a raid "successful". Detailed rules live in the linked documents; this page is the map and the parameter list.

> [!success] CONFIRMED (D-024, D-021)
> - Base raiding is **optional**.
> - Eggs stored in the **base** can be stolen. **Backpack eggs can never be stolen.**
> - A defending animal can be stolen **only after it has been knocked out**. Undefeated defenders cannot be stolen.
> - **Maximum THREE animals** stolen per successful raid.
> - **Offline bases cannot be raided.**
> - Bases are protected by **shields** and **physical defences**.

> [!warning] UNDECIDED
> Raid duration ([[Open Questions#Q-012]]), egg theft limit ([[Open Questions#Q-013]]), defeat penalties ([[Open Questions#Q-014]]), what stolen animals keep ([[Open Questions#Q-025]]), matchmaking ([[Open Questions#Q-029]]), shield acquisition ([[Open Questions#Q-030]]), which animals defend ([[Open Questions#Q-033]]), whether the defender's own team joins ([[Open Questions#Q-035]]). New: raid opt-in model (Q-207), attackers per raid (Q-208), cross-server raids (Q-209).

## Roles

| Role | Who | Brings |
|---|---|---|
| **Attacker** | One player (recommended at launch, Q-208) | Their player character and three equipped companions (team lock applies, D-010) |
| **Defender** | The base owner, who must be online ([[Raid Eligibility and Offline Protection]]) | Themselves (if they return to defend), guard animals, defence structures, shields |
| **Guard animals** | Owned animals assigned to defend | Which animals defend is **UNDECIDED** ([[Open Questions#Q-033]]); AI in [[Animal Guards and Base Defence AI]] |
| **Third parties** | Everyone else | Nothing. Other players cannot enter a base during a raid *(PROPOSED)*. |

> [!warning] UNDECIDED (Q-208)
> **How many attackers can join one raid?** Options: solo only; a party of up to 2; up to 3 with defender scaling. **Recommendation (PROPOSED, unapproved):** solo at launch. It keeps balance, validation and the three-animal cap easy to reason about; parties can follow once raid data exists.

## Objective and flow (PROPOSED)

1. **Initiate.** The attacker picks an eligible base from the Raid Board in the hub ([[UI - Raid Interface]]), or at the base's raid gate. The server validates eligibility.
2. **Warning.** The defender is notified and may return to defend; `RaidWarningSeconds` runs.
3. **Assault.** The raid timer (`RaidDurationSeconds`, **UNDECIDED**) starts. The attacker fights through physical defences and guard animals towards the **Vault Lock** on the [[Module - Egg Vault]].
4. **Breach.** When the Vault Lock reaches 0, the vault is breached. Only now can eggs be taken.
5. **Theft.** The attacker carries eggs one at a time to the extraction point to **secure** them ([[Egg Theft Rules]]) and captures knocked-out defenders ([[Animal Theft Rules]]).
6. **Resolution.** The raid ends when the timer expires, the attacker leaves through the extraction point, the attacker is defeated, either side goes offline, or the server shuts down. The server commits the outcome atomically.
7. **Aftermath.** Shields, cooldowns, rewards and compensation are applied ([[Shield Mechanics]], [[Raid Rewards and Defender Compensation]]).

Full states and the sequence diagram: [[Raid Lifecycle and States]].

## Definition of a successful raid

> [!info] PROPOSED definition
> A raid is **successful** if, and only if:
> 1. the attacker **breached the Vault Lock** while the raid was in the `Active` state and the defender was online, **and**
> 2. the server reached the `Resolving` state and committed the outcome without the raid being **voided** by [[Raid Anti-Exploit Validation]] or a server failure ([[Raid Disconnection Handling]]).
>
> Securing eggs is only possible after a breach, so any raid with a stolen egg is successful. Animal captures made before a breach are held provisionally and returned if the raid is not successful.

This definition matters because the confirmed **three-animal cap applies per successful raid** (D-024): at most three captured animals are transferred, and only from a successful raid.

## Physical defences (PROPOSED)

| Defence | Source | Role in a raid |
|---|---|---|
| Barricades | [[Module - Defence Station]] | Destructible walls that force the attacker through chokepoints |
| Traps | [[Module - Defence Station]] | Slows and damage on paths |
| Turrets | [[Module - Defence Station]] | Automatic ranged fire at the attacker and their companions |
| Vault Lock | [[Module - Egg Vault]] | The breach objective; HP scales with Egg Vault level |
| Shield | [[Module - Shield Generator]] | Prevents a raid from starting while active ([[Shield Mechanics]]) |
| Guard animals | [[Module - Animal Pens]] / team (Q-033) | Fight the attacker; can be knocked out and captured |

Tuning guideline *(new)*: `VaultLockHP` per Egg Vault level should be set so an on-curve attacker, with no guards and no defender, needs 25–40% of `RaidDurationSeconds` to breach. This ties the lock to the duration decision (Q-012) without inventing a duration. Values for structures belong in [[Base Defence Overview]].

## Raid opt-in

> [!warning] UNDECIDED (Q-207)
> **How does a player opt into raiding?** "Base raiding is optional" is confirmed (D-024), but the mechanism is not. Options:
> 1. **Reciprocal opt-in toggle:** only players who opted in can raid, and only opted-in bases can be raided. Toggle changes take effect after a 24 h delay and cannot happen during a raid or cooldown.
> 2. One-way: anyone can raid opted-in bases (opted-out players can raid without risk; unfair).
> 3. Opt-out only by building no Egg Vault (unclear and unfriendly).
>
> **Recommendation (PROPOSED, unapproved):** option 1. Reciprocity is the fairest reading of "optional": you can only take from players who accepted the same risk.

## Cross-server raids

> [!warning] UNDECIDED (Q-209)
> This design assumes (PROPOSED) that a player's base exists in the server hosting their session, so raids happen only between players in the **same server**. Cross-server raiding would need the defender's base loaded in another server, live cross-server presence checks and cross-server transactions, and makes offline protection harder to guarantee. **Recommendation (PROPOSED, unapproved):** same-server only at launch.

## Raid parameters

| Parameter | Value | Status | Owner document |
|---|---|---|---|
| `MaxAnimalsStolenPerRaid` | 3 | **CONFIRMED** | [[Animal Theft Rules]] |
| `RaidDurationSeconds` | No approved value | **UNDECIDED** (Q-012) | [[Raid Lifecycle and States]] |
| `MaxEggsStolenPerRaid` | No approved default | **UNDECIDED** (Q-013) | [[Egg Theft Rules]] |
| `RaidWarningSeconds` | 20 | **PROPOSED** *(new)* | [[Raid Lifecycle and States]] |
| `RaidCarryCapacity` | 1 egg at a time | **PROPOSED** *(new)* | [[Egg Theft Rules]] |
| `DroppedEggReturnSeconds` | 10 | **PROPOSED** *(new)* | [[Egg Theft Rules]] |
| `AnimalCaptureChannelSeconds` | 3 | **PROPOSED** *(new)* | [[Animal Theft Rules]] |
| `OnlineHeartbeatTimeoutSeconds` | 10 | **PROPOSED** *(new)* | [[Raid Eligibility and Offline Protection]] |
| `RaidMinimumLevel` | 20 (attacker and defender) | **PROPOSED** *(new)* | [[Raid Eligibility and Offline Protection]] |
| `AttackerRaidCooldownSeconds` | 900 | **PROPOSED** *(new)* | [[Raid Eligibility and Offline Protection]] |
| `PairRaidCooldownSeconds` | 86,400 | **PROPOSED** *(new)* | [[Raid Eligibility and Offline Protection]] |
| `MaxRaidsReceivedPerDay` | 3 | **PROPOSED** *(new)* | [[Raid Eligibility and Offline Protection]] |
| `PostRaidShieldSeconds` | 1,800 after a failed raid; 3,600 after a successful raid | **PROPOSED** *(new)*, acquisition model Q-030 | [[Shield Mechanics]] |
| `RaidResolutionTimeoutSeconds` | 15 | **PROPOSED** *(new)* | [[Raid Disconnection Handling]] |

All parameters live in one server configuration module ([[Configuration Modules]]) so owner decisions change data, not code. `RaidDurationSeconds` and `MaxEggsStolenPerRaid` must be set explicitly per test build and must fail loudly if missing; there is deliberately no fallback value.

## Services
- [[Service - RaidService]] owns the raid session; [[Implementation - Raid Session Controller]] is the reference implementation.
- [[Service - BaseService]] owns structures and storage; [[Service - DataService]] owns profiles and transactions.

## Related documents
- [[Raid Lifecycle and States]]
- [[Raid Eligibility and Offline Protection]]
- [[Shield Mechanics]]
- [[Egg Theft Rules]]
- [[Animal Theft Rules]]
- [[Raid Disconnection Handling]]
- [[Raid Anti-Exploit Validation]]
- [[Raid Rewards and Defender Compensation]]
- [[Base Defence Overview]]
- [[Animal Guards and Base Defence AI]]
- [[Player Base System]]
