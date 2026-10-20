---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.validation
title: JSON validation and evidence levels
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
- data/reference/json/ccb_json_object_types.json
- tools/json_api/contract-inventory.schema.json
- tools/json_api/generate_contracts.py
- tools/json_api/test_generate_contracts.py
- src/init.cpp
- src/generic_factory.h
- tests/json_load_test.cpp
- doc/JSON/JSON_INHERITANCE.md
- doc/JSON/JSON_STYLE.md
source_symbols: []
source_queries: []
source_fingerprint: d4736958a65401eacd855859ce5668adf6b7de5ae4cbd2d5c85cd7b4c959994c
authority: api-contract
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 894bf59b0d4817ec0038d2fc7234d09c02265e59d75e8ef6c6c715583bcc2b74
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
- eoc.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; source contracts and Git history remain authoritative.
example_validation_ids:
- json-contract
- json-load
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1038
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/doc/JSON/JSON_STYLE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.validation%29%3A+&body=Document+ID%3A+json.validation%0ALanguage%3A+en%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON validation and evidence levels

Different checks prove different facts. Do not report “parses” as “fully loads,” and do not use
lexical occurrence counts as evidence that a field is required.

## Recommended order

1. Run the repository JSON formatter to prove canonical project formatting.
2. Regenerate contract inventories and run their Schema, count, source-location, and example-pointer tests.
3. Run `json-check`. The current `chkjson` checks object/array syntax and a top-level string `type`
   under `data/json`; it is not a full semantic invocation of every loader.
4. Build the test program. Test startup loads core/test data; then run focused Catch2 tests for the type.
5. For an external mod, load it in a real CCB executable and test world; record version,
   dependencies, and logs.

Run these from the CCB source root:

```sh
# validation: json-contract
python3 tools/json_api/generate_contracts.py --check
python3 -m unittest discover -s tools/json_api -p 'test_*.py'
# validation: json-load
make -j2 json-check
```

## Evidence levels

| Marker | What it proves | What it does not prove |
| --- | --- | --- |
| `mandatory` / `optional` | Explicit field-read evidence in a loader | Every conditional and cross-field constraint |
| `partial` | A subset of the contract is classified | That omitted fields are safe or optional |
| `unclassified` | No publishable source classification yet | That the field does not exist |
| `lexical_only` | Matching text exists in data or legacy prose | A minimal valid example, requiredness, or equal semantics |
| `schema: none` | No general validator-backed Schema is recorded | That the loader performs no validation |

The generator reads only tracked paths returned by `git ls-files` and pins coverage at
190/275/306. Count changes must accompany registry/parser changes and a generated diff. Never edit
the generated inventories or generated reference pages by hand.


## Validation example: sling-ready ammunition

Direct staff-sling launching uses the `SLING_LAUNCHER` flag. Compatible ammunition must have `SLING_AMMO` and a `transform` use action with a specific target. The six existing sling-ready grenades and Molotov cocktails retain their item IDs and manual activation rules. Wield the sling and use the fire action to retrieve one carried round; choose first when multiple ammunition types are available. Cancelling targeting does not retrieve ammunition, ignite a fuse, or spend moves.

After confirmation, the existing transformation handles ignition resources, damaged-item activation failures, and the fuse. Only the requirement to wield the ammunition is waived for launching. Already active rounds, ammunition on the ground or carried by someone else, and rounds inside magazines or sealed pockets cannot be launched directly. The cost is 200 preparation moves plus the existing throwing and retrieval costs; Molotov cocktails retain their additional ignition cost.

`STOP_ON_CONTACT` applies only to direct launches. The projectile falls at the first above-water creature or impassable obstacle on its actual trajectory. Projectile hit checks still determine impact damage; avoiding damage does not let the round pass through to the rear rank. Grenades detonate as dropped active items when their original fuse expires, without copying immediate ammunition explosion effects. Molotov cocktails retain ignition on impact. Ordinary hand throwing does not add this flag.

Validation should cover native data loading, single-round consumption, cancellation and missing ignition resources, walls and intervening creatures, timed detonation, and manual activation. Sources are `src/sling.cpp`, `src/ballistics.cpp`, and `src/ranged.cpp`; regressions are in `tests/staff_sling_test.cpp`. Generated inventories remain tied to the final merged CCB source; refresh the companion documentation against that commit before merging it.
