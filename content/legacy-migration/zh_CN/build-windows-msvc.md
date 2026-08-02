## 当前 MSVC 与 vcpkg 路线

CCB 的完整 MSVC 路线由 `msvc-full-features/` solution、vcpkg manifest/triplet、CMake
preset 和 `.github/workflows/msvc-full-features.yml` 共同定义。旧文档中的 CleverRaven
clone、任意最新 vcpkg 和旧 Visual Studio 版本不能替代这些固定契约。

### 推荐入口

安装 Visual Studio 2022 的 C++ desktop/game workload、Git、与项目兼容的 CMake 和
vcpkg。固定来源的 CI 使用 CMake 3.31.6，并把 vcpkg 固定到
`f6672d8e480ccdecddfad3fd1b838ba369ffe6cd`；本地改变版本时必须记录差异。

可选择两条路线：

1. 打开 `msvc-full-features/Cataclysm-vcpkg-static.sln`，使用 `Release`/`x64`；
2. 使用 `windows-x64-msvc` 或 `windows-tiles-sounds-x64-msvc` CMake preset。

CI 的核心 solution 构建命令是：

```powershell
msbuild -m -p:Configuration=Release -p:Platform=x64 -p:UseSDL3=false `
  "-target:Cataclysm-vcpkg-static;Cataclysm-test-vcpkg-static;JsonFormatter-vcpkg-static;zzip" `
  msvc-full-features/Cataclysm-vcpkg-static.sln
```

这是 CI 证据，不表示本文在本机 Windows 重新执行过该命令。

### 测试与运行

- 用与游戏相同的 configuration/platform 构建 test target。
- 从生成目录运行 focused Catch2 filter；Release 通常适合日常验证，Debug 留给需要
  iterator diagnostics 或逐步调试的情形。
- localization、Tiles、sound、SDL2/SDL3 与 static linking 会改变目标与依赖；PR 中
  写明组合。
- vcpkg 安装失败时先保存对应 buildtree log 和锁定 revision，不要直接升级到任意 HEAD。

本页不发布签名或分发步骤；发布与打包见[发布维护](../maintenance/releases.md)。
