---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: developer-tooling
title: 'Legacy migration draft: developer tooling'
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
- doc/c++/DEVELOPER_TOOLING.md
- build-scripts/clang-tidy-run.sh
- build-scripts/ci-iwyu-run.py
- .github/workflows/clang-tidy.yml
- .github/workflows/iwyu.yml
source_symbols: []
source_queries: []
source_fingerprint: 71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1879198adf7ba5e7b0479d5363ab05b8997739674958edd566bf66f3beb12d40
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: dumb-kevin, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/developer-tooling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/developer-tooling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/developer-tooling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/DEVELOPER_TOOLING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/DEVELOPER_TOOLING.md
- path: build-scripts/clang-tidy-run.sh
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/build-scripts/clang-tidy-run.sh
- path: build-scripts/ci-iwyu-run.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/build-scripts/ci-iwyu-run.py
- path: .github/workflows/clang-tidy.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/clang-tidy.yml
- path: .github/workflows/iwyu.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/iwyu.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28developer-tooling%29%3A+&body=Document+ID%3A+developer-tooling%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: developer tooling

This is the migration draft page for `developer-tooling`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `developer-tooling`
- Target: `cpp/developer-tooling.md`
- Replacement: developer-tooling
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| developer-tooling | doc/c++/DEVELOPER_TOOLING.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB developer toolchain

Choose tools by change type; contributors do not need the entire static-analysis stack for every
task. The minimum loop is to locate source and tests, configure a reproducible build, compile
the narrowest target, run focused validation, and inspect the diff. Clang-tidy, IWYU, clangd,
ctags, and profilers are additional layers as needed.

### Compilation database and editors

Generate `compile_commands.json` with a current CMake configuration:

```sh
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build -j2
```

Match feature flags to the platform or CI job under review. Point clangd to the database in the
build directory. Do not commit `compile_commands.json`, clangd indexes, ctags, Doxygen HTML, or
large symbol databases. Keep them as local caches or CI artifacts.

### Clang-tidy

`.clang-tidy` and `tools/clang-tidy-plugin` define CCB checks. CI is driven by
`.github/workflows/clang-tidy.yml` and `build-scripts/clang-tidy-run.sh`. The script creates a
compilation database, selects directly and transitively affected translation units, and expects
the built Cata plugin.

Even a one-file local check needs the matching database and plugin or wrapper. A bare system
clang-tidy can omit `cata-*` checks. Review each change after an automatic `-fix`; do not accept
cross-file rewrites blindly.

### Include-what-you-use

`.github/workflows/iwyu.yml` and `build-scripts/ci-iwyu-run.py` are the current CI entry points.
The script depends on `files_changed`, affected-file analysis, `tools/iwyu/cata.imp`, and a
blacklist, and explicitly targets CI. For a local run, follow the current example in the script
header and use matching tool and database versions instead of a copied LLVM installation guide.

IWYU suggestions are not automatically correct. Platform wrappers, template instantiation,
associated headers, and keep pragmas have project rules. Recompile affected targets after applying them.

### Formatters, indexes, and generated output

- C++: run `make astyle-check`; after `make astyle`, inspect the complete diff.
- JSON: use the repository formatter, then run loader and ID checks.
- Python: run locked lint and tests only for relevant scripts and tests.
- ctags and Doxygen: use them for navigation, not as API authority, and do not commit output.

Take every command from current CI, CMake, Makefile, and scripts. A legacy fixed LLVM version,
upstream download, or old IDE extension is historical material rather than a CCB requirement.

## History and attribution

Accepted inventory contributors: dumb-kevin, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `71d889bd30bafd07c041e9d131a9381325bce710155ffaeb9c5b11c336bd282d`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/DEVELOPER_TOOLING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/DEVELOPER_TOOLING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/DEVELOPER_TOOLING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
