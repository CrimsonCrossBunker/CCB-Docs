## Soundpack 契约

Soundpack 是 `data/sound/` 下带 `soundpack.txt` 的目录；`NAME` 是 option 使用的唯一 ID，
`VIEW` 是显示名。`load_soundset` 解析当前选择，找不到时回退到 `basic`，再通过
`DynamicDataLoader` 加载目录内 JSON。音频功能未成功初始化时 sound JSON loader 会提前返回。

### SFX 与 playlist

`sound_effect` 要求 `id` 和 `files`，`volume` 默认 100；`variant` 可为字符串或数组，省略时为
`default`。`season`、`is_indoors`、`is_night` 进入查找 key。多个 file 是同一 key 的随机候选，
路径相对于 soundpack。实际 fallback 由 `sfx_resources` 查找实现；某些调用点会要求 exact
variant，因此不能假定每个 ID 都回退到 `default`。

`sound_effect_preload` 只预热列出的 key，不改变播放契约。`playlist` 包含 `playlists` 数组，每项
有 ID、可选 shuffle 和 `{file, volume}` 列表；同 ID 后加载的定义会替换 map entry。音乐 ID 的
激活和优先级由当前 `music` 调用代码决定，旧文档中的四项列表不是保证完整的 registry。

### 清点与验证

SFX 的 ID/variant 没有一份永远完整的手工清单：从所有 `play_variant_sound`、ambient、vehicle、
UI 和 music 调用点生成清单，并和 soundpack JSON 比对。检查缺失文件、解码格式、空列表、重复
key、exact/default fallback、季节/室内/昼夜组合、preload、shuffle、音量叠乘、loop/channel、
距离/pan/pitch、切换 pack 和禁用声音。发布音频还必须记录作者、来源和兼容许可证；不要把测试
模式或无音频 backend 的“成功加载”当成真实播放验证。
