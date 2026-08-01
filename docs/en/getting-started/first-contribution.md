---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.first-contribution
title: First contribution
language: en
status: draft
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
authority: governance
verified_commit: 11748581a0df8651380cfb8ae37ae91baafe054d
verified_at: '2026-08-01'
generated: false
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
risk_group: governance
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/551
stale_reason: null
search:
  exclude: true
---

# First contribution

This route serves first-time CCB contributors and agents that need reliable
task context. The goal is not to understand the whole project first; it is to
finish one scoped, verifiable change.

## 1. Start from authoritative facts

Identify the subsystem, then read the root `AGENTS.md` and the nearest nested
`AGENTS.md` for the target path. Use `ai/project-map.yml` to locate entry points
and `ai/test-matrix.yml` to select validation.

Do not infer runtime behaviour only from an old issue, a search summary, or
this site's prose. Confirm it in source and tests.

## 2. Create an isolated branch

Start from current `master` and keep the branch focused on one problem. Do not
include local caches, build outputs, or unrelated changes. In particular, do
not scan, stage, or commit `obj-lua/`.

## 3. Make the smallest change and validate it

Before changing a public ID, schema, LuaLS declaration, registration, or build
interface, inspect callers, generation rules, and existing tests. Choose the
smallest sufficient checks from the
[validation quickstart](../validation/quickstart.md), and report only commands
that actually ran.

## 4. Complete the pull-request contract

Every pull request fills in:

- `Responsible human`: a real GitHub account;
- `Documentation impact`: none, an update, or a stale marker;
- `Related CCB-Docs PR`: use `None` when absent;
- `Affected documentation IDs`: stable catalog IDs;
- `Generated reference impact`: schema, LuaLS, registration, or inventory
  consequences.

Tool or model disclosure is optional, but responsibility cannot be delegated
to a tool. See [Responsible human](../contributing/responsible-human.md).

## 5. Coordinate cross-repository documentation

A docs pull request may be prepared before its source pull request merges, but
it remains draft and records the source pull request. After source merge,
refresh `verified_commit` to the final commit, regenerate catalog outputs, and
rerun validation before requesting human docs merge.

Completion means a reviewer can understand why the change exists, what it
does, how it was verified, and whether documentation or generated references
are affected.
