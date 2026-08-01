---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.shaders
title: SDL3 shader
language: zh_CN
status: draft
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
include_in_search: false
include_in_ai_index: false
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/resources/shaders/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.shaders%29%3A+&body=Document+ID%3A+resources.shaders%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# SDL3 shader

SDL3 tiles build 在 packaging 前把 GLSL source 编译为 backend-specific artifact；运行时
CCB 按 SDL 报告 GPU format 选择 Vulkan 的 SPIR-V、D3D12 的 DXIL 或 Metal 的 MSL。

## 权威 pipeline

- 人工维护 source 是 `data/shaders/*.frag` 与 `*.vert`；
- `tools/build_shaders.py` 调用 `glslangValidator` 与 SDL_shadercross；
- `.github/actions/build-sdl3-shaders/action.yml` 固定/构建 toolchain 并上传 artifact；
- Make/CMake/MSVC rule 消费 artifact，`src/cata_shader.*` 在运行时选择并拥有它们。

显式 generator 接口为：

```sh
python3 tools/build_shaders.py --shader-dir data/shaders --formats spv,dxil,msl
```

它需要外部 compiler。因工具缺失而失败的命令不能算 shader 验证通过。

## 生成边界

`.spv`、`.dxil`、`.msl` 与 build-stamp 是 generated artifact。修改 GLSL/generator 后
重新生成，不手改 binary。除非主仓库 generated-file policy 明确跟踪，否则大型生成输出
保留在 CI/release artifact。

## 运行时不变量

artifact basename/stage 与 GLSL 匹配；uniform/sampler count 与 runtime creation 匹配；
至少一个 shipped format 适配 active GPU；缺失/无效 artifact 提供有用 log；renderer
recovery 安全释放并重建 shader/render-state resource。

## 验证

编译所有请求 format、保留 generator log、运行 SDL3 shader CI lane，在代表性 Vulkan/
D3D12/Metal backend 启动，覆盖各视觉 variant 与 renderer recovery，并比较受控 screenshot。
SDL2 不能验证本 pipeline。

## 性能与兼容

避免 runtime compile 和每次 draw 重建 render state。uniform、binding 或 backend preference
变化属于类似 API 的 renderer 变化，需要三个 artifact format 和 fallback/error-path 证据。
