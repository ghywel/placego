# N-Frame temporal analysis via ffmpeg and a patched libplacebo

## What this is

[frame-mix-hook.patch](frame-mix-hook.patch) is a small patch to
[libplacebo](https://code.videolan.org/videolan/libplacebo) -- the GPU
rendering library ffmpeg's `libplacebo` filter is built on -- that adds a
new custom-shader hook stage, `PL_HOOK_FRAME_MIX`. It gives a
user-supplied GLSL shader (the same `.hook`-format shaders mpv and ffmpeg
already support via `custom_shader_path`) simultaneous access to a whole
*window* of source video frames at once (as many as that specific shader
declares it wants, from 1 up to 8), plus the exact timing relationship
between them, instead of a single already-blended texture. When the
queue cannot fill the declared window (a clip's first and last frames,
or a host fault), the hook is skipped and the builtin mixer draws the
frame -- and the patch says so at error level on every such frame; set
`PL_FRAME_MIX_STRICT` in the environment and it paints the frame magenta
instead, so a miss can never pass for a result. A companion
patch to ffmpeg's filter, [frame-mix-nn-threshold.patch](frame-mix-nn-threshold.patch),
lets the window fire when the output rate equals the input rate, which
turns out to matter more than it sounds, and sizes the frame queue's
lookahead to the window the shader declares once it exceeds four frames
(four fit the default radius, and keep it, so their published numbers
stand; five need more, and without this a fifth-frame hook silently gets
the builtin mixer on some frames).

Everything downstream of that -- motion-compensated interpolation,
temporal denoising, custom deinterlacing, scene-cut-aware effects, or
anything else that needs to reason across time rather than within a
single frame -- is then just a GLSL shader, running as part of one
ordinary `ffmpeg` command.

What was built on it is the reason this repository exists, and it is not
the frame-rate conversion. The shaders here look at three and four frames
at once and write out, for every point on the screen and in real time,
not just where things are moving but how that motion is changing -- and,
because they run at the video's own frame rate as readily as at a higher
one, what they produce can be a measurement rather than a picture.
[WHAT-WE-BUILT.md](WHAT-WE-BUILT.md) says in plain language what that
turned out to be good for, where it fails, and what it was measured
against. Start there if you want to know why. Start below if you want to
know how.

## Why it's needed

Stock libplacebo's `frame_mixer` option
(`linear`/`oversample`/`mitchell_clamp`/`hermite`) is a fixed 1D temporal
blend kernel -- it can cross-fade between frames on a timeline, but it has
no concept of motion, and no way for a custom shader to see more than one
frame. `custom_shader_path` hooks only ever receive a single,
already-composited texture (confirmed by reading `pl_render_image_mix` in
`src/renderer.c` directly). There was, in short, no way to write a GPU
shader that looks at two frames and reasons about what changed between
them -- which is the fundamental operation behind almost every genuinely
temporal video technique.

This patch closes that gap at the library level rather than in any one
shader, so any custom shader -- from a one-line cross-fade to a full
motion-estimation pipeline -- can opt into it.

## What's new

- **`PL_HOOK_FRAME_MIX`** -- a new hook stage that fires once per output
  frame, in place of the builtin blend, whenever exactly as many source
  frames are available around the requested output timestamp as the
  attached hook declared it wants.
- **N-frame access** -- a hook declares how many frames it wants (from 1
  up to `PL_FRAME_MIX_MAX`, currently 8) simply by which `FRAME<n>` names
  it binds in its GLSL (`HOOKED`/`NEXT` remain the friendly aliases for
  `FRAME0`/`FRAME1`, the two-frame case). The renderer only fires the hook
  once it can supply exactly that many frames -- fewer (e.g. the first and
  last few output frames of a clip) fall back to the builtin blend
  instead, needing proportionally more lead-in the larger the window.
- **`mix_t`** -- the output frame's normalized position between the first
  two frames (0.0 at `FRAME0`, 1.0 at `FRAME1`), provided as a convenience
  for the two-frame case. Not well-defined for three or more points, so
  it is left unset for hooks wanting more than 2 frames.
- **`rts_mix[]`** -- the raw relative timestamps every frame in the
  window was selected at, for a shader that needs the actual frame
  spacing (to detect a scene cut or VFR discontinuity, or to fit a curve
  through more than two points).
- **`num_mix`** -- how many frames are actually in the window this call
  (always exactly what the hook declared, once it fires at all).
- **`pair_changed`** -- true only when the whole window of source frames
  has actually changed since the previous call, false when this is just
  another output frame within the *same* window (only relative position
  moved). Lets a shader maintain a persistent GPU-side cache (via the
  existing mpv-shader `//!TEXTURE ... //!STORAGE` directive) of expensive
  per-window work -- a motion field, say -- and skip recomputing it for
  every output frame at non-integer fps ratios.
- **`frame_mixer=custom_n`** -- a new named entry in libplacebo's own
  frame-mixer preset table for this use case, so the ffmpeg command line
  doesn't have to name an unrelated cubic kernel (`mitchell_clamp`) to
  get the queue radius it happens to need (see Usage below). Currently an
  alias for `mitchell_clamp`'s existing config, not a new filter.
- **N:N operation** (the companion patch) -- libplacebo's frame queue
  quietly collapses to a single-frame mix whenever the output rate is
  within its interpolation threshold of the input rate, which for a
  matched rate is exactly 0, and the hook never fires. The second patch
  disables that collapse only while a `PL_HOOK_FRAME_MIX` hook is
  attached, so a shader can see its full window at the source's own
  frame rate. That is what makes the shaders usable as instruments
  rather than only as interpolators.

None of this requires any ffmpeg source changes -- `fps=`, frame pacing,
`custom_shader_path` loading, and `frame_mixer=` string lookup all
already existed in `vf_libplacebo.c` unmodified. Only libplacebo needs
the patches.

## Benefits

- **Real-time, GPU-native.** Runs as ordinary GLSL/compute shaders on
  whatever GPU backend libplacebo targets (Vulkan under ffmpeg; libplacebo
  itself also speaks OpenGL and D3D11) -- no CPU round-trip, no separate
  motion-estimation pass.
- **Cross-platform, no vendor lock-in.** Not tied to a proprietary
  optical-flow SDK or a specific vendor's hardware interpolation block --
  portable GLSL running through libplacebo's existing, already
  cross-platform GPU abstraction.
- **Single ffmpeg command.** No external tooling, no scripted multi-pass
  pipeline, no intermediate files -- this plugs directly into the same
  `-vf libplacebo=...` invocation you're already using.
- **Extensible.** The hook doesn't know or care what the shader does
  with the frames it's given -- motion compensation is one use, but
  temporal denoising, custom deinterlacing, or anything else that needs
  "this frame against the last one (or several)" fits the same interface.

## Costs and limitations

- **Requires a patched libplacebo.** This isn't merged upstream, so you
  are building against a patched library, not a stock release.
  [BUILDANDUSAGE.md](BUILDANDUSAGE.md) is the build guide for Linux,
  Windows and macOS, and the three build scripts in this directory do
  it end to end.
- **A fixed window per hook, not padded.** A hook's frame count is fixed
  for its lifetime (however many `FRAME<n>` names its own GLSL binds) and
  the renderer only ever fires it with *exactly* that many real frames --
  never fewer, via padding or repeated frames. This is deliberate --
  padding with repeated frames would need a "how many of these are real"
  count, which a shader author could forget to check, silently
  double-counting a padded frame. The cost is that a hook wanting a large
  window simply won't fire at all near a clip's start and end, where that
  many real frames don't yet exist.
- **Startup frame-hold.** Before enough real frames exist to fill a
  hook's declared window, output falls back to libplacebo's own
  zero-order-hold behaviour -- the same single decoded frame held across
  several consecutive output frames until the next one arrives. A wider
  window needs proportionally more lead-in (measured: a 4-frame window
  held frames 2-4 of a clip before real output took over on frame 5).
- **`PL_FRAME_MIX_MAX` (8) is a hard ceiling.** Not runtime-configurable;
  raising it means patching the constant and rebuilding. The shaders here
  bind 2, 3 and 4 frames; what a fifth would buy, and what it would cost,
  is worked out in [NFRAME-LIMITS.md](NFRAME-LIMITS.md).
- **Storage-cache textures have a fixed size ceiling.** A shader that
  uses `pair_changed` to drive a persistent `//!STORAGE` cache (as the
  interpolators here do) runs into an existing mpv-shader-format
  constraint, not something this patch adds: `//!TEXTURE`'s `//!SIZE`
  only accepts literal integers, unlike the `//!WIDTH`/`//!HEIGHT` on
  regular hook passes (which support expressions like `HOOKED.w 4 /`).
  So a cache texture can't size itself to the actual video resolution --
  it has to be allocated at a fixed ceiling (4K in the shaders here) up
  front, and a shader author needs to raise that ceiling explicitly to
  support larger sources. Source video larger than the configured ceiling
  reads and writes outside the allocated texture, which is undefined
  behaviour, not just wasted memory. **Untested above 1280x720**, the
  size everything in this repository has run at.
- **No automatic invalidation across discontinuities.** `pair_changed`
  is a straightforward signature comparison against the previous call on
  the same renderer -- it correctly detects an ordinary cut to a new
  window of frames, but hasn't been stress-tested against seeks or
  stream discontinuities specifically.
- **The shaders' own limits are documented with their results.** Where
  the motion estimator fails -- and it does, on rotation, on certain
  textures at certain speeds, and near the edges of its search reach --
  is measured and written down in [WHAT-WE-BUILT.md](WHAT-WE-BUILT.md),
  [NFRAME-LIMITS.md](NFRAME-LIMITS.md) and [tests/TESTING.md](tests/TESTING.md),
  with the same care as the successes. Nothing here should be attached
  to anything safety-critical.

## Testing status

Verified configurations. Anything not listed here is untested rather than
known-good -- treat it as a lead to confirm, not a claim.

| CPU / GPU | OS and build | Vulkan driver | Status |
|---|---|---|---|
| Intel i5-9500, UHD Graphics 630 iGPU (Coffee Lake, gen9) + Intel Arc A310 dGPU (Alchemist, gen12) | Debian, compiled against jellyfin-ffmpeg | Mesa | patch and shaders tested |
| Intel i9-9880H, AMD Radeon Pro 560X dGPU | Windows 26H1, WSL2 Ubuntu | Mesa lavapipe (software) | patch and shaders tested |
| Intel i9-9880H, AMD Radeon Pro 560X dGPU | Windows 26H1, native MSYS2/mingw-w64 | AMD proprietary (Boot Camp) | patch and shaders tested; ladder matches Linux to 0.01 dB |
| AMD Radeon RX 6600 eGPU (same machine, over Thunderbolt) | Windows 26H1, native MSYS2/mingw-w64 | AMD proprietary, Adrenalin 26.8.1 | patch and shaders tested; the Windows workhorse since 2026-09-02, when the eGPU's driver was replaced and it first appeared as a Vulkan device. Bit-reproducible run to run, ~2.1x the 560X, and field-matched to it. Every measurement in [NFRAME-LIMITS.md](NFRAME-LIMITS.md) and [THREEDIMENSIONAL.md](THREEDIMENSIONAL.md) was taken here |
| AMD Radeon RX 6600 eGPU, Radeon Pro 560X, UHD 630 (same machine) | macOS 15.7.9, Intel | MoltenVK 1.4.2 | patch and all shaders build and run; harness 10/10. Correctness target only: output is not bit-reproducible run to run, and the cause is upstream of this project -- see [BUILDANDUSAGE.md](BUILDANDUSAGE.md#macos) |
| Apple M2, 8-core GPU, unified memory | macOS 26.6.2, arm64 | MoltenVK 1.4.2 | patch and shaders tested; tri ladder matches the Windows numbers to 0.03 dB on five of seven reference cases; the interpolator diverges at the bit level but bounded (ladder scores move at most 0.25 dB). See [BUILDANDUSAGE.md](BUILDANDUSAGE.md#apple-silicon-measured-2026-09-01-m2) |
| NVIDIA, any | -- | -- | **untested** |

So the patch has run against four different Vulkan implementations -- Mesa
on Intel, Mesa lavapipe in software, AMD's proprietary Windows driver (two
generations of it, on two GPU architectures), and MoltenVK translating to
Metal -- on three operating systems, three compilers, and two CPU
architectures. The MoltenVK case is the strongest portability evidence,
because a translation layer shares no code with the others, and it has been
verified over two unrelated Metal stacks underneath (AMD silicon on the
Intel Mac, Apple's own GPU on the M2), with the M2 matching the Windows
ladder to hundredths of a dB.

## Verifying the N-frame case

Going from exactly two frames to a hook-declared N was a structural change
to `pl_hook_params`' fields, not an additive one, so it needed a real
build-and-run cycle to trust, not just a clean `git apply`.
[SHADERS.md](SHADERS.md) documents `nframe-smoketest.glsl`, a smoke-test
shader built for exactly this: it binds 4 frames at once and renders each
into its own grid cell with a diagnostic overlay (a distinct colour tag per
index, a frame-count readout, a per-frame timestamp bar, and the same
red/green `pair_changed` indicator the flow debug shader uses), so binding
more than 2 frames from a real GPU dispatch is something you can look at
rather than take on trust. Point `custom_shader_path` at it the same way as
any other shader here before relying on a wider window for anything real.
The three- and four-frame interpolators are the everyday users of the wider
window now; the smoke test remains the quick check that a build is sound.

## Usage

Point `custom_shader_path` at any `PL_HOOK_FRAME_MIX`-aware shader (see
[SHADERS.md](SHADERS.md)), and use `frame_mixer=custom_n` rather than
`linear`.

`custom_n` is a named entry this patch adds to libplacebo's own
`pl_frame_mixers[]` preset table (`src/renderer.c`) -- the same table
`vf_libplacebo.c` already does a plain string lookup against for
`frame_mixer=`, so no ffmpeg changes are needed for this either. It is a
direct alias for the existing `mitchell_clamp` entry (identical
`pl_filter_config`, radius 2.0), kept as a separate name because
`frame_mixer=mitchell_clamp` was accurate about the radius but misleading
about what happens: that kernel is *never* evaluated for the blend once a
`PL_HOOK_FRAME_MIX` hook is attached and fires -- `pl_render_image_mix`
intercepts and bypasses it -- and the radius is the only thing about it
that still matters, because it sets how far libplacebo searches for
candidate frames when building the queue. Using `mitchell_clamp` directly
still works identically.

```bash
./ffmpeg/ffmpeg \
    -init_hw_device drm=dr:/dev/dri/renderD129 \
    -init_hw_device vaapi=va@dr \
    -init_hw_device vulkan=vk@dr \
    -filter_hw_device vk \
    -hwaccel vaapi -hwaccel_output_format vaapi \
    -i "/share/sample.mp4" \
    -c:a copy -sn -dn \
    -vf "hwmap=derive_device=drm,format=drm_prime,\
libplacebo=format=p010le:fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation.glsl,\
format=vulkan,hwmap=derive_device=vaapi,format=vaapi" \
    -c:v hevc_vaapi -global_quality 20 \
    -y /share/output.mp4
```

`fps=` can be any target rate, including non-integer ratios (24->60 is the
one the ladder measures) -- `mix_t` and `rts_mix[]` come from the real frame
timestamps, not a fixed step. Setting `fps=` equal to the source rate, with
the companion patch applied, makes the shader run at N:N: no frames are
invented, and its diagnostic outputs become the measurement the rest of
this repository is about. [BUILDANDUSAGE.md](BUILDANDUSAGE.md) has the
Windows and macOS forms of the command, and
[tests/TESTING.md](tests/TESTING.md) the ground-truth harness that every
number in the other documents was produced by.

## Also in this directory

- **Patches.** [frame-mix-hook.patch](frame-mix-hook.patch), the hook
  stage above; [frame-mix-nn-threshold.patch](frame-mix-nn-threshold.patch),
  its N:N companion; and
  [hw-base-encode-eof-nullcheck.patch](hw-base-encode-eof-nullcheck.patch),
  an unrelated one-line fix for a genuine upstream ffmpeg bug (a NULL
  pointer dereference in `libavcodec/hw_base_encode.c` on early EOF
  flush) found while testing this project -- see the patch itself.
- **Build scripts.** `build-windows.ps1`, `build-windows.sh` and
  `build-macos.sh` build a patched ffmpeg end to end;
  [BUILDANDUSAGE.md](BUILDANDUSAGE.md) explains them.
- **Shaders** (in [shaders/](shaders/)). The two- to five-frame interpolators, each
  carrying a human-reading view that paints what the estimator is
  thinking over the picture (off by default, one shader parameter to
  switch on; one demonstration file has it on), and two small examples that exist to demonstrate the hook.
  A `-seeded` variant of each costs about a tenth more render time and
  is up on most of the ladder, and a `-propagated` one on top of it costs
  a further 1-4% and is up on every real segment measured and 2 dB on
  the ladder, with an `-animation` setting of it for hand-drawn content; [SHADERS.md](SHADERS.md) says which to use
  and why;
  [TRIDIRECTIONAL.md](TRIDIRECTIONAL.md), [QUADDIRECTIONAL.md](QUADDIRECTIONAL.md)
  and [QUINTDIRECTIONAL.md](QUINTDIRECTIONAL.md) are the records of the
  three-, four- and five-frame experiments, hypotheses stated before the
  results.
- **What it found.** [WHAT-WE-BUILT.md](WHAT-WE-BUILT.md) in plain
  language; [NFRAME-LIMITS.md](NFRAME-LIMITS.md) on where adding frames
  stops paying and why; [THREEDIMENSIONAL.md](THREEDIMENSIONAL.md) on what
  a two-dimensional field can and cannot say about motion in depth;
  [PRIOR-ART.md](PRIOR-ART.md) on where all of it sits in the record.
- **How it was done.** [METHODOLOGY.md](METHODOLOGY.md) on the working
  method and how to re-establish it; [tests/TESTING.md](tests/TESTING.md)
  and [tests/TOOLS.md](tests/TOOLS.md) on the harness and its
  instruments; [PLAN.md](PLAN.md) on what is next and what was refuted on
  the way.
- **A native port.** [metal-demo/](metal-demo/) is the four-frame shader
  machine-translated to Metal and wrapped in a small macOS app, with
  [METALPORT.md](METALPORT.md) as its record and `QuadDemo-macos-arm64.zip`
  as the built artefact.
