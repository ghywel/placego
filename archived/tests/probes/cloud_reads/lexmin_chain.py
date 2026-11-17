"""CL540: the small-bin top-tight peel as a GREEDY CHAIN, sizes (3, 3, 3, X).  A (the top-tight small bin) takes its
lexmin triple (CL536); the next small bin takes its lexmin triple from what is left; the last small bin takes ANY
triple of its target; the big bin takes the rest.  Two orders for the middle bin: smaller remaining target first
('lo') or larger first ('hi').  Then CL524's blind rules for the middle bin (lexmin, minmax, maxmin, refined; both
orders), last bin any triple: 'rules4+swap'.  Run: python3 lexmin_chain.py [M,h,X ...].

OUTCOME (CL540).  Plain chain: lo 95.7-98.8%, hi 95.4-97.8%, either 99.5-99.97%: a pure lexmin chain is not enough.
rules4+swap: 100% at (X, h) = (6, 1) 29,799; (6, 2) 133,684; (6, 3) 347,453; (8, 1) 58,370; (8, 2) 295,134;
(10, 1) 101,650 (965,990 instances); (4, 1) 12,173 all; (4, 2): 2 misses of 46,998; (4, 3): 42 of 104,588; every miss
has EQUAL small targets (holes 1, 9 | 25 25 28 17; holes 6, 8 | 22 22 22 25).
So for X >= 6 on these domains the small-bin top-tight case is solved by a blind two-step chain, no search but the
last bin.
OUTCOME (CL542).  MODE=a ALLR=1: keep top-tightness, take EVERY triple R of sum u_A (not only lexmin): the child is
solved by the chain for every (instance, R): (6,1) 362,861; (6,2) 2,026,835; (8,1) 893,450 pairs, 0 misses (top of R
in the pool's top three for 306,954 / 1,556,843 / 706,029 of them; the rest also solved).  X = 4, h = 1: 44 misses of
112,219, all with equal small targets.  MODE=b (lexmin, top-tightness dropped, A = each small bin of every H(h)
instance): (6,1) 167,795 of 185,517 (90.4%).  Top-tightness carries the small-bin case; lexmin is incidental.
"""
import sys
from itertools import combinations
from collections import Counter
_argv_sl = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/small_toptight_census.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _argv_sl

def lexmin(pool, u):
    for T in combinations(sorted(pool), 3):
        if sum(T) == u: return T
    return None

def pick(pool, u, rule):
    Ts = [T for T in combinations(sorted(pool), 3) if sum(T) == u]
    if not Ts: return None
    if rule == 'lexmin': return Ts[0]
    if rule == 'minmax': return min(Ts, key=lambda T: (T[2], T))
    if rule == 'maxmin': return max(Ts, key=lambda T: (T[0], [-x for x in T]))
    if rule == 'refined':   # CL524: the triple through min(pool) with the largest maximum
        Z = [T for T in Ts if T[0] == min(pool)]
        return max(Z, key=lambda T: T[2]) if Z else None
    return None

RULES = ('lexmin', 'minmax', 'maxmin', 'refined')

def chain4(pool, A, b, c, t):
    """A lexmin; then the middle bin (b or c) by any of three blind rules; the last bin by any triple."""
    R = lexmin(pool, t[A]); p = [x for x in pool if x not in R]
    for mid, last in ((b, c), (c, b)):
        for rule in RULES:
            Q = pick(p, t[mid], rule)
            if Q is not None and lexmin([x for x in p if x not in Q], t[last]) is not None: return rule
    return None

def chain(pool, order, t):
    p = list(pool)
    for j, i in enumerate(order):
        if j == len(order) - 1:
            return lexmin(p, t[i]) is not None      # any triple exists iff a lexmin one does
        R = lexmin(p, t[i])
        if R is None: return False
        p = [x for x in p if x not in R]

def chain4R(pool, R, b, c, t):
    p = [x for x in pool if x not in R]
    for mid, last in ((b, c), (c, b)):
        for rule in RULES:
            Q = pick(p, t[mid], rule)
            if Q is not None and lexmin([x for x in p if x not in Q], t[last]) is not None: return rule
    return None

MODE = __import__('os').environ.get('MODE', '')
ALLR = __import__('os').environ.get('ALLR') == '1'   # MODE=a: every realization of A, not only top-in-top-three

def run(M, h, X):
    C = (3, 3, 3, X); cnt = Counter(); ex = []
    groups = [J for s in (1, 2, 3) for J in combinations(range(4), s)]
    for H in combinations(range(M + 1), h):
        S = [x for x in range(M + 1) if x not in H]; tot = sum(S)
        for u1 in range(3 + 3 * h, 3 * M):
            for u2 in range(u1, 3 * M):
                for u3 in range(u2, 3 * M):
                    t = (u1, u2, u3, tot - u1 - u2 - u3); sig = {}; bad = False
                    for J in groups:
                        r = sum(C[i] for i in J); u = sum(t[i] for i in J); s_ = u - L(r) - h * r
                        if s_ < 0: bad = True; break
                        sig[J] = s_
                    if bad: continue
                    mn = min(sig.values()); arg = [J for J in sig if sig[J] == mn]
                    if MODE == 'b':   # lexmin, no top-tightness: A = each small bin in turn
                        for A in range(3):
                            b, c = [i for i in range(3) if i != A]
                            cnt['b_n'] += 1; ok = chain4(S, A, b, c, t) is not None
                            cnt['b_solved'] += ok
                            if not ok and len(ex) < 4: ex.append((H, t, A))
                        continue
                    if any(len(J) <= 2 for J in arg): continue
                    tops = {[i for i in range(4) if i not in J][0] for J in arg}
                    if tops == {3}: continue
                    A = min(i for i in tops if i < 3); cnt['n'] += 1
                    b, c = sorted((i for i in range(3) if i != A), key=lambda i: t[i])
                    if MODE == 'a':   # top-tight kept; A = every triple of sum u_A whose top is among the top three
                        for R in combinations(S, 3):
                            if sum(R) != t[A] or (R[2] < S[-3] and not ALLR): continue
                            cnt['a_top3'] += R[2] >= S[-3]
                            cnt['a_n'] += 1; ok = chain4R(S, R, b, c, t) is not None
                            cnt['a_solved'] += ok; cnt['a_lexmin'] += R == lexmin(S, t[A])
                            if not ok and len(ex) < 4: ex.append((H, t, A, R))
                        continue
                    lo = chain(S, (A, b, c), t); hi = chain(S, (A, c, b), t)
                    cnt['lo'] += lo; cnt['hi'] += hi; cnt['either'] += lo or hi
                    r4 = chain4(S, A, b, c, t); cnt['rules4+swap'] += r4 is not None
                    if r4 is None:
                        cnt['miss_eq' if t[b] == t[c] else 'miss_neq'] += 1
                        if len(ex) < 4 or t[b] != t[c]: ex.append((H, t, A))
    return cnt, ex

if __name__ == '__main__':
    doms = [tuple(map(int, a.split(','))) for a in sys.argv[1:]] or [(15, 1, 6), (16, 2, 6), (17, 1, 8)]
    for M, h, X in doms:
        cnt, ex = run(M, h, X); print('X', X, 'h', h, 'M', M, dict(cnt), ex, flush=True)
