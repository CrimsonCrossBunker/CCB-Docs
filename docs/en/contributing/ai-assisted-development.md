---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.ai-assisted-development
title: AI-assisted development
language: en
status: active
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
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
source_queries: []
source_fingerprint: 10ff7889c4f1dc39e9419cdd01036cd6507b47d017dba51d3cd58161725d41d0
authority: governance
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 89bb9e5d9c1ed291a5f8279742a98a4dd5dc42fb68eb643852b07b38b066ff0c
prerequisites:
- contributing.responsible-human
depends_on:
- contributing.documentation-policy
redirect_from: []
supersedes: []
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/ai-assisted-development/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/ai-assisted-development/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/ai-assisted-development/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/ai-assisted-development/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CONTRIBUTING.md
- path: GOVERNANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/GOVERNANCE.md
- path: .github/pull_request_template.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/pull_request_template.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.ai-assisted-development%29%3A+&body=Document+ID%3A+contributing.ai-assisted-development%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# AI-assisted development

CCB accepts AI-assisted work, but it reviews the resulting change, evidence,
and human accountability—not the confidence of a tool's explanation. Naming
the tool or model is optional.

## The Responsible human remains responsible

Every pull request names a Responsible human. That person must understand the
change, review the final diff, own the reported test results, verify licensing
and external provenance, and answer review questions. A generated patch that
the Responsible human cannot explain is not ready for review.

## Safe workflow

1. Read the root and nearest nested `AGENTS.md` before editing.
2. Inspect source, tests, registrations, schemas, and generated boundaries.
3. Give the tool a narrow task and explicit non-goals, especially compatibility
   and runtime-behaviour boundaries.
4. Review every changed file and remove unrelated formatting, guessed paths,
   caches, machine paths, credentials, and generated-file edits.
5. Run the checks routed by `ai/test-matrix.yml`; report only commands that
   actually ran.
6. Complete the documentation-impact fields and link dependent docs PRs.

## Evidence standards

Do not publish invented APIs, paths, commands, test output, reviewers, or
licenses. Generated reference must trace to schemas, LuaLS declarations,
registrations, inventories, or tests. When evidence is unavailable, mark the
claim unverified or the page draft instead of filling the gap by inference.

AI systems and bots cannot approve their own PRs or satisfy the human-reviewer
requirement. Human review is a governance boundary, not a disclosure ritual.
