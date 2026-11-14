---
title: VFX Bible
type: guide
category: vfx
status: proposed
priority: P0
owner: VFX Artist
last_updated: 2026-11-14
tags:
  - vfx
  - style-guide
  - performance
  - particles
  - mobile
---

# VFX Bible

Style, colour language, budgets, quality tiers, implementation rules and ID allocation for every visual effect, plus the register of system effects (eggs, merging, ascension, base, shield, raid). Topic registers: [[VFX - Combat Effects]], [[VFX - Rarity and Variant Effects]], [[VFX - Environment Ambient Effects]].

> [!info] PROPOSED
> Everything here is **PROPOSED** by the VFX Artist. Rarity colour keys come from [[Canonical Proposed Values]] §1; the frame-rate targets (60 FPS mid-range PC, 30 FPS minimum mid-range phone) from §15.

---

## 1. Style

| Rule | Detail |
|---|---|
| Shape language | Chunky, faceted, low-poly shapes that match the models ([[Art Bible]]): triangular sparks, hexagonal shield panels, stylised leaves, star bursts, rounded puffs. No photographic smoke, fire or blood textures |
| Motion | Fast burst, slow fade (mirrors the animation "fast-in, slow-out" rule in [[Animation Bible]]) |
| Values | Bright cores with darker rims, so effects read on both bright grass and dark caves |
| Friendly danger | Danger is shown with warm orange-red telegraphs and dizzy stars, never with gore, skulls or horror imagery (D-026) |
| Elements | Water, frost, leaf, spark, wind, ember-spark, bubble, petal, starlight. Fire only as stylised ember sparks and warm glows; no burning creatures |
| Texture size | Particle textures ≤ 256 × 256; flipbooks ≤ 512 × 512 using `ParticleEmitter.FlipbookLayout` (2×2 or 4×4) |
| Screen coverage | No single particle may cover more than 25% of a phone screen at gameplay zoom (overdraw) |

---

## 2. Colour language

| Meaning | Colour (PROPOSED unless from canonical) | Never used for |
|---|---|---|
| Rarity tiers | Common `#9AA5B1`, Uncommon `#4CC26A`, Rare `#3D8BFF`, Epic `#A55BFF`, Legendary `#FFB020`, Mythical `#FF4D8D`, Secret `#1B1B2F` with prismatic shimmer (canonical §1) | Combat danger cues |
| Enemy danger (telegraphs) | `#FF5A36` | Any friendly effect |
| Safe zone | `#7FD3FF` | Danger |
| Heal | Mint `#7DF2B0` (distinct from Uncommon green by lightness and the cross-shaped motes) | Damage |
| Buff | Warm gold `#FFD86B` with upward motes | Debuffs |
| Debuff / slow | Desaturated lilac `#B9A7D9` with downward drips | Buffs |
| Stun | Yellow stars `#FFE45C` | — |
| Player command | The local player's team colour (white by default) | Other players |
| Raider | Amber `#FF8A3D` | Defender cues |
| Defender | Red `#FF4D4D` | Raider cues |
| Shield | Cyan `#5CE1FF` | Danger |

Colour is never the only carrier of meaning: every tier and every gameplay cue also differs in **shape** (rarity: dot, leaf, ray, orbit, pillar, petal, prism) and **sound** ([[UI Accessibility Standards]], [[Rarity Visual Language]]).

---

## 3. Quality tiers

| Tier | Default for | Auto rule |
|---|---|---|
| Low | Phones and tablets whose average frame time over 10 s exceeds 36 ms on Medium | Drop a tier after 10 s above 36 ms |
| Medium | Phones and tablets (start tier when touch is the primary input) | Raise a tier after 60 s below 20 ms (never above the player's chosen tier) |
| High | PC and console (start tier) | — |

The player can lock a tier in [[UI - Settings]]. Animation LOD shares the same tier ([[Animation Bible]] §8). Reading Roblox's own graphics quality setting from a script is *unverified* and is not relied on.

### 3.1 Budgets per client

| Budget | Low | Medium | High |
|---|---:|---:|---:|
| Continuous emitter `Rate` cap (per emitter, particles/s) | **20** | **40** | **80** |
| Burst cap per `ParticleEmitter:Emit` call | 12 | 24 | 48 |
| Enabled continuous emitters | 25 | 50 | 90 |
| Estimated live particles | 600 | 1,500 | 3,000 |
| Active `Beam`s | 8 | 16 | 32 |
| Active `Trail`s | 6 | 14 | 24 |
| Active `Highlight`s | 4 | 8 | 12 |
| Dynamic `PointLight` / `SpotLight` from VFX | 4 | 8 | 16 |
| VFX light shadows | Off | Off | Off |
| Beam `Segments` | 8 | 12 | 16 |

Notes:
- Roblox limits how many Highlights render at once (reported as 31 in documentation we have not verified, *unverified*). Our High budget of 12 stays well below any such limit.
- Highlight reserve: 1 slot is always kept for the local damage flash; during a raid, up to 6 slots go to stealable outlines ([[Animation - Animal Defeat and Victory]]).
- An authored `Rate` above the cap is clamped by the VFX controller at runtime; authors must design effects that still read at the Low cap.

### 3.2 Priority classes

| Class | What | Over budget |
|---|---|---|
| P0 Critical | Boss and wild telegraphs, raid markers and prompts, steal progress rings, stealable outlines, target command ring, KO stars | Never culled; exempt from caps except Highlights (reserve) |
| P1 Own | Effects from the local player, their companions and their own presentations (reveals, merges) | Culled last |
| P2 Others' combat | Other players' and wild animals' attacks and abilities | Rate halved, then culled beyond 80 studs |
| P3 Ambient | Region ambience, idle loops, decorative motes | Culled first, and always beyond 120 studs |

---

## 4. Implementation rules

1. **One client VFX controller** owns all cosmetic effects ([[Client Controllers]]): `Vfx.play(id, attachment, params)`, `Vfx.burst(id, attachment, count)`, `Vfx.stop(handle)`. It enforces tier caps, priority culling and pooling.
2. **Templates live in `ReplicatedStorage/VFX/<VFX-###>`** and are cloned from a pool, never created ad hoc.
3. **Bursts use `ParticleEmitter:Emit(n)`** on pooled, disabled emitters. Continuous effects toggle `Enabled`.
4. **Spawn on rig attachments** listed in [[Animal Rig Standards]] §6.
5. **Gameplay never depends on VFX.** Effects are cosmetic and client-side; server-relevant shapes (telegraph areas) come from configuration and are drawn by the client from replicated data.
6. **Sorting:** `ZOffset` for layering bursts over trails; `LightEmission` 0.3–1 for glows, 0 for dust and debris.
7. **Lifetime hygiene:** every effect has a maximum lifetime; the controller returns it to the pool even if the owner is destroyed.
8. **Streaming:** effects attached to parts that stream out are released at once ([[Replication Strategy]]).

Illustrative Luau (not tested in Studio):

```lua
local TierCaps = { Low = 20, Medium = 40, High = 80 }

function Vfx.play(id: string, attachment: Attachment, params)
	local template = Pool.take(id)
	if not template then return nil end
	for _, emitter in template:GetDescendants() do
		if emitter:IsA("ParticleEmitter") then
			emitter.Rate = math.min(emitter:GetAttribute("AuthoredRate") or emitter.Rate, TierCaps[Quality.tier])
		end
	end
	template.Parent = attachment
	return Handle.new(id, template, params)
end
```

---

## 5. Photosensitivity

| Rule | Limit |
|---|---|
| Flash frequency | No more than **3** flashes in any 1 s window, for any effect or combination of effects owned by the controller |
| Full-screen flash brightness | Peak ≤ 80% white; ramp in over ≥ 2 frames |
| Saturated red flashes | Not permitted as full-screen effects |
| Strobing loops | Not permitted; shield expiry flicker is local, low contrast and replaced by a steady colour change with reduce motion ([[Animation - Shield Activation]]) |

---

## 6. ID allocation

| Range | Document |
|---|---|
| VFX-001 – VFX-099 | [[VFX - Combat Effects]] |
| VFX-100 – VFX-199 | [[VFX - Rarity and Variant Effects]] |
| VFX-200 – VFX-299 | [[VFX - Environment Ambient Effects]] |
| VFX-300 – VFX-399 | This document, §7 (system effects) |
| VFX-400 – VFX-499 | Reserved for live content ([[Content Expansion Guidelines]]) |

The master list is the [[Asset Register]]; new effects use [[Template - VFX]].

---

## 7. System effects register

| ID | Effect | Components | Priority class | Used in | Status |
|---|---|---|---|---|---|
| VFX-300 | Egg shrine idle | Neon rune ring, 1 emitter of rising motes (rate 6) | P3 | [[Animation - Egg Roll]] | **PROPOSED** |
| VFX-301 | Egg descent beam | 1 Beam, soft cream | P1 | Egg roll | **PROPOSED** |
| VFX-302 | Egg crack light leaks | Emissive crack decal + 1 emitter of short rays; tinted per rarity in hatches, neutral white in roll builds | P1 | Roll, hatch | **PROPOSED** |
| VFX-303 | Hatch shell burst | Burst of 6–16 shell fragments (tier-capped), dust puff | P1 | [[Animation - Egg Hatch]] | **PROPOSED** |
| VFX-304 | Multi-hatch slot pads | Neon pads under each slot, pulsing in egg colour | P1 | Multi-hatch | **PROPOSED** |
| VFX-310 | Ascension orb stream | Paw-print orb part + 1 Beam per orb | P1 | [[Animation - Ascension]] | **PROPOSED** |
| VFX-311 | Ascension star ignite | Star UI flare + 12-particle burst | P1 | Ascension | **PROPOSED** |
| VFX-312 | Ascension completion burst | Ring + rays; size scales A1 → A5 | P1 | Ascension | **PROPOSED** |
| VFX-320 | Merge station idle L1 (leaf swirl) | 1 emitter, rate 4 | P3 | [[Animation - Egg Merge]] | **PROPOSED** |
| VFX-321 | Merge station idle L2 (rune glow, sparks) | 1 emitter, rate 3; Neon runes | P3 | Merge | **PROPOSED** |
| VFX-322 | Merge station idle L3 (crystal shimmer) | 1 emitter, rate 6 | P3 | Merge | **PROPOSED** |
| VFX-323 | Merge station idle L4 (aurora ribbons) | 2 Beams | P3 | Merge | **PROPOSED** |
| VFX-324 | Merge station idle L5 (starfield) | 1 emitter, rate 8; constellation Beams | P3 | Merge | **PROPOSED** |
| VFX-325 | Station upgrade transformation flash | Burst + light pulse 0.3 s | P1 | Merge | **PROPOSED** |
| VFX-326 | Merge egg orbit trails | 3 Trails | P1 | Merge | **PROPOSED** |
| VFX-327 | Merge fusion flash | Burst + ring, tinted to the output rarity | P1 | Merge | **PROPOSED** |
| VFX-328 | Merge output emerge | Sparkle column in output rarity | P1 | Merge | **PROPOSED** |
| VFX-330 | Construction ring, dust and scaffold sparkle | Ground ring decal, dust bursts, sparkle emitter | P1 | [[Animation - Base Upgrades]] | **PROPOSED** |
| VFX-331 | Upgrade complete burst | Ring + 24-particle burst, light pulse | P1 | Base upgrades | **PROPOSED** |
| VFX-332 | Module level trim glow | `Neon` material swap on trim parts (no particles) | P3 | Base upgrades | **PROPOSED** |
| VFX-333 | Turret muzzle puff | 6-particle burst | P2 | Base defence | **PROPOSED** |
| VFX-334 | Trap trigger (sticky puddle or net pop) | Decal + 10-particle burst | P0 | Base defence | **PROPOSED** |
| VFX-335 | Barricade dust | 8-particle burst | P2 | Base defence | **PROPOSED** |
| VFX-340 | Shield raise (generator beam, ring flashes) | 1 Beam, ring mesh flashes | P1 | [[Animation - Shield Activation]] | **PROPOSED** |
| VFX-341 | Shield idle | `ForceField` sphere (plain sphere on Low), scan band | P3 | Shield | **PROPOSED** |
| VFX-342 | Shield impact ripple | Hex decal expanding 0.5 s | P2 | Shield | **PROPOSED** |
| VFX-343 | Shield expiry flakes | Burst 20/40/80 by tier | P1 | Shield | **PROPOSED** |
| VFX-344 | Shield break shatter | Burst 20/40/80 by tier + crack decal | P1 | Shield | **PROPOSED** |
| VFX-350 | Raid alarm siren light | 1 SpotLight + 1 Beam cone, rotating | P0 | [[Animation - Raid Interactions]] | **PROPOSED** |
| VFX-351 | Raid boundary wall | Transparent shimmer wall segments | P0 | Raid | **PROPOSED** |
| VFX-352 | Steal progress ring | SurfaceGui ring on a flat part, filled by replicated progress | P0 | Raid | **PROPOSED** |
| VFX-353 | Capture orb | Transparent sphere, amber rim, inner sparkle (rate 6) | P0 | Raid | **PROPOSED** |
| VFX-354 | Secure burst | Amber sparkles 16 | P1 | Raid | **PROPOSED** |
| VFX-355 | Drop and return poofs | 8-particle puffs | P1 | Raid | **PROPOSED** |
| VFX-356 | Raid end banner burst | Screen-space confetti or relief sparkles | P1 | Raid | **PROPOSED** |
| VFX-357 | Stealable outline and overhead marker | `Highlight` (outline only) from the raid reserve + billboard icon | P0 | [[Animation - Animal Defeat and Victory]] | **PROPOSED** |

---

## 8. Review checklist

1. Reads at Low tier on a phone at gameplay zoom.
2. Within the per-emitter cap and the effect's priority class.
3. Colour and shape follow §2; no danger hue on friendly effects.
4. Passes the photosensitivity rules (§5).
5. Pooled and returned; no leaked instances after 10 minutes of combat ([[Test Cases - Mobile Performance]]).

---

## Related documents
- [[Animation and VFX Index]]
- [[VFX - Combat Effects]]
- [[VFX - Rarity and Variant Effects]]
- [[VFX - Environment Ambient Effects]]
- [[Animation Bible]]
- [[Art Bible]]
- [[Colour Palette]]
- [[Rarity Visual Language]]
- [[Performance Guidelines]]
- [[Template - VFX]]
