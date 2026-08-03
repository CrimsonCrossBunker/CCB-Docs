---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.packaging
title: 打包
language: zh_CN
status: active
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- .github/workflows/release.yml
- .github/workflows/release-android-bundle.yaml
- build-scripts/windist.ps1
- Makefile
source_symbols: []
source_queries:
- Experimental Release
source_fingerprint: 9b918f82112a662be47c58bb3000b480f8061242242ffbe820c702729ba5f321
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a517c91c633dea4acc9e1d492c333d8f5be8b148ab981b63ac2b46b1d72db68b
prerequisites:
- platforms.matrix
- validation.testing
depends_on:
- resources.translation
- resources.tiles
- resources.fonts
- resources.sound
- resources.shaders
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/operations/packaging/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/packaging/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/packaging/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/packaging/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/release.yml
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/release-android-bundle.yaml
- path: build-scripts/windist.ps1
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/build-scripts/windist.ps1
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.packaging%29%3A+&body=Document+ID%3A+operations.packaging%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 打包

packaging 把 executable 与离开开发 checkout 运行所需的准确 data、graphics、translation、
shader、library、license、launcher/support file 和平台 metadata 组装起来。编译成功不等于
package 成功。

## 权威入口

使用当前 release workflow、`Makefile` install/package target、Gradle Android bundle task
和 `build-scripts/` 平台 helper。`build-scripts/windist.ps1` 拥有 Windows distribution
staging；Android Gradle 拥有 APK/AAB 内容；release job 拥有最终 artifact 名与上传。

## 可复现输入

记录 source commit/tag、toolchain/dependency revision、feature flag（curses/tiles、SDL2/SDL3、
sound、localization、Lua）、architecture/ABI、build type、translation artifact、shader artifact
与 asset source。不能从不干净开发目录随意捡文件打包。

## 平台检查

- Linux：检查 dynamic dependency/预期 static set、data path、executable bit、desktop/icon
  metadata 与 archive extraction；
- Windows：在无 developer `PATH` 环境测试，检查 DLL/PDB pairing 与 path case/encoding；
- Android：检查 variant/ABI、manifest、asset/native library、version code/name、signature、
  install/upgrade 与真机启动。

## Smoke test

解压/安装到干净位置，启动，创建/读取 world，验证 JSON/Mod loading、目标 build 的 Lua API、
translation、font、tiles、sound、shader variant、save/write path 与干净 shutdown；明确报告
每个有意省略 feature。

## 安全与许可证

signing key、password、service token 与 local certificate 留在 tracked file/log 外。包含所需
license/attribution 与 source/commit reference。对最终 artifact 扫描意外 credential/本地
path，不能只检查源码 checkout。

## Artifact 政策

除非 checked generated-file policy 明确规定，不提交 package、build directory、symbol 或
生成 shader/translation output。package 与匹配 symbol 作为 CI/release artifact 上传，并
记录 retention/restore。
