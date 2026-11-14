---
title: Changelog
type: reference
category: decisions
status: confirmed
priority: P1
owner: Production Manager
last_updated: 2026-11-14
tags:
  - changelog
  - decisions
---

# Changelog

A dated record of changes to the vault and to game decisions. The format and the versioning rules are defined in [[Versioning and Changelog Policy]]. Vault versions use `MAJOR.MINOR.PATCH`: MAJOR for a restructure, MINOR for new documents or decisions, PATCH for corrections.

## v0.1.0 — 2026-11-14 — Vault created

### Added
- Vault structure: 28 numbered folders (00–27), the Home and Design and Development dashboards, the [[Vault Map]], [[How To Use This Vault]], the root `README.md` and `CLAUDE.md`, and `.obsidian` configuration (core plugins, a templates folder, bookmarks).
- [[Decision Register]] with 29 **CONFIRMED** owner decisions (D-001 to D-029), recorded from the owner's brief, and 16 **PROPOSED** team decisions (D-030 to D-045).
- [[Open Questions]]: Q-001 to Q-019 from the owner's brief, plus Q-020 to Q-035 raised by the team.
- [[Canonical Proposed Values]]: the single source for all proposed numbers.
- 60 animal documents, generated from one data model with the [[Animal Stat Budget Model]], plus the [[Animal Index]], [[Animal Statistics Database]], [[Animal Roles]], [[Animal Families]], [[Animal Variants]] and [[Animal Abilities Catalogue]].
- [[Dynamic Luck Probability Tables]] and [[Hatch Pool Tables]], generated and checked so that every distribution sums to 100%.
- Full documentation for vision, core gameplay, world (8 regions, a hub, 8 mini-bosses, 4 world bosses), combat, eggs and hatching, ascension and progression, bases, PvP and raiding, economy and monetisation, UI/UX, art, animation and VFX, sound, technical architecture, Luau implementation, multiplayer and security, data and balancing, QA, roadmap (23 milestones), live operations, references, backlog, 16 templates and the glossary.
- A concept title treatment (an original SVG placeholder, not a final logo).

### Verified
- Animal count 60, with a rarity split of 12/11/10/9/8/6/4 (generator assertion).
- Every animal's Power Index lies within ±0.06 of its role target (generator assertion).
- Every hatch pool and egg-rarity table sums to 100% at all sampled progression levels (generator assertion).
- Link and frontmatter audit results are recorded in the final audit section below.

### Not verified
- No Luau has been executed. No Roblox Studio build exists. Roblox platform claims marked *unverified* in [[Roblox API Reference Notes]] still need checking against official documentation.

## Entry template

```markdown
## vX.Y.Z — YYYY-MM-DD — Short title
### Added
### Changed
### Deprecated
### Decisions
- D-0xx moved from PROPOSED to CONFIRMED by the owner (reason)
### Fixed
```

## Related documents

[[Decision Register]] · [[Decisions Index]] · [[Versioning and Changelog Policy]]
