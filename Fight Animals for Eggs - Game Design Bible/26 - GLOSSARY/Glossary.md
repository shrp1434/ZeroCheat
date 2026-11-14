---
title: Glossary
type: reference
category: glossary
status: mixed
priority: P1
owner: Technical Documentation Architect
last_updated: 2026-11-14
tags:
  - glossary
  - reference
---

# Glossary

Project terminology in alphabetical order. Each term links to its owning document. Where a term's meaning depends on an undecided rule, the entry says so.

| Term | Definition | Owning document |
|---|---|---|
| **A0–A5** | Ascension levels of an animal, shown as 0–5 stars. A0 is freshly hatched. Five levels is **PROPOSED** ([[Open Questions#Q-004]]). | [[Ascension System]] |
| **Ability (animal)** | A special action of an animal. It is either **automatic** (fires when ready) or **manual** (player-triggered); both kinds are **CONFIRMED**. | [[Abilities and Cooldowns]] |
| **Ancient lineage** | **PROPOSED** theme in which Mythical and Secret animals are colossal or prehistoric species. | [[Animal Families]] |
| **Animal Index (catalogue)** | The team's catalogue of all 60 launch animals. Not the same as the in-game discovery index. | [[Animal Index]] |
| **Animal Index (in-game)** | The player's discovery record. Wild defeats register an animal; it distinguishes *discovered* from *owned*. **CONFIRMED** concept. | [[Animal Index Feature Specification]] |
| **Ascension** | Raising an animal's level by consuming duplicate copies of the same species. The original is kept. **CONFIRMED**. | [[Ascension System]] |
| **ATK** | Attack: damage per basic hit before defence reduction. | [[Damage, Defence and Health Model]] |
| **AS** | Attack speed in basic hits per second. | [[Animal Stat Budget Model]] |
| **Backpack** | The player's carried egg storage: 10 slots at the start. Backpack eggs can **never** be stolen. **CONFIRMED**. | [[Egg Storage]] |
| **Base** | A player's personal, modular home. The team can only be changed here. **CONFIRMED**. | [[Player Base System]] |
| **Base lock** | The rule that the equipped team is locked from the moment the player leaves their base until they return. **CONFIRMED**. | [[Team Equipping and Base Lock Rule]] |
| **Base storage / Egg Vault** | The base's egg storage: 50 slots at the start. It can be stolen from during an eligible raid. **CONFIRMED**. | [[Module - Egg Vault]] |
| **Cash** | The soft currency earned by defeating wild animals and spent on egg rolls. **CONFIRMED**. | [[Economy Overview]] |
| **Chill** | **PROPOSED** stacking slow; three stacks become a short freeze. | [[Animal Abilities Catalogue]] |
| **Class weight** | An animal's base weight inside its hatch pool: Standard 10, Scarce 6, Elusive 3 (**PROPOSED**). | [[Hatch Pool Tables]] |
| **Combat tag** | The window during which a unit counts as "in combat" and contributes to kill credit. | [[Multiplayer Combat Rules]] |
| **Controller** | A role specialising in stuns, roots, slows, silences and pulls. | [[Animal Roles]] |
| **DEF** | Defence. Damage reduction = DEF / (DEF + 100) (**PROPOSED**). | [[Damage, Defence and Health Model]] |
| **Discovered** | An animal the player has defeated in the wild, registered in the index. | [[Animal Index Feature Specification]] |
| **Duplicate** | An extra copy of an owned species. Duplicates are useful for ascension; there is no duplicate protection. **CONFIRMED**. | [[Independent Random Outcomes]] |
| **Dynamic progression luck** | The hidden system by which progression improves egg-rarity and hatch odds. The actual odds are always disclosed before the player commits. **CONFIRMED** principle; the formula is **PROPOSED**. | [[Dynamic Progression Luck]] |
| **Egg Merging Station** | The purchasable, upgradeable base facility that merges 3 eggs into 1 egg of the next rarity. **CONFIRMED**. | [[Egg Merging Station]] |
| **Egg roll** | Spending Cash to receive an egg whose rarity is randomly decided (stage one of randomness). **CONFIRMED**. | [[Egg Roll System]] |
| **Equipped team** | The exactly three animals that fight alongside the player. **CONFIRMED**. | [[Team Equipping and Base Lock Rule]] |
| **Hatch** | Opening an egg to receive one animal from that rarity's pool (stage two of randomness). Up to 5 at once. **CONFIRMED**. | [[Hatch System]] |
| **Hatch pool** | The set of animals an egg of a given rarity can produce. | [[Hatch Pool Tables]] |
| **Independent outcome** | Every hatch is a fresh random draw, unaffected by history or ownership. **CONFIRMED**. | [[Independent Random Outcomes]] |
| **Knocked out (KO)** | The defeated state of a defending animal during a raid. Only knocked-out defenders can be stolen. **CONFIRMED**. | [[Animal Theft Rules]] |
| **Leash** | **PROPOSED** distance (60 studs) after which a wild animal gives up the chase and resets. | [[Wild Animal AI]] |
| **Mini-boss** | A region's elite encounter; one per region is **PROPOSED**. Bosses are **CONFIRMED** to exist. | [[Boss Design Overview]] |
| **MS** | Movement speed in studs per second (the player's default is 16). | [[Animal Stat Budget Model]] |
| **Offline protection** | Offline players' bases cannot be raided. **CONFIRMED**. | [[Raid Eligibility and Offline Protection]] |
| **oddsVersion** | **PROPOSED** server token binding the odds shown to the player to the odds used for a roll or hatch. Stale tokens are rejected. | [[Randomised Reward Compliance]] |
| **Owned** | An animal in the player's collection, whether hatched, received or stolen. | [[Animal Collection System]] |
| **P (normalised progression)** | Progression Score ÷ 1000, clamped to 0–1. The baseline odds apply at P = 0.30 (**PROPOSED**). | [[Progression Score Specification]] |
| **Pivot** | The P value (0.30) at which the dynamic odds equal the baseline table. | [[Dynamic Luck Probability Tables]] |
| **Player strength** | The player's own power statistic, separate from animal strength. **CONFIRMED**. | [[Player Strength]] |
| **Power Index (PI)** | The balance metric: the geometric mean of offence and effective HP, normalised per rarity. | [[Animal Stat Budget Model]] |
| **Progression Score (PS)** | **PROPOSED** 0–1000 score from level, discoveries, bosses, regions and base progression. It drives dynamic luck. | [[Progression Score Specification]] |
| **PvP** | Player-versus-player combat. Optional (**CONFIRMED**); the activation method is **UNDECIDED** ([[Open Questions#Q-011]]). | [[PvP System]] |
| **Raid** | An optional attack on another online player's base to steal base-stored eggs and knocked-out defenders. **CONFIRMED**. | [[Base Raiding System]] |
| **Rarity** | One of seven tiers: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret. **CONFIRMED**. | [[Egg Rarity System]] |
| **Region multiplier** | **PROPOSED** scaling of wild HP and ATK, Cash and XP by region (×1.0 to ×11.5). | [[Canonical Proposed Values]] |
| **Respawn** | Wild animals return after being defeated; rarer animals take longer. **CONFIRMED**. | [[Wild Animal Spawning and Respawn]] |
| **Rare-spawn event** | **PROPOSED** server-announced spawn window for Mythical and Secret wild animals. | [[Wild Animal Spawning and Respawn]] |
| **Role** | One of seven combat jobs: Tank, Bruiser, Assassin, Skirmisher, Ranged, Support, Controller (**PROPOSED**). | [[Animal Roles]] |
| **Shield (base)** | Raid protection for a base. Shields are **CONFIRMED** as a protection method; acquisition is **UNDECIDED** ([[Open Questions#Q-030]]). | [[Shield Mechanics]] |
| **Shield (combat)** | A temporary HP buffer granted by abilities. | [[Damage, Defence and Health Model]] |
| **Special move** | A player ability with a cooldown (**PROPOSED**: Power Strike, Ground Slam, Rally Cry). | [[Player Combat]] |
| **Stat budget** | The rule that stats derive from rarity × role × species tweak. | [[Animal Stat Budget Model]] |
| **Tilt** | **PROPOSED** factor by which progression shifts hatch odds towards Scarce and Elusive animals inside a pool. | [[Hatch Pool Tables]] |
| **Variant** | A special version of a species (Golden, Diamond, Rainbow, Shadow, Neon). **CONFIRMED** to exist; acquisition is **UNDECIDED**. | [[Animal Variants]] |
| **World boss** | A server-wide, scheduled boss encounter; four are **PROPOSED**. | [[Boss Design Overview]] |
| **Wild animal** | An animal roaming the world that can be fought (not captured) for Cash, XP and index entries. | [[Wild Animal AI]] |

## Related documents

[[Home]] · [[Vault Map]] · [[How To Use This Vault]]
