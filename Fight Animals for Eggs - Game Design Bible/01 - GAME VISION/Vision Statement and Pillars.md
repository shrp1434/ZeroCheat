---
title: Vision Statement and Pillars
type: vision
category: game-vision
status: mixed
priority: P0
owner: Executive Game Director
last_updated: 2026-11-14
tags:
  - vision
  - pillars
  - game-direction
---

# Vision Statement and Pillars

> [!success] CONFIRMED foundations
> Title *Fight Animals for Eggs* on Roblox (D-001), one large shared world for solo and multiplayer play (D-025), real-time hybrid combat (D-005), seven rarities (D-003), a launch target of 60 animals (D-004), two-stage egg randomness (D-015), hidden progression luck with honest disclosure (D-017), modular bases (D-022), optional PvP and raids (D-023, D-024) and balanced monetisation (D-027).

> [!info] PROPOSED
> The wording of the vision statement, the pillar names and the design tests in this document are proposals from the direction team. They interpret the confirmed facts; they do not add new rules.

## 1. Vision statement

**You and your three animals fight side by side across a living world, turn every victory into eggs, and grow a collection, a home and a reputation that are unmistakably yours.**

*Fight Animals for Eggs* is a real-time action-collection game. The player is never a spectator: they swing, dodge and use specials while three companions fight with them. Defeating wild animals earns Cash and fills the [[Animal Index Feature Specification|Animal Index]]; Cash buys egg rolls; eggs hatch into new companions; duplicates make favourites stronger through ascension; and a modular base turns all of that into a place to defend, show off and return to.

The game should feel **easy to understand within one minute, deep enough to master over months, and honest at every step where chance is involved.**

## 2. The five pillars

| # | Pillar | One-line promise | Confirmed basis | Systems that carry it |
|---|---|---|---|---|
| 1 | **Fight Together** | The player and three animals are one fighting unit. | D-005, D-006, D-008, D-009 | [[Combat System Overview]], [[Player Combat]], [[Animal Combat Behaviour]], [[Targeting and Command System]] |
| 2 | **Honest Luck** | Chance creates excitement, never suspicion. The odds you see are the odds you get. | D-015, D-017, D-018 | [[Egg Roll System]], [[Hatch System]], [[Dynamic Progression Luck]], [[Randomised Reward Compliance]] |
| 3 | **A Collection Worth Keeping** | Sixty distinct, readable animals, each with a role, a home and a reason to own several. | D-003, D-004, D-019, D-028, D-029 | [[Animal Collection System]], [[Animal Index Feature Specification]], [[Ascension System]], [[Animal Variants]] |
| 4 | **Grow Your Haven** | Your base is your loadout room, your vault and your trophy cabinet. | D-010, D-020, D-021, D-022 | [[Player Base System]], [[Team Equipping and Base Lock Rule]], [[Egg Merging Station]], [[Egg Storage]] |
| 5 | **Fair Rivalry** | Competing with other players is a choice, with clear limits on what can be lost. | D-023, D-024 | [[PvP System]], [[Base Raiding System]], [[Animal Theft Rules]], [[Design Principles and Fairness Charter]] |

### Pillar 1: Fight Together

The player is a combatant, not a summoner. Player [[Player Strength]] is a separate statistic from animal strength (D-007), so the player always matters, even with weak animals, and strong animals never make the player irrelevant. Animals auto-target but accept commands (D-009), so a new player can fight by pressing one button while a skilled player focuses fire, peels for a fragile Assassin and saves a manual ability for the right moment.

**Design test:** in any fight, removing the player's own damage should make the fight noticeably slower, and removing the animals should make it noticeably harder. If either side becomes optional, the pillar is broken.

### Pillar 2: Honest Luck

Luck in this game is **hidden but honestly disclosed**. The progression formula may remain private (D-017), but the actual rarity and hatch odds for *this player, right now* are always shown before they commit, and are bound to a server token so they cannot change silently (D-041 **PROPOSED**). Hatches are independent: no duplicate protection, no secret bias towards unowned animals (D-018). This honesty is part of the brand, not a compliance afterthought.

**Design test:** if a player screenshots the odds panel and then rolls, the server log for that roll must show the same odds version.

### Pillar 3: A Collection Worth Keeping

Every animal is recognisable at a glance, has a clear combat role (see [[Animal Roles]]) and belongs to a home region. Duplicates are never "dead pulls" because they feed [[Ascension System|ascension]] (D-019). The index records how and where the player met each species, so the collection is also a travel diary.

**Design test:** a player should be able to say why they want a specific animal (its role, its look, its region, its ascension) rather than only "because it is rarer".

### Pillar 4: Grow Your Haven

The base is where decisions happen. The team can only be changed there (D-010), merges happen there, base-stored eggs hatch there, and modules feed Strength, Cash and progression. Returning home is a ritual, not a chore.

**Design test:** a typical session should include at least one meaningful visit home, and every visit should offer at least one decision (equip, upgrade, merge, hatch, ascend).

### Pillar 5: Fair Rivalry

PvP and raiding are optional (D-023, D-024). The worst case is bounded and known in advance: backpack eggs are never stealable, offline bases cannot be raided, an undefeated defender cannot be taken, and no more than three animals can be stolen in one successful raid. Raid duration (Q-012) and egg theft limits (Q-013) are **UNDECIDED** and must be published to players once decided.

**Design test:** a player who never opts into PvP or raids must still be able to reach every region, every boss and every animal.

## 3. Experience goals

| Goal | What the player should feel | Measured by (PROPOSED) |
|---|---|---|
| Immediate clarity | "I know what to do next." | FTUE completion, first egg rolled within the first session ([[New Player Onboarding]]) |
| Mastery headroom | "I'm getting better, not just bigger." | Boss clear time variance between players of the same Progression Score |
| Long-session interest | "One more region, one more hatch." | Session length, return visits to base per session ([[Session Flow and Player Journey]]) |
| Ownership | "This collection and this base are mine." | Index completion spread, base module diversity |
| Trust | "The game is fair to me." | Support tickets about odds, raid complaint rate |

## 4. Tone and identity

- **Bright adventure, not comedy chaos.** Colourful, polished, low-poly animals with clear silhouettes (D-026). No horror, no "Italian brainrot", no meme animals. See [[Art Bible]].
- **Respect for animals.** Battles end in knock-outs, never gore. Defeated wild animals faint and fade; they do not die on screen. See [[Animation - Animal Defeat and Victory]].
- **Ancient wonder at the top end.** The proposed "ancient lineage" theme for Mythical and Secret animals (D-033 **PROPOSED**, [[Open Questions#Q-027]]) gives the rarest eggs a mythic, prehistoric flavour.

The full treatment of what makes this game distinct is in [[Unique Selling Points and Identity]].

## 5. What this game is not

| Not this | Because |
|---|---|
| An idle clicker where numbers fight for you | Pillar 1: the player fights in real time |
| A gacha storefront with a world attached | D-027: paid random rewards are not the main revenue source; D-044 **PROPOSED**: Cash is never sold for Robux |
| A forced-PvP survival game | D-023, D-024: PvP and raiding are optional |
| A trading economy | D-045 **PROPOSED**: no trading at launch ([[Open Questions#Q-026]]) |
| A meme-animal simulator | D-026 |

## Related documents
- [[Game Vision Index]]
- [[Target Audience and Player Motivations]]
- [[Unique Selling Points and Identity]]
- [[Scope and Launch Targets]]
- [[Design Principles and Fairness Charter]]
- [[Core Gameplay Loop]]
- [[Decision Register]]
