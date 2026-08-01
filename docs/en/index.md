---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: home
title: CCB Developer Documentation
language: en
status: draft
source_paths:
- AGENTS.md
- GOVERNANCE.md
authority: docs-explanation
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: project-context
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
---

# CCB Developer Documentation

This is the formal developer explanation, tutorial, architecture, and
navigation site for Cataclysm: Cleanwater Bomb.

!!! warning "Phase 0/1 draft"
    These demonstration pages depend on CCB source pull request #551. They
    become active only after human review, source merge, and refresh to the
    final commit.

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
