## JSON 加载阶段与顺序

CCB 对每个 active Mod 按 world 已解析的依赖顺序调用 loader。单个路径内
`get_files_from_path(..., recursive=true)` 以 breadth-first 发现 JSON，同一目录按当前 filesystem
排序；普通 Mod 数据排除 `mod_interactions`，所有普通数据完成后再加载命中的 interaction。

### 可以依赖什么

可以依赖明确的 Mod dependency、generic factory deferred loading，以及 owning loader 文档化
的 finalize 解析。不要把文件名或目录深度当成通用 forward-reference API。某些 object 在
parse 时强制目标已存在，另一些只存 string ID 到 consistency check；必须检查具体 handler。

Core `data/json` 的历史目录布局曾用深度表达 skills→professions→scenarios 等顺序，但新代码
应优先让 factory/loader 明确处理关系。把文件移动到子目录可能改变 parse 次序，并影响依赖
旧偶然顺序的内容；这种变化属于高风险 JSON 修改。

### Mod 与 interaction

`dependencies` 决定 active Mod 顺序。普通内容必须在声明依赖之后可解析。
`mod_interactions/<target-id>/` 在普通 pass 后加载，source 记录为 `base#target`；它不能解决
普通文件在之前已经抛出的错误，也不支持嵌套多目标目录。

### 验证

运行 formatter、`make -j2 json-check` 和完整依赖组合 `--check-mods`。对顺序敏感修改，
加入最小 fixture，分别测试父/子先后、缺失 dependency、两个 Mod 覆盖、interaction 和
finalize。不要只在开发 checkout 测试；打包后的 path/case 行为也要由目标平台 CI 覆盖。
