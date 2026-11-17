"""G78 PC1-PC2, preregistered at14fde39.
PC1 MUST HOLD: m1..8,T=m..24, exact backward proxy agrees with
independent forward counts/tail moments, including T=m and lower bound.
PC2 MUST HOLD: coin DP m1..32,T=8*m gives U/Q>m; m2,T5 direct guard.
CF: ideal coin full-class proxy equals signed discrepancy0; MUST FAIL.
REFUTED-BY: m2,T5 Q1/2, proxy3/4, normalized proxy3/2.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
PC1 PASS164 exact proxy/moment identities, including8 empty tails.
PC2 PASS32 exact strict linear-horizon bounds and direct four-word guard.
CF REFUTED: ideal signed error0 versus proxy3/4. No actual-start scan.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from collatz_gpt_backward_weights import backward
from collatz_gpt_boundary_loss import admissible, threshold


def classes(T):
    counts = {0: 1}
    rows = [counts]
    for t in range(T):
        following = Counter()
        for a, n in counts.items():
            for b in (0, 1):
                if 3**(a+b) >= 2**(t+1):
                    following[a+b] += n
        counts = following
        rows.append(counts)
    return rows


def tail_moment(m, T):
    counts = classes(m)[-1]
    moments = {a: 0 for a in counts}
    for t in range(m, T):
        following, next_moments = Counter(), Counter()
        for a, n in counts.items():
            for b in (0, 1):
                if 3**(a+b) >= 2**(t+1):
                    following[a+b] += n
                    next_moments[a+b] += moments[a]+b*n
        counts, moments = following, next_moments
    V, Z = sum(counts.values()), sum(moments.values())
    return V, Z, Fraction(2*Z-(T-m)*V, V)


def main():
    rows = classes(24)
    cases = boundary = 0
    for m in range(1, 9):
        for T in range(m, 25):
            f = backward(T)
            U = sum((Fraction(2**m*n, 2**(t+1))*(f[t+1][a+1]-f[t+1][a])
                     for t in range(m, T) for a, n in rows[t].items()), Fraction(0))
            V, Z, score = tail_moment(m, T)
            Q = Fraction(V, 2**(T-m))
            assert U/Q == score and score >= 2*threshold(T)-T-m
            if T == m:
                assert U == score == Z == 0
                boundary += 1
            cases += 1
    linear = []
    for m in range(1, 33):
        _, _, score = tail_moment(m, 8*m)
        assert score > m
        linear.append((m, score))
    tails = [w[2:] for w in product((0, 1), repeat=5) if admissible(w)]
    assert sorted(tails) == [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1)]
    V, Z, score = tail_moment(2, 5)
    Q = Fraction(V, 8)
    assert score == Fraction(3, 2) and Q == Fraction(1, 2)
    assert Q*score == Fraction(3, 4) > 0
    print('PC1 PASS', cases, 'exact proxy/moment comparisons;', boundary, 'empty-tail controls')
    print('PC2 PASS32 strict linear-horizon bounds; final m:', linear[-1][0])
    print('CF REFUTED: ideal fair discrepancy0, proxy3/4; tails:', tails)


if __name__ == '__main__':
    main()
