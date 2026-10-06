# Demand log-concavity needs a separate absorbing-edge inequality

*The waiting room (not yet verified). Derived from [PROOFS.md](../PROOFS.md), entry "G94. Demand log-concavity needs
a separate absorbing-edge inequality (2026-10-06)"; rebuild with `python3 proofs/build.py`. Edit the proof in
PROOFS.md and this summary in [summaries.md](summaries.md), never this file.*

**Status:** in the waiting room: stated with a proof, not yet checked by a second reader.

## In plain words

An induction proof for demand log-concavity must control the absorbing edge separately.

**What it says.** Away from the barrier, demand atoms undergo ordinary two-point averaging, which preserves log-concavity. At the edge an extra half of the first atom stays there. One explicit inequality among the first four future atoms is necessary and sufficient to preserve log-concavity when the future law is already log-concave.

**Why it matters.** A uniform four-atom synthetic law fails this edge inequality, so generic log-concavity cannot complete the proof. It is not an actual Collatz demand counterexample. The small finite evidence remains intact; the new target is the edge inequality for the real barrier schedule. Independent review and boundary controls remain pending.

**An everyday picture.** Averaging keeps a smooth pile smooth until material hits a wall and accumulates at its edge. That extra pile needs its own check.

## The formal statement and proof

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
