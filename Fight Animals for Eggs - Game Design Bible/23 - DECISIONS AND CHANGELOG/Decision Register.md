---
title: Decision Register
type: decision-register
category: decisions
status: mixed
priority: P0
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - decisions
  - governance
---

# Decision Register

The master record of every major game decision. **CONFIRMED** entries come directly from the project owner's brief (recorded 2026-11-14). **PROPOSED** entries are team recommendations that are awaiting owner approval. Unresolved items live in [[Open Questions]].

> [!important] How to change a decision
> 1. Never edit a confirmed entry silently. Add a new entry that supersedes it and mark the old one **DEPRECATED** with a link to the new ID.
> 2. Only the project owner can move an entry to **CONFIRMED**.
> 3. Record every change in the [[Changelog]].
> 4. New entries use [[Template - Decision]].

## Summary

| Status | Count |
|---|---:|
| CONFIRMED | 29 |
| PROPOSED | 16 |
| DEPRECATED | 0 |

---

## Confirmed decisions

| ID | Title | Description | Status | Date | Reasoning | Affected systems | Related documents |
|---|---|---|---|---|---|---|---|
| D-001 | Title and platform | The game is called *Fight Animals for Eggs* and ships on Roblox. | **CONFIRMED** | 2026-11-14 | Owner brief | All | [[Vision Statement and Pillars]] |
| D-002 | Core gameplay loop | Explore → fight wild animals → earn cash → register in index → roll eggs → hatch → collect duplicates → ascend → equip three → upgrade base → bosses → new areas → optional PvP and raids. | **CONFIRMED** | 2026-11-14 | Owner brief | All gameplay | [[Core Gameplay Loop]] |
| D-003 | Seven rarity tiers | Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret. | **CONFIRMED** | 2026-11-14 | Owner brief | Animals, eggs, UI, art | [[Egg Rarity System]], [[Rarity Visual Language]] |
| D-004 | Launch roster target | Launch target of 60 animals. | **CONFIRMED** | 2026-11-14 | Owner brief | Animals, content | [[Animal Index]] |
| D-005 | Real-time hybrid combat | Real-time combat in which the player and their animals fight together. The player has basic attacks and special moves, and special moves may have cooldowns. | **CONFIRMED** | 2026-11-14 | Owner brief | Combat | [[Combat System Overview]], [[Player Combat]] |
| D-006 | Team size of three | A player equips exactly three animals. | **CONFIRMED** | 2026-11-14 | Owner brief | Combat, UI, data | [[Team Equipping and Base Lock Rule]] |
| D-007 | Separate player strength | Player strength is a statistic separate from animal strength. | **CONFIRMED** | 2026-11-14 | Owner brief | Combat, progression | [[Player Strength]] |
| D-008 | Manual and automatic abilities | Animal abilities can be manually or automatically activated. Both types exist. | **CONFIRMED** | 2026-11-14 | Owner brief | Combat, UI | [[Abilities and Cooldowns]] |
| D-009 | Auto-targeting with manual commands | Animals auto-target nearby enemies. Players can issue manual target commands. | **CONFIRMED** | 2026-11-14 | Owner brief | Combat, AI, UI | [[Targeting and Command System]] |
| D-010 | Team changes only at base | Equipped animals can only be changed at the player's own base. The team is locked from leaving the base until returning. | **CONFIRMED** | 2026-11-14 | Owner brief | Team, base, data | [[Team Equipping and Base Lock Rule]] |
| D-011 | Wild respawn | Wild animals respawn. Rare animals have longer respawn times. | **CONFIRMED** | 2026-11-14 | Owner brief | World, spawning | [[Wild Animal Spawning and Respawn]] |
| D-012 | Bosses | Mini-bosses and world bosses exist. | **CONFIRMED** | 2026-11-14 | Owner brief | World, combat | [[Boss Design Overview]] |
| D-013 | Mixed defeat penalties | Defeat consequences differ by battle type. Exact penalties are undecided (Q-014). | **CONFIRMED** | 2026-11-14 | Owner brief | Combat, economy | [[Player Defeat and Penalties]] |
| D-014 | Cash economy entry | Defeating wild animals earns cash. Cash purchases egg rolls. | **CONFIRMED** | 2026-11-14 | Owner brief | Economy, eggs | [[Economy Overview]] |
| D-015 | Two-stage randomness | The roll decides egg rarity. The hatch picks an animal from that rarity's pool. | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs | [[Egg Roll System]], [[Hatch System]] |
| D-016 | Five simultaneous hatches | Up to five eggs can be hatched at once. | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs, UI | [[Hatch System]] |
| D-017 | Hidden progression luck | Progression improves egg-rarity and hatch odds. It does not affect wild encounter rarity. The formula may be hidden, but actual odds must be disclosed before committing and must never be altered silently after purchase. | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs, luck, compliance | [[Dynamic Progression Luck]], [[Randomised Reward Compliance]] |
| D-018 | Independent hatches | No duplicate protection, no bias towards unowned animals, no history influence. Duplicates feed ascension. | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs, ascension | [[Independent Random Outcomes]] |
| D-019 | Ascension by duplicates | Ascension consumes the required duplicates. The original animal is retained. | **CONFIRMED** | 2026-11-14 | Owner brief | Ascension | [[Ascension System]] |
| D-020 | Egg merging | 3 eggs of one rarity → 1 egg of the next rarity. Requires a purchased Egg Merging Station, which must be upgraded for higher rarities and changes appearance with each upgrade. | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs, base | [[Egg Merging]], [[Egg Merging Station]] |
| D-021 | Egg storage | Backpack 10, base 50, total 60. Backpack eggs cannot be stolen. Additional space is purchasable (currency and price undecided). | **CONFIRMED** | 2026-11-14 | Owner brief | Eggs, raids, economy | [[Egg Storage]] |
| D-022 | Modular personal bases | Every player owns a personal modular base with individually upgradeable sections. Base progression can contribute to multipliers, strength and progression. | **CONFIRMED** | 2026-11-14 | Owner brief | Base | [[Player Base System]] |
| D-023 | Optional PvP | PvP is optional. Players choose whether to take part. | **CONFIRMED** | 2026-11-14 | Owner brief | PvP | [[PvP System]] |
| D-024 | Optional raids and theft rules | Raids are optional. Base eggs are stealable. A defending animal can be stolen only after being knocked out. Maximum three animals per successful raid. Offline bases cannot be raided. Protection comes from shields and physical defences. | **CONFIRMED** | 2026-11-14 | Owner brief | Raids, base, data | [[Base Raiding System]], [[Animal Theft Rules]] |
| D-025 | Shared world, solo and multiplayer | One large shared world that supports both single-player and multiplayer play. | **CONFIRMED** | 2026-11-14 | Owner brief | World, network | [[World Overview and Map]], [[Multiplayer Architecture]] |
| D-026 | Visual direction | Colourful, polished, low-poly animals with clear silhouettes. No horror, Italian brainrot or meme animals. | **CONFIRMED** | 2026-11-14 | Owner brief | Art | [[Art Bible]] |
| D-027 | Balanced monetisation | Fully playable without Robux. No essential progression behind purchases. Paid random rewards are not the main revenue mechanism. | **CONFIRMED** | 2026-11-14 | Owner brief | Monetisation | [[Monetisation Principles]] |
| D-028 | Special variants exist | Selected species have special variants (examples: Golden, Diamond, Rainbow, Shadow, Neon). Acquisition is undecided (Q-006). | **CONFIRMED** | 2026-11-14 | Owner brief | Animals, art | [[Animal Variants]] |
| D-029 | Animal index | Defeating wild animals registers them in the index. The index distinguishes discovered animals from owned animals. | **CONFIRMED** | 2026-11-14 | Owner brief | Index, UI, data | [[Animal Index Feature Specification]] |

## Proposed decisions (awaiting owner approval)

| ID | Title | Description | Status | Date | Reasoning | Affected systems | Related documents |
|---|---|---|---|---|---|---|---|
| D-030 | Rarity distribution | 12 / 11 / 10 / 9 / 8 / 6 / 4 animals per rarity. | **PROPOSED** | 2026-11-14 | Supplied by owner as a proposal; gives deeper common pools for early variety | Animals, hatch pools | [[Animal Index]] |
| D-031 | Baseline egg odds | 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 %. | **PROPOSED** | 2026-11-14 | Owner-supplied provisional values | Eggs | [[Egg Roll System]] |
| D-032 | Launch roster | The 60 species in [[Canonical Proposed Values#2. Launch roster (PROPOSED)]]. | **PROPOSED** | 2026-11-14 | Distinct roles and habitats per family | Animals | [[Animal Index]] |
| D-033 | Ancient lineage theme | Mythical and Secret tiers use colossal and prehistoric animals. | **PROPOSED** | 2026-11-14 | Clear, recognisable escalation; ties to "ancient egg" fiction | Animals, art, eggs | [[Animal Families]] |
| D-034 | Role-based stat budget | Stats come from a rarity tier multiplier × role multiplier × small species tweak, checked with a Power Index. | **PROPOSED** | 2026-11-14 | Coherent, auditable balance | Animals, combat | [[Animal Stat Budget Model]] |
| D-035 | Eight-region hybrid world | Hub plus eight habitat regions, unlocked sequentially. | **PROPOSED** | 2026-11-14 | Habitat variety; staged power curve | World | [[World Overview and Map]] |
| D-036 | Progression Score luck model | PS 0–1000 from level, discoveries, bosses, regions and base. Linear slope per rarity around the P = 0.30 pivot. | **PROPOSED** | 2026-11-14 | Transparent to designers; easy to disclose as final odds | Luck | [[Progression Score Specification]] |
| D-037 | Five-level ascension | A1–A5. Duplicate requirements fall as rarity rises. | **PROPOSED** | 2026-11-14 | Keeps rare-animal ascension reachable | Ascension | [[Ascension Progression Table]] |
| D-038 | Five-level merge station | Level gates per merge tier, plus cash fees. | **PROPOSED** | 2026-11-14 | Main late-game cash sink | Eggs, economy | [[Egg Merging Station]] |
| D-039 | Flat egg roll price | 200 Cash per roll. | **PROPOSED** | 2026-11-14 | Simple and readable; acceleration is intended | Economy | [[Egg Pricing]] |
| D-040 | Shared kill credit | Every contributor with ≥10% damage gets the full reward. | **PROPOSED** | 2026-11-14 | Removes kill-stealing friction in a shared world | Combat, economy | [[Multiplayer Combat Rules]] |
| D-041 | Odds version tokens | Displayed odds are bound to a server token. Stale tokens are rejected. | **PROPOSED** | 2026-11-14 | Enforces D-017 disclosure technically | Eggs, tech | [[Randomised Reward Compliance]] |
| D-042 | Animals do not level individually | Animal power comes from rarity, ascension and base bonuses. There is no per-animal XP at launch. | **PROPOSED** | 2026-11-14 | Avoids adding an unrequested system | Animals, progression | [[Open Questions#Q-021]] |
| D-043 | Aquatic animals "air-swim" | Aquatic companions float and swim through the air with water-trail VFX. | **PROPOSED** | 2026-11-14 | Lets aquatic animals join land combat | Animation, VFX | [[Open Questions#Q-028]] |
| D-044 | No Robux sale of Cash | Cash is never sold for Robux, so cash-purchased egg rolls are not paid random items. | **PROPOSED** | 2026-11-14 | Compliance and fairness | Monetisation | [[Roblox Monetisation Policy Requirements]] |
| D-045 | No trading at launch | Player-to-player trading is out of scope at launch. | **PROPOSED** | 2026-11-14 | Not in the brief; large exploit surface | Economy, security | [[Open Questions#Q-026]] |
