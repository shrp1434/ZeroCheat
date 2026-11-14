---
title: Canonical Proposed Values
type: spec
category: balancing
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - balancing
  - economy
  - data
  - source-of-truth
---

# Canonical Proposed Values

> [!important] Single source of truth for numbers
> Every number in the vault comes from this page or from one of the generated tables it links to. If a document needs a value that is not here, add it here first (marked **PROPOSED**) and then reference it. Values marked **CONFIRMED** come from the project owner and must not be changed without a new entry in the [[Decision Register]].

Generated companion tables:
- [[Animal Statistics Database]]: per-animal stats derived from §3
- [[Dynamic Luck Probability Tables]]: egg-rarity odds derived from §6
- [[Hatch Pool Tables]]: per-pool hatch odds derived from §7

---

## 1. Rarity tiers

| Index | Rarity | Status | Launch animals (PROPOSED) | Tier stat multiplier *M* (PROPOSED) | Colour key (PROPOSED) |
|---:|---|---|---:|---:|---|
| 0 | Common | **CONFIRMED** tier | 12 | 1.00 | `#9AA5B1` slate grey |
| 1 | Uncommon | **CONFIRMED** tier | 11 | 1.30 | `#4CC26A` leaf green |
| 2 | Rare | **CONFIRMED** tier | 10 | 1.70 | `#3D8BFF` sky blue |
| 3 | Epic | **CONFIRMED** tier | 9 | 2.20 | `#A55BFF` violet |
| 4 | Legendary | **CONFIRMED** tier | 8 | 2.85 | `#FFB020` gold |
| 5 | Mythical | **CONFIRMED** tier | 6 | 3.70 | `#FF4D8D` magenta-rose |
| 6 | Secret | **CONFIRMED** tier | 4 | 4.80 | `#1B1B2F` deep night with prismatic shimmer |
| | **Total** | | **60** (target **CONFIRMED**, split **PROPOSED**) | | |

## 2. Launch roster (PROPOSED)

Pool weight classes set the base weight inside a hatch pool: **Standard = 10, Scarce = 6, Elusive = 3** (see §7).

| # | Animal | Rarity | Family | Role | Home region | Pool class |
|---:|---|---|---|---|---|---|
| 1 | [[Rabbit]] | Common | Forest Animals | Skirmisher | Whisperwood Forest | Standard |
| 2 | [[Squirrel]] | Common | Forest Animals | Ranged | Whisperwood Forest | Standard |
| 3 | [[Hedgehog]] | Common | Forest Animals | Tank | Whisperwood Forest | Standard |
| 4 | [[Raccoon]] | Common | Forest Animals | Assassin | Whisperwood Forest | Scarce |
| 5 | [[Frog]] | Common | Other Animals | Controller | Whisperwood Forest | Standard |
| 6 | [[Duck]] | Common | Birds | Support | Whisperwood Forest | Standard |
| 7 | [[Woodpecker]] | Common | Birds | Skirmisher | Whisperwood Forest | Elusive |
| 8 | [[Boar]] | Common | Forest Animals | Bruiser | Whisperwood Forest | Standard |
| 9 | [[Goat]] | Common | Other Animals | Bruiser | Whisperwood Forest | Standard |
| 10 | [[Meerkat]] | Common | Safari Animals | Support | Sunscorch Savanna | Scarce |
| 11 | [[Zebra]] | Common | Safari Animals | Controller | Sunscorch Savanna | Standard |
| 12 | [[Crab]] | Common | Aquatic Animals | Tank | Coral Coast | Elusive |
| 13 | [[Fox]] | Uncommon | Forest Animals | Assassin | Whisperwood Forest | Standard |
| 14 | [[Owl]] | Uncommon | Birds | Controller | Whisperwood Forest | Scarce |
| 15 | [[Deer]] | Uncommon | Forest Animals | Support | Whisperwood Forest | Standard |
| 16 | [[Badger]] | Uncommon | Forest Animals | Bruiser | Whisperwood Forest | Standard |
| 17 | [[Beaver]] | Uncommon | Forest Animals | Tank | Whisperwood Forest | Standard |
| 18 | [[Hyena]] | Uncommon | Safari Animals | Skirmisher | Sunscorch Savanna | Standard |
| 19 | [[Flamingo]] | Uncommon | Birds | Support | Sunscorch Savanna | Scarce |
| 20 | [[Cobra]] | Uncommon | Other Animals | Ranged | Sunscorch Savanna | Standard |
| 21 | [[Monkey]] | Uncommon | Other Animals | Skirmisher | Emerald Canopy | Standard |
| 22 | [[Seal]] | Uncommon | Aquatic Animals | Controller | Coral Coast | Scarce |
| 23 | [[Penguin]] | Uncommon | Birds | Tank | Frostfang Tundra | Elusive |
| 24 | [[Wolf]] | Rare | Forest Animals | Bruiser | Whisperwood Forest | Standard |
| 25 | [[Brown Bear]] | Rare | Forest Animals | Tank | Whisperwood Forest | Standard |
| 26 | [[Cheetah]] | Rare | Big Cats | Skirmisher | Sunscorch Savanna | Standard |
| 27 | [[Kangaroo]] | Rare | Other Animals | Bruiser | Sunscorch Savanna | Standard |
| 28 | [[Leopard]] | Rare | Big Cats | Assassin | Emerald Canopy | Scarce |
| 29 | [[Toucan]] | Rare | Birds | Ranged | Emerald Canopy | Standard |
| 30 | [[Peacock]] | Rare | Birds | Support | Emerald Canopy | Scarce |
| 31 | [[Octopus]] | Rare | Aquatic Animals | Controller | Coral Coast | Standard |
| 32 | [[Walrus]] | Rare | Aquatic Animals | Tank | Frostfang Tundra | Standard |
| 33 | [[Arctic Fox]] | Rare | Other Animals | Controller | Frostfang Tundra | Elusive |
| 34 | [[Tiger]] | Epic | Big Cats | Assassin | Emerald Canopy | Standard |
| 35 | [[Gorilla]] | Epic | Other Animals | Tank | Emerald Canopy | Standard |
| 36 | [[Crocodile]] | Epic | Aquatic Animals | Controller | Emerald Canopy | Standard |
| 37 | [[Rhino]] | Epic | Safari Animals | Bruiser | Sunscorch Savanna | Standard |
| 38 | [[Hippo]] | Epic | Safari Animals | Tank | Sunscorch Savanna | Scarce |
| 39 | [[Golden Eagle]] | Epic | Birds | Skirmisher | Skyreach Peaks | Standard |
| 40 | [[Dolphin]] | Epic | Aquatic Animals | Support | Coral Coast | Standard |
| 41 | [[Electric Eel]] | Epic | Aquatic Animals | Ranged | Emerald Canopy | Scarce |
| 42 | [[Snow Leopard]] | Epic | Big Cats | Controller | Skyreach Peaks | Elusive |
| 43 | [[Lion]] | Legendary | Big Cats | Bruiser | Sunscorch Savanna | Standard |
| 44 | [[Elephant]] | Legendary | Safari Animals | Tank | Sunscorch Savanna | Standard |
| 45 | [[Great White Shark]] | Legendary | Aquatic Animals | Assassin | Coral Coast | Standard |
| 46 | [[Orca]] | Legendary | Aquatic Animals | Controller | Frostfang Tundra | Standard |
| 47 | [[Narwhal]] | Legendary | Aquatic Animals | Ranged | Frostfang Tundra | Scarce |
| 48 | [[Peregrine Falcon]] | Legendary | Birds | Skirmisher | Skyreach Peaks | Standard |
| 49 | [[Giant Panda]] | Legendary | Other Animals | Support | Skyreach Peaks | Scarce |
| 50 | [[Komodo Dragon]] | Legendary | Other Animals | Controller | Emberheart Caldera | Elusive |
| 51 | [[Sabre-Tooth Tiger]] | Mythical | Big Cats | Assassin | Emberheart Caldera | Standard |
| 52 | [[Woolly Mammoth]] | Mythical | Other Animals | Tank | Frostfang Tundra | Standard |
| 53 | [[Megalodon]] | Mythical | Aquatic Animals | Bruiser | Starfall Sanctuary | Standard |
| 54 | [[Haast's Eagle]] | Mythical | Birds | Skirmisher | Skyreach Peaks | Scarce |
| 55 | [[Blue Whale]] | Mythical | Aquatic Animals | Support | Starfall Sanctuary | Scarce |
| 56 | [[Giant Squid]] | Mythical | Aquatic Animals | Controller | Starfall Sanctuary | Elusive |
| 57 | [[Mosasaurus]] | Secret | Aquatic Animals | Assassin | Starfall Sanctuary | Standard |
| 58 | [[Quetzalcoatlus]] | Secret | Other Animals | Ranged | Starfall Sanctuary | Standard |
| 59 | [[Titanoboa]] | Secret | Other Animals | Controller | Emberheart Caldera | Scarce |
| 60 | [[Tyrannosaurus Rex]] | Secret | Other Animals | Bruiser | Emberheart Caldera | Elusive |

Family totals: Big Cats 6, Forest Animals 11, Safari Animals 6, Aquatic Animals 14, Birds 10, Other Animals 13 = 60.

> [!info] PROPOSED theme — "Ancient lineage"
> Mythical and Secret tiers lean on colossal and prehistoric animals (Sabre-Tooth Tiger, Woolly Mammoth, Megalodon, Haast's Eagle, Mosasaurus, Quetzalcoatlus, Titanoboa, Tyrannosaurus Rex). This ties the rarest eggs to "ancient eggs" fiction while keeping every animal recognisable. Needs owner approval ([[Open Questions#Q-027]]).

## 3. Animal stat model (PROPOSED)

**Reference stats** (Common, role-neutral, ascension 0):

| Stat | Reference | Unit | Notes |
|---|---:|---|---|
| Health (HP) | 200 | points | |
| Attack (ATK) | 20 | damage per basic hit | |
| Defence (DEF) | 10 | rating | Reduction = DEF / (DEF + 100) |
| Attack speed (AS) | 1.00 | basic hits per second | Not scaled by rarity |
| Movement speed (MS) | 16 | studs per second | 16 matches the default Roblox Humanoid WalkSpeed; not scaled by rarity |

**Formula:** `Stat = Reference × M(rarity) × RoleMultiplier × SpeciesTweak` (HP, ATK and DEF). AS and MS use `Reference × RoleMultiplier × SpeciesTweak`.

**Role multipliers:**

| Role | HP | ATK | DEF | AS | MS | Basic range (studs) | Design intent |
|---|---:|---:|---:|---:|---:|---:|---|
| Tank | 1.55 | 0.70 | 1.60 | 0.85 | 0.90 | 5 | Absorbs damage, draws aggro |
| Bruiser | 1.10 | 1.00 | 1.10 | 0.95 | 1.00 | 5 | Sustained melee all-rounder |
| Assassin | 0.75 | 1.45 | 0.70 | 1.05 | 1.20 | 5 | Burst damage, fragile |
| Skirmisher | 0.85 | 0.80 | 0.80 | 1.55 | 1.30 | 5 | Fast hits, mobility |
| Ranged | 0.75 | 1.15 | 0.70 | 1.00 | 1.00 | 28 | Safe damage from distance |
| Support | 1.00 | 0.65 | 1.00 | 1.00 | 1.00 | 18 | Heals or buffs; low raw power |
| Controller | 0.95 | 0.80 | 0.95 | 1.00 | 1.00 | 12 | Stuns, slows, pulls |

**Power Index (PI)** — the balance check: `PI = sqrt((ATK × AS) × (HP × (1 + DEF/100)))`, normalised so the Common reference = 1.00 per tier. Pure combat roles target PI ≈ 1.00 (±0.08). Support (≈0.81) and Controller (≈0.87) give up raw power to pay for utility. Species tweaks must keep an animal within ±0.06 of its role's PI. The [[Animal Statistics Database]] shows the PI for every animal.

**Ability scaling:** ability damage is written as a percentage of the animal's ATK. Heals are written as a percentage of the target's max HP.

## 4. Combat values (PROPOSED)

| Value | Proposal |
|---|---|
| Damage formula | `Damage = ATK × SkillMultiplier × (100 / (100 + DEF_target)) × Random(0.95, 1.05)` |
| Critical hits | None at launch |
| Wild animal HP multiplier | ×2.0 versus companion stats of the same species |
| Wild animal ATK multiplier | ×0.75 versus companion stats |
| Player HP | `100 + 12 × (Level − 1)` |
| Player DEF | `5 + 0.5 × (Level − 1)` |
| Player base Strength | `10 + 2 × (Level − 1)` |
| Player effective Strength | `BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)` |
| Player basic combo | 3 hits at Strength × 0.8 / 0.8 / 1.4; 0.45 s per hit; resets after 1.2 s idle |
| Player special — Power Strike | Strength × 3.0, single target, 6 s cooldown, unlocked at level 1 |
| Player special — Ground Slam | Strength × 2.0 to all enemies within 10 studs, 12 s cooldown, unlocked at level 10 |
| Player special — Rally Cry | Team +15% damage for 6 s, 25 s cooldown, unlocked at level 25 |
| Player dodge roll | 0.3 s invulnerability, 12-stud roll, 4 s cooldown |
| Player walk speed | 16 studs/s (Roblox default) |
| Global cooldown between manual animal abilities | 0.5 s |
| Region scaling of DEF | None. DEF is not region-scaled, so DEF/(DEF+100) stays bounded |
| Hard crowd-control cap | 1.5 s against normal enemies; reduced or converted to slows against bosses ([[Animal Abilities Catalogue]]) |
| Crowd-control diminishing returns | Hard CC on the same target within 6 s: 100% → 50% → 25% → 4 s immunity |
| Ability count by rarity | Common/Uncommon 1; Rare/Epic 2 (1 auto + 1 manual); Legendary and above 2 + passive |
| Leash range (wild animals) | 60 studs from spawn point, then reset to full HP |
| Combat tag timeout | 8 s without dealing or receiving damage |

## 5. Regions (PROPOSED — world layout is UNDECIDED, Q-001)

| # | Region | Theme | Stat and cash multiplier | Unlock requirement | Mini-boss | Recommended level |
|---:|---|---|---:|---|---|---|
| 0 | [[Hub - Hatchling Haven]] | Safe hub, egg shrine, base portals | — | Start | — | — |
| 1 | [[Region - Whisperwood Forest]] | Temperate forest | ×1.0 | Start | [[Mini-Boss - Bramblehorn]] | 1–10 |
| 2 | [[Region - Sunscorch Savanna]] | Safari grassland | ×1.5 | Level 8 + defeat Bramblehorn | [[Mini-Boss - Dustmane]] | 8–20 |
| 3 | [[Region - Emerald Canopy]] | Jungle | ×2.2 | Level 18 + defeat Dustmane | [[Mini-Boss - Vinecoil]] | 18–30 |
| 4 | [[Region - Coral Coast]] | Ocean shore and reef | ×3.2 | Level 28 + defeat Vinecoil | [[Mini-Boss - Hammertide]] | 28–42 |
| 5 | [[Region - Frostfang Tundra]] | Arctic | ×4.5 | Level 40 + defeat Hammertide | [[Mini-Boss - Rimeback]] | 40–54 |
| 6 | [[Region - Skyreach Peaks]] | Mountain | ×6.2 | Level 52 + defeat Rimeback | [[Mini-Boss - Stormtalon]] | 52–66 |
| 7 | [[Region - Emberheart Caldera]] | Volcanic lost valley | ×8.5 | Level 65 + defeat Stormtalon | [[Mini-Boss - Cinderjaw]] | 65–80 |
| 8 | [[Region - Starfall Sanctuary]] | Special endgame (celestial archipelago) | ×11.5 | Level 80 + defeat Cinderjaw + defeat at least 2 different world bosses | [[Mini-Boss - Eclipse Panther]] | 80–100 |

The region multiplier applies to wild animal HP and ATK (on top of the §4 wild multipliers) and to cash and XP rewards.

**World bosses (PROPOSED):**

| World boss | Base animal | Home | Recommended level | Spawn cadence |
|---|---|---|---:|---|
| [[World Boss - Ironbark Colossus]] | Ancient tortoise with a forest on its shell | Whisperwood–Savanna border | 15 | Every 45 min per server, announced 2 min ahead |
| [[World Boss - Thunderhoof]] | Colossal storm elephant | Sunscorch Savanna | 30 | Every 50 min |
| [[World Boss - Abyssal Leviathan]] | Giant whale | Coral Coast | 45 | Every 55 min |
| [[World Boss - Ashwing Condor]] | Ember-feathered giant condor | Emberheart Caldera / Skyreach Peaks rim | 70 | Every 60 min |

Mini-boss respawn: 10 min per server instance. Reward eligibility: once per player per spawn (rewards are UNDECIDED, Q-015).

## 6. Wild rewards and respawn (PROPOSED)

| Rarity | Base cash per defeat | Base XP per defeat | Respawn time | Wild spawn behaviour |
|---|---:|---:|---|---|
| Common | 10 | 10 | 20 s | Fixed spawn points |
| Uncommon | 16 | 15 | 35 s | Fixed spawn points |
| Rare | 28 | 25 | 60 s | Fixed spawn points, fewer of them |
| Epic | 50 | 45 | 120 s | Dedicated points |
| Legendary | 95 | 80 | 300 s | Single point per region; 50% chance per respawn window |
| Mythical | 190 | 150 | 900 s window | Rare-spawn event: 25% chance per window, announced to the server |
| Secret | 400 | 300 | 2,700 s window | Rare-spawn event: 10% chance per window, announced to the server |

`Cash = BaseCash × RegionMultiplier × (1 + CashBonuses)`. `XP = BaseXP × RegionMultiplier`.

Kill credit in multiplayer: every player who dealt at least 10% of the target's max HP (directly or through their animals) within the combat-tag window receives the **full** reward. This avoids kill-stealing. (**PROPOSED**)

## 7. Eggs, rolls and hatching

| Value | Status | Proposal |
|---|---|---|
| Egg roll price | **PROPOSED** | 200 Cash per roll, flat. Pricing model is UNDECIDED (Q-020) |
| Bulk roll | **PROPOSED** | Roll ×5 for 1,000 Cash (no discount; convenience only) |
| Baseline egg-rarity odds | **PROPOSED** (owner-supplied provisional values) | 65 / 22 / 9 / 3 / 0.8 / 0.18 / 0.02 % |
| Maximum simultaneous hatch | **CONFIRMED** | 5 eggs |
| Hatch presentation time | **PROPOSED** | Instant result, 3.5 s single-egg animation, 5.0 s for a multi-hatch (skippable after first viewing). Timed incubation is an alternative (Q-023) |
| Hatch location | **PROPOSED** | Backpack eggs: anywhere outside combat. Base-stored eggs: only at the player's base |
| Pool weight classes | **PROPOSED** | Standard 10, Scarce 6, Elusive 3 |
| Animal storage capacity | **UNDECIDED** (Q-022) | Working assumption for prototyping: 100 owned animals |

## 8. Dynamic progression luck (PROPOSED — final formula UNDECIDED, Q-017)

**Progression Score (PS)**, range 0–1000:

| Input | Points | Maximum |
|---|---|---:|
| Player level | 4 per level (level 100 cap) | 400 |
| Unique animals discovered (index) | 3 per species | 180 |
| Mini-bosses defeated (unique) | 10 each (8) | 80 |
| World bosses defeated (unique) | 20 each (4) | 80 |
| Regions unlocked beyond the first | 20 each (7) | 140 |
| Base progression | `round(120 × TotalModuleLevels / MaxModuleLevels)` | 120 |
| **Total** | | **1000** |

Normalised progression: `P = clamp(PS / 1000, 0, 1)`. The baseline table applies at the **pivot P₀ = 0.30**.

**Egg-rarity weights:** `w_r(P) = Base_r × (1 + s_r × (P − 0.30))`, then normalise so all seven sum to 100%.

| Rarity | Base_r (%) | Slope s_r | Multiplier at P = 0 | Multiplier at P = 1 |
|---|---:|---:|---:|---:|
| Common | 65 | 0.0 | 1.00 | 1.00 |
| Uncommon | 22 | 0.6 | 0.82 | 1.42 |
| Rare | 9 | 1.2 | 0.64 | 1.84 |
| Epic | 3 | 1.8 | 0.46 | 2.26 |
| Legendary | 0.8 | 2.4 | 0.28 | 2.68 |
| Mythical | 0.18 | 2.8 | 0.16 | 2.96 |
| Secret | 0.02 | 3.2 | 0.04 | 3.24 |

**Hatch-pool weights:** `w_i(P) = ClassWeight_i × (1 + H × (P − 0.30) × Tilt_i)`, normalised within the pool. `H = 1.0`. `Tilt`: Standard 0, Scarce 0.5, Elusive 1.0.

**Disclosure rule (CONFIRMED principle):** the server computes the player's current odds and the client shows them before every roll or hatch is committed. The server issues an `oddsVersion` token with the displayed odds. If the odds change before confirmation (for example the player levels up), the server rejects the stale token and the client re-displays the new odds.

## 9. Ascension (PROPOSED — levels Q-004, duplicates Q-005)

Five ascension levels, A1–A5, shown as stars.

| Rarity | Duplicates for A1 / A2 / A3 / A4 / A5 | Total duplicates | Cash fee per step *n* |
|---|---|---:|---|
| Common | 1 / 2 / 3 / 4 / 5 | 15 | 100 × n |
| Uncommon | 1 / 2 / 3 / 3 / 4 | 13 | 200 × n |
| Rare | 1 / 1 / 2 / 3 / 3 | 10 | 400 × n |
| Epic | 1 / 1 / 2 / 2 / 3 | 9 | 800 × n |
| Legendary | 1 / 1 / 1 / 2 / 2 | 7 | 1,600 × n |
| Mythical | 1 / 1 / 1 / 1 / 2 | 6 | 3,200 × n |
| Secret | 1 / 1 / 1 / 1 / 1 | 5 | 6,400 × n |

| Effect per ascension level | Proposal |
|---|---|
| HP, ATK, DEF | +8% of base per level (A5 = +40%) |
| Ability effectiveness (damage, heal, duration) | +5% per level (A5 = +25%) |
| Visual tier | A1 coloured trim; A2 rarity-coloured eye glint; A3 soft aura; A4 particle accents; A5 crest and full aura |

## 10. Egg merging and the Egg Merging Station

| Rule | Status |
|---|---|
| 3 eggs of the same rarity → 1 egg of the next rarity | **CONFIRMED** |
| Requires a purchased Egg Merging Station | **CONFIRMED** |
| Higher rarities need station upgrades | **CONFIRMED** |
| Station appearance changes per upgrade | **CONFIRMED** |
| Secret eggs cannot be merged further | **CONFIRMED** (no rarity above Secret) |
| All levels, costs, fees and gates below | **PROPOSED** (Q-019) |

| Station level | Name | Cost (Cash) | Extra gate | Merges unlocked | Merge fee (Cash) |
|---:|---|---:|---|---|---|
| 1 | Twig Nest Press | 2,500 | — | Common→Uncommon; Uncommon→Rare | 100; 300 |
| 2 | Stonebound Hatchery Forge | 15,000 | Region 2 unlocked | Rare→Epic | 900 |
| 3 | Crystal Incubator | 60,000 | Region 4 unlocked | Epic→Legendary | 2,700 |
| 4 | Aurora Crucible | 250,000 | Region 6 unlocked + 1 world boss defeated | Legendary→Mythical | 8,000 |
| 5 | Celestial Convergence Altar | 1,000,000 | Region 8 unlocked | Mythical→Secret | 25,000 |

Merging happens at the player's base. Input eggs may come from the backpack or base storage. The output egg goes to base storage (capacity always frees by two). Merge presentation: 2.5–6 s animation by tier, no wait timer (timers are an alternative, Q-034).

## 11. Egg storage (CONFIRMED start values; expansion PROPOSED / UNDECIDED)

| Location | Start capacity | Stealable | Expansion step (PROPOSED) | Max (PROPOSED) | Currency and price |
|---|---:|---|---|---:|---|
| Backpack | 10 (**CONFIRMED**) | Never (**CONFIRMED**) | +5 per step, 3 steps | 25 | **UNDECIDED** (Q-009, Q-010) |
| Base storage (Egg Vault) | 50 (**CONFIRMED**) | During an eligible raid (**CONFIRMED**) | +25 per step, 6 steps | 200 | **UNDECIDED** (Q-009, Q-010) |

## 12. Base modules (PROPOSED — availability Q-007)

Upgrade cost: `Cost(L) = BaseCost × 2.5^(L − 1)` for L = 1–5 (L1 = construction).

| Module | Base cost | L1 | L2 | L3 | L4 | L5 | Effect summary |
|---|---:|---:|---:|---:|---:|---:|---|
| [[Module - Animal Pens]] | 1,000 | 1,000 | 2,500 | 6,250 | 15,625 | 39,063 | Owned-animal housing and guard posts (display rule Q-008) |
| [[Module - Egg Vault]] | 1,500 | 1,500 | 3,750 | 9,375 | 23,438 | 58,594 | Base egg storage security and visuals; capacity expansion is separate (Q-009) |
| [[Module - Defence Station]] | 2,000 | 2,000 | 5,000 | 12,500 | 31,250 | 78,125 | Barricades, traps, turrets |
| [[Module - Shield Generator]] | 2,500 | 2,500 | 6,250 | 15,625 | 39,063 | 97,656 | Raid shield duration and recharge |
| [[Module - Training Grounds]] | 1,500 | 1,500 | 3,750 | 9,375 | 23,438 | 58,594 | +5% player Strength and +4% equipped animal stats per level |
| [[Module - Multiplier Shrine]] | 3,000 | 3,000 | 7,500 | 18,750 | 46,875 | 117,188 | +10% Cash per level |
| [[Module - Trophy Hall]] | 1,000 | 1,000 | 2,500 | 6,250 | 15,625 | 39,063 | Boss trophies; +1% Cash per unique boss trophy displayed (max 12%) |
| [[Egg Merging Station]] | see §10 | | | | | | 5 levels |
| Plot Expansion (see [[Base Layout and Plot Expansion]]) | 5,000 × 3^(n−1) | 5,000 | 15,000 | 45,000 | 135,000 | — | 4 stages; unlocks module slots |

Max module levels for the PS calculation: 7 modules × 5 + Egg Merging Station 5 + Plot Expansion 4 = **44**.

## 13. Player progression (PROPOSED)

| Value | Proposal |
|---|---|
| Level cap | 100 |
| XP to reach next level | `XP(L) = round(100 × L^1.6)` |
| Specials unlock | Power Strike L1; Ground Slam L10; Rally Cry L25 |

## 14. Variants (CONFIRMED to exist; acquisition UNDECIDED, Q-006)

Variant names (examples from the owner): Golden, Diamond, Rainbow, Shadow, Neon. Eligibility per species is listed in [[Animal Variants]] (**PROPOSED**). Whether variants have stat bonuses is UNDECIDED (Q-024).

## 15. Server and performance targets (PROPOSED)

| Value | Proposal |
|---|---|
| Max players per server | 16 (Q-031) |
| Active wild animals per server | ≤ 180 simulated; ≤ 60 with full AI near players |
| Companion animals per player | 3 (team) |
| Target client frame rate | 60 FPS on mid-range PC; 30 FPS minimum on mid-range mobile |

## 16. Animal model budgets (PROPOSED)

| Rarity | LOD0 triangle budget | LOD1 | LOD2 | Production priority |
|---|---:|---:|---:|---|
| Common | 1,500 | 50% | 20% | P0 |
| Uncommon | 2,000 | 50% | 20% | P0 |
| Rare | 2,500 | 50% | 20% | P1 |
| Epic | 3,500 | 50% | 20% | P1 |
| Legendary | 4,500 | 50% | 20% | P1 |
| Mythical | 6,000 | 50% | 20% | P2 |
| Secret | 7,500 | 50% | 20% | P2 |
