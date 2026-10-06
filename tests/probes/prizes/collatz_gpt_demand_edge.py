"""G94 BC1-BC2: publish before running. NOT RUN.
BC1 MUST HOLD: independently enumerated T1..8,r1..T-1 demand laws
satisfy the absorbing-edge operator, critical/noncritical cases retained.
BC2 MUST HOLD: uniform four-atom synthetic input is log-concave but
folded output is not; q0=0 has ordinary averaging without extra edge mass.
UNEXPECTED CHECK: synthetic edge deficit is exactly 1/32.
COUNTERFACTUAL MUST FAIL: generic log-concavity survives the edge fold.
REFUTED-BY: a boundary-operator mismatch or a nonnegative guard deficit.
No actual-start ensemble, large profile search or shape theorem.
OUTCOME 2026-10-06, GPT Intel Python, under one second:
BC1 PASS 28 independent boundary operators: 19 critical, 9 noncritical.
BC2 PASS synthetic deficit -1/32 and critical ordinary-averaging guard.
Generic log-concavity-preservation counterfactual REFUTED; no control failed.
Predictions and script at fea12c1 via 5854db3 before execution.
"""
from fractions import Fraction
from collatz_gpt_boundary_loss import threshold
from collatz_gpt_demand_shape import enumerated


def fold(q, lower, upper):
    p = {a: Fraction(0) for a in range(upper+1)}
    p[lower] = q.get(lower, Fraction(0)) + q.get(lower+1, Fraction(0))/2
    for a in range(lower+1, upper+1):
        p[a] = (q.get(a, Fraction(0))+q.get(a+1, Fraction(0)))/2
    return p


def main():
    critical = noncritical = 0
    for T in range(1, 9):
        for r in range(1, T):
            q = enumerated(T, r+1)
            p = enumerated(T, r)
            assert fold(q, threshold(r), T+1) == p
            if threshold(r+1) > threshold(r):
                critical += 1
                assert q[threshold(r)] == 0
            else:
                noncritical += 1
    q = {j: Fraction(1, 4) for j in range(4)}
    assert all(q[j]**2 >= q[j-1]*q[j+1] for j in (1, 2))
    p = fold(q, 0, 4)
    assert [p[j] for j in range(4)] == [Fraction(3,8),Fraction(1,4),Fraction(1,4),Fraction(1,8)]
    deficit = p[1]**2-p[0]*p[2]
    assert deficit == Fraction(-1, 32)
    critical_q = {0: Fraction(0), 1: Fraction(1, 3),
                  2: Fraction(1, 3), 3: Fraction(1, 3)}
    critical_p = fold(critical_q, 0, 4)
    assert all(critical_p[j] == (critical_q.get(j, 0)+critical_q.get(j+1, 0))/2
               for j in range(5))
    print('BC1 PASS:',critical+noncritical,'future-string boundary operators;',
          critical,'critical,',noncritical,'noncritical')
    print('BC2 PASS: synthetic fold deficit -1/32; critical operator ordinary averaging')
    print('Generic log-concavity-preservation counterfactual REFUTED')
    print('No counterexample to the actual Collatz demand law inferred')


if __name__ == '__main__':
    main()
