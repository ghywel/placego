# The held anchor: what is wrong, and what the fix must do

Written 2026-09-09 BEFORE the change, from the before-measurement and the code, so the after-measurement can
falsify it rather than confirm whatever happens.

## The mechanism

The diagnostic field is built about an ANCHOR slot. Naturally the anchor is the straddling frame nearer the
output, `clamp(s <= 0.5 ? p : p + 1, 1, hi)`, where `p` is the lower straddler and `s` the phase within the
straddle interval. That flips within one window as `s` crosses 0.5, and the two slots carry flow stencils
with independent sub-pixel noise, so a live display strobes between two decorrelated fields at about 36 Hz.
`DIAG_HOLD_ANCHOR = 1`, which the reading tail sets, stops that by pinning the anchor to a LITERAL slot
index: 1 for the four-frame family, 2 for the five, 3 for the six.

A literal is only correct for the window it was chosen against. The reading is then reported at that slot's
instant, so the measurement stands at `rts_mix[anchor]` source intervals from the output.

## Where it stands now, measured, and the model that reproduces it

`phaseprobe.py` finds the instant by sweeping an assumed offset and correlating against the analytic
derivative — it reads none of the shader's own logic, so it cannot inherit its assumption.

| shader | rate | acceleration delta | velocity delta (control) |
|---|---|---|---|
| quad | 24 -> 24 | **-1.00** | +0.50 |
| quad | 24 -> 60 | **-0.60** | +0.10 |
| quint | 24 -> 24 | -0.00 | +0.50 |
| quint | 24 -> 60 | -0.00 | +0.10 |
| sext | 24 -> 24 | -0.50 | +0.50 |
| sext | 24 -> 60 | -0.15 | +0.10 |

The arithmetic reproduces the quad's two numbers exactly, which is why the model is believed. At 24 -> 60
the phases cycle through {0, 0.4, 0.8, 0.2, 0.6}. At every interior phase the window is [-1, 0, +1, +2], so
`p = 1` and the held anchor 1 sits at `-phase`. At phase 0 the window shifts to [-2, -1, 0, +1] and `p = 2`,
but the anchor is still pinned to 1, which is now a whole interval before the output. Mean over the five
phases: (-1 - 0.2 - 0.4 - 0.6 - 0.8) / 5 = **-0.60**, and at N:N every frame is phase 0, so **-1.00**. Both
match the measurement to the resolution of the sweep.

**The velocity control behaves as the record says it should** and is not evidence of a fault: velocity is the
straddle pair's own forward flow and never touches the anchor, so its +0.50 at N:N is the chord n -> n+1
measured at its midpoint, exactly the N:N convention the record already documents.

## The two families that are NOT broken, and why the commit's "all 25 shaders" is too wide

The M-series commit proposed pinning to the straddle pair's lower slot everywhere. Measurement says only the
four-frame family needs it.

- **The quint is already correct at both rates.** Its window itself shifts at phase 0.5 (five frames lean
  toward whichever side the output is nearer), so the fixed slot 2 IS the nearer straddler at every phase,
  and the switch happens on a window advance rather than within a window: no strobe and no bias. Pinning it
  to `p` instead would give `-phase` at every interior phase and make it WORSE, about -0.40.
- **The sext's -0.50 at N:N is its documented definition, not a defect.** `SEXT_CENTRED = 1` fits about the
  weighted centre of the points in use, and the shader's own comment says acceleration and jerk are then
  reported at the centre instant, "half an interval before the anchor at N:N". That is exactly -0.50.

So the change is to the four-frame family only: five shaders, two occurrences each (the main pass and the
tail's cloned field pass), and one generator line. No `-4k` build carries an anchor.

## The fix, and its predictions

`anchor = 1` becomes `anchor = clamp(p, 1, 2)` — the straddle pair's lower slot, which is a function of the
window alone and so still cannot strobe within one.

1. quad at 24 -> 24: **-1.00 becomes 0.00**. At N:N `p = 2` and slot 2 is the frame the output sits on.
2. quad at 24 -> 60: **-0.60 becomes -0.40**. Only phase 0 changes; the four interior phases keep `p = 1`
   and are untouched.
3. quint and sext: **unchanged**, because they are not edited.
4. velocity, every shader, both rates: **unchanged**, because it never reads the anchor. If this moves, the
   edit did more than intended and must be reverted.
5. the picture path: **byte-identical**. The edited line is guarded by `TRI_DIAG != 0`, and the warp never
   sets it, so an ordinary interpolated render cannot change. This is the control that must not move, and it
   is checked by comparing rendered bytes, not by re-running the ladder.

## The residual, stated rather than hidden

-0.40 at 24 -> 60 is not a bug left in; it is the price of not strobing. The lower straddler is behind the
output by the phase, and no window-constant slot can track the nearest straddler when the window does not
itself shift at phase 0.5 — which is exactly the four-frame family's situation and not the quint's. The
honest options are to accept a known half-interval lag on a display, or to evaluate the fitted cubic at the
output instant instead of at the anchor (`a_out = a_anchor + jerk * (-rts_mix[anchor])`), which would remove
the offset using a quantity the shader already computes. The second is a change to what the field MEANS
across three families and is not part of this fix; it is recorded as an option.
