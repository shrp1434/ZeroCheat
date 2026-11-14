---
title: Roblox Platform References
type: reference
category: references
status: proposed
priority: P1
owner: Production Manager
last_updated: 2026-11-14
tags:
  - references
  - roblox
  - platform
  - compliance
---

# Roblox Platform References

The official Roblox documentation topics the team should consult before building or changing the systems in this vault. Each entry says what to look for and which vault documents depend on it. This page is a reading list, not a summary of the platform: always read the current official page, because platform limits and policies change.

> [!info] How the links were checked
> Every URL below was opened on 2026-11-14 and resolved to the Roblox Creator Hub page named in the table. Entries marked **URL to be verified** have no checked link from an approved source (create.roblox.com or en.help.roblox.com); find the current page through the Creator Hub or Help Centre search before relying on it. Re-check all links at each roadmap gate.

> [!warning] Technical honesty
> Notes in the "What to check" column describe what the team needs to find out. They are not claims about current platform behaviour. Anything this vault states about platform behaviour without a check against these pages is *unverified* (see [[Roblox API Reference Notes]]).

## Persistence and cross-server

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| DataStoreService (API reference) | https://create.roblox.com/docs/reference/engine/classes/DataStoreService | `GetDataStore`, `GetAsync`, `SetAsync`, `UpdateAsync` semantics; request budget API | [[Service - DataService]], [[Save, Load and Recovery]] |
| Data stores (guide) | https://create.roblox.com/docs/cloud-services/data-stores | Recommended patterns, versioning, metadata, testing in Studio | [[Data Architecture Overview]], [[Data Validation and Migration]] |
| Data store error codes and limits | https://create.roblox.com/docs/cloud-services/data-stores/error-codes-and-limits | Per-server request budgets, key and value size limits, throttling behaviour | [[Save, Load and Recovery]], [[Risk Register]] (R-016) |
| MemoryStoreService (API reference) | https://create.roblox.com/docs/reference/engine/classes/MemoryStoreService | Sorted maps, queues, hash maps; expiry; quotas | [[Shared World and Player Sessions]], [[Raid Eligibility and Offline Protection]] |
| Memory stores (guide) | https://create.roblox.com/docs/cloud-services/memory-stores | Use cases, limits and best practices | [[Multiplayer Architecture]] |
| MessagingService (API reference) | https://create.roblox.com/docs/reference/engine/classes/MessagingService | `PublishAsync` and `SubscribeAsync`, message size and rate limits, delivery guarantees | [[Live Operations Framework]] (kill switches), [[World Boss - Ironbark Colossus]] and other world boss announcements |
| Cross-server messaging (guide) | https://create.roblox.com/docs/cloud-services/cross-server-messaging | Patterns and limits for cross-server communication | [[Configuration Modules]], [[Content Update Pipeline]] |

## Monetisation and compliance

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| PolicyService (API reference) | https://create.roblox.com/docs/reference/engine/classes/PolicyService | `GetPolicyInfoForPlayerAsync` and the `ArePaidRandomItemsRestricted` field; other policy fields | [[Roblox Monetisation Policy Requirements]], [[Randomised Reward Compliance]] |
| Paid random items policy guidelines | https://create.roblox.com/docs/production/monetization/paid-random-items | What counts as a paid random item (including items bought with currency that Robux can buy); odds disclosure requirements; handling restricted users | [[Randomised Reward Compliance]], [[Roblox Monetisation Policy Requirements]], [[Open Questions#Q-032]] |
| MarketplaceService (API reference) | https://create.roblox.com/docs/reference/engine/classes/MarketplaceService | `ProcessReceipt` callback rules (one handler, idempotent granting), `PromptProductPurchase`, `UserOwnsGamePassAsync` | [[UI - Shop]], [[Monetisation Product Concepts]] |
| Developer products | https://create.roblox.com/docs/production/monetization/developer-products | Product setup and receipt handling guidance | [[Monetisation Product Concepts]] |
| Passes | https://create.roblox.com/docs/production/monetization/game-passes | Pass setup and ownership checks | [[Monetisation Product Concepts]] |
| Content ratings (experience guidelines) | https://create.roblox.com/docs/production/promotion/experience-guidelines | Questionnaire topics relevant to combat, theft mechanics and paid random items | [[M22 - Launch]], **UNDECIDED** (Q-1116) |
| Community Standards | **URL to be verified** | Rules on violence depiction, scams, and conduct that apply to experiences and player interaction | [[Art Bible]], [[Risk Register]] (R-014) |
| Terms of Use | **URL to be verified** | Platform terms relevant to virtual items and player trading | [[Open Questions#Q-026]] |

## World, streaming and performance

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| Instance streaming (StreamingEnabled guide) | https://create.roblox.com/docs/workspace/streaming | Streaming behaviour, persistent models, streaming modes, client-side handling of non-streamed instances | [[Performance Guidelines]], [[M20 - Optimisation]] |
| Workspace (API reference, includes `StreamingEnabled`) | https://create.roblox.com/docs/reference/engine/classes/Workspace | Streaming-related properties | [[Performance Guidelines]] |
| Performance optimisation | https://create.roblox.com/docs/performance-optimization | Server and client optimisation guidance, memory, physics, rendering | [[Performance Guidelines]], [[Animal Scalability and Performance Budgets]] |
| MicroProfiler | https://create.roblox.com/docs/studio/microprofiler | Frame profiling on server and client | [[M20 - Optimisation]], [[Test Cases - Mobile Performance]] |
| PathfindingService (API reference) | https://create.roblox.com/docs/reference/engine/classes/PathfindingService | Path computation cost, agent parameters, waypoints | [[Implementation - Animal AI State Machine]], [[Wild Animal AI]] |

## Animation

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| Animation (overview) | https://create.roblox.com/docs/animation | Rigs, Animation Editor, inverse kinematics, animation events | [[Animation Bible]], [[Animal Rig Standards]] |
| Animator (API reference) | https://create.roblox.com/docs/reference/engine/classes/Animator | `LoadAnimation`, replication of animation tracks | [[Animation - Animal Locomotion]], [[Client Controllers]] |

## Networking and security

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| Remote events and callbacks | https://create.roblox.com/docs/scripting/events/remote | RemoteEvent, RemoteFunction and UnreliableRemoteEvent usage and limits | [[Remote Communication Contract]], [[Implementation - Remote Validation Layer]] |
| Security and cheat mitigation tactics | https://create.roblox.com/docs/scripting/security/security-tactics | Server authority, validating client input, common exploit classes | [[Security Architecture]], [[Exploit Prevention]], [[Threat Model]] |
| HttpService (API reference) | https://create.roblox.com/docs/reference/engine/classes/HttpService | Limits and restrictions if external telemetry is ever used | **UNDECIDED** (Q-1108), [[Service - AnalyticsAndLoggingService]] |

## Publishing and operations

| Topic | Official page | What to check | Vault documents that depend on it |
|---|---|---|---|
| Create and publish games and places | https://create.roblox.com/docs/production/publishing/publish-experiences-and-places | Publishing flow, places within an experience (relevant to test environments) | [[Content Update Pipeline]], **UNDECIDED** (Q-1109) |
| Place version history and reverting a published version | **URL to be verified** | Whether and how a place can be reverted to an earlier published version | [[Content Update Pipeline]] (rollback) |
| Shutting down or migrating servers to a new version | **URL to be verified** | Options for moving live servers to an update | **UNDECIDED** (Q-1115) |
| Analytics | https://create.roblox.com/docs/production/analytics | Built-in analytics dashboards and custom events | [[Service - AnalyticsAndLoggingService]], [[Live Operations Framework]] |
| Localization | https://create.roblox.com/docs/production/localization | Translation tooling and text handling | [[UI Design System]], **UNDECIDED** (Q-1111) |

## Maintaining this page

- Add a topic only with a link opened and checked against the page title, or mark it **URL to be verified**.
- When a platform page changes a limit the vault relies on, update the dependent document and record it in the [[Changelog]].
- API facts the vault relies on are collected in [[Roblox API Reference Notes]]; this page only points to the sources.

## Related documents
- [[References Index]]
- [[Roblox API Reference Notes]]
- [[Roblox Monetisation Policy Requirements]]
- [[Randomised Reward Compliance]]
- [[Performance Guidelines]]
- [[Security Architecture]]
