# Chalkboard check: at m=24 every all-odd town is forced to three planks per street, i.e. eight index triples from {0..23}.
# Does a TRANSVERSAL tiling (one index from each third {0..7},{8..15},{16..23}) always exist? Compare with any tiling.
import itertools, sys, time
sys.path.insert(0, '/home/user/placego/tests/probes/cloud_reads')
from e_slice import solve
def transversal(targets):  # targets: eight index-sums; assign highs 16..23 in all ways? use search: pick triple for each high
    k = len(targets); L = list(range(k)); M = list(range(k, 2*k)); H = list(range(2*k, 3*k))
    tg = sorted(targets)
    # backtracking: for each high h (descending), choose a target slot and an (l,m) pair with l+m = target-h
    usedL = [False]*k; usedM = [False]*k; usedT = [False]*k; sol = []
    def rec(hi):
        if hi == k: return True
        h = H[k-1-hi]
        seen = set()
        for ti in range(k):
            if usedT[ti] or tg[ti] in seen: continue
            seen.add(tg[ti]); need = tg[ti] - h
            for l in L:
                if usedL[l]: continue
                m = need - l
                if m < k or m >= 2*k or usedM[m-k]: continue
                usedT[ti] = usedL[l] = usedM[m-k] = True; sol.append((l, m, h))
                if rec(hi+1): return True
                usedT[ti] = usedL[l] = usedM[m-k] = False; sol.pop()
        return False
    return sol[:] if rec(0) else None
T0 = time.time(); n = any_t = trans = 0; miss = []
for town in itertools.combinations_with_replacement(range(69, 115, 2), 8):
    if sum(town) != 576: continue
    n += 1; idx = [(l-3)//2 for l in town]
    tr = transversal(idx)
    if tr: trans += 1
    else:
        bins, dt, nodes = solve(24, list(town), cap=30)
        if bins: any_t += 1; miss.append(town)
        elif bins is None: miss.append(('unknown', town))
        else: miss.append(('IMPOSSIBLE', town))
print(f"all-odd towns at m=24: {n}; with a transversal tiling {trans}; tiled only non-transversally {any_t}; others {[x for x in miss if isinstance(x[0], str)][:5]}; first non-transversal {miss[:4]} ({time.time()-T0:.0f}s)")
