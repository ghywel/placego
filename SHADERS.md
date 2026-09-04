# Shaders

Nineteen `.hook`-format GLSL shaders built on
[frame-mix-hook.patch](frame-mix-hook.patch)'s `PL_HOOK_FRAME_MIX` stage --
see [README.md](README.md) for what that patch adds and why.

They divide into three groups: **sixteen interpolators** (one recommended for
viewing, one cheap baseline, three variants of that baseline -- seeded,
seeded plus propagation, and an animation-tuned setting of that -- each
with the three- and four-frame shaders generated from it, a five-frame
shader generated from the propagated variant for the field, and two
superseded),
**one human-reading demonstration** (every interpolator carries the
reading view inside it, off by default; this file is the four-frame
propagated shader with it switched on), and **two small examples**
that exist to demonstrate the hook rather than to interpolate anything.

All of them live in [shaders/](shaders/). The generators and the test scripts
resolve a bare shader name there, so every command quoted in this file works
unchanged from `scripts/` or `scripts/tests/`; a name with a directory in it
is used as given.

For the tools that measure all this, start at [tests/TOOLS.md](tests/TOOLS.md).
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

If the fast tier is what you need and a 13% render-time cost is inside
your budget, use `bidirectional-interpolation-propagated.glsl` (the seeded
base plus eight 1/8-level passes that let flat texels inherit their
textured neighbours' motion, checked against the two frames, and blend
where a flow's own neighbourhood contradicts it): above the seeded base on
every real segment measured (+0.5 to +4.1 dB, six segments) and on 21 of
32 ladder cases by +2.1 dB mean, with one case 1.4 dB down and one 1.0 dB
down (a 40 px/frame translation). For hand-drawn or
cel-shaded content use `bidirectional-interpolation-animation.glsl`, the same
shader with a finer disagreement threshold: on flat-shaded anime it matches
the variational build (42.50 against 42.48 dB) at a third of the passes,
and costs a little on plain rotation and fast textured translations, which
is the right trade there and the wrong one for live action. If a 10%
cost is the limit, use `bidirectional-interpolation-seeded.glsl` instead of the
base, and the `-seeded` tri and quad generated from it for the field. It
is the base with the two coarsest levels choosing among three candidate
motions -- from zero, from the neighbouring ring, and from the previous
window where a round trip vouches for it -- instead of following one
descent from zero (its file header says
how and why), and on the synthetic ladder it is up on 25 of 32 cases by
more than a tenth of a decibel and down on none by more than 0.07. On real
footage the gain is small but consistent: +0.45 dB PSNR and +0.0016 SSIM over the base on
the avengers clip, every segment at or above the base, and the same margin
for its quad over the stock quad, while the variational build stays 1.5 dB
and 0.008 SSIM ahead of both (table below). The ladder's large gains are on
synthetic content whose failures the coarse seed decides outright; real
footage is decided by coherence, which is the variational cascade's job.
On the ladder each beats the other on different cases (the variational on
A1-A3, L4, L9; this on L1, L2, L6, L8, M2). Its first customer is the field instrument, whose acceleration and
jerk readings inherit the coarse seeds: on the lattice-textured
calibration cases the stock coarse search returns the texture's own
symmetry vector instead of the motion on 40-75% of texels
(NFRAME-LIMITS.md section 8), and this variant returns those cases to
stock or better and lifts the acceleration field's coverage on A7's
mid-speed frames from 36% to 67%.

Do not use the two `diffuse-*` variants for new work. They are a superseded
branch, kept for the record (see below).

## The interpolator family

All four share the same skeleton and are derived from the same base file.
The lineage is strictly additive, and the two branches are alternatives to
each other rather than steps in one line:

```
bidirectional-interpolation.glsl            24 passes   the base (N = 2)
  |
  +-- -diffuse-coarse.glsl                  31   base + coarse flow diffusion
  |     |                                        (SUPERSEDED)
  |     +-- -diffuse-dual.glsl              39   + fine diffusion
  |                                              (SUPERSEDED)
  |
  +-- -variational.glsl                    115   base + variational cascade
  |                                              + coarse vector medians
  |                                              (RECOMMENDED for viewing,
  |                                              generated)
  |
  +-- -seeded.glsl                          23   base + ring and gated
  |     |                                        temporal seeds, arbitrated
  |     |                                        at 1/8 res (VARIANT: +10%
  |     |                                        time, up on 25 of 32 cases)
  |     +-- tri-/quaddirectional-…-seeded   48/68 generated from it with the
  |     |                                        generators' base argument
  |     +-- -propagated.glsl                32   seeded + flow propagation at
  |           |                                  1/8 res behind a two-frame
  |           |                                  check (VARIANT: +1-4% over
  |           |                                  seeded, +2.1 dB on the ladder)
  |           |     +-- tri-/quad…-propagated    64/92 generated from it
  |           |     +-- quintdirectional-…-propagated 127 N = 5: the symmetric
  |           |                                        quartic field (the
  |           |                                        picture is the quad's)
  |           +-- -animation.glsl           32   propagated with the finer
  |                 |                            disagreement threshold
  |                 |                            (VARIANT for line art)
  |                 +-- tri-/quad…-animation     64/92 generated from it
  |
  +-- tridirectional-interpolation.glsl     48   N = 3: + acceleration field
  |                                              + quadratic placement
  |                                              (EXPERIMENTAL, generated --
  |                                              see TRIDIRECTIONAL.md)
  |
  +-- quaddirectional-interpolation.glsl    68   N = 4: + jerk field
                                                 + cubic placement
                                                 + measured confidence
                                                 (EXPERIMENTAL, generated --
                                                 see QUADDIRECTIONAL.md)
```

The N = 3 and N = 4 builds are the *n-frame temporal analysis* line: their
product is the per-texel motion field (velocity, acceleration and -- at
N = 4 -- jerk), with interpolation as the corollary. Both regenerate from
the base via `tests/gen_tridirectional.py` / `tests/gen_quaddirectional.py`
and inherit every base fix on regeneration.

### `bidirectional-interpolation.glsl` -- the base, 23 passes

The hierarchical block-matching pyramid, and the file every other build in
the family derives from. Edit this and the variational build inherits the
change on regeneration; the human-reading view is generated into every
shader from that shader's own final pass, so it cannot drift from it.

Written against exactly 2 frames and needed *no changes* for the patch's
N-frame generalisation -- `HOOKED` and `NEXT` still mean frame index 0 and
1, so this shader is simply the N=2 case of the now-more-general mechanism.

### `bidirectional-interpolation-seeded.glsl` -- the base with three coarse seeds, 23 passes

Same passes as the base and byte-identical from the quarter-resolution
level down. Each 1/16-resolution search runs three descents -- from zero
(the stock path), from the best point of the +/-1-texel ring outside the
first result's basin, and from the previous window's flow at that texel --
and each 1/8-resolution pass refines all three and keeps the lowest SAD
plus a magnitude prior of 0.3 per texel toward zero plus a prior of 0.5
toward the previous flow. The temporal seed and its prior are used only
where the cached forward flow and the reverse flow at its landing point
close a round trip within one 1/8-level texel; an ungated version
re-seeded its own mistakes and lost 2.9 dB on the accelerating-texture
case A5 with a field that lagged the motion. The weights are measured
(NFRAME-LIMITS.md section 8: 0.06 loses on every lattice case, 3.0
reverts to stock). One storage texture per coarse pass is added for the
previous flow. Cost: +10% on this shader, +10% on the quad generated
from it (O5 at 24->60, median of three). The tri and quad variants are
generated from it with the generators' base argument:

    ./tests/gen_tridirectional.py  tridirectional-interpolation-seeded.glsl  bidirectional-interpolation-seeded.glsl
    ./tests/gen_quaddirectional.py quaddirectional-interpolation-seeded.glsl bidirectional-interpolation-seeded.glsl

What it was built for and did not do: the speed comb (fine aperiodic
texture at non-integer coarse speeds) was pre-registered to rise by 6 dB
and rose by 0.3-2.2, because no correct basin exists at the coarse level
there for any seed to find. What it did instead: every edge-driven and
integer-speed case up by 1-21 dB, the lattice-textured accelerating cases
up by 1.0-3.3, rotation up by 0.8-1.6, and the two-seed precursor's one
real loss (L7, -0.5) gone. It replaced that precursor (`-twoseed`, same
day) at the same cost; NFRAME-LIMITS.md section 8 has all three ladders
-- two seeds, three ungated, three gated -- and the diagnosis.

### `bidirectional-interpolation-propagated.glsl` -- the seeded base plus flow propagation, 32 passes

The seeded base byte for byte, plus eight passes at the 1/8 level. Why:
on flat-shaded line art the fast tier's loss against the variational build
is on the edges, not in the fills (NFRAME-LIMITS.md section 8) -- an edge
constrains one component of motion and the block matcher wanders along it.
Three Jacobi passes per direction let each texel take the contrast-weighted
mean of its 5x5 neighbours' flow (neighbours vote by their own local
contrast; a textured texel keeps its own), reaching 16 px per pass; then
one check pass per direction scores the propagated flow, the refine's own
and zero on the two frames' 1/8-level luma. A textured texel keeps the
propagated flow where it strictly wins; where instead the consensus
contradicts the refine's flow by more than 1.5 texels, or half the flow's
own length if that is larger, it takes zero -- a blend -- because a flow
its own neighbourhood disagrees with is an alias suspect, and an alias
scores the same SAD as the truth (this is what lifts the lattice-textured
cases by 4-12 dB; the relative term keeps a fast translation from being
mistaken for one); otherwise the three-way rule within 10%. A flat texel keeps the propagated flow only where it is
strictly best, else zero. Without the check a static flat background
beside a moving object inherits the object's flow and the clean
translations lose 8-22 dB; with it they hold. Cost: +1-4% over the seeded
base, about +13% over stock. Against the seeded base: +2.14 dB ladder
mean, 21 cases up, three down (L7 -1.4, L4 -1.0, L1 -0.2); real footage
up on all six segments measured (tables below), above the variational
build on one of them and within 1.5 dB of it on the flat-shaded anime. For the field instrument
the quad's A7 velocity field is 26.9% gross on the mid-speed frames
(the seeded quad 37.5%, stock 39-75%) with the acceleration field at 100%
coverage. The tri and quad are generated with the base argument (the
generators carry the extra passes into every pair's chain):

    ./tests/gen_tridirectional.py  tridirectional-interpolation-propagated.glsl  bidirectional-interpolation-propagated.glsl
    ./tests/gen_quaddirectional.py quaddirectional-interpolation-propagated.glsl bidirectional-interpolation-propagated.glsl

The knobs, for the record: without the check the propagation reaches
41.6 dB on the anime segment but drags static backgrounds; blending
wherever a flow cannot prove itself against zero beats the variational on
both anime segments but collapses every smooth case; a fixed disagreement
threshold of 0.75 texels reaches 43.1 dB on the anime (above the
variational) at the cost of 2 dB on the plain translations and 0.6 on live
action; a fixed 1.5 gives 0.1-0.4 dB more on four lattice cases and 0.8
less on L4, 0.2-0.3 less on live action; the check without the
disagreement rule at all is 1.5 dB worse on the ladder mean and 2 on the
anime. NFRAME-LIMITS.md section 8 has all of it.

### `bidirectional-interpolation-animation.glsl` -- the propagated shader tuned for line art, 32 passes

The propagated shader with one constant changed: the disagreement
threshold at which a textured texel blends instead of trusting the refine's
flow is 0.75 texels of the 1/8 level rather than 1.5 (the flow-scaled term
stays, so a pan is not mistaken for an alias). Hand-drawn and cel-shaded
content has flat fills, its information in the line art, and no natural
depth; on it the tracker's wrong flows are small and scattered, and the
finer threshold catches them. Measured on the flat-shaded anime segment:
42.50 dB against the propagated shader's 40.98, the seeded base's 36.89 and
the variational build's 42.48. Live action is a wash (within 0.1 dB on all
four segments); the ladder mean against the seeded base is the same +2.14,
with R3 +1.0 and A5 +0.2 more and R1 -0.6, L7 -0.4, L4 -0.3 less -- the
trade that makes it the wrong general file and the right animation one.
Same cost. A finer threshold still (0.5) changes nothing measurable; the
fixed 0.75 without the flow-scaled term reaches 43.1 dB on the anime but
loses 2 dB on plain translations and 0.8 on live action. The tri and quad
are generated with the base argument:

    ./tests/gen_tridirectional.py  tridirectional-interpolation-animation.glsl  bidirectional-interpolation-animation.glsl
    ./tests/gen_quaddirectional.py quaddirectional-interpolation-animation.glsl bidirectional-interpolation-animation.glsl

### `quintdirectional-interpolation-propagated.glsl` -- five frames, for the field, 127 passes

Generated from the propagated two-frame base by `tests/gen_quintdirectional.py`
(any base works: `./tests/gen_quintdirectional.py <out> <base>`). Everything
the quad has plus the slot 3 <-> 4 flow chains and, at the exact N:N phase,
the exact quartic through the anchor's four displacements over a symmetric
window (taus -2, -1, +1, +2; the far two composed from adjacent links, each
round-trip checked), read for acceleration and jerk with the snap row
ignored, degrading to the quad's cubic and the tri's quadratic as links fall
away. The picture is the quad's cubic on the four slots around the output,
so the interpolation ladder is the quad's (within 0.06 dB); the fifth frame
buys the field: on fast, small oscillations the four-frame acceleration is
the discrete second difference and reads 0.14-0.28 px/interval^2 below the
truth at eight and six samples per period, the quartic 0.04-0.05 (2.7x and
6.7x); on the jerk null the noise floor is 2.9x lower. Costs: one more frame
of latency at N:N, +18% render time over the quad, and the fifth slot only
fits under libplacebo's 16-bind ceiling by packing (the cut statistics, the
half-res and the full-res flows into RGBA textures). Diagnostic modes 8 and
9 report the quad's cubic from the same anchor, so the two estimators can be
chosen per regime. Needs the host to deliver five-frame windows: the N:N
patch's queue lookahead, and the hook patch's loud skip. Design,
pre-registration and results: [QUINTDIRECTIONAL.md](QUINTDIRECTIONAL.md).

### `bidirectional-interpolation-variational.glsl` -- recommended, 115 passes

Regenerated on 2026-09-04 when the human-reading tail was added: the
committed file had predated the sub-pixel refinement block the base gained
on 2026-08-31 (inert in the interpolators at `SUBPEL_REFINE = 0`; since
2026-09-04 the same is true of `SUBPEL_SELFREF`, the self-referenced fit that
removes the refinement's own texture-phase bias -- off in every two-frame
shader, on in every generated one, NFRAME-LIMITS.md section 9), and the
fresh generation scores the same L1 figure, 54.24 dB, so `tests/smoke.sh`
step 3 is green again.

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
itself as "the highest-quality variant measured", which was written before the
variational build existed. They are also stale in the code, not just the
comments: both still carry the occlusion fallback that was removed from the
base, which is why they lose on angled and fast motion, and `-diffuse-coarse`
measures below stock linear blending on real-footage SSIM.

That said, `-diffuse-dual`'s header is closer to right than it looked until
recently: on the reset ladder it is the **best of the whole family on clean
rigid translation**, by a wide margin. See "Why the diffuse variants measure
badly -- and where that turned out to be wrong" below.

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

(Since 2026-09-04 the fast tier has an animation-tuned file of its own,
`bidirectional-interpolation-animation.glsl`, which matches this build's
score on the flat-shaded anime segment at a third of the passes; the
redrawn-feature cross-fade above is a correspondence-free case and is the
same in both.)

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
| `-seeded` (2026-09-03; same run: base 34.29 / 0.9647, `-variational` 36.27 / 0.9741) | 34.74 | 0.9663 |
| `-propagated` (2026-09-04, same segments) | 35.28 | 0.9696 |
| `-animation` (2026-09-04, same segments) | 35.25 | 0.9694 |
| quad stock / quad `-seeded` (same run) | 34.22 / 34.67 | 0.9635 / 0.9651 |
| quad `-propagated` (2026-09-04, same segments) | 35.30 | 0.9685 |

**Five more real segments** (2026-09-03, RX 6600; 4-second segments sampled
from the owner's library, screened for full per-frame motion with
`screen.sh`, one 72-frame decimate-and-reconstruct window each; PSNR dB /
SSIM of the synthesised frames):

| segment | linear | base | `-seeded` | `-propagated` | `-animation` | `-variational` | quad | quad `-seeded` | quad `-propagated` |
|---|---|---|---|---|---|---|---|---|---|
| anime, 1080p24, moving shot | 43.03 / 0.9825 | 46.50 / 0.9887 | 46.67 / 0.9889 | **47.21 / 0.9897** | 47.22 / 0.9897 | 46.83 / 0.9897 | 45.76 / 0.9870 | 45.94 / 0.9871 | 46.47 / 0.9879 |
| anime, 1080p24, flat-shaded characters | 35.92 / 0.9739 | 36.38 / 0.9729 | 36.89 / 0.9742 | 40.98 / 0.9807 | **42.50 / 0.9817** | 42.48 / 0.9817 | 36.12 / 0.9713 | 36.62 / 0.9727 | 40.58 / 0.9791 |
| live action film, 1080p24 | 42.82 / 0.9937 | 45.25 / 0.9951 | 45.66 / 0.9953 | 46.58 / 0.9957 | 46.62 / 0.9957 | **47.07 / 0.9960** | 45.00 / 0.9946 | 45.43 / 0.9948 | 46.42 / 0.9952 |
| live action film, 1080p24, fast | 28.16 / 0.8617 | 31.91 / 0.9417 | 32.58 / 0.9461 | 33.39 / 0.9533 | 33.31 / 0.9525 | **34.99 / 0.9639** | 31.74 / 0.9386 | 32.42 / 0.9430 | 33.30 / 0.9502 |
| live action show, 1080p30 | 29.01 / 0.9260 | 31.55 / 0.9552 | 32.12 / 0.9580 | 33.30 / 0.9646 | 33.33 / 0.9645 | **34.61 / 0.9714** | 31.47 / 0.9545 | 32.05 / 0.9573 | 33.22 / 0.9638 |

The flat-shaded anime segment contains one cut inside its window; excluding
that frame lifts every arm on it by about 0.7 dB and changes no ordering.

The propagated quad matches the propagated two-frame shader on every
segment (it used to trail the two-frame base by 0.2-0.3 dB), so the field
instrument no longer pays for its window on real footage.

The ordering the one clip above gave holds on all five: `-seeded` above the
base on every segment (+0.17 to +0.67 dB, SSIM up on each), the seeded quad
above the stock quad by the same margins, and the variational build ahead of
everything by 0.3 to 6.1 dB. The 6.1 is the flat-shaded anime, where block
matching has least to hold on to: there, `linear`'s SSIM even edges the
base's, and coherence is worth six decibels.

**Synthetic ladder** (`bench.sh all`, PSNR dB of genuinely interpolated
frames). Re-measured 2026-08-31 after the ladder reset -- these numbers are
**not comparable** with any published before that date, because the ladder's
ground truth was pixel-quantised until then and suppressed absolute scores
substantially. See `tests/TESTING.md`, "The ladder reset". Windows figures;
the WSL/lavapipe run agrees to within 0.05 dB everywhere.

| case | hold | linear | base | coarse | dual | variational | seeded | propagated | animation |
|---|---|---|---|---|---|---|---|---|---|
| L0_static | inf | 79.43 | 79.43 | 79.43 | 79.43 | 79.43 | 79.43 | 79.43 | 79.43 |
| L1_trans_8px | 32.78 | 35.44 | 61.26 | 61.10 | **76.84** | 54.24 | 75.02 | 74.80 | 74.80 |
| L2_trans_16px | 29.59 | 32.16 | 41.78 | 39.04 | 48.68 | **50.15** | 62.32 | 62.30 | 62.30 |
| L3_trans_23px | 27.98 | 30.53 | 40.49 | 32.62 | 38.02 | **41.60** | 42.62 | 44.40 | 44.39 |
| L4_trans_40px | 25.48 | 27.96 | 31.57 | 27.39 | 27.39 | **33.96** | 31.50 | 30.49 | 30.21 |
| L5_lowcontrast | 55.57 | 57.47 | **62.27** | 62.27 | 62.27 | 60.54 | 62.27 | 62.27 | 62.27 |
| L6_flat_large | 30.81 | 33.50 | 55.52 | 45.71 | **56.03** | 52.21 | 65.44 | 65.45 | 65.45 |
| L7_textured_large | 20.82 | 21.04 | **25.30** | 22.11 | 22.16 | 23.41 | 25.29 | 23.90 | 23.46 |
| L8_diagonal | 27.83 | 30.25 | 40.09 | 33.50 | 35.65 | **45.77** | 46.13 | 47.53 | 47.51 |
| L9_occlusion | 29.71 | 32.21 | 39.83 | 36.55 | 40.84 | **44.39** | 41.58 | 42.13 | 42.13 |
| M1_noise_large | 24.19 | 25.51 | 46.93 | 43.61 | 46.90 | **48.04** | 49.84 | 49.91 | 49.91 |
| M2_period40 | 23.58 | 27.29 | 53.64 | 53.64 | **60.04** | 54.40 | 59.77 | 59.98 | 59.98 |
| M3_period16_trap | 20.72 | 21.01 | 21.90 | 23.48 | **23.49** | 22.06 | 21.91 | 21.91 | 21.91 |
| M4_belowgate | 62.06 | 60.58 | 60.58 | 60.58 | 60.58 | 60.59 | 60.58 | 60.58 | 60.58 |
| A1_accel_8mean | 33.64 | 36.23 | 46.81 | 44.51 | 49.46 | **51.24** | 47.93 | 48.19 | 48.19 |
| A2_accel_16mean | 30.25 | 32.68 | 42.54 | 37.85 | 41.11 | **45.16** | 44.88 | 45.24 | 45.17 |
| A3_accel_23mean | 28.59 | 31.00 | 38.03 | 34.12 | 37.17 | **41.69** | 39.91 | 39.95 | 39.86 |
| F1_fourier_edge | 27.33 | 30.31 | 46.91 | 42.78 | 46.12 | **47.26** | 51.74 | 54.02 | 54.02 |
| F2_fourier_accel | 28.07 | 31.01 | 39.12 | 32.55 | 33.41 | **43.76** | 40.58 | 43.31 | 43.47 |
| R1_rot_const | 29.53 | 32.42 | 37.30 | 33.40 | 34.23 | **41.02** | 38.26 | 40.70 | 40.14 |
| R2_rot_accel | 30.35 | 33.20 | 37.58 | 34.13 | 34.72 | **41.16** | 38.42 | 40.87 | 40.87 |

The `seeded`, `propagated` and `animation` columns were measured 2026-09-03/04
on the RX 6600 against the same ladder; its stock-base column that day agrees with the `base` column above
to within 0.04 dB on every case, so the columns are comparable. Its file
header and NFRAME-LIMITS.md section 8 carry the full account.

Every build beats stock `linear` on every case, which is the bar this harness
exists to enforce. Beyond that, **the reset removed the simple ordering these
numbers used to show.** The variational build no longer wins nearly
everywhere; it wins where the *block-match model is wrong* -- rotation,
acceleration, diagonal motion, occlusion, motion past the search ceiling --
and loses on clean rigid translation, where flow diffusion or no smoothing at
all does better. `L1` is the extreme case: `-diffuse-dual` reaches 76.84 dB
against the variational build's 54.24, within 2.6 dB of the round-trip
ceiling.

Read that as a statement about *robustness across motion types*, which is what
a production shader needs, rather than as accuracy on any one of them. And
read it as a lead: `tests/TESTING.md` records two anomalies in this table that
have no measured explanation, including a 19.5 dB collapse between `L1` and
`L2` for the base shader that is not monotonic with speed.

### Why the diffuse variants measure badly -- and where that turned out to be wrong

`-diffuse-coarse` scores **below stock linear blending** on real-footage SSIM
(0.9444 against 0.9451). That measurement is on real footage, is unaffected by
anything below, and stands.

**The synthetic-ladder half of this section was wrong, and the 2026-08-31
ladder reset is what showed it.** It used to say both variants "lose to the
plain base shader across most of the ladder" and that "the one thing they
still genuinely win is M3_period16_trap". On the reset ladder that is false
for `-diffuse-dual`, which wins on clean rigid translation and wins big:
**76.84 dB on `L1` against the base's 61.26 and the variational build's
54.24**, within 2.6 dB of the round-trip ceiling. It also takes `M2_period40`
(60.04), `L6_flat_large` (56.03) and `L9_occlusion` (40.84).

The old verdict was an artifact of the measurement. The ladder's ground truth
was pixel-quantised to 2px, which capped exactly the sub-pixel accuracy
diffusion buys on uniform flow, so the one thing these forks are good at was
the one thing the ladder could not see.

What the reset **confirms** is the diagnosis below. `-diffuse-dual` still
loses, and loses hardest precisely where the occlusion fallback does its
damage: `L8_diagonal` -4.4, `L4_trans_40px` -4.2, rotation -3.1,
`F2_fourier_accel` -5.7 against the variational build. The mechanism was
identified correctly; only the sweeping conclusion drawn from it was wrong.

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
moved on and they have not. They still win `M3_period16_trap`, the
correspondence-ambiguity case they were built for, which was always a fair
record of the idea being sound even though the files are not -- and since the
reset, they win a good deal more than that.

**So the recommendation has changed.** Deleting them is no longer one of the
reasonable options. Regenerating `-diffuse-dual` from the current base --
keeping the diffusion, dropping the occlusion fallback the base already
removed -- is now a well-motivated experiment with a specific prediction
attached: it should keep the clean-translation wins that the fallback is not
responsible for, and give up the angled- and fast-motion losses that it is.
Whether diffusion and the variational cascade compose, or whether they are two
answers to the same question, is unmeasured and is the more interesting
version of the question.

Until someone runs that, they remain **not for production use** -- stale
forks, carrying a fallback measured worse than none, and without the
`TIE_MARGIN` fix. What has changed is the reason to keep them: not merely as a
record of reasoning, but because the mechanism in them measurably does
something the current production shader does not.

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

## The human-reading view

A motion field is meaningless to human eyes until it is transformed: raw
per-texel vectors read as noise even where the estimator is right. The
Metal demo's "Reading" display solved that (pool, remember, gate, then
paint hue for direction and colour for magnitude), and every interpolator
in `shaders/` now carries that display inside it, as a tail of passes
behind its own final pass, switched by one shader parameter:

    read_view   0   normal output (the default; no reading pass runs)
                1   velocity        painted for a human
                2   acceleration    painted for a human      (three- and four-frame shaders)
                3   jerk            painted for a human      (three- and four-frame shaders)
                4   velocity        the raw field, for a machine
                5   acceleration    the raw field, for a machine
                6   jerk            the raw field, for a machine

The two-frame family has one flow, so its modes all read velocity. In mpv
the parameter is `--glsl-shader-opts=read_view=1`; ffmpeg's libplacebo
filter exposes no shader parameters, so edit the default -- the bare
number that ends the `//!PARAM read_view` block at the tail of the file --
or regenerate with `./tests/add_human_reading.py <shader> --default 1`.
`human-reading-quad.glsl` is that: the four-frame propagated shader with
the default at 1, kept as the one named demonstration so anyone can plug
it in and see what the estimator is thinking.

Every tail pass carries `//!WHEN read_view 0 >`, so at the default nothing
runs and the output is byte-for-byte the shader's own (verified on the
ladder: identical frames). Switched on, the tail costs about one extra
final pass: the shader's own final pass cloned at 1/8 resolution in its
diagnostic mode (so the field is exactly what that shader computes, not a
re-implementation), a 13x13 pool at 8 px spacing with an exponential memory
across frames in a storage texture, and a present pass that paints hue =
direction, visibility and saturation = magnitude above the field's gate,
over the picture at 35% luma. The tail is generated, never edited:
`tests/add_human_reading.py` appends it (idempotently) and the generators
call it last, so regenerating any shader is always safe.

Constants at the top of the tail's passes, for those who want to tune:

- `READ_EMA_ALPHA` (0.12): the memory across output frames, the demo's
  value for a live 60 Hz display. 1.0 gives a frame-by-frame reading: with
  memory on, an oscillating textured square averages to nothing; with it
  off the square reads cleanly and the red columns inside it are the coarse
  search's lattice aliases, visible to a human for the first time.
- `READ_VEL_*` / `READ_ACC_*`: the gates per field (velocity 1/2/3 px,
  acceleration and jerk 0.12/0.22/0.30 px, the demo's measured values at
  1280 wide; at 1920 the acceleration gates admit speckle in foliage, and
  doubling them clears most of it).
- `READ_GATE` (1): visibility needs the unpooled field to move within
  `READ_GATE_R` texels of 1/8 resolution (2 = 16 px, the tracker's own
  reach), so the pool cannot paint further than the tracker itself moved.
  Measured on a 100 px moving square: painted area 4.05x the object without
  it, 2.86x with it (halo median 32 -> 22 px), 94% of the square still
  covered. The 22 px that remain are the block matcher's own spread.
- `READ_MACHINE_FS_*`: full scales for the machine modes, which emit the
  unpooled field as 0.5 + px / (2 * FS) in the red and green channels, the
  same encoding the diagnostic modes use and the measurement scripts decode.

What the view showed on first use: on live action the moving subject reads
as one solid colour against the pan; on an anime shot with flat-shaded line
art the field is scattered blobs of contradictory direction, which is the
flat-content weakness (NFRAME-LIMITS.md) made visible.

The three hand-kept diagnostic builds (`interpolate-debug-grid.glsl`,
`-overlay`, `-warp-stages`) were removed on 2026-09-03 and three companion
human-reading files replaced them for a day; packing the view into each
shader replaced those on 2026-09-04, because a companion file reads one
variant and a toggle reads the shader it is in. Comments in the shaders and
the history in tests/TESTING.md still cite the old builds where they
describe how earlier defects were found; that history is accurate and was
left as written.

### Ad-hoc visualisers: `tests/flowvis.py`

The three views above are generated builds. For one-off questions there is
another approach, and it is the one that actually cracked the cartoon defect:

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
| `-seeded` base / quad (2026-09-03, RX 6600, `-f null`) | 720p synthetic O5, 24->60 | stock 2.69 / 4.11 s per 60 frames -> 2.97 / 4.53 s (+10% / +10%) |
| `-propagated` base (2026-09-04, same method) | 720p synthetic O5, 24->60 | seeded 3.12-3.26 s -> 3.15-3.39 s (+1-4%; about +13% over stock) |
| `-animation` base | same | the same passes as `-propagated`; one constant differs |

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
