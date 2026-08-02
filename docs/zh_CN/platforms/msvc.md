---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.msvc
title: MSVC 与 vcpkg
language: zh_CN
status: active
doc_type: how-to
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
- CMakePresets.json
- build-scripts/MSVC.cmake
- build-scripts/windows-tiles-sounds-x64-msvc.cmake
- .github/workflows/msvc-full-features.yml
source_symbols: []
source_queries:
- windows-tiles-sounds-x64-msvc
source_fingerprint: d2dbe858dd29b80612d853044debd594adb8e0ffeaf9d473becbc5dd3d2b0d74
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: de436d260762856faafc61fcc6f466c2b2e07c1d6c8db41648cec2681eda5411
prerequisites:
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
risk_group: platforms-windows
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msvc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msvc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: build-scripts/MSVC.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/MSVC.cmake
- path: build-scripts/windows-tiles-sounds-x64-msvc.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/windows-tiles-sounds-x64-msvc.cmake
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msvc%29%3A+&body=Document+ID%3A+platforms.msvc%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# MSVC 与 vcpkg

MSVC lane 使用 Visual Studio 2022、静态 vcpkg 依赖、仓库 toolchain file，以及明确的
multi-configuration CMake 或受维护 `msvc-full-features` solution。

## CMake preset 路径

在 Visual Studio developer environment 中，让 `VCPKG_ROOT` 指向有效 checkout：

```powershell
cmake --preset windows-tiles-sounds-x64-msvc
cmake --build --preset windows-tiles-sounds-x64-msvc
ctest --preset windows-tiles-sounds-x64-msvc
```

`build-scripts/MSVC.cmake`、`build-scripts/windows-tiles-sounds-x64-msvc.cmake`、vcpkg
manifest/triplet 与 `CMakePresets.json` 共同定义路径。较小的 `windows-x64-msvc` 覆盖
curses/test 配置。

## CI 对齐

`.github/workflows/msvc-full-features.yml` 是默认 Windows CI lane 的权威，包括 Visual
Studio 版本、vcpkg commit/triplet、translation artifact、ccache wrapper、solution target
和 test invocation。使用不同依赖 revision 的本地通过有参考价值，但不等于 CI parity。

## Feature 与 configuration 边界

`Release`、`Debug`、`RelWithDebInfo` artifact 要分开。说明 `UseSDL3` 为 true/false；同一
project 可构建不同 SDL2/SDL3 release package。PDB 必须与发生 crash 的准确 binary 与
commit 匹配。

## 验证与卫生

同一 architecture 执行 configure、build、test 与 package smoke test。不要提交 vcpkg
tree、受维护项目之外的生成 solution、`.vs`、PDB、本地 preset 或签名材料。保留首个
compiler/linker error 与 vcpkg log。
