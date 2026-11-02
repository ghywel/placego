#!/usr/bin/env python3
"""L1304 (Local, 2026-11-02): the 480-state light-speed phase at p = 32, stored and replayed as a witness (GC2361 Q4).
reports/inquisition-local-to-gpt-20261102.md section 6. Run: python3 tests/probes/phase480.py [--write]

With --write: rerun general_front.py's p = 32 sample (seed 2), follow a surviving continuation from the first root that
reaches a non-rain cycle, and write the cycle's states to phase480_p32.txt (one state per line: u v, 32-bit hex, bit t
= time t). Without it: read the file and check, independently of how it was found:
- every edge (u, v) -> (v, w), including the closing one, has |u OR v| even and Delta w = u OR v, where
  Delta w(t) = w(t+1) XOR w(t) on the ring of length 32;
- the states are distinct, and the cycle is neither rain nor white;
- the least periods of the columns, and the number of distinct columns up to rotation.
"""
import random
import sys
P = 32
M = (1 << P) - 1
FILE = __file__.replace('phase480.py', 'phase480_p32.txt')


def delta(w):
    return (w ^ ((w >> 1) | ((w & 1) << (P - 1)))) & M


def integ(d):
    w, acc = 0, 0
    for t in range(P):
        if acc:
            w |= 1 << t
        acc ^= (d >> t) & 1
    return w


def find():
    rnd = random.Random(2); h = P // 2; HM = (1 << h) - 1
    A = sum(1 << t for t in range(1, P, 2)); AB = M ^ A
    roots = []
    for _ in range(3000):
        vh = rnd.randrange(1 << h); v = vh | ((vh ^ HM) << h)
        uh = delta(v) & HM & rnd.randrange(1 << h); roots.append((uh | (uh << h), v))

    def succ(s):
        u, v = s; d = u | v
        if bin(d).count('1') & 1:
            return ()
        w = integ(d); return ((v, w), (v, w ^ M))
    seen = set(roots); st = list(roots); edges = {}
    while st:
        s = st.pop(); edges[s] = succ(s)
        for t in edges[s]:
            if t not in seen:
                seen.add(t); st.append(t)
    outdeg = {s: len(e) for s, e in edges.items()}; pred = {}
    for s, e in edges.items():
        for t in e:
            pred.setdefault(t, []).append(s)
    dead = [s for s in edges if outdeg[s] == 0]; fin = set(dead)
    while dead:
        t = dead.pop()
        for s in pred.get(t, ()):
            outdeg[s] -= 1
            if outdeg[s] == 0 and s not in fin:
                fin.add(s); dead.append(s)
    for r in roots:
        if r in fin:
            continue
        path = {}; s = r; i = 0
        while s not in path:
            path[s] = i; i += 1; s = next(t for t in edges[s] if t not in fin)
        cyc = sorted((x for x, j in path.items() if j >= path[s]), key=lambda x: path[x])
        if not set(cyc) <= {(A, AB), (AB, A)}:
            return cyc


def check(cyc):
    n = len(cyc); ok = True
    for i in range(n):
        (u, v), (v2, w) = cyc[i], cyc[(i + 1) % n]
        if v2 != v or bin(u | v).count('1') & 1 or delta(w) != (u | v):
            ok = False
    A = sum(1 << t for t in range(1, P, 2))
    rainlike = all(s in {(A, M ^ A), (M ^ A, A)} for s in cyc)
    white = all(s == (0, 0) for s in cyc)

    def lp(x):
        q = 1
        while q < P and any(((x >> t) & 1) != ((x >> ((t + q) % P)) & 1) for t in range(P)):
            q *= 2
        return q

    def canon(c):
        return min(((c >> k) | (c << (P - k))) & M for k in range(P))
    cols = [s[1] for s in cyc]
    print('states %d, distinct %d, every edge valid (closing edge included): %s, rain %s, white %s' % (
        n, len(set(cyc)), ok, rainlike, white))
    print('column least periods %s; distinct columns %d, up to rotation %d; column weights %s' % (
        sorted(set(lp(c) for c in cols)), len(set(cols)), len(set(canon(c) for c in cols)),
        sorted(set(bin(c).count('1') for c in cols))))


if '--write' in sys.argv:
    cyc = find()
    with open(FILE, 'w') as f:
        f.write('# L1304: a 480-state cycle of the p = 32 pair graph (u v per line, 32-bit hex, bit t = time t)\n')
        for u, v in cyc:
            f.write('%08x %08x\n' % (u, v))
cyc = [tuple(int(x, 16) for x in line.split()) for line in open(FILE) if not line.startswith('#')]
check(cyc)
