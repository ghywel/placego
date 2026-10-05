# Prior art: where this work sits in the record

> **What this is (2026-10-01).** The public record of the external science surveyed before each leap, newest last.
> Each survey's text is kept as it was filed; dated notes mark what later work did with it, and the
> index below says where each survey led. Five surveys: the four-frame leap and the instrument framing (2026-08-31,
> the opening sections), the periodic interior (2026-09-27), the energy-transfer investigations (2026-09-30), lead 4,
> fast motion of a fine periodic print (2026-09-30), and lead 2, the impact mode as a shader (2026-10-01). Two leaps
> keep their prior art elsewhere: [THREEDIMENSIONAL.md section 3](THREEDIMENSIONAL.md#3-prior-art-stated-narrowly) (motion in depth) and
> [shaders/animation/ANI-PRIOR-ART.md](shaders/animation/ANI-PRIOR-ART.md) (the animation shaders). Authors were added
> to the source lists on 2026-10-01, each checked against the paper, its DOI record, arXiv or the publisher, in one form:
> "Surname, I." for up to three authors, "Surname et al." beyond three; patents name the inventors as first cited, with
> those of US 11,430,138 added.
>
> *Originally:* (A second survey, before the periodic-interior leap of 2026-09-27, follows the first; a third, before the
> energy-transfer investigations of 2026-09-30 (ENERGY-TRANSFER.md), is the last section.)

**Contents**

- [The first survey: before the four-frame leap (2026-08-31)](#prior-art-where-this-work-sits-in-the-record)
  - [The closest discipline is not video processing](#the-closest-discipline-is-not-video-processing)
  - [Directly usable results, in priority order](#directly-usable-results-in-priority-order)
  - [What not to import](#what-not-to-import)
  - [Sources](#sources)
- [Before the periodic-interior leap (2026-09-27)](#before-the-periodic-interior-leap-v3-in-other-peoples-words-surveyed-2026-09-27-night)
  - [The problem has names](#the-problem-has-names); [What four fields agree on](#what-four-fields-agree-on); [Two warnings, and one door already closed](#two-warnings-and-one-door-already-closed)
  - [What to import, in order](#what-to-import-in-order-steps-before-the-leap); [What not to import](#what-not-to-import-1); [Sources](#sources-the-periodic-interior-sweep)
- [Before the energy-transfer investigations (2026-09-30)](#before-the-energy-transfer-investigations-surveyed-2026-09-30)
  - [What the survey changed, in order of weight](#what-the-survey-changed-in-order-of-weight); [Two finds that bear on the record beyond this document](#two-finds-that-bear-on-the-record-beyond-this-document)
  - [Rigid and affine motion as one: the production precedent](#rigid-and-affine-motion-as-one-the-production-precedent-added-2026-09-30-late-evening-with-25s-result)
  - [Sources](#sources-the-energy-transfer-sweep) (filed after the lead-4 survey)
- [Before lead 4: fast motion of a fine periodic print (2026-09-30)](#before-lead-4-fast-motion-of-a-fine-periodic-print-surveyed-2026-09-30-2335-by-a-research-subagent-read-and-checked-before-it-was-filed)
  - [1. Summary](#1-summary); [2. Findings by direction](#2-findings-by-direction); [3. What to try first, ranked](#3-what-to-try-first-ranked); [4. Not to import](#4-not-to-import)
  - [Sources](#sources-the-lead-4-sweep-collected-2026-10-01) (collected on 2026-10-01; the survey cites inline)
- [Before lead 2: the impact mode as a shader (2026-10-01)](#before-lead-2-the-impact-mode-as-a-shader-one-source-per-pixel-chosen-by-the-side-of-tau-surveyed-2026-10-01-0405-by-a-research-subagent-read-and-checked-before-it-was-filed)
  - [Summary](#summary); [1. Hardware MEMC and patents](#1-hardware-memc-and-patents); [2. Non-linear-motion interpolation](#2-non-linear-motion-interpolation); [3. One-sided synthesis per pixel](#3-one-sided-synthesis-per-pixel)
  - [4. Detecting the event in a dense field](#4-detecting-the-event-in-a-dense-field); [5. Perception](#5-perception); [What to try first, ranked](#what-to-try-first-ranked); [Not to import](#not-to-import); [Sources](#sources-1)

**Index: what each leap leaned on, and where it led**

| Leap (date) | Survey | What was taken | Where it led |
|---|---|---|---|
| Four frames, and the field as a calibrated instrument (2026-08-31) | [the first survey](#prior-art-where-this-work-sits-in-the-record) | the equiangular sub-pixel fit (peak locking); the EQVI / All-at-Once fork; the stencil algebra; Savitzky-Golay fits; PIV as the closest discipline | [QUADDIRECTIONAL.md](QUADDIRECTIONAL.md) (P1-P4; [the equiangular fit](QUADDIRECTIONAL.md#post-battery-upgrade-the-equiangular-fit-sharpens-both-fields)); [TRIDIRECTIONAL.md, "Field accuracy, current state"](TRIDIRECTIONAL.md#field-accuracy-current-state-after-sub-pixel--the-equiangular-fit); [NFRAME-LIMITS.md section 1](NFRAME-LIMITS.md#1-the-stopping-point-is-a-signal-to-noise-crossing-not-a-fixed-n) |
| Motion in depth (2026-09-03) | [THREEDIMENSIONAL.md section 3](THREEDIMENSIONAL.md#3-prior-art-stated-narrowly) | Lee's time to contact; Koenderink and van Doorn's divergence, curl and deformation; four-pulse PIV's material derivative | [THREEDIMENSIONAL.md section 9](THREEDIMENSIONAL.md#9-measurements) |
| The animation shaders (from 2026-09-05) | [shaders/animation/ANI-PRIOR-ART.md](shaders/animation/ANI-PRIOR-ART.md) | the Anime4K line shaders; SVP and the cadence | NFRAME-LIMITS.md, ["Content drawn on twos"](NFRAME-LIMITS.md#content-drawn-on-twos-the-family-collapses-to-a-hold-and-the-cadence-is-the-prize-2026-09-19) and ["The cadence branch"](NFRAME-LIMITS.md#the-cadence-branch-the-prize-taken-inside-the-window-and-the-two-things-it-cannot-know-2026-09-19-afternoon) |
| The periodic interior, V3 (2026-09-27) | [this file](#before-the-periodic-interior-leap-v3-in-other-peoples-words-surveyed-2026-09-27-night) | the ambiguity flag; weighting by distinctness; the SGM-form carry; the unwrapping form; gating by ownership; the Imry-Ma warning | NFRAME-LIMITS.md: the flag offline in ["The field on real bodies"](NFRAME-LIMITS.md#the-field-on-real-bodies-two-hours-of-children-scored-against-a-skeleton-it-shares-nothing-with-2026-09-27); `ALIAS_PRIOR` and `ALIAS_CARRY` in ["The half-period alias in the shader"](NFRAME-LIMITS.md#the-half-period-alias-in-the-shader-the-prior-gate-and-the-carry-2026-09-28); the aperture rule in ["The aperture in the carry"](NFRAME-LIMITS.md#the-aperture-in-the-carry-b1-moving-up-and-the-energy-channel-on-rendered-children-2026-09-28-later), in the Cadence player from 1.0.3. The unwrapping form became ENERGY-TRANSFER.md's [STAGE v1](ENERGY-TRANSFER.md#stage-1a-concluded-the-taxonomy-the-refine-and-stage-v1-frozen) and then `OUTLINE_ADOPT` |
| Energy transfer (2026-09-30) | [this file](#before-the-energy-transfer-investigations-surveyed-2026-09-30) | splitting at an impact; the unit-free two-drop witness; a sphere fit for spin; shared motion for held objects; sub-pixel floors; the codecs' affine motion | ENERGY-TRANSFER.md, ["What the survey changed"](ENERGY-TRANSFER.md#what-the-survey-changed-2026-09-30) and each investigation's results; the rigid-region repair (lead 3) is [parked](ENERGY-TRANSFER.md#results-25e-lead-3s-selection-rule-the-m5-r1-and-r2-missed-the-lead-is-parked-with-its-reason) |
| Lead 4: fast motion of a fine periodic print (2026-09-30) | [this file](#before-lead-4-fast-motion-of-a-fine-periodic-print-surveyed-2026-09-30-2335-by-a-research-subagent-read-and-checked-before-it-was-filed) | carrying the aliases down and re-scoring them at full resolution (the BBC's menu; Nam et al.; MRMCS); the per-level trust gate (Battiti et al.; Anandan) | NFRAME-LIMITS.md, ["The weave"](NFRAME-LIMITS.md#the-weave-a-two-dimensional-periodic-print-where-the-field-locks-one-period-away-and-the-family-sits-at-the-blend-2026-09-30-late-evening), steps 0 to 1c; ENERGY-TRANSFER.md, lead 4 through [the cost cap](ENERGY-TRANSFER.md#results-b--2000-k2-passed-k3-missed-the-shipped-choice-a-budget-per-size): `PRINT_LATTICE`, the Cadence player's default (High) quality tier. The trust gate is [parked](ENERGY-TRANSFER.md#parked-by-the-owner-2026-10-01-morning-the-per-level-trust-gate-to-return-to-within-hours) |
| Lead 2: the impact mode as a shader (2026-10-01) | [this file](#before-lead-2-the-impact-mode-as-a-shader-one-source-per-pixel-chosen-by-the-side-of-tau-surveyed-2026-10-01-0405-by-a-research-subagent-read-and-checked-before-it-was-filed) | the four-field pair test (BBC, US 6,005,639); a fifth sample from the carry; WENO and ICI triggers | nothing built: [parked for the player](ENERGY-TRANSFER.md#the-owners-two-decisions-2026-10-01-morning-and-the-tiers-costs); the offline prototype is ENERGY-TRANSFER.md [3.2](ENERGY-TRANSFER.md#results-32-the-impact-placer-prototype-2026-09-30) |

---

Surveyed 2026-08-31, before the four-frame leap, to answer one question
honestly: are we treading new ground or old footsteps? The answer splits
cleanly by layer, and the split is worth internalising.

**The motion model: old footsteps, independently re-derived.** The exact
algebra of the tridirectional shader is in the record. *Quadratic Video
Interpolation* (Xu et al., NeurIPS 2019) models inter-frame motion as
`x(t) = x0 + v*t + a/2*t^2`, recovers per-pixel acceleration from the two
flows out of an anchor frame as `a = f(0->1) + f(0->-1)`,
`v = (f(0->1) - f(0->-1))/2` -- our N:N centred stencil, symbol for symbol --
and places interpolated content on the curve instead of the constant-velocity
line. Even our term exists: *High-quality Frame Interpolation via
Tridirectional Inference* (Choi et al., WACV 2021) uses three frames for
exactly the reason we did (two frames cannot see nonlinear motion). The cubic
extension over four frames exists too (*All at Once: Temporally Adaptive
Multi-Frame Interpolation with Advanced Motion Modeling*, ECCV 2020; also a
granted US patent, 11,430,138, on multi-frame VFI with higher-order models).

**The delivery and the instrument: no footsteps found.** Every one of those
is a deep-learning system -- PWC-Net-class flow networks feeding synthesis
CNNs, offline, non-deterministic, benchmarked on PSNR of pictures. The
searches found no prior work that (a) gives real-time user shaders an N-frame
window inside a production video pipeline (the `PL_HOOK_FRAME_MIX` patch has
no counterpart we could find), (b) treats the per-texel acceleration field as
the *product*, calibrated against analytic ground truth with coverage and
conditional-accuracy reporting, or (c) does any of it deterministically. The
practical block-matching lineage (MVTools/SVP, and commercial MEMC / optical
-flow frame generation) shares our estimator vocabulary but stops at 2-frame
windows and at pictures.

So: the mathematics is confirmed rather than invented here -- which is worth
having, since QVI's published results are an independent replication of our
central hypothesis on real footage -- and the engineering plus the
instrument framing is, as far as the record shows, ours.

## The closest discipline is not video processing

**Particle image velocimetry.** Fluid dynamicists have spent thirty years
extracting velocity fields from image sequences *as calibrated instruments*,
and the acceleration extension is mature there: four-pulse PIV measures
material acceleration directly (Liu & Katz 2006, *Experiments in Fluids*);
N-pulse PIV-accelerometry (N = 3, 4) is an instrument class of its own; and
"fluid trajectory correlation" fits curved trajectories across whole N-frame
bursts. Their vocabulary maps one-to-one onto ours -- interrogation window =
block, correlation peak fit = sub-pixel refinement, seeding density =
texture coverage -- and their failure taxonomy is our failure taxonomy,
twenty years better documented. When the N-frame generalisation needs
estimator designs or error budgets, read PIV literature, not VFI literature.

## Directly usable results, in priority order

1. **Peak locking (PIV/stereo term for a bias we are already carrying).**
   Sub-pixel fits through a cost minimum bias the estimate toward integer
   positions, with error a known function of the true fractional part
   (Shimizu & Okutomi). The fit should match the valley's shape: a parabola
   is the matched fit for an SSD valley, but an **SAD valley is piecewise
   linear**, for which the **equiangular (V-shaped) fit** is the matched
   estimator. Ours is a parabola over SAD -- mismatched -- and peak-locking
   bias is *toward zero at small displacements*, which is the shape of the
   residual under-read still visible in `A4`. One-line change, sweepable
   against the same calibration. Cheapest open win we have.

   *2026-10-01: done: the equiangular fit shipped ([QUADDIRECTIONAL.md, "Post-battery upgrade"](QUADDIRECTIONAL.md#post-battery-upgrade-the-equiangular-fit-sharpens-both-fields);
   [TRIDIRECTIONAL.md, "Field accuracy, current state"](TRIDIRECTIONAL.md#field-accuracy-current-state-after-sub-pixel--the-equiangular-fit)).*

2. **The fourth frame is a fork, and both arms are in the record.** EQVI
   (Liu et al., ECCV-W 2020, AIM 2020 winner) fits the *quadratic* by least
   squares over three flows `f(0->-1), f(0->1), f(0->2)` -- spending the
   extra frame on consistency, not on jerk. All-at-Once fits the *cubic* --
   spending it on jerk, keeping zero redundancy. This is exactly the
   degrees-of-freedom fork our spanning-flow proof predicted. Nobody we
   found reads the least-squares residual back out as a per-texel
   confidence field, which is what our T3.1 wants it for. Pre-register both
   arms and measure.

   *2026-10-01: measured in [QUADDIRECTIONAL.md](QUADDIRECTIONAL.md#p4----the-lsq-residual-partially-confirmed-and-the-fork-is-decided) (P4): the exact cubic, `QUAD_MODE 0`, is the
   default, and the least-squares residual serves as a trust gate.*

3. **Stencil algebra sharpens the leap's success criteria** (classical
   numerical differentiation, no citation needed). For the symmetric N:N
   window, `a = d(+1) + d(-1)` cancels ALL odd-order terms: constant jerk
   cannot bias the centred estimate, whose leading truncation error is
   snap/12. And a cubic fit through `d(-1), d(+1), d(+2)` returns the
   *identical* anchor acceleration -- the jerk term lands in `j`, not in `a`.
   Two consequences, both pre-registerable:
   - The four-frame shader should NOT be expected to improve the N:N anchor
     acceleration on smooth content. Its gains land elsewhere: the jerk
     field itself, the consistency residual as measured confidence, and
     cubic *placement* at 24->60, where the stencil is asymmetric and jerk
     does not cancel.
   - The 11.2% residual at `O5` frame 10 is therefore probably not jerk
     truncation at all -- a sinusoid's zero crossing is also its *velocity
     maximum* (a third variable the scene welds to the other two), and
     matching error grows with speed. If the four-frame fit does not move
     that number, this is why, and the control is a scene that separates
     |v| from jerk.

   *2026-10-01: P1 was confirmed to the digit (QUADDIRECTIONAL.md). The O5 frame-10 figure later fell to 4.9% with
   the equiangular fit ([TRIDIRECTIONAL.md](TRIDIRECTIONAL.md#field-accuracy-current-state-after-sub-pixel--the-equiangular-fit)) and to 2.1% against the corrected
   discrete truth ([QUADDIRECTIONAL.md, "CORRECTION, 2026-09-01"](QUADDIRECTIONAL.md#correction-2026-09-01-the-jerk-truth-model-was-wrong-and-the-field)).*

4. **Savitzky-Golay filters are the N-frame endgame.** A degree-d
   least-squares fit over N uniform samples, evaluated at a fixed point, is
   a fixed FIR filter with closed-form coefficients and known white-noise
   variance amplification. The N-frame roadmap ("each n smooths the curve")
   has a seventy-year-old theory: choose N and d from the SG variance
   formulas instead of sweeping blind.

5. **The causal path has a standard answer we should name.** Our proof that
   a 3-frame causal window buys nothing stands; the literature's answer to
   causal acceleration from noisy positions is not a finite window at all
   but the **alpha-beta-gamma filter** (Kalman filter, constant-acceleration
   model): recursion over *all* past frames with a tunable lag/variance
   trade. That is the real-time sensing variant, when it is wanted.

6. **Independently reproduced, now with names.** Our round-trip trust gate
   is forward-backward consistency checking, the standard optical-flow
   occlusion test; our vector median is the standard vector median filter
   (Astola et al. 1990). Convergent reinvention is evidence the designs are
   right, and the named literature carries refinements if either ever needs
   one.

## What not to import

The QVI/EQVI/tridirectional-inference line gets its picture quality from CNN
synthesis stacks on top of the motion model. Importing that would cost
everything the project is for: determinism, calibratability, the
1927-frames-per-second shader budget, and the ability to prove the field
against analytic truth. Take their algebra and their ablations; leave their
networks.

## Sources

- Xu et al., *Quadratic Video Interpolation*, NeurIPS 2019 —
  https://proceedings.neurips.cc/paper/2019/hash/d045c59a90d7587d8d671b5f5aec4e7c-Abstract.html
- Liu et al., *Enhanced Quadratic Video Interpolation*, ECCV-W 2020 —
  https://arxiv.org/abs/2009.04642
- Choi, J., Park, J. and Kweon, I. S., *High-quality Frame Interpolation via Tridirectional
  Inference*, WACV 2021 —
  https://openaccess.thecvf.com/content/WACV2021/papers/Choi_High-Quality_Frame_Interpolation_via_Tridirectional_Inference_WACV_2021_paper.pdf
- Chi et al., *All at Once: Temporally Adaptive Multi-Frame Interpolation
  with Advanced Motion Modeling*, ECCV 2020 — https://arxiv.org/abs/2007.11762
- US Patent 11,430,138, Chi et al. (Huawei), *Systems and methods for multi-frame video frame
  interpolation*
- Liu, X. and Katz, J., *Instantaneous pressure and material acceleration measurements
  using a four-exposure PIV system*, Exp. Fluids 2006 —
  https://link.springer.com/article/10.1007/s00348-006-0152-7
- Ding, L. and Adrian, R. J., *N-pulse particle image velocimetry-accelerometry*, Meas. Sci. Technol.
  2017 — https://iopscience.iop.org/article/10.1088/1361-6501/28/1/014001
- Shimizu, M. and Okutomi, M., sub-pixel estimation bias / equiangular fit (via
  stereo sub-pixel literature); Nehab, D., Rusinkiewicz, S. and Davis, J., *Improved Sub-pixel Stereo
  Correspondences through Symmetric Refinement*, ICCV 2005 —
  https://gfx.cs.princeton.edu/pubs/Nehab_2005_ISS/subpixel.pdf
  *Which paper (note added 2026-10-01): the record names no Shimizu and Okutomi paper. The best candidate is Shimizu,
  M. and Okutomi, M., "Sub-pixel estimation error cancellation on area-based matching", IJCV 63(3), 207-224, 2005,
  which treats the bias toward integer positions and names the equiangular fit for SAD. Their "Significance and
  attributes of subpixel estimation on area-based matching", Systems and Computers in Japan 34(12), 1-10, 2003,
  analyses the same bias and the matched pairs of similarity and fitting functions.*
- Astola, J., Haavisto, P. and Neuvo, Y., *Vector median filters*, Proc. IEEE 78(4), 678-689, 1990 (cited in item 6
  above; entry added 2026-10-01)

## Before the periodic-interior leap: V3 in other people's words (surveyed 2026-09-27, night)

The owner's steer before the leap, 2026-09-27: consider whether any external science is relevant. The problem might
be novel, or esoterically mathematical, but "there is always some mad scientist out there who has made a piece of
maths because it is beautiful and nobody knows what to do with it." Four sweeps ran in parallel:
- computer vision (stereo and optical flow);
- the production disciplines (TV motion-compensated frame-rate conversion, codec motion search, PIV);
- vision science;
- mathematics.

Each sweep checked its citations against search results or the papers; the ones seen only as an abstract are marked
below. The problem is NFRAME-LIMITS.md's V3: a square-wave print, period 24 px, moving exactly half a period (12 px) a
frame. Inside the patch +12 and -12 score alike, and only the patch's ends can say which.

### The problem has names

- **Mathematics: a lift of a covering map, which is phase unwrapping.**
  - Inside the patch the displacement is known only on the circle R/PZ (P = 24). The truth is its lift to R, and a
    lift is unique only once a starting point is fixed (the unique path-lifting property; residues are where it
    becomes path-dependent).
  - At P/2, +12 and -12 are one point on the circle. Zero motion is exactly opposite it, and zero is the reference
    most readily to hand: the background, a search centred on 0, a prior from rest.
  - Itoh's condition (neighbours differ by less than P/2) fails *with equality* at the patch's edge. So the background
    cannot start the lift, and V3 is the worst case of the lift by construction.
  - Persistence is a lift along time from the first frame. Anchoring at the ends would be a lift in space.
- **Signal and perception: the interior has no direction to find.**
  - When a square wave shifts by exactly half a period, every odd harmonic shifts by an odd multiple of 180 degrees.
    A motion-energy detector (Adelson & Bergen 1985) therefore sees pure counterphase flicker in the interior, with
    zero net direction. The direction lives only in the envelope.
  - Ohtani, Ido & Ejima (1995) is our stimulus exactly: a grating shifted 180 degrees is seen moving either way, or
    both, and flanking unambiguous motion always captures it.
  - McKee et al.'s wallpaper illusion (2004, 2007) is the stereo twin: the envelope decides first, and the human
    error comes only after the envelope signal adapts away.
- **Measurement: known modulo the period.** Wildeman (2018, Schlieren against a periodic backdrop) states displacement
  modulo the period, valid below half of it, and unwraps from a reference.
- **Ours on top:** the 1/8 level's flow is in whole 8-px texels. There, 12 px is a four-way tie (+8, +16, -8, -16),
  not a two-way one.

### What four fields agree on

1. **Combine hypotheses as costs or beliefs, never as vectors.**
   - **PIV:** Hart's correlation-based correction multiplies neighbouring correlation planes element by element, and
     he stresses that it is not an averaging technique. Meinhart, Wereley & Santiago average correlation planes, not
     vectors.
   - **Vision:** Weiss (1997) passes beliefs, not estimates. On the aperture problem it was right after 3 iterations
     where relaxation on point estimates was still wrong after 500.
   - **Vision science:** Lidén & Pack's MT model keeps support per direction, suppresses locations where several
     directions are active, and spreads each direction's support separately.
   - **TV frame-rate conversion:** 3-D recursive search (de Haan et al. 1993) re-scores neighbours' vectors in the
     cell's own SAD and never averages them.
   - **Mathematics:** averaged as phasors e^(2 pi i d / P), +12 and -12 agree exactly (Singer 2011; Cucuringu &
     Tyagi).
   - **The counter-example:** GMFlow's global matching and flow propagation are softmax and attention means of
     vectors. They work only because learned features are not periodic.
   - **Ours:** the 1/8 propagation is a contrast-weighted mean of vectors, the one operation all four fields avoid.
     SGM's min-sum recursion shows why costs survive a tie: a margin picked up at the boundary crosses a tied interior
     of any width undiminished (up to its jump penalty P2).
2. **Weight by distinctness, not by contrast.**
   - **The measures:**
     - PIV weights by peak ratio (Charonko & Vlachos 2013; commercial vector validation does the same).
     - Stereo uses the confidence measures in Hu & Mordohai (2012; abstract only): the second local minimum against
       the first. Use the *difference* (MM) with the distance between the two minima, not a ratio, since SAD near 0
       makes ratios unstable.
     - Ohtani's capture strengthens with the flankers' contrast and weakens with the test grating's own.
   - **Ours:** the propagation's weight is the 5 x 5 luma range. A V3 interior cell is high-contrast and perfectly
     ambiguous, so it gets the *highest* weight.
3. **Anchor at intrinsic boundaries, and carry the answer inward within the frame, with reach.**
   - **Mathematics:** reliability-guided phase unwrapping (Su & Chen 2004) floods outward from the most reliable
     pixels.
   - **Stereo and flow:**
     - SGM carries the boundary's margin along 1-D paths: one scan per direction crosses the patch. The GPU precedent
       is Hernandez-Juarez et al. 2016. DCFlow's Flow-SGM uses 4 paths over 2-D labels.
     - NG-fSGM restricts each cell's labels to its neighbours' 2 best (N = 2-3 was optimal). That is exactly what
       keeps both aliases alive.
     - Meyer et al.'s phase-based frame interpolation (CVPR 2015) lets the coarser level override a fine phase that
       disagrees by more than a quarter cycle (their shift correction). It is the vision instance of hierarchical
       unwrapping, which our pyramid already is.
   - **GPU propagation:** jump flooding (Rong & Tan 2006) and pull-push or normalised convolution (Gortler et al.
     1996; Knutsson & Westin 1993) give log-depth reach.
   - **The brain** takes 60-400 ms to fill from terminators (Pack & Born 2001, and Born et al.), longer for longer
     bars. An interpolator cannot show those frames: the fill must finish inside one.
4. **Persistence is a bounded tie-breaker that loses to fresh spatial evidence.**
   - **Vision science:**
     - Visual inertia is a 10-20% bias that fades over about half a second (Anstis & Ramachandran 1987).
     - Strong hysteresis is a documented human FAILURE: observers had to look away for 10-30 s to escape it
       (Ramachandran & Anstis 1983, 1985).
     - Hysteresis breaks when evidence shrinks the held basin (Hock, Kelso & Schöner 1993).
   - **TV frame-rate conversion:** 3DRS orders its penalties so a temporal candidate loses ties to spatial ones.
   - **Learned flow:** RAFT re-reads its costs every iteration, and rejects coarse-to-fine cascades as unable to
     recover from coarse errors.
   - **Stereo:** cross-scale cost aggregation (Zhang et al. 2014) passes costs between scales, not vectors, because
     coarse-to-fine narrowing freezes a basin.
   - **Ours:** this is our V3 behaviour exactly. The 1/8 level's temporal seed (the previous flow at the same cell,
     with SEED_TEMP_LAMBDA) is the hysteresis. Because it is not motion-compensated, it is also why a correction
     heals the patch from one edge only.
5. **Gate the spread by ownership, not by luminance.**
   - **Vision science:**
     - A boundary counts only if it moves with the pattern (Shimojo, Silverman & Nakayama 1989: intrinsic against
       extrinsic terminators).
     - Luminance-gated diffusion (Tlapale, Masson & Kornprobst 2010) would stop at the first stripe.
   - **Stereo:** DCFlow's intensity-adaptive P2 would shrink the carried margin at every stripe edge. Inside a pattern
     the penalty must be constant.
   - **The undecidable case:** a print drifting behind a still window at P/2 is undecidable, and should fall back
     gracefully rather than choose.

### Two warnings, and one door already closed

- **Weak interior preferences break a boundary condition.**
  - In 2-D, an arbitrarily weak random field makes the Ising model's boundary conditions lose their grip on a large
    interior (Imry & Ma 1975; Aizenman & Wehr 1989).
  - So a locally coupled smoothness model whose ambiguous cells carry even a faint preference breaks into domains,
    whatever the edges say.
  - COARSE_ENERGY's pinned domain wall is this in miniature: a coherent wrong preference in the interior, and the
    edges hold only two or three bands.
  - The rule that follows: keep an ambiguous cell's data exactly flat, and carry the anchor non-locally.
- **More frames cannot break an exact half-period tie.**
  - At an integer baseline of n frames, a constant velocity is known only modulo P/n. Every such modulus divides P,
    so the Chinese remainder theorem can never resolve past v mod P. That is the modulus radar's range-ambiguity
    resolution needs co-prime (Trunk & Brockett 1993; Li, Liang & Xia 2009, robust CRT).
  - The same arithmetic defeats the production versions: Panasonic's n-2 candidate (EP1592255A1) and multi-frame
    pyramid correlation in PIV (Sciacchitano et al. 2012).
  - Okutomi & Kanade's multiple-baseline stereo works for depth only because its baselines are not commensurate with
    the pattern (seen as an abstract; the PDF is a scan).
  - **For the N-frame roadmap:** an exact periodic alias is a limit a longer window cannot buy its way out of. Only
    an edge, a non-integer baseline, a second period in the content, or a known start can break it.
- **Closed:** the prefiltered pyramid, which the engineering sweep offered as the cheapest check, was built and refuted
  on 2026-09-03 (NFRAME-LIMITS.md section 8).

### What to import, in order (steps before the leap)

1. **The ambiguity flag.**
   - What: in the 1/8 search, keep the best cost and the best cost at least half a period away (MM plus the distance
     between them).
   - Cost: nearly free.
   - As a diagnostic first: does it light the V3 interior and not its ends, and what else lights on the ladder and on
     real footage?
2. **Distinctness for contrast** in the propagation's weight, and **no temporal tie-break in a flagged cell**.
   - Size: each a few lines of the generator.
   - Measured by v3phase.sh and the full gate, as any switch.
3. **The leap: per-hypothesis aggregation with reach, deterministic, a handful of dispatches.** Either of two forms:
   - **SGM form:**
     - four scans over a small candidate set per 1/8 cell (the prior, the neighbours' two best, the cell's own
       second minimum: NG-fSGM's subset, without its random candidates);
     - a constant jump penalty inside the pattern;
     - then winner-takes-all.
   - **Unwrapping form:**
     - jump-flood a reference from the anchor cells, where the anchors are the unambiguous cells with the same wrapped
       value and period;
     - then lift each flagged cell as d = w + P round((r - w) / P).

*2026-10-01: items 1-3 were built: the flag offline in NFRAME-LIMITS.md, ["The field on real bodies"](NFRAME-LIMITS.md#the-field-on-real-bodies-two-hours-of-children-scored-against-a-skeleton-it-shares-nothing-with-2026-09-27);
`ALIAS_PRIOR` and `ALIAS_CARRY` in ["The half-period alias in the shader"](NFRAME-LIMITS.md#the-half-period-alias-in-the-shader-the-prior-gate-and-the-carry-2026-09-28),
with the aperture rule in ["The aperture in the carry"](NFRAME-LIMITS.md#the-aperture-in-the-carry-b1-moving-up-and-the-energy-channel-on-rendered-children-2026-09-28-later), in the Cadence player from
1.0.3. The unwrapping form became ENERGY-TRANSFER.md's [STAGE v1](ENERGY-TRANSFER.md#stage-1a-concluded-the-taxonomy-the-refine-and-stage-v1-frozen) and then
`OUTLINE_ADOPT`.*

### What not to import

- **Learned networks** (RAFT, GMFlow, LiteFlowNet3): principles only.
- **Any averaging of vectors:** soft-argmax, attention, and our own mean.
- **Random candidates** (PatchMatch, NG-fSGM's random vectors): they break determinism. Also, PatchMatch accepts only a
  strictly better candidate, so it stalls on a tie anyway.
- **Full-range global optimisation:** Full Flow takes 30 s to 2 min a frame; DCFlow's aggregation 0.45 s.
- **Loopy belief propagation run to convergence:** its iterations grow with the patch.
- **Least-squares (Poisson) unwrapping:** it smears, and reads the P/2 edge as a tie.
- **Serial solvers:** min-cost flow and graph cuts.
- **Noise or adaptation as the release from hysteresis:** the brain's release, but in an interpolator it is flicker.
- **Temporal multi-baseline.**
- **Luminance- or intensity-gated diffusion inside a pattern.**
- **Vector-domain validation as the fix:** the median tests and the TV chips' pitch-and-regional-vector penalties all
  pass a coherent wrong alias.
- **The no-motion-compensation fallback** except as a last resort.

### Sources (the periodic-interior sweep)

Mathematics
- Itoh, K., *Analysis of the phase unwrapping algorithm*, Applied Optics 21(14), 1982 — https://opg.optica.org/ao/abstract.cfm?uri=ao-21-14-2470
- Goldstein, R. M., Zebker, H. A. and Werner, C. L., *Satellite radar interferometry: two-dimensional phase unwrapping*, Radio Science 23(4), 1988 — https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/rs023i004p00713
- Su, X. and Chen, W., *Reliability-guided phase unwrapping algorithm: a review*, Optics and Lasers in Eng. 42, 2004 — https://www.sciencedirect.com/science/article/abs/pii/S0143816603001404
- Ghiglia, D. C. and Romero, L. A., weighted and unweighted unwrapping by fast transforms, JOSA A 11(1), 1994 — https://opg.optica.org/josaa/abstract.cfm?uri=josaa-11-1-107
- Zuo et al., *Temporal phase unwrapping algorithms for fringe projection profilometry: a comparative review*, Optics and Lasers in Eng. 85, 2016 — https://www.sciencedirect.com/science/article/abs/pii/S0143816616300653
- Wilkins, D. R., *Covering maps and the monodromy theorem* (TCD course notes) — https://www.maths.tcd.ie/~dwilkins/Courses/421/421S3_0809.pdf
- Singer, A., *Angular synchronization by eigenvectors and semidefinite programming*, ACHA 30(1), 2011 — https://arxiv.org/abs/0905.3174
- Cucuringu, M. and Tyagi, H., modulo-1 samples of a smooth function and phase unwrapping, 2018 — https://arxiv.org/abs/1803.03669
- Imry, Y. and Ma, S.-k., PRL 35:1399, 1975 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1399 ; Aizenman, M. and Wehr, J., PRL 62:2503, 1989 — https://link.aps.org/doi/10.1103/PhysRevLett.62.2503
- Li, X., Liang, H. and Xia, X.-G., *A robust Chinese remainder theorem*, IEEE TSP 57(11), 2009 — https://dl.acm.org/doi/abs/10.1109/TSP.2009.2025079 ; Trunk, G. and Brockett, S., *Range and velocity ambiguity resolution*, IEEE National Radar Conf., 1993
- Rong, G. and Tan, T.-S., *Jump flooding in GPU*, I3D 2006 — https://www.comp.nus.edu.sg/~tants/jfa.html ; Gortler et al., *The Lumigraph* (pull-push), SIGGRAPH 1996 ; Knutsson, H. and Westin, C.-F., *Normalized and differential convolution*, CVPR 1993

Stereo and optical flow
- Hirschmüller, H., *Stereo processing by semiglobal matching and mutual information*, TPAMI 30(2), 2008 — https://dl.acm.org/doi/10.1109/TPAMI.2007.1166 ; Hernandez-Juarez et al., embedded real-time SGM on the GPU, ICCS 2016 — https://arxiv.org/abs/1610.04121
- Xu, J., Ranftl, R. and Koltun, V., *Accurate optical flow via direct cost volume processing* (DCFlow), CVPR 2017 — https://arxiv.org/abs/1704.07325 ; Chen, Q. and Koltun, V., *Full Flow*, CVPR 2016 — https://arxiv.org/abs/1604.03513
- Li et al., *Neighbor-guided SGM optical flow* (NG-fSGM), IEEE TCSVT 29(7), 2019, doi:10.1109/TCSVT.2018.2854284
- Weiss, Y., *Interpreting images by propagating Bayesian beliefs*, NIPS 9, 1996 — https://papers.nips.cc/paper/1309-interpreting-images-by-propagating-bayesian-beliefs ; Felzenszwalb, P. F. and Huttenlocher, D. P., *Efficient belief propagation for early vision*, IJCV 70, 2006
- Barnes et al., *PatchMatch*, SIGGRAPH 2009 ; Besse et al., *PMBP*, BMVC 2012 ; Bailer, C., Taetz, B. and Stricker, D., *Flow Fields*, ICCV 2015 — https://arxiv.org/abs/1703.02563
- Zhang et al., *Cross-scale cost aggregation for stereo matching*, CVPR 2014 — https://arxiv.org/abs/1403.0316 ; Rhemann et al., *Fast cost-volume filtering*, CVPR 2011 (abstract only)
- Hu, X. and Mordohai, P., *A quantitative evaluation of confidence measures for stereo vision*, TPAMI 34(11), 2012 (definitions via Poggi et al., TPAMI 44(9), 2022, https://arxiv.org/abs/2101.00431)
- Okutomi, M. and Kanade, T., *A multiple-baseline stereo*, TPAMI 15(4), 1993 (abstract only) ; Lin, W.-C. and Liu, Y., lattice-based MRF tracking of near-regular texture, TPAMI 29(5), 2007
- Teed, Z. and Deng, J., *RAFT*, ECCV 2020 — https://arxiv.org/abs/2003.12039 ; Xu et al., *GMFlow*, CVPR 2022 — https://arxiv.org/abs/2111.13680
- Meyer et al., *Phase-based frame interpolation for video*, CVPR 2015 — https://cgl.ethz.ch/publications/papers/paperMey15a.php

Production disciplines
- de Haan et al., *True-motion estimation with 3-D recursive search block matching*, IEEE TCSVT 3(5), 1993 — https://research.tue.nl/en/publications/true-motion-estimation-with-3-d-recursive-search-block-matching/ ; Pohl et al., real-time 3DRS for frame-rate conversion, IS&T EI 2018
- Periodic-structure patents: US20130039427A1 (Marvell/Synaptics), US8253854B2 (Broadcom), US10057596B2 (Novatek), US8675080B2 (STMicro), US10395378B2 (Samsung), EP1592255A1 (Panasonic)
- Hart, D. P., *PIV error correction*, Exp. Fluids 29, 2000 — https://web.mit.edu/dphart/www/PIV_ERROR2.PDF
- Meinhart, C. D., Wereley, S. T. and Santiago, J. G., *A PIV algorithm for estimating time-averaged velocity fields*, J. Fluids Eng. 122, 2000
- Charonko, J. J. and Vlachos, P. P., uncertainty from the correlation peak ratio, Meas. Sci. Technol. 24, 2013 — https://iopscience.iop.org/article/10.1088/0957-0233/24/6/065301
- Westerweel, J. and Scarano, F., *Universal outlier detection for PIV data*, Exp. Fluids 39, 2005 ; Masullo, A. and Theunissen, R., multiple correlation peaks in PIV, Exp. Fluids 2018 (abstract only) ; Sciacchitano, A., Scarano, F. and Wieneke, B., multi-frame pyramid correlation, Exp. Fluids 53, 2012
- Wildeman, S., *Real-time quantitative Schlieren imaging by fast Fourier demodulation of a checkered backdrop*, Exp. Fluids 59, 2018 — https://arxiv.org/abs/1712.05679

Vision science
- Adelson, E. H. and Bergen, J. R., *Spatiotemporal energy models for the perception of motion*, JOSA A 2, 1985 — https://opg.optica.org/josaa/abstract.cfm?uri=josaa-2-2-284
- Wallach, H., 1935, translated by Wuerger, S., Shapley, R. and Rubin, N., Perception 25, 1996 — https://journals.sagepub.com/doi/10.1068/p251317
- Shimojo, S., Silverman, G. H. and Nakayama, K., *Occlusion and the solution to the aperture problem for motion*, Vision Res. 29, 1989 — https://pubmed.ncbi.nlm.nih.gov/2603398/
- Ohtani, Y., Ido, K. and Ejima, Y., Vision Res. 35, 1995 — https://pubmed.ncbi.nlm.nih.gov/7571464
- McKee et al., *The wallpaper illusion explained*, J. Vis. 7(14), 2007 — https://pubmed.ncbi.nlm.nih.gov/18217805
- McKee, S. P., Verghese, P. and Farell, B., *What is the depth of a sinusoidal grating?*, J. Vis. 4(7), 524-538, 2004 (the
  "2004" cited above beside the 2007 paper; identified 2026-10-01 as the only 2004 McKee paper the 2007 paper cites)
- Anstis, S. and Ramachandran, V. S., *Visual inertia in apparent motion*, Vision Res. 27, 1987 — https://pubmed.ncbi.nlm.nih.gov/3660637/ ; Ramachandran, V. S. and Anstis, S. M., Nature 304, 1983 ; Ramachandran, V. S. and Anstis, S. M., *Perceptual organization in multistable apparent motion*, Perception 14(2), 135-143, 1985 (the "1985" cited above; entry added 2026-10-01)
- Hock, H. S., Kelso, J. A. S. and Schöner, G., *Bistability and hysteresis in the organization of apparent motion patterns*, JEP:HPP 19, 1993 — https://pubmed.ncbi.nlm.nih.gov/8440989/
- Pack, C. C. and Born, R. T., *Temporal dynamics of a neural solution to the aperture problem in visual area MT*, Nature 409, 2001 — https://www.nature.com/articles/35059085
- Born et al., *Temporal evolution of 2-dimensional direction signals used to guide eye movements*, J. Neurophysiol.
  95(1), 284-300, 2006 (the "Born et al." cited above; identified 2026-10-01 from its abstract: longer bars, 50-400 ms)
- Lidén, L. and Pack, C., Vision Res. 39, 1999 — https://pubmed.ncbi.nlm.nih.gov/10615497/ ; Chey, J., Grossberg, S. and Mingolla, E., JOSA A 14, 1997 ; Tlapale, É., Masson, G. S. and Kornprobst, P., Vision Res. 50, 2010
- Weiss, Y., Simoncelli, E. P. and Adelson, E. H., *Motion illusions as optimal percepts*, Nat. Neurosci. 5, 2002 — https://www.nature.com/articles/nn858

## Before the energy-transfer investigations (surveyed 2026-09-30)

The owner's rule: survey before designing any leap. ENERGY-TRANSFER.md parks five investigations that ask the field
what energy it cannot see. This is their survey, done the day they were written: a web search per topic, preferring
primary sources. The document's own bibliography was checked the same day and is kept there. The newest arXiv items
below (2025-2026) were found by that search and have not been re-read individually.

*2026-10-01: the investigations have since run as far as they can without a camera; see the status note at the top of
[ENERGY-TRANSFER.md](ENERGY-TRANSFER.md).*

### What the survey changed, in order of weight

1. **At an impact, split; do not smooth through it.** Every working system fits each side of an impact and
   intersects the fits:
   - Hawk-Eye-class line calling. The ITF protocol asks each system how many images it uses before and after the
     bounce.
   - Tracking by Deblatting, which finds the bounces by dynamic programming and fits a polynomial to each piece in
     continuous time.
   - FBDepth, which fits straight lines per pixel to three frames each side and takes the collision time from their
     intersection, pooled over the object. It reaches a few milliseconds from 30 fps video.

   FBDepth's authors state that frame interpolation cannot interpolate across a collision. Our step 3.1 measures
   exactly that for our family. The derivative kernels need a one-sided mode, triggered by a jerk spike.
2. **Rolling shutter is both a bias and a clock.** It skews a fast mover (the g-test must timestamp each row). It
   also samples time finer than the frame rate: the visual microphone got 8-9x the frame rate from a 60 fps rolling
   shutter, and Šmíd and Matas synchronise cameras to 0.3-0.5 ms with it. Measure each camera's readout time once,
   with a flash.
3. **Ground truth on real footage fails on geometry first.** Teaching labs measure errors of up to 40 percent from a
   scale reference at the wrong depth, or a throw that is not square to the camera. Frame rate barely matters. A
   parabola in a tilted plane is a general conic in image space. The better witnesses:
   - fit in the throw's plane through a homography;
   - use a unit-free two-drop ratio (t1^2 / t2^2 = h1 / h2) that needs no g, scale or frame rate.

   **Scoring optical flow by physical constancy on real video appears unclaimed**: nothing was found. The nearest
   discipline is uncertainty quantification in particle image velocimetry (PIV).
4. **Curl alone cannot recover a ball's spin.** A 2-D field's curl sees only spin about the line of sight. Spin
   about an axis in the image plane appears as a depth-weighted shear, so a sphere fit is needed (omega x r with
   z = sqrt(R^2 - x^2 - y^2)). Spin along the direction of travel (gyrospin) never shows in a trajectory. Spin above
   half the frame rate aliases.
5. **A held object is the textbook case where JPDA merges tracks.** So hand and ball should not be tracked as
   rivals matched by position. They belong together when their relative velocity and acceleration stay near zero
   over a window. A release is an impulse event, as in finding 1.
6. **The cradle's middle balls are an open measurement.** Nothing was found measuring them, or the click's timing,
   with a high-speed camera. The realistic sub-pixel floor for phase-based methods is about 0.01 px. The 0.001 px
   figures needed high-speed, controlled scenes. Timing an impact by sound needs ~2.9 ms per metre of travel and
   each device's audio-video offset (~1 ms on an iPhone, per FBDepth).

### Two finds that bear on the record beyond this document

- **Koenderink and van Doorn (1976)** split a flow field into divergence, curl and two deformation parts. They are
  the pioneers of the velocity gradient tensor the reading has emitted since Lead E (read_view 9), and the record
  never cited them.
- **Zhang, Pintea and van Gemert, "Video Acceleration Magnification" (CVPR 2017)** magnifies the second derivative
  in time and ignores linear motion. It is the closest published relative of the acceleration field, which the first
  survey found no footsteps for. It magnifies acceleration; it does not measure or calibrate it, so the first
  survey's claim (b), the calibrated per-texel acceleration field as the product, stands.

### Rigid and affine motion as one: the production precedent (added 2026-09-30, late evening, with 2.5's result)

- **Video coding already moves rotation as one.** VVC (H.266) carries block-based affine motion compensation,
  4-parameter (translation, one rotation, one zoom) and 6-parameter. The motion of each 4x4 sub-block is derived
  from two or three control-point vectors. The 4-parameter model is Li et al., "An Efficient Four-Parameter Affine
  Motion Model for Video Coding", IEEE TCSVT 28(8), 1934-1948 (2018). Earlier, rotational block matching against
  an interpolated reference was published in EURASIP J. Adv. Signal Process. (2010).
- **What that means for 2.5.** A codec chooses the affine model per block by rate-distortion cost, with the
  original frame in hand. An interpolator has no original to test against. So the codec's model is the precedent,
  but not its selection rule: the region has to be found from the field. 2.5 measured the model's worth with the
  region given (a repair of 8-28 dB where the family fails, little where it works). The selection is the open part.
- **Kept for the lead:** the control-point form (two vectors define a block's rotation and zoom) is the natural way
  to carry a rigid fit into a per-block shader, and it is cheap to evaluate per pixel.

*2026-10-01: the selection rule was tested in ENERGY-TRANSFER.md 2.5b-2.5e, and lead 3 is parked
([Results: 2.5e](ENERGY-TRANSFER.md#results-25e-lead-3s-selection-rule-the-m5-r1-and-r2-missed-the-lead-is-parked-with-its-reason)).*

## Before lead 4: fast motion of a fine periodic print (surveyed 2026-09-30, 23:35, by a research subagent; read and checked before it was filed)

Scope: the fast-weave lock (11-19 px/frame; it enters at the 1/8 and 1/16 levels; the outline locks too). This adds
to PRIOR-ART.md's periodic-interior sweep (09-27) without repeating it: SGM/NG-fSGM, unwrapping, PatchMatch, learned
flow, BP, the CRT, 3DRS and the six patents listed there are cited by pointer only. Every citation was checked by web
search tonight. "(abstract)" means only the abstract or a summary was seen; UNVERIFIED means not confirmed.

### 1. Summary

- **A textbook failure.** In hierarchical search, "an erroneous match in the higher level is almost always propagated
  to the lower levels". Brox & Malik (2011) name "an inherent dependency between the scale of structures and the
  velocity that can be estimated". In our terms (our inference, consistent with W2/W3): the 1/8 level samples
  displacement every 8 px while the print's cost repeats every 14 px, so the displacement axis is aliased: the comb.
- **Two published fixes, neither a prefilter:**
  - carry several candidates down to a level that can tell them apart (Nam 1995; MRMCS 2001; the BBC's menu);
  - run the coarse pass at FULL resolution with a large window (PIV multigrid; BBC phase correlation; Flow Fields).
- **No field resolves an exactly periodic interior from its own two frames.** All import a reference: the outline,
  the neighbours, a region model, time, or a small-vector prior. The TV chips' last resort is to stop compensating.
- **Our weave is not exactly periodic.** Its 3-px value noise (0.1 against the threads' 0.7) differs between v and
  v - 28, and the full and 1/2 levels resolve it. So a fine re-score of BOTH candidates could pick the truth from the
  data alone (estimated margin about 0.02 luma, 5-6/255: not measured). Real cloth is irregular in the same way.

  *2026-10-01: measured: +0.0190 luma at full resolution, the truth lowest on every block (NFRAME-LIMITS.md,
  ["The weave"](NFRAME-LIMITS.md#the-weave-a-two-dimensional-periodic-print-where-the-field-locks-one-period-away-and-the-family-sits-at-the-blend-2026-09-30-late-evening), step 0).*
- **Temporal priors help only where the print was once read right.** Constant-velocity multi-frame fits cannot break
  a period tie (the CRT, on record).

#### 2. Findings by direction

#### 2.1 Coarse-to-fine failure and large-displacement flow
- **Brox & Malik, "Large displacement optical flow: descriptor matching in variational motion estimation", TPAMI
  33(3), 2011.** Coarse-grid descriptor matches act as soft constraints in variational coarse-to-fine (the quote
  above). Fit: no (seconds per frame). Principle: a full-resolution match re-enters where the pyramid lost the
  structure.
- **Steinbrücker, Pock & Cremers, "Large displacement optical flow computation without warping", ICCV 2009**
  (abstract). A relaxation decouples the data term; there is no warping pyramid, and it wins on "large displacements
  of small scale structures". Fit: parallel and deterministic, but the full range at every pixel, and it ties inside
  a print.
- **Sevilla-Lara, Sun, Learned-Miller & Black, "Optical flow estimation with channel constancy", ECCV 2014**
  (abstract). A pyramid of smoothed soft-histogram channels in which small objects survive. Inside a uniform print
  the channels are shift-invariant: it adds the outline only, as COARSE_ENERGY does.
- **Bailer, Taetz & Stricker, Flow Fields (ICCV 2015; in PRIOR-ART).** New detail, from the arXiv text: the coarse
  scales are full-resolution positions with scale-space patches, not a downsampled image. Repeats match when "the
  influence area of the coarsest scale is larger than the ambiguous repetitive pattern". Random search, so no.
- **Revaud et al., DeepMatching (IJCV 2016) and EpicFlow (CVPR 2015).** DeepMatching builds its coarse responses
  bottom-up from fine correlations and is reported strong on repetitive textures. Fit: no (seconds; EpicFlow
  averages vectors). Principle: build the coarse COST from fine costs, not from a coarse image.
- **Hu, Song & Li, CPM, CVPR 2016:** random search, so no.
- **Su et al., "Multiple hypothesis flow estimation for VFI under matching ambiguity", arXiv 2608.07120, Aug 2026**
  (abstract): top-K matches kept through refinement, and a learned router picks one per pixel. Principle only: keep
  K, choose late.
- **Reijalt et al., FlowFactor, arXiv 2607.10470, Jul 2026** (abstract): large-motion gains trade against robustness
  in small-motion and static scenes. It is our prefilter lesson, in a benchmark.

#### 2.2 Per-level trust and several hypotheses per level
- **Anandan, IJCV 2:283, 1989:** hierarchical SSD with confidence from the SSD surface's principal curvatures, and
  confident measurements spread to their neighbours. Fit: yes. But curvature is sharpness, not uniqueness, so an
  aliased sharp minimum reads as confident: pair it with PRIOR-ART's second-minimum flag.
- **Battiti, Amaldi & Koch, IJCV 6:133, 1991** (abstract): the scale is chosen per location from an estimate of the
  velocity error. The published precedent for section 8's per-level trust gate. Fit: yes.
- **Nam, Kim, Park & Shim, IEEE TCSVT 5(4):344, 1995:** K candidates per level seed the next, and the error spans
  full search to three-step search as K varies. Fit: yes, the candidates only (its mean pyramid is our refuted box).
- **Lee, Lim, Song & Ra, MRMCS, IEEE TCSVT 11, 2001** (abstract): 2 coarse candidates plus 1 spatial neighbour as
  the middle level's centres. **Chalidabhongse & Kuo, IEEE TCSVT 7(3):477, 1997:** spatial, temporal and
  hierarchical candidates at every level. **Bierling, SPIE 1001, 1988:** TV hierarchical block matching, the
  ancestor of our design. All fit.
- **Rothermel et al., SURE/tSGM, LC3D 2012.** The citation is verified; the detail is UNVERIFIED (from memory): the
  per-pixel range comes from the coarser level's min/max in a window, wider where that level is invalid.
- **Pauwels & Van Hulle, "Realtime phase-based optical flow on the GPU", CVPRW 2008** (abstract): reliability from
  phase consistency over time. A precedent for a temporal trust term.

#### 2.3 Coarse passes at full resolution: PIV and the BBC
- **PIV:** Scarano & Riethmuller, Exp. Fluids 26:513, 1999; Westerweel, Dabiri & Gharib, Exp. Fluids 23, 1997;
  Keane & Adrian, MST 1990 (the one-quarter rule). The coarse passes shrink the WINDOW, never the image: an FFT over
  a large full-resolution window scores every integer displacement up to a quarter of it. Fit: the direct sum over
  a short candidate list is per-pixel; the FFT is not.
- **The BBC:** Thomas, BBC RD 1987/11 (bibliographic record only); Thomas & Borer, US4873573A (1986), read.
  - Phase correlation on 64 x 32 blocks at full resolution (+-32 px, up to 3 peaks), giving a menu of up to 27
    vectors from the block and its neighbours.
  - Each small block takes the least-error vector, with a weight that rises with magnitude.
  - A periodic block peaks at every alias, so the choice falls to that assignment: a deterministic per-pixel
    re-score.
- **Eckstein, Charonko & Vlachos, Exp. Fluids 45:485, 2008:** whitened (phase-transform) correlation cuts erroneous
  vectors and peak locking. **Stone, Orchard, Chang & Martucci, IEEE TGRS 39(10), 2001** (abstract): drops the
  Fourier components that aliasing has made unreliable.
- **Our inference, not cited.** A print's energy sits in a few bins, which support every alias equally. Aperiodic
  detail spreads over many bins, which support only the truth. So whitening favours the truth wherever any aperiodic
  detail exists, where SAD is dominated by the threads.

#### 2.4 TV frame-rate conversion: repeat patterns (beyond PRIOR-ART's six patents)
- **Lee, Kwon & Park, "Motion vector correction based on the pattern-like image analysis", IEEE TCE 49(3):479, 2003**
  (abstract), and **Samsung US7555166B2** (2003), read.
  - A block is periodic when the projections of its SAD map show 2 or more minima.
  - A static pattern takes the minimum nearest zero; a moving one, the minimum nearest the neighbours' MEAN vector.
  - It is unwrapping with the neighbours as the reference, so it fails on a coherent lock.
- **Samsung US8223831B2** (2007): a spectral peak detects the pattern, and the output there is mixed towards the
  repeated pixel. The fallback.
- **Marvell/Synaptics US9197891B1** (2012): autocorrelation pitch finds periodic segments, and a RANSAC affine fit
  per segment replaces their vectors.

#### 2.5 Temporal priors
- **Huntley & Saldner, Appl. Opt. 32(17):3047, 1993:** unwrap along time from a known start, each step under half a
  period. Fit: yes (one fetch), if the start is right.
- **Schanz, Gesemann & Schröder, Shake-The-Box, Exp. Fluids 57:70, 2016** (abstract): tracks predicted from their
  past resolve ambiguities one step cannot; tracks start where particles are distinct. Principle: a
  motion-compensated temporal candidate.
- **Ren, Gallo, Sun, Yang, Sudderth & Kautz, WACV 2019:** warped previous flows as hypotheses, with learned fusion.
  **Volz et al., ICCV 2011** (citation only): variational trajectory coherence, bound by the CRT.

#### 2.6 Perception
- **Low spatial frequencies decide the direction of apparent motion:** Ramachandran, Ginsburg & Anstis, Perception
  12:457, 1983 (abstract), most of all at fast alternation. See also Ramachandran & Cavanagh, "Motion capture
  anisotropy", Vision Res. 27:97, 1987 (citation only), and Burt & Sperling, Psych. Rev. 88:171, 1981 (paths
  compete; one wins).
  - So the viewer takes the envelope's (the outline's) motion and lets it capture the texture. A wrong-alias
    interior tears at the boundary.
- **Chubb & Sperling, JOSA A 5(11):1986, 1988 (non-Fourier motion):** the name for COARSE_ENERGY's channel, which is
  flat inside a uniform print. That is why it left the comb open.

### 3. What to try first, ranked

1. **Carry the aliases down; re-score at the finest level that resolves aperiodic detail (1/2 or full).**
   Precedents: Nam, MRMCS, the BBC's assignment, Samsung 2003.
   - **Step 0 (numpy):** block SAD at full and 1/2 resolution, the truth against v - 28 and the diagonal aliases,
     with noise as the control. No margin means the lead is dead for the synthetic weave (not for real cloth).
   - **The shader:** in flagged cells, score {seed, seed +- p1, seed +- p2}, each refined +-1 texel.
     - p1 and p2 are the lattice vectors, from a per-cell self-SAD over shifts of 8-32 px (the chips' pitch
       detector, made deterministic).
     - Switch only when the margin clears a noise threshold.
     - Edge-ring cells see the ground and should choose the truth even without noise, which re-opens the outline
       cue for the existing lift.
   - **Cost:** 1-2 dispatches.
   - **Risk:** exact prints (V3, the lattice) still tie, with a lossless fallback; camera noise may flip picks
     (needs hysteresis); a wrong pitch drops the truth.
2. **The per-level trust gate; the first honest level searches wide** (section 8; Battiti, Anandan, tSGM,
   PIV/BBC).
   - **The flag:** point-sampled contrast against box-filtered contrast per texel and level (section 8: 11-28% of
     the variance kept).
   - **A flagged level** gives flat data and no seed.
   - **The first unflagged level** (1/4 for P = 14) searches +-24 px, seeded by the global, energy and temporal
     candidates.
   - **Cost:** +0-1 pass for the flag, plus the wide search on flagged texels (13 x 13 x 5 x 5 taps at 1/4; a few ms
     at 720p, estimated; 1-D along the lattice to cut it).
   - **Risk:** the interior still ties at 1/4, so item 1 or the outline carry must follow; false matches on real
     footage (FlowFactor; L0_static); a new threshold to sweep on the Arc.
3. **The motion-compensated temporal lift** (Huntley & Saldner; STB; 3DRS).
   - **The candidate:** the previous final vector read at x - v_prev, lifted to its nearest alias,
     d = w + P round((r - w) / P). It is re-scored in the cell's own cost and loses ties to fresh distinct evidence.
   - **Cost:** 1 fetch and 1 candidate. That is 0 new dispatches if it replaces the 1/8 temporal seed, which is not
     motion-compensated today.
   - **Risk:** it helps only prints once read right (so it needs a 0 -> 19 px/frame ramp test; the constant-speed
     sweep cannot show it); a wrong start persists (the V3 hysteresis).
4. **(Only if step 0 finds SAD's margin too thin.)** A whitened correlation menu on 64 x 64 tiles at 1/2 (the BBC's
   scheme), feeding item 1.
   - Cost: new FFT machinery, 2+ dispatches.
   - Risk: the range is limited to a quarter of the window, and the choice still falls to the re-score.

*2026-10-01: item 1 was built as `PRINT_LATTICE` (NFRAME-LIMITS.md, "The weave", steps 0 to 1c; ENERGY-TRANSFER.md,
lead 4 through the cost cap) and is the Cadence player's default (High) quality tier; item 2 is
[parked](ENERGY-TRANSFER.md#parked-by-the-owner-2026-10-01-morning-the-per-level-trust-gate-to-return-to-within-hours); items 3 and 4 are not recorded as tried.*

*2026-10-01, evening: item 2 is built as `TRUST_GATE` ([ENERGY-TRANSFER.md](ENERGY-TRANSFER.md#where-the-per-level-trust-gate-stands-2026-10-01-evening)). Its flag needed BOTH terms: the level's aliasing (the box against the point samples, as here) and the level's ambiguity (the second-minimum margin, Anandan's caveat above). The first honest level offers, and full resolution decides, with item 1's uniqueness test. The survey's risk (the interior ties at 1/4) was met by letting full resolution decide rather than the quarter level.*

### 4. Not to import
- **Mean, box or Gaussian pyramids** (any prefilter): refuted on 09-03, 8-20 dB on fine texture.
- **The non-MC fallback** (US8223831): the gates already fall to the blend, which is poor at 11-19 px/frame.
- **RANSAC or consensus region fits** (US9197891): random, and on a coherent lock the consensus IS the lock (the core
  outnumbers the edge, as measured).
- **The neighbours' mean as the output** (US7555166 uses it only as a reference): in a locked region it carries the
  lock.
- **LDOF, EpicFlow, DeepMatching, CPM, Flow Fields:** seconds per frame, random search, or averaged vectors.
- **Learned top-K and learned fusion** (Su 2026, Ren 2019): principles only.
- **A small-vector prior alone** (the BBC's weight; Weiss et al.): it fixes 11-13 px/frame but breaks 15-17, which
  read right today.
- **Channel-constancy pyramids:** they add only the outline, as COARSE_ENERGY does.
- **Multi-frame constant-velocity fits** (the CRT), and **a full-range point-wise search at every pixel**
  (Steinbrücker 2009).

**Checked on filing:** the project facts it cites (the comb, W2/W3, the refuted prefilter, the outline at slow speeds) match the record. Citations were checked by web search in the survey; the two 2026 arXiv items and tSGM's range detail are the least certain.

### Sources (the lead-4 sweep; collected 2026-10-01)

*Added 2026-10-01. The survey above cites inline; this list collects the works it cites, with their authors, in the
form used across this file. Works it cites by pointer to the earlier surveys are not repeated.*

- Brox, T. and Malik, J., *Large displacement optical flow: descriptor matching in variational motion estimation*, IEEE TPAMI 33(3), 500-513, 2011
- Steinbrücker, F., Pock, T. and Cremers, D., *Large displacement optical flow computation without warping*, ICCV 2009, 1609-1614
- Sevilla-Lara et al., *Optical flow estimation with channel constancy*, ECCV 2014, LNCS 8689, 423-438
- Revaud et al., *DeepMatching: hierarchical deformable dense matching*, IJCV 120(3), 300-323, 2016
- Revaud et al., *EpicFlow: edge-preserving interpolation of correspondences for optical flow*, CVPR 2015, 1164-1172
- Hu, Y., Song, R. and Li, Y., *Efficient coarse-to-fine PatchMatch for large displacement optical flow*, CVPR 2016, 5704-5712
- Su et al., *Multiple hypothesis flow estimation for video frame interpolation under matching ambiguity*, arXiv 2608.07120, 2026
- Reijalt et al., *On the real-world generalisability of optical flow models*, arXiv 2607.10470, 2026 (the paper that introduces the FlowFactor benchmark)
- Anandan, P., *A computational framework and an algorithm for the measurement of visual motion*, IJCV 2(3), 283-310, 1989
- Battiti, R., Amaldi, E. and Koch, C., *Computing optical flow across multiple scales: an adaptive coarse-to-fine strategy*, IJCV 6(2), 133-145, 1991
- Nam et al., *A fast hierarchical motion vector estimation algorithm using mean pyramid*, IEEE TCSVT 5(4), 344-351, 1995
- Lee et al., *A fast multi-resolution block matching algorithm and its LSI architecture for low bit-rate video coding* (MRMCS), IEEE TCSVT 11(12), 1289-1301, 2001
- Chalidabhongse, J. and Kuo, C.-C. J., *Fast motion vector estimation using multiresolution-spatio-temporal correlations*, IEEE TCSVT 7(3), 477-488, 1997
- Bierling, M., *Displacement estimation by hierarchical blockmatching*, Proc. SPIE 1001, 942-951, 1988
- Rothermel et al., *SURE: photogrammetric surface reconstruction from imagery*, LC3D Workshop, Berlin, 2012
- Pauwels, K. and Van Hulle, M. M., *Realtime phase-based optical flow on the GPU*, CVPR Workshops 2008
- Scarano, F. and Riethmuller, M. L., *Iterative multigrid approach in PIV image processing with discrete window offset*, Exp. Fluids 26(6), 513-523, 1999
- Westerweel, J., Dabiri, D. and Gharib, M., *The effect of a discrete window offset on the accuracy of cross-correlation analysis of digital PIV recordings*, Exp. Fluids 23(1), 20-28, 1997
- Keane, R. D. and Adrian, R. J., *Optimization of particle image velocimeters. I. Double pulsed systems*, Meas. Sci. Technol. 1(11), 1202-1215, 1990
- Thomas, G. A., *Television motion measurement for DATV and other applications*, BBC Research Department Report RD 1987/11, 1987
- Eckstein, A. C., Charonko, J. and Vlachos, P., *Phase correlation processing for DPIV measurements*, Exp. Fluids 45(3), 485-500, 2008
- Stone et al., *A fast direct Fourier-based algorithm for subpixel registration of images*, IEEE TGRS 39(10), 2235-2243, 2001
- Lee, S.-H., Kwon, O. and Park, R.-H., *Motion vector correction based on the pattern-like image analysis*, IEEE TCE 49(3), 479-484, 2003
- Huntley, J. M. and Saldner, H., *Temporal phase-unwrapping algorithm for automated interferogram analysis*, Appl. Opt. 32(17), 3047-3052, 1993
- Schanz, D., Gesemann, S. and Schröder, A., *Shake-The-Box: Lagrangian particle tracking at high particle image densities*, Exp. Fluids 57(5), article 70, 2016
- Ren et al., *A fusion approach for multi-frame optical flow estimation*, WACV 2019, 2077-2086
- Volz et al., *Modeling temporal coherence for optical flow*, ICCV 2011, 1116-1123
- Ramachandran, V. S., Ginsburg, A. P. and Anstis, S. M., *Low spatial frequencies dominate apparent motion*, Perception 12(4), 457-461, 1983
- Ramachandran, V. S. and Cavanagh, P., *Motion capture anisotropy*, Vision Res. 27(1), 97-106, 1987
- Burt, P. and Sperling, G., *Time, distance, and feature trade-offs in visual apparent motion*, Psychol. Rev. 88(2), 171-195, 1981
- Chubb, C. and Sperling, G., *Drift-balanced random stimuli: a general basis for studying non-Fourier motion perception*, JOSA A 5(11), 1986-2007, 1988
- Patents, as cited above: Thomas and Borer (BBC), US4873573A (1986); Samsung, US7555166B2 (2003) and US8223831B2 (2007); Marvell/Synaptics, US9197891B1 (2012)

### Sources (the energy-transfer sweep)

*2026-10-01 note: these are the sources of ["Before the energy-transfer investigations"](#before-the-energy-transfer-investigations-surveyed-2026-09-30) above. The lead-4
survey, filed between them, cites inline; its works are collected in the list just above.*

Conservation laws as truth
- Brown, D., Tracker (Open Source Physics) — https://opensourcephysics.github.io/tracker-website/
- Echiburu Fuenzalida, M. and Fernández Astudillo, N., "Does a Higher Frame Rate Improve the Measurement of g?", arXiv 2609.16243 (2026)
- Martin, T., Frisch, K. and Zwart, J., "Systematic Errors in Video Analysis", Phys. Teach. 58, 195 (2020) ; Stephens, J., Bostjancic, M. and Koskulitz, T., "A Study on Parallax Error in Video Analysis", Phys. Teach. 57, 193 (2019), doi:10.1119/1.5092485
- Webering et al., IEEE ICCE 2021 (scale from a fall's parabola) — https://ieeexplore.ieee.org/document/9427685/
- Thozhiyoor et al., arXiv 2512.02016 (2025): the unit-free two-drop test
- Rozumnyi et al., "Non-Causal Tracking by Deblatting", GCPR 2019, arXiv 1909.06894
- Sciacchitano, A., "Uncertainty quantification in PIV", Meas. Sci. Technol. (2019)
- Shrbený et al., arXiv 2608.28304 (2026): per-row rolling-shutter correction of meteor video

Spin
- Tamaki, T., Sugino, T. and Yamamoto, M., "Measuring ball spin by image registration", FCV 2004 ; Ijiri et al., SIViP 11, 1197 (2017), doi:10.1007/s11760-017-1075-x
- Gossard et al., CVPRW 2024, arXiv 2404.09870 ; Xue et al., arXiv 2606.31760 (2026): spin from one rolling-shutter frame
- Nathan, A. M., "Determining the 3D Spin Axis from Statcast Data" — https://baseball.physics.illinois.edu/trackman/spinaxis.pdf
- Kienzle et al., CVPRW 2025, arXiv 2504.19863
- Koenderink, J. J. and van Doorn, A. J., JOSA 66, 717 (1976)
- Alciatore, D. G., the 90 and 30 degree rules and TP A.4 (the post-contact parabola, ~0.75 s) — https://drdavepoolinfo.com/technical-proof/ ; Mathavan, S., Jackson, M. R. and Parkin, R. M., Am. J. Phys. 77, 788 (2009)

Impacts
- Owens, N., Harris, C. and Stennett, C., "Hawk-Eye tennis system", VIE 2003, doi:10.1049/cp:20030517 ; ITF Technical Centre (International Tennis Federation), Electronic Line-Calling evaluation, rev. 26 (2020)
- Collins, H. and Evans, R., Public Underst. Sci. (2008) ; Whitney et al., Curr. Biol. (2008), doi:10.1016/j.cub.2008.08.021
- Rozumnyi et al., "Tracking by Deblatting", IJCV (2021), doi:10.1007/s11263-021-01480-w ; DeFMO (Rozumnyi et al., CVPR 2021)
- Sun, W. and Qiu, L., FBDepth, arXiv 2207.03074
- Shechtman, E., Caspi, Y. and Irani, M., "Space-Time Super-Resolution", TPAMI 27, 531 (2005)
- Xu et al., "Quadratic Video Interpolation", NeurIPS 2019 (already in the first survey)
- Scholl, B. J. and Tremoulet, P. D., TICS 4, 299 (2000) ; CLEVRER (Yi et al., ICLR 2020) ; Physion (Bear et al., NeurIPS 2021) ; Galileo (Wu et al., NeurIPS 2015)

Held objects
- Kellman, P. J. and Spelke, E. S., Cogn. Psychol. 15, 483 (1983) ; Brox, T. and Malik, J., ECCV 2010 ; Tangemann, M., Kümmerer, M. and Bethge, M., NeurIPS 2024, arXiv 2411.01505
- Shan et al., CVPR 2020 ; EPIC-KITCHENS VISOR (Darkhalil et al., NeurIPS 2022) ; EgoHOS (Zhang et al., ECCV 2022)
- Fortmann, T., Bar-Shalom, Y. and Scheffe, M., IEEE J. Ocean. Eng. 8, 173 (1983) ; Kropfreiter et al., arXiv 2308.06326

Sub-pixel and sub-frame
- Wadhwa et al., "Motion microscopy for visualizing and quantifying small motions", PNAS 114, 11639 (2017), doi:10.1073/pnas.1703715114
- Zhang, Y., Pintea, S. L. and van Gemert, J. C., "Video Acceleration Magnification", CVPR 2017, arXiv 1704.04186
- Hinch, E. J. and Saint-Jean, S., Proc. R. Soc. A 455, 3201 (1999) ; Cross, R. and Gauld, C., Phys. Educ. 56, 025002 (2021) ; Pal, S. K., Panchadhyayee, P. and Sarkar, S., Phys. Teach. 64, 72 (2026)
- Šmíd, M. and Matas, J., VISAPP 2017, arXiv 1902.11084

Cosmography
- Blandford et al., "Cosmokinetics", arXiv astro-ph/0408279 ; Rodrigues, G., de Souza, R. and Alcaniz, J., arXiv 2506.22373 (model-independent j0 with DESI DR2: consistent with 1 alone, 3.4-5.4 sigma from 1 with supernova catalogues) ; Worsley, J., Chakraborty, S. and Dunsby, P., arXiv 2607.20348 (model-based fits with Planck hold j0 ~ 1)

Rigid and affine motion (2.5)
- Li et al., "An Efficient Four-Parameter Affine Motion Model for Video Coding", IEEE TCSVT 28(8), 1934-1948 (2018), dblp journals/tcsv/LiLLLYLCW18
- Ng et al., "Block-Matching Translational and Rotational Motion Compensated Prediction Using Interpolated Reference Frame", EURASIP J. Adv. Signal Process. (2010), doi 10.1155/2010/385631

## Before lead 2: the impact mode as a shader, one source per pixel chosen by the side of tau (surveyed 2026-10-01, 04:05, by a research subagent; read and checked before it was filed)

Scope: the per-pixel / per-block shader form of the impact placer. PRIOR-ART.md's energy-transfer survey (09-30)
already holds Hawk-Eye/ITF, Tracking by Deblatting, FBDepth, Michotte's ~60-70 ms and 3DRS; they are cited by pointer
only. Every citation below was checked by web search tonight. "(abstract)" means only the abstract or a summary was
read; "(claims summary)" means a patent read through its Google Patents record; UNVERIFIED means not confirmed.

### Summary

No product or paper found places an impact time inside a source interval and switches the source there, but every
part exists. A 1990 BBC patent already decides per pixel, from four fields t-1..t+2, which source PAIR a trial vector
fits (three two-field errors), then extrapolates one-sided from t or from t+1: that is the impact placer's structure,
with a region switch where we need a time switch. TV chips add cheap safety nets (median protectors, the output phase
pulled toward the nearest frame, frame repeat). Academic non-linear interpolation fits smooth polynomials; one paper
names "sudden jerks" as where the quadratic fails, and none models a kink. Our own algebra (checked in exact
fractions) gives the sharpest finding: **from four frames a rigid bounce at mid-interval is exactly a parabola**. The
four-frame jerk is zero there, so a jerk trigger is blind exactly where the error is largest; QVI or a cubic draws the
body at v/8 of its excursion, a two-frame interpolator at 0 (d(0) = 0), the truth is v/2. Wrongly applying the kink to
a true smooth turn costs the mirror error (3a/8), so four frames cannot decide; **a fifth sample (k-2, which the carry
holds) can**: a bounce has zero acceleration before the interval, a parabola does not. Statistics supplies robust,
soft triggers (jump-preserving regression, WENO stencil weights, the ICI rule, maneuver detection). Perception: a
33 ms dwell already weakens Michotte's launching and raises "sticking"; nothing was found on interpolation artefacts
at collisions as such.

### 1. Hardware MEMC and patents

- **BBC, US 6,005,639 (Thomas & Burl; priority 1990, granted 1999)** (claims summary). Four fields t-1, t, t+1, t+2.
  For each trial vector, three two-field errors E0, E1, E2 (pairs t-1/t, t/t+1, t+1/t+2) are weighted into classes:
  low everywhere = foreground (four-field interpolation); low only in the first pair = obscured (extrapolate from t);
  low only in the last pair = revealed (extrapolate from t+1); none low = a non-adaptive four-tap filter. Weights
  favour foreground at edges. **Transfer:** an impact is a body whose vL fits E0 and whose vR fits E2 while neither
  fits E1 straight. The class supplies the trigger and the confidence; sign(t - tau) picks the side. Cost per
  candidate: 3 pair errors, cheap at 8x8 blocks.
- **Philips/NXP.** Ojo & de Haan (1997): vector reliability steers the filtering. US 6,385,245 (de Haan et al.) (claims
  summary): a three-tap median of the two MC pixels and the non-MC average. US 5,929,919 (de Haan & Biezen): graceful
  degradation by scaling vectors alternately above and below the trajectory, trading irregular errors for regular
  judder. Occlusion: a tritemporal estimator plus a vector retimer (Mertens & de Haan, SPIE 4310, 2001; van Gurp,
  US 2009/0251612, abandoned). Piek, US 8,373,796 (claims summary): covering vs uncovering from the RELATIVE forward
  and backward match errors over n-2, n-1, n. **Transfer:** the relative error is the cheap side test; the median is
  a 3-fetch safety net.
- **Others with one-sided modes.** STMicro US 8,576,341: one-sided compensation in reveal/conceal regions, median
  elsewhere, and a fade control between them. ASTRI US 9,148,622: hybrid uni-/bi-directional vectors from three
  frames. Intel US 8,472,524: a five-tap median "protector" returns an original pixel when the MC values disagree.
- **Retreat toward the nearest frame.** Imagination US 8,953,687 (claims summary): when estimation is poor, the working
  time instance moves toward the nearest input frame, globally or per block (maximum distance 0.5 -> 0.25 of a
  period). Google US 9,300,906: repeat an input frame when motion smoothness is low. Pixelworks US 9,552,623: TprDiff,
  a block's vector difference between consecutive frames, lowers MEMC strength ("random motions"). TprDiff is the
  industry's jerk-like statistic, and it is used only to back off, never to model.
- **Acceleration.** Qualcomm US 2006/0017843 (abandoned): constant-acceleration extrapolation from the current vector
  and the reversed previous one; no reversal handling.
- **Not found:** any patent that estimates an impact time inside the interval and switches source there (a search
  result, not proof of absence).

### 2. Non-linear-motion interpolation

- **QVI** (Xu et al., NeurIPS 2019): quadratic flow from frames -1, 0, 1 (and 0, 1, 2). **EQVI** (Liu et al., ECCV-W
  2020): least-squares rectified. **All at Once** (Chi et al., ECCV 2020): "cubic-based". Smooth polynomials only.
- **Dutta, Subramaniam & Mittal (CVPRW 2022).** Four input frames; per-pixel flow alpha*t + beta*t^2 with alpha and
  beta from a 3-D CNN, to "softly switch between a linear and a quadratic model". They state that a quadratic "can
  also be inaccurate, especially in the case of motion discontinuities over time (i.e. sudden jerks)". The only
  per-pixel model selection found; it has no piecewise-linear member and shows no reversal cases.
- **BiM-VFI** (Seo, Oh & Kim, CVPR 2025) (abstract) lists "changing directions" among the non-uniform motions that
  blur; a learned motion map conditions the flow. **Zhong et al.** (ECCV 2024): velocity ambiguity, distance indexing.
  Learned, two-frame: principle only.
- **At a reversal (our algebra, checked tonight in exact fractions at tau = 1/4, 1/2, 3/4).** A bounce at tau = 0.5 gives positions -v, 0, 0, -v at
  k-1..k+2. Four points fit a parabola exactly (acceleration -v per frame^2). The four-frame jerk
  d(+1) - 2d(0) + d(-1) = -2v(2tau - 1) vanishes at mid-interval. At t = 0.5, QVI and the cubic draw v/8, two-frame
  linear draws 0, truth is v/2: a 3v/8 shortfall, and the fitted acceleration is v. The reverse error (the kink
  applied to a true smooth turn of acceleration a) is a 3a/8 overshoot. So four frames give two exact hypotheses of
  mirror cost; a prior or a fifth sample decides. With k-2: bounce d(-1) - d(-2) = 0; parabola = a.

### 3. One-sided synthesis per pixel

- **Super SloMo** (Jiang et al., CVPR 2018): learned soft visibility maps weight the two warped frames. **DAIN** (Bao
  et al., CVPR 2019): depth-aware flow projection, nearer wins. Both learned and soft: they cross-fade.
- **Softmax splatting** (Niklaus & Liu, CVPR 2020): forward splat weighted by exp(Z), Z = alpha x brightness-constancy
  error (alpha learned); large |alpha| tends to a z-buffer pick. **Splatting-based synthesis** (Niklaus, Hu & Chen, WACV 2023)
  (abstract): splatting alone, much faster for multi-frame output. **Transfer:** splatting solves the retiming problem.
  The impact record (vL, vR, tau, confidence) must sit where the body IS at t, at x_k + vL*min(t, tau) +
  vR*max(0, t - tau), not where it was at k. A compute pass over flagged cells only (~0.2%) can splat it with an
  atomic-min key on the residual.
- **TI US 2009/0174812** (abandoned): the sign of the flow divergence picks the source frame per pixel (a hard switch).
- **Which serves "own side of tau":** the BBC/Piek pair test (does each side's vector fit its own clear pair?) for
  trigger and confidence, then sign(t - tau): one comparison and one fetch per pixel once the record is splatted.
- **Stability.** The sources use soft fades (STMicro), continuous phase scaling (Imagination), medians (Philips) and
  foreground bias (BBC). The step at tau is meant to be a step in time. Flicker comes from the trigger toggling
  between intervals or neighbouring cells, so pool tau over the body (FBDepth pools over the object), add hysteresis,
  and use continuous weights (section 4).

### 4. Detecting the event in a dense field

- **It is a jump, not a kink.** In the displacement series d(n) (velocity per frame), the reversal is a jump, so
  jump-preserving regression applies directly. McDonald & Owen (1986): left, right and centred linear fits, weighted
  by fit quality. Gijbels, Lambert & Qiu (2007) (abstract): choose among left, right and two-sided local linear fits
  by their weighted residual mean squares. Needs two or more samples per side (six frames, or the carry).
- **ENO/WENO** (Harten et al. 1987; Jiang & Shu 1996). Choose (ENO) or weight (WENO) the stencil with the smallest
  smoothness indicator, so a derivative near a discontinuity uses the one-sided stencil automatically and the weights
  vary continuously. **This is the one-sided derivative mode as an established construction.** Cost: a few
  multiply-adds on displacements already fetched.
- **ICI rule** (Katkovnik, Egiazarian & Astola 2002): widen a window only while confidence intervals intersect.
  **Transfer:** replace a raw jerk threshold with |vL - vR| > Gamma*(sigmaL + sigmaR), sigma from each pair's match
  quality: a normalised test against the field's truncation noise.
- **Maneuver detection** (Li & Jilkov, Parts IV-V) (abstract) and **IMM** (Blom & Bar-Shalom 1988): declare a
  maneuver when the innovation against the constant-velocity prediction is large; IMM carries per-model probabilities. **Transfer:**
  with the carry, predict d(+1) from d(-2), d(-1) and test the innovation; a per-cell model probability persisted by
  the carry is the soft weight.
- **Pathological motion** (Corrigan, Harte & Kokaram 2008): five frames, not three, to tell an impulsive temporal
  profile from a quasi-periodic one. The same lesson: the window must exceed the stencil by one.
- **Black & Anandan (CVPR 1991):** a robust temporal-continuity constraint; abrupt motion changes become outliers.
  **Transfer:** gate the carry and any temporal candidate at flagged cells, or they carry vL across the reversal.
- **l1 trend filtering** (Kim et al. 2009): a piecewise-linear trend whose kinks are events, the exact bounce model;
  an iterative solver, so offline. CUSUM (Page 1954) and BOCPD (Adams & MacKay 2007) accumulate evidence over long
  series.

### 5. Perception

- **White (2025)**, a registered replication of Michotte on a 60 Hz display: a 33.3 ms delay was rated significantly
  lower on launching and higher on "sticking" than 0 or 16.7 ms; Michotte reported launching reduced at 70 ms and
  absent at 154 ms. Inference (ours): a two-frame interpolator turns a mid-interval bounce into a 42 ms dwell short
  of the wall, above that threshold.
- **Eagleman & Sejnowski (2000):** the position seen at an instant depends on about 80 ms of what follows. Inference:
  viewers judge the trajectory over about two 24 fps frames, so the shortfall at the apex is probably the salient
  error, more than per-pixel ghosting.
- **Suchow & Alvarez (2011):** motion silences awareness of change on moving objects. Inference: blend artefacts on a
  fast body are partly masked, less so at a hand's turn where speed passes through zero.
- **BVI-VFI** (Danier, Zhang & Bull 2023): frame repeat and averaging can beat deep VFI on rapid irregular motion.
  Supports a nearest-frame fallback as perceptually safe.
- Nothing was found on interpolation artefacts at collisions specifically.

### What to try first, ranked

1. **The four-field pair test per 8x8 cell, with a time switch.** Flag a cell when the normal component of d(-1) and
   d(+1) changes sign and each side's vector fits its own clear pair; tau = (d0 - vR)/(vL - vR) along the normal,
   kept only inside (0, 1). Splat the record to output time; the gather draws from k at x - vL*t if t < tau, else from
   k+1 at x + vR*(1 - t). **Cost:** one sparse compute pass over cells (3 vector fetches each), then one record fetch
   plus one one-sided fetch per pixel, fewer than the two-sided blend. **Risk:** false triggers at smooth turns (3a/8
   overshoot), holes behind the body (fill one-sided from the background vector, as occlusion handling does).
2. **The fifth sample from the carry.** Test d(-1) - d(-2) (from the carry): near zero means impulse (kink), near the
   current acceleration means parabola. **Cost:** one carried value per cell. **Risk:** the carried value is itself an
   estimate; an impact in the previous interval contaminates it.
3. **A normalised, soft trigger.** ICI-style |vL - vR| against the pair errors, WENO-like weights between the
   two-sided and one-sided estimates, and hysteresis across intervals. Blend the two TRAJECTORIES (a position), never
   the two pixels; when undecided the mid trajectory halves the worst error at mid-interval (3a/16). **Cost:** arithmetic. **Risk:** a
   blended position drawn from both sides can ghost again; keep the source one-sided.
4. **A fallback when the model fails its own check** (tau outside (0, 1), or a high match error at the one-sided
   fetch): pull the phase toward the nearest frame for that block (Imagination) or take a 3-tap median (Philips).
   **Cost:** trivial. **Risk:** local judder.
5. **Gate the carry at flagged cells** (Black & Anandan). **Cost:** one branch. **Risk:** low.

*2026-10-01: none was built; the impact mode was parked for the player
([ENERGY-TRANSFER.md, "The owner's two decisions"](ENERGY-TRANSFER.md#the-owners-two-decisions-2026-10-01-morning-and-the-tiers-costs)).*

### Not to import

- **Higher-order polynomials at impacts** (QVI, EQVI, cubic): from four frames they fit the bounce exactly, cannot flag
  it, and draw a quarter of the excursion.
- **Learned visibility, BiM, distance indexing:** networks; their fusion is still a cross-fade.
- **Frame-wide retreat** (Google's frame repeat, Pixelworks' strength back-off): judder on 99.8% of cells to fix 0.2%.
- **Alternating vector scaling** (US 5,929,919): manufactures judder; it is for failed estimation, not known motion.
- **BOCPD, CUSUM, l1 trend filtering in the shader:** sequential or iterative. l1 trend filtering is fine offline, as
  a labeller for real footage.
- **Depth-ordered splatting** (DAIN): needs depth we do not have.

### Sources

Patents (Google Patents records read 2026-10-01):
- US 6,005,639, Thomas & Burl (BBC), "Vector assignment for video image motion compensation" — https://patents.google.com/patent/US6005639A/en
- US 5,929,919, de Haan & Biezen (Philips), "Motion-compensated field rate conversion" — https://patents.google.com/patent/US5929919A/en
- US 6,385,245, de Haan, Schutten & Pelagotti (Philips) — https://patents.google.com/patent/US6385245B1/en
- US 8,373,796, Piek (NXP; now Dynamic Data Technologies), "Detecting occlusion" — https://patents.google.com/patent/US20120033130A1/en
- US 2009/0251612, van Gurp (NXP), "Motion vector field retimer" (abandoned) — https://patents.google.com/patent/US20090251612A1/en
- US 8,576,341, Petrides (STMicroelectronics) — https://patents.google.com/patent/US8576341B2/en
- US 9,148,622, Liu et al. (ASTRI) — https://patents.google.com/patent/US9148622B2/en
- US 8,472,524, Lu (Intel) — https://patents.google.com/patent/US8472524B2/en
- US 8,953,687, Morphet & Fishwick (Imagination), "Video interpolation" — https://patents.google.com/patent/US8953687B2/en
- US 9,300,906, Kokaram, Kelly & Crawford (Google), "Pull frame interpolation" — https://patents.google.com/patent/US9300906B2/en
- US 9,552,623, Cheng et al. (Pixelworks), "Variable frame rate interpolation" — https://patents.google.com/patent/US9552623B1/en
- US 2009/0174812, Hong (TI) (abandoned) — https://patents.google.com/patent/US20090174812A1/en
- US 2006/0017843, Shi & Raveendran (Qualcomm) (abandoned) — https://patents.google.com/patent/US20060017843A1/en

TV papers:
- Ojo, O. A. and de Haan, G., "Robust motion-compensated video upconversion", IEEE TCE 43(4):1045-1056, 1997 — doi:10.1109/30.642370
- Mertens, M. J. W. and de Haan, G., "Motion vector field improvement for picture rate conversion with reduced halo", Proc. SPIE 4310:352-362, 2001 — doi:10.1117/12.411812

Interpolation:
- Xu et al., "Quadratic video interpolation", NeurIPS 2019 — https://arxiv.org/abs/1911.00627
- Liu et al., "Enhanced quadratic video interpolation", ECCV-W 2020 — https://arxiv.org/abs/2009.04642 ; doi:10.1007/978-3-030-66823-5_3
- Chi et al., "All at once: temporally adaptive multi-frame interpolation with advanced motion modeling", ECCV 2020 — https://arxiv.org/abs/2007.11762 ; doi:10.1007/978-3-030-58583-9_7
- Dutta, S., Subramaniam, A. and Mittal, A., "Non-linear motion estimation for video frame interpolation using space-time convolutions", CVPRW (CLIC) 2022 — https://arxiv.org/abs/2201.11407 (quotes read at ar5iv)
- Seo, W., Oh, J. and Kim, M., "BiM-VFI", CVPR 2025 — https://arxiv.org/abs/2412.11365
- Zhong et al., "Clearer frames, anytime: resolving velocity ambiguity in video frame interpolation", ECCV 2024 (arXiv retitled "Velocity disambiguation for video frame interpolation") — https://arxiv.org/abs/2311.08007
- Jiang et al., "Super SloMo", CVPR 2018 — https://arxiv.org/abs/1712.00080
- Bao et al., "Depth-aware video frame interpolation", CVPR 2019 — https://arxiv.org/abs/1904.00830
- Niklaus, S. and Liu, F., "Softmax splatting for video frame interpolation", CVPR 2020 — https://arxiv.org/abs/2003.05534
- Niklaus, S., Hu, P. and Chen, J., "Splatting-based synthesis for video frame interpolation", WACV 2023 — https://arxiv.org/abs/2201.10075

Detection and statistics:
- McDonald, J. A. and Owen, A. B., "Smoothing with split linear fits", Technometrics 28:195-208, 1986 — https://www.semanticscholar.org/paper/2a5ae7d06748fdfd373c1222aa8244f035fd74e6
- Gijbels, I., Lambert, A. and Qiu, P., "Jump-preserving regression and smoothing using local linear fitting: a compromise", Ann. Inst. Stat. Math. 59:235-272, 2007 — doi:10.1007/s10463-006-0045-9
- Harten et al., "Uniformly high order accurate essentially non-oscillatory schemes, III", J. Comput. Phys. 71:231-303, 1987 — https://ntrs.nasa.gov/citations/19870062149
- Jiang, G.-S. and Shu, C.-W., "Efficient implementation of weighted ENO schemes", J. Comput. Phys. 126:202-228, 1996 — https://www.sciencedirect.com/science/article/abs/pii/S0021999196901308
- Katkovnik, V., Egiazarian, K. and Astola, J., "Adaptive window size image de-noising based on intersection of confidence intervals (ICI) rule", JMIV 16:223-235, 2002 — doi:10.1023/A:1020329726980
- Li, X. R. and Jilkov, V. P., "A survey of maneuvering target tracking, Part IV: decision-based methods", Proc. SPIE 4728, 2002 — https://www.semanticscholar.org/paper/f27fb881ee7b5f1b443028b87b01b43a2a330e1b ; "Part V: multiple-model methods", IEEE TAES 41(4):1255-1321, 2005 — doi:10.1109/TAES.2005.1561886
- Blom, H. A. P. and Bar-Shalom, Y., "The interacting multiple model algorithm for systems with Markovian switching coefficients", IEEE TAC 33(8):780-783, 1988 — doi:10.1109/9.1299
- Corrigan, D., Harte, N. and Kokaram, A., "Pathological motion detection for robust missing data treatment", EURASIP J. Adv. Signal Process. 2008 — doi:10.1155/2008/542436
- Black, M. J. and Anandan, P., "Robust dynamic motion estimation over time", CVPR 1991, pp. 296-302 — https://dblp.uni-trier.de/rec/html/conf/cvpr/BlackA91 (DOI UNVERIFIED; "temporal continuity" quote from https://cs.brown.edu/people/mjblack/Thesis/thesis.html)
- Kim et al., "l1 trend filtering", SIAM Review 51(2):339-360, 2009 — https://web.stanford.edu/~boyd/papers/l1_trend_filter.html
- Page, E. S., "Continuous inspection schemes", Biometrika 41:100-114, 1954 — https://www.semanticscholar.org/paper/ae3c60cf4066589d91256d52c6f568665f70568e
- Adams, R. P. and MacKay, D. J. C., "Bayesian online changepoint detection", 2007 — https://arxiv.org/abs/0710.3742

Perception:
- White, P., "Michotte's research on perceptual impressions of causality: a registered replication study", R. Soc. Open Sci. 12(9):250244, 2025 — doi:10.1098/rsos.250244 (the 33.3 ms result via search snippet; the full results section was not reachable)
- Eagleman, D. M. and Sejnowski, T. J., "Motion integration and postdiction in visual awareness", Science 287:2036-2038, 2000 — https://science.sciencemag.org/content/287/5460/2036.abstract
- Suchow, J. W. and Alvarez, G. A., "Motion silences awareness of visual change", Current Biology 21(2):140-143, 2011 — https://scholar.harvard.edu/alvarez/publications/motion-silences-awareness-visual-change
- Danier, D., Zhang, F. and Bull, D. R., "BVI-VFI: a video quality database for video frame interpolation", IEEE TIP 32:6004-6019, 2023 — doi:10.1109/TIP.2023.3327912 ; finding quoted from https://github.com/danier97/BVI-VFI-database

By pointer (PRIOR-ART.md): de Haan et al. 3DRS (1993); FBDepth (Sun, W. and Qiu, L., arXiv 2207.03074); Tracking by
Deblatting (Rozumnyi et al., IJCV 2021); Hawk-Eye/ITF. Seen only through citing works, not cited above: de Haan et al.,
"Graceful degradation in motion-compensated field-rate conversion" (HDTV Workshop 1993); Wittebrood, R. B., de Haan, G. and Lodder, R.,
"Tackling occlusion in scan rate conversion systems" (ICCE 2003).

**Checked on filing:** the algebra was re-derived independently (positions -v, 0, v(2 tau - 1), v(2 tau - 2); the third difference -2v(2 tau - 1), zero at tau = 1/2; the parabola through the four samples draws v/8 at t = 1/2). Three citations were re-read at their sources: US 6,005,639 (four fields, three pair errors, obscured regions from preceding fields only, revealed from following); US 8,953,687 (the working time instance shifted toward the nearest input frame, globally or per block); Dutta et al. (CVPRW 2022, soft switching between linear and quadratic models; its abstract does not state the four input frames, which the survey read in the paper's text).

## Before rung 2's leap: periodic columns of Rule 30 (surveyed 2026-10-04, 23:15, by Cloud)

Scope: what is known about a column of a finite Rule 30 configuration being eventually periodic, and especially
about period two, before PRIZE-PROBLEMS.md §8.2's next step (naming the templates). Sources were checked tonight by
web search and by reading them. "(abstract)" means only an abstract or a summary was read.

### Summary

Period one is closed (Condrey, 2026-09-08). Period two is open and is being worked on in public: a bounded search
like our rung 1, and the same "remaining inference" as our Conjecture B in its weak form. Two of this project's results
were already known: the forced left half (Condrey's "triangular uniqueness", by left-permutivity) and the fact that
no constant bound governs period two. Our two-sided measurements, the four arms, Lemmas 3 and 4 and the templates
were not found in any source. The new import is Rowland's "local restart", which is the first concrete hypothesis
for what a template is.

### Core field

- **Condrey, "Finite Configurations Cannot Generate a Constant Trace in Rule 30"**, arXiv:2609.09431 (2026-09-08).
  - For each right half, a unique left half gives a constant centre trace. For trace 0 it is an alternating tail
    after the right half's first one; for trace 1 it is one universal checkerboard. Both are infinite, so no finite
    configuration has an eventually constant column.
  - The tool is Lemma 1, "triangular uniqueness", by left-permutivity. It is the same forced left half as our
    `rule30_periodic.py`. Lean proofs ship with the paper.
  - Conclusion, quoted: "The next unresolved case is eventual period two ... At p=2 no bounded law can exist ...
    H(2,w) ≥ w for every w ... a structural account of period-two exclusion remains open."
  - $H(p, w)$ is the longest $p$-periodic prefix of the trace over rows of support radius $w$. That differs from
    our X3 statistic (zero runs of the infinite forced left half, for a finite right half), but it is the same kind
    of fact: no constant bound.
- **Public period-two work**, GitHub woahwhattheheck/commons, issue 15314 and PR 15318 (read 2026-10-04).
  - A "bounded fiber engine" for support radius 1 to 14 examined 65,532 candidates. All escape, and the longest
    horizon is 19.
  - It states "period_two_infinite_theorem=false". Its named next inference is "every eventually-zero positive right
    half forces completion obstruction or infinitely many ones in the alternating trace". That is our Conjecture B in
    its weak form.
  - Our rung 1 (right halves up to 18 cells, left half forced to depth 256, 27,262,976 cases) covers more. The
    issue quotes Jen as "a finite Rule 30 orbit has at most one eventually periodic column".
- **Jen, E., "Aperiodicity in one-dimensional cellular automata"**, Physica D 45:3-18 (1990) (summary via MathWorld
  and a search snippet; the scan at OSTI was not read).
  - From a single black cell, the sequence attained by any two adjacent cells is not periodic.
  - Rule 30's right diagonals are periodic with periods $2^\alpha$.
  - The commons issue's stronger phrasing, "at most one eventually periodic column", is UNVERIFIED against the paper.
    PRIZE-PROBLEMS.md §5 keeps the weaker, adjacent-columns form.
- **Rowland, E. S., "Local nested structure in rule 30"**, Complex Systems 16(3) (read, pages 1 to 4).
  - At row $2^n$ a region of the initial condition reappears on the right side, and the automaton "begins again"
    locally. This follows from left bijectivity (our left-permutivity) and from the right diagonals' periods
    $2^\alpha$.
  - The diagonal periods are characterised by $a(n)$ = 1, 3, 4, 6, 7, 9, 15, 16, 24, ... (no known fast formula).
  - The left diagonals are only eventually periodic. Their period doubling is proved in §5.
- **"Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical Computer
  Science (2022), ScienceDirect pii S0304397522007502: the page refused access (403). UNVERIFIED and not read;
  listed so it is not forgotten.

### What to import, ranked

1. **Rowland's restart as the hypothesis for a template.** With column 0 clamped, every diagonal that starts at
   position 1 or more at time 0 never meets column 0 (each diagonal is computed from the two on its right). So that
   wedge is ordinary Rule 30 with its power-of-2 periods, and only the region between it and column 0 is driven by the
   trace. A long two-sided run may be the left side's echo of a local restart. Test: whether column 1, or the long
   runs, recur at times related to powers of 2.
2. **Octaves as the owner's "harmonics".** Period doubling is a harmonic series in octaves: diagonal $k$ from the
   edge repeats every $2^{\alpha(k)}$ steps. The run lengths' steps of 2 (§8.2) are the trace's own period, so two
   kinds of "harmonic" are on the table: multiples of $p$ (from column 0) and powers of 2 (from the right side). The
   probe for §8.3 separates them.
3. **Lean, as Condrey did.** Not yet: there is no theorem to formalise.

### Not to import

- Condrey's explicit fibres. For period two the forced left half is aperiodic (`rule30_rings.py`: 1,999 of 2,048
  right halves show no period up to 128), and Condrey's conclusion says no bounded law exists there either.
- Condrey's support-radius horizon $H(p, w)$, as the target statistic. It grows trivially, by truncation, so it
  cannot separate a proof route from a dead end.

### Sources

- Condrey, D. L., arXiv:2609.09431 — https://arxiv.org/abs/2609.09431 (abstract, conclusion and Lemma 1 read via
  the HTML version)
- woahwhattheheck/commons issue 15314 — https://github.com/woahwhattheheck/commons/issues/15314 ; PR 15318 —
  https://github.com/woahwhattheheck/commons/pull/15318 (claims summary)
- Jen, E., Physica D 45:3-18, 1990 — summary at https://mathworld.wolfram.com/Rule30.html ; scan at
  https://www.osti.gov/servlets/purl/7230855 (not read)
- Rowland, E. S., "Local nested structure in rule 30", Complex Systems 16(3) —
  https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf
- "Rapid left expansivity ..." — https://www.sciencedirect.com/science/article/pii/S0304397522007502 (403; not read)

## Before the particle step: domains and particles (surveyed 2026-10-05, by Cloud)

Scope: the slips of the wheel (PRIZE-PROBLEMS.md section 8.7) turned out to be defects of a domain that travel as
particles. That is the subject of computational mechanics.

- **Hanson, J. E. and Crutchfield, J. P., "Computational mechanics of cellular automata: an example"**, Physica D
  103:169-189 (1997) (abstract and summary read). On elementary rule 54 they identify the dominant regular domain,
  construct a domain filter that locates and classifies defects, and identify the primary particles, their
  interactions, and the equation of motion of the filtered spacetime. **Import:** the domain filter (our
  departure-from-D pattern is one, with the wheel as the domain) and their particle-interaction catalogue, as the
  method for part 3 of the route (how trains of particles move the wheel's phase).
- Sources: https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf ;
  https://www.semanticscholar.org/paper/Computational-mechanics-of-cellular-automata:-an-Hanson-Crutchfield/036e7cb40ee06918aa47da9163ee866b9f316e4a
