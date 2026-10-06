# the absorbing-edge inequality, which fails from horizon 65

*GPT's proofs, second-read by Local. Derived from [PROOFS.md](../PROOFS.md), entry "G.GPT94. the absorbing-edge
inequality, which fails from horizon 65 (second-read by Local, 2026-10-06)"; rebuild with `python3 proofs/build.py`.
Edit the proof in PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** proved by GPT and second-read by Local.

## In plain words

A smooth-shape argument fails: the coin weights stop being a smooth single hump beyond 64 steps.

**What it says.** One hoped to prove that the coin weights always form a smooth single hump (in the jargon,
log-concave), since ordinary averaging keeps that shape. At the survival boundary an extra piece stays put, and GPT
found the exact condition for the shape to survive there. Local then checked the real boundary: the shape holds in
every case up to 64 steps, fails beyond, first at 73, and always at the edge, never in the middle.

**Why it matters.** It closes the route, and records exactly where and why it breaks.

**An everyday picture.** A sandpile shaken against a wall stays a smooth mound in the open, but sand piling up
against the wall can form a shoulder.

## The formal statement and proof

### G94. Demand log-concavity needs a separate absorbing-edge inequality (2026-10-06)

G93's finite profiles suggest log-concavity, but induction from arbitrary log-concave future laws fails. Fix r < T and l = ell_r. Write q_j for the demand atom at time r+1 and count l+j, putting missing atoms equal to zero; support begins at ell_(r+1), so q_0 = 0 at a critical threshold increment. Let p_j be the demand atom at time r and count l+j. The exact backward recurrence gives

    p_0 = q_0 + q_1/2,
    p_j = (q_j+q_(j+1))/2 for j >= 1.

Proof: f_r(a) = (f_(r+1)(a)+f_(r+1)(a+1))/2 for a >= l, while f_r(l-1) = 0. Differencing gives the interior rule; at the edge f_(r+1)(l) = q_0 and f_(r+1)(l+1) = q_0+q_1, yielding p_0. This is the demand distribution of G74, not an actual-population transition.

Assume q is log-concave with no internal support gaps. Ordinary two-point averaging preserves log-concavity away from the absorbing edge. Indeed, with s_j = q_j+q_(j+1),

    s_j^2-s_(j-1)*s_(j+1)
      = (q_j^2-q_(j-1)*q_(j+1))
        + (q_(j+1)^2-q_j*q_(j+2))
        + (q_j*q_(j+1)-q_(j-1)*q_(j+2)) >= 0.

The last term is nonnegative by the ordered adjacent ratios of a log-concave sequence, with zero-end cases checked directly. Thus all new interior inequalities from j = 2 on follow. The remaining edge inequality, at j = 1, is exactly

    (q_1+q_2)^2 >= (2*q_0+q_1)*(q_2+q_3).

There are no newly created internal gaps; the inequality at j = 0 has zero left neighbour and is automatic. Consequently, given log-concave q, this one edge inequality is necessary and sufficient for p to be log-concave. At a critical increment q_0 = 0 and ordinary averaging supplies it. At a noncritical step it is a genuinely additional condition.

**Unexpected synthetic guard, not a Collatz demand law.** Take q_0 = q_1 = q_2 = q_3 = 1/4 and all other atoms zero. It is log-concave. A noncritical absorbing step gives p = (3/8,1/4,1/4,1/8). But p_1^2 = 1/16 < p_0*p_2 = 3/32. The edge condition fails (left side 1/4, right side 3/8). Hence generic log-concavity alone cannot prove G93's proposed shape by induction. This does not refute the actual demand law: a uniform four-atom future law is not claimed to arise from its particular barrier schedule. The next missing statement is the extra edge inequality for the actual sequence of thresholds.

**BC1-BC2 preregistered NOT RUN.** BC1: independently enumerate future coin strings for T = 1 to 8 and r = 1 to T-1, require the edge/interior operator above to reproduce each preceding demand distribution, retaining critical and noncritical cases separately. BC2: exact synthetic uniform guard must refute generic preservation; the critical version with q_0 = 0 must reproduce ordinary averaging without an extra edge mass. These test the new boundary operator, not a repeat of G93's horizon-64 shape search. No new population, colleague job or global count estimate. The proof is elementary differencing and sequence algebra; no external novelty claim. Independent review requested.


### G94 absorbing-edge controls outcome (2026-10-06)

BC1 passes 28 independently enumerated future-string boundary operators, split into 19 critical and nine noncritical steps. BC2 verifies the synthetic noncritical deficit -1/32 and critical ordinary-averaging identity. The generic log-concavity-preservation counterfactual is REFUTED; no control failed. Predictions and script at fea12c1, published via 5854db3 before execution. GPT Intel Python, under one second. No actual demand log-concavity counterexample or population estimate is inferred; the extra edge inequality for the true threshold schedule remains open. Independent proof review pending.

Probe: `tests/probes/prizes/collatz_gpt_demand_edge.py`.


*Second reader's note on G94 (Local, 2026-10-06; chat L048).* Correct, and sharp on the actual schedule. The
recurrence follows from the backward weights ($f_r(\ell_r - 1) = 0$, $f_{r+1}(\ell_r) = q_0$); the three-term
identity expands as stated; for log-concave $q$ the only new condition is the edge triple, $p_1^2 \ge p_0 p_2$, which
is $(q_1 + q_2)^2 \ge (2q_0 + q_1)(q_2 + q_3)$; the synthetic guard checks. Measured (`collatz_audit_g93_g94.py`,
E0 to E3, predictions at 87f0571): G93's log-concavity holds for the 2,080 laws with $T \le 64$ but FAILS beyond,
against my blind prediction: 48,727 of the 524,800 laws with $T \le 1024$ are not log-concave, the first at $T = 73$,
$r = 8$ (a noncritical step, $\ell_8 = \ell_9 = 6$; the law at time 9 log-concave; $p_1^2 - p_0 p_2 = -9.9 \times 10^{-8}$, re-checked in exact fractions by separate code). Every violation is G94's edge triple, right after a
noncritical step, with remaining horizon at least 65; no interior triple fails. So the edge inequality is the exact
place where the shape breaks, and an allocation argument may use log-concavity away from the edge atom only (the
measured statement, through $T = 1024$).
