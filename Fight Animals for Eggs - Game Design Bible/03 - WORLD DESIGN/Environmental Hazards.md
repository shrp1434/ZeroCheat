---
title: Environmental Hazards
type: system
category: world-design
status: proposed
priority: P1
owner: World / Environment Director
last_updated: 2026-11-14
tags:
  - world
  - hazards
  - combat
  - accessibility
---

# Environmental Hazards

> [!info] PROPOSED
> The hazard system, catalogue and every value on this page are proposals. Hazard damage is expressed as a percentage of the victim's maximum HP so it scales with level and region without new tables. Values are local proposals pending addition to [[Canonical Proposed Values]].

## 1. Purpose

Hazards make each region **play** differently, not just look different. They create positioning decisions in fights, reward attention, and give boss arenas extra texture. They must never feel like unfair, invisible traps.

## 2. Global hazard rules

| # | Rule |
|---|---|
| H1 | **Ambient** hazards affect players and their companions only. Wild animals and bosses are immune and path around them. This prevents using hazards to farm wild animals. |
| H2 | Ambient hazard damage **cannot deliver a knock-out**: it stops at 1 HP. Knock-outs only come from attacks. This keeps hazards from triggering defeat penalties (**UNDECIDED**, [[Open Questions#Q-014]]). |
| H3 | **Boss-created** hazards (lava waves, ice spikes) are attacks, follow the boss telegraph standard, and *can* knock out ([[Boss Design Overview]]). |
| H4 | Every damaging hazard has a telegraph of at least **1.0 s** if it deals ≥ 5% max HP, or is a persistent, clearly marked zone. |
| H5 | Hazard damage gives no kill credit and no combat tag on its own (so it never blocks Return Home or team edits). |
| H6 | No hazards in [[Hub - Hatchling Haven]], on base plots, on Waystone clearings or on main paths' centre lines. |
| H7 | Falls below a region's kill plane return the player to the last safe point (recorded every 2 s while grounded on a safe surface) with 10% max HP damage, floored at 1 HP (H2). Companions teleport with the player. |
| H8 | In PvP, hazard damage is attributed to the environment, not to an opponent who knocked the player into it ([[PvP System]]). |
| H9 | Every hazard has an accessibility alternative for flashing or shaking effects (reduced-flash mode, [[UI Accessibility Standards]]). |
| H10 | Hazards are server-authoritative: the server applies damage and status; clients only render ([[Server-Client Responsibilities]]). |

## 3. Hazard catalogue

| ID | Hazard | Region | Type | Telegraph | Effect |
|---|---|---|---|---|---|
| HZ-01 | Bramble Thicket | [[Region - Whisperwood Forest]] | Zone | Visible thorny bushes | −30% move speed inside; 1% max HP/s after 3 s inside |
| HZ-02 | Fernmire Bog | Whisperwood Forest | Zone | Dark water, bubbles | −25% move speed; dodge roll distance halved |
| HZ-03 | Dust Devil | [[Region - Sunscorch Savanna]] | Moving | Visible whirlwind, 1.5 s wind-up sound | Knockback 12 studs; 4% max HP |
| HZ-04 | Sinksand | Sunscorch Savanna | Zone | Rippling sand texture | −40% move speed; cannot dodge roll |
| HZ-05 | Spore Bloom | [[Region - Emerald Canopy]] | Periodic zone | Flower swells 1.5 s before bursting | 1.5% max HP/s for 5 s inside the cloud |
| HZ-06 | Rotten Walkway | Emerald Canopy | Trigger | Creak + dust 1.5 s | Plank segment drops; player falls to the lower layer, no damage |
| HZ-07 | River Rapids | Emerald Canopy | Zone | White water, arrows in foam | Pushes 6 studs/s downstream |
| HZ-08 | Tide Surge | [[Region - Coral Coast]] | Periodic | Conch horn and foam line 5 s ahead; every 120 s | Waves sweep the tidal flats: 6% max HP, knockback 10 studs |
| HZ-09 | Urchin Bed | Coral Coast | Zone | Purple spiny clusters | 3% max HP on contact, at most once per second |
| HZ-10 | Blizzard | [[Region - Frostfang Tundra]] | Event | Wind rise 10 s ahead; 60 s duration every 6 min | −15% move speed and fog; standing within 15 studs of a Hearthstone brazier negates both |
| HZ-11 | Thin Ice | Frostfang Tundra | Trigger | Cracks appear, 2.5 s | Player drops into icy shallows: Chilled (−30% attack speed for 6 s) |
| HZ-12 | Gale Gust | [[Region - Skyreach Peaks]] | Periodic | Wind lines and blown leaves 1.5 s ahead | Push of 8 studs/s for 3 s in the gust direction |
| HZ-13 | Rockfall | Skyreach Peaks | Trigger | Ground shadow 1.2 s | 8% max HP and 0.5 s stagger |
| HZ-14 | Summit Lightning | Skyreach Peaks | Event (storms) | Crackling ring 1.5 s | 12% max HP |
| HZ-15 | Lava | [[Region - Emberheart Caldera]] | Zone | Bright flow, heat haze | 15% max HP per second and an outward bounce impulse; floored at 1 HP (H2) |
| HZ-16 | Geyser Vent | Emberheart Caldera | Periodic (20–40 s) | Steam hiss and glow 1.5 s | 10% max HP and launch upward 20 studs (no fall damage on landing) |
| HZ-17 | Ash Fog | Emberheart Caldera | Zone | Grey haze | Visibility only; companion auto-target range −25% |
| HZ-18 | Void Edge | [[Region - Starfall Sanctuary]] | Fall | Starfield below island edges | H7 fall return |
| HZ-19 | Meteor Shower | Starfall Sanctuary | Event | Targeting circles 2.0 s | 12% max HP per impact |
| HZ-20 | Gravity Well | Starfall Sanctuary | Zone (beneficial) | Floating motes | Jump height ×2; fall speed halved |

## 4. Hazard interaction with combat

- **Companions** obey the same hazard rules as players. Companion AI avoids persistent hazard zones when choosing positions ([[Animal Combat Behaviour]]), but will follow a manual target command into a hazard if commanded; the UI shows a warning tint on the commanded target if it stands in a hazard (**PROPOSED**).
- **Wild animals** never path into hazard zones, but can stand at the edge. Skilled players use this to fight from favourable terrain.
- **Status stacking:** hazard slows do not stack with each other; the strongest applies. Hazard slows stack multiplicatively with combat slows, with a floor of 40% of base move speed.

## 5. Telegraph and readability standard

| Damage band | Minimum telegraph | Visual | Audio |
|---|---|---|---|
| < 5% max HP or zone | Persistent zone | Distinct material and colour | Ambient loop |
| 5–10% | 1.0 s | Ground decal or particle wind-up | Wind-up cue |
| > 10% | 1.5 s | Bright decal + rim light | Strong cue ([[Audio Mixing and Priority]]) |

Hazard decals use the **environmental blue-white** telegraph colour so they are never confused with boss attack colours ([[Combat Feedback and Readability]]).

## 6. Implementation notes

- Hazard volumes are parts tagged `Hazard` with attributes `HazardId`, `Shape`, `Active`. The server checks player presence on a 0.2 s cadence using spatial queries against the hazard set of the player's current region only.
- Periodic hazards run from server-side timers and broadcast their state through a `RemoteEvent`; telegraph visuals start on the client upon receipt, so the effective telegraph on clients is the authored telegraph minus one-way latency. For this reason each telegraph has a **150 ms latency allowance** included in its authored time ([[Latency Handling]]).
- Cosmetic-only parts of hazards (particles, decals) are client-side.

## 7. Performance

| Budget | Target (PROPOSED) |
|---|---|
| Active hazard volumes per region | ≤ 40 |
| Periodic hazard timers per server | ≤ 60 |
| Hazard particle emitters visible at once | ≤ 12 on mobile |

## 8. Test hooks

- Stand in lava at 5% HP → HP floors at 1, no knock-out.
- Wild animal kited towards Bramble Thicket → it stops at the edge.
- Hazard telegraph measured on a 150 ms simulated latency client → at least 0.85 s visible before damage for a 1.0 s hazard.
- Reduced-flash mode on → Summit Lightning uses a non-flashing ring.

## Related documents
- [[World Design Index]]
- [[Combat Feedback and Readability]]
- [[Player Defeat and Penalties]]
- [[VFX - Environment Ambient Effects]]
- [[Sound - Ambient World]]
- [[UI Accessibility Standards]]
