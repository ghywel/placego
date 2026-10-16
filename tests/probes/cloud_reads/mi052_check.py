# Independent re-implementation of MI052's repeated-receipt extension of G304 (Cloud carrying read).
import itertools, sys
def construct(h, n, pairs, run, e):
    """pairs: list of (lower, upper) with constant sum S; run: list of upper tokens in consecutive order
    (consecutive odds, differences 2); e: deviations, e_i <= h, sum 0. Returns bins (lists of ints)."""
    S = pairs[0][0] + pairs[0][1]
    assert all(a + b == S for a, b in pairs) and len(pairs) == h * n
    assert all(run[i] - run[i+1] == 2 for i in range(len(run)-1)) and sorted(run) == sorted(p[1] for p in pairs)
    assert all(x <= h for x in e) and sum(e) == 0 and len(e) == n
    pair_of = {u: (l, u) for l, u in pairs}
    pos = [i for i in range(n) if e[i] > 0]; neg = [i for i in range(n) if e[i] < 0]
    # slots: each positive bin i has e_i labelled slots
    slots = [i for i in pos for _ in range(e[i])]
    bins = [[] for _ in range(n)]; used = set(); cursor = 0; chains = []
    for d in neg:
        k = -e[d]
        seg = run[cursor:cursor + k + 1]; cursor += k + 1
        assert len(seg) == k + 1, "chain does not fit in the run"
        mine, slots = slots[:k], slots[k:]
        bins[d].extend(pair_of[seg[0]]); used.add(seg[0])
        for j, b in enumerate(mine):
            bins[b].extend(pair_of[seg[j+1]]); used.add(seg[j+1])
        chains.append((d, seg, mine))
    assert not slots
    assert cursor == sum(-e[d] + 1 for d in neg) <= h * n
    # fill to h pairs each
    free = [p for p in pairs if p[1] not in used]
    for i in range(n):
        while len(bins[i]) < 2 * h:
            bins[i].extend(free.pop())
    assert not free
    # swaps
    for d, seg, mine in chains:
        for j, b in enumerate(mine):
            x, y = seg[j], seg[j+1]
            assert x in bins[d] and y in bins[b]
            bins[d].remove(x); bins[b].remove(y); bins[d].append(y); bins[b].append(x)
    return bins
def check(h, n, pairs, run, e, targets):
    bins = construct(h, n, pairs, run, e)
    allv = sorted(v for b in bins for v in b)
    assert allv == sorted(v for p in pairs for v in p), "coverage"
    assert all(len(b) == 2*h for b in bins)
    assert [sum(b) for b in bins] == list(targets), ([sum(b) for b in bins], targets)
# (1) generic small cases: first 4hn odds, S = 4hn, upper run descending
total = 0
for h in (1, 2, 3):
    for n in range(1, 6):
        S = 4*h*n; pairs = [(x, S - x) for x in range(1, 2*h*n, 2)]; run = sorted((p[1] for p in pairs), reverse=True)
        lo = -h*(n-1)
        for e in itertools.product(range(lo, h+1), repeat=n):
            if sum(e) != 0: continue
            check(h, n, pairs, run, e, [h*S + 2*x for x in e]); total += 1
print("generic (h<=3, n<=5) vectors checked:", total)
# (2) E31 lone-odd-93 slice: pool = odds 3..59, pairs sum 62, upper run 59,57,...,33 (14 tokens), h=2, n=7
pairs = [(x, 62 - x) for x in range(3, 31, 2)]; run = list(range(59, 31, -2))
assert sorted(v for p in pairs for v in p) == [x for x in range(1, 62, 2) if x not in (1, 31, 61)]
cnt = 0; mins = 999
for t in itertools.combinations_with_replacement(range(100, 129, 2), 7):
    if sum(t) != 868: continue
    e = [(x - 124)//2 for x in t]
    check(2, 7, pairs, run, e, t); cnt += 1; mins = min(mins, min(t))
print("E31 lone-93 slice: sorted even 7-tuples <=128, sum 868:", cnt, " smallest target seen:", mins)
# (3) the hand boundary example as written
ex = [[1,31,61],[3,35,29,33],[5,59,7,57],[9,55,11,53],[13,51,15,49],[17,47,19,45],[21,43,23,41],[25,39,27,37]]
assert sorted(v for b in ex for v in b) == list(range(1, 62, 2)) and [sum(b) for b in ex] == [93,100]+[128]*6
print("hand example (93,100,128^6): coverage and sums OK")
# (4) is every E31 tuple with lone odd target 93 of this shape? E31: targets in [?,128], sum 961.
# With 93 fixed, the other seven are even (one odd target only), each <= 128, sum 868: exactly the slice above.
print("E31 tuples with exactly one odd target equal to 93 and all targets <= 128:", cnt)
