---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: governance.security-license
title: Security, licensing, and provenance
language: en
status: active
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
source_fingerprint: 7cf4f8f2dfa74210240f7fd70014606f14a4aad2ba4e021a825d2c5bd5acf68b
authority: governance
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/governance/security-license/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/governance/security-license/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/governance/security-license/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/governance/security-license/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: SECURITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/SECURITY.md
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CONTRIBUTING.md
- path: LICENSE.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/LICENSE.txt
- path: OWNERSHIP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/OWNERSHIP.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28governance.security-license%29%3A+&body=Document+ID%3A+governance.security-license%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
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
