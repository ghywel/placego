# Building and using it

You need an `ffmpeg` linked against a **patched** libplacebo. The patch
([frame-mix-hook.patch](frame-mix-hook.patch)) adds the
`PL_HOOK_FRAME_MIX` shader hook stage; without it the shaders in this
repository cannot run at all, because stock libplacebo never hands a custom
shader more than one frame. The patch also makes a skipped window loud:
when the frame queue cannot fill the window a shader declares, libplacebo
logs an error on that frame (expected at a clip's first and last frames
only) and, with `PL_FRAME_MIX_STRICT` set in the environment, paints the
frame magenta instead of falling back to the builtin mixer -- the bench
scripts fail a run that shows more than the two boundary skips.

`fps=`, frame pacing, `custom_shader_path` loading and `frame_mixer=` string
lookup all already exist in `vf_libplacebo.c`, so for **frame-rate scaling**
(24 -> 60 and similar) libplacebo is the only thing that needs patching.

A **second, optional patch**
([frame-mix-nn-threshold.patch](frame-mix-nn-threshold.patch)) is needed only
for the **N:N flow-field** use case -- running the shader at the source's own
rate to read the motion field out, rather than to insert frames. Without it
the hook silently never fires at a matched rate: libplacebo's frame queue
point-samples to a single frame whenever the output and input rates agree to
within `interpolation_threshold` (default `1e-6`), and a one-frame mix cannot
satisfy an N-frame hook. The patch lowers that threshold, and only when a
`PL_HOOK_FRAME_MIX` hook is actually attached. See
[TRIDIRECTIONAL.md](TRIDIRECTIONAL.md) for the full diagnosis.

Workaround if you would rather not patch ffmpeg: ask for `fps=24.0001`
instead of `fps=24`. That clears the threshold while the two rates diverge by
one frame only after ~240,000 frames.

Three build guides follow, one per platform. They produce the same thing and
the same shaders work on all of them -- verified by running the whole test
harness on each (see "Verifying the build" below). Linux and Windows agree on
the ladder numbers to 0.01 dB; macOS runs everything but does not reproduce
its own numbers from run to run, which is documented in the macOS section and
is a real finding rather than a caveat to skim.

- [Linux](#linux)
- [Windows](#windows)
- [macOS](#macos)
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

For the N:N flow-field use case, and for any shader declaring a window of
five or more frames, apply the ffmpeg-side patch before building (it also
sizes the frame queue's lookahead to a declared window of five or more
frames; without it a five-frame hook is skipped on some frames in favour
of the builtin mixer, with no error):

```bash
git apply /path/to/Novel-Interpolate/scripts/frame-mix-nn-threshold.patch
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

## macOS

**Builds and runs, verified 2026-08-30** on macOS 15.7.9 (Intel), against
MoltenVK 1.4.2 and vulkan-loader 1.4.357, driving an AMD Radeon RX 6600 eGPU.
[build-macos.sh](build-macos.sh) took five fixes to get there; it is no longer
a considered starting point but a path that has been walked.

```bash
./build-macos.sh                 # deps | placebo | ffmpeg | verify
```

The whole harness passes: `10 passed, 0 failed` from
[tests/smoke.sh](tests/smoke.sh), including shader compilation, a 60-frame
Vulkan render, and the ground-truth ladder against both baselines.

**Read the accuracy caveat below before trusting a number from this platform.**

### What is different here

**There is no native Vulkan.** Everything runs through
[MoltenVK](https://github.com/KhronosGroup/MoltenVK), which translates Vulkan
to Metal. That makes macOS a genuinely third Vulkan implementation after Mesa
and AMD's Windows driver -- and a translation layer rather than a driver, so
it is a harder portability test than Windows was.

The loader will not find a device unless it is told where the ICD manifest is.
Note Homebrew installs the manifest under `etc`, not `share`, despite what
most documentation says:

```bash
export VK_ICD_FILENAMES="$(brew --prefix)/etc/vulkan/icd.d/MoltenVK_icd.json"
```

You do **not** need to set any `DYLD_*` variable. ffmpeg would normally
`dlopen` the Vulkan loader by bare name and fail to find Homebrew's copy, but
this build passes `--enable-vulkan-static` so the loader is an ordinary linked
dependency instead. That is deliberate: `DYLD_FALLBACK_LIBRARY_PATH` does fix
the `dlopen`, but SIP strips every `DYLD_*` variable when a protected binary
is exec'd -- and `/bin/bash` and `/usr/bin/nohup` are both protected, so it
vanishes the moment the harness shells out. Anything relying on it works only
by accident of which `bash` is first on `PATH`.

### The two things most likely to break -- one resolved, one confirmed

- **`VK_KHR_push_descriptor` -- fine.** MoltenVK 1.4.2 advertises it and
  ffmpeg uses it (`Using device extension VK_KHR_push_descriptor`). This was
  the top suspect and it is a non-issue on current versions.
- **Storage images -- this is the real problem, and it does not announce
  itself.** The shaders load, compile and render without a single error or
  validation warning. But the ladder is **not reproducible from run to run** --
  for reasons that turn out not to be about storage images at all; see below.

### The accuracy caveat: results here are nondeterministic

Repeated runs of an identical case with an identical shader, same binary,
nothing changed in between:

| case | observed (base interpolator) | spread | Linux/Windows |
|---|---|---|---|
| `L1_trans_8px` | 41.34, 40.16, 39.68, 38.93 | **2.41 dB** | 41.34 |
| `L2_trans_16px` | 38.44, 38.44, 38.26, 37.48, 37.41, 37.41 | **1.03 dB** | 38.45 |
| `L9_occlusion` | 38.31, 37.08, 36.98, 35.98 | **2.33 dB** | 38.31 |

**These are PRE-RESET figures and will not reproduce.** The synthetic ladder's
scenes were rewritten on 2026-08-31 because their ground truth was
pixel-quantised, which moved every absolute score on the ladder substantially
-- see "The ladder reset" in [tests/TESTING.md](tests/TESTING.md). The table
above is kept because what it demonstrates is the *spread* between repeated
identical runs, which is a property of the platform and remains valid. But do
not compare a fresh macOS number against the "Linux/Windows" column here: on a
re-run, measure a fresh Linux or Windows baseline with the current scenes and
compare against that. The framemd5 tables further down are unaffected, since
they compare renders to each other rather than to a ground truth.

The cause was investigated on 2026-08-30. **It is not a defect in this
project's patch or shaders**, and the flow cache -- the obvious suspect -- was
ruled out by experiment.

**What it is: a baseline bit-nondeterminism in the Vulkan/MoltenVK path, which
the motion search then amplifies catastrophically.** Measured with
`-f framemd5`, which compares frames exactly rather than through a PSNR figure
rounded to two decimals:

| path | frames differing out of 60 | magnitude |
|---|---|---|
| `fps=60`, no Vulkan at all | **0** | -- |
| stock `frame_mixer=linear` | 1 | negligible |
| a trivial 1-pass custom hook (`nframe-smoketest.glsl`) | 1 | negligible |
| the interpolator | 9--14 | up to 39 dB |

The CPU path is exactly reproducible. Nondeterminism appears as soon as
anything goes through Vulkan here, **including stock libplacebo with no custom
shader and no storage images at all** -- one frame in sixty, at a magnitude too
small to see in a PSNR figure. That is the root, and it is upstream of this
project.

The interpolator turns that into whole ruined frame groups because block
matching selects an **argmin over candidate offsets**. Where the cost surface
has a tie or near-tie, a one-LSB difference flips the chosen motion vector
outright, and the entire warp for that source pair is then built on the wrong
vector. The amplification tracks how tie-prone the content is, exactly as that
model predicts:

| scene | frames differing out of 60 |
|---|---|
| `L0_static` (no motion) | 1--2 |
| `M1_noise_large` (aperiodic, fewest ties) | 3--4 |
| `L6_flat_large` (flat interior, many ties) | 7--9 |
| `L7_textured_large` | 9--10 |

**Severity also scales with how far the GPU's memory is from the CPU**, which
is what makes this so visible on the machine it was found on. Same MoltenVK,
same binary, same scene, three devices:

| device | frames differing out of 60 | worst deviation |
|---|---|---|
| RX 6600 (eGPU over Thunderbolt) | 14 | **39.11 dB** |
| Radeon Pro 560X (internal discrete) | 1 | 10.48 dB |
| Intel UHD 630 (integrated, shared memory) | 3 | 1.80 dB |

**Two hypotheses were tested and refuted, and are recorded so they are not
retried:**

- **It is not the flow cache.** A variant with all twelve
  `if (!pair_changed)` cache-read branches forced off -- so every frame
  recomputes from scratch and no cross-frame storage read happens at all --
  is *just as* nondeterministic (14/60 frames, 41.76 dB worst). The model
  above explains why: each of the four frames in a group independently hits
  the same tie and independently lands on the same wrong vector, which is
  also why the bad values are identical no matter which group fails.
- **It is not a missing barrier, as far as validation can tell.** 180 frames
  under `VK_LAYER_KHRONOS_validation` with synchronization validation active
  (confirmed active by the unrelated VUID it emits) reported **zero**
  `SYNC-HAZARD` findings. Note the limit of that evidence: validation checks
  that the API usage is correct, not that the driver honours it.

**Where that leaves it.** The remaining candidates are MoltenVK's translation
to Metal, or Metal/driver behaviour on these GPUs. Both are upstream, and
neither has been isolated further. What is established is that the patch and
the shaders are not at fault, and that a single run on macOS still proves the
shader *runs* correctly under a translation layer.

**If you must measure on macOS, use the integrated GPU** (`vulkan=vk:2` here,
check ordering with `vulkaninfo --summary`). It reduced the worst per-frame
deviation from 39.11 dB to 1.80 dB -- twenty times better, though still not
clean. It is slower, but this is a correctness instrument, not a timing one.

**The amplifier has since been fixed -- but not yet verified here.** The
argmin now requires a candidate to beat the incumbent by a relative
`TIE_MARGIN` before displacing it, which stops a near-tie being decided by the
last bits. It was implemented and measured on Windows, where a reproducible
baseline exists to verify against, using a deliberate perturbation in place of
this platform's free one: `tests/tieprobe.sh`, documented in
[tests/TESTING.md](tests/TESTING.md). At one float32 ULP it takes the base
shader from 56 noise-decided frames in 240 to 0, and the production shader
from 138 to 3 cosmetic ones, for at most 0.02 dB on the ground-truth ladder.

**What that does NOT establish is the macOS result**, and the tables above
have deliberately not been re-run or amended. The fix defends against
perturbation of arithmetic size -- summation order, a different compiler. If
MoltenVK's nondeterminism is that small, the 9--14 ruined frames above should
collapse to roughly nothing; if it is coarser, they will not, and that is a
genuinely useful thing to learn since it would rule out a whole class of
cause. **Re-running the framemd5 tables on this platform is the outstanding
stress test.** It is the only environment here that perturbs the inputs
enough to exercise the tie-breaking at all, which is why it is worth doing
rather than assuming. Until it has been run, treat the macOS numbers above as
current.

**Practical consequence:** do not tune a parameter against macOS numbers, and
do not compare a macOS figure against a Linux or Windows one -- the difference
you measure may be entirely this. A single run here proves the shader *runs*
under a translation layer, which is what the platform is genuinely good for.

### GPU expectations

Apple added RDNA2 support for the Radeon RX 6000 series on Intel Macs in
macOS 12 Monterey, and this is confirmed in practice: MoltenVK enumerates an
RX 6600 eGPU as a Vulkan device and ffmpeg selects it
(`Device 0 selected: AMD Radeon RX 6600 (discrete) (0x73ff)`), in preference
to the internal Radeon Pro 560X.

That is *not* the case on this project's Windows install, where the same card
in the same enclosure is enumerated by the OS and driven by D3D12 but never
appears as a Vulkan device (see the testing matrix in [README.md](README.md)).
So macOS is the only configuration in this project pairing a modern GPU with a
translation-layer Vulkan.

### Running it here: there is no zero-copy path

On Linux the production pipeline never brings a frame back to system memory --
VAAPI decodes, `hwmap` re-maps that memory into Vulkan through DRM PRIME, and
`hwmap` maps it back for the VAAPI encoder. **None of that exists on macOS.**
This build offers exactly two device types:

```
$ ffmpeg -init_hw_device list
videotoolbox
vulkan
```

and mapping between them is not implemented:

```
[Parsed_hwmap_0] Failed to created derived device context: -78.
Task finished with error: Function not implemented
```

`-78` is `ENOSYS`. VideoToolbox decodes into `CVPixelBuffer`s and MoltenVK
cannot import them, so **at least one CPU round-trip per frame is structural
on macOS.** This is an ffmpeg-level gap rather than a hardware limit -- there
is no code path, not a failed negotiation.

The working command, with the download made explicit because it cannot be
avoided:

```bash
export VK_ICD_FILENAMES="$(brew --prefix)/etc/vulkan/icd.d/MoltenVK_icd.json"

ffmpeg \
  -init_hw_device vulkan=vk -filter_hw_device vk \
  -hwaccel videotoolbox -hwaccel_output_format videotoolbox_vld \
  -i input.mkv -c:a copy \
  -vf "hwdownload,format=nv12,\
libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation-variational.glsl" \
  -c:v hevc_videotoolbox output.mkv
```

VideoToolbox decode is still worth using -- it measured about 8% faster
end to end than software decode -- but the gain is from the decode itself, not
from keeping anything resident.

### What the round-trip costs

1080p source, 24->60, base interpolator, RX 6600, 600 frames:

| chain | fps |
|---|---|
| shader, downloaded to system memory each frame | 65.3 |
| shader, frames kept in Vulkan (`,format=vulkan`) | **100.5** |
| stock `frame_mixer=linear`, downloaded each frame | 103.9 |
| stock `frame_mixer=linear`, kept in Vulkan | **262.0** |

**Read shader-vs-linear comparisons off the resident rows, not the downloaded
ones.** With the readback in the chain the shader looks like 1.6x the cost of
linear (103.9 -> 65.3); on the GPU it is really 2.6x (262.0 -> 100.5). The
readback is a fixed per-frame cost that dominates the cheap mode and so
flatters the expensive one. Any figure measured through a downloading pipeline
understates what the shader actually costs.

The readback here is ~5.8 ms/frame for a ~2.85 MiB frame, about 490 MB/s
effective -- roughly a fifth of what this Thunderbolt link sustains, which
says the cost is dominated by synchronisation stalls rather than bandwidth.
That has not been separated properly and is an inference, not a measurement.

Note the ladder harness in `tests/` deliberately downloads every frame,
because `psnr` is a CPU filter. It is a correctness instrument and **no
throughput number should be taken from it.**

### Why not OpenGL instead? Because it is closed off twice over

libplacebo's own README says it "supports Vulkan (including MoltenVK), OpenGL,
and Direct3D 11", which makes OpenGL look like an available escape route from
everything above. It is not, for two independent reasons, either of which
would be sufficient on its own. Both were checked rather than assumed, because
the question costs a day to answer from scratch.

**1. ffmpeg only ever instantiates the Vulkan backend.** That README describes
*libplacebo's* capabilities, not ffmpeg's use of them.
`libavfilter/vf_libplacebo.c` contains **zero** references to OpenGL or D3D11,
and accepts exactly one device type:

```c
if (avhwctx->type == AV_HWDEVICE_TYPE_VULKAN)
    vkhwctx = avhwctx->hwctx;
...
s->vulkan = pl_vulkan_create(s->log, ...);
```

Since ffmpeg is this project's entire delivery vehicle, that alone settles it
-- on every platform, not just macOS.

**2. macOS OpenGL could not run these shaders anyway.** Apple froze OpenGL at
4.1 and deprecated it in 2018. Queried directly on this machine:

```
GL_VERSION   : 4.1 ATI-7.0.24
GL_RENDERER  : AMD Radeon RX 6600 OpenGL Engine
GLSL         : 4.10
image_load_store (GL 4.2, required by //!STORAGE) : NO
compute_shader   (GL 4.3, required to dispatch)   : NO
```

In libplacebo a `//!STORAGE` declaration becomes a `PL_DESC_STORAGE_IMG` and
is dispatched through `pl_dispatch_compute`, so the ten flow-cache images need
GL 4.3. macOS is two versions short, and will not be catching up.

**The consequence that matters: on macOS there is no alternative backend, so
the nondeterminism above has no route around it.** MoltenVK is the only way
libplacebo reaches a GPU here.

For completeness, the one theoretical path runs outside ffmpeg entirely: mpv,
which does use libplacebo's GL backend, running a *storage-free* variant of
the shader -- without `//!STORAGE` the passes are ordinary fragment shaders and
GL 4.1 would suffice. That means giving up the flow cache that makes the
shader affordable, abandoning the ffmpeg harness this project is built on, and
it is entirely unknown whether GL would be any more deterministic. That is a
different project, not a workaround. Direct3D 11 is Windows-only and equally
unreachable through ffmpeg.

### This is an Intel Mac -- Apple Silicon will differ, probably a lot

Everything in this section was measured on an **Intel** MacBook Pro (x86_64,
macOS 15.7.9) with an AMD RX 6600 in a Thunderbolt enclosure. Several findings
here are properties of that arrangement rather than of macOS, and an M-series
machine should be expected to diverge:

- **eGPUs are not supported on Apple Silicon at all.** The RX 6600 result does
  not transfer in any form; there, MoltenVK would be running on Apple's
  integrated GPU.
- **Unified memory changes the economics of the round-trip.** The readback
  measured above crosses Thunderbolt to a discrete card, which is the worst
  case available. On an M-series part CPU and GPU share physical memory, so
  the same `hwdownload` should be far cheaper -- possibly cheap enough that
  the missing zero-copy bridge stops mattering. **The `ENOSYS` itself will
  still be there** (it is an absent ffmpeg code path, not a hardware
  constraint); only its cost should change.
- **The nondeterminism finding does not transfer in either direction.**
  MoltenVK there translates to Apple's own GPU driver rather than AMD's, so
  the storage-image behaviour has to be re-measured, not assumed. It could be
  absent, or worse.
- **Paths differ.** Homebrew's prefix is `/opt/homebrew`, not `/usr/local`.
  `build-macos.sh` uses `brew --prefix` throughout and should adapt, but any
  literal path written in this document will be wrong there.
- **The build is architecture-specific.** This one is x86_64; `nasm` is in the
  dependency list for ffmpeg's x86 assembly and is simply unused on arm64.

When that list was written none of it had been tested; it was reasoning
about mechanisms, flagged as such. It has now been tested, and the section
below scores each prediction against measurement. The reasoning is kept as
written so the predictions stay honest.

### Apple Silicon: measured (2026-09-01, M2)

Tested on the smallest Apple Silicon GPU sold: a fanless MacBook Air, M2
with the **8-core GPU** variant (`system_profiler` and `ioreg` agree on 8),
8 GB of unified memory, macOS 26.6.2. By public architecture figures that
is 1,024 FP32 ALUs at ~1.4 GHz — **~2.9 TFLOPS, almost exactly a Radeon
Pro 560X's nominal compute**, which makes those two machines a matched
pair for separating architecture from arithmetic. Toolchain: MoltenVK
1.4.2 (driver 0.2.2210) under vulkan-loader 1.4.357, shaderc 2026.3,
Apple clang 21, libplacebo 7.371.0, meson 1.12. MoltenVK reports subgroup
width 32 (variable 4–32), 1024 max workgroup invocations, 32 KB shared
memory.

Scoring the predictions above: **unified memory — confirmed,
emphatically** (measured below). **Nondeterminism — present but
transformed**, in an interesting way (below). **eGPU, paths, nasm — as
predicted**; `build-macos.sh` adapts via `brew --prefix` without edits.

#### Build deltas from the Intel walk-through

- `build-macos.sh` runs unmodified on arm64, but **predates
  `frame-mix-nn-threshold.patch`**: apply that to the ffmpeg clone by hand
  (`git apply`) and rebuild before trusting any N:N run. The marker test
  catches the omission — a dark corner at exactly `fps=24` with
  `TRI_DIAG=2` means the patch is missing.
- The stage argument is a *starting* stage, not a selection:
  `./build-macos.sh deps` runs deps, placebo, ffmpeg AND verify.
- **The harness python trap, arm64 edition.** macOS puts `/usr/bin` ahead
  of `/opt/homebrew/bin` on a stock PATH, so `python3` is the system 3.9
  while the venv `ensure_python` builds (from meson's shebang) is Homebrew
  3.14. The venv's numpy then fails under the wrong interpreter with
  `No module named 'numpy._core._multiarray_umath'` — a version-mismatch
  error that reads like a broken install. Fix: put `/opt/homebrew/bin`
  first on PATH for any harness run, so `python3` matches the venv that
  `PYTHONPATH` exposes.

#### Correctness: agreement to hundredths of a dB

The full tri ladder was run against the Windows (560X, native AMD driver)
reference numbers. Five of seven agree to ≤0.03 dB — four essentially
exact — across a translation layer onto a different GPU architecture:

| case | Windows | M2 | Δ |
|---|---|---|---|
| `L1` | 61.39 | 61.38 | −0.01 |
| `L2` | 42.10 | 42.10 | 0.00 |
| `L9` | 40.13 | 40.13 | 0.00 |
| `M3` | 21.92 | 21.92 | 0.00 |
| `O2` | 45.99 | 45.76 | −0.23 |
| `O4` | 47.42 | 47.17 | −0.25 |
| `O5` | 34.03 | 34.06 | +0.03 |

The two O-series deltas are the same order as this platform's own
run-to-run spread (re-runs gave O2 45.69, O4 46.95), so they cannot be
read as a cross-platform bias at n=2.

The field calibrations transfer to the decimal: accel A4 f9 6.6%, A5
2.5%, A6 2.4%, A7 1.8%, O6 0.7% — all identical to Windows; O5 5.6% vs
4.9%; the A4 f6 blemish reproduces (18.3% vs 17.2%). The quad jerk field:
O5 f10 3.6% vs 3.4%, nulls −0.028/−0.034 vs −0.020/−0.033. The measured
failures also reproduce as failures — F2 26–73% (ref 24–74%), R2/R3
median vector error 133–207% (ref 100–207%) — which is its own kind of
confirmation. The **quad ladder with the full-resolution level** was run
here in full for the first time anywhere: O3 came in at **+1.04 dB over
tri** against a prediction of "about +1.1", non-oscillation drag mostly
within the stated 0.1–0.35 dB band, with `L6_flat_large` an unpredicted
**+3.18** outlier in quad's favour and L1/O6 slightly past the drag band
(−0.82/−0.85).

#### Reproducibility: transformed, not gone

Measured with `framemd5` repeat pairs, the right instrument for this
question:

- stock `frame_mixer=linear`: **0/60 frames differ** — the first fully
  bit-reproducible stock Vulkan render measured on any Mac in this
  project (the Intel machine's best was 1/60).
- tri: **60/60 frames differ** — but the worst between-run frame PSNR is
  **52.9 dB**, and ladder scores move ≤0.25 dB. Nothing resembling the
  Intel arrangement's ruined frames (whole frames swinging up to 39 dB).
- quad: 16/60, same benign magnitude.

60/60-but-bounded fits a specific mechanism: the flow cache carries state
from frame to frame, so a single early one-LSB divergence propagates a
bit-level difference into every subsequent frame — while `TIE_MARGIN`
stops any of them from flipping an argmin and ruining the frame. Whether
the credit belongs to `TIE_MARGIN` or to a tamer driver cannot be
separated here; that is the Intel Mac's outstanding stress test, which
this machine does not discharge. Practically: still do not tune a
parameter against a single run here, but this platform is no longer the
measurement write-off the eGPU arrangement was — it agreed with Windows
to 0.03 dB on most of the ladder.

#### Unified memory: the round-trip stops mattering

The `ENOSYS` is still there, exactly as predicted — `videotoolbox` and
`vulkan` remain underivable from each other, and every frame still makes
the API-level round trip. What changed is what the round trip costs when
the "copy" lands in the same physical DRAM instead of crossing
Thunderbolt/PCIe. Same four chains as the Intel table, avengers clip at
native resolution, 24→60:

| chain | M2 8-core | Intel Mac, RX 6600 eGPU |
|---|---|---|
| tri shader, downloaded each frame | 13 | 65.3 (base shader) |
| tri shader, kept in Vulkan | 12 | 100.5 |
| linear, downloaded each frame | **182** | 103.9 |
| linear, kept in Vulkan | 234 | 262.0 |

Two readings. First, the readback penalty on the shader path went from
**35% to zero within noise** (13 vs 12 is rounding, and the resident run
came later on a passively-cooled machine), and on the linear path from
**60% to 22%**. Second — the cleanest demonstration of the architecture —
the base M2 **beats the RX 6600 eGPU rig outright on the downloading
linear path** (182 vs 104 fps), the bus-bound case, while losing heavily
on the compute-bound shader path to a GPU three times its size. Unified
memory wins exactly where the mechanism says it should, and nowhere else.

This also inverts the Intel measurement trap: there, the fixed readback
flattered the shader (it looked 1.6× linear's cost; resident showed
2.6×). Here the resident rows give the honest ratio directly, and it is
~19× on this small GPU — the shader really is expensive relative to a
blend; UMA just stops the pipeline hiding it.

#### Throughput on the films, and the exact commands

Every row below was produced by this command shape (all of them logged
verbatim at measurement time; the fps is ffmpeg's own end-of-run average
and includes software decode, matching how the Arc A310 figures were
taken):

```
ffmpeg -init_hw_device vulkan=vk -filter_hw_device vk \
  -i avengersclip.mp4 \
  -vf "scale=1280:-2,libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=tri.glsl" \
  -an -f null -
```

Variants: drop `scale=1280:-2,` for native resolution; append
`,format=vulkan` after `libplacebo=...` for the resident rows; replace
`-f null -` with `-c:v hevc_videotoolbox -b:v 6M -f null -` for the
encode rows. `VK_ICD_FILENAMES` must point at Homebrew's MoltenVK
manifest (under `etc`, not `share`).

| run, 24→60 | tri (48 passes) | quad (68 passes) |
|---|---|---|
| avengers 720p, `-f null` | 30 | 18 |
| back to the future 720p, `-f null` | 19 | 15 |
| avengers 720p, + hevc_videotoolbox | 26 | 18 |
| avengers native (1920×808), `-f null` | 13 | 8.7 |

**Postscript, same day: the native Metal port beat this whole table.**
The mpv-hook shader was machine-translated to Metal compute and run by a
native Swift host (`metal-demo/`, plan and outcomes in METALPORT.md) —
hardware decode, zero-copy frames, no translation layer. Same films,
same machine, native resolution: **quad 12.7 fps vs 8.7 above (+46%),
tri 16.9 vs 13 (+30%)** — and the port reproduces the ladder and the
field calibrations through the project's own tools before its numbers
count. The taxes measured individually in the section above compound to
a third-to-half again of throughput at film sizes; "a vendor-native port
should run faster" is now a measurement, not an expectation.

Read this row as the bottom anchor of a compute-proportional line, not as
"macOS is slow". The N=2/3/4 shader family is the scaling knob — cost
tracks model order — and the hardware table now spans this 2.9-TFLOPS
fanless machine to an 8.9-TFLOPS discrete card running the same shaders
and agreeing to hundredths of a dB. The hardware scales with the
use-case.

Two caveats on the absolute numbers, stated so nobody over-reads them.
Per-FLOP this path delivers roughly a third of what the Arc A310 gets
through Mesa (104 fps × 41 passes at ~3.1 TFLOPS there, 30 × 48 at ~2.9
here) — candidates are MoltenVK translation overhead, 8 GB memory
pressure, and thermal throttling, which the measurements cannot yet
separate. And these runs came late in a ~30-minute sustained GPU load on
a fanless chassis, so they are a conservative floor; the 560X, at
near-identical nominal TFLOPS, is the controlled comparison worth running
on the return trip.

**Update, same day: the first caveat has now been decomposed — see the
next section. Translation of kernels is exonerated; the deficit is
delivered clock plus a real per-dispatch tax.**

#### Is MoltenVK the bottleneck? Measured, and mostly no

The obvious suspicion about any number on this platform is that the
Vulkan→Metal translation layer is eating it. That is untestable at the
pipeline level — there is no native-Metal libplacebo to race — but it is
directly testable at the kernel level, and `tests/mvkbench/` now does:
the same kernel logic written twice, GLSL dispatched through
Vulkan/MoltenVK against MSL dispatched through Metal natively, same
grids, same barrier policy, same wall-clock method, batches interleaved
A/B so thermal drift cannot favour either side. Three kernels isolate
three suspects — pure-FMA chains (`alu`, delivered FLOPS), a 5×5
block-match with 8×8 SAD patches and the production tie margin (`sad`,
the flow search in miniature), and near-empty dispatches (`tiny`,
per-dispatch fixed cost).

| kernel | Metal | Vulkan/MoltenVK | ratio |
|---|---|---|---|
| `alu` | 32.99 ms | 32.86 ms | 1.00 |
| `sad` | 33.27 ms | 33.39 ms | 1.00 |
| `tiny` | 1.3 µs | 36 µs | **~28×** |

Three findings, in order of surprise:

1. **Kernel execution is at parity to under half a percent**, for both
   ALU-bound and texture-bound work. The GLSL → SPIR-V → (SPIRV-Cross)
   → MSL path arrives at the same machine-code performance as
   hand-written Metal. The translation layer is exonerated for what the
   shaders spend almost all their time doing.
2. **Per-dispatch overhead is ~28× native** (~36 µs vs ~1.3 µs — encoder
   splits and fences where Metal's own barrier is nearly free). At 60
   output frames/s × 48 passes ≈ 2,900 dispatches/s that is ~10% of
   frame time from dispatch count alone, plausibly a few tens of percent
   with libplacebo's real barrier and descriptor traffic. A real tax; not
   a 3× explanation.
3. **Delivered FLOPS is the machine's, not the API's: ~1.04 TFLOPS on
   both sides** — 36% of the 8-core M2's ~2.9 nominal. A cool-down probe
   (4 idle minutes, re-run) moved nothing by even 1%, so it is not
   measurably thermal either: that is this chassis's steady-state compute
   for a workload of this shape, and the honest denominator for any
   per-FLOP comparison.

So the macro deficit against the Arc re-assigns: mostly the delivered
compute envelope, partly the dispatch tax, and essentially none of it
kernel translation. Two follow-ups fall out. `vkbench` deliberately has
no Metal dependency and now guards its portability-enumeration bits, so
the **same binary measures delivered FLOPS on any Vulkan driver** — run
`vkbench alu` on the 560X, the Arc and the RX 6600 to put *delivered*
rather than nominal numbers in the scaling ledger (the Arc's 104 fps at
an unknown delivered-FLOPS figure is the current gap in the per-FLOP
comparison). And if the dispatch tax ever matters enough to chase,
MoltenVK's barrier-to-fence mapping is where to look, not the shaders.

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

### Reading those commands

The shape is always:

```
ffmpeg <hardware setup> <input options> -i INPUT <filters> <output options> OUTPUT
```

with **two independent hardware decisions** inside the first part, which is
the thing most easily missed:

- `-init_hw_device` / `-filter_hw_device` set up the device the **filters**
  run on. libplacebo needs a Vulkan device here or it cannot run at all.
- `-hwaccel` / `-hwaccel_output_format` control the **decoder**, separately.

The whole question of whether a pipeline is fast is whether frames can cross
between those two without a trip through system memory.

In the Linux command above, `@dr` is what makes that possible:
`-init_hw_device vaapi=va@dr` and `vulkan=vk@dr` *derive* both devices from
the same DRM device, so VAAPI and Vulkan become two views of one driver
context rather than two unrelated ones. `hwmap` then re-maps the same physical
memory between them through DRM PRIME -- it is an import/export, **not a
copy**, which is why it is free. The chain reads:

```
hwmap=derive_device=drm,format=drm_prime   VAAPI decode output -> dma-buf
libplacebo=...                              Vulkan imports that dma-buf
format=vulkan,hwmap=derive_device=vaapi,format=vaapi   back for the encoder
```

Both APIs have to agree on a shared handle for this to work. Where they
cannot -- macOS being the case in this project -- there is no way to avoid a
copy.

### Checking whether frames are actually staying on the GPU

Worth checking rather than assuming, because the expensive case is the silent
one: the `libplacebo` filter happily accepts software frames, uploads them,
renders, and downloads the result, and the filter graph shows plain
`yuv420p` at both ends with no indication that a round-trip happened.

The reliable test is to force the issue. Append `,format=vulkan` after
`libplacebo` and see whether ffmpeg still runs:

| chain | result |
|---|---|
| `libplacebo=fps=60` | runs -- but silently round-trips |
| `libplacebo=fps=60,format=vulkan` | runs -- frames stay on the GPU |
| `libplacebo=fps=60,format=vulkan,hflip` | **fails** -- *"Impossible to convert between the formats"* |
| `...,format=vulkan,hwdownload,format=yuv420p,hflip` | runs -- download now explicit |

ffmpeg will **not** silently pull frames off the GPU once they are in a
hardware format; it refuses, and the error names the filter that forced the
issue. So if your chain runs with `,format=vulkan` appended, it is resident;
if it fails, the message tells you exactly where you are leaving.

To catch the other direction -- software frames entering the graph and being
uploaded for you -- run with `-v verbose` and read the graph input line:

```
[graph -1 input from stream 0:0] w:1920 h:1038 pixfmt:yuv420p ...
```

A software pixel format there (`yuv420p`, `nv12`) means the decoder handed
over system memory and libplacebo is uploading every frame itself.

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
needs no source video; everything is generated. It passes 10/10 on Linux,
Windows and macOS.

For the full ground-truth ladder:

```bash
./bench.sh all ../shaders/bidirectional-interpolation-variational.glsl mine
./analyze.py --variants
```

See [tests/TESTING.md](tests/TESTING.md) for what those
numbers mean and, importantly, the several ways this kind of measurement can
silently produce confident nonsense.
