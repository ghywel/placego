"""G74 controls, preregistered at4a78c0b.
BW1 MUST HOLD: widths2..10, final horizons m..24: rational backward
weights, direct survivor states, increments, telescoping and bound agree.
BW2 MUST HOLD: T<=10, enumerated future-bit demand matches every weight.
CF: noncritical steps contribute nothing; MUST FAIL at width3,T4.
REFUTED-BY: the noncritical t2 term is1/4, equal to final discrepancy.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
BW1 PASS180 final horizons/1740 increments, including516 empty parents.
BW2 PASS440 independent future-string demand weights. CF REFUTED:
width3,T4 discrepancy1/4 comes entirely from the noncritical t2 term.
No control failed; no cancellation or decay estimate measured.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from collatz_gpt_boundary_loss import threshold, coin


def backward(T):
    f = [dict() for _ in range(T+1)]
    f[T] = {a: Fraction(a >= threshold(T)) for a in range(T+2)}
    for t in range(T-1, -1, -1):
        f[t] = {a: (f[t+1][a]+f[t+1][a+1])/2
                if a >= threshold(t) else Fraction(0)
                for a in range(T+1)}
        f[t][T+1] = Fraction(1)
    return f


def states_at(w, T):
    states = [(n, 0) for n in range(2**(w-1), 2**w)]
    rows = [states]
    for t in range(T):
        children = []
        for y, a in states:
            b = y % 2
            if 3**(a+b) >= 2**(t+1):
                children.append(((3*y+1)//2 if b else y//2, a+b))
        states = children
        rows.append(states)
    return rows


def main():
    finals = increments = zero = demands = 0
    guard = None
    V, _ = coin(24)
    for w in range(2, 11):
        m = w-1
        rows = states_at(w, 24)
        for T in range(m, 25):
            f = backward(T)
            H = [sum((f[t][a] for _, a in rows[t]), Fraction(0))
                 for t in range(m, T+1)]
            Q = Fraction(2**m*V[T], 2**T)
            assert H[0] == Q and H[-1] == len(rows[T])
            total = bound = noncritical = Fraction(0)
            for t in range(m, T):
                I = Counter()
                for y, a in rows[t]:
                    I[a] += 1 if y % 2 else -1
                weights = {a: f[t+1][a+1]-f[t+1][a]
                           for a in range(T+1)}
                assert all(0 <= v <= 1 for v in weights.values())
                assert sum(weights.values()) == 1
                assert all(weights[a] == 0 for a in range(threshold(T), T+1))
                term = sum((I[a]*weights[a]/2 for a in I), Fraction(0))
                absolute = sum((abs(I[a])*weights[a]/2 for a in I), Fraction(0))
                assert H[t-m+1]-H[t-m] == term
                if threshold(t+1) == threshold(t):
                    noncritical += term
                total += term
                bound += absolute
                increments += 1
                zero += not rows[t]
            assert total == len(rows[T])-Q and abs(total) <= bound
            finals += 1
            if (w, T) == (3, 4):
                guard = (total, noncritical)
    assert guard == (Fraction(1, 4), Fraction(1, 4))
    print('BW1 PASS:', finals, 'finals,', increments, 'increments,', zero,
          'empty-parent increments retained')
    for T in range(1, 11):
        f = backward(T)
        for t in range(T):
            distribution = Counter()
            for word in product((0, 1), repeat=T-t-1):
                z = 0
                J = threshold(t+1)
                for j, b in enumerate(word, t+2):
                    z += b
                    J = max(J, threshold(j)-z)
                distribution[J] += 1
            denominator = 2**(T-t-1)
            for a in range(T+1):
                assert f[t+1][a+1]-f[t+1][a] == Fraction(distribution[a+1], denominator)
                demands += 1
    print('BW2 PASS:', demands, 'backward weights independently matched by future-string demands')
    print('CF REFUTED:', guard, 'entire width3,T4 discrepancy is noncritical')


if __name__ == '__main__':
    main()
