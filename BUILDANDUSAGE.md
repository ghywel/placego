# Building and using it

You need an `ffmpeg` linked against a **patched** libplacebo. The patch
([frame-mix-hook.patch](frame-mix-hook.patch)) adds the
`PL_HOOK_FRAME_MIX` shader hook stage; without it the shaders in this
repository cannot run at all, because stock libplacebo never hands a custom
shader more than one frame.

No ffmpeg source changes are needed. `fps=`, frame pacing,
`custom_shader_path` loading and `frame_mixer=` string lookup all already
exist in `vf_libplacebo.c` unmodified. Only libplacebo is patched.

Two build guides follow, one per platform. They produce the same thing and
the same shaders work on both -- verified by running the whole test harness on
each and comparing the numbers (see "Verifying the build" below).

- [Linux](#linux)
- [Windows](#windows)
- [Using it](#using-it)

---

## Linux

### Dependencies

```bash
sudo apt install -y git meson ninja-build pkg-config \
    libvulkan-dev libshaderc-dev glslang-tools python3-jinja2
```

Two of these matter more than they look:

- **`libshaderc-dev`** supplies the runtime GLSL-to-SPIR-V compiler libplacebo
  needs to compile *custom* `.hook` shaders when they are loaded. Without it,
  meson still succeeds and produces a libplacebo that silently cannot run any
  of these shaders.
- **`python3-jinja2`** is used by libplacebo's build to generate shader
  source. Debian usually pulls it in transitively, so it is easy to omit and
  then be confused on a leaner system.

For a GPU you also need working Vulkan drivers (`mesa-vulkan-drivers` on
Intel/AMD). For correctness testing you do not need a GPU at all -- Mesa's
software Vulkan device (**lavapipe**) is sufficient, and is what most of this
project's measurements were taken on.

### libplacebo, patched

```bash
git clone --depth 1 https://code.videolan.org/videolan/libplacebo.git
cd libplacebo
git apply /path/to/Novel-Interpolate/scripts/frame-mix-hook.patch
meson setup build --buildtype=release \
    -Dvulkan=enabled -Dopengl=disabled -Ddemos=false \
    -Dprefix="$HOME/libplacebo-install"
ninja -C build && ninja -C build install
```

**`-Dopengl=disabled` is required, not optional,** with a shallow clone.
`--depth 1` does not fetch submodules, so the `glad` dependency the OpenGL
backend needs is absent and that backend hard-fails. Nothing here uses OpenGL.

Before building, confirm meson actually found shaderc:

```bash
grep -i "shaderc" build/meson-logs/meson-log.txt | head -3
```

You want `YES`. If it says `NO`, stop and fix that first -- everything will
appear to build and then no shader will load.

### ffmpeg against it

```bash
git clone --depth 1 https://github.com/FFmpeg/FFmpeg.git ffmpeg
cd ffmpeg
PKG_CONFIG_PATH="$HOME/libplacebo-install/lib/x86_64-linux-gnu/pkgconfig" \
./configure --enable-libplacebo --enable-vulkan --disable-doc \
    --extra-ldflags="-Wl,-rpath,$HOME/libplacebo-install/lib/x86_64-linux-gnu"
make -j"$(nproc)"
```

The `-rpath` means the built binaries find `libplacebo.so` at run time without
`LD_LIBRARY_PATH`. Adjust the pkg-config path to wherever `ninja install`
actually put it (`find "$HOME/libplacebo-install" -name 'libplacebo.pc'`) --
the multiarch directory name varies by distribution.

### Alternative: jellyfin-ffmpeg

If you are deploying rather than developing, jellyfin-ffmpeg is the easier
route and is what this project's production testing used. It already carries a
libplacebo patch directory:

1. Drop `frame-mix-hook.patch` into `builder/patches/libplacebo/`
2. Build as normal, e.g. `./build trixie amd64`

Also worth applying
[hw-base-encode-eof-nullcheck.patch](hw-base-encode-eof-nullcheck.patch)
to `src/libavcodec/hw_base_encode.c`. It fixes an upstream ffmpeg NULL pointer
dereference that segfaults when seeking input with an `fps=`-scaled output --
which is exactly the shape of command this project uses everywhere.

### Linux caveats

- **No PNG encoder if `zlib1g-dev` is missing.** ffmpeg's configure disables
  it silently. Write diagnostic frames as `.jpg` (`-q:v 2`) instead, or
  install zlib and reconfigure.
- **`--disable-x86asm`** avoids needing nasm/yasm if you do not have them, at
  some decoding speed cost. Fine for correctness work, not for production.
- **Software Vulkan is slow but correct.** Roughly 30x real time at 1080p.
  That is a fine way to verify behaviour and a poor way to measure speed.

---

## Windows

Native, via MSYS2 and mingw-w64. This is a real second platform -- different
compiler, different Vulkan loader, different vendor driver -- and the shaders
produce the same numbers on it.

### Scripted

```bash
powershell -ExecutionPolicy Bypass -File scripts\build-windows.ps1
```

That installs MSYS2 if absent, updates its package database, and hands off to
[build-windows.sh](build-windows.sh) inside the MINGW64 shell.
It is resumable -- `-Stage deps|placebo|ffmpeg|verify` -- and asserts its
preconditions rather than assuming them. The final stage compiles every shader
and runs part of the ground-truth ladder against the Linux reference numbers.

### By hand

From the **MINGW64** shell specifically (`C:\msys64\mingw64.exe`) -- not the
plain MSYS shell, which builds against `msys-2.0.dll` and does not produce a
native Windows binary:

```bash
pacman -S --needed --noconfirm git make diffutils \
    mingw-w64-x86_64-toolchain mingw-w64-x86_64-meson mingw-w64-x86_64-ninja \
    mingw-w64-x86_64-pkgconf mingw-w64-x86_64-shaderc \
    mingw-w64-x86_64-vulkan-headers mingw-w64-x86_64-vulkan-loader \
    mingw-w64-x86_64-nasm mingw-w64-x86_64-python \
    mingw-w64-x86_64-python-jinja mingw-w64-x86_64-python-numpy
```

Then the same libplacebo and ffmpeg steps as Linux above, minus the `-rpath`
flag, which Windows does not have. Afterwards:

```bash
cp "$HOME/libplacebo-install/bin/"libplacebo*.dll ffmpeg/
```

`pacman` does not need administrator rights.

### Windows caveats

These are the things that cost real time. None of them are obvious, and
several report an error that blames something else entirely.

**Absolute paths cannot appear inside an ffmpeg filter argument.** The colon
in `C:` is ffmpeg's own option separator, so the parser splits the argument:

```
No option name near '/Users/you/shaders/bidirectional-interpolation.glsl'
```

Note that it blames the *input file*. Escaping the colon, single-quoting the
value, and disabling MSYS2's path conversion were each tested and each fail --
the first is mangled by the argument converter, the second is eaten by the
shell, the third hands a POSIX path to a native binary that cannot open it.
**Use a relative path**, which also works unchanged on Linux:

```bash
cd /path/to/shaders
ffmpeg ... -vf libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation.glsl ...
```

**Paths inside filter strings are not path-converted at all.** MSYS2's
conversion heuristic only fires on standalone arguments, so a POSIX path left
inside a `-filter_complex` reaches a native `ffmpeg.exe` unconverted and
cannot be opened. Combined with the point above, a relative path is the only
form that works either way.

**A relative path is not always enough either.** MSYS2's POSIX root `/` is
`C:\msys64`, while `/c` is a virtual mount of `C:\`. A relative path spanning
the two is meaningless to a native binary. If your shader and your output are
on opposite sides of that boundary, copy the shader next to the output and use
a bare filename -- which is what `scripts/tests/bench.sh` does.

**`mingw-w64-x86_64-python-jinja`, not `python-jinja2`.** libplacebo generates
shader source with a Jinja2 template step. Debian supplies it transitively so
Linux never notices; here it fails partway through `ninja` as a bare
`ModuleNotFoundError` naming no package.

**No rpath.** `libplacebo-*.dll` must sit beside `ffmpeg.exe` or be on `PATH`,
or the binary fails at load with an unhelpful error.

**WSL2 cannot give you Vulkan on a real GPU.** WSL exposes `/dev/dxg`, a D3D12
paravirtualisation interface, but no `/dev/dri` render node -- which Mesa's
RADV/ANV drivers require. Vulkan there sees only lavapipe (software). Use WSL
for correctness and a native Windows or Linux build for anything involving a
GPU.

---

## Using it

Point `custom_shader_path` at a shader and set `frame_mixer=custom_n`. See
[SHADERS.md](SHADERS.md) for which shader to choose --
`bidirectional-interpolation-variational.glsl` is the recommended one.

Simplest form, software decode:

```bash
ffmpeg -init_hw_device vulkan=vk -filter_hw_device vk -i input.mkv \
  -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation-variational.glsl,format=yuv420p" \
  -c:v libx264 -crf 18 output.mkv
```

With hardware decode and encode, as used in production here:

```bash
ffmpeg \
  -init_hw_device drm=dr:/dev/dri/renderD129 \
  -init_hw_device vaapi=va@dr -init_hw_device vulkan=vk@dr \
  -filter_hw_device vk \
  -hwaccel vaapi -hwaccel_output_format vaapi \
  -i input.mkv -c:a copy -sn -dn \
  -vf "hwmap=derive_device=drm,format=drm_prime,\
libplacebo=format=p010le:fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation-variational.glsl,\
format=vulkan,hwmap=derive_device=vaapi,format=vaapi" \
  -c:v hevc_vaapi -global_quality 20 output.mkv
```

`frame_mixer=custom_n` is a named entry the patch adds to libplacebo's own
preset table. It is currently an alias for `mitchell_clamp`'s config, kept as
a separate name because that kernel is never evaluated once a
`PL_HOOK_FRAME_MIX` hook fires -- only its queue radius still matters.
`frame_mixer=mitchell_clamp` works identically.

`fps=` can be any target rate including non-integer ratios such as 23.976 to
60; `mix_t` is computed from real frame timestamps, not a fixed step.

### Verifying the build

Do not assume it works because it built. Run the harness:

```bash
export FFMPEG=/path/to/your/ffmpeg FFPROBE=/path/to/your/ffprobe
cd scripts/tests
./smoke.sh
```

That exercises every tool in the harness -- scene generation, frame-exact
clipping, shader generation, the flow visualiser, the numpy metrics, the
ground-truth ladder and the visual diff -- and reports pass/fail per tool. It
needs no source video; everything is generated. It passes 10/10 on both Linux
and Windows.

For the full ground-truth ladder:

```bash
./bench.sh all ../bidirectional-interpolation-variational.glsl mine
./analyze.py --variants
```

See [tests/TESTING.md](tests/TESTING.md) for what those
numbers mean and, importantly, the several ways this kind of measurement can
silently produce confident nonsense.
