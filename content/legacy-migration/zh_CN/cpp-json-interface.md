## CCB C++ JSON 接口

先区分三种任务：载入人写的 game data、读取程序写的旧存档、写出新的存档。它们共享
`JsonValue`、`JsonArray`、`JsonObject`、`JsonMember` 和 `JsonOut`，但兼容策略不同。
Game data 支持 factory 继承；save data 必须能识别旧格式，不能把 `copy-from` 当存档机制。

### 读写基础

`JsonValue` 可测试并读取 scalar 或转成 object/array；`JsonObject` 按 member 名访问，
`JsonArray` 迭代或按位置读取，`JsonMember` 同时保留 key 和 value。优先用 `read` 以及
项目已有 deserialize/reader，不重复手写类型分支。

实现 `T::serialize( JsonOut & ) const` 或自由 `serialize` 后，`JsonOut::write/member` 可
组合该类型。读取对应实现 `deserialize`。写出格式是兼容契约：字段改名、删除或改变类型前
必须保留旧格式 reader 和 round-trip/旧 fixture 测试。

### Game data loader

generic factory 管理 ID、`copy-from`、deferred load、finalize 和 consistency check。对象
`load` 通常使用：

- `mandatory( jo, was_loaded, name, member[, reader] )`：首次对象必须提供；
- `optional( jo, was_loaded, name, member[, reader], default )`：首次缺失时使用明确 default；
- typed reader：解析 shorthand、单位、ID、容器和该字段允许的继承操作。

Default 必须出现在 `optional` 调用中，而不是只依赖 header 初始化。`was_loaded` 让子对象
缺失字段时保留父值；错误传 false 会抹掉继承值，错误传 true 会跳过首定义要求。

`extend`/`delete`、`relative`、`proportional` 都是 opt-in。容器 reader 常支持前两者，
数值操作依赖类型和 reader；字段看起来“像 vector/int”不证明它自动支持相应 patch。

### 错误和严格性

让 `JsonObject`/reader 在具体 member 抛出错误，以保留文件、行列和 member context。
不要为“兼容”广泛调用 `allow_omitted_members`；只在明确转发或忽略对象的边界使用。
加载成功后仍要运行 finalize/consistency checks，因为 cross-ID 和循环往往到该阶段才发现。

### 验证

Game data 运行 formatter、`make -j2 json-check`、真实 Mod 集 `--check-mods` 和 object
focused tests。Save data 用当前写出→读回、冻结旧 fixture→当前读取、缺失/新增字段与损坏
输入测试。C++ 改动还要编译所有使用公开 header 的 target，并确认错误消息仍指向来源。
