# Ground-truth testing for the interpolation shader

## The idea

Real footage is a bad first debugging surface. It is complex, it has no
correct answer to compare against, and every judgement about it comes down
to looking at a frame and deciding whether it seems smudgy. That makes
small regressions invisible and turns every hypothesis into an argument.

Synthetic material fixes both problems at once. If a scene's motion is a
pure function of time -- a box at `x = 384*t` -- then rendering it natively
at 60fps produces *exactly* the frames a perfect 24->60 interpolator would
have produced from the 24fps render of the same scene. There is a correct
answer, and it can be generated on demand.

So interpolation error becomes measurable:

```
lavfi scene @ 24fps ──> [interpolate to 60] ──┐
                                              ├─> PSNR ──> a number
lavfi scene @ 60fps ──────────────────────────┘
   (ground truth)
```

No source video files are needed; `lavfi` generates everything.

## Why three modes, always

A PSNR figure on its own says nothing about whether a 23-pass motion
estimation pipeline is worth running. Every case is therefore measured
three ways:

| mode | what it is | why |
|---|---|---|
| `hold` | frame duplication, no interpolation | the floor -- what you get for free |
| `linear` | stock libplacebo `frame_mixer=linear` | **the bar** -- what you get without this project at all |
| `shader` | the shader under test | must clearly beat `linear` to justify itself |

A shader that does not beat `linear` is not earning its complexity, however
good its output looks in isolation.

## Reading the numbers honestly

- **Passthrough frames are excluded.** At 24->60 every 5th output frame
  lands exactly on a source frame and is trivially perfect for *every*
  mode. Including them inflates all columns by the same meaningless amount.
- **Startup frames are dropped.** The hook falls back to a zero-order hold
  until it has a full frame window, so the first few frames measure startup,
  not interpolation.
- **~79 dB is the practical ceiling, not infinity.** `hold` can hit infinite
  PSNR on a static scene because it copies frames byte-for-byte. Anything
  going through libplacebo tops out near 79 dB from the GPU round-trip
  alone. That gap is not a shader defect.
- **Absolute scores are not comparable across cases.** High-frequency
  content punishes a half-pixel error far more than flat content does. Only
  compare *within* a case, or compare the deltas.

## The complexity ladder

Cases build from trivial to genuinely hard, so a failure localises itself:
if L1 passes and L4 fails, the problem is in the search's reach, not in the
warp or the blend.

| case | what it isolates |
|---|---|
| `L0_static` | no motion at all -- must be a clean passthrough |
| `L1`/`L2`/`L3`/`L4` | translation at 8 / 16 / 23 / 40 px per frame |
| `L5_lowcontrast` | weak signal, but above the contrast gate |
| `M4_belowgate` | weak signal *below* the contrast gate |
| `L6`/`L7`/`M1`/`M2`/`M3` | the texture series (below) |
| `L8_diagonal` | axis asymmetry in the search |
| `L9_occlusion` | two objects crossing -- forward/backward consistency |
| `A1`/`A2`/`A3` | translational **acceleration** (below) |
| `F1_fourier_edge` | an irregular, multi-frequency boundary (below) |
| `R1`/`R2` | **rotation**, constant and accelerating (below) |

The velocity ladder is calibrated against the shader's own arithmetic, not
picked arbitrarily: the coarse search reaches `step_px * 1.9375` coarse
texels = `0.75 * 1.9375 * 16` ≈ **23 full-res px per frame pair**. L3 sits
at that ceiling and L4 deliberately past it.

### The texture series

`L6`, `L7`, `M1`, `M2`, `M3` are the controlled experiment: an **identical**
300x300 object moving at an **identical** 16px/frame. The only variable is
what fills its interior. That isolates what the motion search can actually
resolve from what merely looks difficult.

Note `sin(X/k)` has spatial period `2*pi*k` px, so `k=2.546` gives a 16px
period -- exactly the per-frame travel distance.

### Acceleration, and why nothing tested it before

Added 2026-08-31. Every case above this point moves at a **constant
velocity**, which means the block match's central assumption -- that one
offset describes the whole interval between two source frames -- is exactly
true, and the linear lift of that flow to an intermediate time
(`flow_ab * mix_t` in the warp) is exactly right. Neither holds for anything
that speeds up, and the ladder had no case where they failed.

Each acceleration case is twinned with a constant-velocity case above it.
`x = c*t^2` covers the same distance in the same second as `x = c*t`, so the
object, the start and end positions, and the mean velocity are **identical**
to the twin; only the velocity profile differs, ramping `0 -> 2c` instead of
holding at `c`.

| case | twin | velocity | mid-frame error |
|---|---|---|---|
| `A1_accel_8mean` | `L1` | 0 -> 16 px/frame, mean 8 | 0.08 px |
| `A2_accel_16mean` | `L2` | 0 -> 32 px/frame, mean 16 | 0.17 px |
| `A3_accel_23mean` | `L3` | 0 -> 46 px/frame, mean 23 | 0.24 px |
| `F2_fourier_accel` | `F1` | 0 -> 32 px/frame, mean 16 | 0.17 px |

**That twinning is useful but not perfectly clean, and an early draft of this
section claimed it was.** Two confounds were found by running it rather than by
thinking about it. One has since been removed; the other cannot be.

1. **Equal mean velocity is not equal difficulty**, and this one is inherent.
   Error grows faster than linearly with speed, and the ramp spends half its
   time below the mean and half above, so the mean of the per-frame scores is
   not the score at the mean speed. It can push the accelerating case either
   way, and on the pre-reset ladder it did: `A2` scored *above* its twin.
   Reading that as "acceleration helps" would have been wrong.
2. **The ground truth was pixel-quantised**, and two different velocity
   profiles accumulated that snapping error differently. **Fixed by the
   2026-08-31 reset** -- every case is now analytic and exact, so this confound
   is gone from all four pairs.

So read a twin difference as "what acceleration costs on this trajectory",
not as an isolated coefficient. `F2_fourier_accel` remains the best-controlled
pair of the four, since `F1`'s constant-velocity trajectory is the one the
estimator handles most cleanly, leaving the least room for confound (1) to
contribute.

"Mid-frame error" is the calibration that makes a result mean something: over
one 24fps interval the true mid-frame position and the linear interpolation of
the two endpoints differ by `a*dt^2/8 = a/4608` px. It is deliberately
sub-pixel, because any acceleration large enough to make it a whole pixel also
throws the object past the coarse search's reach within the second and would
confound two failures. On a hard edge a tenth of a pixel is not nothing --
roughly 10% of full contrast on the boundary texel.

### Rotation

Also added 2026-08-31, and a gap of a different kind: block matching searches
over **translations**, so rotation is a motion it cannot represent exactly
anywhere except instantaneously and locally. The true flow diverges across the
object, and only a sufficiently local match can follow it.

The rotating object has to be `F1`'s Fourier blob rather than a disc, because
a rotating disc is indistinguishable from a stationary one -- there is no
feature whose motion could be recovered. Both cases are calibrated on rim
speed so they sit on the same scale as the velocity ladder: at `R=150` an
angular rate of 2.56 rad/s is 384 px/s at the rim, i.e. `L2`'s 16px/frame.
`R2_rot_accel` covers the same total rotation as `R1_rot_const` in the same
second, ramping `0 -> 32 px/frame` at the rim -- the rotational twin of the
A-series, and the only case here whose motion is both non-translational and
changing.

### Results on the reset ladder

Measured 2026-08-31 on **both** build hosts after the ladder reset described
below -- native Windows (Radeon Pro 560X, AMD's proprietary Vulkan ICD,
mingw-w64) and WSL2 (Mesa lavapipe, software Vulkan, gcc). Numbers below are
the Windows run; **the two agree to within 0.05 dB on every one of the 21
cases for both shaders**, so treat any difference smaller than that as noise.

| case | hold | linear | base | `-coarse` | `-dual` | `-variational` |
|---|---|---|---|---|---|---|
| `L0_static` | inf | 79.43 | 79.43 | 79.43 | 79.43 | 79.43 |
| `L1_trans_8px` | 32.78 | 35.44 | 61.26 | 61.10 | **76.84** | 54.24 |
| `L2_trans_16px` | 29.59 | 32.16 | 41.78 | 39.04 | 48.68 | **50.15** |
| `L3_trans_23px` | 27.98 | 30.53 | 40.49 | 32.62 | 38.02 | **41.60** |
| `L4_trans_40px` | 25.48 | 27.96 | 31.57 | 27.39 | 27.39 | **33.96** |
| `L5_lowcontrast` | 55.57 | 57.47 | **62.27** | 62.27 | 62.27 | 60.54 |
| `L6_flat_large` | 30.81 | 33.50 | 55.52 | 45.71 | **56.03** | 52.21 |
| `L7_textured_large` | 20.82 | 21.04 | **25.30** | 22.11 | 22.16 | 23.41 |
| `L8_diagonal` | 27.83 | 30.25 | 40.09 | 33.50 | 35.65 | **45.77** |
| `L9_occlusion` | 29.71 | 32.21 | 39.83 | 36.55 | 40.84 | **44.39** |
| `M1_noise_large` | 24.19 | 25.51 | 46.93 | 43.61 | 46.90 | **48.04** |
| `M2_period40` | 23.58 | 27.29 | 53.64 | 53.64 | **60.04** | 54.40 |
| `M3_period16_trap` | 20.72 | 21.01 | 21.90 | 23.48 | **23.49** | 22.06 |
| `M4_belowgate` | 62.06 | 60.58 | 60.58 | 60.58 | 60.58 | 60.59 |
| `A1_accel_8mean` | 33.64 | 36.23 | 46.81 | 44.51 | 49.46 | **51.24** |
| `A2_accel_16mean` | 30.25 | 32.68 | 42.54 | 37.85 | 41.11 | **45.16** |
| `A3_accel_23mean` | 28.59 | 31.00 | 38.03 | 34.12 | 37.17 | **41.69** |
| `F1_fourier_edge` | 27.33 | 30.31 | 46.91 | 42.78 | 46.12 | **47.26** |
| `F2_fourier_accel` | 28.07 | 31.01 | 39.12 | 32.55 | 33.41 | **43.76** |
| `R1_rot_const` | 29.53 | 32.42 | 37.30 | 33.40 | 34.23 | **41.02** |
| `R2_rot_accel` | 30.35 | 33.20 | 37.58 | 34.13 | 34.72 | **41.16** |

**Every shader still beats `linear` on every case**, which is the bar the
harness exists to enforce. What changed is everything about the margins.

#### 1. No single build wins the ladder any more

Before the reset the ordering was simple: `-variational` first, base second,
the diffuse forks nowhere. That ordering was an artifact. With an exact ground
truth the family splits by *what kind of motion* a case contains:

- **`-variational` wins where the block-match model is wrong** -- rotation
  (+3.7), acceleration (+2.6 to +4.6), diagonal (+5.7), occlusion (+4.6),
  motion past the search ceiling (+2.4). Its smoothness term is a repair for
  flow the pyramid cannot express.
- **`-diffuse-dual` wins where the true flow is genuinely uniform** -- clean
  rigid translation. `L1` at **76.84 dB** is within 2.6 dB of the 79.43
  round-trip ceiling, against 61.26 for the base and 54.24 for
  `-variational`. Diffusing flow into low-texture neighbours pushes toward the
  right answer when the right answer really is constant across the object.
- **The base wins where any smoothing is a liability** -- `L7`, whose texture
  repeats at close to the travel distance, and `L5`.

#### 2. Two open anomalies, both reproduced on both platforms

**`L1` against `L2`.** The base shader scores 61.26 at 8px/frame and 41.78 at
16px/frame -- a 19.5 dB collapse for a doubling of speed, on the same object,
while `-variational` loses only 4.1 dB across the same step and `-dual` 28.2.
A tidy story ("smoothing hurts where the flow is piecewise-constant") fits
`L1`, `L6`, `L5` and `L7` and is contradicted by `L2`, where `-variational`
wins by 8.4. **No mechanism is offered here, because none has been measured.**
16px/frame is exactly one coarse-level texel, which is suggestive and nothing
more.

**`M3_period16_trap` barely moved** (22.15 -> 21.90) while `M2_period40` rose
16.8 dB. Both are sine textures on the same object at the same speed; only the
period differs. That is the correspondence-ambiguity failure being genuinely
insensitive to ground-truth quality, which is what a real estimation failure
should look like, and is a useful negative control on the reset itself.

#### 3. What this says about the recommended build -- and what it does not

`SHADERS.md` recommends `-variational` for production. **Nothing here
overturns that**, and this section should not be read as trying to. That
recommendation rests on a 60-second real-hardware viewing and on fixing the
cartoon-face defect, neither of which a synthetic ladder can speak to, and
this harness's own standing caution is that a result here is a lead to confirm
on real footage rather than a conclusion.

What it does establish is that the *reason* to prefer it is narrower than the
old numbers implied: it is the most robust across motion types, not the most
accurate on all of them.

It also revives a question `SHADERS.md` raises and then drops. The diffuse
forks are stale: they still carry the occlusion fallback the base removed
after every version of it measured worse than none. The reset **confirms that
diagnosis** -- `-dual` loses hardest exactly where that fallback does its
damage, on angled and fast content (`L8` -4.4, `L4` -4.2, rotation -3.1,
`F2` -5.7) -- while showing its diffusion mechanism is worth far more on clean
translation than anyone could see before. Regenerating `-diffuse-dual` from
the current base, with the diffusion and without the fallback, is now a
well-motivated experiment rather than housekeeping.

## What this found

Running the ladder produced results that corrected a previously-held
conclusion, and is the reason this harness exists rather than being a
nice-to-have.

**The shader works.** On translation within its search reach it beats stock
linear blending by +2.2 to +9.1 dB, and beats no-interpolation by up to
+11.7 dB. This is the first time that has been quantified rather than
asserted.

**Flat regions are fine; ambiguous ones are not.** Same object, same
motion, only the interior texture changing:

| interior | gain vs `linear` |
|---|---|
| periodic, period 40px (2.5x the motion) | **+9.10 dB** |
| flat, no texture at all | +6.40 dB |
| aperiodic noise | +5.33 dB |
| periodic, period 15.7px (0.98x) | +1.25 dB |
| periodic, period 16.0px (1.00x) | **+0.48 dB** |

Monotonic in how close the texture's period sits to the distance travelled
per frame. This *contradicts* the earlier "aperture problem" diagnosis:
flat interiors score near the top. A wrong vector inside a flat region still
samples the same colour, so the error self-conceals. The real failure is
**correspondence ambiguity** -- a repeating pattern makes "moved one full
period" and "did not move" genuinely indistinguishable from two frames and a
local search.

**The failure is visible directly.** Under `interpolate-debug-grid.glsl`,
the ambiguous case shows correct flow only in two narrow strips at the
object's leading and trailing edges, with the entire interior exactly zero.
The same object with aperiodic noise shows uniform correct flow throughout.
Correct-at-edges plus zero-in-interior is precisely what produces the
long-reported "smudge tool pushed part of the image but left some behind"
artefact: the edges displace, the interior stays.

**Two plausible mechanisms were tested and refuted**, each in minutes:

- *"A refine level wanders onto a period alias"* -- `REFINE_SEARCH_RADIUS`
  2->1 changed nothing anywhere; several cases came out bit-identical.
- *"The pattern averages flat at 1/16 res, so the contrast gate fires"* --
  disabling the coarse gate entirely produced **bit-identical** output. It
  never fires here.

What actually happens is that the regulariser is working as designed: the
cost surface really is flat, `REG_LAMBDA` exists to break exactly that tie
toward zero, and it does. The information needed is not in the local block
at all -- only the surrounding edges know the true motion. **So neither
contrast-gate nor refine-search tuning can fix this**; only spatial
propagation of flow from confident regions can.

**Past its reach, the shader is actively harmful.** At 40px/frame it scores
*worse than stock linear blending* (-0.54 dB) -- it commits to a wrong
vector and warps confidently, where linear degrades to a symmetric ghost.
That is a separate, cheaper-to-fix problem than the above: a match-quality
check that falls back to blending when the best cost stays poor.

## What the flow-diffusion generation ("gen2") actually does

The edge-aware confidence-weighted flow diffusion built at `ae2887b` (8 extra
passes: 2 confidence + 6 diffusion, 31 total vs 23) was designed to fix the
ambiguous-texture failure by propagating trusted edge flow into untrusted
interiors. Measured against the ladder, it **does not do that at all**:

| case | gen2 - gen1 |
|---|---|
| `M3_period16_trap` (the target) | **+0.01** |
| `L7_textured_large` | **+0.04** |
| `M1_noise_large` | +0.11 |
| `L4_trans_40px` | +0.00 |
| `L2_trans_16px` | +1.65 |
| `L3_trans_23px` | +1.99 |
| `L6_flat_large` | +1.34 |
| `L1_trans_8px` | +1.44 |

Every gain lands on cases that already worked; the ambiguity cases it was
built for are untouched. **The reason is in its confidence metric**, which is
local luma contrast alone:

```glsl
return vec4(clamp((hi - lo) / CONFIDENCE_SCALE, 0.0, 1.0), ...);
```

In the trap case the interior contrast is ~0.43 against a `CONFIDENCE_SCALE`
of 0.1, so confidence **saturates to 1.0 across the entire wrong-flow
interior**, and diffusion correctly declines to overwrite a maximally-
confident region. Correspondence ambiguity is a *high-contrast,
high-confidence, wrong-answer* failure, and contrast measures texture
presence, not match reliability.

So gen2 is a general flow-field regulariser -- worth roughly +1.5 dB on
well-conditioned content, and visibly less tearing on real footage (SSIM
+0.004 mean, +0.013 on the highest-motion segment) -- but it is not a fix for
the defect that motivated it. Its cost measured here is 1.8x gen1's render
time in software, closely matching the 1.9x reported on real GPU hardware
(172 -> 89 fps).

**The concrete improvement this points at:** feed diffusion a confidence
derived from *match quality* rather than contrast -- the SAD cost at the
chosen match, the margin between best and second-best candidate, or
forward/backward flow consistency (computable from the existing `FLOW_*`
textures with no new search). Any of those is low near an ambiguous match and
high near a reliable one, which is exactly the signal diffusion needs and
exactly what contrast cannot provide.

## Fixing it: what actually worked

Following that lead produced
`bidirectional-interpolation-diffuse-coarse.glsl`. **Two** things had to
change, and testing them one at a time is what found the second.

### 1. The confidence signal

Replacing local contrast with **match distinctiveness** -- how much better
the chosen match is than the best genuinely-different rival:

```glsl
conf = 1 - cost(chosen) / cost(best rival)
```

A ratio, not a difference, so it needs no absolute threshold and is
invariant to local contrast and exposure. It goes to 0 when a rival ties the
winner (ambiguous), to 0 when everything ties (flat -- also correctly
untrusted), and approaches 1 only when the chosen match is distinctly best.

Measured at matched resolution, this beat contrast on exactly the cases it
targets (ambiguous-case mean 23.88 vs 23.60) and lost on well-conditioned
ones. But the trap case itself barely moved: 21.91 -> 21.96.

*A confound worth noting:* the first attempt changed the metric **and** its
resolution at once. Re-running as a 2x2 showed resolution was not the cause
at all -- quarter-res was slightly *better* than half for both metrics. Always
separate the variables before concluding.

### 2. Where diffusion runs -- the binding constraint

The same ambiguous content at four object sizes, half-resolution diffusion:

| ambiguous object | distinctiveness gain |
|---|---|
| **60px** | **+1.07 dB** |
| 120px | +0.01 |
| 200px | +0.03 |
| 300px | +0.05 |

Diffusion carries radius 4 x 2px = 8px per pass, ~24px over three passes. It
repairs a region it can physically cross and nothing wider. **Reach, not the
confidence signal, was the limit** -- and no confidence metric can fix that,
because the information never arrives.

Moving diffusion to the coarsest level solves it: at 1/16 resolution one
texel is 16px of source, so the same radius reaches **64px per pass** (~190px
over three) while costing **1/64 as much per pass**. Strictly better on both
axes. The refinement levels then carry the repaired coarse flow down, which is
what they already exist to do.

### Results

| ambiguous object | base | fine diffusion | **coarse** | **coarse+fine** |
|---|---|---|---|---|
| 60px | 36.88 | 36.92 | 42.63 | **43.29** |
| 120px | 30.66 | 30.68 | 37.52 | **38.33** |
| 200px | 25.78 | 25.79 | 28.66 | **28.73** |
| 300px | 21.91 | 21.91 | 23.19 | **23.20** |
| general ladder, mean | 32.48 | 33.35 | 32.71 | **33.88** |
| real footage, SSIM | 0.9292 | 0.9334 | 0.9355 | **0.9415** |
| software render cost | 1.0x | 1.8x | **1.6x** | 2.7x |

Coarse-only is the better trade: **cheaper than the fine-diffusion variant
and far more effective**. Coarse+fine is the highest quality measured, at
2.7x. Neither is GPU-validated yet.

One case regresses under both: `L7_textured_large` (-0.5 dB), a 300px object
whose texture period is 15.7px against 16px of motion -- near-but-not-exact
aliasing. `M3` at exactly 16px improves (+1.28), so this is not simply "large
ambiguous regions". Unexplained; worth a look before adopting either variant
as the default.

## The remaining defect: edges

Real-hardware testing of the coarse-diffusion variant (196fps at 720p,
142fps at 1080p -- effectively free) reported the ambiguity fix helping
somewhat on live action, but the cartoon source still showing the original
defect, with **edges** as the sticking point: "when the edges lose their
definition the whole composition of the interpolated frame is ruined."

That is confirmed and quantified by `edgeerror.sh`:

| variant | err at edges | err elsewhere | ratio |
|---|---|---|---|
| linear blend | 24.45 | 5.45 | 4.5x |
| base | 18.53 | 3.74 | 5.0x |
| coarse diffusion | 17.56 | 3.37 | 5.2x |
| coarse+fine | 16.20 | 2.95 | 5.5x |

Edges are ~15% of pixels but carry ~5x the per-pixel error, so roughly half
of all error. Coarse diffusion improves edge error by only **5%** -- real,
but far too small to perceive, which is exactly why whole-frame PSNR/SSIM
said "clearly better" while a viewer said "no change". **This is the metric
to watch for this defect.**

### What has been ruled out

- **Edge-aware (joint bilateral) flow upsampling in the warp.** The flow
  field's finest level is half resolution, so it is bilinearly upsampled,
  which blends foreground and background motion across a several-pixel band
  at every object boundary -- a plausible cause of dark outline pixels being
  dragged into light regions. Replacing that with a guided upsample, using
  the full-resolution source luma to weight neighbouring flow values so the
  discontinuity snaps to the real image edge, cost ~6% and changed edge
  error by **0.04 (17.56 -> 17.52), i.e. nothing.** Refuted.
- **Diffusion damaging edges.** The `E1`-`E4` motion-discontinuity cases
  above were added specifically to test this (every earlier scene put the
  object on flat black, where smeared flow cannot show). Coarse diffusion
  *improves* all four (+0.16 to +1.65 dB). Not the cause.

### What is known

Isolating the pipeline with `interpolate-debug-warp-stages.glsl` at the real
24->60 rate shows the individual directional warps are largely clean, with
mild raggedness at high-contrast boundaries -- so the defect is not a gross
flow failure, and not the cross-blend or the occlusion fallback either.

## Grid alignment -- MOSTLY EXPLAINED, see the correction below

> **Correction (added after the occlusion-fallback fix).** The 10.5 dB
> grid-alignment deficit described in this section was *largely the occlusion
> fallback misfiring*, not an intrinsic limit of block matching on angled
> content. Re-measured after that fix, the base interpolator scores 34.34 at
> 0 degrees and 33.07 at 45 -- a gap of **1.3 dB**, down from 10.5 -- and its
> absolute score at 45 degrees rose from 20.34 to 33.07.
>
> The mechanism: the `(4, 7)` px gate fired harder on angled content, because
> FB-consistency errors are larger there, so its damage was itself
> angle-dependent. That is the shape originally misread as a property of the
> square grid. The measurements below are all correct as taken; the
> *interpretation* of them as a grid effect was not.
>
> The controlled-experiment design in this section still stands, and remains
> the right way to isolate grid alignment. It is kept in full because the
> reasoning is sound and because the mistake is instructive: a deficit that
> varies with a variable is not necessarily *caused* by that variable.



Every scene above uses axis-aligned rectangles, so every edge is exactly
horizontal or vertical -- lined up with both the pixel grid and the flow
field's block grid. That is the one case a square flow grid can represent
exactly, and real content essentially never looks like it.

`scene_rot` isolates this: pattern **and** motion rotate together, so the
geometry is identical at every angle and only the alignment to the square
grid changes. Cells are band-limited, so angled edges are not aliased.

| grid angle | hold | linear | shader | gain vs linear |
|---|---|---|---|---|
| 0 deg | 15.34 | 19.14 | **30.86** | **+11.72** |
| 10 deg | 15.33 | 19.13 | 22.96 | +3.83 |
| 22.5 deg | 15.33 | 19.13 | 20.66 | +1.53 |
| 45 deg | 15.33 | 19.13 | **20.34** | **+1.21** |

**`hold` and `linear` are flat across all four angles.** The content is
equally hard at every angle; only the motion-compensated shader degrades,
losing **10.5 dB** and nearly all of its advantage over a plain blend. This
is the largest single effect found in this project, larger than the
correspondence-ambiguity problem, and it applies to essentially all real
content.

A second experiment, using isotropic noise so the pattern has no preferred
direction, separates motion *direction* from motion *magnitude* alignment:

| motion (px/frame) | gain vs linear |
|---|---|
| (15,0) axis-aligned | **+4.89** |
| (10,0) axis-aligned | **+0.03** |
| (15,15) diagonal | +2.14 |
| (10,5) diagonal | -0.63 |

Both matter, and note that *axis-aligned* motion can also collapse (+0.03).
So this is not purely about diagonal edges.

### Mechanisms ruled out

Four candidate explanations were each tested and refuted, which is worth
recording so they are not re-tried:

- **Sub-pixel resampling blur.** Motion vectors were chosen so displacements
  are exactly integer at every output frame (multiples of 5 px/frame, since
  `mix_t` steps by 0.2), meaning no resampling occurs at all. Diagonal motion
  collapsed identically with and without resampling. Not the cause.
- **Anisotropic regularisation.** Both regularisers penalise by Euclidean
  length, so a diagonal step costs sqrt(2) more than an axis-aligned one.
  Zeroing both changed diagonal by -0.03 dB (and hurt axis-aligned, as
  expected). Not the cause.
- **Sub-pixel search quantisation.** The coarse search halves its step 5
  times from 0.75 texels, so flow lands on a 0.75px lattice. Extending to 7
  and 9 iterations (0.19px, 0.047px lattice) changed off-lattice cases by
  0.01 dB. Note 10px is off-lattice at *every* depth, since 10/0.75 = 40/3 is
  never a dyadic multiple -- so the residual error shrinks to 0.016px with no
  benefit, cleanly ruling sub-pixel accuracy out.
- **Edge-aware flow upsampling** (see above). No effect.

Two further candidates, both aimed at the square structures inside the coarse
search itself, were also tested:

- **Isotropic search directions.** The 8 candidates are `(x,y)` on a square
  lattice, so axis candidates sit at radius `s` and diagonal ones at
  `s*sqrt(2)` -- the search samples direction space unevenly. Normalising all
  8 onto a circle of radius `s` made things slightly *worse* everywhere
  (-1.35 dB at 0 deg, -0.5 at 22.5 deg).
- **Isotropic matching aperture.** `sad5x5_s` sums a square 3x3 box, which
  reaches `sqrt(2)` further at its corners than along its axes, so match
  strength depends on the orientation of edges inside the window. Gaussian
  weighting by radius helps off-axis in the expected direction (+0.21 dB at
  22.5 deg, +0.11 at 45 deg) at a small on-axis cost (-0.45 dB). Real, and
  the right sign -- but 0.2 dB against a 10 dB deficit.

The effect is real, large, reproducible, and controlled. Its mechanism is
**still unidentified** -- worth stating plainly rather than guessing at,
because six plausible-sounding explanations have now failed. That pattern
(every local, parameter-level fix producing tenths of a dB against a ~10 dB
gap) is itself evidence: it suggests the limit is structural to local
block-matching rather than a defect in any one part of it, and that closing
it would need a different class of flow estimator -- a global/variational
solve rather than independent local searches -- not another constant.

### Matching costs: SAD wins, so there is no cheap win here

Search *geometry* has been tuned exhaustively, but every version minimised SAD
on raw luma -- the least discriminative common choice. Four costs were
compared across all 8 matching functions, each also built with regularisation
zeroed (the regulariser is added to the raw cost, so a differently-scaled cost
silently changes regularisation strength; zeroing it isolates the data term):

| case | linear | shipped | sad r0 | ssd r0 | zsad r0 | census r0 |
|---|---|---|---|---|---|---|
| rot 0 deg | 19.14 | **30.86** | 25.45 | 23.63 | 23.91 | 18.69 |
| rot 22.5 deg | 19.13 | **20.66** | 19.60 | 19.41 | 19.45 | 18.58 |
| M1 noise | 20.65 | **25.98** | 25.45 | 25.45 | 25.35 | 20.39 |
| L9 occlusion | 32.07 | **36.09** | 31.77 | 31.80 | 31.79 | 31.68 |

SAD is best and every alternative is worse. Census is dramatically bad --
flat at ~18.6 across all angles, *below* plain linear blending -- which is
explicable rather than surprising: it buys illumination invariance this
content does not need, and pays by discarding magnitude to keep only 8 bits of
local ordering, which at smoothed coarse pyramid levels is mostly noise.

Incidentally: shipped SAD **with** regularisation scores 30.86 against 25.45
**without** it. The regulariser is worth 5.4 dB, consistent with the wider
finding that coherence is exactly what this estimator is short of.

## Variational refinement: milestone 1

The structural conclusion above -- that coherence has to be *in* the
objective, not imposed afterwards -- was tested by adding a warped
Horn-Schunck stage with edge-aware smoothness on top of the existing pyramid,
at half resolution. `gen_variational.py` generates it (the DSL has no loop
across passes, so each iteration is its own `//!HOOK` block; 24 iterations per
direction is 71 passes total, which libplacebo compiles and runs without
complaint).

On the rotation ladder -- the ~10 dB deficit this was aimed at -- it works,
and scales monotonically with iteration count, which is what a converging
solver should do:

| angle | linear | base | var4 | var12 | var24 | var24 - base |
|---|---|---|---|---|---|---|
| 0 deg | 19.14 | 30.86 | 35.95 | 37.45 | **38.24** | **+7.38** |
| 10 deg | 19.13 | 22.96 | 23.23 | 23.90 | 26.68 | +3.72 |
| 22.5 deg | 19.13 | 20.66 | 21.09 | 22.37 | 24.82 | +4.16 |
| 45 deg | 19.13 | 20.34 | 20.26 | 22.22 | **25.64** | **+5.30** |

At 45 degrees the advantage over a plain blend goes from +1.21 dB to +6.51 dB.
The diagnosis is validated.

**But it does not transfer to real footage:**

| | linear | base | coarse diffusion | var12 | var24 |
|---|---|---|---|---|---|
| SSIM mean | 0.9062 | 0.9292 | **0.9355** | 0.9314 | 0.9334 |
| edge error | 24.45 | 18.53 | **17.56** | 18.68 | 18.31 |

It beats the base shader but loses to the coarse diffusion already in the
tree, and the reason is the reach lesson again. **Where the image is flat,
`Ix = Iy = 0`, so the Horn-Schunck update degenerates to `f_new = favg`** --
pure neighbourhood averaging. Flat-shaded animation is mostly flat, so on that
material this whole stage collapses into short-range diffusion at half
resolution, which is precisely the configuration already measured as
ineffective (+0.02 dB at 120px). It excels on the checkerboard because that
has brightness gradients everywhere and a single uniform motion.

So the mechanism is right and the placement is wrong -- the same mistake the
diffusion work made, and for the same reason.

## Milestone 2: iterate at every pyramid level -- this is the fix

Spreading the same iterations across the whole cascade (16/12/8/4 at
S/E/Q/H) rather than concentrating them at half resolution. One iteration
propagates information one texel, so at 1/16 resolution that is 16px of reach
per iteration against 2px at half resolution -- the same arithmetic that made
coarse diffusion work.

| angle | linear | base | var24 (half-res only) | **cascade** |
|---|---|---|---|---|
| 0 deg | 19.14 | 30.86 | 38.24 | 37.94 |
| 22.5 deg | 19.13 | 20.66 | 24.82 | **30.42** |
| 45 deg | 19.13 | 20.34 | 25.64 | **32.66** |

**+12.3 dB over the base shader at 45 degrees**, and the grid-alignment gap
that started this line of work halves (10.5 -> 5.3 dB). Note it is also
*cheaper* than the half-res-only version, because coarse iterations cost
almost nothing -- and that adding more fine-level iterations (24/16/10/6)
makes things slightly *worse*, which is the reach principle again.

**And unlike milestone 1, it transfers to real footage:**

| | linear | base | coarse diffusion | var24 | **cascade** |
|---|---|---|---|---|---|
| SSIM mean | 0.9062 | 0.9292 | 0.9355 | 0.9334 | **0.9546** |
| SSIM, highest-motion segment | 0.7926 | 0.8616 | 0.8806 | 0.8743 | **0.9340** |

Visually it resolves the reported defect directly: on the reference clip
(`blueyreduced.mp4`, source frames 29-40) the moving character's dark outline
stays continuous instead of fraying into dashes.

Costs, measured like-for-like on one 3s segment (render only): linear 2.7s,
base 12.9s, coarse diffusion 17.0s, coarse-only cascade 26.0s, **cascade
31.0s (2.4x base)**, heavy cascade 38.4s. Software rasterisation, so treat
the *ratio* as indicative and confirm on GPU.

Small regressions remain on cases that were already good (-0.2 to -0.7 dB on
the trap, noise, plain-translation and occlusion cases). Occlusion is the
expected weak spot: a smoothness term necessarily fights a genuine motion
discontinuity, and an L1/TV penalty rather than this L2-style one is the
standard answer if it matters.

### 23.976 vs 24: no error, but a calibration difference

"24fps" almost always means 24000/1001 = 23.976. That matters here because
60/24 = 2.5 exactly while 60/23.976 = 2.5025 does not, so it is worth being
explicit about what is and is not affected.

**The shader is unaffected.** It never sees a frame rate -- only `mix_t`,
which libplacebo derives from real PTS. Verified directly: an identical scene
at an identical physical velocity (specified in px/*second*, so rate-agnostic)
rendered as a 24.000 source and as a 23.976 source, both interpolated to 60
and scored against the same 60fps ground truth:

| shader / source | all frames | passthrough | synthesised | # passthrough |
|---|---|---|---|---|
| base @ 24.000 | 28.12 | 58.8 | 20.44 | **24** |
| base @ 23.976 | 19.72 | 58.8 | 19.39 | **1** |
| variational @ 24.000 | 28.23 | 58.8 | 20.58 | 24 |
| variational @ 23.976 | 19.77 | 58.8 | 19.44 | 1 |

Passthrough frames score an identical 58.8 dB in all four cases, confirming
alignment is correct throughout.

**But the ladder is slightly optimistic.** The large "all frames" gap is not
error: at exactly 24->60 `mix_t` cycles 0/0.4/0.8/0.2/0.6 with period 5, so
every 5th output frame is a free exact copy (24 of 121). At 23.976->60 the
phase drifts and there are effectively none (1 of 121). Synthesised-frame
quality matches within ~1 dB, and even that is because the drifting phase
visits `mix_t` near 0.5 -- the hardest point -- more often than the fixed
four-phase cycle does.

Since the synthetic scenes here are generated at exactly 24 and 60, they get
that free frame every fifth output and real 23.976 content does not. Rankings
between modes are unaffected; absolute figures are a little flattering
compared with real playback. The real-footage harness is immune, since its
2:1 decimation classifies frames by parity rather than by assuming a period.

## The occlusion fallback: two independent defects

Real-hardware testing of the cascade reported a residual artifact on
`avengersclip.mp4` (source frames 539-553, a head moving left to right): the
leading edge against a near-static background "resembles wobbling jelly" and
appears to **snap** into place, suggesting a timing abnormality.

It is a timing abnormality, and it is generated by the shader. The warp pass
had:

```glsl
float occluded = smoothstep(4.0, 7.0, fb_error_px);
vec4 fallback = mix_t < 0.5 ? HOOKED_tex(HOOKED_pos) : NEXT_tex(NEXT_pos);
```

**Defect 1 -- discontinuity.** That ternary is a hard switch. Wherever
`occluded` is non-zero -- the edges of a moving object -- the output jumps by
the full inter-frame displacement the instant `mix_t` crosses the midpoint,
once per source frame pair, every ~2.5 output frames at 24->60.

Measurable directly, as frame-to-frame change in the output grouped by phase
(5 output frames span exactly 2 source pairs, so `mix_t` crosses 0.5 twice):

| variant | median | by phase (n mod 5) | max/min |
|---|---|---|---|
| linear blend | 11.3 | 12.4, 10.2, 9.0, 11.6, 12.9 | 1.43x |
| base shader | 12.5 | 7.6, **46.6**, 5.8, **51.2**, 7.0 | **8.75x** |
| cascade | 17.7 | 15.6, 21.8, 14.2, 25.8, 13.9 | 1.86x |

Smooth motion gives a flat series. An 8.75x spike on exactly the two phases
where the crossing happens is the shader, not the content. (The cascade
already suppressed it to 1.86x, because better flow means lower FB error means
less weight on the fallback.)

**Defect 2 -- threshold.** The `(4, 7)` px gate fired at ordinary object edges,
not only at genuine occlusion. `L2_trans_16px` is *pure translation with no
occlusion at all*, and disabling the gate entirely gained **+5.5 dB** there.
It was discarding good warps precisely where detail matters.

The two are independent -- raising the threshold makes the jump fire less
often but does not remove it -- so both were fixed:

| | gate10 only | fallback OFF | **both fixed** |
|---|---|---|---|
| synthetic mean | 34.92 | 36.18 | 35.15 |
| real SSIM | 0.9595 | 0.9576 | **0.9590** |
| jitter max/min | -- | 1.31x | **1.12x** |

Disabling the fallback outright wins on synthetic but *loses* on real footage
(seg_240: 0.9519 against 0.9590), so occlusion handling is still earning its
place -- it was simply mis-tuned. Fixing both gives real SSIM 0.9546 -> 0.9590
against the previously shipped cascade, and jitter 1.86x -> **1.12x**, flatter
than plain linear blending's own 1.43x.

### Resolution: the fallback is gone entirely

A third version was then built -- **directional** handling, judging each side's
reliability at its own sample position and weighting toward the
self-consistent one, using the *warped* sample so no ghost is possible. That
is the geometrically principled form: a leading edge covers background (those
pixels exist in A, not B), a trailing edge reveals it (B, not A), so which
frame to trust is a property of the geometry rather than of where `mix_t` sits.

All three were then viewed directly against **no fallback at all**, on a clip
cut specifically around the reported artifact (`headdefect.mkv`, a head
translocating faster than its surroundings). **No-fallback was cleanest in
every comparison** -- the other three each introduced more than they removed.

Re-measured after removal:

| | with fallback | **without** |
|---|---|---|
| bluey SSIM | 0.9590 | 0.9576 |
| avengers SSIM | 0.9773 | **0.9777** |
| `L9_occlusion` | 35.82 | **40.09** |
| `L2_trans_16px` | 34.40 | **39.92** |
| temporal jitter | 1.12x | **1.09x** |
| render time (variational) | 31.9s | **30.9s** |

Better nearly everywhere, best jitter measured, and slightly faster -- it also
removes a full-resolution texture fetch per pixel. Only the cartoon dips, by
0.0014, which is noise at this scale.

**Why removal works, rather than merely being less bad:** `mc_result` already
degrades gracefully on its own. Both samples use the same flow, so where that
flow is wrong they are wrong *together and in the same direction*, which stays
spatially coherent; and as `mix_t` approaches 0 or 1 the blend converges on
the unwarped nearest frame anyway, continuously. Substituting an unwarped
frame mid-interval buys nothing and costs an edge.

**Note the metric disagreed.** Whole-frame SSIM prefers keeping the fallback
on the cartoon, marginally. But that metric rates the segment *containing* the
reported artifact as the best of three -- it is demonstrably blind to this
defect, and a metric that cannot see the thing being judged does not get the
casting vote. `interpolate-debug-grid.glsl` still visualises the
forward/backward consistency error; seeing where it fails is useful even
though nothing acts on it now.

### Historical: the production shader wanted a different gate

Both defects were also present in `bidirectional-interpolation.glsl`, so its
settings were swept separately rather than inheriting the cascade's -- and it
is as well they were:

| | shipped | (4,7)+cont | (10,16)+cont | **(20,30)+cont** | off |
|---|---|---|---|---|---|
| synthetic mean | 32.39 | 32.73 | 33.04 | 34.34 | **34.91** |
| real SSIM | 0.9292 | 0.9332 | 0.9418 | **0.9460** | 0.9463 |
| jitter max/min | **8.75x** | 1.42x | 1.29x | **1.24x** | 1.34x |

The production shader measures best at a **higher** gate (20, 30) than the
variational build (10, 16), despite having the *weaker* flow field. That is
counterintuitive but it makes sense: a weaker flow field produces larger
FB-consistency errors everywhere, so a low gate fires far too broadly. Worse
flow needs a *less* trigger-happy fallback, not a more aggressive one.

`(20,30)` was chosen over disabling the fallback because their real-footage
means are a statistical tie (0.9460 vs 0.9463), `(20,30)` has the better
jitter, and it keeps the mechanism for `seg_240` where the fallback genuinely
helps (0.9525 vs 0.9477). **Re-measure rather than inherit if either shader's
flow estimation changes again.**

The three diagnostic shaders were updated to match, since a diagnostic that
still showed the old artifact would be actively misleading; `interpolate-debug-grid.glsl`
also visualises the occlusion mask, so its threshold has to be the same one
the warp actually uses. The two experimental diffusion variants are
deliberately left alone -- they are superseded snapshots, and rewriting them
would misrepresent what was measured for them.

## The residual fast-object artifact: three remedies, none of them helped

Real-hardware testing of the variational build reported it as a large
improvement (81fps at 1080p, "frame by frame is extraordinary"), with a
residual on `avengersclip.mp4` frames 539-553: a head translocating
horizontally *faster than the rest of the scene*, where the artifact is now
"more a linear fade and less of a jelly", plus a few frames where the nose
"gets left behind".

"Fast object lags, protruding feature lags most, artifact at the object's
defining edges" is the textbook signature of an L2 smoothness penalty
over-regularising -- the fast object's flow gets averaged toward its slower
surroundings. Three remedies were built and measured against ground truth
cut from the avengers clip itself:

- **robust smoothness** -- weight neighbours by flow similarity as well as
  luma, approximating a discontinuity-preserving penalty (sigma 2.0 and 1.0
  texels)
- **weaker smoothness** -- `VAR_ALPHA` 0.3 -> 0.15
- **wider coarse reach** -- `step_px` 0.75 -> 1.0 (~23px -> ~31px), since the
  measured p99 flow magnitude sits at 24.7px, right at the old ceiling

**None of them changed anything measurable.** Segment means differ by at most
0.0007 SSIM; worst-3-frame means by at most 0.0014. Visually, current and
robust are indistinguishable at 2x zoom on the face.

Two things worth recording from the attempt:

**The motion is within reach, so this is not a reach failure.** Flow
magnitudes in the reported frames: median 5.3px, p90 18.5px, p99 24.7px, with
only 0.6% of pixels off-scale (>30px). Only the fastest ~1% brushes the
coarse-search ceiling.

**The metrics cannot see this defect, which is why the variant test was
uninformative.** Whole-frame SSIM rates `seg_22` -- the segment *containing*
the reported artifact -- as the best of the three segments (0.9836 against
0.9698 and 0.9784). An artifact lasting a few frames in a small region is
simply below what a frame-averaged, segment-averaged metric can resolve, and
worst-frame statistics did not rescue it either.

That is the real blocker here, and it should be fixed before more variants
are generated: **without a measurement that responds to this artifact,
producing more candidates is guessing.** The instrument that would probably
work is temporal consistency of the *flow field* rather than of the pixels --
a flow that flickers frame-to-frame in a region whose true motion is smooth
produces exactly "wobble" and "left behind", and unlike pixel error it is not
diluted by the 99% of the frame that is fine.

The robust-smoothness option is kept in `gen_variational.py` (`sigma_flow`,
default 0 = disabled) so it is available if a better metric later shows it
helping. Its default output was verified bit-identical over 24 frames against
the previously committed shader.

### A known limitation of this whole ladder

Every scene here was, until 2026-08-31, built from regular geometry:
rectangles, checkerboards, sine products. Real edges are neither straight nor
smoothly curved; they are irregular, closer to a stack of many spatial
frequencies than to any simple formula, and they carry that irregularity along
their whole length -- so passing this ladder is necessary, not sufficient.
`blueyreduced.mp4` (source frames 29-40, the orange dog walking left) is the
reference case for what the defect actually looks like on real material: a
moving character whose dark outline frays into dashes while stationary
characters in the same frame stay clean.

**This section used to go further and claim that a synthetic pattern could
reproduce "*an* angle, *a* frequency, or *a* motion, but not the joint
irregularity of real content". That was wrong, and it was wrong in a way worth
recording, because it discouraged exactly the work that fixes it.** A Fourier
series represents any shape. Irregularity is a matter of writing down enough
terms, not a property only real content can possess -- you can draw the
outline of a duck this way. The honest limitation was never expressive power;
it was that nobody had built the tooling.

`F1_fourier_edge` is the first scene that does. Its boundary is
`r(phi) = R*(1 + SUM a_n cos(n*phi + psi_n))` with `a_n = 0.36/n` -- a 1/f
amplitude spectrum, which is the spectrum of a fractal (fractional Brownian)
boundary, carrying comparable detail at every scale it represents rather than
one characteristic wiggle size. Harmonics 3, 5, 8, 13, 21, 34 are deliberately
non-harmonic so none reinforce into a regular polygon. See `scenes.sh`.

Two things it does **not** do, stated precisely so the claim is not
over-corrected in the other direction:

- It is the **radial** form, so the curve is single-valued in `phi` and
  therefore star-shaped: it cannot produce a concavity that doubles back, like
  a duck's beak. That needs the **parametric** form,
  `z(s) = SUM c_n exp(i*n*s)`, which draws any closed curve at all -- but that
  is a curve rather than an inside/outside test, and `geq` evaluates one pixel
  at a time with no loops to run a crossing test in. The parametric form needs
  a rasterisation step and an image input; the radial form needs nothing.
  Whether the extra generality buys anything measurable is untested.
- A synthetic scene still has no sensor noise, no compression artefacts, no
  motion blur, and no deformation. Irregular geometry closes one gap, not the
  rest.

Fractals are a live candidate for the same reason and mostly the same
tooling. A 1/f radial spectrum is already a fractal boundary; a genuine
escape-time fractal would need iteration, which `geq` cannot express, so it
would come in as a pre-rendered input and give up the "no source files"
property. Worth doing only if the 1/f boundary turns out not to be irregular
enough to find anything.

### The ladder reset: ground truth used to be pixel-quantised

Found 2026-08-31 while building `scenecheck.sh` to validate new scenes, and it
turned out to matter more than the scenes did. **Fixed the same day by
rewriting every scene analytically; this section records what was wrong and
why every number before that date is not comparable with one after it.**

**`overlay` places its object at a whole, even pixel.** yuv420p chroma
subsampling forces 2px alignment, so a true position of 3.2px was rendered at
2, 6.4 at 6, and 9.6 at 8 -- measured directly, not inferred. The 60fps
"ground truth" therefore advanced in 2px steps where the motion it represented
was smooth, and carried up to 1px of position error at every frame. **A shader
that interpolated correctly to a fractional position was marked down against
it.**

There was a second, worse consequence that only showed up on inspection: the
24fps SOURCE frames were sometimes wrong too. At the instants where the two
rates coincide, the object sits exactly on an even-pixel boundary, so the snap
is a knife edge -- and the two rates do not compute `t` identically:

```
t = 7/12 s, reached as source frame 14 of 24 and output frame 35 of 60
  14 * (1/24) = 0.58333333333333325932
  35 * (1/60) = 0.58333333333333337034     one ULP apart
x = 192 * t   = 111.99999999999998579  vs  112
  truncated       111   vs   112
  snapped to even 110   vs   112          <- a 2px disagreement
```

Multiplying by a rounded reciprocal does it: `1/24` and `1/60` are each
inexact, and the two products land on opposite sides of the integer. So on
those frames the object was rendered 2px away from where the scene's own
arithmetic said it should be. Confirmed by direct measurement: on `L1` frame
14 the true left edge is `8*14 = 112`; the old scene rendered it at 110.

Note what that is an instance of -- an arithmetic difference far below any
meaningful scale, amplified into a visible discrete jump by a hard decision
boundary. It is structurally the same fault as the block match's argmin
flipping on a near-tie, which `TIE_MARGIN` exists to stop.

**The fix: exact box-filter coverage.** Pixel X spans `[X, X+1)`, and a
rectangle spanning `[x0, x0+w)` covers `clip(min(x0+w, X+1) - max(x0, X), 0, 1)`
of it. That is area sampling, not a cosmetic soft edge, and the difference
matters: at an integer position it is 0 or 1 everywhere, so a hard-edged
rectangle stays hard-edged with no anti-aliased fringe invented anywhere; at a
fractional position it is what an ideal renderer would produce. `scenes.sh`
has the implementation.

`scenecheck.sh` now reports the two failure modes separately, because they are
not the same finding. A **positional** difference means the object is in a
different place at the same instant depending on frame rate, and the scene is
broken. **Exact to rounding** means a max delta of 1 on an anti-aliased edge
texel -- the ULP in `t` tipping a coverage value that sat exactly on a
rounding boundary, about 89 dB, on one frame in twelve. After the rewrite,
twelve of twenty-one cases are bit-identical between the rates and the other
nine are exact to rounding. None are positional.

**One content change was unavoidable.** `M1_noise_large`'s texture was a
`floor()`-quantised hash on a 4px grid, and a texture quantised to a grid
cannot be translated to a fractional position -- `floor()` snaps it straight
back to whole pixels, reintroducing inside the object exactly the quantisation
the rewrite removes from its boundary. It is now a sum of five sines at
incommensurate frequencies: still aperiodic with no repeat, which is M1's
actual job in the texture series, but band-limited (shortest period 4.6px) so
it translates exactly. Every other scene's content is unchanged except where
the old one was in the wrong place.

**Why the numbers moved so much.** On `L1_trans_8px` the base shader goes from
41.35 dB to 61.29 -- almost 20 dB. The interpolator was always that accurate on
smooth translation; the ladder could not report it, because the target it was
scored against was quantised to 2px and the shader was being penalised for
being right. Its margin over stock `linear` on that case goes from +4.90 dB to
+25.85. Expect the largest gains on the cleanest, most sub-pixel cases and
little change where the score is dominated by a genuine estimation failure.

## Real footage: decimate-and-reconstruct

Synthetic scenes cannot show how the shader behaves on real content. Real
footage has no native ground truth -- but it can be manufactured: drop every
2nd frame, interpolate back to the original rate, and compare against the
frames that were deleted. Those frames are the exact correct answer. This is
the standard frame-interpolation benchmark method and needs no special
source material.

```bash
export FFMPEG=~/build/ffmpeg/ffmpeg FFPROBE=~/build/ffmpeg/ffprobe
./screen.sh source.mkv                                   # find usable segments
./realbench.sh source.mkv linear linear      210 240 300
./realbench.sh source.mkv gen1 ../shaders/bidirectional-interpolation.glsl 210 240 300
./realanalyze.py linear gen1
```

### Real-footage traps

These are not hypothetical -- each one silently produced a full table of
confident, meaningless numbers before being caught.

- **A misaligned benchmark does not fail, it lies.** It returns well-formed
  dB figures in a believable range that rank the modes plausibly. So build in
  a *passthrough check*: the retained frames must come back bit-exact, and
  that must be asserted on every run. If it fails, stop -- nothing else in
  the output means anything. This check caught all three alignment bugs
  below.
- **`psnr` pairs frames by timestamp, not index.** `24000/1001` fps rounded
  into a millisecond timebase does not pair cleanly, and the `fps` filter can
  emit an extra frame at EOF, flipping the parity of the whole comparison.
  Fix: `setpts=N/TB` on **both** inputs immediately before `psnr`.
- **...but `setpts=N/TB` must not appear in a render step.** Where a file is
  being written it spaces frames a second apart, and `-r` then fills the gaps
  -- 72 frames silently became 1725. Render naturally; align only when
  comparing.
- **Check whether the source is animated "on twos"** before using it. If each
  drawing is held for 2 video frames, half the frames being "reconstructed"
  are duplicates of frames the shader was handed, which flatters every mode.
  This varies *within* a single episode -- dialogue on twos, action on ones.
  `screen.sh` detects it; a held drawing shows as very high (not `inf`, since
  re-encoding perturbs it) PSNR against the previous frame.
- **~58 dB is the passthrough ceiling on real content**, not `inf`. The GPU
  round-trip and 4:2:0 chroma handling cost that much even at `mix_t=0`. It
  is identical across shader variants, so it is a constant offset, not a
  defect.
- **This test is harder than production, and by more than it sounds.**
  Reconstructing 12->24 asks for double the per-pair motion of 24->60
  playback. It is a sound *relative* ranking of modes, but its absolute
  picture is badly misleading: rendered at 12->24 the flow field on real
  cartoon footage looks like noise and the isolated directional warps come
  out visibly shattered, while the *same content at the real 24->60 rate*
  produces a largely clean warp with only mild edge raggedness. Diagnosing
  a mechanism from the decimated run alone will send you after a failure
  production does not have -- confirm anything structural at the real rate
  before acting on it (`visuals.sh` and
  the human-reading views both work on an undecimated source).

### PSNR actively misranks these methods

**Report SSIM alongside PSNR, and prefer SSIM when they disagree.** PSNR is
mean-squared error, which systematically rewards blur: a linear blend's
smooth double-image has lower squared error than a sharp but
slightly-misplaced motion-compensated frame. Measured on real footage, the
two metrics *invert*:

| metric | linear | gen1 | gen2 |
|---|---|---|---|
| PSNR mean | **26.60** | 25.63 | 25.72 |
| SSIM mean | 0.9062 | 0.9292 | **0.9334** |
| SSIM, highest-motion segment | 0.7926 | 0.8616 | **0.8743** |

Direct visual inspection agrees with SSIM, not PSNR: at the same frame, the
linear blend renders a character with three visibly overlaid ears and doubled
eyes, while the shader renders one sharp character with localised tearing.
Ranking those by squared error puts the ghost first. Use `visuals.sh` and
look, rather than trusting either number alone.

## Cartoon faces: false-match islands in the flow field

After the variational cascade and the removal of the occlusion fallback, a 60s
real-footage clip passed with no noticeable defect. The cartoon did not: eyes,
mouth and nose still broke up, on a clip (`blueydefect.mp4`, 21 frames) of a
character simply walking sideways. Trivial motion, visible failure -- which is
usually the shape of a real bug rather than a hard case.

### What it is

Render the flow field itself (replace only the final `hook()` with
`vec4(0.5 + f.x*0.05, 0.5 + f.y*0.05, 0.5, 1.0)`, leaving every pass upstream
untouched) and the cause is immediate. Across the face the field is smooth and
coherent -- the estimator has the head's motion right. But sitting *on* the eye
and *on* the mouth are compact **islands of flow pointing somewhere the entire
surrounding face disagrees with**, one of them opposite in sign to the head it
belongs to. Rendering `|warped_a - warped_b|` alongside confirms it: every
outline shows the thin red of ordinary edge residual, while the mouth and eye
show *filled* red blobs. Correspondence genuinely failed there.

The cause is the animation, not the footage. Between source frames 4 and 5 of
that clip the mouth goes from wide open with teeth to a small dark oval -- it
is **redrawn for lip-sync, not moved**. There is no true correspondence to
find. Block matching does not know that, finds a confident match to the wrong
shape, and returns a large vector. The same happens at the eye.

Note what this is *not*: it is not the aperture problem, not correspondence
ambiguity from a repeating texture, and not an edge-angle effect. Those were
the previous three diagnoses on this ladder and none of them apply. It is a
confident match to a shape that no longer exists.

### Why the existing median did not catch it

The base shader already vector-medians the flow -- but only at H, and only 3x3
run twice, so about 5x5 of reach. The mouth island is roughly 22px across,
which is **11 texels at H**. It out-votes a 5x5 kernel everywhere inside
itself. A median cannot fix at H what is already that large, and scaling the
kernel up there is not affordable: the 3x3 median at H was already the single
largest uncached cost in the shader, and cost grows as the square of the
window (a 5x5 true vector median is 625 distance computations per texel).

The same island is 5.5 texels at Q, 2.8 at E and 1.4 at S. At those levels a
3x3 kernel removes it outright, and the passes are 1/16, 1/64 and 1/256 of
full resolution. This is the **reach principle** this project has now
re-derived four separate times: do the work at the level where the kernel is
large relative to the defect, which is also where it is cheapest.

### Measuring it without being lied to

Frame-averaged image metrics cannot see this. It is a few hundred pixels on a
handful of frames, and the same blindness that made SSIM rate the segment
*containing* the fallback artifact as the best of three applies here. So
measure the defect directly instead of measuring the picture:

**Flow outlier fraction** -- for every pixel, the distance between its flow and
the *median* of its neighbourhood (radius 6px), counted against a 3px
threshold. The asymmetry that makes this work: a genuine motion boundary is a
contiguous region, so most of its neighbours share its value and its deviation
from a large-radius median stays small. An isolated false match is a local
minority everywhere and deviates hugely. The metric therefore sees false
matches and ignores real motion, which is exactly the discrimination the
median filter itself relies on.

Run it with `flowoutliers.py` against a flow-visualiser build. Baseline on
`blueydefect.mp4` was 0.0412% of pixels, ~379 per frame, with deviations up to
20.1px against a head moving 3-5px.

### The fix

`gen_variational.py` gained a median spec (argv[6], `S,E,Q,H`), emitting 3x3
vector-median passes *after* that level's variational iterations, so the
neighbourhood consensus is what seeds the next level down rather than being
re-dirtied by it. The resulting order per level is
`refine -> variational -> median`, with H's existing pair still last before the
warp. The same algorithm as the H median already in the base shader -- the
candidate minimising total distance to all others, a joint choice over (x,y)
rather than two independent scalar medians, which could otherwise invent a
vector no neighbour voted for.

With medians off the generator reproduces the previous shader body
byte-for-byte, so the change is provably behaviour-preserving when disabled.

### Results

Flow outliers on `blueydefect.mp4`:

| median passes S,E,Q,H | outlier pixels | vs base |
|---|---|---|
| none (previous shader) | 0.0412% | -- |
| **2,2,2,0** (shipped) | **0.0147%** | **-64%** |
| 2,2,0,0 | 0.0250% | -39% |
| 1,1,1,0 | 0.0194% | -53% |

Dropping the Q level costs more than halving the passes, so Q is where most of
the work happens -- consistent with the island being ~5.5 texels there, the
finest level at which a 3x3 kernel still wins the vote.

Visually the islands are simply gone: the flow field over the face is smooth
everywhere, and with it the eye smear, the melted nose and the torn mouth. The
frames the median changed most were identified independently -- peak per-frame
difference against the base render, so the search was not restricted to frames
already known to be broken -- and each inspected. Frames 24, 44 and 1 were all
badly damaged in the base (a torn eye with fragmented head markings, a nose
melting into the muzzle, a grey streak through an eye) and all clean after. No
frame was found where the median made the picture worse.

The mouth still cross-fades through its redraw, and it always will. There is
no correspondence to find between two different drawings. What changed is that
it now cross-fades *as a coherent shape in the right place* instead of being
dragged somewhere by a false vector and torn.

### Real footage: no regression

The 60s avengers clip already passed with no noticeable defect, so the only
question there was whether the median cost anything. It did not -- it is
better or equal on every segment and both metrics
(`realbench.sh` at 5 15 21 30 45, segment 21 covering the reported head
anomaly):

| | base | median |
|---|---|---|
| PSNR mean | 36.18 | **36.31** |
| SSIM mean | 0.9748 | **0.9750** |
| SSIM, seg 21 | 0.9811 | 0.9811 |

The passthrough check reads identically for both (60dB on retained frames), so
the alignment trap documented above is not in play and the comparison is fair.

On the synthetic ladder the change is close to neutral, mean -0.06 dB, but the
distribution is informative. Both median strengths are shown because the
comparison between them is what settles the choice:

| case | base | 1,1,1,0 | 2,2,2,0 |
|---|---|---|---|
| L0_static | 79.35 | 0.00 | 0.00 |
| L1_trans_8px | 42.19 | +0.11 | +0.16 |
| L2_trans_16px | 39.92 | -0.02 | -0.03 |
| L3_trans_23px | 40.43 | -0.20 | -0.35 |
| L4_trans_40px | 34.61 | **-0.73** | **-0.86** |
| L5_lowcontrast | 60.00 | -0.04 | -0.05 |
| L6_flat_large | 41.29 | -0.10 | -0.14 |
| L7_textured_large | 23.44 | -0.09 | -0.10 |
| L8_diagonal | 37.38 | +0.02 | +0.01 |
| L9_occlusion | 40.09 | +0.03 | +0.09 |
| M1_noise_large | 27.10 | **+0.27** | **+0.31** |
| M2_period40 | 38.27 | +0.06 | **+0.21** |
| M3_period16_trap | 22.62 | -0.06 | -0.10 |
| M4_belowgate | 60.54 | 0.00 | 0.00 |
| mean | -- | -0.05 | -0.06 |

It gains where false matches are the failure mode -- noise, periodic texture,
occlusion -- and loses on fast translation, in a clean trend with speed (8px
+0.16, 23px -0.35, 40px -0.86). A median erodes a genuine motion boundary by a
texel or two per pass, and the faster the object the more of its area is
boundary rather than interior. L4 is 40px/frame, already past the ~23px coarse
search reach documented above, so its flow was partly wrong before the median
touched it.

The two strengths are what decide the setting. Halving the passes does NOT
avoid the fast-motion cost -- L4 is -0.73 against -0.86, essentially the same
-- while giving up a third of the outlier reduction (53% against 64%). The L4
loss is inherent to medianing at all, not to how hard it is applied, so there
is no cheaper trade hiding here and 2,2,2,0 is taken.

A measurement note worth recording: an early read of this table was taken
while the run was still finishing, and picked up a partially-written log that
reported L9_occlusion 0.3 dB higher than it settled at. Wait for the run to
exit before reading the logs -- the file existing does not mean it is complete.

### Cost

Measured under lavapipe with a discarded warm-up run, so one-time shader
compilation is not charged to render time:

| | previous | shipped | |
|---|---|---|---|
| 720p, 6s | 143.76s | 156.16s | +8.6% |
| 1080p, 6s | 188.78s | 200.33s | +6.1% |

A first attempt at this measurement reported +13.8%, taken on the 21-frame
defect clip with no warm-up -- which charges the one-time compile of twelve
extra passes to a very short render. Warm up before timing, and time something
long enough that per-frame cost dominates.

On the reporting hardware this projects to roughly 104 -> 96 fps at 720p and
77 -> 73 fps at 1080p, both still inside the stated tolerance. Confirm on real
hardware; nothing here measures speed meaningfully.

### Not applied to the base shader

`bidirectional-interpolation.glsl` still medians only at H, so it retains this
defect. The coarse passes are emitted by the generator, and the generator
*reads* the base shader -- adding them there too would make generated builds
median twice per level. If the base variant is ever to get this, the placement
needs deciding in one place rather than both.

## Usage

Requires an `ffmpeg` built against a libplacebo carrying
`frame-mix-hook.patch` (see [README.md](../README.md)). Software Vulkan
(Mesa lavapipe) is entirely sufficient -- this measures correctness, not
speed, and needs no GPU.

```bash
export FFMPEG=~/build/ffmpeg/ffmpeg
./bench.sh all              # run the whole ladder
./analyze.py                # summarise
```

Testing a change without touching the shipped shader:

```bash
sed 's/REFINE_REG_LAMBDA = 0.05/REFINE_REG_LAMBDA = 0.20/' \
    ../bidirectional-interpolation.glsl > /tmp/variant.glsl
./bench.sh all /tmp/variant.glsl reg20
./analyze.py --variants     # columns side by side
```

Baselines are cached per case, so re-running only re-measures the shader.

## Scene cuts: choosing the gate threshold by measurement

Interpolating across a hard cut superimposes two unrelated shots. The gate
that prevents this needs a threshold, and picking one required measuring three
statistics across three clips (13081 frame pairs: a dark night scene, bright
fast action, and flat animation), with cuts located independently by ffmpeg's
own scene filter.

**Mean |A - B| over a sparse whole-frame sample -- chosen, at 0.125.**
Scored against 134 cuts across 12986 non-cut pairs:

| threshold | cuts caught | false | note |
|---|---|---|---|
| 0.120 | 100/134 (75%) | 21 | 9 of them on bright action |
| **0.125** | **96/134 (72%)** | **12 (0.09%)** | none on bright action |
| 0.150 | 88/134 (66%) | 9 | |

The bright-action clip binds it: its highest non-cut reading is 0.1224, so
anything below 0.125 starts snapping frames that should be interpolated, on
material that is otherwise clean.

**A correction worth recording.** The first calibration used only the ten
strongest cuts as ground truth and appeared to catch all of them. Scoring
against a fuller detector setting found 28 cuts in the same clip, and the gate
catches 16. The apparent perfection was a property of the ground truth, not of
the gate -- and it was only noticed because a visibly ghosted cut at 27.9s
turned up during inspection that appeared in no list. **Recall is 72%, not
100%.** Choose ground truth before measuring against it, and be suspicious of
a detector that agrees with you completely.

**Fraction of the frame changed beyond a per-pixel threshold -- rejected.**
Sounds more robust, since a cut changes everything while motion changes only
what moved. In practice grain in dark material trips the per-pixel threshold
across most of the frame, and it separated worse: 23 false positives against
the mean's 2 on the same clip.

**Post-warp residual over raw difference -- rejected.** The most principled
of the three: ask how much of the change motion actually explains, which
should be scale-free. It failed outright. The coarse flow at 1/16 resolution
explains too little for the ratio to separate anything -- non-cut pairs sat at
0.77 against cuts at 0.85, with complete overlap on every clip.

**What the numbers mean, and what they do not.** On the bright fast-action
clip, cuts score *no higher than ordinary motion* (0.118 at cuts against a
0.122 non-cut maximum). That is not the statistic failing. Those cuts are
between visually similar shots, and blending across them does no visible harm
-- that same clip, containing eleven cuts, was viewed as defect-free before
the gate existed. So the gate measures "too different to blend", not "is there
a cut", and that is the property worth gating on.

Verified as inert where it should be: rendering five ladder cases against an
otherwise identical build with the threshold raised beyond reach gives
**bit-identical output**, so the gate provably never fires on synthetic
content. On the real clip it changes 3 frames out of 36 around the cut.

## The ripple: motion far beyond the search reach -- UNSOLVED

Found on a 60-second Back to the Future clip, at 36.9s, by masking scene cuts
out of the prospector ranking and then cross-checking against a second,
temporal detector. It ranked in three independent measures while not being a
cut, which is what made it worth zooming into.

**What it looks like.** The DeLorean passes close to camera at speed. The
shader melts its headlight and bodywork into rippling, dripping waves. Stock
linear blending does *not* -- it produces a soft but coherent double image. So
on this content the motion compensator is worse than doing almost nothing.

**Why it happens.** The headlight crosses several hundred pixels between
source frames. The surface is motion-blurred and low in texture. Adjacent
blocks latch onto different wrong offsets, the flow field breaks into bands,
and the warp drags the picture along them. The banding is directly visible in
a flow visualiser render.

**Four ways of detecting it, all refuted.** Each failed for a reason worth
knowing, because each sounds correct until measured:

*Post-warp residual.* Score the flow hypothesis by how much the two frames
disagree under it, against how much they disagree assuming no motion. Use the
warp only where it wins. Implemented and inert: on blurred low-texture content
**any** displacement matches well, so the wrong flow explains the data
perfectly. The ambiguity is the cause of the defect, not a symptom of it, and
a residual test is blind to it by construction.

*Flow coherence.* Mean disagreement between a flow vector and its neighbours.
Measured 7.37 half-res texels at the ripple against 1.44 on clean content --
but the coherence map fires along **every genuine motion boundary**, which is
exactly where motion compensation earns its keep. Gating on it would disable
the shader where it is most valuable, which is the trap the occlusion fallback
fell into.

*Flow magnitude against the search reach.* We know the estimator's competence
limit, so distrust it when pinned there. Measured 0.92 of reach at the ripple
-- and **0.92 at a nearby moment that renders acceptably**. Saturation is
necessary but not sufficient. Note also that L4_trans_40px scores 33.75 dB
against linear's 27.96 at 40px of motion, well past the coarse reach, so
saturation plainly does not imply failure: the refinement levels extend the
effective reach beyond what the coarse search alone suggests.

*Saturation and incoherence together.* The most promising combination, and
still too close to call: coherence peaks at 7.37 for the broken moment and
5.27 for the acceptable one. A threshold in that gap would be fitted to one
clip and would not survive contact with other material.

**Where this leaves it.** The defect is diagnosed precisely and remains
unfixed. Gating is treating a symptom: the underlying problem is that motion
exceeds what the estimator can resolve, and at that speed the source is so
blurred there may be little left to match even with more reach. If a fix
exists it is more likely to be architectural -- more pyramid levels, or a
genuinely different estimator for extreme motion -- than another threshold on
the signals above. See [ROADMAP.md](../../ROADMAP.md).

## Checking the harness itself

```bash
export FFMPEG=/path/to/ffmpeg FFPROBE=/path/to/ffprobe
./smoke.sh
```

Runs every tool in this directory against generated material -- no source
video needed -- and reports pass/fail for each. Use it after building, after
changing a tool, and on any new platform.

It exists because "the same harness works on Linux and Windows" is easy to
claim and easy to get wrong: the first run under MSYS2 immediately found a
hardcoded `/mnt/c/...` path in `gen_variational.py` that meant the generator
only ever worked on one machine. It currently passes 12/12 on both.

## Finding defects in new material

Two detectors, deliberately different, because each is blind to what the other
finds. Both take `--exclude` to mask scene cuts, which is not optional in
practice: cuts are enormous, they dominate every ranking, and they inflate the
robust deviation so that the threshold rises and everything smaller
disappears. The ripple defect above was invisible until they were masked.

Two tools support the workflow of hardening the shader against new sources,
which is a different activity from benchmarking a change.

```bash
export FFMPEG=~/build/ffmpeg/ffmpeg FFPROBE=~/build/ffmpeg/ffprobe
./prospect.sh <source> [start-seconds] [duration-seconds]
```

Renders the material through a flow-visualiser build of the production shader
and ranks moments by how badly the flow field disagrees with itself, printing
timestamps and a ready-to-run `clip.sh` line for each. It finds data
perturbation, which correlates with visible defects without being the same
thing, so **false positives are expected and correct** -- a human still
decides whether a candidate is a real problem or noise. What it removes is
the need to watch everything.

Its threshold is relative to the scan (median plus k robust deviations),
because what counts as a lot of outlier pixels depends completely on the
material. It therefore finds the worst moments in what it is given, not
moments bad in absolute terms, and on a uniformly poor scan it says so and
declines to rank rather than inventing an order.

Software Vulkan runs roughly 30x slower than real time at 1080p, so scan
scenes rather than films, or leave it running. On a real GPU a 60-second 1080p
clip takes about seven minutes, dominated by the analysis rather than the
render.

**Scans are saved, and can be re-ranked for free.** Every run writes its
per-frame measurements alongside the work directory, because a scan costs
minutes of GPU time and would otherwise exist only as text in a terminal.

```bash
./prospect.py --load <saved.scan> --k 2.5 --gap 12 --top 40
```

That re-ranks an existing scan with different parameters without rendering
anything, which matters because the threshold, the clustering gap and the
ranking depth are all judgement calls worth revisiting once you have seen the
first answer. It also means two scans of the same material -- before and after
a shader change -- can be compared directly rather than remembered.

```bash
./clip.sh <source> <time-or-#frame> [pad-frames] [output.mkv]
```

Cuts a frame-exact lossless clip, addressed by **time**, because a position
read off the 60p interpolated output does not map to a source frame index --
only time does. It also sidesteps the two ffmpeg traps that make hand-cutting
unreliable: `-ss` with `-c copy` cannot be frame-accurate (a stream copy has
to start at a keyframe), and frame numbers reset after a seek, so `n` in a
`select` filter counts from the seek point rather than from the start of the
file. Every cut is verified for exact frame count and a non-black first
frame, and a contact sheet is written alongside.

Proven frame-exact by cutting the same frames two ways -- once with the fast
seek it uses, once by decoding from frame 0 with no seek at all -- and
requiring the results to be bit-identical.

## Deterministic tie-breaking: measuring what noise decides

```bash
export FFMPEG=/path/to/ffmpeg
./tieprobe.sh [shader] [case...]
```

The block match is an argmin over candidate offsets. Where the cost surface is
flat, two candidates differ by less than the arithmetic noise between one
evaluation and another, and which one wins stops being a property of the image.
The chosen motion vector flips on a rounding difference and the whole warp for
that source pair is built on it.

**This is invisible on Linux and Windows, and re-running the benchmark there
proves nothing** -- both are bit-reproducible, so nothing ever perturbs the
comparison. macOS exposed it only because its MoltenVK path is not
reproducible; see the nondeterminism section of
[BUILDANDUSAGE.md](../BUILDANDUSAGE.md).

`tieprobe.sh` supplies the perturbation deliberately, so the property can be
measured where a baseline exists. It renders two builds whose every argmin cost
is nudged by a relative epsilon -- `tieprobe.py` does the rewriting -- and
compares them. Two numbers, because they answer different questions: `differ`
counts frames that are not bit-identical, which is the determinism property
itself; `worst` is the lowest per-frame PSNR between the two renders, which is
whether it *matters*. A single flipped texel lands near 90 dB; a warp built on
the wrong vector lands near 40.

**Confirm the platform first.** Render the unprobed shader two or three times
and compare `framemd5`. If those already differ, this measures the platform
rather than the shader. Both build hosts here are clean: five identical runs,
probed and unprobed, bit-identical every time.

### What it found, and how TIE_MARGIN was chosen

Without a margin, at one float32 ULP (`EPS=1e-7`) -- the scale a differing
summation order actually produces:

| shader | frames noise-decided / 240 | below 60 dB | worst |
|---|---|---|---|
| base | 56 | 44 | 55.7 dB |
| `-variational` (production) | 138 | 52 | 41.4 dB |

The production shader is the *worse* of the two, which is not obvious until
measured: it adds twelve vector-median argmins at the coarse levels, and its
80 Horn-Schunck passes carry any difference forward. Its 41.4 dB worst case is
the same magnitude as the 39 dB seen on macOS.

The defence is a **margin, not a tie rule**. A rule for exact ties would have
been a no-op: a strict `<` against a fixed scan order already resolves those
deterministically, with the incumbent winning. What needs deciding is the
*near*-tie. Requiring a candidate to beat the incumbent by a relative
`TIE_MARGIN` moves the decision threshold off the plateau where the ambiguity
lives, so the outcome stops depending on the last bits.

Sweeping the margin against `EPS=1e-6`, ten times more perturbation than
float32 alone produces, on the base shader:

| TIE_MARGIN | frames differ | below 60 dB | worst ladder regression |
|---|---|---|---|
| 0 (no margin) | 56 | 43 | -- |
| 1e-5 | 8 | 4 | 0.01 dB |
| **1e-4** | **3** | **2** | **0.02 dB** |
| 1e-3 | 6 | 1 | 0.05 dB |
| 1e-2 | 0 | 0 | 0.12 dB |

**Bigger is not better**, which is the part worth knowing. A larger margin
buys headroom against coarser perturbation, but it does so by refusing genuine
improvements where the cost surface is legitimately shallow -- and those are
the cases that are hardest already. At 1e-2 the cost falls on `L3`/`L4` (the
velocity ceiling) and `M3` (the period-16 ambiguity trap), the three scenes
built specifically to be ambiguous. 1e-3 is dominated outright: worse than
1e-4 on determinism *and* on quality.

1e-4 was chosen. At the perturbation float32 actually produces it is complete:

| shader | before | after |
|---|---|---|
| base | 56 frames, 44 harmful | **0 frames** |
| `-variational` | 138 frames, 52 harmful | **3 frames, 0 harmful**, worst 82.5 dB |

The residual three frames are cosmetic -- 82.5 dB is a texel or two, against
the 41.4 dB whole-warp failures it replaced. Ladder cost is at most 0.02 dB on
any case, for either shader.

**How far this goes, stated honestly.** The margin absorbs perturbation of
roughly its own size divided by a thousand. It is measured to be complete at
1e-7 and near-complete at 1e-6; at 1e-5 it barely helps, because no fixed
margin can survive noise approaching the scale of real cost differences. So
this fixes divergence of *arithmetic* origin -- summation order, contraction,
a different compiler. Whether it fixes macOS depends on whether MoltenVK's
nondeterminism is that small, which is not yet known: **that measurement is
the outstanding stress test**, and it needs the machine.

## Limitations

**Synthetic scores are not a substitute for real footage.** These scenes
have hard edges, no sensor noise, no compression artefacts, no motion blur,
and perfectly rigid translation. A parameter tuned to maximise a score here
can easily be overfitted to that. Treat a result as a *lead to confirm on
real content*, not a conclusion.

**Nothing here measures performance.** These runs are software-rendered on
purpose. Frame rate still has to be measured on real hardware.
