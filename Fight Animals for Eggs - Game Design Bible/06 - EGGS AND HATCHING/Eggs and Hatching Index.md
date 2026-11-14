---
title: Eggs and Hatching Index
type: index
category: eggs
status: mixed
priority: P0
owner: Economy and Progression Designer
last_updated: 2026-11-14
tags:
  - index
  - eggs
  - hatching
---

# Eggs and Hatching Index

Everything about eggs: how they are rolled, stored, merged and hatched, how progression luck changes the odds, and how the system stays fair and compliant. Start with [[Egg System Overview]] for the end-to-end pipeline, then follow the stage you are working on.

> [!success] CONFIRMED foundations
> Two-stage randomness (D-015) · hatch up to 5 at once (D-016) · hidden luck with disclosed odds, no effect on wild encounters (D-017) · independent outcomes with no duplicate protection (D-018) · 3 → 1 merging at an upgradeable station (D-020) · storage 10 + 50 = 60, backpack never stealable (D-021).

## Orientation by role

| You are… | Read first |
|---|---|
| Designer | [[Egg System Overview]] → [[Egg Roll System]] → [[Hatch System]] → [[Egg Merging]] |
| Economy / balance | [[Dynamic Progression Luck]] → [[Probability Balancing]] → [[Egg Merging#Merge shortcut analysis]] → [[Ascension Expected Value Analysis]] |
| Engineer | [[Egg Roll System]] (flows and edge cases) → [[Randomised Reward Compliance]] (tokens) → [[Egg Merging Station#Server validation]] |
| Artist / animator / audio | [[Egg Art Direction]] → the seven egg type pages → [[Egg Animations]] → [[Egg Merging Station]] |
| QA | [[Independent Random Outcomes]] → [[Test Cases - Egg Rolls and Hatching]] → [[Test Cases - Egg Merging]] |

## Documents in this folder

| Document | What it covers | Status |
|---|---|---|
| [[Egg System Overview]] | End-to-end pipeline, egg lifecycle, ownership of each stage | mixed |
| [[Egg Rarity System]] | The seven rarities, pool sizes, colour keys, Common-equivalent values, data representation | mixed |
| [[Egg Roll System]] | Buying eggs with Cash: odds disclosure, roll flow, server sequence, bulk rolls, edge cases | mixed |
| [[Hatch System]] | Turning eggs into animals: pool odds, hatch flow, multi-hatch, edge cases, the hatch-odds timing question | mixed |
| [[Dynamic Progression Luck]] | How progress improves odds; "hidden formula, disclosed odds"; worked examples; anti-manipulation | mixed |
| [[Dynamic Luck Probability Tables]] | Generated rarity odds at P = 0, 0.1 … 1.0 (maintained by the lead) | proposed |
| [[Hatch Pool Tables]] | Generated per-animal hatch odds for every pool (maintained by the lead) | proposed |
| [[Independent Random Outcomes]] | The maths of independence, geometric distribution, no duplicate protection, UI copy rules | mixed |
| [[Egg Storage]] | Backpack and base capacities, behaviour when full, transfers, raid interaction | mixed |
| [[Egg Merging]] | Merge rules, consumption, upgrade table and the merge shortcut balance analysis | mixed |
| [[Egg Merging Station]] | The five station levels: costs, gates, physical appearance, upgrade animations, validation | mixed |
| [[Egg Animations]] | Roll, hatch and merge presentation contract and per-rarity escalation | proposed |
| [[Probability Balancing]] | Balance targets, findings, tuning levers, validation checklist, change process | proposed |
| [[Randomised Reward Compliance]] | Odds disclosure, `oddsVersion` tokens, paid-random-item rules, audit logging | mixed |

### Egg Types

| Document | Look in one line | Asset ID |
|---|---|---|
| [[Common Egg]] | Plain speckled slate-grey oval | EGG-01 |
| [[Uncommon Egg]] | Leaf-green with a leaf band and a sprout on top | EGG-02 |
| [[Rare Egg]] | Faceted sky-blue gem with a glass equator ring | EGG-03 |
| [[Epic Egg]] | Violet shell breaking out in crystals with glowing cracks | EGG-04 |
| [[Legendary Egg]] | Gilded gold egg with a crown and a rotating halo | EGG-05 |
| [[Mythical Egg]] | Levitating rose-marble egg with runes and orbiting stones | EGG-06 |
| [[Secret Egg]] | Split night-dark shell around a colour-cycling prismatic core | EGG-07 |

## Open questions touching eggs

| ID | Topic |
|---|---|
| [[Open Questions#Q-016]] | Final egg probabilities |
| [[Open Questions#Q-017]] | Final luck formula and inputs |
| [[Open Questions#Q-018]] | Final hatch pools |
| [[Open Questions#Q-019]] | Final station costs |
| [[Open Questions#Q-020]] | Roll pricing model |
| [[Open Questions#Q-022]] | Owned-animal capacity |
| [[Open Questions#Q-023]] | Hatch timing (instant versus incubation) |
| [[Open Questions#Q-032]] | Robux products granting Cash |
| [[Open Questions#Q-034]] | Merge timing |
| [[Open Questions#Q-009]], [[Open Questions#Q-010]] | Storage expansion currency and price |
| Q-301 | Roll locations and default egg destination (new, pending addition to Open Questions) |
| Q-302 | Whether hatch odds are fixed at roll time or hatch time (new) |
| Q-305 | Disposal of surplus animals (new) |

## Related folders
- [[Ascension and Progression Index]]: what duplicates are for, and how PS is built
- [[Economy and Monetisation Index]]: Cash sources, sinks and pricing
- [[UI and UX Index]]: [[UI - Egg Rolling]], [[UI - Egg Hatching]], [[UI - Egg Storage]], [[UI - Egg Merging]]
- [[Technical Architecture Index]]: [[Service - EggService]], [[Service - HatchService]], [[Service - LuckService]], [[Service - MergeService]]
- [[Vault Map]]
