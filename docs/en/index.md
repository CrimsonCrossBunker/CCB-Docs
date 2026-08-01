---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB Developer Documentation
language: en
status: active
doc_type: explanation
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
review_interval_days: 180
last_human_reviewer: LYHGLYTX
source_paths:
- AGENTS.md
- GOVERNANCE.md
source_symbols: []
source_queries:
- Sources of truth
- Authority model
source_fingerprint: d27dfc345f1f62196b482536e828d7781fbdc467c68ce6d109f8d289f2921adb
authority: docs-explanation
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 38a37cdddd129271ed9a5484f0b0da50d20558876d983fe7eefb471397dcd0af
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/9d8f26582da0f53ca1e29f8f072aeef43955655b
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/AGENTS.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/9d8f26582da0f53ca1e29f8f072aeef43955655b/GOVERNANCE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28home%29%3A+&body=Document+ID%3A+home%0ALanguage%3A+en%0AVerified+commit%3A+9d8f26582da0f53ca1e29f8f072aeef43955655b%0A%0ADescribe+the+documentation+problem%3A%0A
---

# CCB Developer Documentation

This is the formal developer explanation, tutorial, architecture, and
navigation site for Cataclysm: Cleanwater Bomb.

!!! info "Phase 0/1 foundation"
    This release publishes the home page and four complete bilingual example
    topics. The source repository's 175 tracked Markdown files are classified
    in the migration inventory; pages selected for migration do not enter the
    production navigation until their bilingual pair is complete.

## Know the authority boundary first

- Runtime behaviour comes from CCB source and tests.
- JSON, Lua, and API contracts come from schemas, LuaLS declarations,
  registrations, and generated inventories.
- Build and validation behaviour comes from CI, CMake, Makefile, Gradle, and
  repository validators.
- Contribution policy comes from the source repository's `AGENTS.md`,
  `CONTRIBUTING.md`, and `GOVERNANCE.md`.
- This site organizes those facts for learning, reference, and agent routing.

When this site conflicts with a contract, the page must be marked stale and
repaired. The site does not override the contract.

## Choose a route

- [First contribution](getting-started/first-contribution.md): the shortest
  route from locating a change to opening a pull request.
- [Project map](architecture/project-map.md): find source, rules, and tests by
  subsystem.
- [Responsible human](contributing/responsible-human.md): understand
  responsibility for AI-assisted contributions.
- [Build and validation](validation/quickstart.md): choose the smallest
  sufficient validation commands.

The CCB player website and CCB-GUIDE remain separate: the website is the
concise player entry point, while CCB-GUIDE queries game data.
