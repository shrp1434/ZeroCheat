---
title: Module - Animal Pens
type: system
category: base
status: mixed
priority: P1
owner: Base-Building Designer
last_updated: 2026-11-14
tags:
  - base
  - module
  - animals
  - performance
  - raiding
---

# Module - Animal Pens

**Asset ID:** MOD-01 (**PROPOSED**). **Slot:** flexible, recommended front row.

> [!warning] UNDECIDED
> - Whether owned animals are physically displayed in pens: **UNDECIDED** ([[Open Questions#Q-008]]). It drives the performance budget, so it blocks the pen prototype.
> - Whether pens provide guard posts depends on **UNDECIDED** [[Open Questions#Q-033]].
> - Whether this module ships at launch: **UNDECIDED** ([[Open Questions#Q-007]]).

## 1. Purpose

The diegetic home of the player's collection: the place where the team is changed, where favourite animals are shown off, and (if Q-033 resolves to pen guards) where guard animals are posted. The pens do **not** add animal storage capacity; owned-animal capacity is **UNDECIDED** ([[Open Questions#Q-022]], working assumption 100).

## 2. Footprint and appearance

| Property | Proposal |
|---|---|
| Footprint | 30 × 22 studs inside a 32 × 32 slot; 1 entrance facing the Base Core |
| Height | 8 studs (L1) to 14 studs (L5, with canopy) |
| Appearance | A paddock with low fences, a feeding trough, a team-change totem at the entrance and guard-post plinths along the front fence |
| Materials | Wood, rope, hay, grass; later stone, brass and crystal per the shared ladder in [[Base Upgrade System]] |

## 3. Upgrade levels

| Level | Cost (Cash) | Showcase spots (PROPOSED) | Guard posts (PROPOSED, if Q-033 = B or C) | Visual change |
|---:|---:|---:|---:|---|
| L1 | 1,000 | 2 | 1 | Rope-and-post paddock, hay bales, wooden team totem |
| L2 | 2,500 | 4 | 2 | Planed fences, stone water trough, flower boxes |
| L3 | 6,250 | 6 | 3 | Stone gateposts with brass lanterns, a shaded lean-to |
| L4 | 15,625 | 8 | 4 | Crystal-capped posts, a small pond, violet glow on the totem |
| L5 | 39,063 | 10 | 5 | Gold-trimmed canopy, gentle aura over the paddock, banner with the player's favourite animal |

Total: **64,438 Cash**. Level cap is `PlotStage + 1` ([[Base Layout and Plot Expansion]]).

## 4. Display options for Q-008

The core question: if a player owns ~100 animals and a server has 16 bases, physically displaying everything means up to **1,600** animated animals.

| Option | What is shown | Instances per base | Server cost | Client cost | Verdict |
|---|---|---:|---|---|---|
| A. No physical display | Pens are scenery; the collection is UI-only ([[UI - Animal Inventory]]) | 0 | None | None | Cheapest; loses a key "show-off" moment |
| B. Curated showcase | The player picks 2–10 showcase animals (by level) | ≤ 10 | Stores a list of UIDs only | Rendered client-side when within streaming range; low-LOD model and simple idle loops | **Recommended** |
| C. Rotating sample | The pen shows a random rotating selection of owned animals | ≤ 10 | Minimal | As B, plus swap cost every rotation | Viable alternative; less player agency |
| D. Full display | Every owned animal is present | up to ~100 | High if server-simulated | Very high on mobile | Rejected for performance |

> [!info] PROPOSED recommendation: Option B
> Showcase animals are **client-rendered cosmetics** with no server physics or AI. The server replicates only a list of species and variant IDs as an attribute string. Guards (if any) are separate server agents and only gain full AI during a raid. Final decision: **UNDECIDED** ([[Open Questions#Q-008]]).

Showcase animals are spaced on fixed spots and play idle, sit and "look at player" animations from [[Animation - Animal Locomotion]]. Rendering obeys [[Animal Scalability and Performance Budgets]]: beyond 120 studs a showcase animal is hidden; on low-end mobile only 4 are shown.

## 5. Functionality

| Function | Proposal |
|---|---|
| Team change point | The totem at the entrance opens [[UI - Team Selection]]. Team changes are allowed anywhere in the plot ([[Team Equipping and Base Lock Rule]]); the totem is the visible, discoverable place. Without pens, the Base Core serves |
| Showcase | Choose animals for the showcase spots |
| Guard posts | Assign animals as guards (if Q-033 = B or C). See [[Animal Guards and Base Defence AI]] |
| Progression Score | Each level counts towards the 44 base levels |

## 6. Dependencies

- Requires a free slot.
- Guard assignment requires Q-033 to resolve to B or C.
- Showcase requires Q-008 to resolve to B or C.

## 7. Technical implementation

| Layer | Detail |
|---|---|
| Server data | `base.modules.AnimalPens = { level, slot }`, `base.showcase = { animalUid, ... }`, `base.guardAssignments = { animalUid, ... }` ([[Schema - Base Data]]) |
| Instances | `Plot_##.Modules.AnimalPens` (Model, tag `BaseModule`), child `Totem` with a ProximityPrompt, `ShowcaseSpots` (Attachments), `GuardPosts` (Attachments) |
| Replication | Attribute `ShowcaseSpecies` on the module (comma-separated species IDs and variant IDs). The client builds showcase models from local templates |
| Streaming | Module model streams as one unit; showcase models are created by the client only when the module is streamed in and destroyed when it streams out |
| Validation | Showcase and guard UIDs must be owned and not in the equipped team; guard assignment locked during raids |

## 8. Animation and VFX

- Upgrade: fence posts hammer in from the ground (0.3 s stagger), dust puffs, totem lights up ([[Animation - Base Upgrades]]).
- Showcase animals react with a happy emote when their owner walks past (client-side).
- Team change at the totem: short swirl of leaves around the three new team members ([[VFX Bible]]).

## 9. Raid interaction

| Situation | Behaviour |
|---|---|
| Showcase animals | Cosmetic only. Never targetable, never stealable |
| Guards | Defend from their posts, can be knocked out and then stolen ([[Animal Theft Rules]]) |
| Totem | Cannot be used by raiders; the owner can still change team during a raid only if Q-035 allows the owner's team to defend (otherwise locked to avoid mid-raid swaps) |
| Module itself | Not damaged or disabled by raids (Q-403 open for temporary disabling) |

## Related documents
- [[Player Base System]]
- [[Animal Guards and Base Defence AI]]
- [[Team Equipping and Base Lock Rule]]
- [[Animal Collection System]]
- [[Animal Scalability and Performance Budgets]]
- [[Base Art Direction]]
- [[Cost Tables]]
- [[Player Bases Index]]
