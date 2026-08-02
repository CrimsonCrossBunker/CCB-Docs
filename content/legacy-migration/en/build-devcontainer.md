## Current Dev Container workflow

The pinned source contains three separate configurations: `Standard` at the root,
`Standard + Qt5` under `graphical/`, and `Cross-Compile w32` under `cross-compile/`.
Select the intended configuration file; do not follow the old guide's procedure of
commenting and uncommenting large sections of one shared Dockerfile.

### Prerequisites

- an editor with Dev Containers support (the checked configuration primarily targets the
  VS Code extension);
- Docker or a compatible container runtime;
- a cloned CCB fork and a dedicated branch;
- enough image, dependency, and build storage.

Open the repository, select the relevant `.devcontainer/.../devcontainer.json`, and run
“Reopen in Container”. The initial image build can take time. Preserve the build log and
the failing layer instead of repeatedly deleting all Docker data.

### Build inside the container

Use authoritative repository entry points after the container opens, for example:

```sh
make -j2
make -j2 tests
```

Repository CMake presets are also available. Run from the mounted repository root; Make or
CMake determines artifact locations. Graphical execution additionally depends on host
display, GPU or software rendering, and audio forwarding. A successful container compile
does not prove that the graphical binary starts on the host.

### Cross-compilation boundary

Use the dedicated `cross-compile` configuration for a Windows cross-build. It proves the
cross toolchain and target artifact, but does not replace Windows MSYS2/MSVC CI, runtime
DLL checks, or an actual Windows launch.

### Security and reproducibility

- Review Dockerfiles, features, mounts, ports, and host sockets before building.
- Never bake tokens, SSH private keys, signing material, or personal configuration into an
  image.
- When `.devcontainer/` changes, rebuild each affected configuration and record the host
  and runtime versions.
- Current JSON, Dockerfiles, and CI win over conflicting prose.
