#!/usr/bin/env python3
"""ether_core_ticks.py: which top ticks a refutation of the extra tick needs (L1259, round 5, T-K).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/ether_core_ticks.py KLIST MODE

For each k in KLIST (comma-separated, k = 0 or 2 mod 6) and L = floor(2k/3) + 4, the instance of
ether_episode_sat.py (black edge, digits 1..k+1, ticks 0..L-1) is UNSAT in every phase. For the phases whose edge
phase at tick 0 is r = (p + 6k) mod 8 = 7 (p = q + 2i in the exact mode), the top constraint is kept only on a tick
set T, and T is shrunk greedily while the instance stays UNSAT. There are two orders, earliest tick first and
latest tick first, and both give a deletion-minimal T (each remaining tick is necessary). It prints T as runs of
ticks. Control: the full window is UNSAT and the empty window is SAT. MODE is exact or good.
"""
import os
import subprocess
import sys
import tempfile

WORDS = (43, 202, 178, 172)


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def var(j, t, L):
    return (j - 1) * L + t + 1


def base(k, L):
    cl = []
    for t in range(L - 1):
        for j in (1, 2):
            a, b = var(j, t, L), var(j, t + 1, L)
            cl += [[a, b], [-a, -b]]
        for j in range(3, k + 2):
            a, b, c, d = var(j, t, L), var(j, t + 1, L), var(j - 1, t, L), var(j - 2, t, L)
            cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
    return cl


def top(k, L, mode, phase, ticks):
    cl = []
    for t in ticks:
        u, v = var(k + 1, t, L), var(k, t, L)
        if mode == 'exact':
            i, q = phase
            cl += [[v if ether(i, t + q) else -v], [u if ether(i + 1, t + q) else -u]]
        else:
            r = (t + phase) % 8
            cl += {0: [[-u], [v]], 1: [[u]], 2: [[-u], [-v]], 3: [[u]], 4: [[-u], [-v]],
                   5: [[u, v], [-u, -v]], 6: [[u], [-v]], 7: [[u]]}[r]
    return cl


def sat(nv, cl, work):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=work)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
    try:
        p = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    assert p.returncode in (10, 20), p.stderr[-300:]
    return p.returncode == 10


def runs(ts):
    out, ts = [], sorted(ts)
    for t in ts:
        if out and t == out[-1][1] + 1:
            out[-1][1] = t
        else:
            out.append([t, t])
    return ','.join(f"{a}" if a == b else f"{a}-{b}" for a, b in out)


def main():
    ks = [int(x) for x in sys.argv[1].split(',')]
    mode = sys.argv[2]
    work = tempfile.mkdtemp(prefix='core-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
    for k in ks:
        m = (2 * k) // 3
        L = m + 4
        cl0, nv = base(k, L), (k + 1) * L
        if mode == 'exact':
            phases = [(i, q) for i in (0, 1) for q in range(8) if (q + 2 * i + 6 * k) % 8 == 7]
        else:
            phases = [p for p in range(8) if (p + 6 * k) % 8 == 7]
        for ph in phases:
            full = list(range(L))
            assert not sat(nv, cl0 + top(k, L, mode, ph, full), work), "full window SAT"
            assert sat(nv, cl0, work), "empty window UNSAT"
            res = []
            for order in (full, full[::-1]):
                T = set(full)
                for t in order:
                    T2 = T - {t}
                    if not sat(nv, cl0 + top(k, L, mode, ph, sorted(T2)), work):
                        T = T2
                res.append(T)
            print(f"k={k:3d} k%6={k % 6} L={L:3d} {mode} phase={ph}: minimal T, early-first [{runs(res[0])}] "
                  f"({len(res[0])} ticks); late-first [{runs(res[1])}] ({len(res[1])} ticks); L-1={L - 1}", flush=True)
    os.rmdir(work)
    print("CORE_TICKS_DONE")


if __name__ == '__main__':
    main()
