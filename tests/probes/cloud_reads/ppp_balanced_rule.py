"""CL493: the deterministic rule "most balanced PPP pair" (largest x with y = need - x > x) for pair-least I2
instances: does it complete, and is its completion certified by theorems (G340/G3 when |W| >= 7) or by the
six-value table (|W| = 6: complete iff the target is in the pool's listed spectrum)?
Prediction (written first): completes >= 99.5%; certified-or-table on all completing cases.  Counterfactual: a
completing but uncertifiable case would show the certificate is too weak; a failing case needs a second rule.
OUTCOME (2.5 min): M = 12: 8,256 / 8,274 complete, all certified; M = 13: 59,544 / 59,688, all certified; M = 14:
252,960 / 253,356, all certified.  Every failure has the P side fine and the complement failing at EQUAL targets
(24/24, 27/27, 30/30): the balanced choice leaves an equal-split core; another x repairs it (CL484, 100%).
Prediction held (>= 99.5%; all completions certified).
"""
import itertools, sys
from collections import Counter
_a = sys.argv; sys.argv = ['x']
exec(open('tests/probes/cloud_reads/ppp_certified.py').read().rsplit("\nif __name__ == '__main__':", 1)[0])
sys.argv = _a

def run(M):
    cnt = Counter(); ex = []
    for C in itertools.product(range(3, M - 8), repeat=4):
        if sum(C) != M: continue
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for q in range(1, M):
            S = [x for x in range(M + 1) if x != q]; tot = sum(S); N = len(S)
            sp = spectra(S); mins = lambda c: sum(S[:c]); maxs = lambda c: sum(S[N - c:]); Rf = [M - x for x in reversed(S)]
            for t3 in itertools.product(*[range(mins(C[i]), maxs(C[i]) + 1) for i in range(3)]):
                t = t3 + (tot - sum(t3),)
                tJ = {J: sum(t[i] for i in J) for J in SUB}
                if not all(tJ[J] in sp[CJ[J]] and tJ[J] - mins(CJ[J]) >= 2 and maxs(CJ[J]) - tJ[J] >= 2 for J in SUB): continue
                sl = sorted([(tJ[p] - mins(CJ[p]), 'lo', p) for p in PAIRS] + [(maxs(CJ[p]) - tJ[p], 'up', p) for p in PAIRS])
                sing = min(min(t[i] - mins(C[i]), maxs(C[i]) - t[i]) for i in range(4))
                if not sl[0][0] < sing: continue
                cnt['n'] += 1
                _, side, (X, Y) = sl[0]
                Z, tt = (S, t) if side == 'lo' else (Rf, tuple(C[i] * M - t[i] for i in range(4)))
                m = C[X] + C[Y]; pre = Z[:m - 2]; need = tt[X] + tt[Y] - sum(pre)
                cands = [x for x in Z[m - 2:] if need - x > x and need - x in Z and need - x not in pre]
                if not cands: cnt['no_cand'] += 1; continue
                x = max(cands); y = need - x; P = pre + [x, y]; spP = spectra(P)
                pside = tt[X] in spP[C[X]] or tt[Y] in spP[C[Y]]
                W = [v for v in Z if v not in P]; spW = spectra(W)
                comp = [zb for zb in range(4) if zb not in (X, Y) and tt[zb] in spW[C[zb]]]
                ok = pside and bool(comp); cnt['ok'] += ok
                if ok:
                    certified = False
                    for zb in comp:
                        c = C[zb]; lo = sum(W[:c]); hi = sum(W[len(W) - c:]); d = min(tt[zb] - lo, hi - tt[zb])
                        if len(W) >= 7 and (d >= 5 or (d >= 3 and not g3_bad(W, c, 'lo' if tt[zb] - lo <= hi - tt[zb] else 'hi'))): certified = True
                        if len(W) == 6: certified = True       # the six-value table decides it exactly
                    cnt['cert'] += certified
                    if not certified and len(ex) < 4: ex.append(('uncert', q, C, t))
                elif len(ex) < 4: ex.append(('fail', q, C, t, x, y, pside))
    return cnt, ex

if __name__ == '__main__':
    for M in map(int, sys.argv[1:]):
        cnt, ex = run(M)
        print(M, 'pair-least', cnt['n'], 'balanced rule completes', cnt['ok'], 'certified/table', cnt['cert'], 'no candidate', cnt['no_cand'], ex, flush=True)
