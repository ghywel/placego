#!/usr/bin/env python3
"""L1311 T34 part 2 (Local, 2026-11-02): a sound window automaton for the mismatch front against a phase.
reports/rule30-genealogy.md section 39. Run: python3 tests/probes/front_cert.py PHASE W [W ...]   (PHASE: G8, G16, 480 or P1024)

State: (R mod NC, t mod p, window) with window = mismatch bits D_(R-1) .. D_(R-W) above the front R (D_R = 1, D below R
are 0). One tick: D_n(t+1) = D_n xor [((E_(n-1) xor D_(n-1)) | (E_(n-2) xor D_(n-2))) xor (E_(n-1) | E_(n-2))] for
n = R-W .. R+2; the two bits D_(R-W-1), D_(R-W-2) are unknown and branched over; window bits of the new state that lie
below the computed range (after a retreat) are free and branched over. That over-approximates every real run, so a
property of all its infinite paths is a property of every real front. A retreat with no 1 left in R-W .. R+2 is a
FAIL edge.

Certificate: no FAIL edge, and some k with every path of length k advancing by at least 1 (then every cycle has
positive total advance). Every front then advances at a positive minimum mean speed, so the episode length M_E(k) is
finite for every k and, by the bridge of section 38.2, no eternal point of any period ends in E.
"""
import os
import sys
import runpy
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
g = runpy.run_path(os.path.join(here, 'upward_rigid.py'), run_name='lib')


def build_generic(NCL, bg, nxt, W):
    """Window automaton over NCL front classes. bg(cls, o) is the phase's bit at depth R + o at the current time;
    nxt(cls, a) is the class after one tick when the front moves by a."""
    NS = NCL * (1 << W)
    src, dst, adv = [], [], []; fails = 0
    for cl in range(NCL):
        E = {o: bg(cl, o) for o in range(-W - 2, 3)}
        base = cl << W
        for win in range(1 << W):
            for unk in range(4):
                D = {o: 0 for o in range(-W - 2, 3)}
                D[0] = 1
                for j in range(1, W + 1):
                    D[-j] = (win >> (j - 1)) & 1
                D[-W - 1] = unk & 1; D[-W - 2] = (unk >> 1) & 1
                N = {}
                for o in range(-W, 3):
                    e1, e2 = E[o - 1], E[o - 2]
                    N[o] = D[o] ^ (((e1 ^ D[o - 1]) | (e2 ^ D[o - 2])) ^ (e1 | e2))
                ones = [o for o in range(-W, 3) if N[o]]
                if not ones:
                    fails += 1; continue
                a = max(ones)
                known = [N[a - j] if a - j >= -W else None for j in range(1, W + 1)]
                free = [i for i, v in enumerate(known) if v is None]
                c2 = nxt(cl, a)
                for f in range(1 << len(free)):
                    w2 = 0
                    for i, v in enumerate(known):
                        if v is None:
                            v = (f >> free.index(i)) & 1
                        w2 |= v << i
                    src.append(base | win); dst.append((c2 << W) | w2); adv.append(a)
    return NS, np.array(src, dtype=np.int64), np.array(dst, dtype=np.int64), np.array(adv, dtype=np.int64), fails


def build(p, cols, W):
    """Classes (R mod NC, t mod p), for phases given by their columns (G8, G16, the 480-state phase)."""
    NC = len(cols)
    return build_generic(NC * p, lambda cl, o: (cols[(cl // p + o) % NC] >> (cl % p)) & 1,
                         lambda cl, a: ((cl // p + a) % NC) * p + (cl % p + 1) % p, W)


def build_single_column(col0, P, s, W):
    """A single-column phase C_K(t) = col0(t + s*K) (P1024: P = 1024, s = 195). Class theta = (t + s*R) mod P."""
    return build_generic(P, lambda th, o: (col0 >> ((th + s * o) % P)) & 1,
                         lambda th, a: (th + 1 + s * a) % P, W)


def certify(NS, src, dst, adv, kmax=600):
    """Least total advance over all paths of length k (min-plus recurrence). If it reaches >= 1 for some k, every cycle
    has positive total advance (repeat any cycle k times). Returns (k or None, list of (k, least advance))."""
    v = np.zeros(NS, dtype=np.int64); INF = 1 << 40
    hasout = np.zeros(NS, dtype=bool); hasout[src] = True; trace = []
    for k in range(1, kmax + 1):
        nv = np.full(NS, INF, dtype=np.int64)
        np.minimum.at(nv, src, adv + v[dst]); v = nv
        m = int(v[hasout].min())
        if k in (10, 25, 50, 100, 200, 300, 600):
            trace.append((k, m))
        if m >= 1:
            trace.append((k, m)); return k, trace
    return None, trace


if __name__ == '__main__':
    name = sys.argv[1]
    p, cols, _ = g['phases']()[name]
    for W in [int(x) for x in sys.argv[2:]]:
        if name == 'P1024':
            NS, src, dst, adv, fails = build_single_column(cols[0], p, 195, W)
        else:
            NS, src, dst, adv, fails = build(p, cols, W)
        print('%s W=%d: states %d, edges %d, FAIL edges %d, advances %s' % (
            name, W, NS, len(src), fails, sorted(set(adv.tolist()))), flush=True)
        if fails:
            print('   FAIL edges present (a retreat can leave the window): no certificate; the non-FAIL part is still tested', flush=True)
        k, trace = certify(NS, src, dst, adv)
        print('   least advance over paths of length k: %s' % trace, flush=True)
        print('   %s' % (('CERTIFIED: no FAIL edge and every path of length %d advances' % k) if (k and fails == 0) else
                           ('NOT CERTIFIED (FAIL edges present; the non-FAIL part advances on every %d-path)' % k if k else 'NOT CERTIFIED')), flush=True)
