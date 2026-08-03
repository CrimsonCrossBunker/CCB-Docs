---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: how-to.json-tools
title: 'Legacy migration draft: tools'
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
- doc/JSON/JSON_TOOLS.md
- tools/json_tools/keys.py
- tools/json_tools/values.py
- tools/json_tools/pluck.py
- tools/json_tools/table.py
- tools/json_tools/lister.py
source_symbols:
- main
source_queries: []
source_fingerprint: b2259289218e6d63d58941659c741afac360e4de7237e3ddea74b894278277b6
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 20b16ba7efc824d39b91c9594c849c2c44c476f0f3621774ed7ff34b01518f41
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/tools/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/tools/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/JSON_TOOLS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md
- path: tools/json_tools/keys.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/keys.py
- path: tools/json_tools/values.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/values.py
- path: tools/json_tools/pluck.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/pluck.py
- path: tools/json_tools/table.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/table.py
- path: tools/json_tools/lister.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/json_tools/lister.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28how-to.json-tools%29%3A+&body=Document+ID%3A+how-to.json-tools%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: tools

This is the migration draft page for `how-to.json-tools`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `how-to.json-tools`
- Target: `how-to/json/tools.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/tools/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| how-to.json-tools | doc/JSON/JSON_TOOLS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Select JSON tools by task

Repository tools fall into formatters, loaders or validators, read-only queries, and migration
scripts. Run `-h` first and constrain scope with `git diff --name-only`. Query output is not a
contract, and every changed file from a bulk transform needs review.

### Formatting and loading

```sh
make -j2 tools/format/json_formatter.cgi RELEASE=1
tools/format/json_formatter.cgi path/to/changed.json
make -j2 json-check
```

The project formatter understands CCB's JSON dialect; do not let a generic formatter remove comments
or rewrite the repository. `json-check` validates core loading. A Mod also needs real `--check-mods`
coverage.

### Query keys and values

`tools/json_tools/keys.py` counts fields found on matching objects and `values.py` counts values for
one key. They support `key=value` filters, `--human`, and nested dotted keys.

```sh
tools/json_tools/keys.py --human type=TOOL
tools/json_tools/values.py --key material --human type=TOOL
```

MISSING means a sample omits the member; it does not prove absence of a loader default or that the
field is invalid. Use the registry inventory to locate the handler and source for requiredness.

### Generators and specialized tools

`tools/json_api/generate_contracts.py` owns object and EOC inventories. `copy_from.py`,
`dialogue_validator.py`, and `json_tools/*` apply only to structures described by their help. Before
a rewrite, create a narrow file list, preserve the commit, use a dry run or temporary worktree, then
validate with the owner formatter and loader. Do not sweep third-party, generated, or all `data/` as
a cleanup.

### Auditable output

Record command, input paths or filters, tool commit, changed-file count, and validation in the PR.
Fix the first input error rather than publishing partial statistics. Keep decision reports as CI
artifacts; commit only generated references explicitly named by project metadata.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `b2259289218e6d63d58941659c741afac360e4de7237e3ddea74b894278277b6`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_TOOLS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_TOOLS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
