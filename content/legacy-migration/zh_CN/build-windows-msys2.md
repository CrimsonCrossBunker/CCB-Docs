## 当前 MSYS2 路线

旧文档仍指向 CleverRaven clone、旧 Windows 版本和一条冻结的 pacman 包清单。CCB
贡献者应从 CCB fork 工作，并以当前 MSYS2、Make/CMake 配置和 Windows CI 为准。

### 选择 shell 与 toolchain

在现代 Windows 上使用与已安装包前缀一致的 64 位 MinGW/UCRT shell。不要在普通
MSYS shell、MINGW64 与 UCRT64 之间混装 toolchain。先完整更新 MSYS2，再按当前
Makefile/CMake、缺失 header 的首条错误和 CI 依赖安装包；不要长期复制本文中的版本号。

### CMake preset

固定来源提供：

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

Tiles/sound 组合使用 `windows-tiles-sounds-x64`。preset 采用 Ninja Multi-Config，
输出位于 `out/build/<preset>/`；具体 config 与 install 目录以当前 preset 为准。

### Make 入口

Makefile 仍支持 `MSYS2=1` 与 `DYNAMIC_LINKING=1`，并根据 Tiles、sound、localization、
SDL2/SDL3 等开关选择依赖。不要从旧指南复制一条关闭 lint/test 的大命令作为默认验证。
先做目标构建，再按 `ai/test-matrix.yml` 运行格式、JSON 或 focused tests。

### 运行与提交证据

- 从同一 MSYS2 环境运行生成的程序，确认需要的 runtime DLL 能解析。
- 保存 shell 类型、compiler、CMake/Make、package 前缀和完整命令。
- Windows CI 是合并证据；Linux 或 WSL 构建不能替代原生 Windows 结果。
- 发布包由 release/packaging 流程生成，本地开发构建不能直接冒充官方制品。

MSYS2 包名和工具版本会变化；本文刻意不固定完整安装命令。遇到差异时检查当前 CI 和
MSYS2 官方包数据库。
