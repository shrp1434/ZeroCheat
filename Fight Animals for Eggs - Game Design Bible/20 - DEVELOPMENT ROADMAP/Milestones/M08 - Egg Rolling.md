---
title: M08 - Egg Rolling
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - eggs
  - odds-disclosure
  - compliance
milestone: M08
stage: 3
complexity: M
---

# M08 - Egg Rolling

> [!info] PROPOSED milestone
> Stage 3 · Size **M** · Critical path: near-critical (4 units of slack) · Exit gate: **G3 Core loop slice**

## Objective

Let players spend Cash on egg rolls that decide egg rarity (stage one of the **CONFIRMED** two-stage randomness, D-015). Rolls use hidden progression luck (D-017), and the player always sees their **actual current odds before committing**, bound to a server-issued `oddsVersion` token (D-041, **PROPOSED**). Rolled eggs go into egg storage with the **CONFIRMED** capacities.

> [!danger] Compliance
> This milestone carries the odds-disclosure obligation. A displayed table that differs from the server table, or odds that change after the player commits, is a release blocker regardless of any other progress.

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Progression Score calculation and normalised P | Engineering | [[Progression Score Specification]], [[Service - LuckService]] |
| Egg-rarity weight calculation and normalisation | Engineering | [[Implementation - Dynamic Luck Calculation]], [[Dynamic Progression Luck]] |
| Weighted random selection using `Random.new` on the server | Engineering | [[Implementation - Weighted Random Selection]] |
| Roll transaction: price check, Cash debit, rarity roll, storage insert, atomic save | Engineering | [[Implementation - Egg Roll and Hatch Flow]], [[Service - EggService]] |
| `oddsVersion` token issue and stale-token rejection | Engineering | [[Randomised Reward Compliance]] |
| Single and ×5 roll at PROPOSED prices | Engineering, Economy | [[Egg Pricing]], [[Egg Roll System]] |
| Egg storage: backpack 10, base 50 (**CONFIRMED**), destination rules | Engineering | [[Egg Storage]], [[Schema - Egg Inventory]] |
| Odds display before every roll | UI | [[UI - Egg Rolling]] |
| Seven egg models and roll animation | Art, Animation | [[Egg Art Direction]], [[Animation - Egg Roll]], the seven egg type documents (for example [[Common Egg]]) |
| Roll sounds | Audio | [[Sound - Eggs]] |
| Automated parity check: displayed odds equal server odds | QA, Engineering | [[Statistical Testing of Probabilities]] |

## Dependencies

- **Upstream:** [[M07 - Animal Collection]] (index count feeds the Progression Score; Cash from [[M06 - Animal Combat]]).
- **Downstream:** [[M09 - Hatching]].

## Complexity

**M.** The maths is simple; the transaction safety, disclosure binding and statistical verification are what make it non-trivial.

## Risks

| Risk | Why it matters here |
|---|---|
| R-011 (odds mismatch) | Core compliance risk. |
| R-012 (paid random items) | Any Robux path to Cash changes the classification ([[Open Questions#Q-032]]). |
| R-005 (bad-luck perception) | No pity by design (D-018). |
| R-007 (inflation) | Roll price against cash income per region. |
| R-023 (exploits) | Free rolls, replayed tokens, negative prices. |

## Acceptance criteria

- [ ] The odds shown before a roll equal the odds the server uses for that roll, to the displayed precision, in every automated parity test.
- [ ] A roll submitted with a stale `oddsVersion` is rejected and the client re-displays the new odds; no Cash is taken.
- [ ] Odds are recomputed when the Progression Score changes; the change is visible before the next commit and never applied to a roll already committed.
- [ ] Sampling tests over a large number of server rolls match the configured distribution within the tolerance defined in [[Statistical Testing of Probabilities]].
- [ ] Wild spawn rarity is unaffected by luck (regression of the M05 test).
- [ ] Rolling with insufficient Cash or full storage fails cleanly with no partial state.
- [ ] No Robux purchase grants Cash in this build (D-044 **PROPOSED**; [[Open Questions#Q-032]] still open).

## Testing requirements

- [[Test Cases - Egg Rolls and Hatching]]: roll flow, pricing, storage destination, stale token handling.
- [[Statistical Testing of Probabilities]]: distribution sampling at several Progression Score levels from [[Dynamic Luck Probability Tables]].
- [[Test Cases - Inventory and Storage]]: storage capacity and destination.
- [[Test Cases - Exploit Prevention]]: replayed or forged tokens, concurrent roll requests.

## Open questions

- [[Open Questions#Q-016]]: final egg probabilities.
- [[Open Questions#Q-017]]: final dynamic luck formula.
- [[Open Questions#Q-020]]: pricing model (flat versus scaled).
- [[Open Questions#Q-032]]: any Robux product granting Cash.
- **UNDECIDED** (Q-1117): who signs off an odds table before it ships (owner alone, or owner plus a named compliance reviewer).

## Key vault documents
- [[Egg Roll System]] · [[Egg Rarity System]] · [[Dynamic Progression Luck]] · [[Dynamic Luck Probability Tables]]
- [[Randomised Reward Compliance]] · [[Roblox Monetisation Policy Requirements]] · [[Independent Random Outcomes]]
- [[Service - EggService]] · [[Service - LuckService]] · [[Implementation - Egg Roll and Hatch Flow]]

## Related documents
- [[Development Roadmap]]
- [[M07 - Animal Collection]]
- [[M09 - Hatching]]
- [[Versioning and Changelog Policy]]
- [[Risk Register]]
