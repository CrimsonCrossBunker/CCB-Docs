---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.sound
title: Sound and soundpacks
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/SOUNDPACKS.md
- src/sound_backend.h
- src/sdlsound.h
- src/sounds.h
- tests/sound_backend_test.cpp
source_symbols:
- namespace sounds
source_queries:
- soundpack
source_fingerprint: 9f1e5ea8a80d6091a01ff14d6ff874263d556de42bc5ea84ea11c76fda51ef24
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 42715b3663d7e72ab93813b14b8d1d37b2126d3889b073c471ed6d67477145c0
prerequisites:
- platforms.ui
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-sound
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/sound/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/sound/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/sound/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/sound/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: doc/SOUNDPACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/SOUNDPACKS.md
- path: src/sound_backend.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sound_backend.h
- path: src/sdlsound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sdlsound.h
- path: src/sounds.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/sounds.h
- path: tests/sound_backend_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/sound_backend_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.sound%29%3A+&body=Document+ID%3A+resources.sound%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Sound and soundpacks

CCB distinguishes gameplay sound events from audible sample playback. The `sounds` namespace
records simulation events for hearing, AI, and markers; the `sfx` and backend layers map IDs and
variants to files, playlists, channels, attenuation, and SDL playback.

## Authoritative paths

- `src/sounds.*` defines gameplay sound categories and event processing.
- `src/sound_backend.h` and SDL2/SDL3 backend implementations define device/sample behavior.
- `src/sdlsound.*` coordinates initialization, soundset loading, music, and shutdown.
- `doc/SOUNDPACKS.md` describes pack metadata and JSON; `data/sound/Menu_Sound_Test/` is a small
  checked example/fixture.

## IDs, variants, and ownership

Code/data emit a stable sound ID plus variant and context. A soundpack maps it to licensed audio
files. Gameplay events must still work when `SOUND` is disabled or device initialization fails;
audio playback cannot become simulation authority.

## Contributor workflow

Record original source, creator, license, edits, loop status, format, and attribution for every
sample. Normalize only through a documented process. Update mappings and fallback variants;
never hard-code an absolute local audio path.

## Validation

Validate soundpack JSON and referenced files, exact and fallback variants, playlists, loop/fade,
channel/group behavior, indoor/night/season choices, angle/volume, missing sample diagnostics,
device init failure, SDL2/SDL3, and a no-sound build. Use the sound backend tests where applicable.

## Performance and packaging

Preload policy, decoded sample size, simultaneous channels, and repeated variant resolution
affect memory and frame time. Package only distributable assets and preserve case-sensitive
paths. Large third-party soundpacks should remain independently distributed unless policy and
license explicitly allow bundling.

## CCB boundary

CCB may share historical IDs with upstream, but its emitted contexts and bundled mappings are
the contract. Validate a port against CCB events rather than assuming an upstream soundpack is
complete.
