#!/usr/bin/env python3
"""L1307 T29 (Local, 2026-11-02): SAT search for light-speed phases, testing the cycle lemma.
reports/rule30-genealogy.md section 34 (predictions written first).
Run: python3 tests/probes/phase_sat.py [neg P MMAX | pos P MMAX]   (no arguments: the full T29 schedule)

A phase is C_K(t), K in Z, t in Z/p (p = 2L), with C_(K+1)(t+1) xor C_(K+1)(t) = C_(K-1)(t) OR C_K(t) for every K and t,
and C_(K+m)(t) = C_K(t + s) (depth period m, twist s). Variables C_k(t), 0 <= k < m.
(neg): some column has least period p, and no column has four-quarter fold g identically 1 (g(s0) = C(s0) xor
C(s0+L/2) xor C(s0+L) xor C(s0+3L/2)). A solution would refute the cycle lemma.
(pos): some column has least period p; phases are enumerated, each blocked in all depth shifts and time rotations.
Solver: CaDiCaL 1.9.5 through python-sat. UNSAT answers here are solver-reported, not LRAT-certified.
"""
import sys
import time
from pysat.solvers import Cadical195


class Enc:
    def __init__(self, p, m, s, mode):
        self.p, self.m, self.s, self.L = p, m, s, p // 2
        self.nv = m * p; self.cl = []
        for K in range(m):
            for t in range(p):
                o = self.new()
                a, b = self.col(K - 1, t), self.col(K, t)
                self.cl += [[-a, o], [-b, o], [a, b, -o]]
                x, y = self.col(K + 1, t + 1), self.col(K + 1, t)
                for bx in (0, 1):
                    for by in (0, 1):
                        for bo in (0, 1):
                            if bx ^ by ^ bo:
                                self.cl.append([x if not bx else -x, y if not by else -y, o if not bo else -o])
        L = self.L; zs = []
        for k in range(m):                         # some column of least period p
            for t in range(L):
                z = self.new(); u, w = self.var(k, t), self.var(k, t + L)
                self.cl += [[-z, u, w], [-z, -u, -w]]; zs.append(z)
        self.cl.append(zs)
        if mode == 'neg':                          # no column has g identically 1
            q = L // 2
            for k in range(m):
                ys = []
                for s0 in range(q):
                    x0, x1, x2, x3 = (self.var(k, s0 + j * q) for j in range(4))
                    a1, a2, y = self.new(), self.new(), self.new()
                    self.xor2(a1, x0, x1); self.xor2(a2, x2, x3)
                    self.cl += [[-y, -a1, a2], [-y, a1, -a2]]; ys.append(y)
                self.cl.append(ys)

    def new(self):
        self.nv += 1
        return self.nv

    def var(self, k, t):
        return 1 + k * self.p + (t % self.p)

    def col(self, K, t):
        return self.var(K % self.m, t + (K // self.m) * self.s)

    def xor2(self, a, x, y):                       # a <-> x xor y
        self.cl += [[-a, x, y], [-a, -x, -y], [a, -x, y], [a, x, -y]]

    def decode(self, model):
        pos = set(l for l in model if l > 0)
        return [sum(1 << t for t in range(self.p) if self.var(k, t) in pos) for k in range(self.m)]


def tools(p):
    M = (1 << p) - 1

    def integ(d):
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M; s <<= 1
        return (y << 1) & M

    def val(c):
        k = 0
        while c:
            if bin(c).count('1') & 1:
                return k
            c = integ(c); k += 1
        return p

    def rot(c, r):
        r %= p
        return ((c >> r) | (c << (p - r))) & M

    def canon(c):
        return min(rot(c, r) for r in range(p))

    def lp(c):
        q = 1
        while q < p and rot(c, q) != c:
            q *= 2
        return q
    return M, integ, val, rot, canon, lp


def neg(p, mmax):
    t0 = time.process_time(); sat = []
    for m in range(1, mmax + 1):
        for s in range(p):
            e = Enc(p, m, s, 'neg')
            with Cadical195(bootstrap_with=e.cl) as S:
                if S.solve():
                    sat.append((m, s, e.decode(S.get_model())))
    print('neg p=%d m<=%d, all twists: %d instances, SAT %d, CPU %.1f s' % (p, mmax, mmax * p, len(sat), time.process_time() - t0))
    M, integ, val, rot, canon, lp = tools(p)
    for m, s, cols in sat[:3]:
        print('   counterexample m=%d s=%d: valuations %s, least periods %s, columns %s' % (
            m, s, sorted(set(val(c) for c in cols)), sorted(set(lp(c) for c in cols)),
            ' '.join('%0*x' % (p // 4, c) for c in cols)))
    return sat


def pos(p, mmax, cap=40):
    t0 = time.process_time(); M, integ, val, rot, canon, lp = tools(p); phases = {}
    for m in range(1, mmax + 1):
        for s in range(p):
            e = Enc(p, m, s, 'pos')
            with Cadical195(bootstrap_with=e.cl) as S:
                n = 0
                while n < cap and S.solve():
                    cols = e.decode(S.get_model()); n += 1
                    sig = frozenset(canon(c) for c in cols)
                    if sig not in phases:
                        vals = sorted(set(val(c) for c in cols))
                        phases[sig] = (m, s, vals, sorted(set(lp(c) for c in cols)))
                    for k0 in range(m):            # block every depth shift and time rotation of this solution
                        for r in range(p):
                            blk = []
                            # depth shift by k0 within the twisted frame: C'_k = C_(k+k0), and C_(k+m)(t) = C_k(t+s)
                            shifted = [(cols[k + k0] if k + k0 < m else rot(cols[k + k0 - m], s)) for k in range(m)]
                            shifted = [rot(c, r) for c in shifted]
                            for k in range(m):
                                for t in range(p):
                                    v = e.var(k, t)
                                    blk.append(-v if (shifted[k] >> t) & 1 else v)
                            S.add_clause(blk)
    print('pos p=%d m<=%d: %d distinct phases (columns up to rotation), CPU %.1f s' % (p, mmax, len(phases), time.process_time() - t0))
    for sig, (m, s, vals, pers) in sorted(phases.items(), key=lambda kv: (kv[1][0], kv[1][1])):
        print('   first found at m=%d s=%d: %d column classes, least periods %s, valuations %s, largest %d (L/2-1 = %d)' % (
            m, s, len(sig), pers, vals, max(vals), p // 4 - 1))
    return phases


if __name__ == '__main__':
    if len(sys.argv) == 4:
        (neg if sys.argv[1] == 'neg' else pos)(int(sys.argv[2]), int(sys.argv[3]))
    else:
        pos(8, 16); pos(16, 16); neg(8, 64); neg(16, 64)
        pos(32, 32); neg(32, 64)
