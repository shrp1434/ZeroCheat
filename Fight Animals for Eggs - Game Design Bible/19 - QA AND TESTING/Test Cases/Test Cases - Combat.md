---
title: Test Cases - Combat
type: test-cases
category: qa
status: mixed
priority: P0
owner: Quality Assurance Director
last_updated: 2026-11-14
tags:
  - qa
  - test-cases
  - combat
---

# Test Cases - Combat

Test cases for real-time hybrid combat: the damage model, player attacks and specials, player Strength, animal abilities, targeting and commands, combat state, wild-animal modifiers, rewards, kill credit and defeat. System documents: [[Combat System Overview]], [[Player Combat]], [[Player Strength]], [[Damage, Defence and Health Model]], [[Abilities and Cooldowns]], [[Targeting and Command System]], [[Combat States and State Machine]], [[Combat Rewards]], [[Player Defeat and Penalties]].

> [!success] CONFIRMED rules under test
> Player and animals fight together; the player has basic attacks and special moves with cooldowns (D-005). Team of exactly three (D-006). Player Strength is separate from animal strength (D-007). Manual and automatic abilities both exist (D-008). Animals auto-target; players can command targets (D-009). Cash comes from defeating wild animals (D-014). Defeat penalties vary by battle type and are **UNDECIDED** (D-013, [[Open Questions#Q-014]]).

> [!info] PROPOSED values used
> All combat numbers come from [[Canonical Proposed Values]] §3, §4, §6 and §12. Kill credit ≥ 10% (D-040). Exact damage assertions use a stubbed random factor (`QA_StubRng`) so the expected value is exact.

**Fixtures.** `QA_StubDamageRoll(x)` fixes the `Random(0.95, 1.05)` factor to `x`. `QA_SpawnDummy(hp, def)` spawns a stationary target with given HP and DEF. `QA_SetLevel(n)`, `QA_SetModuleLevel(module, level)`, `QA_AdvanceClock(seconds)`. Times are measured on the server clock.

## 1. Damage model

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-001 | Damage formula, neutral roll | Attacker ATK 20; skill multiplier 1.0; dummy DEF 10; stub 1.00 | 1) One basic hit. | Damage = 20 × 1.0 × 100/110 × 1.00 = **18.1818…** (display rounding per [[Damage, Defence and Health Model]]). | P0 | functional | D-005 |
| TC-CMB-002 | Damage formula, roll extremes | As TC-CMB-001; stub 0.95, then 1.05 | 1) Hit with each stub. | 17.2727… and 19.0909… respectively. | P0 | edge | D-005 |
| TC-CMB-003 | Random factor range | Unstubbed; dummy DEF 0; ATK 20 | 1) 100,000 hits via harness. | Every hit in [19.0, 21.0]; mean within 20 ± 0.01; distribution approximately uniform (χ² over 10 bins, α 0.001). | P1 | statistical | D-005 |
| TC-CMB-004 | Zero defence | DEF 0 | 1) Hit with stub 1.0. | Damage equals ATK × multiplier exactly. | P1 | edge | D-005 |
| TC-CMB-005 | Very high defence | DEF 1,000,000 | 1) Hit. | Damage is positive, finite and below 0.01; no NaN, no negative value, no division error. | P1 | edge | D-005 |
| TC-CMB-006 | No critical hits at launch | Harness | 1) 100,000 hits. | No hit exceeds ATK × multiplier × (100 / (100 + DEF)) × 1.05. | P2 | functional | D-005 |
| TC-CMB-007 | Damage is computed by the server | Exploit client | 1) Send a hit request containing a `damage` field of 99,999. | Field ignored; damage computed by the server formula; security log entry. | P0 | security | D-005 |
| TC-CMB-008 | Lethal hit clamps HP at zero | Dummy HP 10 | 1) Hit for 18.18. | HP becomes 0 (not negative); defeat triggers once. | P1 | edge | D-005 |

## 2. Player attacks and specials

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-010 | Basic combo multipliers | Level 1 (Strength 10); dummy DEF 0; stub 1.0 | 1) Three basic attacks in rhythm. | Hits of 8, 8 and 14. | P0 | functional | D-005 |
| TC-CMB-011 | Combo reset after idle | As TC-CMB-010 | 1) Hit once. 2) Wait 1.3 s. 3) Hit. 4) Hit, wait 1.1 s, hit. | Step 3 is hit 1 again (8). In step 4 the second hit continues the combo (8, then 14 on the next). Reset threshold 1.2 s. | P1 | edge | D-005 |
| TC-CMB-012 | Attack cadence cannot be exceeded | Exploit or macro input | 1) Send basic-attack requests every 0.1 s for 5 s. | Server accepts at most one hit per 0.45 s (≤ 12 hits in 5 s, allowing the first at t = 0); excess requests dropped without error spam to the player. | P0 | security | D-005 |
| TC-CMB-013 | Power Strike damage and cooldown | Level 1; dummy DEF 0; stub 1.0 | 1) Power Strike. 2) Retry at 5.9 s. 3) Retry at 6.0 s. | Step 1: 30 damage. Step 2 rejected `on_cooldown`. Step 3 succeeds. | P0 | functional | D-005 |
| TC-CMB-014 | Ground Slam unlock level | Level 9, then level 10 | 1) Try Ground Slam at each level. | Unavailable at level 9 (UI locked, server rejects); available at level 10. | P1 | functional | D-005 |
| TC-CMB-015 | Ground Slam radius | Level 10 (Strength 28); dummies at 9.9 and 10.1 studs | 1) Ground Slam. | Dummy at 9.9 studs takes 56 (DEF 0, stub 1.0); dummy at 10.1 studs takes nothing. Cooldown 12 s. | P1 | edge | D-005 |
| TC-CMB-016 | Rally Cry buff | Level 25; three animals equipped | 1) Rally Cry. 2) Measure damage at 5.9 s and 6.1 s. | Team damage ×1.15 during 6 s, normal afterwards; cooldown 25 s. Team scope as defined in [[Player Combat]]. | P1 | functional | D-005 |
| TC-CMB-017 | Dodge invulnerability window | Enemy attack scheduled | 1) Dodge so that a hit lands at 0.29 s, another at 0.31 s. | First hit ignored; second applies. Roll covers 12 studs; next dodge available after 4 s. | P1 | edge | D-005 |
| TC-CMB-018 | Cooldowns are server-tracked | Exploit client with altered local cooldown | 1) Fire Power Strike twice 1 s apart. | Second use rejected; UI resynchronises to the server cooldown. | P0 | security | D-005 |
| TC-CMB-019 | Cooldown display accuracy | Any special | 1) Use special. 2) Compare UI timer with server at several points. | UI remaining time within one frame of server time plus measured latency. | P2 | functional | D-005 |

## 3. Player Strength and player statistics

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-020 | Player HP by level | Levels 1, 50, 100 | 1) Read max HP. | 100, 688 and 1,288 (`100 + 12 × (L − 1)`). | P1 | functional | D-007 |
| TC-CMB-021 | Player DEF by level | Levels 1, 100 | 1) Read DEF. | 5 and 54.5. | P2 | functional | D-007 |
| TC-CMB-022 | Base and effective Strength | Level 100; Training Grounds L5 | 1) Read Strength. | Base 208; effective 208 × 1.25 = 260. | P1 | functional | D-007 |
| TC-CMB-023 | Strength is independent of animals | Any team | 1) Change team at base. 2) Ascend an equipped animal. | Player Strength unchanged in both steps. Animal stats change only for the affected animal. | P0 | functional | D-007 |
| TC-CMB-024 | Training Grounds affects animals separately | Training Grounds L1 → L2 | 1) Upgrade. | Player Strength bonus +5% → +10%; equipped animals' stats +4% → +8%; unequipped animals unchanged. | P1 | functional | D-007, D-022 |

## 4. Animal abilities

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-030 | Manual ability activation | An equipped animal with a manual ability (see [[Animal Abilities Catalogue]]) | 1) Activate via its ability button or key. | Ability fires once; cooldown starts; button shows cooldown. | P0 | functional | D-008 |
| TC-CMB-031 | Automatic ability trigger | An equipped animal with an automatic ability | 1) Create its trigger condition (for example engage an enemy). | Ability fires without player input when the condition is met and is off cooldown. | P0 | functional | D-008 |
| TC-CMB-032 | Global cooldown between manual abilities | Two animals with manual abilities | 1) Activate animal A. 2) Activate animal B 0.4 s later. 3) Retry at 0.5 s. | Step 2 rejected (or queued, per [[Abilities and Cooldowns]]); step 3 succeeds. 0.5 s global cooldown applies to manual abilities only. | P1 | edge | D-008 |
| TC-CMB-033 | Ability damage scales from ATK | Ability with 150% ATK; animal ATK 20; target DEF 0; stub 1.0 | 1) Use ability. | 30 damage. | P1 | functional | D-034 |
| TC-CMB-034 | Heal scales from target max HP | Heal of 10% max HP on a target with 300 max HP at 100 HP | 1) Heal. | Target HP 130; never above max HP. | P1 | functional | D-034 |
| TC-CMB-035 | Ascension raises ability effectiveness | Same animal at A0 and A3 | 1) Use the same damaging ability. | A3 damage = A0 damage × 1.15 (+5% per level), before the ATK increase from ascension is also applied. Expected value combines both: ATK × 1.24 × ability % × 1.15. | P1 | functional | D-037 |
| TC-CMB-036 | Ability on a knocked-out animal | One animal knocked out | 1) Try its manual ability. | Rejected; button disabled while knocked out. | P1 | edge | D-008 |

## 5. Targeting and commands

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-040 | Auto-targeting | Three animals; two wild enemies in range | 1) Approach. | Each animal selects a target by the rule in [[Targeting and Command System]] without input. | P0 | functional | D-009 |
| TC-CMB-041 | Manual target command | Three enemies | 1) Command focus on enemy C. | All three animals switch to C within the command response time; they stay on C until it is defeated, leaves range, or the command is cancelled. | P0 | functional | D-009 |
| TC-CMB-042 | Command on an illegal target | Another player (PvP off) or their animals | 1) Issue a target command on them. | Command rejected; animals keep their current behaviour. | P0 | negative | D-009, D-023 |
| TC-CMB-043 | Commanded target dies | Command on enemy C | 1) Defeat C. | Animals revert to auto-targeting. | P1 | edge | D-009 |
| TC-CMB-044 | Command target out of range | Enemy beyond the command range | 1) Issue command. | Rejected or animals path towards it, per [[Targeting and Command System]]; never attack through walls or across leash boundaries. | P2 | edge | D-009 |
| TC-CMB-045 | Touch command input | Mobile device | 1) Tap an enemy to command. | Same result as PC; tap target size per [[UI Accessibility Standards]]. | P1 | functional | D-009 |

## 6. Combat state

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-050 | Combat tag duration | Deal damage once | 1) Query state at 7.9 s and 8.0 s. | In combat at 7.9 s; out of combat at 8.0 s. Receiving damage also refreshes the tag. | P1 | edge | D-005 |
| TC-CMB-051 | Combat tag blocks backpack hatching | In combat | 1) Try to hatch a backpack egg. | Rejected `in_combat` (see TC-EGG-060). | P1 | functional | Q-023 |
| TC-CMB-052 | Combat in the hub | Player in [[Hub - Hatchling Haven]] | 1) Try to attack anything. | No damage can be dealt or received in the safe hub. | P1 | functional | D-025 |
| TC-CMB-053 | Team cannot change in combat away from base | In combat in a region | 1) Open team UI. | Team change rejected because the player is not at base (D-010). | P0 | negative | D-010 |

## 7. Wild modifiers, rewards and kill credit

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-060 | Wild HP and ATK multipliers | A species in Sunscorch Savanna (×1.5) | 1) Compare wild stats with companion stats in [[Animal Statistics Database]]. | Wild HP = companion HP × 2.0 × 1.5; wild ATK = companion ATK × 0.75 × 1.5. | P1 | functional | D-034 |
| TC-CMB-061 | Leash reset | Wild animal engaged | 1) Pull it 61 studs from its spawn point. | Animal disengages, returns and resets to full HP. At 59 studs it keeps fighting. | P1 | edge | D-011 |
| TC-CMB-062 | Leash reset clears contribution | Player dealt 50% then leashed it | 1) Defeat it after the reset without further help. | **PROPOSED**: pre-reset damage does not count; the reward requires ≥ 10% of max HP after the reset. | P2 | edge | D-040 |
| TC-CMB-063 | Cash reward, Common in Whisperwood | No cash bonuses | 1) Defeat a Common wild animal. | +10 Cash, +10 XP. | P0 | functional | D-014 |
| TC-CMB-064 | Cash reward with Multiplier Shrine | Shrine L1 | 1) Defeat a Common in Whisperwood. | +11 Cash (10 × 1.0 × 1.10); XP unaffected (+10). | P1 | functional | D-014 |
| TC-CMB-065 | Region multiplier on rewards | Rare in Frostfang Tundra (×4.5), no bonuses | 1) Defeat it. | Cash 28 × 4.5 = 126; XP 25 × 4.5 = 112.5, rounded per [[Wild Animal Cash Rewards]]. | P1 | functional | D-014 |
| TC-CMB-066 | Kill credit threshold | Two players; target max HP H | 1) Player A deals 9.9% of H, player B the rest. 2) Repeat with A at exactly 10.0%. | Run 1: only B rewarded. Run 2: both receive the **full** reward. | P0 | edge | D-040 |
| TC-CMB-067 | Animal damage counts towards credit | Player A's animals deal 12%, A personally 0% | 1) Defeat target. | A receives full reward. | P1 | functional | D-040 |
| TC-CMB-068 | Contribution outside the tag window | A deals 20%, then waits 9 s without dealing or receiving damage | 1) B defeats the target. | A's contribution expired; A receives nothing. | P1 | edge | D-040 |
| TC-CMB-069 | Defeat registers the species in the index | Species not yet discovered | 1) Defeat it. | Index marks it "discovered" (not "owned"); PS rises by 3. | P0 | functional | D-029 |
| TC-CMB-070 | Reward granted once per defeat | Network jitter simulated | 1) Defeat a target while duplicating the client's last hit request. | Exactly one reward per eligible player; ledger has one entry. | P0 | security | D-014 |

## 8. Defeat

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-080 | Penalty applied by battle type | Penalty table configured for each battle type (values **UNDECIDED**, Q-014) | 1) Be defeated in each battle type: wild, boss, PvP, raid attack, raid defence. | For each type the configured penalty is applied exactly once; ledger reasons name the battle type. Types configured as "none" change nothing. | P0 | functional | D-013 |
| TC-CMB-081 | Defeat never removes eggs or animals unless configured | Default configuration | 1) Be defeated in each battle type. | No eggs or animals lost unless the penalty row explicitly includes them; INV-01 and INV-02 hold. | P0 | functional | D-013 |
| TC-CMB-082 | Defeat condition | Player and animals in combat | 1) Reduce player HP to 0 with animals alive. 2) Knock out all animals with player alive. | Each outcome follows the defeat condition in [[Player Defeat and Penalties]]; the state machine enters `Defeated` only once. | P1 | edge | D-013 |
| TC-CMB-083 | Respawn and team after defeat | Defeated in a region | 1) Respawn. | Respawn location per [[Player Defeat and Penalties]]. If respawn is at base, the team may be changed there; otherwise the team stays locked (D-010). | P1 | functional | D-010 |

## 9. Network conditions

| ID | Title | Preconditions | Steps | Expected result | Priority | Type | Decision |
|---|---|---|---|---|---|---|---|
| TC-CMB-090 | Hit registration under latency | Studio network simulation (incoming replication lag, *unverified* setting name) at 200 ms | 1) Fight a wild animal for 2 minutes. | Hits in range are accepted according to the lag tolerance in [[Latency Handling]]; no hits from clearly out-of-range positions. | P1 | performance | D-005 |
| TC-CMB-091 | Feedback timing | 60 FPS PC | 1) Hit an enemy. | Local hit feedback appears in the next frame; server-confirmed damage number appears within one round trip ([[Combat Feedback and Readability]]). | P2 | performance | D-005 |

## Related documents

- [[Test Cases - Animal AI]]
- [[Test Cases - Bosses]]
- [[Test Cases - PvP]]
- [[Test Cases - Exploit Prevention]]
- [[Combat System Overview]]
- [[Player Combat]]
- [[Damage, Defence and Health Model]]
- [[Abilities and Cooldowns]]
- [[Targeting and Command System]]
- [[Multiplayer Combat Rules]]
- [[Implementation - Combat Damage Pipeline]]
- [[Service - CombatService]]
