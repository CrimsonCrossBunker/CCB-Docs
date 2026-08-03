---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.shaders
title: SDL3 shaders
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- tools/build_shaders.py
- .github/actions/build-sdl3-shaders/action.yml
- src/cata_shader.cpp
- data/shaders/nightvision.frag
source_symbols:
- shader::load_fragment
source_queries:
- spv,dxil,msl
source_fingerprint: 50e239f54b8be3024a35dbc60dbec52870146f8f4f0e4f7b8dd0734f4e369f90
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6616d6bb941cc68640f4b48bfc40e9fbf57fd2aae91e0274f24bbdca417869d7
prerequisites:
- platforms.ui
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-shaders
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/shaders/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/shaders/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/shaders/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/shaders/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: tools/build_shaders.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tools/build_shaders.py
- path: .github/actions/build-sdl3-shaders/action.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/actions/build-sdl3-shaders/action.yml
- path: src/cata_shader.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/cata_shader.cpp
- path: data/shaders/nightvision.frag
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/data/shaders/nightvision.frag
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.shaders%29%3A+&body=Document+ID%3A+resources.shaders%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# SDL3 shaders

SDL3 tiles builds compile GLSL sources to backend-specific artifacts before packaging. At
runtime CCB selects SPIR-V for Vulkan, DXIL for D3D12, or MSL for Metal according to the GPU
formats reported by SDL.

## Authoritative pipeline

- Human-maintained sources are `data/shaders/*.frag` and `*.vert`.
- `tools/build_shaders.py` invokes `glslangValidator` and SDL_shadercross.
- `.github/actions/build-sdl3-shaders/action.yml` pins/builds the toolchain and uploads artifacts.
- Make/CMake/MSVC rules consume the artifacts; `src/cata_shader.*` selects and owns them at runtime.

The explicit generator interface is:

```sh
python3 tools/build_shaders.py --shader-dir data/shaders --formats spv,dxil,msl
```

It requires external compilers. A command that failed because those tools are absent is not a
shader validation pass.

## Generated boundary

`.spv`, `.dxil`, `.msl`, and build-stamp files are generated artifacts. Change GLSL or the
generator, then regenerate; do not hand-edit binaries. Keep large/generated outputs in CI or
release artifacts unless the main repository's generated-file policy explicitly tracks them.

## Runtime invariants

Artifact basename/stage matches the GLSL source; uniform/sampler counts match runtime creation;
at least one shipped format matches the active GPU; missing/invalid artifacts fail with useful
logs; renderer recovery releases and recreates shader/render-state resources safely.

## Validation

Compile every requested format, preserve generator logs, run the SDL3 shader CI lane, launch on
representative Vulkan/D3D12/Metal backends, exercise each visual variant and renderer recovery,
and compare a controlled screenshot. SDL2 does not validate this pipeline.

## Performance and compatibility

Avoid compiling at runtime and avoid rebuilding render state per draw. Changing uniforms,
bindings, or backend preference is an API-like renderer change and requires all three artifact
formats plus fallback/error-path evidence.
