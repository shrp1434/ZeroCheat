---
title: Monetisation Product Concepts
type: spec
category: monetisation
status: proposed
priority: P1
owner: Monetisation Designer
last_updated: 2026-11-14
tags:
  - monetisation
  - products
  - cosmetics
  - game-passes
---

# Monetisation Product Concepts

Candidate Robux products, each checked against [[Monetisation Principles]]. **All products and all Robux prices on this page are PROPOSED.** Prices are starting points for testing, not decisions.

> [!success] CONFIRMED constraint (D-027)
> Fully playable without Robux; no essential progression behind purchases; paid random rewards are not the main revenue mechanism.

> [!warning] Do not sell
> - Cash, Cash multipliers or anything that converts to Cash (D-044, **PROPOSED**; [[Open Questions#Q-032]]).
> - Animal variants: acquisition is **UNDECIDED** ([[Open Questions#Q-006]]) and stat effects are **UNDECIDED** ([[Open Questions#Q-024]]). No variant may be sold until both are decided.
> - Shields, defence, vault security or backpack storage (pay-to-protect; see [[Storage Expansion Economics]]).
> - Luck, odds or Progression Score.

## 1. Product catalogue

Status column: **Allowed** = passes all principles; **Review** = needs an owner decision; **Rejected** = fails a principle.

### Player cosmetics (developer products or catalogue-style items)

| Product | Description | Price (Robux, PROPOSED) | Status |
|---|---|---:|---|
| Explorer outfits | Themed player outfits (Ranger, Coral Diver, Peak Climber) | 149–299 | Allowed |
| Trails | Trail instance behind the player (petals, snowflakes, embers) | 75–149 | Allowed |
| Emotes | Victory and greeting emotes | 49–99 | Allowed |
| Name plates | Decorative frame around the player name | 99 | Allowed |
| Hatch Theatre themes | Alternative hatch staging (stage curtains, campfire, starfield). Odds, timing and results identical; result reveal never obscured | 199 each | Allowed |

### Animal cosmetics

| Product | Description | Price (Robux, PROPOSED) | Status |
|---|---|---:|---|
| Accessories | Collars, scarves, tiny hats that respect silhouettes ([[Animal Modelling Principles]]); never change rarity colours | 49–149 | Allowed |
| Name tags | Rename an owned animal (text filtered via TextService; see [[Roblox Monetisation Policy Requirements]]) | 25 per rename or pass below | Allowed |
| Variant-like material skins | Golden or Neon-style surface skins | — | **Rejected** until Q-006 and Q-024 are decided; they would pre-empt the variant system |

### Base cosmetics

| Product | Description | Price (Robux, PROPOSED) | Status |
|---|---|---:|---|
| Module skins | Theme packs per module (e.g. "Coral Reef" Egg Vault) that keep the level silhouette readable ([[Base Upgrade System]] visual ladder) | 149–299 per module, 799 for a full set | Allowed |
| Shield tints | Dome colour; transparency and shimmer unchanged so raiders can always see a shield | 99 | Allowed |
| Decor packs | Props for the decor ring (lanterns, flower beds, statues) | 99–249 | Allowed |
| Plot terrain themes | Snowy, autumn, sakura ground palettes | 249 | Allowed |
| Showcase plinths | Decorative stands for pen showcase animals (does not add showcase spots) | 99 | Allowed |

### Game passes (one-time)

| Pass | Contents | Price (Robux, PROPOSED) | Status |
|---|---|---:|---|
| Supporter Pass | Supporter chat tag (TextChatService), gold name plate, one exclusive emote and a base banner. No power | 399 | Allowed |
| Base Decorator Pass | +20 decor placement slots, colour picker for decor | 249 | Allowed |
| Team Presets Pass | Save up to 5 team presets. Presets can only be **applied at the base** (D-010 unchanged) | 149 | Allowed (convenience) |
| Name Tag Pass | Unlimited animal renames | 149 | Allowed |
| Hatch Theatre Collection | All current hatch themes | 499 | Allowed |

### Optional boosts

| Boost | Effect | Price (Robux, PROPOSED) | Status | Reason |
|---|---|---:|---|---|
| Cash boost | ×2 Cash for 30 minutes | — | **Rejected** | Makes Cash indirectly purchasable (D-044, Q-032); egg rolls could then count as paid random items |
| Luck boost | Better egg odds | — | **Rejected** | Sells odds; conflicts with D-017 disclosure model and P2 |
| XP boost | ×1.5 XP for 30 minutes | 49 (if approved) | **Review** (Q-410) | XP raises level, which raises Progression Score and therefore odds, and shortens region gates. Indirect luck and progression purchase |
| Party Cheer | Server-wide fireworks and confetti with the buyer's name; everyone in the server gets a free cosmetic confetti emote for the session | 25 | Allowed | Social, no power |
| Shield top-up | Extra shield time | — | **Rejected** | Pay-to-protect (P5) |

> [!info] PROPOSED recommendation on boosts
> Launch with **no power boosts at all**. Only the social Party Cheer. Revisit the XP boost after beta, with the owner, once Q-032 and Q-410 are decided.

### Convenience

| Product | Status | Note |
|---|---|---|
| Fast travel between unlocked regions | **Not sold**: free for everyone (waystones) | Time savings convert into Cash |
| Remote egg deposit to base | **Not sold** and not built | Would let players hide eggs from raids remotely, or put eggs at risk unknowingly |
| Extra hatch slots (more than 5 at once) | **Rejected** | The 5-egg limit is **CONFIRMED** (D-016) |
| Skip hatch animation | **Free** after first viewing (canonical §7) | — |
| Private servers | **Review** (Q-413) | If offered, PROPOSED 100 Robux per month; same rules and rewards as public servers |

## 2. Implementation notes

- Developer products use `MarketplaceService.ProcessReceipt`. The handler must be idempotent: record `PurchaseId` in the player's profile (or a purchase-history DataStore) **before** returning `PurchaseGranted`, and return `NotProcessedYet` if the profile is not loaded.
- Game passes: check ownership with `MarketplaceService:UserOwnsGamePassAsync` on join and cache it; listen for in-session purchases (`PromptGamePassPurchaseFinished`) and re-check server-side.
- No product grant may touch [[Service - EconomyService]] Cash functions. A code review checklist item enforces this.
- Cosmetic data lives in the profile ([[Schema - Player Profile]]); cosmetic application is client-visible but validated server-side.

```lua
-- Illustrative Luau (not executed)
local MarketplaceService = game:GetService("MarketplaceService")

MarketplaceService.ProcessReceipt = function(receipt)
	local player = game:GetService("Players"):GetPlayerByUserId(receipt.PlayerId)
	if not player then return Enum.ProductPurchaseDecision.NotProcessedYet end
	local profile = DataService.GetProfile(player)
	if not profile then return Enum.ProductPurchaseDecision.NotProcessedYet end
	if profile.purchases[receipt.PurchaseId] then
		return Enum.ProductPurchaseDecision.PurchaseGranted -- already granted
	end
	local grant = ProductCatalogue[receipt.ProductId]
	if not grant or grant.kind == "Cash" then -- Cash products must never exist (D-044)
		return Enum.ProductPurchaseDecision.NotProcessedYet
	end
	CosmeticService.Grant(player, grant)
	profile.purchases[receipt.PurchaseId] = os.time()
	DataService.SaveNow(player) -- must succeed before acknowledging
	return Enum.ProductPurchaseDecision.PurchaseGranted
end
```

(`DataService.SaveNow` and `CosmeticService` are project modules, not Roblox APIs. Exact save-before-acknowledge sequencing is covered in [[Save, Load and Recovery]].)

## 3. Shop presentation

Owned by [[UI - Shop]]. Rules: prices in Robux are always visible; no Robux prompts outside the shop and vendor NPCs; no shop pop-ups after defeats, thefts or hatches; bundles itemised.

## Related documents
- [[Monetisation Principles]]
- [[Free-to-Play Experience]]
- [[Roblox Monetisation Policy Requirements]]
- [[UI - Shop]]
- [[Base Art Direction]]
- [[Animal Variants]]
- [[Economy and Monetisation Index]]
