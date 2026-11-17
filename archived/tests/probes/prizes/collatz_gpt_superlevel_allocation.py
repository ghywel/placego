#!/usr/bin/env python3
"""GC432 preregistration: superlevel component allocation, seven reused cases.
SL1 MUST HOLD: layer identity equals direct signed demand and literal H;
component bound <= old absolute bound and optimized-centering bound.
SL2 BLIND: at least one total strictly improves optimized centering.
CF MUST FAIL: disconnected components may be replaced by their enclosing
interval in the exact identity. REFUTED-BY I=(1,10,-1),d=(1,0,1).
Unexpected check: endpoint gradient mass equals component endpoints by level.
No larger population scan or asymptotic fit; widths2..8,T=8*(w-1).
OUTCOME 2026-10-08: SL1 PASS196 increments,46 empty; SL2 HELD only
at width7 (ratio0.9971977766); six ties. CF REFUTED by disconnected guard.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_weighted_center import centered


def layer(I, d):
    top = max(set(I) | set(d) | {0})
    assert all(x >= 0 for x in d.values())
    levels = sorted(set(d.values()) - {0})
    previous = signed = bound = endpoint_mass = Fraction()
    for height in levels:
        width = height - previous
        a = 0
        while a <= top:
            if d.get(a, 0) < height:
                a += 1
                continue
            start = a
            while a <= top and d.get(a, 0) >= height:
                a += 1
            imbalance = sum(I.get(j, 0) for j in range(start, a))
            signed += width * imbalance / 2
            bound += width * abs(imbalance) / 2
            endpoint_mass += 2 * width
        previous = height
    direct = sum((I[a] * d.get(a, 0) / 2 for a in I), Fraction())
    old = sum((abs(I[a]) * d.get(a, 0) / 2 for a in I), Fraction())
    _, median, _ = centered(I, d)
    variation = sum(abs(d.get(a, 0) - d.get(a+1, 0)) for a in range(-1, top+1))
    assert signed == direct and endpoint_mass == variation
    assert abs(signed) <= bound <= old and bound <= median
    return signed, bound, old, median


def main():
    results = []
    increments = empty = 0
    for w in range(2, 9):
        m = w - 1
        T = 8 * m
        rows = states_at(w, T)
        f = backward(T)
        total = old = median = signed = Fraction()
        for t in range(m, T):
            I = Counter()
            for x, a in rows[t]:
                I[a] += 1 if x % 2 else -1
            d = {a: f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
            value, bound, earlier, centered_bound = layer(I, d)
            literal = sum((f[t+1][a] for _, a in rows[t+1]), Fraction()) - sum((f[t][a] for _, a in rows[t]), Fraction())
            assert value == literal
            total += bound
            old += earlier
            median += centered_bound
            signed += value
            increments += 1
            empty += not rows[t]
        Q = sum((f[m][a] for _, a in rows[m]), Fraction())
        assert signed == len(rows[T]) - Q
        results.append(dict(w=w, layer=str(total), median=str(median), old=str(old),
                            layer_over_median=float(total/median), improved=total < median))
    guard = layer({0: 1, 1: 10, 2: -1}, {0: Fraction(1), 2: Fraction(1)})
    assert guard[0] == 0 and guard[1] == 1
    assert Fraction(1+10-1, 2) != guard[0]
    print(json.dumps(dict(cases=results, increments=increments, empty=empty,
                          controls="PASS", disconnected_guard="PASS",
                          prediction_any_improvement=any(r['improved'] for r in results)), indent=2))


if __name__ == '__main__':
    main()
