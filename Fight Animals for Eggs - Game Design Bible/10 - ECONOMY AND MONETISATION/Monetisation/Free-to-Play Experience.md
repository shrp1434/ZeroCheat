---
title: Free-to-Play Experience
type: spec
category: monetisation
status: mixed
priority: P0
owner: Monetisation Designer
last_updated: 2026-11-14
tags:
  - monetisation
  - free-to-play
  - player-journey
  - fairness
---

# Free-to-Play Experience

What a player who never spends Robux experiences, from the first minute to the endgame, and the checks that keep it complete. Session structure is owned by [[Session Flow and Player Journey]]; onboarding by [[New Player Onboarding]].

> [!success] CONFIRMED (D-027)
> The game is fully playable without Robux, with no essential progression behind purchases.

## 1. Everything a free player can reach

| System | Free access | Paid-only content |
|---|---|---|
| Regions 1–8, bosses, world bosses | All | None |
| All 60 animals and all seven rarities | All, via rolls, hatches and merging | None |
| Ascension A1–A5 | All | None |
| Every base module L1–L5, Plot Stage 4, Station L5 | All, with Cash | None |
| Storage expansion | Currency **UNDECIDED** ([[Open Questions#Q-009]]); the recommendation keeps every step reachable with Cash | Recommended: none (backpack never for Robux) |
| PvP and raiding | All | None |
| Prestige visuals (A5 auras, trophies, index titles, L5 module looks) | All | None; paid cosmetics are alternatives, not upgrades |
| Cosmetics | Earned set: boss trophies, index milestone titles, seasonal free rewards | Purchasable cosmetic catalogue ([[Monetisation Product Concepts]]) |

## 2. Free journey milestones (PROPOSED model)

Based on [[Progression Bottleneck Analysis]] and [[Expected Value Calculations]], solo play, no Robux.

| Time played | Typical state |
|---|---|
| 0–15 min | Tutorial; first wild defeats; first roll (200 Cash ≈ 20 Common kills); first hatch |
| 15–60 min | Several rolls, first duplicate; Multiplier Shrine L1; first merge after buying the station (2,500) |
| 1–2 h | Bramblehorn defeated; Region 2 unlocked at level 8; Plot Stage 1 |
| ~9 h | Region 3; station L2; first Epics by merging |
| ~21 h | Region 4; station L3; Legendary merges become available |
| ~61 h | Region 6; station L4 with a world boss; Mythical merges |
| ~118 h | Region 8; station L5; first Secret by merging; base can be fully maxed |
| ~165 h | Level 100 |
| 200 h+ | A5 on rare species, full index, all trophies |

The Robux buyer's timeline is **identical**. Nothing in [[Monetisation Product Concepts]] moves any row of this table.

## 3. F2P parity checklist (release gate, PROPOSED)

Run before every release that adds or changes a product ([[Definition of Done]]).

- [ ] No product grants Cash, a Cash multiplier, XP (unless Q-410 is approved), odds, Progression Score, storage needed for core loops, shields or combat stats.
- [ ] No progression gate (region, boss, station, module level) checks for product ownership.
- [ ] The F2P milestone table above is unchanged by the release (simulation diff).
- [ ] No purchase prompt appears automatically after defeat, theft, hatch or merge.
- [ ] All paid cosmetics have an earned equivalent tier of prestige (not identical items).
- [ ] Raid preview and raid UI show no product-based advantage.
- [ ] Paid random items: none (or, if introduced, they pass [[Roblox Monetisation Policy Requirements]]).

## 4. Feel of being free

| Concern | Design response |
|---|---|
| "Paying players look cooler" | The most recognisable visuals (A5 crest and aura, L5 modules, Secret animals, full trophy halls) are earned only |
| "I can't keep up in raids" | No purchasable raid power; matchmaking bands ([[Open Questions#Q-029]]) |
| "Shop nags me" | Shop is opt-in; no interstitials |
| "Storage is a paywall" | Storage expansion recommended as Cash and progression-gated ([[Storage Expansion Economics]]) |
| "Boosts make others faster" | No power boosts at launch |

## 5. Edge cases

| Case | Handling |
|---|---|
| Player buys a cosmetic and a later decision makes it a variant-like item | Not possible: variant-like skins are rejected until Q-006 and Q-024 are decided |
| Product retired | Owners keep it; it is never converted into Cash |
| Refund via Roblox | Cosmetic removed if Roblox's systems report it (exact refund signals are *unverified*); progression is never affected because no progression was sold |

## Related documents
- [[Monetisation Principles]]
- [[Monetisation Product Concepts]]
- [[Progression Bottleneck Analysis]]
- [[Session Flow and Player Journey]]
- [[Target Audience and Player Motivations]]
- [[Design Principles and Fairness Charter]]
- [[Economy and Monetisation Index]]
