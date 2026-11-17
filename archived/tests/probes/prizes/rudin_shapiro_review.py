#!/usr/bin/env python3
"""rudin_shapiro_review.py: Local's review checks for G153 (GPT's Rudin-Shapiro repeat-debt certificate, 2026-10-07),
written in code that shares nothing with Walnut, rudin_shapiro_repeat.py or rudin_shapiro_semantics.py.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/prizes/rudin_shapiro_review.py PATH/rsp-repeat-dd61eb5.txt
            (the exported automaton lives in the shared scratch, not in Git)
COST:       seconds.

  RV1: the exported 78-state relation, read most-significant digit first with missing transitions as rejection,
       agrees with brute force (r(n) = parity of overlapping 11s, inclusive interval) on every a, b, q < 32, at one
       and at four extra leading zeros.
  RV2: Safe(0) on the exported relation by Local's own debt product: d = b - 2a - q read most-significant digit
       first, d' = 2d + b_d - 2a_d - q_d, saturated to -1 (meaning <= -1), 0, 1, 2, 3 (meaning >= 3), which is exact
       because 2(-1) + 1 < 0 and 2(3) - 3 >= 3; the search reports any reachable pair with Rep accepting and d > 0.
  GPT's RSP-S equivalence (its LSD reconstruction against the reversed export) is reproduced separately by running
  rudin_shapiro_semantics.py on the same file.

First attempt, retained: this script first tried an independent most-significant-digit construction (guessing the
digits of s and the carry of s + q from below, then subset construction). It was stopped after ten minutes at 3 GB
resident, still determinising, when GC177 showed GPT had claimed and closed the independent-reconstruction lane;
nothing was concluded from it.

PREDICTIONS, written 2026-10-07 before this version ran: RV1 agreement on all 32^3 triples; RV2 no reachable
violation.
"""
import sys
from itertools import product

SYMS = list(product((0, 1), repeat=3))          # (a_d, b_d, q_d)


def rs_step(st, d):
    h, e = st
    return (d, e ^ (h & d))


def r_of(n):
    st = (0, 0)
    for ch in bin(n)[2:]:
        st = rs_step(st, int(ch))
    return st[1]


def cmp_step(c, x, y):                           # c: 0 equal so far, 1 x < y, 2 x > y
    if c != 0:
        return c
    return 0 if x == y else (1 if x < y else 2)


def run_dfa(start, trans, accept, a, b, q, width):
    st = start
    for i in range(width - 1, -1, -1):
        st = trans[st][((a >> i) & 1, (b >> i) & 1, (q >> i) & 1)]
    return accept[st]


def load_walnut(path):
    lines = open(path).read().split('\n')
    assert lines[0].split() == ['msd_2', 'msd_2', 'msd_2'], lines[0]
    trans, accept, cur = {}, {}, None
    for line in lines[1:]:
        f = line.split()
        if not f:
            continue
        if '->' in f:
            sym = tuple(int(v) for v in f[:3])
            trans[cur][sym] = int(f[4])
        else:
            cur = int(f[0])
            accept[cur] = f[1] == '1'
            trans[cur] = {}
    return 0, trans, accept


def equivalent(A, B):
    (sa, ta, aa), (sb, tb, ab) = A, B
    seen, todo = {(sa, sb)}, [(sa, sb)]
    while todo:
        x, y = todo.pop()
        ax = aa[x] if x is not None else False
        ay = ab[y] if y is not None else False
        if ax != ay:
            return False, (x, y)
        for sym in SYMS:
            nx = ta[x].get(sym) if x is not None else None
            ny = tb[y].get(sym) if y is not None else None
            if (nx, ny) not in seen:
                seen.add((nx, ny))
                todo.append((nx, ny))
    return True, len(seen)


def debt_safe(start, trans, accept):
    """Search Rep x saturated debt d = b - 2a - q (states -1 meaning <= -1, 0, 1, 2, 3 meaning >= 3) for a
    reachable accepting pair (Rep accepting, d > 0)."""
    sat = lambda d: max(-1, min(3, d))
    s0 = (start, 0)
    seen, todo, bad = {s0}, [s0], []
    while todo:
        st, d = todo.pop()
        if accept[st] and d > 0:
            bad.append((st, d))
        for sym in SYMS:
            a_d, b_d, q_d = sym
            nxt = (trans[st][sym], sat(2 * d + b_d - 2 * a_d - q_d))
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    return not bad, len(seen)


def main():
    W = load_walnut(sys.argv[1])
    start, trans, accept = W
    print('exported relation: %d states' % len(trans))

    def run(a, b, q, width):
        st = start
        for i in range(width - 1, -1, -1):
            st = trans[st].get(((a >> i) & 1, (b >> i) & 1, (q >> i) & 1))
            if st is None:
                return False
        return accept[st]

    rv1 = True
    for a in range(32):
        for b in range(32):
            for q in range(32):
                want = q >= 1 and b >= a and all(r_of(s) == r_of(s + q) for s in range(a, b + 1))
                rv1 &= run(a, b, q, 6) == want and run(a, b, q, 9) == want
    print('RV1', 'PASS' if rv1 else 'FAIL', '(exported relation against brute force, all a, b, q < 32, two paddings)')
    sat = lambda d: max(-1, min(3, d))
    s0 = (start, 0)
    seen, todo, viol = {s0}, [s0], []
    while todo:
        st, d = todo.pop()
        if accept[st] and d > 0:
            viol.append((st, d))
        for sym in SYMS:
            nx = trans[st].get(sym)
            if nx is None:
                continue
            a_d, b_d, q_d = sym
            nxt = (nx, sat(2 * d + b_d - 2 * a_d - q_d))
            if nxt not in seen:
                seen.add(nxt)
                todo.append(nxt)
    print('RV2', 'PASS' if not viol else 'FAIL', 'Safe(0): %d reachable debt-product states, %d violations'
          % (len(seen), len(viol)))


if __name__ == '__main__':
    main()
