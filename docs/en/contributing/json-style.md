---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.json-style
title: 'Legacy migration draft: json style'
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
- doc/JSON/JSON_STYLE.md
- Makefile
- .github/workflows/json.yml
- tools/format/format_main.cpp
- data/AGENTS.md
source_symbols:
- main
source_queries: []
source_fingerprint: 31a4661a1f617609395dffcec4a18ea6c54a37c3fc9ee5edae1f6ef65cd3a90f
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1217a7b510c5862ccca3162875cf50edadd3016bac08f932abf30fcd9e67cfeb
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
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/json-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/json-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_STYLE.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/Makefile
- path: .github/workflows/json.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/.github/workflows/json.yml
- path: tools/format/format_main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/tools/format/format_main.cpp
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/AGENTS.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.json-style%29%3A+&body=Document+ID%3A+contributing.json-style%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: json style

This is the migration draft page for `contributing.json-style`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `contributing.json-style`
- Target: `contributing/json-style.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/json-style/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| contributing.json-style | doc/JSON/JSON_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current JSON style and validation

Two-space indentation, stable field layout, short inline arrays, and wrapped long structures
are determined by the repository formatter. Do not guess formatting from a legacy example
or use a generic formatter across whole files. CCB's formatter parses the project's JSON
dialect and emits project style.

### Formatting entry points

CI runs the complete JSON style check with:

```sh
make style-all-json-parallel RELEASE=1
```

For a small set of locally changed, checked files, use:

```sh
make style-json
```

The Makefile's `JSON_FORMATTER_BIN` selects the platform artifact, such as
`tools/format/json_formatter.cgi` or `.exe`. Do not depend on the legacy external web
formatter.

### Semantic validation

```sh
make -j2 json-check
```

Formatting proves layout only; `json-check` also exercises loading. Changes to stable IDs,
`copy-from`, EOCs, item groups, mapgen, or Mod dependencies require the relevant ID,
loader, or focused tests as well. An object type with incomplete Schema coverage is not
valid merely because an editor reports no error.

### Editing principles

- Format only files needed by the PR and inspect every extra formatter change.
- Use neighbouring first-party definitions for field order and actual usage, while treating
  the loader as authoritative for required fields and defaults.
- `//` comments and project extensions are not standard JSON; avoid tools that delete them.
- Run the owner generator instead of editing a generated inventory by hand.
- Record formatter and loading checks, the Mod set, and every skipped check in the PR.

See the [JSON overview](../json/overview.md) and
[inheritance and copy-from](../json/inheritance-copy-from.md).

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `31a4661a1f617609395dffcec4a18ea6c54a37c3fc9ee5edae1f6ef65cd3a90f`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/JSON_STYLE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
