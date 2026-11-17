#!/usr/bin/env python3
"""ether_rigidity.py: does an ether window force the exact ether pair six depths below it? (L1259, round 5, T-R)

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/ether_rigidity.py MODE KLIST LLIST BLIST [DEPTHS=6]

Reduction lemma under test: if depths K, K+1 match the ether on ticks 0..L'-1, then depths K-6, K-5 match it on
ticks 0..L'-5. With the (6, 4) symmetry of the ether, that would turn an episode of length L+4 at depth k+6 into one
of length L at depth k for the same row: M(k+6) <= M(k) + 4.
The test region is depths K-6-B .. K+1 (relative depths 0..B+7), with the recurrence only where its three lower
inputs are inside the region, so the two lowest depths are free columns. No edge is used. This is weaker than any real
instance: any depth range of a real row satisfies these constraints. Ticks are 0..L'-1, and the top is the exact
pair (MODE exact) or `good` (MODE good) at the phase class with edge phase 7 at tick 0. That is
psi(j, t) = t + 2j + 7 (mod 8) at absolute depth j, with K taken as the absolute depth of the top.
For every target cell (depth K-6 or K-5, tick 0..L'-5) it asks kissat whether the ether value can be violated
(rigidity holds there iff UNSAT). It prints the cells that are NOT forced. With B large the region approaches the
no-edge map's; small B tests locality in depth.
"""
import os
import subprocess
import sys
import tempfile

E8 = (1, 1, 0, 1, 0, 1, 0, 0)            # e(phi), word 43; ether pair at phase phi = (e(phi+2), e(phi))
GOODSET = {0: [(0, 1)], 1: [(1, 0), (1, 1)], 2: [(0, 0)], 3: [(1, 0), (1, 1)], 4: [(0, 0)],
           5: [(0, 1), (1, 0)], 6: [(1, 0)], 7: [(1, 0), (1, 1)]}


def eth(j, t):
    """Ether value at absolute depth j, tick t, in the r = 7 class: e(t + 2j + 7)."""
    return E8[(t + 2 * j + 7) % 8]


def check(mode, K, Lp, B, depths):
    j0 = K - depths - B
    var = lambda j, t: (j - j0) * Lp + t + 1
    cl = []
    for t in range(Lp - 1):
        for j in range(j0 + 2, K + 2):
            a, b, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
    for t in range(Lp):
        u, v = var(K + 1, t), var(K, t)
        if mode == 'exact':
            cl += [[u if eth(K + 1, t) else -u], [v if eth(K, t) else -v]]
        else:
            allowed = GOODSET[(t + 2 * K + 7) % 8]
            for uu in (0, 1):
                for vv in (0, 1):
                    if (uu, vv) not in allowed:
                        cl.append([-u if uu else u, -v if vv else v])
    nv = (K + 2 - j0) * Lp
    work = tempfile.mkdtemp(prefix='rig-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
    unforced = []
    for jj in (K - depths, K - depths + 1):
        for t in range(Lp - 4):
            x = var(jj, t)
            extra = [[-x] if eth(jj, t) else [x]]
            fd, path = tempfile.mkstemp(suffix='.cnf', dir=work)
            with os.fdopen(fd, 'w') as f:
                f.write(f"p cnf {nv} {len(cl) + 1}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl + extra))
            p = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
            os.remove(path)
            assert p.returncode in (10, 20)
            if p.returncode == 10:
                unforced.append((jj - K, t))
    os.rmdir(work)
    return unforced


def main():
    mode = sys.argv[1]
    ks = [int(x) for x in sys.argv[2].split(',')]
    ls = [int(x) for x in sys.argv[3].split(',')]
    bs = [int(x) for x in sys.argv[4].split(',')]
    depths = int(sys.argv[5]) if len(sys.argv) > 5 else 6
    for K in ks:
        for Lp in ls:
            for B in bs:
                u = check(mode, K, Lp, B, depths)
                tag = 'RIGID' if not u else 'not rigid'
                print(f"{mode} K={K} L'={Lp} B={B}: {tag}; unforced (rel depth, tick): {u[:12]}{' ...' if len(u) > 12 else ''}",
                      flush=True)
    print("RIGIDITY_DONE")


if __name__ == '__main__':
    main()
