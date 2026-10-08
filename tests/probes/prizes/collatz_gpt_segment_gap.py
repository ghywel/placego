#!/usr/bin/env python3
"""GC436 preregistration: inspect only seven existing GC432 cases.
SG1 MUST HOLD: endpoint-incidence reconstruction, gap identity and tie iff
common segment intersection at all196 increments; literal H independent.
SG2 BLIND: width7 has exactly one incompatible time increment.
CF MUST FAIL: replacing all segments by one enclosing hull preserves gap.
Unexpected check: constant translation13 and empty population/demand cases.
No larger population scan or asymptotic fit. Widths2..8,T=8*(w-1).
OUTCOME 2026-10-08: SG1 PASS196 increments,46 empty populations,
zero actual empty-segment families; SG2 HELD exactly one at width7,t34,
gap97/8192, L1,U0,nine segments. Hull CF REFUTED. Translation and
synthetic empty population/demand guards PASS.
"""
from collections import Counter
from fractions import Fraction
import json
from collatz_gpt_backward_weights import backward, states_at
from collatz_gpt_superlevel_allocation import layer
from collatz_gpt_weighted_center import centered


def segments(I, d):
    top = max(set(I) | set(d) | {0})
    B = {-1: 0}
    for a in range(top + 1):
        B[a] = B[a-1] + I.get(a, 0)
    result = []
    previous = Fraction()
    # Form boundaries by threshold transitions, independently of layer's scan.
    for h in sorted(set(d.values()) - {0}):
        starts = [a for a in range(top+1)
                  if d.get(a, 0) >= h and d.get(a-1, 0) < h]
        ends = [a for a in range(top+1)
                if d.get(a, 0) >= h and d.get(a+1, 0) < h]
        assert len(starts) == len(ends)
        for l, r in zip(starts, ends):
            assert l <= r
            x, y = B[l-1], B[r]
            result.append((h-previous, min(x, y), max(x, y), l, r))
        previous = h
    return result


def gap(rows):
    if not rows:
        return Fraction(), None, None
    candidates = {x for _, l, r, _, _ in rows for x in (l, r)}
    value = min(sum((w * max(l-c, 0, c-r) for w, l, r, _, _ in rows),
                    Fraction()) for c in candidates)
    L = max(l for _, l, _, _, _ in rows)
    U = min(r for _, _, r, _, _ in rows)
    assert (value == 0) == (L <= U)
    translated = [(w, l+13, r+13, a, b) for w, l, r, a, b in rows]
    shifted_value = min(sum((w * max(l-c, 0, c-r) for w, l, r, _, _ in translated),
                            Fraction()) for c in {x+13 for x in candidates})
    assert shifted_value == value
    return value, L, U


def main():
    cases = []
    increments = empty = vacuous = 0
    for w in range(2, 9):
        m = w-1
        T = 8*m
        populations = states_at(w, T)
        f = backward(T)
        misses = []
        gap_total = Fraction()
        for t in range(m, T):
            I = Counter()
            for x, a in populations[t]:
                I[a] += 1 if x % 2 else -1
            d = {a: f[t+1][a+1]-f[t+1][a] for a in range(T+1)}
            rows = segments(I, d)
            value, E, _, M = layer(I, d)
            g, L, U = gap(rows)
            assert sum((wt*(r-l)/2 for wt, l, r, _, _ in rows), Fraction()) == E
            assert M-E == g
            top = max(set(I) | set(d) | {0})
            B = {-1: 0}
            for a in range(top+1):
                B[a] = B[a-1]+I.get(a, 0)
            # Equality for every prefix-value breakpoint, not only minimizers.
            for c in set(B.values()):
                objective = sum((abs(B[a]-c)*abs(d.get(a, 0)-d.get(a+1, 0))/2
                                 for a in range(-1, top+1)), Fraction())
                distance = sum((wt*max(l-c, 0, c-r) for wt, l, r, _, _ in rows), Fraction())
                assert objective == E+distance
            literal = sum((f[t+1][a] for _, a in populations[t+1]), Fraction())-sum((f[t][a] for _, a in populations[t]), Fraction())
            assert value == literal == centered(I, d)[0]
            if g:
                misses.append(dict(t=t, gap=str(g), L=L, U=U,
                                   segments=len(rows), separation=L-U))
            gap_total += g
            increments += 1
            empty += not populations[t]
            vacuous += not rows
        cases.append(dict(w=w, incompatible=misses, gap_total=str(gap_total)))
    guard = segments({0: 1, 1: 10, 2: -1}, {0: Fraction(1), 2: Fraction(1)})
    assert gap(guard)[0] == 9
    hull = [(Fraction(1), min(r[1] for r in guard), max(r[2] for r in guard), 0, 2)]
    assert gap(hull)[0] == 0  # Deliberately wrong replacement loses the gap.
    assert gap(segments({}, {0: Fraction(1)})) == (0, 0, 0)
    assert gap(segments({}, {})) == (0, None, None)
    seven = next(c for c in cases if c['w'] == 7)
    print(json.dumps(dict(cases=cases, increments=increments, empty=empty,
                          vacuous=vacuous, controls='PASS', hull_counterfactual='REFUTED',
                          blind_exactly_one=len(seven['incompatible']) == 1), indent=2))


if __name__ == '__main__':
    main()
