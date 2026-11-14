---
title: Unique Selling Points and Identity
type: vision
category: game-vision
status: mixed
priority: P0
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - vision
  - identity
  - usp
---

# Unique Selling Points and Identity

*Fight Animals for Eggs* must not read as a reskin of an existing Roblox simulator. This document lists the hooks that make it distinct, explains why each one matters, and sets the identity rules every department should apply.

> [!success] CONFIRMED hooks
> Every hook in §1 is built on owner decisions in the [[Decision Register]]. The way each hook is framed and presented is **PROPOSED**.

## 1. The six signature hooks

### Hook 1: You fight in the fight (hybrid combat)

The player and **three** animals fight together in real time (D-005, D-006). The player has a three-hit combo, specials and a dodge roll ([[Player Combat]]); animals auto-target but take manual target commands (D-009) and have both manual and automatic abilities (D-008). Player Strength is its own statistic (D-007).

*Why it is distinctive:* in many collection games the player's avatar stands still while pets do the work. Here, positioning, dodging and focus-fire decide boss fights.

### Hook 2: Two-stage egg randomness

Every egg is decided twice (D-015): the **roll** sets the rarity of the egg, and the **hatch** picks a species from that rarity's pool. Eggs are objects the player holds, stores, merges and chooses when to hatch, not instant slot results.

*Why it is distinctive:* it creates two separate moments of anticipation and a real decision in between (hatch now, store, or merge three into a higher rarity, D-020). See [[Egg Roll System]], [[Hatch System]] and [[Egg Merging]].

### Hook 3: Hidden but honestly disclosed progression luck

Progression improves the player's odds (D-017). The formula may stay hidden, but the **exact current odds are shown before every roll and hatch**, bound to a server-issued odds version so they can never change silently (D-041 **PROPOSED**). Luck never affects which wild animals appear. Hatches are independent with no duplicate protection (D-018).

*Why it is distinctive:* "your luck grows as you grow" is a promise players can verify. See [[Dynamic Progression Luck]] and [[Design Principles and Fairness Charter]].

### Hook 4: The base lock on team changes

The team can only be changed at the player's own base and is locked from the moment they leave until they return (D-010). Choosing three animals becomes an expedition decision, like packing for a trip.

*Why it is distinctive:* it turns the base into a strategic hub and makes team composition matter. A player heading to [[Region - Frostfang Tundra]] chooses differently from one heading to a raid. See [[Team Equipping and Base Lock Rule]].

### Hook 5: Raiding with a knock-out-before-steal rule

In optional raids (D-024), base-stored eggs can be stolen, but a defending animal can only be stolen **after it has been knocked out**; undefeated defenders are safe, at most **three** animals can be taken per successful raid, backpack eggs are never stealable and offline bases cannot be raided.

*Why it is distinctive:* theft is earned through combat, not through a timer or a menu, and the worst case is bounded. See [[Base Raiding System]] and [[Animal Theft Rules]].

### Hook 6: Duplicates are fuel, not waste

Ascension consumes duplicates and keeps the original (D-019). With independent hatches (D-018), every duplicate has a destination, and the proposed A1–A5 star tiers change the animal's look as well as its stats (D-037 **PROPOSED**, [[Ascension System]]).

## 2. Identity statement

> **A bright, low-poly animal world where you fight beside your companions, hatch eggs whose odds you can trust, and build a home worth defending.**

| Identity element | Rule | Owner document |
|---|---|---|
| Visual signature | Colourful, polished, low-poly animals with bold silhouettes and faceted materials; rarity readable at a glance (D-026). | [[Art Bible]], [[Rarity Visual Language]] |
| World signature | Eight habitat regions around a central hub, each with a single dominant colour story and one unforgettable landmark (**PROPOSED**, layout **UNDECIDED** [[Open Questions#Q-001]]). | [[World Overview and Map]], [[Environment Art Direction]] |
| Egg signature | Eggs are physical, weighty objects with a rarity-coloured glow; hatching cracks along faceted seams. | [[Egg Art Direction]], [[Egg Animations]] |
| Combat signature | Snappy player combo plus visible companion focus-fire lines when a target command is issued. | [[Combat Feedback and Readability]] |
| Audio signature | Warm, adventurous orchestral-folk with per-region instrument leads. | [[Music Direction]], [[Sound Bible]] |
| Fiction signature | The rarest eggs are "ancient eggs" that carry colossal and prehistoric lineages (D-033 **PROPOSED**, [[Open Questions#Q-027]]). | [[Animal Families]] |

## 3. Identity do and do not

| Do | Do not |
|---|---|
| Name places and bosses with evocative, original compound names (Whisperwood, Bramblehorn). | Borrow names, UI layouts, egg shapes or catchphrases from other Roblox games. |
| Show real, recognisable animals in a stylised way. | Use meme animals, brainrot characters or horror creatures (D-026). |
| Present odds as a feature ("Your odds today"). | Hide odds behind extra taps or show them only after purchase. |
| Make the player's own character visibly heroic in combat. | Reduce the avatar to a pet-follower. |
| Celebrate a Common hatch modestly and a Secret hatch spectacularly. | Use fake near-miss animations that imply a higher rarity was "almost" won ([[Design Principles and Fairness Charter]]). |

## 4. Positioning summary

| Common genre convention | Our position |
|---|---|
| Pets follow and auto-attack while the player clicks | Player and three animals are a coordinated real-time team |
| One random stage (open egg → pet) | Two stages, with storage and merging between them |
| Luck boosts sold or hidden | Progression luck is earned and disclosed as exact odds |
| Change pets anywhere | Team locked away from base: expedition planning matters |
| Raids steal by timer or menu | Animals only stolen after being knocked out; hard cap of three |
| Separate worlds behind loading screens | One shared world (D-025), hub plus contiguous regions (**PROPOSED**) |

## 5. Expandability as identity

The identity scales with content, not against it:
- New regions slot into the ring layout with their own multiplier and colour story ([[Content Expansion Guidelines]]).
- New species slot into existing rarity pools; pools are re-normalised and the disclosed odds update automatically ([[Hatch Pool Tables]]).
- New bosses add trophies, discovery goals and Progression Score inputs ([[Progression Score Specification]]).
- New variants extend the collection without new stat systems (variant stat bonuses are **UNDECIDED**, [[Open Questions#Q-024]]).

## Related documents
- [[Game Vision Index]]
- [[Vision Statement and Pillars]]
- [[Design Principles and Fairness Charter]]
- [[Core Gameplay Loop]]
- [[Design Inspiration Notes]]
- [[Art Bible]]
