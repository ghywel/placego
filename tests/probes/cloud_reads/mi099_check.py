import itertools, collections
from e28lib import *
# gap graph on labels 0..13
def gap_graph(g):
    E = set()
    for p in range(28):
        q = p + g
        if q <= 27 and label(p) != label(q): E.add(frozenset((label(p), label(q))))
    F = {frozenset((i, j)) for i in range(14) for j in range(14) if i < j and (j - i == g or i + j == 27 - g)}
    assert E == F, g
    return E
def max_matching(E):
    best = 0
    El = list(E)
    def rec(i, used, k):
        nonlocal best
        best = max(best, k)
        for t in range(i, len(El)):
            e = El[t]
            if not (e & used): rec(t + 1, used | e, k + 1)
    rec(0, frozenset(), 0); return best
def five_covers(E):
    return [set(c) for c in itertools.combinations(range(14), 5) if all(e & set(c) for e in E)]
roots = {6: range(7), 7: range(7), 8: range(7), 12: range(7), 13: range(7), 14: range(7), 9: range(1, 8), 10: range(7), 11: (0,1,2,3,4,5,8)}
for g in range(6, 15):
    E = gap_graph(g); C = five_covers(E); m = max_matching(E)
    print(f"g={g}: max matching {m}, five-covers {len(C)}", [sorted(c) for c in C] if C else "")
    for r in roots[g]:
        assert all(label(r) not in c for c in C), (g, r)
# domain and construction
targets = set(); inst = 0; rootuse = collections.Counter()
for h in range(6, 23):
    for g in range(6, 15):
        for a, b, c in itertools.combinations_with_replacement(range(1, 6), 3):
            q = a + b + c; H = h + q
            if H > 22 or max(h, g) + max(H, g) > 28: continue
            inst += 1
            E = gap_graph(g)
            core = [0, h, h + a, h + a + b, H]  # (+h,+a,+b,+c,-H)
            ok = None
            for r in roots[g]:
                P = [p + r for p in core]
                if max(P) > 27: continue
                labs = [label(p) for p in P]
                if len(set(labs)) < 5: continue
                spare = [e for e in E if not (e & set(labs))]
                if not spare: continue
                i, j = sorted(spare[0])
                xs = [x for x in range(28 - g) if {label(x), label(x + g)} == {i, j}]
                ok = (r, xs[0]); break
            assert ok is not None, (h, g, a, b, c)
            r, x = ok; rootuse[r] += 1
            P = [p + r for p in core]
            cyc1 = [(0, P[0]), (2, P[1]), (3, P[2]), (4, P[3]), (5, P[4])]   # bins: 0=+h small, 2,3,4 = +a,+b,+c, 5 = -H
            cyc2 = [(1, x), (6, x + g)]                                       # 1 = +g small, 6 = -g
            t = realize([cyc1, cyc2], {0: h, 1: g}, {2: a, 3: b, 4: c, 5: -H, 6: -g, 7: 0})
            targets.add(t)
print("instances", inst, "distinct targets", len(targets), "roots used", dict(sorted(rootuse.items())))
# independent domain: even E28, two smallest = small bins u,v>=6; among six large exactly 3 positive (<=5), 1 zero, 2 negative,
# and a negative magnitude equals u or v
dom = set()
for t in even_e28():
    u, v = (t[0] - 56)//2, (t[1] - 56)//2
    e = [(x - 112)//2 for x in t[2:]]
    if u < 6 or v < 6: continue
    if sum(1 for x in e if x > 0) != 3 or sum(1 for x in e if x == 0) != 1 or sum(1 for x in e if x < 0) != 2: continue
    if max(e) > 5: continue
    if any(-x in (u, v) for x in e if x < 0): dom.add(t)
print("independent matching domain", len(dom), "equal:", dom == targets)
# counterfactual control: h=10, g=9, a=b=c=1, root 0: valid core but every gap-9 edge covered
E = gap_graph(9); P = [0, 10, 11, 12, 13]; labs = {label(p) for p in P}
print("control h10 g9 (1,1,1) root0: labels", sorted(labs), "spare edges:", [sorted(e) for e in E if not (e & labs)])
