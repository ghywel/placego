# Cloud's independent check of every row of the replayed B124 stream: targets sorted odd 69..121 sum 784; 28 tokens are
# exactly the odds 1..55; bin sizes 7,3,3,3,3,3,3,3; bin sums equal targets in order; first bin equals C(a).
# Also: the set of target rows equals my own enumeration of the domain, with no duplicates.
import sys
ODDS = set(range(1, 56, 2))
def C(a): return {1, 3, 5, 7, 9, 11, a - 36} if a <= 91 else {1, 3, 5, 7, 9, a - 80, 55}
seen = set(); rows = 0
with open(sys.argv[1]) as f:
    for line in f:
        if line.startswith('#'): continue
        v = list(map(int, line.split())); assert len(v) == 36, len(v)
        t, tok = v[:8], v[8:]
        assert t == sorted(t) and all(69 <= x <= 121 and x % 2 for x in t) and sum(t) == 784
        assert set(tok) == ODDS and len(set(tok)) == 28
        bins = [tok[:7]] + [tok[7 + 3*i: 10 + 3*i] for i in range(7)]
        assert [sum(b) for b in bins] == t and set(bins[0]) == C(t[0])
        assert tuple(t) not in seen; seen.add(tuple(t)); rows += 1
def domain():
    out = set()
    def rec(prefix, prev, rem, k):
        if k == 0:
            if rem == 0: out.add(tuple(prefix))
            return
        for x in range(prev, 122, 2):
            if k * x > rem: break
            if rem - x > 121 * (k - 1): continue
            rec(prefix + [x], x, rem - x, k - 1)
    rec([], 69, 784, 8); return out
D = domain()
print("rows", rows, "all pass; distinct targets", len(seen), "; my domain", len(D), "; equal:", seen == D)
