---
title: Definition of Done
type: process
category: production
status: proposed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - production
  - definition-of-done
  - quality
  - process
---

# Definition of Done

The checklist every backlog item must satisfy before it is accepted. A story in the [[Product Backlog]] is done when its own acceptance criteria pass **and** the checklist for its work type below is complete. QA signs off P0 items; the discipline lead signs off the rest.

> [!info] PROPOSED
> This Definition of Done is a **PROPOSED** studio standard. It may be tightened per milestone; it may be relaxed only by the Production Manager with a written reason on the story.

## 1. Universal checklist (every work type)

- [ ] The work matches its owning vault document; if the design changed, that document was updated in the same change and the [[Changelog]] notes it.
- [ ] Every number comes from [[Canonical Proposed Values]] or configuration; no new hard-coded values. New values were added to Canonical Proposed Values as **PROPOSED**.
- [ ] No **UNDECIDED** item was decided by the implementation; such values are configurable and the Q-ID is referenced.
- [ ] No **CONFIRMED** rule is contradicted (team of 3, hatch up to 5, storage 10 + 50, backpack never stolen, at most 3 animals stolen per raid, offline bases never raided, undefeated defenders never stolen, merge 3 → 1, seven rarities).
- [ ] Assets carry IDs from the [[Asset Register]] and follow [[Asset Naming Conventions]].
- [ ] No open S1 or S2 bug against the item ([[Bug Reporting and Severity]]).
- [ ] Reviewed by a second person from the same discipline.

## 2. Feature (gameplay system or player-facing flow)

- [ ] All acceptance criteria and linked test cases pass on the QA build, including every P0 and P1 case listed in the story.
- [ ] Server-authoritative: all state changes happen on the server; client requests are validated through [[Implementation - Remote Validation Layer]] and rate-limited ([[Implementation - Rate Limiting]]).
- [ ] Global invariants INV-01 to INV-12 ([[QA Strategy]]) hold after a 30-minute multi-client session using the feature.
- [ ] Transactions are all-or-nothing under disconnect and server failure (relevant cases in [[Test Cases - Persistence]]).
- [ ] UI states exist for: loading, success, every rejection reason, and disabled controls with an explanation.
- [ ] Works with touch, keyboard and mouse, and gamepad where supported.
- [ ] Telemetry events emitted as defined in [[Service - AnalyticsAndLoggingService]].
- [ ] Mobile frame-time criteria in [[Test Cases - Mobile Performance]] are met in the feature's heaviest scenario.
- [ ] Any probability, odds or random outcome passes the gate in [[Statistical Testing of Probabilities]] and odds are disclosed before commit (D-017).
- [ ] QA hooks for the feature exist in the QA build and are absent from staging (TC-EXP-040).

## 3. Art asset (model, texture, material, environment kit, UI art)

- [ ] Matches the [[Art Bible]], [[Colour Palette]] and the discipline document ([[Animal Modelling Principles]], [[Environment Art Direction]], [[Egg Art Direction]], [[Base Art Direction]], [[Boss Art Direction]] or [[UI Visual Styling]]).
- [ ] Colourful, polished, low-poly with a clear silhouette; no horror, meme or "Italian brainrot" styling (D-026).
- [ ] Rarity is readable at gameplay distance per [[Rarity Visual Language]].
- [ ] Within the triangle, texture and material budgets in [[Performance Guidelines]]; level-of-detail versions provided where required.
- [ ] Collision and pivot set correctly; scale verified against the player character in-engine.
- [ ] Imported in-engine and checked under the lighting in [[Lighting Direction]] on PC and mobile.
- [ ] Animals: rig-ready topology per [[Animal Rig Standards]]; variant material slots per [[Variant Visual Treatments]] if the species is variant-eligible.
- [ ] Registered in the [[Asset Register]] with status updated.

## 4. Animation

- [ ] Follows the [[Animation Bible]] and the specific animation document (for example [[Animation - Animal Attacks and Hit Reactions]]).
- [ ] Plays through `Animator:LoadAnimation` on the target rig without foot sliding or popping; loops are seamless where intended.
- [ ] Gameplay timings match design: hit frames align with server damage events; telegraph lead times match [[Combat Feedback and Readability]] and boss documents.
- [ ] Animation events or markers used by code are named and documented.
- [ ] Readable on a phone screen at gameplay distance.
- [ ] Skippable presentation animations (hatch, merge) can be skipped where specified without changing the outcome.
- [ ] Registered as ANI-### in the [[Asset Register]].

## 5. Sound

- [ ] Follows the [[Sound Bible]] and the specific sound document.
- [ ] Assigned to the correct `SoundGroup` and priority per [[Audio Mixing and Priority]]; loudness consistent with its category.
- [ ] Variations provided for frequent sounds to avoid repetition.
- [ ] Clear on phone speakers; important cues (raid alert, rare-spawn announcement, cooldown ready) remain audible in a busy fight.
- [ ] Respects the volume settings in [[UI - Settings]].
- [ ] Rights and licences recorded; registered as SFX-### or MUS-## in the [[Asset Register]].

## 6. Service (server or client technical component)

- [ ] Follows [[Service Architecture]], [[Luau Coding Standards]] and [[Module Patterns and Bootstrapping]]; public interface documented in its service page.
- [ ] Unit tests for pure logic and integration tests with test doubles (DataStore, RNG, clock) pass.
- [ ] All remotes listed in [[Remote Communication Contract]] with payload types, validation and rate limits.
- [ ] Errors handled and logged per [[Logging and Error Handling]]; no unhandled errors in a 60-minute soak.
- [ ] DataStore usage within budget; writes use `UpdateAsync`; session locking respected ([[Service - DataService]]).
- [ ] Server performance within [[Animal Scalability and Performance Budgets]].
- [ ] Any Roblox platform behaviour relied upon is verified against official documentation or marked *unverified* in [[Roblox API Reference Notes]].
- [ ] Security review against [[Threat Model]] completed for any service that changes items, Cash or odds.

## 7. Data change (schema, migration, configuration structure)

- [ ] The schema document is updated ([[Schema - Player Profile]] and related schemas) with a new schema version.
- [ ] A migration from every supported previous version exists and is tested (TC-PER-030 to 032).
- [ ] Older builds cannot overwrite newer data (TC-PER-031).
- [ ] Defaults for new fields are safe for existing players.
- [ ] Maximum-size profile measured and recorded (TC-PER-007).
- [ ] Rollback plan written: what happens if the release is reverted.
- [ ] [[Data Validation and Migration]] updated.

## 8. Balance change (numbers, odds, pools, costs, rewards)

- [ ] The value is changed in [[Canonical Proposed Values]] first, with status (**PROPOSED** unless the owner confirmed it) and a [[Changelog]] entry.
- [ ] Generated tables regenerated and checked ([[Dynamic Luck Probability Tables]], [[Hatch Pool Tables]], [[Animal Statistics Database]]).
- [ ] Impact assessed with [[Balancing Methodology]], [[Expected Value Calculations]] or the [[Balance Simulation Plan]] as appropriate.
- [ ] For odds or pool changes: the statistical gate passes and the new odds are disclosed before commit; existing purchased eggs keep their rarity and the change is never silent (D-017).
- [ ] Economy effects checked against [[Inflation and Farming Exploit Risks]] and [[Progression Bottleneck Analysis]].
- [ ] Live changes follow the [[Balance Update Process]], including player-facing notes per [[Versioning and Changelog Policy]].

## 9. Documentation (vault document)

- [ ] File name equals the title; frontmatter complete and valid YAML per [[Frontmatter Schemas]].
- [ ] Statuses used correctly: only Decision Register entries marked confirmed are called **CONFIRMED**; open items cite a Q-ID.
- [ ] Every wikilink resolves to a document in the [[Vault Map]]; heading links point to headings that exist.
- [ ] Mermaid diagrams render; code is labelled as illustrative Luau.
- [ ] No duplicated explanations: concepts owned elsewhere are linked, not re-explained.
- [ ] British English; ends with a "Related documents" section.
- [ ] Index page of the folder lists the document with a one-line description.

## 10. Bug fix

- [ ] Root cause recorded on the bug.
- [ ] Fix verified by QA on a build containing it.
- [ ] Regression test case added or updated and cited on the bug.
- [ ] Related systems smoke-tested.

## Related documents

- [[Backlog Index]]
- [[Product Backlog]]
- [[QA Strategy]]
- [[Test Plan Matrix]]
- [[Bug Reporting and Severity]]
- [[Asset Register]]
- [[Template - Task]]
