#!/usr/bin/env python3
"""L1294 T19 (Local, 2026-11-02): defect trees of the 4-cell light-speed glider (period 8), p = 8, 16, 32, 64.
Predictions in reports/rule30-genealogy.md section 29.3, written first. Run: python3 tests/probes/glider_defect.py

The glider: c_4 orbit of a single black cell on a 4-cell ring, c_4(y) = y ^ ((y<<1) | (y<<2)) with wrap. Its columns
c_k(t) = bit k of c_4^t(y0), k in Z/4, t in Z/8, give 4 pair-graph states per phase; all 8 time phases are used. From
each glider state, the child that is not the next glider state starts a defect tree. Reports per p: tree states,
longest path, and entries into the rain, the glider (any phase) or white.
"""


def run(p):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    pc = lambda x: bin(x).count('1')

    def integ(d):
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M
            s <<= 1
        return (y << 1) & M

    def c4(y):
        r1 = ((y << 1) | (y >> 3)) & 15
        r2 = ((y << 2) | (y >> 2)) & 15
        return y ^ (r1 | r2)

    orbit = [1]
    for _ in range(7):
        orbit.append(c4(orbit[-1]))
    assert c4(orbit[-1]) == 1 and len(set(orbit)) == 8
    glider = set()
    for ph in range(8):                       # time phase: start the ring at orbit[ph]
        cols = [sum(((orbit[(ph + t) % 8] >> k) & 1) << t for t in range(p)) for k in range(4)]
        for k in range(4):
            glider.add((cols[k], cols[(k + 1) % 4]))
    rain = {(A, M ^ A), (M ^ A, A)}
    targets = {'rain': rain, 'glider': glider, 'white': {(0, 0)}}
    roots = []
    for (u, v) in glider:
        d = u | v
        assert pc(d) % 2 == 0
        w0 = integ(d)
        for w in (w0, w0 ^ M):
            if (v, w) not in glider:
                roots.append((v, w))
    hits = {k: 0 for k in targets}
    seen, stack, longest = set(), [(r, 1) for r in roots], 0
    while stack:
        (u, v), dep = stack.pop()
        if (u, v) in seen:
            continue
        seen.add((u, v)); longest = max(longest, dep)
        d = u | v
        if pc(d) & 1:
            continue
        w0 = integ(d)
        for w in (w0, w0 ^ M):
            s = (v, w)
            hit = [k for k, T in targets.items() if s in T]
            for k in hit:
                hits[k] += 1
            if not hit:
                stack.append((s, dep + 1))
    print(f'p = {p:2d}: glider states {len(glider)}, defect roots {len(roots)}, defect-tree states {len(seen)}, '
          f'longest path {longest}, entries into rain/glider/white: {hits["rain"]}/{hits["glider"]}/{hits["white"]}')


for p in (8, 16, 32, 64):
    run(p)
print('GLIDER_DEFECT_DONE')
