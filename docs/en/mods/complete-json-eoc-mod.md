---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.complete-json-eoc-mod
title: Complete JSON/EOC mod tutorial
language: en
status: active
doc_type: tutorial
audiences:
- new-contributor
- experienced-contributor
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- data/AGENTS.md
- data/mods/AGENTS.md
- doc/MODDING.md
- data/mods/TEST_DATA/modinfo.json
- data/mods/TEST_DATA/effect_on_condition.json
- Makefile
- data/reference/json/ccb_json_object_types.json
- data/reference/json/ccb_eoc_conditions.json
- data/reference/json/ccb_eoc_effects.json
source_symbols: []
source_queries: []
source_fingerprint: ec7b0afe102b19beb0f77c9ffbe6d8f82e2e06b59e057bdf76d897de092e0b2c
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6ded0b43085f4eef208e8256f7d9d497323f2dba7a085068a440d48be7a306c8
prerequisites:
- json.overview
- eoc.overview
depends_on:
- json.validation
- eoc.nesting
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; tutorial example is maintained in CCB-Docs.
example_validation_ids:
- docs-json-eoc-example
- json-load
- json-mod-load
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: mods
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/complete-json-eoc-mod/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/complete-json-eoc-mod/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/complete-json-eoc-mod/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/complete-json-eoc-mod/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: data/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/AGENTS.md
- path: data/mods/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/AGENTS.md
- path: doc/MODDING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/MODDING.md
- path: data/mods/TEST_DATA/modinfo.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/TEST_DATA/modinfo.json
- path: data/mods/TEST_DATA/effect_on_condition.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/mods/TEST_DATA/effect_on_condition.json
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/Makefile
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/reference/json/ccb_json_object_types.json
- path: data/reference/json/ccb_eoc_conditions.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/reference/json/ccb_eoc_conditions.json
- path: data/reference/json/ccb_eoc_effects.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/reference/json/ccb_eoc_effects.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.complete-json-eoc-mod%29%3A+&body=Document+ID%3A+mods.complete-json-eoc-mod%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Complete JSON/EOC mod tutorial

The maintained fixture lives at `examples/complete-json-eoc-mod/` in CCB-Docs and contains two files:

```text
complete-json-eoc-mod/
├── modinfo.json
└── eocs.json
```

## 1. Declare the mod

`modinfo.json` is a complete JSON array. Its ID uses a project-specific prefix and explicitly
depends on core `dda`:

```json
[
  {
    "type": "MOD_INFO",
    "id": "ccb_docs_json_eoc_example",
    "name": "CCB Docs JSON/EOC Example",
    "authors": [ "CCB contributors" ],
    "description": "A minimal contract-tested EOC mod used by the bilingual developer documentation.",
    "category": "misc_additions",
    "dependencies": [ "dda" ]
  }
]
```

## 2. Add an EOC

`eocs.json` defines an activation EOC that is not triggered automatically, so merely loading the
fixture does not alter normal play:

```json
[
  {
    "type": "effect_on_condition",
    "id": "EOC_CCB_DOCS_HELLO",
    "eoc_type": "ACTIVATION",
    "condition": { "math": [ "1 == 1" ] },
    "effect": [ { "u_message": "The CCB Docs example EOC ran." } ]
  }
]
```

## 3. Validate the maintained fixture

Run this from the CCB-Docs root, replacing the path with a CCB clone containing the PR #566 commit:

```sh
# validation: docs-json-eoc-example
python3 scripts/check_json_eoc_example_mod.py --source-repo /path/to/Cataclysm-Cleanwater-Bomb
```

The check parses both JSON files and proves that `MOD_INFO`, `effect_on_condition`, `math`, and
`u_message` exist in generated inventories at the pinned commit. It deliberately does not claim
to invoke the game loader.

Run the base repository check from the CCB source root:

```sh
# validation: json-load
make -j2 json-check
```

The current `json-check` does not scan this external CCB-Docs fixture. Before release, place the
directory in a supported third-party mod location and invoke the real loader:

```sh
# validation: json-mod-load
ccb_source=/path/to/Cataclysm-Cleanwater-Bomb
ccb_example_user=/tmp/ccb-docs-example-user
mkdir -p "$ccb_example_user/mods"
cp -R examples/complete-json-eoc-mod "$ccb_example_user/mods/ccb_docs_json_eoc_example"
"$ccb_source/cataclysm" --basepath "$ccb_source/" --userdir "$ccb_example_user/" --check-mods ccb_docs_json_eoc_example
```

After `--check-mods` succeeds, enable `dda` plus this mod in a test world, exercise the trigger,
and retain the load log.

## 4. Keep extensions verifiable

- Confirm every top-level `type` in the [object-type registry](../reference/json-object-types.md).
- Confirm every condition/effect key in the [condition](../reference/eoc-conditions.md) and
  [effect](../reference/eoc-effects.md) registries.
- Never treat a `lexical_only` candidate as a minimal valid contract.
- Keep IDs stable and mod-prefixed; declare dependencies explicitly.
- Start from the minimal EOC, then add nesting, variables, and talker use one layer at a time and
  test each layer with the real loader.
