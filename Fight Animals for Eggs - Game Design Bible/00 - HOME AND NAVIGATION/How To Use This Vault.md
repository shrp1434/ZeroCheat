---
title: How To Use This Vault
type: reference
category: navigation
status: confirmed
priority: P0
owner: Technical Documentation Architect
last_updated: 2026-11-14
tags:
  - navigation
  - conventions
  - onboarding
---

# How To Use This Vault

A practical guide for designers, engineers, artists, animators, testers and producers joining *Fight Animals for Eggs*.

## 1. Opening the vault

1. Install Obsidian (desktop) and choose **Open folder as vault**.
2. Select the folder `Fight Animals for Eggs - Game Design Bible`.
3. Open [[Home]]. Everything is reachable from there in two clicks.
4. No community plugins are required. Optional extras are listed in [[Recommended Obsidian Plugins]].

## 2. Reading order by discipline

| You are… | Start with | Then read |
|---|---|---|
| New to the project | [[Vision Statement and Pillars]] | [[Core Gameplay Loop]], [[Glossary]] |
| Game designer | [[Design Dashboard]] | [[Canonical Proposed Values]], [[Open Questions]] |
| Engineer | [[Development Dashboard]] | [[Architecture Overview]], [[Remote Communication Contract]], [[Security Architecture]] |
| Artist | [[Art Bible]] | [[Animal Modelling Principles]], [[Asset Register]] |
| Animator or VFX artist | [[Animation Bible]] | [[Animal Rig Standards]], [[VFX Bible]] |
| Sound designer | [[Sound Bible]] | [[Audio Mixing and Priority]] |
| QA | [[QA Strategy]] | [[Test Plan Matrix]], [[Statistical Testing of Probabilities]] |
| Producer | [[Development Roadmap]] | [[Product Backlog]], [[Risk Register]] |

## 3. The four statuses

Every mechanic and value is marked **CONFIRMED**, **PROPOSED**, **UNDECIDED** or **DEPRECATED**. Only the project owner confirms. The full rules are in the root `CLAUDE.md` and the [[Decisions Index]].

Callout conventions:

> [!success] CONFIRMED
> An owner decision, with its D- ID.

> [!info] PROPOSED
> A team recommendation.

> [!warning] UNDECIDED
> An open question, with its Q- ID.

> [!danger] Risk
> Compliance, security or data-loss hazards.

## 4. Where numbers come from

All proposed numbers live in [[Canonical Proposed Values]]. Three documents are **generated** from it and must not be hand-edited: [[Animal Statistics Database]], [[Dynamic Luck Probability Tables]] and [[Hatch Pool Tables]]. The 60 animal documents are generated from the same model. Change the inputs and regenerate; never hand-edit one cell.

## 5. Naming and linking

- File name = title. Titles are unique across the vault, so `[[Title]]` always resolves.
- Prefixes group related documents: `Region -`, `Mini-Boss -`, `World Boss -`, `Module -`, `UI -`, `Animation -`, `VFX -`, `Sound -`, `Service -`, `Implementation -`, `Schema -`, `Test Cases -`, `M01 -` to `M23 -`, `Template -`.
- Every folder has an index page. The [[Vault Map]] lists every document.

## 6. Adding or changing content

1. Find the owning document using the [[Vault Map]]. Do not duplicate explanations: link instead.
2. New documents use a template from [[Templates Index]] and follow [[Frontmatter Schemas]].
3. New numbers go into [[Canonical Proposed Values]] first.
4. New questions go into [[Open Questions]] with the next free Q- ID.
5. Any change to a decision goes through the [[Decision Register]] and the [[Changelog]].

## 7. Diagrams

Diagrams use Mermaid, which renders natively in Obsidian. Edit them as text; no plugin is needed.

## Related documents

[[Home]] · [[Vault Map]] · [[Glossary]]
