---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.wsl
title: WSL development
language: en
status: draft
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- Makefile
- CMakePresets.json
- doc/c++/COMPILING.md
source_symbols: []
source_queries:
- linux-x64
source_fingerprint: fbd977708b89bb26456c14aa37df1c21f9ca4170fe06454a11a30d7932dad2b0
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0a36c080292216c43bf7099099a3ef9650b42506f28e6cc3ead4c14cbaa6e1d9
prerequisites:
- platforms.linux
- platforms.windows
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-wsl
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/wsl/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/wsl/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/wsl/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/wsl/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakePresets.json
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/c++/COMPILING.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.wsl%29%3A+&body=Document+ID%3A+platforms.wsl%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# WSL development

WSL runs the Linux toolchain on a Windows host. It is useful for Linux builds and tests, but it
does not produce evidence for native MSVC/MinGW packaging, Windows DLL discovery, or the native
Windows console/input path.

## Choose the filesystem deliberately

Linux builds are usually faster and have more predictable permissions inside the WSL Linux
filesystem than under `/mnt/c`. Record whether the checkout and build directory live on the
Linux or mounted Windows filesystem; case sensitivity, executable bits, file watching, and path
translation can change the failure mode.

## Build route

Use the Linux contracts from `Makefile` or `CMakePresets.json`, not a Windows preset:

```sh
cmake --list-presets
cmake --preset linux-x64
cmake --build --preset linux-x64
```

For tiles, sound, or a launched game, separately document WSL version, graphics integration,
display/audio environment, GPU/driver path, and SDL version. A successful headless curses test
does not validate those layers.

## Validation boundary

Report Windows version, WSL version/distribution, filesystem location, compiler, preset/flags,
and whether the binary was only tested inside WSL. Validate line endings and executable bits in
Git, but do not add platform-generated files or local mount paths to the repository.

## Common failures

Slow metadata access on mounted drives, Windows tools accidentally first on `PATH`, CRLF shell
scripts, unavailable GUI/audio sockets, and memory limits need different fixes. Reproduce in a
native Linux CI lane when determining whether a failure is CCB code or WSL integration.
