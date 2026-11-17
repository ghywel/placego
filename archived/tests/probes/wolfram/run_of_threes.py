#!/usr/bin/env python3
"""L1042: after a reset, runs of 3-gaps are bounded, and the exits are forced.

Local, 2026-10-27. Exact depth-first search over the tail bits of a reset row 000+tail (wall x(t,0) = t mod 2). Each
leaf is decided by three-valued simulation (unknown cells propagate as unknown), so the sets are exact. Expected:
after n 3-gaps the next gap can be 1, 2, 3 or 4 for n <= 4; only 1, 3 or 4 for n = 5; only 4 for n = 6; so no reset
is followed by seven 3-gaps. No solver or sampling. Runs in about three minutes.
"""
X = 2


def OR(p, q):
    return 1 if 1 in (p, q) else (0 if p == q == 0 else X)


def XOR(p, q):
    return X if X in (p, q) else p ^ q


def step(r, w):
    return [XOR(w if i == 0 else r[i - 1], OR(r[i], r[i + 1])) for i in range(len(r) - 1)]


def two(r):
    return step(step(r, 0), 1)


def gaps_prefix(tail, k):
    r, out, z = [0, 0, 0] + tail + [X] * (12 * k), [], 0
    while len(out) < k:
        r = two(r)
        p = r[:3]
        if p == [0, 0, 0]:
            out.append(z)
            z = 0
        elif 1 in p:
            z += 1
        else:
            return out, False
    return out, True


EXPECTED = {1: {1, 2, 3, 4}, 2: {1, 2, 3, 4}, 3: {1, 2, 3, 4}, 4: {1, 2, 3, 4}, 5: {1, 3, 4}, 6: {4}}
for n, want in EXPECTED.items():
    nxt = set()

    def dfs(p):
        g, done = gaps_prefix(p, n + 1)
        if any(x != 3 for x in g[:n]):
            return
        if done:
            nxt.add(g[n])
            return
        dfs(p + [0])
        dfs(p + [1])
    dfs([])
    assert nxt == want, (n, nxt)
    print('after a reset and %d 3-gaps, the next gap is in %s' % (n, sorted(nxt)), flush=True)
