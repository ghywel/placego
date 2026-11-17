# E28 cycle model, Cloud's own implementation: odds 1..55 at indices 0..27 (odd 2j+1), pairs {j,27-j} sum 56,
# label(j)=min(j,27-j). Two 1-pair bins (targets 56+2e), six 2-pair bins (112+2e). Active bins hold one
# selected pair; the selected token at index p moves to index p+e (the next bin's selected index).
def label(j): return min(j, 27 - j)
def realize(cycles, small_devs, large_devs):
    """cycles: list of lists of (bin_id, position); bins 0,1 small, 2..7 large. devs: dict bin->e.
    Returns bins as lists of odd values, after whole-pair allocation and selected-token permutation."""
    devs = {**small_devs, **large_devs}
    sel = {}
    for cyc in cycles:
        L = len(cyc)
        for i, (b, p) in enumerate(cyc):
            assert 0 <= p <= 27, (b, p)
            assert p + devs[b] == cyc[(i+1) % L][1], ("edge", b, p, devs[b], cyc[(i+1) % L])
            assert b not in sel; sel[b] = p
    labs = [label(p) for p in sel.values()]
    assert len(set(labs)) == len(labs), ("pair label clash", sel)
    usedpairs = set(labs)
    bins = {b: [] for b in range(8)}
    for b, p in sel.items(): bins[b] = [2*p + 1, 2*(27 - p) + 1]
    free = [j for j in range(14) if j not in usedpairs]
    for b in range(8):
        need = (1 if b < 2 else 2) - len(bins[b]) // 2
        for _ in range(need):
            j = free.pop(); bins[b] += [2*j + 1, 2*(27 - j) + 1]
    assert not free
    # permute selected tokens
    for b, p in sel.items():
        q = p + devs[b]
        bins[b].remove(2*p + 1); bins[b].append(2*q + 1)
    for b in range(8):
        assert b in sel or devs.get(b, 0) == 0
    vals = sorted(v for b in bins.values() for v in b)
    assert vals == list(range(1, 56, 2)), "coverage"
    sums = {b: sum(v) for b, v in bins.items()}
    for b in range(8):
        assert sums[b] == (56 if b < 2 else 112) + 2*devs.get(b, 0), (b, sums[b], devs.get(b, 0))
    return tuple(sorted(sums.values()))
def even_e28():
    out = []
    def rec(i, prev, rem, s):
        if i == 8:
            if rem == 0: out.append(tuple(68 + 2*x for x in s))
            return
        for v in range(prev, min(27, rem) + 1):
            if rem - v > 27*(7 - i): continue
            rec(i + 1, v, rem - v, s + [v])
    rec(0, 0, 120, []); return set(out)
