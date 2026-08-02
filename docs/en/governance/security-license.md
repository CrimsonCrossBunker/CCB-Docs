---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: governance.security-license
title: Security, licensing, and provenance
language: en
status: draft
doc_type: explanation
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
- SECURITY.md
- CONTRIBUTING.md
- LICENSE.txt
- OWNERSHIP.md
source_symbols: []
source_queries: []
source_fingerprint: 54ad33a73b00dd344983f3662e67b76268c2d9d02741dd024f426b2f44d9b7ad
authority: governance
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6bc4417f2dbe99f4e09be3de5e30824afdd1c6b4208bc3ed43c8c25ca96dcc91
prerequisites:
- contributing.responsible-human
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: governance
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# Security, licensing, and provenance

Security reports that could expose data, execute untrusted code, compromise
build or release infrastructure, leak credentials, or provide a practical
exploit must use CCB's private vulnerability-reporting channel. Do not disclose
an exploitable report in a public issue.

## Prepare a private report

Include the affected version, commit, platform, threat model, prerequisites,
impact, minimal reproduction, and redacted logs. Do not send credentials. If a
credential may have leaked, rotate it rather than relying on deletion from Git
history.

Ordinary crashes and gameplay bugs without security impact use the normal bug
form. Third-party mods and unofficial packages normally belong to their owner,
but report any CCB integration boundary clearly.

## License and attribution review

- Identify the license of every imported code, document, image, sound, font,
  tile, or generated dataset before copying it.
- Record source repository/URL, exact commit or version, original contributors,
  modifications, and required notices.
- Preserve compatible notices and commit attribution. A public URL is not a
  license, and AI-generated text does not erase training or supplied-source
  provenance obligations.
- Do not publish anomalous contributor strings from automated history parsing;
  quarantine them for human review.

CCB's repository license files and per-asset notices are authoritative for the
material they cover. A Responsible human owns the final provenance and license
claim in each pull request.

## Privileged changes

Workflow permissions, release signing, Pages deployment, security settings,
and branch rules require least privilege and human review. Bots cannot approve
their own changes. Repository settings are not considered enabled merely
because a target YAML file was committed.
