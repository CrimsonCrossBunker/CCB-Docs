---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-overview
title: 'Legacy migration draft: overview'
language: en
status: active
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/design-balance-lore/lore.md
- doc/design-balance-lore/lore-background.md
- doc/design-balance-lore/lore-factions.md
source_symbols: []
source_queries: []
source_fingerprint: f7d75b8cadfa6753bff60372b7d010d7aa16b90d7fce63e82cafeb143f301074
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: ae0f24ddd5bfa8985065cd8d756657db7d3a753647927daa85cbda39fed4f992
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/lore.md
- path: doc/design-balance-lore/lore-background.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/lore-background.md
- path: doc/design-balance-lore/lore-factions.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/lore-factions.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-overview%29%3A+&body=Document+ID%3A+lore-overview%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: overview

This is the migration draft page for `lore-overview`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `lore-overview`
- Target: `lore/overview.md`
- Replacement: lore-overview
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-overview | doc/design-balance-lore/lore.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Contributor entry point to the setting

CCB's player premise is simple: the world collapsed abruptly, the dead fill cities,
otherworldly creatures and surviving human organizations compete for resources, and the character
does not know the full cause. Developer background is more detailed, but locations, items,
newspapers, logs, dialogue, missions, and interacting systems should let players reconstruct it over
time. Omniscient explanation belongs in contributor material, not ordinary NPC dialogue.

### Information layers

- **Direct observation:** environment, enemy behavior, items, injury, weather, and public events.
- **In-world records:** newspapers, terminals, recordings, missions, and dialogue with an author,
  date, and bias.
- **Expert inference:** XEDRA remnants, the Hub, outside factions, or research records explain part
  of a mechanism but may still be wrong or conceal facts.
- **Backstage canon:** spoiler material that keeps content consistent without promising full
  revelation in game.
- **Future design:** unimplemented direction that remains draft and separate from current behavior.

## Core continuity

The pre-Cataclysm world should remain recognizable as modern society. Narrow differences come from
portal research, XEDRA, and constrained high technology. `XE-037` or Blob contamination, biological
change, reanimation, social collapse, and portal storms combine to create the Cataclysm; there is no
single public explanation. Human factions split from a shared society only recently and still face
ordinary food, safety, trust, and winter problems. Otherworldly powers may have entirely different
timescales, perception, and goals.

New lore should cite current IDs and sources, state what the narrator knows, why, and when, and
check background, technology, factions, missions, and published player clues. A retcon must identify
affected JSON, dialogue, maps, saves, mods, and translations and receive design-Issue review first.
Do not let an old design page override current implementation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `f7d75b8cadfa6753bff60372b7d010d7aa16b90d7fce63e82cafeb143f301074`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/lore.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/lore.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/design-balance-lore/lore.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
