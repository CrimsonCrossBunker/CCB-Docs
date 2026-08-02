## 当前 CCB C++ 风格入口

CCB 的可执行风格契约是 `.astylerc`、`.clang-tidy`、Makefile target 与 CI，不是旧文档中
复制的一串 formatter 参数。工具版本或规则变化时应先更新配置和 CI，再由本文解释结果；
不要在编辑器里维护另一套近似规则。

### 提交前的最小流程

```sh
make astyle-check
git diff --check
```

`astyle-check` 是只读门禁，适合先确认差异。需要自动修正时可运行：

```sh
make astyle
```

`make astyle` 可能修改超出当前手工编辑范围的受管文件。运行后必须检查 `git diff --name-only`
和完整 diff，只提交本任务需要的变化；不要用格式化掩盖无关重构。第三方/生成文件按
仓库清单处理，不应手改。

### 可读性约束

- 使用当前项目类型、单位、point/coordinate 与 ID wrapper，不用裸整数逃避语义。
- 让所有权和空值清晰；优先 RAII 和已有容器/智能指针约定。
- lambda 保持局部、捕获明确；复杂逻辑提取为可命名、可测试的函数。
- 翻译字符串、debug message 和玩家文本使用项目现有 API，并保留格式参数类型。
- header 只暴露需要的依赖；include 调整要同时通过构建、clang-tidy/IWYU 证据。
- 不为“清理”而重命名稳定序列化字段、JSON/Lua API 或跨 Mod ID。

这些是审阅方向，具体机械规则以 clang-tidy 的 `cata-*` checks 和 AStyle 输出为准。若
formatter 与示例冲突，修正示例，不手工反向修改 formatter 结果。

### 改动边界与生成代码

先读最近的 `AGENTS.md` 和 `ai/generated-files.yml`。生成文件必须从 owner generator 更新；
vendored third-party code 只在任务明确要求时修改。大范围 rename、include 重排或 namespace
清理应独立提交，避免与行为修复混在一起。

### 验证选择

风格通过不代表能编译。至少编译受影响 translation unit；公共 header、template、build flag
或跨平台代码需要相应构建矩阵。只报告实际运行的命令，区分本地未安装 formatter、CI 结果
与未执行项。
