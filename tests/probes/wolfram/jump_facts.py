"""jump_facts.py: the one-step facts after a heal of the error edge, by exhaustive enumeration (CL741, CL744; saved as a
replayable source after GC2683). Wall frame: bit j at t+1 reads bits j-2, j-1, j at t. Two configurations a and C agree
below the edge m, differ at m (e_m = 1); at a heal (C_(m-1) = 1, so a_(m-1) = 1 too) the new edge m' = m + d is the
lowest wheel with a != C at t+1. Enumerated over every bit that enters: the strip C at m-L..m+R, the errors e at
m+1..m+W, and fair coins for every other bit in the computation (so the enumeration is exhaustive, whatever the split).
Facts: (1) after a jump of 2 the new parent C_(m'-1)(t+1) is white; (2) after a jump of 3 it is black; (3) after a jump
of 4 or 5 whose new parent is white, the parent at t+2 is black; (4) after a jump of 6 whose new parent is white, the
parent at t+2 is white. Jumps 1 and 7+ are unconstrained. Usage: python3 jump_facts.py"""
import itertools, collections
def enumerate_facts(L, R, W, E):
    lo, hi = -L - 2, R + E
    parent1 = collections.defaultdict(set); parent2 = collections.defaultdict(set); counts = collections.Counter()
    nstate = L + 1 + R + W; ncoin = 2 + E + (R + E - W)
    for s in range(1 << nstate):
        Cs = [(s >> i) & 1 for i in range(L + 1 + R)]; es = [(s >> (L + 1 + R + i)) & 1 for i in range(W)]
        if Cs[L - 1] != 1: continue                       # a heal needs the parent black
        for coins in itertools.product((0, 1), repeat=ncoin):
            k = 0; C = {}; e = {}
            for p in range(lo, hi + 1):
                if -L <= p <= R: C[p] = Cs[p + L]
                else: C[p] = coins[k]; k += 1
            for p in range(lo, hi + 1):
                if p < 0: e[p] = 0
                elif p == 0: e[p] = 1
                elif p <= W: e[p] = es[p - 1]
                else: e[p] = coins[k]; k += 1
            a = {p: C[p] ^ e[p] for p in C}
            C2 = {p: C[p - 2] ^ (C[p - 1] | C[p]) for p in range(lo + 2, hi + 1)}
            a2 = {p: a[p - 2] ^ (a[p - 1] | a[p]) for p in range(lo + 2, hi + 1)}
            e2 = {p: C2[p] ^ a2[p] for p in C2}
            d = next((p for p in range(0, hi + 1) if e2[p]), None)
            if d is None or d > R + E: continue           # the jump must be resolved inside the computed window (its parents lie below it)
            counts[d] += 1; parent1[d].add(C2[d - 1])
            if C2[d - 1] == 0: parent2[d].add(C2[d - 3] ^ (C2[d - 2] | C2[d - 1]))   # the parent at t+2 after a stay at t+1
    return counts, parent1, parent2
counts, p1, p2 = enumerate_facts(L=3, R=4, W=3, E=4)
print("cases by jump d (resolved inside the window):", dict(sorted(counts.items())))
print("new parent's possible values at t+1 by jump:", {d: sorted(v) for d, v in sorted(p1.items())})
print("parent at t+2 after a white new parent, by jump:", {d: sorted(v) for d, v in sorted(p2.items())})
ok = p1[2] == {0} and p1[3] == {1} and p2[4] == {1} and p2[5] == {1} and p2[6] == {0}
print("facts (1)-(4):", "ALL HOLD" if ok else "FAIL")
