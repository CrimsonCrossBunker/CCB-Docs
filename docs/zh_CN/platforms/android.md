---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.android
title: Android 开发
language: zh_CN
status: draft
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- android/AGENTS.md
- android/app/build.gradle
- android/app/jni/CMakeLists.txt
- android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidHudModel.java
- .github/workflows/release-android-bundle.yaml
source_symbols:
- final class AndroidHudModel
source_queries:
- assembleDebug
source_fingerprint: abbe9136186f394a8ed5593fa4e3dd70e18ce3cf1ad53ea999973c7e90df1e3d
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8d05bff99c389df2c85486565e015a054a5ea64cd84279790224aa9d7bd3575f
prerequisites:
- platforms.matrix
- build.overview
depends_on:
- platforms.ui
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- android-unit
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-android
risk_level: high
pending_source_pr: null
stale_reason: null
search:
  exclude: true
---

# Android 开发

Android 由 Gradle application 与 native CMake build 组成，使用 SDL3、按 ABI 的 native
artifact、Java Activity/HUD 集成、Android resource、打包游戏数据，以及不同 debug/
release signing 路径。

## 权威入口

- `android/gradlew`、`android/app/build.gradle`、`android/app/jni/CMakeLists.txt` 定义
  本地 application/native build；
- `android/app/src/main/AndroidManifest.xml` 与 Java source 定义 application/UI bridge；
- `.github/workflows/matrix.yml` 包含当前 build-only Android CI lane；
- `.github/workflows/release-android-bundle.yaml` 定义 release bundle 与 signing。

## 先运行最窄验证

在 `android/` 使用 wrapper，并把 SDK/NDK 配置留在 Git 外：

```sh
./gradlew test
./gradlew assembleDebug
```

第一条覆盖 Android HUD model/geometry/schema 等 JVM unit test。APK assemble 还需要配置
SDK/NDK，并复制 native/game asset。报告 variant、ABI、SDK/NDK、Gradle/Java、SDL、安装
设备与安装结果。

## 运行时边界

Java 拥有 Activity lifecycle、storage path、Android HUD/editor/dialog，并通过定义 bridge
调用 native；native 拥有游戏 runtime。保持 pause/resume、surface/renderer recreation、
text input、touch coordinate、storage permission 和 desktop/Android 行为边界。

## 打包与安全

不要提交 `local.properties`、SDK path、keystore、password、签名 APK/AAB、Gradle state 或
生成 native library。CI release signing 使用 secret，只暴露预期 bundle/artifact。debug
安装不能验证 release signing 或商店交付。

## 失败证据

收集 commit、variant/ABI、device/API level、准确 Gradle task、首个 Gradle/CMake error 和
聚焦 `logcat` crash 段。区分 Java exception、native tombstone、renderer recovery、asset
copy、install/signature 与 storage-path 故障。
