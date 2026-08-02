---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintenance.upstream-sync
title: Upstream synchronization
language: en
status: active
doc_type: how-to
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- doc/development_process.md
source_symbols: []
source_queries: []
source_fingerprint: d5d7414ad8ce1f7b2c96ed84f49a05f3fdce63af9d065c7a906b1d55c165bbd1
authority: governance
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7879927db6623b701d64de6a3aec0cd3ecc14b6c0e248d648b7cd3cfdeffa842
prerequisites:
- getting-started.experienced-index
depends_on:
- compatibility.save
- compatibility.mods
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
risk_group: upstream
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintenance/upstream-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/maintenance/upstream-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/maintenance/upstream-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/maintenance/upstream-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/GOVERNANCE.md
- path: doc/development_process.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/development_process.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28maintenance.upstream-sync%29%3A+&body=Document+ID%3A+maintenance.upstream-sync%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Upstream synchronization

CCB shares history with other Cataclysm-family repositories but is not a mirror.
An upstream commit is evidence and source material, not authority over CCB
runtime behaviour.

## Record provenance before editing

- source repository, PR or issue, and exact commit range;
- original authors and applicable license;
- reason for the port and the CCB problem it addresses;
- files and behaviour intentionally omitted or rewritten;
- known CCB divergence and expected conflict areas.

Preserve attribution in commit messages and pull-request notes. Do not collapse
several upstream changes into an untraceable patch.

## Review the CCB boundaries

Compare registrations, data IDs, serialization, mod loading, EOC context, Lua
v5 public contracts, UI/input, desktop/Android configuration, and tests. Search
for later upstream fixes to the source change, but evaluate them separately.
Passing an upstream test suite does not establish CCB compatibility.

## Validate and document

Run the smallest CCB test that proves the intended behaviour, then expand for
shared core, save, data, API, or platform risk. Document intentional divergence
in code comments only where it prevents a future incorrect re-port; put the
full explanation in CCB-Docs and link the exact source.

A port is ready only when its source is auditable, the final CCB diff is
understood, compatibility impact is explicit, and a Responsible human owns the
result.
