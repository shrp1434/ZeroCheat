---
title: M18 - UI and UX
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - ui
  - ux
  - onboarding
  - accessibility
milestone: M18
stage: 7
complexity: L
---

# M18 - UI and UX

> [!info] PROPOSED milestone
> Stage 7 · Size **L** · Critical path: near-critical (3 units of slack) · Exit gate: **G6 Beta ready**

## Objective

Turn the functional screens built inside each feature milestone into one coherent, accessible, mobile-first interface. Deliver onboarding for new players, the notification system, settings, the progression interface, and the shop with the monetisation integration. The shop must make the game fully playable without Robux obvious from the first session (D-027 **CONFIRMED**).

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Design system applied to every screen | UI, Art | [[UI Design System]], [[UI Visual Styling]], [[Typography]], [[Colour Palette]] |
| Navigation map implemented; no dead ends | UI | [[UI Navigation Map]] |
| Accessibility pass (text scale, colour-blind-safe rarity cues, touch targets) | UI | [[UI Accessibility Standards]], [[Rarity Visual Language]] |
| New player onboarding | Design, UI | [[New Player Onboarding]] |
| HUD consolidation | UI | [[UI - Main HUD]], [[UI - Animal Team Display]], [[UI - Player Strength Display]] |
| Notifications, settings, progression | UI | [[UI - Notifications]], [[UI - Settings]], [[UI - Progression Interface]] |
| Shop and product integration (MarketplaceService, receipt processing) | UI, Engineering | [[UI - Shop]], [[Monetisation Product Concepts]], [[Roblox Monetisation Policy Requirements]] |
| Odds disclosure consistency on every roll and hatch surface | UI, Compliance | [[Randomised Reward Compliance]] |
| UI sound pass | Audio | [[Sound - UI Feedback]] |
| UI asset set (UI-###) | Art | [[Asset Register]] |

## Dependencies

- **Upstream:** [[M10 - Ascension]], [[M11 - Egg Merging]], [[M15 - Base Raids]], [[M17 - Boss Encounters]] (all feature screens exist).
- **Downstream:** [[M21 - Beta Testing]].

## Complexity

**L.** Around twenty screens, three input types, many screen sizes and onboarding that touches every system.

## Risks

| Risk | Why it matters here |
|---|---|
| R-011 (odds mismatch) | Odds text and number formatting must match the server across every surface. |
| R-012, R-015 (paid random items, pay-to-win perception) | The shop is where these risks become visible. |
| R-003 (team lock) | Onboarding must teach the base-only team change early. |
| R-019 (mobile) | UI overdraw and text legibility on small screens. |

## Acceptance criteria

- [ ] Every screen in [[UI Navigation Map]] is reachable and closable on touch, mouse and gamepad.
- [ ] Every roll and hatch surface shows the player's current odds before commit, in the same format.
- [ ] Onboarding teaches fight, cash, roll, hatch, team change at base and ascension without blocking skip for returning players.
- [ ] Rarity is never communicated by colour alone.
- [ ] Product purchases are granted exactly once per receipt; purchases never grant Cash while D-044 stands (**PROPOSED**; [[Open Questions#Q-032]]).
- [ ] If any product is or becomes a paid random item, the PolicyService restriction check hides or blocks it for restricted players (see [[Roblox Monetisation Policy Requirements]]).
- [ ] No placeholder value for an **UNDECIDED** item (raid duration, theft limit, expansion price, boss rewards) is shown to players as final.

## Testing requirements

- [[Test Plan Matrix]]: UI rows for every screen.
- [[Test Cases - Mobile Performance]]: UI cost and legibility on reference devices.
- [[Test Cases - Egg Rolls and Hatching]]: disclosure on every surface.
- [[Test Cases - Exploit Prevention]]: receipt replay, purchase prompts from forged remotes.

## Open questions

- [[Open Questions#Q-009]] and [[Open Questions#Q-010]]: storage expansion currency and price (shop listing).
- [[Open Questions#Q-032]]: any Robux product granting Cash.
- **UNDECIDED** (Q-1111): localisation languages at launch.
- **UNDECIDED** (Q-1110): platform priority for layout defaults.

## Key vault documents
- [[UI and UX Index]] · [[UI Design System]] · [[UI Navigation Map]] · [[UI Accessibility Standards]]
- [[New Player Onboarding]] · [[UI - Shop]] · [[Monetisation Principles]] · [[Free-to-Play Experience]]

## Related documents
- [[Development Roadmap]]
- [[M15 - Base Raids]]
- [[M17 - Boss Encounters]]
- [[M21 - Beta Testing]]
- [[Art Direction Index]]
