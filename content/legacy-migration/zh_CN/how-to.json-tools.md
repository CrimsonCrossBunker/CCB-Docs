## JSON 工具按任务选择

仓库工具分为 formatter、loader/validator、只读查询和迁移脚本。先运行 `-h` 并用
`git diff --name-only` 限定范围；查询输出不是契约，批量转换必须审阅每个 changed file。

### 格式与加载

```sh
make -j2 tools/format/json_formatter.cgi RELEASE=1
tools/format/json_formatter.cgi path/to/changed.json
make -j2 json-check
```

项目 formatter 理解 CCB JSON dialect；不要用通用 formatter 删除 comment 或重排整个仓库。
`json-check` 验证 core load，Mod 还需真实 `--check-mods`。

### 查询 keys/values

`tools/json_tools/keys.py` 统计匹配对象出现的字段，`values.py` 统计一个 key 的值；二者支持
`key=value` filter、`--human` 和 nested dotted key。示例：

```sh
tools/json_tools/keys.py --human type=TOOL
tools/json_tools/values.py --key material --human type=TOOL
```

统计中的 MISSING 只表示样本没显式写，不代表 loader 没有 default 或字段非法。用 inventory
定位 handler，再查源码 requiredness。

### 生成与专项工具

`tools/json_api/generate_contracts.py` 生成 object/EOC inventory；`copy_from.py`、
`dialogue_validator.py` 和 `json_tools/*` 只用于其 help 声明的结构。任何 rewrite 前建立
窄文件清单、保留 commit、先 dry-run/临时 worktree，再用 owner formatter 和 loader 验证。
不要对第三方、generated 或全部 `data/` 运行“顺手清理”。

### 可审核输出

PR 记录命令、输入 path/filter、工具 commit、changed file 数与验证。若工具报 load error，
先修首个输入错误；不要把部分统计当完整结果。用于决策的报告应保存为 CI artifact，只有
项目清单明确要求的生成 reference 才提交。
