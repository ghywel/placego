#!/usr/bin/env python3
"""ether_knowledge_map.py: what a top ether window forces below it, cell pair by cell pair (L1259, round 5).

RUN-ON:     cpu (Python 3 + kissat), minutes
COMMAND:    python3 tests/probes/ether_knowledge_map.py K L MODE PHASE [EDGE=0]
            MODE exact: PHASE = i,q (X_K(t) = ether(i, t+q), X_(K+1)(t) = ether(i+1, t+q) for t < L)
            MODE good:  PHASE = p   (good(t+p, X_(K+1)(t), X_K(t)) for t < L)

Region: digits 0..K+1 on ticks 0..L-1 with the recurrence X_j(t+1) = X_j(t) XOR (X_(j-1)(t) OR X_(j-2)(t)) for
j >= 2. With EDGE=0, digits 0 and 1 are free columns: the map is what the top window alone forces. With EDGE=1, the
black edge is added (X_0 = 1, X_1 alternating). For every depth j <= K and tick t, it computes by SAT the exact set
A(j, t) of values the pair (X_(j+1)(t), X_j(t)) can take, as a nibble: bit 2u+v set when (u, v) is possible. It
prints one row per depth (top first), with the good predicate's own nibble at the matching phase psi = t + p_j beside
it, p_j = p + 6(K - j). In the exact mode p = q + 2i. Marks: '.' = A equals good's set; '<' = A strictly inside it;
'>' = A strictly larger (good not forced there); '!' = A empty (the window is UNSAT).
Models found along the way mark allowed values, so most cells need no extra solve.
"""
import os
import random
import subprocess
import sys
import tempfile

WORDS = (43, 202, 178, 172)


def ether(i, t):
    return (WORDS[i % 4] >> (t % 8)) & 1


GOOD = {0: {(0, 1)}, 1: {(1, 0), (1, 1)}, 2: {(0, 0)}, 3: {(1, 0), (1, 1)}, 4: {(0, 0)},
        5: {(0, 1), (1, 0)}, 6: {(1, 0)}, 7: {(1, 0), (1, 1)}}


def nib(s):
    return sum(1 << (2 * u + v) for u, v in s)


def build(K, L, mode, phase, edge):
    var = lambda j, t: j * L + t + 1
    cl = []
    if edge:
        cl += [[var(0, t)] for t in range(L)]
    for t in range(L - 1):
        if edge:
            a, b = var(1, t), var(1, t + 1)
            cl += [[a, b], [-a, -b]]
        for j in range(2, K + 2):
            a, b, c, d = var(j, t), var(j, t + 1), var(j - 1, t), var(j - 2, t)
            cl += [[-a, b, c, d], [a, -b, c, d], [a, b, -c], [-a, -b, -c], [a, b, -d], [-a, -b, -d]]
    for t in range(L):
        u, v = var(K + 1, t), var(K, t)
        if mode == 'exact':
            i, q = phase
            cl += [[v if ether(i, t + q) else -v], [u if ether(i + 1, t + q) else -u]]
        else:
            r = (t + phase) % 8
            cl += {0: [[-u], [v]], 1: [[u]], 2: [[-u], [-v]], 3: [[u]], 4: [[-u], [-v]],
                   5: [[u, v], [-u, -v]], 6: [[u], [-v]], 7: [[u]]}[r]
    return var, (K + 2) * L, cl


def run(nv, cl, extra, work, seed):
    fd, path = tempfile.mkstemp(suffix='.cnf', dir=work)
    with os.fdopen(fd, 'w') as f:
        f.write(f"p cnf {nv} {len(cl) + len(extra)}\n")
        f.write(''.join(' '.join(map(str, c)) + ' 0\n' for c in cl + extra))
    try:
        p = subprocess.run(['kissat', '-q', f'--seed={seed}', path], capture_output=True, text=True)
    finally:
        os.remove(path)
    if p.returncode == 20:
        return None
    assert p.returncode == 10, p.stderr[-300:]
    lits = [int(x) for line in p.stdout.splitlines() if line.startswith('v') for x in line.split()[1:]]
    return {abs(x): x > 0 for x in lits if x}


def main():
    K, L, mode = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    phase = tuple(int(x) for x in sys.argv[4].split(',')) if mode == 'exact' else int(sys.argv[4])
    edge = len(sys.argv) > 5 and sys.argv[5] == '1'
    p = (phase[1] + 2 * phase[0]) if mode == 'exact' else phase
    work = tempfile.mkdtemp(prefix='kmap-', dir=os.environ.get('CAPPED_OUT', os.getcwd()))
    var, nv, cl = build(K, L, mode, phase, edge)
    allowed = {(j, t): set() for j in range(K + 1) for t in range(L)}
    solves = 0

    def absorb(m):
        for (j, t), s in allowed.items():
            s.add((int(m.get(var(j + 1, t), False)), int(m.get(var(j, t), False))))

    m = run(nv, cl, [], work, 1)
    solves += 1
    if m is None:
        print(f"K={K} L={L} {mode} {phase} edge={int(edge)}: UNSAT")
        os.rmdir(work)
        return
    absorb(m)
    rng = random.Random(7)
    for s in range(2, 12):                         # a few more models with other seeds
        m = run(nv, cl, [], work, rng.randrange(1, 10 ** 6))
        solves += 1
        absorb(m)
    for (j, t) in sorted(allowed):
        for u in (0, 1):
            for v in (0, 1):
                if (u, v) in allowed[(j, t)]:
                    continue
                extra = [[var(j + 1, t) if u else -var(j + 1, t)], [var(j, t) if v else -var(j, t)]]
                m = run(nv, cl, extra, work, 1)
                solves += 1
                if m is not None:
                    absorb(m)
    os.rmdir(work)
    print(f"K={K} L={L} mode={mode} phase={phase} p={p % 8} edge={int(edge)} solves={solves}")
    print("row: depth j (distance K-j from the top) | per tick t: A(j,t) nibble then mark vs good at psi = t + p + 6(K-j)")
    for j in range(K, -1, -1):
        cells = []
        for t in range(L):
            a = allowed[(j, t)]
            g = GOOD[(t + p + 6 * (K - j)) % 8]
            mark = '!' if not a else ('.' if a == g else ('<' if a < g else '>' if a > g else 'x'))
            cells.append(f"{nib(a):x}{mark}")
        print(f"j={j:3d} d={K - j:3d} | " + ' '.join(cells))
    print("KNOWLEDGE_MAP_DONE")


if __name__ == '__main__':
    main()
