---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.comestibles-placement
title: 'Legacy migration draft: comestibles'
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/GUIDE_COMESTIBLES.md
- src/item_factory.cpp
- data/json/items/comestibles/other.json
- data/json/items/comestibles/meat_dishes.json
- tests/comestible_test.cpp
source_symbols:
- islot_comestible::deserialize
- itype::load
source_queries: []
source_fingerprint: 5817fd0e31fe58b676450ee8f73ea9388e21169152d12d5ec577c002b7275538
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 98d6611ee488e7c3a9b4196e8120f7708b4cce17d23c5ece4c710777cd2073a0
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/comestibles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/how-to/json/comestibles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/GUIDE_COMESTIBLES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/GUIDE_COMESTIBLES.md
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/item_factory.cpp
- path: data/json/items/comestibles/other.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/items/comestibles/other.json
- path: data/json/items/comestibles/meat_dishes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/items/comestibles/meat_dishes.json
- path: tests/comestible_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/comestible_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.comestibles-placement%29%3A+&body=Document+ID%3A+json.comestibles-placement%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: comestibles

This is the migration draft page for `json.comestibles-placement`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.comestibles-placement`
- Target: `how-to/json/comestibles.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/how-to/json/comestibles/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.comestibles-placement | doc/JSON/GUIDE_COMESTIBLES.md | migrate_rewrite | stubbed | b1ee97987589450da70f30ee2feed12c9d18f479 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Placing and validating a new comestible

Directories and file names help maintainers find data but do not change `COMESTIBLE` loader
semantics. Identify the content domain, then place the object in the narrowest current file under
`data/json/items/comestibles/` with comparable entries. Do not copy a historical list containing
removed or renamed files.

### Current classification order

Prefer a clear domain file such as medicine, mutagen or serum, MRE, brewing, frozen, spice, protein,
alien, or netherum. Ordinary drinks split among alcohol, soup, drink, and drink_other. Solid food
uses current neighbors for baked goods, bread, casseroles, cereal, dairy, eggs, fruit, junk food,
meat or offal, mushrooms, nuts, raw produce or grain, sandwiches, seeds, vegetables, and wheat. Use
`other.json` only when no natural category exists.

Classification is not a gameplay tag. Declare fields and IDs explicitly for search, recipes, item
groups, or effects rather than relying on the path.

### Loader contract

`comestible_type` is mandatory. Explicit charges are bounded to at least one, while the absent-field
default path can be zero. Other members cover stack size, quench, fun, stimulant, health, spoilage,
calories, vitamins, addiction, cooks or eats like, cooking and smoking results, consumption EOCs, and
contamination. Take requiredness, defaults, and bounds from `islot_comestible::deserialize`.

### Validation

Choose a current comparable item and recipe and inspect nutrition, portions or charges, container,
spoilage, price, item groups, recipe results, and translations. Run formatting,
`make -j2 json-check`, and Mod `--check-mods`. Nutrition or processing changes also need focused
comestible and recipe tests for ingredients, byproducts, `cooks_like`, and `NUTRIENT_OVERRIDE`.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `5817fd0e31fe58b676450ee8f73ea9388e21169152d12d5ec577c002b7275538`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/GUIDE_COMESTIBLES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/GUIDE_COMESTIBLES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/GUIDE_COMESTIBLES.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
