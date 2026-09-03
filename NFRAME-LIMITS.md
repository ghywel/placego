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
and costs noise everywhere else. A 5-frame exact quartic would add a term
whose real-footage SNR is below 1 and whose stencil carries sqrt(20)/sqrt(6) =
1.83x the jerk's noise. Do not build it.

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
starts to earn its keep, and a fifth frame is worth building and testing.
The practical rule for anyone bringing such content to this instrument is to
choose a frame rate (or a frame stride -- see below) that samples the motion
of interest **six to ten times per period**. Faster than that and the
derivatives sink into the noise; slower and the polynomial cannot represent
the motion at all. Nothing at N = 5 has been built or measured; what is
established is that this is the one band where building it is justified.

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
3. **Do not build N = 5 as an exact quartic.** If a fifth frame is built,
   build it as the disjoint-triple acceleration validator, or as a
   fixed-degree fit -- and measure real-footage motion bandwidth first
   (TRI_DIAG=7 velocity at 24:24 over a few seconds; N_max at fixed degree
   is 1 + sqrt((12/w^2 + 7)/3): 3.4 at O3, 4.4 at O5, ~9 at O1).
4. **Retire "residual = measured confidence"** in QUADDIRECTIONAL.md:
   document resid = (3/11)|jerk|, the unit (length(HOOKED_pt)), the max-norm
   and the missing gate; report field statistics as medians over gated
   texels. Its real use is as a per-texel flow-failure gate (27-40x contrast
   between failing and clean bands on R3 -- an analysis-session reading; the
   numbered E2 residual run covered R2 only).
5. **Check the noise-amplification statement numerically** before touching
   QUADDIRECTIONAL.md or the shader header: on the A6 null at N:N, the ratio
   std(jerk field) / std(accel field - 1.333) over the gated interior is
   sqrt(3) = 1.73 if the derivation here is right, sqrt(11/2) = 2.35 if the
   record is.
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
