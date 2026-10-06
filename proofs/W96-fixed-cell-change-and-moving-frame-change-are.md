# Fixed-cell change and moving-frame change are different observables

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G96. Fixed-cell change and
moving-frame change are different observables (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof
in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

Changing a fixed cell and following a moving pattern measure different things.

**What it says.** A difference taken along a constant-speed worldline vanishes on an exactly translating pattern, while a fixed-cell difference need not. Rule30 can be expressed in that moving frame by shifting its update. Its fixed-cell XOR change equals Rule210 evaluated on the state; the resulting change field does not itself evolve by Rule210, as a single-cell example shows.

**Why it matters.** The owner's shader-to-temporal-instrument connection needs a precise choice of observable. A passing pulse can have a nonzero fixed-cell second difference despite zero acceleration of its tracked position. These are scope identities and examples, not a Rule30 travelling-wave, prize or physical instrument claim. Small controls and independent review remain pending.

**An everyday picture.** A lamp moving steadily past a window changes what the window sees. Following the lamp separates that change from a change in its speed.

## The formal statement and proof

Follow the owner's temporal-instrument origin and Local's §8.70. For a binary history x_t(i), define Qx_t(i) = x_t(i+1), time shift Sx_t(i) = x_(t+1)(i), and, for fixed integer v,

    D_v = 1 + S*Q^v over GF(2),
    (D_v x)_t(i) = x_(t+1)(i+v) xor x_t(i).

D_0 is the fixed-cell XOR change. For x_t(i) = w(i-v*t), D_v x is zero everywhere, regardless of w; D_0 need not be zero. This is a generic exact-translation history, not a claimed Rule 30 solution. The dyadic identity is

    D_v^(2^k) = 1 + S^(2^k)*Q^(v*2^k),

by repeated squaring of the single linear operator S*Q^v in characteristic two. It compares cells along the same constant-speed worldline. No real-valued acceleration, physical unit, feature identity or noise model is asserted.

For an actual Rule 30 orbit with global map F, pull back to z_t(j) = x_t(j+v*t). Translation covariance gives

    z_(t+1) = Q^v*F(z_t),
    z_(t+1) xor z_t = Q^v*F(z_t) xor z_t.

Proof: at site j, x_(t+1)(j+v*(t+1)) equals F(x_t) at that site; replacing x_t(i) by z_t(i-v*t) gives F(z_t)(j+v). This is a change of coordinates, without treating the update rule as linear. At v = 0, §8.70 supplies F(x) xor x = R210(x).

**Unexpected derivative-dynamics guard.** Write u_t = F(x_t) xor x_t = R210(x_t). Its next value is R210(F(x_t)), not in general R210(u_t). For a single black cell at site 0, x_1 has black sites {-1,0,1}, so u_0 has {-1,1}. The next Rule 30 row has {-2,-1,2}, giving u_1 = {-2,0,1,2}. But applying Rule 210 to u_0 gives {-2,2}. The shortcut that the velocity field itself evolves by Rule 210 fails at sites 0 and 1. This clarifies the scope of the correct identity in §8.70; that section is not being accused of claiming the shortcut.

**Transport-versus-acceleration guard.** In the generic translating pulse x_t(i) = 1 exactly when i = t, the tracked position p_t = t has numerical velocity 1 and acceleration and jerk zero. At fixed site 0 the first three samples are 1,0,0: its second real finite difference is 1, and its second GF(2) difference is also 1. Along i = t every sample is 1, with zero differences. Thus fixed-cell second differences can reflect passage of a constant-speed pattern, not acceleration of that pattern. The example is a scope guard, not Rule 30 data or a PIV validation.

**MC1-MC2 preregistered NOT RUN.** MC1: every binary ring of widths 3 to 8, integer frames v = -1,0,1, compare literal Rule30 truth-table updates with both the transported update and moving-difference identities; separately require the v = 0 Rule210 identity. MC2: independently evolve the finite single-black-cell guard using padded direct truth tables, and verify the fixed/tracked pulse differences and dyadic worldline identity through lag 8. Counterfactual that u evolves by Rule210 must fail at the stated sites. No centre-column rerun, shader edit or Local complexity job. Existing-record search found §8.70's fixed-cell identity but no moving-frame audit or claimed autonomous derivative law. Elementary shift algebra and the recorded truth tables; no novelty or prize claim. The next question is which coherent structures and phase coordinates justify a tracked observable in actual Rule30 dynamics.

Probe: `tests/probes/rule30_gpt_moving_frame.py`. Independent Local reading requested.
