# Where this goes next

A reassessment, because the leads had gone vague rather than dead. Most of
them were real questions with no attached *prediction* and no *stopping rule*,
which is what makes a path feel stale: you cannot tell whether pulling on it
succeeded. Every item below carries both.

Ranked by cost, cheapest first, per the standing rule in
[METHODOLOGY.md](METHODOLOGY.md): work the cheap band until the gains go flat,
then reassess rather than pushing harder on the same lever.

---

## The one bottleneck both use cases share

The two use cases have been sharing a backlog while wanting different things.
Separating them makes the ranking obvious, because they turn out to share
exactly **one** blocker and diverge only after it.

**24 -> 60 interpolation is in good shape.** `tri` wins eight of nine cases,
up to +4.45 dB, and the gain rises with acceleration exactly as the model
predicts. `ctrl` equals `bi` to the decimal, so the plumbing is right. What is
left here is polish (the `L1` regression at a = 0) and generalisation.

**N:N flow field is not, and the reason is specific.** The calibration says
the field is trustworthy above |a| ~ 5 px/interval^2 and unreliable below ~2.
Real footage measures **0.55-1.5**. So the use case that motivates the whole
thing -- the field as an instrument handed to something downstream -- operates
*entirely inside the band where the instrument is least reliable*. That is the
headline problem, and almost everything cheap should point at it.

### What the low end is actually doing -- and it is not what the log said

The standing explanation was that the low end is **quantisation-limited**: the
field under-reads by 33-66% below |a| ~ 2 because acceleration inherits twice
the flow's own quantisation. Tier 0 refuted that, and the replacement is more
useful.

**Step 1 -- the error is bimodal, not a smooth bias.** Histogramming `O5`'s
live texels, from data already on disk:

| frame | true a_x | median | **near-zero** | at truth | other |
|---|---|---|---|---|---|
| 8 | +7.420 | +7.453 | 5% | 75% | 20% |
| 12 | -8.567 | -8.000 | 6% | 3% | 91% |
| **10** | **-2.218** | **-0.875** | **51%** | 12% | 37% |

("near-zero" = reads below half the true magnitude.) One cluster sits on the
truth and a larger one collapses toward zero, dragging the median into the gap.
A smarter readout does not rescue it -- excluding the collapsed cluster moves
frame 10 from 60.6% error only to 32.0%, and needs the truth to know what to
exclude.

**Step 2 -- the confound.** In `x = A*sin(wt)` the acceleration is
`-Aw^2*sin(wt)` and the jerk is `-Aw^3*cos(wt)`, so **|a| is smallest exactly
where jerk is largest**. Every low-|a| sample in `O5` is also a maximum-jerk
sample. The whole "low |a| is inaccurate" conclusion rested on a scene that
cannot distinguish the two.

**Step 3 -- breaking it.** Two new controls, both cheap:

- **A4-A7**, textured constant-acceleration scenes (`x = X0 - 24V*T + 24V*T^2`)
  at a = 0.33/0.67/1.33/1.67, with **zero jerk** by construction and velocity
  held inside the search's reach.
- **O6**, a textured gentle oscillation with the same texture, object size and
  peak-|a| band as `O5` but **7.8x less jerk**.

The result, at matched magnitude:

| scene | \|a\| | jerk px/interval^3 | error |
|---|---|---|---|
| `O5` frame 10 (zero crossing) | 2.218 | 5.42 | **60.6%** |
| `O6` frame 4 (near peak) | 2.374 | 0.359 | **5.2%** |
| `A6` (constant a) | 1.333 | **0** | **6.8-12.5%** |

**15x less jerk, 11.7x less error, at the same acceleration.** `A6` reads
better at a *lower* magnitude than `O5` does -- the opposite of what a
magnitude limit predicts.

### What that means

**The dominant low-end error is the three-frame model, not the resolution.**
A quadratic through three points assumes acceleration is constant across the
window; where it is changing fastest, that assumption is worst, and the fit
returns something between the window's endpoints rather than the centre value.
That is a **model** failure, and no amount of flow precision fixes it.

Quantisation is real but its reign is much smaller than believed: it dominates
only below |a| ~ 0.5, where `A4` (a = 0.333) errs 69-125% with readings pinned
to the 0.25 lattice. Between 0.67 and 2.4 with low jerk the field is already
good to 5-13%.

**This re-ranks the plan.** Sub-pixel refinement (T1.1) was the obvious lead
under the quantisation story; under the jerk story it buys the band below 0.5
and leaves the measured failure untouched. The fix that addresses jerk
directly is a **degree-3 fit over four frames** -- which was Tier 3, the
expensive leap, and is now the *indicated* change rather than a speculative
one.

Note this arrived the way METHODOLOGY.md says it should, but cheaper: not by
exhausting the parameters until nothing moved, but by building the control
that separated two variables a single scene had welded together.

### Still true: there is no sub-pixel stage anywhere

Worth keeping on the record because it bounds the floor. The pipeline is a
coarse search at 1/16 then integer refinement at 1/8, 1/4 and 1/2, then two
vector-median passes. **Every search steps whole texels in its own level**,
and `best_off / LUMA_A_H_pt` stores integer half-res texels, so the finest
measurement possible is **one half-res texel = 2 full-res px per interval**.
The 0.25 px/interval^2 grid the readings sit on is the bilinear lattice from
sampling a half-res texture at full-res positions -- interpolation between
measurements, carrying no extra information. That sets the floor below |a| ~
0.5 and is why `A4` fails.

## Tier 0 -- no shader change, hours

Measurement and sweeps against tools that already exist. Several of these have
been sitting in the register marked "cheap next check" for a while.

**T0.1 -- Characterise the low-end failure. DONE, this session.** Result
above: bimodal collapse, 51% against 6%, readout-only fixes refuted. Cost:
zero new renders, the data was already on disk. *This is what re-ranked
everything below it.*

**T0.2 -- Sweep `TIE_MARGIN`. DONE -- CLOSED as a clean negative.** It was
the long-flagged cheap check: a second zero-bias in the same path, since it
requires a candidate to *beat* an incumbent that starts at zero motion.
Measured near-zero fraction at `O5` frame 10 across `0 / 1e-4 / 1e-2`:
**51% / 51% / 47%**. A 100x parameter change moves the collapsed population by
four points, which is the "extreme tuning that changes nothing" signature --
`TIE_MARGIN` is not implicated and the item closes.

*One live side-observation, not chased:* at `1e-2` the frame-10 **median**
improves from -0.875 to -1.250 (60.6% -> 43.6%) without the collapse moving,
so it is not inert -- it shifts which candidates win. Worth one ladder run
before anyone changes it, since `TIE_MARGIN` exists for determinism and a
100x change touches every match decision.

**T0.3 -- Calibrate beyond `O5`. DONE, and it found the real problem.**
Running it exposed that `A1`-`A3` carry the right magnitudes but a **flat**
interior, so the field exists only on their perimeter -- coverage 2-15%, with
the few readings saturating the encoding. They cannot calibrate anything, for
the same reason `O1`-`O3` could not and `O5` had to be built. **The band real
footage occupies had no textured ground truth at all**, which is why it took
this long to characterise.

Fixed by adding `A4`-`A7` (textured, constant-acceleration, velocity inside
the search reach, and passing through a genuine reversal) and `O6` (the jerk
control). `accelcheck.py` extended to parse the general quadratic. Those five
scenes are what made the jerk finding above possible, and they are now the
low-band ground truth everything else gets judged against.

*Still open here:* `R2` (rotational acceleration) and `F2` remain
uncalibrated, and rotation is a genuinely different case the field has never
been tested on. **Cheap, and next.**

**T0.4 -- Sweep `ACCEL_MAX_PX`. DONE -- and "already correct" was NOT what
the sweep found.** The prediction (flat from 16 up, harmless everywhere) was
wrong in both directions:

| `ACCEL_MAX_PX` | `L1` | `O2` | `O3` | `O5` |
|---|---|---|---|---|
| 8 | 60.49 | **46.04** | 45.10 | **33.93** |
| 16 | 60.49 | 45.91 | **46.37** | 33.84 |
| 32 / 64 | 60.49 | 45.91 | 46.37 | 33.77 |

The clamp is an ACTIVE NOISE SUPPRESSOR, not a formality: `O5` degrades
monotonically as it loosens (junk above the true 8.6 peak leaks the trust
gate, and the clamp catches some), and 8.0 actually *wins* on `O2`/`O5`
while costing 1.27 dB on `O3` (whose true 13.2 peak it clips). 16 survives
as the measured compromise -- it dominates 32/64 outright and beats 8 on
net -- but it is now a trade-off with numbers attached, not an assumption.

**T0.6 -- N:N vs 24->60 conditioning. CLOSED AS A THEOREM, and the plan's
own framing was wrong.** Setting up the measurement exposed the argument:
the estimator's taus are anchored to FRAMES, not to output time, so at
uniform spacing the stencil is +/-1 interval at every output rate -- the
rate moves only the placement `s`. Same window triple, same cached flows,
identical field, provably. Confirmed digit-for-digit: `O6` anchor frame 6
reads -2.709 at 100.0% coverage at BOTH 24:24 and 24->60 (output frame 15,
which lands exactly on source frame 6); the off-lattice pair (N:N f5 vs
24->60 f13) matches within one readback code (-2.580 / -2.581, coverage
59.2% both). "The symmetric stencil buys nothing" is true for the strongest
possible reason: there is no asymmetric stencil anywhere in the estimator.

**T0.R -- `R2`/`F2` calibration. DONE, and both FAILED -- the day's real
discovery.** `F2` (quadratic translation, a = 1.333, same physics `A6`
reads at 2.0-2.7%) measures 24-74% -- the difference is its FLAT interior:
an isolated edge constrains flow only along its normal (the aperture
problem), and the acceleration inherits the unconstrained tangential part.
`R2` (rotational spin-up, vector truth `a(p) = alpha*J*(p-c) - omega^2*(p-c)`,
measured per-texel by the new `tests/rotcheck.py`) reads 133-207% median
vector error with 60-95 deg direction error. The discriminating control
`R3_rot_tex` -- same rotation, TEX_M2 riding the body frame -- was built to
separate the two suspects, and it fails too (100-207%): **rotation degrades
the field even with full texture, so the aperture is not the whole story.**
The truth formula was verified against the exact discrete second difference
(agreement to 0.3%), so the failure is in the flows, not the algebra or the
instrument. Cause not yet localised; the named next probes are `R1`
(constant omega -- separates spin-up from rotation) and a flow-level (not
accel-level) truth comparison on rotating content.

Two constructive consequences, now open leads: (1) a **structure-tensor
gate** (Shi-Tomasi smaller eigenvalue) so the field reports "no
measurement" on aperture-ambiguous texels instead of confident
contamination -- today the trust machinery passes edge-only readings that
are wrong by construction; (2) the field's trust statement must name
CONTENT limits, not just magnitude limits: translation of textured content
2-7%; edges-only content and rotation currently unreliable.

**T0.5 -- Re-test `ACCEL_DESPIKE_R`.** Currently 0, because the first
implementation was a no-op bug (`lo`/`hi` seeded from the centre value, so the
clamp could never move anything). The bug is fixed; the feature has still
never actually been evaluated. The bimodal picture suggests a despike could
help *or* could eat the sparse correct cluster -- worth one measurement.
**2 ladder runs.**

*(T0.6's original entry superseded by the theorem above.)*

---

## Tier 1 -- small shader edits with sharp predictions, ~a day each

**T1.1 -- Sub-pixel refinement at the half-res level. DONE, and it was the
lead after all.** I demoted this on the jerk finding and that was wrong.
Built as a parabola fit through the SAD minimum and its two neighbours per
axis, at the half-res level only, in the base shader so both shaders inherit
it. Measured:

| | before | after |
|---|---|---|
| `A4` a=0.333 (the judge) | 125.0% | **9.0%** |
| `A5` a=0.667 | 12.5% / 98.3% | **5.5% / 30.3%** |
| `A7` a=1.667 | 55.0% / 20.0% | **11.2% / 4.1%** |
| `O5` frame 10, a=2.218 | 60.6% | **11.2%** |
| `O5` frame 10 near-zero population | 51% | **5%** |
| coverage, low band | 20-75% | **~99%** |

**This corrects the Tier 0 conclusion.** The 51% collapse at `O5` frame 10 was
quantisation, and sub-pixel removes it -- so the low end was quantisation-
dominated as the original log said, and my jerk attribution was over-stated.
Jerk is real but secondary: the `O6`-vs-`O5` gap at matched magnitude has
fallen from 11.7x to about 2.9x (11.2% at maximum jerk against 2-5% at low
jerk). The residual is what four frames should collect.

**The cost, and where it lands.** Fractional flow forces the warp to resample
bilinearly where an integer half-res flow landed on pixel centres, and that
costs real dB on the interpolation ladder -- up to 1.30 dB on `L1`, and the
loss tracks each case's sharpness, which is the signature of added blur. The
null control isolates it: `ctrl` loses 0.48 dB on `L1` from the warp alone,
so the other 0.82 dB was the correction acting on the field's heavier tail.
Hence sub-pixel is **off in the base shader and on in the generated
tridirectional one** -- a pure interpolator pays the cost and has no field to
gain -- and hence the deadband below.

**Follow-up, from the prior-art survey: DONE -- the V-fit ships, and the
literature was right.** Measured A/B on the full low-band calibration,
parabola against equiangular, same battery, parabola arm reproducing every
historical number:

| sample | parabola | equiangular |
|---|---|---|
| `A4` f6 | 25.4% | **4.3%** |
| `A4` f12 | 48.5% | **19.2%** |
| `A5` f12 | 32.0% | **3.9%** |
| `A6` f9 / f12 | 10.9% / 15.3% | **4.8% / 3.3%** |
| `A7` f6 / f12 | 11.2% / 12.6% | **6.7% / 6.7%** |
| `O5` f10 | 11.2% | **7.0%** |
| `O6` f6 | 3.9% | **0.3%** |

15 of 18 paired samples improved; the three losses are all <= 0.7 points.
The quad jerk NULLS fell ~3.7x (`A6` f12 -0.263 -> -0.070), and the jerk
signal at `O5`'s peak improved 8.2% -> 4.4%. Interpolation cost: <= 0.37 dB,
sharpest case only. `SUBPEL_FIT = 1` is now the base default (inert in the
base itself while sub-pixel is off; both field shaders inherit it live).
The low band real footage occupies now calibrates at **3-9% typical** --
against 125% three days of work ago. Original framing kept below. Stereo and PIV literature call it *peak
locking*: sub-pixel fits bias toward integer positions, worst at small
fractional displacements, and the matched fit depends on the valley's shape
-- a parabola matches an SSD valley, but an **SAD valley is piecewise linear**,
for which the **equiangular (V-shaped) fit** is the matched estimator
(Shimizu & Okutomi). Ours is a parabola over SAD, and the residual toward-zero
under-read still visible in `A4` has exactly the peak-locking shape. One-line
change, judged on the same calibration. The cheapest open item in the plan.

Original text kept for the record: a parabola
fit through the SAD minimum and its two neighbours per axis is the standard
trick and roughly ten lines, and it is the direct attack on the bottleneck
identified above. *Prediction, quantitative:* the near-zero collapse fraction
at |a| = 2.2 falls from 51% toward the ~6% seen at high |a|, and the low-end
error falls from 60% toward the ~1% the field already achieves above |a| = 6.
*Stopping rule:* if the collapse fraction does not move, flow precision is
**not** the limiter, the diagnosis above is wrong, and the right response is
to stop and reassess rather than to try a second sub-pixel scheme. Also the
one item expected to help **both** use cases, so measure it on the 24 -> 60
ladder as well as on the calibration -- three modes, per the methodology.

**T1.2 -- A full-resolution refinement level. DONE -- built, and it took
three measured steps to ship.**

*Step 1, the naive build* (H pass transformed one level down, 3x3 SAD,
feeding warp and estimator alike): the field's hard samples improved
sharply (`A4` f12 19.2% -> 5.5%) but two easy samples regressed (`A4` f6
4.3% -> 18.3%) and the ladder paid badly -- `L1` -2.95 dB, from the warp
consuming unfiltered full-res scatter the medians used to remove. Both
failures arrived with their causes pre-named: the aperture caveat and the
unfiltered-final-level risk, both written down before the build.

*Step 2, warp on H / measure on F* -- the two-use-cases split applied a
third time (after the deadband and the sub-pixel default). The estimator
reads the full-res flows; the warp keeps the mediated half-res ones. (In
the quad shader this pushed the final pass to exactly libplacebo's 16-bind
ceiling, paid for by retiring the never-enabled texel-snap gate.)

*Step 3, a 5x5 SAD aperture at F only*, testing the pre-registered suspect:
a full-res 3x3 spans a third of the pattern context the H-level 3x3 does.
Confirmed -- the 5x5 fixed nearly every F-level regression.

Shipped result, against the V-fit/H baseline (18 calibration samples):

| | H level | full-res, shipped |
|---|---|---|
| mean error | 7.24% | **4.31%** |
| median error | 5.0% | **2.9%** |
| worst | 23.8% | 17.2% (= 0.058 px/interval^2 absolute, the smallest signal) |
| `A5`/`A6`/`A7` typical | 3-7% | **1.8-3.1%** |
| `O6` f10 | 14.5% | **7.7%** |
| jerk nulls (quad) | -0.038/-0.070 | **-0.020/-0.033** |
| jerk at `O5` peak | 4.4% | **3.4%** |
| ladder | baseline | equal or better everywhere; `L1` +0.99 |
| cost | -- | +40% (tri), +48% (quad) |

The original measurement that argued for the level, kept below.

The question was how much more is available from resolution once sub-pixel has
been applied. Answering it did not require the level: render the identical
physical scene at **2x scale** -- canvas, object, texture period and every
motion coefficient doubled -- and the estimator's texel becomes half as coarse
*relative to the content*, which is exactly what one more pyramid level buys.
`A4`'s content, at 2x, has a = 0.667 px/interval^2:

| frame | 1x | 2x |
|---|---|---|
| 9 / 15 | 9.0% | **0.8%** |
| 6 / 18 | 25.4% | **10.4%** |
| 12 (velocity reversal) | 48.5% | **27.9%** |
| coverage | ~99.5% | **100%** |

**Doubling the effective resolution roughly halves the relative error at every
sample.** So the low band is still resolution-limited after sub-pixel, and a
full-res level should take `A4`-class content (a ~ 0.33, the bottom of the
real-footage band) from 9-48% to roughly 1-28%.

Two things follow. First, there are **two independent axes left**, not one:
resolution and the jerk/model term. Second, the cost is not free -- a full-res
level adds two luma downsamples and two search passes at 4x the texel count of
the half-res level, on a path whose sensing use case is real-time. Worth
building; worth measuring the frame cost while doing it.

Note the worst sample at both scales is frame 12, which is where velocity
passes through zero. The reversal instant is the hardest one consistently, at
any resolution.

**T1.4 -- Deadband on the correction. DONE. It closed the `L1` regression.**
Not in the original plan; it exists because T1.1's cost had to be paid back.
The field on constant-velocity content (`L7`, truth exactly 0) reads median
0.000 but p90 0.277 and p99 3.914 px/interval^2 -- a heavy tail the warp was
acting on. Deadbanding the acceleration **used for the warp only**, leaving
the reported field untouched, because a sensing consumer wants the
measurement and an interpolator wants only what is safe to move pixels with:

| deadband | `L1` | `O1` | `O2` | `O4` | `O5` |
|---|---|---|---|---|---|
| off | 56.16 | 49.65 | 46.17 | 47.35 | 34.03 |
| 0.25/0.75 | 58.21 | 49.62 | 46.17 | 47.35 | 34.03 |
| **0.5/1.5** | **60.77** | 49.44 | 46.19 | 47.36 | 34.03 |
| 1.0/2.5 | 61.35 | 49.06 | 46.16 | 47.33 | -- |

`L1` climbs 5.2 dB while the oscillation cases -- where the acceleration is
real -- move by hundredths until the widest setting. 0.5/1.5 is the knee and
is now the default.

**Stated precisely, because an earlier note in this session overstated it:**
at the shipped 0.5/1.5 the `L1` regression against `bi` is **reduced from
-3.80 dB to -0.49 dB, not eliminated.** It reaches +0.09 -- genuinely gone --
only at the wider 1.0/2.5, which costs `O1` 0.38 dB. The oscillation cases are
what this shader exists for, so 0.5/1.5 is the trade taken.

The full ladder now shows three small losses rather than one large one:
`L1` -0.49, `L3` -0.34, `F2` -0.14. All three are the sub-pixel **warp** cost,
not the correction, so no deadband setting recovers them. The acceleration
gains are intact (+2.35 to +4.14 across `O1`-`O4`), and `tri` now beats stock
`linear` on `O5` where `bi` loses to it.

**T1.3 -- Localise the `L1` regression. DONE, and answered by T1.4.** It was
the correction acting on sub-quantum noise, not the field being wrong: the
field reads median 0.000 where truth is 0, but its tail reaches ~3.9. Gating
the tail fixes it. Original framing below.

-3.80 dB on content whose true
acceleration is exactly zero, where the shader is required to be a no-op --
and yet `L2`, also constant velocity, *gains* 0.93 dB. The collapse-fraction
instrument from T0.1 gives a way in that did not exist before: read the field
on `L1`, where truth is 0, and see whether it reads non-zero. That separates
"the field is wrong" from "the field is right and the correction misapplies
it", which nothing so far has done. Cheap, and it sits next to the unexplained
`L1`/`L2` anomaly in the base shader.

---

## Tier 2 -- new instruments and new material, ~days

**T2.1 -- Export the field as float data. DONE** -- `tests/fieldexport.py`,
which turns a render into `float32` (frames, H, W, 2) in px/interval^2 plus a
JSON sidecar carrying units, scale and an audit.

The audit is the part that earned its keep. `ACCEL_DIAG_FS` is the encoding's
full scale and anything beyond it is **clipped, not wrapped** -- it returns
exactly +/-FS and reads like a confident measurement. That is not
hypothetical: it silently corrupted the first low-band calibration in this
session, which reported "+4.000" against a true +1.917. Testing the tool on
that same file then exposed a bug in the tool itself -- it called the
saturation "negligible" because only 0.141% of the *frame* was at the rail,
while coverage was 0.7%, so **a fifth of every reading present was clipped**.
Saturation has to be judged against live texels. It also found 3.1% clipping
in an `A6` run I had already treated as clean.

**T2.2 -- Ladder rungs in the 0.3-2 px/interval^2 band.** The band real
footage actually occupies, currently sampled only incidentally by `O5`'s low
points -- which is why the low end took this long to characterise. Without
these rungs, N:N progress is not measurable, and every Tier 1 claim about the
low end rests on two frames of one scene. **Arguably this should be promoted
above T1.1**: it is the ground truth the whole N:N case will be judged
against, and the methodology's own first rule is ground truth before opinions.

**T2.3 -- A causal, backward-only variant. CLOSED by argument, not built.**
The claim here was that a causal window "removes the lag". It does not, and
the reason is structural: a quadratic's second derivative is a *constant*, so
a 3-point fit yields one acceleration for the whole window, and the centre is
only the instant at which that constant best approximates a varying truth.
Counting information age from the newest sample each window consumes:

| window | describes | needs frame | age |
|---|---|---|---|
| centred `{k-1, k, k+1}` | instant `k` | `k+1` | **1 frame** |
| causal `{k-2, k-1, k}` | instant `k-1` | `k` | **1 frame** |

Identical -- they are the same estimator relabelled. Extrapolating does not
help either, since the value extrapolated is constant across the fit. **Three
samples are what it costs to see curvature, and one frame of age is the change
owed on that.** A genuinely current acceleration requires modelling how
acceleration is changing, which is a cubic, which is a fourth frame. Full
argument in [TRIDIRECTIONAL.md](TRIDIRECTIONAL.md).

---

## Tier 3 -- leaps, weeks (T3.1 excepted -- see above)

**T3.1 -- Four frames. DONE -- built, calibrated, and every pre-registration
resolved.** `quaddirectional-interpolation.glsl`, 68 passes, generated by
`tests/gen_quaddirectional.py` (which imports the tri generator's machinery);
full hypothesis, algebra, pre-registrations and results in
QUADDIRECTIONAL.md. The measured summary: P1 held to the digit (the N:N
acceleration field is IDENTICAL to tri's, every case, every frame -- the
stencil algebra said the fourth frame cannot touch it, and it did not); the
jerk field is real and calibrated (8.2% at the O5 jerk peak, 3.4% on O6,
with an acceleration-dependent noise floor mapped on the nulls) [2026-09-01:
those jerk percentages and the noise-floor story were an INSTRUMENT
artifact -- the truth model compared a discrete third difference against a
continuous derivative at the wrong instant; the field is actually good to
a few % of peak across the whole cycle, sub-1% via the Metal port. See
QUADDIRECTIONAL.md's CORRECTION section]; placement
gained +1.10 dB on O3_osc_hard exactly as pre-registered, after the jerk
deadband was widened to 3.0/6.0 (the accel deadband lesson one order up --
sqrt(11/2) noise amplification measured as 4.9 dB of L1 cost at the
inherited band); the LSQ arm decided the fork (cubic default: least squares
collapses to 94% error at the jerk peak where the quadratic model is false,
while the cubic stays at 11.2%); and the ctrl invariant held
interior-exactly, 55/60 frames to the decimal, the other five being the
clip-edge frames where a 4-frame window cannot form. Cost: ~12% slower than
tri. Originally promoted by T0.3 and sharpened by the prior-art survey
(PRIOR-ART.md): Two things the stencil algebra fixes in advance:

- At the symmetric N:N window, `a = d(+1) + d(-1)` cancels every odd-order
  term -- constant jerk cannot bias the centred estimate, and a cubic fit
  through `d(-1), d(+1), d(+2)` returns the *identical* anchor acceleration.
  So the four-frame shader should NOT be expected to improve the N:N field's
  accuracy on smooth content. Its gains are pre-registered elsewhere: the
  jerk field itself, the fit residual as a per-texel *measured* confidence
  signal, and cubic placement at 24->60, where the stencil is asymmetric and
  jerk does not cancel. If the `O5` frame-10 residual does not move, that is
  the algebra talking, not a failure -- the sinusoid's zero crossing is also
  its *velocity maximum*, a third welded variable, and the control is a scene
  separating |v| from jerk.
- The fourth frame is a fork with both arms in the record: least-squares
  QUADRATIC over three flows (EQVI's RQFP -- redundancy spent on consistency)
  against an exact CUBIC (All-at-Once -- redundancy spent on jerk). Build the
  generator to emit both and measure; nobody in the record reads the
  least-squares residual back as a confidence field, which is the arm that
  serves the instrument.

It was already the *necessary* step for a second, independent reason:
three frames cannot validate an acceleration estimate (proved in
[TRIDIRECTIONAL.md](TRIDIRECTIONAL.md)), and four give two independent
estimates that can be checked against each other. That would replace the
round-trip trust heuristic with a **measured** confidence signal -- the thing
standing between this field and being a real instrument. The architecture is
already the right shape (slot-keyed, adjacent-slot chains), and the caching
generalises without a patch change.

**T3.2 -- Real-footage decimate-and-reconstruct for the field.** The
equivalent of the synthetic ground truth, on material that actually exercises
the 0.55-1.5 band.

**T3.3 -- Regenerate `-diffuse-dual`.** The strongest dangling lead in the
whole project, with a specific prediction already attached -- but it is a
*bidirectional* result on a parallel track, and it should not be allowed to
absorb the tridirectional effort.

---

## The order, after Tier 0 rewrote it

Tier 0 cost a few hours, closed two register entries, built five scenes and
**inverted the ranking**. The revised order:

1. **T3.1, four frames.** Promoted from the expensive leap to the indicated
   fix. Everything measured points at the three-frame model, not at precision,
   not at any coefficient. *Prediction:* on `O5` frame 10 -- matched
   magnitude, maximum jerk -- a degree-3 fit closes most of the gap between
   60.6% and the 5.2% `O6` already achieves at low jerk. *Stopping rule:* if
   it does not, the error is not jerk either and the diagnosis needs redoing
   before any more estimator work.
2. **Finish Tier 0's remainder** -- `R2`/`F2` calibration, then T0.4/T0.5/T0.6.
   Hours each, and each most likely closes as "already correct", which is a
   fine outcome.
3. **T2.2 is done early and for free** -- the low-band rungs exist now, as
   `A4`-`A7` and `O6`. This was the plan's biggest measurement gap.
4. **T1.1 and T2.1 after**, judged on `A4` and on whatever four frames leaves
   behind.
5. **T1.3** (`L1` regression) any time -- it is cheap and independent.

The methodology's trigger still stands for whatever comes next: **if a series
of incremental fixes each work slightly and none work well, the model is
wrong, not the parameters.** Tier 0 reached that conclusion without having to
exhaust the parameters, by building the control that separated two variables
one scene had welded together. That is the cheaper route to the same place,
and it is the one to reach for again.
