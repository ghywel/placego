# Chalkboard, part two. (a) PAIR-SUM LEMMA: a multiset d_1<=...<=d_k of pair sums is realizable as {l + sigma(l)} for a
# bijection sigma: {0..k-1} -> {k..2k-1} iff sum d = k(2k-1) and every j smallest d's sum to at least the j smallest possible
# pair sums (L(j) + jk + L(j)) and every j largest to at most the j largest possible. Exhaustive for k <= 8.
# (b) SORTED-H RULE for eight triples from {0..23}: give the largest highs to the largest targets, then solve the pair sums;
# tested on all 70 all-odd 24-day towns and on random cut-satisfying target vectors.
import itertools, sys, random, time
sys.path.insert(0, '/home/user/placego/tests/probes/cloud_reads')
def L(j): return j*(j-1)//2
def realizable(d, k):  # exact search for a bijection
    d = sorted(d); used = [False]*k
    def rec(l):
        if l == k: return True
        for m in range(k):
            if not used[m] and (l + k + m) in rem: 
                rem.remove(l + k + m); used[m] = True
                if rec(l+1): return True
                rem.append(l + k + m); used[m] = False
        return False
    rem = list(d); return rec(0)
def cuts_ok(d, k):
    d = sorted(d); n = len(d)
    if sum(d) != k*(2*k-1): return False
    for j in range(1, k):
        if sum(d[:j]) < L(j) + j*k + L(j): return False
        if sum(d[-j:]) > sum(range(k-j, k)) + sum(range(2*k-j, 2*k)): return False
    return True
T0 = time.time()
for k in range(2, 9):
    tot = bad = 0
    for d in itertools.combinations_with_replacement(range(k, 3*k-1), k):
        if not cuts_ok(d, k): continue
        tot += 1
        if not realizable(list(d), k): bad += 1; print("PAIRSUM FAIL", k, d) if bad <= 3 else None
    print(f"pair-sum lemma k={k}: cut-admitted multisets {tot}, not realizable {bad} ({time.time()-T0:.0f}s)", flush=True)
# (b) sorted-h rule on triples
def sorted_h(targets, k=8):
    tg = sorted(targets); H = list(range(2*k, 3*k))  # largest target gets largest high
    d = [tg[i] - H[i] for i in range(k)]
    return all(k <= x <= 3*k-2 for x in d) and cuts_ok(d, k) and realizable(d, k)
n = ok = 0
for town in itertools.combinations_with_replacement(range(69, 115, 2), 8):
    if sum(town) != 576: continue
    n += 1; ok += sorted_h([(l-3)//2 for l in town])
print(f"sorted-h rule on the 70 all-odd m=24 towns: {ok}/{n}")
# random cut-satisfying eight-triple targets on {0..23}
def triple_cuts(t, k=8, n=24):
    s = sorted(t)
    if sum(s) != n*(n-1)//2: return False
    for j in range(1, k):
        if sum(s[:j]) < sum(range(3*j)) or sum(s[-j:]) > sum(range(n-3*j, n)): return False
    return True
random.seed(1); tried = succ = 0; fails = []
while tried < 4000:
    t = [random.randint(3, 66) for _ in range(7)]; t.append(276 - sum(t))
    if min(t) < 3 or max(t) > 66 or not triple_cuts(t): continue
    tried += 1
    if sorted_h(t): succ += 1
    elif len(fails) < 5: fails.append(sorted(t))
print(f"sorted-h rule on {tried} random cut-admitted eight-triple targets: {succ} succeed; failures e.g. {fails}")
