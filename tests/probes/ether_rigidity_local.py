#!/usr/bin/env python3
"""ether_rigidity_local.py: how wide a time window the six-depth rigidity needs (L1259, round 5, T-R2).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/ether_rigidity_local.py KLIST B WLIST

For each K (the episode length is L' = floor(2K/3) + 4, exact pair, edge phase 7 at tick 0, so the ether value at
absolute depth j and tick t is e(t + 2j + 7)), each target cell (depth K-6 or K-5, tick t in 0..L'-5) and each
half-width w in WLIST, it asks whether the cell is forced to the ether value. The test region is depths K-6-B..K+1
and ticks max(0, t-w)..min(L'-1, t+w), with the recurrence where its inputs lie inside and the top pair on the
region's ticks. That region is a sub-system of every real instance with K-6-B >= 0, so a forcing there is a theorem
for the real row. Prints, per K, the cells not forced at each w, and the smallest w forcing every cell.
"""
import os
import subprocess
import sys
import tempfile

E8 = (1, 1, 0, 1, 0, 1, 0, 0)


def eth(j, t):
    return E8[(t + 2 * j + 7) % 8]


def forced(K, Lp, B, jj, t, w, work):
    j0 = K - 6 - B
    t0, t1 = max(0, t - w), min(Lp - 1, t + w)
    T = t1 - t0 + 1
    var = lambda j, s: (j - j0) * T + (s - t0) + 1
    cl = []
    for s in range(t0, t1):
        for j in range(j0 + 2, K + 2):
            a, b, c, d = var(j, s), var(j, s + 1), var(j - 1, s), var(j - 2, s)
            cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
    for s in range(t0, t1 + 1):
        u, v = var(K + 1, s), var(K, s)
        cl += [[u if eth(K + 1, s) else -u], [v if eth(K, s) else -v]]
    x = var(jj, t)
    cl.append([-x] if eth(jj, t) else [x])
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=work)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {(K + 2 - j0) * T} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    p = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
    os.remove(path)
    assert p.returncode in (10, 20)
    return p.returncode == 20


def main():
    ks = [int(x) for x in sys.argv[1].split(',')]
    B = int(sys.argv[2])
    ws = [int(x) for x in sys.argv[3].split(',')]
    work = tempfile.mkdtemp(prefix='rigl-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
    for K in ks:
        Lp = (2 * K) // 3 + 4
        need = {}
        for jj in (K - 6, K - 5):
            for t in range(Lp - 4):
                need[(jj - K, t)] = None
                for w in sorted(ws):
                    if forced(K, Lp, B, jj, t, w, work):
                        need[(jj - K, t)] = w
                        break
        worst = [c for c, w in need.items() if w is None]
        mx = max((w for w in need.values() if w is not None), default=None)
        prof = ' '.join(f"{t}:{need[(-6, t)]}/{need[(-5, t)]}" for t in range(Lp - 4))
        print(f"K={K} L'={Lp} B={B}: not forced at any tested w: {worst}; largest w needed {mx}", flush=True)
        print(f"   per tick t: w needed at depth K-6 / K-5 -> {prof}", flush=True)
    os.rmdir(work)
    print("RIGIDITY_LOCAL_DONE")


if __name__ == '__main__':
    main()
