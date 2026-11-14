---
title: Service - CombatService
type: technical-service
category: technical-architecture
status: mixed
priority: P0
owner: Senior Luau Engineer
last_updated: 2026-11-14
tags:
  - technical-architecture
  - services
  - combat
  - damage
  - security
---

# Service - CombatService

> [!info] PROPOSED
> Layer **7**. Design is **PROPOSED**; code is illustrative Luau, not tested. Combat design: [[Combat System Overview]], [[Player Combat]], [[Damage, Defence and Health Model]], [[Combat States and State Machine]]. Damage pipeline implementation: [[Implementation - Combat Damage Pipeline]].

> [!success] CONFIRMED rules enforced here
> Real-time hybrid combat with player basic attacks and special moves with cooldowns (D-005). Player strength is separate from animal strength (D-007). Manual and automatic abilities (D-008). Auto-targeting plus manual target commands (D-009). Defeat penalties vary by battle type, values **UNDECIDED** (D-013, [[Open Questions#Q-014]]).

## Responsibility

- Keep the **registry of combat entities**: players, companions, wild animals, bosses and raid guards.
- Validate every player combat intent (attack, special, dodge, manual ability, target command) against server state.
- Compute and apply **all damage and healing** server-side through the damage pipeline.
- Track cooldowns, combat tags (8 s), invulnerability windows and knockout states.
- Decide hostility (who may hit whom), asking [[Service - PvPService]] for player-versus-player and reading the `raidId` tag that [[Service - RaidService]] sets on raid participants (CombatService never calls RaidService, which sits in a higher layer).
- Award **kill credit** (≥ 10% of max HP within the combat-tag window, D-040) and dispatch rewards: Cash (via EconomyService), XP (via ProgressionService) and discovery (via IndexService).
- Raise `PlayerDefeated` with a battle type so the correct penalty hook runs.

## Inputs

| Input | Source |
|---|---|
| `Combat/BasicAttack`, `UseSpecial`, `Dodge`, `UseAnimalAbility`, `CommandTarget` | Client ([[Remote Communication Contract#2.2 Combat]]) |
| `RequestAttack(attackerId, targetId, skillId)` | AnimalAIService (wild, companion, guard), BossService |
| `RegisterEntity` / `UnregisterEntity` | SpawnService, AnimalAIService, BossService, RaidService |
| Player level, strength inputs | ProgressionService |
| Training Grounds, Multiplier Shrine, Trophy Hall bonuses | BaseService |
| Team (which animals are companions) | TeamService |
| PvP permission | PvPService |

## Outputs

| Output | Consumer |
|---|---|
| `Health` / `MaxHealth` attributes on entity models | Clients |
| `Combat/HitConfirm` (unreliable), `EntityState`, `CooldownSync`, `ActionRejected`, `PlayerDefeated`, `RewardGranted` | Clients |
| Signals (below) | AnimalAIService, SpawnService, BossService, RaidService |
| `EconomyService:Credit`, `ProgressionService:AddXP`, `IndexService:RegisterDiscovery` | Reward dispatch |

## Dependencies

[[Service - EconomyService]], [[Service - ProgressionService]], [[Service - IndexService]], [[Service - BaseService]], [[Service - PvPService]], [[Service - TeamService]], [[Service - DataService]], [[Service - AnalyticsAndLoggingService]]. Systems: `DamagePipeline`, `ZoneQuery`.

## Events

| Kind | Name | Payload |
|---|---|---|
| Signal | `EntityDamaged` | `(target: CombatEntity, source: CombatEntity?, amount: number)` |
| Signal | `EntityKnockedOut` | `(target: CombatEntity, source: CombatEntity?)` |
| Signal | `EntityDefeated` | `(target: CombatEntity, credited: { Player })` |
| Signal | `PlayerDefeated` | `(player: Player, battleType: BattleType, source: CombatEntity?)` |
| Signal | `CombatTagChanged` | `(player: Player, inCombat: boolean)` |
| Remotes | see Outputs and Inputs | [[Remote Communication Contract#2.2 Combat]] |

## Data structures

```lua
--!strict
export type EntityKind = "Player" | "Companion" | "Wild" | "Boss" | "Guard"
export type BattleType = "Wild" | "Boss" | "PvP" | "Raid"
export type CombatState = "Active" | "Stunned" | "Invulnerable" | "KnockedOut" | "Defeated"

export type Stats = { hp: number, atk: number, def: number, as: number, ms: number, range: number }

export type CombatEntity = {
	id: string,                 -- server-issued, mirrored to the model as attribute EntityId
	kind: EntityKind,
	model: Model,
	ownerUserId: number?,       -- players, companions, guards
	speciesId: string?,
	regionId: string?,
	stats: Stats,
	hp: number,
	state: CombatState,
	cooldowns: { [string]: number },          -- key -> server time when ready
	damageLedger: { [number]: { dealt: number, at: number } }, -- userId -> contribution
	lastHitAt: number,
	raidId: string?,            -- set while the entity is part of a raid
}

export type DamageResult = {
	applied: number,
	knockedOut: boolean,
	blocked: "Invulnerable" | "NotHostile" | "OutOfRange" | nil,
}
```

## Stat sources (from [[Canonical Proposed Values]], all **PROPOSED**)

| Entity | HP, ATK, DEF |
|---|---|
| Player | HP `100 + 12 × (L − 1)`, DEF `5 + 0.5 × (L − 1)`; attack damage uses effective Strength `BaseStrength × (1 + TrainingGroundsBonus + OtherStrengthBonuses)` with Training Grounds +5% per level |
| Companion | Species stats from [[Animal Statistics Database]] × (1 + 0.08 × ascension level) × (1 + 0.04 × Training Grounds level) |
| Wild | Species stats × HP ×2.0, ATK ×0.75, both × region multiplier |
| Boss | [[Boss Design Overview]] and the individual boss page |

Damage: `ATK × SkillMultiplier × (100 / (100 + DEF_target)) × Random(0.95, 1.05)`, no critical hits at launch. The random factor uses a server `Random.new()` instance owned by the pipeline.

## Public API

```lua
--!strict
function CombatService:RegisterEntity(spec: {
	kind: EntityKind, model: Model, stats: Stats, ownerUserId: number?,
	speciesId: string?, regionId: string?, raidId: string?,
}): CombatEntity
function CombatService:UnregisterEntity(id: string): ()
function CombatService:GetEntity(id: string): CombatEntity?
function CombatService:GetPlayerEntity(player: Player): CombatEntity?

-- Used by AI and bosses. Validates cooldown, range and hostility exactly like player intents.
function CombatService:RequestAttack(attackerId: string, targetId: string, skillId: string): DamageResult?

function CombatService:ApplyHeal(sourceId: string, targetId: string, percentOfMaxHp: number): number
function CombatService:IsHostile(a: CombatEntity, b: CombatEntity): boolean
function CombatService:IsInCombat(player: Player): boolean
function CombatService:Revive(id: string, hpFraction: number): ()

-- Penalty hooks per battle type. Values are UNDECIDED (Q-014): hooks ship as no-ops.
function CombatService:SetDefeatHandler(battleType: BattleType, handler: (player: Player) -> ()): ()
```

## Intent validation (player basic attack)

```lua
--!strict
-- Illustrative Luau, not tested.
local function onBasicAttack(player: Player, p: { seq: number, aim: Vector3, targetId: string? })
	local me = CombatService:GetPlayerEntity(player)
	if not me or me.state == "KnockedOut" or me.state == "Defeated" or me.state == "Stunned" then
		return reject(player, "BasicAttack", p.seq, "E_COOLDOWN")
	end
	if p.seq <= (lastSeq[player] or 0) then return end -- duplicate or replay
	lastSeq[player] = p.seq

	local now = workspace:GetServerTimeNow()
	if now < (me.cooldowns.Basic or 0) - JITTER_ALLOWANCE then
		return reject(player, "BasicAttack", p.seq, "E_COOLDOWN")
	end

	local comboStep = Combo.advance(player, now)              -- 0.8 / 0.8 / 1.4, resets after 1.2 s idle
	me.cooldowns.Basic = now + COMBO_INTERVAL                  -- 0.45 s

	local target = resolveTarget(me, p.targetId, p.aim)        -- server positions only
	if not target then return end                              -- a whiff is valid
	if not inRange(me, target, Tolerance.melee(player)) or not lineOfSight(me, target) then
		return reject(player, "BasicAttack", p.seq, "E_OUT_OF_RANGE")
	end
	if not CombatService:IsHostile(me, target) then return end

	DamagePipeline.apply(me, target, comboStep.multiplier, "Basic")
end
```

Tolerances (range margin, jitter allowance) are defined in [[Server-Client Responsibilities#4. Validation tolerances (PROPOSED)]].

## Kill credit and rewards

When a `Wild` entity's HP reaches 0:

1. Collect every `userId` in its `damageLedger` whose contribution is ≥ 10% of max HP and whose last hit is within 8 s (combat-tag window). Companion damage counts for the owner.
2. For each credited player still in the server: `cash = floor(BaseCash[rarity] × RegionMultiplier × (1 + BaseService:GetCashBonus(player)))`, `xp = BaseXP[rarity] × RegionMultiplier`.
3. Call `EconomyService:Credit`, `ProgressionService:AddXP`, `IndexService:RegisterDiscovery(player, speciesId)`.
4. Fire `EntityDefeated(target, credited)`; SpawnService schedules the respawn, AnimalAIService releases the entity.
5. Send `Combat/RewardGranted` to each credited player.

Bosses use the same ledger, but BossService handles reward eligibility (once per player per spawn) because boss rewards are **UNDECIDED** ([[Open Questions#Q-015]]).

## Battle type resolution

| Situation | Battle type | Penalty hook |
|---|---|---|
| Player KO'd while the last damage source is a wild animal | `Wild` | `Wild` handler (no-op until Q-014) |
| Last source is a boss or boss add | `Boss` | `Boss` handler |
| Last source is another player or their companion, outside a raid | `PvP` | Set by PvPService |
| Either player is in an active raid together | `Raid` | Set by RaidService |

Companion knockout and recovery rules are defined in [[Animal Combat Behaviour]]; this service only exposes `Revive`.

## Error handling

| Case | Behaviour |
|---|---|
| Intent from a player whose entity is not registered (still spawning) | Ignored silently |
| Target ID unknown or despawned | Ignored (honest race with despawn) |
| Out of range, on cooldown | `Combat/ActionRejected` with code; `Info` sampled log |
| Repeated impossible ranges (≥ 3× tolerance) | `Security` log `combat.range_violation`; suspicion score |
| Error inside the pipeline | Caught by `xpcall`; damage not applied; `Error` log; combat continues |

## Security requirements

- The client never sends damage, multipliers, target HP or positions used for validation. All positions come from the server's view of models.
- Cooldowns and combo timing are tracked server-side; the client's cooldown UI is advisory.
- Line of sight uses `workspace:Raycast` with a filter that ignores characters and companions.
- Players inside their own `PlotBounds` during a shield cannot be damaged by other players ([[Shield Mechanics]]).
- PvP damage requires `PvPService:CanDamage(attacker, victim)` on **every** hit, not just at engagement.
- Companion damage is attributed to the owner for kill credit and PvP permission.

## Testing requirements

| Test | Type |
|---|---|
| Damage formula matches the reference within the 0.95–1.05 random band over 10,000 samples | Unit |
| Kill credit: 3 players with 50/40/10% contributions all credited; a 9.9% contributor is not | Unit |
| Contribution older than 8 s is not credited | Unit |
| Basic attack spam at 20/s produces at most the combo cadence of hits | Exploit test |
| Attack from 40 studs with a melee role is rejected | Exploit test |
| PvP hit on a non-participating player deals no damage | Unit, [[Test Cases - PvP]] |
| KO during a raid yields battle type `Raid` | Unit |
| 16 players and 180 wild animals: combat work under 1.5 ms average per frame | Load test ([[Performance Guidelines]]) |

Full case list: [[Test Cases - Combat]].

## Related documents
- [[Technical Architecture Index]]
- [[Combat System Overview]]
- [[Damage, Defence and Health Model]]
- [[Combat Rewards]]
- [[Multiplayer Combat Rules]]
- [[Implementation - Combat Damage Pipeline]]
- [[Service - AnimalAIService]]
- [[Service - PvPService]]
- [[Test Cases - Combat]]
