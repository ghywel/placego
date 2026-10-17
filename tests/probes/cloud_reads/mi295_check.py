# Independent check of MI295's strong claim: three bins, sizes >= 2, SS-feasible targets; from ANY labelled partition with
# the right sizes and error E > 0, at most FOUR adjacent-value swaps (exchange tokens x and x+1 between their owners)
# reduce E by >= 2 with no intermediate increase. Exhaustive on n <= 9.
import itertools, sys, collections
sys.path.insert(0, '.')
from sizes_sums import lo, hi
from ss3_bigger import SS
def err(word, targets, k):
    sums = [0]*k
    for x, b in enumerate(word): sums[b] += x
    return sum(abs(sums[j] - targets[j]) for j in range(k)), sums
def ok_descent(word, targets, k, maxd=4):
    E0, _ = err(word, targets, k)
    frontier = {tuple(word)}
    for depth in range(1, maxd + 1):
        nxt = set()
        for w in frontier:
            for x in range(len(w) - 1):
                if w[x] == w[x+1]: continue
                w2 = list(w); w2[x], w2[x+1] = w2[x+1], w2[x]; w2 = tuple(w2)
                E, _ = err(w2, targets, k)
                if E <= E0 - 2: return depth
                if E == E0: nxt.add(w2)
        frontier = nxt
        if not frontier: return None
    return None
worst = collections.Counter(); total = 0; fails = []
for n in range(6, 10):
    T = n*(n-1)//2
    for sizes in itertools.combinations_with_replacement(range(2, n), 3):
        if sum(sizes) != n: continue
        for targets in itertools.product(*[range(lo(c), hi(c, n) + 1) for c in sizes]):
            if sum(targets) != T or not SS(n, sizes, targets): continue
            # all labelled partitions with these sizes: words over {0,1,2} with prescribed counts
            for word in set(itertools.permutations([0]*sizes[0] + [1]*sizes[1] + [2]*sizes[2])):
                E0, _ = err(word, targets, 3)
                if E0 == 0: continue
                total += 1
                d = ok_descent(word, targets, 3)
                if d is None: fails.append((n, sizes, targets, word))
                else: worst[d] += 1
    print(f"n={n}: cumulative start states {total}, failures {len(fails)}, depth histogram {dict(sorted(worst.items()))}", flush=True)
print("failures:", fails[:5])
