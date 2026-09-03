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

[BUILDANDUSAGE.md](BUILDANDUSAGE.md) is the build guide for Linux
and Windows. [SHADERS.md](SHADERS.md) documents the shaders built on it,
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
- **Startup frame-hold.** Before enough real frames exist to fill a hook's declared
  window, output falls back to libplacebo's own zero-order-hold behavior
  -- the same single decoded frame held across several consecutive output
  frames until the next one arrives. A wider window needs proportionally
  more lead-in (confirmed on real hardware: a 4-frame window held frames
  2-4 of a clip before real output took over on frame 5) 
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

Verified configurations. Anything not listed here is untested rather than
known-good -- treat it as a lead to confirm, not a claim.

| CPU / GPU | OS and build | Vulkan driver | Status |
|---|---|---|---|
| Intel i5-9500, UHD Graphics 630 iGPU (Coffee Lake, gen9) + Intel Arc A310 dGPU (Alchemist, gen12) | Debian, compiled against jellyfin-ffmpeg | Mesa | patch and shaders tested |
| Intel i9-9880H, AMD Radeon Pro 560X dGPU | Windows 26H1, WSL2 Ubuntu | Mesa lavapipe (software) | patch and shaders tested |
| Intel i9-9880H, AMD Radeon Pro 560X dGPU | Windows 26H1, native MSYS2/mingw-w64 | AMD proprietary | patch and shaders tested; ladder matches Linux to 0.01 dB |
| AMD Radeon RX 6600 eGPU (same machine, over Thunderbolt) | Windows 26H1, native MSYS2/mingw-w64 | AMD proprietary, Adrenalin 26.8.1 | patch and shaders tested; **now the Windows workhorse.** Until 2026-09-02 it never appeared as a Vulkan device: the Boot Camp package bound it to a Polaris-era driver whose Vulkan ICD did not know the chip. Binding the current Adrenalin driver to the 6600 alone (the 560X keeps its Boot Camp driver) makes both GPUs enumerate under plain Vulkan. Bit-reproducible run to run, ~2.1x faster than the 560X, and its O5 acceleration field matches the 560X's to three decimals on 19 of 20 frames. Every measurement in [NFRAME-LIMITS.md](NFRAME-LIMITS.md) and [THREEDIMENSIONAL.md](THREEDIMENSIONAL.md) was taken on it |
| AMD Radeon RX 6600 eGPU, Radeon Pro 560X, UHD 630 (same machine) | macOS 15.7.9, Intel | MoltenVK 1.4.2 | patch and all shaders build and run; harness 10/10. **Correctness target only -- output is not bit-reproducible run to run, for reasons upstream of this project.** Investigated and closed; see [BUILDANDUSAGE.md](BUILDANDUSAGE.md#macos) |
| Apple M2, 8-core GPU, unified memory | macOS 26.6.2, arm64 | MoltenVK 1.4.2 | patch and shaders tested; tri ladder matches the Windows numbers to ≤0.03 dB on five of seven reference cases; full quad ladder run here first; stock linear is bit-reproducible (0/60 frames differ) while the interpolator diverges at the bit level but bounded — ladder scores move ≤0.25 dB. See [BUILDANDUSAGE.md](BUILDANDUSAGE.md#apple-silicon-measured-2026-09-01-m2) |
| NVIDIA, any | -- | -- | **untested** |

So the patch has run against four different Vulkan implementations -- Mesa on
Intel, Mesa lavapipe in software, AMD's proprietary Windows driver (two
generations of it, on two GPU architectures), and MoltenVK translating to
Metal -- on three operating systems, three compilers, and now two CPU
architectures. The MoltenVK case is the strongest
portability evidence here, because a translation layer shares no code with
the others -- and it has now been verified over two unrelated Metal stacks
underneath (AMD silicon on the Intel Mac, Apple's own GPU on the M2), with
the M2 matching the Windows ladder to hundredths of a dB. It has never run
on NVIDIA hardware.

### The macOS (Intel) case, closed

Worth reading before anyone spends time on it, because the conclusion is not
the obvious one.

**The patch and shaders are portable to macOS.** Everything builds against
MoltenVK, all nine shaders compile and run, the full harness passes 10/10, and
the RX 6600 eGPU is enumerated and selected as a Vulkan device -- which is more
than the same card manages under Windows on the same machine.
`VK_KHR_push_descriptor`, long the suspected blocker, is supported and used
without incident.

**But macOS output is not bit-reproducible, and that is not this project's
bug.** Repeated identical runs diverge. The cause was investigated and traced
*upstream*: a baseline nondeterminism exists in the Vulkan/MoltenVK path
itself, present even with stock `frame_mixer=linear` and no custom shader or
storage images at all, while the identical CPU-only path is exactly
reproducible. The interpolator amplifies it enormously because block matching
selects an argmin -- one LSB at a tie flips a motion vector and ruins a whole
frame group. Severity scales with how far the GPU's memory sits from the CPU:
worst on a Thunderbolt eGPU, twenty times milder on the integrated GPU. The
flow cache was ruled out by experiment; synchronization validation reports no
hazards.

**There is no way around it on macOS, because there is no other backend.**
libplacebo's README advertises OpenGL and Direct3D 11 alongside Vulkan, but
ffmpeg instantiates only the Vulkan backend -- `vf_libplacebo.c` has zero
references to either -- and macOS OpenGL is frozen at 4.1, lacking both the
image load/store (4.2) and compute shaders (4.3) that the `//!STORAGE` flow
cache requires. Both were verified rather than assumed.

**So: treat macOS as a portability and correctness target, not a measurement
one.** A run there proves the shaders execute correctly under a translation
layer, which is a genuinely strong portability claim. Do not tune parameters
against its numbers, and do not compare one of its figures against Linux or
Windows. If you must measure on macOS, select the integrated GPU -- it is
twenty times better behaved, though still not clean.

**This says nothing about Apple Silicon**, which shares neither the eGPU, the
memory architecture, nor the GPU driver. All of the above is Intel-specific
and would need re-measuring there.

See [BUILDANDUSAGE.md](BUILDANDUSAGE.md) for how to build it on Linux,
Windows or macOS, and [tests/TESTING.md](tests/TESTING.md) for what the measurements
mean.


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

