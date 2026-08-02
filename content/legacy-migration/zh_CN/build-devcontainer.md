## 当前 Dev Container 工作流

固定来源包含三个独立配置：根目录的 `Standard`、`graphical/` 下的
`Standard + Qt5`，以及 `cross-compile/` 下的 `Cross-Compile w32`。选择配置文件，
不要再按旧指南注释或取消注释一个共享 Dockerfile 的大段内容。

### 前置条件

- 支持 Dev Containers 的编辑器（仓库配置以 VS Code 扩展为主要入口）；
- Docker 或兼容的 container runtime；
- 已 clone 的 CCB fork 和单独分支；
- 足够的镜像、依赖和编译空间。

在编辑器中打开仓库，选择对应 `.devcontainer/.../devcontainer.json`，然后执行
“Reopen in Container”。首次构建镜像可能较慢；失败时保存 build log 和具体 layer，
不要反复删除整个 Docker 数据目录。

### 容器内构建

容器打开后仍使用仓库权威入口，例如：

```sh
make -j2
make -j2 tests
```

也可以使用仓库 CMake preset。命令应从挂载的仓库根目录运行，产物位置由 Make/CMake
配置决定。图形运行还依赖 host display、GPU/软件渲染和音频转发；“容器内编译通过”
不代表 host 上的图形程序一定可启动。

### 跨编译边界

Windows 跨编译使用专门的 `cross-compile` 配置。它只能证明交叉 toolchain 和目标产物
可生成，不能替代 Windows 上的 MSYS2/MSVC CI、运行时 DLL 检查或真实启动测试。

### 安全与复现

- 审查 Dockerfile、feature、mount、端口和 host socket 后再允许容器构建。
- 不把 token、SSH 私钥、签名文件或个人配置烘焙进镜像。
- 修改 `.devcontainer/` 时至少重建受影响配置并记录 host/runtime 版本。
- 容器说明与仓库配置冲突时，以当前 JSON、Dockerfile 和 CI 为准。
