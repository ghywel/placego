#!/usr/bin/env python3
"""Direct SAT test: can distinct moduli dividing N (each divisor d>1 used once, one residue) leave at most U
residues of Z/N uncovered?  u(N) = least such U.  Usage: direct_u.py N U [timelimit_s]
Exactly-one residue per divisor (using every divisor is WLOG for minimising the uncovered set).
Cardinality sum z_n <= U by a sequential counter.  A SAT answer is decoded and re-verified."""
import sys, os, subprocess, itertools, time

def main():
    N = int(sys.argv[1]); U = int(sys.argv[2]); tlim = int(sys.argv[3]) if len(sys.argv) > 3 else 300
    divs = [d for d in range(2, N + 1) if N % d == 0]
    nv = 0; var = {}
    for d in divs:
        for r in range(d):
            nv += 1; var[(d, r)] = nv
    cl = []
    for d in divs:
        lits = [var[(d, r)] for r in range(d)]
        cl.append(lits[:])
        if d <= 6:
            for a, b in itertools.combinations(lits, 2):
                cl.append([-a, -b])
        else:
            prev = None
            for x in lits:
                nv += 1; s = nv
                cl.append([-x, s])
                if prev is not None:
                    cl.append([-prev, s]); cl.append([-x, -prev])
                prev = s
    # symmetry: translate so that the class of the smallest divisor is 0
    d0 = divs[0]
    cl.append([var[(d0, 0)]])
    z = []
    for n in range(N):
        c = [var[(d, n % d)] for d in divs]
        if U > 0:
            nv += 1; z.append(nv); c.append(nv)
        cl.append(c)
    if U > 0 and U < N:
        # sequential counter: s[i][j] = at least j+1 of z[0..i] true, j < U
        s = [[0] * U for _ in range(N)]
        for i in range(N):
            for j in range(U):
                nv += 1; s[i][j] = nv
        for i in range(N):
            cl.append([-z[i], s[i][0]])
            if i > 0:
                for j in range(U):
                    cl.append([-s[i - 1][j], s[i][j]])
                for j in range(1, U):
                    cl.append([-z[i], -s[i - 1][j - 1], s[i][j]])
                cl.append([-z[i], -s[i - 1][U - 1]])
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"du_{N}_{U}.cnf")
    with open(path, 'w') as fh:
        fh.write(f"p cnf {nv} {len(cl)}\n")
        for c in cl:
            fh.write(' '.join(map(str, c)) + ' 0\n')
    t = time.time()
    res = subprocess.run(['kissat', '-q', f'--time={tlim}', path], capture_output=True, text=True)
    st = 'UNKNOWN'
    for line in res.stdout.splitlines():
        if line.startswith('s '):
            st = line[2:].strip()
    msg = f"N={N} divisors>1={len(divs)} U={U} vars={nv} clauses={len(cl)} kissat={st} {time.time()-t:.1f}s"
    if st == 'SATISFIABLE':
        vals = set(int(tk) for line in res.stdout.splitlines() if line.startswith('v ')
                   for tk in line[2:].split() if int(tk) > 0)
        choice = {}
        for (d, r), v in var.items():
            if v in vals:
                assert d not in choice; choice[d] = r
        unc = [n for n in range(N) if not any(n % d == r for d, r in choice.items())]
        msg += f" | verified uncovered={len(unc)} (<=U: {len(unc) <= U}) classes={choice}"
    print(msg, flush=True)
    os.remove(path)

if __name__ == '__main__':
    main()
