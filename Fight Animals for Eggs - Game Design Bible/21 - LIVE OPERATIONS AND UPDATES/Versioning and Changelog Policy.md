---
title: Versioning and Changelog Policy
type: policy
category: live-ops
status: proposed
priority: P1
owner: Live Operations Director
last_updated: 2026-11-14
tags:
  - live-ops
  - versioning
  - changelog
  - release
  - odds-disclosure
---

# Versioning and Changelog Policy

How game releases and configuration tables are numbered, how changes are written up for players and for the team, and the checklist every release must pass. Update proposals and release notes are written on [[Template - Update]], which is maintained by the lead.

> [!info] PROPOSED
> The whole policy is **PROPOSED**. The rollout method by which live servers move to a new version is **UNDECIDED** (Q-1115).

## Game version

Game releases use semantic-style versioning: **MAJOR.MINOR.PATCH**, plus a build number for internal tracking.

| Part | Increment when | Examples |
|---|---|---|
| **MAJOR** | A major expansion or a change to a core system; or the first public launch | New region with new systems; launch |
| **MINOR** | A content update, balance update, economy adjustment, seasonal update or event that needs a build | New animals; new boss; ascension retune |
| **PATCH** | Bug fixes and hotfixes with no new content | Exploit fix; UI fix |
| **Build** | Every release candidate build | `1.4.2+b318` (illustrative) |

Rules:
1. Pre-launch builds use `0.MINOR.PATCH`. The first public launch is `1.0.0` (**PROPOSED**).
2. Version numbers never go backwards. A rollback republishes old content under a **new** version number.
3. A hotfix to an older line is not allowed; fixes go forward on the current line.
4. The game version is shown in the settings screen ([[UI - Settings]]) so that bug reports include it.

## Config versions

Configuration tables change independently of the game build (through the config-only lane in [[Content Update Pipeline]]), so each family has its own monotonically increasing integer version.

| Config family | Version name | Covers | Bumps when |
|---|---|---|---|
| Odds tables | `oddsTableVersion` | Egg-rarity base table and slopes, pivot, hatch-pool membership, class weights, tilt, Progression Score input ranges | **Any** change that can alter a player's displayed or actual odds |
| Balance | `balanceConfigVersion` | Animal stats, abilities, player combat values, boss tuning | Any balance value change |
| Economy | `economyConfigVersion` | Prices, fees, rewards, multipliers, costs | Any economy value change |
| Events | `eventConfigVersion` | Event flags, event rules, event tables | Any event change |
| Live flags | `flagsVersion` | Kill switches | Any flag flip |
| Save data | `dataSchemaVersion` | Profile schema | Any schema change ([[Data Validation and Migration]]) |

### How `oddsTableVersion` relates to the `oddsVersion` token

The `oddsVersion` token (D-041, **PROPOSED**; [[Canonical Proposed Values#8. Dynamic progression luck (PROPOSED — final formula UNDECIDED, Q-017)]]) is issued by the server with each displayed odds table for one player at one moment. It is derived from:
- the current `oddsTableVersion`, and
- the player's current progression inputs (so a level-up also invalidates it).

When `oddsTableVersion` increments, every token issued under the old version becomes stale. The server rejects a commit that carries a stale token, takes no Cash and consumes no eggs, and the client re-displays the new odds before the player can commit again. This is what makes "odds must never change silently" (D-017 **CONFIRMED**) enforceable during an update.

> [!info] Illustrative Luau, not run in Roblox Studio
> ```lua
> -- Illustrative only: expose versions to clients and logs.
> local ReplicatedStorage = game:GetService("ReplicatedStorage")
> local Versions = {
> 	game = "1.0.0",
> 	build = 1,
> 	oddsTableVersion = 1,
> 	balanceConfigVersion = 1,
> 	economyConfigVersion = 1,
> 	dataSchemaVersion = 1,
> }
> for key, value in pairs(Versions) do
> 	ReplicatedStorage:SetAttribute("Version_" .. key, value)
> end
> ```
> The real source of the version values is the configuration modules ([[Configuration Modules]]), not a hand-edited table.

### Every log line carries versions

Every roll, hatch, merge, ascension, purchase and raid transfer log entry records the game version and the `oddsTableVersion` (where relevant), so any disputed outcome can be checked against the exact table in force ([[Logging and Error Handling]]).

## Changelog format

Two records are kept for every release.

### 1. Player-facing patch notes

Written from [[Template - Update]] and published in-game and on the experience's update channel.

```markdown
## Version 1.3.0 — <update name>

### New
- <content added, in plain language>

### Odds changes
- <every pool or table that changed, with old and new odds for affected items, or a link to the in-game odds screen>

### Balance
- <animal or system>: <old value> → <new value>. Why: <one line>.

### Fixes
- <bug fixed, in player terms>

### Known issues
- <anything still open that players may meet>
```

Rules:
- The **Odds changes** section is mandatory whenever `oddsTableVersion` changed, even if the change is a side effect (for example a new base module changing the Progression Score maximum). If nothing changed, write "None".
- Every balance change shows the old and new value.
- Plain language; no internal IDs; never describe an **UNDECIDED** item as final.

### 2. Internal release record

An entry in the vault [[Changelog]] for each release, linking the update document and listing:

| Field | Content |
|---|---|
| Game version and build | `1.3.0+b412` |
| Config versions | All six families, with old → new where changed |
| Decisions applied | `D-` IDs from the [[Decision Register]] |
| Questions resolved | `Q-` IDs moved out of [[Open Questions]] |
| Documents changed | Links to every vault document updated |
| Verification records | Links to statistical verification output and test runs |
| Approvals | Who approved, including odds sign-off |
| Rollback plan | Previous version and data compatibility note |

## Release checklist

A release is **no-go** until every applicable line is ticked. Lines marked ⚠ are compliance or data-safety lines and may never be waived.

**Scope and approval**
- [ ] Update document complete on [[Template - Update]] and approved by the owner.
- [ ] Version numbers assigned (game, build, and every changed config family).

**Data safety**
- [ ] ⚠ Data migrations tested on copies of real profile shapes; the previous game version can still read migrated data.
- [ ] ⚠ Item audit and raid reconciliation pass in staging.
- [ ] ⚠ Shutdown and rejoin during each transaction type tested ([[Test Cases - Persistence]]).

**Odds and compliance**
- [ ] ⚠ Every changed pool sums to 100% at every sample progression level (automated check).
- [ ] ⚠ Statistical sampling passed for every changed table ([[Statistical Testing of Probabilities]]).
- [ ] ⚠ Displayed odds equal server odds on every roll and hatch surface (parity check).
- [ ] ⚠ `oddsTableVersion` incremented for any odds change; stale-token rejection tested.
- [ ] ⚠ Advance notice of odds changes published in-game.
- [ ] ⚠ Odds sign-off recorded (authority **UNDECIDED**, Q-1117).
- [ ] ⚠ No product sells Cash for Robux unless [[Open Questions#Q-032]] was decided otherwise and paid-random-item handling is in place ([[Roblox Monetisation Policy Requirements]]).
- [ ] ⚠ Wild spawn rarity confirmed independent of player luck (regression test).

**Quality**
- [ ] Feature test cases for the new content passed.
- [ ] Regression subset passed: [[Test Cases - Egg Rolls and Hatching]], [[Test Cases - Persistence]], [[Test Cases - Exploit Prevention]], plus areas touched.
- [ ] Performance benchmarks within targets ([[Test Cases - Mobile Performance]]).
- [ ] No open top-severity defect ([[Bug Reporting and Severity]]).

**Communication and operations**
- [ ] Player-facing patch notes ready, including the Odds changes section.
- [ ] Internal [[Changelog]] entry drafted.
- [ ] Kill switches for touched systems tested.
- [ ] Monitoring watch list for the release agreed ([[Live Operations Framework#Health monitoring]]).
- [ ] Rollback build identified.

## Related documents
- [[Live Operations Index]]
- [[Content Update Pipeline]]
- [[Content Expansion Guidelines]]
- [[Balance Update Process]]
- [[Live Operations Framework]]
- [[Changelog]]
- [[Template - Update]]
- [[Randomised Reward Compliance]]
