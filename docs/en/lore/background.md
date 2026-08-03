---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: lore-background
title: 'Legacy migration draft: background'
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
- doc/design-balance-lore/lore-background.md
- doc/design-balance-lore/lore.md
- data/json/snippets/epilogue_factions.json
source_symbols: []
source_queries: []
source_fingerprint: 4ef53651276a51dbf6890808327b57987bf5db1c1d12cdd8d23431b6f5686036
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7bc07248b0996e72932974d3b7b9aded650b7a67af306b2512b1f402f149a616
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/background/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/lore/background/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/lore/background/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/lore/background/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/design-balance-lore/lore-background.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md
- path: doc/design-balance-lore/lore.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore.md
- path: data/json/snippets/epilogue_factions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/snippets/epilogue_factions.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28lore-background%29%3A+&body=Document+ID%3A+lore-background%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: background

This is the migration draft page for `lore-background`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `lore-background`
- Target: `lore/background.md`
- Replacement: lore-background
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| lore-background | doc/design-balance-lore/lore-background.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Spoilers and authority boundary

This page is for contributors writing setting, missions, maps, and items and contains central
spoilers. CCB normally lets players reconstruct events through newspapers, logs, dialogue,
locations, and unreliable narrators. Do not paste an omniscient developer timeline directly into
player text. Legacy years and links are background at a pinned commit; current JSON, maps, missions,
and dialogue define what the game actually reveals.

## Cataclysm background

Secret United States research into other dimensions developed into the XEDRA system. Researchers
returned from the netherum with anomalous matter known as `XE-037`; it escaped and spread through
the global environment, affecting living things, encouraging violence, and reanimating the dead.
While infection, unrest, and disastrous responses were already collapsing society, portal storms
tore dimensional boundaries further and admitted otherworldly entities and opportunistic powers.
By game start, coordinated global rescue has failed and survivors face the interaction of
contamination, the dead, invasive ecologies, and remnants of human institutions.

This summary is a writing framework. It does not mean every character knows the cause or that every
clue is correct. Reveal the relationships among `XE-037`, the Blob, portal technology, XEDRA, and
outside powers in layers. Ordinary survivors, government records, researchers, and non-human
entities have different and potentially conflicting information.

## Continuity checks

For new content, identify the narrator, relative date, available knowledge, and uncertainty. Reuse
current snippet, faction, mission, location, and item IDs and inspect date-generation rules, season,
world creation time, and CCB-specific divergence. Separate background canon, currently implemented
clues, and future design; unimplemented ideas stay draft. Run JSON/EOC loading and focused content
tests and call out a lore retcon that changes existing mission, save, or mod assumptions.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `4ef53651276a51dbf6890808327b57987bf5db1c1d12cdd8d23431b6f5686036`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/design-balance-lore/lore-background.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/design-balance-lore/lore-background.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
