---
title: Design Inspiration Notes
type: reference
category: references
status: proposed
priority: P2
owner: Lead Game Designer
last_updated: 2026-11-14
tags:
  - references
  - inspiration
  - genre
  - identity
---

# Design Inspiration Notes

*Fight Animals for Eggs* sits where three familiar genres meet: **collection simulators**, **monster-taming games** and **base-raiding games**, with real-time co-operative combat on top. This page describes the conventions of those genres in general terms and states what the game adopts and what it avoids, so that it keeps its own identity.

> [!important] No copying
> This page describes genre conventions only. It names no specific games and contains no external research. Never copy another game's creatures, names, art, user interface layouts, sound or text. New content must pass the identity checklist at the end of this page. The game's own identity is defined in [[Unique Selling Points and Identity]].

All "adopt" and "avoid" recommendations here are **PROPOSED**. Where they touch a **CONFIRMED** rule, the rule is quoted with its decision ID.

## Collection simulators

**Common conventions:** buying or earning eggs or capsules; rarity colour ladders; dramatic opening animations; companions that follow the player; stacking multipliers; very large numbers; reset-for-bonus loops; automatic opening; leaderboards for rare pulls.

| Adopt | Why | Where it lives |
|---|---|---|
| A clear rarity ladder with consistent colours and effects | Instant readability; seven tiers are **CONFIRMED** (D-003) | [[Rarity Visual Language]] |
| A satisfying hatch reveal that can be skipped after first viewing | Excitement without wasting the player's time | [[Egg Animations]] |
| Companions visibly with the player | Ownership pride; here they also fight | [[Animal Combat Behaviour]] |
| Multi-open convenience | Up to five eggs at once is **CONFIRMED** (D-016) | [[Hatch System]] |

| Avoid | Why |
|---|---|
| Undisclosed or vaguely described odds | Actual odds must be shown before commit (D-017 **CONFIRMED**) |
| Runaway multiplier stacking and inflated numbers | Makes balance and raids meaningless; see [[Inflation and Farming Exploit Risks]] |
| Reset-everything prestige loops | Not in the owner brief; growth here comes from ascension, bases and regions |
| Paid luck boosts as the main revenue engine | Paid random rewards must not be the main revenue mechanism (D-027 **CONFIRMED**) |
| Collection as the only activity | Combat, bosses and bases carry the session, not menus |

## Monster-taming games

**Common conventions:** teams of creatures with distinct roles; growth through levelling or transformation; type or element matchups; a catalogue of discovered creatures; companions with personalities; turn-based battles.

| Adopt | Why | Where it lives |
|---|---|---|
| Distinct roles that make team composition matter | Team of exactly three is **CONFIRMED** (D-006); roles give choices | [[Animal Roles]] |
| A discovery catalogue that separates seen from owned | **CONFIRMED** (D-029) | [[Animal Index Feature Specification]] |
| Growth that makes favourite animals stronger over time | Ascension by duplicates is **CONFIRMED** (D-019) | [[Ascension System]] |
| Animals with personality in animation and sound | Low-poly charm, not realism | [[Animation Bible]], [[Sound - Animal Vocalisations]] |

| Avoid | Why |
|---|---|
| Turn-based battle structure | Combat is real-time and hybrid (D-005 **CONFIRMED**) |
| Large elemental type charts | Adds a learning wall for the audience; roles and abilities carry the variety instead |
| Capturing by weakening wild creatures | Acquisition here is through eggs; defeating wild animals registers them in the index (D-029) |
| Fantasy creatures as the core roster | The roster is real animals, with prehistoric and colossal animals at the top tiers (**PROPOSED**, [[Open Questions#Q-027]]) |
| Per-creature levelling grinds | Not in the launch design (D-042 **PROPOSED**) |

## Base-raiding games

**Common conventions:** personal bases with upgradeable buildings; defensive structures; shields after being attacked; loot limits; offline protection or the lack of it; revenge attacks; matchmaking by strength; upgrade timers that can be skipped with premium currency.

| Adopt | Why | Where it lives |
|---|---|---|
| Modular bases with per-section upgrades | **CONFIRMED** (D-022) | [[Player Base System]] |
| Shields and physical defences | **CONFIRMED** (D-024) | [[Shield Mechanics]], [[Base Defence Overview]] |
| Hard caps on what can be lost | Maximum three animals per successful raid; backpack eggs never stealable (D-021, D-024 **CONFIRMED**) | [[Animal Theft Rules]], [[Egg Theft Rules]] |
| Visible upgrade progress | Every level changes the base's look | [[Base Art Direction]] |

| Avoid | Why |
|---|---|
| Raiding offline players | Offline bases cannot be raided (D-024 **CONFIRMED**) |
| Mandatory participation | PvP and raids are optional (D-023, D-024 **CONFIRMED**) |
| Upgrade timers sold for skipping | Conflicts with fair, fully free progression (D-027) |
| Losses that undo many sessions of play | Drives defenders away (R-004 in [[Risk Register]]) |
| Matchmaking that lets strong players farm weak ones | Matchmaking is **UNDECIDED** ([[Open Questions#Q-029]]); any option must protect newer players |

## Co-operative action and boss games

**Common conventions:** readable boss telegraphs; shared world events; contribution-based rewards; scheduled spawns.

| Adopt | Why | Where it lives |
|---|---|---|
| Telegraphed boss attacks | Fair, learnable fights | [[Boss Design Overview]] |
| Scheduled, announced world bosses | Shared moments in one large world (D-025 **CONFIRMED**) | [[Canonical Proposed Values#5. Regions (PROPOSED — world layout is UNDECIDED, Q-001)]] |
| Shared kill credit | Removes kill-stealing friction (D-040 **PROPOSED**) | [[Multiplayer Combat Rules]] |

| Avoid | Why |
|---|---|
| Visual clutter that hides telegraphs | Readability risk R-002 |
| Rewards only for top damage | Discourages helping others in a shared world |

## Identity: what makes this game its own

1. **The player fights too.** Player Strength is separate from animal strength (D-007), with specials and a dodge. Few collection games make the player a combatant.
2. **Real animals, colourful low-poly, no horror or meme creatures** (D-026).
3. **Two honest random stages** (rarity, then pool), with progression luck that is disclosed before every commit and never touches wild encounters (D-015, D-017).
4. **Deterministic merging** as a guaranteed route alongside luck (D-020).
5. **The base as the team's home**: the team changes only at the base (D-010), linking exploration, bases and combat.
6. **Raids with hard protections**, so PvP risk is bounded and optional.

## Identity checklist for new content

- [ ] Original name, silhouette, colour scheme and abilities; not traceable to another game's content.
- [ ] Real animal (or prehistoric animal for top tiers, if Q-027 is approved), colourful and low-poly.
- [ ] No horror styling, no meme or "brainrot" creature (D-026).
- [ ] Fits an existing role and family, or the new role or family has a design review.
- [ ] Odds disclosure and pool rules followed ([[Content Expansion Guidelines]]).

## Related documents
- [[References Index]]
- [[Unique Selling Points and Identity]]
- [[Vision Statement and Pillars]]
- [[Design Principles and Fairness Charter]]
- [[Art Bible]]
- [[Content Expansion Guidelines]]
