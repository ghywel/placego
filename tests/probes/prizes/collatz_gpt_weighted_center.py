#!/usr/bin/env python3
"""GC426 preregistered weighted-centering diagnostic, seven existing cases.
WC1 MUST HOLD: exact signed Abel and literal H increments agree; optimized
absolute bound holds and does not exceed the old range-product bound.
WC2 BLIND: at least one total improves G74's original absolute bound.
CF MUST FAIL: zero-gradient extrema must affect the optimized bound.
REFUTED-BY: I=(1,1), d=(1,0) gives optimized 1/2 versus range 1.
Unexpected check: retain empty finals, and zero-weight prefix extrema.
Widths2..8, T=8*(w-1); no larger start survey or asymptotic fit.
OUTCOME 2026-10-08: WC1 PASS196 increments,46 empty; WC2 HELD four
improved cases, three ties. CF REFUTED by exact zero-weight guard.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at


def centered(I, d):
    top = max(set(I) | set(d) | {0})
    B = {-1: 0}
    for a in range(top + 1):
        B[a] = B[a - 1] + I.get(a, 0)
    g = {a: d.get(a, 0) - d.get(a + 1, 0)
         for a in range(-1, top + 1)}
    assert sum(g.values()) == 0
    # A weighted absolute-value minimum occurs at a breakpoint B[a].
    optimum = min(sum((abs(B[a] - c) * abs(g[a]) / 2 for a in g),
                      Fraction()) for c in set(B.values()))
    coarse = Fraction(max(B.values()) - min(B.values()), 4) * sum(abs(x) for x in g.values())
    exact = sum((B[a] * g[a] / 2 for a in g), Fraction())
    direct = sum((I[a] * d.get(a, 0) / 2 for a in I), Fraction())
    assert exact == direct and abs(exact) <= optimum <= coarse
    return exact, optimum, coarse


def main():
    results = []
    increments = empty = 0
    for w in range(2, 9):
        m = w - 1
        T = 8 * m
        rows = states_at(w, T)
        f = backward(T)
        old = refined = coarse = signed = Fraction()
        for t in range(m, T):
            I = Counter()
            for x, a in rows[t]:
                I[a] += 1 if x % 2 else -1
            d = {a: f[t+1][a+1] - f[t+1][a] for a in range(T+1)}
            value, bound, bigger = centered(I, d)
            literal = sum((f[t+1][a] for _, a in rows[t+1]), Fraction()) - sum((f[t][a] for _, a in rows[t]), Fraction())
            assert value == literal
            old += sum((abs(I[a]) * d.get(a, 0) / 2 for a in I), Fraction())
            refined += bound
            coarse += bigger
            signed += value
            increments += 1
            empty += not rows[t]
        Q = sum((f[m][a] for _, a in rows[m]), Fraction())
        assert signed == len(rows[T]) - Q
        results.append(dict(w=w, old=str(old), refined=str(refined), coarse=str(coarse),
                            refined_over_old=float(refined/old), improved=refined < old))
    guard = centered({0: 1, 1: 1}, {0: Fraction(1)})
    assert guard == (Fraction(1, 2), Fraction(1, 2), Fraction(1))
    print(json.dumps(dict(cases=results, increments=increments, empty=empty,
                          controls="PASS", prediction_any_improvement=any(r['improved'] for r in results),
                          zero_weight_extremum_guard="PASS"), indent=2))


if __name__ == '__main__':
    main()
