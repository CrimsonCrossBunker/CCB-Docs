## 当前 CCB 物品 JSON 模型

CCB 把可拾取实体统一加载为 `"type": "ITEM"`。通用字段由 `itype::load` 读取，
`subtypes` 再决定是否读取护甲、工具、枪械、弹药等 slot。旧文档中的字段表只能作为
定位入口；字段是否必需、默认值、取值范围和组合限制以当前 loader、注册表、测试及
[JSON object type 索引](../index.md)为准。

### 最小定义与稳定 ID

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_part",
  "name": { "str": "example part" },
  "description": "A component used by the documentation example.",
  "symbol": ";",
  "color": "light_gray",
  "weight": "100 g",
  "volume": "250 ml",
  "price": "1 USD",
  "price_postapoc": "10 cent",
  "material": [ "steel" ]
}
```

`id` 是存档、配方、item group、EOC 与 Mod 间的长期引用。已发布 ID 不应仅为了更整齐
而重命名；确需替换时，要先检查迁移/obsoletion 机制和存档兼容性。面向玩家的
`name`、`description` 应可翻译，不要把 ID 当显示文本。

### subtype 与 slot

当前 `itype::load_slots` 识别 `ARMOR`、`TOOL`、`PET_ARMOR`、`GUN`、`GUNMOD`、
`AMMO`、`MAGAZINE`、`COMESTIBLE`、`BOOK`、`BIONIC_ITEM`、`TOOLMOD`、`ENGINE`、
`WHEEL`、`SEED`、`BREWABLE`、`COMPOSTABLE`、`MILLING` 与 `ARTIFACT`。例如弹药定义
需要显式声明：

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_round",
  "copy-from": "223",
  "subtypes": [ "AMMO" ],
  "name": { "str_sp": "example round" },
  "ammo_type": "223"
}
```

- `subtypes` 控制本次定义读取哪些 slot 字段；不要因为父项拥有某个 slot 就省略子项意图。
- `PET_ARMOR` 与 `ARMOR` 不能同时声明；`GUNMOD` 已包含 tool-mod slot，不能再与
  `TOOLMOD` 同时声明。
- 同一物品可组合其他兼容 subtype，但每个 slot 都可能有自己的 mandatory 字段和
  finalize 检查。

### 通用字段与继承

常见通用字段包括尺寸/质量、价格、材质、显示、近战/投掷数据、flags、qualities、
`use_action`、pocket、variant 与变量。不要从一份示例推断所有字段：部分字段使用单位
字符串，部分读取稳定 ID，部分由专用 reader 校验。

`copy-from` 先复制父定义；顶层直接字段替换对应值，容器字段可在实现支持时用
`extend`/`delete`，数值或专用对象可能支持 `relative`/`proportional`。这些操作不是
所有字段的通用 Schema；详见[继承](../inheritance.md)，并从同一 subtype 的当前数据中
选择相邻样例。

### 修改与验证顺序

1. 在相邻第一方定义中确认 `type`、`subtypes`、字段形状和 ID 引用。
2. 对照 `itype::load` 与对应 slot 的 `deserialize`，确认 required/default/范围。
3. 只格式化本次改动文件，检查 formatter 没有扩大 diff。
4. 运行 `make -j2 json-check`；涉及 pocket、use action、配方或存档 ID 时再运行对应测试。
5. Mod 还应以实际 Mod 集执行 `--check-mods`，并记录未覆盖的平台或交互。

格式通过不代表 loader、ID 或玩法关系正确。Schema 覆盖不完整时，源码加载器和测试
始终优先。
