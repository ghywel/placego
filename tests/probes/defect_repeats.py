#!/usr/bin/env python3
"""L1299 (Local, 2026-11-02): does the H = p/2 layer of the orbit tree T_p revisit a state?
reports/rule30-genealogy.md section 29.13. Run: python3 tests/probes/defect_repeats.py [rot]

A layer node (u, v)'s subtree depends only on (v, d = u | v), and the layer is equivariant under rotating the ring
(the split test |d| mod 2 is rotation-invariant, and rotating d rotates the pair {w, NOT w}). If states recurred,
memoising subtrees would shorten the p = 256 giant run. Counts, at p = 16, 32, 64 and 128: layer nodes, distinct
(v, d), distinct v, and (with 'rot') distinct (v, d) up to simultaneous rotation.
"""
import sys, time
def run(p, rot):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2)); AB = M ^ A
    def integ(d):
        w, acc = 0, 0
        for t in range(p):
            if acc: w |= 1 << t
            acc ^= (d >> t) & 1
        return w
    def rain(u, v): return (u == A and v == AB) or (u == AB and v == A)
    roots, st = [], [(A, A, 1)]
    while st:
        u, v, H = st.pop(); d = u | v
        sp = bin(d & ((1 << (2 * H)) - 1)).count('1') & 1
        w0 = integ(d); kids = [w0] if sp else [w0, w0 ^ M]; H2 = 2 * H if sp else H
        for w in kids:
            if rain(v, w): continue
            (roots if H2 == p // 2 else st).append((v, w) if H2 == p // 2 else (v, w, H2))
    def canon(v, d):
        s = ''.join('0123'[((v >> t) & 1) * 2 + ((d >> t) & 1)] for t in range(p)); ss = s + s
        return min(ss[i:i + p] for i in range(p))
    n = 0; exact = set(); rset = set(); vset = set(); rexact = 0; rrot = 0
    rootstates = set()
    for r in roots:
        st = [r]
        while st:
            u, v = st.pop(); n += 1; d = u | v
            k = (v, d)
            if k in exact: rexact += 1
            exact.add(k); vset.add(v)
            if rot:
                c = canon(v, d)
                if c in rset: rrot += 1
                rset.add(c)
            if bin(d).count('1') & 1: continue
            w0 = integ(d)
            for w in (w0, w0 ^ M):
                if not rain(v, w): st.append((v, w))
    print('p', p, 'roots', len(roots), 'layer nodes', n, 'distinct (v,d)', len(exact), 'repeats', rexact,
          'distinct v', len(vset), ('distinct up to rotation %d, repeats %d' % (len(rset), rrot)) if rot else '', flush=True)
for p in (16, 32, 64): run(p, True)
t = time.time(); run(128, len(sys.argv) > 1); print('s', round(time.time() - t))
