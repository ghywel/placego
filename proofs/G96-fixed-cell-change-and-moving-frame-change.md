# fixed-cell change and moving-frame change

*GPT's proofs, second-read. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT96. fixed-cell change and
moving-frame change (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

Watching one square change and following a moving pattern are different measurements.

**What it says.** These pages come from the owner's questions about clocks and about GPU "races" (CONSTELLATION rows
18 and 19): what happens when a computer updates Rule 30 in place and some squares read a neighbour that has already
been updated. They are about Rule 30 for its own sake, not directly about the prize. A pattern sliding along at a
steady speed changes at every fixed square, yet does not change at all if you move with it. GPT wrote both kinds of
change exactly. The change at a fixed square is Rule 210 applied to the row (C.8), though the pattern of changes
does not itself follow Rule 210.

**Why it matters.** It fixes which "change" an instrument measures before anyone reads physics into it.

**An everyday picture.** From the platform a passing train changes the view every moment; to a passenger looking
round the carriage, nothing changes at all.

## The formal statement and proof

### G96. Fixed-cell change and moving-frame change are different observables (2026-10-06)

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

**MC1-MC2 outcome (2026-10-06 19:16 BST).** Executed only after preregistration was published at e2c6a02. MC1 PASS: 504 ring rows and 1512 moving-frame cases. MC2 PASS: the padded derivative-dynamics guard and 168 dyadic worldline checks. The autonomous Rule210-change-field counterfactual fails at sites 0 and 1, as predicted; the tracked pulse has zero acceleration while its fixed-cell second difference is one. Finite controls support the implementation and examples, not an orbit-distribution or prize claim. Independent review remains pending.

*Second reader's note on G96 (Local, 2026-10-06; chat L051).* Correct. $D_v$ vanishes on any history translating at
speed $v$; the dyadic identity is squaring in characteristic two; the pull-back is a change of coordinates. Checked
(`rule30_audit_g95_g96.py`, V1 to V3): on every ring state of widths 3 to 12 and $v = -1, 0, 1$ the pulled-back step
equals the literal evolution over two steps, $F(x) \oplus x = R_{210}(x)$, and the right-step identity
$F(x)(i+1) \oplus x(i) = x(i+1) \vee x(i+2)$ of the moving-frame run holds exactly; the guards ($u_0$, $u_1$,
$R_{210}(u_0)$, the pulse) and the dyadic worldline identity for $k \le 3$ check. The scope point is right: the
velocity field does not evolve by Rule 210, and §8.70 does not say it does.
