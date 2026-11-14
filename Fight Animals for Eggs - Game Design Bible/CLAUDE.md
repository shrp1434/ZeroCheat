# CLAUDE.md — Vault Rules for AI and Human Contributors

This file governs every edit to the **Fight Animals for Eggs — Game Design Bible** Obsidian vault. Read it in full before creating or changing any document.

## 1. What this vault is

The single source of truth for the Roblox game **Fight Animals for Eggs**: design, art, audio, technical architecture, data, QA, production and live operations. The project owner has final authority over every game decision.

## 2. Status vocabulary (mandatory)

Every mechanic, value and rule carries exactly one status:

| Status | Meaning | Who may set it |
|---|---|---|
| **CONFIRMED** | Explicitly decided by the project owner. Listed in the Decision Register with a `D-` ID and status confirmed. | Project owner only |
| **PROPOSED** | A recommendation from the team. Usable for prototyping. Must not be treated as final. | Anyone |
| **UNDECIDED** | An open question. Listed in Open Questions with a `Q-` ID. Options may be documented; no answer is chosen. | Anyone may raise |
| **DEPRECATED** | Previously proposed or confirmed, now superseded. Keep it for history and link to the replacement. | Owner (for confirmed) / author (for proposals) |

Rules:
1. Never upgrade a PROPOSED item to CONFIRMED without a recorded owner decision.
2. Inline, write statuses in bold capitals: **CONFIRMED**, **PROPOSED**, **UNDECIDED**, **DEPRECATED**.
3. In tables, include a `Status` column whenever rows can differ in status.
4. Use callouts for status-heavy blocks:
   - `> [!success] CONFIRMED` for owner decisions
   - `> [!info] PROPOSED` for recommendations
   - `> [!warning] UNDECIDED` for open questions
   - `> [!danger]` for compliance, security or data-loss risks
5. A document whose contents mix statuses uses `status: mixed` in frontmatter.

## 3. Canonical facts (never contradict)

These are **CONFIRMED** by the owner (see [[Decision Register]]):

- Title: *Fight Animals for Eggs*. Platform: Roblox. One large shared world; single-player and multiplayer.
- Seven rarities, in order: Common, Uncommon, Rare, Epic, Legendary, Mythical, Secret.
- Launch target: 60 animals. (The 12/11/10/9/8/6/4 split is **PROPOSED**.)
- Real-time hybrid combat: the player and their animals fight together. The player has basic attacks and special moves; special moves may have cooldowns.
- **Team size: exactly THREE equipped animals.**
- Player strength is a separate statistic from animal strength.
- Animal abilities can be manual or automatic. Both kinds exist.
- Animals auto-target nearby enemies. Players can issue manual target commands.
- The team can be changed **only at the player's own base**. It is locked after leaving the base until the player returns.
- Wild animals respawn. Rarer animals respawn more slowly. Mini-bosses and world bosses exist.
- The defeat penalty system is mixed, varying by battle type. Exact penalties are **UNDECIDED**.
- Cash comes from defeating wild animals. Cash buys egg rolls.
- Two-stage randomness: (1) the roll decides egg rarity; (2) hatching picks an animal from that rarity's pool.
- Up to **five** eggs can be hatched at once.
- Hidden progression-based luck changes egg-rarity odds and hatch odds. It does **not** change wild encounter rarity. The formula may stay hidden. The **actual odds must be shown before the player commits**, and odds must never change silently after a purchase.
- Every hatch is independent: no duplicate protection, no bias towards unowned animals, no influence from earlier hatches.
- Ascension: duplicates of the same animal are consumed; the original is kept.
- Egg merging: three eggs of one rarity make one egg of the next rarity. It needs a purchased **Egg Merging Station**, which must be upgraded before it can merge higher rarities and which physically changes appearance as it is upgraded.
- Egg storage starts at **Backpack 10 + Base 50 = 60**. Backpack eggs can never be stolen. Extra space can be bought; the currency and pricing are **UNDECIDED**.
- Every player has a modular base, and each section is upgraded separately.
- PvP is optional. Base raiding is optional.
- Raids: eggs stored in the base can be stolen. A defending animal can be stolen only after it has been knocked out. Undefeated defenders cannot be stolen. **Maximum THREE animals stolen per successful raid.** Offline bases cannot be raided. Bases are protected by shields and physical defences.
- Raid duration and the egg theft limit are **UNDECIDED**. Never invent them as final values.
- Visual direction: colourful, polished, low-poly animals. No horror, no "Italian brainrot", no meme animals.
- Monetisation is balanced. The game must be fully playable without Robux. Paid random rewards must not be the main revenue source.

## 4. Proposed numbers live in one place

All proposed numeric values (stats, prices, probabilities, curves) are defined in [[Canonical Proposed Values]]. Do not invent conflicting numbers elsewhere. If a document needs a new value, add it to Canonical Proposed Values (marked **PROPOSED**) and reference it. Generated tables:
- [[Animal Statistics Database]] — per-animal stats
- [[Dynamic Luck Probability Tables]] — egg-rarity odds at sample progression levels
- [[Hatch Pool Tables]] — per-rarity hatch odds (each pool checked to sum to 100%)

## 5. File and link conventions

- Every document's file name is its title. File names are **unique across the vault** so `[[Title]]` always resolves.
- Link only to documents listed in [[Vault Map]]. Never create links to documents that do not exist.
- Inside Markdown tables, escape the alias pipe: `[[Egg Roll System\|egg rolls]]`.
- Heading links use `[[Document#Heading]]`. Only link to headings that exist.
- Use British English (colour, defence, behaviour).
- Do not duplicate explanations. Explain each concept once, in its owning document, and link to it from everywhere else.

## 6. Frontmatter

Every note starts with YAML frontmatter. Schemas are defined in [[Frontmatter Schemas]]. Minimum fields:

```yaml
---
title: Exact File Name
type: system
category: combat
status: mixed
priority: P0
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
---
```

- Tags are lowercase and hyphenated, with no spaces.
- `status` is one of: confirmed, proposed, undecided, deprecated, mixed.
- `priority` is one of: P0, P1, P2, P3 (P0 = essential for launch).

## 7. Diagrams

Use Mermaid in fenced ```` ```mermaid ```` blocks. Keep diagrams valid:
- Put labels containing spaces or punctuation in double quotes: `A["Egg Roll (server)"]`.
- Do not use the bare lowercase word `end` as a node ID.
- Avoid `;` and unescaped quotes inside labels.
- Supported types: flowchart / graph, sequenceDiagram, stateDiagram-v2, erDiagram, classDiagram, gantt, pie, mindmap.

## 8. Technical honesty

- Code in this vault is **illustrative Luau** unless a document states it was executed. None has been run in Roblox Studio at the time of writing.
- Never invent Roblox APIs. Mark any platform behaviour that has not been verified against official documentation as *unverified*.
- Never invent URLs, images or external research.

## 9. Asset IDs

| Prefix | Asset class |
|---|---|
| ANM-### | Animal models (ANM-001 to ANM-060 follow catalogue order) |
| VAR-### | Variant material sets |
| BOS-## | Boss models |
| EGG-## | Egg models |
| ENV-### | Environment kits and props |
| MOD-## | Base module models |
| UI-### | UI assets |
| ANI-### | Animations |
| VFX-### | Visual effects |
| SFX-### | Sound effects |
| MUS-## | Music |

The master list is the [[Asset Register]].

## 10. When uncertain

Document the question in [[Open Questions]] with a new `Q-` ID instead of inventing an answer.
