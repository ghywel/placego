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

**A black hole** (`np-scratch/eyes/blackhole/blackhole.py`, not a test: the owner's curiosity). A
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
it began as np-scratch/eyes/blackhole/kerr.py) is a second, metric-agnostic tracer:
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

The negative half. `np-scratch/eyes/blackhole/greybody.py` integrates the electromagnetic Regge-Wheeler
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
(`np-scratch/metal-prep/snap/PREDICTION.md`): each order should cost about 2.9x in signal-to-noise (the
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
inherit its assumption (`np-scratch/anchor/phaseprobe.py`): render an oscillation, decode the field over the
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
