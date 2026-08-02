## 支持范围由可执行证据定义

编译器支持不是永久版本表。固定 CCB commit 的 `CMakeLists.txt` 要求 C++17；真正受支持的组合由
默认分支 CI、构建脚本和维护者能够复现的发布工具链共同定义。旧页面中的发行版、Xcode 市占率和链接
会随时间失效，不能覆盖当前 workflow。

在本页验证的 source commit，General build matrix 覆盖：

- Ubuntu 上 clang 13 的基础 curses build/test；
- Ubuntu 上 clang 18 的 tiles + ASan；
- Ubuntu 上 GCC 9 的 curses/LTO 以及 tiles/sound/CMake/UBSan 组合；
- Ubuntu 上 GCC 14 的 curses 与 Lua API 组合；
- macOS 15 / Apple Clang 17 的 tiles、sound、SDL2；
- Android arm64 build-only；
- 独立 Windows workflow 在 windows-2022 上使用 MSVC、固定 CMake/vcpkg 和完整 tests。

这些条目描述该 commit 的 CI，不保证任意更旧或更新工具链，也不代表 build-only 平台已经运行测试。

## 修改与验证

选择最接近目标平台的 CMake preset、Make/Gradle 或 MSVC 入口，并记录 OS、arch、compiler、标准库、
generator、SDL、tiles、sound、localization、Lua、sanitizer 和 build type。Linux 成功不能替代 Windows、
macOS 或 Android；cross-compile 成功也不能证明目标平台启动、依赖打包和输入正常。

提高最低版本或使用新标准库功能前，先更新 matrix 让最旧与最新受支持工具链实际编译，再修改说明。
检查 release packaging、第三方依赖和缓存键，并在默认分支稳定成功后才把 check 设为 required。外部链接
只用于寻找工具，不构成支持承诺；CI job 和仓库配置才是证据。
