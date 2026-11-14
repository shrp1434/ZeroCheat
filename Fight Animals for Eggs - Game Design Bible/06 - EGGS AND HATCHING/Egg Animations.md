---
title: Egg Animations
type: system
category: eggs
status: proposed
priority: P1
owner: Systems Designer
last_updated: 2026-11-14
tags:
  - eggs
  - animation
  - vfx
  - presentation
---

# Egg Animations

This page is the **design contract** between the egg systems and the animation, VFX and audio teams: what each egg moment must communicate, how long it may take, and which rules keep it honest. Keyframe-level specifications live in [[Animation - Egg Roll]], [[Animation - Egg Hatch]] and [[Animation - Egg Merge]]; effects in [[VFX - Rarity and Variant Effects]]; audio in [[Sound - Eggs]].

> [!info] PROPOSED
> All timings and beats on this page are **PROPOSED**. The canonical hatch timings (3.5 s single, 5.0 s multi, skippable after first viewing) and the 2.5–6 s merge range come from [[Canonical Proposed Values]] §7 and §10. Timed incubation remains an alternative (**UNDECIDED**, [[Open Questions#Q-023]]).

## 1. Principles

1. **Result first, animation second.** The server has committed the outcome before any animation starts. A disconnect, skip or frame drop cannot change it.
2. **Escalate honestly.** The reveal may build anticipation, but it must never show a higher rarity cue than the true outcome. No fake-outs, no "almost Secret" glows that collapse into a Common (near-miss design is prohibited, see [[Randomised Reward Compliance]]).
3. **Rarity is revealed by one consistent cue.** The egg's colour key appears at a fixed beat in every animation, so players learn to read it.
4. **Skippable after first viewing.** The first time a player sees a given rarity's hatch or merge, it plays in full; afterwards a tap skips to the result card. Secret always offers the full version by default but remains skippable.
5. **Throughput matters.** At endgame roll rates (≈ 335 rolls per hour) animation time must stay a small fraction of play time; see [[Egg System Overview]].
6. **Respect accessibility.** A "reduced motion" setting replaces camera shakes and full-screen flashes with fades ([[UI Accessibility Standards]], [[UI - Settings]]).

## 2. Roll animation (shrine)

| Beat | Time | Content |
|---|---|---|
| Wind-up | 0.0–0.6 s | Shrine glyphs light; neutral white egg rises from the shrine bowl |
| Spin | 0.6–1.4 s | Egg spins; neutral shimmer; no rarity colour yet |
| Reveal | 1.4 s | Egg snaps to its rarity colour and model ([[Common Egg]] … [[Secret Egg]]); rarity sound sting |
| Settle | 1.4–2.0 s (Common–Rare), up to 3.0 s (Mythical, Secret) | Rarity-specific flourish; card shows rarity name and destination |

Bulk ×5: five eggs rise together, spin, and reveal simultaneously; total 2.5 s, with a 0.5 s hold if any is Legendary or above.

## 3. Hatch animation

| Beat | Single egg (3.5 s) | Multi-hatch (5.0 s, 2–5 eggs) |
|---|---|---|
| Wobble | 0.0–1.0 s, amplitude rising by rarity | 0.0–1.2 s, all eggs together |
| Cracks | 1.0–2.0 s, rarity-coloured light leaks from cracks | 1.2–3.2 s, eggs crack in ascending rarity order |
| Burst | 2.0–2.5 s, shell bursts, rarity VFX | Each egg bursts in turn; highest rarity last |
| Reveal | 2.5–3.5 s, animal pose, name, "NEW" or "Duplicate x of y" | 3.2–5.0 s, row of five result cards |

The "NEW" tag is computed after the draw and is presentation only (D-018). The crack-light colour equals the egg's own rarity colour, which the player already knows; the hatch never teases a different rarity.

## 4. Merge animation

| Merge | Duration | Station level | Beats |
|---|---:|---:|---|
| Common → Uncommon | 2.5 s | 1 | Three grey eggs drop into the nest; lever presses; a green egg pops up |
| Uncommon → Rare | 3.0 s | 1 | Same press, with leaf burst and blue reveal |
| Rare → Epic | 3.5 s | 2 | Eggs roll into the forge basin; bellows pump; violet egg emerges from the coals |
| Epic → Legendary | 4.5 s | 3 | Eggs float into the glass dome; pylons pulse; dome fills with light; gold egg descends |
| Legendary → Mythical | 5.0 s | 4 | Eggs rise into the crucible; rings spin up; aurora flares; rose egg rises |
| Mythical → Secret | 6.0 s | 5 | Eggs orbit the altar; platforms lock; sky beam pulses; prismatic egg descends from the beam |

Detail: [[Animation - Egg Merge]]. Station construction sequences: [[Animation - Base Upgrades]].

## 5. Per-rarity escalation summary

| Rarity | Idle in storage | Roll settle | Hatch burst | Camera | Audio layer ([[Sound - Eggs]]) |
|---|---|---|---|---|---|
| Common | Still | Small dust puff | Shell pieces, dust | None | Wooden knock |
| Uncommon | Sprout sways | Leaf flurry | Leaves | None | Knock + leaf rustle |
| Rare | Gentle bob | Bubble sparkle | Water ring | Slight push-in | Glass chime |
| Epic | Bob + crystal glint | Violet spark ring | Crystal shatter | Push-in | Chime + crystal ring |
| Legendary | Halo rotates | Golden rays | Sunburst | Push-in + small shake | Brass swell |
| Mythical | Fragments orbit | Rune flare | Petal and ember storm | Push-in, orbit 30° | Choir pad |
| Secret | Shell segments float apart and back | Prismatic flash, screen vignette | Starfield burst | Full orbit 90° | Choir + sub drone + silence beat |

## 6. Technical notes

- Animations run on the client from a server `RollResult` / `HatchResult` / `MergeResult` payload ([[Remote Communication Contract]]).
- Models and effects for all seven eggs are preloaded on entering the shrine or station area with `ContentProvider:PreloadAsync`, so the reveal never stalls on asset loading.
- Particle budgets per rarity follow [[VFX Bible]] and [[Performance Guidelines]]; mobile caps halve emitter rates (PROPOSED).
- Other players see a reduced version (no camera work, 50 % particles) of rolls and hatches near them; Secret reveals trigger a server-wide toast only if the player has not opted out (PROPOSED).

## Related documents
- [[Animation - Egg Roll]] · [[Animation - Egg Hatch]] · [[Animation - Egg Merge]] · [[Animation - Base Upgrades]]
- [[VFX - Rarity and Variant Effects]] · [[Sound - Eggs]] · [[Egg Art Direction]]
- [[Egg Roll System]] · [[Hatch System]] · [[Egg Merging]] · [[Egg Merging Station]]
- [[UI - Egg Rolling]] · [[UI - Egg Hatching]] · [[UI - Egg Merging]]
