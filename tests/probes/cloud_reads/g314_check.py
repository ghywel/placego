# Independent check of G314's statement: every primitive six-move zero-sum core with two positive moves (a>=c>=1) and four
# negative magnitudes (b1>=..>=b4>=1), a+c = sum b, a+b1 <= 28, places jointly with every cancelling gap g in 1..14:
# some cyclic order, root and physical pair give eight distinct folded labels. Also checks the B62 span classification.
import itertools, collections
def label(j): return min(j, 27 - j)
def primitive(moves):
    n = len(moves)
    for r in range(1, n):
        for sub in itertools.combinations(range(n), r):
            if sum(moves[i] for i in sub) == 0: return False
    return True
cores = []
for a in range(1, 28):
    for c in range(1, a + 1):
        P = a + c
        for b in itertools.combinations_with_replacement(range(1, 28 - a + 1), 4):
            if sum(b) == P: cores.append((a, c, tuple(sorted(b, reverse=True))))
prim = [k for k in cores if primitive((k[0], k[1]) + tuple(-x for x in k[2]))]
print("arithmetic tuples", len(cores), "primitive", len(prim))
def shapes(moves):
    """all cyclic orders starting with +a: partial-sum vertex sets (as sorted tuples normalized to min 0)."""
    a = moves[0]; rest = moves[1:]; out = {}
    for perm in set(itertools.permutations(rest)):
        pts = [0]; s = 0
        for m in (a,) + perm: s += m; pts.append(s)
        pts = pts[:-1]  # closing returns to 0
        if len(set(pts)) < 6: continue
        mn = min(pts); sh = tuple(sorted(p - mn for p in pts)); out[sh] = (a,) + perm
    return out
gapedges = {g: [(x, x + g) for x in range(28 - g)] for g in range(1, 15)}
exc = []; fail = []; spanmin = {}
for (a, c, b) in prim:
    moves = (a, c) + tuple(-x for x in b)
    sh = shapes(moves); spanmin[(a, c, b)] = min(s[-1] for s in sh)
    for g in range(1, 15):
        found = False
        for s in sh:
            span = s[-1]
            for r in range(0, 28 - span):
                P = [p + r for p in s]; labs = {label(p) for p in P}
                if len(labs) < 6: continue
                for x, y in gapedges[g]:
                    if label(x) != label(y) and label(x) not in labs and label(y) not in labs: found = True; break
                if found: break
            if found: break
        if not found: fail.append((a, c, b, g))
print("joint placement failures over", len(prim) * 14, "questions:", len(fail))
wide = [k for k, v in spanmin.items() if v > 20]
print("primitive cores with minimum span > 20:", len(wide), " with a>=21:", sum(1 for k in wide if k[0] >= 21), " others:", [k for k in wide if k[0] < 21])
print("minimum span values among them:", collections.Counter(spanmin[k] for k in wide))
# B62 identity: min span == max(a, min over subsets B of negatives of max(B, P-B))
bad = 0
for (a, c, b) in prim:
    P = a + c; best = min(max(sum(S), P - sum(S)) for r in range(0, 5) for S in itertools.combinations(b, r))
    if spanmin[(a, c, b)] != max(a, best): bad += 1
print("span identity mismatches:", bad)
