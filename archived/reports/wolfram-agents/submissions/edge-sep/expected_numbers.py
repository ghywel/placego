#!/usr/bin/env python3
"""Expected outputs of the essay's Wolfram Language cells for the fixed-edge submission (python3 -I expected_numbers.py).
Independent of the Lean module: a plain scalar rule 30 on dictionaries, no lanes."""
import itertools

def step(cells):  # cells: dict pos -> 1 for black; zero background
    out = {}
    lo, hi = min(cells), max(cells)
    for p in range(lo - 1, hi + 2):
        l, c, r = cells.get(p - 1, 0), cells.get(p, 0), cells.get(p + 1, 0)
        v = l ^ (c | r)
        if v: out[p] = 1
    return out or {0: 0}

def center_trace(cells, T):
    out = []
    for _ in range(T):
        out.append(cells.get(0, 0)); cells = step(cells)
    return out

def box_max(a, b, R, H):
    """Longest common center prefix over rows x with edge a, y with edge b, both supported in [., R]."""
    def rows(e):
        res = []
        for bits in itertools.product((0, 1), repeat=R - e):
            cells = {e: 1}; cells.update({e + 1 + i: bits[i] for i in range(R - e) if bits[i]})
            res.append(tuple(center_trace(cells, H)))
        return sorted(set(res))
    A = rows(a); B = rows(b)
    import bisect
    best = 0
    for tb in B:
        i = bisect.bisect_left(A, tb)
        for j in (i - 1, i):
            if 0 <= j < len(A):
                l = 0
                while l < H and A[j][l] == tb[l]: l += 1
                best = max(best, l)
    return best

def lane_code(bits):  # bits over positions a, a+1, ...; the kit-side lane number is (code - 1) / 2
    n = sum(b << i for i, b in enumerate(bits)); assert n % 2 == 1
    return n, (n - 1) // 2

if __name__ == "__main__":
    # 1. saturation at R = m for the three pairs (the box maximum equals the exact deadline)
    print("box maxima at R = m:", {(-2, -1): box_max(-2, -1, 8, 40), (-4, -3): box_max(-4, -3, 13, 40), (-3, -2): box_max(-3, -2, 14, 40)})
    # 2. the attaining pairs (E2/E2b witnesses, trailing white dropped) and their lane numbers
    W = {(-2, -1): ("100110100", "10010001"), (-4, -3): ("11101101", "1101001001"), (-3, -2): ("10001", "1100001")}
    for (a, b), (wa, wb) in W.items():
        ba = [int(c) for c in wa]; bb = [int(c) for c in wb]
        na, la = lane_code(ba); nb, lb = lane_code(bb)
        xa = {a + i: 1 for i, v in enumerate(ba) if v}; xb = {b + i: 1 for i, v in enumerate(bb) if v}
        m = {(-2, -1): 8, (-4, -3): 13, (-3, -2): 14}[(a, b)]
        ta = center_trace(xa, m + 1); tb = center_trace(xb, m + 1)
        first = next(t for t in range(m + 1) if ta[t] != tb[t])
        print(f"edges {a},{b}: codes {na},{nb} lanes {la},{lb}; first disagreement {first} (expected {m}); traces {''.join(map(str,ta))} {''.join(map(str,tb))}")
    # 3. saturation shown in the essay for (-2,-1): box maxima at R = 6, 8, 10
    print("(-2,-1) box maxima at R = 6, 8, 10:", [box_max(-2, -1, R, 40) for R in (6, 8, 10)])
