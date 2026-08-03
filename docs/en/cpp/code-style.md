---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-code-style
title: 'Legacy migration draft: code style'
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
- doc/c++/CODE_STYLE.md
- .astylerc
- .clang-tidy
- .github/workflows/astyle.yml
- tools/format/format.cpp
source_symbols: []
source_queries: []
source_fingerprint: d2ceaf9331a10f9ab22d13115efd9e7cff032e7669b4193ca524b5e6aeaca2be
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 23289870a5b0971b7ea83a0586d443909eb6761696d6aa030da88f3d40d9f812
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
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/code-style/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/code-style/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/code-style/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/code-style/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/c++/CODE_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c++/CODE_STYLE.md
- path: .astylerc
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.astylerc
- path: .clang-tidy
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.clang-tidy
- path: .github/workflows/astyle.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/.github/workflows/astyle.yml
- path: tools/format/format.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tools/format/format.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-code-style%29%3A+&body=Document+ID%3A+cpp-code-style%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: code style

This is the migration draft page for `cpp-code-style`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `cpp-code-style`
- Target: `cpp/code-style.md`
- Replacement: cpp-code-style
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-code-style | doc/c++/CODE_STYLE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB C++ style entry points

CCB's executable style contract is `.astylerc`, `.clang-tidy`, Makefile targets, and CI, not a
copied legacy list of formatter arguments. Change configuration and CI first when a rule or
tool version changes, then update this explanation. Do not maintain an approximate second rule
set in an editor.

### Minimal pre-commit flow

```sh
make astyle-check
git diff --check
```

`astyle-check` is a read-only gate and is the best first check. To apply automatic corrections:

```sh
make astyle
```

`make astyle` can change managed files outside the lines edited by hand. Inspect
`git diff --name-only` and the full diff afterward and commit only changes belonging to the
task. Formatting is not a reason to hide an unrelated refactor. Follow the repository's
generated and third-party boundaries.

### Readability constraints

- Use current project types, units, point or coordinate types, and ID wrappers instead of
  untyped integers that hide semantics.
- Make ownership and nullability clear; follow existing RAII, container, and smart-pointer patterns.
- Keep lambdas local with explicit captures; extract complex logic into named testable functions.
- Use project APIs for translations, debug messages, and player text while preserving format types.
- Expose only needed header dependencies; include edits need build and clang-tidy or IWYU evidence.
- Do not rename serialized fields, JSON or Lua APIs, or cross-Mod IDs as a style cleanup.

These guide review; the concrete mechanical rules are the current `cata-*` clang-tidy checks
and AStyle output. If an example conflicts with the formatter, update the example instead of
reversing formatter output by hand.

### Change boundaries and generated code

Read the nearest `AGENTS.md` and `ai/generated-files.yml` first. Update generated files through
their owner generator. Edit vendored third-party code only when the task explicitly targets it.
Keep a broad rename, include reorder, or namespace cleanup in a separate commit from a behavior fix.

### Choosing validation

Style success does not prove compilation. Compile at least the affected translation unit. A
public header, template, build flag, or cross-platform path needs the relevant build matrix.
Report only commands that actually ran and distinguish missing local tools, CI evidence, and
checks not run.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `d2ceaf9331a10f9ab22d13115efd9e7cff032e7669b4193ca524b5e6aeaca2be`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/CODE_STYLE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/CODE_STYLE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/c%2B%2B/CODE_STYLE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
