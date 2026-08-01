---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.quickstart
title: Validation quickstart
language: en
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- CMakePresets.json
- android/gradlew
source_symbols: []
source_queries:
- Basic discovery and validation
- 'kind: test_matrix'
source_fingerprint: 900c3cc35f171c4bd297e703e5442b63b64871988f1284b600fca952afe88b1f
authority: build-config
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7bbe452f2a9397eac25ccbfb804f71d0a081288915bb3900ef5f2c0fcb9f4114
prerequisites:
- architecture.project-map
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/quickstart/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/quickstart/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/quickstart/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/quickstart/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/9d8f26582da0f53ca1e29f8f072aeef43955655b
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/AGENTS.md
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/CMakePresets.json
- path: android/gradlew
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/android/gradlew
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.quickstart%29%3A+&body=Document+ID%3A+validation.quickstart%0ALanguage%3A+en%0AVerified+commit%3A+9d8f26582da0f53ca1e29f8f072aeef43955655b%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Build and validation quickstart

CCB CI, CMake, Makefile, Gradle, and repository scripts define validation
behaviour. This page is only a routing aid. If a command here conflicts with a
build file, mark this page stale and repair it against the build contract.

## Choose the smallest sufficient check first

| Changed area | First check | Notes |
| --- | --- | --- |
| Agent/governance metadata | `python3 tools/agent/check_project_metadata.py` | Then run the `tools/agent` unit tests |
| C++ | `make astyle-check` | Behaviour changes also need focused Catch2 tests |
| C++ tests | `make -j2 tests` | Then run `./tests/cata_test "filter"` |
| JSON | `make -j2 json-check` | Also run the repository formatter on changed files |
| Lua contract | `check_luals_declarations.py` and `check_coverage.py` | Check schema, registration, and declaration changes |
| CMake | `cmake --preset linux-x64` | Use an existing repository preset |
| Android | `cd android && ./gradlew test` | Requires a configured Android SDK |

The complete routing data lives in `ai/test-matrix.yml`. If an expensive or
platform-specific check lacks dependencies, report why it was skipped. Never
claim a check passed when it did not run.

## Record validation results

A pull request records:

1. the exact commands that ran;
2. focused test filters or names;
3. results and any relevant RNG seed;
4. skipped checks and reasons;
5. scenarios reviewers should verify separately.

Documentation-impact automation is advisory in Phase 0/1. It does not replace
source tests and does not block an ordinary source pull request because of
unrelated documentation debt.
