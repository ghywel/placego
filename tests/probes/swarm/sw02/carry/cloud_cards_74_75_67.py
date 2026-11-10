#!/usr/bin/env python3
"""Cloud CL774/CL775: controls for the hand reads of GPT's cards 74, 75 and the F^2 extension of 67.

Pair words are lists of (u, v): a column and its right neighbour over time.  The inverse column map is
h(u, v)(t) = (u(t+1) xor (u(t) or v(t)), u(t)), one letter shorter.  Letters are written 2u + v.
"""
import random, math


def h(word):
    return [(word[t + 1][0] ^ (word[t][0] | word[t][1]), word[t][0]) for t in range(len(word) - 1)]


def depth_cells(word, upto):
    """Cells at time 0 at depths 1..upto (first output bit of h^d)."""
    out = []; w = word
    for _ in range(upto):
        w = h(w); out.append(w[0][0])
    return out


def card74():
    rng = random.Random(74)
    ok = True; trials = 0
    for _ in range(300):
        n = rng.randrange(6, 40)
        w = [(rng.randrange(2), rng.randrange(2)) for _ in range(n)]
        base = depth_cells(w, n - 1)
        d = rng.randrange(1, n)
        w2 = list(w); w2[d] = (w2[d][0] ^ 1, w2[d][1])
        new = depth_cells(w2, n - 1)
        ok &= new[d - 1] != base[d - 1] and new[:d - 1] == base[:d - 1]      # depth d flips, shallower depths do not
        trials += 1
    print("C1a pivot: flipping u(d) flips the depth-d cell and no shallower one:", ok, "| trials", trials)
    okc = True; rows = []
    for phase in (0, 1):
        for m in (4, 8, 16):
            C = 32; n = 2 * m + C + 1
            w = [((t + phase) % 2, rng.randrange(2)) for t in range(n)]
            orig = list(w)
            for d in range(m, m + C + 1):
                if depth_cells(w, d)[d - 1] == 1:
                    w[d] = (w[d][0] ^ 1, w[d][1])
            cells = depth_cells(w, m + C)
            white = all(c == 0 for c in cells[m - 1:m + C])
            bound = w[:m] == orig[:m] and w[n - m:] == orig[n - m:] and all(a[1] == b[1] for a, b in zip(w, orig))
            changed = sum(1 for a, b in zip(w, orig) if a != b)
            okc &= white and bound
            rows.append((phase, m, n, changed))
    print("C1b construction (phase, m, length, letters changed): depths m..m+32 white, first and last m letters and "
          "every v unchanged:", okc, rows)


def card75():
    src = [0, 2, 1, 2, 0, 2, 1, 2]
    w = [(a >> 1, a & 1) for a in src]
    firsts = []
    for _ in range(5):
        w = h(w); firsts.append(w[0][0])
    img = [2 * u + v for u, v in w]
    print("C2a h^5 of (0,2,1,2,0,2,1,2):", img, "| first output bits on the way:", firsts,
          "| clock u = t mod 2 in the source:", all((a >> 1) == t % 2 for t, a in enumerate(src)))
    okz = all(h([(0, 0)] * (n + 1)) == [(0, 0)] * n for n in range(1, 60))
    L = [(0, 0, 0)]
    pref = {x[:2] for x in L}; suf = {x[-2:] for x in L}; fac = {x[i:i + 3] for x in L for i in range(len(x) - 2)}
    wid = lambda x: len(x) >= 3 and tuple(x[:2]) in pref and tuple(x[-2:]) in suf and \
        all(tuple(x[i:i + 3]) in fac for i in range(len(x) - 2))
    print("C2b h(0^(n+1)) = 0^n with a white output, n < 60:", okz,
          "| length-3 widening of {000} accepts 0^n for 3 <= n <= 60:", all(wid((0,) * n) for n in range(3, 61)),
          "| and rejects 0010:", not wid((0, 0, 1, 0)))


def card67():
    F = lambda n: (n >> 1) ^ (n | (n << 1))
    G = lambda n: F(F(n))
    ok = True; cases = 0
    for m in range(1, 41):
        e = (m & -m).bit_length() - 1; q = m >> e
        o = 1
        if q > 1:
            while pow(2, o, q) != 1:
                o += 1
        k = o * math.ceil((m.bit_length() + 8) / o)
        K = k + 8 * o * q
        S = sum(1 << (k + 8 * o * j) for j in range(q))
        D = (1 << K) * ((1 << K) - 1)
        for r in range(m):
            ok &= S % m == 0 and D % m == 0
            ok &= F(r + S) == F(r) + 7 * S // 2 and 2 * (F(r + S) - F(r)) == 7 * S
            ok &= F(r + D) == F(r) + 3 * (1 << (2 * K - 1)) + (1 << (K - 1))
            ok &= 4 * (G(r + S) - G(r)) == 25 * S
            ok &= G(r + D) == G(r) + 13 * (1 << (2 * K - 2)) + 7 * (1 << (K - 2))
            cases += 1
    print("C3 block formulas for F and G = F^2, every modulus up to 40 and every residue:", ok, "| cases", cases)


if __name__ == "__main__":
    card74(); card75(); card67()
