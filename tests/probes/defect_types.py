#!/usr/bin/env python3
"""L1297 T26 (Local, 2026-11-02): types and outcomes in the H = p/2 layer of the orbit tree T_p (defect_layer.c).
reports/rule30-genealogy.md section 29.14, predictions written first. Run: python3 tests/probes/defect_types.py

Node (u, v), H = p/2: d = u | v; it splits if |d| is even (children (v, w), (v, NOT w), w = running XOR of d shifted
by one) and dies if odd. Type of a node: |v| mod 2. Counts, over every layer node at p = 64 and 128:
splitting nodes by type; for type 0, both children split / both die; for type 1, exactly one splits (proved);
child type against parent type.
"""
import sys
sys.setrecursionlimit(10000)


def run(p):
    M = (1 << p) - 1
    A = int('10' * (p // 2), 2) & M          # bits 1, 3, 5, ... set
    A = sum(1 << t for t in range(1, p, 2))
    AB = M ^ A

    def integ(d):
        w, acc = 0, 0
        for t in range(p):
            if acc:
                w |= 1 << t
            acc ^= (d >> t) & 1
        return w

    def rain(u, v):
        return (u == A and v == AB) or (u == AB and v == A)
    # phase 1: copy of T_(p/2), collecting roots with H = p/2
    roots, st = [], [(A, A, 1)]
    while st:
        u, v, H = st.pop()
        d = u | v
        sp = bin(d & ((1 << (2 * H)) - 1)).count('1') & 1
        w0 = integ(d)
        kids = [w0] if sp else [w0, w0 ^ M]
        H2 = 2 * H if sp else H
        for w in kids:
            if rain(v, w):
                continue
            (roots if H2 == p // 2 else st).append((v, w) if H2 == p // 2 else (v, w, H2))
    c = dict(nodes=0, split=[0, 0], both=0, none=0, one1=0, other1=0, trans=[[0, 0], [0, 0]], rootsplit=0)
    for r in roots:
        st = [r]
        first = True
        while st:
            u, v = st.pop()
            c['nodes'] += 1
            d = u | v
            if bin(d).count('1') & 1:
                first = False
                continue
            if first:
                c['rootsplit'] += 1
            first = False
            e = bin(v).count('1') & 1
            c['split'][e] += 1
            w0 = integ(d)
            w1 = w0 ^ M
            s0 = bin(v | w0).count('1') & 1
            s1 = bin(v | w1).count('1') & 1
            ec = bin(w0).count('1') & 1
            if e == 0:
                if s0 == 0 and s1 == 0:
                    c['both'] += 1
                elif s0 == 1 and s1 == 1:
                    c['none'] += 1
                else:
                    c['other1'] += 1          # would violate the fact
            else:
                if s0 + s1 == 1:
                    c['one1'] += 1
                else:
                    c['other1'] += 1
            for s_, w in ((s0, w0), (s1, w1)):
                if s_ == 0:
                    c['trans'][e][ec] += 1    # splitting child of a splitting parent: parent type -> child type
                if not rain(v, w):
                    st.append((v, w))
    return len(roots), c


for p in (64, 128):
    R, c = run(p)
    S = sum(c['split'])
    t = c['trans']
    print(f"p={p}: roots {R}, layer nodes {c['nodes']}, splitting {S}; roots that split {c['rootsplit']} (q = {c['rootsplit'] / R:.4f})")
    print(f"  type-0 share among splitting nodes f = {c['split'][0] / S:.4f} ({c['split'][0]} of {S})")
    print(f"  type 0: both children split {c['both']}, both die {c['none']}, share both = {c['both'] / max(1, c['both'] + c['none']):.4f}")
    print(f"  type 1: exactly one splits {c['one1']}; violations of the two-type fact {c['other1']}")
    print(f"  splitting child's type given parent type: from 0 -> (0: {t[0][0]}, 1: {t[0][1]}), from 1 -> (0: {t[1][0]}, 1: {t[1][1]});"
          f" P(child 0 | parent 0) = {t[0][0] / max(1, sum(t[0])):.4f}, P(child 0 | parent 1) = {t[1][0] / max(1, sum(t[1])):.4f}")
    print(f"  model constant 1.128 q / sqrt(f) = {1.128 * (c['rootsplit'] / R) / (c['split'][0] / S) ** 0.5:.3f}")
print('DEFECT_TYPES_DONE')
