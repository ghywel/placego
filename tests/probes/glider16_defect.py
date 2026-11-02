#!/usr/bin/env python3
"""L1294 T23 (Local, 2026-11-02): defect trees of the 128-cell glider G16 at p = 16 and 32.
Predictions in reports/rule30-genealogy.md section 29.11. Run: python3 tests/probes/glider16_defect.py
G16's columns: c_k(t) = bit k of c_128^t(y0), k in Z/128; states (c_k, c_(k+1)). Children leaving G16 start trees;
reports tree states, longest path, and entries into the rain, G16, G8 or white.
"""
RING = ('###..#.#.#####....#...##.##.######..#.###.#.##.##..##.##...####.#.....##..###.#.#..#......####...#.#..#..'
        '###.#..##.#...#.##...#.')


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

    m = len(RING)
    y = [1 if ch == '#' else 0 for ch in RING]
    rows = [y]
    for _ in range(p - 1):
        z = rows[-1]
        rows.append([z[k] ^ (z[k - 1] | z[k - 2]) for k in range(m)])
    cols = [sum(rows[t][k] << t for t in range(p)) for k in range(m)]
    g16 = {(cols[k], cols[(k + 1) % m]) for k in range(m)}
    # G8 at this p, all phases
    def c4(v):
        return v ^ ((((v << 1) | (v >> 3)) & 15) | (((v << 2) | (v >> 2)) & 15))
    orb = [1]
    for _ in range(7):
        orb.append(c4(orb[-1]))
    g8 = set()
    for ph in range(8):
        cs = [sum(((orb[(ph + t) % 8] >> k) & 1) << t for t in range(p)) for k in range(4)]
        for k in range(4):
            g8.add((cs[k], cs[(k + 1) % 4]))
    targets = {'rain': {(A, M ^ A), (M ^ A, A)}, 'G16': g16, 'G8': g8, 'white': {(0, 0)}}
    roots = []
    for (u, v) in g16:
        assert pc(u | v) % 2 == 0
        w0 = integ(u | v)
        for w in (w0, w0 ^ M):
            if (v, w) not in g16:
                roots.append((v, w))
    hits = {k: 0 for k in targets}
    seen, stack, longest = set(), [(r, 1) for r in roots], 0
    while stack:
        s, dep = stack.pop()
        if s in seen:
            continue
        seen.add(s); longest = max(longest, dep)
        u, v = s
        if pc(u | v) & 1:
            continue
        w0 = integ(u | v)
        for w in (w0, w0 ^ M):
            t = (v, w)
            hit = [k for k, T in targets.items() if t in T]
            for k in hit:
                hits[k] += 1
            if not hit:
                stack.append((t, dep + 1))
    print(f'p = {p}: G16 states {len(g16)}, roots {len(roots)}, tree states {len(seen)}, longest {longest}, '
          f'entries rain/G16/G8/white: {hits["rain"]}/{hits["G16"]}/{hits["G8"]}/{hits["white"]}')


for p in (16, 32):
    run(p)
print('GLIDER16_DEFECT_DONE')
