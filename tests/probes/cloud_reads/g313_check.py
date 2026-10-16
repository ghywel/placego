# Cloud's independent implementation of MI141's four-gap construction (G313), plus checks of GPT's B60 file.
import json, sys, itertools, collections
def label(j): return min(j, 27 - j)
def ok(pairs, gaps):
    assert sorted(b - a for a, b in pairs) == sorted(gaps), (pairs, gaps)
    pts = [p for pr in pairs for p in pr]
    assert all(0 <= p <= 27 for p in pts) and len(set(label(p) for p in pts)) == 8, (pairs, gaps)
def path_matching(N, g, forbidden=()):
    """fixed alternating matching of the gap-g graph on 0..N-1 (edges x,x+g), with vertices in forbidden deleted."""
    M = []
    for a in range(g):
        cls = [x for x in range(a, N, g)]
        # alternating edges along the residue path
        for i in range(0, len(cls) - 1, 2): M.append((cls[i], cls[i+1]))
    return [e for e in M if e[0] not in forbidden and e[1] not in forbidden]
def construct(gaps):
    gaps = sorted(gaps); large = [g for g in gaps if g >= 8]; small = [g for g in gaps if g <= 7]
    ell = len(large); pairs = []; holes = []
    for i, d in enumerate(large, 1):
        R = 13 - ell + i; L = 27 - R - d
        pairs.append((L, 27 - R)); holes.append(L)
    assert len(set(holes)) == ell and all(0 <= h <= 5 + ell for h in holes)
    N = 14 - ell  # literal interval 0..13-ell
    used = set(holes)
    if ell == 0:
        for g in small:
            x = min(v for v in range(14) if v not in used)
            assert x + g <= 13 and x + g not in used
            pairs.append((x, x + g)); used |= {x, x + g}
    elif ell == 4:
        pass
    elif ell in (2, 3) or (ell == 1 and any(g not in (4, 5) for g in small)):
        order = list(small)
        if ell == 2 and 4 in order: order.sort(key=lambda g: (g != 4, g))        # gap 4 first
        if ell == 1: order.sort(key=lambda g: (g not in (4, 5), g))              # a non-4/5 gap last
        for g in order:
            M = [e for e in path_matching(N, g, used)]
            assert M, (gaps, g, used)
            e = M[0]; pairs.append(e); used |= set(e)
    else:  # ell == 1, all small gaps in {4,5}: compact shape translated to avoid the hole
        g1, g2, g3 = small; shape = [(0, g1), (1, 1 + g2), (2, 2 + g3)]
        D = max(b for a, b in shape); h = holes[0]; done = False
        for t in range(0, 13 - D):
            pts = [p + t for pr in shape for p in pr]
            if h not in pts:
                pairs += [(a + t, b + t) for a, b in shape]; done = True; break
        assert done, gaps
    return pairs
# (1) my construction over all 2,380 multisets
allg = list(itertools.combinations_with_replacement(range(1, 15), 4)); cnt = collections.Counter()
for gaps in allg:
    ok(construct(gaps), gaps); cnt[sum(1 for g in gaps if g >= 8)] += 1
print("my construction: all", len(allg), "multisets placed; by large count", dict(cnt))
# (2) capacity table by brute-force maximum matching on the literal gap graph of 0..N-1
def maxmatch(N, g):
    E = [(x, x + g) for x in range(N - g)]; best = 0
    def rec(i, used, k):
        nonlocal best; best = max(best, k)
        for t in range(i, len(E)):
            if E[t][0] not in used and E[t][1] not in used: rec(t + 1, used | set(E[t]), k + 1)
    rec(0, set(), 0); return best
tab = {(N, g): maxmatch(N, g) for N in (11, 12, 13) for g in range(1, 8)}
fixed = {(N, g): len(path_matching(N, g)) for N in (11, 12, 13) for g in range(1, 8)}
print("capacity table (max matching == fixed alternating matching):", all(tab[k] == fixed[k] for k in tab), [tab[(N, g)] for N in (11, 12, 13) for g in range(1, 8)])
# (3) GPT's file: primary pairs and corollaries
d = json.load(open(sys.argv[1]))
assert len(d['results']) == 2380
for r in d['results']: ok([tuple(p) for p in r['primary']], r['gaps'])
for c in d['corollary_certificates']:
    bins = c['bins']; t = c['targets']
    assert sorted(len(b) for b in bins) == [2,2,4,4,4,4,4,4] and sorted(v for b in bins for v in b) == list(range(1, 56, 2))
    assert sorted(sum(b) for b in bins) == sorted(t) and t == sorted(t) and all(x % 2 == 0 and 68 <= x <= 122 for x in t) and sum(t) == 784
print("GPT file: 2,380 primary placements and", len(d['corollary_certificates']), "corollary partitions pass my checks; table matches:", [c[2] for c in d['controls']['capacity_table']] == [tab[(N, g)] for N in (11, 12, 13) for g in range(1, 8)] or 'order differs')
# (4) hand-lemma spot checks: ell=1 compact shapes
for g1, g2, g3 in itertools.combinations_with_replacement((4, 5), 3):
    pts = sorted({0, g1, 1, 1 + g2, 2, 2 + g3}); print("compact", (g1, g2, g3), "vertices", pts, "span", max(pts), "3 absent:", 3 not in pts)
