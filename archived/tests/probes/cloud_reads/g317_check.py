# Statement check of G317: R = [0,V] \ {1, v}, three sizes >= 4 summing to V-1, targets summing to sum(R), each target
# individually realizable by a subset of R of its size => joint partition exists. Plus MI350's two negatives.
import itertools, sys, time
sys.path.insert(0, '.')
import itertools as _it
def spectrum(P, r): return {sum(c) for c in _it.combinations(P, r)}
def exists3(P, sizes, targets):
    P = sorted(P); rem_c = list(sizes); rem_s = list(targets)
    def rec(i):
        if i == len(P): return all(x == 0 for x in rem_c)
        x = P[i]; tried = set()
        for b in range(3):
            key = (rem_c[b], rem_s[b])
            if rem_c[b] == 0 or rem_s[b] < x or key in tried: continue
            tried.add(key); rem_c[b] -= 1; rem_s[b] -= x
            if rec(i+1): return True
            rem_c[b] += 1; rem_s[b] += x
        return False
    return rec(0)
t0 = time.time(); tot = fails = 0
for V in range(13, 15):
    for v in range(2, V + 1):
        R = [x for x in range(V + 1) if x not in (1, v)]; S = sum(R)
        for sizes in itertools.combinations_with_replacement(range(4, V), 3):
            if sum(sizes) != V - 1: continue
            sp = {k: spectrum(R, k) for k in set(sizes)}
            for sa in sp[sizes[0]]:
                for sb in sp[sizes[1]]:
                    sc = S - sa - sb
                    if sc not in sp[sizes[2]]: continue
                    if sizes[0] == sizes[1] and sa > sb: continue
                    if sizes[1] == sizes[2] and sb > sc: continue
                    tot += 1
                    if not exists3(R, list(sizes), [sa, sb, sc]): fails += 1; print("FAIL", V, v, sizes, (sa, sb, sc))
    print(f"V={V}: cumulative individually-feasible instances {tot}, failures {fails} ({time.time()-t0:.0f}s)", flush=True)
# MI350 negatives
R1 = [x for x in range(11) if x not in (1, 4)]; print("MI350 special pool (12,12,26):", exists3(R1, [3,3,3], [12,12,26]))
P = [x for x in range(13) if x != 6]
def exists4(P, sizes, targets):
    P = sorted(P); rc = list(sizes); rs = list(targets)
    def rec(i):
        if i == len(P): return all(x == 0 for x in rc)
        x = P[i]; tried = set()
        for b in range(4):
            key = (rc[b], rs[b])
            if rc[b] == 0 or rs[b] < x or key in tried: continue
            tried.add(key); rc[b] -= 1; rs[b] -= x
            if rec(i+1): return True
            rc[b] += 1; rs[b] += x
        return False
    return rec(0)
print("MI350 one-hole four-bin (4,18,18,32):", exists4(P, [3,3,3,3], [4,18,18,32]), "; repaired (4,17,19,32):", exists4(P, [3,3,3,3], [4,17,19,32]))
