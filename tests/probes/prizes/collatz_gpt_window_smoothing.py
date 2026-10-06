"""G82 LW1-LW2; preregistered at42e96b1.
LW1 MUST HOLD: all future strings T1..12,r0..T,K1..h, exact window
identity and independent-prefix convolution; TV <= exact disagreement.
K>=8 geometric bound checked; retain vacuous bounds.
LW2 MUST HOLD: exact binomial first differences n0..256; h4096/8192
chosen windows <=h/2, atom/curvature bounds nonvacuous (arithmetic only).
CF: omit suffix count S_K in retained shift; MUST FAIL T3,r2,K1.
REFUTED-BY: actual demand constant2, erroneous shift2+b.
OUTCOME 2026-10-06, GPT Intel Python, about1 s:
LW1 PASS163872 identities/364 exact convolution-TV checks; all35
small-window geometric bounds vacuous. LW2 PASS257 exact gradients.
Arithmetic h4096,K1065: atom0.01816, curvature0.001319; h8192,K1154:
atom0.01192, curvature0.0005683, double precision, not measurements.
CF REFUTED. No actual-start or Local h200/300 rerun.
"""
from collections import Counter
from itertools import product
from math import ceil, comb, exp, log, sqrt
from fractions import Fraction
from collatz_gpt_boundary_loss import threshold


def reverse_summary(bits, T):
    s = R = 0
    out = [(0, 0)]
    for k, b in enumerate(reversed(bits), 1):
        s += b
        R = max(R, s-(threshold(T)-threshold(T-k)))
        out.append((s, R))
    return out


def main():
    identities = windows = tails = vacuous = 0
    for T in range(1, 13):
        for r in range(T+1):
            h = T-r
            if not h:
                continue
            exact, approximate, disagreements = Counter(), {}, Counter()
            approximate = {K: Counter() for K in range(1, h+1)}
            for bits in product((0, 1), repeat=h):
                z, J = 0, threshold(r)
                for j, b in enumerate(bits, r+1):
                    z += b
                    J = max(J, threshold(j)-z)
                summary = reverse_summary(bits, T)
                assert J == threshold(T)-z+summary[h][1]
                exact[J] += 1
                for K in range(1, h+1):
                    s, RK = summary[K]
                    JK = threshold(T)-z+RK
                    assert JK == threshold(T)-sum(bits[:h-K])-s+RK
                    approximate[K][JK] += 1
                    disagreements[K] += J != JK
                    identities += 1
            denominator = 2**h
            for K in range(1, h+1):
                shifts = Counter()
                for suffix in product((0, 1), repeat=K):
                    s, RK = reverse_summary(suffix, T)[K]
                    shifts[threshold(T)-s+RK] += 1
                n = h-K
                convolution = Counter()
                for W, count in shifts.items():
                    for z in range(n+1):
                        convolution[W-z] += count*comb(n, z)
                assert convolution == approximate[K]
                tv = Fraction(sum(abs(exact[v]-approximate[K][v])
                                  for v in set(exact) | set(approximate[K])), 2*denominator)
                mismatch = Fraction(disagreements[K], denominator)
                assert tv <= mismatch
                if K >= 8:
                    eta = min(1, 64*exp(-K/32))
                    assert float(mismatch) <= eta+1e-14
                    tails += 1
                    vacuous += eta == 1
                windows += 1
    for n in range(257):
        p = [0]+[comb(n, j) for j in range(n+1)]+[0]
        differences = [abs(b-a) for a, b in zip(p, p[1:])]
        assert sum(differences) == 2*max(p)
        assert max(differences)*(n+1) <= 4*2**n
    arithmetic = []
    for h in (4096, 8192):
        K = ceil(128*log(h+1))
        assert 8 <= K <= h/2
        n = h-K
        eta = min(1, 64*exp(-K/32))
        atom, curvature = 1/sqrt(n+1)+eta, 4/(n+1)+2*eta
        assert atom < 1 and curvature < 1
        arithmetic.append((h, K, atom, curvature))
    correct, wrong = Counter(), Counter()
    for b in (0, 1):
        s, R = reverse_summary((b,), 3)[1]
        correct[threshold(3)-s+R] += 1
        wrong[threshold(3)+R] += 1
    assert correct == Counter({2: 2}) and wrong == Counter({2: 1, 3: 1})
    print('LW1 PASS', identities, 'window identities,', windows, 'convolution/TV checks;',
          tails, 'geometric comparisons,', vacuous, 'vacuous')
    print('LW2 PASS257 exact binomial gradient checks; arithmetic(h,K,atom,curvature):', arithmetic)
    print('Arithmetic uses double precision; not a distribution measurement')
    print('CF REFUTED: correct constant2 versus wrong2+b')


if __name__ == '__main__':
    main()
