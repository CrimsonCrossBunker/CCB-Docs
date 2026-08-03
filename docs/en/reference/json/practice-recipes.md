---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.practice-recipes
title: 'Legacy migration draft: practice recipes'
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
- doc/JSON/PRACTICE_RECIPES.md
- src/recipe.cpp
- src/recipe_dictionary.cpp
- data/json/recipes/practice/computers.json
- tests/crafting_gui_test.cpp
source_symbols:
- recipe_dictionary::load_practice
- recipe::load
source_queries: []
source_fingerprint: 888f1cfe57287eb7ec1eb53c459c19afc0fefb5ce004b25807b1dc2373cb3a9f
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3920bc7efa18801188441eee12efeeda35148ec749ec732299d295ba4cae0508
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/practice-recipes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/practice-recipes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/PRACTICE_RECIPES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PRACTICE_RECIPES.md
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/recipe.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/recipe_dictionary.cpp
- path: data/json/recipes/practice/computers.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/recipes/practice/computers.json
- path: tests/crafting_gui_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/crafting_gui_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.practice-recipes%29%3A+&body=Document+ID%3A+json.practice-recipes%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: practice recipes

This is the migration draft page for `json.practice-recipes`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.practice-recipes`
- Target: `reference/json/practice-recipes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/practice-recipes/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.practice-recipes | doc/JSON/PRACTICE_RECIPES.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Practice recipes

`type: practice` uses the main recipe dictionary and crafting UI but has no ordinary result. The
loader rejects `result` and `difficulty`, and requires id, name, category, subcategory, and
`practice_data`; description is optional. Components, tools, using, skill and proficiency,
autolearn, and book learning share recipe contracts, while byproducts remain available.

### practice_data

`min_difficulty` has no separate mandatory check and retains its structure default when absent.
`max_difficulty` defaults to `MAX_SKILL - 1` and `skill_limit` to `MAX_SKILL`. Runtime recipe
difficulty follows practical skill within the range, and the UI marks practice above the skill limit
as no longer increasing it.

The historical recommendations that `skill_limit <= max_difficulty + 1` and every practice takes one
hour are balance conventions, not current loader bounds. Explain exceptions and compare against
current entries for the same skill or proficiency.

### Design and validation

Use `CC_PRACTICE` and the correct subcategory for consistent navigation. Requirements should model
practice consumption; byproducts must not bypass a productive recipe. Proficiency practice also
needs prerequisites, learning time, focus, and failure or time multipliers reviewed.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In the crafting UI, cover locked,
below-range, in-range, above-limit, missing requirement, helper, and book cases. Add focused
`tests/crafting_gui_test.cpp` coverage and prove no result item is generated.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `888f1cfe57287eb7ec1eb53c459c19afc0fefb5ce004b25807b1dc2373cb3a9f`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/PRACTICE_RECIPES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PRACTICE_RECIPES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/PRACTICE_RECIPES.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
