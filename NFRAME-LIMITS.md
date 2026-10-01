# Where the N-frame line stops, what "wobble" really costs, and what the rotation failure actually is

> **Status (2026-10-01).** The running record of the field's limits. Sections 1-8 are 2026-09-02 and 09-03; every
> later entry is a dated subsection of section 9, newest last ("The weave", 2026-09-30 to 10-01). Standing conclusions:
> - On the assumed real-footage band the exact-degree line stops at three or four frames (section 1; sigma_f was
>   measured at 0.070 px in section 8 and the verdict stands). On fast oscillation more frames keep paying, and the
>   five-frame quartic is built ([QUINTDIRECTIONAL.md](QUINTDIRECTIONAL.md)).
> - The coarse pyramid is point-sampled and the prefilter was refuted (section 8), so a fine periodic texture locks in
>   a comb of speeds whose period is the texel of the finest level that aliases it ("The weave").
> - The slow-print repair (`OUTLINE_ADOPT`) and the capped lattice re-score for fast prints (`PRINT_LATTICE`, carried
>   on in [ENERGY-TRANSFER.md](ENERGY-TRANSFER.md)) are both in the Cadence player; the per-level trust gate is parked
>   and has never been built.
>
> Which shader to use: [SHADERS.md, "Which one to use"](SHADERS.md#which-one-to-use). Mac readings taken before
> 2026-09-30 carry MoltenVK's run-to-run wander, and their best-of-three practice is retired ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md)). In section
> 8 and section 9's first entry, "M5" to "M9" are scratch comb scenes; in "The weave", "the M5" is a Mac with an Apple M5. Where "PREDICTION.md"
> appears without a path (2026-09-27 and 09-28), it is `tests/probes/limb/PREDICTION.md`. Paths under `np-scratch/`,
> `hot-drops/` and `claude-handoff/`, and the private app trees named here (the demo's and the party app's), are
> private working folders, not part of this repository.

**Contents**

- [1. The stopping point is a signal-to-noise crossing, not a fixed N](#1-the-stopping-point-is-a-signal-to-noise-crossing-not-a-fixed-n) (2026-09-02)
  - [The exception that matters: fast oscillation, where more frames keep paying](#the-exception-that-matters-fast-oscillation-where-more-frames-keep-paying)
- [2. Wobble: it is real, it is quantified, and it cuts against wide windows](#2-wobble-it-is-real-it-is-quantified-and-it-cuts-against-wide-windows)
- [3. Rotation is not wobble, not order, and mostly not rotation](#3-rotation-is-not-wobble-not-order-and-mostly-not-rotation)
- [4. Two ladder findings that were not on the agenda](#4-two-ladder-findings-that-were-not-on-the-agenda)
- [5. Recommendations, in order](#5-recommendations-in-order)
- [6. Predictions vs outcomes](#6-predictions-vs-outcomes)
- [7. Method notes](#7-method-notes)
- [8. 2026-09-03: the prefilter built and refuted, and two leads closed](#8-2026-09-03-the-prefilter-built-and-refuted-and-two-leads-closed)
- [9. 2026-09-04: the rotation field and A4 re-measured on the shipped family](#9-2026-09-04-the-rotation-field-and-a4-re-measured-on-the-shipped-family); every later entry is a subsection of section 9:
  - [The Moire gate was measuring frame difference](#the-moire-gate-was-measuring-frame-difference-and-that-was-worth-something) (2026-09-04/05)
  - [The resolution half of the scale-aware generator](#the-resolution-half-of-the-scale-aware-generator-and-what-the-4k-test-really-measured)
  - [Weird geometry, and the six-frame line](#weird-geometry-and-the-six-frame-line)
  - [The time asymmetry was the instrument: a retraction](#the-time-asymmetry-was-the-instrument-a-retraction-and-what-the-exact-read-shows)
  - [The phase-locked consensus](#the-phase-locked-consensus-a-loop-reads-a-field-the-mean-of-its-frames-cannot)
  - [Lead A: the two rim biases](#lead-a-the-two-rim-biases-have-mechanisms-and-fixes-and-each-fix-is-a-trade)
  - [Lead G: the reading's memory as a mode](#lead-g-the-readings-memory-as-a-mode-and-where-that-helps)
  - [Lead B: the frame-rate half is a decimation stage](#lead-b-the-frame-rate-half-is-a-decimation-stage-and-the-4k-disc-could-not-have-shown-it)
  - [Lead C: a number beside the project that nobody here chose](#lead-c-a-number-beside-the-project-that-nobody-here-chose)
  - [Lead E: the velocity gradient tensor](#lead-e-the-half-that-needs-no-new-match-the-velocity-gradient-tensor)
  - [The foresight seed (2026-09-06)](#the-foresight-seed-the-windows-other-half-at-the-search-2026-09-06)
    - [The prior's loss, located and repaired: a deadband (2026-09-06, later)](#the-priors-loss-located-and-repaired-a-deadband-2026-09-06-later)
  - [The owner's eyes on three renders (2026-09-06, evening)](#the-owners-eyes-on-three-renders-and-what-they-found-2026-09-06-evening)
  - [The owner's eyes, second day (2026-09-07)](#the-owners-eyes-second-day-the-opacity-switch-a-pendulum-the-stairs-aperture-and-an-idea-for-animation-2026-09-07)
  - [The hole, tested; the stairs, seen again; the tri's root; a second 4K film (2026-09-07, afternoon)](#the-hole-tested-the-stairs-seen-again-the-tris-root-a-second-4k-film-2026-09-07-afternoon)
  - [The aperture series, the tensor fill refuted, and the alias behind the fast end (2026-09-07, afternoon)](#the-aperture-series-the-tensor-fill-refuted-and-the-alias-behind-the-fast-end-2026-09-07-afternoon)
  - [The cube, the manifolds through the reading, and a black hole (2026-09-08)](#the-cube-the-manifolds-through-the-reading-and-a-black-hole-2026-09-08)
  - [Snap is readable, and the family's derivative ceiling is snap (2026-09-08)](#snap-is-readable-and-the-familys-derivative-ceiling-is-snap-2026-09-08)
  - [The held anchor (2026-09-09)](#the-held-anchor-where-the-reading-was-standing-and-a-control-that-could-not-be-used-2026-09-09)
  - [Has animation work polluted the general shaders? (2026-09-09)](#has-animation-work-polluted-the-general-shaders-audited-and-measured-2026-09-09)
  - [Jerk is not noise-limited, it is truncation-limited (2026-09-09)](#jerk-is-not-noise-limited-it-is-truncation-limited-and-no-sinusoid-can-show-that-2026-09-09)
  - [The synthetic pool: 43 gaps found (2026-09-09)](#the-synthetic-pool-43-gaps-found-and-the-bottleneck-is-not-the-scenes-2026-09-09)
  - [The gradient tensor's third component (2026-09-10)](#the-gradient-tensors-third-component-and-why-its-first-two-numbers-were-unfair-2026-09-10)
  - [Verb-object pairs, and the rolling wheel (2026-09-10)](#verb-object-pairs-generate-cases-a-taxonomy-cannot-and-the-rolling-wheel-proves-it-2026-09-10)
  - [Weird geometry: fields that are not constant (2026-09-10)](#weird-geometry-what-the-readers-make-of-fields-that-are-not-constant-2026-09-10)
  - [The non-affine failure (2026-09-10)](#the-non-affine-failure-a-cliff-at-a-fixed-velocity-gradient-entering-at-the-coarse-search-2026-09-10)
  - [Content drawn on twos (2026-09-19)](#content-drawn-on-twos-the-family-collapses-to-a-hold-and-the-cadence-is-the-prize-2026-09-19)
  - [The cadence branch (2026-09-19, afternoon)](#the-cadence-branch-the-prize-taken-inside-the-window-and-the-two-things-it-cannot-know-2026-09-19-afternoon)
  - [The fast pan over fine texture (2026-09-19, evening)](#the-fast-pan-over-fine-texture-crystallised-its-knee-measured-the-mechanism-half-found-2026-09-19-evening)
  - [The global-motion seed (2026-09-20)](#the-global-motion-seed-the-pan-resolved-where-the-texel-cannot-resolve-it-2026-09-20)
  - [The cage (2026-09-21)](#the-cage-a-fine-periodic-print-under-a-sub-pixel-drift-where-every-warp-loses-to-the-blend-2026-09-21)
  - [The field's coherence (2026-09-21, later)](#the-fields-coherence-the-cue-that-separates-and-the-gate-it-makes-2026-09-21-later)
  - [The field on real bodies (2026-09-27)](#the-field-on-real-bodies-two-hours-of-children-scored-against-a-skeleton-it-shares-nothing-with-2026-09-27)
  - [The half-period alias in the shader: the prior gate and the carry (2026-09-28)](#the-half-period-alias-in-the-shader-the-prior-gate-and-the-carry-2026-09-28)
  - [The aperture in the carry (2026-09-28, later)](#the-aperture-in-the-carry-b1-moving-up-and-the-energy-channel-on-rendered-children-2026-09-28-later)
  - [The weave (2026-09-30 to 2026-10-01)](#the-weave-a-two-dimensional-periodic-print-where-the-field-locks-one-period-away-and-the-family-sits-at-the-blend-2026-09-30-late-evening)

Research log, 2026-09-02. Windows, RX 6600 (Vulkan device 0, bit-reproducible
platform). One field -- the O5 tri acceleration sweep -- was re-rendered on
the Radeon Pro 560X and agrees to three decimals on 19 of 20 frames (section
7); nothing else in this file has been run on the 560X. Two questions were
put: (1) is there a natural N beyond which more
source frames add nothing and cost compute -- the Fourier "duck outline" limit;
(2) the polynomial model assumes one smooth curve across the window, but real
acceleration may wobble *inside* it -- is that a problem, what can be done, and
is it related to the rotation failure? Both were answered by derivation first,
then by measurement against pre-registered predictions (the predictions were
written before the ladder ran; the scorecard is at the end). A third result
came out of the controls for the rotation question and is the most actionable
thing in this file: the coarse pyramid is point-sampled, and the synthetic
ladder never noticed because every fine-textured translation case (L7, M1,
M2, M3) moves at exactly one coarse texel per frame and the remaining
textured cases (A4-A7, O5, O6) use a pattern that is sub-Nyquist at the
coarsest level until it is rotated.

## 1. The stopping point is a signal-to-noise crossing, not a fixed N

Two curves cross. Noise in the k-th derivative of block-matched flows grows
with order: on the *flow* sequence (each adjacent-pair flow is an independent
search), velocity, acceleration, jerk and snap carry noise variances of 1, 2,
6 and 20 times the single-flow variance (the central binomial coefficients
C(2k-2, k-1)), i.e. std multipliers 1, 1.41, 2.45, 4.47. This derivation
disagrees with the stencil-only figure in QUADDIRECTIONAL.md and the shader
header: jerk/accel noise comes out as sqrt(3) = 1.73x, not sqrt(11/2) = 2.35x,
because the composed two-interval displacement shares its first flow with the
adjacent one. It also assumes the composed far flow's search noise is
independent of F12's, which the warp does not guarantee, and it has not yet
been checked numerically on the A6 null fields; do that before changing
either document. The 3.0/6.0 jerk deadband was chosen
empirically and does not change either way.

The signal shrinks with order for any band-limited motion: for x = A sin(w t)
with w in radians per frame, the k-th central difference has amplitude
A (2 sin(w/2))^k, which for w < 1 falls geometrically with k. The
discrete-derivative attenuation from the CORRECTION section is the mild part
of this ((2 sin(w/2)/w)^k = 0.83 even at O3, k = 4); the decay is A w^k itself.
The signal-to-noise of order k is therefore

    SNR_k = A (2 sin(w/2))^k / (sigma_f sqrt(C(2k-2, k-1)))

with sigma_f the matcher's per-flow noise. Nothing in the record gives sigma_f
directly; L7's constant-velocity acceleration tail (p90 0.277 px/interval^2)
implies ~0.12 px for the Gaussian core and the corrected jerk nulls imply
0.02-0.07 px at the median. With sigma_f = 0.10 px:

    case      w (rad/frame)   accel SNR   jerk SNR   snap SNR
    O1 gentle    0.26            19          2.9        0.4
    O2 / O5      0.65            58          22         7.6
    O3 hard      1.05 (6 samples/period; 2 sin(w/2) = 1 exactly, so every
                                 order carries the full amplitude A = 12 px)

No real-footage motion spectrum has been measured (section 5, item 3). The
rows above assume real footage sits at or below O1 in per-frame angular
frequency (about 1 Hz at 24 fps); the derivation's own working band, |a| ~ 1
px/interval^2 at 1-4 Hz, gives jerk SNR 1.1 / 1.6 / 2.6 / 4.1 at 1 / 1.5 /
2.5 / 4 Hz and snap SNR 0.2-2.2. On that assumption the fourth frame's jerk
clears SNR 3 only above ~3 Hz and a fifth frame spent on snap never does:
**on the assumed real-footage band the exact-degree line stops at N = 3 or
4 -- 4 if sigma_f is near 0.05 px or the motion is fast, 3 if sigma_f is near
0.12 px and the motion gentle -- and a fifth frame never pays there.** On
fast oscillation (O2 and above) higher orders stay
measurable, and at O3 the differences do not decay at all -- that is the
Fourier resonance of a 6-sample period, not a property of the estimator.

Every number in that table scales with sigma_f, and the record does not pin
it down: L7's acceleration tail implies about 0.12 px, the corrected jerk
nulls 0.02-0.07. At 0.05 px the jerk's SNR doubles and the fourth frame is
comfortably useful on real footage; at 0.12 the third frame is the last that
pays. The first experiment in section 5 is the one that settles it.

The measured ladder says the same thing in dB. Quad (exact cubic) against tri,
32 cases, 24->60:

    quad beats tri by > 0.2 dB only on   O3 +0.98,  L6 +3.64 (see 4),  M2 +0.61 (see 4)
    quad loses to tri by 0.2-0.9 dB on   L1 -0.90, O6 -0.46, A4 -0.40, A5 -0.37, A1 -0.34,
                                         L9 -0.31, F1 -0.27, L3/A3 -0.23, A2/L4 -0.21, F2 -0.20
    everything else within +/-0.2

Both were predicted (P1, P2): the jerk term pays only where the jerk is large,
and costs noise everywhere else. A 5-frame exact quartic would add a SNAP
term whose real-footage SNR is below 1; that part stands. "Do not build it"
does not: the same window's acceleration and jerk rows are a different
matter, and the section 8 addendum, written after the flow-error correlation
had been measured, reverses the recommendation.

### The exception that matters: fast oscillation, where more frames keep paying

The decay above is not universal, and the exception is not a footnote. The
signal in the k-th difference is A (2 sin(w/2))^k, and **2 sin(w/2) = 1
exactly at w = pi/3, which is six samples per period.** So:

    samples per period   2 sin(w/2)   what each added order does to the signal
      24 (O1)              0.26        loses 4x per order -- stop at N = 3
      12                   0.52        loses 2x per order
       9.6 (O2, O5)        0.64        loses 1.6x per order
       6 (O3)              1.00        LOSES NOTHING -- every order carries
                                       the full amplitude A
       5                   1.18        higher orders GROW
       4                   1.41        higher orders grow fast (but Nyquist
                                       is 2, so the margin is thin)

Below about eight samples per period the usual argument inverts: the
polynomial's higher terms stop shrinking, only the noise growth is left to
stop you, and the frame budget becomes worth spending. That is exactly what
the ladder measured -- O3 (six samples per period) is the **only** case in
thirty-two where the four-frame shader beat the three-frame one by a clear
margin (+0.98 dB), and the corresponding jerk reading calibrates to 1.1% of
peak. Everywhere else the fourth frame is noise.

**This is the regime of fast, small, repetitive motion** -- a vibrating
component, a resonating structure, a particle oscillating in a trap or a
flow. For that content the conclusion is the opposite of the film
conclusion: N = 4 is not the ceiling, it is the point where the method
starts to earn its keep, and a fifth frame is worth building -- for a reason
found later the same day (section 8 addendum): not for snap, which stays
noise, but because the four-frame acceleration is a plain second difference
whose truncation is (2 sin(w/2)/w)^2 - 1, i.e. -8.8% at six samples per
period, and a symmetric five-frame quartic removes it, cutting the
acceleration error three- to sixfold there.
The practical rule for anyone bringing such content to this instrument is to
choose a frame rate (or a frame stride -- see below) that samples the motion
of interest **six to ten times per period**. Faster than that and the
derivatives sink into the noise; slower and the polynomial cannot represent
the motion at all. Nothing at N = 5 has been built or measured. What is
established, by simulation on the measured noise, is where it pays:
acceleration at eight samples per period and fewer, and -- a second band
nobody predicted -- jerk on slow motion, where the symmetric stencil's noise
is 2.8x below the four-frame window's.

**Frame rate: the invariant statement is in seconds.** Everything above is
in per-frame units, and the camera rate is inside them: w = 2 pi f_motion /
fps, while sigma_f is in pixels and roughly independent of fps. For fixed
physical motion the k-th derivative's adjacent-frame SNR therefore falls as
fps^(-k). For a 1 Hz, 40 px motion at sigma_f = 0.1 px:

    fps     w (rad/frame)   velocity SNR   accel SNR   jerk SNR
    10         0.63             250           110          40
    24         0.26             105            19          2.9
    100        0.063             25           1.1          0.04
    2000       0.0031             1.3        0.003      ~1e-5

At 100 fps four adjacent frames cannot measure jerk; at 2000 fps they cannot
measure velocity (0.13 px/frame peak is below the matcher's precision). At
10 fps a four-frame window spans 300 ms and exceeds a third of the period for
anything faster than ~1.5 Hz: that is the wobble regime of section 2, where N
must drop, not rise. So the two rules that survive a change of frame rate
are: (1) the window spans at most ~1/3 of the fastest period of interest, so
the number of frames in it scales with fps (N - 1 ~ fps x T_window); (2)
within that span, the fitted degree is set by the physical derivatives
against the noise, and with many samples across the span (high fps) the
right fit is a low degree by least squares, where noise falls as 1/sqrt(N).
Exact degree-(N-1) interpolation through adjacent frames is the low-fps
special case, and 24 fps with N = 3-4 happens to sit in it. For this shader,
pinned at four bound frames, the practical form is a frame STRIDE s chosen
so the strided interval lands in the working band (0.3-1 rad per interval,
6-20 samples per period): for 1 Hz content s ~ 2 at 24 fps, ~8 at 100 fps,
~160 at 2000 fps. The record's open lead "widen the baseline (every k-th
frame) for high-fps input" is this rule; it fixes k. The low-fps end has a
different limiter first: the ~23 px/frame search reach, which 10 fps content
exceeds 2.4x sooner than the ladder's 24 fps does.

**How a fifth frame could still earn its cost.** Two ways, both argued in the
record and both consistent with the numbers here: (a) as the first
*independent validator* of acceleration -- two disjoint triples {0,1,2} and
{2,3,4} differenced against 2j -- which is a gate, not a derivative; (b) as a
fixed-degree (Savitzky-Golay) fit over a longer window, spending the frame on
variance instead of order. The record's caution stands: the shader binds
exactly 16 textures in its final pass and libplacebo's bind ceiling is 16;
a naive fifth frame needs 21. The Fourier intuition supports (b), not the
exact quartic -- but see section 2 for when (b) hurts.

## 2. Wobble: it is real, it is quantified, and it cuts against wide windows

Worst-phase placement error of each fit on the O-series sinusoid at the
interpolated instants, in px (analytic, unit frame spacing):

    case   bi (linear)   tri (3-pt quadratic)   quad exact cubic   anchored LSQ (QUAD_MODE 1)   unanchored 4-pt LSQ
    O1        0.33            0.040                  0.004               0.009                        0.070
    O2        1.02            0.306                  0.079               0.102                        0.53
    O3        1.54            0.724                  0.295               0.295                        1.20

Raising the degree with the frame count keeps paying analytically (tri ->
cubic: 10x on O1, 3.9x on O2, 2.5x on O3); the shipped cubic's jerk deadband
leaves 0.114 / 0.240 / 0.295 px of it, so the gain is realised only on O3,
which is what section 1's ladder shows. Holding the degree and widening the
window -- the "average more frames" reflex -- gets *worse* exactly when the
curve bends inside the window: an unanchored 4-frame least-squares quadratic
(last column) loses to the 3-frame exact quadratic on O2 and O3. The shipped
QUAD_MODE 1 fit is anchored at the straddle frames and its own placement
truncation is smaller than tri's (0.009 / 0.10 / 0.30 px); measured quadlsq -
tri is O2 -0.28, O3 +0.40, O5 -0.42, so its losses below are acceleration
noise through the far flow (P6), not placement wobble. The wobble, in
numbers, is the attenuation that follows. A fixed-degree
fit over N frames averages the derivative over the window; for a sinusoid the
5-frame degree-2 fit reads 0.975 / 0.851 / 0.651 of the true acceleration at
O1 / O2 / O3 against 0.994 / 0.965 / 0.912 for three points. The honest window
rule is: span no more than about a third of the period of the fastest motion
you care about.

Measured (QUAD_MODE 1, the least-squares arm, run as "quadlsq" over the same
32 cases):

    quadlsq - quad(exact):  O2 -0.20,  O3 -0.58,  O5 -0.24,  O6 -0.35     (P5 confirmed)
                            A1 -0.33, A3 -0.24, A7 -0.24, L1 -3.99, L2 -0.43, L9 -0.39
                            wins only M2 +1.35, L3 +0.35, O1 +0.27

The pre-registered expectation that the LSQ arm would *win* on the no-jerk
families (fewer parameters, less noise; P6) was refuted, and the cause is a
gating defect demonstrated on L1 and unexplained elsewhere -- the far-flow
tail it lets through is the matcher's own statistics, which the Gaussian
model of section 1 does not capture: the LSQ acceleration takes the composed
far flow with weight 4/11 under only the 0.5/1.5 acceleration deadband, so
far-flow noise reaches the warp ungated. L1 collapses 4.9 dB below tri
(56.50 vs 61.39) and recovers to 60.33 / 60.51 with ACCEL_DEADBAND 1.0/2.5 /
2.0/5.0 (measured by the wobble analysis before the ladder ran; that sweep
covered L1 and O3 only -- O6 -0.81, L9 -0.70, A1 -0.67, L2 -0.53 and the
other quadlsq-below-tri cases were not re-run at the raised deadband). The
exact cubic with its 3.0/6.0 jerk deadband remains the right default.

**The 4-frame "residual" is not an independent wobble detector.** Algebra: for three
displacements at taus (-1, +1, +2) the LSQ-quadratic residual vector is
j (-1, -3, +1)/11, so the residual equals (3/11)|jerk| per texel, flow noise
included -- it is the same information as the cubic's jerk term, not an
independent confidence. It is also emitted in texel-diagonal units
(1 unit = 2.04 x-px at 1280x720), as a max-norm, and ungated (only the
acceleration is multiplied by the provenance gate). Measured on the flat
O-series boxes (the flat scenes of section 7: edge-driven readings, 5-20x the
(3/11)|j| the model predicts, so behaviour rather than calibration) it reads
zero at every jerk null (O1 frame 6; O3 frames 8, 14, 20 -- the
6-sample-period nulls) and 1-4 units elsewhere, quantised in steps of ~1.1
units (mechanism not established); on A2 (jerk = 0) it *rises* with velocity
from 0.5 to 2.8 as the object approaches the ~23 px/frame search reach. It
measures flow failure, and it does that well (section 5, item 4). A 4-frame
window
sees exactly one wobble number, the third difference, and can spend it on the
jerk or on a residual that equals it; the first *independent* within-window
variance test needs five frames (the disjoint-triple validator above).

What to do about wobble, in order of evidence: keep the exact cubic with the
jerk deadband (it is already a residual-gated order selection: 3.0/6.0 in
jerk units is 0.82/1.64 true px of residual); never widen the window at fixed
degree without the residual's permission; read every per-texel field by
median and percentile, never mean (the fields are heavy-tailed -- L7's p99 is
23 sigma -- and their means are outlier counts in disguise).

## 3. Rotation is not wobble, not order, and mostly not rotation

Order independence, measured: bi / tri / quad / quadlsq on R1 37.30 / 37.26 /
37.07 / 37.05, R2 37.58 / 37.57 / 37.41 / 37.37, R3 28.38 / 28.40 / 28.36 /
28.32 (P8 confirmed). rotcheck on R2 and R3 gives tri and quad identical to
the decimal (at exact N:N the quad's acceleration field is the tri's by
construction): R2 median vector error 134-220%, angular error 61-97 deg; R3
100-211%, 24-67 deg -- at frames 6-15, rim speeds 8-20 px/frame, all inside
the search reach (P9 confirmed). The temporal model is not the bottleneck: a
rim texel traces a sinusoid at 59 samples per revolution (R1; R2, the case
rotcheck measured, reaches 7.4 deg/frame = 49 samples by f15, transfer still
> 0.99), where the
quadratic's placement truncation is 0.01 px and the recorded errors are 1.4-3
px/interval^2 -- two orders of magnitude above anything a window or order
choice can touch. The sine link the question proposed is real and
numerically irrelevant.

Three mechanisms, separated by controls built for the purpose (scratch scenes,
not in the ladder; all pre-registered; seven of the first round's eleven
predictions -- PB, PC, PE, PF, PG, PI, PJ, all downstream of the mis-designed
"aperiodic" control -- and the second round's 8/12 px/frame rescue were
refuted and kept as such, section 6):

- **Aperture (R1, R2, flat blobs).** The field exists only on the rim, where an
  isolated edge constrains flow along its normal. R2's truth is mostly
  tangential (spin-up), exactly the unobservable component: in a per-texel
  decomposition of the tri field made in the analysis session (at FS 32; not
  part of E3, no log in the numbered experiments) the along-normal reading
  matches truth at f6 and f9 (-0.27 vs -0.28, -0.92 vs -0.93) while the
  along-edge reading is uncorrelated with it. The zero-noise aperture floor
  alone, computed from the blob's edge-normal geometry rather than tested
  texel by texel, is 54-94% vector error on R2.
- **Period locking (R3, R6, TEX_M2 blobs).** The product texture is invariant
  under body shifts of (+/-20, +/-20) px; translation breaks the tie by the
  incumbent-at-zero rule (F3, the same blob translating at 16 px/frame, scores
  56.83 dB with 0.37 px median flow error), rotation does not. R6 (constant
  rotation) sits 3.9 dB *below* linear; its velocity field peaks at the 28.3
  px lattice at every frame.
- **Point-sampled pyramid (everything textured, at any non-integer coarse
  speed).** LUMA_*_S/E/Q/H are single bilinear taps of the full-resolution
  frame at 1/16, 1/8, 1/4 and 1/2 resolution -- no box filter, in every
  shader of the family. Any texture component with period below 32 / 16 / 8 /
  4 px is aliased at that level, and an aliased level is shift-invariant only
  for integer shifts of its own texels (tridirectional-interpolation.glsl:
  LUMA_A_S at lines 28-35, _E 443-450, _Q 743-750, _H 974-981; the same
  construction in bidirectional-interpolation.glsl at 76-83). The ladder's
  textured translations
  (L7, M1, M2, M3) all move at 16 px/frame = exactly 1 S = 2 E = 4 Q = 8 H
  texels -- the one speed at which the block matcher can match on aliased
  content. The decisive control, pre-registered before it ran: the same
  TEX_M1 box translating at 6 / 8 / 10 / 12 / 14 px/frame (bi shader only;
  tri and quad were not run on the comb) scores 29.27 / 30.64 / 27.97 /
  27.79 / 29.63 dB (linear 26-28.5) against 46.9 at 16 px/frame. Velocity
  fields, read on the 10 and 12 px/frame cases, are 78-97% gross with median
  errors of 19-20 px, and the error pattern repeats with the box's
  coarse-grid phase (period
  40 px = 5 E texels at 10 px/frame): a sampling-phase signature. The
  textured A/O calibration cases pass at non-integer speeds only because
  TEX_M2 axis-aligned is 0.4 cycles/texel at the coarsest level, below
  Nyquist; rotate it into the 17-73 deg band and it should alias too --
  consistent with, but so far supported only by, R3's interior failing from
  frame 10 onward (theta > 25 deg); that is one datum, not a test. Caveat:
  the control and comb scenes are scratch scenes that were not run through
  scenecheck.sh, so their absolute PSNRs carry the alignment caveat; the
  velocity-field readings (78-97% gross, ~20 px errors, phase-locked to the
  coarse grid) are far less exposed to it -- F3, rendered through the same
  scratch path, reads 0.37 px median flow error, and 20-px errors
  phase-locked to the coarse grid are not an alignment offset -- and say the
  same thing.

Rotation "failed" because it is the one ladder motion that moves textured
content by non-integer, spatially varying coarse-texel amounts while also
removing the tie-break on periodic texture. Real footage does the first of
those in every shot. This is the likely cause of the "defects on nearly
every frame" verdict on real content, and it has a cheap fix with a decisive
test.

## 4. Two ladder findings that were not on the agenda

- **L6_flat_large and M2_period40.** The Apple-silicon (M2 Mac) ladder's
  "+3.18 quad anomaly" on L6 reproduces here as +3.64 -- but it is tri
  collapsing 7.57 dB below bi (47.95 vs 55.52) with quad recovering half, and
  M2_period40 has the same shape (bi 53.60, quad 50.09, tri 49.48). On large
  flat and periodic objects at 16 px/frame the 3-frame estimator hurts and
  the 4-frame one hurts less. Not explained, and no diagnostic data exists
  behind the number (no per-interval PSNR, velocity-field export or accel-off
  run; recommendation 7). The point-sampled pyramid is not a candidate: L6
  has no texture to alias, M2's period-40 texture is sub-Nyquist at the
  coarsest level, and both run at 16 px/frame, the one immune speed. F1 (tri
  -1.16 vs bi) and M1 (-0.83) lean the same way. Flat interiors hide flow
  errors from PSNR while the acceleration term does not.
- **The jerk field's floor, measured on the null case.** A6 (constant
  acceleration, jerk = 0, textured): the jerk field reads -0.106..+0.129
  px/interval^3 across the cycle, median |reading| 0.041 (p90 0.09): the
  floor is about 0.05-0.1 px/interval^3. O6's jerk peaks at 0.706; its
  readings miss by 0.18-0.44 on frames 17-21 but by only 0.00-0.18 on the
  mirror-phase frames 2-6 -- a time-asymmetric miss that looks like a
  window-end effect near the clip tail rather than the floor (untested;
  section 5). Real-footage jerks -- unmeasured, but 0.26-0.64 px/interval^3
  if the assumed 1-2.5 Hz, 1 px/interval^2 band holds -- would sit within a
  factor of ten of the floor: the measured form of the section-1 SNR
  argument.

## 5. Recommendations, in order

0. **Measure sigma_f directly.** Export the N:N velocity field on L1 and L7,
   subtract the analytic flow, report std, p90 and p99 over the textured
   interior. Everything in section 1 scales with it, and the same export
   gives the fraction of texels whose third difference clears the 3.0 jerk
   deadband on constant-velocity content (the tail the record priced at 0.35
   dB on L1 from a jerk-off run on the other platform; the Windows quad-tri
   gap on L1 is -0.90 and has not been decomposed into drag and tail).

   *2026-10-01: answered in section 8: sigma_f = 0.070 px (robust std over M1's interior); the N = 3-or-4 verdict stands.*
1. ~~**Prefilter the pyramid.**~~ **BUILT AND REFUTED 2026-09-03 -- see
   section 8.** The pre-registration was: the speed comb rises from 28-31 dB
   to >= 40; R4/R5 to >= 34; R3/R6 and the 16 px/frame cases unchanged.
   Measured: the comb gains 1.5-2.6 dB, R4/R5 gain 0.8, and the 16 px/frame
   cases are *destroyed* (M1 46.91 -> 28.64). The replacement lead is a
   per-level trust gate, not a filter.
2. **Add the comb to the ladder** (TEX_M1 and TEX_M2 boxes at 10 and 12
   px/frame) and keep F3 as the rotation-vs-texture control. A ladder whose
   only textured speed is one coarse texel cannot see this class of failure.

   *2026-10-01: not done as of this date: no comb case is in `tests/scenes.sh`. "The weave" (2026-09-30) meets the same comb on a two-dimensional print.*
3. ~~**Do not build N = 5 as an exact quartic.**~~ **REVERSED 2026-09-03 --
   see the section 8 addendum; BUILT AND MEASURED 2026-09-04, QUINTDIRECTIONAL.md:
   2.7x and 6.7x on acceleration at eight and six samples per period, 2.9x on
   the jerk floor, +18% time.** Build it as an exact quartic over a
   SYMMETRIC window and ignore its snap row: acceleration error falls 3-6x at
   <= 8 samples/period (truncation of the plain second difference) and jerk
   noise 2.8x at >= 12 (stencil coefficients +/-0.5 against +1, +2, -1). The
   fixed-degree fit halves acceleration noise only on very slow content and
   is catastrophic below ~16 samples/period. Real-footage motion bandwidth
   (TRI_DIAG=7 velocity at 24:24 over a few seconds) is still the first
   measurement to make; N_max at fixed degree is 1 + sqrt((12/w^2 + 7)/3):
   3.4 at O3, 4.4 at O5, ~9 at O1.
4. **Retire "residual = measured confidence"** in QUADDIRECTIONAL.md:
   document resid = (3/11)|jerk|, the unit (length(HOOKED_pt)), the max-norm
   and the missing gate; report field statistics as medians over gated
   texels. Its real use is as a per-texel flow-failure gate (27-40x contrast
   between failing and clean bands on R3 -- an analysis-session reading; the
   numbered E2 residual run covered R2 only).

   *2026-10-01: not done in QUADDIRECTIONAL.md's own text; a dated note there now points to section 2.*
5. ~~**Verify the noise ratio.**~~ **ANSWERED 2026-09-03 -- see the section 8
   addendum.** Measured from the solve's own flows: 1.40 on A4, 1.07 on M1
   (robust 1.15 / 1.00). sqrt(3) is the independent-noise limit, reached by
   neither; the window's flows are correlated (0.35 / 0.9). A first figure of
   0.63-0.80 was a decode error and is retracted in the addendum.
6. **Re-label the rotation lead** in PLAN.md as three leads: aperture on
   edge-only blobs (structure-tensor gate), period locking on symmetric
   texture (tie-break under rotation), and pyramid aliasing (item 1).

   *2026-10-01: not done as of this date; PLAN.md was not relabelled.*
7. ~~**Explain the tri collapse on L6 and M2.**~~ **ANSWERED 2026-09-03 --
   see section 8.** With the acceleration deadband raised until the term is
   off, L6 goes 47.95 -> 54.76 and M2 49.48 -> 52.46, recovering 6.81 of the
   7.57 dB and 2.98 of the 4.12 dB. The acceleration term firing on flat and
   periodic interiors is the cause, as predicted.
8. **Test the O6 window-end asymmetry**: re-run the O6 jerk sweep with the
   anchor side swapped (JERK_CENTRE=+0.5) and on a clip padded by four frames.
   If the 0.18-0.44 misses move to frames 2-6 or vanish, they are a window
   artefact, not the floor.

   *2026-10-01: partly run on 2026-09-03 (section 8): swapping the anchor side made every frame worse and did not move the asymmetry; the padded-clip test was not run.*

## 6. Predictions vs outcomes

Written 12:14, before the ladder ran (17:19-18:07).

    P1  quad > tri only at O3 (+0.8..+1.3), O2/O1 flat         O3 +0.98, O2 -0.08, O1 -0.17      confirmed
    P2  quad < tri by 0.1-0.9 on no-jerk families               A/F/L/M -0.0..-0.90 (L6 +3.64, M2 +0.61 excepted, see 4)   confirmed
    P3  L6 +3.18 reproduces 50/50                               +3.64, as a tri collapse           real, reframed
    P4  Windows within 0.3 dB of the Apple Silicon build on shared cases   O3 -0.06, L1 -0.08, O6 +0.39, L6 +0.46   2 of 4
    P5  quadlsq < quad on O2/O3/O5, >= 0.3 at O3                -0.20 / -0.58 / -0.24              confirmed
    P6  quadlsq >= quad on no-jerk families                     -0.33..+0.06, L1 -3.99             refuted (mechanism: far flow under the accel deadband)
    P7  residual: O3 >> A2                                      A2 rises with velocity past O3     refuted (residual = flow failure)
    P8  rotation dB N-independent (< 0.5)                       max spread 0.23                    confirmed
    P9  rotcheck tri ~ quad                                     identical to the decimal           confirmed
    P10 calibrations reproduce the record                       O5 accel 0.4% / jerk 1.1% of peak  confirmed on textured cases
        (the first attempt on the flat O1-O3/A2 boxes was a method error: no interior texture, nothing to calibrate)

Theory-side, the stopping-point analysis (written before the ladder) had
predicted that the L6 +3.18 would *not* reproduce on Windows and that quad
would trail tri by 0.1-0.6 dB on every non-O3 family. The first is refuted
(+3.64); the second is exceeded by L1 (-0.90) on one side and crossed by
M2_period40 (+0.61), O4 (+0.08), M1 (+0.03) and A7 (0.00) on the other. Both
are kept on the record.

Rotation controls (pre-registered separately, 18:22 and 18:29): PA F3 clean --
confirmed; PB/PC "aperiodic" rotating blobs fine -- refuted (the texture has a
19.8 px near-period; the control was mis-designed and is recorded as such,
and PF/PG (R4/R5 velocity fields clean: median < 1-1.5 px, < 10-15% gross)
and PI/PJ (R4/R5 acceleration fields within 40-50% / 25-30 deg) fell with it
-- refuted at 58-83% and 67-79% gross with medians 10-23 px, and 96-186% and
76-145% vector error); PD R6 locked -- confirmed; PE ordering -- refuted (flat
blobs outscore textured ones: flat interiors hide flow errors); PH R6 lattice
peak -- confirmed; PK residual localises R3 -- confirmed; comb collapse at
6/10/14 px/frame -- confirmed, and the "integer at a finer level rescues"
fine structure at 8/12 -- refuted (they collapse too).

## 7. Method notes

- Every render on the RX 6600 (Adrenalin 26.8.1). The O5 acceleration field
  rendered on the Radeon Pro 560X (older driver) agrees to three decimals on
  19 of 20 frames (f7 +8.062 vs +8.078, true +8.195): the tri acceleration
  path agrees across the two GPUs on this one case and field; jerk-field and
  PSNR parity between them has not been checked, so the 6600 is
  provisionally validated for field work.
- Calibrating a field on a flat rectangle is not a measurement: the O1-O3 and
  A1-A3 scenes have no interior texture and exist for placement PSNR. Only the
  textured cases (A4-A7, O5, O6) calibrate the field. Recorded here so the
  mistake is not repeated.
- The residual and jerk fields are heavy-tailed; quote medians and
  percentiles. A mean over a field with a 23-sigma tail is a count of
  outliers.
- Every field calibration here is against the DISCRETE difference (the
  CORRECTION's convention). The continuous derivative differs by the
  attenuation factor (sin(w/2)/(w/2))^k -- 3.5% on O5's acceleration -- so
  "wobble is measured, not suffered" holds for the discrete quantity the
  shader actually estimates.
- Raw logs and scratch scenes for the controls and the comb are not in the
  repository; the scene definitions are one-line variants of scenes.sh's
  _rect and _blob (TEX_M1 box at 144/192/240/288/336*T px/s; TEX_M2 and TEX_M1
  blobs under theta = 2.56 T and 2.56 T^2) and are trivial to recreate.

## 8. 2026-09-03: the prefilter built and refuted, and two leads closed

Same platform, same day-after. Predictions from section 5 were built and run.

**The prefilter is refuted, and the mechanism runs opposite to the
diagnosis.** Each coarse level was rebuilt as an exact box average over its
own footprint (an N x N grid of bilinear taps at 2-texel spacing; the
transform is mechanical and was applied to all three shaders). Measured:

    speed (px/frame)      6      8     10     12     14   |  16 (control)
    stock              29.27  30.64  27.97  27.79  29.63  |  46.91
    prefiltered        31.07  32.11  30.59  29.39  29.23  |  28.64

The comb gains 1.5-2.6 dB where >= 40 was pre-registered, and the 16 px/frame
control loses 18.27 dB. On the full ladder the prefilter helps low-frequency
moving content (L3 +3.39, L9 +2.59, A2 +2.33, A3 +1.97, A1 +1.47, O1/O2/O4
+0.7 to +1.2) and destroys anything whose signal is fine: M1 -18.27,
A4 -17.81, F3 -19.86, L0_static -15.07, M2 -14.04, L6 -10.99, A5 -10.55,
L1 -8.71, F1 -7.27. Rotation controls: R4 +0.79 and R5 +0.86 against the
>= 34 dB predicted (refuted); R3 -1.06 and R6 -0.10 unchanged (confirmed,
period locking is a separate mechanism); R1 +1.02, R2 +0.11.

**Why, confirmed analytically.** A box matched to a level's own footprint
keeps only **11% of TEX_M1's variance at 1/16** (contrast x0.33; 28% at 1/8,
49% at 1/4), because four of that texture's five components sit above the
level's Nyquist and the box annihilates them. Point sampling keeps 100% of
the contrast, as a Moire. **The aliased detail is load-bearing.** At exactly
one coarse texel per frame the Moire is shift-invariant, so the aliased match
is *correct*, which is why the 16 px/frame cases score 46.9 and why removing
the aliasing costs 18 dB. Point sampling: full contrast, wrong motion at
every other speed. Box: right motion, nothing left to match on. Both fail on
fine texture, for opposite reasons.

The clearest single symptom is **L0_static**, a scene with no motion at all:
stock scores the 79.43 dB round-trip ceiling, prefiltered scores 64.36. A
matcher given a near-flat coarse level invents motion where there is none,
which is the degenerate-SAD tie-breaking failure this project already
documented, reached by a new route.

**So the replacement lead is a per-level trust gate, not a filter**: decide
per texel and per level whether that level's honestly-filtered contrast is
high enough to seed from, and fall back when it is not. The shader already
carries `local_contrast_5x5_s()` machinery to build on. A blur/contrast
trade-off sweep (S-only, SE-only, half-width, tent) is queued; if no point on
that curve helps the non-integer speeds without costing the integer one, the
filter approach is finished and the gate is the only way forward.

**The L6/M2 collapse is explained** (section 5 item 7, as predicted). Running
the three-frame shader with its acceleration deadband raised until the term
is inert:

    case              bi      tri   accel-off    recovered
    L6_flat_large   55.52   47.95     54.76      6.81 of 7.57 dB
    M2_period40     53.60   49.48     52.46      2.98 of 4.12 dB
    M1_noise_large  46.91   46.08     46.12      none
    F1_fourier_edge 46.93   45.77     45.50      none

The acceleration term firing on large flat and periodic interiors is the
cause. F1's and M1's smaller deficits are something else and remain open.

**The O6 jerk asymmetry is real.** At the host's own window side the late
frames miss by 0.179 / 0.317 / 0.437 / 0.267 / 0.305 px/interval^3 while the
mirror-phase early frames, at the same true jerk, miss by 0.000 to 0.184. A
symmetric noise floor cannot produce that. Swapping the anchor side makes
every frame worse (confirming the recorded convention) but does not move the
asymmetry, so the cause is still open; the clip-tail padding test was not run.

**Two jobs measured nothing, and both were mine.** The sigma_f measurement
read velocity fields inside L1 and L2, which are flat boxes with no interior
texture -- the exact flat-scene error recorded in section 7 the day before,
repeated the day after -- and it rendered through the prefiltered shader that
had just been shown to break fine-texture matching. Void, re-queued on stock
with textured cases. The noise-ratio job compared the spread of the
acceleration and jerk fields, but 73-78% of the jerk field's texels read
exactly zero because the provenance gate zeroes them before the diagnostic is
emitted, so the statistic measured the gate and not the stencil; sqrt(3)
versus sqrt(11/2) needs the ungated fields and is re-queued that way. Neither
number should be quoted from the first attempt.

**Addendum, same day, after the trade-off sweep and the corrected re-runs.**

*The filter approach is finished.* Five variants (full box, half-width box,
tent, S-and-E only, S only) on the comb and the 16 px/frame control: every
one drops M1 to 28.5-30.5 dB, and the best non-integer gain anywhere is +2.6
(M5 under the full box). Touching only the coarsest level costs 17.6 dB on
M1. The losses are not the contrast gate either: the S-level gate is an
absolute MIN_CONTRAST = 0.02 on a 5x5 max-min, and a box-filtered TEX_M1
still spans >= 0.125 at S (point-sampled: >= 0.315), while a filtered flat
box passes MORE texels through the gate (380 against 304), not fewer. So the
fine-texture mechanism is what section 8 says: SAD degeneracy on a near-flat
level. The flat-content losses (L6 -11, L0 -15, L1 -9 dB) are explained by
NEITHER the gate nor the filter width -- a correctly sized 16 px box barely
softens a 300 px edge -- and are open. The one candidate: a softened edge
broadens the S-level cost surface enough for the small-magnitude bias or a
near-tie to pick a neighbouring coarse texel, a 16 px seed error the finer
levels cannot reach back from. Untested.

*sigma_f is measured: 0.070 px.* Robust std of the stock four-frame shader's
N:N velocity field against analytic truth over M1's interior; p90 0.26,
p99 0.34, no texel beyond 0.5 px, identical on every frame. That is the
middle of the 0.02-0.12 bracket section 1 assumed, so the N = 3-or-4 verdict
stands as written. L7 returned 8.2 px with 65% of texels gross -- not noise
but the period-locking failure (texture period 15.7 px at 16 px/frame), so L7
measures a failure, not sigma_f. One content class at one speed: fine
aperiodic texture moving exactly one coarse texel per frame, the matcher at
its best.

*The jerk/acceleration noise ratio, measured properly: 1.0 to 1.4, and the
correlated model reproduces it.* The paragraph this replaces claimed
0.63-0.80 and "both models refuted". That was a DECODE ERROR of mine: the
two ungated jerk renders were meant to set JERK_DIAG_FS to 1.0 (A4) and 4.0
(A6), but the sed pattern used one space where the shader's column-aligned
constant has two, the substitution silently did not take, the fields were
emitted at the default 2.0, and the reader decoded them at 1.0 -- every jerk
reading halved. The acceleration sed had matched. The batch-1 job asserted
every patched constant; batches 3-4 asserted only the trust gate. The third
time today a column-aligned constant defeated an exact-match sed.

The measurement that replaces it is stronger than the one it corrects. A
scratch variant emits the solve's three inputs as diagnostic modes --
f_prev (k -> k-1), f_next (k -> k+1) and the composed far flow -- on A4 and
M1, and the jerk rebuilt from them through the shader's own stencil matches
the directly emitted jerk field texel by texel (correlation 0.998-1.000 on
every frame checked). At N:N on the ffmpeg host frame k is slot 2 and the
composed link runs BACKWARD, taus (-1, +1, -2), so the stencil is
a = f_prev + f_next and j = f_next + 3 f_prev - f_far -- the form
QUADDIRECTIONAL.md already records for the N:N window; a first reconstruction
with the 24->60 form disagreed by construction. With flow errors e_p, e_n and
the link's own e_l:

    e_a = e_p + e_n                 e_j = e_n + 2 e_p - e_l

    scene  sigma_p sigma_n sigma_l  r_pn  r_nl  r_pl  a std/rob   j std/rob   j/a std/rob
    A4      0.139   0.151   0.163   0.36  0.34  0.33  0.42/0.30   0.59/0.35   1.40/1.15
    M1      0.093   0.093   0.093   0.90  0.89  0.96  0.15/0.19   0.16/0.19   1.07/1.00

(rob = 1.4826 MAD; A4 medians over frames 4-19; M1 identical on every
frame.) Put the measured covariance into the stencil algebra and it returns
the measured spreads: at equal sigma,

    var_j / var_a = (6 + 4 r_pn - 2 r_nl - 4 r_pl) / (2 + 2 r_pn)

gives 1.41 for A4 (measured 1.40) and 1.02 for M1 (measured 1.07). So the
ratio is not a constant of the stencil. It is sqrt(3) = 1.73 only when the
three flow errors are independent; it falls to 1.4 when they are mildly
correlated (A4, 0.35) and to 1.0 when they are almost entirely common-mode
(M1, 0.9), because the stencil's coefficients (+1, +2, -1) cancel a shared
error. Consequences: section 1's C(2k-2, k-1) growth is the independent-noise
upper bound; on the matcher's best content the jerk field is no noisier than
the acceleration field, and the jerk SNR on real-footage motion is up to
1.7x better than section 1's table says. Whether the same correlation helps
a fourth difference is unknown until one is built. sqrt(11/2) was never
right for either host; recommendation 5 is answered. Also measured on the
way: the F-level flows on M1 spread 0.093 px against 0.070 for the H-level
straddle flow read through mode 7 -- two different estimators -- so
sigma_f on the matcher's best content should be quoted as 0.07-0.09.

*The fifth frame, re-examined with the measured correlation.* With the
flow-error covariance in hand, the four-frame stencil and three five-frame
candidates were run on x = A sin(w t) at A = 40 px with the A4 noise model
(sigma 0.15, r 0.35; the M1 model gives the same shape), scoring total
error -- truncation plus noise -- against the continuous derivative at each
stencil's own centre. A symmetric five-frame window has displacements at
taus (-2, -1, +1, +2), the composed ones built exactly as the quad builds
its far flow. RMS error in px/interval^k:

    samples/period   accel: 4-frame  5-quartic  5-cubic-LSQ | jerk: 4-frame  5-quartic
        24 (O1)          0.25       0.30       0.12      |        0.34       0.12
        12               0.30       0.30       0.66      |        0.37       0.30
         8               0.91       0.31       3.2       |        1.08       2.0
         6 (O3)          2.7        0.48       9.3       |        4.2        8.0
         5               5.6        1.1       18         |       10.2       18.9
       noise only        0.25       0.30       0.11      |        0.34       0.12

Three things follow, and the first two reverse recommendation 3. (1) The
four-frame acceleration is the plain second difference f_prev + f_next,
whose truncation on a sinusoid is (2 sin(w/2)/w)^2 - 1: -8.8% at six samples
per period, 2.7 px RMS against O3's 44 px peak. The symmetric quartic
corrects it and is 3-6x better at eight samples per period and fewer. That
is where the fast-oscillation regime of section 1 actually pays -- in
acceleration, not in snap. (2) On slow motion the symmetric window's jerk
stencil has coefficients of +/-0.5 on each flow against the asymmetric
window's (+1, +2, -1), so its noise is 0.81 sigma_f against 2.30 at r = 0.35
(0.32 against 2.05 at r = 0.9): 2.8x cleaner at 24 samples per period, 6x on
the matcher's best content -- the floor-limited real-footage jerk band of
section 4. (3) The compact four-frame stencil keeps winning jerk at eight
samples per period and fewer, where the wider odd stencil's truncation
dominates, and it edges the quartic's acceleration at 24 (0.25 against 0.30:
the composed flows' lever arm costs noise when there is no truncation to
buy back). The fixed-degree cubic fit halves the acceleration noise at 24
samples per period and is catastrophic below about sixteen -- section 2's
wobble finding, quantified. Snap is noise below five samples per period, as
section 1 said.

So the right fifth frame is an exact quartic over a symmetric window with
its snap row ignored, chosen per regime; the fixed-degree fit recommended
in section 5 is the wrong tool except on very slow content. Costs stated
plainly: a symmetric window at N:N needs frame k+2 (two frames of latency
instead of one); the 16-texture bind ceiling (a naive fifth slot needs 21)
has to be met by packing four luma levels into one RGBA texture; the
generator gains a slot; and at 24 -> 60 the output sits off the window's
centre, so this is a gain for the field instrument first and the
interpolator second. Pre-registered for when it is built: O3's N:N
acceleration error falls from 2.7 to about 0.5 px RMS; the A6 jerk-null
floor falls by 2.8x; L1 and the other slow cases lose nothing beyond 0.05
dB. Scripts: the session scratch cov/n5.py and cov/n5sim.py.

*Late the same day, from the 3D programme (THREEDIMENSIONAL.md section
9.7): the point-sampled level's rule, and what the A-series was hiding.*
A7's velocity field is 39-75% wrong on its mid-speed frames (4-11 px/frame)
and 1-11% wrong at one coarse texel per frame. The wrong readings are the
texture's lattice aliases d + L, with L = (+/-20, -/+20) or (+/-40, 0) for
TEX_M2, and the winner on every frame is whichever candidate lies nearest
an integer coarse-texel shift -- section 3's shift-invariance statement
with the lattice added, and the mechanism behind the comb, R3/R6, D9 and
A7 at once. The A-series acceleration calibrations pass through it because
the backward flow aliases by the mirror vector and f_prev + f_next cancels
the pair; the jerk stencil does not cancel it. Measured the same evening: on the
mid-speed frames the round-trip gate blanks 77-86% of the acceleration
texels (the alias fails to round-trip unless the reverse flow aliases
identically), and on the frames the gate passes the acceleration reads
within 2-13% while the jerk, truth zero, reads a median of up to 0.65
px/interval^3 with 35-60% gross (THREEDIMENSIONAL.md section 9.7). The
gate is why the acceleration field survives lattice texture at all; the
jerk-null floor on such texture is frame-dependent and far above the A6
clip median. Section 5's item 1 has a
successor at last: carry the best two coarse minima down as seeds and let
the resolved finer levels arbitrate. Pre-registered against A7's mid-speed
field, the comb and R4/R5.

How the alias is produced, from the search's own structure. The coarse
level does not search a window; it descends -- five iterations of a 3x3
probe from zero offset, step 0.75 then halving, on a 3x3 SAD plus a small
magnitude prior, reach 1.45 texels. On a point-sampled lattice texture the
descent lands on the nearest integer-texel minimum of the Moire, (1, -1)
texels = (16, -16) px, which is what A7 reads; the next level's +/-2-texel
refine (+/-16 px) then reaches the exact symmetry vector (20, -20), where
the SAD is identically zero, so no finer level can reject it by SAD -- only
the magnitude prior can. So the successor to the prefilter is two descents,
not two minima from one window: one from zero and one from the best of a
coarse +/-1-texel grid (or last frame's flow), both carried to the next
level and arbitrated there by SAD plus the prior. Costed and pre-registered
in the work queue; a shader change, so a proposal until agreed.

*The two-descent gate, built and measured the same evening (agreed as the
next shader step; the five-frame window deferred).* Implemented as a
transform of the bidirectional base -- the generators build the three- and
four-frame shaders from that base, so the change propagates on
regeneration -- in scratch: each coarse pass runs a second descent from
the best point of the +/-1-texel ring at least 0.75 texel from the first
result and stores both seeds in the cache's unused .zw; each 1/8-res pass
refines both and keeps the lower SAD plus a magnitude prior of 0.06 per
texel toward zero. Scratch tri and quad regenerated from the variant with
the machinery intact. Against the pre-registration, the verdict is split:

    case                        stock   two-descent   pre-registered
    L1_trans_8px (flat, edges)  61.24     75.01       "unchanged" -- +13.8
    L6_flat_large               55.52     65.48       "unchanged" -- +10.0
    M1_noise_large (16 px/f)    46.91     49.75       "unchanged" -- +2.8
    comb M5/M6/M7/M8/M9      28-31   +0.2..+1.8 (M7 -0.3)   >= +6 dB: REFUTED
    R4 / R5                  29.95/30.09  +0.2/+0.2          >= +3 dB: REFUTED
    L0, R3                        --     unchanged           unchanged
    L7                          25.25     24.85              -0.4, a wart
    A7 mid-speed velocity, gross  ~46%    ~70%               <= 35%: REFUTED, harmful

The three results say three different things. Where a correct basin
exists at the coarse level and the descent from zero was missing it --
edge-driven objects at sub-texel speeds, fine texture at exactly one
texel -- the second descent finds it and the gain is large and
unpredicted (and it propagates: the scratch tri and quad read 74.3 and
74.0 on L1 against their stock 61.4 and 60.5). Where no correct basin
exists -- aperiodic super-Nyquist texture at non-integer speeds, the comb
-- a second wrong basin is no better than the first, which is the
load-bearing-aliasing finding again from the other side. And where the
competing basin is an exact symmetry of the texture, A7, the gate is
harmful: the alias's SAD at the next level is identically zero, a prior
of 0.06 per texel cannot outweigh any nonzero SAD at the true sub-texel
displacement, so the second descent finds the alias more often and the
arbitration keeps it. That was the design's own stated weak point, now
with a number on it. The one knob that separates the two basins on an
exact-symmetry texture is the prior's weight, and it trades directly
against the velocity-ceiling cases L3 and L4, where a strong pull toward
zero under-tracks genuine fast motion. Running: the full ladder for the
variant, and a sweep of the prior at 0.3, 1.0 and 3.0 on A7 against L1,
L3, L4, M1 and L6. Not shippable as it stands; the flat-and-edge gain is
the thing to keep whatever the sweep says.

The full ladder makes the split exact. Stock against the variant, 32
cases: 12 gains above 0.5 dB, 10 losses, mean +1.49 dB. Every edge-driven
or integer-speed case gains -- L1 +13.8, L6 +10.0, L2 +9.1, M2 +6.2, L8
+5.6, F1 +4.6, M1 +2.8, L9 +1.7, A1-A3 +0.9 to +1.7, L3 +1.6 -- and every
case textured with the exact-symmetry sine product loses: A6 -2.6, O6
-2.5, O5 -2.5, A7 -2.4, A5 -1.1, A4 -0.8, with R1 and L7 -0.4, L4 and R2
-0.1, and the rest unchanged within 0.5. The losses are the A7 mechanism
on the ladder's own calibration cases; the gains are the missed-basin
mechanism on everything else; the arbitration is the whole question. A
magnitude prior is the weakest tie-breaker there is against an alias whose
SAD is exactly zero. The strongest cheap one is time: the previous
window's flow at the same texel already sits in the storage cache and is
read before it is overwritten, and on every ladder case the true flow is
within about two pixels of last window's while the alias is twenty to
thirty away. Two temporal variants -- a temporal prior at the arbitration,
and a temporal second seed -- are queued behind the magnitude sweep on the
loss cases, the big-gain cases and the velocity ceiling.

The magnitude sweep finds a knee. Prior weight per E-texel against the
five cases that bound the trade-off, and A7's mid-speed velocity field:

    prior          0 (stock)   0.06    0.3     1.0     3.0
    L1_trans_8px      61.24   75.01   75.01   76.55   61.25
    L3_trans_23px     40.48   42.03   42.62   42.55   41.86
    L4_trans_40px     31.57   31.47   31.51   31.48   31.46
    L6_flat_large     55.52   65.48   65.48   63.58   55.26
    M1_noise_large    46.91   49.75   49.82   47.75   45.52
    A7 gross, mid     45.6%    70%    44.9%   44.7%   44.3%
    A7 accel coverage 35.8%     --    49.7%   49.5%   50.2%

At 0.3 every gain survives, the velocity ceiling is untouched (L4 within
0.06 dB), and the lattice case returns to stock with fourteen points more
acceleration coverage. At 3.0 the prior overrides the SAD outright and the
shader reverts to stock to the hundredth on L1 and L6, which is the proof
that the first descent is the stock path. No weight of magnitude prior
beats stock on the lattice: the coarse Moire has no minimum at a
non-integer true displacement, so no descent lands there, and whether the
next level can reach it depends only on which basin the second seed fell
in -- which is what the temporal seed is for. (Correction on the way: the
stock coverage figure quoted above as 14-23% was inferred from the
acceleration medians; measured with the same reader it is 35.8%.) What
0.3 has not yet been measured on is the rest of the lattice cases, A4-A6
and O5/O6, at -0.8 to -2.6 under 0.06; that measurement and its full
ladder are the ship gate and are queued behind the temporal variants.

The temporal variants split the cases complementarily, and that is the
most useful thing the gate has said so far. Both at magnitude 0.06 with a
temporal prior of 0.5 per E-texel on distance from the previous window's
flow, read from the cache before it is overwritten:

    case             stock   ring 0.06   T1 ring+temporal   T2 temporal seed
    A6 (lattice)     36.18     33.60         34.99               37.70
    A7 (lattice)     37.01     34.65         34.94               37.68
    O5 (lattice)     33.09     30.61         32.25               33.83
    O6 (lattice)     32.73     30.20         30.63               33.58
    L1 (edge)        61.24     75.01         75.02               61.24
    L2 (edge)        41.76     50.81         68.57               41.77
    L6 (edge)        55.52     65.48         65.46               55.52
    M2 (integer)     53.60     59.82         59.77               53.60
    L3 / L4 (ceil)   40.48/31.57  42.03/31.47  42.69/31.50       40.60/32.10
    A7 field, gross   45.6%     70%           53.4%               43.3%
    A7 accel cover    35.8%      --           37.5%               57.4%

The ring seed keeps every edge and integer gain and lifts L2 by a further
eighteen decibels, and still loses on every exact-symmetry lattice. The
temporal seed is the first variant to *beat* stock on every lattice case
-- and on A7's field it is the best measured, 43% gross and 57%
coverage -- and it gives up every edge gain to the hundredth of a
decibel, because on those scenes the previous window's flow is the stock
answer and the temporal prior then keeps it. The ring finds the better
sub-texel basin the descent from zero misses on edges; the temporal seed
finds the true basin on lattices; neither finds both. A three-descent
variant -- zero, ring, previous flow, with the next level refining all
three and arbitrating by SAD plus both priors -- is queued, with its
render time, behind the timing of the two-seed variant. Cost is now part
of every ship decision: a variant that costs time ships beside the stock
shader as its own file, generated from its own base by the generators'
new base argument, and the stock files stay byte-identical.

*The ship gate: the two-seed variant at a magnitude prior of 0.3 on the
full ladder.* Stock against the variant, 32 cases: **20 gains above 0.5
dB, 2 losses, mean +2.43 dB.** Every lattice case that lost under 0.06 now
gains -- A4 +0.9, A5 +1.0, A6 +0.7, A7 +0.8, O5 +0.4, O6 +0.3 -- the edge
gains hold and grow (L2 +20.6 to 62.32, L1 +13.8, L6 +10.0, M2 +6.3, L8
+6.1, M1 +2.9, L3 +2.1, L9 +1.8, A1-A3 +1.1 to +2.3, F1/F2 +0.8/+1.1), and
rotation improves for the first time in the record (R1 +0.6, R2 +0.5, R3
+1.4). Unchanged within 0.5: L0, L5, M3, M4, O1-O4. The two losses: L4 at
-0.06 (the velocity ceiling, within noise) and L7 at -0.52 (the
period-locking case, real and small). On the ten-case table the variant
is at or above stock everywhere but L4, and it is beaten only by the
temporal seed on A6 and O6 and by the ring-plus-temporal-prior on L2. The
pre-registration is another matter and stays on the record as written:
the comb was to rise by 6 dB, the rotation controls by 3, and A7's field
was to fall to 35% gross; at 0.3 A7's field sits at stock's 45%, and the
comb and controls have yet to be benched at 0.3 (queued). The gate does
not do what it was predicted to do; it does something broader.

The decision, under the rule that a change costing render time ships as
its own file: this variant is shippable as a variant once its render time
is measured (queued), and the stock bidirectional, tridirectional and
quaddirectional shaders stay byte-identical. The three-seed variant is
still being measured and may supersede it on the lattice cases.

Render time, measured as the rule requires (O5, 60 output frames at
24 -> 60, ffmpeg's own benchmark clock, median of three runs, whole
process): bidirectional 2.69 s stock against 3.04 s with two seeds, +13%;
quaddirectional 4.11 s against 4.45 s, +8%. The coarse pass doubles at
1/16 resolution and the 1/8-resolution pass doubles its search; nothing
finer changes. That is a cost, so the variant ships as its own file and
the stock shaders stay as they are. Run-to-run spread on this machine is
about +/- 10%, so the cost is known to about a third of itself; the
ordering held in every run.

*Three seeds, measured.* Zero, ring and previous flow as the three coarse
descents, the third seed in a second storage cache per coarse pass (which
exposed and fixed a generator assumption of one texture block per pass),
priors 0.3 and 0.5, every seed refined at 1/8 resolution and arbitrated
there. On the ten-case set against stock: A6 +2.7, A7 +0.8, L1 +13.8,
L2 +28.8, L3 +2.3, L4 +0.4, L6 +9.2, M2 +6.2, O5 +1.1, O6 +1.0 -- every
case up, the first variant for which that is true. Against the two-seed
variant at 0.3 it adds A6 +1.9, L2 +8.2, L4 +0.5, O5 and O6 +0.7 and gives
back L6 -0.75. A7's mid-speed field: 39.6% gross (stock 45.6%), acceleration
coverage 64% (stock 36%) -- the coverage pre-registration met, the gross
target (35%) not. Render time 3.02 s against stock 2.69, +12%: the third
refine at 1/8 resolution costs nothing measurable over the second, so the
three-seed variant sits in the same cost tier as the two-seed one. It is
the variant to ship, subject to its full ladder, which is running.

*Three seeds on the full ladder.* Stock against the three-seed variant,
32 cases: **21 gains above 0.5 dB, one loss, mean +2.71 dB.** The two-seed
variant's two small losses are gone (L7 -0.02, L4 +0.43); the comb gains
0.3-1.6 and the rotation controls +0.5 to +1.3, still nowhere near the
pre-registration; the quad generated from it costs +4% (4.28 s against
4.11, the two-seed quad 4.45; all within the +/- 10% run-to-run spread of
one another, so call the family +4 to +12%). The one loss is A5 at
-2.91 dB, a lattice-textured calibration case the two-seed variant had at
+0.96. That has the signature of the temporal seed making an alias sticky
across windows in one speed band -- the previous window's wrong flow
seeding the next -- which is the hysteresis risk the temporal prior was
noted to carry. Whether A5's *field* is corrupted, or only its warp, was
measured before the ship decision, because the field is the variant's
first customer. It is corrupted. Frame by frame on A5, three seeds
against stock: velocity gross fraction 84 / 75 / 66 / 46 / 27 / 22% on
frames 5-10 against 78 / 59 / 48 / 23 / 12 / 15%, and 64 / 65 / 79 / 56%
on frames 18-21 against 57 / 46 / 76 / 43%; acceleration coverage on
frames 8-10 falls from 76 / 100 / 100% to 42 / 65 / 84%. The alias chosen
around frame 4-5, where stock is also mostly wrong, is carried forward
by the temporal seed into frames where stock recovers. That is the
hysteresis the temporal prior was noted to risk, now measured, and it
disqualifies the three-seed variant as the field's shader. **Decision:
the two-seed variant at prior 0.3 ships**, under the rule set before
looking -- twenty gains, no loss beyond 0.52, A5 +0.96, +13% and +8% --
and the three-seed variant stays a lead with this diagnosis. The obvious
repair, for whoever picks it up: let the temporal seed compete only when
the previous window's flow at that texel round-tripped, so a wrong flow
cannot seed its own successor.

*Real footage, the same evening.* The shipped two-seed variant through
realbench.sh on the avengers clip at the record's five segments, six arms
in one run. The run reproduces the record's own numbers (linear 31.90 /
0.9451 exactly; base 34.29 / 0.9647 against the recorded 34.34 / 0.9655;
variational 36.27 / 0.9741 against 36.31 / 0.9750), and its passthrough
check sits where those runs' did (retained frames 55-62 dB, none bit-exact
after the yuv420p round trip), so the comparison is on the published
footing. Synthesised frames, means over the five segments:

    arm            PSNR    SSIM      arm               PSNR    SSIM
    linear         31.90   0.9451    quad (stock)      34.22   0.9635
    base           34.29   0.9647    quad -twoseed     34.41   0.9639
    -twoseed       34.48   0.9651    -variational      36.27   0.9741

So on real footage the variant is +0.19 dB and +0.0004 SSIM over the base,
every segment at or above it, and the same margin for its quad over the
stock quad: a small, consistent gain, nothing like the ladder's +2.4 mean.
The ladder's large gains are on content whose failures the coarse seed
decides outright -- flat edges at sub-texel speed, integer-speed fine
texture, exact lattices -- and real footage is decided by coherence, which
is what the variational cascade adds and this variant does not. The
recommendation in SHADERS.md is unchanged: the variational build for
viewing, this variant for the fast tier and for the field.

*The pre-registration, closed.* The two-seed variant at 0.3 on the cases
the gate was built for: comb M5 +1.2, M6 +0.3, M7 +0.3, M8 +2.2, M9 +1.0
against a pre-registered +6; R4 +0.5 and R5 +0.5 against +3; A7's
mid-speed field 45% against 35% (39.6% with three seeds). All gains, none
near the prediction, and the reason is now understood rather than
guessed: on aperiodic super-Nyquist texture at non-integer coarse speeds
there is no correct basin at the coarse level for any seed to find, so a
better choice among coarse basins cannot help there. The gate was
predicted to fix the comb and instead fixed the edges, the integer-speed
textures, the lattices and rotation; the comb waits for something that
changes what the coarse level sees, not how it chooses.

*The three-seed repair, measured (2026-09-03 evening).* The three-seed
variant's A5 field hysteresis came from an ungated temporal seed: a wrong
flow, once cached, re-seeded itself. Variant R keeps the three descents
(zero, ring, temporal) but trusts the temporal seed only where the cached
forward flow and the reverse flow at its landing point close a round trip
within one E-texel (`SEED_RT_MAX = 1.0`), and adds a temporal prior at E
(`SEED_TEMP_LAMBDA = 0.5`) only under the same trust. Against the
pre-registration: A5 back to +1.02 over stock (asked: at least +0.9; the
two-seed's +0.96), A6/O5/O6 at +3.30/+1.64/+2.38 (asked: keep the
three-seed's +2.67/+1.07/+1.04), A7's field 37.5% gross at 66.7% coverage
(asked: at most 40%), and no ladder case more than 0.10 dB below the shipped
two-seed (M2) or 0.07 below stock (L4). Ladder mean over 32 cases: R +2.90
over stock, against the two-seed's +2.43 and the ungated three-seed's
+2.71; eleven cases gain more than 0.1 over the two-seed, none loses more
than 0.1, and the two-seed's one real ladder loss (L7, -0.52) is gone
(+0.04). The ungated three-seed still beats R on L2 by 8 dB (70.5 against
62.3, both far above stock's 41.8) and on A3 by 0.8: those were the cases
its unguarded temporal seed happened to get right. Render time, median of
three on the 1280x720 clip: bi-R 2.973 s against stock 2.691, two-seed
3.035, three-seed 3.016; quad-R 4.531 against 4.110 / 4.454 / 4.283 -- the
two-seed's cost, within the run-to-run spread. Real footage, same
decimate-and-reconstruct on the five segments: R 34.74 dB / 0.9663 SSIM
against the base's 34.29 / 0.9647 and the two-seed's 34.48 / 0.9651;
quad-R 34.67 / 0.9651 against 34.22 / 0.9635 and 34.41 / 0.9639. That is
+0.45 dB over the base, more than double the two-seed's real-footage
margin, on every segment. R passes every pre-registered criterion at the
two-seed's cost; whether it replaces the shipped two-seed or joins it is
the owner's call (the two-seed is stateless across frames, R is not --
its temporal seed is gated, not absent). The call was replace and rename:
R shipped the same evening as `bidirectional-interpolation-seeded.glsl`
with its generated tri and quad, and the `-twoseed` files were removed.

*Five more real segments, same evening.* Sampled at random from the owner's
library (anime, film and a 30 fps show; 4-second segments, screened for
full per-frame motion), decimate-and-reconstruct as above: `-seeded` above
the base on all five by 0.17-0.67 dB with SSIM up on each, its quad above
the stock quad by the same margins, the variational build ahead by 0.3-6.1
dB. The table is in SHADERS.md. The 6.1 dB case is flat-shaded anime, the
flat-content weakness of section 8 in numbers on real footage: block
matching there is barely above `linear` (which beats it on SSIM), and the
variational cascade's coherence is worth six decibels.

*The flat-content weakness, diagnosed on real footage (2026-09-03 night).*
On the flat-shaded anime segment the loss is not where the name says. Split
by local texture (mean gradient over 15x15 of the truth frame, quartiles;
per-frame dB, the segment's one cut frame excluded), every arm including
`linear` sits at 46-47 dB on the flattest quartile and the base only trails
by 0.5-2 dB on the middle two; the whole gap is in the most textured
quartile -- the line art -- where the base scores 29.6, the seeded 30.1 and
the variational 36.0 dB. Line art is edges with flat fills either side, and
an edge constrains one component of motion (the aperture problem); the
block matcher's coarse descent wanders on it, and only coherence from
corners and junctions along the edge -- what the variational cascade adds
-- fixes it. The segment's global motion is a slow pan of about 4 px per
interval (phase correlation), so reach is not the issue.

*A cheap coherence step.* Three Jacobi passes per direction at the 1/8
level, inserted after that level's refine: each texel takes the
contrast-weighted mean of its 5x5 neighbours' flow (a neighbour votes in
proportion to its own 5x5 luma range), mixed with its own flow by 8 x its
contrast squared. Six tiny passes. On the seeded base, real footage: the
anime segment 36.89 -> 41.60 dB (variational 42.48), a fast live-action
film segment 32.58 -> 33.96 (34.99), the 30 fps show 32.12 -> 33.65
(34.61) -- more than half the gap to the 115-pass build closed. Ladder
subset: A5 +10.1, A7 +6.9, O6 +10.3, R3 +3.1 over the seeded (the
consensus overrules the lattice aliases), but L1 -22, L2 -8, L6 -9: the
static flat background next to a moving square inherits its flow, because
nothing in one image tells a flat texel which side of an edge it belongs
to. Variants tried the same night: a luma-similarity (bilateral) kernel
suppresses votes inside textures and gives the gains back while only half
restoring the translations (wrong knob); a check against zero flow alone
reverts the wrong texels (the far band is harmless, the near band lies
inside the block window where SAD sides with the object); requiring every
texel to hold evidence proves the far band is harmless. What works is a
three-way SAD check per texel -- propagated, raw, zero -- with texture
keeping the consensus within 10% of the best and flat texels needing
strict evidence: L1/L2/L6 return to the seeded's figures, the real-footage
gains keep 45-70% of the unchecked version's (anime +2.0, film +1.1, show
+1.1 over the seeded), and the textured cases fall back to the seeded's
level, because the raw flow is by construction the 1/8-level SAD minimum
and a SAD check re-trusts the landscape that misled it. So two prizes sit
on the same mechanism: the checked version is a candidate for the fast tier
now; the unchecked version's +10 dB on lattice textures waits for a way to
arbitrate the near-edge band that does not use the 1/8-level SAD -- the
occlusion-boundary problem, which is the variational build's fine-level
data term in disguise.

*Shipped.* The checked version is `bidirectional-interpolation-propagated.glsl`
with its generated tri and quad (the generators now carry a base's extra
per-level passes into every pair's chain). Full ladder against the seeded
base: +0.66 dB mean over 32 cases, 22 up by more than 0.1, three down (L7
-1.3, L1 -0.2, L4 -0.15); largest gains F1/F2 +2.3, L3/O5 +2.0, A4 +1.9,
R2 +1.7, A7 +1.6, A6/L8 +1.5, R1 +1.4. Render time on O5 at 24->60: seeded
3.19 s, propagated 3.28 s per 60 frames (+3%; the stock 2.9-3.2 s across
the night's runs). Real footage, all six segments up: the avengers clip
34.74 -> 35.24 dB / 0.9663 -> 0.9694; the library's anime 46.67 -> 47.09
(the variational's 46.83) and 36.89 -> 38.91, film 45.66 -> 46.41 and
32.58 -> 33.42, the 30 fps show 32.12 -> 33.19. A sibling that keeps the
raw flow whenever it beats zero by 10% and prefers the propagated one when
it also beats the raw (prop8 in the scratch record) scores the same ladder
mean (+0.67) with one loss instead of three but is 0.1-0.3 dB behind on
every real segment and costs +8% instead of +3%; the shipped one is the
one that wins where the fast tier is used. The prove-it-or-zero sibling's
numbers, for the record: A4 54.5, A5 53.5, A6 47.1, O5 40.0, O6 47.3,
R3 37.8 (the seeded: 49.4, 40.2, 39.5, 34.7, 35.1, 30.0) and both anime
segments above the variational (48.25 and 44.20) -- against L2 34.7, L3
33.6, L6 36.2, M1 29.4, M2 28.2 and live action below the stock base.

*Replaced the same night.* A disagreement rule on top of the check --
a textured texel whose consensus contradicts the refine's flow by more than
1.5 texels of the 1/8 level, with neither proven, takes zero (a blend)
instead of trusting the refine -- lifts the lattice-textured cases by 4-12
dB (O6 +12.2, A5 +11.2, A6 +9.8, O5 +7.2, A7 +7.2, A4 +4.7, R3 +4.1 over
the seeded base) with the translations intact, because it keys on the one
signal an alias cannot fake: its own neighbourhood. Against the seeded
base the shipped file is now +2.14 dB ladder mean, 21 up, four down (L4
-1.8, L7 -1.4, A3 -0.2, L1 -0.2); render time 3.15 against 3.12 s; real
footage the avengers clip 35.15 dB / 0.9690, the library 47.27, 40.99,
46.61, 33.21 and 33.02 dB, all above the seeded base, the flat-shaded
anime up 4.1 dB and within 1.5 of the variational. The threshold is the
knob between applications: at 0.75 texels the anime reaches 43.1 dB, above
the variational, and O6/R3 gain another 0.1/3.2, but L3/L4/L7/L8 lose 2 dB
and live action 0.6; without the rule at all (the file shipped an hour
earlier) live action is 0.1-0.2 dB better on three segments and L4 1.6 dB
better, and the ladder mean 1.5 dB worse. 1.5 texels was chosen as the
setting that keeps live action within 0.2 dB of the best while taking most
of the lattice prize. The near-edge band and the true occlusion-boundary
problem remain open; both prizes above are now in the shipped file except
the last 2 dB on the flat-shaded anime.

*And once more, for the fast translations.* With a fixed 1.5-texel
threshold a 40 px/frame translation (L4) lost 1.8 dB: near the object's
edges the consensus is diluted by background votes, disagrees with the
refine's (correct) flow by more than 1.5 texels, and the texel blends.
Scaling the threshold with the flow -- max(1.5 texels, half the flow's own
length) -- keeps that: L4 -1.0 instead of -1.8, A2/A3 +0.2/+0.3, live
action +0.1 to +0.3 on every segment (the avengers clip 35.28, film 33.39,
the show 33.30), against 0.1-0.4 dB less on four lattice cases (O6 46.95,
A7 46.94) and the same ladder mean, +2.14. That is the shipped file.

*The field instrument, its first customer.* The quad generated from the
shipped file, on A7's mid-speed frames with the same instrument as before:
velocity field 26.9% gross (the seeded quad 37.5%, stock 39-75%; the
target set on 2026-09-03 was 35% and this is the first build under it),
acceleration field 33.9% gross (57.6%) at 100% coverage (66.7%; stock
14-23%). The disagreement blend is what does it: on a lattice texture the
texels whose neighbourhood contradicts their alias no longer carry it into
the acceleration stencil.

On real footage the propagated quad now matches the propagated two-frame
shader on every segment (the avengers clip 35.30 against 35.28; the
library 46.47, 40.58, 46.42, 33.30, 33.22), where the stock and seeded
quads trailed their two-frame bases by 0.2-0.3 dB.

*The animation fork (2026-09-04 morning).* The owner's call: hand-drawn
content is its own application -- flat fills, information in the line
art, no natural depth -- and deserves its own file. The finer disagreement
threshold (0.75 texels, with the flow-scaled term kept) ships as
`bidirectional-interpolation-animation.glsl` with its tri and quad: the
flat-shaded anime 42.50 dB, matching the variational build's 42.48 at a
third of the passes, the other anime segment 47.22, live action within
0.1 dB of the general file, and on the ladder the same +2.14 mean with R3
+1.0 and A5 +0.2 more and R1 -0.6, L7 -0.4, L4 -0.3 less. Two more
settings were measured and not shipped: 0.5 texels changes nothing the
harness can see (every case within 0.05 dB, the anime 42.65), and 0.75
without the flow-scaled term reaches 43.1 dB on the anime but loses 2 dB
on plain translations and 0.8 on live action. So the relative term is what
makes the finer threshold safe: below 1.5 texels of flow it is the fixed
threshold that decides, above it the flow's own length, and a pan over a
painted background stays a pan.

## 9. 2026-09-04: the rotation field and A4 re-measured on the shipped family

Section 3's rotation numbers were taken on the stock tri/quad before the
seeded and propagated variants existed; WHAT-WE-BUILT's rotation warning
rested on them. Re-measured at N:N (24 -> 24, TRI_DIAG 2, ACCEL_DIAG_FS 2.0,
16-bit) with `rotcheck.py` on frames 6/9/12/15 (rim inside the search reach)
and `accelcheck.py` on A4 over frames 4-20; RX 6600, the quint under the
fixed host (section 8 of QUINTDIRECTIONAL.md). Coverage is the annulus
fraction carrying a reading at f6 -> f15; errors are medians over live texels.

| case | shader | coverage | vector error f6 / f9 / f12 / f15 | angular error (deg) |
|---|---|---|---|---|
| R2 flat | quad stock | 11 -> 6% | 118 / 138 / 100 / 112% | 61 / 78 / 62 / 96 |
| R2 flat | quad propagated | 25 -> 11% | 121 / 122 / 109 / 103% | 62 / 78 / 76 / 84 |
| R2 flat | quint propagated | 29 -> 14% | 113 / 107 / 101 / 102% | 69 / 74 / 77 / 85 |
| R3 textured | quad stock | 17 -> 15% | 106 / 89 / 119 / 58% | 52 / 41 / 63 / 25 |
| R3 textured | quad propagated | 45 -> 22% | 71 / 59 / 47 / 49% | 26 / 22 / 19 / 21 |
| R3 textured | quint propagated | 47 -> 23% | 86 / 71 / 62 / 62% | 31 / 26 / 23 / 26 |

A4 (a = 0.333 px/interval^2), RMS of the box-median error over frames 4-20:
quad stock 0.055 (17% of the value, the figure WHAT-WE-BUILT carried), quad
propagated 0.036 (11%), quint 0.044 (13%); on frame 10 all three read within
1.4%, coverage 98-100% throughout.

Reading. **R2 is unchanged and will stay unchanged**: the flat blob's field
is the aperture floor of section 3 (54-94% vector error at zero noise, the
tangential spin-up unobservable on an isolated edge); propagation doubles
the coverage with borrowed vectors that are exactly as wrong as the rim's,
which is the register's "a guess there, not a measurement" in numbers.
**R3 is halved by propagation** (vector error 58-119% -> 47-71%, angle
25-63 -> 19-26 deg), the first movement on rotation in the record, and what
remains is the period-locking and pyramid-alias residue of section 3, which
the prefilter could not remove (section 8). **The quint is 10-15 points
worse than the quad on R3 and 2 points on A4**, the A7 pattern of
QUINTDIRECTIONAL.md: the composed +/-2 links carry the alias into the
quartic. Whether that is the far links or the extra chains was a one-render
question, answered the same morning: **the quint's cubic mode 8 reproduces
the propagated quad to the decimal** on both scenes (R3 71.0 / 58.9 / 47.2 /
49.0% and 26.1 / 22.1 / 18.9 / 20.6 deg at identical coverage; A4 0.036,
11%), so the loss is entirely the quartic's composed +/-2 links and the two
extra chains cost the field nothing -- and the quint's inner four slots
produce the quad's flows bit for bit, a consistency check on the generator.
The rotation warning stands as rewritten in WHAT-WE-BUILT.

**The same morning, the riddle narrowed (scratch instruments `rotmap.py`,
the painted views; all at N:N through the propagated quad).** The velocity
field on R3 reads 6-12% inside the disc (median error 0.45-0.55 px at
rim speeds 5-13 px/frame; the painted velocity and acceleration views are
clean hue wheels). The per-texel acceleration error is zero-mean mottle
locked to the texture lattice, not bias: pooled over 12 / 24 / 48 px
windows it reads 20-27% / 14-18% / 10-18% with direction within 7 / 5 / 4
deg (f6-f15). Two mechanisms refuted by measurement: peak locking (the
fractional parts of the measured displacement are flat, and the signed
error has no S-curve against the true fraction) and within-block shear
(the error is 0.45 px at 1.8 deg/frame, 0.53 at 4.8, 1.02 at 7.9 -- a
floor, not a proportion). A control built from the blob primitive itself,
per-texel velocity noise (std per axis, gross excluded), same texture:

| motion | noise |
|---|---|
| translating 8.3 px/frame, texture axis-aligned | 0.28-0.30 px |
| translating 8.3 px/frame, texture at 0.36 rad (R3's f9 angle) | 0.35-0.42 px |
| rotating (R3), propagated | 0.49-0.54 px, gross 7-8% at f5-f9, 35% at f13 |
| rotating (R3), seeded, no propagation | 0.49-0.53 px, gross 30-62% |
| A5 box accelerating, propagated | 0.25-0.36 px |

Rotation's per-texel noise is 1.7x the translation floor on the same
texture (orientation accounts for a third of that), not ten; propagation
removes the gross lattice jumps below ~15 px/frame rim speed and none of
the fine noise. And the comparison that produced "rotation is unreliable"
was never fair: every calibration number in the record is a pooled
median over the object and every rotation number a per-texel median
against a per-texel truth; A4's per-texel spread (IQR +/-0.23 on 0.333) is
of the same order as R3's. The honest statement is now: the acceleration
of a turning textured body is a patch-resolution reading (24 px, ~15%),
not a texel-resolution one; a flat turning body is unreadable; and the
per-texel floor of ~0.3-0.5 px is the matcher's, on every motion. Where
that floor comes from (0.29 px on the cleanest translation is far above
the 0.02-0.07 px median flow error the record quotes, which is a pooled
number too) is the open question that replaces the rotation riddle.

**The per-texel floor, found and removed on periodic texture (2026-09-04,
later the same morning).** The 0.27 px per-texel velocity noise on TEX_M2
translating is the same at 8.33 px/frame, at the integer 8.00 and at 4.17,
the same through stock, seeded and propagated, and a fixed function of the
texture phase (+0.16 -0.15 -0.04 +0.17 -0.27 px over the 40 px period);
TEX_M1, aperiodic, sits at 0.13 with a flat profile. That is not matching
noise and not the sub-pixel step's quantisation: it is the refinement fit's
own vertex for a PERFECT match. The equiangular fit reads the 3x3 costs at
-1 and +1 texel around the minimum, and on any block spanning a fraction of
a texture period those two costs differ, so the vertex moves with the
block's phase even when the match is exact and c0 = 0. The vertex the fit
would return for a perfect match is the fit of the reference block against
ITSELF shifted by -1 and +1 -- computable from one frame -- and subtracting
it makes the fit exact at integer shifts (`SUBPEL_SELFREF`, both half-res
refine passes; four extra 3x3 SADs per texel). Measured through the
propagated quad:

| test | shipped | self-referenced |
|---|---|---|
| TEX_M2 translating 8.00 px/frame (integer), median per-texel error | 0.33 px | 0.001 px |
| TEX_M2 translating 8.33, noise std x / y | 0.28 / 0.29 px | 0.12 / 0.22 px |
| TEX_M1 (aperiodic) 8.33 | 0.13 / 0.14 px | 0.12 / 0.13 px |
| TEX_M2 at 0.36 rad translating, median error | 0.40 px | 0.20 px |
| R3 rotating, velocity std / per-texel accel f9 | 0.49 px / 59.5% | 0.46 px / 53.0% |
| A4 accel, RMS of the box median over f4-20 / per-texel IQR at f10 | 0.036 (11%) / +/-0.21 | 0.026 (8%) / +/-0.09 |
| 24->60 ladder, 32 cases | -- | mean +0.54 dB, 23 up by more than 0.3, 8 within 0.3, L1 -4.73 (73.94 -> 69.21, the near-ceiling flat square) |
| O5 24->60 time, interleaved medians | 5.04 s | 5.16 s (+2.4%) |

Real footage (avengers, the record's five segments): the propagated quad 35.30 dB / 0.9685 SSIM, the corrected quad 35.31 / 0.9686 -- unchanged to the second decimal on every segment (decimate-and-reconstruct at 5/15/21/30/45 s, synthesised frames only).

Shipped as `SUBPEL_SELFREF`: off in every two-frame base, exactly as
`SUBPEL_REFINE` is (the picture shaders are unchanged to the bit), on in
every generated tri, quad and quint, whose ladders move by the table above.
Rotation keeps its second mechanism: the oblique texture's residual (0.20 px
median on the fixed-angle control after the fix, against 0.13 axis-aligned)
and the spatially varying flow on top of it. The comb (M5-M9) and the
integer-speed lattice cases are the natural next check: a bias that was
invisible at integer speeds because every calibration pooled it away should
now be gone there as well.

**The matcher is blind on the diagonal, and every textured ladder case moves
along x (2026-09-04, afternoon).** Found through the rotating disc's painted
acceleration: its outline is a four-leaf clover fixed to the screen at the
diagonal azimuths, where the round-trip trust gate zeroes 70-83% of texels
against 17-40% on the axes. The control: the same textured box at the same
8.33 px/frame, along x and along the diagonal.

| motion at 8.33 px/frame | TEX_M2 (periodic) | TEX_M1 (aperiodic) |
|---|---|---|
| along x | 0.13 px median, 0-1% gross | 0.15 px, 1-2% gross |
| along the diagonal, propagated quad | 94% locked to the lattice copy 28 px away | 0.27 px std, 13-17% gross |
| along the diagonal, stock quad | 99% | 39% gross |

The only diagonal ladder case, L8, is a flat square. Seeds, propagation and
SUBPEL_SELFREF do not touch it. The speed ladder on the TEX_M2 diagonal
convicts the point-sampled coarse pyramid (section 3, mechanism c) rather
than the search geometry, which is identical at every row:

| diagonal speed, px/frame per axis | in coarse texels | result |
|---|---|---|
| 16 | 1 (integer) | 0.10 px, 0% gross |
| 8 | 1/2 | 61% locked, 21 px |
| 4 | 1/4 | 98% locked, 28.3 px |
| 2 | 1/8 | 0.25 px, 0.3% (the refine levels' own reach) |

An aliased level is shift-invariant only for integer shifts of its own
texels, and sin x sin y is two diagonal plane waves of period 28.3 px --
above the 1/16 level's 32 px Nyquist -- whose 40 px axis period is their
beat: along x the coarse level sees a clean sinusoid, along the diagonal a
Moire. The fixed-angle texture (0.36 rad) moving along x is fine, so it is
the motion's direction against the texture's structure, not the texture's
orientation. Section 8's prefilter was judged along x only.

**The zero seed, four passes, not yet shipped.** The 1/8 level resolves the
28 px structure and searches +/-2 of its texels (+/-16 px) around each of
its three seeds; a fourth seed at zero, refined like the others, finds the
true match wherever the coarse seeds are Moire and the motion is within
reach. Measured through the propagated quad, 32-case ladder, five avengers
segments:

| pass | rule | (8,8) diagonal | disc r 40-70 gross | ladder mean | worst | footage |
|---|---|---|---|---|---|---|
| shipped | -- | 21 px / 61% | 25% | -- | -- | 35.31 / 0.9686 |
| 1 | competes with the magnitude prior | 0.03 px / 0% | 6% | +0.78 dB (L2 +8.5, L7 +3.5, L8 +3.5) | L3 -4.2, L6 -1.1 | 34.90 / 0.9659 (loss) |
| 2 | + seeds scored at their sub-pixel-fitted SAD | same | 2.5% | -- | L3 -4.3, M2 -1.8 | -- |
| 3 | + seeds scored at the V fit's vertex cost | same | 5% | -- | L1 -9.5, M2 -6.1 | -- |
| 4 | wins on SAD alone (10% margin), boundary discount | same | 22% | +0.14 dB (R3 +2.2, O6 +1.3) | L3 -1.4, F1 -1.0 | 35.36 / 0.9687 |
| 5 | pass 1 where the coarse level is Moire, pass 4 elsewhere | same | 14% | +0.15 dB (R3 +2.3, O6 +1.3, A5 +1.0) | L3 -1.4, F1 -1.0 | 35.32 / 0.9685 |
| **6, shipped** | pass 5 + the aperture gate | same | 14% | **+0.23 dB** (R3 +2.4, O6 +1.3, A5 +1.0, A7 +0.8, L1 +0.6) | F1 -0.9, L3 -0.5 | 35.32 / 0.9685 |

Two facts fall out. The fractional-1/8 diagonals ((4,4) 98%, (5.9,5.9) 85%)
stay locked under every pass, because the zero seed's own +/-2 texel window
contains the periodic copy at (-16,-16) px -- an exact integer match at cost
0 -- while the truth sits half a texel off every integer candidate at ~1.2
amplitudes of cost; a 3x3-texel window (24 px) is smaller than the 28 px
period and cannot tell copies apart, and no scoring after the integer search
can undo its choice. That is period locking (section 3, mechanism b) with
its condition stated: a matching window smaller than the texture period, at
a fractional shift of that level. And the edge cases (L3, F1, L2, the
footage) lose whenever the zero seed is allowed to win with the prior, and
still lose a little on cost alone: on one-dimensional structure a zero seed
that slides along the edge is a legitimately lower cost -- the aperture
problem, whose gate (a structure tensor on the block) is the register's
oldest open lead -- and pass 6 built it: a 3x3 structure tensor of the
reference block at 1/8; where the smaller eigenvalue is below a tenth of
the larger (an edge) and the zero seed's offset lies mostly along the edge,
the seed slid and is discounted. It did what it was built for: L3's loss
-1.4 -> -0.5, L2's -0.75 -> -0.1, everything else held, footage unchanged
(35.32 / 0.9685 against 35.31 / 0.9686). Time +3.9% on the quad (5.34 ->
5.55 s, interleaved on a quiet GPU). Shipped 2026-09-04 as `ZERO_SEED`:
OFF in the seeded family's three two-frame bases (seeded, propagated,
animation -- their time and numbers unchanged; the picture tier does not
pay the 4%) and ON in every tri, quad and quint generated from them, where
the field is the product; the stock and variational lines have a
single-seed 1/8 pass and are untouched. The fractional-1/8 diagonal of a
perfectly periodic texture stays a limit of the record. Textured diagonal
cases belong on the ladder and are queued.

**Where the time goes (2026-09-04, evening), and a correction to every timing
above.** Asked to move the engine to the GPU's compute path, the first proof
converted the 1/8 refine to a `//!COMPUTE` pass with shared-memory tiles
(correct within 0.05 dB; slower: +13% on the two-frame base, +9% on the
quad), the second cut its texture taps 4.5x by fetching the 7x7 grid once
(bit-identical; no change in time). Both were optimising a rounding error:
stubbing every flow-pass family of the two-frame base to a passthrough moves
its frame time by about two milliseconds of fifty-five. The split, O5 at
24 -> 60, sixty output frames, RX 6600:

| pipeline | seconds |
|---|---|
| the lavfi source alone, no libplacebo | 2.27 |
| lavfi + the stock mixer, no hook | 2.99 |
| lavfi + the shipped two-frame propagated | 3.23 |
| file source + the stock mixer | 0.74 |
| file + the then-shipped two-frame (32 passes, pre-fusion) | 1.42 |
| file + the two-frame with all 14 flow passes trivial | 1.23 |
| file + the then-shipped propagated quad (92 passes, pre-fusion) | 3.48 |
| file + the quad with all 48 flow passes trivial | 2.21 |

The synthetic source is a per-pixel expression evaluated on the CPU: 38 ms
per frame, seventy percent of every "render time" quoted in this document
before this paragraph. From a file the two-frame shader costs 11 ms per
frame, of which about 8 ms is thirty-two pass dispatches at roughly 0.27 ms
each and about 3 ms is arithmetic; the quad costs 46 ms, of which 24.5 ms
is its 92 dispatches and 21 ms its flow arithmetic (six pairs, six times the
two-frame's, as expected). The engine's time is pass count first and
arithmetic second, and neither shared memory nor tap reuse touches either.

Restated on the shader's own time (the lavfi constant removed): the
self-referenced fit's "+2.4%" is about +4%; the zero seed's "+3.9%" about
+8%; the quint's "+18% over the quad" about +30%. The differences were
measured correctly; the base they were divided by was mostly the source.
From now on time from a pre-rendered file (`ffv1`), interleaved; `bench.sh`
keeps `lavfi` for correctness, where it is exact.

The move that pays is pass fusion, and it needs no compute: every A->B pass
has a B->A twin doing identical work on swapped inputs, and a fragment pass
can already write a second result into a storage image. Shipped the same
evening. The twin's hook becomes `hook_ba()`, its returns store into a
storage image at the same texel, its consumers read that image, and one
dispatch does the work of two with the arithmetic untouched -- identical by
construction, and the ladder agrees to the hundredth of a dB on the
translation, acceleration and rotation cases.

What fused: the coarse search (the B->A result into the cache image it
already writes, the B->A refine reading its seed from that image at the
texel it already snapped to), the three propagation iterations, the
three-way check, the first vector median. Each propagation iteration needs
its own storage image: a storage image cannot be double-buffered the way
libplacebo re-saves a texture, and a Jacobi step must read the previous
iteration while its neighbours are being written. What did not: the 1/8
refines read the other direction's coarse cache, so their order is part of
the algorithm; the 1/2 refines are the blocks the generators clone into the
full-resolution passes, found by saved texture name; the second medians feed
bilinear samplers, which an image read cannot replace. The generators learned
the fused form -- a pair's passes are emitted in the base's own order with
both directions interleaved, since a fused block computes both at once --
and a base is recognised as fused by its descriptions, so an unfused base
still regenerates byte for byte.

| shader | passes | before | after | |
|---|---|---|---|---|
| two-frame propagated | 32 -> 26 | 1.387 s | 1.309 s | -5.6% |
| tridirectional propagated | 64 -> 52 | 2.627 s | 2.484 s | -5.4% |
| quaddirectional propagated | 92 -> 74 | 3.482 s | 3.340 s | -4.1% |
| quintdirectional propagated | 127 -> 103 | 4.595 s | 4.203 s | -8.5% |

The estimate in the paragraph above -- forty-two dispatches off the quad,
about a quarter of its shader time -- assumed every pair could fuse,
including the refines and the half-res passes whose consumers sample
bilinearly. Eighteen came off, and the saving is 0.13-0.27 ms per removed
dispatch: fusing a pass saves the dispatch, not the work. The remaining
engine cost is the dispatch count that the algorithm genuinely needs, and
the 21 ms of arithmetic on the quad is the searches themselves, which is a
question of algorithm, not of engine.

### The Moire gate was measuring frame difference, and that was worth something

The zero seed's wide path -- where the coarse level looks aliased, the seed
competes on score instead of having to beat the best coarse seed by ten
percent -- is gated on `moire_s`: the point-sampled 1/16 luma's local
contrast against the same footprint box-averaged from the 1/8 luma. Point
contrast far above box contrast means texture above the coarse grid's
Nyquist, which is where the coarse match is a Moire.

The comparison only means anything within one frame. In every cloned pair it
was between two: the generators renamed a pass's own level, so the 1/8 term
became slot 1's or slot 2's luma while the 1/16 term stayed slot 0's. Pairs
beyond the first were therefore scoring how much two frames differ, not
whether the coarse level aliased -- and the shipped tri, quad and quint all
have such pairs. Fixed 2026-09-04 (`shift_lumas` renames every level a pass
reads and binds what it renames).

The fix costs picture PSNR, which is the interesting part. Eight cases on the
propagated line: A5 -0.14/-0.27/-0.52 dB (tri/quad/quint), A7 -0.18/-0.31/
-0.16, L8 -0.07/-0.13/-0.13, O9_osc_tex_fast -0.41/-0.82/-0.83, and no change
on translation, flat texture, gentle oscillation or rotation. The loss grows
with the number of pairs and concentrates on fast textured motion -- which is
exactly where two frames of a window differ most, so the broken term was
large there and let the zero seed in. The accident was a motion-sensitive
gate, and it was doing useful work.

That is a lead about the gate rather than about the bug: the zero seed is
being kept out of places where it would help. The threshold is the obvious
first probe, and lowering `MOIRE_MIN` from 0.25 to 0.02 on the quad moves the
whole 32-case ladder by +0.06 dB in the mean, with the gains where this
project's known weaknesses are:

| better | | worse | |
|---|---|---|---|
| R3_rot_tex | +0.64 | A2_accel_16mean | -0.15 |
| A7_accel_tex_a167 | +0.48 | L3_trans_23px | -0.11 |
| L8_diagonal | +0.45 | F2_fourier_accel | -0.10 |
| O1_osc_gentle | +0.40 | L9, O5, M2, L2, O2 | -0.06 or less |
| R1 +0.14, R2 +0.06, O3 +0.13 | | eight cases | unchanged |

Every rotation case improves, which is the interesting part: the coarse
level's Moire is what the rotation work of section 9 kept running into, and
the gate was refusing the seed that answers it. What the looser threshold
does NOT recover is O9_osc_tex_fast (+0.02 of the 0.82 the fix cost there),
so the motion sensitivity is not a looser threshold in disguise: there is
something in "these two frames differ here" that Moire evidence alone does
not carry. Two candidates, untested: a deliberate inter-frame term beside the
Moire one, and a per-pair rather than global threshold.

Real footage says do not ship it. Five segments of the reference clip through
the quad: PSNR mean 35.34 -> 35.27 dB and SSIM 0.9686 -> 0.9683, down on
every segment, consistently and slightly. The zero seed at MOIRE_MIN 0.25 was
measured as leaving footage unchanged; at 0.02 it costs a little. So the
threshold stays at 0.25 in the shipped shaders and 0.02 is recorded here as
what it buys and what it costs: a synthetic ladder that likes it, real
footage that does not, and a hypothesis it does not explain.

The deliberate term, tested the same night. `frame_diff_s`: the largest
absolute difference of the two 1/16 lumas over the 3x3 coarse footprint, and
the gate becomes `moire > MOIRE_MIN || fdiff > DIFF_MIN`. Both coarse lumas
are bound in each 1/8 refine, so the generators carry the term to every slot
pair correctly -- which the Moire fix is what made possible. On the quad,
DIFF_MIN 0.10 against the shipped gate, all 32 cases:

| better | | worse | |
|---|---|---|---|
| O1_osc_gentle | +1.17 | F2_fourier_accel | -0.36 |
| R3_rot_tex | +1.07 | L3_trans_23px | -0.36 |
| O4_osc_flat300 | +0.83 | A2_accel_16mean | -0.17 |
| F1_fourier_edge | +0.71 | L9_occlusion | -0.11 |
| A7_accel_tex_a167 | +0.50 | L2_trans_16px | -0.09 |
| L1_trans_8px | +0.47 | L6, R1, A4 | -0.05 or less |
| O2 +0.39, A1 +0.32, O6 +0.31, O3 +0.28, A6 +0.21 | | six cases | unchanged |

Mean +0.18 dB, three times the threshold probe; every oscillation case up;
pure translation up, which the threshold never touched. Real footage, five
segments: PSNR 35.34 -> 35.24, SSIM 0.9686 -> 0.9682, down on every segment.
File-source time unchanged (3.502 -> 3.506 s). It still does not recover
O9_osc_tex_fast (+0.02), so whatever the broken comparison was scoring there
is not the frame difference either; that one stays open.

So the same trade as the threshold, larger on both sides, and the same
answer for the shipped numbers: the term is in the three zero-seed bases
behind `FRAME_DIFF_GATE`, off, beside `ZERO_SEED`, with the trade written
into the shader at the switch. It costs nothing off, 18 taps per 1/8-refine
texel on, and is a field-shader question throughout since ZERO_SEED is off in
the picture bases. A field-only reading -- on in the generated tri/quad/quint,
off in the two-frame picture shaders -- is one line in each generator, where
ZERO_SEED and SUBPEL_SELFREF already flip; that is the owner's call, against
a tenth of a decibel of footage.

### The resolution half of the scale-aware generator, and what the 4K test really measured

`tests/scale_shader.py` doubles every pyramid divisor of a two-frame picture
shader, rewrites the three hand-offs between levels and the warp's
conversion, and refuses anything with a pixel constant it does not know. The
variational build so scaled, at twice the ladder's size, reproduces the
shipped build at native size case for case (SHADERS.md, "the 4K shader"),
which is the design working; on 2x footage it is 1.5 dB and 0.0036 SSIM
above the shipped build run at that size, and 11% faster.

Two things worth keeping. First, a test that upscales content with lanczos
is a test of band-limited content: the shipped build at 2x scored 12 dB
higher on A5 and 6 dB on R3 than at native, because with no energy above
half Nyquist the fine levels' sub-texel fits are unusually clean. That is
not 4K's fineness paying off, it is the resampler's; footage, which carries
detail to its own Nyquist, showed the opposite ordering. Any 4K claim needs
native 4K content or a source rendered at that size, not an upscale.
Second, keeping the finest level at its native fineness while doubling the
coarse three (2,2,2,1) bought nothing on the textured cases and cost a
little reach, so the fineness that helped the shipped build at 2x lives in
the coarse and middle levels, where it was the resampler's gift, not in the
warp's resolution. The general design for a larger frame is therefore the
whole pyramid shifted, not a deeper one -- until native 4K content says
otherwise.

The field shaders followed the same night. The tool now takes the generated
tri/quad/quint: their hand-offs between slots beyond A and B, the fused
propagated lineage's coarse-cache image loads (the seeds it converts on the
next line), the full-resolution flow level below the half-resolution one
(the ratio becomes four), the two half-resolution-to-frame conversions (the
warp and the reading tail's copy of the final pass), the seven constants in
the frame's pixels (the acceleration and jerk caps, the diagnostic and
machine-read full scales, the residual's) and the corner marker -- and it
still refuses any pixel use it does not know. The quad so scaled loads and
runs at 3840x2160 with no skipped window.

The judged test, then: the textured disc at 3840x2160, 72 fps, three times
the 720p scene, frame 100, painted velocity and acceleration through the
shipped quad and through the scaled one, beside the 720p scene through the
shipped quad at 24 and at 72 fps (the frame-rate effect on its own). The
velocity map: the shipped quad at 4K is wrong across the whole disc, in
large patches; the scaled quad gives the hue wheel back, with a few wrong
patches left near the rim. The acceleration map: the scaled quad at 4K and
72 fps is still wrong, in coherent blobs, and the 720p reference at 72 fps
mostly declines to paint. So the resolution half repairs the velocity field,
as the register predicted, and the acceleration at 72 fps is the frame-rate
limit -- one ninth of the acceleration per frame, the same noise per reading
-- which no resolution scaling touches. That half is a stride through the
frames, so the motion of interest is sampled six to ten times per cycle,
and it is the next thing to build. The montages are in the owner's renders
folder; the scaled quad is not shipped as a file (one command makes it:
`./scale_shader.py ../shaders/quaddirectional-interpolation-propagated.glsl
<out> 2`), because a field shader at 4K owes a ladder at 4K first.

*Dated note, 2026-09-05 (Lead B, below): the exact read disagrees with the
eye here. Through `tests/discaccel.py`, the scaled quad's velocity on the 4K
disc at 72 fps is exact inside 0.3 R and REVERSED over 0.3-0.7 R (along
the truth -0.97 and -0.56), which the pooled, remembered painting smoothed
into a wheel whose sides turn the wrong way. The disc's 40-px texture is
1.25 texels at the scaled pyramid's coarsest level, below its Nyquist, so
that level matches one period away; the resolution half repaired the
constants and the scene defeated the pyramid. "The hue wheel back" stands
only for the inner third.*

### Weird geometry, and the six-frame line

`tests/manifolds.py` renders four deterministic scenes with the exact 2D
velocity of every visible pixel: a textured torus spinning about an axis
tilted 55 degrees from the line of sight, a Mobius band tumbling, a
tesseract rotating in two 4D planes drawn as tubes, and the Hopf
fibration of the 3-sphere rotating along its own fibres. `tests/fieldcheck.py`
scores a machine-read velocity frame against them, per texel and pooled
over 24 px, and against the two neighbouring truth frames -- which is how
the window rule showed itself: at the exact N:N phase the output sits at
the end of its straddle interval, so output frame n reports the chord
from n-1 to n, and a checker that assumed the chord out of n would call a
correct field one frame wrong.

The quad's velocity on them, frame 48: the torus reads 2.0 px median on a
5.8 px field and 45% pooled, the band 1.1 px on 3.3 and 30% pooled with
the magnitude 19% LOW even pooled -- a bias, not noise, on a foreshortened
surface; the tubes 40 degrees off in direction, which is the aperture
problem by construction. Two cautions on the torus: an early texture with
50-100 px periods made the whole surface aperture-limited, and a later one
with 5 px components aliased against the render's own sample lattice; the
texture that stands is the ladder's M1 recipe band-limited to 12-42 px in
surface arc length, which foreshortening still compresses toward the coarse
levels' Nyquist near the rim. The 19% low reading on the band was the
read path, withdrawn below.

The six-frame shader (`SEXTDIRECTIONAL.md`) is the night's other result:
built from the quint's generator, a weighted least-squares quartic with a
residual. Fitted at the anchor its lopsided stencil (three links behind,
two ahead) carries an odd-order truncation bias of 0.2 px/interval^2 at
every zero crossing of O9's acceleration, three times the quint's RMS;
fitted about the centre of its point set the bias cancels (0.066 against
the quint's 0.051) and the noise is half the quint's. The general lesson
is the one the quint's symmetric window already embodied: for a
polynomial field estimator, the stencil's symmetry about the instant it
reports at is worth more than its length, and an even frame count buys
symmetry only by reporting half an interval off the anchor.

### The time asymmetry was the instrument: a retraction, and what the exact read shows

The finding above of 2026-09-05's small hours -- that the tumbling band
played backwards is measured three times better -- is withdrawn. It was the
read path. A machine field written with `-pix_fmt rgb48le` on ffmpeg's
OUTPUT passes through an 8-bit limited-range YUV frame after libplacebo:
every value is scaled by 219/255 and shifted by about half a pixel, the two
channels differently through the chroma path, with quarter-pixel steps.
Decoded as the full-range field it never was, that produced a uniform 25%
"underestimation", fixed offsets that followed the pipeline's axes, and a
run in which the two happened to cancel. A rigid translation reading 0.80
of itself a hundred pixels from any edge was the tell; the acceleration
comparison in the previous section used raw video and was exact, which is
why it reproduced the quint's published number. With `format=rgb48le`
inside the filter graph the field is exact, `tests/fieldcheck.py` now
refuses a frame whose off-object zero level is not 0.5, and the memory of
this project carries the rule: calibrate a read on a translation the ladder
already knows before scoring anything new.

Through the exact path, the same scenes, the quad's velocity at frame 48:

| scene | median error | gross (> 2 px) | direction | magnitude along the truth |
|---|---|---|---|---|
| Mobius band, forward | 0.19 px on 3.4 | 5.9% | 1.9 deg | 0.97 |
| Mobius band, reversed | 0.18 | 4.5% | 1.8 deg | 0.98 |
| Mobius band, mirrored | 0.19 | 5.9% | 1.9 deg | 0.98 |
| aperture (rigid translation behind a static rim) | 0.55 on 4.3 | 20.8% | 6.0 deg | see below |
| zoom (pure expansion; contraction the same) | 0.52 on 1.3 | 0.4% | 14 deg | see below |
| torus, tilted, spinning (either direction) | 1.7-2.0 on 5.8 | 47-50% | 7-9 deg | see below |
| tesseract, Hopf (tubes) | 1.9-3.0 | 49-73% | 30-34 deg | aperture-limited by design |

The band is tracked to a fifth of a pixel, forward, backward and mirrored
alike, on a surface that twists, tumbles and occludes itself. Three things
survive the correction, each with its profile against distance from the
object's outline (ratio of the measurement along the truth; the rows are
3-8, 8-16, 16-24, 24-32, 32-48, 48-64, 64-96 and 96-131 px):

- **Silhouette capture is real, and local.** The aperture: 0.80, 0.94,
  0.96, 0.92, 0.89, 0.93, 1.00, 1.03. A rigid translation of texture behind
  a rim that does not move reads a fifth low within eight pixels of the rim,
  five to ten percent low out to about sixty, and exactly beyond. The
  coarse levels' windows (80 and 40 px) contain the outline, the outline's
  contrast dominates a sum of absolute differences, and the outline's motion
  is zero; the refines recover most of it but not within the window's
  reach of the edge. The torus shows the same rim: 0.67, 0.87, 0.94, 0.97,
  0.98, 0.95, 0.94.
- **Small flows read low.** The zoom's field grows with radius, so distance
  from its rim is distance toward slow flow: 1.00 at the rim where the flow
  is 1.9 px, then 0.84, 0.85, 0.90, 0.84, 0.81, 0.77, 0.76 toward the centre
  where it is half a pixel. Flows above about 1.5 px read exactly; flows of
  half a pixel read about three quarters. Expansion and contraction are the
  same. This is the small-signal floor of the sub-texel fit and the seeds'
  priors, and it is what the reading's own floors were set to hide.
- **The torus interior is a real hard case.** Along the truth it reads
  0.94-0.98 beyond sixteen pixels from the rim, but the error there is 1.3
  to 2.9 px on a 5.8 px field: cross-flow, a direction error on a surface
  whose flow curves and shears strongly under foreshortening, with the far
  half hidden. Nothing above explains it yet.

The night's other retraction is smaller: the band reading "19% low even
pooled" in the weird-geometry section above was the same read path, and
the disc's 15% pooled error, which that was offered as an explanation for,
stands on its own measurement through the tools that were always exact.

### The phase-locked consensus: a loop reads a field the mean of its frames cannot

The owner's isometric torus (`tests/loop_torus.py`: symmetry axis 54.7
degrees from the line of sight, one turn per 80 frames, the outer rim at
19.6 px/frame) was rendered to be looped, and looking at the painted
reading over the loop he saw it flicker and cover different parts of the
torus at different times, and asked whether the average over a full turn
would shade it exactly. It is the right object for that question: a torus
spinning about its own symmetry axis presents the same surface, silhouette
and shading at every frame with only the texture sliding, so the velocity
field under every pixel is stationary and the truth computed at frame 80
differs from frame 120 by zero pixels. Every frame of the turn is a fresh
reading of one field.

**The mean does not converge, at any speed.** The machine field (mode 4,
the exact read) of the middle turn, scored at its own 8-px cells:

| torus | single frame | mean of the turn | mode of the turn | oracle | tracker right |
|---|---|---|---|---|---|
| as rendered (shaded, 19.6 px/frame) | 9.3 px, 0.77 of magnitude | 7.8 px, 0.34 | **1.29 px, 0.95** | 0.43 px | 1 frame in 5 |
| the same without shading | 8.7, 0.77 | 7.8, 0.34 | 1.28, 0.95 | 0.45 | 1 in 5 |
| broadband texture (84 and 170 px periods added) | 3.2, 0.87 | 4.0, 0.68 | 1.05, 0.99 | 0.33 | 2 in 5 |
| half speed (one turn per 160 frames, 9.8 px/frame) | 1.2, 1.05 | 2.2, 0.67 | **0.47, 1.00** | 0.085 | 1 in 2 |

Median absolute error per cell and the median ratio of the estimate's
magnitude to the truth's; "oracle" is the reading closest to the truth
among the turn's frames, the floor no estimator can beat; "tracker right"
is the median over cells of the fraction of frames whose reading is within
2 px of the truth. Averaging the turn makes the error worse than a single
frame in three of the four rows and shrinks the magnitude to a third or two
thirds in all of them, and the running mean never turns around: on the
torus as rendered it goes 6.9, 7.3, 7.4, 7.6, 7.5, 8.0, 8.2 px at 1, 2, 4,
8, 16, 40 and 80 frames while the magnitude falls from 0.73 to 0.37.

**Because the tracker is not noisy about the truth; it is right some of
the time and reads an alias the rest.** The hit map (`hit.png`) is the
picture of it: the tracker is right in nearly every frame across the front
band, where the ring's texture slides horizontally and unforeshortened, and
in a stripe at the top, and right one frame in ten at the sides, where the
tilt compresses the same texture along the direction of motion by
cos 54.7 = 0.58. The texture's longest period is 42 px in arc length; at the
sides that is 24 px on screen against an 11 px shift, and at the coarse
levels of the pyramid, which are all that can see a shift that size, a
texture with one period left in it matches itself equally well one period
away. The aliases are not symmetric about the truth, so no mean of them
converges. Three controls say which ingredient it is: removing the shading
changes nothing (row two), so the static pattern the spin leaves under the
sliding texture is not the cause; long periods the coarse levels can hold
halve the single-frame error and double the hit fraction (row three); and
halving the shift makes the tracker right in half its frames (row four).
This is also the explanation the weird-geometry section above did not have
for "the torus interior is a real hard case": the manifold torus moves its
rim at 9.4 px/frame on the same texture, and its 1.7 px median with 47%
gross is the same alias problem at the half-speed row's strength.

**The mode of the turn is the estimator, and it shades the torus.** Per
cell, a 1-px histogram of the turn's readings, its peak refined by mean
shift, recovers the field wherever the truth is the most common reading:
1.3 px on the torus as rendered (two thirds of its cells; the rest are the
sides, where the hit fraction is below a tenth and the most common reading
is an alias), 1.05 px with broadband texture, and 0.47 px with a 1.0-px
90th percentile and the exact magnitude at half speed. Pooling the
histogram over the cell's eight neighbours changes little. The median and
the trimmed mean sit between the mean and the mode, as they must for a
mixture. `tests/loopfield.py` computes all of it and paints it with the
shader's own palette (`tests/fieldpaint.py`), and `tests/loop.sh` runs the
render, the exact read and the scoring.

Two consequences. The painted reading's memory (`READ_EMA_ALPHA`, an
exponential mean across frames) is a mean, and on content like this it
shrinks toward zero exactly as the turn average does; a histogram memory in
a storage image, reporting the peak, would report the consensus instead,
and that is on the lead list. And the per-frame error metric this document
has used throughout, a median over cells, cannot see a bimodal reading: the
hit fraction, or the oracle-to-single gap (0.43 against 9.3 px here), is
the measure of a tracker on texture it cannot hold.

### Lead A: the two rim biases have mechanisms and fixes, and each fix is a trade

The geometry ladder's two biases (section 9, the retraction): SILHOUETTE
CAPTURE, a rigid translation seen through a static rim reading a fifth low
within eight pixels of the rim and five to ten percent low out to sixty
(`tests/rimprofile.py`), and the SMALL-FLOW FLOOR, flows under two pixels
reading about three quarters (`tests/smallflow.py`, the zoom scene). Both
were taken apart on 2026-09-05 with scratch variants of the four-frame
shader, scored on the aperture and the zoom, on the other weird geometries,
on a fourteen-case subset of the picture ladder, on cel and live-action
footage by decimate-and-reconstruct, and for time.

**Silhouette capture: a hard cap on the cost kills the search's basin; a
weight by each texel's own temporal change does not.** The coarse levels
(1/16 and 1/8) match a 3x3 window of block-averaged luma by a plain sum of
absolute differences, and a static rim inside the window dominates the sum
at every candidate but zero. Two robust costs were tried at those levels
only (at the finer levels either one collapses the torus):

- A truncated sum, min(|a - b|, tau). At tau 0.15 nothing changes: a
  rim's coarse-level differences are 0.05 to 0.15. At 0.03 the aperture
  is exact (gross 20.8% to 3.0%, magnitude 4.33 against a true 4.27, the
  8 to 64 px rim bands 0.90-0.95 to 0.99-1.03) and the manifold torus
  halves its error (median 1.73 to 1.03 px, pooled 2.01 to 0.77). And the
  ladder refutes it: the 23-px translation 43.4 to 33.3 dB, the flat
  large block 65.1 to 56.5, the noise texture 49.6 to 35.2, live action
  -0.3 dB. A texture's own coarse-level differences are on the same scale
  as a rim's, so a cap that removes the rim's dominance also flattens the
  basin a 23-px search descends. The two cannot be separated by size.
- A weight by temporal change, w = clamp(|a(x) - b(x)| / 0.10, 0.25, 1)
  on each window texel: a texel that shows the same luma in both frames
  at its own position -- a static rim, a static background -- counts a
  quarter. That separates them by a different property and keeps the
  basin. Aperture gross 20.8% to 9.1%, the rim bands exact beyond 8 px,
  magnitude 4.98 to 4.40; the torus -0.1 px; Mobius, zoom and Hopf
  unchanged; +1.1% render time at 1080p. The ladder subset is a trade:
  diagonal +1.3 dB, the textured trap -1.0, low contrast -0.5, the 23-px
  case -0.35, the rest within 0.2; cel footage 35.24 to 35.21 dB and live
  action 46.70 to 46.62. The floor is load-bearing: at 0.50 the aperture
  is only half fixed, at a tau of 0.20 low contrast loses 3.6 dB, and
  NORMALISING the weighted sum by the window's mean weight (so the
  regulariser sees the same scale) overshoots everywhere (aperture 6.3
  against 4.27, zoom 1.8 against 1.28): the raw weights' pull toward zero
  where evidence is weak is doing work of its own.

**The small-flow floor is a fifth the finest level's regulariser, and not
the fit.** On the zoom the reading is exact at 0.5-0.75 px and 0.74-0.83
of the truth below and above that; the parabola fit is worse (peak
locking, as the equiangular fit's comment predicted), the self-reference
is neutral, and a walk when the fit lands on its half-texel clamp changes
nothing. Setting the half-res level's REFINE_REG_LAMBDA (0.05, a penalty
per texel step away from the seed) to zero at that level only lifts flows
of 1-2 px from 0.74-0.77 to 0.83-0.86 of the truth, the zoom's pooled
error 0.41 to 0.31 px, and the Hopf reading 3.00 to 2.81 px, with the
aperture, torus, Mobius and tesseract unchanged and no gross error added.
The picture ladder refuses it outright: the flat large block 65.1 to 49.6
dB, the noise texture 49.6 to 44.6, the 8-px square 69.8 to 65.0, the
oscillation 49.1 to 45.0. The fine level's search wanders without it on
content whose finest level carries no signal, and the picture pays; the
field on a textured surface would rather it did not hold. The zoom's
remaining floor is anisotropic (vertical flows read 0.72-0.77 where
horizontal read 0.86-0.87) and it is not the frame border (a 96-px margin
does not move it); the texture's own gradient energy is the candidate.

**What ships.** Nothing as a default. The weight is the right fix for
silhouette capture and costs a decibel on one ladder case; the regulariser
is the right knob for small flows and costs fifteen on another. Both are
field-tier trades, described above precisely enough to rebuild, and the
right home for either is a switch in the reading's generator when a use
asks for it. The instruments that measure them are in `tests/`.

### Lead G: the reading's memory as a mode, and where that helps

The painted reading remembers its field with an exponential mean across
frames, and the phase-locked consensus above says what a mean does on a
field the tracker aliases: it shrinks toward zero. The shader form of the
consensus is an online mode: per 1/8-res cell, three candidate readings
(mean, weight) in a storage image; each frame's raw reading joins the
nearest candidate within 1.5 px or replaces the weakest; weights decay by
0.97 a frame; the heaviest is the cell's reading. It is now a switch in
the reading tail every shipped shader carries (`tests/add_human_reading.py`,
READ_MEMORY: 0 the mean, the default; 1 the mode), with read_view 7 and 8
exporting the pooled reading and the per-cell mode raw so `tests/loop.sh`
can score a memory frame by frame; the tracker always runs, at +0.1%.

**Order matters: the consensus must come before the pool.** The first
build put the mode after the shipped 13x13 pool and read 9.7 px on the
torus loop, worse than the mean's 8.4: a spatial mean over 169 cells whose
readings are aliases in different directions is as small as a temporal
mean of them, and no memory downstream of it can recover the field. Per
cell, on the raw field, the mode reads 1.6 px at every frame of the turn
(the offline mode of the same readings was 1.29), with 58% of cells right
more than half the time against 16% for the raw field. Pooling the modes
13x13 with each weighted by its support still shrinks to 5.5 px; 3x3 reads
1.70. On a torus loop with a static textured backdrop and sensor noise
(`loop_torus.py bg=tex noise=3`, `loopfield.py`'s backdrop score) the
per-cell mode also does the pool's other job: the backdrop's speckle p95
is 0.029 px against the raw field's 0.145 and the shipped pooled
reading's 0.246, which is the 13x13 pool smearing the torus's motion 48 px
into the backdrop.

**The horizon is one knob with two answers.** The steady field needs a
long one: decay 0.97 (about 33 frames) reads 1.7 px, 0.90 reads 3.1, 0.80
reads 5.1. On five seconds of live action a long horizon holds the zeros
each cell learned while still, so a walking figure is missed and a pan
paints grainier than the pooled mean, and a short one gives the consensus
away. That is why the mean stays the default: it is the right memory for
transient motion, and the mode is the right one for a steady field, which
is what the reading is pointed at when it is used as an instrument.

**An adaptive horizon is the middle way, and it is a dial, not a fix.** A
cell that counts consecutive frames whose reading joined no candidate,
and past a threshold fades every candidate by an extra factor a frame,
re-anchors on new motion while a cell whose readings keep agreeing keeps
the long horizon (MODE_MISS, MODE_FAST in the mode pass; off by default).
On the noisy loop: 3 misses and x0.7 reads 2.2 px, 2 and x0.5 reads
2.4-3.8, 1 and x0.3 reads 4-5, against 1.7 for the fixed horizon and 8.6
for the mean; on the live clip only 2 and x0.5 and below paint the
walking figure again, grainier than the pooled mean because every cell
shows its own mode. The loop's alias cells miss as often as the true
cells hit, so whatever shortens the memory on a transient shortens it
on the consensus too; the three settings are three uses, and the eye
decides the painted one.

### Lead B: the frame-rate half is a decimation stage, and the 4K disc could not have shown it

The record above says the acceleration at 72 fps is the frame-rate limit
(a ninth of the acceleration per interval against the same noise per
reading) and that the answer is a stride through the frames. Measured on
2026-09-05 with `tests/discaccel.py` on the 720p disc of `scenes.sh`
(R 150, pi rad/s, the shipped four-frame shader, the exact read, frame
100), the reading along the centripetal truth and the angle to it by
radius band, 0.1-0.3 / 0.3-0.5 / 0.5-0.7 / 0.7-0.85 / 0.85-0.97 R:

| disc | velocity along truth | acceleration along truth | acceleration angle |
|---|---|---|---|
| 24 fps (rim 19.6 px/frame, a 2.6 px/frame^2) | 0.97 1.00 0.99 0.89 0.47 | 1.11 0.93 0.89 0.25 0.00 | 16 14 12 26 71 deg |
| 72 fps native (rim 6.5, a 0.29) | 0.88 0.99 0.99 0.99 0.98 | 1.74 0.92 0.90 0.63 0.50 | 61 59 54 52 65 deg |
| 72 fps, `fps=24` in front of the hook | | 1.22 0.94 0.90 0.22 0.03 | 16 12 12 32 73 deg |

At 72 fps the velocity is exact to the rim (the shift is small enough for
the 40-px texture everywhere) and the acceleration is noise: the ratio
looks fair in the middle bands and the angle says it is not a field. With
every third frame handed to the shader by one filter the acceleration map
is back, band for band the 24-fps reading, in units of the decimated
interval. For a measurement pipeline that is the frame-rate half, and it
needs no shader: choose the stride so the motion of interest moves 5-20 px
per interval it sees, and scale by the stride. The two rims say what the
stride costs: at 24 fps the rim's 19.6-px shift is half the texture's
period and the velocity reads 0.47 there, so a stride is bounded above by
the reach and the texture as well as below by the noise.

The 4K disc that motivated the lead cannot show it. Decimated to 24 its
rim moves 59 px, past any reach, so its velocity reads zero everywhere
and its acceleration with it; and at 72 native its velocity is reversed
over the middle radii (the dated note above), so its acceleration was
never going to be a field there. A fair 4K scene carries texture with
periods the scaled coarse level can hold (above 64 px) and a stride that
keeps the rim inside the reach; `loop_torus.py`'s broad texture at a high
turn count is the shape of it.

What remains is the real-time form: a stride inside the mixer's window,
so the picture path interpolates at the source rate while the field passes
read frames 0, 3 and 6 of an eight-frame window (`PL_FRAME_MIX_MAX` is 8:
a three-frame shader at stride 3, a four-frame at stride 2). That is a
generator change to the slot-to-frame mapping and the final pass's roles,
gated by the table above reproduced from a 72-fps source with the shader
striding instead of the filter.

### Lead C: a number beside the project that nobody here chose

The Middlebury optical-flow benchmark (Baker, Scharstein, Lewis, Roth,
Black and Szeliski, IJCV 2011) publishes dense ground-truth flow for the
frame10 to frame11 pair of eight short colour sequences, 584x388 to
640x480 px, with hidden-texture, synthetic and real content. Fed to the
shipped shaders as eight-frame videos at N:N and read through the exact
path (`tests/middlebury.py`), the field's average endpoint error in px, the
benchmark's own measure, at the better of the two output frames that
bracket the pair, and the zero field's floor:

| sequence | four-frame reading | two-frame reading | zero field |
|---|---|---|---|
| RubberWhale (real, small motions) | **0.67** (84% within 1 px) | 1.09 | 1.26 |
| Hydrangea (real) | **0.85** (75%) | 1.39 | 3.73 |
| Grove2 (synthetic foliage) | 1.33 | 1.69 | 3.09 |
| Grove3 | 1.73 | 2.08 | 3.91 |
| Dimetrodon (two frames only) | - | 1.73 | 2.06 |
| Venus (two frames only) | - | 2.30 | 3.80 |
| Urban2 (synthetic city, motions to 30 px) | 4.03 | 4.17 | 8.39 |
| Urban3 | 4.16 | 4.43 | 7.31 |

What the number is: a field at 1/8 resolution, upsampled bilinearly by
the shader, scored per pixel against a per-pixel truth, so it carries the
resolution's own error at every edge; the benchmark's published methods
are per-pixel and an order finer, and the table is not a claim on them.
It is the honest external number for a real-time coarse field, and two
things in it are the project's own findings seen from outside. The Urban
pair's motions run past the tracker's 23-px reach, and the reading there
is a third of the way from the zero field to the truth. And the four-frame
reading beats the two-frame one on every sequence by 0.2-0.5 px even
though the truth is a single pair's flow: its estimate is centred at its
anchor, so the truth's chord is half a frame off it either way, and which
of the bracketing output frames wins (frame10 on Hydrangea, 0.85 against
1.54; frame11 on Grove2) depends on the sequence's own acceleration. The
two-frame reading at output frame 10 IS the pair's flow and is still
worse: the extra frames are worth more than the half-frame offset costs.

Particle image velocimetry, the other external measure the lead named:
the Cai, Liang, Zhou, Xu and Wei 2019 set (256x256 pairs with .flo truth,
research use) is on Google Drive and needs a browser download; the
Synthetic Particle Image Dataset (Zenodo 7935215, CC-BY-4.0, 665x630
pairs with exact flow, six flow families, noise and particle-size sweeps)
is one 16.7 GB file, a direct download when there is a reason to spend
the disk. Both score with `middlebury.py`'s reader once their flows are
in .flo form.

### Lead E, the half that needs no new match: the velocity gradient tensor

The lead asks for an affine block match at the fine level, which would
measure the local gradient of the flow directly and repair the direction
error on sheared surfaces. The tensor itself is available now from the
field the reading already has: central differences of the raw 1/8-res
field over neighbouring cells give divergence du/dx + dv/dy, curl
dv/dx - du/dy and the two shears, per frame, and read_view 9 emits them
raw (`tests/add_human_reading.py`; `tests/tensorcheck.py` scores them).
Two scenes are exact gates: the zoom, a flat disc expanding 0.6% a frame
(divergence 0.012, curl 0), and the rotating disc at 24 fps (curl
2 omega / fps = 0.262, divergence 0). Medians by radius band, 0.1-0.4 /
0.4-0.7 / 0.7-0.85 R:

| scene | divergence | curl |
|---|---|---|
| zoom (truth 0.012, 0) | 0.0098 0.0063 0.0034 | -0.002 -0.001 +0.001 |
| disc (truth 0, 0.262) | -0.022 -0.018 -0.018 | **0.260 0.249** 0.068 |

The curl of a rigid rotation reads within one to five percent over the
inner seventy percent of the disc and dies at the rim with the velocity
it is made of (the 40-px texture's alias band). The divergence of the
zoom reads 30-80 percent because it is the derivative of a field the
small-flow floor already under-reads, most where the flow is smallest,
and it comes with the per-cell noise differentiated (the 10th-90th
percentile spread is 0.05 a frame against a truth of 0.012). The pooled
field is the wrong source: its 13x13 window is a third of this disc's
radius and damps the curl to 0.21, 0.13 and 0.03. So the reading now
reports curl to the precision of its velocity and divergence to the
precision of its small-flow floor, and both improve with the floor; the
affine match is still the way to measure shear where the field itself
is a blur of two motions.

### The foresight seed: the window's other half, at the search (2026-09-06)

The question came from outside the project. The owner's wife, who is not
named here, described the five-frame window in her own words without
having read its design: render on the middle frame, two past and two
future, and let the front frame run out of sync (QUINTDIRECTIONAL.md,
"Convergent restatement"). Checking that against the code showed where
the window's symmetry stopped. The fit is symmetric and the picture's
straddle sits between two frames each side, but the SEARCH still looked
only backwards: in the seeded family every pair's coarse search starts
one of its descents from the previous window's flow for that pair, which
is the past-adjacent pair's motion at that texel, and its 1/8 arbitration
adds a prior toward it; nothing reads the next pair's flow, although that
flow is computed in the same window. Every pass of the generated quad's
slot 1 -> 2 chain binds its own caches and the lumas and never a
neighbour's flow.

**What was built.** The temporal seed mirrored in time, as a generator
transform (`tests/foresight.py`, applied by `gen_quaddirectional.py` and
`gen_quintdirectional.py`; `FORESIGHT=0` regenerates without it): a
generated pair that has a later neighbour in the window gets, at 1/16, a
fourth descent from the neighbour's arbitrated 1/8 flow at the same texel
(stored in the spare half of the temporal cache) and, at 1/8, a fifth
refined candidate, plus a prior of `SEED_FUT_LAMBDA` per texel toward
that flow under the same round-trip trust the temporal prior uses: the
neighbour's forward flow against its reverse at the landing point, within
one 1/8 texel. Forward flows take the neighbour's forward flow, backward
flows the neighbour's backward flow. For the neighbour's caches to hold
this window's values the generator emits the later pair first; that
reorder alone is bit-identical on every case (the pairs share no
texture), and it was the gate before any number was read. No new pass, no
new texture, two more binds on three passes per seeded pair. A base
without the temporal seed regenerates unchanged. The two-frame shaders
have no neighbour and are untouched; the tri's one generated pair is the
window's last and has no future either.

**Two instrument facts first.** (1) At the source rate the final pass's
rule, p = the last slot at or before the output, puts the output ON the
first frame of its straddle pair, so the velocity a machine reads at
output n is the FORWARD chord n -> n+1 of the window's LAST pair. Measured
on A5 at N:N: the median reading sits within 0.05 px of the forward chord
on every frame and 0.67 px from the backward one. Two places in the record
said the backward chord and are corrected (`tests/TOOLS.md`,
`tests/loop_torus.py`; that loop's field is stationary, so its numbers
stand). Consequence here: the quad's N:N velocity read comes from the one
pair that has no future in the window and cannot see the seed; the
quint's last-but-one pair can. (2) `accelcheck` at full scale 2.0 rails on
O9 (3.70 px per interval squared) and O5 (8.57), and a railed field reads
the same RMS for every shader; those rows were taken at 8 and 16.

**Pre-registered, then measured** (the predictions were written before
the first table was read; the scratch file is quoted in the commit).
The prior at 0.5, the mirror of the temporal prior:

| | predicted | measured |
|---|---|---|
| reorder alone | bit-identical | identical to the hundredth on every case |
| picture, 32-case ladder mean | within +/-0.10 dB | +0.02 dB |
| L1, L2, M2 (constant velocity, period lock) | unchanged within 0.05 | L1, M2 unchanged; **L2 -2.28** |
| A6, A7, O2-O5 | up 0.1-0.5 | A7 +0.98, A5 +1.23, O1 +0.36, O6 +0.21; A6, O2-O5 within 0.05 |
| L9 occlusion | at least +0.2 | +0.05 |
| aperture, mobius, zoom fields (quad) | unchanged within 0.02 px | identical (the read is the last pair's) |
| torus gross fraction (quad) | down 2-7 points | identical (same reason) |
| time, O5 from a file | quad +2 to +4%, quint +3 to +5% | quad +0.6%, quint +2.2% |
| footage, five segments | within +/-0.10 dB, sign positive | **+0.13 dB, +0.0005 SSIM, every segment up** |

**The ladder was a trade with a shape.** Every textured case whose motion
changes inside the window gained, and four fast flat-edge cases lost:

| case | shipped quad | prior 0.5 | candidate only |
|---|---|---|---|
| A5_accel_tex_a067 | 52.76 | 53.99 | 53.98 |
| A7_accel_tex_a167 | 50.15 | 51.13 | 51.04 |
| R3_rot_tex | 36.49 | 37.28 | 37.49 |
| O1_osc_gentle | 51.68 | 52.04 | |
| F2_fourier_accel | 43.37 | 43.73 | |
| R1_rot_const | 40.64 | 40.93 | |
| R2_rot_accel | 40.57 | 40.79 | |
| O6_osc_tex_gentle | 51.59 | 51.80 | |
| L8_diagonal | 49.32 | 49.42 | |
| A3_accel_23mean | 40.44 | 40.13 | 40.42 |
| L6_flat_large | 65.13 | 64.67 | 65.13 |
| L3_trans_23px | 43.44 | 42.70 | 43.52 |
| L2_trans_16px | 61.44 | 59.16 | 61.44 |

The other nineteen cases moved by 0.06 dB or less. The quint reproduces
the quad's picture as it must (A5 +1.25, R3 +1.00 on the smoke cases).

**The ablation separated the two halves.** The same seed with the prior
zeroed, the candidate alone competing on SAD and the existing priors
(third column): every gain stays, R3 gains more, and every loss goes back
to the shipped number to the hundredth. So the gains are the CANDIDATE's,
a fourth basin where the past and the future disagree: on accelerating
texture the descent from the next pair's flow lands in the basin the
descent from the previous pair's flow misses, and on the rotating disc
and the slow oscillations the second opinion breaks alias ties the first
could not. The losses were the PRIOR's, and the mechanism is the flat
interior at 16-23 px per frame: a flow there is defined only at edges and
a round trip closes anywhere, so the trust gate is vacuous and the prior
pulls an edge texel toward a neighbour's value that belongs to other
content. The temporal prior survives the same gate because the flow it
pulls toward is one interval behind the same content; the mirrored prior
pulls toward what will be there next. `SEED_FUT_LAMBDA` ships at 0 and
stays as the documented knob.

**Real footage.** Five segments of the 720p live-action clip,
decimate-and-reconstruct, the quad, the prior at 0.5:

| segment | shipped PSNR | foresight | shipped SSIM | foresight |
|---|---|---|---|---|
| 5 | 30.38 | 30.51 | 0.9510 | 0.9519 |
| 15 | 31.80 | 31.85 | 0.9627 | 0.9629 |
| 21 | 38.64 | 38.78 | 0.9768 | 0.9771 |
| 30 | 39.07 | 39.21 | 0.9752 | 0.9756 |
| 45 | 36.82 | 36.99 | 0.9776 | 0.9779 |
| mean | 35.34 | 35.47 | 0.9686 | 0.9691 |

Every segment up on both metrics, for +0.6% of the quad's time. For
comparison the temporal seed itself was worth +0.45 dB over the base on
these segments, the zero seed nothing and the Moire fix nothing. The
candidate-only form, the one that ships, on the same five segments:
35.34 -> 35.37 dB, 0.9686 -> 0.9687 SSIM, every segment up on both. A
second clip, the 60-second film excerpt at 24 fps, five segments, the
same method:

| segment | shipped PSNR | foresight | shipped SSIM | foresight |
|---|---|---|---|---|
| 5 | 41.87 | 41.87 | 0.9887 | 0.9887 |
| 15 | 34.11 | 34.11 | 0.9692 | 0.9693 |
| 25 | 37.96 | 38.03 | 0.9718 | 0.9719 |
| 35 | 29.80 | 29.83 | 0.9448 | 0.9449 |
| 45 | 24.44 | 24.44 | 0.9335 | 0.9336 |
| mean | 33.64 | 33.66 | 0.9616 | 0.9617 |

Every segment up on both metrics there too.

**The field.** On the manifolds at N:N the quad cannot show the seed
(fact 1). The quint, whose read comes from a seeded pair, moved a little
the wrong way with the prior at 0.5: aperture gross 18.0 -> 19.6% and the
over-read of the rigid translation 4.92 -> 5.08 px on 4.27; torus gross
46.9 -> 48.2%; mobius median 0.192 -> 0.200 px; zoom unchanged. The
acceleration field at N:N by `accelcheck` (the discrete truth, so the
quint's quartic is penalised by its own truncation correction here and
only each shader's own delta is meaningful), RMS over frames 4-20:

| case (full scale) | quad shipped | quad foresight | quint shipped | quint foresight |
|---|---|---|---|---|
| O9_osc_tex_fast (8) | 0.028 | 0.028 | 0.107 | 0.106 |
| O5_osc_textured (16) | 0.040 | 0.036 | 0.198 | 0.204 |
| A5_accel_tex_a067 (2) | 0.039 | 0.038 | 0.043 | 0.042 |
| A6_accel_tex_a133 (2) | 0.070 | 0.072 | 0.087 | 0.091 |

Coverage up by one to two points on every row. So the seed is a picture
result, not a field result: what it buys is a better choice among coarse
basins for the pair the picture is warped across, and the field's own
estimator sees a wash.

**The fully symmetric form, built and not shipped.** Deferring the base
pair's own chain until after the generated pairs and seeding it from
slot 1 <-> 2 too, so that every pair but the last is seeded from both
sides, changes the 32-case ladder by 0.03 dB or less against the partial
form (L2 a further -0.15 with the prior on), the footage by nothing, the
manifolds by nothing, and costs +5.0% on the quad and +3.2% on the quint.
The picture is warped across the middle pair and the base pair only feeds
the far link, so there was nothing for it to buy. Recorded so it is not
rebuilt.

**Shipped, in place, on by default.** The ship gate was the candidate-
only form against the shipped files in one sitting: the quad's 32-case
ladder must lose nowhere by more than 0.10 dB, the quint's likewise,
both real clips must not fall, and the time must stay within the run-to-
run spread. Measured: the quad's ladder mean +0.13 dB, worst case
A4_accel_tex_a033 -0.06, up by more than 0.1 on 5 cases
(A5_accel_tex_a067 +1.22, R3_rot_tex +1.00, A7_accel_tex_a167 +0.89,
O1_osc_gentle +0.35, O6_osc_tex_gentle +0.32), down by more than 0.1 on
0 (none); the quint's ladder mean +0.14 dB, worst A4_accel_tex_a033
-0.07; time quad +1.3%, quint +3.0% from a file. That is the one class
of change the variants rule lets replace a shipped file in place (free
within the spread, never worse on the ladder), and the owner's rule for
switches puts the default on the pole that works best in most uses: both
clips are up or level on every segment. The prior's extra tenth on the
live-action clip was the prior's own (the candidate alone gains a few
hundredths there), and it came with the 2.3 dB loss on a flat 16-px
translation, which is exactly the content of title cards and cel fills;
so the candidate ships and `SEED_FUT_LAMBDA` stays at 0 as the knob for
a live-action-only pipeline that wants the tenth. So `FORESIGHT` is on
by default in the two generators, the generated quad and quint files
from the seeded, propagated and animation bases are regenerated with it
(SHADERS.md's N-frame table carries the new quad and quint columns), and
`FORESIGHT=0` regenerates the 2026-09-04 form for a regression check.
The two-frame shaders and the tri are byte-identical. What the seed does
not do is on the record above: the field at N:N is unchanged in the quad
by construction and a wash in the quint, and the fully symmetric form
buys nothing. What remains open is the same question one level up: the
temporal seed reads the previous WINDOW; a reading that wanted the past
and the future of the LAST pair too would need the window to grow, which
is the quint's business, not a generator's.

#### The prior's loss, located and repaired: a deadband (2026-09-06, later)

The story above blamed the prior's 2.3 dB loss on the flat box on a trust
gate that a flat interior satisfies by accident. That was the first thing
tested, and it was wrong. Trusting the next pair's flow only where the
next pair's first frame has texture at the texel (`FUT_TRUST_CONTRAST` in
`tests/foresight.py`, off) changed nothing: with the prior at 0.5 every
one of the seven ablation cases and the live-action clip reproduced the
prior form to the hundredth (L2 59.16, L3 42.70, L6 64.67; 35.47 dB), and
the candidate-only form with the same trust reproduced the shipped file.
The flow the prior trusted had been matched on texture: at 1/8 res the
5x5 window reaches sixteen pixels, which is the edge.

The loss was then located in the picture. On the 16-px box the frames
that lose are one phase in five, the output two tenths past a source
frame, by one to two and a half decibels from a 63 dB level; the picture
pair's own flow, read through `read_view 4` at 24->60, is exact on both
edges for both forms; and a texel-by-texel difference against the truth
puts the whole of the extra error in the one to three columns of the
LEADING edge, where the prior form renders the anti-aliased edge a
fraction of a pixel further along (the edge column reads 240 against a
truth of 204, which the shipped form gets exactly). So the prior was not
choosing a wrong basin. It was breaking a sub-texel near-tie: the
candidates refined from different seeds land at slightly different
sub-texel positions inside the same basin, and a prior toward the next
pair's flow prefers the one nearest that flow over the SAD minimum. The
temporal prior has the same form and survives because the flow it pulls
toward was itself the previous window's SAD choice on the same content.

The repair follows from the mechanism: let the prior pull only beyond
half a 1/8 texel (`FUT_PRIOR_DEADBAND`), so it can break a basin tie
(aliases sit two or more texels apart) and never a sub-texel one.
Pre-registered before the run: L2 back to at least 61.3, L3/L6/A3 within
0.10 of the shipped file, A5/A7/R3 within 0.10 of the prior form, the
clip at least 35.44 dB. Measured, the prior at 0.5 with the deadband:
L2 61.44 (the shipped number), L3 43.51, L6 65.08, A3 40.35; A5 54.00,
A7 51.10, R3 37.33; the clip 35.47 dB and 0.9691 SSIM, the prior form's
full tenth, every segment above the shipped file. Every line met.

**The full gate, same sitting, against the committed files.** The quad's
32-case ladder: mean +0.02 dB against the shipped candidate-only form,
down by more than 0.1 on R3_rot_tex -0.16, up by more than 0.1 on R2_rot_accel +0.19, R1_rot_const +0.28, F2_fourier_accel +0.32; the
quint's mean +0.03, down by more than 0.1 on A6_accel_tex_a133 -0.14. Footage: the
live-action clip 35.37 -> 35.47 dB, 0.9687 -> 0.9691
(every segment up on both); the film
excerpt 33.66 -> 33.71, 0.9617 -> 0.9619
(every segment up on both). Time from a
file: quad +0.1%, quint -0.9%.

**What ships.** The deadband prior is a TRADE against the committed
candidate-only form: a tenth on live action for a few tenths on the
rotating texture and a hundredth or two on the flat cases. The variants
rule keeps a trade out of a shipped file, so the committed default
stays the candidate only (`SEED_FUT_LAMBDA` 0) and the prior with its
deadband is the documented pair of knobs, `SEED_FUT_LAMBDA` 0.5 with
`FUT_PRIOR_DEADBAND` 0.5, generated through `tests/foresight.py`. Whether
the live-action tenth is worth the rotating disc's loss is the owner's
call, and the numbers to make it with are the two paragraphs above.

### The owner's eyes on three renders, and what they found (2026-09-06, evening)

The owner watched the day's drops and reported by timecode: on the film
through the four-frame propagated shader, panning shots of texture and of
edges defect, and worst of all a flight of horizontal stairs mid-frame,
panning vertically, whose steps "alias"; on the cel episode through the
animation quad, a badly warped character at one instant and, throughout,
the loss of edge definition that has followed the cartoon content from the
start; on the 4K film through the 4K shader, nothing to fault and no
visible difference from the unscaled file. And a question: how much is
lost to the lossy encoding every source has been through. Each was taken
as a lead and measured.

**The stairs are a ladder gap, and the ladder had it coming.** Horizontal
edges at a regular spacing panning along their own period is the period
lock of section 3 in a direction the ladder never moved: every periodic
case moves along x. Three vertical cases were added and pass
`scenecheck.sh` bit-identical: soft bars of period 24 px on a box panning
down 6 px per frame (V1), the same bars hard-edged like stairs (V2), and
the hard bars at half a period per frame (V3, the alias by construction);
two horizontal twins of the first two (H1, H2) settle period against
direction. The family on them, PSNR at 24->60:

| case | hold | linear | variational | propagated quad | the same without the foresight seed |
|---|---|---|---|---|---|
| M2_period40 (horizontal, for reference) | 23.58 | 27.29 | 54.43 | 58.76 | 58.76 |
| V1_bars_sine24_v6 | 24.50 | 30.03 | **19.33** | 50.36 | 50.59 |
| V2_stairs_sq24_v6 | 18.19 | 21.48 | **16.60** | 27.21 | 27.15 |
| V3_stairs_sq24_v12 | 15.64 | 18.63 | 15.92 | 16.42 | 16.37 |

The recommended picture shader, the variational build, collapses on the
soft bars to five decibels BELOW frame duplication, and a frame shows
why: its bars are all present and sharp, and displaced against the truth
by a fraction of the period, the whole field on the alias, with the
box's top and bottom smeared where that flow meets the edge. To an eye
that is bars flowing at the wrong speed, which is what blinds, railings
and stairs do. The four-frame propagated quad reads 50 dB on the same
bars, and the day's foresight seed changes nothing there (50.36 against
50.59). On the hard-edged stairs both are poor and the variational is
again below hold; at half a period per frame nothing can tell the copies
apart, as section 3 says. Then every two-frame file was run on the soft
bars, vertical and horizontal: stock 19.21, seeded 19.22, propagated
19.26, animation 19.40, the variational 19.33, the 4K variational 19.62,
and the variational cascade rebuilt on the seeded base 19.28 and on the
propagated base 19.29, against the quad's 51.78 and 50.36. The direction
is irrelevant and so are the coarse seeds and the cascade: every two-
frame file collapses and the only four-frame file does not. What the
quad has and no two-frame file has is the ZERO SEED at the 1/8 level
(section 9), which the generators switch on for every field shader and
every picture base ships with off, and whose job is exactly this: a
coarse level that is Moire and a motion inside the 1/8 level's reach.
Pre-registered and then measured: with ZERO_SEED on, the propagated two-
frame file goes from 19.26 to 49.55 on the vertical bars and 51.81 on
the horizontal, level with the quad's 50.36 and 51.78; the cascade
rebuilt on the propagated base from 19.29 to 52.72 and 55.86, the best
of all; the hard stairs reach 27.43 and 26.96 (the quad's 27.21) and
29.03 and 28.64 for the cascade; the seeded file without the propagation
stage gains only to 36.8, so the propagation carries the basin the seed
finds. The references did not merely hold, as pre-registered, but rose:
the propagated file L1 74.80 to 76.37, A5 51.34 to 52.11, R3 34.04 to
36.37, O5 41.72 to 41.86; the rebuilt cascade A5 53.06 to 54.24 and R3
35.72 to 38.21 with L1 66.21 to 65.25. Time from a file: the propagated
file 1.270 against 1.260 s with the seed on, nothing. On real footage
the shipped variational still leads: clip 1 over five segments 36.27 dB
and 0.9741 against the rebuilt cascade's 35.70 and 0.9720 with or
without the seed, and the propagated file with the seed at 35.30 and
0.9696; on the stairs shot 40.36 against 40.09. The rebuilt cascade is a
quarter faster (1.618 against 2.134 s). So the collapse has a one-
constant fix in every base that carries the zero-seed code, its ship
gate is the full ladder and two clips (in flight as this is written),
and the cascade on the propagated base is a variant that trades half a
decibel on live action for immunity to this class, a quarter of the time
and ten decibels on the synthetic references; the variational build as
shipped cannot take the seed, since it is built on the stock base which
has no zero-seed code, and its 4K sibling shares the fault.

**The stairs the owner saw are not that.** The shot itself, eight seconds
around the timecode at 1080p, decimate-and-reconstruct on two windows: the
variational 40.36 dB and 0.9736 SSIM, the propagated quad he watched 39.19
and 0.9669, the same quad without the foresight seed 39.18 and 0.9668,
linear 37.15, hold 34.99; in the moving band, on the window holding the
stairs, 27.56 for the variational against 26.57 for the quad; at edges
(`edgeerror.sh`, mean luma error per edge pixel) 4.06 against 4.41. The
field on those frames, read exactly, pans at one pixel per frame with its
modes half a pixel apart and no second mode a period away. So the shot is
a slow pan of sharp edges, the defect is sub-pixel edge shimmer at the
interpolated phases, and the watch went through the field tier: the
picture tier does better on it by a decibel, and a three-way half-speed
crop of the stairs (blend, quad, variational) is in the owner's renders
folder for his eyes to confirm. The foresight seed neither helped nor hurt
there, to the hundredth.

**The cel shot cannot be scored.** Eight seconds around the warped dog
screen as drawn on twos (22 of 71 frames held at the start, holds
throughout), which the record says invalidates decimate-and-reconstruct:
frame duplication tops every metric there, as it must. The 360p excerpt
the animation work was measured on was screened for full motion; this one
was not, and the numbers are recorded only as a caution. What the owner
asked for is the line: the whole two minutes through the line-art shader,
the version the animation record says to carry and which had never been
in front of his eyes, is in his renders folder beside a three-way of the
dog shot (blend, animation quad, line-art). His eyes are the instrument
for that one.

**What lossy encoding of the source costs, measured on the stairs shot.**
The clean reference stays the truth while the decimated INPUT is taken
from an H.264 encode of the same frames; the retained frames then read
the encode's own loss and the synthesised frames the interpolator's from a
degraded input. Targets 20, 4 and 1.5 Mbit/s came out at about 8, 4 and 2
Mbit/s from the Media Foundation encoder:

| input | retained frames | hold | linear | variational | propagated quad |
|---|---|---|---|---|---|
| clean | exact | 34.99 | 37.15 | 40.36 | 39.19 |
| about 8 Mbit/s | 48-49 dB | 34.00 | 35.84 | 38.94 | 37.95 |
| about 4 Mbit/s | 45-47 dB | 33.82 | 35.59 | 38.61 | 37.65 |
| about 2 Mbit/s | 43-45 dB | 33.57 | 35.23 | 38.08 | 37.22 |

A good rip costs the variational 1.4 dB, a poor stream 2.3, and most of
that is the encode degrading the picture itself: frame duplication loses
1.0 and 1.4 from the same inputs, so the interpolator's own extra loss is
0.4 dB at a good bitrate and 0.9 at a poor one. The order never changes
and the variational keeps three decibels over the blend at every bitrate.
The owner's intuition holds, and its size is about a decibel and a half
at the bitrates his library carries. The same experiment on the synthetic
ladder is void and says why: the scenes are so simple that the encoder
wrote the same five-kilobyte file at every target, and a file source with
a different pixel format shifts the shaders' numbers on its own (L1 61 dB
from a lossless gray file against 70 from the lavfi source), which is an
instrument caveat for anyone who benches from files.

**The zero seed's gate, and what ships (later the same evening).** The
propagated two-frame file with the zero seed on against the same file
with it off, the ladder's 37 cases in one sitting: mean +2.48 dB, down
by more than 0.1 on F1_fourier_edge -1.19, L3_trans_23px -0.56,
R2_rot_accel -0.28, M2_period40 -0.19, L7_textured_large -0.15,
M3_period16_trap -0.13, up by more than 0.1 on 17 cases (L1_trans_8px
+1.57, R3_rot_tex +2.33, H2_stairs_sq24_h6 +11.23, V2_stairs_sq24_v6
+11.70, V1_bars_sine24_v6 +30.29, H1_bars_sine24_h6 +32.55). Real
footage, the live-action clip: 35.28 -> 35.30 dB, 0.9696 -> 0.9696; the
film excerpt: 33.74 -> 33.79, 0.9629 -> 0.9629. Time from a file 1.270
-> 1.260 s. Not clean: the seed stays off in the bases and the trade is
recorded here for the owner. The cascade rebuilt on the propagated base
with the seed, against the shipped variational on the same ladder: mean
+3.71 dB, down by more than 0.1 on L6_flat_large -3.49, L4_trans_40px
-3.39, M2_period40 -2.43, A3_accel_23mean -1.73, M1_noise_large -1.12,
O4_osc_flat300 -0.37, L3_trans_23px -0.33, O2_osc_medium -0.33,
M3_period16_trap -0.29, O1_osc_gentle -0.19, O3_osc_hard -0.18,
L2_trans_16px -0.16, L9_occlusion -0.15, up by more than 0.1 on 21
cases; on the film excerpt 34.44 -> 34.10 dB and 0.9662 -> 0.9645, on
the live-action clip 36.27 -> 35.70 (job P). It ships as `bidirectional-
interpolation-variational-propagated.glsl`, generated by
`gen_variational.py` with its new base argument, a variant beside the
recommended file: a quarter faster, immune to the collapse, half a
decibel behind on live action. Which of the two the picture
recommendation names is the owner's, as it always was.

**The owner's two decisions (2026-09-06, late).** On the picture recommendation, in
substance: quality matters more than performance, the gain on the
cascade-on-propagated is significant, and a GPU that cannot run the
better shader needs upgrading rather than the shader shrinking. So
`bidirectional-interpolation-variational-propagated.glsl` is the recommended
file, and its scaling the 4K one: on the real 4K film 35.01 dB and
0.9646 SSIM over the five segments against the previous 4K file's
35.62 and 0.9665, 53.5 dB on the period-24 bars at twice the
ladder's size where the previous file reads 19.3, time 7.46 against
8.73 s. On the zero seed: the Fourier-edge case under rotation is a
scientific interest, a particle jiggling in a trap; film is panning,
zooming and translation, and the switch depends on what the use case
asks for. So the seed is on by default in the propagated, seeded and
animation bases (their generated field shaders had it already and are
byte-identical), and the switch stays for the laboratory.

### The owner's eyes, second day: the opacity switch, a pendulum, the stairs' aperture, and an idea for animation (2026-09-07)

**The reading's opacity as magnitude, and the switch.** The owner asked (2026-09-06) whether the
painting's transparency could carry what its hue cannot: a rotating disc is fastest at its rim and still
at its axis, and the painting saturated everything past 3 px. It can, and it shipped as `read_alpha`
(4278d2c): opacity = magnitude / scale. His first look was "absolutely brilliant", his second question
was the right one: with a fixed scale "the middle 0 and the outside 1 would look very good, but it would
only scale for this particular image." So the parameter became a three-pole switch on his call (669cd9c):
0 = auto (the default; full at the frame's running maximum of the pooled field, an exposure with attack
0.3, decay 0.99 per frame, floored at the field's HI gate), above 0 = manual px per frame for fine
tuning, below 0 = the flat painting of before. Measured on his large ordinary disc (radius 480 px, plain
edge, rim 8.0 px per frame): the estimator reads omega r at 0.93-1.03 in every band from r 30 to the
rim; the pooled field the painting shows is 0.89-1.00 out to r 430 and falls only inside its last half
window (0.84 at r 430-460, 0.61 at 460-478), so on a disc larger than a few windows the manual scale at
the rim's speed paints opacity r / R. The auto scale's limit sits beside its point: a disc slowing to a
stop stays dense until the decay catches up, so the physics of a deceleration is the manual scale's to
show. Renders: `hot-drops/bigdisc-*`, `oscdisc-*`, `disc-*` (not in the repo).

**The pendulum.** He asked for the disc swinging: from a stop, accelerating to the rim's 8 px per frame,
decelerating to a stop, and back (theta = A (1 - cos 2 pi t / P), P = 6 s, A = 0.382 rad), with the
velocity and acceleration readings beside the picture. The velocity panel reads the physics: dim and
hollow while accelerating, a full wheel at the peak, fading toward the stop, nothing at the stop, the
hues reversed on the way back. The acceleration panel shows the tangential ring at the stops (r alpha,
0.35 px per frame^2 at the rim, above the SAT gate) and only sparse patches at the peak, where the
tangential part is zero and the centripetal omega^2 r = 0.13 px per frame^2 sits at the LO gate; the
ring fades toward the axis exactly as the velocity did, because the acceleration is r alpha.

**The hole.** He finds the gate's hole at the axis "fascinating": not a circle but "a loop of string".
It is where the speed is below the 1-2 px gate, and its shape is the estimator's: at r 30-150 the raw
magnitude ratio is 0.77-0.85 in two 30-degree sectors aligned with the texture's lattice and 1.0-1.08
elsewhere, so the under-read along the lattice pushes more of the disc under the gate in that direction
and the hole is a tilted ellipse that grows as the disc slows (frames 18 and 60 of the pendulum).
Observed, not explained; the test is to turn the texture 45 degrees and watch the ellipse turn with it.

**The stairs' "lensing".** On `stairs-3way-linear-quad-variational-halfspeed.mp4` he saw the variational
(right) get the stairs perfectly right for stretches and then lose it for moments, "like the lensing of
a drop of water where a bit of the shader has lost cohesion", while the quad's defect ran throughout.
Measured (np-scratch/eyes/stairs-loss; the field at N:N, mode 4, every frame of the 8 s clip, for the
old variational and the recommendation): the shot is a horizontal pan that accelerates from 1 px per
frame (frames 96-106) to 20 (frame 128) across a flight of horizontal steps (period 27 px along y) with
a dancing man in front, and the watched window (frames 60-132) covers the whole acceleration. No
whole-frame moment exists: the consecutive-frame difference of the three renders has no spike beyond
the shared onset at frames 7-10, and the local incoherence (cells more than 1 px from their 5x5
neighbourhood's median) rises smoothly with the pan, 0.01 at 0.5 px per frame, 0.05 at 2, 0.12 at 3.5,
0.2-0.37 at 13. The events are local and late: of the 40x40-px blocks whose frame-to-frame change
exceeds linear's by more than the 99.5th percentile, 201 (variational) and 220 (recommendation) fall in
the last watch second against at most 46 in any other, and the two shaders' top events coincide in
block and time. On the stairs alone, clear of the man (crop x 480-720, y 0-180), the spread of the
horizontal component across a rigid background (p90 - p10, which a camera pan should leave near zero)
is 1.2 px at a 1 px per frame pan, 2.6-3.3 at 1.5-2, 6-8 at 3.5-4, and 8-18 at 11-20, the recommendation
wider at the fast end (p10 4-6 px against the variational's 10-12). The mechanism is the aperture: the
steps are horizontal lines, which cannot see horizontal motion, so their horizontal component comes
from whatever structure is nearest, the man's (-12 to -17 px per frame, the cells that read backwards
at frames 118-136 are his figure, x 250-700 of the crop) or the background's (+17 to +22), and the
picture warps blob by blob. The propagated base carries the man's vector further into the steps, which
is its cost here. The ladder has no case for it: its period-24 series pans ALONG the bars' period (the
constrained direction); this shot pans ACROSS horizontal lines with sparse vertical features, and a
case for that is the next instrument. A fix would be an aperture-aware fill: where the structure tensor
is one-dimensional, take the along-line component from the nearest two-dimensional structure rather
than from the nearest cell.

**The reading segments the mover.** At the same moment (`stairs-3way-picture-variationalreading-variationalpropagatedreading-halfspeed.mp4`
at 5.0 s) the painted field shows the man as one green figure on a red background: the reading already
separates the object in motion from the pan.

**The owner's idea for animation, recorded.** `watch-cel-lineart-60fps.mp4` is "interesting but still
not viable, heavily defective"; on `dog-3way-linear-animquad-lineart-halfspeed.mp4` the linear is the
most watchable, and the linears are flawed because a damaged frame in motion does not look nice played
back. His proposal: an image classifier as a pre-processing step to identify objects in motion and the
sub-parts of objects (the full body of the dog, the legs, the arms, the ears, the mouth on the head),
tracing every coherent feature, so that the two approaches strengthen each other. He does not think it
can be solved here, and the standing rule remains that no tweak on animation has yielded a significant
result. It is on the outline list beside the depth-from-parallax and known-motion items, with the note
above that the reading's own field already segments a mover on live action.

### The hole, tested; the stairs, seen again; the tri's root; a second 4K film (2026-09-07, afternoon)

**His eyes on the stairs renders.** On `stairs-3way-linear-variational-variationalpropagated-halfspeed.mp4`
the recommendation's effect over the variational is that the lensing defect is now "in small blobs rather
than fully eliminated": a noticeable change, the defect remaining over the sequence, which is what the
aperture measurement above predicts (the steps borrow their horizontal component blob by blob; the
propagated base changes the blobs, not the borrowing). On the readings file the recommendation's reading
is the cleaner: where the variational's shows "a substantial yellow hot spot on the stairs which is a
miss-fire", the recommendation's shows "a reasonable clean plate on the same frame".

**The hole's size scales with the derivative order** (his observation on the pendulum: the acceleration
panel's hole is larger). A field on a disc grows linearly with radius, so the hole's radius is the gate
over the field's rate per pixel of radius: velocity at the peak, rate 1/60 px per frame, gate 1/2 px,
hole r 60-120; acceleration at a stop, rate 7.3e-4 px per frame^2, gate 0.12/0.22, hole r 165-303.
Measured at the 10% and 50% chroma crossings: velocity r 140/230, acceleration r 280/340, the excess
over the prediction from the gate's smoothstep, the pool's window cancelling opposite vectors across the
axis, and the memory's lag; the ratio of the two holes is the predicted two. Each time derivative of a
swing divides the signal by the swing's angular frequency (a factor of 23 per order at this period)
while the gates fall a decade, so the unreadable core grows with every order; the jerk would show
nothing at all here (0.015 px per frame^3 at the rim against a gate of 0.12).

**The hole's shape, tested cheaply** (`claude-handoff/d3/reading-alpha/hole/`). Five spinning variants
of the large disc, the raw field (mode 4) at 1080p, the magnitude ratio to omega r binned by the
MEASURED vector's direction (so no sign convention enters), r 60-300; then pure translation of the
same lattice disc at 1.0, 1.5 and 2.5 px per frame in eight directions; then a control with band-limited
isotropic noise (periods 30-80 px, random phases, bilinear-sampled so it is rigidly attached).

- Not the estimator's sign bias: the translation test's direction dependence is 180-degree periodic
  (45 and 225 read 1.13 and 1.16, 135 and 315 read 0.66 and 0.63, with 26-degree angle errors).
- Not peak locking: the same ratios at 1.0, 1.5 and 2.5 px per frame, integer or not.
- The texture's aperture: the weak direction turns with the texture (spin +, frame 4 with the texture
  near 0 degrees: weakest at 90-150; frame 47 with the texture at 45: weakest at 30-60; spin -: 90
  then 150; the texture pre-turned 45: 60 then 0). The lattice is a product of sines, two diagonal
  gratings, and one diagonal is weak across; the isotropic noise reads 0.90-0.99 in every direction
  (spread 0.05-0.09 against the lattice's 0.21 at frame 4) and its hole is round
  (`hot-drops/hole-lattice-vs-isotropic-frame40.png`). The translating noise disc reads 0.91 at 18
  degrees where the lattice read 0.63 at 26.
- The anisotropy is strongest early and under acceleration: the lattice's spread falls from 0.21 at
  frame 4 to 0.05-0.07 by frame 40 of a steady spin, so it depends on the temporal seed having a good
  previous flow; the pendulum, accelerating continuously, keeps the seed stale, which is why its hole is
  the long string and the steady disc's is a lumpy square. Suggestive, not separately verified.
- Twice the texture period: spread 0.08 at frame 4 in the folded-direction binning, flat by frame 47.

So the conundrum resolves into three parts, none mysterious and none insurmountable: the hole's SIZE is
the gate over the signal (a display choice); its SHAPE is the texture's aperture, a property of the
picture that any local matcher shares, worst under acceleration where the temporal seed lags; and the
estimator's own contribution is a direction-independent 5-10% under-read in the sub-2 px regime. The
open item is the aperture-aware fill already named for the stairs: it is the same physics at a smaller
scale.

**The tri's root** (his question: it was made before much was known; is it symmetric, and should it be
rooted in the middle frame?). It is, where three frames allow. The generator is slot-keyed: the window
is {prev2, prev, next} while the output sits in the first half of a source interval and {prev, next,
next2} in the second, the anchor is always slot 1 (the middle frame), and the acceleration solve is
centred on it (a = F10 + F12). At N:N the output is on frame n, the straddling pair is (n, n+1) and the
nearest third is n-1, so the window is {n-1, n, n+1} with the output on the anchor: one back, one
forward, exactly his prescription. Between frames a three-frame window is necessarily lopsided by one;
the quad's 2+2 and the quint's 2+3 are the symmetric straddles for interpolation, which is why the
family moved there.

**A second 4K film.** Supplied 2026-09-07 (3840x2160 ten-bit HEVC, 23.976 fps, 156 min, 19 Mbit/s; never
the title in this record). For his eyes: ten random non-overlapping 60 s clips at the source's own
rate with the velocity reading painted over the picture (read_view 1, the auto scale), through the 4K
recommendation, native size: `hot-drops/4k2-01.mp4` to `4k2-10.mp4` in time order, starts in
`4k2-clips.txt`. Each 60 s clip rendered in 60-160 s. His note on the fields: the velocity is the one
humans read, "because the muscles of our eyes are used to tracking at a constant rate, not an
accelerating one". The decimate-and-reconstruct bench, nine 3 s segments spread over the film (900 to
8100 s at 900 s steps), five modes, PSNR / SSIM means over the segments:

    hold 39.78 / 0.9769   linear 41.35 / 0.9795   variational-4k 43.45 / 0.9828
    variational-propagated-4k (the recommendation) 43.34 / 0.9827   its unscaled form 42.93 / 0.9822

The recommendation and the variational-4k are equal on this film (0.1 dB on the mean, the same SSIM),
both two decibels over linear; the scaling is worth 0.4 dB on the mean and 2.0 on the fastest segment
(900 s: 44.66 against 42.68 unscaled), so the 4K recommendation stands. The hardest segment is 5400 s
(36.9 dB, all modes within 0.5 of each other), the easiest 6300 s (46.1, where linear is within 0.15
of every shader). The source is much cleaner than the first 4K film (its means were in the mid
thirties): the numbers here are the pipeline's, not the grain's. Passthrough on this ten-bit source
reads 54 dB with no retained frame bit-exact, the known ten-bit floor of the render path, not a
misalignment (hold reads infinite on the same frames).

**The seven-frame question** (the owner, 2026-09-07: "is it worth building the 7-frame symmetrical rooted
in frame 4 looking 3 back and 3 forward, or would this be a wobble too far?"). Section 2's analysis,
extended to seven points: a centred least-squares fit's fraction of the true acceleration on the O series
(periods 23.4, 9.6 and 6.0 frames, recovered from the three-point attenuations) and its noise gain for
unit noise per sample.

    window, degree             O1      O2      O3    noise gain
    3 frames, degree 2        0.994   0.965   0.912    2.45      (the tri)
    5 frames, degree 2        0.974   0.852   0.652    0.54
    5 frames, degree 4        1.000   0.998   0.988    3.13      (the quint)
    7 frames, degree 2        0.944   0.701   0.370    0.22
    7 frames, degree 4        0.999   0.982   0.898    0.93
    7 frames, degree 6        1.000   1.000   0.998    3.46

For the picture, no: the ladder's quint column is the quad's within a tenth of a decibel on every case,
the picture's information being in the straddle pair and the next frame out, and the sext measured the
cost of going further. For the field, seven at degree 2 is the wobble too far (a third of O3's
acceleration), seven at degree 6 gains nothing over the quint and is noisier, and seven at degree 4 is
the one configuration worth a line: the tri's fidelity on the fastest case, better on the rest, at less
than a third of the quint's noise. Its use would be the machine's acceleration field on slow motion,
inside the window rule (a third of the fastest period); it does nothing for velocity, which the straddle
pair already gives exactly, and nothing for the hole. Caveat from P6: the far flows are the noisy
samples, so the realised gain is smaller than the equal-noise table. Left on the outline list; the
generators are general in N, so it is a day from the sext's.

**Four more renders for his eyes, and what they show** (`hot-drops/orbitdisc-*`, `sqdisc-*`, `sqorbit-*`;
scripts in `claude-handoff/d3/reading-alpha/`). The pendulum disc whose centre also circles its origin
(50 px radius every 4 s, so 3.3 px per frame of translation under a rim speed of 8): the instantaneous
centre of rotation wanders, the velocity hole leaves the disc's centre at peak spin (to 3.3 / omega, about
200 px) and vanishes at the stops, where the motion is pure translation and the whole disc paints one
hue. At those stops a dark patch appears where the translation runs along the lattice's weak diagonal:
the translation test's 0.63 under-read, seen in the painting. The same two motions with a rotating
square (half-side 340 px, corners at the disc's radius): the corners paint strongest, the hole is a
diamond stretched along the square's diagonal and larger than the disc's, because the straight edges add
their own aperture to the lattice's, and the orbiting square shows the same wandering and the same dark
patch at the stops. Nothing in the four contradicts the hole's account above; the square adds the
edge-aperture to it.

### The aperture series, the tensor fill refuted, and the alias behind the fast end (2026-09-07, afternoon)

The owner left the afternoon open ("dive into the previous leads, be chaotically random sometimes"). The
lead was the one his stairs opened: build the ladder case that pans ACROSS lines, measure, and try the
aperture-aware fill named above.

**The series** (`tests/scenes.sh`, P1-P5; all bit-identical at both rates). The V2 stairs again, 600 x 300,
panning ALONG their bars with a weak speckle riding on them (contrast 12) so a wrong horizontal component
warps something visible: P1 at 4 px per frame on a fine speckle (period 13.8 x 11.3 px), P2 and P3 at 8
and 12 on a coarse one (40 x 30 px), P4 at 8 with a textured crosser moving the other way in front (the
film's geometry), P5 at 8 on the fine speckle. The first form put the fine speckle on all of them, and the
raw field said why that was wrong: at 8 px per frame 39% of the stairs' cells read -5.8, which is 8 minus
the period, and at 12 every cell read -15, the second alias, while the picture still scored 37 dB because
bars warped along themselves look the same. Two lessons: the picture metric is nearly blind to a wrong
horizontal component on bars, so the field's spread across the stairs (`claude-handoff/d3/reading-alpha/
aperture/pspread.py`) is the instrument for these cases; and a fine texture under a fast pan is an alias
trap, not an aperture test. Hence the two speckles.

**What the clean cases show** (picture; the field's p90 - p10 of the horizontal component across the
stairs at frame 16, truth uniform):

    case                 hold  linear   base   quad   vari    vp  |  spread: quad   vp
    P1 fine, 4 px        34.1   37.4   43.4   43.2   37.2  45.3  |
    P2 coarse, 8 px      31.3   34.1   60.1   58.3   55.6  58.6  |          0.81  2.03
    P3 coarse, 12 px     29.4   32.1   47.9   48.0   52.4  53.7  |          1.16  2.13
    P4 crosser, 8 px     26.1   30.1   52.2   50.7   26.9  51.6  |          0.81  2.09
    P5 alias, 8 px       30.7   33.4   42.0   42.0   37.7  41.9  |         13.84 13.23

With a resolvable texture the propagated family handles the aperture: 60 dB at 8 px per frame against a
plain translation's 62, the quad's field within 0.8 px across the whole flight. The old variational
COLLAPSES on the crosser to 26.9 dB, below linear: the man's vector diffused into the stairs, which is the
film's failure in one number, and the recommendation holds 51.6 there, which is what his eyes reported
(the lensing "in small blobs rather than fully eliminated"). At 12 px the two-frame base falls to 48 and
the cascade lifts it to 54 with a wider field (2.1 px against the quad's 1.2): the cascade's picture wins
at the fast end though its field is looser.

**The tensor fill, refuted twice** (`tests/gen_aperture.py`, behind PROP_TENSOR, off = byte-identical to
the base). Form 1: each neighbour votes through its trace-normalised structure tensor over a radius-8
window, the own vote as the base's, the check's disagreement projected through the cell's tensor. The
41-case gate: mean -0.70 dB, 17 cases down by more than 0.1 (A5 -6.1, R3 -4.5, L1 -3.5, A4 -3.2, O6 -2.8,
L2 -1.8, M2 -1.5), 6 up (V1 +1.6, L8 +0.7). Two faults, both diagnosable from the table: trace
normalisation makes an isotropic cell half the identity, so the projected disagreement is halved and the
alias rejection the base earned its keep with (M2, O6, A5) is defeated; and a radius-8 window carries
twelve times the base's neighbour votes against the same self weight, so constrained components are
smoothed too (L1, L2, R3). Form 2 fixes both (largest-eigenvalue normalisation; self weight scaled to the
window) and on the seven deciding cases reads A5 +0.9, M2 and O6 flat, L1 -1.9, R3 -0.45, P2 and P4
+0.0 at either radius. The gains it was built for do not exist, because the base already fills the
aperture where a resolvable texture constrains it, and it still costs a plain translation two decibels.
REFUTED; the generator stays as the record of the design point and ships no shader.

**The alias behind the fast end.** P5 is the ladder's proxy for the film's stairs at 11-20 px per frame
with their fine sequin texture: 39-46% of the cells on the alias for every shader, spread 13-14 px, and no
shader fixes it. The mechanism is the period-24 lesson's other half: for a periodic texture of period p
moving at v > p / 2 the alias v - p is NEARER ZERO than the truth, the coarse level is blind to the texture
(below its Nyquist) and to the motion along the bars (the aperture), and the arbitration's magnitude
prior (SEED_MAG_LAMBDA) then prefers the alias in a SAD tie; the temporal seed perpetuates whichever won
at the window's start. The disambiguator has to come from outside the texture: the box's own motion at
the coarse level (its ends), or continuity across frames. An open lead, with the case to gate it.

**The chaos he asked for: twelve random segments of the second 4K film.** Seed from the clock (1788786914),
3 s each, decimate-and-reconstruct, the three broken by GPU contention re-run alone. PSNR / SSIM means:
linear 41.01 / 0.9765, variational-4k 42.27 / 0.9836, the recommendation 42.93 / 0.9853. The random draw
found what the nine fixed segments had not: two segments of fast action at 9029 and 9090 s where linear
reads 23 dB, the variational-4k 28.5 and 27.7, and the recommendation 31.0 and 31.1, a gain of 2.6 and 3.4
decibels on the hardest footage in the film; and one segment (3545 s) where the variational-4k loses to
linear (44.2 against 45.2) and the recommendation does not (46.5). The recommendation is never below
the variational-4k by more than 0.3 on any of the twelve. The 4K recommendation stands, more firmly than
the fixed segments said.

**The owner's 3D question** ("are we neglecting 3D shapes, translating and rotating spheres and cubes?").
The ladder is planar; the manifold renderer has the 3D work on the field side (torus, band, tesseract,
Hopf) and taught the limb and the aperture lessons. A sphere would repeat the torus's; a CUBE would add
what the ladder lacks: per-face affine flow (divergence and shear, no affine case exists), edges as
aperture on the object, and self-occlusion at its own silhouette as faces turn in and out, which is what
buildings, vehicles and turning faces do on film. The path is cheap, six textured quads with hidden-face
removal in the renderer and the decimate-and-reconstruct bench on the rendered clip. On the outline list,
on paper until the GPU is free.

**Housekeeping from the same afternoon.** Running five GPU jobs at once made h264_mf fail with "Cannot
allocate memory" and libplacebo with vkAllocateMemory failures: two 4K bench segments aborted and one
rendered corrupt frames that scored a plausible 39 dB the alarm did not catch. 4K work runs alone from
now on, chained on the previous job's DONE line, and every bench's .err files are grepped for allocation
failures before a number is trusted (the memory carries the rule). The reading's plate under the
painting, the luma alone at 35% inherited from the Metal demo's display, read as black and white on his
clips; a colour plate at the same 35% read the same to his eyes, and the measurement said why: the chroma
was there in proportion (2.8 on a luma of 14 where the source had 7.3 on 38) and invisible, because a
dimmed plate of a dark film shows no colour. The plate's brightness is now a parameter of the tail,
`read_plate`, default 1 (the picture as it is, the field painted over it), 0.35 the old look, verified on
a mid-brightness frame beside the source before the clips were rendered again. The lesson is recorded
against the author, not the shader: the first fix was confirmed by its mechanism and a dark frame, not by
the outcome the owner would see.

**And a third time: the film is HDR.** With the plate at full brightness his eyes still saw a washed-out
picture in the wrong palette and suspected the overlay's blend. The blend was innocent. The second 4K
film is HDR10 (BT.2020 primaries, PQ transfer; the first film was BT.709 and needed nothing), the clips
were rendered without tone mapping and written as 8-bit files with no colour tags, so every player showed
PQ code values as SDR gamma. The verification of the plate had compared the clip to a source frame decoded
the same naive way, which is why it passed: a reference is only a reference when it comes from an
independent correct path. Fixed on the GPU: the shader's own libplacebo instance outputs BT.709 SDR
(`colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv`, the default tone mapping) and the
file is tagged; measured against libplacebo's own tone map without the shader, the unpainted pixels
agree to 2.2 levels (luma 80.7 against 80.3, chroma 20.2 against 17.1, the difference the paint's soft
edges), and a two-instance path (tone map first, then the shader) gives the same to 2.4. `watch.sh` and
the clips script probe the transfer and do this for any PQ or HLG source from now on. The reading's
hues over a bright SDR plate read pastel where they read saturated over the dark one; `read_plate` is
the knob if the owner wants them stronger.

### The cube, the manifolds through the reading, and a black hole (2026-09-08)

The owner, out of ideas for the moment, asked for a look at the stairs work, some 3D human-reading
renders, and, unprompted by anything but curiosity, a black hole.

**The stairs work, for his eyes.** Two aperture-series cases as half-speed three-ways and as readings
(`hot-drops/stairs-ladder-P4-crosser-*`, `stairs-ladder-P5-alias-*`, each scene extended to 2.5 s and
played three times). On P5's reading the alias shows itself: the stairs paint red for their rightward
motion with dark holes where the pool averages the true +8 against the alias's -5.8 and falls under
the gate.

**The manifolds through the reading** (`hot-drops/manifold-<torus|mobius|tesseract|hopf>-picture-velocity-acceleration.mp4`,
`manifolds-four-velocity-readings.mp4`). The torus and the band paint; the tesseract and the Hopf
fibres barely do. That is the reading's honest answer on thin tubes, which the record already knew
from the field checker: the aperture problem everywhere, and a pooled field under the gate.

**The cube** (`tests/manifolds.py`, scenes `cube` and `cubet`; half-side 150 px; the M1 texture in
each face's own coordinates with a Lambert shade; hidden faces removed by the splat's depth buffer;
`cube` rotates in place about a tilted axis at 0.5 rad/s, `cubet` also translates in a 220 px circle
every 8 s). It adds what the planar ladder lacks: per-face affine flow, edges as aperture on the
object, and self-occlusion as faces turn in and out. First numbers, decimate-and-reconstruct on 3 s
of each (PSNR / SSIM), and the quad's raw field against the analytic truth at frame 48:

    cube  (rotating, |v| ~2 px)  hold 30.42  linear 34.36  base 31.92  quad 31.87  vari 30.78  vp 33.55
                                 SSIM .9711  .9832  .9770  .9758  .9722  .9822
    cubet (+ translating, ~6 px) hold 24.63  linear 26.71  base 27.79  quad 27.77  vari 27.42  vp 28.45
                                 SSIM .9128  .9178  .9442  .9435  .9486  .9454
    field, cube  frame 48: median 0.44 px, p90 2.3, gross (>2 px) 11%, angle 3.6 deg, |v| 2.14 true / 2.24 read
    field, cubet frame 48: median 0.41 px, p90 6.4, gross 17%, angle 3.3 deg, |v| 5.99 true / 6.77 read

The rotating cube is the first synthetic case where LINEAR BEATS EVERY SHADER, by 0.8 dB over the
recommendation and 2.4 over the two-frame base. The field says why: the median is fine but a tenth of
the pixels are gross, at the turning edges where a face's affine motion is not one vector per block and
where faces appear and disappear with no correspondence to find; warping a high-contrast lattice
texture on a wrong vector costs more than a blend's blur at 2 px per frame. With translation added the
shaders win again (+1.7 dB for the recommendation over linear) because the translation dominates, but
the gross fraction rises to 17%. This is the case the outline list's "affine match" item was waiting
for: a matcher that fits a per-block affine (or at least a divergence and shear) would be gated here,
and the self-occlusion half would need occlusion reasoning the family does not have. Both stay on
paper; the cube now measures them.

*(2026-09-28: the `scripts/blackhole/` folder was removed from the repository at the owner's word, as superfluous to
the scripts. Every script named below is in git history, last at `111cb2f`, and is published with its renders at
cadencevideoplayer.com/blackholes/.)*

**A black hole** (`blackhole/blackhole.py`, not a test: the owner's curiosity). A
Schwarzschild black hole in geometric units with a thin, opaque, glowing dust disc from the innermost
stable orbit at 6 M to 18 M, seen from 40 M at 78 degrees from the disc's axis. Every pixel's null
geodesic is integrated once in its own orbital plane (the Binet equation u'' = -u + 3 u^2, fourth-order
Runge-Kutta, 921,600 rays) until it falls in, escapes to a lensed star field, or crosses the disc; the
crossing's radius, azimuth and redshift factor g = sqrt(1 - 3/r) / (1 + Omega b_z) (gravitational and
Doppler together, a Keplerian emitter) are kept, and each frame is then a lookup of a multi-octave dust
pattern winding up under differential rotation, weighted g^4 and coloured by the observed temperature.
The picture has what the famous ones have because the physics puts it there: the shadow, the disc in
front, its far side lensed into an arch above and a lobe below, the approaching side beamed bright,
and the thin photon ring inside the shadow. `hot-drops/blackhole-disc-10s.mp4`, and the same through
the human reading (`blackhole-disc-picture-velocityreading.mp4`): the field of a warped, differentially
rotating disc as the shader reads it.

**Black holes that are not Schwarzschild** (the owner's challenge, the same evening: every exact solution sets
something to zero; render one that is not the Schwarzschild metric). There is no general solution to
render: the general case exists only in numerical relativity, and even there as two holes merging. What
can be done is two steps out. `scripts/blackhole/geodesic_disc.py` (the owner's choice for the repository;
it began as blackhole/kerr.py) is a second, metric-agnostic tracer:
Hamilton's equations for a null geodesic in the full four dimensions, the metric entering only as its
five covariant components g_tt, g_tphi, g_rr, g_thetatheta, g_phiphi as functions of (r, theta), the
inverse taken numerically and the derivatives by central differences, fourth-order Runge-Kutta with the
step shrinking toward the horizon and toward the coordinate poles (a seam at the top of the shadow until
it did). The disc's innermost stable orbit, orbital frequency and u^t are found numerically from the
metric, so nothing about the spacetime is derived by hand; the redshift is Cunningham's
g = 1 / (u^t (1 - Omega p_phi)). Three metrics from one camera (40 M, 78 degrees off the axis): the
Schwarzschild control, which the general tracer reproduces (horizon 2, ISCO 6.00); Kerr at a = 0.9
(horizon 1.436, ISCO 2.321, the D-shaped shadow flattened on the prograde side, the disc reaching in to a
third of the radius, frame dragging in the light); and the Johannsen-Psaltis deformation of that Kerr
metric with eps3 = 3, which solves NO vacuum field equation, the kind of parametrised non-Kerr black hole
astronomers test the no-hair theorem against (ISCO 1.465, the image visibly different: a smaller, dimmer
disc that reaches almost to the horizon). Files: `hot-drops/blackhole-<schwarzschild|kerr|jp>-5s.mp4`,
`blackhole-triptych-schwarzschild-kerr09-johannsenpsaltis-5s.mp4`, `blackhole-triptych-frame60.png`, and
the triptych through the human reading.

**Hawking radiation, rendered as far as the mathematics allows** (the owner, the next morning: Hawking
radiation is undetectable in nature because it is fainter than the cosmic background, but our synthetic
space has no background; can a black hole be rendered close enough to visualise the never-seen glow?).
The answer has a negative half, computed rather than quoted, and two honest pictures.

The negative half. `blackhole/greybody.py` integrates the electromagnetic Regge-Wheeler
equation for the horizon-born photon modes at 260 frequencies and eight multipoles (fourth-order
Runge-Kutta in the tortoise coordinate from r = 3000 M in to r - 2M = 1e-7; the outgoing/ingoing
decomposition at the horizon end gives the transmission). Checks: Gamma -> 1 at high frequency, Gamma_1
goes as w^4.1 at low (theory 4), the multipole sum tends to the capture cross-section 27 w^2 above
w ~ 1/M, and the total photon power comes out 3.364e-5 hbar c^6 / G^2 M^2 against Page's 1976 value
3.36e-5. The photon spectrum peaks at w M = 0.243 = 6.1 T_H (a blackbody peaks at 2.8 T_H: the potential
barrier at r = 3M throws the long wavelengths back in), which is a wavelength of 25.8 M = 12.9 horizon
radii FOR ANY MASS, and 98% of the power is in l = 1 (Gamma_1 = 0.415 at the peak, Gamma_2 = 0.0004). A
black hole radiating at its own peak is a pure dipole. Its light carries no image of it, at any distance,
in any instrument: an emitter thirteen times smaller than its light is a point, and going closer never
changes that. The wished-for render of "the hole lit by its own Hawking glow" does not exist, not for
lack of signal but for lack of wavelength. The mass ladder (`hawkchart.py`): a hole glowing at the Sun's
colour has M = 2e19 kg, a 30-nanometre horizon and 1.4 microwatts; the film's 2000 K hole is 6.1e19 kg
(a 35-km asteroid), a 91-nm horizon, 150 nanowatts, at arm's length a faint orange star; above 4.5e22 kg
(T_H = 2.73 K) a hole absorbs more background than it emits, which is the observation problem in one line.

The two pictures. (1) `hawkapproach.py` -> `hot-drops/hawking-approach-hover-40M-to-2.02M-10s.mp4` and the
stills `hawking-approach-r{40,10,4,2.5,2.1,2.02}M.png`: ray optics, honest for the short-wavelength tail
of the spectrum and stated as such. A static (hovering) observer descends from 40 M to 2.02 M looking
straight down and straight up. Every direction traced backwards either came from the horizon, carrying the
Hawking glow (uniform: a blackbody at T_H / sqrt(1 - 2M/r), the same in every direction for a static
observer), or from infinity, carrying nothing but starlight, lensed and blueshifted (the Unruh state, an
evaporating hole in empty space: exactly the owner's "no background"). The border is the escape cone,
sin(psi_e) = (3 sqrt3 M / r) sqrt(1 - 2M/r), analytic and confirmed by the tracer on every frame. So THE
GLOW IS THE SHADOW: the disc that is black under external light is precisely the set of directions that
carry Hawking flux, 7 degrees across at 40 M, half the sky at 3 M, and at 2.02 M everything but a 15-degree
cone straight up into which the whole universe is compressed, Einstein rings at its rim. The colour runs
orange-red (2000 K) through white (4900 K at 2.4 M) to blue-white (20,100 K at 2.02 M) while the camera's
exposure drops 17 stops (the caption counts them; the stars are drawn at fixed brightness with their true
colour shift, or they would vanish within a few M). The thrust to hover ends at 2.46 c^4/GM, 5e23 g, and
there the glow's temperature T_H / sqrt(1 - 2M/r) tends to a / 2 pi: the hovering observer's thermometer
reads the Unruh temperature of its own acceleration; at the horizon Hawking's radiation and Unruh's are one
thing. The glow is a blackbody, not the greybody spectrum: the filter is the barrier at 3 M (a hoverer
inside it sees the unfiltered flux) and the filter is the wave effect that forbids the picture's sharp
edge; the blackbody is the one spectrum consistent with ray optics. Not rendered: the free-falling
observer (what a falling detector clicks is a literature of its own; the naive Doppler bookkeeping gives a
finite mild temperature and is not the whole answer). (2) `hawkmode.py` ->
`hawking-mode-dipole-quadrupole-10s.mp4` and `hawking-mode-frame120.png`: the thing ray optics cannot draw,
the mode itself. The l = m = 1 photon mode at the peak frequency in the equatorial plane,
Re[psi(r*) exp(i(phi - w t))], flux-normalised, born at the horizon with unit amplitude, 41% transmitted
through the barrier and 59% reflected (a near-standing wave inside 3 M), a spiral wave outside with a
wavelength thirteen times the horizon; beside it l = m = 2 at the same frequency, trapped (Gamma = 0.0004).
Near the horizon the crests pile up (r* -> -infinity) and peel off at the coordinate speed 1 - 2M/r: the
trans-Planckian side of Hawking's derivation, to scale. `hawking-spectrum-chart.png` has the greybody
factors and the spectrum against the blackbody it is usually drawn as. Scripts and logs in
`claude-handoff/d3/reading-alpha/blackhole/`; numpy only, minutes on one CPU.

### Snap is readable, and the family's derivative ceiling is snap (2026-09-08)

Preparing the Metal demo's next round, the owner asked for "human-reading fields for any relevant fields
missing (jerk - snap - crackle - pop - whatever)". Two answers, one structural and one measured.

**The ceiling is degree four, and it is not where the window sizes suggest.** N frames give N-1 links and a
polynomial with N-1 coefficients, so five frames could carry snap and six crackle. The quint does fit an
exact quartic through its four links and solves the snap row, using it only as an alarm. The sext does NOT
fit a quintic: it fits a quartic again, by weighted least squares over up to seven points (six links plus
the anchor), spending its sixth frame on overdetermination rather than another order, and the leftover
becomes the fit's per-texel RESIDUAL. That was the deliberate choice the seven-frame analysis argued on
paper. So crackle and pop exist nowhere in this family and cannot be read without a new estimator, while
snap is already computed twice and discarded, and the sext's residual is a confidence map that is already
computed and never shown.

**Snap reads far better than the noise model predicts.** Pre-registered
(`tests/probes/snap/PREDICTION.md`): each order should cost about 2.9x in signal-to-noise (the
signal falls by the per-frame angular frequency, 0.65 on the test scene, while the fourth difference
amplifies independent link noise by sqrt(70)), putting snap at 2-5 where jerk sits near 10. Measured on
O5_osc_textured, the field-calibration scene, through the quint's machine modes at N:N, against the analytic
derivatives (a scratch variant hoists the snap row out of the solver and paints it as mode 10):

    acceleration  FS 16  gain 0.996  correlation 1.000  residual 0.071 px/frame^2   peak/residual 121
    jerk          FS 8   gain 0.895  correlation 1.000  residual 0.047 px/frame^3   peak/residual 118
    snap          FS 8   gain 0.927  correlation 0.997  residual 0.179 px/frame^4   peak/residual  20

The acceleration row is the instrument checking itself against a field the record calibrates independently.
Snap comes in at 20:1, not 2-5. THE PREDICTION'S ERROR IS THE INTERESTING PART: it assumed each link's error
was independent. On a large, well-textured object in smooth motion the estimator's sub-pixel bias is
phase-locked to the texture and travels WITH the object, so it is common to every link and CANCELS in the
differences instead of adding — the same peak-locking bias that ADDS in the even orders on a static scene
(the Metal demo's measured 0.52 px acceleration floor). Snap costs about 6x jerk's signal-to-noise here, not
the 8-30x an independent model gives. The caveat stands: 20:1 is a strong, smooth, well-textured motion, and
ordinary content will sit far closer to the noise.

A first attempt measured on O2_osc_medium, a FLAT square, and read the acceleration field at gain 0.035 —
a flat interior has no features, so the field inside it is whatever propagation fills in. Field measurements
go on the textured scenes, at a full scale above the peak truth, and with the noise taken as the residual
after fitting a gain (on a flat background the floor measures exactly zero).

**What each shader costs, measured on one machine in one pass** (720p, 24 -> 60, 120 output frames, an ffv1
file source interleaved over three rounds, `-f null`, RX 6600; the first such table for the whole family):

    linear 14.1 ms/frame (1.00x)   base2 22.2 (1.57)   prop2 24.7 (1.75)   vp2 29.9 (2.11)
    tri 39.6 (2.80)   quad 45.5 (3.22)   quadp 53.1 (3.76)   quint 66.6 (4.71)   sext 79.2 (5.60)

And an eight-shader reference ladder over all 42 synthetic cases is in
`np-scratch/metal-prep/ladder-refs-table.txt`. Two things in it are new: the two-frame shaders collapse
BELOW HOLD on structure crossed by motion (V1/H1/V2 at 15-19 dB against hold's 18-24), which the aperture
series predicted and no table had shown side by side; and the recommendation is not uniformly best, losing
to the propagated four-frame family across the oscillation set while winning on the translation and stairs
cases. Both are arguments for the demo's shader drop-down: they are visible only by switching shaders on one
clip.

### The held anchor: where the reading was standing, and a control that could not be used (2026-09-09)

The M-series trip left one defect open, and it is the best specimen of a silent error this project has
produced. The diagnostic field is built about an ANCHOR slot, naturally the straddling frame nearer the
output; that flips within one window as the phase crosses 0.5, and the two slots carry flow stencils with
independent sub-pixel noise, so a live display strobes between two decorrelated fields. `DIAG_HOLD_ANCHOR`,
which the reading tail sets, stops the strobe by pinning the anchor to a LITERAL slot index. A literal is
only correct for the window it was chosen against, and the window rule was corrected on the Mac.

**Where the reading was actually standing**, found by a probe that reads none of that logic and so cannot
inherit its assumption (`tests/probes/anchor/phaseprobe.py`): render an oscillation, decode the field over the
object, sweep an assumed measurement offset and correlate against the analytic derivative. The offset of
maximum correlation is the instant the reading reports.

    shader   rate      acceleration delta, before -> after      velocity delta (control)
    quad     24 -> 24      -1.00  ->  -0.00                        +0.50  (unchanged)
    quad     24 -> 60      -0.60  ->  -0.40                        +0.10  (unchanged)
    quint    24 -> 24      -0.00  ->  -0.00                        +0.50  (unchanged)
    quint    24 -> 60      -0.00  ->  -0.00                        +0.10  (unchanged)
    sext     24 -> 24      -0.50  ->  -0.50                        +0.50  (unchanged)
    sext     24 -> 60      -0.15  ->  -0.15                        +0.10  (unchanged)

The arithmetic reproduces the quad's two numbers exactly, which is why the diagnosis is believed rather than
guessed. At 24 -> 60 the phase cycles through {0, 0.4, 0.8, 0.2, 0.6}; at every interior phase the window is
[-1, 0, +1, +2] so the lower straddler is slot 1 and the held anchor sits at -phase, but at phase 0 the
window shifts to [-2, -1, 0, +1] and the lower straddler becomes slot 2 while the anchor stays pinned to 1 —
a whole interval early. The mean over the five phases is -0.60, and at N:N every frame is phase 0, so -1.00.
The fix names the lower straddler from the window instead of by a literal, `anchor = clamp(p, 1, 2)`, which
is still a function of the window alone and so still cannot flip within one.

**The commit's proposed scope was too wide, and measurement is why.** It proposed pinning to the lower
straddler in all 25 shaders. Only the four-frame family needs it. The QUINT already reads at 0.00 at both
rates: its own window shifts at phase 0.5, so a fixed slot IS the nearer straddler at every phase and the
switch happens on a window advance rather than within a window — pinning it to `p` would have made it worse,
about -0.40. The SEXT's -0.50 at N:N is not a defect either but its own documented definition, the centred
fit reporting at the weighted centre of its points, "half an interval before the anchor at N:N" in the
shader's own words. Five shaders changed, two occurrences each; the quint and sext untouched.

**The residual is the price of not strobing, and is stated rather than hidden.** -0.40 at 24 -> 60 remains
because the lower straddler is behind the output by the phase, and no window-constant slot can track the
nearer straddler when the window does not itself shift at 0.5 — the four-frame family's situation, not the
quint's. Two honest options: accept a known lag on a display, or evaluate the fitted cubic at the output
instant rather than at the anchor (`a_out = a_anchor + jerk * (-rts_mix[anchor])`), which would remove the
offset using a quantity the shader already computes. The second changes what the field MEANS across three
families and is left on paper.

**A CONTROL THAT COULD NOT BE USED, which is the wider lesson.** The plan was to prove the picture path
untouched by rendering it before and after and comparing bytes: the edited line is guarded by
`TRI_DIAG != 0`, so an ordinary interpolated render cannot reach it. The bytes differed. Two runs of the
SAME shader are byte-identical, so the comparison was sound; and then a SEMANTICALLY NULL edit — writing the
original behaviour as `clamp(1, 1, 2)` instead of `1`, still dead code — produced the identical difference:
2 samples out of 110,592,000, one frame, at most 16 parts in 65535. So the picture path is not byte-stable
against recompilation at all, and a byte-compare is not available as a control for any shader edit here. The
cause is the near-tie sensitivity the macOS investigation identified as platform-independent: the block match
selects an argmin, and one bit of difference in a cost comparison flips a vector outright. On this platform
it surfaces as two texels rather than the fourteen frames it caused there. The usable control is a magnitude
bound, not equality.

Verified besides: all four quad shaders and `human-reading-quad.glsl` regenerate byte-identical from the
edited generator, and `tests/smoke.sh` passes 15 of 15. For his eyes:
`hot-drops/reading-anchor-before-after-24fps.mp4`, the painted acceleration at N:N with the old anchor on the
left and the new on the right.

The Metal app picks this up whenever its Metal shaders are regenerated from this GLSL; nothing in the app's own code changes.

### Has animation work polluted the general shaders? Audited and measured (2026-09-09)

The owner's question: a great deal of work went into animation before it was split into its own class, so
have fixes meant for the cartoon case been left applied to film, where they are wrong? Audited through the
history and then measured. **The answer is no, and in the one place the suspect feature is fully present it
is load-bearing for content that has nothing to do with animation.**

**Four things entered the general path from animation work.** Traced to their commits and to what each was
gated on at the time.

- FLOW PROPAGATION (`ea0c725`) was motivated by "the fast tier's loss on flat-shaded line art is on the
  edges (aperture), not in the fills" -- and shipped measured up on everything: ladder mean +0.66, the
  avengers clip 34.74 -> 35.24, five library segments +0.4 to +2.0. An animation problem that produced a
  general improvement. It is the base of the current recommendation.
- THE COARSE VECTOR MEDIANS (`bd92eea`) were added explicitly to fix a cartoon face defect. The marginal
  case, and the subject of the measurement below.
- THE SNAP CHECK'S EDGE GATING was found on a cartoon (Bluey's ear outlines fragmenting) and the design
  consciously avoided this very trap: rather than blending globally, "which softens this everywhere to fix
  a problem that only happens in specific spots", the fix is gated to edges by EDGE_A/EDGE_B.
- THE SCENE-CUT THRESHOLD (0.125) was chosen across three clips including flat animation, but the BINDING
  constraint was the bright-action clip, whose highest non-cut reading is 0.1224. Film set the number.

The `-animation` fork itself is clean: it differs from the general propagated base by one constant
(`PROP_DISAGREE` 0.75 against 1.5).

**The medians are barely in the recommendation.** `bd92eea` added them at S, E and Q. The recommendation
(`-variational-propagated`) is generated with `0,0,2,0` -- the Q pair only -- because its cascade starts at
Q. Regenerating it with `0,0,0,0` and rendering the flow field through `flowvis.py`: **2 pixels out of
104,140,800 differ, by one quantisation step, on the cartoon; ZERO on live action.** That is consistent with
the commit's own argument, which is that the mouth island is 11 texels at H, 5.5 at Q, 2.8 at E and 1.4 at S
and that a 3x3 median cannot remove an island bigger than itself: the two levels that did the work are the
ones the recommendation does not carry. On the ladder the pair is worth +0.025 dB mean (helps 14, hurts 9),
and on film nothing at all: avengers 42.47 / 42.46, back to the future 34.30 / 34.28, the cartoon
30.04 / 30.01.

CAVEAT ON THAT FLOW COMPARISON: `flowvis.py` encodes +-10 px in 8 bits, so one step is 0.078 px -- the same
scale as the flow differences that move a 65 dB ladder case by a decibel. It can say the flow is unchanged
at its resolution; it cannot say the picture is.

**In the full variational, where the feature lives, it is load-bearing and not for animation.** `2,2,2,0`
against `0,0,0,0` (123 passes against 111), whole ladder and both content types:

    ladder mean, removing the medians          -0.841 dB   (helps 16, hurts 17, neutral 9)
    what removing them COSTS      A4_accel_tex_a033 -7.88   A6_accel_tex_a133 -5.63
                                  P3_stairs_along_v12 -4.52  P5_stairs_along_v8_alias -4.52
                                  O6_osc_tex_gentle -3.53   P2_stairs_along_v8 -3.49
    what removing them GAINS      L6_flat_large +2.16   L3_trans_23px +1.36   L4_trans_40px +0.95
                                  L2_trans_16px +0.73   A2_accel_16mean +0.60
    cartoon (bluey, 5 segments)   29.94 -> 29.58 dB, SSIM 0.9688 -> 0.9677
    live action (avengers, 5)     42.63 -> 42.61 dB

So the medians are worth +0.84 dB mean on the ladder, +0.36 on the cartoon they were built for, and +0.02 on
film. THE LARGE GAINS ARE ON TEXTURED ACCELERATION AND THE APERTURE SERIES, neither of which is animation
content and neither of which existed as a ladder case when the feature was gated. A fix motivated by a
cartoon turned out to be general, and by a wide margin.

**The cost is real and is where the original commit said it would be.** The medians lose on flat, large and
fast: L6_flat_large -2.16, L3 -1.36, L4 -0.95, exactly the "clean trend with speed" `bd92eea` reported
(a median erodes a genuine motion boundary by a texel or two per pass, and the faster the object the more of
its area is boundary rather than interior). Those losses are larger than the -0.86 measured then, because
the trend was measured on a ladder that stopped at 40 px translation and did not yet contain the flat-large
or aperture cases. Render cost was not measured cleanly here (the first run of a fresh ladder pays for the
hold and linear baselines); the figure on record is +8.6% at 720p for twelve passes.

**Left open, deliberately.** The recommendation's cascade starts at Q, so it cannot carry S or E medians as
the variational does; whether an equivalent exists for it, and whether it would bring any of that +0.84, is
a question this audit raises and does not answer. Nothing was changed: the audit found nothing to undo.

### Jerk is not noise-limited, it is truncation-limited, and no sinusoid can show that (2026-09-09)

The owner's question: have we dug deep into jerk, given it sits barely above the noise floor? The answer is
that we have never isolated it at all, and that the thing limiting it is not the noise floor.

**No case in the ladder has a cubic term.** Every one of the 42 motion laws is a constant, a straight line,
a quadratic or a sinusoid. A quadratic has jerk of exactly zero. A sinusoid has jerk, but welded to
acceleration through one parameter: for x = A sin(w t), the derivatives are A w, A w^2, A w^3, so raising
jerk by raising w raises acceleration by w^2 and velocity by w. **Jerk has never been varied in this project
with anything else held still**, and the case that would do it -- a constant non-zero jerk, x = j t^3 / 6 --
does not exist.

**The sweep, on cases that already exist.** Four textured oscillations share their geometry exactly (a
300x300 TEX_M2 square at y = 210) and differ only in amplitude and frequency, which spans jerk about eight
to one for free. The reading tail's machine jerk and acceleration were scored against the analytic
derivatives at N:N, full scales raised so nothing clips (`tests/probes/jerk/jerksweep.sh`):

    case                 jerk px/f^3   gain    resid    jerk/resid   resid/jerk    accel jerk/resid
    O6_osc_tex_gentle       0.72       0.987   0.197       3.64         0.274         25.2
    O9_osc_tex_fast         2.91       0.805   0.731       3.98         0.251        123.2
    O10_osc_tex_tiny        4.59       0.761   1.460       3.15         0.318        171.6
    O5_osc_textured         5.61       0.898   1.201       4.67         0.214        102.9

**The signal-to-residual is FLAT at 3.1 to 4.7 across an eightfold range of jerk.** More jerk does not buy a
better reading. The residual instead scales WITH the jerk -- resid/jerk stays at 0.21 to 0.32 throughout --
and that is the signature of a systematic error proportional to the signal, not of an additive noise floor
that a larger signal would climb above. Acceleration on the identical clips reads at 25 to 172 to one,
twenty to fifty times better.

**The mechanism is finite-difference truncation, and the numbers say so.** A cubic through four equally
spaced samples estimates the third derivative by the third difference, which attenuates a sinusoid's true
third derivative by [2 sin(w/2) / w]^3 -- pure sampling arithmetic, no noise term. Predicted against
measured gain: 0.991 / 0.987 on O6, 0.948 / 0.898 on O5, 0.925 / 0.805 on O9, 0.871 / 0.761 on O10. The
slowest case matches to four thousandths; the faster ones fall further below the prediction, which is the
estimator's own trust gates and clamps adding to the arithmetic. The ordering and the direction are the
sampling's.

**So every jerk figure this project has ever measured is contaminated by the sinusoid's own higher
derivatives, and no oscillation case can ever separate the two.** That is what makes the missing cubic
decisive rather than merely absent. On x = j t^3 / 6 every derivative above the third is identically zero,
so a cubic fit is EXACT and the truncation term vanishes by construction: any residual measured there is
pure noise. It also sweeps acceleration linearly through zero inside the clip,
which isolates jerk at full strength with acceleration momentarily absent -- something no sinusoid does
except at an instant.

CORRECTED THE SAME EVENING, and the correction matters. The paragraph above first claimed that one such case
would decompose the 3-to-5 into truncation and noise. It cannot, and the reason is a design ceiling nobody
had noticed: with acceleration zero at mid-clip over 23 intervals the velocity swing is 72j, so j = 0.25
already runs velocity from 22 down to 4 px per frame and anything above about 0.28 reverses it. A constant-
jerk scene that stays inside the ~23 px coarse reach therefore cannot deliver more than a quarter of a pixel
per interval cubed -- twenty-one times BELOW O5's actual discrete jerk peak of 5.31, and nearly three times
below O6's 0.712. So the cubic is a third data point at a NEW and much lower jerk level rather than a
matched comparison, and at that level its own signal-to-floor is 2.5 to 5, the thinnest on the ladder. What
it can still do is test the complementary half of the truncation claim -- that a cubic fit to a cubic has
gain exactly 1.0, no attenuation at all -- against the sinusoids' measured 0.76 to 0.99. That is worth
having. It is not the decomposition that was claimed.

The same case was proposed independently by two of the eight angles of the 2026-09-09 case-design sweep
(clustered as "constant jerk, acceleration through zero"), before this measurement was made.

### The synthetic pool: 43 gaps found, and the bottleneck is not the scenes (2026-09-09)

The owner's argument, after the median audit: the value is in the synthetic cases because that is where the
answer is known exactly, and the risk is not that synthetic differs from real but that the space of possible
cases is unbounded while the pool is 42. A sweep was run to map it -- five parallel surveys of what the 42
isolate, what fails with no case exposing it, what the construction machinery can express, what real footage
does that the pool does not, and where the estimator must fail by design; then eight independent taxonomies
proposing cases against those surveys; then one agent per surviving mechanism required to write the ACTUAL
pasteable scenes.sh line, the closed form proving exact ground truth, and the closest existing case.

Sixty candidates, clustering to 43 distinct mechanisms. **Fourteen were reached independently by more than
one taxonomy**, which is the useful signal in the run: three separate angles arrived at divergence and zoom,
three at pure shear, three at acceleration perpendicular to velocity, and two each at parallax, constant
jerk, sustained sub-pixel velocity, a flash firing the cut gate, a static occluder, and opposed motion
without occlusion. Of the 39 fully build-checked, **39 pass: all buildable, all with exact ground truth, all
genuinely distinct** -- 33 as a single geq expression, 6 needing a second layer, and NONE needing
manifolds.py. One checker went as far as running scenecheck.sh on its proposed cubic and reported it
bit-identical over all twelve coincident frames.

**The finding is not the case list. It is that building a case takes minutes and READING it is the work.**
The checkers were asked for the strongest objection to building each case, and the same objection came back
in different words for most of them: the ladder's own instrument cannot see the mechanism. Whole-frame PSNR
over an object occupying a fraction of the frame will not show a parallax boundary, a superposed second
motion, a swarm's median erosion, a moat's propagation limit, or an intermediate-angle aperture. Several
cases would print a confidently wrong row if dropped into ALL_CASES as-is, because analyze.py's assumptions
about the rate do not hold for them. Others were shown to be already measured, or to confound the mechanism
they name with a second one moving at the same time, or -- in two instances -- to be arithmetically
degenerate on their own constants: a proposed highlight case works out to a null, and a proposed cut case
has the gate's statistic already above threshold on content that is not a cut.

That is the same lesson this project has now learned three times, most recently on the vector median: a
metric that cannot see the thing being judged does not get to judge it. It changes the shape of the work
from "write 43 scenes" to "for each mechanism, decide what reads it, and build that first". The scenes are
cheap and will keep; the instruments are the schedule.

**What follows for how the pool grows.** Cases whose mechanism the existing instruments already read --
whole-frame PSNR against exact truth, or the field checkers against an analytic field -- can be added
immediately and cost almost nothing. Cases needing a new statistic should wait for it, because a case that
cannot be read is worse than no case: it occupies render time on every future regression run and reports a
number that means nothing. And a case earns its place permanently, so the survivors shown to duplicate an
existing case or to confound their own mechanism should not be built at all, whatever their proposer claimed.

The material is in `np-scratch/cases/` (the surveys and JSON; the clustering is `tests/probes/cases/cluster.py`): the five surveys, all sixty raw
proposals, the 43 clustered mechanisms with their vote counts, and the build-checks, each carrying its
pasteable line, its closed form, and its objection.

### The gradient tensor's third component, and why its first two numbers were unfair (2026-09-10)

Lead E scored the velocity gradient tensor (read_view 9) against two exact gates: a flat disc expanding
0.6% a frame for divergence, and the rotating disc for curl. It never scored the FIRST SHEAR
(du/dx - dv/dy), and could not have: a rigid rotation has no shear and neither does a pure zoom, so the one
component that distinguishes a DEFORMING subject from a rigid one had no scene on the ladder that produces
it.

**A hyperbolic strain isolates it exactly.** Every point moves at u = K(x - cx), v = -K(y - cy), so the field
stretches in x and compresses in y at matched rates: divergence and curl are identically zero and the first
shear is 2K/fps everywhere. The forward map x(t) = cx + (x0 - cx) e^{Kt} is a closed form in t, so geq
samples its inverse and the ground-truth property holds. Scored on a textured field at K = 0.48/s, 24 fps
(shear 0.04 per frame, 7.6 px/frame at the edge of the scored region): **the first shear reads 0.0386 against
a truth of 0.0400 -- 96.4%, frame-to-frame spread 2.6%** -- with divergence and curl reading +0.0010 and
-0.0002, near enough zero, which is the built-in leakage control.

**The recorded 30-80% for divergence was a property of the SCENE, not of divergence.** That gate was a FLAT
disc with flows of well under a pixel a frame -- no texture to match and the smallest flows the estimator
will ever be handed, which is the hardest case for a small-flow floor. Putting all three components on ONE
construction -- the same 40 px texture, the same tensor magnitude of 0.04 per frame, the same 7.6 px/frame at
the region's edge, differing only in which component is non-zero -- gives the first comparable reading:

    scene       live component     truth      read    % of truth   frame sd   leakage into the other two
    expand      divergence        0.0400    0.0371       92.8%      0.0008    curl 0.0000, shear +0.0007
    rotate      curl              0.0400    0.0381       95.2%      0.0014    div -0.0037, shear -0.0002
    strain      first shear       0.0400    0.0386       96.4%      0.0010    div +0.0010, curl -0.0002

**All three read within 93 to 96% of truth, and cross-talk is under 10% of the live component in the worst
case and under 3% in five of the six.** The tensor is a working three-component instrument on content that
has texture and enough motion, which is a considerably stronger statement than the record carried before, and
it comes with the honest condition attached: the flat, sub-pixel case that produced the 30-80% figure is still
the flat, sub-pixel case, and nothing here repairs it.

What this opens is the class of DEFORMING subjects. One vector per block cannot say whether a plate of jelly
is wobbling or sliding; divergence, curl and shear can, and now all three are known to read to about five
percent. The scenes are `tests/probes/shear/shear.sh` and `matched.sh`, kept out of ALL_CASES deliberately --
they were built as gates for an instrument, and a case earns a permanent place on the regression ladder only
by informing a decision that recurs.

A note on the control, because it did not quite agree and that was useful. Scored on the rotating disc the
same scorer read curl at 85% where Lead E's inner bands read 95-99%. The record's own banding explains it:
the reading falls with radius and collapses past 0.7 R, so a single wide annulus is the area-weighted mean of
a declining profile. What the control established firmly is that the channels are not transposed -- the
rotation showed curl and essentially zero shear -- which is the failure that would have made the shear number
meaningless.

### Verb-object pairs generate cases a taxonomy cannot, and the rolling wheel proves it (2026-09-10)

The owner's suggestion, offered as a throwaway after the jelly: name a VERB and an OBJECT and see what falls
out. "Wobbling jelly." "Spinning dinnerplate" -- which resembles a disc but is concave. "Flapping bird" --
features that narrow to a line and yet definable wings.

Tested against the 43 mechanisms the eight analytic taxonomies produced the day before. **Five verb-object
pairs fall outside all 43:**

- ROLLING WHEEL -- rotation and translation LOCKED at omega = v/R, so one rigid body contains every speed
  from zero at the contact to 2v at the top, simultaneously.
- FLAPPING BIRD -- articulation: rigid parts hinged on a shared pivot, sharing a boundary. The list has
  several movers, and it has a crease, but nothing hinged.
- SPINNING DINNERPLATE -- the owner's own point: a flat plane turning gives AFFINE flow, which the list has;
  a concave one gives flow quadratic in position, which it does not.
- RIPPLING FLAG -- a wave whose phase velocity and material velocity are both non-zero and different. The
  list has a shadow over a static surface, the degenerate case where the material velocity is zero.
- WOBBLING JELLY -- a gradient tensor that VARIES IN TIME. Everything measured on the tensor the same
  morning was constant.

**Why the frame works, which is worth more than the five cases.** An analytic taxonomy decomposes along
independent axes -- motion type, structure, photometry, time -- and enumerates points in that space. A
physical object BUNDLES those axes into constrained combinations. Rolling is not a point in the space of
motions; it is a curve through it, defined by a lock between two axes that no axis-wise enumeration proposes,
because the enumeration has no notion that two axes might be tied. Taxonomy supplies dimensions. Physics
supplies constraints. That is the whole of it, and it is why an exasperated throwaway produced what a careful
eight-way sweep did not.

**The rolling wheel, built and measured** (`tests/probes/verbs/rolling.sh`). R = 150 px, v = 8 px/frame, so the
contact is at rest and the top runs at 16. The forward map is a rotation matrix in t composed with a linear
translation, so the ground-truth property holds. Truth along the vertical diameter is a straight line,
u = v - (v/R) dy, and the machine velocity reads:

    dy from centre    -120    -80    -40      0    +40    +80   +120
    truth px/frame   14.40  12.27  10.13   8.00   5.87   3.73   1.60
    read             14.47  12.08  10.16   7.94   5.83   3.64   1.39
    % of truth      100.5%  98.5% 100.2%  99.2%  99.3%  97.5%  86.9%

Leakage into the perpendicular component, which is exactly zero on this diameter, stays within 0.18 px/frame
throughout.

**So the reading holds between 97 and 100 percent of truth from 16 px/frame down to about 3.7, and has lost
13 percent by 1.6.** That is the small-flow floor, measured for the first time as a CURVE along a gradient
inside one rigid object, at one instant, with the same texture and the same body throughout -- no confound
from comparing separate scenes at separate speeds, which is how every previous statement about small flows
was arrived at.

It also explains a number recorded the same morning. The divergence gate reads only 30-80% of truth, and that
gate is a flat disc expanding 0.6% a frame: its flows sit well under a pixel a frame, deep inside the falling
region this profile maps. The gate's poor figure was never a property of divergence; it is this curve, seen
end-on.

### Weird geometry: what the readers make of fields that are not constant (2026-09-10)

The owner's request: "really weird forms of synthetic geometry". The morning's tensor gates were all constant
fields, one component live at a time, and the case survey's lesson was that a scene is worthless without a
reader that can see its mechanism. So the useful weirdness is scenes whose velocity AND gradient-tensor
fields are analytic and NOT constant, scored by the two readers that exist (read_view 4 velocity, read_view 9
divergence / curl / first shear). Five verb-object scenes, each a closed-form inverse map in T so the
ground-truth property holds (`tests/probes/weird/weird.py`, 1280x720, N:N at 24 fps, 48 frames, the first
20 skipped -- see below):

    spiral   z(t) = z0 e^{(a+ib)t}                       divergence and curl live at once, constant
    vortex   theta = theta0 + w(r) t, w Gaussian in r      curl and shear varying smoothly in space
    flag     y = y0 + A sin(kx - Wt), five wavelengths     a curl field sinusoidal in x; the crest moves at
                                                           W/k while the material moves at AW
    jelly    x = x0 e^{K(1-cos Wt)/W}, y = y0 e^{-...}     the first shear oscillating in time
    bird     two wings hinged on a static body             a curl that flips sign across a hinge

**What reads well.**

- THE BIRD'S CREASE IS RESOLVED TO ONE CELL. Along the wings' centre line the curl goes from -0.13 to 0 within
  16 px of the left hinge and from 0 to +0.13 within 16 px of the right one, with the body reading 0.000
  between. Median curl per wing 0.105-0.117 against a truth of 0.121-0.131 (85-90%), correct sign on each
  wing, and the wing velocities read at gain 0.95 / 1.00, correlation 0.93 / 0.99. Articulation -- rigid
  parts sharing a pivot -- is read at the instrument's native resolution.
- THE FLAG SETTLES PHASE VERSUS MATERIAL. At a wavelength of 640 px the crest crosses the frame at 27 px/frame
  while the material moves at 4. The estimator follows the material, gain 0.98, and never the crest, at every
  wavelength down to 80 px. The curl's spatial transfer function -- the first bandwidth figure the tensor
  instrument has had -- is flat to within ten percent:

      wavelength px    1280    640    320    160     80
      v gain          0.983  0.976  0.972  0.950  0.956
      curl gain       0.985  0.977  0.971  0.935  0.895

  The curl channel's per-pixel noise floor is 0.02-0.03 per frame; its correlation rises from 0.58 to 0.98
  across the sweep only because the truth grows against that fixed floor.
- THE JELLY'S TIME-VARYING SHEAR TRACKS AT 0.9995. Per-frame median first shear against 2K sin(Wt)/fps:
  correlation 0.9995, gain 0.968, with a lag of +0.60 frames -- the same measurement-instant offset the phase
  probe found for velocity at N:N.
- THE READING TAKES TWENTY FRAMES TO SETTLE on a field that changes everywhere. The spiral's velocity
  residual falls from 12 px/frame at frame 8 to 0.6 at frame 20 and stays there; skipping only 8 frames had
  polluted every score. All figures here skip 20.

**What fails, and the shape of the failure.**

The vortex and the jelly fail PER PIXEL: velocity gain 0.4-0.65, correlation 0.3-0.5, residual 4-6 px/frame
on truths of 3-5. The failure has a shape. The median pixel is right -- direction error under 5 degrees,
speed error under 0.4 px/frame -- and a minority of ten to twenty-five percent lock onto a wrong vector,
often reversed (the 90th percentile of direction error is 106 degrees on the vortex and 146 on the jelly)
and up to ten px/frame too fast, with none reading zero. The jelly's failure tracks its instantaneous strain
rate: 0.5 px/frame residual where the strain passes through zero, 9 at its peak. The vortex fails outside
r = 80 from the first settled frame regardless of how far the texture has wound; the core, at 2.5 px/frame,
reads to 0.5. Because the per-frame MEDIAN of the tensor is right while the per-pixel field is wrong, the
jelly's time-tracking figure above is real and its per-pixel shear correlation (0.15-0.22) is also real.

**The texture was not the mechanism, and the test that showed it caught a silent failure first.** The scenes
were rerun on the ladder's aperiodic five-sinusoid texture to separate "deformation defeats the matcher"
from "a periodic lattice aliases under deformation". The first pass returned numbers identical to four
decimals to the periodic run -- 0.988 / 0.995 / 0.4283 on the spiral in both -- which is not a coincidence
but a scorer that had rendered the new frames and then loaded the old ones: the texture suffix was applied
in the render path and not in the load path. Caught by the identical-numbers rule, fixed, rescored:

                      periodic lattice (40 px)          aperiodic five-sinusoid
      spiral   u/v    gain 0.99 / 1.00, corr 0.995     gain 0.44 / 0.83, corr 0.30 / 0.81
      vortex   u/v    gain 0.59 / 0.58, corr 0.37      gain 0.61 / 0.66, corr 0.48 / 0.53
      jelly    u/v    gain 0.38 / 0.38, corr 0.28      gain 0.51 / 0.56, corr 0.48 / 0.35

So the non-affine scenes fail on both textures, and texture shifts them by a tenth. The spiral is the
surprise: a uniform rotation-and-dilation reads to one percent on the coarse lattice and to 0.44 on the
fine aperiodic texture, whose components are 5-8 px wavelengths that the coarse pyramid levels barely see
and that the dilation moves through the aliasing band. Texture scale and deformation interact, and that
interaction is unmeasured beyond these two points.

**The mechanism of the non-affine failure is open.** What is established: it is not the texture's period;
it is not winding (the vortex fails before it winds); it scales with the strain rate; it is a minority of
pixels locked to wrong vectors, not a broad scatter. Candidates in order of cheapness to test: which pyramid
level the wrong vectors come from (a raw per-level debug view scored against the same truth); a strain-rate
ladder of the jelly, K swept, to get the failing fraction as a curve; a shallower vortex; and the
texture-scale by deformation cross. The harness is written and each of those is a parameter change.

What follows for the family: articulation, transverse waves, and a similarity motion on coarse texture are
in reach of the estimator as shipped, and the tensor reads them to within a few percent; smooth non-affine
deformation -- a real jelly, a real vortex -- is not, and a picture that looks plausible on such content is
carrying a field that is wrong at one pixel in five. That is the honest boundary of "deforming subjects are
supported", drawn one day after the sentence was written.

### The non-affine failure: a cliff at a fixed velocity gradient, entering at the coarse search (2026-09-10)

The three cheap tests named in the previous section, run the same afternoon. Two of them are one design.

**The strain-rate ladder.** The jelly's K and the vortex's core rate each halved four times from the
failing values (`tests/probes/weird/weird.py`, LADDER=1). Expressed as the peak velocity gradient per frame
-- K/24 for the jelly, w0/24 for the vortex -- the two geometries agree on where the cliff is:

    scene            gradient /frame   failing   gain (u)   corr (u)
    jelly  K 0.045       0.002            0        0.91       0.98
    jelly  K 0.09        0.004          0.000      0.93       0.99
    jelly  K 0.18        0.008          0.003      0.94       0.975
    jelly  K 0.36        0.015          0.165     -0.76      -0.31
    jelly  K 0.72        0.030          0.143      0.38       0.28
    vortex w 0.15        0.006            0        0.91       0.95
    vortex w 0.3         0.013          0.042      0.83       0.59
    vortex w 0.6         0.025          0.104      0.84       0.34
    vortex w 1.2         0.050          0.213      0.59       0.37

("failing" is the fraction of samples whose read direction is more than 45 degrees off the truth, among
truth speeds above 1 px/frame.) Below a gradient of about 0.008 per frame both read at gain 0.9 and
correlation 0.95 or better. Above about 0.013 both fail. The jelly goes from 0.3% failing to 16.5% between
K = 0.18 and 0.36 with nothing in between, and at K = 0.36 the whole field reads REVERSED on average, gain
-0.76: at that rate it is not a minority locking to a wrong vector, it is the majority. A hard threshold at
a fixed gradient with a reversal at its onset is a much stronger constraint than the previous section had.

**Which level it enters at.** `levels.py` exposes the shader's own flow at each pyramid level by the flowvis
trick (the final pass rewritten to dump FLOW_S_AB, FLOW_E_AB_RAW, FLOW_E_AB, FLOW_Q_AB or FLOW_H_AB, scaled to
full-resolution px), scored against the same truth. The spiral is the units check and the control:

    scene          level     gain u/v        corr u/v      failing
    spiral         S (1/16)  0.83 / 0.94     0.91 / 0.95    0.056
                   E raw     0.93 / 0.98     0.95 / 0.98    0.031
                   E         0.94 / 0.98     0.98 / 0.99    0.003
                   Q         0.95 / 0.99     0.98 / 0.99    0.006
                   H (1/2)   0.99 / 1.00     0.99 / 1.00    0.005
    jelly K 0.72   S        -0.22 / -0.30   -0.14 / -0.13   0.623
                   E raw     0.11 / 0.29     0.07 / 0.11    0.413
                   E         0.24 / 0.34     0.19 / 0.17    0.291
                   Q         0.48 / 0.58     0.35 / 0.28    0.203
                   H         0.52 / 0.60     0.36 / 0.29    0.168
    vortex w 1.2   S        -0.13 / -0.15   -0.07 / -0.08   0.805
                   E raw     0.37 / 0.36     0.18 / 0.17    0.453
                   E         0.41 / 0.40     0.26 / 0.26    0.347
                   Q         0.59 / 0.59     0.35 / 0.35    0.230
                   H         0.59 / 0.59     0.35 / 0.35    0.202

On the similarity motion the pyramid does what a pyramid should: each level refines the one above, 0.83 at
the coarsest to 0.99 at the finest, failing fraction 5.6% down to 0.5%. On the non-affine scenes **the
coarsest level is already wrong, and wrong in sign**: FLOW_S_AB reads with negative gain and 62-80% of
its vectors more than 45 degrees off. Every finer level repairs part of that -- 62 to 41 to 29 to 20 to
17% on the jelly, 80 to 45 to 35 to 23 to 20% on the vortex -- and the last fifth is never recovered. So
the mechanism is located: **the failure enters at the coarse search at 1/16 resolution and the fine levels
cannot climb out of it**, because a reversed coarse seed is further from the truth than any refinement
radius reaches. The zero seed, which exists precisely to let the fine levels also try from rest, is what
lifts the recovery from wherever it would otherwise stop to the 80% seen here; it cannot lift it further.

**Why the coarse level reverses, and why the aperiodic texture reversed the spiral's fortune.** At 1/16
resolution the ladder's 40 px lattice is 2.5 texels, at the edge of Nyquist, and the aperiodic texture's
components (5 to 36 px) are all at or below it. A rigid or similarity motion moves an aliased pattern
consistently, and the coarse match, though aliased, seeds the fine levels near enough; a strain changes
the pattern's period between frames, and a periodic pattern near Nyquist whose period changes appears to
move the wrong way -- the wagon-wheel effect, in the coarse search. That is consistent with everything
measured (the threshold at a fixed gradient, the reversal at onset, the coarse level's sign, the fine
levels' partial recovery, the spiral reading to 1% on the lattice and 0.44 on the fine texture whose
components the coarse level cannot see at all). It is a mechanism consistent with the data, not yet a
demonstrated one. The demonstration is cheap and named: the same ladder on a texture whose period stays
above the coarse level's Nyquist under the largest stretch (80-160 px), which should move the cliff, and
the coarse search's window against the gradient, which should set where.

What follows for the family stands as written a section earlier, now with a number on it: a smooth
deformation whose velocity gradient exceeds about one percent per frame puts the coarse search into a
regime it cannot report, and the picture path is carrying a field wrong at one pixel in five from that
point on. Below that gradient, deforming subjects are read as well as rigid ones.

**Demonstrated, the same evening.** The same ladder on the same lattice at a 120 px period -- 7.5 texels at
the coarse level, above its Nyquist even under the jelly's full 1.58 compression -- with nothing else
changed (`TEX=M2W LADDER=1`):

    scene            40 px lattice: failing / gain u / corr u     120 px lattice: failing / gain u / corr u
    jelly  K 0.18         0.003 / 0.94 / 0.975                        0.005 / 0.96 / 0.97
    jelly  K 0.36         0.165 / -0.76 / -0.31                       0.003 / 0.96 / 0.99
    jelly  K 0.72         0.143 / 0.38 / 0.28                         0.005 / 0.96 / 0.99
    vortex w 0.3          0.042 / 0.83 / 0.59                         0.028 / 0.93 / 0.95
    vortex w 0.6          0.104 / 0.84 / 0.34                         0.015 / 0.89 / 0.95
    vortex w 1.2          0.213 / 0.59 / 0.37                         0.052 / 0.85 / 0.92

The cliff is not moved; it is gone. The jelly at K = 0.36, which read reversed on the 40 px lattice, reads at
gain 0.96 and correlation 0.99 on the 120 px one, and at twice that rate the same. The vortex at its
harshest goes from a fifth of its vectors wrong to a twentieth. So the mechanism is the coarse level's
wagon-wheel reversal of a near-Nyquist lattice whose period a strain changes between frames -- and the
"practical number" three paragraphs up must be restated, because it was a property of the test texture,
not of deformation:

**A deforming subject is read as well as a rigid one, at three times the gradient that failed before,
provided the content has structure the coarse level can see.** What fails is content whose dominant
period sits near the coarse level's Nyquist -- about 40 px at this frame size -- when it is stretched or
sheared by more than about one percent per frame. That is the ladder's M2 texture, which was chosen for
the period-40 case precisely because it is a trap: today's non-affine failure is the period-collapse family
that the zero seed was built against, met on content the seed can rescue for rigid motion and cannot for a
strain. Real footage carries structure at every scale and the coarse level locks to its coarsest, so the
one-pixel-in-five figure belongs to single-frequency content near 40 px, not to jelly.

### Content drawn on twos: the family collapses to a hold, and the cadence is the prize (2026-09-19)

**The question.** The owner, returning to the shaders after the player shipped: *"We have shelved the animation
interpolation project as being too difficult, however my gut says it must be possible because I know apps like
SVP can do it. So it must be possible and we must be missing something - or our shaders are alien to their
closed-source methodology. The key question is how are other player apps able to generate varied interpolated
content including cartoon/anime whereas ours struggles."* And the method he set: sample varied content, find
sequences with detectable error that are not cuts, and *"when trying to fix a fault reductively crystallise it
in to a synthetic test and solve on the deterministic synthetic data before working on the real source."*

**What the record already knew** (`shaders/animation/ANIMATION.md`): the redrawn feature has no correspondence,
and that limit is not crossed here. What it had not measured is the other thing anime does: it is drawn at
twelve (or eight) drawings a second and delivered at twenty-four, every drawing held for two or three frames.
`screen.sh` has always screened such segments OUT of the decimate-and-reconstruct bench, because a deleted
duplicate is reconstructed perfectly by hold and the bench cannot score it. The ladder can: its truth is the
scene's motion, and the native 60 fps render of a continuous motion is the exact answer for ANY source of it.

**The instrument: `tests/probes/twos/twos.sh`.** One scene, one 60 fps truth, three sources -- the scene at 24 fps
(the ladder as it is), the scene at 12 fps with every frame doubled to 24 (what an on-twos file does to us),
and the scene at 12 fps (the ceiling a perfect duplicate remover would hand the shader, 5x with doubled
motion) -- through hold, linear, the recommendation and the quad-propagated. Then two more: the doubled source
with ffmpeg's own duplicate dropper in front (`select` on its scene score; this build has no `mpdecimate`), on
exact duplicates and on a real encoder's near-duplicates (an H.264 file of the doubled source). PSNR Y, the
hook's passthrough instants excluded as `analyze.py` excludes them.

    L1_trans_8px                    ones 24->60   twos (12x2)->60   dedup 12->60   dropper   lossy   lossy+dropper
    hold                                 32.78            29.59          29.59       29.59   29.59          29.59
    linear                               35.44            31.18          31.99       31.99   31.18          31.99
    variational-propagated (rec.)        63.99            31.82          49.79       49.00   31.98          49.08
    quad-propagated                      67.06            32.58          57.83       59.48   32.42          55.15

    A5_accel_tex_a067
    hold                                 36.57            31.42          31.42       31.42   31.00          30.99
    linear                               42.71            33.92          36.10       36.10   33.54          35.81
    variational-propagated (rec.)        53.24            34.61          46.10       46.10   34.19          45.42
    quad-propagated                      52.82            35.29          50.10       50.16   35.08          46.92

    (ones / twos / dedup only)      V2_stairs_sq24_v6        R3_rot_tex            O5_osc_textured
    hold                            18.19 / 15.64 / 15.64    28.53 / 25.20 / 25.20  31.33 / 27.71 / 27.71
    linear                          21.48 / 17.29 / 18.44    32.60 / 26.65 / 27.38  33.90 / 27.48 / 26.78
    variational-propagated (rec.)   28.82 / 16.68 / 26.59    37.83 / 26.47 / 28.01  42.27 / 28.12 / 27.05
    quad-propagated                 27.67 / 17.57 / 17.73    37.30 / 26.38 / 27.84  48.69 / 26.93 / 26.66

    (a verifier's own runs, the same afternoon; rec. = variational-propagated)
                                    ones 24->60   twos (12x2)->60   dedup 12->60   dropper
    L2_trans_16px   rec. / linear     49.64 / 32.16   29.02 / 28.09     35.07 / 28.88   35.90
    L3_trans_23px   rec. / linear     40.89 / 30.53   26.75 / 26.48     28.61 / 27.26   28.62
    A6_accel_a133   rec. / linear     50.23 / 36.64   29.36 / 28.65     35.58 / 29.89   35.65

**The finding.** On content drawn on twos every shader in the family collapses to within a decibel of a frame
hold: the recommendation reads 63.99 dB on the 8 px translation delivered on ones and 31.82 on the same motion
delivered on twos, against hold's 29.59 and linear's 31.18. The estimator is not at fault -- the same shader
handed the twelve distinct frames reads 49.79, the quad 57.83 -- the SHADER IS INTERPOLATING BETWEEN TWO COPIES
OF ONE DRAWING (a hold) AND THEN ACROSS THE DRAWING CHANGE IN THE NEXT PAIR, so the output judders at twelve
holds and twelve moves a second however good the vectors. The prize of handling the cadence is 16.5 dB on the
translation (the quad 25), 11.5 on textured acceleration (the quad 15), 9.9 on the period-24 stairs for the
recommendation (the quad only 0.2: at the doubled 12 px/frame the quad locks onto the bars' alias, the
period-collapse family; the recommendation is immune, as shipped). The prize falls with speed as the doubled
motion passes the coarse search's reach (about 23 px/frame): 6.1 dB at 16 px/frame delivered on twos (32 at
12 fps), 1.9 at 23 (46 at 12 fps), 6.2 on the fast textured acceleration. Where the doubled motion is beyond the
family regardless -- the textured oscillation at twice its speed, the textured rotation -- there is nothing to
win (O5: dedup no better than twos). A duplicate dropper in front of the interpolator, with no change to any
shader, recovers essentially all of it: 49.00 against the 49.79 ceiling on exact duplicates, 49.08 on the
encoder's near-duplicates (a threshold of 0.002 on the scene score separates the synthetic file's duplicates,
0.000000-0.000004, from its moves, 0.0076).

**What the other players do, from the research of the same day** (sources in `shaders/animation/ANI-PRIOR-ART.md`,
"SVP and the cadence"): SVP's classical engine is a refactored MVTools2, the same hierarchical block matcher as
this family; its anime recipe is policy, not estimation (no blending, a search coarsened until only global
motion survives, retreat to original frames when the vectors are bad, SAD-masked overlay of originals), and
for content on twos it decimates UNCONDITIONALLY before interpolating ("Remove every other frame", a
`SelectEvery(2,0)`; its developer: "only for the simplest case", no cadence detection). Every offline anime
tool removes duplicates before interpolating (Flowframes' de-duplication, DAIN-App's `mpdecimate` modes,
Topaz's "Replace Duplicate Frames"). The television MEMC lineage detects the cadence from the pattern of frame
differences or the motion estimator's own statistics and interpolates across the true frame period. Nobody
solves the redraw inside the estimator; SVP's own developers say the anime artefacts can only be hidden.
So the answer to the key question, for the part of it that is measurable here: the gap is a CADENCE STEP we
lack, and behind it a fallback policy, not an estimation mechanism.

**Two things the real source taught, the same afternoon, before anything else is built.**
(1) On a real encode of real anime an absolute threshold is not the detector: in the on-twos stretches of the
    episode to hand the held drawings score 0.0056 on the scene statistic after the encoder and the small
    moves 0.0126, a ratio of two; and the pattern there is period THREE (a large change, a small one, a
    near-zero one), drifting in phase across cuts. The detector must read the cadence pattern, as the pulldown
    detectors do, and it must be bounded: a global dropper also drops every frame of a long static hold, and a
    blink after two seconds of stillness would then be smeared across those two seconds. A four-frame window is
    bounded by construction -- it can only re-time a duplicate run that ends inside it.
(2) On the libplacebo route the dropper cannot be a filter in front: libplacebo's frame queue builds each
    output's mix from the source frames within a radius of a RUNNING ESTIMATE of the source interval, and any
    interval deviating from that estimate by more than thirty per cent resets it (`frame_queue.c`,
    `update_estimate`, `max_delta = 0.3`). Regular spacing after the dropper (the probe's 12 fps) is fine;
    the irregular spacing of real cadence starves the window and the queue falls back to the nearest frame --
    a hold. A twenty-second render of the anime with a bounded dropper in front came out with MORE exact
    duplicate output frames than the untouched render (35 per cent against 15). So, for the hook: the re-timing
    goes INSIDE the window (the quad's window holds both copies and the next drawing; a hold pair warps slot 1
    to slot 3 at half the phase, a move pair at the other half), which is the next build, and `twos.sh` is its
    exact test. For the player, whose engine takes frames by index and computes the window's relative times
    itself (`QuadEngine.render`, `rts`), the cadence stage is a duplicate detector in the frame feed with true
    timestamps carried into `rts`, the same bound applied.

**The funnel, `tests/probes/dig/dig.sh`**, built the same day for the other half of his method: `prospect.sh`
finds estimator disagreement, which is not a visible fault; so each candidate is cut, decimated and
reconstructed, and ranked by the shader's margin over linear. Its first three windows: the anime opening's
credits over a dense cityscape pan -- 16 per cent of every frame a flow outlier, sustained for the whole shot
-- reconstructs 3.7 dB AHEAD of linear (41.57 against 37.84, SSIM 0.9896 against 0.9804, the lowest edge
error): a hard field, not a defect; the Pixar film's pointillist end credits -- linear ahead by 0.9 dB on
PSNR, the shader ahead on SSIM (0.9597 against 0.9345) and at edges (4.08 against 4.84): stipple punishes
any sub-pixel displacement and the blend of a near-static painting is nearly perfect, an instrument note, not
a defect; two windows of the live-action film uniform to the metric. The material needs the NAS: the one anime
episode to hand is a copy cut off at five and a half minutes.

**The pool, the same midday (the NAS mounted; `tests/probes/twos/cadence.py`).** How much of real animation is on
twos or threes, read from ffmpeg's frame-difference series with a RELATIVE rule (a frame is held when its score
is below 0.08 of the local level of change, the 80th percentile over two seconds; static shots reported apart),
four minutes from the middle of one episode per title:

    title (24 fps unless said)          static   of moving intervals: ones / twos / threes / longer   frames in twos-threes runs
    twelve anime titles                  14-87%   31-71% / 14-30% / 7-44% / 3-9%                    33-71% of moving frames
       (typical: Death Note, Re Zero,    34-40%   57-63% / 22-23% / 10-13% / 5-7%                   43-44%
        SAO, Violet Evergarden)
    Western TV animation (Avatar,        3-39%    37-63% / 20-44% / 7-20% / 9-12%                    33-53%
        Family Guy, Bluey)
    a 30 fps NTSC cartoon (Futurama)     6%       30% / 38% / 21% / 12%                              56%   (the telecine's own pattern on top)
    LIVE ACTION (Firefly), the control   0%       68% / 19% / 7% / 6%  at ratio 0.35;  91 / 8 / 1 / 0 at 0.08     16% at 0.08

A live-action episode holds nothing, so what the rule reads on it is its false floor: 27 per cent of moving
frames at a ratio of 0.15, 16 at 0.08, while two anime episodes read 50-53 and 44-45 -- the anime figure is
stable where the control falls, so 0.08 is the tool's default and 16 per cent the floor to read every figure
against. Read against it, roughly HALF of the moving frames of a typical anime episode, and a third to a half
of a Western cartoon's, sit inside a twos or threes run: the population the cadence step acts on. The tool is
the survey instrument, not the detector; the detector reads the pattern (periodicity), which is what takes it
below the floor.

**The funnel on the pool.** A live-action episode's most active minute (screened first) gave five candidates,
all reconstructed AHEAD of linear by 1.6-3.2 dB; two were behind at edges. The first is a hand-held pan across a
perforated lamp panel -- a periodic dot grid under camera motion, the period-collapse family in live action,
which the ladder holds as its M and V series (edge error 42.0 against linear's 40.1, PSNR 23.4 against 21.6 on
a scene that decimation puts beyond reach). The other straddles two cuts inside the clip's padding, and its
deficit (SSIM 0.9668 against 0.9741) is the cut frames, where the shader's cut gate holds and a blend half
matches: a bench artefact, not a fault -- the funnel should score away from cuts, which it does not yet. An
anime episode's middle minute was uniform to the prospector. The picture that emerges from three films and two
shows is the record's own: on film and live television the family is mature, and the mechanisms that show are
the ones the ladder already names; the material where it is not mature is animation, and there the largest
term is the cadence.

### The cadence branch: the prize taken inside the window, and the two things it cannot know (2026-09-19, afternoon)

The morning's finding was that content drawn on twos collapses every shader to a hold and that a duplicate
dropper in front recovers 16-25 dB; the afternoon put the step where the libplacebo route can have it, inside
the quad's window, and then into the player's engine ahead of any shader. The two are one idea measured twice.

**The branch.** `tests/gen_quaddirectional.py` with `CADENCE=1` in the environment emits
`shaders/quaddirectional-interpolation-propagated-cadence.glsl`: the quad with one branch in its final pass
(the shipped quad regenerates byte-identical without the variable). Interior windows only. Case A: the
straddling pair (slots 1, 2) is a held copy and slot 3 is the new drawing -- the output belongs to the span
from the first copy in the window (slot 0 if it too is a copy, else slot 1) to slot 3, and is warped plainly
between slot 2 and slot 3 with that pair's flow. Case B: the straddling pair is the change and slot 0 was a
copy of slot 1 -- the span began a slot earlier. Plain warps (a = j = 0), because the cubic assumes uniform
sampling of a continuous motion, which held copies break; never across a cut. The held-copy test is a new
statistic without a new bind: the three pair statistics the quad already carries (mean |A - B| over a sparse
24 x 24 grid of the coarse level, the cut gate's number) gain a second channel, the LARGEST |A - B| over every
texel of the coarse level (one bilinear tap per 16 x 16 cell), and a pair is a copy when that is under 0.02.

The first cut was refuted the same hour and is worth a sentence. It tested the mean statistic with a relative
rule (a pair is a copy when its mean is under 0.15 of the window's largest, and under 0.02): on the plain
8-px translation ON ONES it cost 14 dB (54.97 against 68.74), because the mean of a sparse grid fluctuates
pair to pair on a small moving object (0.0000, 0.0035, 0.0069 for the same motion, `tests/probes/twos/dupstat.py`)
and a ratio between fluctuations reads as a copy. The maximum over the whole level does not fluctuate (0.5 and
1.0 for the same pairs), and it survives the encoder: on the lossy file of the probe held pairs read 0.000-0.002
and moves 1.0.

**The gate, `tests/probes/twos/twos.sh`, twelve cases** (the quad, then the quad with the branch; PSNR Y against
the native 60 fps render; the threes source and the edge series added to the probe today):

    case                  ones            twos            threes          dedup           mpd (dropper)   lossy
    L1_trans_8px        67.29 -> 64.98*  32.77 -> 59.77  30.76 -> 36.99  57.62 -> 57.63  57.63 -> 57.61  32.49 -> 58.78
    L2_trans_16px       58.42 -> 61.35*  29.18 -> 35.43  26.90 -> 28.94  35.11 -> 35.46  35.46 -> 35.46  29.06 -> 35.15
    L3_trans_23px       43.21 -> 43.26   26.62 -> 28.56  25.42 -> 27.15  28.30 -> 28.30  28.30 -> 28.30  26.63 -> 28.69
    L9_occlusion        42.58 -> 42.65   28.97 -> 36.98  27.11 -> 30.01  35.93 -> 36.90* 36.87 -> 36.84  28.99 -> 37.17
    A5_accel_tex_a067   53.82 -> 53.66   35.23 -> 45.09  32.63 -> 38.12  50.10 -> 50.13  50.10 -> 50.10  35.08 -> 41.72
    V2_stairs_sq24_v6   27.70 -> 27.70   17.62 -> 22.15  16.20 -> 16.89  17.19 -> 17.73  17.73 -> 17.73  17.48 -> 20.59
    O5_osc_textured     48.72 -> 48.72   26.91 -> 26.75  25.29 -> 26.02  26.75 -> 26.75  26.67 -> 26.67  26.92 -> 27.11
    R3_rot_tex          37.28 -> 37.27   26.38 -> 27.21  26.17 -> 27.24  27.82 -> 27.81  27.81 -> 27.83  26.39 -> 26.94
    E1_edge_on_texture  25.52 -> 25.39   19.31 -> 20.46  19.52 -> 19.77  20.80 -> 20.80  20.80 -> 20.81  19.32 -> 20.45
    E2_cartoon_edge     38.83 -> 38.53   30.39 -> 34.95  30.64 -> 31.40  34.93 -> 34.37* 34.94 -> 34.94  30.40 -> 34.79
    E4_thin_lines       31.01 -> 31.03   26.74 -> 27.10  26.81 -> 26.86  27.22 -> 27.22  27.22 -> 27.22  26.76 -> 27.02
    O8_osc_fast_tiny    50.54 -> 43.86   39.73 -> 41.98  34.85 -> 34.84  41.95 -> 41.95  36.42 -> 36.42  39.58 -> 42.09
    (* the Mac ladder's own noise, below)

Read across: the twos column reaches the dropper row wherever the doubled motion is in reach (L1 59.8 against
the row's 57.6 -- above it, because the plain warp between two distinct frames beats the cubic's guess on a
12 fps source; L9 37.0 against 36.9; E2 34.95 against 34.94; L2 35.4 against 35.5), is short of it on the
accelerating object (A5 45.1 against 50.1: the branch warps plainly and the cubic's acceleration is not to be
had across a copy), is nil where the doubled motion is out of reach (O5, R3, E4, within 0.4 dB either way),
and the lossy column tracks the twos column everywhere, which is the statistic surviving a real encoder. The
threes column gains 0.7 to 6 dB, not the prize: the window's bound (case B sees the run's last two copies and
starts its span a slot late). The dedup and dropper rows do not move (no false fire under doubled motion), and
the ones column does not move beyond the ladder's noise -- except O8, which is the second thing below.

**The Mac ladder is not deterministic, and the propagation is where.** The ones control moved 2.3 dB under the
branch on L1, and the offline statistic said the branch never fires there (every pair 0.5-1.0 against 0.02). Three
runs of the PLAIN quad on the same source: 68.39, 68.67, 69.84 -- and frame by frame the difference is pairs of
consecutive output frames, the first two after a passthrough, falling from 64-78 dB to 45-49, at different
windows each run (frames 12-13 and 19; 17-18; none). The non-propagated quad and the plain variational are
deterministic to 0.02 dB and show the same pairs at 45-49 on EVERY window: the propagated family lifts them
and, at random windows, does not. So the noise is the propagation's -- the storage-cached flow read stale or
unwritten for that window, on the MoltenVK route -- and the Metal engine, which drives the same graphs with
its own command buffers, is deterministic to the hundredth (66.00 and 66.00; 68.71 and 68.71). Two consequences.
A control on the Mac ladder is read frame by frame or as the best of three runs, never as one run's mean to the
hundredth (best of three: quad 69.84, quad with the branch 69.81 on L1's ones). And the mechanism is an open
item on the Vulkan side, for a day with time: the "hook skipped" count is the same in every run, so it is not
the window; it is in the cache.

*2026-10-01: superseded: the Mac wander is two MoltenVK hazards rather than the cache, and with MoltenVK's two switches set one Mac run is a measurement again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), sections 2, 5-6 and 8).*

**The turning point sampled twice.** O8's ones column falls from 50.5 to 43.9, and that is not noise: the scene
is a sinusoid with six samples a period, and sin 60 = sin 120, so every third pair of its frames is an EXACT copy
by construction (8 of 23, `dupstat.py`: max 0.0000). Two identical frames are either a drawing held or a motion
that came back to the same place, and no statistic on the pair can tell them apart; nor can a pattern detector,
since O8's copies are periodic. The cost is bounded by the motion inside the re-timed span (here 1.4 px at the
peak instead of 0.5), and the coincidence is constructed: in the pool's live action exact copies occur only at
clip ends, and the nearest real thing -- the duplicate a 25-to-24 or 30-to-24 conversion leaves once a second
-- is a held frame, where the re-timing is right. Recorded as the branch's known cost, not fixed.

**The statistic on real encodes** (`dupstat.py`, the pool's clips; the value is the largest coarse-level
difference of each pair, the verdict at 0.02):

    anime, on twos (Fruits Basket)    the pattern H.H.H.H. through the second half; held 0.005-0.008, moves 0.03-0.3
    anime, on threes (Attack on Titan)   HH.HH.HH. and long holds; held 0.003-0.011, moves 0.81-0.87
    two anime clips on ones              no pair under 0.03 (a pan, a fight)
    six live-action clips                0.03-0.9; exact copies only at the clips' last frames; one clean static
                                         shot (a digital film, no grain) at 0.016-0.019 -- read as copies, harmless,
                                         since nothing moves across the span either way

The separation on animation is a factor of three to a hundred; the one place 0.02 is a near thing is a static
shot, where a wrong verdict changes nothing.

**The engine's stage.** The player's engine takes frames by index and computes the window's relative times
itself, so the cadence step there is not a branch in a shader but a stage in the frame feed: a frame that is a
copy of the one before it (the same statistic, one small kernel per new source frame, the maximum reduced on the
CPU), in a run of at most two copies, is left out of the window, and the window is chosen among the frames
that remain with their true times in rts -- the two-frame family then warps across the real span, and the
quad's window is four distinct drawings. Runs longer than two are holds and stay (the blink after two seconds
of stillness). Built into the private NFrameDemo tree's engine and the player's copy the same afternoon, with
the demo's `--cadence` flag and a checkbox, and the player's Settings toggle, on by default. Its exact test is
the probe's chain run through the engine (the private tree's `prep/cadence-check.sh`; ones, twos, threes
through the recommendation and the quad, stage off and on):

    case                  recommendation, stage off -> on          quad, stage off -> on                   ones (either, unchanged)
                          twos            threes                   twos            threes
    L1_trans_8px          31.79 -> 50.32  30.15 -> 41.28           32.83 -> 59.35  30.80 -> 43.31          66.00 / 68.71
    L2_trans_16px         29.21 -> 35.81  27.11 -> 29.40           29.27 -> 35.87  26.96 -> 29.46          51.16 / 61.48
    L3_trans_23px         26.81 -> 28.72  25.50 -> 27.59           26.69 -> 28.83  25.43 -> 27.60          41.88 / 44.04
    L9_occlusion          28.79 -> 37.57  27.41 -> 31.16           29.16 -> 37.45  27.12 -> 31.12          44.53 / 43.07
    A5_accel_tex_a067     34.59 -> 46.15  31.57 -> 40.67           35.30 -> 50.69  32.56 -> 47.99          53.72 / 54.44
    V2_stairs_sq24_v6     16.65 -> 26.37  16.07 -> 17.93           17.39 -> 17.57  16.17 -> 17.54          27.39 / 26.69
    O5_osc_textured       28.20 -> 26.85  25.47 -> 26.14           26.82 -> 26.56  25.28 -> 26.22          42.41 / 49.00
    R3_rot_tex            26.39 -> 28.06  26.14 -> 27.66           26.30 -> 27.70  26.11 -> 27.47          37.87 / 37.26
    E2_cartoon_edge       31.12 -> 34.05  30.71 -> 31.16           30.33 -> 34.89  30.63 -> 31.39          39.19 / 38.69
    O8_osc_fast_tiny      39.59 -> 43.13  34.87 -> 34.87           39.94 -> 42.71  34.87 -> 34.87          48.85 -> 43.70 / 50.18 -> 48.14

The ones column is unchanged to the hundredth on every case but the turning-point scene (no frame of a ones
source is a copy; O8's are, by construction, and the stage pays the same bounded cost the branch does), the
twos column lands on the Vulkan probe's dropper row or above it (L1: the recommendation 50.3 against the row's
49.0, the quad 59.4 against 57.6; A5: 46.2 and 50.7 against 46.1 and 50.1 -- the acceleration the branch
could not have, the stage gives the quad, because its window is four distinct drawings), nil on O5 (the
doubled motion out of reach either way; the recommendation loses 1.3 dB there, the one case the stage costs
anything on a twos source), and threes gain the whole prize where the branch got the window's share (L1 41.3
and 43.3 against the branch's 37.0; A5's quad 48.0 against 38.1), because the stage drops both copies of a
threes run. On the on-twos anime clip the stage left out 26 of
132 frames: exactly the pairs the offline statistic reads as copies, which is the count that says the kernel
and the instrument agree. Throughput unchanged within the run-to-run noise (37-45 fps at 1080p either way).

**What this settles.** The question of the morning -- what the players that interpolate anime do that we do
not -- has its answer measured: the cadence step, worth 16-27 dB on the ladder's on-twos sources and nil on
ones, available on the libplacebo route inside the quad's window (`-cadence`) and on the player's route ahead
of every shader. What it does not settle: the redrawn feature (unchanged, correspondence-free), the branch's
short measure on accelerating motion (a cubic across the re-timed span would need the flows of the distinct
frames, which the engine's stage gives the quad and the branch cannot), and the look of it on real anime by eye,
which is the next thing and is the demo's.

*His eyes, the same evening (2026-09-19).* Real content through the player with the stage on -- not full films
yet, a first pass: *"interpolation is looking brilliant on animated as well as live action content --
significant improvements."* The first time the animation side has had that verdict from him; the full-film
tests are his next.

### The fast pan over fine texture: crystallised, its knee measured, the mechanism half-found (2026-09-19, evening)

His report, from a full film through the player: *"The problem remains relatively fast panning shots or
character translations, particularly upon texture dense surfaces. In the given film between 6:29 and 6:34
there is a panning shot across a sandstone textured wall that displays the error. It is jarring to the eye
because the pan goes from 'smooth' to 'weird' in the uncanny valley."* The method is his own: measure it on
the source, crystallise it into a synthetic case, solve on the synthetic, then back to the film.

**The source, measured.** The shot is a tracking shot: the subject walks left along a sandstone wall, the
camera tracking her, so the SUBJECT is near-static in the frame and the WALL crosses it -- `tests/probes/dig/
panspeed.py` (phase correlation at quarter size) reads the wall at 12 px per source frame rising to 38 and
falling to 16 over the five seconds, a cut to a static interior after. The decimate-and-reconstruct bench on
the clip (181 frames; the bench doubles the motion, so read its speeds as half of what the shader saw):

    wall speed (px per source frame)   hold   linear   recommendation   margin over linear
    0-8                                21.6   23.9     26.3             +2.4
    8-16                               21.8   24.2     27.2             +3.0
    16-24                              19.9   22.2     23.7             +1.5
    24-32                              19.4   21.6     22.6             +1.0
    32-40                              20.3   22.7     23.3             +0.7
    (and two frames at 21 px, doubled to 42, where the recommendation fell to the hold's level: -2.2)

The margin shrinks with the speed and the picture becomes linear's -- the ghosted double wall -- which is the
"weird". The subject stays right throughout, which is why it jars: half the frame smooth, half not.

**The synthetic cases** (`tests/scenes.sh`, the edge series; `tests/probes/pan/pan.sh` scores them by speed
band against the native 60 fps render): W1_wall_pan_ramp, a textured ground panning 8 -> 40 px per source
frame over two seconds (x = 192 t + 192 t^2) under a static textured subject, the ground the ladder's 4-px
noise; W2, the same with a ground that has structure at every scale as sandstone has (128-px blocks, 32-px
grain, 4-px noise, summed); W3, W2's wall alone, no subject. The recommendation, PSNR Y by band:

    band px/frame     W1 (fine noise)          W2 (multiscale, subject)   W3 (multiscale, alone)     linear (W3)
    8-12              20.8                     32.8                       33.5                       19.0
    12-16             17.0                     26.2                       24.2                       18.5
    16-20             16.0                     26.3                       27.0                       17.9
    20-24             11.5                     25.0                       24.1                       17.3
    24-28             10.9                     21.8                       22.4                       17.2
    28-32             10.7                     22.3                       22.4                       17.1
    32-36             10.8                     20.6                       20.3                       17.0
    36-41             10.5                     18.1                       17.6                       16.6

Three things read off it. On pure fine noise (W1) the family has no coarse basin at all -- the record's speed
comb -- and holds only to 16-20 px, the reach of the fine levels alone; that is not the film's wall, which
has structure. On the structured wall the loss is GRADUAL from 12 px and the collapse comes at 36 px, with
or without the subject (W2 and W3 agree within a decibel), so the disocclusion at the subject's edges is not
the term; the wall itself is. And linear is flat at 17 whatever the speed: the ghost.

**The field, read** (`read_view 4`, the machine velocity, W3 at N:N): the fraction of the wall's texels whose
flow is within 1.5 px of the pan is 100% at 12 and 20 px, 58% at 16 (one coarse texel exactly: a phase
signature), 86% at 24, 81% at 28, 66% at 32 -- the gradual loss is a growing minority of texels on the wrong
flow -- and 0% at 36 and 39 px, where the median flow is -2.3 px and -6.6: the field has snapped to near
zero. The collapse, not a blur.

**Two mechanisms tested, one refuted, one half-confirmed.** (1) The temporal seed does not carry the pan
because it chains from the previous pair's ZERO-seeded descent (`prev_s` reads the cache's `.xy`, which is
off_a); seeding it from the previous temporal descent instead (off_c, the cache's second texture): 36-41
band 18.1 -> 18.4, 32-36 20.6 -> 21.6. Refuted as the term. (2) The coarse descent's reach: a first step of
0.75 texel halving over five iterations reaches 1.45 texels = 23 px from any seed; doubling the first step
(1.5, six iterations) lifts 32-36 by three decibels (20.3 -> 23.3) and moves the collapse from 34 to 37 px,
and no further: the field read with the doubled reach is 99% right at 32 px, 46-53% at 35-36, 11-13% at
37-39 with the median at -2.5 px. That last number is the clue. 37 px is 2.3 coarse texels, and the wall's
32-px grain is a 2-texel period at the coarse level -- its Nyquist: a shift of 2.3 texels and a shift of 0.3
are the same to the 32-px component there, and the search takes the nearer, which REG_LAMBDA also prefers.
At 32 px (2.0 texels, one whole period) the alias and the truth coincide, which is why that band is the
best in the run. This is the period-collapse family of 2026-09-06 (the stairs, the zero seed) wearing the
fast pan's face: mid-scale texture at the coarse level's Nyquist, and real sandstone has grain at exactly
that scale.

**What follows** (not built tonight). The estimator cannot resolve the alias at the coarse level per texel,
because per texel there is nothing to resolve; the frame as a whole can -- the phase correlation that
measured the film's pan reads 38 px exactly off the same images, because it uses every texel at once and
the 128-px blocks break the tie. So the candidate is a GLOBAL-MOTION SEED: one small pass over the coarse
level that finds the frame's dominant shift (a search over a few texels of shift, scored on a sparse grid,
the 24 x 24 of the cut statistic), handed to every texel's coarse search as a fourth seed beside zero, the
ring and the temporal one, for the finer levels' three-way check to accept or refuse as they do the others.
A pan is then always in the candidate set whatever its speed. A variant behind a switch, the full ladder
its gate (it must not touch a single case that has no global motion), W2/W3 its measure, the film its
proof. The animation synthesis of the morning refused a global candidate for anime's redraws; this is
live action's pan, a different question with the same word in it.

### The global-motion seed: the pan resolved where the texel cannot resolve it (2026-09-20)

The sequel to the evening's finding. The candidate was a whole-frame shift handed to every texel's search;
it was built as an experiment on a copy of the recommendation, measured on W3 and the film, and then put into
the generator behind a switch. Three steps, the third the one that mattered.

**The seed.** Two small passes before the coarse search: GLOBAL_COST, one texel per candidate shift (17 x 9,
half-texel steps over +-4 x +-2 coarse texels, 64 x 32 px at 1080p), each the SAD of A against B shifted on a
16 x 16 sparse grid of the central frame, computed in parallel; then GLOBAL_SHIFT, one texel, the argmin with
a small pull toward zero so a blank frame picks nothing. Offline, the same cost surface on W3's fast frames
puts the minimum at the truth (-2.25 texels, cost 0.012) against 0.08-0.09 at zero and at the alias: the
frame as a whole is never in doubt, as the phase correlation that measured the film's pan had said. The
coarse search descends from it as a fourth seed beside zero, the ring and the temporal one (kept in the
second cache's free .zw), and the 1/8 level refines it as a fifth candidate scored like the others.

That alone: W3 36-41 px 17.6 -> 18.2, 32-36 20.3 -> 22.1, and the field read at 37-39 px still 4-8% right
with the median at -17 and -8 px -- the 1/8 level was refusing the true candidate. The reason is in its
score: `sad + SEED_MAG_LAMBDA * |flow| + ...`, a prior toward SMALL motion (0.3 per 1/8-texel, put there
against fisheye bulges on flat ground). At 4.6 texels of true motion that term is 1.4, the size of the whole
SAD of a good match, and no correct candidate could pay it.

**The term that mattered.** The prior is now measured from the frame's own shift: `SEED_MAG_LAMBDA * |flow -
g|` with g the global shift at the 1/8 level (its negative in the B -> A direction). With no global motion g
is zero and every scored term is exactly what it was; on a pan the prior pulls toward the pan, which is
what a small-motion prior was always for -- toward the motion the frame is making, not toward nothing.

    W3_wall_pan_ramp_alone, PSNR Y by band     recommendation   + seed only   + seed, prior from the shift   gated (-global)
    8-12                                       33.5             36.0          35.8                           35.9
    12-16                                      24.2             26.2          26.3                           26.2
    16-20                                      27.0             27.0          26.7                           26.3
    20-24                                      24.1             25.1          26.7                           25.6
    24-28                                      22.4             23.4          24.9                           22.6
    28-32                                      22.4             25.2          29.1                           30.1
    32-36                                      20.3             22.1          25.6                           22.4
    36-41                                      17.6             18.2          22.5                           21.4      (linear 16.6, hold 15.2)

The collapse is gone: 22.5 dB at 36-41 where the recommendation had 17.6 and linear 16.6. The remaining
decline from 36 dB is real and is the next question (a fraction of texels still wrong at the fastest
speeds; the field read will say which).

**The film.** The wall shot through the decimate-and-reconstruct bench (the bench doubles the motion):

    wall speed (px per source frame)   hold   linear   recommendation   ungated seed   gated (-global)
    0-8                                21.6   23.9     26.3             26.7           26.6
    8-16                               21.8   24.2     27.2             28.6           27.4
    16-24                              19.9   22.2     23.7             26.6           26.1
    24-32                              19.4   21.6     22.6             27.0           26.0
    32-40                              20.3   22.7     23.3             28.2           28.3
    the whole shot                                      24.78            27.31          26.67

Nothing lost where the pan is slow; the fast half of the shot lifted two to five decibels (the gates give back
half a decibel of the ungated gain over the shot, none of it at the fastest speeds), which is the difference
between the ghosted wall and the wall. The side-by-side at 60 fps is in hot-drops
(`wall-pan-recommendation-left-global-seed-right-60fps.mp4`).

**The gate: the full ladder, and the gates the ladder taught.** The seed with the prior, ungated, on all 42
cases: the reach cases up (L4 40-px 30.6 -> 33.9, L7 textured large 23.6 -> 27.3, F2 43.4 -> 46.1, A3 +1.2,
V3 +1.2, M1 +1.3) and the PERIODIC family destroyed -- H2 stairs 28.7 -> 17.3, V2 29.0 -> 16.5, P1 45.3 ->
37.0, V1 -4.5, P4 -3.2 -- the capped mean 38.04 -> 37.59. Read at the shift itself (a debug tail that paints
the pass's own output): on the stairs the coarse level's picture is a Moire, and what moves at 1/16 is the
Moire at its own speed -- H2's motion is 0.375 texel and the frame's best shift read +0.4, -1.0, +1.8, -0.6
pair by pair. Four gates were tried against it, in order. A margin over the runner-up more than a texel away:
refused V2 and nothing else, and on the film -- whose still subject makes every frame's cost surface
two-valued -- it refused the pan on every other frame and the prior flickered, worse than either state;
dropped. Consistency with the last pair (a pan persists, the Moire's picks jump): P1 39.6, V2 28.9, but
consecutive wrong picks can agree. Engagement only for a fast pan, faded in between one and two texels
(within 24 px the per-texel search reaches the motion on its own): H2 back to 28.66. And the frame's MOIRE
EVIDENCE, the per-texel statistic the zero seed's gate already uses, taken as a mean over the sparse grid
(the 1/8 lumas moved ahead of the coarse search for it): above 0.25 the coarse level cannot see the frame
and the shift is refused -- the film reads 0.108, the stairs 0.107-0.182, W3 0.207, so it separates little on
its own but holds the line with the other two. With the three (`-global.glsl`, GLOBAL_SEED=1), the ladder:

    up:   F2 fourier accel +2.33   V3 stairs v12 +1.91   L4 40-px +1.34   V1 bars +1.27   O2/O6 +0.93   M1/M2 +0.87
    down: P1 stairs along v4 -4.13   P3 -0.56   F1/R1 -0.50   L3 -0.42   H2 -0.35   V2/L6 -0.31
    the rest within +-0.2;  capped mean 38.04 -> 38.11

Everything within half a decibel is inside the Mac ladder's own noise for the propagated family (the
2026-09-19 note); the two real terms are P1 down four and the reach cases up one to two. P1 is the pure
periodic print moving along its steps at 4 px, whose frame-wide picks (+1.4, +1.8, +2.0 texels) pass every
gate when three of them agree; there is nothing else in that frame to break the tie, which is what the
synthetic case is for and what a real wall has (the 128-px blocks, a window, a door).

**Where it lives.** `tests/gen_variational.py` with `GLOBAL_SEED=1` in the environment emits it (the banner
line names the variable); without the variable the recommendation regenerates byte-identical (checked, zero
lines of difference), so it is a switch in the sense the project means: the old form is one regeneration
away. It ships as `shaders/bidirectional-interpolation-variational-propagated-global.glsl` (63 hook passes
against the recommendation's 61), and the recommendation is UNCHANGED: the ladder reads the seed as a trade
-- the tracking shot and the reach cases against one synthetic periodic print -- and a trade is his call, as
the zero seed's was. The demo's family can offer it beside the recommendation for his eyes.

**Time.** The film's clip from its lossless file, 181 frames at 1080p to 60 fps, three interleaved pairs, the
median: the recommendation 3.39 s, the variant 3.52 s -- +3.8 per cent on the whole run, of which the decode
is a part, so about five per cent of the shader's own time: two small passes, a fourth coarse descent and a
fifth candidate at 1/8.

**And the question of the night, from him:** *"Is there any benefit from testing with higher frame-rate
conversions, ie 24p -> 120p -- in theory high conversions have to invent more frames so the error is more
likely to be more pronounced?"* No new frames, as it happens: 120/24 is exactly five, so every output sits at
a phase of 0, 0.2, 0.4, 0.6 or 0.8 between two source frames -- and 60/24 is 2.5, whose phases step by 0.4
and land, over two source frames, on the same five. The 60 fps ladder already invents every frame 120 would;
120 renders each of them once per source pair instead of once per two, and the eye sees the same errors
twice as often. What WOULD show more: a ratio that lands a phase at 0.5, the furthest point from both
frames (24 -> 48 is nothing but that phase), and the ladder's 0.4 and 0.6 sit close enough to it that the
figures would move little. The conversions that differ in kind are the downward ones and the odd ones (25
-> 60, whose phases never repeat), which the engine's window test covers.


### The cage: a fine periodic print under a sub-pixel drift, where every warp loses to the blend (2026-09-21)

His second report from the same film: *"A problem that remains is the aliasing problem ... a short book-end
around 10:16 ... some sort of white cage or grid with vertical lines (we previously worked on horizontal steps
with the aliasing issue, but I don't think we worked on verticals)."* A screenshot circled it: the white
railing of the market cross behind the crowd, and in the interpolation its bars bend, fork and break.

**Measured on the source** (`tests/probes/dig/`: the clip, a 4x crop, `panspeed.py` on the railing's rectangle
alone). The bars are 9 px apart, 3 px wide, 80 levels over the wall; the railing drifts a fraction of a pixel a
frame sideways (0.2-0.7 px), moves down 3-4 px a frame at the shot's start, and the crowd crosses it at 6-16.
The recommendation's output at 60 fps, tiled: bars bowed, joined in Y's, one zigzagging -- a flow field that
varies across the railing by fractions of a bar period, not a ghost.

**Crystallised** (`tests/scenes.sh`, `tests/probes/cage/cage.sh`, scored on the whole frame and on the cage's own
rectangle, because a small region's fault vanishes in a frame mean -- which is how his eye found what the
ladder's mean had not): C1_cage_drift, soft-edged bars of that period and contrast on a wall with the ladder's
32-px grain, the whole scene drifting 0.5 px a frame; C2, the same with a dark figure crossing at 6 px a frame.

    C1_cage_drift, PSNR Y          frame    cage's rectangle        C2 (occluded)   frame    cage
    hold                           36.6     31.0                                    35.8     30.0
    linear (the blend)             47.4     43.2                                    39.5     34.1
    the base                       28.6     21.8
    propagated                     29.0     22.2
    variational                    30.3     23.5
    variational-propagated (rec)   31.6     24.9                                    32.4     25.8
    -global                        31.6     24.8                                    32.3     25.7
    the quad                       28.7     21.9

Every member of the family is 6 dB below a HOLD and 18 below the plain blend on the cage, and worse than the
hold on the whole frame, which the cage's fifth dominates. The field, read (`read_view 4`): on the cage 54 per
cent of texels within 0.3 px of the drift, 22 per cent at zero (the small-flow floor), and 20 per cent at -3 to
-10 px -- a bar period away, and those are the bends. The mechanism is the period-collapse family at a finer
scale than the record had it: bars 9 px apart are a MOIRE to the 1/8 level (8-px sampling), the Moire moves
at its own speed, the 1/8 flow is the Moire's, and the quarter level refines from a seed a period out into the
match one period along, which is as good as the true one. The block matcher cannot tell them apart; only a
prior can.

**The ceiling, and what it says.** The family's own warp with the TRUE flow forced (0.5 px, uniform; an oracle
variant): 37.4 on the cage against the blend's 43.2. A warp of half a pixel moves nothing the eye can see and
resamples every bar it touches; on fine detail under sub-pixel motion the blend is the better interpolator
whatever the estimator does. That sets the target: not a better flow here, but knowing when not to warp.

**Four remedies, measured.**
(1) The quarter level refining from ZERO where the 1/8 level's picture is a Moire (`moire_e`, the coarse
    level's own statistic one level down; the 1/8 lumas bound): cage 24.9 -> 30.5 -- and the ladder wrecked
    (L1 -5, L2 -6, M1 -10: the ladder's 4-px noise reads as Moire at 1/8 everywhere, and a good 1/8 flow was
    thrown away for a zero descent that cannot reach 8 px). Refined to a COMPETITION: the zero descent wins
    only as the smaller of two GOOD matches (within 0.3 of the local contrast per tap) with a RIDGE between
    them (the match half way between two minima of a periodic print is at its worst; a flat interior -- L1's
    white block, whose edge the Moire test reads as Moire -- matches everywhere and has no ridge, and there
    the seed stands: without that test L1 lost 6 dB with the gate barely opening). Cage 24.9 -> 27.9, C2 25.8
    -> 27.7; the film's railing 25.5 -> 26.3; the ladder within its noise (L1 +1.1, V3 +1.2, P4 +1.1 / M1 -1.75,
    F1 -1.3, L2 -1.2, the rest under a decibel). In the generator as `QZERO_MOIRE=1`.
(2) A PERIODIC FALLBACK in the final pass: a half-level pass asking whether the final flow is one of several
    equally good matches (its match, the zero offset's match, the ridge between), and blending the frames
    unwarped where it is: cage 28.6, C2 28.2 alone; stacked on (1), with the small-motion blend, 31.2 / 29.9
    -- the hold's level, the wrong texels that remain being sub-period errors no gate names.
(3) The SMALL-MOTION BLEND: blend unwarped under a pixel of flow. Nothing on the cage by itself (the wrong
    texels' flows are not small), a component of the stack.
(4) REFUTED: blending wherever the two frames AGREE locally (the zero offset's match within a fraction of the
    contrast). It gives the cage the blend's own score -- 43.3 at half the contrast, the film's railing 25.5 ->
    29.4 -- and it wrecks the ladder: at half the contrast M1 -17, P2 -11, L1 -9, F1 -7; at three tenths M1
    -9, F1 -4, P3 -3. Random texture and a periodic print in MOTION "agree" to that degree at a wrong offset
    as readily as a sub-pixel drift does at the right one; local agreement cannot tell the two apart, and the
    warp of a moving texture is exactly what the blend then ghosts. The record's old occlusion fallback died
    the same death for the same reason.

**Where it stands.** The cage is a case now (C1, C2, the probe), the mechanism is named, and the honest measure
of the family on it is 6 dB below a hold with the ceiling 6 dB below the blend. (1) is a switch worth three
decibels and no more; the answer the ceiling asks for -- warp where the flow is trusted, blend where it is
not, decided by something that separates a sub-pixel drift of bars from a moving texture -- is not built. The
cue that separates them is not local agreement (refuted) and not the flow's magnitude (the wrong flows are
large); it may be the field's own coherence (a periodic print's wrong flows come in patches at one period's
offset from their neighbours, a moving texture's do not), which is the next thing to measure.

### The field's coherence: the cue that separates, and the gate it makes (2026-09-21, later)

The measure the cage left open: is there anything in the FLOW FIELD itself that tells a periodic print's wrong
flows from a moving texture's right ones, where the frames' local agreement could not? The final half-res
flow painted for a machine (a tail pass, one texel per 2 x 2 block), read on twelve pairs of C1, of the new
C3 (below), and of three ladder controls the agreement blend had wrecked (M1's noise, P2's speckle, L1's white
square), each texel scored against its case's truth, and six cues of the field computed per texel: the
distance from the 9 x 9 median, the 9 x 9 spread, the SUPPORT (the share of the 9 x 9 neighbours within
0.75 px of the texel's own flow), the 5 x 5 range, the forward/backward mismatch, and the change since the
last pair.

    at the threshold that catches 75% of the cage's wrong flows, the share of each population flagged
    cue            thr    C1 wrong  C1 right  C1 wall  |  M1 right  M1 wrong  P2 right  P2 wrong  L1 wrong
    1 - support    0.47      76%        2%       0%    |      0%       98%        0%        1%       51%
    range 5x5      2.44      75%       13%       0%    |      0%       89%        0%        1%       15%
    spread 9x9     1.85      75%       20%       0%    |      0%       12%        0%        0%        0%
    fwd/bwd        1.92      75%       18%       0%    |      0%       90%        2%       42%        5%
    dt             1.73      75%       16%       0%    |      0%       99%        0%        2%       31%

The support separates: three quarters of the cage's wrong flows have under 53 per cent of their neighbours
with them, 98 per cent of its right flows have more, and a moving texture's right flows are NEVER below it
(M1 and P2 0 per cent, against the agreement blend that flagged M1 wholesale). It even catches M1's own
wrong texels (98 per cent). So the cue is real -- and the gate it makes was measured next: a pass at the half
level (81 taps of the flow), and in the final pass the two frames blended UNWARPED where the support is low,
faded between two supports.

**C3, his case: the bars at every angle.** *"Construct a grid of parallel bars, then have that grid both rotate
and translate about its origin -- this avoids thinking in terms of horizontal or vertical bars but the more
general case at any angle."* C3_bars_spin_drift: the same bars and wall as C1, rigidly rotating about the
grid's origin at 0.15 rad/s (17 degrees over the two seconds) while the origin translates at 1 x 0.5 px a
frame; the motion is a different vector at every texel, sub-pixel near the origin and two pixels at the rim of
the 300-px disc the bars fill; scored on the disc. Harder than the cage by every measure: the family's flow is
wrong on 88 per cent of the disc (median error 8.8 px), half of the wrong flows mostly ALONG the bars (the
aperture: a 1-D print cannot say how far it slid along itself, and the grain beneath is too faint to say for
it), and of the across-bar errors 48 per cent are one period out and 9 per cent two. The disc: hold 24.4,
blend 28.9, the recommendation 21.9, -global 21.8, QZERO_MOIRE 21.9 -- the quarter level's zero descent does
nothing here, because its ridge test wants two minima with a worse match between them and the ambiguity along
a bar is a valley, not a second minimum. The whole frame (the rotating wall) 25.4 against the hold's 27.3,
the wall's own flow smoothed short of the rotation (median error 1.2 px at the corners' 4 px).

**The gate alone (support 0.5-0.7): the cage's best number and the ladder's worst.** C1's cage 24.9 -> 33.4
(above the hold's 31.0), C2 25.8 -> 31.6, C3's disc 21.9 -> 26.8; and the ladder: L1 -24, L2 -17, F1 -17,
L8 -15, P3 -15, L6 -14, A1 -12, M1 -11, the capped mean 38.0 -> 35.5. Why, when the cue never flagged a
moving texture's interior: the interior is not where a moving OBJECT lives. At the object's boundary the
window straddles two motions and every texel's support is near a half; inside a flat object the flow is
whatever the propagation left, incoherent and harmless -- until the blend puts the object's edge down twice,
eight pixels apart. The support says where the field disagrees with itself; it does not say the blend is
right there, and at a moving edge it never is.

**The second condition: the frames must agree unmoved.** What the cage has that a moving edge has not: the
two frames, laid over each other with NO shift, nearly agree (a sub-pixel drift moves a bar's edge a
quarter of its contrast; a 5 x 5 mean of |A - B| a tenth to a quarter of the local contrast), where an edge
that moved eight pixels disagrees by the whole contrast across the band. Not the refuted agreement gate: that
blended WHEREVER the frames agreed; here the agreement is required together with the field's own
incoherence, and a coherent field never blends. The pass gains the 5 x 5 agreement at zero as a share of the
local contrast, the blend is the product of two fades -- and the ladder's losses shrink from twenty decibels
to five (agreement 0.25-0.40: L1 -5.0, F1 -5.9, M1 -4.7, H1 -3.3, V1 -2.5; capped mean -0.08) but do not go:
M1's random texture agrees with itself unmoved to a THIRD of its contrast at any offset (the mean |x - y| of
two uniform draws), which sits inside the fade, and no absolute threshold separates a third from the cage's
quarter. The same fragility that refuted the agreement blend, one condition down.

**The third: zero must match as well as the flow does.** A periodic print a period out matches at zero
exactly as well as at its flow -- they are the same match; a random texture in motion matches at zero to a
third of its contrast and at its flow to nothing. So the RELATIVE agreement, |A - B| at zero against |A - B|
at the texel's own flow (with a tenth of the contrast in the denominator so a flat patch reads as agreeing):
under one, zero is as good as the flow; M1's interior reads three, L1's band ten. The product of the three
fades (support 0.5-0.7, absolute agreement 0.40-0.55, relative 0.8-1.3):

    the ladder, propagated-family Mac noise +-1.8   M1 -2.3  F1 -1.6  H1 -1.4  L8 -0.9  F2 -0.8  L7 -0.7  R1/R2 -0.6
                                                    P1 +7.4  L1 +2.2  M2 +1.3  P5 +1.3  L0 +1.3  P3 +1.2  P2 +1.1
                                                    capped mean 38.02 -> 38.02, raw 46.15 -> 46.35
    the cage    C1 24.9 -> 33.2 (hold 31.0)   C2 25.8 -> 31.1 (hold 30.0)   C3 21.9 -> 23.2 (hold 24.4)
    the film    the railing 25.5 -> 27.9 (hold 25.3, blend 29.4); the whole frame 28.67 -> 28.84
    time        +2.8% (720p, 24 -> 60, ffv1 source, three rounds interleaved)

Stacked on QZERO_MOIRE (the zero descent mends the flows it can, the gate blends the rest): C1's cage 35.8,
C2 32.2, the railing 27.5, +0.6% time; the ladder M1 -3.6, F1 -2.2, H1 -1.8, L8 -1.6, L3 -1.3 / P1 +7.5, P4
+1.4, L0 +1.3, M2 +1.2, the capped mean 38.02 -> 38.00 -- the two switches' M1 losses add, and the stack is
the one to read best-of-3 on M1 before anything else.

*2026-10-01: the best-of-3 readings in this entry predate MoltenVK's two switches; with them set, one Mac run is a measurement again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), section 8).*

**Where it stands.** The cue was the measure and it held: the field's own support is the first statistic
that tells the cage's wrong flows from a moving texture's right ones, and it needs the two agreement tests
beside it before the blend it gates is safe at a moving edge. In the generator as `COHERENCE_GATE=1` (off:
the recommendation byte-identical; on: the tested file to a run's wander), stacking with `QZERO_MOIRE=1`; the
recommendation UNCHANGED -- a ship is the full ladder's call and his, and the ladder's M1 -2.3 is at the
edge of the family's noise on this Mac (best-of-3 before any ship decision). C3 is not solved by any of it:
the aperture along a bar is not a period-out match, and its gate would be the flow's variance along the
bar's own direction, unmeasured. The ceiling stands (the blend beats the true-flow warp on such content);
what the gate buys is the part of that ceiling the family can reach without knowing the truth.

**The gate's M1, best-of-3, and the retune.** M1 x3: the recommendation 45.7 / 46.7 / 47.0, the zero descent
46.4 / 46.0 / 45.9 (noise), the gate 44.6 / 44.4 / 43.2 -- a real 2.3 dB. Not the halo of the support window
(the relative test closes a right texel whatever its support): the wrong flows of a random texture in fast
motion match badly at their own offset too, so zero matches "as well" (rel 0.77) and the blend opens where
the warp was no better -- and the fade's partials around them are where the decibels went. The relative
fade tightened to 0.5-1.0: M1 45.9 / 45.5 (within the noise), the cage 32.4 (+7.5); the support fade
tightened instead (0.4-0.6) gives M1 46.0 but the cage 31.5; the absolute agreement tightened (0.30) gives
nothing. 0.5-1.0 is the generator's default.

**The three together, and the player's rule.** His rule for the Cadence player, the same day: *"the best
possible shader that works in most use-cases regardless of performance -- so long as performance stays
within a real-time tolerance ... where a switch-toggle provides some tangible benefit for a specific content
type but might be detrimental to say film, this determines the shader used."* The three switches in one
file, the full ladder, one run each against the recommendation:

    within +-1.7 everywhere: M1 -1.2, L2 -1.4, L0 -1.6 (at 78 dB)  /  V3 +3.0, P4 +1.7, L4 +1.5, M2 +1.2, L1 +1.2, P2 +1.1, P3 +1.0
    capped mean 38.02 -> 38.10, raw 46.15 -> 46.36
    the cage C1 24.9 -> 34.6, C2 25.8 -> 31.6, C3 21.9 -> 22.7; the railing 25.5 -> 27.1; the wall's pan as -global (+1.9, +5 at the fastest)
    time +6.4% at 720p (the seed +2.5, the gate +2.8, the descent +0.6)

The seed's P1 -4 is gone (the gate's P1 +7 covers it: the two answer the same periodic print from two sides).
Ships as `shaders/bidirectional-interpolation-variational-propagated-global-cage.glsl` with a `-4k` form
(`scale_shader.py` taught the global shift's coarse-to-1/8 hand-off; the recommendation's 4K file still
regenerates byte-identical), and by his rule it is the player's default graph from today; the recommendation
stands as the science's reference. One thing to watch: on C1 the combined file's third pair dips (frames 12-13
of the cage at 20-21 dB against the run's 30s), which `-global` alone also does there -- the seed's first
engagements before its consistency memory has a history; two frames in a hundred, and the mean carries it,
but it is the seed's, not the gate's.

**C3's aperture, measured, and the normal flow that could not matter.** The measure taken at leisure: on C3's
disc the wrong flows' along-bar error is COHERENT (correlation 0.98 with its own 9 x 9 mean -- the regulariser's
guess, smoothed into patches, not texel noise; 9 x 9 spread 1.2 px against the right flows' 0.3), so no local
variance cue sees it; and it does not matter: the along-bar component of a flow on a one-dimensional print
moves nothing the picture can see, by the same aperture that made it unobservable. Tried anyway, as the one
cheap thing -- the final pass warping by the flow's projection onto the structure tensor's gradient where the
5 x 5 patch is one-dimensional (lambda2 / lambda1 under 0.15) -- and C3's disc is unchanged to the hundredth
(21.93 -> 21.93 on the recommendation, 22.69 -> 22.64 on the three-switch file), C1 +0.2. What costs on C3 is
the ACROSS error (7.4 px median on the wrong texels, a period or two out) at a motion of one to two pixels,
where the zero descent has no ridge along a bar and the gate's agreement test is rightly closed: the bars have
moved. The remedy for a rotating print would have to resolve the period ambiguity at two pixels of motion, and
nothing measured does; C3 stays open with its number, hold 24.4, blend 28.9, the family 22.7.

### The field on real bodies: two hours of children, scored against a skeleton it shares nothing with (2026-09-27)

WHAT-IT-CAN-MEASURE.md closed on the gap that mattered most: every number the family has was taken on a synthetic
scene with an analytic answer, and the transfer to real footage was assumed, not shown. This is the first real
content with an independent answer key.

**The data.** A live camera (an iPhone 12 Pro's 1x lens via Continuity Camera, 1920x1440 scaled to 1280x960, 30
fps) watched children play for about two hours twenty (2026-09-27, four sessions, 251,527 frames). The recording is
NUMBERS ONLY: no picture was kept, because the players are other families' children. It holds:
- the recommendation's field on every frame, from a Metal host. This is the party app's copy of the plain
  recommendation, without the global seed or the coherence gate: FLOW_H_AB, the two-frame forward flow at half
  resolution, 2-px cells, in field-only mode;
- every 2-px cell once a second, and every frame through a crossing; every frame at 8-px cells;
- Apple Vision's 2D body pose on the same frames: 19 joints per person with confidences.

Vision is a neural detector with no block matching in it, so where the two agree it is not by a shared failure. The
recorder and the formats are in the party app's tree (PartyApp/Recorder.swift); the loaders, the drivers and the
pre-registered predictions are in tests/probes/party/. Data: np-scratch/lillys/party-2026-09-27 and
np-scratch/party-analysis.

**The instrument, first.**
- **The answer key's noise.** Vision's frame-to-frame jitter where the field says the body is still has a median of
  0.8-1.1 px and a p90 of 2.4-3.2 px, with a heavy tail: left/right swaps and lost detections.
- **Midpoints, not joints.** A joint sits at a limb's END or EDGE, where a field window is half background.
  Scoring moved to BONE MIDPOINTS: a rigid segment's midpoint moves by exactly the mean of its ends, and its window
  lies inside the limb. On still bodies the midpoints' noise floor is 0.4 px.
- **The alignment check** (the PSNR-alignment trap, applied first). The field against Vision shifted by -1, 0, +1
  and +2 frames, on identical records, correlates 0.448 / 0.502 / 0.461 / 0.352. The pairing is right.
  - A smaller subset had put +1 first. The rerun on identical records is what overturned it.
- **The control with exact truth.** The party app's own fieldcheck scores the same field against Blender's exact
  flow on rendered children: the bench clips, with every 2-px cell of the actor scored.

**1. Velocity: the middle transfers, and the reach cliff is on real bodies.**
Arms, the unbiased once-a-second records (gain = the field projected on Vision's displacement, median; "zero" =
the share with gain under 0.25):

    px/frame      8-12  12-16  16-20  20-24  24-28  28-32  32-36  36-42  42-50  50-64  64-90
    gain p50      0.71   0.75   0.74   0.71   0.62   0.55   0.50   0.38   0.31   0.15   0.03
    zero          18%    15%    16%    14%    22%    24%    32%    40%    42%    67%    84%

The crossing runs agree band for band, on 10-30 times the samples.

- **The middle band.** The bench's exact truth reads 0.86-0.90 at 4-12 and 12-24 px/frame on rendered children. The
  gap to 0.71-0.75 is about 0.05 from Vision's noise (the attenuation of a projection gain at these speeds) and
  the rest from real content.
- **The cliff starts at 24 px/frame and is half-way by about 40.** It is not a uniform shrink: the median declines
  while a growing share snaps to near zero. That is the fast pan's signature, on bodies against a still room.
- **The cliff moves with the BACKGROUND.** The bench collapses at 24-36 px/frame in its textured room (star jump
  -0.03, dance 0.07) and only past 36 in its dark room (0.53 at 24-36). The still texture behind a limb is what
  wins the search.
- **The global-motion seed cannot reach it:** the frame's dominant shift is zero when only the children move.
- **Size is not the cause** (the hypothesis that a child's limb is one texel at the coarse search: refuted). At
  8-32 px/frame the gain is 0.60-0.74 for body rulers from 90 to 2000 px, with no trend.
- **Direction barely matters.** Vertical motion reads 0.06 lower than horizontal.
- **Legs read worst** (thighs 0.27-0.49, shins 0.36-0.51): party dresses, whose fabric the field follows and the
  skeleton does not.

**How often real children pass the cliff.** Frame-to-frame speeds of 308k frames of Vision bone midpoints, Vision
glitches dropped:

    share of frames over    24 px/frame  36 px/frame  | the same motion at 1080p24 (x1.875): over 24  over 36
    forearms                    8.7%        3.1%      |                                      24.1%    13.3%
    upper arms                  3.3%        0.8%      |                                      14.0%     6.0%
    torso                       1.5%        0.2%      |                                       8.6%     3.2%

Filmed at 1080p24 with the same framing, a quarter of a playing child's forearm frames would be past the cliff and
one in eight deep in it. The fix it asks for is a LOCAL reach: a candidate the coarse search cannot miss where one
region moves fast against a still one. The frame-global seed does not provide that. It is the next lead, and it has
a real-content gate: this data.

*2026-10-01: answered in part below: the coarse texture-energy channel (prototyped in this entry) moves the reach cliff on rendered bodies from 24 to past 36 px/frame ([The aperture in the carry](#the-aperture-in-the-carry-b1-moving-up-and-the-energy-channel-on-rendered-children-2026-09-28-later)).*

**2. The halo, measured on real limbs.** 4,644 profiles across the moving arm bones of children standing alone (no
one within two rulers, so the background's true field is zero). The field is sampled perpendicular to the bone
and projected on the bone's own displacement (Vision's), in units of the limb's motion. +s is the side the limb
moves toward.

    offset px          -64  -48  -32  -16    0  +16  +32  +48  +64
    8-16 across       0.06 0.19 0.49 0.77 0.84 0.81 0.66 0.37 0.14
    16-24 across      0.06 0.16 0.47 0.77 0.84 0.83 0.70 0.42 0.16
    8-16 along        0.05 0.10 0.24 0.45 0.54 0.47 0.30 0.13 0.06

The field falls to half the limb's motion 32 px from the bone's centre-line on the side the limb is LEAVING, where
the background is visible in both frames and its true field is exactly zero. On the side it moves TOWARD it falls
to half at 44 px. It reaches a tenth only at 60 / 72 px. A child's forearm here is 30-45 px wide, so the field's
moving region is about twice the limb.

This is the interpolator's halo, from real content: the synthetic bench's "bleeds 12-32 px" (the party app's
research/01), confirmed. The along-bone rows are the APERTURE on real limbs. An arm moving along its own length (a
push, a reach) reads 0.44-0.54 of its motion at its centre, against 0.84 moving across.

**3. The tensor on real bodies, and depth (THREEDIMENSIONAL.md section 9.8).**
- Divergence and curl both read at the right SIGN on real children.
- Divergence reads at about 0.6 of its magnitude; curl at about 0.9 once the raw field is fitted directly.
- The detail, and the refutation of P4's magnitude, are there.

**4. At an occlusion the field follows the front surface.** 2,347 overlaps of two children's torsos whose motions
differ by 3 px or more. The front child is taken as the larger body ruler (at least 1.15x; a proxy that
misorders a small child in front of a tall one, so the true figure is higher).
- The field's median vector in the overlap is nearer the front child's motion 69.9% of the time (median 3.96 px to
  the front, 6.49 px to the back).
- That rises to 73% with a clearer size order or a larger motion difference.
- It is NOT "the faster motion wins": the faster child wins only 35-41%.
- For the picture this is the right answer. For a skeleton it is P3's warning: the covered child's joints read the
  front child's motion.

**5. Real motion, as the interpolators' input** (Vision bone midpoints at 30 fps, the truth; its floor on still
bodies is 0.4 px).
- **Persistence.** Arms moving at >= 8 px/frame in consecutive frames turn a median 15.5 deg per frame; 17% turn
  more than 45 deg, and **6-7% reverse** (over 90 deg). The rate holds from 8 to 20+ px/frame, so it is motion, not
  noise. The temporal seed's premise holds in the median and fails one moving frame in fifteen.
- **The order question, as path error.** Decimate to 15 fps and rebuild the dropped frames: the straight line (the
  two-frame family) against the cubic through four kept frames (the quad's order). Arms, 15 -> 30:

      local speed at 30 fps   still (floor)   4-8 px/f     8-16 px/f    16-32 px/f
      linear p50 / p90         0.42 / 1.38   2.05 / 5.69  2.97 / 8.15  4.38 / 13.09
      cubic  p50 / p90         0.41 / 1.34   1.83 / 5.17  2.51 / 7.40  3.57 / 12.28
      cubic wins                  53%           58%          61%          63%

  The four-frame order puts a moving limb 11-19% closer to where it really was, and about 20% closer at 10 -> 30.
  Past 32 px/frame both fail alike (p90 about 41 px). This is the benefit the whole-frame picture test could not
  see (per-segment selection worth 0.04 dB): it lives on the moving limbs, a small share of any frame.

**6. The live camera's floor.**
- In an empty room the whole-frame median |f| is 0.01-0.02 px/frame, with a p99 of about 1 (bumps and exposure
  steps). The first session read 0.31 (its setup).
- A 10 Hz line stands 6-9x above the spectrum's median in every session: 100 Hz mains flicker beating against 30
  fps capture. The bench named it and never modelled it. It is present, and tiny.

**Caveats.**
- Vision's joints are kinematic points, not material ones. Bone midpoints mitigate this; they do not remove it.
- The front order at crossings is a size proxy.
- In the last session someone pressed the field's key at 14:58, and 45% of that session's frames have no field
  (the analyses read only the records that exist).
- Every figure is at 1280x960 and 30 fps, on this camera, in this room.

**Predictions (tests/probes/party/PREDICTION.md, written before any score).**
- **P0, Vision's jitter 1-3 px: MET** in the median (0.8-1.1, p90 2.4-3.2), with a heavy tail.
- **P1 (the middle band).**
  - Torso 0.85-1.0: REFUTED, 0.69-0.72 (the bench's exact truth reads 0.86-0.90; the gap is real content plus the
    answer key's noise).
  - Wrists and forearms 0.6-0.9: MET, 0.71-0.75.
- **P2, the gain under 0.6 at 24-48 px/frame, gradual, no snap:** MET on the gain (0.62 -> 0.31); REFUTED on the
  mechanism. The loss is a growing share snapping to near zero (22% -> 42%), as on the fast pan, not a uniform
  shrink.
- **P3, occlusion: RE-POSED and measured.** At an overlap the field follows the front surface 70-73% of the time.
  The joint-level 2x ratio was not scored; the party app's bench had already shown it (12 px against 0.09 at
  visible joints).
- **P4, depth.** Sign: MET (divergence 79%, curl 90% at clear motion). Magnitude, gain 0.7-1.1: REFUTED for
  divergence (0.55-0.64 on the raw field), MET for curl (0.89-0.91 on the raw field).

**The limb on the ladder, and its two mechanisms (2026-09-27, the same evening; tests/probes/limb/).** The cliff is
crystallised as three edge cases (scenes.sh). K1 is a textured limb (48 x 200, the object grain) sweeping a STILL
wall with W2's multiscale texture, at 12 -> 60 px per source frame over the second. K2 is the same limb over a flat
dark wall. K3 is K1 with only the limb's mean brightness raised. All are scored in a box that follows the limb
(limb.sh: whole-frame PSNR would be the still wall's), five runs each, because the propagated family wanders here.

*2026-10-01: the propagated family's wander on the Mac was MoltenVK's; with its two switches set one run is a measurement again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md)).*

- **K1 reproduces the real cliff.** The recommendation leads linear by 5.4 dB at 12-18 px/frame, 1.1 at 18-24 and
  0.2 at 24-30, and sits at or below it from 30. `-global-cage` and the quad do the same: the global seed cannot
  see a lone limb.
- **K2 holds.** The shaders stay 5-10 dB above linear to 36 px/frame, so the background decides.

The per-level view (limblevels.py, levels.py's trick on the recommendation, scored inside the limb; the pairing
checked both ways) separates two mechanisms.

**(1) The coarse level is point-sampled** (one bilinear tap per 16 x 16 footprint; section 8). A fine grain moving by
anything but a multiple of 16 px is tapped at different grain cells in A and B, so the limb's coarse picture is
scrambled while the still wall's taps match exactly at zero.
- The coarse search reads K1's limb at gain 0.26 at 18-24 px/frame.
- It reads K3's (the same grain, a brighter mean, so the limb stands out whatever the taps catch) at 0.87, and the
  final field then holds 1.03 / 0.94 / 0.91 to 36 px/frame.
- So what fails is not speed and not the wall's texture: it is **a finely textured object whose coarse taps
  scramble against a background whose taps do not.**

**(2) The 1/8 propagation is a contrast-weighted mean**, and a textured still background is all high-contrast zeros.
- K1: the fresh 1/8 search reads 0.67 at 18-24, and after propagation 0.29.
- K3: 0.62 -> 0.29 at 36-42.
- A flat wall's zeros carry no weight, which is why K2 never showed it.

**Two remedies, prototyped and gated (the full 42-case ladder, best-of-3 on the Mac, against the committed control
reproduced byte-for-byte).**

*2026-10-01: best-of-3 here and below predates MoltenVK's two switches; with them set, one Mac run is a measurement again ([MOLTENVK-NONDETERMINISM-INVESTIGATED.md](MOLTENVK-NONDETERMINISM-INVESTIGATED.md), section 8).*

- **EDGE_PROP** (gen_variational.py, a switch; each propagation neighbour weighted by its flow's agreement with the
  texel's own, by the texel's confidence). The limb: +1.07 dB at 18-24 px/frame. The ladder: REFUTED.
  - Capped mean -0.36 dB, 21 cases down.
  - The period family collapses: H1 and V1 -11.6, H2 and V2 -5.8, R3 -4.6, A5 -4.0.
  - In the period cases a texel's raw match is confidently wrong, and the mean across disagreeing neighbours is what
    carries the right basin over it. The agreement weight protects exactly the confident, disagreeing texel: right
    at a motion edge, fatal at an alias, and disagreement alone cannot tell the two apart.
  - Kept as the design record.
- **A coarse texture-energy channel** (energyvariant.py, a prototype patch). Beside the point-sampled luma, each 1/16
  texel carries its footprint's mean 2-px gradient magnitude, and the coarse SAD adds W |dE|. This is NOT section
  8's prefilter, which replaced the taps and lost the load-bearing aliased contrast.
  - The limb: the coarse gain at 18-24 px/frame on K1 goes 0.26 -> 0.44 / 0.60 / 0.64 / 0.72 at W 1 / 2 / 4 / 8. The
    final field on K1 improves little, because the 1/8 level aliases the same grain and propagation dilutes (the
    mechanisms stack).
  - On K2 the reach extends: the final field reads 0.87 at 36-42 px/frame and 0.69-0.73 at 42-48 (committed: 0.52
    and 0.15).
  - The ladder: A TRADE. Capped mean -0.11 (W 4) and -0.12 (W 8).
    - Down: the period family (V1 and H1 -2.1 to -2.3; V3 -6.8 at W 8; H2 and V2 -2.2 at W 4) and P5 -1.0/-1.1. The
      pre-registered risk: energy has its own structure where a print's period sits near the coarse texel.
    - Up: L7 +1.7/+2.0, L1 +1.6, M1 +0.6, A5 +0.4/+0.6.
    - L0_static unchanged, as predicted.
  - Real footage (real.sh; realbench's decimate-and-reconstruct, three segments per clip; on this Mac the
    passthrough frames return at ~60 dB, not bit-exact: the known floor of the MoltenVK libplacebo path, not a
    misalignment, which reads 20-30):

        PSNR mean      street (people)   avengers   bttf    bluey
        committed          26.47           36.87    32.53   30.48
        W 4                26.48           37.22    32.19   30.50
        W 8                26.48           37.08    32.53   30.50

  - W 8 is level to slightly positive on real footage, and the street clip does not move at all.
  - **So the channel is a real reach extension for a fast object over a background that does not compete, bought
    with 2-7 dB on the period family** -- the family the zero seed was built to rescue. By the rule it could only
    ship as a switch, off, and the owner's call. It is kept as the prototype (energyvariant.py) and not in the
    generator.
  - **What would make it more than a trade:** keep the energy term out of texels whose coarse luma is a periodic
    print. The QZERO_MOIRE and coherence cues already say where those are. Carry it to the 1/8 level too, where
    the same grain aliases. Both are open.

**The energy channel, second form: smoothed, dense, and at two levels (2026-09-27, evening; energyvariant2.py).**
The first form's losses were read as the energy aliasing: a 24-px print's gradient energy averaged over a 16-px box
ripples with the print's phase.

- **Step 1 (a refutation).** A Gaussian footprint (sigma 12 px) with taps sigma/2 apart made the period family WORSE
  (V1 -19 to -27, H1 to -24). The TAPS aliased: a sine print's |gradient| repeats every 12 px, and a 6-px lattice
  samples it at one phase. Smoothing a statistic does not help if the statistic is sampled below its own Nyquist.
- **Step 2.** Taps every 2 px (25 x 25 out to 2 sigma), at both the coarse level (W_S 8) and the 1/8 level (W_E 1).
  The 1/8 level's post-propagation data check must score the same way, or it rejects the energy-chosen vector by
  luma alone. (Found: the dark-wall limb's raw 1/8 search read 0.95 while its final field fell to 0.2.)

**The result (dense, W_S 8, W_E 1), full ladder best-of-3:**
- **26 cases up by more than 0.3 dB:** L1 +7.2, L2 +5.0, L8 +3.8, F1 +2.7, L3 +2.6, M2 +2.4, M1 +2.3, L4 +2.3,
  R3 +2.3, P3 +2.3, F2, A3 and A2 +1.8 to +2.0, L7 +1.6, L9 +1.2, O1 +1.0, ...
- **7 down:** V3 -8.26, V1 -2.29, H1 -1.89, V2 -1.56, P1 -0.44, H2 -0.41, A5 -0.32.
- **The capped mean reads -0.10** only because most gains sit on cases already above the 40 dB cap, while V3 (26 dB)
  counts in full.
- **The limb, five runs:** K1 +4.6 / +2.9 / +3.2 / +1.1 dB at 18-24 / 24-30 / 30-36 / 36-42 px/frame; K2 +2.5 to
  +3.3 to 48 px/frame.
- **Real footage:** street +0.03, avengers +0.17, bttf +0.34, bluey (the cartoon) -0.14.
- **Cost: x4.0 the recommendation on this Mac** (5.07 s against 1.27 for 3 s of 720p 24 -> 60, interleaved, the cost
  probe's method). The prototype computes each texel's energy from 625 taps at both levels. The engineering form is
  one half-resolution gradient-energy pass per frame, blurred separably and sampled by both levels.

**Open.**
- The cost, by that engineering form.
- **V3, the half-period alias** (square stairs moving 12 px a frame on a 24-px period), which the channel costs 8 dB.
  Its patch moves over black, so the energy blob's edges carry the true motion. The loss is not the obvious one,
  and the per-level view on V3 is the next measurement.
- The sine bars' -2.

**The lead is real:** a phase-free coarse cue beside the point-sampled taps lifts most of the ladder's movers and the
limb that started it.

**The engineering form, the weights, and V3 (2026-09-27, late evening; coarse_energy.py, gen_variational.py
COARSE_ENERGY=1).** The dense prototype's cost (625 taps per texel) was removed by computing the same statistic once
per frame. Each 4 x 4 block's 2-px gradient magnitude on dense taps, at quarter resolution, is blurred separably
(sigma 12 px), and both levels take one sample of it.
- **Cost:** x1.07 the recommendation, against the prototype's x4.04, interleaved on this Mac.
- **Equivalence:** it matches the prototype on the limb (K1 22.90 / 19.96 / 19.32 dB at 18-36 px/frame, against
  22.45 / 19.62 / 19.63).

**Four weightings on the full ladder, best-of-3:**

    W_S / W_E    capped    up / down >0.3    V3      the rest of the losses
    8 / 1        -0.065      23 / 6          -7.90   V1 -1.82, H1 -1.49, V2 -1.05, L0 -0.56, P1 -0.45
    8 / 0        -0.021      16 / 9          -4.97   V1 -3.29, H1 -3.22, L1 -2.38, V2 -1.26
    4 / 1        -0.206      23 / 7          -7.44   H2 -3.18, V2 -1.76, V1 -1.17
    4 / 0        -0.218      12 / 9          -6.56   H2 -3.67, V2 -2.22, L1 -2.02, L0 -1.71

- 8 / 1 is the best form. Real footage: street +0.01, avengers +0.66, bttf +0.12, bluey -0.11.
- **V3 is lost at every weight.** The per-level view (rectlevels.py) shows why:
  - On the committed file the coarse level falls for V3's half-period alias (49% of the patch reversed), and the
    1/8 level's fresh luma search RESCUES it (gain 1.05, 8% reversed), which holds to the end (1.00).
  - With the energy term the coarse seed moves (median gain 1.52: it overshoots), and the 1/8 search then settles on
    the alias (-0.54, 56% reversed).
  - With the energy at the coarse level only, the 1/8 search rescues part of it (31% reversed at the end).
- **So the rescue the base performs on V3 is fragile to ANY change in the coarse cost.** A fix would have to keep the
  1/8 level's alias rescue independent of the coarse seed.
- It ships as the switch COARSE_ENERGY=1 (off; byte-identical when off; SHADERS.md): a trade, and the owner's call.

**Three steps before any leap (2026-09-27, late; the owner's call: "the steps may provide insight into how we leap").**
Three depth leads in the party data that had not been looked at: Apple's 3D pose, the ground plane, and the arm
pointed at the camera. The drivers are pose3d.py, groundplane.py and pointing.py (tests/probes/party/).

**1. Apple's 3D pose is a scale reading, not a depth sensor** (5,260 results at 2 Hz, the first two sessions).
- **It assumes f = 731 px at 1280 wide (82 deg across).** Its own joints, camera pose and image points fit that
  projection to 0.2 px. That is Apple's default; the 12 Pro's 1x lens is about 67 deg (f ~ 962).
- **Its distance is the 2D skeleton's size.** 1/distance correlates 0.85 with the body ruler, with a 13% spread
  (distance x ruler p10-p90 283-365 m px). It adds no metric depth, and its 1.8-m reference body makes a child's
  distance wrong by a factor of about 0.73 H.
- **Its limb tilt out of the picture agrees only moderately with the 2D bone-length rule** (correlation 0.42). The
  2D rule's median tilt is 29 / 38 / 52 / 60 deg where Apple's is 0-20 / 20-40 / 40-60 / 60-90: monotonic, and
  over-reading small tilts.
- **As a teacher for the field's depth it gives the sign and relative scale, which the skeleton already gives.**
- **Re-test on every macOS / Vision update** (the owner: "updates literally update what was previously impossible;
  if Apple fix 3D pose and we aren't paying attention, we can be blind to it for ever after"). pose3d.py runs in
  seconds on any recording made with the 3D pose on. The verdict above is for macOS 27.0, 2026-09-27; what would
  change it is an assumed focal length that matches the camera, a bodyHeight that is measured rather than the 1.8-m
  reference, or a distance no longer explained by the 2D size.

**2. The ground plane is there per child, and the camera's pose is not identifiable from it.**
- For a standing child a pinhole camera gives y_foot - cy = (h_c / cH) s - f theta: one slope per child, one
  intercept per camera.
- On 74,531 standing frames of 103 children (upright, knees straight, both feet in the picture), each child's foot
  row follows its size with a median R^2 of 0.68.
- **The shared intercept (the camera's tilt) is NOT identifiable.** Fitted per session it reads +11.5 / +6.0 / +3.2
  / -2.2 deg. Fitted per half-session it moves as much within a session (+7.5 then -8.7) as between them. Each
  child's range of sizes is too narrow, so the intercept trades against the slopes.
- **One measured quantity would anchor it:** the tripod's height and pitch, or one person of known height standing
  at two marked distances. Then every standing body in the room has a metric depth.
- A cheap thing to capture at the next home session.

**3. The arm pointed at the camera: an arm LOST, not an arm seen short.**
- **Detection:** the shoulder confident while the arm's 2D length falls under 0.35 of that child's own typical
  length, for 3 or more frames.
- **4,148 such episodes, 10.4 per child-arm-minute,** median 0.13 s (p90 0.43 s): puppet 3,024, free draw 781,
  shape draw 343.
- **Vision loses the wrist, not shortens it:** median confidence 0.10, kept in 12% of the frames. This is the owner's
  "no arm bones visible", measured. The same loss comes from an arm behind the back, another child in front, or
  blur, and 2D cannot tell those from pointing.
- **The field shows the fold, not an approach.** At the shoulder (a 40-px window on the 8-px field) the divergence
  entering an episode is -2.54%/frame (51% of frames below -1%), and leaving it is +0.53%. It is the 2D image of an
  arm folding onto the shoulder. No looming signature separates "toward the camera" from the rest at this scale.
- **Apple's 3D pose does not separate them either** (inside an episode the wrist is more than 0.25 m nearer the
  camera than the shoulder in 21% of samples, 17% outside).
- **For the app:** hold the last good wrist through the median 0.13-s loss.
- **For the shaders:** a limb along the viewing axis is where every cue to depth motion (the field's divergence, the
  2D bone rule and a learned 3D model) goes quiet or misleads: the field reads a fold as contraction.

**What the three say before the leap.**
- Relative depth from scale is all a single camera gives here. The field's divergence (sign right 79-90%, magnitude
  about 0.6) and the skeleton's scale are the two readings of it.
- Metric depth needs one calibration.
- The energy channel's open problem (V3) is a matching problem, not a depth problem; nothing here bears on it. It
  stays documented where it is.

**V3 reopened (2026-09-27, night): the half-period alias is a basin the committed shader holds by luck of phase.**

**The per-frame, per-level view** (V3's in-patch gain every frame) shows how the committed shader gets V3 right:
- The coarse level flips every frame between +1.93 and -1.94 (the alias).
- The 1/8 level wanders (0.66 / 1.33, even -1.3).
- The quarter level recovers the true motion (1.00) almost every frame, and the half level holds it.
- Inside the patch the two answers are the SAME picture: a 24-px period moved 12 px up or down. Only the patch's top
  and bottom edges say which. So the interior's right answer is held from frame to frame, not re-derived.

With COARSE_ENERGY (8/1) the 1/8 level declines over the clip (0.66 -> 0.58 -> 0). The quarter level fails for three
frames (9-13). The half level flips into the alias at frame 11 and STAYS there (-0.74 to -0.97), even when the
quarter level recovers at frames 14-18: a flip made permanent by persistence.

**The start sweep (v3phase.sh):** V3 started at six offsets against the coarse grid (y0 = 100..120 in 4-px steps),
three runs each, whole-frame PSNR as bench.sh scores it.
- **The committed shader is BIMODAL:** about 26 dB where it holds the basin, 19-20 where it flips.
  - It holds at 100 and 108, flips at 104, 112 and 120, and does both at 116, on different runs. On a second sweep
    it flipped once even at the ladder's own start (25.8 / 19.5 / 26.1).
  - Averaged over starts and runs it reads about 22.3. **The ladder's 25.97 is a fortunate phase.**
- **The energy channel never holds the basin:** 8/1 reads about 18.2 at every start, coarse-only about 19.6.
- **So its true V3 cost is about -4 dB (8/1) or -2.7 (coarse-only), not -7.9.**

**The other period cases are NOT phase-fragile** (the same sweep: stable to about 1 dB across starts, rare outliers):

    phase-averaged      committed   COARSE_ENERGY 8/1
    V1 (sine, 6 px)       ~55.1        ~53.8   (above 40 dB: invisible)
    H1 (sine, 6 px)       ~55.3        ~53.4   (invisible)
    V2 (square, 6 px)     ~29.0        ~27.7   -1.3, visible
    H2 (square, 6 px)     ~28.4        ~29.3   +0.9, and steadier

**What this changes.**
- **The energy channel's cost in the visible regime** is V3 (about -4, from a baseline that is itself about 22 on
  average) and V2 (-1.3), against 23 cases up.
- **The ladder's V3 is not a stable measurement.** Any gate that moves it by a few dB may be reading the phase, not
  the change. A phase-averaged V3 (six starts x three runs, about 2 minutes) is the honest form.
- **V3's real problem, for every shader:** a periodic interior's motion is decided at the patch's EDGES and held
  inward and forward by propagation and persistence, and nothing re-derives it when it is lost. That is the leap,
  now well defined: carry an edge's evidence into an ambiguous interior every frame. It stays documented here.

**Where V3's answer lives, band by band (v3edges.py, 2026-09-27, night).** The last paragraph's "nothing re-derives it"
was too strong. Per frame and per pyramid level, the field's vertical gain in each of the patch's 13 bar-bands (24 px
each, top edge to bottom). Two starts: 108 (held in 3 of 3 sweep runs) and 112 (flipped in 3 of 3).
- **The coarse level knows nothing.** Its whole-patch gain alternates +1.93 / -1.94 every frame, and in the committed
  shader the finer levels ignore it.
- **The 1/8 level cannot even say 12.** Its flow is in whole texels of 8 px, so in a periodic interior +8, +16, -8 and
  -16 all score alike (each is 4 px from +12 or from -12): a four-way tie, decided by the seeds and by the Mac's own
  run-to-run noise. The quarter level (12 px = 3 texels) is a clean two-way tie.
- **Held start (108), two runs.** The 1/8 search before propagation is right in all 13 bands on every frame, in both
  runs. After the propagation and its data check (a contrast-weighted MEAN of vectors, whose ties go to the
  consensus), one run carried the alias in the interior and grew the right answer back from the BOTTOM edge at
  about one band (24 px) per frame; the other stayed right until frame 19. The quarter and half levels held the right
  answer in both. The propagation's outcome on a tie is a coin the hardware tosses.
- **Flipped start (112), three runs, alike to the band.** Every level starts in the alias. The right answer grows from
  the bottom edge at about one band per frame, at every level from the raw 1/8 search down, and fills the patch by
  about frame 20. **So the
  committed shader does re-derive V3 from an edge -- slowly, and from one edge only.** The flipped start's 19-20 dB is
  eighteen frames of healing in a 24-frame clip.
- **Why one edge.** The 1/8 level's temporal seed is the previous frame's flow at the SAME cell. It is gated by a round
  trip but not motion-compensated. The patch moves down 12 px a frame, so a cell's seed carries the answer of the
  content 12 px below it. A correction at the bottom edge therefore rides up into the patch, and one at the top edge
  rides out of it. The search's reach adds the rest of the band per frame.
- **COARSE_ENERGY 8/1 pins a domain wall.** Its coarse level is now right at both edges and COHERENTLY wrong inside
  (`+.+--------.+`), where the committed coarse level was incoherent and so ignored. The right answer holds two or three
  bands in from each edge and never spreads. From the held start, the alias grows out of the lower interior, band by band, until the
  quarter and half levels follow it (frame 10-13) and only the edge bands stay right. Two runs each, alike. A weak but coherent wrong preference inside, and the boundary loses its grip:
  the 2-D random-field result of statistical physics (Imry and Ma; Aizenman and Wehr) in miniature (PRIOR-ART.md).

**The ambiguity flag, offline (ambiguity.py; the survey's first step, PRIOR-ART.md).** The 1/8 level is emulated in
numpy: luma at each texel's centre, 5 x 5 SAD, every integer shift within +-3 texels.
- **The test.** A cell is AMBIGUOUS when a second BASIN scores near its best. That means a shift at least 2 texels away
  whose straight path back crosses a ridge above both ends by a quarter of the curve's typical rise (the cage's zero
  descent uses the same logic). The margin is the second basin's cost over the best, in units of that rise.
- **The rejected first form.** "Any low cost two texels away" flagged 60-70% of plain translations: it could not tell
  the alias from a stripe's aperture valley.
- **V3 (A -> B; each band spans 24 px from the top edge down):**
  - Bands 2-11 are flagged at 100%, at both starts.
  - The top end (band 0) is flagged at 0%, and all of its confident cells give the RIGHT answer at both starts. **The
    anchors exist, and the flag finds them.**
  - The bottom end is flagged at 33%, and its confident cells are right.
  - One trap: at the flipped start, band 1's confident cells give the ALIAS. The 1/8 level's whole 8-px texels cannot
    say 12, so near the end the quantisation can favour a wrong integer shift. The lift belongs at the quarter level
    (12 px = 3 texels) or needs sub-texel costs.
- **The ladder, share of textured cells flagged at margin < 0.05:**
  - Every non-periodic case (translations, accelerations, oscillations, occlusion, noise, static): 0-1.8%.
  - The textured-motion cases (O5, A5-A7, O6, R3): 1-22%.
  - The periodic prints (L7, M2, M3, V1-V3, H1-H2, P1-P5): 65-93%.
- **Real footage (the three standard clips and the street, 12 segments), share flagged:**
  - 0.1-2.6% at margin < 0.05;
  - 1-7% at margin < 0.15.
- **So the trigger is clean:** rare on real content, and nearly total on a periodic print. It is the gate any
  per-hypothesis carry would open.

**The carry, offline (carry.py; the survey's leap, tried in numpy before any GLSL).** At the QUARTER level, emulated as
the shader builds it, because 12 px is exactly 3 of its texels.
- **The model:**
  - Every textured cell keeps two hypotheses, its best shift and its rival basin (ambiguity.py's ridge test, within
    +-5 texels). The best costs 0 and the rival costs its margin, EXACTLY 0 when the cell is flagged (the Imry-Ma rule).
  - A cell with no rival is a hard anchor, and flat cells break the paths.
  - Four scans of SGM's min-sum run with a small penalty for a one-texel step and P2 beyond. The four are summed, and
    each cell takes its cheaper hypothesis.
  - A small magnitude prior stands in for the shader's own (SEED_MAG_LAMBDA). Without it a stripe's aperture valley
    picks a wild horizontal shift.
- **The first form failed instructively.** Every unflagged cell was a hard anchor. The cells beside a pattern's END
  half-see it and come out confidently WRONG at small margins (0.1-0.2); as hard anchors they won every path through
  them, and V1 fell from 96% to 35%. With the rival's margin as a soft data cost, the run of right cells behind them
  outvotes them.
- **Inside the rectangle, share of textured cells within 0.75 texel of the truth, winner-takes-all -> carry:**
  - V3, at all six starts: 8% -> 100%. (Winner-takes-all breaks the exact tie toward the alias.)
  - V1, V2, H1, H2: 96-97% -> 97%.
  - M3, the period-equals-motion trap: 49% -> 58%.
  - Unchanged: L7, M1, M2, P1-P5, L1-L3, L8. The flat squares score only their edges at this level.
- **Real footage** (street, avengers, bttf, bluey; one segment each):
  - flagged: 0.5-1.9% of textured cells;
  - changed by the carry: 0.02-1.86%.
- **So the leap works on paper:** V3 is re-derived from its ends in every frame, at every start, and nothing else moves.
  The GLSL form still needs to be built:
  - a quarter-level rival search (the full +-5 curve is 121 SADs a cell; the rival of a periodic print sits a period
    away, so a sparse search may do);
  - four sequential scan passes (one invocation per row or column);
  - a combine pass;
  - then the gate, v3phase.sh and the Mac clock.

**COARSE_ENERGY on the player's default, the cage (2026-09-27, night; gateset.sh with the cage as the control, three runs;
v3phase.sh; real.sh; timing.sh).**
- **The ladder:** 26 cases up and 4 down, capped mean +0.10.
  - Down: H1 -2.1 and V1 -1.6 (both at 55 dB), P1 -1.2 (at 47 dB), V3 -0.5 (single start). All above 40 dB.
  - Up: L1 +6.4, L2 +4.3, L8 +3.6, L3 +3.2, M2 +3.0, F1 +2.7, R3 +2.4, P3 +2.2, A2 +2.0, M1 +1.9, and 16 more.
- **V3, phase-averaged (six starts x three runs):**

      recommendation 22.9 (19.3-26.5, bimodal)   + energy 18.0
      cage           27.4 (26.5-28.9, STABLE)    + energy 26.2 (24.8-27.7, stable)

  The cage is not phase-fragile, and on it the energy costs V3 about -1.2, where on the bare recommendation it costs -5.
- **Real footage (the cage -> the cage with energy):**

      clip        PSNR    SSIM
      avengers    +0.30   +0.0011
      bttf        +0.31   +0.0020
      street      -0.06   -0.0005
      bluey       -0.02   +0.0006

  The films are up; the street and the cartoon are level.
- **Time:** +5.3% over the cage (720p, 24 -> 60, interleaved), and +6.4% on the bare recommendation.
- **By the owner's rule for the player,** this is a default: it gains on real content, and its losses are above 40 dB.
  It ships as `-global-cage-energy` beside the cage. Changing the Cadence default is his call (2026-09-27): he approved
  the channel as a player VARIANT.

**Which of the cage's switches holds V3 (v3phase.sh, each switch alone on the recommendation).** Phase-averaged:
- the recommendation: 22.4 (18.1-26.7);
- QZERO_MOIRE alone: 22.9. No effect: its zero descent wins only as the SMALLER of two good matches, and V3's two
  aliases are the same size;
- COHERENCE_GATE alone: 23.0. No effect: V3's frames do not agree unmoved;
- **GLOBAL_SEED alone: 27.0 (25.2-28.8), stable at every start.**

The global-motion seed's frame shift on V3 (dumped per pair): **+12 px moving down, -12 moving up**. Its pair-to-pair
gate zeroes it on some pairs. The shift follows the patch because the patch is the only mover, and the 1/8 level's
small-motion prior is centred on it, so the right alias is the cheaper one. Mirrored V3 (UP=1 in v3phase.sh), the
switch alone reads 28.1-29.1 at every start, and so does the cage; the recommendation reads 17-23.

**B1, the case built to take the frame's anchor away** (scenes.sh `B1_alias_over_pan`: V3's bars in a 200-px patch over a
smooth background panning left 8 px a frame). Its first form panned fine noise, tripped the scene-cut gate, and read
10.18 dB for every shader. That reading is void; the case was rebuilt before any valid run (PREDICTION.md). Phase-
averaged:

    B1, patch moving DOWN:  recommendation 21.3   cage 24.4   global seed alone 24.6   cage + energy 26.4
    B1, patch moving UP:    recommendation 23.0   cage 20.6   global seed alone 20.5

- **The global shift on B1 is (+24, +24) px**, wrong for the background (-8, 0) and for the patch (0, +/-12). It is
  probably a coarse-level Moire of the background: its 40-px component sits near the 1/16 level's Nyquist. It passes
  every gate.
- The 1/8 prior, centred on it, favours whichever alias points DOWN. So the cage "holds" the downward patch by
  coincidence and LOSES the upward one, 2.4 dB below the recommendation.
- **This is the Imry-Ma warning at the scale of the frame:** a coherent wrong preference, from a global estimate that is
  confidently wrong, decides every local tie the same way.

**What this changes:**
- **The player's default has a failure the ladder never showed:** a periodic region moving against a background whose
  coarse picture is a Moire. The global seed's gates (Moire evidence over the whole frame, agreement with the last pair,
  a fade below a texel and a half) did not catch it.
- **The leap's target is confirmed:** a LOCAL carry from the pattern's own ends. B1 up and down is its test. Offline
  (carry.py), the quarter-level carry holds B1's patch at 95% of cells against winner-takes-all's 24%.
- **A step before the leap:** the global prior should not decide a local tie between aliases. In a flagged cell,
  measure the prior from zero, or leave it out.

### The half-period alias in the shader: the prior gate and the carry (2026-09-28)

Steps 1 to 3 of the survey's order (PRIOR-ART.md, the periodic-interior survey), built as two generator switches in
`tests/alias_carry.py`. Both are byte-identical when off.
- **The 1/8 basins pass (either switch adds it).** Each cell's cost curve over +-3 texels. The best shift, the rival
  behind a ridge, and the margin between them (the offline ambiguity flag, in a pass).
- **`ALIAS_PRIOR=1` (with GLOBAL_SEED).** Where a cell's two basins tie, the frame's shift may break the tie only if
  it IS one of them.
- **`ALIAS_CARRY=1`.** At the quarter level:
  - each cell keeps its own two basins, both refined there, with soft data costs (exactly flat on a tie);
  - four scans of semi-global matching's min-sum, one invocation per line per direction;
  - each TIED cell whose own flow lies in one of its basins takes the cheaper one.

**Four builds, three of them teaching.**
1. **The level's own flow as the first hypothesis.** Scored between texels while the rival sat on the lattice: a
   coherent faint preference, and the cage's V3 went to the alias. The Imry-Ma warning, reproduced in our own
   shader.
2. **Both hypotheses scored on the lattice.** V3 down was fixed, but the level's flow at a pattern's SIDES is junk,
   and side cells anchored on it along every row. The cage's B->A flipped every fourth frame, and V3 up stayed at
   21-22.
3. **Junk cells made breakers.** That lost the decisive END's evidence too.
4. **Each cell carries its OWN two basins** (the 1/8 curve's best and rival) and maps the choice back to the level's
   flow only for output. Build 3 also replaced flows in cells whose basins were both wrong, near a pattern's ends,
   which cost V1 and H1 20 dB on the ladder's first run. Build 4 changes only a tied cell whose flow lies in one of
   its basins.

**Build 4, measured (six starts x three runs; the ladder three runs; real.sh; the Mac clock).**

    phase-averaged        recommendation   + carry     cage   + prior   + prior + carry
    V3 down                    22.6          28.6      27.6     27.2         28.7
    V3 up                      19.7          28.0      28.3     28.5         28.6
    B1 down                    21.4          24.2      24.5     23.1         25.3
    B1 up                      23.0          22.4      20.6     21.3         21.8

- **On the player's default (the cage + prior + carry, against the cage):**
  - the ladder: capped +0.09, 14 up and 1 down (P5 -0.47 at 43 dB). Up: P1 +5.1, V2 +1.2, V1 +1.1, L2 +1.1,
    R3 +0.9, V3 +0.8;
  - real footage: PSNR 0 / -0.06 / -0.15 / 0, SSIM level;
  - time: +5% at 720p.
  - **Clean: V3 right both ways at every start, B1 better both ways, nothing visible lost.**
- **On the bare recommendation (+ carry): a trade.**
  - V3 +6 / +8, V2 +1.4, M3 +1.0, M1 +1.0, and real films +0.12 / +0.28;
  - against 13 ladder cases down 0.3-0.8 (F2, P3, R3, M2, P1, F1 among them);
  - +15% time.
- **The prior alone** is neutral on the ladder (capped +0.01; P1 +6.3, V1 +1.4 / L0 -1.0 at 79 dB, V3 -0.5). It
  removes the cage's lucky tilt on B1 (down 24.5 -> 23.1, up 20.6 -> 21.3).

**What remains:**
- **B1.** Moving up, the carry holds 21.8 on the cage against the recommendation's 23.0. The patch's ends sit against a
  background moving otherwise, and the cells straddling that edge make mixed anchors. The perception survey's rule
  (a boundary votes only if it moves with the pattern) is the next step, and B1 up and down is its test.
- **The carry on the energy variant**, the party app's default, is unmeasured.
- **The Metal side.** The carry compiles for Metal (gen_metal: 70/70 and 67/67 passes); the lockstep has not been run
  with it.

*2026-10-01: all three are taken up in the next entry: build 5's aperture rule for B1 moving up, the carry measured with the energy channel, and the lockstep run with the carry in the demo's family (15 of 15).*

### The aperture in the carry: B1 moving up, and the energy channel on rendered children (2026-09-28, later)

**B1 moving up, read cell by cell.** `tests/probes/limb/ownerdump.py` dumps the carry's own inputs per quarter-level
cell of a carry shader: the two basins, their data costs, which basin the four scans prefer, the level's flow before
the pick, and the flow after it. On the cage with prior and carry, B1 moving up, frame 8:
- **The interior split in half.** The upper half's scans chose the wrong alias ("down") and the lower half's chose
  the right one.
- **The top end was not the "mixed anchor" the survey predicted.** Its cells held the RIGHT vertical motion (-3
  quarter texels) in their best basin, with a margin, but with a junk horizontal part: (-4, -3), (-8, -3), (+4, -3).
  Their rival, the wrong alias, sat at exactly (0, +3).
- **Why.** Inside horizontal stripes x cannot be measured (the aperture). Under the right alias the background in a
  window near the end maps onto background, which pulls x toward the background's own motion. Under the wrong alias
  it maps onto bars, which do not care about x, so x stays at the magnitude prior's zero. The same happens for cells
  within the 1/8 level's reach of the ends, whose basins are refined from that level.
- **What the carry did with it.** Its penalty compared whole vectors, so the right chain paid P2 at every junk step
  and the clean wrong chain paid nothing. The scans carried "down" in from the top.
- **Moving down, the same bias was hidden.** There the 1/8 level already held "down" across the patch, so the carry
  had little to do.

**The rule: a cell vouches only for what it can see** (Wallach 1935; Adelson & Movshon 1982's intersection of
constraints; the normal-flow view). The penalty between two hypotheses, and the pick's tests, ignore the component
of their difference along the cell's stripes. The stripe direction is the structure tensor's minor axis over the 5 x 5
window, weighted by sqrt(smoothstep(0.5, 0.9, coherence)), so it is zero on isotropic texture. Of the two cells in a
step, the more coherent decides. A switched flow keeps the level's own component along the stripes.
- **This is not the refuted structure-tensor FILL** (gen_aperture.py, which rewrote flows along bars), **nor the
  normal-flow projection of the output on C3** (which changed nothing). It changes only which of a tied cell's two
  aliases the carry picks.
- **Offline first** (`apcarry.py`, carry.py's quarter-level emulation):
  - B1 up 83% -> 99% of cells right, B1 down 95% -> 100%, M3 58% -> 61%;
  - V3 at three starts both ways and the period family unchanged (V3 100%);
  - real footage: 0.02-1.82% of cells changed, against 0.05-1.86% for the carry without the rule.
- **In the shader:** `alias_carry.py` build 5, on by default under ALIAS_CARRY. `ALIAS_APERTURE=0` stores a zero
  stripe direction, which behaves exactly as build 4. The rule adds a 7 x 7 luma read per quarter cell to the
  hypotheses pass.

**Build 5 against build 4** (v3phase.sh, six starts x three runs; predictions B5.1-B5.7 in PREDICTION.md, written
before these readings except two of B1 up's starts):

    phase-averaged       vp     cage+prior+carry (b4)   cage+prior+carry (b5)   vp+carry (b5)
    B1 up              22.8          21.8                     23.7                  24.3
    B1 down            21.1          25.3                     27.0                  26.1
    V3 up              20.0          28.3                     28.6                  27.8
    V3 down            22.3          28.6                     28.6                  28.5

Every build-5 start reads above build 4's mean on B1 (up: lowest 23.1; down: lowest 26.0). V3 is unchanged, as the
offline emulation said (V3's patch sits on black, so nothing pulls its x).

**With the energy channel** (the same chain, a second session):

    phase-averaged       vp     cage+energy   cage+energy+prior+carry (b5)
    V3 down            22.5        25.9               29.1
    V3 up              19.9        29.1               29.1
    B1 down            21.4        26.5               27.4
    B1 up              23.0        21.0               24.5

The carry repairs the energy channel's V3 loss (25.9 -> 29.1 moving down), and the combination is the best shader
measured on all four readings; every one of its starts reads 23.9 or more.

**The same carry on Metal** (`tests/probes/limb/metalcarry.sh`). The lockstep's own checks run the recommendation,
where the carry never engages, so this renders the cases where it does through the demo's engine and through
libplacebo (median of three runs):

    Metal | libplacebo      cage            cage+energy     cage+prior+carry   cage+energy+prior+carry
    V3 down             28.89 | 27.91   28.35 | 27.36   29.33 | 29.28      29.44 | 29.45
    V3 up               28.87 | 29.11   29.22 | 29.36   29.13 | 28.85      29.41 | 29.36
    B1 down             24.81 | 24.41   26.96 | 26.48   27.09 | 26.85      27.29 | 26.85
    B1 up               19.51 | 19.83   20.08 | 20.33   23.48 | 23.53      24.36 | 24.38
    L1 (control)        66.15 | 65.03   71.26 | 72.03   66.15 | 65.74      71.26 | 70.62
    O5 (control)        42.41 | 42.23   42.61 | 42.13   42.19 | 41.62      42.38 | 41.66
    V1 (control)        51.25 | 56.04   53.76 | 54.08   55.37 | 55.31      53.76 | 54.44
    M3 (control)        21.51 | 21.54   21.69 | 21.71   21.70 | 21.81      21.87 | 21.99

- The carry's scans do on Metal what they do on libplacebo: on the alias cases every carry reading agrees within
  0.3 dB, and within 0.7 dB on the controls. The one larger gap is the plain cage's V1 (4.8 dB, above 50), with no
  carry in it.
- On Metal the carry leaves L1 exactly where it was (66.15, 71.26): it does not engage on a plain translation.
- The combination (energy with prior and carry) is the best of the four on all four readings, on both hosts.

**The energy channel on rendered children: the party app's default, measured.** The party recording holds numbers
only, so no other shader can be run on it. The exact-truth instrument is the party app's own bench: fieldcheck
scores the engine's field against Blender's flow on rendered children. `fieldcheck bench --graph <folder>` (new) runs
the bench through any graph, rendering every pass. Gain per band of true speed, the recommendation -> with the
energy channel:

    px/frame                       12-24          24-36          36+
    star jump 30 fps, textured     0.59 -> 0.96   -0.03 -> 0.86  -0.02 -> 0.33
    star jump 60 fps, textured     0.68 -> 0.97    0.01 -> 0.83     --
    dance 30 fps, textured         0.61 -> 0.89    0.07 -> 0.81  -0.01 -> 0.27
    star jump 30 fps, dark         0.96 -> 0.97    0.53 -> 0.97   0.00 -> 0.69

- **The reach cliff moves from 24 to past 36 px/frame** on bodies, in both rooms. On the party's real children, 8.7%
  of forearm frames at 30 fps (24% at 1080p24) are past 24.
- **Nothing is lost for it.** The slow bands are level (the dance's 1-4 px/frame 0.75 -> 0.72); the joints are level
  or better (median 0.826 -> 0.752 px on the wave); the still-actor control reads exactly zero.
- **The party app's field-only skip holds on the new graph.** FLOW_H_AB is bit-identical with and without the skip,
  and the field dispatches 40 of 67 passes (the recommendation's 34 plus the six energy passes).
- **So the energy graph is the party app's default** (his call of 2026-09-27, now measured on the instrument the app
  has): `LiveField.graphName`, LillysParty.

**Build 5's ladder gate refuted its prediction, and build 6 is the repair.** Against the cage, build 5's carry lost
four non-periodic cases, stable to the hundredth over three runs: A6 -1.21, A7 -0.65, O5 -0.58, R1 -0.32.
- **Found by switching parts off** (`tests/probes/limb/cases.sh`): A6, A7 and O5 carry the ladder's M2 texture,
  sin x sin y with a 40-px period. Build 5's tensor window was the quarter level's 5 x 5, 20 px, half that period.
  Near the texture's zero lines half a period reads as stripes, so the rule discarded a component those cells could
  measure. A strict coherence threshold and a scans-only form both kept the loss.
- **Build 6 reads the tensor over the 1/8 level's 5 x 5 window (40 px).** One period of M2 reads isotropic there,
  and V3's and B1's bars still read as stripes.

**Build 6, gated** (three runs, the cage the control; PREDICTION.md B6.1-B6.4):

    against                          capped   up / down   down
    cage + energy + prior + carry
      vs the cage                    +0.17    26 / 3      H1 -1.61, V1 -0.47 (55 dB), L0 -0.48 (79 dB)
      vs the cage + energy           +0.08     9 / 6      P2 -0.63, H1 -0.61, P3 -0.58 (54+ dB); L3 -0.35, A1 -0.32, A3 -0.32
    cage + prior + carry
      vs the cage                    +0.07    11 / 4      M1 -0.62, M2 -0.51, L0 -0.49, L5 -0.33

- **The M2 cases are back:** A6 -0.16, O5 +0.04, A7 +0.54 against the cage + energy.
- **V3 and B1 kept build 5's gains.** With energy: V3 29.1 / 29.2, B1 27.4 / 24.4. On the cage alone: V3 28.7 / 28.6,
  B1 26.9 / 23.6.
- **Real footage, against the cage:** street level, avengers +0.47, bttf +0.09, the cartoon +0.07. Against the
  cage + energy: within 0.10 on every clip.
- **Time:** x1.29 of the recommendation, +20% over the cage.

**Build 6 on Metal** (metalcarry.sh, the demo's family graph against libplacebo, median of three):

    Metal | libplacebo     cage + energy     cage + energy + prior + carry (b6)
    V3 down               28.35 | 27.92     29.44 | 29.44
    V3 up                 29.22 | 29.23     29.41 | 29.35
    B1 down               26.96 | 26.84     27.32 | 27.23
    B1 up                 20.08 | 20.56     24.38 | 24.55
    A6                    50.38 | 50.39     50.38 | 50.27
    O5                    42.61 | 42.43     42.61 | 42.56
    L1                    71.26 | 72.27     71.26 | 71.30
    M3                    21.69 | 21.71     21.70 | 21.80

On Metal A6, O5 and L1 read exactly as without the carry. The lockstep with the new graph in the demo's family:
PASS, 15 of 15 (graphs by hash, the engine's self-tests, scenes, painting, constants, picture, ladder).

**So the player's default moves** to `bidirectional-interpolation-variational-propagated-global-cage-energy-carry`
(and its -4k form), by his rule: the best shader for most content within real time. That is Cadence 1.0.3. On
Metal, the carry does what it does on libplacebo (the table above); the demo's family offers it, and the lockstep
was run with it in the family.

*2026-10-01: superseded on 2026-10-01: the outline adoption (`-adopt`) and then the capped lattice (`-adopt-lattice`) followed; see the end of "The weave" and [SHADERS.md, "Which one to use"](SHADERS.md#which-one-to-use).*

**What remains.**
- **The half-period alias when the pattern is drifting behind a still window** (the survey's undecidable case). It
  was never built as a scene.
- **A6's residual, about 0.2.** It belongs to the carry itself, with or without the aperture rule, and moves run to
  run.
- **The carry on the bare recommendation stays a trade** (build 4's gate). It was not re-gated at build 6, and it is
  in no app.

### The weave: a two-dimensional periodic print, where the field locks one period away and the family sits at the blend (2026-09-30, late evening)

Found by ENERGY-TRANSFER.md 2.5 (moving a rigid rotation as one), then checked in translation, where it was not
expected. The masters' `weave` texture is a woven-fabric pattern: sinusoidal threads of period 14 px in x and y,
with an over-under checker of period 28 px and fine noise at about 3 px. The master tier had only ever been scored
on `sines`.

**The master tier, textured ground, ladder mean over 240 frames** (`masters/check.sh`, TEXTURE=weave against
TEXTURE=noise; the Cadence default against linear):

    scene                 noise: default / linear    weave: default / linear
    bounce-constant       51.15 / 39.16              26.42 / 25.26
    bounce-oscillating    53.89 / 42.10              27.47 / 28.82   (below linear)
    spin-constant         52.76 / 42.80              20.39 / 21.16   (below linear)
    roll-12               45.42 / 30.08              29.49 / 24.78

On aperiodic texture the default beats the blend by 12-15 dB. On the weave it gains about a decibel, and falls below
the blend on two scenes.

**The whole family, not the default's gates** (`bounce-constant`, weave):

    member          plain   variational   var-propagated   -global   -global-cage   -energy   quad-propagated
    ladder mean     26.64   26.94         26.68            26.68     26.18          27.17     26.50    (linear 25.26)

**The field, read** (the field tier's instrument, the quad at N:N; `fieldtier.sh` now takes TEXTURE):
- **On noise:** median error 0.54-0.62 px, 12-16 percent gross.
- **On the weave:** median error 26.6-27.8 px, 96 percent gross, at an angle 82 degrees off, but with the right SPEED
  (19.0 against 19.2 px/frame).
- The weave maps onto itself under a shift of (0, 28) px, the checker's period. The true motion, (15.8, 10.8), minus
  that period is (15.8, -17.2), at -47.3 degrees. The measured angle error of 81.8 degrees puts the reading at -47.4.
- **So the field matched the print one full period away, where it looks the same.** It is the record's period
  locking (the cage, V3) in two dimensions and at full speed, not at a sub-pixel drift.
- The gates then do what they were built for. The coherence cue and the cage see a field they cannot trust and
  fall back towards the blend, which is why the default lands at linear's level rather than below it. At 19 px a
  frame the blend is a poor answer, not the right one: the cage's ceiling (the blend beats any warp) was measured
  on a sub-pixel drift.

**What the right answer is worth, and the cue that could find it.**
- In rotation (ENERGY-TRANSFER 2.5), a warp driven by the TRUE rigid motion scores 34.6-37.9 dB on the weave
  against the default's 13.8-19.6: 15-24 dB.
- Registration seeded by a field that is wrong but not blind finds the truth. Seeded by a blind one, it does not.
- The cue that is NOT periodic is the object's outline. A body's boundary moves with its true motion, and its
  interior's match is ambiguous up to a period. A region-level prior, "the interior moves with its boundary", is the
  disambiguation the record's cage section said only a prior could give.
- It is the same shape as ENERGY-TRANSFER's two leads (the impact placer and the rigid-region mode): a model of
  the body, found from the field and finished at the pixel level. 2.5c measures the pixel-level finish.

**Where it stands.** A case class the ladder does not contain, measured on the masters: fine two-dimensional
periodic texture in fast motion (woven fabric, checked cloth, grilles and tiles) puts the whole family at the
blend. It is not yet crystallised as a ladder case, and not yet looked for in real footage. The next measurements:
- a weave ladder case at several speeds and periods (where the lock begins);
- whether the outline cue can seed the interior;
- a real clip of checked cloth.

**Pre-registered (2026-09-30, night, before it ran): where the lock begins.** `tests/probes/weave/weavesweep.py`: a
320 x 202 box translating horizontally at 2-24 px/frame over a flat ground, the weave against noise. For each speed,
the field (the quad at N:N) against the true velocity over the eroded box (median error, gross fraction), and the
Cadence default's PSNR on the box region against the closed form, with linear beside.
- Horizontally the weave repeats every 28 px, and also along the diagonal (14, 14).
- For a horizontal motion v, the alias (v - 14, -14) is SHORTER than the truth once v > 14, as is v - 28.
- **Prediction W1:** the field reads the weave as well as noise below about 12 px/frame, and locks (gross above 50
  percent) from 14-16 px/frame up. The default falls to linear's level where it locks.
- If it locks well below 14, the matcher's preference is not for the shortest vector, and the mechanism is
  elsewhere: the coarse levels' aliasing, which starts wherever the texture's period is under two coarse texels.

**Results (2026-09-30, night, the M5): W1 REFUTED, and the lock is a comb in speed, period 8 px.**
`weavesweep.py`, horizontal translation, 48 source frames. The speeds were 3-19: 24 does not fit the frame in 48
frames, as the pre-registration's "2-24" had assumed.

    v px/f   noise: field gross / default - linear      weave: field gross / measured vx / default - linear
     3         0.5%  +20.6                                 71.9%   +15.67   -6.47   (below the blend)
     5         0.6%  +16.1                                 63.4%   +14.31   -5.10   (below the blend)
     7         0.0%  +23.3                                  0.0%    +7.00  +21.99
     8         0.0%  +28.0                                  0.0%    +8.00  +23.29
     9         0.0%  +26.2                                  0.0%    +8.97  +24.32
    11         0.9%  +23.3                                 94.7%   -16.91   +2.08   (v - 28)
    13         0.9%  +20.7                                 96.8%   -14.05   +2.09
    15         0.0%  +16.4                                 28.4%   +14.94  +13.45
    16         0.0%  +17.1                                  0.0%   +15.94  +23.89
    17         0.1%  +16.0                                 15.3%   +16.97  +19.50
    19         1.6%  +20.4                                 97.7%    -8.97   +1.34   (v - 28)
    (field: the four-frame shader's raw velocity, gross = |error| > 2 px over the eroded box; the default against
    linear, PSNR-Y on the box region, equal footing)

- **Not a threshold.** The weave reads exactly at 7, 8, 9 and 16 px/frame, mostly at 15 and 17, and locks at 3, 5,
  11, 13 and 19.
- **The locked vectors are the print's periods, and not the shortest.** At 11 and 19 the field reads exactly
  v - 28 (-17 and -9). At 3 and 5 it reads about +15, far longer than the truth. The matcher does not prefer the
  shortest vector, so W1's premise was wrong.
- **The fit is the alternative the pre-registration named: the coarse levels' aliasing.** The immune speeds sit
  within one pixel of 8 and 16, the 1/8 level's texel and its double. This is the record's point-sampled pyramid
  (section 3). An aliased level is shift-invariant only for whole shifts of its own texels, and the weave's
  14 / 28-px print is aliased at 1/8 and 1/16. The prefilter that would stop it was built and refuted on 09-03
  (section 8), so the pyramid is still point-sampled.
- **The costliest band is SLOW motion, the commonest in footage.** At 3-5 px/frame the field locks to a vector
  three to five times too long, the gates do not catch it, and the default falls 5-6.5 dB BELOW the blend. The
  coherence gate and the cage were built for a sub-pixel drift, and a slow lock is outside what they see.
- **What the translating masters showed earlier fits.** Their bounce runs at 19.2 px/frame along a diagonal: a
  locked speed.
- **This comb is not new: section 8 measured it on 09-03.** On TEX_M1 at 6-14 px/frame the stock scored 28-31 dB
  against 46.9 at the immune 16. The prefilter that would stop the aliasing was refuted there: a box keeps the
  motion right but leaves nothing to match on, and costs the fine ladder 8-20 dB. Section 8's replacement lead was
  a PER-LEVEL TRUST GATE: decide per texel and level whether that level's honestly filtered contrast can seed the
  search. That is the answer this section should have named; nothing later in the record builds it.
- **What the weave adds to section 8:**
  - a two-dimensional print;
  - the SLOW speeds, which section 8 did not measure, where the current default falls BELOW the blend;
  - the fact that every gate added since (the coarse energy, the cage, the coherence cue, the global seed) leaves
    the comb open on it.
- **Next:**
  - the period test (W2, W3, below) to pin the level;
  - the per-level trust gate, section 8's lead, never built;
  - a real clip of checked cloth moving slowly.

**Pre-registered (before it ran): the period test, which separates the mechanism.** The same sweep with the weave's
thread period P set to 10 and to 20 (the checker 2P), at 3-19 px/frame.
- **W2:** P = 10 shows the same comb (immune near 8 and 16, locked between), since 10 is aliased at 1/8 as 14 is.
- **W3:** P = 20 reads at EVERY speed (gross under 5 percent). 20 is above the 1/8 level's Nyquist period (16 px),
  so that level sees the print unaliased. P = 14 read correctly near 8 px/frame although the 1/16 level also aliases
  it, so the 1/16 level's aliasing alone should not lock.
- If P = 20 also locks, the mechanism is not the 1/8 level's aliasing alone.

**Results (the M5): W2 PASSED, W3 MISSED as worded; the comb follows the finest level that aliases the print.**

    v px/f   P = 10: gross / measured vx / default - linear     P = 20: gross / measured vx / default - linear
     3        95.5%  -16.95  -6.15                                0.1%   +3.00  +13.66
     5        94.8%  -15.00  -1.62                                1.4%   +4.94  +17.53
     7         1.5%   +7.00 +24.82                                0.0%   +7.03  +20.81
     8         0.0%   +8.00 +28.95                                0.0%   +8.00  +21.88
     9         1.1%   +8.97 +22.28                                0.0%   +8.94  +22.71
    11        99.1%   -8.97  +2.25                               18.7%  +10.91  +20.99
    13        99.7%   -7.02  +1.70                               17.5%  +12.94  +17.90
    15         2.7%  +15.00 +25.94                                0.0%  +15.00  +28.68
    16         0.0%  +15.91 +20.42                                0.0%  +15.94  +24.68
    17         1.0%  +16.97 +21.03                                0.5%  +16.97  +24.55
    19        98.3%   -0.97  +0.36                               71.7%   +8.72   +4.79

- **W2 PASSED:** P = 10 has the same comb as P = 14. Every lock is exactly v - 20, the 20-px checker period. At 3
  px/frame the default is again 6 dB below the blend.
- **W3 MISSED as worded, and it is the more useful half.** P = 20 removes the 8-px comb: every speed from 3 to 9
  reads cleanly. What is left is a weaker disturbance at 11-13 (18 percent gross) and a lock at 19.
- **The reading:** P = 10 and 14 are aliased at the 1/8 level (Nyquist period 16 px), and they carry a comb of
  period 8. P = 20 escapes the 1/8 level but is still aliased at 1/16 (Nyquist period 32 px). That leaves a weaker
  comb, felt far from multiples of 16. **The comb's period is the texel of the finest level that aliases the
  print.** This is section 8's mechanism, now with its level identified by a controlled change of period.
- **For the trust gate:** it has to act per level. A print aliased at 1/8 only needs 1/8 distrusted; a print
  aliased at 1/16 only needs 1/16 distrusted.
- **The Linux witness (the NAS's Arc, Mesa):** the P = 14 comb reproduces on the other platform. The same speeds
  lock; gross fractions agree within 2 points and the default's PSNR within 0.2 dB at every speed. The comb is the
  shader's, not MoltenVK's.

**Pre-registered (before it ran): is the outline cue already in the field?** The coherence gate cannot see this
lock: at a locked speed the whole box reads ONE wrong vector, which is coherent. The record's cue for a periodic
interior is the body's outline, which moves with the true motion. `weavesweep.py --rings` splits the box into an
edge ring (within 16 px inside the boundary) and a core (more than 32 px inside), at the locked speeds on the NAS.
- **W4:** where the core is locked (gross above 90 percent), the edge ring reads the true velocity on most of its
  texels (gross under 40 percent). The outline cue is then already in the field, and a fix needs only to carry it
  inward.
- If the ring is locked as badly as the core, the lock enters at the coarse level before the edge can speak, and a
  fix has to act at the level itself (the per-level trust gate).

**Results (the NAS's Arc): W4 MISSED where it was registered, and the split by speed is the finding.**

    v px/f   whole box gross   edge ring (0-16 px inside)   core (32+ px inside)   default - linear
     3        71.2%             19.0%                        80.6%                  -6.34
     5        65.6%             16.4%                        73.7%                  -5.16
     8         0.0%              1.9%                         0.0%                 +23.27
    11        94.9%             67.1%                        99.8%                  +2.09
    13        96.7%             73.7%                       100.0%                  +2.12
    19        97.8%             79.3%                       100.0%                  +1.31

- **W4 MISSED as registered.** Where the core is locked above 90 percent (11, 13, 19 px/frame), the edge ring is
  locked too (67-79 percent gross). At those speeds the lock enters at the coarse level before the edge can
  speak, and the fix has to act at the level: the per-level trust gate.
- **But at the SLOW speeds the outline cue is already in the field.** At 3 and 5 px/frame the edge ring reads the
  true motion (16-19 percent gross) while the core is 74-81 percent locked. This is the costliest band, where the
  default falls 5-6 dB below the blend. There, carrying the edge's motion inward (the region-level prior "the
  interior moves with its outline") could fix the lock without touching the pyramid.
- **Two fixes, not one:** a propagation of the outline's motion for slow prints, and a per-level trust gate for
  fast ones.

**Pre-registered (before it ran): the outline carried inward, on the slow weave.** `tests/probes/weave/weaveedge.py`
keeps the box region GIVEN, as ENERGY-TRANSFER 2.5 did, to isolate the one question. It takes the region's motion as
the median of the field over its EDGE RING (0-16 px inside the boundary), then warps the region by that motion from
source frames k and k + 1 (equal footing, bilinear). A RANSAC consensus would pick the locked vector: the locked
core outnumbers the edge. Scored on the box against the default.
- **E1:** at 3 and 5 px/frame the edge ring's median is within 0.5 px of the truth, and the edge-driven warp beats
  the default by at least 10 dB on the box (the default is at 16-20 dB; a correct warp should reach about 40).
- **E2 (the control):** at 11, 13 and 19 px/frame the ring is locked (67-79 percent gross), so its median is wrong
  and the warp does not help.
- noise at the same speeds as a second control: the edge warp is at least as good as the default there.

**Results (the M5): E1 and E2 PASSED. On a slow print, the outline's motion carried inward is a 22-30 dB repair.**

    tex     v px/f   edge-ring motion (truth v)   ring gross   default   edge warp   linear   edge - default
    weave    3        +3.03                         18.8%       20.27     42.31      26.74    +22.04
    weave    5        +5.00                         15.3%       16.23     45.84      21.33    +29.60
    weave   11       -12.77                         68.3%       15.94     15.08      13.86     -0.86
    weave   13        -3.45                         74.3%       15.18     15.16      13.09     -0.03
    weave   19        -8.37                         78.9%       15.66     14.87      14.32     -0.79
    noise    3        +2.84                          3.4%       51.06     52.80      30.46     +1.74
    noise    5        +4.91                          5.7%       43.37     45.53      27.31     +2.15
    noise   11       +10.66                         12.4%       48.44     50.78      25.17     +2.34
    noise   13       +12.91                         11.9%       45.44     48.24      24.76     +2.80
    noise   19       +18.72                         14.2%       44.48     46.84      24.08     +2.36
    (PSNR-Y on the box, dB; the region given, the motion from the field's edge ring alone)

- **E1 PASSED:** at 3 and 5 px/frame the edge ring's median is the truth to 0.03 px. Drawing the region with it
  lifts the box from 16-20 dB to 42-46: +22 and +30 dB, over the default AND over the blend. This is the band where
  the default falls below the blend.
- **E2 PASSED:** at the fast locks the ring is locked too (its median -12.8, -3.5 and -8.4 against +11, +13 and
  +19), and the edge warp does nothing.
- **The noise control PASSED:** the edge warp never loses to the default. Its +1.7 to +2.8 dB there is the given
  region's exact boundary, the caveat ENERGY-TRANSFER 2.5 recorded.

**Where the weave stands, in one paragraph.** A fine two-dimensional print locks the field one period away at every
speed that is not near a whole texel of the finest level that aliases it (a comb; section 8's mechanism, both
platforms). Two different repairs fit two bands:
- **SLOW prints:** the outline already reads the truth, so a region-level prior carried inward repairs them by
  22-30 dB. It needs the region found, which ENERGY-TRANSFER 2.5b-2.5d measure for rigid bodies.
- **FAST prints:** the lock enters at the coarse level before the edge can speak, so the per-level trust gate is
  the only candidate (section 8, never built).

Neither is built. Both would be variants behind a switch, gated on the Arc.

*2026-10-01: both bands have since been taken further: the slow-print repair is in the player (the end of this entry), and fast prints got the lattice re-score (`PRINT_LATTICE`, [ENERGY-TRANSFER.md, lead 4](ENERGY-TRANSFER.md#the-glsl-form-built-testsprint_latticepy-print_lattice1-and-a-second-instrument-fault-found-by-g1)) in place of the per-level trust gate, which was [parked on 2026-10-01](ENERGY-TRANSFER.md#parked-by-the-owner-2026-10-01-morning-the-per-level-trust-gate-to-return-to-within-hours) and has never been built.*

**Pre-registered (before it ran): lead 4's step 0, is there a margin to re-score on?** PRIOR-ART's lead-4 survey
ranks first "carry the aliases down, re-score at a fine level". The weave is not exactly periodic: its 3-px value
noise differs between v and its aliases. `tests/probes/weave/rescore0.py` takes 16 x 16 blocks of the translating
box's core (32+ px inside), frames 10-30, at FULL resolution and at 1/2. It compares the mean |S_k - S_k+1(shifted)|
at the truth (v, 0) against the aliases (v +- 28, 0), (v +- 14, +-14) and (v, +-28).
- **S1:** on the fast weave (11, 13, 19 px/frame) the truth has the lowest cost of the set on over 90 percent of the
  core's blocks at full resolution, and over 80 percent at 1/2, with a median margin (the nearest alias minus the
  truth) of at least 0.01 luma.
- **The control:** noise at the same speeds, the truth lowest on 100 percent with a large margin.
- **If S1 fails,** the synthetic print is too exactly periodic for re-scoring, and the lead must bring a reference
  from outside (the trust gate, time). Real cloth, less regular, would be untested.

**Results (the M5): S1 PASSED at full resolution; the fast weave's lock is not a lack of information.**

    tex     v px/f         full resolution: truth lowest / median margin    1/2: truth lowest / median margin
    weave   5, 11, 13, 19  100.0% / +0.0190 luma (2520 blocks)             100.0% / +0.0066
    noise   5, 11, 13, 19  100.0% / +0.0273                                100.0% / +0.0258

- **The numbers are the same at every speed, and they should be.** For a rigidly translating texture, the cost at an
  alias is the texture compared with itself one lattice vector away, which does not depend on the speed.
- **At full resolution the frames prefer the truth on every block**, by about 5/255 (the survey estimated about
  0.02). At 1/2 the margin is thin (about 1.7/255), a level where camera noise could flip it.
- **What it means:** the lock is not in the data. The pyramid never asks the question. The finer levels search a
  small window seeded by the aliased coarse level, and the truth, 28 px away, is outside it.
- **The fix, as PRIOR-ART's lead-4 survey ranks first:** carry the aliases (the seed plus and minus the print's
  lattice vectors) down, and re-score them at full resolution. The margin is there to re-score on, at least for the
  synthetic print; real cloth is untested. Its detection of the lattice per cell, and a lossless fallback where the
  margin is under the noise, are the design's open parts.

**Pre-registered (before it ran): lead 4's step 1, the fine re-score offline on the default's own flow.**
`tests/probes/weave/rescore1.py`, on the default's quarter flow after the carry (flowtap T2), per 1/8 cell of the
translating box:
- the candidates are the cell's own flow w and w plus and minus the print's lattice vectors;
- the lattice is found PER CELL by a deterministic self-match: the two lowest-cost non-collinear shifts of the cell's
  own 32 x 32 neighbourhood against itself, over 8-40 px, kept only if their cost is under 0.3 of the neighbourhood's
  mean absolute deviation;
- each candidate is refined +-1 px (half-pixel steps), then scored by a 16 x 16 full-resolution SAD;
- the best replaces w only if it beats w by at least 0.004 luma (1/255: the fallback where the margin is under the
  noise).

The predictions:
- **F1:** the fast weave's core gross (11, 13, 19 px/frame) falls from 94-100 percent to under 20 percent.
- **F2 (noise, the control):** no lattice is found, and under 1 percent of the box's cells change.
- **F3:** the slow weave (3, 5) is not made worse than the default's own flow (the stage's switch handles it; the two
  must not fight).

**Results (the M5): lead 4's step 1, the fine re-score offline, in three forms; F1 MISSED with large gains, F2
MISSED in an informative way, F3 PASSED.**
- **The first form** (the candidates w +- the per-cell basis): weave 11 px/frame core 98.2 -> 70.0 percent.
- **With the lattice's nearest points** (combinations +-1): 67.8. Two cells' anatomy showed why that was not enough:
  - a valid basis, (14, 14) and (0, -28), needs 2 p1 + p2 for the fix (28, 0);
  - some locked cells read about ZERO, which is no lattice step from the truth, while the frames still preferred
    the truth decisively (a cost of 0.0000 against 0.143).
- **Step 1b (labelled):** every lattice point within 45 px, plus a MENU of the 3 x 3 neighbours' flows and their
  lattice points (the BBC's menu, PRIOR-ART lead 4):

    case        core gross before -> after   box before -> after   cells changed   lattice found
    weave 11    98.2% -> 36.7%               89.2% -> 31.9%        77.5%           98.8%
    weave 13    99.5% -> 42.2%               87.5% -> 31.6%        77.1%           98.8%
    weave 19    97.6% -> 46.4%               86.9% -> 37.2%        68.4%           98.8%
    weave  3    70.8% -> 35.0%               52.4% -> 25.0%        56.9%           98.8%
    weave  5    91.5% -> 61.4%               77.5% -> 46.2%        58.3%           98.8%
    noise 11     3.5% ->  2.4%               14.8% ->  6.0%        10.9%           69.2%
    noise 19     3.2% ->  2.2%               12.0% ->  5.9%         8.4%           69.2%

- **F1 MISSED:** the fast lock falls from 98-99 percent to 37-46, short of the 20 line. The re-score works; what
  stays wrong is next (the same taxonomy that ended stage 1a's loop).
- **F2 MISSED:** the per-cell self-match finds a "lattice" in 69 percent of noise's moving cells (a smooth texture's
  self-match is low at 8 px), and 8-11 percent of noise's cells change. But they change for the BETTER: the noise
  box's gross falls from 14.8 to 6.0 percent. The menu re-score is acting as a general full-resolution refinement of
  the field, with the frames choosing. Whether that is a feature or a hazard is for the ladder to say; as a switch
  for prints, it needs the stage's specific gate (the 1/8 rival basins).
- **F3 PASSED:** the slow weave improves (3 px/frame 71 -> 35, 5 px/frame 92 -> 61) rather than worsening, so it
  will not fight OUTLINE_ADOPT.

**Lead 4, step 1c (after a taxonomy, labelled): the fine re-score takes the fast lock to 5-13 percent.** The
taxonomy of step 1b's remaining errors: 95 percent had the truth IN the menu, cut by an integer ranking. A candidate
built from a neighbour's fractional flow rounds up to 0.5 px off, which on the print's steep gradients costs as much
as an alias. This is stage 1a's lesson again. Step 1c ranks every candidate after a small refine (+-0.5 px):

    case        core gross before -> after   box before -> after   cells changed
    weave 11    98.2% ->  4.9%               89.2% ->  7.2%        87.3%
    weave 13    99.5% -> 13.3%               87.5% -> 12.0%        83.1%
    weave 19    97.6% ->  8.4%               86.9% ->  7.9%        86.1%
    weave  3    70.8% ->  9.4%               52.4% ->  7.0%        59.9%
    weave  5    91.5% -> 24.1%               77.5% -> 19.9%        69.3%
    noise 11     3.5% ->  2.9%               14.8% ->  8.5%         7.3%
    noise 19     3.2% ->  2.6%               12.0% ->  7.2%         5.8%

- **F1 PASSED (on this post-hoc form):** the fast weave's core is under 20 percent at every fast speed (4.9, 13.3
  and 8.4). What stays wrong is now split between the truth missing from the menu and ranking cuts.
- **F3 PASSED:** the slow weave improves as well (3 px/frame 71 -> 9.4 percent).
- **F2 still MISSED as worded:** 6-7 percent of noise's cells change, again for the better (its box 14.8 -> 8.5).
- **So lead 4 has an offline mechanism:** the aliases carried down as a menu (the cell's and its neighbours' flows
  plus the print's lattice points) and re-scored at FULL resolution, each candidate refined before it is ranked.
- **The GLSL form's open parts:**
  - the lattice in a shader (a per-cell self-match is too dear; a coarse-cell self-match over a sparse set of
    shifts, or ALIAS_E's rival basin, are the candidates);
  - its gate (the 1/8 rival basins, for specificity);
  - its cost.

*2026-10-01: all three were taken up in ENERGY-TRANSFER.md, lead 4: steps 1d to 1r, [the GLSL form `PRINT_LATTICE`](ENERGY-TRANSFER.md#the-glsl-form-built-testsprint_latticepy-print_lattice1-and-a-second-instrument-fault-found-by-g1), its gates and its cost cap.*


**The slow weave's fix is the player's default (2026-10-01).** The owner adopted OUTLINE_ADOPT for Cadence:
`shaders/...-global-cage-energy-carry-adopt.glsl` and its `-4k` (SHADERS.md). The 4K twin reproduces the 720p
file's gains at twice the size (+21.2 / +7.7 dB), and the Metal port agrees with libplacebo on the same frames.
The 5-px gain shrinks on Metal's input path (+2.8 against +9.8), because it is a tie-break that sub-LSB differences
flip (ENERGY-TRANSFER.md, "OUTLINE_ADOPT adopted for the player"). Lead 4's lattice, for the FAST weave, continues
in ENERGY-TRANSFER.md (steps 1h onward: the 1/8 rival basins give true lattice vectors, but long ones and too few
directions).

*2026-10-01: lead 4 was carried through in ENERGY-TRANSFER.md: the GLSL form (`PRINT_LATTICE`), its ladder and real-footage gates, fusion and a cost cap. It is the Cadence player's default (High) quality tier, with `OUTLINE_ADOPT` alone as Standard ([SHADERS.md, "Which one to use"](SHADERS.md#which-one-to-use)).*
