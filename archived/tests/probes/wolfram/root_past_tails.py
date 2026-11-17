#!/usr/bin/env python3
"""L1032: the root's full-line pasts, counted by right-tail type (carrying check of GC1981/82/84, extended).

Local, 2026-10-27. Prediction written in L1031 before any run: the right-tail periods keep growing, so there is no
finite set of tail types.

Method (exact, no search).
- Every predecessor row is fixed by its right ray, then extends uniquely leftwards (left-permutivity).
- For a periodic target tail y of period p, the parent pairs s_i = (x_i, x_(i+1)) satisfy s_(i-1) = G_(y_i)(s_i),
  with G_b(c, r) = (b XOR (c OR r), c) (GPT's GC1984 tables).
- Infinite parent rays are exactly the periodic points of the one-period composite map M on 4 pair states. A point
  outside M's cycles has only finite chains.
- Each ray found is verified against its target tail.

Outcome (2026-10-27, M5, under 1 s):
- Row counts by depth: 1, 2, 5, 8, 14, 20, 26, 32, 44, 56, 74, 98, 122. The first four agree with GPT's hand
  counts.
- Largest tail period by depth: 1, 3, 3, 6 (depths 4 to 9), then 12 (depths 10 to 12). The prediction held to
  depth 12. Counts grow far below 4^k.
"""
def G(b, s):
    c, r = s
    return (b ^ (c | r), c)


def rays(y):
    p = len(y)

    def M(s):
        for i in range(p, 0, -1):
            s = G(y[i % p], s)
        return s
    cyc = set()
    for s in [(a, b) for a in (0, 1) for b in (0, 1)]:
        seen, x = [], s
        while x not in seen:
            seen.append(x)
            x = M(x)
        cyc.update(seen[seen.index(x):])
    out = []
    for s in cyc:
        cl, t = 1, M(s)
        while t != s:
            t, cl = M(t), cl + 1
        chain = [s]
        for _ in range(cl - 1):
            chain.append([v for v in cyc if M(v) == chain[-1]][0])
        bits = [None] * (p * cl)
        for k in range(cl):
            cur, pos = chain[(k + 1) % cl], (k + 1) * p
            for i in range(p, 0, -1):
                cur = G(y[i % p], cur)
                pos -= 1
                bits[pos % (p * cl)] = cur[0]
        out.append(tuple(bits))
    return out


def maps_to(x, y):
    n = len(x) * len(y)
    xx = [x[i % len(x)] for i in range(n + 2)]
    return all((xx[i - 1] ^ (xx[i] | xx[i + 1])) == y[i % len(y)] for i in range(1, n + 1))


if __name__ == '__main__':
    level, counts, periods = [(0,)], [1], []
    for d in range(1, 13):
        level = [x for y in level for x in rays(y) if maps_to(x, y) or (_ for _ in ()).throw(AssertionError)]
        counts.append(len(level))
        periods.append(max(len(x) for x in level))
    print("row counts by depth:", counts)
    print("largest tail period by depth 1..12:", periods)
