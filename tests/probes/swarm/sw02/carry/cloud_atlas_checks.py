# Own-code checks for the atlas-only batch of SW-02's carry debt (Cloud, CL766). Exact, exhaustive where stated.
import sys, itertools
forb = {5: open(sys.argv[1]).read().split(), 6: open(sys.argv[2]).read().split()}
print("== 1. BR-5.2: the strip's eventual image at widths 5 and 6, and the kit's forbidden column-1 words")
def tick(x, c, w):            # cells 1..w in bits 0..w-1, centre c; valid result bits 0..w-2
    return (((x << 1) | c) ^ (x | (x >> 1))) & ((1 << w) - 1)
def step2(x, e1, e2, b):      # white tick -> next white tick; column b+1 takes e1 then e2
    y = tick(x | (e1 << b), 0, b + 1) & ((1 << b) - 1)
    return tick(y | (e2 << b), 1, b + 1) & ((1 << b) - 1)
for b in (5, 6):
    succ = {x: {step2(x, e1, e2, b) for e1 in (0, 1) for e2 in (0, 1)} for x in range(1 << b)}
    cur = set(range(1 << b)); sizes = [len(cur)]
    while True:
        nxt = set().union(*(succ[x] for x in cur))
        if nxt == cur: break
        cur = nxt; sizes.append(len(cur))
    lim = cur
    # strong connectivity of lim under succ restricted to lim
    def reach(s, g):
        seen = {s}; st = [s]
        while st:
            v = st.pop()
            for w in g[v]:
                if w in lim and w not in seen: seen.add(w); st.append(w)
        return seen
    pred = {x: set() for x in lim}
    for x in lim:
        for y in succ[x]:
            if y in lim: pred[y].add(x)
    s0 = next(iter(lim)); sc = reach(s0, succ) == lim and reach(s0, pred) == lim
    def readable(word):
        layer = {x for x in lim if (x & 1) == int(word[0])}
        for ch in word[1:]:
            layer = {y for x in layer for y in succ[x] if y in lim and (y & 1) == int(ch)}
            if not layer: return False
        return True
    hit = [w for w in forb[b] if readable(w)]
    # minimal forbidden words of the limit set's column-1 language up to length 13
    minimal = []
    for L in range(1, 14):
        for w in map(''.join, itertools.product('01', repeat=L)):
            if any(m in w for m in minimal): continue
            if not readable(w): minimal.append(w)
    print(f"b={b}: image sizes {sizes}, stabilised after {len(sizes)-1} double steps; limit set strongly connected: {sc}")
    print(f"   kit forbidden words readable in the limit set: {hit} (expected none of {len(forb[b])})")
    print(f"   minimal forbidden column-1 words of the limit set up to length 13: {minimal}")
    print(f"   kit list equals that minimal list: {sorted(minimal) == sorted(forb[b])}")
F = lambda Y: (Y >> 1) ^ (Y | (Y << 1))
print("== 2. CT-3.1(a) and the width-bounded rank: survivor counts on the zero boundary")
def alive_through(Y, t):
    for s in range(0, t + 1):
        if s % 2 == 0 and not (Y & 1): return False
        Y = F(Y)
    return True
def S(W, t): return sum(1 for Y in range(1 << W) if alive_through(Y, t))
print("S_9(12), S_9(14) =", S(9, 12), S(9, 14), "; S_11(t), t=18..28 even:", [S(11, t) for t in range(18, 29, 2)])
surv = [Y for Y in range(1 << 11) if alive_through(Y, 28)]
def first_even_white(Y):
    t = 0
    while True:
        if t % 2 == 0 and not (Y & 1): return t
        Y = F(Y); t += 1
print("rows below 2^11 alive through tick 28:", surv, "widths", [y.bit_length() for y in surv], "first even white tick", [first_even_white(y) for y in surv])
print("exact range law S_W(t) = 2^(W - t//2 - 1), t < W, checked W <= 12:", all(S(W, t) == 2 ** (W - t // 2 - 1) for W in range(2, 13) for t in range(0, W)))
print("== 3. BR-6.1: rules 90 and 150 in the same frame")
F90 = lambda Y: (Y >> 1) ^ (Y << 1)
F150 = lambda Y: (Y >> 1) ^ Y ^ (Y << 1)
def death(Y, G, cap=400):
    for t in range(cap):
        if t % 2 == 0 and not (Y & 1): return t
        Y = G(Y)
    return None
def D(W, G):
    ds = [death(Y, G) for Y in range(1, 1 << W)]
    return None if any(x is None for x in ds) else max(ds)
def k_star(W):
    k = W + 1
    while k % 2 == 0 or k % 3 == 0: k += 1
    return k
rows = []
for W in range(2, 15):
    rows.append((W, D(W, F90), k_star(W) - 1, D(W, F150), 2 * ((W + 1) // 2)))
print("W, D_90(W), k*-1, D_150(W), 2*ceil(W/2):", rows)
print("closed forms hold for W=2..14 (as the first even white tick):", all(r[1] == r[2] and r[3] == r[4] for r in rows), "| offsets D_90-(k*-1):", sorted(set(r[1] - r[2] for r in rows)), "D_150-2ceil:", sorted(set(r[3] - r[4] for r in rows)))
def S_g(W, t, G):
    c = 0
    for Y in range(1 << W):
        y = Y; ok = True
        for s in range(t + 1):
            if s % 2 == 0 and not (y & 1): ok = False; break
            y = G(y)
        c += ok
    return c
print("rules 90 and 150 share the range law for t < W, W <= 10:", all(S_g(W, t, G) == 2 ** (W - t // 2 - 1) for G in (F90, F150) for W in range(2, 11) for t in range(W)))
print("== 4. LN-02.1: the cone-tip second derivative, and rule 210")
def a(Y, t, G):
    for _ in range(t): Y = G(Y)
    return Y & 1
ok = True
for t in range(2, 13):
    for Y in range(1 << (t + 1)):
        u, v = 1 << (t - 1), 1 << (t - 2)
        d2 = a(Y, t, F) ^ a(Y ^ u, t, F) ^ a(Y ^ v, t, F) ^ a(Y ^ u ^ v, t, F)
        if d2 != (t - 1) % 2: ok = False
print("D_(t-1) D_(t-2) a_t = (t-1) mod 2 for every row, t = 2..12:", ok)
F210 = lambda Y: (Y >> 1) ^ (~Y & (Y << 1))
print("rule 210: a_t(Y) = y_t for every Y in F_2^(t+1):", {t: all(a(Y, t, F210) == (Y >> t) & 1 for Y in range(1 << (t + 1))) for t in (3, 7, 11, 15)})
print("== 5. XP-2.2: whole-line configurations fixed by F^k (periodic points of the left-determination map on 2k cells)")
def Fk_cell(cells, k):         # cells: list of 2k+1 values x_(i-k)..x_(i+k); returns F^k(x)_i
    c = list(cells)
    for _ in range(k): c = [c[j - 1] ^ (c[j] | c[j + 1]) for j in range(1, len(c) - 1)]
    return c[0]
for k in (1, 2, 4):
    n = 2 * k; phi = {}
    for s in range(1 << n):
        right = [(s >> j) & 1 for j in range(n)]          # x_(i-k+1)..x_(i+k)
        xl = next(b for b in (0, 1) if Fk_cell([b] + right, k) == right[k - 1])   # x_(i-k), unique by left-permutivity
        assert sum(1 for b in (0, 1) if Fk_cell([b] + right, k) == right[k - 1]) == 1
        phi[s] = xl | ((s << 1) & ((1 << n) - 1))
    cur = set(phi)
    while True:
        nxt = {phi[s] for s in cur}
        if nxt == cur: break
        cur = nxt
    print(f"F^{k}: {len(cur)} whole-line fixed configurations")
print("== 6. LN-03.1: two rows with one image")
N = 4200
def rep(pre, per, n=N):
    bits = pre + per * ((n - len(pre)) // len(per) + 2)
    return sum(int(ch) << i for i, ch in enumerate(bits[:n]))
A, C, B = rep('', '1011111'), rep('', '1100001'), rep('11', '01001011001000')
G = lambda Y: F(F(Y)); M = (1 << (N - 200)) - 1
print("G(A) = C, G(B) = C on the first", N - 200, "depths:", (G(A) & M) == (C & M), (G(B) & M) == (C & M))
print("depths at which A and B differ, among the first 140:", sum(1 for i in range(140) if ((A ^ B) >> i) & 1), "; period of the difference pattern divides 14:", all((((A ^ B) >> i) & 1) == (((A ^ B) >> (i + 14)) & 1) for i in range(2, 2000)))
def in_K(Y, ticks=300):
    for t in range(ticks):
        if t % 2 == 0 and not (Y & 1): return False
        Y = F(Y)
    return True
print("A, B, C alive (depth 1 black at every even tick) through 300 ticks:", in_K(A), in_K(B), in_K(C), "; G(C) = C:", (G(C) & M) == (C & M))
