"""G79 SB1-SB2, preregistered at343dbb1.
SB1 MUST HOLD: existing180 width/horizon cases, exact probability weights,
signed/absolute means recover D/Q and A/Q; U0 cases have D=A0.
Extrema have no size/rate prediction; report only positive-weight support.
SB2 MUST HOLD: independent width2,T4 guard gives epsilon-4, Delta1.
CF: epsilon is always in[-1,1]; MUST FAIL on the guard.
REFUTED-BY: even current4, I-1, coin class mass1/4, epsilon-4.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
SB1 PASS168 weighted and12 zero-proxy cases. Peak supported epsilon
131072/6167 at w5,T24,t20,a15, mu6167/1953628. Largest absolute mean
17/9 at w3,T7 with empty final ensemble. SB2 PASS; CF REFUTED.
No asymptotic fit, uniform bound, or larger actual population.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_coin_proxy import classes
from collatz_gpt_boundary_loss import admissible, direct_count


def main():
    coin = classes(24)
    cases = zero = 0
    peak = None
    averages = []
    for w in range(2, 11):
        m = w-1
        rows = states_at(w, 24)
        for T in range(m, 25):
            f = backward(T)
            weighted = []
            D = A = U = Fraction(0)
            for t in range(m, T):
                I = Counter()
                for y, a in rows[t]:
                    I[a] += 1 if y % 2 else -1
                assert all(a in coin[t] for a in I)
                for a, n in coin[t].items():
                    q = Fraction(2**m*n, 2**t)
                    delta = f[t+1][a+1]-f[t+1][a]
                    weight = q*delta/2
                    epsilon = I[a]/q
                    U += weight
                    D += I[a]*delta/2
                    A += abs(I[a])*delta/2
                    if weight:
                        weighted.append((t, a, weight, epsilon))
            Q = Fraction(2**m*sum(coin[T].values()), 2**T)
            C = direct_count(2**m, 2**(m+1), T)
            assert D == C-Q
            if not U:
                assert D == A == 0
                zero += 1
                continue
            mu = [(t, a, weight/U, e) for t, a, weight, e in weighted]
            assert sum(r[2] for r in mu) == 1
            mean = sum((p*e for _, _, p, e in mu), Fraction(0))
            absolute = sum((p*abs(e) for _, _, p, e in mu), Fraction(0))
            S = U/Q
            assert S*mean == D/Q and S*absolute == A/Q
            averages.append((w, T, C, S, mean, absolute))
            for t, a, p, e in mu:
                if peak is None or abs(e) > abs(peak[4]):
                    peak = (w, T, t, a, e, p)
            cases += 1
    y, a = 3, 0
    for t in range(1, 4):
        b = y % 2
        a += b
        y = (3*y+1)//2 if b else y//2
        assert 3**a >= 2**t
    words = [word for word in product((0, 1), repeat=3)
             if admissible(word) and sum(word) == 2]
    assert words == [(1, 1, 0)] and y == 4 and a == 2
    q = Fraction(2*len(words), 8)
    epsilon = Fraction(-1)/q
    delta = int(3**3 >= 2**4)-int(3**2 >= 2**4)
    assert epsilon == -4 and delta == 1
    print('SB1 PASS', cases, 'weighted cases and', zero, 'zero-proxy cases')
    print('Peak support fields w,T,t,a,epsilon,mu:', peak)
    print('Largest absolute weighted mean fields w,T,C,S,mean,absolute:',
          max(averages, key=lambda r: r[5]))
    print('SB2 PASS; CF REFUTED: independent guard epsilon-4, Delta1')


if __name__ == '__main__':
    main()
