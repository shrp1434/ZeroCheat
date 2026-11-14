---
title: M10 - Ascension
type: milestone
category: roadmap
status: mixed
priority: P0
owner: Production Manager
last_updated: 2026-11-14
tags:
  - roadmap
  - milestone
  - ascension
milestone: M10
stage: 3
complexity: M
---

# M10 - Ascension

> [!info] PROPOSED milestone
> Stage 3 · Size **M** · Critical path: no (10 units of slack) · Exit gate: **G3 Core loop slice**

## Objective

Give duplicates their purpose. Ascension consumes duplicates of the same animal and keeps the original (D-019 **CONFIRMED**). The PROPOSED model has five levels (A1–A5) with duplicate requirements and Cash fees that vary by rarity, stat gains per level and a visual tier per level ([[Canonical Proposed Values#9. Ascension (PROPOSED — levels Q-004, duplicates Q-005)]]).

## Deliverables

| Deliverable | Track | Owning document |
|---|---|---|
| Ascension rules and table in config | Design, Engineering | [[Ascension System]], [[Ascension Progression Table]] |
| Ascension transaction: validate duplicates, consume, debit fee, raise level, atomic save | Engineering | [[Implementation - Ascension Transaction]], [[Service - AscensionService]] |
| Stat and ability scaling per level | Engineering | [[Ascension System]], [[Damage, Defence and Health Model]] |
| Ascension screen with duplicate selection and preview | UI | [[UI - Ascension]] |
| Visual tiers A1–A5 | Art, VFX | [[Rarity Visual Language]], [[VFX - Rarity and Variant Effects]] |
| Ascension animation and sound | Animation, Audio | [[Animation - Ascension]], [[Sound - Ascension]] |
| Expected-value check of duplicate supply per rarity | Economy | [[Ascension Expected Value Analysis]] |

## Dependencies

- **Upstream:** [[M09 - Hatching]] (duplicates come from hatches).
- **Downstream:** [[M18 - UI and UX]].

## Complexity

**M.** A self-contained transaction. Care is needed with which instance is kept, equipped animals and stolen-animal interactions later.

## Risks

| Risk | Why it matters here |
|---|---|
| R-025 (duplication) | Interrupted ascension must not duplicate or lose animals. |
| R-038 (nerfs to ascended animals) | Ascension creates long-term investment that balance updates must respect. |
| R-005 (bad luck) | Ascension is the main answer to duplicate-heavy luck. |

## Acceptance criteria

- [ ] Ascension consumes exactly the configured number of duplicates of the same species and keeps the selected original.
- [ ] The player chooses which instances are consumed; equipped animals and the original cannot be consumed by mistake.
- [ ] Stats rise by the configured amount per level; ability effectiveness rises separately.
- [ ] Visual tier updates immediately and replicates to other players.
- [ ] An interrupted transaction leaves the collection unchanged or fully ascended, never in between.
- [ ] Ascending beyond the configured maximum is rejected.

## Testing requirements

- [[Test Cases - Ascension]]: requirements, fees, instance selection, stat changes, maximum level.
- [[Test Cases - Persistence]]: transaction under shutdown.
- [[Test Cases - Exploit Prevention]]: forged instance IDs, consuming animals the player does not own, concurrent requests.

## Open questions

- [[Open Questions#Q-004]]: exact ascension levels (working assumption 5). Blocks beta.
- [[Open Questions#Q-005]]: exact duplicate requirements. Blocks launch.
- [[Open Questions#Q-025]]: what a stolen animal keeps (affects whether ascension level transfers in raids).

## Key vault documents
- [[Ascension System]] · [[Ascension Progression Table]] · [[Ascension Expected Value Analysis]]
- [[Implementation - Ascension Transaction]] · [[Service - AscensionService]] · [[UI - Ascension]]

## Related documents
- [[Development Roadmap]]
- [[M09 - Hatching]]
- [[M15 - Base Raids]]
- [[M18 - UI and UX]]
- [[Balance Update Process]]
