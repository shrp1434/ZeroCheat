---
title: Egg Rarity System
type: system
category: eggs
status: mixed
priority: P0
owner: Systems Designer
last_updated: 2026-11-14
tags:
  - eggs
  - rarity
  - data
---

# Egg Rarity System

Rarity is the single most important attribute of an egg. It is decided by the roll (stage 1 of the two-stage randomness, D-015), fixed for the egg's lifetime unless the egg is merged, and it determines which hatch pool the egg draws from (stage 2). Animals carry the same rarity as the pool they hatched from.

> [!success] CONFIRMED
> Seven rarities exist, in this order: **Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret** (D-003). Merging moves an egg exactly one step up this ladder (D-020). Nothing exists above Secret, so Secret eggs cannot be merged.

## 1. Rarity ladder

| Index | Rarity | Status of tier | Pool size (PROPOSED, D-030) | Pool weight total at P = 0.30 | Baseline egg odds (PROPOSED, D-031) | Tier stat multiplier *M* (PROPOSED) | Colour key (PROPOSED) | Egg document |
|---:|---|---|---:|---:|---:|---:|---|---|
| 0 | Common | **CONFIRMED** | 12 | 98 | 65 % | 1.00 | `#9AA5B1` | [[Common Egg]] |
| 1 | Uncommon | **CONFIRMED** | 11 | 91 | 22 % | 1.30 | `#4CC26A` | [[Uncommon Egg]] |
| 2 | Rare | **CONFIRMED** | 10 | 85 | 9 % | 1.70 | `#3D8BFF` | [[Rare Egg]] |
| 3 | Epic | **CONFIRMED** | 9 | 75 | 3 % | 2.20 | `#A55BFF` | [[Epic Egg]] |
| 4 | Legendary | **CONFIRMED** | 8 | 65 | 0.8 % | 2.85 | `#FFB020` | [[Legendary Egg]] |
| 5 | Mythical | **CONFIRMED** | 6 | 45 | 0.18 % | 3.70 | `#FF4D8D` | [[Mythical Egg]] |
| 6 | Secret | **CONFIRMED** | 4 | 29 | 0.02 % | 4.80 | `#1B1B2F` + prismatic shimmer | [[Secret Egg]] |
| | **Total** | | **60** | | **100 %** | | | |

Check: 65 + 22 + 9 + 3 + 0.8 + 0.18 + 0.02 = **100.00 %**.

Pool weight totals come from the pool classes in [[Canonical Proposed Values]] §2 (Standard 10, Scarce 6, Elusive 3). For example, the Common pool has 8 Standard, 2 Scarce and 2 Elusive animals: 8 × 10 + 2 × 6 + 2 × 3 = 98. Per-animal odds are in each egg document and in [[Hatch Pool Tables]].

## 2. What rarity controls

| System | Effect of rarity | Owning document |
|---|---|---|
| Egg roll | Probability of receiving the rarity (luck-adjusted) | [[Egg Roll System]], [[Dynamic Progression Luck]] |
| Hatch | Which pool is sampled | [[Hatch System]] |
| Animal stats | Tier multiplier *M* on HP, ATK and DEF | [[Animal Stat Budget Model]] |
| Ascension | Duplicates and fees per step fall as rarity rises | [[Ascension Progression Table]] |
| Merging | Station level needed; merge fee | [[Egg Merging Station]] |
| Wild rewards | Cash, XP and respawn of wild animals of that rarity | [[Wild Animal Cash Rewards]], [[Wild Animal Spawning and Respawn]] |
| Presentation | Egg model, colour, materials, particles, sounds, animation length | [[Rarity Visual Language]], [[Egg Art Direction]], [[Egg Animations]] |

> [!info] Rarity of wild encounters is separate
> Wild spawn rarity is governed by [[Wild Animal Spawning and Respawn]]. Progression luck does **not** touch it (D-017). An egg's rarity and a wild animal's rarity share the same ladder and colour key, but never share odds.

## 3. "Value" of a rarity in Common-equivalents

Because merging is a fixed 3 → 1 exchange, a rarity-*r* egg is worth exactly **3^r Common eggs** in merge terms. This is the natural unit for comparing rarities.

| Rarity | Common-equivalents (3^r) | Expected direct rolls to obtain one at P = 0.30 (1 / p) | Rolls via full merging at P = 0.30 |
|---|---:|---:|---:|
| Common | 1 | 1.54 | 1.54 |
| Uncommon | 3 | 4.5 | 2.29 |
| Rare | 9 | 11.1 | 4.25 |
| Epic | 27 | 33.3 | 9.22 |
| Legendary | 81 | 125 | 22.6 |
| Mythical | 243 | 556 | 60.5 |
| Secret | 729 | 5,000 | 175 |

The gap between the two right-hand columns is the merge shortcut. It is analysed, including fees, in [[Egg Merging#Merge shortcut analysis]].

## 4. Data representation (PROPOSED)

Rarity is stored as an integer index 0–6, never as a display string, so that ordering, merging (`rarity + 1`) and comparisons are trivial and localisation-safe.

```lua
-- Illustrative Luau (not executed). Shared configuration module.
local Rarity = table.freeze({
	Common = 0, Uncommon = 1, Rare = 2, Epic = 3,
	Legendary = 4, Mythical = 5, Secret = 6,
})

local RarityInfo = table.freeze({
	[0] = { key = "Common",    colour = Color3.fromHex("9AA5B1"), multiplier = 1.00 },
	[1] = { key = "Uncommon",  colour = Color3.fromHex("4CC26A"), multiplier = 1.30 },
	[2] = { key = "Rare",      colour = Color3.fromHex("3D8BFF"), multiplier = 1.70 },
	[3] = { key = "Epic",      colour = Color3.fromHex("A55BFF"), multiplier = 2.20 },
	[4] = { key = "Legendary", colour = Color3.fromHex("FFB020"), multiplier = 2.85 },
	[5] = { key = "Mythical",  colour = Color3.fromHex("FF4D8D"), multiplier = 3.70 },
	[6] = { key = "Secret",    colour = Color3.fromHex("1B1B2F"), multiplier = 4.80 },
})

local MAX_RARITY = 6 -- Secret: merge input rejected at this index
```

Configuration lives in [[Configuration Modules]]. Validation rule: any rarity value from a client is ignored; the server reads rarity only from the persisted egg record.

## 5. Accessibility of rarity cues

Colour alone must never be the only signal (see [[UI Accessibility Standards]]). Each rarity has:

1. A distinct egg **silhouette feature** (sprout, facets, crystals, halo, orbiting fragments, split shell; see each egg document).
2. A **text label** and an icon pip count (1–7 pips, PROPOSED) wherever the rarity is shown.
3. A distinct **sound signature** that rises in pitch and layering by rarity ([[Sound - Eggs]]).

## 6. Edge cases

| Case | Behaviour | Status |
|---|---|---|
| A config update changes pool contents | Existing eggs keep their rarity; hatch pools at hatch time apply (see Q-302 in [[Hatch System]]) | **PROPOSED** |
| A new rarity is requested in future | Not allowed without an owner decision; seven tiers are **CONFIRMED** | **CONFIRMED** |
| Client sends a rarity in a merge request | Ignored; server derives rarity from the egg IDs | **PROPOSED** |
| Secret egg placed in the merge station | Rejected with "Secret is the highest rarity" | **CONFIRMED** rule, **PROPOSED** copy |

## Related documents
- [[Egg System Overview]] · [[Eggs and Hatching Index]]
- [[Egg Roll System]] · [[Hatch System]] · [[Hatch Pool Tables]] · [[Dynamic Luck Probability Tables]]
- [[Rarity Visual Language]] · [[Egg Art Direction]]
- [[Animal Index]] · [[Animal Stat Budget Model]]
- [[Canonical Proposed Values]]
