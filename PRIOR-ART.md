# Prior art: where this work sits in the record

(A second survey, before the periodic-interior leap of 2026-09-27, is the last section.)

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
- Itoh, *Analysis of the phase unwrapping algorithm*, Applied Optics 21(14), 1982 — https://opg.optica.org/ao/abstract.cfm?uri=ao-21-14-2470
- Goldstein, Zebker & Werner, *Satellite radar interferometry: two-dimensional phase unwrapping*, Radio Science 23(4), 1988 — https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/rs023i004p00713
- Su & Chen, *Reliability-guided phase unwrapping algorithm: a review*, Optics and Lasers in Eng. 42, 2004 — https://www.sciencedirect.com/science/article/abs/pii/S0143816603001404
- Ghiglia & Romero, weighted and unweighted unwrapping by fast transforms, JOSA A 11(1), 1994 — https://opg.optica.org/josaa/abstract.cfm?uri=josaa-11-1-107
- Zuo et al., *Temporal phase unwrapping algorithms for fringe projection profilometry: a comparative review*, Optics and Lasers in Eng. 85, 2016 — https://www.sciencedirect.com/science/article/abs/pii/S0143816616300653
- Wilkins, *Covering maps and the monodromy theorem* (TCD course notes) — https://www.maths.tcd.ie/~dwilkins/Courses/421/421S3_0809.pdf
- Singer, *Angular synchronization by eigenvectors and semidefinite programming*, ACHA 30(1), 2011 — https://arxiv.org/abs/0905.3174
- Cucuringu & Tyagi, modulo-1 samples of a smooth function and phase unwrapping, 2018 — https://arxiv.org/abs/1803.03669
- Imry & Ma, PRL 35:1399, 1975 — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.35.1399 ; Aizenman & Wehr, PRL 62:2503, 1989 — https://link.aps.org/doi/10.1103/PhysRevLett.62.2503
- Li, Liang & Xia, *A robust Chinese remainder theorem*, IEEE TSP 57(11), 2009 — https://dl.acm.org/doi/abs/10.1109/TSP.2009.2025079 ; Trunk & Brockett, *Range and velocity ambiguity resolution*, IEEE National Radar Conf., 1993
- Rong & Tan, *Jump flooding in GPU*, I3D 2006 — https://www.comp.nus.edu.sg/~tants/jfa.html ; Gortler et al., *The Lumigraph* (pull-push), SIGGRAPH 1996 ; Knutsson & Westin, *Normalized and differential convolution*, CVPR 1993

Stereo and optical flow
- Hirschmüller, *Stereo processing by semiglobal matching and mutual information*, TPAMI 30(2), 2008 — https://dl.acm.org/doi/10.1109/TPAMI.2007.1166 ; Hernandez-Juarez et al., embedded real-time SGM on the GPU, ICCS 2016 — https://arxiv.org/abs/1610.04121
- Xu, Ranftl & Koltun, *Accurate optical flow via direct cost volume processing* (DCFlow), CVPR 2017 — https://arxiv.org/abs/1704.07325 ; Chen & Koltun, *Full Flow*, CVPR 2016 — https://arxiv.org/abs/1604.03513
- Li et al., *Neighbor-guided SGM optical flow* (NG-fSGM), IEEE TCSVT, doi:10.1109/TCSVT.2018.2854284
- Weiss, *Interpreting images by propagating Bayesian beliefs*, NIPS 9, 1996 — https://papers.nips.cc/paper/1309-interpreting-images-by-propagating-bayesian-beliefs ; Felzenszwalb & Huttenlocher, *Efficient belief propagation for early vision*, IJCV 70, 2006
- Barnes et al., *PatchMatch*, SIGGRAPH 2009 ; Besse et al., *PMBP*, BMVC 2012 ; Bailer, Taetz & Stricker, *Flow Fields*, ICCV 2015 — https://arxiv.org/abs/1703.02563
- Zhang et al., *Cross-scale cost aggregation for stereo matching*, CVPR 2014 — https://arxiv.org/abs/1403.0316 ; Rhemann, Hosni et al., *Fast cost-volume filtering*, CVPR 2011 (abstract only)
- Hu & Mordohai, *A quantitative evaluation of confidence measures for stereo vision*, TPAMI 34(11), 2012 (definitions via Poggi et al., https://arxiv.org/abs/2101.00431)
- Okutomi & Kanade, *A multiple-baseline stereo*, TPAMI 15(4), 1993 (abstract only) ; Lin & Liu, lattice-based MRF tracking of near-regular texture, TPAMI 29(5), 2007
- Teed & Deng, *RAFT*, ECCV 2020 — https://arxiv.org/abs/2003.12039 ; Xu et al., *GMFlow*, CVPR 2022 — https://arxiv.org/abs/2111.13680
- Meyer et al., *Phase-based frame interpolation for video*, CVPR 2015 — https://cgl.ethz.ch/publications/papers/paperMey15a.php

Production disciplines
- de Haan et al., *True-motion estimation with 3-D recursive search block matching*, IEEE TCSVT 3(5), 1993 — https://research.tue.nl/en/publications/true-motion-estimation-with-3-d-recursive-search-block-matching/ ; Pohl et al., real-time 3DRS for frame-rate conversion, IS&T EI 2018
- Periodic-structure patents: US20130039427A1 (Marvell/Synaptics), US8253854B2 (Broadcom), US10057596B2 (Novatek), US8675080B2 (STMicro), US10395378B2 (Samsung), EP1592255A1 (Panasonic)
- Hart, *PIV error correction*, Exp. Fluids 29, 2000 — https://web.mit.edu/dphart/www/PIV_ERROR2.PDF
- Meinhart, Wereley & Santiago, *A PIV algorithm for estimating time-averaged velocity fields*, J. Fluids Eng. 122, 2000
- Charonko & Vlachos, uncertainty from the correlation peak ratio, Meas. Sci. Technol. 24, 2013 — https://iopscience.iop.org/article/10.1088/0957-0233/24/6/065301
- Westerweel & Scarano, *Universal outlier detection for PIV data*, Exp. Fluids 39, 2005 ; Masullo & Theunissen, multiple correlation peaks in PIV, Exp. Fluids 2018 (abstract only) ; Sciacchitano, Scarano & Wieneke, multi-frame pyramid correlation, Exp. Fluids 53, 2012
- Wildeman, *Real-time quantitative Schlieren imaging by fast Fourier demodulation of a checkered backdrop*, Exp. Fluids 59, 2018 — https://arxiv.org/abs/1712.05679

Vision science
- Adelson & Bergen, *Spatiotemporal energy models for the perception of motion*, JOSA A 2, 1985 — https://opg.optica.org/josaa/abstract.cfm?uri=josaa-2-2-284
- Wallach 1935, translated by Wuerger, Shapley & Rubin, Perception 25, 1996 — https://journals.sagepub.com/doi/10.1068/p251317
- Shimojo, Silverman & Nakayama, *Occlusion and the solution to the aperture problem for motion*, Vision Res. 29, 1989 — https://pubmed.ncbi.nlm.nih.gov/2603398/
- Ohtani, Ido & Ejima, Vision Res. 35, 1995 — https://pubmed.ncbi.nlm.nih.gov/7571464
- McKee, Verghese, Ma-Wyatt & Petrov, *The wallpaper illusion explained*, J. Vis. 7(14), 2007 — https://pubmed.ncbi.nlm.nih.gov/18217805
- Anstis & Ramachandran, *Visual inertia in apparent motion*, Vision Res. 27, 1987 — https://pubmed.ncbi.nlm.nih.gov/3660637/ ; Ramachandran & Anstis, Nature 304, 1983
- Hock, Kelso & Schöner, *Bistability and hysteresis in the organization of apparent motion patterns*, JEP:HPP 19, 1993 — https://pubmed.ncbi.nlm.nih.gov/8440989/
- Pack & Born, *Temporal dynamics of a neural solution to the aperture problem in visual area MT*, Nature 409, 2001 — https://www.nature.com/articles/35059085
- Lidén & Pack, Vision Res. 39, 1999 — https://pubmed.ncbi.nlm.nih.gov/10615497/ ; Chey, Grossberg & Mingolla, JOSA A 14, 1997 ; Tlapale, Masson & Kornprobst, Vision Res. 50, 2010
- Weiss, Simoncelli & Adelson, *Motion illusions as optimal percepts*, Nat. Neurosci. 5, 2002 — https://www.nature.com/articles/nn858
