---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-technology
title: 'Legacy migration draft: technology'
language: en
status: draft
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/design-balance-lore/technology.md
- doc/design-balance-lore/lore.md
- data/json/materials.json
source_symbols: []
source_queries: []
source_fingerprint: cf792ec1d56aa4d6f5a0efbea73bc7d7269987b7cf5ea1aa4062810c965350fb
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: fa74e29f412f65c20bab175551a4ebe53d79d0bd759ad8f91773d6e1cd3c0108
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: lore
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/technology/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/technology/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/technology/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/technology/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/design-balance-lore/technology.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/technology.md
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/lore.md
- path: data/json/materials.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/materials.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-technology%29%3A+&body=Document+ID%3A+lore-technology%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: technology

This is the migration draft page for `lore-technology`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `lore-technology`
- Target: `lore/technology.md`
- Replacement: lore-technology
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-technology | doc/design-balance-lore/technology.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Technology baseline

Pre-Cataclysm CCB Earth should remain recognizably modern in technology. A divergence should be
narrow, sourced, and connected to portal research, XEDRA, or explicit off-world technology. If an
invention would transform all pre-Cataclysm society, normally narrow or rewrite it instead of
turning the setting into generic science fiction.

### Technology layers

- **Civilian and ordinary industry** primarily follow real capability, supply chains, and cost.
  Somewhat wider fuel-cell or powered-assistance use does not make hypertechnology ubiquitous.
- **Military and XEDRA** may have rare energy sources, power armor, robots, experimental weapons,
  portals, and dimensional heuristics, constrained by programs, facilities, secrecy, quantity, and
  reliability.
- **Mutation** exploits universal Blob contamination and is not ordinary genetic engineering. Current
  mutation data and code still define visible behavior.
- **CBMs and the Exodii** belong to an interdimensional survivor tradition. Common functions should
  remain explainable by modern principles where practical; unusual interfaces, inherited
  manufacturing, and a few story-gated devices carry the handwaving.
- **Mi-go, Yrax, triffid, Blob, and similar capability** may exceed human understanding. The less
  comprehensible it is, the less a player should dismantle, redesign, or mass-produce it like
  ordinary machinery.

## Selecting technology for content

State who made it, when and why, the energy and materials it needs, who can maintain it, and why it
remains available after collapse. Distinguish prototype, limited deployment, and mass production;
an experiment needs plausible operation, failure, and supply constraints. A display name or lore
claim does not prove item behavior: trace current JSON, recipes, item uses, mapgen, factions, and
tests.

The legacy technology scale and explanations are writing models, not APIs. For a device change,
check provenance, spawn density, repair, disassembly, ammo or batteries, skills, NPC acquisition,
saves, and mod compatibility, then run JSON loading and focused tests. Unimplemented Yrax or other
sections remain draft.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `cf792ec1d56aa4d6f5a0efbea73bc7d7269987b7cf5ea1aa4062810c965350fb`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/technology.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/technology.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/design-balance-lore/technology.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
