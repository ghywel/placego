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
between them, instead of a single already-blended texture.

[SHADERS.md](SHADERS.md) documents the shaders built on this patch,
[tests/TESTING.md](tests/TESTING.md) the ground-truth harness, and
[METHODOLOGY.md](METHODOLOGY.md) how the whole thing was actually
developed and how to re-establish the loop that did it.

Everything downstream of that -- motion-compensated interpolation,
temporal denoising, custom deinterlacing, scene-cut-aware effects, or
anything else that needs to reason across time rather than within a
single frame -- is then just a GLSL shader, running as part of one
ordinary `ffmpeg` command. [SHADERS.md](SHADERS.md) documents a working
bidirectional interpolation shader built on top of it, as a worked
example -- using exactly 2 frames, the common and most-tested case (see
"Verifying the N-frame case" below for how a wider window is checked).

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
  `FRAME0`/`FRAME1`, the common 2-frame case). The renderer only fires
  the hook once it can supply exactly that many frames -- fewer (e.g. the
  first/last couple of output frames in a clip) fall back to the builtin
  blend instead, needing proportionally more lead-in frames the larger
  the window.
- **`mix_t`** -- the output frame's normalized position between the first
  two frames (0.0 at `FRAME0`, 1.0 at `FRAME1`), provided as a convenience
  for the common two-frame case. Not well-defined for three or more
  points, so it's left unset for hooks wanting more than 2 frames.
- **`rts_mix[]`** -- the raw relative timestamps every frame in the
  window was selected at, for a shader that needs the actual frame
  spacing (e.g. to detect a scene cut or VFR discontinuity) or wants to
  build its own weighting across more than two frames.
- **`num_mix`** -- how many frames are actually in the window this call
  (always exactly what the hook declared, once it fires at all).
- **`pair_changed`** -- true only when the whole window of source frames
  has actually changed since the previous call, false when this is just
  another output frame within the *same* window (only relative position
  moved). Lets a shader maintain a persistent GPU-side cache (via the
  existing mpv-shader `//!TEXTURE ... //!STORAGE` directive) of expensive
  per-window work -- e.g. a motion vector field -- and skip recomputing it
  for every output frame at non-integer fps ratios.
- **`frame_mixer=custom_n`** -- a new named entry in libplacebo's own
  frame-mixer preset table specifically for this use case, so the ffmpeg
  command line doesn't have to name an unrelated cubic kernel
  (`mitchell_clamp`) to get the queue radius it happens to need (see
  Usage below). Currently just an alias for `mitchell_clamp`'s existing
  config, not a new filter.

None of this requires any ffmpeg source changes -- `fps=`, frame pacing,
`custom_shader_path` loading, and `frame_mixer=` string lookup all
already existed in `vf_libplacebo.c` unmodified. Only libplacebo needs
the patch.

## Benefits

- **Real-time, GPU-native.** Runs as ordinary GLSL/compute shaders on
  whatever GPU backend libplacebo already targets (Vulkan, OpenGL,
  D3D11) -- no CPU round-trip, no separate motion-estimation pass.
- **Cross-platform, no vendor lock-in.** Not tied to a proprietary
  optical-flow SDK or a specific vendor's hardware interpolation block --
  it's portable GLSL running through libplacebo's existing, already
  cross-platform GPU abstraction.
- **Single ffmpeg command.** No external tooling, no scripted multi-pass
  pipeline, no intermediate files -- this plugs directly into the same
  `-vf libplacebo=...` invocation you're already using.
- **Extensible.** The hook doesn't know or care what the shader does
  with the frames it's given -- motion compensation is one use, but
  temporal denoising, custom deinterlacing, or anything else that needs
  "this frame vs. the last one (or several)" fits the same interface.

## Costs and limitations

- **Requires a patched libplacebo.** This isn't merged upstream (yet --
  see below), so you're building against a patched library, not a stock
  release.
- **A fixed window per hook, not padded.** A hook's frame count is fixed
  for its lifetime (however many `FRAME<n>` names its own GLSL binds) and
  the renderer only ever fires it with *exactly* that many real frames --
  never fewer, via padding or repeated frames. This is deliberate --
  padding with repeated frames would need a "how many of these are real"
  count, which a shader author could forget to check, silently
  double-counting a padded frame. The cost is that a hook wanting a large
  window simply won't fire at all near a clip's start/end, where that
  many real frames don't yet exist.
- **Startup frame-hold, and a possible small A/V offset for wider
  windows.** Before enough real frames exist to fill a hook's declared
  window, output falls back to libplacebo's own zero-order-hold behavior
  -- the same single decoded frame held across several consecutive output
  frames until the next one arrives. For the common 2-frame case this is
  one or two held frames, with no observed sync drift across all testing
  to date. A wider window needs proportionally more lead-in (confirmed on
  real hardware: a 4-frame window held frames 2-4 of a clip before real
  output took over on frame 5) -- and with a 4-frame window specifically,
  audio was observed drifting from video by roughly 3 frames over a
  60-second clip. The likely mechanism is that extra startup hold, but
  this hasn't been root-caused at the code level -- it isn't yet
  confirmed whether this is a fixed, one-time startup offset (bounded,
  and probably not worth fixing) or something that could compound over a
  longer file. Treat wider-window output as needing an A/V sync check;
  the 2-frame case hasn't shown this problem.
- **`PL_FRAME_MIX_MAX` (8) is a hard ceiling.** Not runtime-configurable;
  raising it means patching the constant and rebuilding. Chosen as
  generous headroom over realistic use (the shaders in this directory
  only need 2) rather than tuned against any specific larger use case.
- **Storage-cache textures have a fixed size ceiling.** A shader that
  uses `pair_changed` to drive a persistent `//!STORAGE` cache (as the
  example shader does) runs into an existing mpv-shader-format
  constraint, not something this patch adds: `//!TEXTURE`'s `//!SIZE`
  only accepts literal integers, unlike the `//!WIDTH`/`//!HEIGHT` on
  regular hook passes (which support expressions like `HOOKED.w 4 /`).
  So a cache texture can't size itself to the actual video resolution --
  it has to be allocated at a fixed ceiling (e.g. 4K) up front, and a
  shader author needs to explicitly raise that ceiling to support larger
  sources. Source video larger than the configured ceiling reads/writes
  outside the allocated texture, which is undefined behavior, not just
  wasted memory. **Untested above 1080p**, including this exact scenario.
- **No automatic invalidation across discontinuities.** `pair_changed`
  is a straightforward signature comparison against the previous call on
  the same renderer -- it correctly detects an ordinary cut to a new
  window of frames, but hasn't been stress-tested against seeks or
  stream discontinuities specifically.

## Testing status

No known issues with the libplacebo patch at this time

## Verifying the N-frame case

Going from exactly-2-frames to a hook-declared N was a structural change
to `pl_hook_params`' fields (not an additive one), so it needed an actual
build-and-run cycle to trust, not just a clean `git apply`.
[SHADERS.md](SHADERS.md) documents `nframe-smoketest.glsl`, a
smoke-test shader built specifically for this: it binds 4 frames at once
and renders each one into its own grid cell with a diagnostic overlay (a
distinct color tag per index, a frame-count readout, a per-frame
timestamp bar, the same red/green `pair_changed` indicator the flow
debug shader uses), so binding more than 2 frames from a real GPU
dispatch is something you can actually look at rather than just trust.
Point `custom_shader_path` at it the same way as any other shader here to
check it before relying on a wider window for anything real.

## Building

In this project testing was performed against [jellyfin-ffmpeg 8.1](https://github.com/jellyfin/jellyfin-ffmpeg)
There is already a patch against libplacebo in builder/patches/libplacebo
place the frame-mix-hook.patch file in here and build as normal with
./build trixie amd64 for example. For normal ffmpeg builds apply the patch
and build as normal. It is also recommended to apply the
hw-base-encode-eof-nullcheck.patch to src/libavcodec/hw_base_encode.c
to fix an unpatched ffmpeg null pointer dereference bug that causes
a segfault when seeking input with a fps= scaled output.

Example ffmpeg build:
```bash
# 1. Patch and build libplacebo
git clone https://code.videolan.org/videolan/libplacebo.git
cd libplacebo
git apply /path/to/frame-mix-hook.patch
meson setup build -Dvulkan=enabled -Dprefix=/opt/libplacebo-mc
ninja -C build install

# 2. Build ffmpeg against it (no ffmpeg source changes needed)
git clone https://github.com/FFmpeg/FFmpeg.git ffmpeg
cd ffmpeg
export PKG_CONFIG_PATH=/opt/libplacebo-mc/lib/x86_64-linux-gnu/pkgconfig
./configure --enable-libplacebo --enable-vulkan --enable-vaapi \
    --extra-ldflags="-Wl,-rpath,/opt/libplacebo-mc/lib/x86_64-linux-gnu"
make -j$(nproc)
```

Adjust the pkg-config path to match wherever `meson`/`ninja install`
actually put it on your distro (`find /opt/libplacebo-mc -name 'libplacebo.pc'`).

## Usage

Point `custom_shader_path` at any `PL_HOOK_FRAME_MIX`-aware shader (see
[SHADERS.md](SHADERS.md)), and use `frame_mixer=custom_n` rather than
`linear`.

`custom_n` is a new named entry this patch adds to libplacebo's own
`pl_frame_mixers[]` preset table (`src/renderer.c`) -- the same table
`vf_libplacebo.c` already does a plain string lookup against for
`frame_mixer=`, so no ffmpeg changes are needed for this either. For now
it's a direct alias for the existing `mitchell_clamp` entry (identical
`pl_filter_config`, radius 2.0), kept as a separate name specifically
because `frame_mixer=mitchell_clamp` was accurate about the radius but
misleading about what's actually happening: that kernel is *never*
evaluated for the blend itself once a `PL_HOOK_FRAME_MIX` hook is
attached and fires -- `pl_render_image_mix` intercepts and bypasses it
entirely, and radius is the only thing about it that still matters (it's
what determines how far libplacebo searches for candidate frames when
building the queue; the hook always picks exactly the frames that
bracket the target timestamp regardless of how many extra frames a wider
radius pulls in, so there's no downside to the larger radius). Using
`mitchell_clamp` directly still works identically -- `custom_n` is a
clearer name for the same thing, not a behavior change.

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

`fps=` can be any target rate, including non-integer ratios (e.g.
24->60) -- `mix_t` is computed from the real frame timestamps, not a
fixed step. (`bidirectional-interpolation.glsl`, shown above, has only
actually been tested end to end at `fps=60` so far; N:N ratios like
`24->24` have been confirmed with `motion-edges-dual.glsl` instead.)

## Also in this directory

[hw-base-encode-eof-nullcheck.patch](hw-base-encode-eof-nullcheck.patch)
is an unrelated one-line fix for a genuine upstream ffmpeg bug (a NULL
pointer dereference in `libavcodec/hw_base_encode.c` on early EOF flush)
found while testing this project -- see the patch file itself for
details.
