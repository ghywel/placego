#!/usr/bin/env python3
"""phase_family_sat.py NMIN NMAX LIMIT: single-column light-speed phases as rings y on Z/N with c(y) = rho^r(y),
c(y)_n = y_n XOR (y_{n-1} OR y_{n-2}) (the two-sided deep-word map), for every lag r in 1..N-1, N = 2^k.
Primitive solutions only (y != rho^{N/2} y). Prints each SAT lag with the time period N/gcd(N, r), the weight, and whether
the solution is a rotation class representative. python-sat CaDiCaL 1.9.5 with a conflict budget per instance."""
import sys, math, time
from pysat.solvers import Solver
NMIN, NMAX, LIMIT = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
def census(N):
    found = []; undecided = []
    t0 = time.time()
    for r in range(1, N):
        per = N // math.gcd(N, r)
        if per < 8: continue
        y = lambda i: (i % N) + 1
        cl = []; nv = N
        for n in range(N):
            nv += 1; o = nv; a, b = y(n-1), y(n-2)
            cl += [[-a, o], [-b, o], [a, b, -o]]
            x, z = y(n-r), y(n)
            cl += [[-x, z, o], [-x, -z, -o], [x, -z, o], [x, z, -o]]   # x = z XOR o
        # primitivity: OR over i of (y_i != y_{i+N/2})
        ds = []
        for i in range(N // 2):
            nv += 1; d = nv; a, b = y(i), y(i + N // 2); ds.append(d)
            cl += [[-d, a, b], [-d, -a, -b]]   # d -> a != b
        cl.append(ds)
        with Solver(name='cadical195', bootstrap_with=cl) as s:
            s.conf_budget(LIMIT)
            res = s.solve_limited()
            if res is True:
                m = s.get_model(); bits = [1 if m[i] > 0 else 0 for i in range(N)]
                # verify
                ok = all(bits[(n - r) % N] == bits[n] ^ (bits[(n-1) % N] | bits[(n-2) % N]) for n in range(N))
                found.append((r, per, sum(bits), ok, ''.join(map(str, bits[:64]))))
            elif res is None:
                undecided.append(r)
    print(f"N={N}: {len(found)} SAT lags, {len(undecided)} undecided (budget {LIMIT} conflicts), {time.time()-t0:.0f} s", flush=True)
    for r, per, w, ok, pre in found: print(f"  r={r} time period {per} weight {w} verified {ok} ring[:64]={pre}", flush=True)
    if undecided: print("  undecided lags:", undecided[:40], flush=True)
N = NMIN
while N <= NMAX:
    census(N); N *= 2
print("PHASE_FAMILY_DONE")
