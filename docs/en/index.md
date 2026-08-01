---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB Developer Documentation
language: en
status: active
source_paths:
- AGENTS.md
- GOVERNANCE.md
authority: docs-explanation
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
risk_group: project-context
risk_level: normal
pending_source_pr: null
stale_reason: null
---

# CCB Developer Documentation

This is the formal developer explanation, tutorial, architecture, and
navigation site for Cataclysm: Cleanwater Bomb.

!!! info "Phase 0/1 foundation"
    This release publishes the home page and four complete bilingual example
    topics. The remaining 175 first-party Markdown documents stay staged in
    the migration inventory; incomplete bilingual pages do not enter the
    production navigation.

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
