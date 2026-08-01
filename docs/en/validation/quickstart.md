---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.quickstart
title: Build and validation quickstart
language: en
status: draft
source_paths:
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- CMakePresets.json
- android/gradlew
authority: build-config
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: build
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
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
