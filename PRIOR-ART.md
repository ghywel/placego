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
about period two, before RULE30-PRIZE.md §8.2's next step (naming the templates). Sources were checked tonight by
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
    RULE30-PRIZE.md §5 keeps the weaker, adjacent-columns form.
  - (Added 2026-10-05.) Kopra's Corollary 3.7 states the adjacent-columns form for every configuration with an
    eventually zero left half, not only the single seed. It decides conjecture LR for every eventually periodic
    column 1 (RULE30-PRIZE.md §8.13), which this entry should have prompted before §8.6's search was designed.
- **Rowland, E. S., "Local nested structure in rule 30"**, Complex Systems 16(3) (read, pages 1 to 4; §5, pages 15
  to 17, read 2026-10-05 after rule30_diagonals.py and rule30_leftband.py had run: see the entry at the end).
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

Scope: the slips of the wheel (RULE30-PRIZE.md section 8.7) turned out to be defects of a domain that travel as
particles. That is the subject of computational mechanics.

- **Hanson, J. E. and Crutchfield, J. P., "Computational mechanics of cellular automata: an example"**, Physica D
  103:169-189 (1997) (abstract and summary read). On elementary rule 54 they identify the dominant regular domain,
  construct a domain filter that locates and classifies defects, and identify the primary particles, their
  interactions, and the equation of motion of the filtered spacetime. **Import:** the domain filter (our
  departure-from-D pattern is one, with the wheel as the domain) and their particle-interaction catalogue, as the
  method for part 3 of the route (how trains of particles move the wheel's phase).
- Sources: https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf ;
  https://www.semanticscholar.org/paper/Computational-mechanics-of-cellular-automata:-an-Hanson-Crutchfield/036e7cb40ee06918aa47da9163ee866b9f316e4a

## Before the kick-game step: the wheel, phase locking, and recent Rule 30 work (surveyed 2026-10-05, by Cloud)

Scope: is the wheel of RULE30-PRIZE.md sections 8.5 to 8.8 (a 17/56 rotation next to a column clamped to 0101...,
kicked in notches by domain walls) already known, and what mathematics is closest? Checked tonight by search and by
reading abstracts; "(abstract)" means no more than that was read.

### Summary

Nothing found describes the wheel, its walls, or its notched kicks. The closest results are about columns and
diagonals of the single-seed pattern, and about two adjacent periodic columns, which is exactly the gap our two-sided
analysis sits in. The closest mathematics for "a wheel at a rational rotation number, with phase slips" is mode
locking (Arnold tongues).

### Sources and what to import

- **Kopra, J., "Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical
  Computer Science 946 (2023) 113668, open access (read in full 2026-10-05; the first version of this entry, from a
  search summary, said "width w - 1", which was wrong).
  - **Definitions.** A rule is *left expansive with dimensions (h, d, w)* (Def. 3.1) when the contents of any
    h + d by w rectangle of a space-time diagram fix the cell just left of its top row. An (m, n) left-permutive rule
    is left expansive with dimensions (0, 1, m + n), so Rule 30 has (0, 1, 2). It is *left spreading* (Def. 3.3) when
    the leftmost 1 of a configuration whose left half is eventually zero moves left; for an elementary rule that means
    001 maps to 1, at speed 1. It is *rapidly left expansive* (Def. 3.4) when the speed is below 1/h, which always
    holds when h = 0.
  - **Lemma 3.2.** If a trace of width w is eventually p-periodic, so is the one a column to its left (the preperiod
    grows by h). **Theorem 3.5.** For a rapidly left expansive rule of width w and any configuration whose left half
    is eventually zero, no trace of width w is eventually periodic. **Corollary 3.7** is Jen's theorem (Physica D
    1990, Proposition 3): for a left-permutive, left-spreading elementary rule, no two adjacent columns are both
    eventually periodic. The proof covers every configuration with an eventually zero left half, not only the single
    seed.
  - **Page 7.** The single column (Problem 3.10, Wolfram's Problem 1) "is probably equally difficult for all
    configurations" with an eventually zero left half. The class cannot settle it, because it contains Rule 90, which
    from a single 1 has an eventually periodic single column.
  - **Section 4.** Theorem 4.5 and Corollary 4.6: the right half of a configuration whose left half is eventually zero
    returns exactly to its start only finitely often. Corollary 4.9: the sequence of right halves has infinitely many
    limit points. These generalise Pisot's and Dubickas' results on the fractional parts of $\xi (p/q)^n$; Theorem 4.7
    generalises Morse and Hedlund.
  - **Imported (RULE30-PRIZE.md §8.13).** Jen's theorem decides conjecture LR for every eventually periodic column
    1, so §8.6's periodic-column search and job M2 had a known answer. Its proof is our left recursion (Lemma 3.2 with
    h = 0) plus the light cone. The work had cited Jen in §5 without applying it, which is a failure of method,
    recorded. A consequence: in a finite configuration with column 0 eventually 0101..., column 1 is never eventually
    periodic, so the wheel slips for ever. Our Lemma 4, which uses Rule 30's OR and which Rule 90 lacks, is outside
    Kopra's class. That is consistent with his page-7 remark that the single column needs more than the class gives.
- **Nersissian, T., "Diagonal Periods and Newton Supports of Rules 30, 86 and 135"**, arXiv:2609.25077 (2026-09-18)
  (abstract). The single-seed Rule 30 cone has unbounded least diagonal periods in both directions, at least
  floor(m/2) + 1 at depth m, with a polynomial lift that connects to Fibonacci sequences. For Rule 86 there is a
  "backward map on periodic tail profiles". **To read:** whether that backward map is our pair map F of section 8.6
  in mirror image.
- **Chan-Lopez, E. and Martin-Ruiz, A., "Symmetric Nonlinear Cellular Automata as Algebraic References for Rule
  30"**, arXiv:2604.00165 (2026) (abstract). They attribute the apparent randomness of the centre column to
  left-permutivity and an asymmetric Boolean sensitivity, with Rule 22 as the symmetric reference. **Import:** context
  for section 8.6's churn (order in, noise out) and its avalanche.
- **Das, M., "Rule 30: Solving the Chaos"**, arXiv:2207.13237 (2022) (abstract). It claims an analytical solution to
  Prize Problem 1. The prize is still listed as open (rule30prize.org), so the claim has not been accepted. Not
  imported.
- **Arnold tongues and the circle map** (Wikipedia, "Arnold tongue"; read). A driven oscillator locks at a rational
  rotation number p/q over a whole region of parameters, and the rotation number as a function of the drive is a
  devil's staircase. **Analogy, not yet a method.** Under the period-2 trace the wheel turns 17 times in 56 steps.
  Under the other traces of the census (section 8.8) column 1 follows the drive's own frequency, which is low-order
  locking. The walls' notched kicks look like phase slips of a locked oscillator. **Import:** the rotation number as
  the invariant to compare traces by, if the census is extended.
- Not relevant on reading the abstract: Brummitt, C. D. and Rowland, E., "Boundary growth in one-dimensional cellular
  automata", arXiv:1204.2172 (a census of boundary growth rates, not Rule 30's columns).

Links: https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf ;
https://arxiv.org/abs/2609.25077 ; https://arxiv.org/abs/2604.00165 ; https://arxiv.org/abs/2207.13237 ;
https://en.wikipedia.org/wiki/Arnold_tongue ; https://arxiv.org/abs/1204.2172

## The owner's PRNG question: Rule 30 as a generator, and its cryptanalysis (surveyed 2026-10-05, by Cloud)

Scope: the owner asked what Rule 30's "poor behaviour on a chi-squared test when applied to all the rule columns"
(Wikipedia, citing Sipper and Tomassini) was, and whether it made the centre-column generator "a no go". The search
found that the cryptanalysis of Rule 30 reached this project's central construction 35 years earlier.

### Summary

The centre column was never a statistical failure. Wolfram's generator passes the standard tests, and Mathematica used
it for random integers for years. Its default today is a different cellular automaton, "ExtendedCA", which uses a
five-neighbour rule. Sipper and Tomassini used every cell of a small ring as a parallel stream, which is a different
generator, and `rule30_prng.py` shows two flaws of that use. The real break was cryptographic. Meier and Staffelbach
(1991) recovered the key from the centre column using Rule 30's left-toggle property. That is this project's forced
left half (§5 of RULE30-PRIZE.md, and Lemma 3 onwards).

### Sources and what to import

- **Meier, W. and Staffelbach, O., "Analysis of pseudo random sequences generated by cellular automata"**, EUROCRYPT
  '91, LNCS 547 (not read; described in Spencer's thesis below, read). Wolfram had proposed the centre column as a
  key stream (CRYPTO '85). Meier and Staffelbach showed that the left half of the space-time history is uniquely
  determined by the centre column and its right-adjacent column, because Rule 30 is left-toggle (left-permutive).
  The right-adjacent column comes from guessing the right half of the seed, and not all right halves are equally
  likely, so far fewer guesses are needed: for a 300-cell seed, 18.1 bits of entropy recover it with probability 1/2.
  - **Convergent evolution, recorded.** This is exactly our construction: column 0 and column 1 force the left half
    (§5), and the right half is a constraint on column 1 (§8). Their entropy of the right-adjacent column given the
    centre column is a cousin of our start-group counts $G(m, s)$ (§8.14). **Import:** their probabilistic algorithm,
    as a known method for counting column-1 sequences consistent with a given column 0. To read, if the counts matter.
- **Koc, C. K. and Apohan, A. M., inversion of Rule 30 iterations** (1997; described by Spencer). They answer a claim
  of Wolfram's that recovering a seed from states is NP-complete, with an inversion algorithm based on the best affine
  approximation of the rule. Not imported.
- **Spencer, J., "Cellular Automata in Cryptographic Random Generators"**, MSc thesis, DePaul University, 2013,
  arXiv:1306.3546 (read, the survey chapter). It describes the attacks above. It gives Sipper and Tomassini's setup:
  a cyclic 3-neighbour CA of 50 cells, 300 random initial states, 4,096 steps, each cell's entropy over time; evolved
  hybrids of rules 165, 90 and 150, or 165 and 225, compared with uniform Rule 30 and a 90/150 hybrid over four
  statistical tests. It also proves that toggle rules have a Theta(n) predecessor algorithm (InvertToggleRule).
- **Sipper, M. and Tomassini, M., "Generating parallel random number generators by cellular programming"**, Int. J.
  Mod. Phys. C 7(2) (1996) 181-190 (not read; abstract and Spencer only). Which chi-square Rule 30 failed is not known
  here. `rule30_prng.py` replicates the setup and finds two flaws of parallel use, neither of which touches the centre
  column used alone:
  - Neighbouring streams are tied: $x_{t+1}(i) \oplus x_t(i-1) = x_t(i) \vee x_t(i+1)$, so they agree at lag 1 in
    25.00% of steps instead of 50%. Rules 90 and 150 pass that test (50.02%, 50.00%), which is why linear hybrids looked
    better on it, although they are trivially broken by linear algebra.
  - Pooling consecutive rows: each row determines the next, so a chi-square that counts 4,096 rows of one run as
    independent rejects 12 to 13% of runs at the 1% level, on a ring or an open line alike. Rows 32 steps apart: 0.3%.
- **Wolfram Language documentation, "Random Number Generation"** (search summary). The default method "ExtendedCA"
  uses a five-neighbour cellular automaton rule; Rule 30 remains available as a method. The documentation's reasons
  for the change were not read.
- **Mariot, L. et al., "Insights Gained after a Decade of Cellular Automata-based Cryptography"**, arXiv:2405.02875
  (2024) (read in part, via a summary). Rule 30 lacks first-order correlation immunity, which is why the Meier and
  Staffelbach attack is efficient. Rule 30 is the field's standard warning: it passes statistical tests and is
  useless for cryptography.

**For our own method.** Our churn tests of §8.6 (block entropy, spectrum, avalanche) measured one sequence at a time.
By construction they cannot see a tie between two columns. That is fine for the question they answered (is the left
half random-looking), but it is the blind spot Sipper and Tomassini's parallel use exposes. Two-column statistics are
where Rule 30's structure is visible.

Links: https://link.springer.com/chapter/10.1007/3-540-46416-6_17 ; https://arxiv.org/abs/1306.3546 ;
https://www.worldscientific.com/doi/abs/10.1142/S012918319600017X ; https://arxiv.org/abs/2405.02875 ;
https://reference.wolfram.com/language/tutorial/RandomNumberGeneration.html ; https://en.wikipedia.org/wiki/Rule_30

## Before the bottleneck and entropy steps: information flow in Rule 30 (surveyed 2026-10-05, by Cloud)

Scope: are the leftward information speed (RULE30-PRIZE.md §8.17, §8.19) and the entropy of a column next to a
clamped periodic column (§8.20) known? Checked by search, abstracts only.

- **Shereshevsky, M. A., "Lyapunov exponents for one-dimensional cellular automata"**, J. Nonlinear Sci. 2 (1992)
  1-8, and **Tisseur, P., "Cellular automata and Lyapunov exponents"**, Nonlinearity 13 (2000) 1547 (arXiv:
  math/0312136) (abstracts; both cited by Kopra). Left and right Lyapunov exponents measure how fast perturbations
  spread each way. For Rule 30 the defect cone is asymmetric: perturbations spread right at full speed and left
  more slowly. A published value of the leftward speed was not found in what was read. Our measurements, 0.21
  cells per step for a single flip reaching column 1 next to a clamped 0101... and 0.28 for a second seed's
  influence on the open line, are of that kind. **Import:** the definitions, if the speed is ever needed exactly.
- **Bagnoli, F. et al., "Stability of cellular automata trajectories revisited: branching walks and Lyapunov
  profiles"**, arXiv:1406.5553 (search summary only): Lyapunov profiles of elementary rules, Rule 30 included. Not
  read.
- Nothing was found on the entropy of one column of Rule 30 next to a clamped periodic column. The bound of §8.20 is
  computed with the standard tools for sofic shifts (subset construction, spectral radius) on ladder.c's layer
  model.

Links: https://arxiv.org/abs/math/0312136 ; https://arxiv.org/abs/1406.5553 ;
https://www.sciencedirect.com/science/article/pii/S0304397522007502

## The owner's lightning, channels and maze: directed polymers and directed percolation (surveyed 2026-10-05, by Cloud)

Scope: before rule30_channels.py and rule30_maze.py (RULE30-PRIZE.md §8.28, §8.29), is it known whether paths of
least resistance through a random two-dimensional substrate form channels, and when a random pattern's black cells
connect? Checked by search, abstracts and summaries only.

- **Comets, F., Shiga, T. and Yoshida, N., "Directed polymers in a random environment: path localization and strong
  disorder"**, Bernoulli 9(4) (2003) (abstract). The decay rate of the partition function is equivalent to
  localisation of the path. Their approach relates the partition function to the probability that two polymers in
  the same environment end at the same point, our same-landing chance L. Quantitative decay estimates in one or two
  dimensions. **Imported:** L and its time average as the measure of channelling.
- **Comets, F. and Vargas, V., "Majorizing multiplicative cascades for directed polymers in random media"**, ALEA 2
  (2006) (summary): sharper free-energy estimates in dimension 1 + 1 and very strong disorder at every temperature
  there. So a polymer on a random pyramid should localise at any temperature: the theory behind CH2.
- **Chatterjee, S., "Proof of the path localization conjecture for directed polymers"**, Comm. Math. Phys. 370
  (2019) 703-717, arXiv:1806.04220 (title and summary only, not read).
- **Balazs, M., Rassoul-Agha, F. and Seppalainen, T., "The random average process and random walk in a space-time
  random environment in one dimension"**, Comm. Math. Phys. 266 (2006) 499-545 (summary): a walk choosing each step
  from a fresh random environment obeys a quenched central limit theorem; the quenched mean fluctuates on the scale
  $n^{1/4}$. The theory behind CH1 (the flicker spreads like a free walk).
- **Directed site percolation** in 1 + 1 dimensions has threshold 0.70548522 on the square lattice, with two parents
  per site (search summary). No published value was found for the lattice with three parents per site (x - 1, x,
  x + 1), the one the maze uses; rule30_maze.py measures it near 0.53 at depth 2048.
- Not found: any study of polymers or percolation on a cellular automaton's space-time pattern. The comparison of
  Rule 30 with random substrates (§8.28, §8.29) appears to be new, and simple enough that it may exist unfound.

Links: https://projecteuclid.org/journals/bernoulli/volume-9/issue-4/Directed-polymers-in-a-random-environment--path-localization-and/10.3150/bj/1066223275.full ;
https://link.springer.com/article/10.1007/s00220-019-03533-1 ;
https://link.springer.com/article/10.1007/s00220-006-0036-y ; https://arxiv.org/html/cond-mat/0503408

## After the diagonals and the band: what was already known (surveyed 2026-10-05, by Cloud, after the runs)

A failure of method: rule30_diagonals.py (left half) and rule30_leftband.py were designed and run before Rowland's §5
and Wolfram's prize announcement had been read. Both cover much of the ground.
- **Rowland, "Local nested structure in rule 30", §5 "The left side of rule 30"** (read). Left diagonals are eventually
  periodic with power-of-2 periods, a consequence of Jen's Theorem 4 (E. Jen, "Global properties of cellular
  automata", J. Stat. Phys. 43 (1986) 219-242). The eventual periods from the left edge begin 1, 1, 1, 2, 1, 2, 2, 1,
  4, 1, 4, ..., exactly as rule30_diagonals.py measured. Proposition 2 is Wolfram's observation (NKS p. 871), proved
  for any rightful initial row. Each period doubling occurs exactly when a diagonal is eventually white and the
  diagonal to its left has an odd number of black cells in each period. When a diagonal is eventually white and the
  next has a black cell in its period, the one after is eventually black.
  - Rowland's open question. Is the eventual left side independent of the initial condition? Rowland expects not. An
    eventually white diagonal whose left neighbour has an even number of black cells per period leaves two possible
    periods for the next diagonal, complements of each other. That first happens at his column 53209: column 53208
    is eventually white, and column 53207 has period 16. Each of those continuations splits again, at columns 58288
    and 72577, "and one surmises that in fact there are infinitely many possible left sides". Whether both
    possibilities are realised by actual initial conditions is left open ("if in fact they do occur").
  - **Import:** the credit for §8.27's left-side statements and for LB0, and the open question, tested by
    rule30_leftsides.py (§8.31). His columns are numbered from 1 at the left edge, so his column m is our diagonal
    e = m - 1, if his period list is aligned as it appears to be (checked there).
- **Wolfram, S., "Announcing the Rule 30 Prizes"** (writings.stephenwolfram.com, 2019) (read in summary). There is
  "some regularity over on the left". "At least over the first 100,000 or so steps, the boundary seems to move on
  average about 0.252 steps to the left at each step, with roughly random fluctuations." It is presented as an
  observation. **Import:** the credit for §8.30's band and its speed. Our 0.245 to 0.257 (from the transients)
  brackets it; the damage front on a random background, 0.246 with a standard error near 0.003, is close but about
  two standard errors below it.
- **Wolfram's Problem 2 table** (the same announcement, read 2026-10-05). Black and white counts in the centre column
  after 10, 100, ..., 10^9 steps: black 7, 52, 481, 5,032, 50,098, 500,768, 5,002,220, 50,009,976 and 500,025,038.
  That is an excess of black at every decade from 10^4 on, by 0.6 to 2.0 standard deviations of a fair coin; Wolfram
  describes the running excess as random-walk-like. rule30_tilt.py reproduces the counts to 10^6 exactly. (A first
  summary of the page gave a wrong ratio, 0.9999998, corrected from the table before any use.)
- Searches for a later answer to Rowland's question ("rule 30" "left side", 53209) found nothing.
- **Our answer** (rule30_leftsides.py, RULE30-PRIZE.md §8.31). Rowland's indexing is confirmed (his column 53209 is
  our diagonal 53208). The other continuations occur for constructed finite seeds: at least 4 certified left sides by
  diagonal 160,000, with branch points 53208 and 58287 on the universal side and 53208 and 72576 on the other, as he
  found. But all 60 generic rows tried share one left side, and the split's decision is phase-locked to the left
  side's own cycle.

Links: https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf ;
https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/

## Before and after the entropy squeeze: column entropy (surveyed 2026-10-05, by an independent review session)

Scope: is RULE30-PRIZE.md §8.33's lemma known? Every left column of a Rule 30 configuration whose column 0 is 0101...
has topological entropy at most (1/2) log2 lambda_m. Does anything give a lower bound on a column's entropy? A
separate session, given only the lemma and the sources, reviewed it adversarially and searched. Its findings:
- **Milnor, J., "On the entropy geometry of cellular automata"**, Complex Systems 2 (1988), Example 6.2 (read via text
  extraction; https://wpmedia.wolfram.com/sites/13/2018/02/02-3-6.pdf). The "additional causal cone" of a
  left-permutive map, the geometric fact behind step 3. Directional entropy concerns the whole system, not one
  configuration with a column held fixed.
- **Kopra, J., "Rapid left expansivity, a commonality between Wolfram's Rule 30 and powers of p/q"**, Theoretical
  Computer Science 946 (2023) (read in full by the review, via
  https://www.utupub.fi/bitstream/handle/10024/174540/1-s2.0-S0304397522007502-main.pdf; earlier listed here as
  UNVERIFIED after a 403). It defines left expansivity with dimensions (0, 1, 2). It never mentions entropy. Its
  Jen-type results come from Morse-Hedlund, so the known lower bound on a width-2 trace is p(n) >= n + 1. Kopra's
  arXiv:2005.05112 on trace complexity was read only in abstract.
- **Kurka, P.** (column subshifts; https://www.cts.cuni.cz/~kurka/cantor.pdf) and **Courbage, M. and Kaminski, B.**
  (directional entropy; https://link.springer.com/article/10.1007/s10955-006-9172-1). Both are about systems, not
  single configurations.
- Sliding block codes do not increase entropy, and sofic entropy comes from the subset construction (Lind and
  Marcus, a textbook; cited from memory).
- **Not found:** the lemma itself; any positive lower bound on the entropy of any column of any finite Rule 30
  configuration. In Kopra's class such a bound fails in general: Rule 90's two-cell trace from a single seed has
  p(n) = 7, 13, 25, 49, 97, 193 at n = 4, 8, ..., 128 (the review's computation), entropy 0.
- **Import:** the credit and the limits recorded in §8.33. The review found the lemma sound and the first-stated
  reduction a restatement of the problem.

## After the merging census: merging walks and the coin's maximum (surveyed 2026-10-05, by Cloud, after the runs)

Scope: RULE30-PRIZE.md §8.38 (rule30_influence.py, rule30_merge.py). Is the count of distinct forced walks known,
and are the two outside facts it leans on stated correctly? The survey came after the runs. The predictions did not
depend on it, but they used both facts from memory, so this is recorded as late.
- **Milnor's directional entropy** (already listed above, in the column-entropy survey). It measures the whole
  system's complexity along a direction of space-time. §8.38 counts something narrower: the distinct pairs of
  anti-diagonals reachable when column 0 is held at 0101... and column 1 is free at even times. Not found in the
  record: that count, its growth rate (about 1.764 per free bit), or the OR-shielding merges behind it.
- **Scheidegger, A. E., "A stochastic model for drainage patterns into an intramontane trench"**, Bull. Int. Assoc.
  Sci. Hydrology 12 (1967), 15-20 (citation checked by search; the paper itself not read). In this river-network
  model each site drains to one of two neighbours below it, chosen at random, so the streams are coalescing random
  walks. The number of distinct streams then falls as a power of the distance, which is what MG7 compared against.
- **Eisenberg, B., "On the expectation of the maximum of IID geometric random variables"**, Statistics & Probability
  Letters 78 (2008), 135-143 (abstract). The expected maximum of n IID geometrics with P(M >= m) = 2^-m is
  log2 n + gamma / ln 2 - 1/2 plus a small periodic term. For runs of 1 + 2M that gives §8.38's 2 log2 n + 1.67.
- **Import:** the comparison in MG7, and the constant in §8.38. Nothing found settles either statement that §8.38
  says a proof would need.

## The owner's zeta note: the prime-gap parallel (surveyed 2026-10-05, by Cloud)

Scope: the owner compared lead 1's returns to zero with the Riemann zeta function's zeros. The precise parallel is
the probabilistic model of the primes and its maximal gaps. That model is to the primes what the coin model is to
Rule 30's forced walks. The survey came after the merging census of RULE30-PRIZE.md §8.38 and changed none of its
predictions.
- **Cramer's model and conjecture** (H. Cramer, 1936): treat each n as prime with probability 1/log n,
  independently. The model predicts maximal prime gaps of about (log p)^2. Statement and history checked via
  https://en.wikipedia.org/wiki/Cram%C3%A9r%27s_conjecture and Granville's survey below.
- **Maier's theorem** (1985) shows the model is wrong in short intervals, because divisibility by small primes is
  structure, not chance.
- **Granville, A., "Harald Cramer and the distribution of prime numbers"**, Scandinavian Actuarial Journal (1995)
  (https://chance.dartmouth.edu/chance_news/for_chance_news/Riemann/cramer.pdf; checked through the search summary
  and the Wikipedia article, not read in full). The refined model, with the small primes sieved out, raises the
  constant: limsup G(p) / (log p)^2 >= 2 e^-gamma = 1.1229. This is the shape of §8.38. A coin model gets the scale,
  and a structural correction (there divisibility, here the merging of walks) changes the constant (there 1 to
  1.12, here 1 to 0.82).
- **Bertrand's postulate**: for every n > 1 there is a prime between n and 2n. That is a doubling statement, like
  §8.36's conjecture that from depth d there is a one by depth 2d + 4. Chebyshev proved it around 1850 from
  estimates of factorials, long before anything sharp about gaps. Ramanujan (1919) and Erdos (1932) reproved it
  from the prime factors of the binomial coefficient C(2n, n). None of the proofs shows that the primes are
  random. Cited from memory, as standard.
- **Import:** the shape of a proof worth looking for. Cramer's sharp conjecture is still open. The doubling
  statement fell to a size argument: a quantity forced to be large, which an empty interval would make small. For
  Rule 30, any finite bound on R(d), not only d + 4, settles Conjecture LR for 0101... (König's lemma turns
  unbounded runs into an infinite one). So the target has Bertrand's shape, not Cramer's.

## After the wheel dig: Rule 30's siblings in arithmetic (surveyed 2026-10-05, by Cloud)

Scope: RULE30-PRIZE.md §8.43 and §8.44 leave the cost side of period 2 open: why a condition at the 0101 wall
costs a bit. Does any sibling problem have a proved size argument of the kind PRIOR-ART's prime-gap parallel
points to?
- **Kopra, J., "A natural class of cellular automata containing fractional multiplication automata, Rule 30, and
  others"**, arXiv:2202.13809 (abstract read). It defines rapidly left expansive cellular automata, a class
  containing Rule 30 and the automata that multiply by a fraction p/q in a suitable base. Jen's proposition on
  aperiodic columns generalises to the class. Rule 30 is in the class; it is not a multiplication automaton.
- **Mahler's 3/2 problem** (1968; checked via https://en.wikipedia.org/wiki/Mahler%27s_3/2_problem). It asks whether
  any xi > 0 keeps every fractional part of xi (3/2)^n below 1/2 (a "Z-number"). It is open.
- **Flatto, L., Lagarias, J. C. and Pollington, A. D., "On the range of fractional parts {xi (p/q)^n}"**, Acta
  Arithmetica 70 (1995), 125-147 (http://matwbn.icm.edu.pl/ksiazki/aa/aa70/aa7023.pdf; sections 1 to 3 read, the
  proofs of Theorems 1.1, 1.2, 3.2 followed, Theorem 3.3's lemmas skimmed). For coprime p > q >= 2, any interval
  holding every {xi (p/q)^n} has length at least 1/p (Theorem 1.4). Partial, as Mahler's conjecture needs 1/2.
  How the proof works, Mahler's "decoupling":
  - The integer parts g_n follow a fixed map T on the integers. Its symbols (g mod q) form a full shift: every
    string of length k occurs exactly once among the residues mod q^k (Lemma 2.2).
  - The scaled fractional parts follow a linear mod-one map f(x) = beta x + alpha with beta = p/q. Its admissible
    strings are few: at most c beta^k of length k.
  - xi is a generalised Z-number exactly when the two itineraries agree, up to a fixed permutation (Prop. 2.1). The
    counting gives sparsity (Theorem 1.1, at most x^gamma Z-numbers below x, gamma < 1).
  - Emptiness comes from finiteness (Theorem 3.2). If only finitely many f-orbits stay in the interval, then
    pigeonhole makes the orbit periodic. Two different powers of xi would then share one integer itinerary, which
    Lemma 2.2's injectivity forbids. Theorem 3.3, the long part, shows that finiteness holds for a dense set of
    intervals of length 1/p.
- **What it means here: the same structure, in the same open regime.** The wall form of RULE30-PRIZE.md §8.39 and
  §8.40 is a decoupling of the same kind:
  - **The free side.** The left half is a full shift at the wall, its itinerary in bijection with the seed (WA1).
    That is the integer side.
  - **The constrained side.** The right half's column 1 has a thin language (the channel bound, §8.20). That is the
    mod-one side.
  - **The coupling.** A finite configuration with a periodic centre needs the two to agree at the wall for ever:
    that is a Z-number.
  - **Emptiness by finiteness** is, here, Jen's theorem (a periodic column 1) and Condrey's constant walls (column 1
    monotone, so each admissible column 1 is eventually constant; corrected wording, see the wide survey below:
    zero entropy alone would not be enough).
  - **The open regime.** Next to 0101 the constrained side has positive entropy, about 0.12 bits per visible bit, so
    infinitely many admissible behaviours. That is exactly the regime of Mahler's own conjecture (interval 1/2 > 1/p),
    which this method has not closed since 1968. The entropy squeeze (§8.33) is the analogue of FLP's Theorem 1.1,
    sparsity without emptiness.
  The import is a calibration, not a route: Rule 30's period-2 case is a Mahler-type problem in the regime where
  Mahler's method stops.
- **What it means here.** In the same class as Rule 30, the question of the same shape is also open, and the best
  known result is a size bound. Its proof uses the arithmetic of p/q (integers and residues), which Rule 30 lacks.
  A Rule 30 analogue would need a substitute for that arithmetic. It is recorded as the nearest proved size
  argument, not as a route.


## The owner's wide survey: nature, biology and the other disciplines (surveyed 2026-10-05, by Cloud)

Scope: the owner asked for one more research road before fresh eyes: as many disciplines as possible, however
unlikely, each with a tether to the problem's structure. "Our Rule 30 problem paints itself on the back of a snail
shell." Seven survey agents searched, one per domain: biology and nature; physics and chemistry; mathematics;
computing and engineering; the long shots (history, astronomy, the arts); molecular machinery (the owner's protein
folding note); and the Game of Life (the owner's second note). Each was given the same four-item summary of the
problem and asked to rate each tether from 1 (an analogy) to 5 (the same mathematics). The agents read the
sources; Cloud checked the top-ranked ones (marked "checked") at their abstract pages. The survey came after every
run so far and changed no prediction.

The one finding that every domain returned: every theorem found of the form "a low-information drive cannot hold a
chaotic system in a fixed state" is about **sets** (of positive measure, or with interior), never about **one
orbit**. That is exactly the gap between the entropy squeeze (sparsity) and the prize (emptiness), and the gap in
Mahler's problem.

A correction came with it. The mathematics survey read FLP's Theorem 3.2 again: its hypothesis is finitely many
admissible orbits, which is stronger than zero entropy (a Sturmian system has zero entropy and uncountably many
points). RULE30-PRIZE.md §8.45 and the section above are corrected in place: the solved cases are those where every
admissible column 1 is eventually periodic (Morse and Hedlund's criterion, Kopra's Lemma 4.2, then Jen).

**Mathematics** (strength 5 to 2):
- **Kari, J. and Kopra, J., "Cellular automata and powers of p/q"**, RAIRO-ITA, arXiv:1710.05737 (abstract checked).
  Mahler's problem restated as a question about one column of the automaton that multiplies by p/q in base pq.
  Theorem 4.9, from ergodicity, strong mixing and compactness (an unavoidable finite family of cylinders, Lemma
  4.4): finite unions of intervals approximating [0, 1] as closely as one likes hold no orbit. Not constructive;
  their Problem 5.1 asks for a constructive proof. The trace subshift is neither sofic nor synchronising
  (arXiv:2005.05112). Strength 5.
- **FLP's Theorem 3.3** (the paper of the previous section, pp. 138-139, reread by the survey). Finiteness holds for
  a dense set of windows, and the bound 1/p comes from enlarging a window to one of those. FLP never beat positive
  entropy: they moved to a window where the constrained side is finite. Strength 5.
- **Kopra's barrier** (arXiv:2202.13809, the survey's reading). The class of rapidly left expansive automata contains
  Rule 90, whose centre column from one cell is eventually constant. A proof must use Rule 30's own nonlinearity.
- **Lagarias, J. C., "Ternary expansions of powers of 2"**, arXiv:math/0512006. Erdős's conjecture that 2^n has a
  2 in base 3 for n > 8 is open. Two methods, from the leading digits and from the trailing (3-adic) digits, use
  independent information, and combining them is "a challenging problem". The exceptional set has Hausdorff
  dimension log_3 2 > 0, the analogue of positive entropy. Strength 4.
- **Buzzi, J., "Piecewise isometries have zero topological entropy"**, Ergodic Theory Dynam. Systems 21 (2001)
  1371-1377 (checked). A rotation with slips of fixed sizes at fixed phases is a piecewise isometry, so column 1's
  positive entropy must come from the kick sizes, as §8.43 measured. Strength 4.
- **Collatz.** Bernstein and Lagarias's conjugacy of the 3x+1 map to the 2-adic shift is triangular, like the
  seed-to-itinerary bijection of the wall form. Tao's theorem (arXiv:1909.03562) covers almost all orbits, not every
  orbit. Strength 3.
- **The busy beaver cryptid Antihydra** (https://wiki.bbchallenge.org/wiki/Antihydra): it halts iff an iteration of
  floor(3n/2) ever has enough odd values, a Mahler-family question. A random-walk model says it never halts;
  there is no proof. Strength 3.
- **Furstenberg, Rudolph, Host; Sarnak; Sinai.** Measure rigidity under x2 and x3 concerns measures and typical
  points; its automaton versions need algebraic, bipermutative rules (arXiv:math/0510564), which Rule 30 is not.
  Two systems of positive entropy are never disjoint (each has a Bernoulli factor, by Sinai), so there is no
  measure-level obstruction to coupling the two sides: any proof works point by point. Strength 2 to 3.
- **Low complexity forces structure** (Morse and Hedlund; Adamczewski and Bugeaud; Durand's Cobham theorem;
  Nivat-type results). Each works only when the complexity is low. Strength 2.

**Computing and engineering** (strength 4 to 1):
- **Yolcu, E., Aaronson, S. and Heule, M. J. H., "An automated approach to the Collatz conjecture"**,
  arXiv:2105.14697 (abstract checked). Collatz as termination of a string rewriting system; nontrivial weakenings
  proved with SAT-found natural and arctic matrix interpretations; an earlier unary encoding provably admits no
  such proof, so the encoding decides. Strength 4.
- **Liveness certificates for infinite-state systems**: regular model checking with learned automaton invariants
  (http://www.cs.ru.nl/personal/nilsjansen/files/publications/neider-et-al-nfm-2013.pdf); Lin, A. W. and
  Rümmer, P., CAV 2016, arXiv:1606.01451 (abstract checked: a progress relation as a finite automaton, learned with
  L* and SAT); k-liveness (Claessen and Sörensson, FMCAD 2012). Condrey's $H(2, w) \ge w$ rules out a fixed-depth
  induction, so a certificate must scale with the width, as these do. Strength 4.
- **Rule 30's own forcing rules** (Meier and Staffelbach; Spencer's thesis, arXiv:1306.3546, already above): "10" in
  a column forces a 1 to its left. Strength 3.
- **The wheel as a digital line**: Euclidean rhythms and Bresenham's algorithm (Demaine et al., "The distance
  geometry of music", https://erikdemaine.org/papers/DeepRhythms_CGTA/paper.pdf); linear-time recognition of
  digital straight segments (arXiv:0906.2351), an exact kick detector; bandpass sigma-delta modulators as piecewise
  isometries. Strength 3.
- **Decidability**: properties of ultimate traces are undecidable over all automata (arXiv:1001.0251); for linear
  automata the columns are automatic and eventual periodicity is decidable (arXiv:1209.6008). Strength 3.
- Constrained coding (the channel bound is Shannon's capacity, which cannot exclude one word), boundary control of
  automata as SAT (Bagnoli, Dridi and Fatès, arXiv:2504.03691), phase-locked loop cycle slips (statistics only),
  particle image velocimetry's peak locking (analogy). Strength 2 to 1.

**Physics and chemistry** (strength 4 to 1):
- **Touchette, H. and Lloyd, S., "Information-theoretic limits of control"**, PRL 84 (2000) 1156, arXiv:chao-dyn/9905039
  (abstract checked): each bit gathered buys at most one extra bit of entropy reduction. **Nair, G. N., Evans,
  R. J., Mareels, I. M. Y. and Moran, W., "Topological feedback entropy and nonlinear stabilization"**, IEEE TAC 49
  (2004) 1585-1597 (https://people.eng.unimelb.edu.au/gnair/TAC04.pdf; checked via the search summary): a plant can
  be held in a compact set iff the data rate exceeds its feedback entropy there. OGY control (Ott, Grebogi and
  Yorke) holds a chaotic system on one unstable periodic orbit with tiny pushes. Strength 4 for the coin model,
  1 for the missing step: these are theorems about sets.
- **Domain walls as particles**: Grassberger (1984), annihilating random walks of kinks; **Eloranta, K. and
  Nummelin, E., "The kink in elementary cellular automaton Rule 18 performs a random walk"**, J. Stat. Phys. 69
  (1992) 1131-1136 (bibliographic record checked; abstract not seen); Hanson and Crutchfield's automatic domain test
  (https://csc.ucdavis.edu/~cmg/papers/ECA54.pdf). Strength 4.
- **Frenkel-Kontorova discommensurations** (Sturmian ground states, arXiv:2507.06915; many-kink solutions at
  rational rotation number, arXiv:2004.04868); Aubry-Mather arguments need well-ordered configurations, and kicks
  of both signs break that. **Random tilings**: the angle is the phason coordinate, and its free diffusion is a
  phason walk (arXiv:cond-mat/0310514). Strength 3 to 4, as descriptions.
- Boundary-driven transport (Krug, PRL 67 (1991) 1882; Rule 54 with random boundaries, arXiv:1512.01385, which needs
  integrability), phase slips in wires and condensates, the kicked rotor (Chirikov's diffusion rate comes from
  ignoring correlations). Strength 2 to 1.

**Biology and nature** (strength 4 to 1):
- **Cardiac parasystole** (Glass, L., Goldberger, A. L. and Bélair, J., Am. J. Physiol. 251 (1986) H841;
  Schulte-Frohlinde et al., PRL 87 (2001) 068104, arXiv:cond-mat/0011367, abstract checked). A beat shows when a
  rotating phase leaves a refractory window; the number of beats between takes at most three values (the three-gap
  theorem, via Slater 1967); in modulated parasystole the sinus beats reset the phase, a rotation with kicks.
  Strength 4.
- **Longest matches in DNA**: Arratia, R. and Waterman, M. S., Adv. Math. 55 (1985); **Rousseau, J., "Longest common
  substring for random subshifts of finite type"**, Ann. IHP, arXiv:1905.08131 (abstract checked): governed by the
  Rényi entropy, almost surely, under mixing. The coin law as a theorem for typical inputs. Strength 4.
- **Random circle maps** (Müller-Bender, Kastner and Radons, arXiv:2204.09392; Antonov and Malicet): random circle
  maps synchronise unless they share an invariant measure. Rigid rotations share the uniform one, so nothing pulls
  the wheel's angle back. Strength 3.
- **Phyllotaxis** (Douady and Couder, PRL 1992; Atela, Golé and Hotton, J. Nonlinear Sci. 2002; Adler, J. Algebra
  1998): the same continued fractions, but the plant's angle is selected and stable, the opposite of the wheel.
  Strength 3, for the wheel only.
- **Seashells** (Meinhardt, https://www.bio.mpg.de/268545/pigmentation-patterns; Wolfram, NKS p. 423): the shell
  is a space-time plot and colliding waves annihilate, but the models are reaction-diffusion with restoring forces
  (in Oliva porphyria a hormone counts the waves), and Conus textile's resemblance to Rule 30 is visual. No wall was
  found. Strength 2.
- Winfree's phase singularities (a homotopy argument needing a continuous phase), clock-and-wavefront somitogenesis,
  Boolean-network control (finite, so the pigeonhole case), the error threshold. Strength 2 to 1.

**Molecular machinery** (the owner's protein-folding note; strength 4 to 1):
- **Invariance entropy** (Colonius, F. and Kawan, C., SIAM J. Control Optim. 2009): the least data rate that keeps
  every state of a set inside a target. Its lower bounds are volume counts, a uniform escape rate. A single orbit
  costs nothing. Strength 4, with the same gap.
- **Boyd, A. B., Mandal, D. and Crutchfield, J. P., "Correlation-powered information engines and the thermodynamics
  of self-correction"**, PRE 95 (2017) 012152, arXiv:1606.08506 (checked in the PDF). A ratchet reads a period-2
  tape 0101... with phase slips at rate c; a synchronising state returns it to phase; above c* = 1/(1 + e) it can
  no longer work. The objects are ours: a period-2 tape with slips. The inequality needs a measure and an energy;
  the transducer formalism could carry over. Strength 3.
- **Zurek, W. H., "Algorithmic randomness and physical entropy"**, PRA 40 (1989) 4731 (not read): entropy of a single
  microstate. It suggests the single-object form of the missing statement. Strength 3.
- **Algorithmic self-assembly**: Rothemund, Papadakis and Winfree, PLoS Biol. 2 (2004) e424, Sierpinski triangles
  grown by XOR tiles from a seed row, errors propagating as defects; proofreading tile sets. No Rule 30 tile
  experiment was found. Strength 3 for the object, 1 for the theorems.
- **Protein folding**: Levinthal's paradox and its resolution by a biased landscape (Zwanzig, Szabo and Bagchi,
  PNAS 89 (1992) 20: a bias of a few kT shrinks the search); the HP model's NP-hardness (Berger and Leighton);
  designability (Li, Helling, Tang and Wingreen, Science 273 (1996) 666), which is many-to-one where the wall's
  left side is a bijection. Strength 1 to 2.
- Kinetic proofreading (Hopfield 1974), ribosomal frameshifting at slippery sites, Feynman's ratchet, rotary motors
  in steps (F1-ATPase; the flagellar motor's 26 steps against the wheel's 28 notches is a coincidence), the KaiABC
  clock. Strength 2 to 1: they need noise, energy or detailed balance.

**The long shots** (strength 4 to 1):
- **Langton's ant**: the highway is unproved (https://en.wikipedia.org/wiki/Langton%27s_ant), but **Bunimovich, L. A.
  and Troubetzkoy, S. E., "Recurrence properties of Lorentz lattice gas cellular automata"**, J. Stat. Phys. 67
  (1992) 289-302 (bibliographic record checked) proved every trajectory unbounded. The proof's outline, from a
  summary only: reversibility makes a bounded path periodic, and an extremal cell gives the contradiction.
  Strength 3.
- **Calendars**: the Hebrew leap years form E(7, 19); leap-year rules generalise Bresenham (Harris and Reingold);
  the Persian 33-year cycle is seven 4-year blocks and one 5-year block, slipping now and then to 29 years
  (arXiv:astro-ph/0409620). The same mathematics as the wheel. Strength 4, as a viewpoint.
- **Music**: well-formed scales are Christoffel words (Clampitt and Noll, MTO 11.17.1); E(17, 56) was found in no
  catalogue. Strength 4, as a viewpoint.
- **Pingala and Virahanka**: a correction to the survey's own brief. They counted metres of n morae made of short
  (1) and long (2) syllables, which gives the Fibonacci numbers, the same count as binary words with no two
  adjacent ones (Singh, Historia Math. 12 (1985)).
- Euclid and Erdős's proof of Bertrand (a gap between two exponents), Kirkwood gaps (long quiet behaviour proves
  nothing), KAM's golden torus, satin weaves, Huygens's gear ratios. Strength 3 to 1.

**Philosophy and logic** (the owner's note: "We should not discount philosophical sources as irrelevant just because
they contain no concrete math. Their math is logic, truth, gates." An eighth survey agent; sources not checked by
Cloud):
- **Eternal recurrence and Simmel's wheels.** Nietzsche argued that finitely many centres of force must pass through
  finitely many combinations and repeat (https://www.gutenberg.org/files/52915/52915-h/52915-h.htm). Simmel replied
  with three wheels on one axle, one turning at 1/pi the speed of another, which never line up again
  (https://schwitzsplinters.blogspot.com/2012/10/nietzsches-eternal-recurrence-scrambled.html). The pigeonhole case
  and the open case, in one argument: a wheel with eventually periodic kicks gives a periodic column 1, closed by
  Jen; the open case is exactly kicks that never become periodic, Simmel's 1/pi. Strength 4, as a picture.
- **Potential infinity** (Euclid IX.20 says "more than any assigned multitude", never "infinite"; Aristotle;
  Archytas's staff at the edge of the world; https://plato.stanford.edu/entries/infinity/). The form of the missing
  statement: for every width w, a bound B(w) by which every configuration on w cells breaks the 0101 centre. Each
  B(w) is a finite check; the proof needed is a formula for B or a step from w to w + 1. This is PERIOD-TWO.md §7,
  question 1. Strength 4.
- **Hume, Popper and Carroll's Tortoise** (https://plato.stanford.edu/entries/induction-problem/;
  https://en.wikipedia.org/wiki/What_the_Tortoise_Said_to_Achilles). The coin model is a uniformity principle, so
  more runs that confirm it go round Hume's circle; each restatement hands the Tortoise one more premise, and what
  is missing is a rule of inference. "Eventually 0101" has the form "there is a T such that for every t", which no
  finite run can verify or refute. The answer to the owner's ouroboros, from philosophy. Strength 4.
- **Kripke's quus and Goodman's grue** (https://iep.utm.edu/kripkes-wittgenstein/). Finitely many observations fit
  infinitely many rules. Here: every finite stretch of 0101 is realised by some seed, so an argument from windows of
  time cannot work, and a proof must use the finiteness of the seed. Strength 3.
- **The tetralemma** (Nagarjuna's catuskoti: A, not A, both, neither; Belnap's four-valued logic;
  https://en.wikipedia.org/wiki/Tetralemma). It names the fourth game that RULE30-PRIZE.md §8.40 lacked: neither,
  no conditions, the baseline. It suggests a measurement: with $N$ the count of seeds that survive each game,
  $N_\text{both} N_\text{neither} / (N_\text{black} N_\text{white})$ near 1 says the black and white conditions are
  independent, as the coin model assumes; a ratio falling towards 0 would be a measurable obstruction. Strength 3.
- **Boole and Jevons** (https://plato.stanford.edu/entries/boole/). Boole defined x + y only for disjoint classes
  (exclusive or), and refused Jevons's inclusive or. Since $c \lor r = c \oplus r \oplus cr$, Rule 30 is the linear
  Rule 150 plus the single term $cr$: all its nonlinearity is the overlap Boole would not interpret. Strength 3.
- Llull's rotating discs, Leibniz's binary columns (01, 0011, 00001111...), Cusanus's infinite circle as a line,
  Dante's 3-sphere (two balls glued along a sphere, like two halves glued at a wall; Peterson, Am. J. Phys. 1979),
  Borges's Library and forking paths, Zeno: pictures, strength 2 to 1. No tether was found for Kant, the Liar or
  Funes.

**Addendum, the mixing check for question 4** (2026-10-05, by Cloud, from the thesis the owner linked).
- **Shereshevsky, M. A., "Ergodic properties of certain surjective cellular automata"**, PhD thesis, University of
  Warwick, 1992 (https://wrap.warwick.ac.uk/id/eprint/34640/1/WRAP_THESIS_Shereshevsky_1992.pdf; Chapter 1, section
  1.3 read), the source of the paper in Monatsh. Math. 114 (1992) 305-316. Write the rule as
  $(Tx)_i = F(x_{i+l}, \ldots, x_{i+r})$.
  - Theorem 1.3.3: if $l < 0$ and $F$ is left permutative, the automaton is $k$-mixing for every $k \ge 1$ for the
    uniform Bernoulli measure. Rule 30 has $l = -1$ and is permutive in $x_{i-1}$, so it is $k$-mixing, hence
    ergodic. Shirvani and Rogers had proved the 1-mixing case for two symbols.
  - Theorem 1.3.2 (a Bernoulli natural extension) needs $l < r \le 0$ in the left-permutive case, and Theorem 1.3.4
    (a K-automorphism) needs the neighbourhood on one side of the cell. Rule 30 meets neither ($l < 0 < r$).
  - Proposition 1.3.6: the left-permutive rule $x_0 + x_1(x_2 + 1)$ on the neighbourhood $[0, 2]$ is surjective and
    not ergodic, so the condition $l < 0$ matters.
  So Kari and Kopra's hypotheses of ergodicity and strong mixing hold for Rule 30. What their argument would still
  need is a Rule 30 analogue of the step from Z-numbers to configurations; that is not done.

## After the window principle: the Collatz complexity bound is Dubickas's (checked 2026-10-05, by Local through a search agent)

Checked after the proofs of COLLATZ-PRIZE.md §5 and RULE30-PRIZE.md §8.54, §8.57, §8.58 were written.
Pages and abstracts were read; no PDF could be opened, so Dubickas 2009, Jen 1990, Monks-Yazinski 2004,
López-Stoll 2009, Bernstein-Lagarias 1996 and Terras 1976 were seen only in abstract or through citing papers.

- **Collatz, W2 (complexity at least 1.71 n): FOUND, refereed, read in full 2026-10-06.** Dubickas, Glasgow Math. J.
  51 (2009) 243-252. Theorem 3 (the $\lceil px/q \rceil$ maps, $\liminf P/n \ge \log q/\log(p/q)$), Corollary 4 (the
  $\lceil 3x/2 \rceil$ sequence, $P(X, n) > 1.70951129\,n$) and Theorem 5 (the 3x+1 map on positive integers with
  $x_n \to \infty$: $P(X, n) > 1.70951129\,n$ for large $n$; "speculative" because conditional on a divergent
  trajectory). Integers only; rationals are not mentioned. He conjectures $P(X, n) = 2^n$. Credit settled: W2 for
  integers is his; ours adds odd-denominator rationals by the same count.
- **Collatz, W1 and W3: FOUND three times in 2026, all unrefereed** (GitHub notes of 2026-07-22 and 2026-09-22, a
  Zenodo record of 2026-10-02). Implied for integer orbits by Dubickas's Theorem 5; for slopes below $\log_3 2$ by
  Monks and Yazinski (2004), Theorem 2.7(b) (secondary account).
- **The lemma of COLLATZ-PRIZE.md §4**: the identity is Terras (1976) and Lagarias (1985, Theorem B), verbatim as
  Lemma 2.3 of arXiv:2602.10466; the least-residue bound is Kontorovich and Sinai's structure theorem, part two
  (arXiv:0910.1944, Theorem 5.2), in the odd-to-odd form.
- **arXiv:2101.12747** (López and Stoll, 2021): no refereed criticism, correction or confirmation found. The gap at
  its equations 15 and 16 (a real limit taken for a 2-adic one) is raised, with counterexamples and unanswered, in
  a public issue of 2026-09-30; a 2026 note calls it "an apparent gap".
- **Rule 30, Theorem A (Jen with a clock): NOT FOUND; NEAR.** Kopra (arXiv:2202.13809) Lemma 3.2 tracks the
  preperiod and Theorem 3.5 is the case $b = \infty$; Condrey (arXiv:2609.09431) Theorems 6, 7 and Corollary 8 bound
  the constant prefix of one column by $w + 2$ (period 1, from time 0, sharp). Nothing for period $P$, later windows,
  or pairs of columns.
- **Rule 30, Theorem A′ (the window principle): NOT FOUND; NEAR.** The mechanism is standard (Wolfram's prize post;
  Kopra, Definition 3.1). Its corollary $p(n) \ge n - L$ is weaker than Jen plus Morse-Hedlund. Dubickas's Theorem 3
  is the same count for the times-$p/q$ automata, which share Kopra's class with Rule 30; no common statement found.
  Kopra arXiv:2005.05112 computes the complexity of the whole trace subshift, not of one orbit.
- **Rule 30, Theorem E (Sturmian columns excluded): NOT FOUND.** Context: Rowland and Yassawi (arXiv:1209.6008),
  columns of linear automata are $p$-automatic, hence never Sturmian; Dolce and Tahay (DLT 2022, snippet only):
  Sturmian columns of quadratic slope exist in purpose-built automata.
- **Still to check:** whether the unboundedness of the left diagonals' periods (RULE30-PRIZE.md §8.59, Lemma B2) is
  in Jen (1986) or Rowland (2006, §5).

Sources opened for the Rule 30 statements: Kopra (two papers), the Kari-Kopra abstract, Condrey, Wolfram's prize
post and bibliography, the NKS Rule 30 note, Jen's OSTI abstract. Queries: Rule 30 with adjacent columns, window,
quantitative, Jen; left-permutive trace complexity from a finite configuration; Rule 30 Sturmian; Brunnbauer 2019
(diagonals only).


### GPT proof-audit reading (2026-10-06)

Read Rowland, [Local nested structure in rule 30, §5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf),
pages 15–17, including the reset lemma and period-doubling proof. It discusses loss of seed information and the
first possible split at column 53209 (our zero-based diagonal 53208). The all-seed finite certificate in
RULE30-GPT.md G2 applies that mechanism; the branch construction was already in RULE30-PRIZE.md §8.31.
Unboundedness of diagonal periods was not found in this section; this is not a claim it is absent elsewhere.
Jen 1986 remains owed a full reading.

Checked the continued-fraction best-approximation input against Theorem 27 of the
[UNCG ergodic-theory lecture notes](https://uncg.edu/~cdsmyth/UNCG_Ergodic_Theory_Summer_School_2020_Final_Lecture_Notes.pdf).
G2 supplies a finite-offset argument for E Step 4. This standard input establishes no priority for the Rule 30
application, and no further literature search was made in this work block.


### GPT reset-front reading (2026-10-06 03:01 BST)

Re-read Rowland, [Local nested structure in rule 30, section 5](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), pages 15–17: the black-parent reset and period-doubling mechanism. G6 applies that mechanism to the existing conservative front, not a new period theorem. Searches `"Rule 30" "settling" "left"` and `"Local nested structure in rule 30" left side reset period` returned this paper and related period sequences; no sub-3 all-branch settling theorem was found in these search results. This is a limited search, not proof of absence. The phase comparison below is an elementary order argument derived here; no priority claim.


### GPT waiting-budget and branch-tree check (2026-10-06 04:37 BST)

The source for the backward-reading argument is this project's RULE30-PRIZE.md Lemma B2, checked directly; the reset/extension mechanism is Rowland section 5, previously read in full. G7 states elementary quantitative consequences without claiming priority. Searches `"rule 30" "left side" "graph" period` and `"rule 30" "left side" "settling time"` found Rowland and a [2011 shift-subsystem paper](https://content.wolfram.com/sites/13/2019/01/20-1-3.pdf) (search result only, not read or used), alongside irrelevant results. No applicable all-branch sub-3 waiting bound was found in this limited search. G7's interval diagnostic applies existing evidence, not a new imported theorem.


### GPT finite local front potential (2026-10-06 04:49 BST)

G8 applies G7's unique-predecessor graph and G6's reset clock. The cycle obstruction and telescoping inequality are proved directly in G8. The graph/potential method is standard, not claimed novel. During this block, a search `Karp 1978 characterization minimum cycle mean digraph pdf Berkeley` located the [original Berkeley technical report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1977/ERL-m-77-47.pdf) and its [published abstract](https://www.sciencedirect.com/science/article/pii/0012365X78900110), which describes weighted cycle means and their algorithmic characterization. The archive PDF fetch returned403; the Berkeley EECS fallback succeeded and its full six-page text was read, including Lemma1's removal of negative cycles and Theorem1's characterization. Negating weights gives the corresponding maximum-reward statement used here. G8's specialized cycle traversal and reverse relaxation are not Karp's algorithm. The complete edge inequalities certify the result independently. No prior-art claim is made for the Rule 30 cycle or potential.


### GPT birth-restart transfer (2026-10-06 06:26 BST)

G9 uses elementary order distributivity: a monotone scalar map preserves finite maxima. No novelty claim for the maximum-over-restarts argument. Searches `Lindley recursion maximum partial sums workload queue lecture notes pdf`, `site.mit.edu Lindley recursion max partial sums pdf`, and `site.inria.fr max plus monotone maps distributivity maximum queue recursion` located reflected queue recurrences and max-plus methods. Read the publisher page of [Boxma et al., A multiplicative version of the Lindley recursion](https://link.springer.com/article/10.1007/s11134-021-09698-8), including its description of the classical queue special case, and the abstract only of [Akian and Fodjo, Probabilistic max-plus schemes for solving Hamilton-Jacobi-Bellman equations](https://arxiv.org/abs/1801.01780), which explicitly identifies distributivity of monotone operators with respect to suprema as a mechanism. Neither source supplies the Rule30 budget. Our nonlinear next-black maps are not asserted to be the classical additive Lindley recursion or globally max-plus linear. The scalar finite-maximum identity and its birth-budget consequence are proved directly in G9; no full-text priority survey was made.


### GPT aligned finite certificate audit (2026-10-06 06:35 BST)

G10 uses only mechanisms already read and credited in G7–G9: the project's unique predecessor, the maximum-cycle reward/potential argument (Karp report read in G8), and the temporal-rotation quotient proved in G9.4. Searched the repository for cycle means, potentials and aligned fronts before starting; no P6/P7 or P10 certificate was already recorded. No new external result or new literature priority is asserted. The additional periods test an existing candidate rather than import a new route. Exact edge inequalities and scalar witness checks establish the finite statements independently.


### GPT Condrey-end full reading (2026-10-06 07:05 BST)

Read all seven pages of [Condrey, Finite Configurations Cannot Generate a Constant Trace in Rule30](https://arxiv.org/pdf/2609.09431): triangular uniqueness; zero-trace invariant classes and OR latch; all-one checkerboard; finite-support corollaries; horizon proofs; conclusion and partial formalization limits. G11 distinguishes its zero-wall latch from its one-wall universal fibre. The one-hole prefix follows by applying the latter on the first black window and explicitly solving one inverse step; no novelty claim. Searches `"Rule 30" "one zero" periodic trace Condrey` and `"Rule 30" constant trace checkerboard preimage periodic holes`, restricted to arXiv and Rowland's site, returned Condrey, Rowland and other Rule30 papers but no exact repeated-hole budget usable here. This is a limited search, not proof of absence. Nersissian's period paper reappeared and was already listed in this document as abstract-only; it was not imported into this proof.

### 2026-10-06 — GPT G12, local hole shielding and the input time

Used the already-read Condrey triangular uniqueness and black-wall checkerboard (full reading recorded under G11), and the project's RULE30-PRIZE.md §8.2 Lemma4, rather than proposing a new ray or superposition route. G12's four-black-window shielding is a direct inverse-recurrence consequence of G11's first four cells; no independent priority claim. Local's C021 exploratory negative is retained: spreading on an earlier row differs from shielding on the injection row. This bounded algebraic audit did not conduct a new literature survey or import an external global propagation theorem.

### 2026-10-06 — GPT G13, synchronizing automata for a single inverse row

The project's §8.19 already reconstructs Rule30 preimages leftwards; G12 supplies injection-row agreement. Searches `"Rule 30" inverse synchronizing automaton` (arXiv/Complex Systems) and `synchronizing automaton reset word definition` (arXiv) returned Rowland's local nested-structure paper and general synchronization literature, but no directly usable Rule30 inverse-row reset-gap theorem. This limited search is not a novelty or absence claim. Opened [Maslennikova2014](https://arxiv.org/abs/1405.3576), **abstract only**, for the standard definition of a reset word; none of its complexity theorems was imported. G13 directly proves the four-state transitions and regular reset language, retaining a false first characterization. Survey results about random automata were not applied to this deterministic driver, and no uniform reset gaps were assumed.

### 2026-10-06 — GPT G14, extending the project's latch count

Read RULE30-PRIZE.md §8.2's Pell full-column count and Fibonacci visible language, §8.62/C022's white-wall latch and independent-shape bound, and the width-one golden-ratio control in `rule30_entropy.py`. G14 extends those elementary local rules to wall0^(p-1)1 with an exact two-state transfer matrix; the p2 case is credited as an existing result. No new external theorem, random-information hypothesis, or literature priority claim was imported. It is a bounded audit of the recorded mechanism, not a new global route or a substitute for Local's larger-width automaton.

### 2026-10-06 — GPT G15, arbitrary white-time gaps in the existing width-one envelope

Used RULE30-PRIZE.md §8.2's local constraints and known Fibonacci visible language, G14's exact latch count, and the project's width-one layer interpretation. G15 gives the elementary projected language for arbitrary white-time gaps by explicitly constructing each hidden interval; no new external theorem was invoked. The golden-ratio gap2 case is credited as known; gap>=3's full visible shift is only a one-layer relaxation, not a physical channel or prize claim. This is a bounded audit of the existing mechanism, with no claim of literature priority.

### 2026-10-06 — GPT G16, four-state refinement of the existing layer

Used the project’s layer update (`ladder.c`, §8.14/§8.20), §8.2’s known Fibonacci visible language, and G15’s width-one envelope. G16 directly composes the four-state relations and proves their eventual two-periodicity, rather than importing an external theorem or asserting novelty. It is a bounded audit of the same mechanism. The finite-state transducer distinction in C030 is proved in G16.3; no arbitrary driver was assumed to have a regular prefix language.

### 2026-10-06 — GPT G17, finite certificate in the existing right layer

Read the project’s layer definition, G16’s parity certificate, and the existing §8.20 projection machinery. G17 directly verifies the eight-state black relation and accepting subset graphs, proving equality of width-two/three languages. No external theorem or priority claim is imported; this is a bounded refinement and negative of the existing layer question, not a new global prize route.

### 2026-10-06 — GPT G18, auditing C032’s slow-switch proposal

Used Lemma1/§8.2’s future black-window checkerboard, G13’s inverse reset, G15’s latch language and C032/§8.63’s slow-wall proposal. G18 directly composes the existing inverse rule to certify a finite prefix and protected band. No new external theorem or priority claim is imported. The proposed complete per-period finite state is not assumed: a valid width-one tail counterexample identifies the missing closure premise.

### 2026-10-06 — GPT G19, balanced-latch finite-prefix obstruction

Used §8.2’s monotone right latch, G18’s exact prefix construction and C032’s slow-wall question. G19 directly lists all six prefixes for0^5 1^5 and independently evolves the64 small left seeds. This is a finite-window certificate, not a new global route or literature priority claim. No external theorem or asymptotic law was imported; the all-a support observation remains finite evidence.

### 2026-10-06 — GPT G20, another finite relation certificate in the existing layer

Used the existing layer definition (§8.14/§8.20, ladder.c), G16/G17’s subset-language proof and CONSTELLATION row16’s p5 question. G20 directly verifies a sixteen-state relation identity and extends six representative odd-period graphs to all odd p>=5. No external theorem or priority claim was imported; this is a bounded negative on the first restrictive width, not an assumed infinite-layer construction.

### 2026-10-06 — GPT G22, formalizing the recorded inverse-column rule

Used the inverse-column equation in CONSTELLATION row5/§8.36 and distinguished G7’s anti-diagonal predecessor coordinates. G22 directly constructs the image condition, fibres and finite-neighbourhood ternary recoding; no external entropy or CA classification theorem is imported. It claims no literature priority. A broader study of the induced CA still needs the standing literature check; the current result is a bounded algebraic formalization of the recorded rule.


- 2026-10-06, GPT G26 scope audit: Kopra (2023) Definition3.3/Corollary3.7 require left-spreading together with left-permutivity; Rule210 satisfies both. The Rule210 empty-left walled parity subsystem is Rule90; its return-path derivation uses standard Catalan decomposition, with binary generating series C(z)=1+z*C(z^2). These mechanisms are credited rather than proposed as new. Full-orbit compatibility remains separate.

- 2026-10-06, GPT G27: automatic-sequence terminology from Allouche/Shallit (2003), publisher extracts only, https://www.cambridge.org/core/books/automatic-sequences/B092437A099192BA22DE4CF638142558/listing . Three-state dyadic DFA derived directly, no novelty claim. Half-line obstruction reuses Jen/Kopra's zero-height periodic propagation with the boundary source of a left1 explicit; no assumed right-half realization.

- 2026-10-06, GPT G29: independently read Dubickas2009 Theorem5 and its proof (positive integers tending to infinity), https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C40C0C07FEC20797475BB2899C436C9A/S0017089508004655a.pdf/on_integer_sequences_generated_by_linear_maps.pdf . The signed fixed-odd-denominator bound is the project's credited extension of the same divisibility/growth argument; exact rounding and cycle/interval controls are audits, not a novelty claim.

### Rule 30 on rings: what is tabulated (checked 2026-10-06, Local, for CONSTELLATION.md row 10)
- OEIS A334497, "Maximum value of eventual period for any starting configuration for a rule 30 cellular automaton in
  a cyclic universe of width n": 1, 1, 1, 8, 5, 1, 63, 40, 171, 15, 154, 102, 832, 1428, 1455, 6016, 10846, 2844,
  3705, 6150 (n = 1 .. 20). OEIS A334496, the period reached from the single cell: 1, 1, 1, 8, 5, 1, 4, 40, 72, 15,
  154, 102, 260, 1428, 1455, 6016, 10846, 2844, 247, 3420.
- NKS note 6.4 ("Periods in rules 30 and 45"): the single cell is not always the seed of the longest cycle (n = 13:
  832 against 260); a growth estimate near 2^(0.61 (n + 1)) for the maximum period appears in Wolfram's random-
  generator patent (US 4,961,159).
- Not found in the OEIS (searched "rule 30" with cycles / periodic / transient): the number of cycles by n, the
  number of states on cycles, the longest transient, or the gliding (rotation-invariant) cycles. `ring_census.c`
  computes all four exactly to n = 24.
- Triangle-size statistics (checked 2026-10-06): NKS note 6.1 ("Properties of initially random cellular automaton
  patterns"): "The density of triangles of size n goes roughly like 2^-n for rules 126, 30 (see also page 871), 150
  and 182 and roughly like 1.3^-n for rule 22", for random initial conditions, with no constant and no derivation.
  The 1984 Physica D paper is a scanned PDF (fetched; not text-extractable here; its text was not read). So the
  ratio one half is known approximately; the exact law 3 * 2^-(L+4) per cell from the invariant uniform measure,
  and its 0.1% match on the single cell's core (section 8.68), were not found. Page 871 of NKS is still to be read.



**2026-10-06 10:55 BST — GPT primary-source access update (G36).** The [Monks–Yazinski author PDF](https://monks.scranton.edu/files/pubs/AutoConjV13.pdf) is accessible despite the publisher403. Read the definition of Omega, Theorems2.1/2.7(b) and relevant proof portions, not the full paper. The rational divergent-orbit lower-density bound now has firsthand verification; global rationality preservation of the complement autoconjugacy is conjectural and equivalent to rational-orbit periodicity. G36 retains the square-zero route's limitation. This updates the earlier secondary-only/PDF-unavailable scope, without erasing that historical report.

### Collatz circuits (checked 2026-10-06, Local, for GPT's G47)
- R. P. Steiner, "A theorem on the Syracuse problem", Proceedings of the 7th Manitoba Conference on Numerical
  Mathematics and Computing (1977, published 1978), 553 to 559: there is no nontrivial 1-cycle (a "circuit": one
  run of odd steps followed by one run of even steps). Generalised by J. Simons and B. de Weger (2005) to m-cycles
  for small m. Found through the secondary literature (Lagarias's annotated bibliography); the paper itself not yet
  read. It closes G47's open clause: G47's surviving family members are circuits, so only k = 1 qualifies.



### 2026-10-06 — GPT G48: first-deficit scope and adjacent-swap prior art

[Primary author paper, Rozier–Terracol, arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2), Definition1.2 and Lemma2.1/proof read. The first-deficit census probes Terras's coefficient-stopping-time equality; the paper also supplies the known affine adjacent-swap comparison used in G40. Targeted reading only; original Terras PDF download failed. See RULE30-GPT.md G48 for scope and the retained small-start exception.

**2026-10-06 — GPT G50 primary-source scope update.** [Kari–Kopra, arXiv:1710.05737v1](https://arxiv.org/html/1710.05737v1): introduction, canonical base expansions, Lemma2.1/proof, base-six local-rule construction and trace Definition3.2/Corollary3.3 read. The full-alphabet local rule is not left-permutive; broader expansivity and selected real configuration realization must be checked separately. G50 specializes the already recorded decoupling mechanism; no novelty claim or whole-paper audit.

**2026-10-06 15:41 BST — GPT Collatz first-deficit envelope audit (G67).** Re-read [Rozier–Terracol arXiv:2502.00948v2](https://arxiv.org/html/2502.00948v2), Definition1.2, Lemma2.1 and Theorem2.2 with proof, not the whole paper. Actual/coefficient stopping-time equality is a conjecture for n>=2. The source's offset extrema range over unrestricted parity words. G67 conditions the same affine sum on the first-deficit barrier; its latest allowed odd positions are derived explicitly, with no novelty claim. No larger first-deficit census or external computational verification was audited.


**2026-10-06 — GPT G69 logarithmic-source audit.** Read [Rozier–Terracol v3](https://arxiv.org/html/2502.00948v3), Definition1.2 and Section6 around Proposition6.3: source-attributed Rhin exponent13.3 is unconditional; their later finite-total argument uses additional orbit conjectures. Original1987 Rhin proof not read. Read [Languasco–Luca–Moree–Togbé Theorem2.1](https://link.springer.com/article/10.1007/s12188-025-00293-9), positive rational Matveev statement and its prime-power-gap application. G69's barrier-conditioned polynomial ceiling is a direct synthesis, no novelty claim.

**New related preprint, audit required.** [Tong Niu, arXiv:2605.13886v1](https://arxiv.org/html/2605.13886v1), introduction and Sections3–4 sampled. It discusses fixed-length affine counting, overlapping G45's elementary residue/ceiling formulation. Displayed text defines r_w as normalized E, then inserts it as an integer intercept in the affine formula; those conventions differ by2^k. Its offset-bound proof also attributes the unrestricted maximum to ones-then-zeros, contrary to Rozier–Terracol Theorem2.2. The exact1100/0011 example gives B5/20 at a2,t4 and exposes that attribution reversal. These are specific textual normalization/order flags, not a complete refutation or audit of the manuscript. No count or acyclicity adjustment is imported from it.


### GPT G74 — backward first-step analysis, 2026-10-06

Existing-record search `adjoint`, `Duhamel`, `completion probability`, `backward kernel` found no earlier Collatz backward-completion identity in this record. Web searches `Markov chain perturbation telescoping finite horizon backward transition kernel Duhamel formula` and `site.maths.cam.ac.uk Markov chains backward equations discrete time transition probabilities lecture notes` located general perturbation work and teaching notes. Read [Chen's University of Washington lecture3](https://faculty.washington.edu/yenchic/18A_stat516/Lec3_DTMC_p1.pdf), section3.4 (pages5-6), which derives backward equations by conditioning on the first transition. G74 applies that elementary method to a killed, time-dependent fair-coin barrier and proves its finite telescoping identity directly. No published Collatz cancellation estimate is imported; no novelty claim or exhaustive prior-art search. The actual deterministic ensemble is not assumed Markov on odd counts.


### GPT G75 — binomial concentration and a dependent overshoot, 2026-10-06

The search `Hoeffding 1963 probability inequalities sums bounded random variables theorem 2 pdf` located [Hoeffding's original paper](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf) and its [publisher abstract](https://www.tandfonline.com/doi/abs/10.1080/01621459.1963.10500830). Only the search metadata and abstract excerpt were inspected, not the full paper. No general theorem from that paper is imported: G75 proves the required fair-binomial concentration estimate by its elementary cosh moment-generating function, and proves the central-atom estimate by induction. The reverse maximum and dependent truncation are derived directly from G74. No novelty claim, exhaustive literature claim, or independence of overshoot and endpoint count.


### GPT G78 — finite product-measure differentiation, 2026-10-06

Search `Russo formula derivative probability increasing event expected number pivotal original paper pdf` located [Grimmett's author-hosted Probability on Graphs draft](https://www.statslab.cam.ac.uk/~grg/books/pgs2e-draft.pdf), indexed section4.7, theorem4.66. Its search excerpt identifies the derivative as the mean number of pivotal coordinates for increasing events. Opening the PDF and locating that theorem failed with502; the full theorem was not read, and original Margulis/Russo papers were not audited. G78 directly differentiates its finite polynomial and separately differentiates each tail coordinate, so it imports no probability theorem. No novelty claim or assertion about actual Collatz class allocation. The method is the standard finite increasing-event sensitivity identity.


### GPT G82 — truncating a reverse maximum in time, 2026-10-06

Search `random walk maximum negative drift truncation anti concentration convolution binomial` located [Kugler and Wachtel's author preprint abstract](https://arxiv.org/abs/1107.5400), describing truncation methods for maxima of negative-drift walks. Only the search abstract excerpt was read; no theorem or constant was imported. G82 proves its bounded fair-bit coupling error directly with G75's tail estimate, then proves the binomial first-difference estimate by convolution and unimodality. Its moving ceiling barrier is handled explicitly. No novelty claim, exhaustive search claim, or transfer of iid assumptions to actual Collatz inputs.


### Owner's temporal-instrument connection — publisher abstracts checked, 2026-10-06

To situate the origin in WHAT-WE-BUILT.md, read the publisher abstract of Westerweel, Elsinga and Adrian, [Particle Image Velocimetry for Complex and Turbulent Flows](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-120710-101204), Annual Review of Fluid Mechanics 45 (2013). It describes time-resolved vector-field capture and discusses finite accuracy and spatial resolution; full text was not read. Also checked the publisher abstract of [3D Lagrangian Particle Tracking in Fluid Mechanics](https://www.annualreviews.org/content/journals/10.1146/annurev-fluid-031822-041721), volume 55 (2023): tracking individual particles provides position, velocity and acceleration. This supports the distinction between field changes at fixed locations and motion followed along trajectories. It does not establish equivalence of this project's video tracker to a calibrated PIV/LPT instrument, a performance or novelty claim, or a theorem about Rule 30. The discrete moving-frame identity proposed in the chat is elementary and will need its own scope audit before research use.

### GPT G98 — clock and causal-diamond scope audit, 2026-10-06

Read the abstract of Saravani and Aslanbeigi, [On the Causal Set-Continuum Correspondence](https://arxiv.org/abs/1403.6429): it treats number-volume correspondence and distinctions between small regions, sprinklings and large-volume lattices. No theorem from the full text was imported. Read the abstract/introduction of Baburin et al., [Universality Frontier for Asynchronous Cellular Automata](https://drops.dagstuhl.de/storage/00lipics/lipics-vol345-mfcs2025/html/LIPIcs.MFCS.2025.11/LIPIcs.MFCS.2025.11.html), MFCS2025: asynchronous simulation can use additional state, so a raw-update noncommutation guard must not be recast as impossibility of asynchronous simulation. G98's continuum Jacobian, discrete count, global-clock invariance and raw Rule30 update counterexamples are derived directly. No physics or novelty claim.

### Local — unequal ticks and asynchronous updating (the owner's question, CONSTELLATION row 19), 2026-10-06

Read via search summaries only, not the papers; status: pointers to read before any asynchronous run.

- **Nakamura (1974), asynchronous cellular automata and their computational ability.** Any synchronous $q$-state
  rule can be simulated by an asynchronous rule with the same neighbourhood and $3q^2$ states: a cell that has
  updated waits until its neighbours have caught up before its next transition, so it always reads the right
  generation. This is the classical form of GPT's G089 and G090 "versioned prior-generation reads": the synchronous
  history survives any schedule once each update reads the previous generation. Survey with the construction:
  Fatès, [A guided tour of asynchronous cellular automata](https://arxiv.org/abs/1406.0792).
- **$\alpha$-asynchronous elementary rules** (Fatès and co-authors, 2005 onward; Fatès, Thierry, Morvan and
  Schabanel, fully asynchronous double-quiescent rules, Theoretical Computer Science 2006): each cell updates with
  probability $\alpha$ per step; for some rules the behaviour changes abruptly as $\alpha$ varies, a second-order
  phase transition in the directed-percolation or parity-conserving class. What Rule 30 itself does under
  $\alpha$-asynchrony was not found in the summaries; to be read before any run.
- **Time Warp** (Jefferson's optimistic parallel discrete-event simulation) has been applied to simulations with
  asynchronous cellular automata ([core.ac.uk record](https://core.ac.uk/works/44253136)): processors run ahead on
  their own clocks and roll back when a late message arrives, which is the engineering form of the owner's unequal
  ticks with the synchronous history preserved.

Links: https://arxiv.org/abs/1406.0792 ; https://arxiv.org/pdf/2501.02578 ; https://en.wikipedia.org/wiki/Asynchronous_cellular_automaton ;
https://core.ac.uk/works/44253136 ; https://arxiv.org/abs/nlin/0703044

### GPT G104 — oriented random updates and spatial measures, 2026-10-06

Searched for asynchronous one-sided updates and invariant Bernoulli measures. Read the publisher abstract of Mairesse and Marcovici, [Probabilistic cellular automata and random fields with i.i.d. directions](https://www.numdam.org/articles/10.1214/12-AIHP530/), AIHP2014: it concerns synchronous probabilistic local updates and product invariant measures. Its update assumptions differ from our sequential raced-neighbour recursion; no theorem was imported. The search also returned [Orbits of the Bernoulli measure in single-transition asynchronous cellular automata](https://dmtcs.episciences.org/en/articles/2972); the page failed to fetch, so only its search excerpt about cylinder measures was read. G104 proves its oriented conditional inverse and first-row pair formula directly, with no novelty or exhaustive prior-art claim.

### GPT G105 — boundary and healing scope, 2026-10-06

Existing-record checks included RULE30-PRIZE.md §8.66 and PROOFS.md C.4 on background-dependent healing. Read the perturbation-wave section of [Formation of Morphogenetic Patterns in Cellular Automata](https://pmc.ncbi.nlm.nih.gov/articles/PMC7304752/): it already discusses Rule30's right-moving perturbation border and boundary-dependent recovery of periodic backgrounds. These are known mechanisms, not new discoveries here. G105 directly counts zero-row preimages in the finite cyclic snapshot/race implementation; no literature theorem or novelty claim is imported. The search is limited, not an exhaustive novelty audit.


### Projected memory and G112 (GPT, 2026-10-06)

Search: “Markov chain lumpability conditional past projected process criterion Kemeny Snell paper”. Read the abstract and metadata of Geiger and Temmel, [Lumpings of Markov chains, entropy rate preservation, and higher-order lumpability](https://arxiv.org/abs/1212.4375), revised2015. The abstract defines coordinate-wise projections and strong k-lumpability, with finite-state entropy criteria. Only the abstract was read. Projected Markov memory and higher-order lumpability are existing theory; those finite-state criteria are not invoked as an infinite-Rule30 theorem. G112 instead uses direct conditional probabilities, a local OR shielding identity and positive finite cylinders. Existing G102-G111 already supply masking, pulse echo and the finite table; no general theory novelty is claimed.


### GPT G131 — Sturmian block factors and orbit endpoints, 2026-10-06

Searched finite block coding of rotations with endpoints on one orbit. Read the publisher abstract of Kupsa and Starosta, [On the partitions with Sturmian-like refinements (2015)](https://www.aimsciences.org/article/doi/10.3934/dcds.2015.35.3483). It treats rotation partitions whose atoms are finite unions of half-open intervals with endpoints on one past orbit, and discusses stronger refinement/factor results. Only the abstract was read. G131 does not import those refinement or injectivity theorems: it constructs the finite XOR code directly and transfers the already proved Rule 30 repeat obstruction. These coding ingredients are established symbolic dynamics; no general coding novelty or exhaustive prior-art search is claimed.


### GPT — half-circle codes and the XOR-derivative bridge, 2026-10-07

Targeted record search for Rote, half-circle, antiperiod and Sturmian integration found no matching entry. Web query: “Rote sequences difference Sturmian sequences rotation half circle paper”. Read the abstract and introduction (printed pp.125–126) of Medkova, Pelantova and Vuillon, [Derived sequences of complementary symmetric Rote sequences](https://www.numdam.org/item/10.1051/ita/2019004.pdf), RAIRO 53 (2019), DOI10.1051/ita/2019004, also [arXiv1812.03748](https://arxiv.org/abs/1812.03748). The introduction states the known half-circle rotation construction and the equivalence between complementary symmetric Rote sequences and sequences whose modulo-two difference is Sturmian, crediting Rote. No later return-word theorem or algorithm was imported. GC158 tests only the elementary repetition transfer: the derivative loses the distinction between repeats and complement-repeats. This does not extend the Rule30 Sturmian exclusion to these codes.

## openai/math: a released collection of model-proved manuscripts (noted 2026-10-07, by Cloud)

[openai/math](https://github.com/openai/math), first commit 2026-10-06: 722 manuscripts (372 families) by an
unreleased OpenAI model, 162 with Lean formalisations, the rest at varying stages of verification. Read here: the
README and the catalogue (CONTENTS.md), not the proofs. Its claims on the prize pool are listed in PRIZE-PROBLEMS.md
§1, update of 2026-10-07.

For this record. No manuscript concerns Rule 30, elementary cellular automata, Collatz, Mahler's 3/2 problem, or
linear forms in log 2 and log 3 (the Collatz lane's G69 rests on Rhin's bound for those). Two are near neighbours.
Family 197 refutes Gottschalk's surjunctivity conjecture with an injective, non-surjective cellular automaton on a
nonsofic group; the integers are amenable, where the Garden of Eden theorem makes every injective automaton
surjective, so Rule 30 on a line is untouched. Family 017 proves that the irrationality exponent of π is exactly 2
(with Lean), a far sharper form of Lambert's 1761 theorem that π is irrational (the owner's question of 2026-10-06).

Use. Treat each manuscript as a preprint: prefer the Lean-formalised ones, check the main statement in the formal
file rather than the abstract, and cite the family number and manuscript title.


### GPT — Rote exponent comparison for the phase-zero repeat debt, 2026-10-07

Query: “Rote sequences critical exponent continued fractions parity numerators initial repetitions silver ratio”. Read only the abstract of Dvorakova, Medkova and Pelantova, [Complementary symmetric Rote sequences: the critical exponent and the recurrence function](https://arxiv.org/abs/2003.06916), DMTCS22(1), 2020. It gives continued-fraction formulas and a classification at critical exponent at most three. That ordinary factor exponent does not include our interval starting index a, so neither its classification nor the reported uncountability transfers to G144's boundary-phase debt. No paper theorem was imported; the G144 first-hit obstructions and converse are written out independently. No exhaustive novelty claim.

Independently read the current [openai/math README](https://github.com/openai/math), confirming that it presents manuscripts with differing verification status and warns of possible issues in unformalized results. This check does not verify any of CL010's headline mathematical statements or Lean artifacts. Local's catalogue-only Q7 scan is accepted separately; no mathematical result from the release is used here.

### Local — catalogue-only scan of openai/math for question 7, 2026-10-07

Scope, as GC161 set it: the release's `CONTENTS.md` only (all 372 family headers and every manuscript abstract
listed there), no proofs and no Lean files read. Keywords: Sturmian, Rote, rotation codes, mechanical and Beatty
words, balanced words, repetitions and critical exponents, three-distance, symbolic dynamics and subshifts,
cellular automata, combinatorics on words, inhomogeneous approximation. Result: no family or abstract is about
Sturmian, Rote or rotation codes, repetitions, critical exponents, subshifts or cellular automata on the integers, so
nothing in it helps question 7. Recorded and stopped. The three nearest, none usable:

| Family | Main statement, as the catalogue gives it | Formal artifact | Why it does not help |
|---|---|---|---|
| 022 | The weak inhomogeneous Duffin–Schaeffer conjecture: divergence of the totient-weighted series gives infinitely many solutions of the shifted approximation inequality for almost every x | no Lean link in the catalogue | a statement about almost every angle; our half-circle questions are about specific quadratic angles and fixed phases |
| 017 | The irrationality exponent of pi is 2 | Lean link in the catalogue | an exponent for one constant, not a method stated for rotation codes |
| 197 | A torsion-free nonsofic group algebra that is not directly finite; companion examples give injective nonsurjective cellular automata, refuting Gottschalk's surjunctivity conjecture | Lean link for the family; which statement it formalises was not checked | needs a nonsofic group; on the integers the Garden of Eden theorem holds (Cloud's CL010 reading confirmed against the catalogue) |

### GPT — periodic-predecessor parity, 2026-10-07

Query: “rule 30 periodic preimages period doubling synchronizing runs modulo 3”. Read the abstract and section 5 opening/proposition and proof of Eric Rowland, [Local Nested Structure in Rule 30](https://ericrowland.github.io/papers/Local_nested_structure_in_rule_30.pdf), Complex Systems16 (2006). Its period-doubling result concerns temporal diagonals in a left-justified evolution. G150 concerns spatial predecessors of a prescribed periodic row and derives its zero-gap criterion from the already recorded inverse transducer; no diagonal theorem is imported.

Also read only the abstract of [Diagonal Periods and Newton Supports of Rules 30, 86 and 135](https://arxiv.org/abs/2609.25077), submitted September2026. It claims unbounded single-seed diagonal periods and a backward periodic-tail map. The manuscript proof and relationship to G123/G124 or the wall route have not been audited. No result from it is used, and no novelty or exhaustive-search claim for G150 is made.

### GPT — diagonal-profile boundary audit, 2026-10-07

Read section 4 through Theorem13 of [Nersissian, Diagonal Periods and Newton Supports of Rules30,86 and135](https://arxiv.org/html/2609.25077v1). Checked the reset/integration argument and the finite-state first-hit proof. The latter counts absolute-time periodic profile pairs: a zero boundary is fixed and a nonzero boundary pair maps into it. Different transient lengths do not invalidate taking large times in each residue class. This shares G123's absorbing-orbit pigeonhole method, but follows temporal diagonal profiles rather than spatial ancestor rows.

**Unexpected map check, by hand.** Its backward map is B(u,v)=(S v XOR (u OR v),u). Our vertical inverse is H(a,b)=(S a XOR (a OR b),a), as in G128/G129. The shift acts on different coordinates. On constant tracks, B(0,1)=(0,0), whereas H(0,1)=(1,0) and H(1,0)=(0,1). Thus the same nonzero pair is absorbed in B and cycles in H; even their constant-track graphs are not conjugate. No wall conclusion or novelty claim is imported. The remaining manuscript, its numerical data and support representations were not audited here.

**GPT follow-up to Local L107 (2026-10-07).** The constant-track guard excludes even an injective encoding between these two full pair spaces that intertwines their depth maps and commutes with, or reverses, temporal shift. A shift-fixed pair must map to a shift-fixed pair. There are four such pairs on each side; injectivity makes the restricted map a bijection, hence a conjugacy of the two four-state depth graphs. Their periodic-point counts, one for B and three for H, contradict this. No continuity or local-code assumption is needed. This strengthens the failed faithful-identification route, not a general ban on transfers. The identified unexpected countercheck is the non-injective map sending every pair to (0,0): it intertwines both depth maps and respects shift in either direction. It carries no nonzero boundary information. Any useful factor-map bridge would therefore need an explicit boundary-preservation hypothesis, not just shift compatibility. This is an elementary audit of the recorded maps, not an imported theorem or a new numerical experiment.

### GPT — rotation-quotient first-hit bound, 2026-10-07

Read the abstract of Frati, Petak and Cheney, [Networks of Binary Necklaces Induced by Elementary Cellular Automata Rules](https://arxiv.org/abs/2409.04780) (2024): quotienting cyclic CA states by rotation is established, not a new method here. Their full paper and data were not inspected. Also read Klaus Sutner’s [Moebius Inversion lecture notes](https://www.cs.cmu.edu/~cdm/resources/24-moebius.pdf), pages5–8 and12–14, for divisor inversion, primitive words and necklace counts. G152 combines these standard counts with the recorded G124 period classification and a self-contained absorbing-orbit argument; no source theorem about Rule30’s zero basin is imported. Search “Rule30 zero periodic configurations necklace transient bound” located the necklace-network paper but no checked exact bound of this form. This is a limited search, not evidence of novelty.

### GPT — Rudin–Shapiro logical repeat-filter lane, 2026-10-07

Read Shallit and Xu, [Repetition factorization of automatic sequences](https://arxiv.org/html/2311.14961v2), section2 through Theorem2 and its repetition-predicate construction; also section6's stated Rudin–Shapiro result and proof outline. The cited first-order decision theorem covers addition, comparison, quantifiers and sequence indexing. Their repetition-factorization widths are not the project's start-index repeat debt, and no factorization theorem is imported as an exclusion. The RSP formula is an application of the standard method, not a novelty claim. Searches for Rudin–Shapiro repetitions and Walnut found this primary source and Rampersad–Shallit's summatory-function work; the latter's proof was not read or used here.

**RSP tool provenance.** Used the official [Walnut7.1.0 source](https://github.com/Walnut-Theorem-Prover/Walnut/tree/67e69c248d07324b25de1d4a498e877ac504999a), pinned before runs, and its supplied RS output automaton. The source was built in an isolated temporary toolchain. G153 records the exact formula, relation hash, instrument controls and independent product replay; semantic review remains pending. A raw tool decision is not claimed as an independently verified proof.

**G154 scope and method (2026-10-07).** This adapts the existing G147 countable/dense phase argument to a minimal symbolic trace family, using G140's reviewed coding and radius clock. The Rudin–Shapiro substitution is derived directly from its binary digit recurrence; bounded-gap minimality and nonperiodicity are proved in the entry, not imported from an unread substitution theorem. Countability, atom propagation and the isolated-point argument are elementary. No novelty is claimed for those general dynamical facts, and no generic exclusion is treated as exclusion of the specified original word.

**RSP verification update (2026-10-07).** Local L111 audits the direct LSD reconstruction and debt comparator and independently replays them, discharging G153's dependency on Walnut compilation semantics. The standard automaton method remains prior art. G153 is a reviewed computer-assisted necessary-filter pass, not a finite-wall construction.

**G155 method/scope (2026-10-07).** The two-supertile count is proved directly from G154's length-two four-letter substitution; no exact published Rudin–Shapiro factor formula is asserted or needed. This applies elementary factor counting to the reviewed wall-prefix locality, improving G147/G154's fixed-radius exception bound. It does not infer positive entropy or specified-word exclusion.

**G156 edge-diagonal correction of scope (2026-10-07).** Re-read section4 through Theorem13 of [Nersissian's paper](https://arxiv.org/html/2609.25077v1). Its B(u,v)=(S v XOR (u OR v),u) matches G7's diagonal-tree predecessor exactly. The previous comparison to the vertical wall inverse H remains valid: they shift different coordinates. The paper's absolute-profile bound therefore has a direct diagonal interpretation, without a wall conjugacy. G156 combines that existing first-hit mechanism with standard four-letter necklace counting, derived in the proof; no paper result is imported as a waiting-time or vertical-wall theorem. The theorem's record-spacing question remains open. Sections4.3-4.4 were inspected for scope: their finite support representations depend on actual period/transient sizes, and the formal milestone polynomial is explicitly not identified with a physical diagonal. Neither is used as a uniform bound.

### GPT — exact Rudin–Shapiro factor complexity, 2026-10-07

Read Allouche and Shallit, [Complexité des suites de Rudin-Shapiro généralisées](https://www.numdam.org/item/JTNB_1993__5_2_283_0.pdf), Journal de théorie des nombres de Bordeaux5(2),1993, printed pages285-288, section2 through Proposition2 and the small-length table. Theorem1 gives P_r(k)=8k-8 for k>=8. The four-letter substitution and binary coding match G154 after a'=c,b'=d; d=1 is the adjacent-11 parity word. Rendered formulas were checked because extracted text omitted inequality signs. The length-eight base enumeration is accepted as part of the published proof, not rerun. The later generalized-sequence proof was not read or imported. G155's application is N_(X_r)(L)<=8*ceil(L/2)-8 for L>=15; it counts possible exceptions rather than deciding existence. The paper's table at k=7 gives46, which is an explicit guard against extending the affine formula to all lengths. No new factor census.

**G157 finite-tree transfer (2026-10-07).** Re-read [Nersissian section4, Theorems10-12](https://arxiv.org/html/2609.25077v1): active drivers reset and preserve a common period, inactive drivers integrate with a possible doubling, and initialized diagonal tails have dyadic periods. G157 proves this mechanism for arbitrary two-sided periodic rooted histories and derives equality of the period-P and period-2^v2(P) trees. This is a finite-tree corollary and scope transfer, not novelty claimed for the underlying dyadic-period theorem or a physical-transient bound.

**G158 quotient branching (2026-10-07).** The reset/integration mechanism already checked in Nersissian section4, Theorems10-12, supplies the scalar recurrence classification. G158 adds the parent-stabilizer argument for child rotation orbits and the elementary finite-tree leaf count. Existing G152 concerns a spatial transition quotient that may merge, not this rooted edge tree. No literature novelty claim is made for integration or tree counting.

**Temporal-difference reformulation (2026-10-07).** Read [Nersissian section2.3, Theorems1 and4](https://arxiv.org/html/2609.25077v1), on the highest surviving Newton index, exact dyadic period, and finite-difference companion order. The G158-G161 source addendum derives the cyclic operator identities directly and uses them to restate the reviewed zero-driver parity test. This is standard GF(2) difference algebra; no novelty or new rooted absence theorem is claimed. Formal polynomial lifts of physical transients are not imported.

**Existing-record correction (2026-10-07).** G2.3 already derives the reset/even-parity classification and certifies the first genuine period16 split at diagonal53208, with an independent spatial-update check and disjoint cycles. G158 and G161 restate that mechanism in rooted-tree/orbit terms; the first branch is not new or unresolved. FBR16's no-branch prediction is rejected by prior evidence, retained honestly, and any completed new path run is only an independent replay.

**G163 monotone timing maps (2026-10-07).** Read the primary [Mathlib translation-number module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Dynamics/Circle/RotationNumber/TranslationNumber.html), its introductory statement and declarations for phase-independent limits, bounded iterate displacement and translation-number powers. The general monotone degree-one mechanism is established prior art. G163 gives a self-contained integer-period proof and applies it to the full-line reset return map, deriving a discrete P-1 error and a bounded whole-block potential. This is neither a new rotation theorem nor a Lean-checked Rule30 proof. Existing G6, G8 and G10 are the internal comparison/finite-cycle records. Continuity and invertibility are not imported; no uniform compatible-cycle slope or transient-tree debt bound follows.


**HG4 horizon interpretation (2026-10-07).** Read the primary [CMU CS15-451 Lecture13, shortest paths](https://www.cs.cmu.edu/afs/cs/academic/class/15451-s14/www/LectureNotes/lecture13.pdf), pages3-6: bounded-edge Bellman recursion and Johnson potential reweighting with its telescoping identity. G166 uses the reward-sign version and a free stopping option to identify stabilization with shortest tight-edge distance to zero potential. G8/G10 already supply the internal least-potential framework. This is a standard finite-graph interpretation, not a new shortest-path theorem or a Rule30 compatibility bound.


### GPT — companion-paper frame constraint, 2026-10-07

Read the abstract, definitions and section10 through the opening of10.2 in [Nersissian, Diagonal Bases and Diagonal Periods of Elementary Cellular Automata](https://arxiv.org/html/2609.25078v1). Theorems7–9 identify Pascal as the unique lower-triangular binary transform making truncated OR convolution pointwise, while transporting truncated increment J to strict prefix XOR L. Full prefix I+L is a different operator. Nonzero nilpotent J cannot be diagonal in any invertible binary linear frame.

**Unexpected boundary check, by hand:** at length2, J sends e0 to e1 and e1 to0, hence J²=0 but J is nonzero; at length1, J=0 and the obstruction disappears. This concerns truncated coefficient increment, not G161's cyclic temporal difference.

The supplied-window recurrence cost does not improve the same rotated local update. Section10.2 separates constructing a support representation from querying it. No cumulative rooted-return estimate was established by this bounded reading; the remaining manuscript was not audited. No new computation, novelty claim or period-growth result.


**Companion growth-scope follow-up (GPT, 2026-10-07).** Read sections12.1 (Theorems12–13 and Corollary9),16–17 and the opening of19 in [Nersissian's companion paper](https://arxiv.org/html/2609.25078v1). The integer lift has Fibonacci degree, yielding an exponential period ceiling after reduction. This is an upper bound, not an asymptotic equality or a least binary interpolation order. Section17 explicitly leaves jump spacing undetermined. Its right-column recurrence and single-seed census do not provide an all-history bound for our rooted left-side stages.

**Unexpected hand check:** the stated recurrence gives D0=1, D1=t and D2(t)=sum_(u<t)(2u+1)=t². Its integer degree is2, but modulo2 it equals t, with period2 rather than the permitted ceiling4. Thus exact integer degree cannot be transferred to least binary order. This source check supplies no rooted cumulative-return estimate; uninspected sections and the census data were not audited or rerun.

### Cloud — a scan for outside work on period 2 since Condrey, 2026-10-07 21:22 BST

Asked by the owner's steer to find a weakness "by any means", Cloud first checked whether anyone outside had found
one. Searches: Rule 30 centre column period two finite configuration 2026; Condrey follow-ups on eventual period
two; Rule 30 prize progress 2026. Nothing found settles period 2 or offers a ready-made lever. What turned up:
- Condrey's own repository, github.com/dcondrey/rule30, is listed by the search engine as "Proof-oriented,
  reproducible research on the Wolfram Rule 30 Prize Problems: partial theorems, exact certificates, and audited
  experiments", but returned HTTP 404 when fetched. Its contents were not read; worth retrying.
- [Patto1155/rule30-foundry PR 47](https://github.com/Patto1155/rule30-foundry/pull/47): audits the
  right-special-factor route and finds it is Prize 1 restated (by Morse–Hedlund: right-special factors at every
  length are equivalent to non-periodicity). Certified p(n) = 2^n for n up to 18. Not a route.
- [fabianxvogt/rule30](https://github.com/fabianxvogt/rule30): no solution claimed; the centre column has no
  eventual period up to 2,048 in its first million bits. Its statement of the barrier is worth keeping: "Two adjacent
  periodic columns ⇒ everything left of them periodic ⇒ contradiction. (Proved.) One periodic column gives _no_
  known second periodic object."
- [TheJustinSunPrize/awards issue 774](https://github.com/TheJustinSunPrize/awards/issues/774) (2026-09-17): lists
  the centre column's aperiodicity with the prize as USD 10,000, from rule30prize.org; no new prize.
- The woahwhattheheck/commons issue 15314 and PR 15318, Condrey's paper and Nersissian's papers, all already here.
This is a limited search, not a novelty audit.

## The move to a finite window, read at the source: Bugeaud and Dubickas (read 2026-10-07, by Local, for Q2)

- **Bugeaud, Y. and Dubickas, A., "Fractional parts of powers and Sturmian words"**, C. R. Acad. Sci. Paris, Ser. I
  341 (2005) 69-74 (read in full, all six pages; doi 10.1016/j.crma.2005.06.007).
  - **Theorem 2.1.** For an integer b >= 2 and irrational xi, the numbers {xi b^n} cannot all lie in an interval
    shorter than 1/b. They all lie in a closed interval of length 1/b exactly when xi = g + k/(b - 1) + t_b(w), with
    w a Sturmian word on {0, 1}: the extremal cases are Sturmian.
  - **The mechanism.** A window shorter than 1/b confines the b-adic digits to two adjacent values. Irrationality
    makes the digit word aperiodic, so by Morse and Hedlund it has at least m + 1 factors of each length m. Then for
    every m some factor w_m occurs after both a 0 and a 1. The two tails then differ by more than 1/b - b^(-m), so
    the window has length at least 1/b. This is combinatorics on words, not pigeonhole over a bounded set; GPT's
    GC360 was right to reject my recalled version (L217, L219).
  - **The general p/q case,** Flatto, Lagarias and Pollington's theorem and its extension to algebraic numbers that
    are neither Pisot nor Salem, is Dubickas's, in the papers cited there as [4, 6]. It works through the "reduced
    length" of polynomials, with ell(qX - p) = p. Not read yet.
  - **For us.** The extremal Sturmian case matches the record's Theorem E, which excludes every Sturmian column 1.
    The step "a factor preceded by two different letters forces a spread" is the shape of §8.58's window identity,
    where two times at which column 1 agrees for n steps force a zero run in the left half. Morse and Hedlund give
    such factors at every length in any aperiodic column 1. What Q2 needs is the converse pressure: a bound on zero
    runs that forbids them.
- **The general p/q case: Dubickas's reduced length** (found 2026-10-07 by search; Dubickas, Bull. London Math. Soc. 38
  (2006) 70-80, and the papers cited in Bugeaud and Dubickas as [4, 6]; the argument below is reconstructed from the
  definition and the search summaries, not read in the paper). For algebraic alpha with minimal polynomial
  P = sum p_k X^k, write xi alpha^n = x_n + r_n. Then sum p_k x_(n+k) = -sum p_k r_(n+k), an integer, because
  P(alpha) = 0. If every r_n lies in an interval of length L, the right side ranges over a window of length
  L * L(P), with L(P) the sum of |p_k|. If that is below 1, the integer is constant, the x_n satisfy a linear
  recurrence of fixed order, and that contradicts the hypothesis on xi unless alpha is Pisot or Salem. Replacing P by
  PQ for a normalized Q lowers L(P) to the reduced length ell(P), and ell(qX - p) = p gives Flatto, Lagarias and
  Pollington's 1/p. **For Q2:** the finite object is a fixed-order integer recurrence. A Rule 30 analogue would need a
  linear form of bounded order in column 0's and the left half's cells, forced constant by a window of the wall,
  which would put column 1 under a linear recurrence. Rule 30's OR is linear only where one input is known, so
  whether such a bounded-order relation exists inside zero runs is the Q2 question in FLP's terms.

### Local — unimodality of the Collatz demand law (Q9), searched 2026-10-08 05:37 BST

Searched before any proof attempt of "every actual demand law is unimodal" (DU, L275). Two standard web searches; the
items below are known from search summaries, not read in full.
- **Keilson and Gerber, "Some results for discrete unimodality", JASA 66 (1971) 386-389.** On the integers, a law is
  strongly unimodal (its convolution with every unimodal law is unimodal) exactly when it is log-concave. This covers
  the (1,1) part of the demand step, so unimodality can only break at the absorbing edge.
- **Passage-time unimodality** for one-dimensional strong Markov processes and its random-walk analogue (found as an
  Ann. Probab. item) concerns the law of the TIME of first passage, not the law of the minimum LEVEL at a
  fixed horizon, which is what the demand is (L275: d_a = P(min over s of (S_s - ell_s) = -1 - a)).
- **Log-concavity of exit distributions** of walks in bounded regions (a UCLA preprint found by search) cannot apply
  as stated: L048 shows the actual demand is not always log-concave.
No result was found on unimodality of the running minimum of a nonhomogeneous skip-free walk at a finite horizon. The
question stays ours; a proof would need an edge invariant that survives the critical/noncritical schedule.

### GPT GC487 automatic-kernel scope audit (2026-10-08)

Searches `site.cs.uwaterloo.ca Shallit k kernel automatic sequences finite kernel` and `site.writings.stephenwolfram.com rule 30 prizes automatic sequences` located Shallit's [Automatic Sequences slides](https://cs.uwaterloo.ca/~shallit/Talks/cant22-m.pdf). Read pages16-17: kernel definition and finite-kernel characterization statement, not an imported proof. GC487 independently proves a positive-continuation state-size lemma for canonical-binary LSB-first DFAO and a conditional finite-kernel indexing construction. Existing G137/Walnut prior art concerns automatic-word predicates, a different application. Finite signature counts cannot prove nonautomaticity, and nonautomaticity alone would not settle Rule30 indexing hardness. No novelty claim for kernel theory.


**GPT GC490,2026-10-08 — bounded parity-of-square-root search.** Query `automatic sequence "floor" "sqrt" squares nonautomatic` found no relevant primary-source treatment of the particular spin (-1)^floor(sqrt(n)) in the returned results. NOT FOUND in this bounded search, not a novelty claim. No secondary result imported. GC490 gives its discrepancy, explicit infinite decimations and arithmetic indexing proofs directly as a scope control; standard finite-state background remains GC487's Shallit source.

### 2026-10-08 — GPT GC520, zero-fibre contraction and bounded run search

Re-read the primary [Condrey paper](https://arxiv.org/html/2609.09431v1), already fully credited under G11, and the [Wolfram prize announcement](https://writings.stephenwolfram.com/2019/10/announcing-the-rule-30-prizes/). GC520 applies their recorded context to GC513/GC517; it asserts no new fibre classification. Searches for arbitrarily long Rule 30 centre runs, central-column run proofs, and constant-run results on Wolfram and Complex Systems domains found no usable selected unbounded-run theorem. Search scope was bounded; this records a failed lead, not absence of prior art. No statistical or secondary-source assertion was imported.

### 2026-10-08 — GPT GC521, actual unit-jump return constraint

Checked GC505-GC512 and the existing damage derivative record for all-time reversal and bounded-width escape results before claiming this block. GC521 extends the recorded initial reversal directly from Rule 30's local truth table; no external speed theorem or novelty priority is asserted. Its 128 finite local controls do not estimate transport. The larger-jump obstruction is retained rather than inferred away from conditional freshness.

### 2026-10-08 — GPT GC522, larger-jump return guard

Read GC507-GC508's finite jump/reset family and GC521's exact unit-reversal proof before this block. The first two healed-site equations directly supply the new guard; no external transport result or novelty claim is imported. GC507's existing N=1 example independently refutes all-positive immediate reversal. Local controls do not establish iid reachability or a long-time recovery law.

### 2026-10-08 — GPT GC523, actual escape template

Checked GC507-GC508's finite perturbation family and GC509-GC512's exposure and recurrence records before the audit. The invariant template follows directly from local Rule 30 updates; no external novelty or transport theorem is claimed. GC507's already-recorded N=1 example independently enters it. The finite-background construction and iid null-event caveat are retained separately.

### 2026-10-08 — GPT GC524, exact escape corridor probability

Used GC523's local template and G97's already-recorded spatial fair-product invariance. The two-step corridor inversion, finite time/site union and summable-event argument are elementary direct deductions; no new literature priority or external speed theorem is asserted. Adaptive-start conditioning is deliberately not replaced by an iid assumption. No new experiment was run.

### 2026-10-08 — GPT GC525, exact bulk-equivalence bridge

Checked the repository's right-edge confinement question and seed/trace-equivalence references before applying GC523's exact support. This is a direct corollary of that pending template proof, with no new classification or literature-priority claim. The right-light-cone disagreement is retained as the limit of the interior-equivalence statement. No new experiment was run.

### 2026-10-08 — GPT GC526, width-two confinement guard

Checked the existing confinement and damage-width record before using GC521's unit reversal and GC524's exact corridor probability. This direct width-transition deduction asserts no external novelty or general transport theorem. The endpoint reversal and deterministic singleton position are audited explicitly; no experiment was run.

### 2026-10-08 — GPT GC527, weighted front-displacement budget

Checked the existing jump-frequency and weighted-jump record before combining GC521 unit reversal with GC512 finite-exposure bounds. The pairing inequality is a direct elementary consequence, with GC505 and GC523 endpoint controls; no external novelty or transport estimate is asserted. No experiment was run.

### 2026-10-08 — GPT GC528, MSB convention audit

Used GC487's already-read automatic-sequence context and fixed sample. The separate prefix-state argument is direct deterministic-automaton reasoning, with no novelty priority asserted. No external result, larger sample or asymptotic automaticity claim is imported.
