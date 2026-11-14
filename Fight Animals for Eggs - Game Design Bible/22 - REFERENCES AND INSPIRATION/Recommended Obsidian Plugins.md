---
title: Recommended Obsidian Plugins
type: reference
category: references
status: proposed
priority: P3
owner: Technical Documentation Architect
last_updated: 2026-11-14
tags:
  - references
  - obsidian
  - tooling
---

# Recommended Obsidian Plugins

How to set up Obsidian for this vault. **The vault works without any community plugin.** Every document is plain Markdown with YAML frontmatter, wikilinks and Mermaid diagrams, all of which Obsidian renders out of the box. Community plugins are optional conveniences for people who want dashboards, boards or sketches.

> [!info] PROPOSED
> These are recommendations, not requirements. Never write a document whose meaning depends on a community plugin: plugin output (for example a query result) must also be understandable from the plain Markdown around it.

## Core plugins to enable

Core plugins ship with Obsidian. Enable them in **Settings → Core plugins**.

| Core plugin | Setting for this vault | Why |
|---|---|---|
| **Templates** | Template folder location: `25 - TEMPLATES` | Inserts the vault's templates (for example [[Template - Animal]], [[Template - Update]]) with the frontmatter from [[Frontmatter Schemas]] |
| **Graph view** | Optional filter: exclude `25 - TEMPLATES` to reduce noise | Shows how systems, milestones and decisions connect; orphan notes stand out |
| **Backlinks** | Show in the right sidebar | See every document that links to the one you are reading, for example every milestone that cites [[Randomised Reward Compliance]] |
| **Outline** | Show in the right sidebar | Navigate long documents such as [[Canonical Proposed Values]] by heading |
| Outgoing links | Optional | Spot links that do not resolve yet |
| Search | Enabled by default | Find Q- and D- IDs quickly, for example `Q-012` |
| Properties view | Optional | Read and edit frontmatter fields such as `status` and `owner` |

> [!tip] Templates folder
> The folder name must match exactly, including the number and spaces: `25 - TEMPLATES`. Templates are indexed in [[Templates Index]].

## Optional community plugins

Install from **Settings → Community plugins** only if you want them. Check each plugin's own documentation before use; behaviour described here is general and *unverified* against any specific plugin version.

| Plugin | Optional use in this vault | Without it |
|---|---|---|
| **Dataview** | Live tables of documents by frontmatter, for example all milestones with `status: mixed`, or every document owned by one role | Use the hand-written index pages (for example [[Roadmap Index]]) and [[Vault Map]] |
| **Templater** | Templates with automatic dates, file names and prompts | Use the core Templates plugin and fill fields by hand |
| **Kanban** | A working board for milestone or backlog tasks | Use [[Product Backlog]] and [[Development Dashboard]] |
| **Excalidraw** | Freehand sketches for level layouts or UI flows | Use Mermaid diagrams, or describe layouts in text; images are placeholders in [[Visual Reference Placeholders]] |

### Example Dataview query (optional)

If Dataview is installed, this lists every milestone with its status and size. Without Dataview, the block shows as plain code and the [[Roadmap Index]] table holds the same information.

```dataview
TABLE status, complexity, stage
FROM "20 - DEVELOPMENT ROADMAP/Milestones"
SORT milestone ASC
```

## Rules when using plugins

1. **Plain Markdown remains the source of truth.** A Dataview table is a view; the frontmatter it reads is the data.
2. **No plugin-only syntax in core content.** Keep Templater commands inside template files only, never in finished documents.
3. **Frontmatter stays valid YAML** whatever a plugin offers ([[Frontmatter Schemas]]).
4. **Do not commit personal plugin settings** that change how others see the vault; share recommendations here instead.
5. **Mermaid is built in.** Do not add a diagram plugin for diagrams Mermaid can draw.

## Related documents
- [[References Index]]
- [[How To Use This Vault]]
- [[Templates Index]]
- [[Frontmatter Schemas]]
- [[Vault Map]]
