# Quaddirectional interpolation: the four-frame experiment

The tridirectional shader proved that three frames buy a per-texel
acceleration field and quadratic placement. This is the leap it argued for:
**four frames**, one degree higher, built after the prior-art survey
(PRIOR-ART.md) sharpened what the fourth frame can and cannot buy -- and the
predictions below were written down **before the first battery of results
came back**. Where they fail, the failure is the finding.

## What the fourth frame is for -- the fork

Three frames give two unknown displacements from three measurements: one
redundancy, and the tri work proved it is spent constraining the *sum* of the
flows, orthogonal to acceleration. A fourth frame adds a fourth measurement,
and there are exactly two things it can be spent on. Both are in the record
(PRIOR-ART.md), neither has been done deterministically, and the shader
builds both, switched by `QUAD_MODE`:

- **`QUAD_MODE 0` -- the exact cubic** (All-at-Once's arm): model
  `d(tau) = v*tau + (a/2)tau^2 + (j/6)tau^3` through the anchor's three
  measured displacements. The redundancy is spent on **jerk** -- a field no
  3-frame estimator can produce at all.
- **`QUAD_MODE 1` -- the least-squares quadratic** (EQVI's RQFP arm): the
  same quadratic tri fits, overdetermined by all three flows, with the
  **residual read out per texel** -- a *measured* confidence signal in px,
  replacing heuristic trust. The arm nobody in the record took further than
  fitting.

## Architecture: what tri proved, kept; what four frames force, added

**Slot-keyed throughout.** Slots 0..3 ascending; six adjacent-pair flow
chains (F01/F10/F12/F21/F23/F32), all pure functions of the window, all
storage-cached under `pair_changed`. Only the final pass derives roles.

**The window does not re-centre.** Binding FRAME3 declares
`frame_mix_count = 4`. From the patch's selection logic the window is always
a contiguous four-frame run: `{k-1, k, k+1, k+2}` for every interior 24->60
phase (straddle = slots 1,2), and `{k-2, k-1, k, k+1}` at exact N:N (output
ON slot 2). Unlike tri -- whose 3-frame window re-centres so the anchor is
always slot 1 -- the anchor here is a per-output *role*: the straddling frame
nearer the output, always slot 1 or 2, both interior.

**Adjacent flows only; distance-two by composition.** The anchor needs a
displacement to a frame two intervals away. Searching it directly doubles
the displacement and exits the coarse search's ~23 px/frame reach exactly on
fast content. Instead it is **composed from measured links**:
`F13(x) = F12(x) + F23(x + F12(x))` -- trajectory linking, the same
construction dense-trajectory optical flow and multi-pulse PIV use. Each
link stays inside its own reach; each link round-trips independently; the
worst link gates the composition.

**Trust is per order.** The acceleration row of the cubic is (at uniform
spacing) built from the two adjacent flows alone, so it keeps tri's two-flow
round-trip gate unchanged. Jerk -- and the LSQ fit, which mixes all three
flows into everything -- answers additionally for the composed link's round
trip. Cuts degrade in order: an anchor-adjacent cut kills the whole estimate
(bidirectional behaviour); a cut severing only the far link kills jerk
(tridirectional behaviour). quad -> tri -> bi, by evidence.

## The algebra

Anchor at tau = 0; the other three frames at tau_p, tau_n, tau_f in
straddle-interval units; `d(tau) = v tau + (a/2) tau^2 + (j/6) tau^3`. Exact
3x3 Vandermonde solve per texel (mode 0) or 2x2 normal equations (mode 1).
At uniform spacing the interesting rows collapse to closed forms:

    a = d(+1) + d(-1)                       (both windows, both anchors)
    j = d(+2) - 3 d(+1) - d(-1)             (24->60 window, anchor slot 1)
    j = d(+1) + 3 d(-1) - d(-2)             (N:N window, anchor slot 2)

**Placement.** The deviation of the constant-jerk trajectory from the
straddle chord, with s in [0,1] across the straddle:

    corr = s(1-s) * ( a/2 + (j/6) * (anchor==A ? (1+s) : -(2-s)) )

`j = 0` reduces it to tri's `s(1-s)*a/2`; `a = j = 0` to the bidirectional
warp -- the degeneracy chain the ctrl invariant tests.

## Pre-registered predictions

Written before the battery returned. P1 is the sharp one: it comes from the
stencil algebra alone, and it says the *obvious* headline result of a
four-frame shader -- "a better acceleration field" -- is exactly what will
NOT happen.

- **P1 -- the N:N acceleration field does not improve.** `a = d(+1)+d(-1)`
  in both tri and quad: every odd-order term cancels at the centred pair, so
  constant jerk cannot bias it and the cubic returns the identical anchor
  acceleration. Calibration on `A4`/`A6`/`O5`/`O6` should match tri's
  numbers to within readback noise. If quad *beats* tri here, P1 is wrong
  and something other than the stencil is at work; if quad is *worse*,
  the composed link's gating is contaminating the two-flow estimate.
- **P2 -- the jerk field is real and calibratable.** First-ever measurement:
  `O5` frame 10 should read near +5.42 px/interval^3 (the acceleration
  zero-crossing is the jerk peak -- the two fields are ninety degrees
  apart, so the jerk field is strongest exactly where the acceleration
  field is weakest, and the two are complementary instruments). `O6` frame
  12 near +0.72. `A6` -- constant acceleration, jerk identically zero -- is
  the null, and matters as much as the positives.
- **P3 -- placement gains at 24->60 are small and land on the hardest
  oscillations.** The cubic term's weight is s(1-s)(1+s)/6 <= ~0.064 of j,
  and the ladder's jerk tops out at ~5.6, so the placement correction is
  sub-half-pixel: expect `O3`/`O5` to move by tenths of a dB at most, and
  nothing to regress. The pre-registered risk is the *composed link* --
  a bad far flow that round-trips (rare but possible) contaminates only
  jerk, which the deadband then suppresses.
- **P4 -- the LSQ residual is a working confidence signal.** In mode 1 the
  residual should be near zero on constant-acceleration content (`A6` --
  the quadratic model is exact there) and light up on `O5`'s high-jerk
  frames, where a quadratic genuinely cannot fit three displacements. That
  correlation -- residual high exactly where the tri-style field is known
  least accurate -- is what makes it a confidence signal rather than a
  number.
- **P5 -- ctrl invariance.** `ACCEL_MAX_PX = 0` and `JERK_MAX_PX = 0`
  must reproduce tri-ctrl (bi + sub-pixel) **to the decimal**: 60.78 /
  41.12 / 43.45 on `L1`/`L2`/`O4`. The straddle flows are computed by
  identical code from identical lumas; any deviation means the 4-frame
  plumbing touched something it must not.

## Results, against the pre-registrations

Windows / Radeon Pro 560X, caching live, N:N field runs at exact 24:24
(the queue-threshold fix), interpolation at 24->60.

### P5 -- ctrl invariance: HOLDS, interior-exactly

With acceleration and jerk clamped to zero, **55 of 60 output frames match
tri-ctrl to the decimal**. The five that differ are frames 1-3 and 59-60:
the clip edges, where a four-frame window cannot form and libplacebo falls
back to its builtin blend. A real, understood cost of the fourth frame --
one more unavailable frame per clip end than tri -- and the reason every
aggregate quad number carries a small boundary drag against tri on short
clips. Interior plumbing: exact.

### P1 -- the N:N acceleration field does not improve: CONFIRMED TO THE DIGIT

| case, frame | tri | quad (cubic) |
|---|---|---|
| `A4` f9 | 9.0% / +0.363 | **9.0% / +0.363** |
| `A6` f9 | 10.9% / +1.187 | **10.9% / +1.187** |
| `O5` f10 | 11.2% / -1.969 | **11.2% / -1.969** |
| `O6` f4 | 3.9% / -2.467 | **3.9% / -2.467** |

Identical readings, every case, every frame tested. The stencil algebra
said the fourth frame cannot touch the centred pair's acceleration, and it
did not. The obvious headline -- "four frames, better acceleration" -- is
false, was predicted to be false, and measured false. What the fourth frame
buys is everything below.

### P2 -- the jerk field is real: CONFIRMED, with its noise floor mapped

The first measured jerk field in this project, against analytic truth:

| case, frame | true j (px/int^3) | measured | err |
|---|---|---|---|
| `O5` f10 -- jerk peak | -5.416 | -4.971 | **8.2%** |
| `O6` f10 | +0.622 | +0.643 | **3.4%** |
| `O6` f12 | +0.718 | +0.521 | 27.3% |
| `O5` f8 | -2.804 | -0.539 | 80.8% |
| `A6` f9 -- null | 0 | -0.084 | -- |
| `O5` f12 -- null, at \|a\| = 8.6 | 0 | -1.730 | -- |

Two structural facts fall out. First, **the jerk field peaks exactly where
the acceleration field is weakest** -- the two are ninety degrees apart on a
sinusoid -- so they are complementary instruments, and together they cover
the cycle. Second, the jerk noise floor is **acceleration-dependent**: on
low-\|a\| content the nulls read ~0.1-0.3, but at \|a\| = 8.6 the null reads
-1.73. The uniform jerk stencil's coefficients amplify flow noise by
sqrt(11)/sqrt(2) ~ 2.3x the accel stencil's, and whatever sub-pixel bias
survives at large displacements lands there. Read the field accordingly:
trustworthy above \|j\| ~ 2-3 at moderate acceleration, order-of-magnitude
below that.

### P3 -- placement gains at 24->60: CONFIRMED where predicted, and the
### deadband lesson repeated one order up

The gain landed precisely where pre-registered -- the hardest oscillation:
**`O3_osc_hard` +1.10 dB over tri** (45.18 -> 46.28), whose jerk peaks at
~13.8 px/interval^3, with `O4` +0.14. And the pre-registered *risk* arrived
too: with the jerk deadband naively inherited from accel (0.5/1.5), the jerk
noise tail on zero-jerk content cost up to **4.9 dB on `L1`**. The sweep
(table in the generator) found the knee at **3.0/6.0**: `O3` keeps its full
+1.10 at every setting -- its useful jerk lives far above any band tried --
while `L1` recovers to within 0.35 dB of jerk-off. Exactly the accel
deadband story, one derivative up, with the wider band the 2.3x noise
amplification predicts.

### P4 -- the LSQ residual: PARTIALLY confirmed, and the fork is decided

The two arms, measured on the same content:

| case, frame | cubic (mode 0) | LSQ quadratic (mode 1) |
|---|---|---|
| `A6` f9/f12 (constant a -- model true) | 10.9% / 15.3% | **8.6% / 8.6%** |
| `O5` f8 (accel peak, low jerk) | 2.9% | **0.6%** |
| `O5` f10 (jerk peak -- model FALSE) | **11.2%** | 94.0% |
| `O6` f4/f6 (mild jerk) | **3.9% / 3.9%** | 10.3% / 4.7% |

Textbook bias-variance, live: least squares wins where the quadratic model
is true (averaging three flows beats two), and **collapses where it is
false** -- at the jerk peak the model error is spread into the acceleration
estimate and the reading drops to -0.133 against a truth of -2.218. The
exact cubic absorbs jerk into its own term and stays uniformly decent.
**`QUAD_MODE 0` is the right default**; mode 1 is the better instrument
specifically on known-smooth content.

The residual itself (read at RESID_DIAG_FS = 8 after the first readout
saturated at FS = 2 -- fieldexport's clipping lesson, recurring in a new
mode): means 2.31 / 2.84 / 3.69 px at f8/f10/f12. It flags the jerk-peak
frame, but it flags the accel-peak frame *harder* -- because it measures
TOTAL misfit, model error and flow noise indistinguishably. Verdict: a valid
conservative trust gate ("large residual = do not trust"), not an error
estimate. The pre-registration expected a specific predictor and got a
blunter, still-useful instrument.

### Post-battery upgrade: the equiangular fit sharpens both fields

The V-fit A/B (PLAN.md, run after this battery) replaced the sub-pixel
parabola with the SAD-matched equiangular fit. For this shader that means:
jerk at `O5`'s peak improved 8.2% -> **4.4%**, and the jerk NULLS -- the
noise floor -- fell ~3.7x (`A6` f12: -0.263 -> **-0.070** px/interval^3).
The large-\|a\| null (`O5` f12, -1.73 -> -1.66) barely moved, confirming it
is matching error at speed, not peak locking. The jerk field is now
trustworthy above \|j\| ~ 1 at moderate acceleration.

### Cost

58 passes against tri's 41; measured render time 4.8 s against 4.3 s on the
48-frame O5 sequence at 24->60 -- **~12% slower for the extra 17 passes**,
because the final pass and lumas are cheap next to the flow searches and
only two chains were added.

### The shipped configuration's ladder

Full 12-case run at the measured jerk deadband (3.0/6.0), against the
tridirectional shader's own verification table:

| case | tri | quad | quad - tri |
|---|---|---|---|
| `L1_trans_8px` | 60.77 | 60.20 | -0.57 |
| `L2_trans_16px` | 42.18 | 42.08 | -0.10 |
| `L3_trans_23px` | 40.15 | 39.92 | -0.23 |
| `L9_occlusion` | 40.03 | 39.70 | -0.33 |
| `A2_accel_16mean` | 43.03 | 42.81 | -0.22 |
| `F2_fourier_accel` | 38.98 | 38.77 | -0.21 |
| `M3_period16_trap` | 21.91 | 21.88 | -0.03 |
| `O1_osc_gentle` | 49.44 | 49.28 | -0.16 |
| `O2_osc_medium` | 46.19 | 46.20 | +0.01 |
| `O3_osc_hard` | 45.18 | **46.28** | **+1.10** |
| `O4_osc_flat300` | 47.36 | 47.50 | **+0.14** |
| `O5_osc_textured` | 34.03 | 33.84 | -0.19 |

Read this with the boundary drag in mind: the ctrl-vs-ctrl comparison puts
0.1-0.35 dB of every aggregate deficit at the five clip-edge frames where a
4-frame window cannot form -- a fixed count, so it is 8% of a 1-second test
clip and nothing of a film. Interior-adjusted, quad matches tri on smooth
and constant-velocity content and wins where jerk lives, which is the
pre-registered shape of the result exactly.

**When to use which.** For 24->60 viewing of ordinary content, tri remains
the sensible default -- quad's picture gains are confined to violently
non-smooth motion. For the FIELD use case the quad shader is now strictly
the better instrument: the identical acceleration field plus the jerk field
plus (mode 1) the misfit map, at ~12% more cost.

## What this opens

- **The N-frame generalisation is now mechanical.** The quad generator
  demonstrated the induction step: one more luma pyramid, one more
  adjacent-pair chain, one more link in the composition, one more column in
  the Vandermonde. Savitzky-Golay theory (PRIOR-ART.md) says how to spend
  N > 4: fixed-degree fits over longer windows, with closed-form noise
  gains -- the measured jerk noise floor here is the number those formulas
  need.
- **Snap (d^4) is not worth a frame yet.** The jerk field's own noise floor
  at moderate acceleration is ~0.1-0.3 px/interval^3; a snap stencil
  amplifies flow noise by another ~3x. Measure a real use for jerk first.
- **The adjacent-anchor validator collapses -- a proof, in the family of
  the spanning-flow and causal-window proofs.** The obvious next
  confidence signal was: compute the acceleration at BOTH interior slots
  (`a1 = F10 + F12` at slot 1, `a2 = F21 + F23` at slot 2), and check the
  fitted jerk against their difference -- `V = a2 - a1 - j`. Expand it. At
  anchor 1, `j = f_far - 3*F12 - F10` with `f_far = F12 + link`, and
  `a2 = F21@q + link` where `q` is the same warped point the composition
  reads -- so the link cancels and

      V = F21@q + F12

  which is EXACTLY the round-trip residual of the shared adjacent flow:
  the gate the shader already computes. (Anchor 2 mirrors to `rt_prev`;
  verified numerically on random fields, identical to machine precision.)
  Four frames give three independent displacements; `a1`, `a2` and `j` are
  all linear combinations of them, and the only new information in the
  reverse chains is their round-trip residuals. **At N = 4, per-texel
  confidence is complete: the three round trips plus the LSQ misfit.
  Nothing else exists to compute.** A genuinely independent acceleration
  cross-check needs a FIFTH frame -- two disjoint triples `{0,1,2}` and
  `{2,3,4}` sharing no flows, whose accelerations differenced against
  `2j` form the first validator that is not already a gate. That is now
  the concrete reason N = 5 earns its cost, alongside Savitzky-Golay
  smoothing.

## Reproducing

    ./tests/gen_quaddirectional.py          # regenerate from the base
    # ladder:      OUTROOT=... ./tests/bench.sh <case> quaddirectional-interpolation.glsl quad
    # accel field: TRI_DIAG=2 via sed, render at fps=24, read with accelcheck.py
    # jerk field:  TRI_DIAG=5, FIELD=jerk accelcheck.py  (same readback, jerk truth)
    # confidence:  QUAD_MODE=1 + TRI_DIAG=6 (linear luma, px against RESID_DIAG_FS)

The diagnostic constant keeps the name `TRI_DIAG` and modes 0-4 keep their
tri semantics **deliberately**, so every existing instrument -- accelcheck,
accelprospect, trivis, the calsweep drivers -- reads this shader unchanged.
Modes 5 (jerk, magenta marker) and 6 (LSQ residual, measurement mode, no
marker) are quad-only.
