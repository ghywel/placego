# Prior art: where this work sits in the record

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

2. **The fourth frame is a fork, and both arms are in the record.** EQVI
   (Liu et al., ECCV-W 2020, AIM 2020 winner) fits the *quadratic* by least
   squares over three flows `f(0->-1), f(0->1), f(0->2)` -- spending the
   extra frame on consistency, not on jerk. All-at-Once fits the *cubic* --
   spending it on jerk, keeping zero redundancy. This is exactly the
   degrees-of-freedom fork our spanning-flow proof predicted. Nobody we
   found reads the least-squares residual back out as a per-texel
   confidence field, which is what our T3.1 wants it for. Pre-register both
   arms and measure.

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
- Liu, Xu et al., *Enhanced Quadratic Video Interpolation*, ECCV-W 2020 —
  https://arxiv.org/abs/2009.04642
- Choi et al., *High-quality Frame Interpolation via Tridirectional
  Inference*, WACV 2021 —
  https://openaccess.thecvf.com/content/WACV2021/papers/Choi_High-Quality_Frame_Interpolation_via_Tridirectional_Inference_WACV_2021_paper.pdf
- Chi et al., *All at Once: Temporally Adaptive Multi-Frame Interpolation
  with Advanced Motion Modeling*, ECCV 2020 — https://arxiv.org/abs/2007.11762
- US Patent 11,430,138, *Systems and methods for multi-frame video frame
  interpolation*
- Liu & Katz, *Instantaneous pressure and material acceleration measurements
  using a four-exposure PIV system*, Exp. Fluids 2006 —
  https://link.springer.com/article/10.1007/s00348-006-0152-7
- *N-pulse particle image velocimetry-accelerometry*, Meas. Sci. Technol.
  2017 — https://iopscience.iop.org/article/10.1088/1361-6501/28/1/014001
- Shimizu & Okutomi, sub-pixel estimation bias / equiangular fit (via
  stereo sub-pixel literature); Nehab et al., *Improved Sub-pixel Stereo
  Correspondences through Symmetric Refinement* —
  https://gfx.cs.princeton.edu/pubs/Nehab_2005_ISS/subpixel.pdf
