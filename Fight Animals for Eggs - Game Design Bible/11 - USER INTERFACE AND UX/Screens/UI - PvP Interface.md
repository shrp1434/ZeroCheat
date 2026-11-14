---
title: UI - PvP Interface
type: ui-screen
category: ui
status: mixed
priority: P1
owner: Senior UI/UX Designer
last_updated: 2026-11-14
tags:
  - ui
  - pvp
  - combat
  - opt-in
---

# UI - PvP Interface

> [!success] CONFIRMED
> PvP is optional; players choose whether to take part (D-023).

> [!warning] UNDECIDED
> - The PvP activation method is **UNDECIDED** ([[Open Questions#Q-011]]). Options are documented in [[PvP Activation Options]].
> - PvP defeat penalties are **UNDECIDED** ([[Open Questions#Q-014]]).
>
> This page does **not** choose an activation method. It defines a modular UI kit that supports each candidate, so whichever option the owner picks can ship without a redesign.

> [!info] PROPOSED
> Every component and layout on this page is **PROPOSED**.

## Purpose

Make the player's PvP state impossible to misread: whether *they* can be attacked, whether *another player* can be attacked, and what happens if they lose. Provide the combat UI for player-versus-player fights (opponent health, defeat and result screens).

## Layout

- HUD PvP chip in the context strip ([[UI - Main HUD]]).
- Nameplate markers over other players (world `BillboardGui`).
- Opponent bar in the combat overlay during a PvP fight.
- Activation surfaces (one or more, depending on Q-011).
- Defeat / victory overlay.

## Hierarchy

1. My PvP state (chip).
2. Whether the player in front of me is attackable (nameplate).
3. Opponent health during a fight.
4. Result and consequences.

## Elements

| Element | Type | Content | Behaviour |
|---|---|---|---|
| PvP chip | Chip with icon | "PvP OFF" (shield icon) / "PvP ON" (crossed-swords icon) / "PvP zone" | Tap explains the current state and how to change it |
| Nameplate marker | `BillboardGui` | Crossed-swords icon on attackable players only | Non-attackable players show no marker; hover / tap shows "Not in PvP" |
| Opponent bar | `Bar/Health` (large) in CombatOverlay | Opponent name, health, their three animals' small health pips | Appears on first PvP damage exchange |
| Activation surface | See matrix below | Toggle, zone border, duel request, etc. | Per Q-011 |
| Opt-in confirm | `Modal/Confirm` | "Turn PvP on? Other players with PvP on can attack you and your animals." + penalty text from config | Mandatory the first time per session (**PROPOSED**) |
| State change countdown | Caption on chip | "PvP turns off in 10…" | Only if the chosen method uses a delay; the delay value is part of the Q-011 decision |
| Defeat overlay | Full-screen overlay | "Defeated by Player123" + consequences from config | Consequences **UNDECIDED** (Q-014) |
| Victory toast | `Toast` (success) | "You defeated Player123" | Rewards per [[PvP System]] |

### Activation method support matrix

| Candidate method (authoritative list: [[PvP Activation Options]]) | UI pieces needed |
|---|---|
| Global toggle in the menu | Toggle in the PvP chip's sheet and in [[UI - Settings]]; opt-in confirm; optional change countdown |
| PvP zones in the world | Zone border VFX; entry warning toast "Entering PvP area"; chip switches to "PvP zone"; exit toast |
| Duel requests | Request modal ("Player123 challenges you"), accept / decline, request cooldown, duel arena countdown |
| Opt-in flag at the hub | `ProximityPrompt` at a hub object; opt-in confirm; chip |
| Combination | Chip shows the most permissive current state, with a sheet listing why |

Whatever the method, two rules are fixed in the UI (**PROPOSED**): the player always sees their own state on the HUD, and a player with PvP off never shows an attackable marker.

## Interactions

- Tap chip → bottom sheet explaining state and (if the method allows) the control to change it.
- Attempting to attack a non-PvP player: the attack still plays locally as a whiff only if the combat system allows; the server deals no damage and a toast "Not in PvP" appears once per 10 s (**PROPOSED** throttle).
- Duel request (if chosen): request modal never blocks combat input; auto-declines after the server-defined expiry.

## States

| State | Chip | Notes |
|---|---|---|
| PvP off | "PvP OFF" | Default (**PROPOSED**; the default is part of Q-011) |
| PvP on | "PvP ON" | Attackable marker visible to other PvP players |
| In a PvP fight | "PvP ON" pulsing | Opponent bar shown |
| Transitioning | Countdown caption | Only if method has a delay |
| Defeated | Defeat overlay | Penalties per Q-014 |
| In a raid | Raid HUD takes priority over the PvP chip | Raid combat is governed by [[Base Raiding System]] |

## Empty states

No other players with PvP on in the server: the PvP sheet shows "No other players have PvP on right now."

## Error states

| Reason code (illustrative) | Copy |
|---|---|
| `TargetNotPvP` | "That player isn't in PvP." |
| `ToggleCooldown` | "You can change PvP again in 20 s." (value set by the chosen method) |
| `InCombat` | "You can't change PvP during combat." |

## Loading states

The chip reads the server-set PvP attribute on spawn; until it replicates, the chip shows "PvP …" and the player is treated as not attackable in the UI (the server is authoritative regardless).

## Mobile layout

Chip in the context strip (44 high hit area). Opponent bar under the top inset, full width minus margins. Duel modal (if used) with large Accept / Decline buttons away from the action cluster to prevent accidental acceptance during combat.

## Desktop layout

Same pieces; opponent bar 640 wide centred top.

> [!note] Console / gamepad
> PvP sheet opens from the menu hub. Duel requests (if used) bind Accept to `DPadUp` hold and Decline to `DPadDown` hold so they cannot be triggered by combat buttons (**PROPOSED**).

## Accessibility

- PvP state uses distinct icons (shield versus crossed swords) and text, never colour alone.
- Entering a PvP zone (if used) triggers a toast **and** a sound **and** a persistent chip change.

## Roblox implementation notes

- PvP state is a server-set player attribute ([[Service - PvPService]]); nameplate markers read the attribute of each player. Damage legality is enforced in [[Implementation - Combat Damage Pipeline]], never by the UI.
- Activation surfaces send intents (illustrative `SetPvPEnabled(bool)`, `SendDuelRequest(userId)`); all are rate-limited ([[Implementation - Rate Limiting]]).
- Components live in `HUD/ContextStrip/PvPChip`, `CombatOverlay/OpponentBar`, `Modals/DuelRequest`.

## Wireframe

```text
+--------------------------------------------------------------------------+
| [HP ██████]  Sunscorch Savanna  [⚔ PvP ON]                       12.4K   |
|               +------------------------------------------+               |
|               | Player123   ████████████░░░░  [▮][▮][▯]   |  ← opponent  |
|               +------------------------------------------+               |
|        (Player123) ⚔            (OtherPlayer)  (no marker: PvP off)      |
+--------------------------------------------------------------------------+
```

## Related documents

- [[PvP System]] · [[PvP Activation Options]] · [[Player Defeat and Penalties]] · [[Multiplayer Combat Rules]]
- [[UI - Main HUD]] · [[UI - Raid Interface]] · [[UI - Settings]] · [[Service - PvPService]] · [[Test Cases - PvP]]
