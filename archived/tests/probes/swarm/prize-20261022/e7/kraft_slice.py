#!/usr/bin/env python3
"""Kraft slicing test for odd distinct coverings with lcm dividing 3^a * m (all a at once).

Lemma (union bound on a 3-adic slice): write Z/(3^a m) = Z/3^a x Z/m.  A progression with modulus 3^i d'
(d' | m) is "active" on the slice over y in Z/m iff y lies in its class mod d'; on that slice it covers one
class mod 3^i, i.e. a fraction 3^-i.  If for some y the active 3-weights sum to < 1, the slice is not covered.
Pure powers of 3 (d' = 1) are active everywhere with total T <= sum_{i>=1} 3^-i < 1/2.
So a covering needs, for every y:  sum_{d'>1, d'|m} sum_i 3^-i [ (i,d') used, y in its class ] > 1/2.
Relaxation in the coverer's favour: keep only i < L and give each family d' its whole tail (3/2)3^-L everywhere.
In integers (x 3^(L-1)):  S(y) >= theta' := floor((3^(L-1) - (tau(m)-1)) / 2).
If the relaxed system is UNSAT, there is no distinct covering with lcm | 3^a m for ANY a.

Usage: kraft_slice.py m_factors L [theta_override] [timelimit]
  m_factors like "5,7" or "5^2,7" ;  theta_override 'auto' or an integer (scaled units).
"""
import sys, os, subprocess, itertools, time

T0 = time.time()

def parse_m(s):
    fac = []
    for part in s.split(','):
        if '^' in part:
            p, e = part.split('^'); fac.append((int(p), int(e)))
        else:
            fac.append((int(part), 1))
    return fac

def divisors_from(fac):
    ds = [1]
    for p, e in fac:
        ds = [d * p**k for d in ds for k in range(e + 1)]
    return sorted(ds)

def main():
    fac = parse_m(sys.argv[1])
    L = int(sys.argv[2])
    th_arg = sys.argv[3] if len(sys.argv) > 3 else 'auto'
    tlim = int(sys.argv[4]) if len(sys.argv) > 4 else 300
    q = int(os.environ.get('Q', '3'))
    m = 1
    for p, e in fac:
        m *= p**e
    assert m % q != 0 and m % 2 == 1
    divs = [d for d in divisors_from(fac) if d > 1]
    tau1 = len(divs)
    if th_arg == 'auto':
        theta = (q**(L - 1) * (q - 2) - tau1) // (q - 1)
    else:
        theta = int(th_arg)
    W = [q**(L - 1 - i) for i in range(L)]  # integer weights of q-exponents i = 0..L-1
    # variables x[(i,d,r)] : family (i,d) uses residue r mod d
    nv = 0
    var = {}
    for i in range(L):
        for d in divs:
            for r in range(d):
                nv += 1; var[(i, d, r)] = nv
    clauses = []
    # at most one residue per family (sequential AMO via pairwise for small d, ladder for large)
    for i in range(L):
        for d in divs:
            lits = [var[(i, d, r)] for r in range(d)]
            if d <= 8:
                for a, b in itertools.combinations(lits, 2):
                    clauses.append([-a, -b])
            else:
                # ladder encoding
                prev = None
                for k, x in enumerate(lits):
                    nv += 1; s = nv
                    clauses.append([-x, s])
                    if prev is not None:
                        clauses.append([-prev, s])
                        clauses.append([-x, -prev])
                    prev = s
    # symmetry: translation lets us fix family (0, smallest prime) residue to 0 if used
    p0 = min(divs)
    for r in range(1, p0):
        clauses.append([-var[(0, p0, r)]])
    # per point y: sum_{(i,d)} W[i] * x[(i,d,y mod d)] >= theta  (BDD-like DP encoding)
    for y in range(m):
        terms = [(W[i], var[(i, d, y % d)]) for i in range(L) for d in divs]
        terms.sort(key=lambda t: -t[0])
        # suffix max sums for pruning
        suf = [0] * (len(terms) + 1)
        for k in range(len(terms) - 1, -1, -1):
            suf[k] = suf[k + 1] + terms[k][0]
        if suf[0] < theta:
            clauses.append([])  # trivially impossible
            continue
        # A(k, s): "terms k.. must contribute >= s"; root A(0, theta) true.
        memo = {}
        def node(k, s):
            nonlocal nv
            if s <= 0:
                return 'T'
            if suf[k] < s:
                return 'F'
            key = (k, s)
            if key in memo:
                return memo[key]
            nv += 1; a = nv
            memo[key] = a
            w, x = terms[k]
            hi = node(k + 1, s - w)
            lo = node(k + 1, s)
            # a -> (x and hi) or (not x and lo)  ; monotone: a -> lo or (x and hi)
            # encode: a -> (lo or x) ; a -> (lo or hi)
            if lo == 'T':
                return a
            if lo == 'F':
                clauses.append([-a, x])
                if hi == 'F':
                    clauses.append([-a])
                elif hi != 'T':
                    clauses.append([-a, hi])
            else:
                if hi == 'F':
                    clauses.append([-a, lo])
                elif hi == 'T':
                    clauses.append([-a, lo, x])
                else:
                    clauses.append([-a, lo, x])
                    clauses.append([-a, lo, hi])
            return a
        sys.setrecursionlimit(100000)
        root = node(0, theta)
        if root == 'F':
            clauses.append([])
        elif root != 'T':
            clauses.append([root])
    tag = f"q{q}_m{m}_L{L}_th{theta}"
    cnf = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"ks_{tag}.cnf")
    with open(cnf, 'w') as fh:
        fh.write(f"p cnf {nv} {len(clauses)}\n")
        for c in clauses:
            fh.write(' '.join(map(str, c)) + ' 0\n')
    print(f"q={q} m={m} fac={fac} divisors>1={divs} L={L} theta'={theta} (of scale {q**(L-1)}; "
          f"theta={theta/q**(L-1):.5f}) vars={nv} clauses={len(clauses)} build={time.time()-T0:.1f}s", flush=True)
    t1 = time.time()
    res = subprocess.run(['kissat', '-q', f'--time={tlim}', cnf], capture_output=True, text=True)
    out = res.stdout
    status = 'UNKNOWN'
    for line in out.splitlines():
        if line.startswith('s '):
            status = line[2:].strip()
    print(f"kissat: {status} in {time.time()-t1:.1f}s", flush=True)
    if status == 'SATISFIABLE':
        vals = set()
        for line in out.splitlines():
            if line.startswith('v '):
                for t in line[2:].split():
                    v = int(t)
                    if v > 0:
                        vals.add(v)
        # decode and verify independently
        fam = {}
        for (i, d, r), v in var.items():
            if v in vals:
                assert (i, d) not in fam, "AMO violated"
                fam[(i, d)] = r
        worst = None
        for y in range(m):
            s = sum(W[i] for (i, d), r in fam.items() if y % d == r)
            worst = s if worst is None else min(worst, s)
        print(f"verified: min over y of S(y) = {worst} (theta'={theta}) ok={worst >= theta}")
        print("families used (i, d') -> residue:", dict(sorted(fam.items())))
    os.remove(cnf)

if __name__ == '__main__':
    main()
