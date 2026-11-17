# Cloud's independent implementation of MI165's parity-bridge family (B72) in the split-anchor model of MI153.
import itertools, collections
def label(j): return min(j, 27 - j)
b = (77, 79, 81, 87, 89, 91); anchors = (21, 23, 25, 31, 33, 35)
assert all(a % 2 == 1 and 56 + a == bb for a, bb in zip(anchors, b))
R = {10, 11, 12}; assert {label((a - 1)//2) for a in anchors} == R
def build(c):
    m = max(c); j = c.index(m); assert m >= 2
    h = [2 if i == j else 1 for i in range(6)] + [2, 2]; assert sum(h) == 11
    rest = [(i, c[i]) for i in range(6) if i != j]
    # grouping into A and B, sums <= 4
    if m >= 5: A = rest; B = []
    elif m == 4:
        k = next(i for i, (idx, v) in enumerate(rest) if v > 0); A = [rest[k]]; B = rest[:k] + rest[k+1:]
    elif m == 3:
        if any(v == 3 for _, v in rest): k = next(i for i, (idx, v) in enumerate(rest) if v == 3)
        else: k = next(i for i, (idx, v) in enumerate(rest) if v == 2)
        A = [rest[k]]; B = rest[:k] + rest[k+1:]
    else:
        ks = [i for i, (idx, v) in enumerate(rest) if v == 2][:2]; assert len(ks) == 2
        A = [rest[k] for k in ks]; B = [r for i, r in enumerate(rest) if i not in ks]
    A = [(i, v) for i, v in A if v > 0]; B = [(i, v) for i, v in B if v > 0]
    s = sum(v for _, v in A); t = sum(v for _, v in B); assert s <= 4 and t <= 4
    x = 8 - 2 * s; D = 28 - 2 * m
    # cycle: list of (bin, position, move)
    cyc = []; p = x
    for i, v in A: cyc.append((i, p, 2 * v)); p += 2 * v
    assert p == 8
    cyc.append((6, p, 5)); p += 5; cyc.append((7, p, 5)); p += 5
    for i, v in B: cyc.append((i, p, 2 * v)); p += 2 * v
    cyc.append((j, p, -D)); assert p - D == x
    pos = [q for _, q, _ in cyc]; labs = [label(q) for q in pos]
    assert all(0 <= q <= 27 for q in pos) and len(set(pos)) == len(pos) and len(set(labs)) == len(labs) and not (set(labs) & R)
    # allocation
    bins = {i: [anchors[i]] for i in range(6)}; bins[6] = []; bins[7] = []
    free = [l for l in range(14) if l not in R and l not in labs]
    for i, q, e in cyc: bins[i] += [2 * q + 1, 2 * (27 - q) + 1]
    for i in range(8):
        need = h[i] - (1 if any(bi == i for bi, _, _ in cyc) else 0)
        for _ in range(need): l = free.pop(); bins[i] += [2 * l + 1, 2 * (27 - l) + 1]
    assert not free
    for i, q, e in cyc: bins[i].remove(2 * q + 1); bins[i].append(2 * (q + e) + 1)
    return bins
targets_seen = set(); n = 0; inE28 = 0; hist = collections.Counter()
for c in itertools.product(range(10), repeat=6):
    if sum(c) != 9: continue
    n += 1; hist[max(c)] += 1
    T = [b[i] + 4 * c[i] for i in range(6)] + [122, 122]
    bins = build(c)
    assert sorted(v for bb in bins.values() for v in bb) == list(range(1, 56, 2))
    assert [sum(bins[i]) for i in range(8)] == T and [len(bins[i]) % 2 for i in range(8)] == [1]*6 + [0, 0]
    if all(x <= 122 for x in T): inE28 += 1; targets_seen.add(tuple(sorted(T)))
print("labelled parameters", n, "all partitions pass; in E28", inE28, "distinct sorted targets", len(targets_seen), "max histogram", dict(sorted(hist.items())))
