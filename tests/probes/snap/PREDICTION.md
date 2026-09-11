# Is snap a readable field? The prediction, written before the measurement

2026-09-08, pre-registered the way this project pre-registers (the foresight seed's table was written
before its first run). The owner asked for "human-reading fields for any relevant fields missing (jerk -
snap - crackle - pop - whatever)". Snap is the fourth derivative of position; the quint already computes
it and throws it away.

## What each window can carry

A window of N frames gives N-1 displacement links, and a polynomial through them has N-1 coefficients.
So the highest derivative a window can represent at all is:

| frames | links | fit | highest derivative | in this repo |
|---|---|---|---|---|
| 2 | 1 | linear | velocity | the bidirectional family |
| 3 | 2 | quadratic | acceleration | the tridirectional |
| 4 | 3 | cubic | jerk | the quaddirectional (the demo's shader) |
| 5 | 4 | quartic | **snap** | the quintdirectional (solves it, uses it only as an alarm) |
| 6 | 5 | quintic | **crackle** | the sextdirectional |
| 7 | 6 | sextic | **pop** | does not exist; the record's seven-frame analysis says degree 4 is the only worthwhile form |

So snap needs the quint and crackle needs the sext: both already exist. Nothing new has to be built to
try. That is why this is a measurement and not a project.

## The prediction

Signal. For an oscillation A sin(ωt) the k-th derivative has amplitude A ω^k. The measurement scene is
O2_osc_medium: A = 20 px, ω = 15.708 rad/s, which at 24 fps is w = 0.6545 rad per frame. So per frame^k:

| field | amplitude |
|---|---|
| velocity | 13.09 px/frame |
| acceleration | 8.57 px/frame² |
| jerk | 5.61 px/frame³ |
| snap | 3.67 px/frame⁴ |

Each order costs a factor w = 0.65.

Noise. The k-th derivative is the k-th finite difference of the links, whose coefficients are the binomial
row: acceleration (1, −2, 1), jerk (1, −3, 3, −1), snap (1, −4, 6, −4, 1). If each link's flow error were
independent with standard deviation σ, the difference amplifies it by the row's Euclidean norm:

| field | row norm | amplification |
|---|---|---|
| acceleration | √6 | 2.45 σ |
| jerk | √20 | 4.47 σ |
| snap | √70 | 8.37 σ |

The errors are NOT independent — the estimator's sub-pixel bias is phase-locked to the texture and adds
rather than cancels in the even orders (measured on a static scene in the demo's defect list: acceleration
0.52 px rms, jerk 0.54) — so this is a lower bound on the noise, and the even orders should do worse than
it says.

Together: **each derivative order costs about 2.9× in signal-to-noise** (0.65 in signal, 1.87 in noise).

**So the prediction is: on O2, if jerk reads at a signal-to-floor ratio of about 10, snap reads at about
3.5 — visible on a strong, smooth motion and lost on anything ordinary.** Concretely, before seeing the
numbers:

1. the snap field will correlate with the analytic snap (correlation above 0.7), so it is a real signal
   and not noise;
2. its least-squares gain will be BELOW 1 (the quint's trust gates and the ACCEL_TRUST/snap clamp pull the
   estimate toward the cubic wherever the far links are not believed, which is a deliberate attenuation,
   not an error);
3. its noise floor will be roughly twice the jerk's;
4. the peak-signal-to-floor ratio will land between 2 and 5.

If (1) fails, snap is not readable at all and the answer to the owner is a clean no with a number. If (4)
lands above 5, a snap reading is worth offering on the quint. If it lands below 2, crackle on the sext is
not worth measuring, because it would be another 2.9× down.

## What the answer is worth either way

The finding is the deliverable, not the feature (the owner's own rule: "an exploration of a hypothesis does
not necessarily mean we do the work — reporting findings is often worth more"). A number for where the
derivative ladder runs out is a better answer to "jerk, snap, crackle, pop" than a menu entry painting
noise.
