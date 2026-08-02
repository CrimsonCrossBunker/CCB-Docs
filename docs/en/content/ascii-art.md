---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: content.ascii-art
title: 'Legacy migration draft: ascii art'
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
- doc/ASCII_ART.md
- src/ascii_art.cpp
- src/ascii_art.h
- src/init.cpp
- data/json/ascii_art/generic_ascii.json
- data/json/bodypart_graphs/arms.json
source_symbols:
- ascii_art::load_ascii_art
source_queries: []
source_fingerprint: 090e72917bd4e8a3f233d97efdbe4ac036e3a13900805cf10c6f78d534fdc30e
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 330c6e811a69ea3a09b6f3fe005bf10e8349f1379b275b262ddad2331490c354
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
risk_group: ui
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/content/ascii-art/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/content/ascii-art/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/ASCII_ART.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/ASCII_ART.md
- path: src/ascii_art.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/ascii_art.cpp
- path: src/ascii_art.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/ascii_art.h
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/init.cpp
- path: data/json/ascii_art/generic_ascii.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/ascii_art/generic_ascii.json
- path: data/json/bodypart_graphs/arms.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/bodypart_graphs/arms.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28content.ascii-art%29%3A+&body=Document+ID%3A+content.ascii-art%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: ascii art

This is the migration draft page for `content.ascii-art`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `content.ascii-art`
- Target: `content/ascii-art.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/content/ascii-art/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| content.ascii-art | doc/ASCII_ART.md | migrate_rewrite | stubbed | 5f23722ff28c5cc552baa0422b32b1f10fd890fa | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## ASCII-art data contract

First-party ASCII art uses an `ascii_art` JSON object with at least a stable `id` and a string-array
`picture`. Current `ascii_art::load` removes color tags and measures each line by terminal display
width. A line wider than `41` display columns is trimmed and emits a debug message. A column is not a
UTF-8 byte: wide and combining characters and color tags must be checked through the real loader.

```json
{
  "type": "ascii_art",
  "id": "example_art",
  "picture": [ "<color_white>+---+</color>", "<color_white>|   |</color>" ]
}
```

This example illustrates structure and is not a resource to submit. Use existing valid color names
and close tags correctly. Blank lines, leading spaces, and Unicode box characters are part of the
image; text processing beyond the project JSON formatter can damage alignment. Body-part graphs use
a different data and rendering path, so visual similarity does not prove identical fields or size.

## Creation and review

Any editor that preserves UTF-8, spaces, and line boundaries works. REXPaint is optional tooling,
not a project contract. Confirm provenance and licensing for an external palette, font, template, or
source image instead of importing unknown artwork.

Before submission, run project JSON formatting and loading, check duplicate IDs, invalid color tags,
and debug output, and inspect the real target UI in curses and tiles with default and fallback fonts,
narrow windows, scaling, and both language environments. Measure display width after removing tags,
not only the editor canvas. ASCII art cannot be the sole way to identify an item or body-part state;
an accessible path still needs text or structure.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `090e72917bd4e8a3f233d97efdbe4ac036e3a13900805cf10c6f78d534fdc30e`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/ASCII_ART.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/ASCII_ART.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/ASCII_ART.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
