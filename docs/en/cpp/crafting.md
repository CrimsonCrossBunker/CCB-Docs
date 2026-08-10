---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.crafting
title: Crafting subsystem
language: en
status: stale
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/crafting.h
- src/crafting.cpp
- src/craft_command.h
- tests/crafting_test.cpp
source_symbols:
- class craft_command
source_queries: []
source_fingerprint: 6a0103d0d82160158e816f25c0ecaa11fa3c7c84fdac85f214eca5538595d42f
authority: source-and-tests
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6c119fe070dc1bedf79c5cf26341ce81984e28e46e4732baf7f04c8e26ba9c24
prerequisites:
- cpp.character
- cpp.inventory
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp-crafting
risk_level: normal
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: src/crafting.cpp'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: src/crafting.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/crafting.h
- path: src/crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/crafting.cpp
- path: src/craft_command.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/craft_command.h
- path: tests/crafting_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/crafting_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.crafting%29%3A+&body=Document+ID%3A+cpp.crafting%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Crafting

## Responsibility

Crafting resolves recipe knowledge, component/tool requirements, accessible inventories,
batch/time calculations, selections, work progress, and creation or disassembly of item
results. `craft_command` records a chosen execution plan.

## Entry points

Start with `src/crafting.h`, `src/crafting.cpp`, and `src/craft_command.h`. Character-specific
access is in `character_crafting.cpp`, presentation in `crafting_gui.cpp`, and static recipe
contracts in recipe and requirement loaders.

## Data ownership

Registries own recipes and requirements. Characters and nearby containers own source items;
temporary crafting inventories are views. An in-progress craft item owns selected components
and progress needed to resume work.

## Dependencies

Crafting depends on recipes, requirement data, item locations and pockets, skills,
proficiencies, qualities, map/vehicle inventories, activities, calories and time.

## Lifecycle

Recipes load and finalize; a character builds an accessible inventory, checks knowledge and
requirements, chooses components, starts an activity, advances work, then completes, aborts,
or resumes the craft.

## Invariants

Selections satisfy the exact requirement alternative; consumed items still belong to valid
locations; batch math and progress use consistent units; completion cannot consume twice; and
resume data matches the recipe and components.

## Extension points

Add recipes and requirements in JSON. Native extensions should add a reusable requirement or
activity rule rather than a recipe-ID special case, and must cover UI and non-UI callers.

## Serialization

`craft_command` selections and in-progress craft data have serialization in the native save
layer. Persist IDs and selected components, not temporary inventory caches or UI filters.

## Tests

Use crafting, requirements, temporary-inventory, uncraft, GUI, attention, proficiency, and
activity tests. Cover competing alternatives and interrupted/resumed work.

## Performance

Recipe filtering repeatedly queries large inventories. Reuse scoped requirement caches and
avoid rebuilding map-wide crafting inventories for each displayed recipe.

## CCB divergence

CCB recipes and crafting behaviors may differ from upstream even when recipe IDs match. Ports
must load CCB data and validate requirement, duration, and resume semantics.

## Technical debt

Requirement solving, UI selection, and activity execution cross several layers. Keep their
contracts explicit and do not let UI state become execution authority.
