## CCB JSON object type 注册表

`DynamicDataLoader` 的 native `add(type, handler)` 调用决定可识别的 object type。
`data/reference/json/ccb_json_object_types.json` 是由
`tools/json_api/generate_contracts.py` 生成的检查清单，当前覆盖 191 个注册调用、190 个唯一
type。它证明“发现并索引”，不证明每个 handler 已有完整字段 Schema。

### 如何使用清单

每项记录 type、handler、source symbol/line、可证实的 mandatory/optional 字段、first-party
example 和 documentation status。`schema_status`/`documentation_status` 必须按原值解释；
`unclassified` 或 lexical-only 不能提升为必填、默认或完整支持。

生成清单禁止手改。新增/删除注册、修改 handler 或示例后运行 generator、仓库 JSON formatter、
`--check` 与 `tools/json_api` 单测。若提取器无法证明复杂 reader，应扩展可审核提取或加入
非行为性 registration metadata，而不是猜测。

### 从 type 到权威契约

1. 在 inventory 找 handler 和 source。
2. 阅读 loader 的 `mandatory`、`optional`、custom reader、finalize/check。
3. 找相邻第一方 JSON 与 focused test。
4. 检查 ID、copy-from、deferred load、单位、translation、migration 和 Mod 边界。
5. 用 formatter、`make -j2 json-check`、`--check-mods` 验证真实组合。

Editor Schema 可以提供补全，但 loader 和测试胜出。Occurrence count 只说明样本中出现频率，
不能证明 requiredness；成功解析也不证明 cross-ID finalize、平衡或存档兼容。
