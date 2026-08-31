# Shaders

Nine `.hook`-format GLSL shaders built on
[frame-mix-hook.patch](frame-mix-hook.patch)'s `PL_HOOK_FRAME_MIX` stage --
see [README.md](README.md) for what that patch adds and why.

They divide into three groups: **four interpolators** (one recommended, one
cheap baseline, two superseded), **three diagnostic builds** of the same
algorithm that render what the estimator is thinking instead of the picture,
and **two small examples** that exist to demonstrate the hook rather than to
interpolate anything.

For how any of this was arrived at, see [METHODOLOGY.md](METHODOLOGY.md); for
the measurements behind the claims, [tests/TESTING.md](tests/TESTING.md).

## Which one to use

**Use `bidirectional-interpolation-variational.glsl`.** It is the
recommended production shader. On real footage it passes a 60-second
real-hardware viewing with no noticeable or distracting defect. On animation
it is clearly the best of the family and still not perfect, in one specific
way described below.

Use `bidirectional-interpolation.glsl` only if you have measured that the
variational build does not fit your hardware budget. It is roughly a fifth
of the passes and visibly worse -- on real footage it produces the edge
fraying and non-rigid warping that the variational cascade exists to fix.

Do not use the two `diffuse-*` variants for new work. They are a superseded
branch, kept for the record (see below).

## The interpolator family

All four share the same skeleton and are derived from the same base file.
The lineage is strictly additive, and the two branches are alternatives to
each other rather than steps in one line:

```
bidirectional-interpolation.glsl            23 passes   the base
  |
  +-- -diffuse-coarse.glsl                  31   base + coarse flow diffusion
  |     |                                        (SUPERSEDED)
  |     +-- -diffuse-dual.glsl              39   + fine diffusion
  |                                              (SUPERSEDED)
  |
  +-- -variational.glsl                    115   base + variational cascade
                                                 + coarse vector medians
                                                 (RECOMMENDED, generated)
```

### `bidirectional-interpolation.glsl` -- the base, 23 passes

The hierarchical block-matching pyramid, and the file every other build in
the family derives from. Edit this and the variational build inherits the
change on regeneration; the diagnostic builds are kept in deliberate
lockstep with it by hand.

Written against exactly 2 frames and needed *no changes* for the patch's
N-frame generalisation -- `HOOKED` and `NEXT` still mean frame index 0 and
1, so this shader is simply the N=2 case of the now-more-general mechanism.

### `bidirectional-interpolation-variational.glsl` -- recommended, 115 passes

A strict superset of the base: every one of its 23 passes, plus 80
variational-refinement passes and 12 vector-median passes distributed across
the pyramid. Two things it adds, both of which turned out to matter more
than any parameter tuning ever did:

- **Warped Horn-Schunck refinement at every pyramid level** (16/12/8/4
  iterations at 1/16, 1/8, 1/4, 1/2 resolution). Coherence enters the
  *objective* here rather than being imposed afterwards -- each iteration
  jointly minimises brightness-constancy residual and deviation from the
  neighbourhood, so neighbouring texels constrain each other instead of each
  deciding alone. This is what fixed the edge fraying and the non-rigid
  warping.
- **Vector medians at the coarse levels** (2 passes per direction at 1/16,
  1/8 and 1/4, on top of the 2 the base already runs at 1/2). These reject
  isolated false-match islands -- the failure mode that wrecked cartoon
  faces, where a redrawn eye or mouth gets confidently matched to the wrong
  shape and returns a vector the whole surrounding face disagrees with.

**This file is generated.** It carries a `GENERATED FILE -- DO NOT EDIT BY
HAND` banner recording the exact command that produced it. Change the
variational stage by editing `tests/gen_variational.py` and regenerating;
hand edits will be lost, and ~100 near-identical iteration passes are not
maintainable by hand anyway:

```bash
./tests/gen_variational.py "16,12,8,4" 0.3 0.08 bidirectional-interpolation-variational.glsl 0 "2,2,2,0"
```

The arguments are: variational iterations per level (S,E,Q,H), the smoothness
weight `alpha`, the edge-aware luma sigma, the output path, an optional
robust-flow sigma (0 = off, measured as no help), and median passes per level.

### `-diffuse-coarse.glsl` and `-diffuse-dual.glsl` -- superseded

Base + flow diffusion at 1/16 resolution (coarse), and additionally at 1/2
(dual). These were the first fix for correspondence ambiguity -- the failure
where content repeating at roughly the distance it travels per frame makes
"moved one full period" and "did not move" genuinely indistinguishable, so
the regulariser breaks the tie toward zero and part of an object gets left
behind.

They worked, and the reasoning that produced them was sound and is worth
reading. They are superseded because the variational cascade solves the same
problem as a consequence of a more general mechanism, and does more besides.

They also did **not** get the `TIE_MARGIN` tie-breaking fix, deliberately:
they are kept as a record of what was tried, not as builds anyone should run,
and changing them would make them a worse record without making them useful.
So their argmins can still be decided by arithmetic noise. That is one more
reason not to use them, and it is not an oversight to fix.
**Their file headers still contain stale claims** -- `diffuse-dual` describes
itself as "the highest-quality variant measured", which was true when written
and is not now. They are also stale in the code, not just the comments: both
still carry the occlusion fallback that was removed from the base, which is
why they now measure worse than the base and, in one case, worse than stock
linear blending. See "Why the diffuse variants measure so badly" below.

### Known remaining weakness: motion beyond the search reach

When an object crosses several hundred pixels between source frames -- a car
passing close to camera, for instance -- the search cannot resolve it, the
flow field breaks into bands, and the warp drags the picture into rippling,
molten waves. On that content the shader is **worse than stock linear**, which
stays coherent because blur hides its doubled contour.

This is diagnosed and unfixed. Four detection criteria were implemented and
measured, and each fails for a specific reason -- residual is blind to it,
coherence fires at every motion boundary, magnitude fires on fast motion that
renders fine, and the combination is too close to separate. The evidence is in
tests/TESTING.md. A fix is more likely to be architectural than another
threshold.

### Known remaining weakness: animation

Flat-shaded animation is the hardest case for this design, and one class of
defect in it is not fully solved.

Small high-contrast facial features -- an eye, a mouth -- are frequently
**redrawn between source frames rather than moved**, for lip-sync and
expression. There is then no correspondence to find: the two drawings are
different shapes, and no motion field maps one to the other. The coarse
vector medians fix the visible *damage* this caused (the estimator used to
return a confident vector to the wrong shape, dragging and tearing the
feature), so the feature now travels with the face and the shape change
resolves as a clean cross-fade in the right place.

What remains is that cross-fade itself, which is inherent. A redrawn mouth
passes through a brief soft blend rather than snapping between two drawings
the way the original animation does. It is much improved and still visible
on close inspection.

Fixing this properly is judged to need a different class of shader rather
than a change to this one -- see [ROADMAP.md](../ROADMAP.md), "A shader class specific to
animation".

## Measured comparison

All four measured in one sitting, on the same harness, so these numbers are
comparable with each other -- unlike the figures in the shader file headers,
which were taken at different times against different versions of the base.

**Real footage** (`realbench.sh`, avengers clip, decimate-and-reconstruct at
5/15/21/30/45s). SSIM is the column to read: PSNR systematically rewards blur,
and will rank a smooth double-image above a sharp but slightly-misplaced
motion-compensated frame.

| | PSNR mean | SSIM mean |
|---|---|---|
| `linear` (stock libplacebo) | 31.90 | 0.9451 |
| base | 34.34 | 0.9655 |
| `-diffuse-coarse` | 30.71 | **0.9444** |
| `-diffuse-dual` | 30.98 | 0.9503 |
| **`-variational`** | **36.31** | **0.9750** |

**Synthetic ladder** (`bench.sh all`, PSNR dB of genuinely interpolated
frames):

| case | hold | linear | base | coarse | dual | variational |
|---|---|---|---|---|---|---|
| L0_static | inf | 79.43 | 79.35 | 79.35 | 79.35 | 79.35 |
| L1_trans_8px | 32.26 | 36.45 | 41.34 | 41.06 | 42.66 | 42.35 |
| L2_trans_16px | 30.17 | 32.04 | 38.45 | 35.97 | 37.95 | **39.89** |
| L3_trans_23px | 28.10 | 30.51 | 39.10 | 33.51 | 36.25 | **40.08** |
| L4_trans_40px | 25.32 | 27.96 | 31.28 | 27.42 | 27.42 | **33.75** |
| L5_lowcontrast | 56.15 | 57.37 | 60.66 | 60.51 | 60.61 | 59.95 |
| L6_flat_large | 31.38 | 33.38 | 40.27 | 39.44 | 40.99 | 41.15 |
| L7_textured_large | 21.30 | 21.47 | **24.36** | 22.22 | 22.26 | 23.34 |
| L8_diagonal | 28.13 | 30.02 | 36.75 | 32.43 | 33.71 | **37.39** |
| L9_occlusion | 29.45 | 32.07 | 38.31 | 36.08 | 37.38 | **40.18** |
| M1_noise_large | 19.66 | 20.65 | 26.51 | 26.27 | 26.34 | **27.41** |
| M2_period40 | 24.68 | 27.30 | 36.84 | 37.02 | 37.89 | **38.48** |
| M3_period16_trap | 21.23 | 21.42 | 22.15 | 23.19 | **23.20** | 22.52 |
| M4_belowgate | 62.66 | 60.54 | 60.53 | 60.53 | 60.53 | 60.54 |

The variational build wins nearly everywhere, and wins by the most on exactly
the cases that matter: fast translation, diagonal motion, occlusion, noise.

### Why the diffuse variants measure so badly

This deserves stating plainly, because their own headers claim the opposite.
`-diffuse-coarse` scores **below stock linear blending** on real-footage SSIM
(0.9444 against 0.9451), and both variants lose to the plain base shader
across most of the ladder.

They are **stale forks**. Both still contain the occlusion fallback that was
removed from the base after every version of it measured worse than none:

```glsl
float occluded = smoothstep(4.0, 7.0, fb_error_px);
vec4 fallback = mix_t < 0.5 ? HOOKED_tex(HOOKED_pos) : NEXT_tex(NEXT_pos);
return mix(mc_result, fallback, occluded);
```

That is the original, most aggressive gate, blending toward an *unwarped*
frame -- which at any moving edge means a translucent doubled contour, and
does more damage on angled content, which is why L8_diagonal and the fast
translation cases suffer most.

So their headers were not dishonest when written: at that time the base
carried the same fallback, and the comparison was fair. The base has since
moved on and they have not. The one thing they still genuinely win is
M3_period16_trap -- the correspondence-ambiguity case they were built for --
which is a fair record of the idea being sound even though the files are not.

Given they are superseded by a better mechanism and currently measure worse
than doing nothing, the reasonable options are to delete them or to
regenerate them from the current base. They are kept for now as a record of
the reasoning, which remains worth reading.

## How the interpolator works

Each output frame is synthesised from the two source frames the hook hands
it (`HOOKED` = earlier, `NEXT` = later) in five stages.

**1. Downsample.** Both frames' luma is reduced to four pyramid levels --
referred to throughout as S (1/16), E (1/8), Q (1/4) and H (1/2).

**2. Coarse search.** At S only, a full iterative block-matching search from
scratch: 5 halving steps, reaching about 23px at full resolution. Both
directions are searched independently (A->B and B->A, not one derived from
the other by sign-flipping), because occlusion makes them genuinely
different problems. A magnitude-regularisation term biases ambiguous and flat
regions toward small motion rather than spurious large jumps.

The reach cap is deliberate. It is the single most-confirmed finding in this
project: **one iteration propagates one texel, so a coarse level buys reach
at a fraction of the cost.** At 1/16 resolution one texel is 16px, so a given
iteration count reaches sixteen times further than the same work at full
resolution, for 1/256 of the price. Nearly every fix in this shader is an
application of that fact.

**3. Refine, level by level.** E, Q and H each take the level above as a
seed and search only a small neighbourhood around it. The fine levels supply
detail; they cannot supply reach, which is why step 2 exists.

Every one of these searches -- and every vector median below -- selects an
**argmin**, and each requires a candidate to beat the incumbent by a relative
`TIE_MARGIN` before displacing it. Without that, a near-tie on a flat cost
surface is decided by whichever candidate rounds lower, so a motion vector can
flip on arithmetic noise and take the whole warp with it. Preferring the
incumbent is also the right answer on the merits: it is the coarse level's
estimate at a refine level, and zero motion at the coarsest, which is the same
conservative direction the magnitude regularisation already argues for. The
value is measured rather than assumed, and larger is *not* safer -- see
tests/TESTING.md, and `tests/tieprobe.sh` for how to re-measure it.

**4. Regularise.** In the variational build, each level runs its Horn-Schunck
iterations and then a vector median, in that order, so the neighbourhood
consensus is what seeds the next level rather than being re-dirtied by it.
Per level the sequence is `refine -> variational -> median`.

**5. Scene-cut gate.** Before warping anything, one number decides whether
these two frames can be blended at all. Across a hard cut they are unrelated
images: no correspondence exists, and interpolating superimposes two shots as
a ghosted double exposure. The gate compares a sparse whole-frame sample of
the 1/16 luma and, above a threshold, reproduces the cut instead:

```glsl
if (SCENE_DIFF_tex(vec2(0.5)).r > SCENE_CUT_DIFF)
    return mix_t < 0.5 ? HOOKED_tex(HOOKED_pos) : NEXT_tex(NEXT_pos);
```

A hard switch is *correct* here, which is worth stating given the occlusion
fallback was removed for being one. At an occlusion boundary correspondence
exists for most of the frame, so substituting an unwarped frame threw away
good information. At a cut nothing corresponds, and the original edit was
itself a hard switch.

Stated honestly, this measures "too different to blend", not "is there a cut",
and it is a **partial fix**: measured recall is 72% of 134 cuts across three
clips. Cuts between visually similar shots are missed -- but those are also
the ones that do least visible harm when blended, which is why a 60-second
clip containing twelve of them was viewed as defect-free before this existed.
The gate fires on what looks wrong rather than on edit structure. Threshold,
evidence, and a correction to an earlier over-claim are in tests/TESTING.md.

**6. Warp and blend.** The flow is read at half resolution and lifted to full:

```glsl
vec2 flow_ab = FLOW_H_AB_tex(HOOKED_pos).xy * 2.0 * HOOKED_pt;
vec4 warped_a = warp_sample_a(HOOKED_pos - flow_ab * mix_t);
vec4 warped_b = warp_sample_b(NEXT_pos   + flow_ab * (1.0 - mix_t));
return mix(warped_a, warped_b, mix_t);
```

Note what is *not* here: **there is no occlusion fallback.** Three versions
of one were built and every single one measured worse than none -- a hard
`mix_t` switch produced an 8.75x periodic jump, a continuous blend of two
unwarped frames produced a translucent doubled contour at every moving edge,
and directional per-side weighting was better than both and still worse than
removing it. `tests/gen_variational.py` contains a guard that fails loudly if
a fallback is ever reintroduced upstream, so generated builds cannot silently
inherit a gate that was never measured for them.

Removal works rather than merely being less bad because the blend degrades
gracefully on its own: both samples use the same flow, so where that flow is
wrong they are wrong *together and in the same direction*, which stays
spatially coherent; and as `mix_t` approaches 0 or 1 the result converges on
the unwarped nearest frame anyway, continuously.

**Caching.** The expensive per-window work -- the flow search at all four
levels, and both directions' second vector-median pass -- is cached in
persistent `//!TEXTURE ... //!STORAGE` textures, keyed on the patch's
`pair_changed` flag. At a non-integer fps ratio like 24->60, consecutive
output frames share a source pair; without this the whole pyramid would be
recomputed for each of them. Note the fixed-size ceiling this implies, and
its consequence above 4K, documented in README.md's Costs and limitations.

## The diagnostic shaders

All three are the same algorithm as the base, kept in lockstep pass-for-pass,
differing only in what the final pass returns. That lockstep is the point: a
diagnostic that has drifted from the shader it is diagnosing is worse than no
diagnostic. When the occlusion fallback was removed, all three were updated
in the same commit.

### `interpolate-debug-grid.glsl`

Renders a 3x2 diagnostic grid instead of the final picture:

```
+-------------+-------------+-------------+
|  source A   |  source B   | flow colour |
|  (HOOKED)   |   (NEXT)    |    wheel    |
+-------------+-------------+-------------+
| flow magni- |  forward /  |   actual    |
| tude heat-  |  backward   |   warped    |
| map (A->B)  |  consistency|   result    |
+-------------+-------------+-------------+
```

The consistency panel still *visualises* forward/backward error even though
nothing acts on it any more -- it remains diagnostically useful for seeing
where the estimator disagrees with itself.

### `interpolate-debug-overlay.glsl`

The real warped result at full resolution with diagnostics drawn over it.
The grid's limitation is that shrinking a frame into one of six cells
destroys exactly the fine spatial detail a subtle localised defect needs in
order to be judged. This one keeps full resolution.

### `interpolate-debug-warp-stages.glsl`

Isolates the individual warp stages so a defect can be attributed to one of
them rather than to "the warp" as a whole.

### Ad-hoc visualisers: `tests/flowvis.py`

The three files above are permanent builds. For one-off questions there is a
better approach, and it is the one that actually cracked the cartoon defect:

```bash
./tests/flowvis.py bidirectional-interpolation-variational.glsl /tmp/vis.glsl
```

This rewrites **only the final `hook()`** of any interpolator, leaving all
114 passes upstream untouched, so what it renders is exactly what production
computes rather than a re-implementation that could drift. The default
replacement encodes the flow field as colour. Swapping in a different final
pass -- three lines -- gives the post-warp residual `|warped_a - warped_b|`,
which is the honest "did correspondence succeed" map, since after a *correct*
warp the two samples should agree.

Together those two views localised the cartoon face defect in a single pass:
the flow view showed saturated islands sitting exactly on the eye and mouth,
and the residual view showed filled blobs there rather than the thin outlines
every other edge produces.

## The two small examples

### `motion-edges-dual.glsl` -- 1 pass

Deliberately the opposite end of the complexity range from the flagship: a
single pass, no motion estimation at all. It outlines moving edges in each of
the two source frames and tints them differently, so the before-position and
after-position of everything in motion are visible simultaneously.

It exists because a hook stage whose only example is a 115-pass motion
compensator is hard to learn from. It is also the shader that confirmed the
hook fires correctly at N:N ratios (24->24, no frame insertion), which the
interpolators do not exercise because they lean on `mix_t`.

It is worth noting for future work that this shader produces a strikingly
accurate outline of a character's before and after position -- see
[ROADMAP.md](../ROADMAP.md), where using that directly to warp a whole character or feature
as a template, rather than consulting a mostly-static whole-frame flow
field, is parked under "A shader class specific to animation".

### `nframe-smoketest.glsl` -- 1 pass

Binds 4 frames at once and renders each into its own grid cell with a colour
tag per index, a frame-count readout, a per-frame timestamp bar, and a
red/green `pair_changed` indicator. It has nothing to do with interpolation.

Going from exactly-2-frames to a hook-declared N was a structural change to
`pl_hook_params`, not an additive one, so it needed a real build-and-run
cycle to trust rather than a clean `git apply`. This makes binding more than
two frames from a real GPU dispatch something you can look at. The *absence*
of the grid on the first few output frames of a clip is the visual
confirmation that the boundary behaviour works as designed.

## Performance

Two separate things get measured here and they should not be confused: real
hardware determines whether this is usable, and software rendering under
lavapipe determines only whether one change costs more than another.

### Real hardware

End-to-end through a full encode pipeline (`hevc_vaapi -global_quality 20`,
the command in README.md's Usage section), on a low-end discrete GPU:

| shader | source | rate |
|---|---|---|
| `-variational` | 720p animation | ~104 fps |
| `-variational` | 1080p live action | ~77 fps |
| base (older measurement) | 1080p | ~138 fps |

The variational figures predate the coarse vector-median passes, which were
measured under lavapipe at +8.6% (720p) and +6.1% (1080p) and confirmed on
real hardware as still within tolerance.

### What caching buys

Measured on the base shader with output discarded (`-f null -`) to remove
encoding from the measurement, 1080p:

| | Low-end discrete GPU | Weaker iGPU |
|---|---|---|
| No caching | 144 fps | 33 fps |
| + flow-search caching | 174 fps | 44 fps |
| + median-filter caching | 184 fps | 48 fps |

The gain is smaller than per-pass cost would predict, most likely because of
fixed per-dispatch overhead -- the shader issues its dispatches every output
frame regardless of cache state -- and possible `PL_MEMORY_COHERENT`
synchronisation cost on every storage access. Neither is something caching
can remove.

### Where to look if it is too slow

4K is untested and is the known risk, both for speed and for the storage
ceiling in README.md. If it struggles, the coarse levels are counter-
intuitively *not* the place to cut -- they are 1/256 and 1/64 of full
resolution and buy the reach the whole design depends on. Cut the H-level
work first: the half-resolution variational iterations and the H median are
the expensive part, and `gen_variational.py` takes both as parameters, so
`"16,12,8,0"` or a reduced median spec can be measured without editing a
shader.
