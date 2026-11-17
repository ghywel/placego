import json, sys, collections, random
sys.path.insert(0, '.')
from e28lib import even_e28
d = json.load(open(sys.argv[1]))
EV = even_e28()
def e28(t):
    e = [x - 68 for x in t]; return list(t) == sorted(t) and all(0 <= x <= 54 for x in e) and sum(e) == 240
def check_bins(bins, targets):
    assert sorted(len(b) for b in bins) == [2,2,4,4,4,4,4,4]
    assert sorted(v for b in bins for v in b) == list(range(1, 56, 2))
    assert sorted(sum(b) for b in bins) == sorted(targets)
g0, g1 = d['groups']
ranks = set(); strata = collections.Counter()
for r in g0['rows']:
    assert r['status'] == 'WITNESS'; t = tuple(r['targets']); assert t in EV, t
    check_bins(r['bins'], t); ranks.add(r['rank'])
    strata[sum(1 for x in t[2:] if x < 112)] += 1
print("even group: rows", len(g0['rows']), "distinct ranks", len(ranks), "all witnesses checked; strata by negatives", dict(sorted(strata.items())))
w = o = 0; ranks = set()
for r in g1['rows']:
    t = tuple(r['targets']); assert e28(t), t; ranks.add(r['rank'])
    if r['status'] == 'WITNESS':
        assert all(x % 2 == 0 for x in t) and t in EV; w += 1
        if 'bins' in r: check_bins(r['bins'], t)
    else:
        assert any(x % 2 for x in t); o += 1
print("all group: witnesses", w, "outside class", o, "distinct ranks", len(ranks), "witness rows carry bins:", 'bins' in g1['rows'][0] or any('bins' in r for r in g1['rows']))
# uniformity plausibility: exact negative-count distribution over the whole even domain vs the sample
full = collections.Counter(sum(1 for x in t[2:] if x < 112) for t in EV)
print("expected counts in a uniform 2,000-sample by negatives:", {k: round(2000 * v / len(EV), 1) for k, v in sorted(full.items())})
chi = sum((strata[k] - 2000 * full[k] / len(EV)) ** 2 / (2000 * full[k] / len(EV)) for k in full)
print("chi-square vs uniform (5 df):", round(chi, 2))
