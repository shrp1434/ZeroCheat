---
title: Content Expansion Guidelines
type: guideline
category: live-ops
status: mixed
priority: P1
owner: Live Operations Director
last_updated: 2026-11-14
tags:
  - live-ops
  - content
  - hatch-pools
  - odds-disclosure
  - compliance
---

# Content Expansion Guidelines

Rules for adding content after launch: animals, variants, bosses, areas, eggs and base modules. The aim is to grow the game without breaking balance, odds disclosure, saved data or the game's identity. The process that carries content from idea to release is in [[Content Update Pipeline]].

> [!success] CONFIRMED constraints no expansion may break
> - Seven rarities only: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret. No new rarity tier.
> - Team size exactly three. Hatch up to five at once. Merge is three of one rarity into one of the next.
> - Storage starts at backpack 10 + base 50 = 60; backpack eggs are never stealable.
> - Raids: maximum three animals stolen per successful raid; offline bases never raidable; undefeated defenders never stealable.
> - Hatches are independent (D-018). Hidden luck never changes wild encounter rarity (D-017). Actual odds are shown before commit and never changed silently after purchase (D-017).
> - Visual direction: colourful, polished, low-poly; no horror, no meme animals (D-026).

## General rules for every expansion

1. **One owning document per new thing.** A new animal gets an animal document from [[Template - Animal]]; a new boss from [[Template - Boss]]; a new region from [[Template - World Region]]; a new egg from [[Template - Egg]]. The update itself is described with [[Template - Update]].
2. **Numbers come from the models.** Stats from [[Animal Stat Budget Model]], costs from the formulas in [[Canonical Proposed Values]]. New values are added to the canonical page first.
3. **Asset IDs continue the register.** New animals take the next ANM-### after ANM-060, new bosses the next BOS-##, and so on ([[Asset Register]], [[Asset Naming Conventions]]).
4. **Save data is migrated, never broken.** Any new field gets a default and a migration step in [[Data Validation and Migration]].
5. **Any change to a random outcome is an odds change.** It follows the hatch-pool rules below, even when the change looks cosmetic.
6. **Any change to a Progression Score input range is an odds change.** See [[#Content that changes the Progression Score]].

## Adding an animal

| Step | Rule | Reference |
|---|---|---|
| Identity | A real, recognisable animal; colourful low-poly; not a meme or horror creature; not a copy of another game's creature | [[Animal Modelling Principles]], [[Design Inspiration Notes]] |
| Rarity | One of the seven tiers. Higher tiers keep the escalation theme in use (ancient lineage is **PROPOSED**, [[Open Questions#Q-027]]) | [[Egg Rarity System]] |
| Role and family | One of the seven roles; one family; justify against current role counts in its pool | [[Animal Roles]], [[Animal Families]] |
| Home region | An existing region (or the new region it ships with) | [[World Overview and Map]] |
| Pool class | Standard, Scarce or Elusive | [[Canonical Proposed Values#7. Eggs, rolls and hatching]] |
| Stats | `Reference × M(rarity) × RoleMultiplier × SpeciesTweak`; Power Index inside the role band | [[Animal Stat Budget Model]], [[Animal Statistics Database]] |
| Abilities | Use existing ability archetypes before inventing a new mechanic; a new mechanic needs its own design review | [[Animal Abilities Catalogue]] |
| Rig and animation | Reuse a body-plan rig where possible | [[Animal Rig Standards]] |
| VFX and audio | Rarity effects, vocalisations | [[VFX - Rarity and Variant Effects]], [[Sound - Animal Vocalisations]] |
| Index | New index entry; discovered and owned states | [[Animal Index Feature Specification]] |
| Spawning | Wild spawn point and respawn time by rarity | [[Wild Animal Spawning and Respawn]] |
| Hatch pool | Follow the next section in full | — |

## Adding an animal without breaking hatch pools

Adding an animal to a rarity changes that rarity's hatch pool. Every existing animal in the pool becomes slightly less likely. This is legitimate, but only if it is done openly and correctly.

> [!danger] Mandatory rules — release blockers
> 1. **Re-normalise every affected pool** so that the probabilities sum to exactly 100% (internally to floating-point tolerance) at every progression level.
> 2. **Re-verify every affected pool** with the automated sum check and the sampling tests in [[Statistical Testing of Probabilities]], at every sample progression level used in [[Hatch Pool Tables]].
> 3. **Update the odds disclosure before release.** The hatch screen and any odds page show the new pool, including the new animal, from the first moment the new pool is live.
> 4. **Bump the odds-table version** (`oddsTableVersion`, see [[Versioning and Changelog Policy#Config versions]]). Every `oddsVersion` token issued under the old table is rejected after the switch, and the client re-displays the new odds before the player can commit (D-041).
> 5. **Announce the change in advance** in-game and in the patch notes, listing which pools change.
> 6. **Never change an outcome already committed.** A roll or hatch committed under the old table resolves under the old table.
> 7. **The egg-rarity table is untouched** by adding an animal; only the pool of that animal's rarity changes. If both change in one update, both get re-verified and the version bumps once for the combined table.

### Worked example: a new Common animal (Standard class)

The launch Common pool (**PROPOSED**, [[Canonical Proposed Values#2. Launch roster (PROPOSED)]]) has 8 Standard, 2 Scarce and 2 Elusive animals. Class weights: Standard 10, Scarce 6, Elusive 3. Hatch-pool weights use `w_i(P) = ClassWeight_i × (1 + H × (P − 0.30) × Tilt_i)` with H = 1.0 and Tilt Standard 0, Scarce 0.5, Elusive 1.0 ([[Canonical Proposed Values#8. Dynamic progression luck (PROPOSED — final formula UNDECIDED, Q-017)]]).

At the pivot P = 0.30 the tilt term is zero:

| Pool state | Total weight | Each Standard | Each Scarce | Each Elusive | Sum check |
|---|---:|---:|---:|---:|---|
| Launch (12 animals) | 8×10 + 2×6 + 2×3 = **98** | 10.204% | 6.122% | 3.061% | 8×10.204 + 2×6.122 + 2×3.061 = 100.000% (to rounding) |
| After adding one Standard (13 animals) | 9×10 + 2×6 + 2×3 = **108** | 9.259% | 5.556% | 2.778% | 9×9.259 + 2×5.556 + 2×2.778 = 100.000% (to rounding) |

The same check must run at the other sample levels. At P = 1.0 (Scarce weight 8.1, Elusive 5.1):

| Pool state | Total weight | Each Standard | Each Scarce | Each Elusive |
|---|---:|---:|---:|---:|
| Launch | 106.4 | 9.398% | 7.613% | 4.793% |
| After adding one Standard | 116.4 | 8.591% | 6.959% | 4.381% |

Two things to communicate from this example:
- Every existing Common animal is now less likely (a Standard animal drops from about 10.2% to about 9.3% at the pivot). Players chasing duplicates for ascension will notice. The patch notes must say so plainly.
- Displayed percentages are rounded, so the displayed column may sum to 99.99% or 100.01%. The internal values sum to 100%. How rounding is displayed is owned by [[Randomised Reward Compliance]].

### Verification hook (illustrative Luau)

> [!info] Illustrative Luau, not run in Roblox Studio
> A build-time check that every pool sums to 1 at every sample progression level. The weight function is the one specified in [[Implementation - Dynamic Luck Calculation]]; the names here are placeholders.

```lua
-- Illustrative only. Fails the build if any pool does not normalise to 1.
local SAMPLE_P = { 0.0, 0.15, 0.30, 0.5, 0.75, 1.0 } -- use the levels in Hatch Pool Tables
local TOLERANCE = 1e-9

local function verifyPools(pools, weightFn)
	for rarity, members in pairs(pools) do
		for _, p in ipairs(SAMPLE_P) do
			local total = 0
			for _, animal in ipairs(members) do
				total += weightFn(animal.poolClass, p)
			end
			local sum = 0
			for _, animal in ipairs(members) do
				sum += weightFn(animal.poolClass, p) / total
			end
			assert(math.abs(sum - 1) <= TOLERANCE,
				string.format("Pool %s does not sum to 1 at P=%.2f (sum=%.12f)", rarity, p, sum))
		end
	end
end
```

The tolerance of `1e-9` is a local **PROPOSED** value for floating-point checks.

### Open questions on pool expansion

> [!warning] UNDECIDED
> - **UNDECIDED** (Q-1106): how post-launch animals enter pools. Options: (A) join the standard rarity pools, diluting existing animals as in the example; (B) appear only in new themed eggs with their own pools, leaving standard pools untouched; (C) a mix. Also whether an animal may ever be retired from a pool. **Recommendation (PROPOSED):** prefer B for event or themed animals and A for permanent roster growth, with retirement avoided.
> - **UNDECIDED** (Q-1118): whether unhatched eggs owned before a pool change hatch under the pool current at hatch time (simple; the hatch screen shows current odds before commit) or under the pool in force when the egg was rolled (preserves expectations; needs eggs to store a pool version). The hatch commit always shows the odds it will use, whichever option is chosen.

## Content that changes the Progression Score

The Progression Score has fixed maximums per input ([[Progression Score Specification]]). Adding content can change those maximums, which shifts every player's P and therefore everyone's displayed odds.

| Content added | Input affected | Required action |
|---|---|---|
| New animal species | Unique animals discovered (3 points each, 180 max at 60 species) | Decide whether the cap changes; if the formula changes, it is an odds change for all players |
| New mini-boss or world boss | Bosses defeated | Same |
| New region | Regions unlocked | Same |
| New base module or module level | Base progression (`TotalModuleLevels / MaxModuleLevels`, 44 at launch) | A larger denominator lowers every player's base component; treat as an odds change |

> [!danger] Rule
> Any change to a Progression Score input range bumps `oddsTableVersion`, is re-verified across [[Dynamic Luck Probability Tables]] and is announced in advance. No player's displayed odds may change without that process. The final formula is **UNDECIDED** ([[Open Questions#Q-017]]).

## Adding variants

- Variants exist (D-028 **CONFIRMED**); acquisition is **UNDECIDED** ([[Open Questions#Q-006]]) and stat effects are **UNDECIDED** ([[Open Questions#Q-024]]). Until both are decided, new variants are material sets (VAR-###) only.
- If variants are ever obtained randomly, the variant chance is part of the disclosed odds and follows every hatch-pool rule above.
- Visual rules: [[Variant Visual Treatments]]. Eligibility per species: [[Animal Variants]].

## Adding bosses

- Use [[Template - Boss]] and the framework in [[Boss Design Overview]] and [[Boss AI]].
- Every attack has a telegraph readable in a full server ([[Combat Feedback and Readability]]).
- Rewards follow the reward structure decided under [[Open Questions#Q-015]]; until then, reward tables are placeholders.
- A new boss that counts towards the Progression Score triggers the rule above.

## Adding areas

- A new region is a **major expansion** and is planned as its own milestone with the structure of [[M16 - World Design]].
- It needs an unlock gate that continues [[Region Unlock Progression]], a spawn table, a mini-boss, hazards and its own art kit.
- Region multipliers continue the existing curve; the new value is added to [[Canonical Proposed Values]] first.
- Wild encounter rarity in the new region is set only by its spawn table, never by player luck.

## Adding eggs

- **No new rarity tier.** Seven rarities are **CONFIRMED**.
- New egg *types* (for example a themed egg) are **UNDECIDED** (Q-1114). If approved, each has its own disclosed rarity table and pools, its own odds-table entry, and explicit rules for storage, stealability in raids and merging.
- Egg art follows [[Egg Art Direction]]; each new egg type has an owning document from [[Template - Egg]].

## Adding base modules

- New modules follow the cost curve shape in [[Canonical Proposed Values#12. Base modules (PROPOSED — availability Q-007)]] and the module structure in [[Player Base System]].
- A module must not make raids unwinnable or make the **CONFIRMED** three-animal theft cap (D-024) or the egg theft limit, once decided (Q-013), irrelevant.
- A module that adds levels changes `MaxModuleLevels`; treat it as an odds change (see above).
- Every level has a visible change, as for launch modules ([[Base Art Direction]]).

## Related documents
- [[Live Operations Index]]
- [[Live Operations Framework]]
- [[Content Update Pipeline]]
- [[Versioning and Changelog Policy]]
- [[Hatch Pool Tables]]
- [[Randomised Reward Compliance]]
- [[Statistical Testing of Probabilities]]
- [[Template - Update]]
