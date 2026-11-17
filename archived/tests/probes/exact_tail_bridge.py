#!/usr/bin/env python3
"""L1361 (Local, 2026-11-03): independent check of GC2430's 87-input cone/quantifier bridge. Run:
python3 tests/probes/exact_tail_bridge.py SAMPLES

The A1 reference E at alignment (c0, c1) = (4, 3): initial row ether(x + 4, 3) for x < 0, black at 0, white for x > 0.
GC2430's query: rows G with G(0, x) = E(0, x) for x <= 111, any tail beyond; does G(222, x) = E(222, x) for every
x <= -24? Checks:
  B1 the counts: 87 targets [-110, -24], cone [-332, 198], 444 fixed and 87 free inputs, 68,907 cells and 68,376
     update constraints in the layers x = -332 + t .. 198 - t, every parent in the previous layer;
  B2 the light-cone guard: with x <= 111 fixed, cells x <= -111 at T = 222 agree for every sample;
  B3 the quantifier bridge in its forward direction, sampled: for random free bits 112..198 and random junk at
     199..W (W = 900), the whole-line targets equal the targets of the cone circuit built from [-332, 198] alone;
  B4 the protected control: with 112 fixed back to E (free 113..198) no target differs (the reviewed 112 result);
  B5 the mismatch identity, exhaustively over parents and differences: the code's form
     dl ^ (~r & dc) ^ (~c & dr) ^ (dc & dr) holds, and the report's prose form (masks swapped) fails.
Byproduct, no claim beyond the count: how many random 111-tails (B3's samples) give a target difference.
  B6 detector control: with x <= CUT' fixed for smaller CUT' (0 .. 110), random cone inputs beyond; how many of 300
     samples differ at a target (the detector must see differences when the cut is low).
"""
import random
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
C0, C1, T, Q, CUT = 4, 3, 222, -24, 111


def ether(j, phi):
    return TAB[j % 7][phi % 4]


def rule(l, c, r):
    return l ^ (c | r)


assert all(ether(j, p + 1) == rule(ether(j - 1, p), ether(j, p), ether(j + 1, p)) for j in range(7) for p in range(4))


def E0(x):
    return ether(x + C0, C1) if x < 0 else int(x == 0)


def evolve(lo, cells, steps):
    """Row of bits for x = lo .. lo + len - 1, evolved `steps` ticks on its shrinking valid range: returns (lo', cells')."""
    n = len(cells)
    a = sum(b << i for i, b in enumerate(cells))         # bit i is x = lo + i
    for _ in range(steps):
        a = ((a << 1) ^ (a | (a >> 1))) >> 1              # new bit i (x = lo + 1 + i) reads old bits i, i + 1, i + 2
        n -= 2; lo += 1
        a &= (1 << n) - 1
    return lo, [(a >> i) & 1 for i in range(n)]


def at(lo, row, x):
    return row[x - lo]


# B1: the counts.
lo_t, hi_t = CUT + 1 - T, Q                               # first target cell -110 (cells <= -111 are guarded)
clo, chi = lo_t - T, hi_t + T
cells = sum((chi - t) - (clo + t) + 1 for t in range(T + 1))
b1 = (hi_t - lo_t + 1, clo, chi, CUT - clo + 1, chi - CUT, chi - clo + 1, cells, cells - (chi - clo + 1))
print('B1 targets %d; cone [%d, %d]; fixed %d, free %d, inputs %d; cells %d, update constraints %d' % b1)
assert b1 == (87, -332, 198, 444, 87, 531, 68907, 68376)
assert all((clo + t - 1) >= clo + (t - 1) and (chi - t + 1) <= chi - (t - 1) for t in range(1, T + 1))

# Reference E on a wide row with white beyond (its own tail), and its targets.
W = 900
LO = -W
ref_lo, ref = evolve(LO, [E0(x) for x in range(LO, W + 1)], T)
assert all(at(ref_lo, ref, x) == ether(x + C0, T + C1) for x in range(-110, -37 + 1)), 'E is the ether left of xB'

rng = random.Random(2430)
b2 = b3 = b4 = 0; diffs = 0; first = None
for s in range(N):
    free = [rng.getrandbits(1) for _ in range(CUT + 1, chi + 1)]
    junk = [rng.getrandbits(1) for _ in range(chi + 1, W + 1)]
    row = [E0(x) for x in range(LO, CUT + 1)] + free + junk
    g_lo, g = evolve(LO, row, T)
    b2 += any(at(g_lo, g, x) != at(ref_lo, ref, x) for x in range(-300, lo_t))
    c_lo, c = evolve(clo, row[clo - LO:chi - LO + 1], T)
    assert (c_lo, len(c)) == (lo_t, 87)
    b3 += any(at(g_lo, g, x) != at(c_lo, c, x) for x in range(lo_t, hi_t + 1))
    d = [x for x in range(lo_t, hi_t + 1) if at(c_lo, c, x) != at(ref_lo, ref, x)]
    if d:
        diffs += 1
        first = first or (s, ''.join(map(str, free)), d)
    prot = list(row); prot[CUT + 1 - LO] = E0(CUT + 1)
    p_lo, p = evolve(clo, prot[clo - LO:chi - LO + 1], T)
    b4 += any(at(p_lo, p, x) != at(ref_lo, ref, x) for x in range(lo_t, hi_t + 1))
print('B2 samples with a difference at x <= -111: %d of %d' % (b2, N))
print('B3 samples where the whole line and the cone circuit disagree on a target: %d of %d' % (b3, N))
print('B4 protected samples (112 fixed to E) with a target difference: %d of %d' % (b4, N))
print('byproduct: random 111-tails with a target difference: %d of %d%s' % (
    diffs, N, '' if first is None else '; first: sample %d, free bits 112..198 = %s, differing targets %s' % first))

# B5: the mismatch identity.
code = prose = 0
for l in (0, 1):
    for c in (0, 1):
        for r in (0, 1):
            for dl in (0, 1):
                for dc in (0, 1):
                    for dr in (0, 1):
                        true = rule(l ^ dl, c ^ dc, r ^ dr) ^ rule(l, c, r)
                        code += true == dl ^ ((1 - r) & dc) ^ ((1 - c) & dr) ^ (dc & dr)
                        prose += true == dl ^ ((1 - c) & dc) ^ ((1 - r) & dr) ^ (dc & dr)
print('B5 mismatch identity, 64 cases: code form holds in %d, prose form in %d' % (code, prose))
# B6: the detector sees differences when the cut is low.
for cut in (0, 40, 60, 70, 80, 85, 90, 95, 100, 105, 110):
    hits = 0
    for _ in range(300):
        lo, c = evolve(clo, [E0(x) for x in range(clo, cut + 1)] + [rng.getrandbits(1) for _ in range(cut + 1, chi + 1)], T)
        hits += any(at(lo, c, x) != at(ref_lo, ref, x) for x in range(lo_t, hi_t + 1))
    print('B6 fixed x <= %3d, random cone inputs beyond: %3d of 300 differ at a target' % (cut, hits))
print('EXACT_TAIL_BRIDGE_DONE')
