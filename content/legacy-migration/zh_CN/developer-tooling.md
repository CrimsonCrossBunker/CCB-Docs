## 当前 CCB 开发工具链

工具选择由修改类型决定，不要求每个贡献者安装整套静态分析栈。最小开发循环是：定位受
影响源码/测试、配置一个可复现 build、编译最小目标、运行 focused validation、检查 diff。
clang-tidy、IWYU、clangd、ctags 和 profiler 属于按需层。

### compilation database 与编辑器

用当前 CMake 配置生成 `compile_commands.json`：

```sh
cmake -S . -B build -DCMAKE_EXPORT_COMPILE_COMMANDS=ON
cmake --build build -j2
```

具体 feature flags 应与要审阅的平台/CI job 一致。让 clangd 指向 build 内的 database；
不要提交 `compile_commands.json`、clangd index、ctags、Doxygen HTML 或大型 symbol database。
它们可以作为本地缓存或 CI artifact。

### clang-tidy

`.clang-tidy` 与 `tools/clang-tidy-plugin` 定义 CCB checks，CI 由
`.github/workflows/clang-tidy.yml` 和 `build-scripts/clang-tidy-run.sh` 驱动。脚本会创建
compilation database、定位直接/间接受影响 translation units，并要求构建的 Cata plugin。

本地只检查一个文件时也必须使用与 build 匹配的 database 和 plugin/wrapper；系统自带的
裸 clang-tidy 结果可能缺少 `cata-*` checks。自动 `-fix` 后逐项审阅，不能盲目接受跨文件
重写。

### include-what-you-use

`.github/workflows/iwyu.yml` 与 `build-scripts/ci-iwyu-run.py` 是当前 CI 入口。该脚本依赖
`files_changed`、affected-file 分析、`tools/iwyu/cata.imp` 和 blacklist；它明确面向 CI。
本地运行应按脚本头部的当前示例配置工具版本和 database，不能复制旧 LLVM/IWYU 安装指南。

IWYU 建议不是自动正确：平台 wrapper、template 实例化、associated header 和 keep pragma
都有专用规则。应用后必须重新编译受影响目标。

### formatter、索引与生成物

- C++：`make astyle-check`，修正时 `make astyle` 后检查完整 diff。
- JSON：使用仓库 formatter，再运行 loader/ID 检查。
- Python：只对相关 scripts/tests 运行仓库锁定的 lint/test。
- ctags/Doxygen：用于导航，不是 API 权威来源，也不提交输出。

所有工具命令以当前 CI、CMake、Makefile 和脚本为准。旧文档若指定固定 LLVM 版本、上游
仓库下载或过时 IDE 扩展，应视为历史材料而不是 CCB 要求。
