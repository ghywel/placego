"""CL486: prefix-plus-pair (PPP) boundaries for the one-hole four-bin problem, all instance classes, and pair-choice rules.

PPP for a pair (X, Y) of the four bins, in the frame where the pair's slack is a LOWER slack: P = the m-2 smallest
pool values plus one pair {x, y}, m = c_X + c_Y, sum t_X + t_Y; P completes if t_X in Sigma_(c_X)(P) and some other
t_Z in Sigma_(c_Z)(S minus P).
For every I2 instance (all 14 group spectra feasible, every margin >= 2) record:
  any    : some pair of bins (both orientations, i.e. lower frame or reflected) has a completing PPP;
  least  : the least-slack pair (in its own frame) has one;
  rules  : for the least-slack pair, does the rule "smallest x", "largest x" (most balanced pair), or "x closest to
           the hole" pick a completing PPP?
Predictions (written first): 'least' is 100% for pair-least instances (as in CL484) and >= 99% overall; 'any' is
100%; "largest x" is the best single rule.  Counterfactual: 'any' < 100% means PPP is not a universal boundary.

OUTCOME (M = 12, 12 s): pair-least 8,274: least-pair PPP 8,274 (100%); rules smallest-x 7,566, largest-x
8,256 (99.8%), nearest-hole 7,980.  Singleton-least 114,703: least-pair PPP 91,180, some pair 102,470, so
PPP is NOT universal (prediction failed there); 5 instances (q1 3333 (8,20,20,29) ...) have no PPP at all.
"""
import itertools, sys
from collections import Counter
T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]
PAIRS = list(itertools.combinations(range(4), 2))

def spectra(pool):
    sp = [set() for _ in range(len(pool) + 1)]; sp[0].add(0)
    for x in pool:
        for k in range(len(pool) - 1, -1, -1):
            if sp[k]: sp[k + 1] |= {s + x for s in sp[k]}
    return sp

def ppp_candidates(Z, m, target):
    pre = Z[:m - 2]; need = target - sum(pre); out = []
    rest_vals = Z[m - 2:]
    for x in rest_vals:
        y = need - x
        if y <= x or y not in rest_vals: continue
        out.append((x, y, pre + [x, y]))
    return out

def completes(Z, P, C, tt, X, Y):
    rest = [v for v in Z if v not in P]
    if tt[X] not in spectra(P)[C[X]]: return False
    spR = spectra(rest)
    return any(tt[z] in spR[C[z]] for z in range(4) if z not in (X, Y))

def run(M, limit=None):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:])
            R = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                cnt['n'] += 1
                tr = tuple(C[i] * M - t[i] for i in range(4))
                slacks = []
                for pr in PAIRS:
                    slacks.append((tJ[pr] - mins(CJ[pr]), 'lo', pr)); slacks.append((maxs(CJ[pr]) - tJ[pr], 'up', pr))
                slacks.sort()
                sing = min(min(t[i] - mins(C[i]), maxs(C[i]) - t[i]) for i in range(4))
                cat = 'pair-least' if slacks[0][0] < sing else 'singleton-least'
                cnt[(cat, 'n')] += 1
                def frame(side): return (S, t) if side == 'lo' else (R, tr)
                # least pair, rules
                h, side, (X, Y) = slacks[0]; Z, tt = frame(side)
                cands = ppp_candidates(Z, C[X] + C[Y], tt[X] + tt[Y])
                goods = [c for c in cands if completes(Z, c[2], C, tt, X, Y) or completes(Z, c[2], C, tt, Y, X)]
                least_ok = bool(goods)
                cnt[(cat, 'least')] += least_ok
                if cands:
                    hole = q if side == 'lo' else M - q
                    for name, key in (('smallest x', lambda c: c[0]), ('largest x', lambda c: -c[0]), ('x nearest hole', lambda c: abs(c[0] - hole))):
                        pick = min(cands, key=key)
                        cnt[(cat, name)] += pick in goods
                any_ok = least_ok
                if not any_ok:
                    for h2, side2, (X2, Y2) in slacks[1:]:
                        Z2, tt2 = frame(side2)
                        for c in ppp_candidates(Z2, C[X2] + C[Y2], tt2[X2] + tt2[Y2]):
                            if completes(Z2, c[2], C, tt2, X2, Y2) or completes(Z2, c[2], C, tt2, Y2, X2): any_ok = True; break
                        if any_ok: break
                cnt[(cat, 'any')] += any_ok
                if not any_ok and len(ex) < 5: ex.append((q, C, t))
                if limit and cnt['n'] >= limit: return cnt, ex
    return cnt, ex

if __name__ == '__main__':
    M = int(sys.argv[1]); limit = int(sys.argv[2]) if len(sys.argv) > 2 else None
    cnt, ex = run(M, limit)
    for cat in ('pair-least', 'singleton-least'):
        n = cnt[(cat, 'n')]
        print(M, cat, 'n', n, 'least-pair PPP', cnt[(cat, 'least')], 'some pair PPP', cnt[(cat, 'any')],
              '| rules on least pair: smallest x', cnt[(cat, 'smallest x')], 'largest x', cnt[(cat, 'largest x')], 'x nearest hole', cnt[(cat, 'x nearest hole')])
    print('no PPP at all:', ex, flush=True)
