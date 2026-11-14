---
title: Frontmatter Schemas
type: reference
category: templates
status: confirmed
priority: P0
owner: Technical Documentation Architect
last_updated: 2026-11-14
tags:
  - templates
  - conventions
  - frontmatter
---

# Frontmatter Schemas

Every note in the vault starts with YAML frontmatter. The schemas below keep the vault filterable with Obsidian's core search (`[type:animal]`, `tag:#combat`) and, optionally, the Dataview community plugin ([[Recommended Obsidian Plugins]]). This page documents the vault's conventions (status **CONFIRMED** as a documentation standard); it makes no game-design decision.

## Common fields (all notes)

| Field | Type | Required | Allowed values | Notes |
|---|---|---|---|---|
| `title` | string | Yes | Must equal the file name | Quote it if it contains `:`, `#`, `'` or `"` |
| `type` | string | Yes | See the type list below | |
| `category` | string | Yes | Folder topic, for example `combat`, `eggs`, `ui` | Lowercase |
| `status` | string | Yes | `confirmed`, `proposed`, `undecided`, `deprecated`, `mixed` | `mixed` = contains items with several statuses |
| `priority` | string | Yes for systems, features, assets and tasks | `P0`, `P1`, `P2`, `P3` | P0 = essential for launch |
| `owner` | string | Yes | Discipline role, not a person's name | For example `Combat Designer` |
| `last_updated` | date | Yes | `YYYY-MM-DD` | |
| `tags` | list | Yes | Lowercase, hyphenated | No spaces, no `#` |

## Type list

| `type` | Used for | Extra fields |
|---|---|---|
| `dashboard` | Home and dashboards | — |
| `index` | Folder index pages and maps of content | — |
| `system` | Game systems | — |
| `feature` | Discrete features | `milestone` |
| `spec` | Specifications, formulas, data tables | — |
| `analysis` | Balance and EV analyses | — |
| `animal` | Animal documents | `name`, `species`, `animal_id`, `rarity`, `family`, `role`, `habitat`, `pool_class`, `ability_activation` |
| `region` | World regions | `region_index`, `region_multiplier` |
| `boss` | Mini-bosses and world bosses | `boss_type`, `boss_id`, `region` |
| `egg` | Egg type documents | `egg_id`, `rarity` |
| `ui-screen` | UI screen specifications | `screen_id` |
| `animation` | Animation specifications | `animation_id`, `rig` |
| `vfx` | VFX specifications | `vfx_id` |
| `sound` | Sound specifications | `sound_id` |
| `service` | Technical services | `service_name` |
| `implementation` | Luau implementation notes | — |
| `schema` | Data schemas | `schema_version` |
| `test-suite` | QA test case collections | `system` |
| `milestone` | Roadmap milestones | `milestone_id`, `complexity` |
| `task` | Backlog items | `task_id`, `milestone`, `estimate`, `assignee` |
| `decision` / `decision-register` | Decisions | `decision_id`, `decided_by`, `supersedes` |
| `update` | Live update notes | `version`, `config_version`, `release_type` |
| `reference` | References, conventions, glossary | — |
| `template` | Templates (this folder) | — |

## Animal example

```yaml
---
title: Tiger
type: animal
name: Tiger
species: Panthera tigris
animal_id: ANM-034
rarity: Epic
family: Big Cats
role: Assassin
habitat: Emerald Canopy
pool_class: Standard
ability_activation: Auto and Manual
status: proposed
priority: P1
owner: Animal and Character Designer
last_updated: 2026-11-14
tags:
  - animal
  - epic
  - big-cats
  - assassin
  - emerald-canopy
---
```

## System example

```yaml
---
title: Egg Merging
type: system
category: eggs
status: mixed
priority: P0
owner: Systems Designer
last_updated: 2026-11-14
tags:
  - eggs
  - merging
---
```

## Search recipes (core Obsidian, no plugins)

| Goal | Search query |
|---|---|
| All Epic animals | `[rarity:Epic]` |
| All proposed systems | `[type:system] [status:proposed]` |
| Everything P0 | `[priority:P0]` |
| Every UNDECIDED marker in body text | `"UNDECIDED"` |

## Related documents

[[Templates Index]] · [[How To Use This Vault]] · [[Vault Map]]
