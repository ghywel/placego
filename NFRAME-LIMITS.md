# Where the N-frame line stops, what "wobble" really costs, and what the rotation failure actually is

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
1. ~~**Prefilter the pyramid.**~~ **BUILT AND REFUTED 2026-09-03 -- see
   section 8.** The pre-registration was: the speed comb rises from 28-31 dB
   to >= 40; R4/R5 to >= 34; R3/R6 and the 16 px/frame cases unchanged.
   Measured: the comb gains 1.5-2.6 dB, R4/R5 gain 0.8, and the 16 px/frame
   cases are *destroyed* (M1 46.91 -> 28.64). The replacement lead is a
   per-level trust gate, not a filter.
2. **Add the comb to the ladder** (TEX_M1 and TEX_M2 boxes at 10 and 12
   px/frame) and keep F3 as the rotation-vs-texture control. A ladder whose
   only textured speed is one coarse texel cannot see this class of failure.
3. ~~**Do not build N = 5 as an exact quartic.**~~ **REVERSED 2026-09-03 --
   see the section 8 addendum.** Build it as an exact quartic over a
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
5. ~~**Verify the noise ratio.**~~ **ANSWERED 2026-09-03 -- see the section 8
   addendum.** Measured from the solve's own flows: 1.40 on A4, 1.07 on M1
   (robust 1.15 / 1.00). sqrt(3) is the independent-noise limit, reached by
   neither; the window's flows are correlated (0.35 / 0.9). A first figure of
   0.63-0.80 was a decode error and is retracted in the addendum.
6. **Re-label the rotation lead** in PLAN.md as three leads: aperture on
   edge-only blobs (structure-tensor gate), period locking on symmetric
   texture (tie-break under rotation), and pyramid aliasing (item 1).
7. ~~**Explain the tri collapse on L6 and M2.**~~ **ANSWERED 2026-09-03 --
   see section 8.** With the acceleration deadband raised until the term is
   off, L6 goes 47.95 -> 54.76 and M2 49.48 -> 52.46, recovering 6.81 of the
   7.57 dB and 2.98 of the 4.12 dB. The acceleration term firing on flat and
   periodic interiors is the cause, as predicted.
8. **Test the O6 window-end asymmetry**: re-run the O6 jerk sweep with the
   anchor side swapped (JERK_CENTRE=+0.5) and on a clip padded by four frames.
   If the 0.18-0.44 misses move to frames 2-6 or vanish, they are a window
   artefact, not the floor.

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
