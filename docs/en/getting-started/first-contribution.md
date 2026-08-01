---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: getting-started.first-contribution
title: First contribution
language: en
status: active
doc_type: tutorial
audiences:
- new-contributor
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- .github/pull_request_template.md
source_symbols: []
source_queries:
- Responsible human
source_fingerprint: 92bbc1c991b6ad674114072e80aa45f9cc05cb3bf47bc24c8b2dc4ab2dd10695
authority: governance
verified_commit: 9d8f26582da0f53ca1e29f8f072aeef43955655b
verified_at: '2026-08-01'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e1294cff2297b0bbc3d6164e822d1743655a127ae19259e4b4b0260fb4f1a730
prerequisites: []
depends_on:
- contributing.responsible-human
redirect_from: []
supersedes:
- getting-started.how-you-can-help
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: high
pending_source_pr: null
stale_reason: null
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
