# SEXTDIRECTIONAL -- six frames, for the field

Built on the night of 2026-09-05 at the owner's request, from the quint's
generator by asserted substitution (`tests/gen_sextdirectional.py`), and
calibrated once. Everything here is that one night's measurement; the
pre-registration the other lines had, this one does not.

## What it is

The quint binds five frames and, at the exact N:N phase, fits the exact
quartic through the anchor's four displacements over a symmetric window
(taus -2, -1, +1, +2). That symmetric window exists because five is odd.
Six frames have no centre: at N:N the output sits at the end of its
straddle interval, on slot 3, with three links behind it and two ahead,
and at every other phase the anchor is slot 2 or 3 with the links split
3+2 or 2+3. So there is no symmetric stencil to solve exactly, and the
six-frame field is a WEIGHTED LEAST-SQUARES fit instead: every
displacement the window offers (taus -3..+3, the far ones composed from
adjacent links, each round-trip checked), weighted by its own round trip,
plus the anchor itself as a point at tau 0. Seven points, five unknowns
(a free constant, velocity, acceleration, jerk, snap), the leftover as a
per-texel RESIDUAL in mode 6 -- the confidence channel the quad had at
four frames (its mode 1) and the quint gave up.

The picture is the quad's cubic placement on the four slots around the
output, as the quint's is. Fewer than four trusted links: the quad's cubic.

## The one thing that had to be learned

Fitted at the anchor, the lopsided stencil leaves an odd-order truncation
bias. On O9_osc_tex_fast (8 samples per period, amplitude 3.70 px per
interval squared), scored against the continuous acceleration at the
anchor's instant over frames 4-20 at N:N:

| estimator | RMS error | error at the zero crossings | IQR at the peaks |
|---|---|---|---|
| quint, exact symmetric quartic | 0.051 | +0.03 | 0.24 |
| six-frame, quartic fitted at the anchor | 0.162 | +-0.20, alternating | 0.13 |
| six-frame, quartic fitted about the window's centre | 0.066 | +-0.02 | 0.13 |

The quint's number reproduces its published 0.050. The uncentred
six-frame fit has half the quint's noise and three times its error,
because the asymmetry of three-behind-two-ahead puts the fifth
derivative into the acceleration at every zero crossing. Fitting about
the weighted centre of the points in use (`SEXT_CENTRED = 1`, the
default) makes the stencil symmetric -- taus -3..+2 about -0.5 -- and
the odd orders cancel: the error falls to 0.066, within a third of the
quint's, with the noise still halved. The price is definitional: the
centred fit reports acceleration and jerk at the CENTRE instant, half an
interval before the anchor at N:N, and a reader of its field must know
that. `SEXT_CENTRED = 0` fits at the anchor like the quint.

So on the quint's own showcase the quint is still the more accurate
estimator by a third and the six-frame the quieter by half. Where that
trade lands on slow, noisy motion -- the regime where a second link on
each side should pay -- is unmeasured.

## What else was measured

- Picture: on L1_trans_8px, A5_accel_tex_a067 and R3_rot_tex the
  interpolated frames equal the quad's on 49 of 60, differing at the
  window's head and tail and on a handful of mid-stream frames where the
  wider window gives the anchor real far links.
- Skips: a six-frame window skips three boundary outputs on this host
  (one at the head, two at the tail) where the quad and quint skip one or
  two. `bench.sh` reads `SKIPS_ALLOWED` (default 2) for that; run the
  six-frame shader with `SKIPS_ALLOWED=3` and treat a fourth skip as the
  alarm it is.
- Time, 1080p from a file, 60 output frames: quint 4.11 s, six-frame
  4.83 s (+17%; 127 passes against 106).
- Final pass: 15 binds of the 16 allowed (six frames, the cut statistics
  in a 2x1 texture, three half-res packs, five full-res packs).

## Owed

The field on O6 and O10 and the rest of the field cases; the full
32-case ladder; real footage; the residual's calibration as a confidence
signal (mode 6 exists and is unmeasured); a host lookahead sized for six
frames so the tail skips go; and a pre-registration written before any
of that, which this line never had.
