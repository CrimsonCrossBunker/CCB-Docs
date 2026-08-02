## 当前贡献任务路线

旧 FAQ 中关于 `omdata.h`、大型 `switch`、`player::activate_bionic` 和直接注册
`iuse` 的步骤已经不能当成当前流程。现在先找数据类型的加载器、相邻的第一方
JSON 例子和对应测试，再决定是否真的需要 C++ 扩展。

### 添加或修改怪物

1. 在 `data/json/` 或目标 Mod 中找到同类 `MONSTER` 定义，复制最小可工作的例子。
2. 使用全局唯一 ID；若要自然生成，再修改对应 monster group，而不是只添加类型。
3. 掉落物使用已有 item group；特殊攻击优先使用已有 JSON actor/EOC 能力，只有公开
   数据契约无法表达时才修改 native 注册。
4. 运行 JSON 格式与加载检查，再运行 `tests/monster_test.cpp` 中最接近改动的过滤测试。

`MonsterGenerator::load_monster` 把定义交给 monster factory；一致性检查还会验证物种、
harvest、ammo 与相关 ID。因此“JSON 能解析”不等于“定义完整”。

### 添加 overmap 地形或建筑

1. 先确认目标是 overmap terrain、overmap special 还是 mapgen；三者不是同一个层级。
2. 从 `data/json/overmap/`、目标 Mod 和相邻 mapgen 定义中选择当前例子。
3. 为需要的方向、连接规则、城市放置或 wilderness special 明确数据关系。
4. 运行 JSON 加载和 mapgen/overmap 相关测试；不要照搬旧文档中的硬编码 enum 与
   `draw_map` switch 流程。

`overmap_terrains::load` 使用 factory 载入数据，随后的一致性检查会解析 mapgen ID 和
spawn group。新增建筑时必须同时验证 overmap 放置与实际 mapgen。

### 添加物品、护甲或可使用动作

1. 从当前同类 object type 和相邻数据定义开始，确认 `copy-from`、必需字段与默认值。
2. 护甲要同时检查 pocket、coverage、material、layer 和受击部位语义；不要把旧 FAQ
   的保护计算步骤视为稳定公式。
3. 优先复用已有 use action、EOC 或 Lua API。只有新行为不能由公开契约表达时，才添加
   native action，并同步注册、测试和文档影响字段。
4. 运行 JSON 格式、加载、ID 检查和受影响的 focused test。

`itype::load` 直接读取重量、体积、长度、价格及各 subtype slot，随后还有 factory
finalize/check 阶段；修改者应追踪完整加载生命周期，不能只看一个 JSON 样例。

### 提交前最小闭环

- 从最近的 `AGENTS.md` 与 `ai/test-matrix.yml` 选择最窄验证。
- 在 PR 中填写 Documentation impact、Related CCB-Docs PR、Affected documentation IDs、
  Generated reference impact 与 Responsible human。
- 记录实际运行的命令、平台和结果；未运行项写明原因，不用全量测试掩盖 focused 失败。
- 若改动公开 Schema、LuaLS 声明、注册或生成清单，重新生成引用并检查 diff。

进一步入口见[常见任务](../../getting-started/common-tasks.md)、
[JSON 概览](../../json/overview.md)、[EOC 概览](../../eoc/overview.md)与
[测试策略](../../validation/testing.md)。
