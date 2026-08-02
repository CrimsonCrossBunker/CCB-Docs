---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.releases
title: 发布操作
language: zh_CN
status: active
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: Pending human review
source_paths:
- .github/workflows/release.yml
- .github/workflows/release-android-bundle.yaml
- doc/RELEASE_PROCESS.md
- build-scripts/generate-release-notes.js
source_symbols: []
source_queries:
- workflow_dispatch
source_fingerprint: 9b2686c6179dcc7fd3710b82931aa8b4061b7911ee1a4c4b670d0e265034702c
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 968e8122bf55cc278a9f3c5c45d8fbeedfea0f436185c719787a5f53e02533fc
prerequisites:
- operations.packaging
depends_on:
- maintenance.releases
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: release
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/operations/releases/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/releases/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/releases/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/releases/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/release.yml
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/release-android-bundle.yaml
- path: doc/RELEASE_PROCESS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/RELEASE_PROCESS.md
- path: build-scripts/generate-release-notes.js
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/build-scripts/generate-release-notes.js
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.releases%29%3A+&body=Document+ID%3A+operations.releases%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 发布操作

CCB experimental release workflow 由 `master` 相关 push 触发，也支持手工 dispatch。它创建
带时间戳 prerelease metadata、根据 Git history 生成 release note、创建 GitHub release，
再协调 translation、tileset、shader、desktop package 与 Android bundle 等 artifact。

## 权威与顺序

`.github/workflows/release.yml` 与 `.github/workflows/release-android-bundle.yaml` 定义实际
job、permission、dependency、artifact name 与 trigger；`doc/RELEASE_PROCESS.md` 提供背景。
操作前始终检查 release commit 上的 workflow。

1. 确认 target commit 与默认分支 CI；
2. 确认 translation、shader/tile generation、version metadata 与平台 build input；
3. 只触发预期 workflow/event，不重跑无关旧 commit；
4. 监视每个 dependent job，保留 run URL/log；
5. 公告前比较 release target SHA、notes range、tag、checksum、artifact set、signature 与
   smoke test。

## 失败处理

GitHub release 已创建不能证明所有 artifact 成功。下游失败时准确说明缺失/被替代 artifact；
通过 PR 修 workflow/input 后有意重跑。不能在可信 release name 下上传临时本地替代品。

## 安全与权限

release token/signing material 只留 GitHub secret/protected environment。workflow、permission、
signing 与 destination 变化需人类审查。当前宽 permission 是安全审查目标；在 setting 与
workflow scope 证明前，文档不能声称已实现 least privilege。

## 记录与回退

保留 release commit、tag、run ID、artifact checksum、toolchain/dependency revision、signing
identity、Responsible human、known issue 与 supersession/rollback 决定。优先发布修正/替代
release，不静默替换 artifact。

## 验证

从 published artifact 对每个平台 smoke-test，验证 data、Mod、Lua、translation、graphics/
audio、save/load 与 upgrade。归档匹配 symbol 及诊断该准确 release 所需 docs/API snapshot。
