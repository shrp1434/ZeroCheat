---
title: Combat Feedback and Readability
type: spec
category: combat
status: proposed
priority: P1
owner: Combat Designer
last_updated: 2026-11-14
tags:
  - combat
  - feedback
  - readability
  - accessibility
  - ui
---

# Combat Feedback and Readability

Rules that make fights legible on a phone in a busy shared world: hit feedback, damage numbers, health bars, target markers, telegraphs and accessibility options. Art, VFX and audio documents implement these rules; this page states what must be communicated and with what priority.

> [!info] PROPOSED
> Everything on this page is a proposal. Rarity colours come from [[Canonical Proposed Values]] §1 and [[Rarity Visual Language]]. Timings and limits are new values.

## Readability priorities

When effects compete for attention, higher priority wins (lower-priority effects are dimmed or culled):

| Priority | Information | Why |
|---:|---|---|
| 1 | Telegraphs that threaten the local player or their companions | Avoidable damage must always be visible |
| 2 | Local player's HP, specials and dodge cooldown | Moment-to-moment decisions |
| 3 | Own companions' HP, KO and manual-ability readiness | Team management |
| 4 | Focus and command target markers | Intent confirmation |
| 5 | Damage numbers and hit effects from the local player's team | Reward and feedback |
| 6 | Other players' hit effects | Ambience in a shared world |

## Hit feedback layers

| Layer | Local player and own team | Other players |
|---|---|---|
| Hit animation and reaction | Always ([[Animation - Animal Attacks and Hit Reactions]]) | Always |
| Impact VFX | Full ([[VFX - Combat Effects]]) | Reduced (one particle burst, no trails) |
| Impact sound | Full ([[Sound - Combat Impacts]]) | Attenuated by distance; capped voices ([[Audio Mixing and Priority]]) |
| Damage numbers | Shown | Hidden by default |
| Target flash | `Highlight` flash on the target for 0.1 s on finisher and specials only | None |
| Hit-stop | 50 ms on Power Strike and combo hit 3 only, local player only | None |
| Camera shake | Ground Slam and heavy boss attacks only; amplitude limited; toggle in settings ([[Camera Behaviour Guidelines]]) | None |

## Damage numbers

| Rule | Value |
|---|---|
| Aggregation | Hits on the same target from the same source within 0.25 s merge into one number |
| Size | Scales with damage as a share of the target's max HP: small under 5%, medium 5–15%, large above 15% |
| Colours | Player hits white; companion hits tinted with the companion's rarity colour; damage taken by the local player red; heals green; absorbed damage grey with a shield glyph |
| Lifetime | 0.8 s float and fade |
| Cap | At most 12 numbers on screen; oldest fade first |
| Off switch | Settings toggle ([[UI - Settings]]) |

No critical hits exist at launch, so no "crit" styling is needed.

## Health bars and status

| Element | Rule |
|---|---|
| Wild animal bar | Hidden until the animal is damaged, targeted or aggroed; frame colour = rarity colour; name and rarity shown on focus |
| Companion bars | On the team bar ([[UI - Animal Team Display]]) and as a slim bar above each companion |
| Player bar | HUD ([[UI - Main HUD]]); red screen-edge vignette below 30% HP |
| Boss bar | Top of screen with phase markers at threshold HPs ([[UI - Boss Health Bar]]) |
| Status icons | Stun, slow, taunt, shield, damage over time: icon row above the bar; every icon also has a distinct shape |
| Knocked out | Companion collapse animation, spirit marker, greyed portrait with recovery timer ([[Animation - Animal Defeat and Victory]]) |

## Target and intent markers

| Marker | Look |
|---|---|
| Soft target | Thin ground ring under the enemy |
| Focus target | Bold animated ring plus a HUD chip with the enemy's portrait |
| Command target | Paw-print marker above the enemy for the command's 8 s duration, with lines from each commanded companion for 1 s |
| Enemy targeting you | Small red chevron above the enemy pointing towards the local player |
| Alert | Exclamation mark during the wild animal's 0.75 s `Alert` state ([[Wild Animal AI]]) |
| In combat | Crossed-swords icon on the HUD while the combat tag is active |

## Telegraph standard

All telegraph rules for timing are in [[Boss AI#Telegraph rules]]. The visual standard:

| Element | Rule |
|---|---|
| Shape | Ground decal in the exact hit shape: circle, cone, line, donut, or a ring on a marked player |
| Fill | Fills from the edge to the centre over the wind-up, so the fill completing means the hit lands |
| Colour | One reserved warning colour for every enemy telegraph; never used for anything else. Heavy attacks add a pulsing outline |
| Colour-blind mode | Adds a hatched pattern and a thicker outline; colour is never the only cue ([[UI Accessibility Standards]]) |
| Audio | Every heavy attack has a wind-up sound cue |
| Own abilities | Player and companion ground-targeted abilities preview in a neutral colour distinct from the warning colour |

## Defeat summary
On player defeat, the 5 s respawn screen shows the last three damage sources (portrait, name, damage), and a one-line tip when a telegraphed attack caused the defeat ([[Player Defeat and Penalties]]).

## Performance limits for feedback
- Combat VFX per hit: at most one `ParticleEmitter` burst plus an optional `Trail` on the local team; other players' hits use the burst only.
- Mobile quality tier halves particle rates and disables hit-stop and screen shake by default.
- Targets: 60 FPS on mid-range PC, 30 FPS minimum on mid-range mobile (canonical §15; [[Performance Guidelines]]).

## Accessibility settings
Reduce camera shake, reduce flashing (disables `Highlight` flashes and the low-HP pulse), damage numbers on or off, colour-blind telegraph mode, larger status icons, and audio cues for telegraphs. Full requirements in [[UI Accessibility Standards]].

## Test hooks
- With colour removed from a screenshot (greyscale), QA can still identify every telegraph and every status effect.
- In a 16-player world boss fight on a mid-range phone, the local player's telegraphs remain visible and the frame rate stays at or above 30 FPS ([[Test Cases - Mobile Performance]]).
- QA can name the source of every defeat from the defeat summary.

## Related documents
- [[VFX - Combat Effects]]
- [[Sound - Combat Impacts]]
- [[Animation - Animal Attacks and Hit Reactions]]
- [[UI - Main HUD]]
- [[UI - Animal Team Display]]
- [[UI - Boss Health Bar]]
- [[UI Accessibility Standards]]
- [[Rarity Visual Language]]
- [[Camera Behaviour Guidelines]]
