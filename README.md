# N-Frame temporal analysis via ffmpeg and a patched libplacebo

## What this is

[frame-mix-hook.patch](frame-mix-hook.patch) is a small patch to
[libplacebo](https://code.videolan.org/videolan/libplacebo), the GPU rendering library that ffmpeg's `libplacebo`
filter is built on. It adds a custom-shader hook stage, `PL_HOOK_FRAME_MIX`, that hands a user-supplied GLSL shader
(the `.hook` format that mpv and ffmpeg already load through `custom_shader_path`) a whole *window* of source frames
at once, from 1 up to 8, with the exact timing between them. Stock libplacebo gives such a shader one
already-blended frame. A companion patch to ffmpeg's filter,
[frame-mix-nn-threshold.patch](frame-mix-nn-threshold.patch), lets that window fire when the output rate equals the
input rate, and makes room in the frame queue for windows of five frames or more.

Anything that needs to reason across time rather than within one frame then becomes a shader in an ordinary
`ffmpeg` command: motion-compensated interpolation, temporal denoising, custom deinterlacing, scene-cut-aware
effects.

What was built on it here is a family of shaders that look at two to six frames at once and write out, for every
point on the screen, where things are moving and how that motion is changing. Because they run at the video's own
frame rate as readily as at a higher one, what they produce can be a measurement rather than a picture.

- [WHAT-WE-BUILT.md](WHAT-WE-BUILT.md): what that turned out to be good for, where it fails, and what it was
  measured against, in plain language. It also maps every document in this directory.
- [WHAT-IS-ACTUALLY-HAPPENING-HERE.md](WHAT-IS-ACTUALLY-HAPPENING-HERE.md): what a shader is and why this matters
  to a scientist, written by the human collaborator for readers with no background.
- [WHAT-IT-CAN-MEASURE.md](WHAT-IT-CAN-MEASURE.md): what each shader reads, and how well.

## Where it has run

Anything not listed is untested rather than known to work.

| GPU | OS and build | Vulkan driver | Status |
|---|---|---|---|
| Apple M5 | macOS 27.0.1, arm64 | MoltenVK 1.4.2 | the main development host since 2026-09-11; `smoke.sh` 17 of 17 at the current pins (2026-10-01) |
| Intel Arc A310 (beside a UHD 630) | Debian: jellyfin-ffmpeg (the 2026-09-04 production build); and since 2026-09-30 a Debian trixie container at the current pins | Mesa | patch and shaders tested; the container is exactly reproducible run to run, so a shader is gated there in one run |
| AMD Radeon RX 6600 eGPU | Windows, MSYS2 / mingw-w64 | AMD, Adrenalin 26.8.1 | patch and shaders tested; the Windows workhorse from 2026-09-02; reproducible run to run; most of the measurements in [NFRAME-LIMITS.md](NFRAME-LIMITS.md) up to mid-September, and those in [THREEDIMENSIONAL.md](THREEDIMENSIONAL.md), were taken here |
| AMD Radeon Pro 560X | Windows, MSYS2 / mingw-w64 | AMD (Boot Camp) | patch and shaders tested; the ladder matched Linux to 0.01 dB |
| RX 6600 eGPU, Radeon Pro 560X, UHD 630 (an Intel MacBook Pro) | macOS 15.8 (15.7.9 when first built) | MoltenVK 1.4.2 | patch and shaders build and run; `smoke.sh` 15 of 15 at the current pins (2026-09-30) |
| Apple M2, 8-core GPU | macOS 26.6.2, arm64 | MoltenVK 1.4.2 | tested 2026-09-01; the three-frame ladder matched Windows to 0.03 dB on five of seven reference cases ([BUILDANDUSAGE.md](BUILDANDUSAGE.md#apple-silicon-measured-2026-09-01-m2)) |
| Radeon Pro 560X, through WSL2 | Ubuntu under WSL2 | Mesa lavapipe (software) | tested in August 2026; this setup was retired on 2026-09-19 |
| NVIDIA, any | -- | -- | **untested** |

On macOS the results wandered from run to run until two of MoltenVK's own switches were found that end it; the
test harness sets them. The record is
[MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md). The exact ffmpeg and libplacebo
commits each host was verified at are in [BUILDANDUSAGE.md](BUILDANDUSAGE.md#status-and-pins).

## Trying it

You need an ffmpeg built against the patched libplacebo. [BUILDANDUSAGE.md](BUILDANDUSAGE.md) covers Linux (by
hand, or in a container), Windows and macOS, and the scripts beside it ([build-macos.sh](build-macos.sh),
[build-windows.ps1](build-windows.ps1), [linux/build-linux.sh](linux/build-linux.sh)) do it end to end. Then, with
software decode:

```bash
ffmpeg -init_hw_device vulkan=vk -filter_hw_device vk -i input.mkv \
  -vf "libplacebo=fps=60:frame_mixer=custom_n:custom_shader_path=bidirectional-interpolation-variational-propagated.glsl,format=yuv420p" \
  -c:v libx264 -crf 18 output.mkv
```

Run it from the [shaders/](shaders/) directory, or copy the shader beside your files: a path inside a filter
argument should be relative. [SHADERS.md](SHADERS.md), "Which one to use", says which shader fits which job.
`fps=` can be any rate, including non-integer ratios. Set it equal to the source's rate (with the companion patch)
and no frames are invented: the shader's diagnostic outputs become the measurement.

## Limits, briefly

- **Patched builds are required.** Neither patch is merged upstream.
- **A fixed window, and a short hold at the start.** A shader fires only when its full window of real frames
  exists, so near a clip's first and last frames the builtin mixer draws instead (see the reference below).
- **Eight frames at most** (`PL_FRAME_MIX_MAX`), fixed at build time.
- **Storage caches have a size ceiling** set in the shader: the unscaled shaders fit sources up to 3840 wide, and
  the `-4k` versions up to 7680 (see the reference below).
- **The motion estimator has measured failure cases** (rotation, certain textures at certain speeds, motion
  beyond its search reach), written down with the same care as the successes. Nothing here should be attached to
  anything safety-critical.

## Where to go next

[WHAT-WE-BUILT.md](WHAT-WE-BUILT.md) ends with a map of every document here, grouped by what a reader is looking
for: the plain-language account, building and running, the experiments by window size, the research record, the
instruments, the scientific record the work leaned on, and the rules the work follows.

---

## Reference: the hook, for review

### Why it's needed

Stock libplacebo's `frame_mixer` option
(`linear`/`oversample`/`mitchell_clamp`/`hermite`) is a fixed 1D temporal
blend kernel -- it can cross-fade between frames on a timeline, but it has
no concept of motion, and no way for a custom shader to see more than one
frame. `custom_shader_path` hooks only ever receive a single,
already-composited texture (confirmed by reading `pl_render_image_mix` in
`src/renderer.c` directly). There was no way to write a GPU shader that
looks at two frames and reasons about what changed between them, which is
the basic operation behind most temporal video techniques.

This patch closes that gap at the library level rather than in any one
shader, so any custom shader -- from a one-line cross-fade to a full
motion-estimation pipeline -- can opt into it. It runs as ordinary shaders
inside the existing `libplacebo` filter, in one ffmpeg command, with no
vendor SDK and no intermediate files.

### What's new

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
- **A skipped window is loud.** When the queue cannot fill the declared
  window (a clip's first and last frames, or a host fault), the hook is
  skipped and the builtin mixer draws the frame, and the patch says so at
  error level on every such frame. Set `PL_FRAME_MIX_STRICT` in the
  environment and it paints the frame magenta instead, so a miss can never
  pass for a result.
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
  get the queue radius it happens to need. Currently an alias for
  `mitchell_clamp`'s existing config, not a new filter (below).
- **N:N operation** (the companion patch) -- libplacebo's frame queue
  quietly collapses to a single-frame mix whenever the output rate is
  within its interpolation threshold of the input rate, which for a
  matched rate is exactly 0, and the hook never fires. The second patch
  disables that collapse only while a `PL_HOOK_FRAME_MIX` hook is
  attached, so a shader can see its full window at the source's own
  frame rate. That is what makes the shaders usable as instruments
  rather than only as interpolators. It also sizes the queue's lookahead
  to a declared window of more than four frames (four fit the default
  radius, and keep it, so their published numbers stand; without the
  patch a five-frame hook silently gets the builtin mixer on some frames).

`fps=`, frame pacing, `custom_shader_path` loading and `frame_mixer=` string
lookup all already existed in `vf_libplacebo.c`. So frame-rate scaling with a
window of up to four frames needs only the libplacebo patch; the N:N case and
windows of five or more frames need the ffmpeg-side patch as well.

### `frame_mixer=custom_n`

Point `custom_shader_path` at any `PL_HOOK_FRAME_MIX`-aware shader and use
`frame_mixer=custom_n` rather than `linear`. `custom_n` is a named entry this
patch adds to libplacebo's own `pl_frame_mixers[]` preset table
(`src/renderer.c`) -- the same table `vf_libplacebo.c` already does a plain
string lookup against for `frame_mixer=`, so no ffmpeg change is needed for
it. It is a direct alias for the existing `mitchell_clamp` entry (identical
`pl_filter_config`, radius 2.0), kept as a separate name because
`frame_mixer=mitchell_clamp` was accurate about the radius but misleading
about what happens: that kernel is *never* evaluated for the blend once a
`PL_HOOK_FRAME_MIX` hook is attached and fires -- `pl_render_image_mix`
intercepts and bypasses it -- and the radius is the only thing about it
that still matters, because it sets how far libplacebo searches for
candidate frames when building the queue. Using `mitchell_clamp` directly
still works identically.

`mix_t` and `rts_mix[]` come from the real frame timestamps, not a fixed
step, so any target rate works. [BUILDANDUSAGE.md](BUILDANDUSAGE.md#using-it)
has the hardware-decode forms of the command (VAAPI on Linux, VideoToolbox on
macOS).

### Costs and limitations, in full

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
  bind 2 to 6 frames; where adding frames stops paying is worked out in
  [NFRAME-LIMITS.md](NFRAME-LIMITS.md).
- **Storage-cache textures have a fixed size ceiling.** A shader that
  uses `pair_changed` to drive a persistent `//!STORAGE` cache (as the
  interpolators here do) runs into an existing mpv-shader-format
  constraint, not something this patch adds: `//!TEXTURE`'s `//!SIZE`
  only accepts literal integers, unlike the `//!WIDTH`/`//!HEIGHT` on
  regular hook passes (which support expressions like `HOOKED.w 4 /`).
  So a cache texture can't size itself to the actual video resolution --
  it has to be allocated at a fixed ceiling up front, and a shader author
  needs to raise that ceiling explicitly to support larger sources. Source
  video larger than the configured ceiling reads and writes outside the
  allocated texture, which is undefined behaviour, not just wasted memory.
  The ceilings as shipped: the unscaled shaders' caches fit sources up to
  3840 wide (a 4096-wide DCI master would overrun them); the `-4k` versions
  (made by `tests/scale_shader.py`, see [SHADERS.md](SHADERS.md)) halve every
  level's texel count and their caches fit 7680 wide, so UHD and DCI are both
  inside them. Measured at 3840x2160 and, from 2026-09-06, on real 3840x2076
  ten-bit films; nothing wider has been run.
- **No automatic invalidation across discontinuities.** `pair_changed`
  is a straightforward signature comparison against the previous call on
  the same renderer -- it correctly detects an ordinary cut to a new
  window of frames, but hasn't been stress-tested against seeks or
  stream discontinuities specifically.
- **Tested on Vulkan only.** libplacebo also has OpenGL and D3D11
  backends; the hook has not been run on them.

### Verifying the N-frame case

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
The three- to six-frame shaders are the everyday users of the wider window;
the smoke test remains the quick check that a build is sound.

### The patches

- [frame-mix-hook.patch](frame-mix-hook.patch): the hook stage above (libplacebo).
- [frame-mix-nn-threshold.patch](frame-mix-nn-threshold.patch): its companion in ffmpeg's filter, for N:N and for
  windows of five or more frames.
- [hw-base-encode-eof-nullcheck.patch](hw-base-encode-eof-nullcheck.patch): an unrelated one-line fix for an
  upstream ffmpeg bug (a NULL pointer dereference in `libavcodec/hw_base_encode.c` on an early EOF flush), found
  while testing this project.
