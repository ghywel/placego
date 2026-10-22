# For prime power q, min degree s, and target order N: is there a set S of q^2+q+1-N points of PG(2,q)
# such that ER_q - S has minimum degree >= s?  (ER_q - S is C4-free automatically.)
# Usage: python3 del_search.py q s Nlo Nhi [per_instance_timeout] [total_budget]
import sys, time, os
from satlib import CNF
from pg import plane

def instance(q, s, N, nbr):
    n = len(nbr)
    m = n - N
    cnf = CNF()
    x = [cnf.var() for _ in range(n)]
    for P in range(n):
        t = len(nbr[P]) - s
        cnf.atmost([x[Q] for Q in nbr[P]], t, guard=x[P])
    cnf.atmost(x, m)
    cnf.atleast(x, m)
    return cnf, x

def check(q, s, S, nbr):
    n = len(nbr)
    Sset = set(S)
    rem = [v for v in range(n) if v not in Sset]
    mind = min(sum(1 for u in nbr[v] if u not in Sset) for v in rem)
    return len(rem), mind

if __name__ == '__main__':
    q, s, Nlo, Nhi = map(int, sys.argv[1:5])
    tmo = int(sys.argv[5]) if len(sys.argv) > 5 else 60
    budget = float(sys.argv[6]) if len(sys.argv) > 6 else 540
    pts, line, ab, nbr = plane(q)
    T0 = time.time()
    here = os.path.dirname(os.path.abspath(__file__))
    for N in range(Nhi, Nlo - 1, -1):
        if time.time() - T0 > budget:
            print('budget exhausted before N=%d' % N, flush=True)
            break
        cnf, x = instance(q, s, N, nbr)
        path = os.path.join(here, 'cnf', 'del_q%d_s%d_N%d.cnf' % (q, s, N))
        os.makedirs(os.path.dirname(path), exist_ok=True)
        rem_t = int(min(tmo, budget - (time.time() - T0))) + 1
        st, model, dt = cnf.solve(path, timeout=rem_t)
        msg = 'q=%d s=%d N=%d n=N-s=%d m=%d : %s (%.1fs)' % (q, s, N, N - s, len(nbr) - N, st, dt)
        if st == 'SATISFIABLE':
            S = [P for P in range(len(nbr)) if x[P] in model]
            nn, mind = check(q, s, S, nbr)
            msg += ' verified order=%d mindeg=%d S=%s' % (nn, mind, S)
            assert nn == N and mind >= s
        print(msg, flush=True)
        os.remove(path)
