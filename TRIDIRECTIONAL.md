# Tridirectional interpolation: encoding acceleration, not just velocity

**Status: hypothesis CONFIRMED -- up to +4.45 dB over the bidirectional
shader, winning on eight of nine benchmark cases, with the gain rising as
acceleration rises exactly as the model predicts. Caching now works. One
regression remains (3.8 dB on L1_trans_8px) and is PROVED unfixable at three
frames. A demonstration that the hypothesis is true, not yet production code.**

This is a research log, kept in the shape the result actually arrived in
rather than tidied into a conclusion it has not earned.

## What this is actually for

**The interpolated frames are not the product. The flow field is.**

That reframing came from the human collaborator after the first real-hardware run, and it is
worth stating before the rest of this document, because it changes what
"success" means here. A motion field that encodes ACCELERATION as well as
velocity is a measurement of the scene, and one that appears not to have
existed as a real-time GPU primitive before. The interpolator is the harness
that made it testable -- a way to check the field against ground truth by
seeing whether it puts content in the right place -- rather than the
deliverable.

Read the rest of this file with that in mind. The PSNR ladder is an instrument
for validating the field, not a claim that this is a better way to make films
look smooth. The `TRI_DIAG` outputs and `tests/trivis.py` are, on that reading,
closer to the actual product than `TRI_DIAG = 0` is.

It also reorders what matters next. Extraction and export of the field, its
units and calibration, and its behaviour on real scenes matter more than
squeezing dB out of the warp.

## The two use cases, and why N:N is the important one

They are different modes with different requirements, and only one of them is
about video.

**Frame-rate scaling (24 -> 60).** The interpolator. Acceleration earns its
place by putting accelerating content in the right position instead of on the
constant-velocity straight line. Measured at up to +4.45 dB. This is the
corollary use.

**Flow field direct (N:N -- 24p -> 24p, 60p -> 60p, 200p -> 200p).** No frame
insertion at all. The output picture is irrelevant; the deliverable is the
per-texel field, one reading per source frame, handed to whatever consumes it.
The autonomous-vehicle shape is the clearest example: camera stream in, GPU
does the N-frame analysis, the field goes to a system that decides what the
acceleration of a pedestrian or another vehicle *means*. The shader is the
pre-processing stage, not the decision-maker.

N:N is also the better-conditioned mode on paper. The output coincides with a
source frame, so the window sorts to `{S_k-1, S_k, S_k+1}` with
`rts = {-D, 0, +D}`: `s = 0`, the anchor lands on `S_k` itself, and the
estimate is a **centred second difference at the current frame** rather than
an off-centre one. Symmetric stencil, no mid-interval phase flip.

### Exact N:N did not fire -- found, diagnosed, and fixed

**The symptom.** Using the `TRI_DIAG` corner marker to detect whether the hook
ran at all, from a 24p source: it fired at 24.5, 25, 30, 36, 48 and 60, and
never at exactly 24. The picture at 24 passed through at 71.7 dB, which is
also what a correct `s = 0` passthrough looks like -- so the prediction "the
picture should pass through cleanly" was *confirmed by a run in which the
shader never executed*. The passthrough was libplacebo's fallback. Only the
marker separated the two. **A diagnostic that proves the code ran is worth
more than a result that looks right.**

**The cause**, from libplacebo's own trace rather than inference. At fps=24
the renderer logged 7 "Considering image" lines for 7 output frames -- exactly
one candidate frame each, and 7 "Single frame not found in cache, bypassing".
At 24.5 it logged 30 candidates and dispatched the hook 7 times with
`num_frames=3`. So the queue was handing the renderer a **one-frame mix**.

In `src/utils/frame_queue.c`, `interpolate()` falls back to `nearest()` --
which returns `.num_frames = 1` -- whenever

    |fps_estimate / vps_estimate - 1| <= interpolation_threshold

and the default threshold is `1e-6`. At a matched rate that ratio is 0. The
single-frame mix then sets `single_frame` in `pl_render_image_mix`, which both
excludes every frame but the reference and (with ffmpeg's
`skip_caching_single_frame`, set whenever output fps >= input fps) bypasses to
`fallback` before the hook is ever reached. **Two gates, both closing only at
matched rates.**

Entirely correct behaviour for a frame *mixer*: interpolating when the rates
already match is a pointless blur. Wrong for a FRAME_MIX *analysis* hook,
which wants its window regardless of what the output rate is.

**The prediction that confirmed it.** A `1e-6` threshold means the trigger is
exact rate equality, not a broad band -- so the boundary should sit between
24.00001 (ratio 4.17e-07) and 24.0001 (4.17e-06). Measured:

| rate | ratio | hook fires |
|---|---|---|
| 24 | 0 | no |
| 24.00001 | 4.17e-07 | no |
| **24.0001** | **4.17e-06** | **yes** |
| 24.001 ... 24.5 | >= 4.17e-05 | yes |

The boundary landed exactly where the threshold predicts. Had the cause been
something vaguer about "matched rates", everything below ~24.24 would have
failed instead.

**The fix** is one addition to `vf_libplacebo.c` (kept as
`frame-mix-nn-threshold.patch`): when any attached hook declares
`PL_HOOK_FRAME_MIX`, pass a negative `interpolation_threshold`, which a
non-negative ratio can never satisfy. It is deliberately scoped to that case
so behaviour is untouched for everyone else. The threshold belongs to the
queue, and the queue knows nothing about hooks -- ffmpeg owns both, so this is
the layer where the two facts meet.

**Verified after rebuilding:**

- the hook fires at 24, 23, 25, 30 and 60 -- every rate tested
- **24 source frames in, 24 out**: true 1:1, and the trailing boundary frame
  that the 24.0001 workaround produced is gone
- the field calibration at true 24:24 is identical to 24 -> 60 and to the
  24.0001 workaround, digit for digit (-8.275 -> -7.750 at 6.4%,
  +7.420 -> +7.453 at 0.5%, -4.284 -> -4.250 at 0.8%)
- no hook + matched rate still point-samples (71.61 dB worst, unchanged)
- the 2-frame bidirectional shader still renders at 24 -> 60, and now also
  renders at 24 -> 24, which was previously impossible

The flow-field use case now works at its native rate. If running against an
unpatched ffmpeg, requesting 24.0001 instead of 24 is a complete workaround:
it clears the threshold by 4x while the rates diverge by one frame only after
~240,000 frames, about 2.8 hours.

### One frame of latency, and the causal variant

Worth stating for the autonomous-vehicle framing, because it is a property of
the estimator rather than of this implementation. The centred second
difference at `S_k` needs `S_k+1`, so a reading about the current frame cannot
be produced until the next frame arrives: **the field carries one frame of
latency**, 42 ms at 24p, 5 ms at 200p.

For true real-time sensing the window would have to be causal --
`{S_k-2, S_k-1, S_k}`, fitting the same quadratic but *extrapolating* the
estimate to `S_k` instead of interpolating to the centre. That is a different
and noisier estimator (extrapolation amplifies the same quantisation the
calibration already shows dominating the low end) and it has not been built or
measured. It is the obvious next thing to try for that use case.

### High frame rates make acceleration HARDER, not easier

This follows from the calibration and is worth stating before anyone reaches
for a 200p sensor expecting a better field.

Acceleration is measured in px per source-interval squared, so a fixed
physical acceleration in px/s² scales as `1/fps²`. Going from 24p to 200p
divides the per-interval signal by about **69**. The calibration says the
field is accurate above ~5 px/interval² and quantisation-limited below ~2 --
so motion that reads a healthy 8 px/interval² at 24p reads about 0.12 at 200p,
which is far inside the regime where the field returns approximately nothing.

The rate does not change the physics; it changes where the physics lands
relative to a fixed quantisation floor. Two ways out, neither tested:

- **Widen the baseline.** Estimate across every k-th frame rather than
  adjacent ones, recovering the `k²` factor at the cost of larger
  displacements to search.
- **Accumulate over more frames.** The N-frame generalisation, where a
  degree-(N-1) fit over a longer window extracts a small curvature from many
  samples rather than three.

Either way, **high-rate input is an argument FOR N-frame, not a substitute for
it.**

## Real-hardware confirmation

First run on real hardware, 2026-08-31, by the human collaborator: **jellyfin-ffmpeg on Debian
Trixie, Intel Arc A310** -- the project's existing Linux test box (see the
hardware table in README.md), not a new platform. Mesa, as the WSL loop is,
but a real GPU rather than a software rasteriser.

- **Performance far exceeded expectations**: 104 fps on the Avengers clip and
  88 fps on the Back to the Future clip, 24 -> 60, on a low-end GPU. Two extra
  flow chains and 41 passes were expected to cost far more than this.
- **Motion is "extremely smooth"**, with visual defects on nearly every frame
  -- which was expected and is consistent with the known `L1`-style regression
  plus the fact that nothing here has been tuned for real content.
- Verdict: **the accelerated 3-frame proof of concept is a success.**

The performance number is the surprise and is worth not losing: whatever else
is true, the cost of estimating acceleration is affordable on hardware nobody
would call fast.

## The hypothesis

A 2-frame shader can only encode constant velocity. It sees content at A and
at B, and an inserted frame places that content on the straight line between
them. If the object is accelerating, the straight line is the wrong place: the
correct position is off it, to one side.

At 24fps cinema rates that error is small and the result is "good enough" --
nobody is measuring where a football actually was. It stops being good enough
the moment the flow field is meant to be an *actionable* description of the
world rather than a plausible-looking picture: a car's camera pipeline
deciding where a pedestrian will be needs the position to be right, not
merely smooth.

Three frames are three data points, and three points determine a quadratic.
So the hypothesis: **a 3-frame shader can encode acceleration as well as
velocity, and place content at its correct position on the curve.** By
extension a 4-frame shader could encode jerk, and so on -- untested, and
deliberately out of scope here.

## The algebra

Let the two frames straddling the output be A and B, `s` in [0,1] the output's
position across that interval, and `f` the flow A->B. The anchor is whichever
straddling frame is adjacent to the third (outer) frame T, and it has two
outgoing flows: `f_str` toward the other straddler, `f_out` toward T.

For uniform frame spacing the result is remarkably cheap:

    a = f_out + f_str

Under constant velocity those two flows are equal and opposite and cancel
exactly. **Whatever survives the cancellation IS the acceleration.** The
shader implements the general non-uniform (VFR-safe) solve, which reduces to
this.

The placement then becomes

    d(s) = f*s - (a/2)*s*(1-s)

which is the bidirectional shader's linear warp plus a correction that
vanishes at both endpoints and peaks at `a/8` px mid-interval. **At `a = 0`
the tridirectional shader degenerates to the bidirectional one exactly** --
that is both its safety property and the null hypothesis.

## How it is built

`tests/gen_tridirectional.py` generates
`tridirectional-interpolation.glsl` from the bidirectional base: **41 passes** =
the base's 24, plus 4 slot-2 luma downsamples, 1 extra scene-cut statistic,
and 12 passes of slot-1 <-> slot-2 flow (both directions). Generated rather
than forked so base improvements -- the block match, `TIE_MARGIN`, the
medians, the caching -- are inherited on regeneration instead of rotting the
way the `diffuse-*` forks did.

Binding `FRAME2` declares `frame_mix_count = 3`. **`mix_t` is only valid for
`num_mix == 2`** and is not used anywhere; all timing comes from `rts_mix[]`.

**Everything is keyed on SLOTS, not roles**, and that is the single most
important structural decision here -- see "Cache the slots, not the roles"
below for what happens otherwise. Slots 0, 1, 2 in ascending time are stable
for the window's whole life, so the four adjacent-slot flows F01, F10, F12,
F21 are pure functions of the window and cache correctly. Only the final pass
knows about roles, and it derives them per output frame from `rts_mix`.

The anchor -- the frame with two outgoing flows inside the window -- is
therefore **always slot 1**, whichever half of the interval the output sits
in, and the acceleration solve has no phase dependence at all.

This is the shape that generalises: an N-frame window has N-1 adjacent slot
pairs and fits a degree-(N-1) polynomial. Nothing in the architecture is
specific to three.

## The test ladder

Sustained linear acceleration cannot be tested at interesting magnitudes: the
correction scales as `a/8`, but a ramp changes velocity by `a` px/frame every
frame, so any `a` big enough to matter drives the object past the ~23px/frame
search reach within about three frames. The existing `A1`-`A3` cases sit at
the ceiling of what a 1-second ramp can do, and their mid-interval error is
only 0.08-0.24px.

Oscillation sustains high acceleration at bounded velocity indefinitely, and
is also the real content class where this matters (camera vibration, pan
jitter, a bouncing object). `O1`-`O3` in `tests/scenes.sh`:

| case | A (px) | f (Hz) | v peak px/frame | a peak px/int² | mid-frame error | quadratic validity |
|---|---|---|---|---|---|---|
| `O1_osc_gentle` | 40 | 1.0 | 10.5 | 2.7 | 0.34 px | clean (cubic ~0.1px) |
| `O2_osc_medium` | 20 | 2.5 | 13.1 | 8.6 | 1.07 px | partial (cubic ~0.9px) |
| `O3_osc_hard` | 12 | 4.0 | 12.6 | 13.2 | 1.64 px | model edge, 6 samples/period |
| `O4_osc_flat300` | 20 | 2.5 | 13.1 | 8.6 | 1.07 px | O2 on a 300px flat object |
| `O5_osc_textured` | 20 | 2.5 | 13.1 | 8.6 | 1.07 px | O4 + period-40px interior |

All keep peak velocity well under the search ceiling, so a failure is about
**placement**, not reach. `O3` is deliberately past what a
constant-acceleration model can represent -- a win there was never predicted.

## Cache the SLOTS, not the roles -- and the two wrong diagnoses on the way

This invalidated an entire round of results, took three attempts to explain,
and the two failed explanations are kept because each was plausible and each
is a trap someone else will fall into.

`tri_a0` -- the tridirectional shader with `ACCEL_MAX_PX = 0`, so the
correction is identically zero -- **must** be bit-for-bit identical to the
bidirectional shader. It was not: 2.35 dB out on `O1`, 3.47 dB out the other
way on `L1`.

Ruled out by measurement first: clip-boundary fallback (excluding the last 6
output frames moves every build equally); window ordering (the patch does hand
frames over in ascending time); and **hook fire rate** -- a marker build
returning a flat colour showed the hook firing on 60 of 60 output frames for
both the 2-frame and 3-frame shaders. Disabling every `if (!pair_changed)`
branch made `tri_a0` exactly equal `bi`, so it was the flow cache.

**Wrong diagnosis 1: a Vulkan storage-image ceiling.** The base declares 8
`//!STORAGE` textures and the tridirectional build 12, so "8 works, 12 does
not" looked like a limit. It is not: this Radeon reports
`maxPerStageDescriptorStorageImages = 4294967295` and Mesa lavapipe reports
1000000. The claim had been reasoned rather than checked, and checking it
refuted it immediately.

**Wrong diagnosis 2: `pair_changed` is deficient for N > 2.** Narrowing by
scope showed disabling only the *new* chain's caches changed nothing, and only
disabling the *base* caches helped -- so it was neither count nor the new
passes. The frame arithmetic then showed something real:

| output frame | τ within interval | straddling pair | 3-frame window |
|---|---|---|---|
| n=2 | 0.8 | (S0, S1) | {S0, S1, S2} |
| n=3 | 0.2 | **(S1, S2)** | **{S0, S1, S2}** |

Same window, different pair. `pair_changed` reads false and the cached flow
belongs to the previous pair. That observation is correct -- but the
conclusion drawn from it, that the patch should expose a finer signal, was
not.

**The actual cause: the shader was caching ROLE-KEYED state.** Roles -- "frame
A", "frame B", "the anchor", "the outer frame" -- rotate *within* a fixed
window, so anything keyed on them is not a function of the window and
`pair_changed` cannot possibly invalidate it correctly. `pair_changed` means
exactly what it says. It is the right signal for a window-keyed quantity and
the wrong one for anything else, and the patch needs no change.

**The fix is to key on SLOTS.** Slots 0, 1, 2 in ascending time are stable for
the window's whole life, so the four adjacent-slot flows F01, F10, F12, F21
are pure functions of the window and cache correctly with `pair_changed`
unmodified. Only the final pass knows about roles, and it derives them per
output frame from `rts_mix` while reading cached fields.

Two things fall out beyond correctness:

- **The acceleration solve loses its phase dependence.** The anchor -- the
  frame with two outgoing flows inside the window -- is *always* slot 1,
  whichever half of the interval the output sits in. So `a = F10 + F12` with
  no case analysis, where the role-keyed version needed a branch.
- **It is the shape that generalises.** An N-frame window has N-1 adjacent
  slot pairs and fits a degree-(N-1) polynomial. Nothing in the architecture
  is specific to three.

Verified: with caching **enabled**, `ctrl` (the zeroed build) equals `bi` to
the decimal on all nine benchmark cases. The shader now runs at full speed
with its caches live, where every measurement before this had to be taken
cacheless.

One lesson generalises past this shader. The natural way to *describe* an
N-frame algorithm is in roles, because that is how the maths reads. The
correct way to *implement* one is in slots, because that is what the cache
invalidation signal is about. Those two do not coincide for N > 2, and nothing
warns you when they diverge.

## What each frame PAIR buys, and why only some of them are worth computing

Three frames A, B, C admit six directed flows. Working out what each one
contributes turned out to be the most productive hour of this experiment, so
the algebra is here in full. With A, B, C at t = -1, 0, +1 and a quadratic
trajectory p(t) = p0 + v*t + (a/2)*t^2:

    d_AB = v - a/2          (adjacent, first interval)
    d_BC = v + a/2          (adjacent, second interval)
    d_AC = 2v               (spanning, both intervals)

Three consequences, in increasing order of usefulness:

**The spanning pair measures velocity directly.** `d_AC / 2` is `v` with no
differencing at all, where the adjacent pairs only give it as a sum. Anything
derived by differencing two large near-equal numbers is noisy; this is not.

**Acceleration is the difference of the adjacent pairs**, `a = d_BC - d_AB`,
which for the anchored form this shader actually uses is the sum
`a = f_out + f_str`. That is what it computes.

**And the three are redundant, which is the valuable part:**

    d_AB + d_BC = d_AC

This identity holds for *any* trajectory, not just a quadratic -- it is just
"getting from A to C via B is getting from A to C". So it is a check on the
MEASUREMENTS rather than on the motion model, and it is exactly the
discriminator this experiment needs. At a velocity reversal, where the naive
magnitude gate fails hardest, the identity holds perfectly. Under occlusion,
where one flow matched unrelated content, it breaks.

The reverses (B->A, C->B, C->A) buy something different and cheaper:
per-pair **round-trip consistency**. Following A->B then B->A should land
back where it started. That is the classic occlusion test, and the base
shader already computes both directions of the straddling pair, so the first
of them costs nothing.

Both were implemented. The results below are what separated them.

## Results

Windows (Radeon Pro 560X), **flow caching enabled** -- which the slot-keyed
build supports and every earlier measurement could not. `ctrl` is the null
control: the same shader with `ACCEL_MAX_PX = 0`, so the quadratic correction
is identically zero and it must reduce to the bidirectional shader.

| case | a peak px/int² | bi | ctrl | tri | **Δ** |
|---|---|---|---|---|---|
| `L1_trans_8px` | 0 | 61.26 | 61.26 | 57.46 | **−3.80** |
| `L2_trans_16px` | 0 | 41.78 | 41.78 | **42.71** | +0.93 |
| `A2_accel_16mean` | 1.9 | 42.54 | 42.54 | **43.17** | +0.63 |
| `F2_fourier_accel` | 1.9 | 39.12 | 39.12 | **39.20** | +0.08 |
| `O1_osc_gentle` | 2.7 | 47.09 | 47.09 | **49.41** | **+2.32** |
| `O2_osc_medium` | 8.6 | 42.05 | 42.05 | **46.50** | **+4.45** |
| `O3_osc_hard` | 13.2 | 41.75 | 41.75 | **45.03** | **+3.28** |
| `O4_osc_flat300` | 8.6 | 43.61 | 43.61 | **47.80** | **+4.19** |
| `O5_osc_textured` | 8.6 | 33.09 | 33.09 | **34.02** | +0.93 |

**`ctrl` equals `bi` to the decimal on all nine cases.** That is what the
algebra demands and it is the strongest available evidence that the timing,
the slot mapping and the 3-frame plumbing are right -- now with the caches
live rather than disabled to hide a bug.

**The hypothesis is confirmed. `tri` wins on eight of nine cases**, by up to
4.45 dB, and the gain rises with acceleration across the oscillation ladder
(+2.32 at a=2.7, +4.45 at 8.6) as the model predicts. `O3` at 13.2 gains 3.28
dB despite being calibrated in advance as past what a constant-acceleration
model can represent -- the quadratic is evidently still a better description
than a straight line well beyond the point where it stops being an exact one.

### Re-measured after sub-pixel refinement and the correction deadband

Full ladder, Windows / Radeon Pro 560X, caching live. `ctrl` is `tri` with
`ACCEL_MAX_PX = 0`.

| case | bi | ctrl | tri | tri - bi |
|---|---|---|---|---|
| `L1_trans_8px` | 61.26 | 60.78 | 60.77 | **-0.49** |
| `L2_trans_16px` | 41.78 | 41.12 | 42.18 | +0.40 |
| `L3_trans_23px` | 40.49 | 40.41 | 40.15 | -0.34 |
| `L9_occlusion` | 39.83 | 39.63 | 40.03 | +0.20 |
| `A2_accel_16mean` | 42.54 | 42.25 | 43.03 | +0.49 |
| `F2_fourier_accel` | 39.12 | 38.91 | 38.98 | -0.14 |
| `M3_period16_trap` | 21.90 | 21.91 | 21.91 | +0.01 |
| `O1_osc_gentle` | 47.09 | 47.37 | **49.44** | **+2.35** |
| `O2_osc_medium` | 42.05 | 41.81 | **46.19** | **+4.14** |
| `O3_osc_hard` | 41.75 | 41.72 | **45.18** | **+3.43** |
| `O4_osc_flat300` | 43.61 | 43.45 | **47.36** | **+3.75** |
| `O5_osc_textured` | 33.09 | 33.08 | 34.03 | +0.94 |

**The `L1` regression is reduced from -3.80 dB to -0.49 dB, not eliminated.**
It reaches +0.09 -- genuinely gone -- at the wider `1.0/2.5` deadband, but
that setting costs `O1` 0.38 dB, and the oscillation cases are what this
shader exists for. `0.5/1.5` is the shipped trade. Precision matters here:
an earlier note in this session claimed the regression was closed, which was
true of the wider setting and not of the default.

Three cases now lose slightly instead of one losing badly: `L1` -0.49,
`L3` -0.34, `F2` -0.14. All three are the **sub-pixel warp cost** rather than
the acceleration correction -- fractional flow forces bilinear resampling
where integer half-res flow landed on pixel centres -- so the deadband cannot
recover them and no setting eliminates them. The oscillation gains are intact
(+2.35 to +4.14), and `tri` now beats stock `linear` on `O5` (+0.13) where
`bi` loses to it (-0.81).

### The `ctrl == bi` invariant, restated

`ctrl` no longer equals `bi` to the decimal, and that is expected rather than
a regression: sub-pixel refinement is ON in the generated tridirectional
shader and OFF in the base, so `ctrl` measures *bi plus sub-pixel*. The
difference between the two columns above IS the sub-pixel warp cost, isolated.

**With sub-pixel matched, the invariant still holds exactly** -- `ctrl` built
with `SUBPEL_REFINE = 0` returns 61.26 / 41.78 / 43.61 on `L1` / `L2` / `O4`,
identical to `bi` in every digit. That remains the strongest available
evidence that the timing, the slot mapping and the 3-frame plumbing are
right, and it now has to be tested with the flag matched or it measures
something else.

### The E-series is not reachable through `scene()`

`E1`-`E4` live in `scene_edge()`, a separate function, so `scene E2_... 24`
correctly returns `UNKNOWN_CASE` and `bench.sh` correctly reports "unknown
case" on **stderr**. Suppressing stderr turns that into an empty row in
`analyze.py` that looks like a rendered result. It happened in this session;
the four edge cases were silently absent from a ladder run until the empty
row was chased. Do not discard `bench.sh`'s stderr.

### The gate that made it work

The first confidence gate rejected acceleration by MAGNITUDE: large `|a|`
relative to the flows means they failed to cancel, so distrust it. That cannot
work, and why is the central difficulty of the whole approach. Two completely
different things stop the flows cancelling:

- **Occlusion.** One flow matched unrelated content. The residual is junk.
- **Reversal.** The object genuinely turned around, both flows are good
  matches pointing the same way, and the residual is the largest and most real
  acceleration in the scene.

A magnitude ratio drives toward 1 in both, so it discarded the signal exactly
where it was strongest. The fingerprint was in the numbers: the gain *fell* as
acceleration rose (+1.82 dB at a=2.7 down to +0.91 at 8.6) when the model
should help more. Replacing it with **round-trip consistency** -- judging the
answer's provenance rather than its size, since a reversal round-trips
perfectly and an occlusion cannot -- inverted that ordering and was worth up
to +4.4 dB. Both of the anchor's flows are round-tripped and the worse decides.

Thresholds swept (first time, 0.25/0.75 through 2.0/5.0): clean monotonic
trade-off, no knee, 2.0/5.0 kept.

### Cross-platform

Re-run in full on WSL2 / Mesa lavapipe, a completely different Vulkan
implementation from the Windows AMD ICD, with caching enabled on both:

| case | Win bi | WSL bi | Win tri | WSL tri |
|---|---|---|---|---|
| `L1_trans_8px` | 61.26 | 61.29 | 57.46 | 57.55 |
| `O2_osc_medium` | 42.05 | 42.05 | 46.50 | 46.50 |
| `O4_osc_flat300` | 43.61 | 43.65 | 47.80 | 47.86 |

**Maximum deviation 0.09 dB across all nine cases, most within 0.01**, and
`ctrl` equals `bi` exactly on lavapipe as it does on Windows. The slot-keyed
caching therefore behaves identically on two unrelated Vulkan
implementations, which is the result that matters most for new generated
code -- a caching bug that depended on driver behaviour would show here.
Together with the Arc A310 run that is three implementations.

### The one remaining regression

`L1_trans_8px` loses 3.80 dB on content whose true acceleration is exactly
zero, where the shader is required to be a no-op. Note `L2_trans_16px`, also
constant velocity, *gains* 0.93 -- so this is not simply "constant velocity
breaks it", and it sits next to the unexplained `L1`/`L2` anomaly in the base
shader recorded in TESTING.md.

The next section is why this cannot be fixed at three frames.

## Acceleration cannot be validated from three frames -- a proof, not a guess

`L1_trans_8px` still regresses 3.80 dB. It is pure constant velocity, the true
acceleration is exactly zero, and the shader is required to be a no-op. Three
separate attempts to gate that away have now failed, and the third one failed
in a way that explains the other two and redirects the whole programme.

**Attempt 1, magnitude ratio.** Cannot separate occlusion from a genuine
velocity reversal; both stop the flows cancelling. Replaced by round trips,
worth up to +4.4 dB on the O-series.

**Attempt 2, per-pair round trips (both of them).** No effect on `L1`, in
every digit, and `trivis`'s trust panel reads GREEN along both object edges --
the texels doing the damage. At a moving edge the block match locks onto the
edge feature, which is high-contrast in all three frames, so every pair
matches it consistently in both directions. Each pair is individually
self-consistent. Round trips are a per-pair test and cannot see a
relationship *between* pairs.

**Attempt 3, the spanning flow and the triangle identity.** Built as 6
generated passes on the reasoning that `d(F0->F1) + d(F1->F2) == d(F0->F2)`
checks the measurements against one another rather than against a motion
model. That reasoning is correct. The conclusion drawn from it was wrong, and
the degrees of freedom say so:

> Three frames give **two** unknown displacements, `d01` and `d12`. With the
> spanning flow there are **three** measurements. That is exactly **one**
> redundancy, and the triangle identity is it -- constraining the **sum**,
> `d02 = d01 + d12`.
>
> Acceleration is the **difference**, `a = d12 - d01`.
>
> Sum and difference are orthogonal components. The single available
> constraint cannot touch acceleration at all.

A **common-mode error** -- both anchor flows biased the same way, which is
exactly what a moving edge produces -- creates spurious acceleration while
leaving `d02` untouched, and is therefore invisible to the identity by
construction.

Measured, and it is worse than blind. Weighting the triangle residual 20x:

| triangle weight | `L1` (want 61.26) | `O2` (want high) |
|---|---|---|
| 0 (off) | 57.46 | 46.46 |
| 0.5 | 57.46 | 46.45 |
| 2.0 | 57.46 | 46.31 |
| 10.0 | **57.55** | **43.87** |

It recovers 0.09 dB of the fault it was built to catch while destroying 2.59
dB of the signal it must not touch -- **anti-correlated with its purpose**.
The residual it measures is dominated by its own reach limitation: a spanning
displacement is twice a per-interval one and leaves the coarse search's
~23px/frame window on fast content, so it rejects good acceleration and keeps
bad. The six passes were removed; the shader is back to 41.

### What this means for the programme

**Validating acceleration requires a fourth frame.** F0..F3 give three
unknown displacements against six pairwise measurements -- three redundancies
-- which is enough for **two independent estimates of `a`**, from (F0,F1,F2)
and from (F1,F2,F3), that can be checked against each other. A common-mode
bias would have to be consistent across both to survive, which is a far
stronger condition than anything available with three frames.

That converts the 4-frame window from a tidiness argument (a symmetric
stencil, no mid-interval anchor flip) into the **necessary next step**, and it
is now the top open lead. Note what gates it: `pair_changed` is already
insufficient at three frames, and a 4-frame window has more phases still, so
the cache-keying fix above is a prerequisite rather than a nicety.

It also bounds what the current 3-frame shader can ever be. It wins where
acceleration is real and it cannot be made safe where acceleration is
spurious, because with three frames nothing can tell those apart at a moving
edge. **As it stands the shader is a demonstration that the hypothesis is
true, not a candidate for production.**

## Calibrating the field: what it actually reads

If the field is the product, "it looks plausible" is not a result. The
O-series has analytically exact acceleration -- `x(t) = X0 + A·sin(ωt)` gives
`a(t) = −A·ω²·sin(ωt)` -- so `tests/accelcheck.py` reads the rendered field
back in px/interval² and compares it against a number derived from the scene
definition, not from the render.

Two details, each of which would otherwise manufacture a fake error. The
shader's estimate is a quadratic fit through three frames, so what it reports
is the acceleration at the fit's **centre** -- slot 1 -- not at the output
timestamp; for a sinusoid those differ. And the readback is **16-bit**
(`-pix_fmt rgb48le`): at 8 bits the encoding is coarser than the signal on
quiet content, which would put the instrument's own resolution into the error
bars.

### The field is sparse, and that is correct

The first run sampled the interior of `O1`-`O3` and measured **exactly zero**
-- median 0.000, IQR [0, 0]. Those are flat white boxes. A flat region has no
matchable texture, so the flow is legitimately zero there and the acceleration
with it. All the signal is at the edges, and the edges are where the trust
gate discards it.

**So the field only exists where there is texture to carry it.** That is a
property of block matching rather than of this shader, but it decides where
the field is usable, and it is the first thing to check on any real scene.
`O5_osc_textured` exists for this reason.

### The calibration curve

`O5`'s sinusoid sweeps true acceleration across its whole range, so one render
gives accuracy as a function of magnitude rather than spot checks. Every frame
of the 60-frame sequence, sampled (half shown; the other half repeats exactly,
which is itself the instrument's repeatability check -- frames 4 and 56, 8 and
52, 12 and 48 return identical readings):

| true a_x | measured | error | coverage |
|---|---|---|---|
| −8.275 | −7.750 | 6.4% | 49.0% |
| −7.915 | −7.750 | **2.1%** | 54.9% |
| +7.420 | +7.453 | **0.5%** | 54.9% |
| −6.797 | −6.750 | **0.7%** | 45.5% |
| +6.058 | +5.250 | 13.3% | 38.0% |
| −2.218 | −0.875 | **60.6%** | 64.9% |
| +1.118 | +0.750 | **33.0%** | 78.7% |

**Above |a| ≈ 6 the field is accurate to well under 1% in most samples.** Below
|a| ≈ 2 it under-reads by a third to two thirds. The transition is sharp, and
the direction is almost always toward zero.

Coverage moves the opposite way -- 38-55% at high magnitude against 65-80% at
low -- so the field is sparsest exactly where its values are best.

### Why it under-reads: one hypothesis half-right, and a better one

The standing explanation was `REG_LAMBDA`: it pulls each flow estimate toward
zero motion, and an acceleration built from two such flows would inherit that
pull twice. **Tested by sweeping it, at the worst sample (a = −2.218):**

| `REG_LAMBDA` | measured | error |
|---|---|---|
| 0.00 | −1.062 | 52.1% |
| 0.06 (shipped) | −0.875 | 60.6% |
| 0.18 | −0.750 | 66.2% |

Monotonic, so the regulariser genuinely contributes. **But it is not the
cause.** Removing it entirely still leaves 52% error, and at a = +1.118 the
reading is +0.750 at all three settings -- completely insensitive to it.

The measured values say what does dominate. Across the whole sweep they
cluster on multiples of **0.25 px/interval²**: 0.750, 5.250, 6.750, 7.750.
The acceleration is `2·(f10 + f12)` in half-res flow texels, so it inherits
twice the flow field's own quantisation, and 0.25 px/interval² is a quarter of
the signal at |a| = 1 and a fortieth of it at |a| = 8. **That is the shape of
the error curve exactly**: quantisation-dominated at the low end, negligible
at the high end.

Two consequences worth carrying:

- **The low end is a resolution limit, not a bias to correct.** Tuning
  `REG_LAMBDA` down buys a few percent and costs whatever the regulariser was
  earning elsewhere. Improving the low end means a finer flow estimate --
  sub-texel refinement, or a higher-resolution final level -- not a
  coefficient.
- **`TIE_MARGIN` is a second zero-bias mechanism** in the same path, added
  earlier for the tie-breaking work: it requires a candidate to beat the
  incumbent, and the coarse search's incumbent starts at zero motion. It has
  not been swept against this calibration and should be, since unlike
  `REG_LAMBDA` its purpose is unrelated to biasing.

### CORRECTION: the low end is jerk-limited, not quantisation-limited

Everything above is measured correctly and interpreted wrongly, and the
section is kept rather than deleted because the wrong turn is part of the
evidence.

`O5` is a sinusoid, and in `x = A·sin(ωt)` the acceleration is `−Aω²·sin(ωt)`
while the jerk is `−Aω³·cos(ωt)`. **|a| is smallest exactly where jerk is
largest.** Every low-|a| sample in the curve above is also a maximum-jerk
sample, so the scene cannot separate "small acceleration" from "acceleration
changing fast" -- and the conclusion attributed the error to the wrong one.

Two controls were built to break the confound: **`A4`-`A7`**, textured
constant-acceleration scenes with **zero jerk** by construction, and **`O6`**,
the same texture and object size as `O5` with 7.8× less jerk. At matched
magnitude:

| scene | \|a\| | jerk px/interval³ | error |
|---|---|---|---|
| `O5` frame 10 (zero crossing) | 2.218 | 5.42 | **60.6%** |
| `O6` frame 4 (near peak) | 2.374 | 0.359 | **5.2%** |
| `A6` (constant a) | 1.333 | **0** | **6.8-12.5%** |

**15× less jerk, 11.7× less error, at the same acceleration** -- and `A6`
reads *better* at a *lower* magnitude, which a magnitude limit cannot produce.

So the dominant low-end error is **the three-frame model**. A quadratic
through three points must assume acceleration is constant across the window;
where it changes fastest that assumption is worst. No amount of flow precision
fixes it -- four frames and a degree-3 fit do.

Quantisation is real but its reign is much smaller than claimed above: it
dominates only below |a| ≈ 0.5, where `A4` (a = 0.333) errs 69-125% with
readings pinned to the 0.25 lattice. Between 0.67 and 2.4 at low jerk the
field is already good to 5-13%.

`TIE_MARGIN`, flagged above as the cheap next check, was also swept and is
**not** implicated: near-zero fraction 51%/51%/47% across 0/1e-4/1e-2. A 100×
change moving four points is the "extreme tuning that changes nothing"
signature. (It does shift the frame-10 median, 60.6% → 43.6% at 1e-2, without
touching the collapse -- unchased, and it would need a ladder run first.)

**Read the field accordingly: at low jerk it is good to ~5-13% from |a| ≈ 0.67
upward, quantisation-floored below ~0.5, and unreliable wherever acceleration
is changing rapidly regardless of its magnitude.**

The old summary said that for real footage, at mean |a| 0.55-1.5, the field
reports the right *structure* but not reliable *magnitudes*. That now needs
splitting: on smoothly accelerating content those magnitudes are good to
5-13%, which is usable; it is **abrupt** motion -- high jerk -- that the
three-frame estimator cannot report reliably, at any magnitude. For the
autonomous-vehicle framing that is the more consequential half, since a
pedestrian changing direction or a vehicle braking hard is precisely a
high-jerk event.

## Field accuracy, current state (after sub-pixel + the equiangular fit)

Two estimator upgrades landed after the calibration sections above were
written, and the field they describe is now substantially better than the
text records. Sub-pixel refinement removed the integer-lattice collapse
(O5 frame 10: 60.6% -> 11.2%), and replacing the parabola sub-pixel fit
with the equiangular V fit -- the matched estimator for an SAD valley;
see PRIOR-ART.md on peak locking -- took the low band the rest of the way:

    A4 (a = 0.333)   best-frame error  6.6%     (was 125% pre-sub-pixel)
    A5 (a = 0.667)                     2.5%
    A6 (a = 1.333)                     2.0%
    A7 (a = 1.667)                     1.8%
    O5 f10 (max jerk)                  4.9%
    O6 f4                              0.7%

(A third upgrade landed after the first two: a FULL-RESOLUTION refinement
level -- estimator only; the warp keeps the mediated half-res flows -- with
a 5x5 aperture. See PLAN.md T1.2 for its three-step history.) The band real
footage occupies (mean |a| 0.55-1.5) now calibrates at **2-7% typical**.

**Correction to the O-series rows above (2026-09-01, from the Metal-port
investigation -- full account in QUADDIRECTIONAL.md's CORRECTION
section):** the quadratic estimator measures the discrete second
difference, which on a sinusoid is (sin(w/2)/(w/2))²-attenuated against
the continuous derivative accelcheck originally compared to. Under the
corrected truth `O5` f10 reads **2.1%** (was 4.9-5.6) and `O6` f4
**1.3%**. The A-series rows are exact under both models and stand
unchanged -- so the 2-7% claim for the real-footage band tightens rather
than loosens. The F2 and rotation limits below are untouched (measured
against per-texel truth, not the sinusoid model).

**And two content limits, measured the same day the numbers above were
(PLAN.md, the Tier-0 proofs).** The 2-7% claim holds for TRANSLATION OF
TEXTURED CONTENT. It does not hold for:

- **edges-only content** (`F2`, flat interior, Fourier boundary: 24-74% at
  the same physics `A6` reads at 2%) -- the aperture problem: an isolated
  edge constrains flow only along its normal, and the acceleration
  inherits the unconstrained tangential part;
- **rotation** (`R2` flat and `R3` textured both: 100-207% median vector
  error against the exact truth `a(p) = alpha*J*(p-c) - omega^2*(p-c)`,
  per-texel via `tests/rotcheck.py`) -- and the textured control proves
  this is not merely the aperture. Cause not yet localised; the flows
  themselves are off by pixels on rotating content.

A consumer of this field should treat readings on texture-poor regions and
on rotating structure as unreliable until the structure-tensor gate (open
lead) exists to mask the former and the rotation failure is diagnosed. The earlier sections are kept as the record of how it got here.

## Reading the fields: TRI_DIAG

Set `TRI_DIAG` at the top of the final pass. No rebuild, no separate file.

| mode | shows | marker |
|---|---|---|
| 0 | normal interpolated output | none |
| 1 | the quadratic **correction** -- how far this texel is moved off the constant-velocity line, in px | red |
| 2 | the **acceleration** field, px/interval², direction as hue | blue |
| 3 | acceleration **magnitude** as a heat map, direction discarded | green |

Full scale is set by `ACCEL_DIAG_FS` (px/interval², modes 2 and 3) and
`CORR_DIAG_FS` (px, mode 1), both right above `TRI_DIAG`, so a pixel converts
back to a number instead of being a vibe.

**Two traps, both hit in practice and both now designed against.**

**The values are far smaller on real footage than on the ladder.** The
synthetic O-series reaches 13 px/interval²; ordinary camera motion is one to
two orders of magnitude below that. The original constants were calibrated on
the ladder and rendered real content invisible -- mode 1 deviated by ONE level
out of 255, which is indistinguishable from a mode that did not engage. The
defaults are now set for real footage (`ACCEL_DIAG_FS = 2.0`,
`CORR_DIAG_FS = 0.25`); raise them for synthetic tests.

**A near-zero field and an inactive switch look identical**, since zero
encodes as mid-grey and fills the screen with it. So every non-zero mode burns
a **solid colour block into the top-left corner**, one colour per mode. If the
marker is absent, the shader being rendered is not the one you edited -- which
is easy to do, because a shader referenced from an ffmpeg filter argument has
to be a *relative* path (the drive-letter colon is ffmpeg's own option
separator), so the usual workflow copies it next to the output and it is the
copy that gets loaded.

Mode 1 is additionally zero on every fifth output frame at 24 -> 60, and that
is correct rather than broken: the correction is `a/2 · s(1−s)`, and those
frames land exactly on a source frame where `s = 0`.

## Reproducing


```bash
./tests/gen_tridirectional.py                       # regenerate the shader
./tests/scenecheck.sh O1_osc_gentle O2_osc_medium O3_osc_hard
./tests/trivis.py tridirectional-interpolation.glsl /tmp/vis.glsl
```

In-shader diagnostics, without a separate build: `TRI_DIAG` in the final pass
(0 = normal, 1 = the quadratic correction amplified, 2 = the acceleration
field wheel-encoded).

## Why the visualiser has four panels

A flow field is 2D and the colour wheel encodes exactly 2D. Acceleration is a
*second* 2D field, and the wheel has no third and fourth dimension to extend
into -- overloading brightness collides with saturation, and the thing you
most need to see is where the two fields disagree. So `trivis.py` shows four
separable panels on a shared layout: velocity and acceleration in the *same*
encoding and gain (so "is the acceleration comparable to the velocity here?"
is a direct visual comparison), the **correction** `|a|/8` as a heat map in
px, and the **trust** gate.

The correction panel is the one that matters, and is why this is not just two
`flowvis.py` renders side by side. Acceleration in px/int² means little to a
viewer; the placement error it implies means everything, and it reads
directly as *how wrong is the bidirectional shader here*. If that panel is
black on your content, a 3-frame shader has nothing to win.

The trust panel is the honesty check. Without seeing where the gate fired you
cannot distinguish a real acceleration field from noise that happened to
survive -- which is exactly the mistake the first build made.

## Separation from the bidirectional work

Deliberate, so neither line of work constrains the other:

- The tri shader is **generated** from the bidirectional base, so base fixes
  propagate and nothing in the base has to know tri exists.
- No bidirectional shader, tool or scene was modified. `O1`-`O3` are additive
  ladder cases, verified by `scenecheck.sh` as exact ground truth, and are
  useful to the bidirectional shader independently.
- `trivis.py` refuses to run on a shader without `FLOW_H_AT`, so it cannot be
  pointed at a bidirectional build and produce something meaningless.
- `flowvis.py`, `bench.sh` and the rest are untouched and work on both.

## A causal window buys nothing at three frames -- a proof, not a measurement

The latency note recorded earlier said the centred estimate lags by one frame
because it needs the next frame, and that a causal `{S_k-2, S_k-1, S_k}`
window extrapolating to `S_k` would remove the lag. **The second half of that
is wrong**, and it is worth writing down as an argument rather than leaving it
as an untried lead, because the conclusion is structural.

A quadratic's second derivative is a CONSTANT. So a 3-point fit does not
produce "the acceleration at the centre" as opposed to "the acceleration at
the end" -- it produces one number for the whole window. The centre only
enters as the instant at which that constant is the best approximation to a
true acceleration that is varying; where jerk is zero the attribution is
arbitrary, and where it is not, the fitted constant tracks the truth near the
middle of the window and drifts from it at the ends.

Count the information age both ways, in frames, from the newest sample each
one consumes:

| window | fitted `a` describes | needs frame | age when available |
|---|---|---|---|
| centred `{k-1, k, k+1}` | instant `k` | `k+1` | **1 frame** |
| causal `{k-2, k-1, k}` | instant `k-1` | `k` | **1 frame** |

They are the same estimator, relabelled. The causal window waits for nothing,
but the answer it hands back is about the frame before last; the centred
window describes the middle frame, but cannot be evaluated until the frame
after it arrives. **Three samples are what it costs to see curvature at all,
and one frame of age is the change owed on that.**

Extrapolating does not help either, for the same reason: the value being
extrapolated is constant across the fit, so evaluating it at `S_k` instead of
`S_k-1` returns the identical number -- more confidently attributed and no
more accurate. Getting a genuinely *current* acceleration means modelling the
way acceleration is changing, which is a cubic, which is a fourth frame.

So for the real-time sensing case the honest statement is: **the field is
inherently one frame old at three frames -- 42 ms at 24p, 5 ms at 200p -- and
no arrangement of those three frames improves on that.** The lead is closed by
argument. What remains open is whether a fourth frame buys back the frame of
age as well as the jerk term, and that belongs with the four-frame work.

## Open leads, across all of this work

Kept here rather than in a head, because the pattern of this project is that
a productive rabbit hole leaves good leads dangling behind it. Roughly in
order of expected value.

**From the tridirectional experiment:**

0. **A causal (backward-only) variant for real-time sensing.** The centred
   estimate needs the next frame, so the field lags by one frame -- 42 ms at
   24p. A `{S_k-2, S_k-1, S_k}` window extrapolating to `S_k` removes the lag
   but amplifies exactly the quantisation that already dominates the low end.
   Not built, not measured; the obvious next step for the vehicle use case.
   (The N:N *firing* blocker that stood here is fixed -- see
   `frame-mix-nn-threshold.patch`.)
0b. **Get the field out as DATA, not as an image to read by eye.** `TRI_DIAG`
   encodes into pixels and `accelcheck.py` decodes back; that round trip
   through a video path is the weakest link in treating this as an instrument.
   A direct export -- flow and acceleration as float data, per frame, with
   units attached -- is what turns a picture into a measurement.
1. **The low end is quantisation-limited, and that is now measured.** The field
   is accurate to under 1% above |a| ~ 6 and under-reads by 33-66% below |a| ~ 2,
   because acceleration is 2*(f10 + f12) and inherits twice the flow field's
   quantisation -- readings cluster on multiples of 0.25 px/interval^2.
   REG_LAMBDA contributes (52%/60.6%/66.2% error at 0.00/0.06/0.18) but is not
   the cause. Improving it needs a finer flow estimate, not a coefficient.
   TIE_MARGIN is a second zero-bias in the same path and has NOT been swept
   against the calibration; that is the cheap next check.
2. **Coverage is 41-79% and inversely related to acceleration** -- the field
   is sparsest exactly where its values are most accurate, because the trust
   gate discards more when motion is hard. Worth understanding whether that
   is the gate being right or being crude.

3. **Generalise to N frames.** The architecture is already the right shape:
   slot-keyed, N-1 adjacent-slot flow chains, a degree-(N-1) polynomial fit.
   Four frames is the necessary next step rather than merely the next one --
   three frames cannot *validate* an acceleration estimate (proved below),
   and F0..F3 give three redundancies and two independent estimates of `a`
   that can be checked against each other. Beyond that, each added frame
   raises the polynomial degree: a smoother trajectory through more evidence
   rather than a quadratic through three jagged points. Cost grows with the
   number of chains, so measure whether degree 3 buys anything before
   assuming degree 4 does.
4. **The caching is solved and generalises.** Slot-keyed fields are pure
   functions of the window, so `pair_changed` is the correct invalidation
   signal at any N and needs no patch change. This was the blocker; it is
   closed.
5. **Gate thresholds: swept, done.** 2.0/5.0 kept; clean monotonic
   trade-off, no knee, no headroom. Re-sweep only once a new trust signal
   exists to sweep against.
6. **Do not rebuild the spanning F0->F2 flow.** Built, measured,
   anti-correlated with its purpose, removed. The degrees-of-freedom argument
   below says why it cannot work, so this is closed by proof rather than
   untried.

**Turned up incidentally and not chased:**

5. **`bi` loses to stock `linear` on `O5_osc_textured`** (33.09 against
   33.90). A textured object oscillating at 13px/frame peak, with a
   period-40px interior that should be unambiguous, and the motion-compensated
   shader is worse than blending. That is a bidirectional finding with nothing
   to do with acceleration, and it is unexplained.
6. **`M3_period16_trap` barely moved through the ladder reset** (22.15 to
   21.90) while `M2_period40` rose 16.8 dB. Correspondence ambiguity is
   insensitive to ground-truth quality -- a good negative control, and a
   reminder that this case is the one genuinely unsolved estimator failure.

**From the ladder reset, still open (see TESTING.md):**

7. **Regenerate `-diffuse-dual` from the current base**, diffusion kept and
   occlusion fallback dropped. The reset showed it winning clean translation
   outright (76.84 dB on `L1`, within 2.6 dB of the ceiling) while losing
   exactly where its stale fallback does damage. Specific prediction attached.
   This is the strongest dangling lead in the whole project.
8. **The `L1`/`L2` anomaly.** The base shader collapses 19.5 dB between
   8px/frame and 16px/frame, non-monotonically, and the base-vs-variational
   sign flips across the same step. No measured explanation.
9. **The original fourteen scenes still carry hard edges only.** `F1`'s
   Fourier boundary exists; nothing else uses it.

**Blocked on hardware:**

10. **The macOS tie-breaking stress test** needs the Intel Mac specifically --
    an M-series machine is predicted to be too clean to exercise it. See
    `BUILDANDUSAGE.md`.
