---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.upstream-math-compatibility
title: 'Draft: hunger and morale math compatibility'
language: en
status: draft
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- src/math_parser_diag.cpp
- tests/upstream_math_compat_test.cpp
source_symbols:
- hunger_eval
- hunger_ass
- morale_eval
source_queries:
- hunger
- morale
- raw
source_fingerprint: 63aa23636f78e390885922176617b76ce1872b96b4bf9d6ff98c47798b061ccf
authority: api-contract
verified_commit: e6d42fcd151236cc3b5824107986911b15969a65
verified_at: '2026-10-13'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3fb01cbe28214e221cb3ade36edc0e1b7b6b544b0a575b51083cd1908b2dbc4b
prerequisites:
- eoc.overview
depends_on:
- eoc.talkers
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; parser registrations, inventories, and tests remain authoritative.
example_validation_ids: []
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/995
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/upstream-math-compatibility/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/upstream-math-compatibility/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/eoc/upstream-math-compatibility/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/eoc/upstream-math-compatibility/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/e6d42fcd151236cc3b5824107986911b15969a65
source_urls:
- path: src/math_parser_diag.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/e6d42fcd151236cc3b5824107986911b15969a65/src/math_parser_diag.cpp
- path: tests/upstream_math_compat_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/e6d42fcd151236cc3b5824107986911b15969a65/tests/upstream_math_compat_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.upstream-math-compatibility%29%3A+&body=Document+ID%3A+eoc.upstream-math-compatibility%0ALanguage%3A+en%0AVerified+commit%3A+e6d42fcd151236cc3b5824107986911b15969a65%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: hunger and morale math compatibility

This page accompanies unmerged CCB PR #995 and its source and focused regressions. The complete synchronization data needs these registrations. The page remains a draft outside production search and AI indexes.

`u_hunger()` and `n_hunger()` read the corresponding Character's hunger. Assignment calls native `Character::set_hunger` using integer values. Assignment to a non-Character fails. Legacy `val('hunger')` reads remain supported.

`u_morale()` and `n_morale()` read morale using CCB's existing rules. The `raw` keyword is accepted and both values follow that same CCB rule. Legacy `val('morale')` reads remain supported. This port does not restore additional upstream morale penalties.

The native talker implementation of morale assignment has no behavioral proof from these regressions. To change morale, inspect existing supported morale effects or Lua Platform v1 services. This evidence covers morale reads and does not prove assignments take effect.

Acceptance reused the matching SDL3 Release engine cache and rebuilt the affected source and tests. Two tests and twenty assertions passed with seed 20261013: player/NPC reads, hunger assignment, legacy reads, non-Character rejection and a real negative-morale fixture. This does not establish a full native batch rebuild, old-save or all-platform acceptance.

Adapted from CDDA #88622 (RenechCDDA) and #88818 (Anton Simakov), retaining authors and source SHAs in source commits. Lua Platform v1 remains the sole CCB Lua runtime. Native math registrations do not add another Lua runtime. Responsible human: LYHGLYTX.
