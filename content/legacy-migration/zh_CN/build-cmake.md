## 当前 CMake 路线

仓库的 `CMakePresets.json` 是 preset 名称、generator、输出目录和默认 feature 组合的
权威来源。旧文档中“CMake 非官方”、手工下载 SDL DLL 和 in-tree `build/` 的叙述已经
过时；CCB 当前 CI 会实际使用 CMake，但仍要求 out-of-tree 构建。

### 发现并配置

在仓库根目录先运行：

```sh
cmake --list-presets
cmake --preset linux-x64
```

`linux-x64`、`linux-tiles-sounds-x64`、Windows MSYS2 与 MSVC preset 均在固定来源
commit 的 `CMakePresets.json` 中。输出默认位于 `out/build/<preset>/`。如果本机列表
为空或缺少目标 preset，先检查平台、generator、toolchain 与 preset condition，不要
把旧文档中的命令直接拼到当前配置上。

### 构建和覆盖选项

```sh
cmake --build --preset linux-x64
```

临时覆盖使用 `-DNAME=VALUE`，但提交前必须确认该选项仍由 `CMakeLists.txt` 定义。
Tiles、sound、localization、Lua、SDL2/SDL3 与 sanitizer 会改变依赖和产物；记录实际
preset 和覆盖值。不要提交本机的 `CMakeUserPresets.json`、绝对路径、vcpkg 根目录或
生成的 build tree。

### 验证和故障定位

1. 保存 configure 的第一条错误，而不只保存最后的 build failure。
2. 核对 CMake、compiler、Ninja/MSBuild 与依赖版本。
3. 只删除明确的 `out/build/<preset>/` 构建目录；不要清理源码树或未跟踪文件。
4. 重新 configure，再构建受影响 target；涉及测试时运行对应 preset 产物中的 focused
   test。

`cmake --list-presets` 已在 Linux 对文档分支实际验证；Windows preset 的可用性与完整
编译由对应 Windows CI 证明，不能由 Linux 结果替代。总览见[构建 CCB](overview.md)，
平台差异见[平台矩阵](../platforms/matrix.md)。
