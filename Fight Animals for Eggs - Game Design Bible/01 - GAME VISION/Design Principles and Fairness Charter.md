---
title: Design Principles and Fairness Charter
type: vision
category: game-vision
status: mixed
priority: P0
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - vision
  - design-principles
  - fairness
  - compliance
---

# Design Principles and Fairness Charter

Part A lists the design principles every feature is reviewed against. Part B is the **Fairness Charter**: the promises we make to players. Charter items built on owner decisions are **CONFIRMED**; the rest are **PROPOSED** and need owner approval before they are published to players.

---

## Part A: Design principles

| # | Principle | What it means in practice | Review question |
|---|---|---|---|
| P1 | **Easy to understand** | One primary action per screen, one objective at a time in onboarding, plain-language labels. | Can a new player explain this feature in one sentence after first use? |
| P2 | **Hard to master** | Depth comes from decisions (team composition, target commands, dodge timing, merge vs hatch), not from hidden complexity. | Does a skilled player get a visibly better result than an unskilled one with the same collection? |
| P3 | **Always rewarding** | Every fight pays Cash and XP; every hatch has a use (new species or ascension fuel); every visit home has a decision. | Is there any outcome that feels like wasted time? |
| P4 | **Interesting over long sessions** | Short, mid and long loops interlock ([[Core Gameplay Loop]]); regions change mechanics through hazards and boss patterns, not only through numbers. | What does hour three offer that hour one did not? |
| P5 | **Solo and multiplayer** | Everything except PvP and raids is completable solo; groups go faster and have more fun, not exclusive access. | Can a solo player finish this? Is it better with friends? |
| P6 | **A large, desirable collection** | 60 species with distinct silhouettes, roles and homes; variants and ascension tiers add visible prestige. | Would a player want this animal for something other than its rarity? |
| P7 | **Visually distinctive** | Low-poly, colourful, polished (D-026); every region has its own dominant palette and landmark. | Could a screenshot of this be mistaken for another game? |
| P8 | **Fair to free players** | Fully playable without Robux (D-027); purchases save time or add cosmetics, never gate progression. | Does a non-paying player have the same ceiling? |
| P9 | **Expandable** | Data-driven content (pools, regions, bosses) so updates are additive ([[Content Expansion Guidelines]]). | Can we add a species or region without code changes to core systems? |
| P10 | **Own identity** | Original names, original mechanics framing, no borrowed UI or catchphrases ([[Unique Selling Points and Identity]]). | Would we be comfortable showing this beside the game it most resembles? |
| P11 | **Server authority** | Every outcome that matters (damage, rolls, hatches, theft, team changes) is decided on the server ([[Server-Client Responsibilities]]). | What happens if the client lies? |

### Principle conflicts and tie-breakers

When principles conflict, apply this order: **fairness and safety (Part B) > server authority (P11) > clarity (P1) > depth (P2) > everything else.**

*Example:* a "quick team swap from anywhere" button would help clarity and convenience but breaks D-010 and the expedition decision it creates. The confirmed rule wins; the convenience need is met instead by a short, interruptible return-home action ([[Team Equipping and Base Lock Rule]]).

---

## Part B: Fairness Charter

### B1. Odds and randomness

| # | Promise | Status |
|---|---|---|
| F1 | Before every egg roll and every hatch, you see the **exact odds that apply to you right now**. | **CONFIRMED** (D-017) |
| F2 | Those odds cannot change between the moment you see them and the moment you commit. If they would change (for example you level up), the game shows you the new odds and asks again. | Principle **CONFIRMED** (D-017); mechanism **PROPOSED** (D-041 odds version token) |
| F3 | Your luck improves as you progress. The exact formula may stay private, but its effect is always visible as the odds on screen. | **CONFIRMED** (D-017) |
| F4 | Luck never changes which wild animals appear. | **CONFIRMED** (D-017) |
| F5 | Every hatch is independent. There is no duplicate protection, no hidden push towards animals you do not own and no memory of earlier hatches. | **CONFIRMED** (D-018) |
| F6 | Duplicates are always useful: they power ascension. | **CONFIRMED** (D-019) |
| F7 | Hatch and roll animations never fake a near-miss or imply a better result was "almost" won. The animation is chosen after the result and shows only the result. | **PROPOSED** |
| F8 | Paid random items follow Roblox policy, including regional restrictions checked through `PolicyService:GetPolicyInfoForPlayerAsync` (`ArePaidRandomItemsRestricted`). | **PROPOSED** implementation; see [[Roblox Monetisation Policy Requirements]] |

### B2. Spending

| # | Promise | Status |
|---|---|---|
| F9 | The whole game can be played and completed without Robux. | **CONFIRMED** (D-027) |
| F10 | Paid random rewards are not the main way we make money. | **CONFIRMED** (D-027) |
| F11 | Cash is never sold for Robux. | **PROPOSED** (D-044), [[Open Questions#Q-032]] |
| F12 | Nothing essential to progression is sold. | **CONFIRMED** (D-027) |

See [[Monetisation Principles]] and [[Free-to-Play Experience]].

### B3. PvP, raids and loss

| # | Promise | Status |
|---|---|---|
| F13 | PvP is optional. | **CONFIRMED** (D-023) |
| F14 | Raiding is optional. | **CONFIRMED** (D-024) |
| F15 | Eggs in your backpack can never be stolen. | **CONFIRMED** (D-021) |
| F16 | Your base cannot be raided while you are offline. | **CONFIRMED** (D-024) |
| F17 | A defending animal can only be stolen after it has been knocked out. Undefeated defenders are safe. | **CONFIRMED** (D-024) |
| F18 | No more than three animals can be stolen in one successful raid. | **CONFIRMED** (D-024) |
| F19 | Raid duration and the number of eggs that can be stolen will be published in-game once decided. | Values **UNDECIDED** ([[Open Questions#Q-012]], [[Open Questions#Q-013]]) |
| F20 | Before you opt into raiding, the game shows exactly what can be lost and what is always safe. | **PROPOSED** |
| F21 | Defeat penalties differ by battle type and are shown before you enter that type of battle. | Mixed system **CONFIRMED** (D-013); values **UNDECIDED** ([[Open Questions#Q-014]]) |

### B4. Shared world

| # | Promise | Status |
|---|---|---|
| F22 | Everyone who contributes meaningfully to defeating a wild animal or boss gets the full reward; nobody can "steal" your kill. | **PROPOSED** (D-040, 10% damage threshold) |
| F23 | Rare-spawn announcements go to the whole server at the same moment. | **PROPOSED** ([[Wild Animal Spawning and Respawn]]) |
| F24 | Reward eligibility for a boss is once per player per spawn, so groups never compete for a single drop. | **PROPOSED** ([[Boss Design Overview]]) |

### B5. Data and recovery

| # | Promise | Status |
|---|---|---|
| F25 | Transactions that consume items (ascension, merging, hatching, theft) either complete fully or not at all. | **PROPOSED** ([[Data Consistency and Transactions]]) |
| F26 | If something goes wrong, support can see what happened through server-side logs. | **PROPOSED** ([[Logging and Error Handling]]) |

> [!danger] Compliance-critical
> F1, F2, F5, F8 and F11 have legal and platform-policy consequences. Any change to egg, hatch or monetisation systems must be reviewed against [[Randomised Reward Compliance]] and [[Roblox Monetisation Policy Requirements]] before merging.

## Applying the charter

- **Design reviews:** every feature spec lists which charter items it touches.
- **QA:** each charter item has at least one test in [[Test Plan Matrix]]; odds items are tested statistically in [[Statistical Testing of Probabilities]].
- **Player communication:** an in-game "How luck works" panel summarises F1–F6 in plain words (**PROPOSED**, [[UI - Egg Rolling]]).

## Related documents
- [[Game Vision Index]]
- [[Vision Statement and Pillars]]
- [[Randomised Reward Compliance]]
- [[Independent Random Outcomes]]
- [[Monetisation Principles]]
- [[Raid Eligibility and Offline Protection]]
- [[Decision Register]]
