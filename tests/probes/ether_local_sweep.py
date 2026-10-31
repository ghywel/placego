#!/usr/bin/env python3
"""ether_local_sweep.py: a sound top-down local propagation for the ether-episode window (L1259, round 5, T-L).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/ether_local_sweep.py K L MODE PHASE [U=3] [B=4] [A=3] [Bt=4] [WORKERS=6] [ROWS=0]
            MODE exact: PHASE = i,q; MODE good: PHASE = p (as in ether_episode_sat.py)

The full instance (black edge, digits 0..K+1, ticks 0..L-1, top constraint at depth K) is the CNF of
ether_episode_sat.py. Here no global solve is made. Knowledge is a set A(j, t) of possible values of the pair
(X_(j+1)(t), X_j(t)), kept as a nibble (bit 2u+v). It starts with the top constraint at j = K and "anything" elsewhere,
and is refined depth by depth from j = K down to j = 0. A value (u, v) is removed from A(j, t) when the LOCAL CSP is
UNSAT. The local CSP has:
- cells: depths max(0, j-B)..min(K+1, j+U+1), ticks max(0, t-A)..min(L-1, t+Bt);
- every recurrence whose four cells lie in the window, plus the edge (X_0 = 1) where depth 0 is in it;
- the current sets A(i, s) for every pair (i, i+1) inside the window, with i >= j;
- the trial value (u, v) at (j, t).
Each local CSP is a relaxation of the full instance, and every set used was itself derived soundly, so A(j, t) always
contains every value the pair takes in some solution. An empty set therefore proves the full instance UNSAT.
At each depth, ticks are swept forward then backward until no set changes. Prints per depth the end e of the
exact-ether run of single values from tick 0, the partial front after it, the number of solves and, with ROWS=1, the
whole nibble row. A soundness control is the caller's job: run SAT instances (they must never be refuted).
"""
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

WORDS = (43, 202, 178, 172)
TOPSET = {0: 0b0010, 1: 0b1100, 2: 0b0001, 3: 0b1100, 4: 0b0001, 5: 0b0110, 6: 0b0100, 7: 0b1100}


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


def main():
    K, L, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    phase = tuple(int(x) for x in sys.argv[4].split(',')) if mode == 'exact' else int(sys.argv[4])
    U, B, A, Bt, WORKERS = (int(sys.argv[i]) if len(sys.argv) > i else d for i, d in ((5, 3), (6, 4), (7, 3), (8, 4), (9, 6)))
    ROWS = len(sys.argv) > 10 and sys.argv[10] == '1'
    work = tempfile.mkdtemp(prefix='sweep-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
    know = {}
    for t in range(L):
        if mode == 'exact':
            i, q = phase
            know[(K, t)] = 1 << (2 * ether(i + 1, t + q) + ether(i, t + q))
        else:
            know[(K, t)] = TOPSET[(t + phase) % 8]

    def get(j, t):
        return know.get((j, t), 0b1111)

    def local_sat(j, t, u, v):
        j0, j1 = max(0, j - B), min(K + 1, j + U + 1)
        t0, t1 = max(0, t - A), min(L - 1, t + Bt)
        idx = {}
        for jj in range(j0, j1 + 1):
            for tt in range(t0, t1 + 1):
                idx[(jj, tt)] = len(idx) + 1
        cl = []
        for (jj, tt), x in idx.items():
            if jj == 0:
                cl.append([x])
            if tt + 1 <= t1 and jj >= 1 and (jj - 1, tt) in idx and (jj == 1 or (jj - 2, tt) in idx):
                a, b, c = x, idx[(jj, tt + 1)], idx[(jj - 1, tt)]
                if jj == 1:                                  # X_1(t+1) = X_1(t) XOR X_0(t)
                    cl += [[-a, -b, -c], [a, b, -c], [-a, b, c], [a, -b, c]]
                else:
                    d = idx[(jj - 2, tt)]
                    cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
        for jj in range(max(j, j0), j1):
            for tt in range(t0, t1 + 1):
                s = get(jj, tt)
                if s == 0b1111:
                    continue
                hi, lo = idx[(jj + 1, tt)], idx[(jj, tt)]
                for uu in (0, 1):
                    for vv in (0, 1):
                        if not (s >> (2 * uu + vv)) & 1:
                            cl.append([-hi if uu else hi, -lo if vv else lo])
        hi, lo = idx[(j + 1, t)], idx[(j, t)]
        cl += [[hi if u else -hi], [lo if v else -lo]]
        fd, path = tempfile.mkstemp(suffix='.cnf', dir=work)
        with os.fdopen(fd, 'w') as f:
            f.write(f"p cnf {len(idx)} {len(cl)}\n" + ''.join(' '.join(map(str, c)) + ' 0\n' for c in cl))
        try:
            p = subprocess.run(['kissat', '-q', '-n', path], capture_output=True, text=True)
        finally:
            os.remove(path)
        assert p.returncode in (10, 20), p.stderr[-300:]
        return p.returncode == 10

    total = 0
    empty_at = None
    with ThreadPoolExecutor(WORKERS) as ex:
        for j in range(K, -1, -1):
            solves = 0
            changed = True
            while changed and empty_at is None:
                changed = False
                for order in (range(L), range(L - 1, -1, -1)):
                    for t in order:
                        s = get(j, t)
                        cands = [(u, v) for u in (0, 1) for v in (0, 1) if (s >> (2 * u + v)) & 1]
                        res = list(ex.map(lambda uv: local_sat(j, t, uv[0], uv[1]), cands))
                        solves += len(cands)
                        ns = sum(1 << (2 * u + v) for (u, v), r in zip(cands, res) if r)
                        if ns != s:
                            know[(j, t)] = ns
                            changed = True
                        if ns == 0:
                            empty_at = (j, t)
                            break
                    if empty_at:
                        break
            total += solves
            row = [get(j, t) for t in range(L)]
            e = -1
            for t, s in enumerate(row):
                if s in (1, 2, 4, 8):
                    e = t
                else:
                    break
            front = ''.join(f"{s:x}" for s in row[e + 1:] if s != 0b1111)
            line = f"j={j:3d} d={K - j:3d} exact to {e:3d} front {front:10s} solves {solves}"
            if ROWS:
                line += " | " + ' '.join(f"{s:x}" for s in row)
            print(line, flush=True)
            if empty_at:
                print(f"EMPTY SET at depth {empty_at[0]} tick {empty_at[1]}: instance UNSAT (sound refutation)")
                break
    os.rmdir(work)
    print(f"K={K} L={L} mode={mode} phase={phase} U={U} B={B} A={A} Bt={Bt} total solves {total} "
          f"result {'REFUTED' if empty_at else 'not refuted'}")
    print("LOCAL_SWEEP_DONE")


if __name__ == '__main__':
    main()
