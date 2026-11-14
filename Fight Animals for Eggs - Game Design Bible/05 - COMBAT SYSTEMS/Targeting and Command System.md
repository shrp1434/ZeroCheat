---
title: Targeting and Command System
type: system
category: combat
status: mixed
priority: P0
owner: Gameplay Systems Architect
last_updated: 2026-11-14
tags:
  - combat
  - targeting
  - ai
  - controls
  - input
---

# Targeting and Command System

How companions choose what to attack, how the player overrides them, and how every combat action maps to PC, mobile and gamepad.

> [!success] CONFIRMED
> Animals auto-target nearby enemies. Players can issue manual target commands (D-009).

> [!info] PROPOSED
> The scoring algorithm, command set and input maps below are proposals. New local values are marked *(new)* and are listed for [[Canonical Proposed Values]].

## Targeting concepts

| Term | Meaning |
|---|---|
| **Soft target** | The enemy the player's attacks will hit next: the nearest enemy inside a 60° cone in front of the camera within 40 studs *(new)*. Highlighted with a thin ring. |
| **Focus target** | An enemy the player has explicitly selected (tap, click or lock-on) or hit within the last 3 s *(new)*. Highlighted with a bold ring and shown on the HUD. |
| **Command target** | An enemy that a Focus command has assigned to one or all companions. Overrides auto-targeting for 8 s *(new)* or until the target is defeated, leashes or becomes invalid. |
| **Candidate** | Any enemy that passes the eligibility filter below. |

## Auto-target scoring

Each companion re-evaluates its target **4 times per second** *(new)* on the server.

### Step 1: eligibility filter
A candidate must be:
1. Hostile to the player (wild animal in combat or aggressive, boss in combat, raid defender or attacker, or valid PvP opponent).
2. Alive and targetable (not in a reset, not in a spawn-protection window).
3. Within **30 studs of the player** *(new)*. Companions never acquire targets relative to their own position ([[Animal Combat Behaviour]]).
4. Reachable: a path exists, or the companion is Ranged/Support/Controller with line of sight.
5. Not a neutral or skittish wild animal that has not yet entered combat, unless commanded.

### Step 2: score

```
Score = Command + Focus + Protect + Proximity + Finish + RolePreference + Stickiness − Penalties
```

| Term | Value *(new)* | Notes |
|---|---:|---|
| `Command` | +1000 | Candidate is this companion's command target. Effectively a hard override. |
| `Focus` | +60 | Candidate is the player's focus target. |
| `Protect` | +40 if attacking the player; +30 if attacking another companion | Tanks multiply Protect by 1.5. |
| `Proximity` | +25 × (1 − d / 30) | `d` = distance from the companion, clamped to 0–30. |
| `Finish` | +20 × (1 − HP / MaxHP) | Encourages finishing wounded enemies. |
| `RolePreference` | +15 | Assassin: enemy is Ranged or Support. Controller: enemy is winding up a telegraphed attack. Tank: enemy is attacking an ally. Support: never applies (Supports prioritise healing). |
| `Stickiness` | +20 | Candidate is the current target. |
| `Penalties` | −15 if Controller and target already stunned; −1000 if unreachable for more than 4 s | |

### Step 3: switch rule
Switch only if `bestScore > currentScore + 15` *(new)* (hysteresis), or if the current target becomes ineligible. This prevents target flicker. A command always switches immediately.

### Worked example
The player (focus on a wild Boar at 12 studs) is attacked by a wild Frog. A Tank companion is 6 studs from the Frog and 10 from the Boar.

| Candidate | Focus | Protect | Proximity | Finish (Boar at 40% HP, Frog full) | Role | Stickiness (current = Boar) | Total |
|---|---:|---:|---:|---:|---:|---:|---:|
| Boar | 60 | 0 | 25 × (1 − 10/30) = 16.7 | 12 | 0 | 20 | **108.7** |
| Frog | 0 | 40 × 1.5 = 60 | 25 × (1 − 6/30) = 20 | 0 | 15 | 0 | **95.0** |

The Tank stays on the Boar (95 is not more than 108.7 + 15). A Bruiser in the same spot would score Frog 40 + 20 = 60, also staying. If the player issues a Focus command on the Frog, the Tank switches at once.

### Illustrative Luau

```lua
-- Illustrative Luau, not tested in Roblox Studio.
local W = { Command = 1000, Focus = 60, ProtectPlayer = 40, ProtectAlly = 30,
	Proximity = 25, Finish = 20, Role = 15, Sticky = 20, Hysteresis = 15 }

local function scoreCandidate(companion, enemy, ctx): number
	local s = 0
	if ctx.commandTarget == enemy then s += W.Command end
	if ctx.playerFocus == enemy then s += W.Focus end
	local protectMul = companion.role == "Tank" and 1.5 or 1
	if enemy.currentTarget == ctx.player then
		s += W.ProtectPlayer * protectMul
	elseif ctx.isTeammate(enemy.currentTarget) then
		s += W.ProtectAlly * protectMul
	end
	local d = math.clamp((enemy.position - companion.position).Magnitude, 0, 30)
	s += W.Proximity * (1 - d / 30)
	s += W.Finish * (1 - enemy.hp / enemy.maxHp)
	if ctx.rolePrefers(companion, enemy) then s += W.Role end
	if companion.target == enemy then s += W.Sticky end
	return s - ctx.penalties(companion, enemy)
end
```

## Command set

| Command | Effect *(new)* | Duration |
|---|---|---|
| **Focus Attack (team)** | All three companions attack the selected enemy. | 8 s or until the target is invalid |
| **Send (individual)** | One chosen companion attacks the selected enemy; the other two keep auto-targeting. | 8 s or until invalid |
| **Regroup** | All companions disengage, return to formation and ignore auto-targeting for 3 s. Threat on enemy tables is kept. | 3 s |
| **Manual ability** | Fires a companion's manual ability at the focus target or a ground point. See [[Abilities and Cooldowns]]. | Ability-specific |

Rules:
- Commands are **requests** sent by `RemoteEvent` and validated on the server (target exists, is eligible, is within 40 studs of the player). Rate limit: 4 commands per second per player *(new)* ([[Implementation - Rate Limiting]]).
- A command on a target that is out of range is rejected with a short "Too far" prompt, not silently ignored.
- In PvP and raids, commands obey the same rules; there is no remote "attack anything anywhere".

## Input mapping

All bindings are **PROPOSED** and remappable on PC and gamepad in [[UI - Settings]]. Bind with `ContextActionService` so the same action names work on every device. Interaction with Roblox's default core bindings (for example the gamepad A button for jump and the default touch thumbstick) is *unverified* and must be checked in Studio.

### PC (keyboard and mouse)

| Action | Binding |
|---|---|
| Basic attack | Left mouse |
| Set focus target | Click an enemy with middle mouse, or press Tab to cycle the nearest enemies |
| Power Strike / Ground Slam / Rally Cry | E / R / F |
| Dodge roll | Q |
| Companion manual abilities (slots 1–3) | 1 / 2 / 3 |
| Focus Attack (team) | T (on focus target, or soft target if none) |
| Send individual companion | Ctrl + 1 / 2 / 3 |
| Regroup | G |

### Mobile (touch)

| Action | Control |
|---|---|
| Move | Roblox dynamic thumbstick (left side) |
| Basic attack | Large attack button, bottom right |
| Specials | Three smaller buttons in an arc around the attack button, each with a radial cooldown sweep |
| Dodge | Button left of the arc |
| Set focus target | Tap an enemy (generous 48 px touch radius *(new)*) |
| Companion manual abilities | Tap a companion portrait on the team bar |
| Send individual companion | Long-press (0.4 s) a portrait, then tap an enemy |
| Focus Attack (team) | Crosshair button beside the portraits |
| Regroup | Whistle button beside the portraits |

Mobile layout, button sizes and safe areas are owned by [[UI - Main HUD]] and [[UI - Animal Team Display]]; accessibility minimums by [[UI Accessibility Standards]].

### Gamepad

| Action | Binding (Xbox / PlayStation) |
|---|---|
| Basic attack | RT / R2 |
| Power Strike / Ground Slam | X / Square, Y / Triangle |
| Rally Cry | RB / R1 |
| Dodge roll | B / Circle |
| Lock-on and cycle focus target | Right stick click (R3), flick right stick to cycle |
| Companion manual abilities | Hold LB / L1 + X, Y, B for slots 1, 2, 3 (labels change while LB is held) |
| Focus Attack (team) | D-pad up |
| Regroup | D-pad down |
| Send individual companion | Hold LB / L1 + D-pad left, up, right for slots 1, 2, 3 |

## Manual-ability UX summary
The team bar ([[UI - Animal Team Display]]) is the single place where manual abilities live:
- Each of the three portraits shows HP, a manual-ability icon with a radial cooldown, and a ready glow.
- Automatic abilities show a small pip that flashes when they fire, so the player learns what the AI is doing.
- A KO companion's portrait greys out with a recovery timer ([[Animal Combat Behaviour#Knock-out and recovery]]).
- Targeted manual abilities fire at the focus target; ground-targeted ones fire at the soft-target position on mobile and gamepad, and at the cursor on PC.
Full rules are in [[Abilities and Cooldowns]].

## Edge cases

| Case | Rule (PROPOSED) |
|---|---|
| Focus target leashes back to its spawn | Focus clears; companions resume auto-targeting. |
| Commanded target enters a safe zone (other player's PvP-off state, hub) | Command cancelled. |
| Player commands an attack on another player's mini-boss | Allowed; bosses are shared ([[Multiplayer Combat Rules]]). |
| Two enemies tie exactly | Lower entity ID wins (deterministic for tests). |

## Test hooks
- Deterministic scoring: given fixed positions and HP, the chosen target matches the worked example.
- Hysteresis: a challenger scoring current + 14 does not cause a switch; current + 16 does.
- A forged command for a target 200 studs away is rejected and logged ([[Test Cases - Exploit Prevention]]).

## Related documents
- [[Animal Combat Behaviour]]
- [[Abilities and Cooldowns]]
- [[Player Combat]]
- [[UI - Animal Team Display]]
- [[UI - Main HUD]]
- [[Client Controllers]]
- [[Remote Communication Contract]]
- [[Test Cases - Animal AI]]
