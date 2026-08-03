---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.android
title: Android development
language: en
status: active
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
source_fingerprint: 2f89f749f203c15dc2918c940f0c1923bfe566f0eaaa848b2709462f8ef74065
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/android/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/android/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/android/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/android/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: android/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/android/AGENTS.md
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/android/app/build.gradle
- path: android/app/jni/CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/android/app/jni/CMakeLists.txt
- path: android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidHudModel.java
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/android/app/src/main/java/com/crimsoncrossbunker/cataclysmcb/AndroidHudModel.java
- path: .github/workflows/release-android-bundle.yaml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/release-android-bundle.yaml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.android%29%3A+&body=Document+ID%3A+platforms.android%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Android development

Android is a Gradle application plus a native CMake build. It uses SDL3, ABI-specific native
artifacts, Java activity/HUD integration, Android resources, packaged game data, and distinct
debug/release signing paths.

## Authoritative entry points

- `android/gradlew`, `android/app/build.gradle`, and `android/app/jni/CMakeLists.txt` define the
  local application and native build.
- `android/app/src/main/AndroidManifest.xml` and Java sources define the application/UI bridge.
- `.github/workflows/matrix.yml` contains the current build-only Android CI lane.
- `.github/workflows/release-android-bundle.yaml` defines release bundle and signing behavior.

## Narrow validation first

From `android/`, use the wrapper and keep the SDK/NDK configuration outside Git:

```sh
./gradlew test
./gradlew assembleDebug
```

The first command exercises JVM unit tests such as the Android HUD model/geometry/schema tests.
APK assembly additionally requires a configured SDK/NDK and copies native/game assets. Report
variant, ABI, SDK/NDK, Gradle/Java versions, SDL version, install device, and install result.

## Runtime boundaries

Java owns Activity lifecycle, storage paths, Android HUD/editor/dialogs, and calls into the
native layer through the defined bridge. Native code owns the game runtime. Preserve pause/
resume, surface/renderer recreation, text input, touch coordinates, storage permission, and
desktop/Android behavior boundaries.

## Packaging and security

Never commit `local.properties`, SDK paths, keystores, passwords, signed APK/AAB files, Gradle
state, or generated native libraries. CI release signing uses secrets and should expose only the
intended bundle/artifacts. Debug installs do not validate release signing or store delivery.

## Failure evidence

Capture commit, variant/ABI, device/API level, exact Gradle task, the first Gradle/CMake error,
and a focused `logcat` crash section. Distinguish Java exception, native tombstone, renderer
recovery, asset-copy, install/signature, and storage-path failures.
