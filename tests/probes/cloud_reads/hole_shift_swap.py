"""CL475 bounded test: induction on the hole position, with the rooting problem repaired by adjacent swaps.

Pools P_q = [0, M] minus {q}.  Replacing token q by q+1 maps a partition of P_(q+1) with targets t - e_i
to one of P_q with targets t - e_i + e_j, where j is the bin that held q.  If j != i, try to move one unit
from bin j to bin i by ADJACENT SWAPS: v in bin A and v+1 in bin B (both in P_q) exchange, giving A +1, B -1.
Bin graph: edge B -> A when some v in A has v+1 in B.  Repair is possible when i is reachable from j
(path realisability is checked by actually performing the swaps).

Step statement tested (adversarial, all partitions): for every baseline-protected (t_J >= T_(C_J))
instance on P_q, sizes all >= 3, there is a bin i such that t - e_i is protected on P_(q+1) and EVERY
partition of (P_(q+1), t - e_i) is repaired to (P_q, t).  Base q + 1 = M is the full interval.
Predictions: the step holds for every instance at M = 12 except possibly a few with tight groups;
an obstruction has the reachable set's tokens forming initial segments of both blocks (proved by hand).
Counterfactual: frequent adversarial failures mean the route needs a choice of partition, not just of i.

OUTCOME (M = 12, sizes 3333, all holes, 70,119 protected instances): the adversarial step holds in only
14,973 (no tight group: 12,033 of 53,209; with a tight group: 2,940 of 16,910).  Repair from SOME
source partition works in all but the 198 instances with no admissible i (all have a tight group).
Prediction FAILED: adjacent swaps do not repair the rooting problem; the route needs a choice of
source partition, which is the original difficulty.
"""
import itertools, sys
from collections import defaultdict

T = lambda n: n * (n + 1) // 2
SUB = [J for s in (1, 2, 3) for J in itertools.combinations(range(4), s)]

def partitions(pool, C):
    pool = list(pool)
    def rec(rest, b):
        if b == 3:
            yield (tuple(rest),); return
        for comb in itertools.combinations(rest, C[b]):
            s = set(comb); rem = [x for x in rest if x not in s]
            for tail in rec(rem, b + 1): yield (comb,) + tail
    yield from rec(pool, 0)

def repair(bins, j, i, pool):
    """Move one unit from bin j to bin i by adjacent swaps; return True if achieved."""
    bins = [set(b) for b in bins]
    for _ in range(8):
        where = {v: k for k, b in enumerate(bins) for v in b}
        # BFS from j over edges B -> A (v in A, v+1 in B)
        prev = {j: None}; frontier = [j]
        while frontier:
            nf = []
            for B in frontier:
                for v1 in bins[B]:
                    v = v1 - 1
                    if v in where and where[v] not in prev:
                        prev[where[v]] = (B, v); nf.append(where[v])
            frontier = nf
        if i not in prev: return False
        # do the swap on the LAST edge of the path first (into i), then re-plan
        path = []; x = i
        while prev[x] is not None: path.append((prev[x][0], x, prev[x][1])); x = prev[x][0]
        B, A, v = path[0]          # edge B -> A = i
        bins[A].remove(v); bins[A].add(v + 1); bins[B].remove(v + 1); bins[B].add(v)
        if B == j: return True
        j_new = B
        # now bin B is short by one; continue moving one unit from j to B
        i = B
    return False

def run(M, C):
    res = dict(instances=0, step_ok=0, no_admissible=0, fail=[], adv_fail_examples=[])
    for q in range(1, M):
        src_pool = [x for x in range(M + 1) if x != q + 1]      # q + 1 = M gives the full interval [0, M-1]
        S = T(M) - q
        by_target = defaultdict(list)
        for p in partitions(src_pool, C):
            tau = tuple(sum(b) for b in p)
            j = next(k for k in range(4) if q in p[k])
            by_target[tau].append((p, j))
        CJ = {J: sum(C[i] for i in J) for J in SUB}
        for t3 in itertools.product(*[range(T(C[i]), S - T(M - C[i]) + 1) for i in range(3)]):
            t = t3 + (S - sum(t3),)
            if not all(sum(t[i] for i in J) >= T(CJ[J]) for J in SUB): continue
            res['instances'] += 1
            adm = [i for i in range(4) if all(sum(t[k] for k in J) - (i in J) >= T(CJ[J]) for J in SUB)]
            if not adm:
                res['no_admissible'] += 1; res['fail'].append((q, t, 'no admissible i')); continue
            ok = False
            for i in adm:
                tau = tuple(t[k] - (k == i) for k in range(4))
                parts = by_target.get(tau, [])
                if not parts: continue            # source instance has no partition (would contradict IH)
                good = True
                for p, j in parts:
                    if j == i: continue
                    newp = [tuple(q + 1 if x == q else x for x in b) for b in p]
                    if not repair(newp, j, i, None): good = False; break
                if good: ok = True; break
            if ok: res['step_ok'] += 1
            else:
                res['fail'].append((q, t, adm))
    res['fail'] = res['fail'][:6]
    return res

if __name__ == '__main__':
    M = int(sys.argv[1]); C = tuple(map(int, sys.argv[2].split(',')))
    print(M, C, run(M, C), flush=True)
