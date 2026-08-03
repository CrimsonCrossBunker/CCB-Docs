---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build-devcontainer
title: 'Legacy migration draft: devcontainer'
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
review_interval_days: 365
last_human_reviewer: Pending human review
source_paths:
- doc/c++/COMPILING-DEVCONTAINER.md
- .devcontainer/devcontainer.json
- .devcontainer/Dockerfile
- .devcontainer/graphical/devcontainer.json
- .devcontainer/cross-compile/devcontainer.json
source_symbols: []
source_queries: []
source_fingerprint: 8f68c334544cfd8d659189c98b595176526138bcc7ce376643893903767ec072
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b8c25f3ab0ba0a1494b2fd6ba162548e3d85474a1a7f6b2bc1a300248124da1e
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/devcontainer/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/devcontainer/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/devcontainer/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/devcontainer/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/c++/COMPILING-DEVCONTAINER.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c++/COMPILING-DEVCONTAINER.md
- path: .devcontainer/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.devcontainer/devcontainer.json
- path: .devcontainer/Dockerfile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.devcontainer/Dockerfile
- path: .devcontainer/graphical/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.devcontainer/graphical/devcontainer.json
- path: .devcontainer/cross-compile/devcontainer.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.devcontainer/cross-compile/devcontainer.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build-devcontainer%29%3A+&body=Document+ID%3A+build-devcontainer%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: devcontainer

This is the migration draft page for `build-devcontainer`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `build-devcontainer`
- Target: `build/devcontainer.md`
- Replacement: build-devcontainer
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| build-devcontainer | doc/c++/COMPILING-DEVCONTAINER.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current Dev Container workflow

The pinned source contains three separate configurations: `Standard` at the root,
`Standard + Qt5` under `graphical/`, and `Cross-Compile w32` under `cross-compile/`.
Select the intended configuration file; do not follow the old guide's procedure of
commenting and uncommenting large sections of one shared Dockerfile.

### Prerequisites

- an editor with Dev Containers support (the checked configuration primarily targets the
  VS Code extension);
- Docker or a compatible container runtime;
- a cloned CCB fork and a dedicated branch;
- enough image, dependency, and build storage.

Open the repository, select the relevant `.devcontainer/.../devcontainer.json`, and run
“Reopen in Container”. The initial image build can take time. Preserve the build log and
the failing layer instead of repeatedly deleting all Docker data.

### Build inside the container

Use authoritative repository entry points after the container opens, for example:

```sh
make -j2
make -j2 tests
```

Repository CMake presets are also available. Run from the mounted repository root; Make or
CMake determines artifact locations. Graphical execution additionally depends on host
display, GPU or software rendering, and audio forwarding. A successful container compile
does not prove that the graphical binary starts on the host.

### Cross-compilation boundary

Use the dedicated `cross-compile` configuration for a Windows cross-build. It proves the
cross toolchain and target artifact, but does not replace Windows MSYS2/MSVC CI, runtime
DLL checks, or an actual Windows launch.

### Security and reproducibility

- Review Dockerfiles, features, mounts, ports, and host sockets before building.
- Never bake tokens, SSH private keys, signing material, or personal configuration into an
  image.
- When `.devcontainer/` changes, rebuild each affected configuration and record the host
  and runtime versions.
- Current JSON, Dockerfiles, and CI win over conflicting prose.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `8f68c334544cfd8d659189c98b595176526138bcc7ce376643893903767ec072`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/COMPILING-DEVCONTAINER.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/COMPILING-DEVCONTAINER.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/c%2B%2B/COMPILING-DEVCONTAINER.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
