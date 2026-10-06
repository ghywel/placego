"""G69 LF1–LF2; preregistered at 68a8d88.

Finite integer application controls, not a verification of Rhin's theorem.
"""
from collections import Counter
from itertools import product
from collatz_gpt_actual_ceiling import specification, trajectory
from collatz_gpt_barrier_offset import extremal
from collatz_gpt_first_deficit_gap import first_deficit, terminal


def main():
    for a in range(1, 257):
        word, B = extremal(a)
        t = len(word)
        A, D = 3**a, 2**t-3**a
        assert D**10*t**133 > A**10
        K = B//D
        assert K**10*3**10 < a**10*t**133
    print('LF1: 256 exact denominator and maximum-ceiling inequalities pass')

    words = survivors = 0
    counts = Counter()
    for t in range(1, 17):
        for word in product((0, 1), repeat=t):
            if not first_deficit(word):
                continue
            words += 1
            r, K = specification(word)
            m0 = int(r == 0)
            for m in range(m0, (K-r)//(2**t)+1):
                n = r+2**t*m
                assert trajectory(n, t) == (word, True)
                q = terminal(n, word)
                assert 3*n < t**15 and 3*q < t**15
                survivors += 1
                counts[t] += 1
    for t in range(1, 17):
        assert counts[t] <= t**15//3
    print(f'LF2: {words} words/{survivors} independently evolved survivors; '
          'coarse start, terminal and time-count cutoffs pass')
    print('Survivor counts by first-deficit time:', sorted(counts.items()))
    # Analytic counterfactual witness: this odd start exceeds the t=1 cutoff.
    assert trajectory(3, 1) == ((1,), True) and 3 > 1**15/3
    print('CF: no-deficit horizon survivor cutoff refuted; all odd starts survive step1')


if __name__ == '__main__':
    main()
