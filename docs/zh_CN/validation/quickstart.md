---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: validation.quickstart
title: 验证快速入门
language: zh_CN
status: active
doc_type: how-to
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
- AGENTS.md
- ai/test-matrix.yml
- Makefile
- CMakePresets.json
- android/gradlew
source_symbols: []
source_queries:
- Basic discovery and validation
- 'kind: test_matrix'
source_fingerprint: 900c3cc35f171c4bd297e703e5442b63b64871988f1284b600fca952afe88b1f
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7bbe452f2a9397eac25ccbfb804f71d0a081288915bb3900ef5f2c0fcb9f4114
prerequisites:
- architecture.project-map
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- cpp-format
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/validation/quickstart/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/validation/quickstart/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/validation/quickstart/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/validation/quickstart/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/AGENTS.md
- path: ai/test-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/ai/test-matrix.yml
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: android/gradlew
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/android/gradlew
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28validation.quickstart%29%3A+&body=Document+ID%3A+validation.quickstart%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 构建与验证快速入口

验证命令以 CCB 主仓库的 CI、CMake、Makefile、Gradle 和脚本为准。本文只提供
选择入口；如果本文命令与构建文件冲突，应标记本文 stale 并按实际构建契约修复。

## 先选最小充分检查

| 修改区域 | 首选检查 | 说明 |
| --- | --- | --- |
| Agent/治理元数据 | `python3 tools/agent/check_project_metadata.py` | 再运行 `tools/agent` 单元测试 |
| C++ | `make astyle-check` | 行为变化还需聚焦 Catch2 测试 |
| C++ 测试 | `make -j2 tests` | 然后运行 `./tests/cata_test "过滤器"` |
| JSON | `make -j2 json-check` | 单文件同时运行仓库 JSON formatter |
| Lua 契约 | `check_luals_declarations.py` 与 `check_coverage.py` | Schema/注册/声明变化都要检查 |
| CMake | `cmake --preset linux-x64` | 使用仓库现有 preset |
| Android | `cd android && ./gradlew test` | 需要配置好的 Android SDK |

完整命令与路径映射位于 `ai/test-matrix.yml`。耗时检查或平台检查缺少依赖时，
明确说明跳过原因，不得声称已经通过。

## 记录验证结果

PR 中应记录：

1. 实际运行的完整命令；
2. 聚焦测试过滤器或测试名称；
3. 结果和必要的 RNG seed；
4. 未运行检查及原因；
5. 建议审阅者额外验证的场景。

文档影响检查在 Phase 0/1 只提示；它不会代替源码测试，也不会因为无关文档债务
阻止普通源码 PR。
