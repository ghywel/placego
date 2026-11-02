#!/usr/bin/env python3
"""L1304 (Local, 2026-11-02): the first H2 block after GC2361. Run: python3 tests/probes/h2_block1.py
reports/inquisition-local-to-gpt-20261102.md section 6. Three parts, each a control rather than a search:
1. numeric controls for GC2361's hand sketches (level signs, the p = 4 coin control, A/C/beta, generator growth);
2. return-section conventions against the actual maps on Z/2^16 and actual Phi-orbits on T_p nodes (p = 8, 16),
   and the kit's decomposition b = tau' o a, c = sigma o b (here tau' flips bit 1 when bit 0 is 1), so
   a^-1 psi a = omega o a^2 with omega = +1 mod 4 on the two lowest bits;
3. family (F): every return section of cycle length L is l o c^L with l finitary of depth <= 2L.
"""
print('== part 1: GC2361 controls')
import itertools, random
random.seed(0)
# automaton 2369 on words (bit lists, index 0 first): state after reading ...x y: y=1 -> a, (x,y)=(1,0) -> b, (0,0) -> c
# a = sigma(b, a), b = sigma(c, a), c = (c, a): (flip?, section after 0, section after 1)
AUT = {'a': (1, 'b', 'a'), 'b': (1, 'c', 'a'), 'c': (0, 'c', 'a')}
def act1(s, w):            # apply state s to word w
    out = []
    for x in w:
        f, s0, s1 = AUT[s]; out.append(x ^ f); s = s1 if x else s0
    return out
def act(word, w):          # word = (s_{L-1}, ..., s_0): apply s_0 first
    for s in reversed(word): w = act1(s, w)
    return w
def section(word, x):      # section at the one-letter word x; returns (output letter, section word)
    sec = []
    for s in reversed(word):
        f, s0, s1 = AUT[s]; sec.append(s1 if x else s0); x ^= f
    return x, tuple(reversed(sec))
E = {'a': (1, 0, 0), 'b': (0, 1, 0), 'c': (0, 0, 1)}
def evec(word): return tuple(sum(E[s][i] for s in word) % 2 for i in range(3))
# (i) level signs lambda_n(g) = sum over depth-n vertices of root activity of the section
def lam(word, n):
    tot = 0
    for v in itertools.product((0, 1), repeat=n):
        g = word
        for x in v: _, g = section(g, x)
        tot ^= AUT_act(g)
    return tot
def AUT_act(word): return sum(AUT[s][0] for s in word) % 2
rows = [(1, 1, 0), (0, 1, 1), (1, 1, 1)] + [(0, 0, 0)] * 3
ok = True
for _ in range(300):
    L = random.randint(1, 7); word = tuple(random.choice('abc') for _ in range(L)); e = evec(word)
    for n in range(6):
        pred = sum(rows[n][i] * e[i] for i in range(3)) % 2
        if lam(word, n) != pred: ok = False
print('(i) level signs lambda_0..5 = (110),(011),(111),0,0,0 on 300 random positive words:', ok)
# (iii) p = 4 control: v = 0000; u = 1100 vs 1010 (time left to right); g = s_3 s_2 s_1 s_0
def s_of(u, v): return 'a' if v else ('b' if u else 'c')
def integ(d):
    w, acc = [], 0
    for x in d: w.append(acc); acc ^= x
    return w
for u in ((1, 1, 0, 0), (1, 0, 1, 0)):
    v = (0, 0, 0, 0); d = [x | y for x, y in zip(u, v)]; w = integ(d)
    coin = sum(x | y for x, y in zip(v, w)) % 2
    g = tuple(s_of(u[t], v[t]) for t in reversed(range(4)))
    # child return sections g|_0, g|_1: their root activity must equal the coin
    c0 = AUT_act(section(g, 0)[1]); c1 = AUT_act(section(g, 1)[1])
    print('(iii) u =', ''.join(map(str, u)), 'w =', ''.join(map(str, w)), 'coin', coin, 'g =', ''.join(g), 'e =', evec(g), 'child activities', c0, c1)
# (v) A, C, beta at type-0 splits on random even rings
bad = 0
for _ in range(2000):
    p = random.choice((4, 8, 16, 32))
    v = [random.randint(0, 1) for _ in range(p)]; u = [random.randint(0, 1) for _ in range(p)]
    d = [x | y for x, y in zip(u, v)]
    if sum(v) % 2 or sum(d) % 2: continue
    w = integ(d); A = sum(w) % 2; A2 = sum(d[s] for s in range(0, p, 2)) % 2
    C = sum(x & y for x, y in zip(v, w)) % 2
    child = (sum(w) % 2, sum(x & (1 - y) for x, y in zip(v, w)) % 2, sum((1 - x) & (1 - y) for x, y in zip(v, w)) % 2)
    beta = sum(x | y for x, y in zip(v, w)) % 2
    B = lambda f, g: sum(f[s] * g[t] for s in range(p) for t in range(s + 1, p)) % 2
    h = [1 - x for x in v]
    if not (A == A2 and child == (A, C, (A + C) % 2) and beta == (A + C) % 2 and beta == B(d, h)
            and (B(d, h) + B(h, d)) % 2 == sum(x * y for x, y in zip(d, h)) % 2): bad += 1
print('(v) A = sum of d at even times, child e = (A, C, A+C), beta = A + C = B(d,h), B(d,h)+B(h,d) = <d,h>: failures', bad)
# (iv) growth: each of a, b, c raises log2 of a positive natural by exactly 2 (bit lists are little-endian, finite tail 0)
def nat_bits(n, L): return [(n >> i) & 1 for i in range(L)]
ok = True
for n in range(1, 4000):
    k = n.bit_length() - 1
    for s in 'abc':
        out = act1(s, nat_bits(n, k + 8)); val = sum(b << i for i, b in enumerate(out))
        if val.bit_length() - 1 != k + 2: ok = False
print('(iv) each generator raises log2(n) by exactly 2 for n = 1..3999:', ok)
print('== part 2: conventions')
AUT = {'a': (1, 'b', 'a'), 'b': (1, 'c', 'a'), 'c': (0, 'c', 'a')}
def gen(s, z, n):                      # apply automaton state s to z mod 2^n (bit 0 read first)
    out = 0
    for i in range(n):
        x = (z >> i) & 1; f, s0, s1 = AUT[s]; out |= (x ^ f) << i; s = s1 if x else s0
    return out
def Phi(z, n): return (z ^ ((z << 1) | (z << 2) | 3)) & ((1 << n) - 1)
n = 16; N = 1 << n
# 1. the automaton states are the 2-adic maps a(z) = z xor ((z<<1)|(z<<2)|3), b = ...|1, c = ...|0
ok = all(gen('a', z, n) == Phi(z, n) and gen('b', z, n) == (z ^ ((z << 1) | (z << 2) | 1)) % N
         and gen('c', z, n) == (z ^ ((z << 1) | (z << 2))) % N for z in range(N))
print('a, b, c are the three edge maps on Z/2^16:', ok)
# 2. b = tau o a and c = sigma o b, with sigma = flip bit 0 and tau = flip bit 1 when bit 0 is 1; omega = sigma o tau
sig = lambda z: z ^ 1
tau = lambda z: z ^ (2 if z & 1 else 0)
ok2 = all(gen('b', z, n) == tau(gen('a', z, n)) and gen('c', z, n) == sig(gen('b', z, n)) for z in range(N))
print('b = tau o a and c = sigma o b on Z/2^16:', ok2)
om = lambda z: sig(tau(z))
print('omega = sigma o tau on two-bit words (z mod 4 -> omega(z) mod 4):', [om(z) % 4 for z in range(4)], '(adds 1 mod 4, no carry)',
      all(om(z) >> 2 == z >> 2 for z in range(N)))
# 3. psi = a o c is conjugate by a to omega o a^2:  a^{-1} psi a = omega a^2
psi = lambda z: gen('a', gen('c', z, n), n)
f = lambda z: om(gen('a', gen('a', z, n), n))
ok3 = all(psi(gen('a', z, n)) == gen('a', f(z), n) for z in range(N))
print('psi o a = a o (omega o a o a) on Z/2^16:', ok3)
# 4. return sections from columns versus the actual orbit: walk T_p from the defect for p = 8 and 16, carrying the
#    actual word (digits at time 0); at each node check the orbit length and the states along the orbit
def check(p, depth_cap=40):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    def integ(d, L):
        w, acc = 0, 0
        for t in range(L):
            if acc: w |= 1 << t
            acc ^= (d >> t) & 1
        return w
    # columns as rings of length p; the black edge: c_{-2} = 0, c_{-1} = all ones; digit k of the point at time t = c_k(t)
    # start from the black edge and build columns down to the defect, then branch; verify against Phi on integers
    nodes = 0; bad = 0
    st = [([0, M], 1)]                 # list of columns (c_{-2}, c_{-1}, c_0, ...), current half-period H
    while st:
        cols, H = st.pop()
        k = len(cols) - 2              # number of real digits so far
        if k >= 1:
            nodes += 1
            L = 2 * H
            z = sum(((cols[2 + i] >> 0) & 1) << i for i in range(k))       # digits at time 0
            # actual orbit of z mod 2^k under Phi: its length must be L, and digits at time t must match the columns
            y = z; orbit = []
            for t in range(L):
                orbit.append(y); y = Phi(y, k)
            if y != z or any(Phi(orbit[t], k) == z for t in range(L - 1)): bad += 1
            for t in range(L):
                if any(((orbit[t] >> i) & 1) != ((cols[2 + i] >> t) & 1) for i in range(k)): bad += 1
            # the return-section word g = s_{L-1} ... s_0 with s_t = s(c_{k-2}(t), c_{k-1}(t)) must act on the next digit
            # exactly as Phi^L does on the lifts of z
            word = tuple(('a' if (cols[-1] >> t) & 1 else ('b' if (cols[-2] >> t) & 1 else 'c')) for t in reversed(range(L)))
            for x in (0, 1):
                zz = z | (x << k); y = zz
                for t in range(L): y = Phi(y, k + 1)
                out = x
                for s in reversed(word): out ^= AUT[s][0]
                if ((y >> k) & 1) != out: bad += 1
            if k > depth_cap: continue
        u, v = cols[-2], cols[-1]; d = (u | v) & ((1 << (2 * H)) - 1)
        sp = bin(d).count('1') & 1
        H2 = 2 * H if sp else H
        if 2 * H2 > p: continue
        L2 = 2 * H2
        dd = u | v
        w0 = integ(dd, L2); Lm = (1 << L2) - 1
        # extend w0 periodically to length p
        def per(w, L):
            out = 0
            for t in range(p): out |= ((w >> (t % L)) & 1) << t
            return out
        kids = [per(w0, L2)] if sp else [per(w0, L2), per(w0 ^ Lm, L2)]
        for w in kids: st.append((cols + [w], H2))
    print('p', p, 'nodes checked', nodes, 'mismatches', bad)
check(8); check(16)
print('== part 3: family (F)')
import random
AUT = {'a': (1, 'b', 'a'), 'b': (1, 'c', 'a'), 'c': (0, 'c', 'a')}
def gen(s, z, n):
    out = 0
    for i in range(n):
        x = (z >> i) & 1; f, s0, s1 = AUT[s]; out |= (x ^ f) << i; s = s1 if x else s0
    return out
def word_act(word, z, n):
    for s in reversed(word): z = gen(s, z, n)
    return z
def c_inv(y, n):          # c(z) = z xor ((z<<1)|(z<<2)): solve bit by bit
    z = 0
    for i in range(n):
        b = ((y >> i) & 1) ^ ((((z >> (i - 1)) & 1) if i >= 1 else 0) | (((z >> (i - 2)) & 1) if i >= 2 else 0))
        z |= b << i
    return z
def nodes(p):
    M = (1 << p) - 1
    def integ(d, L):
        w, acc = 0, 0
        for t in range(L):
            if acc: w |= 1 << t
            acc ^= (d >> t) & 1
        return w
    def per(w, L):
        out = 0
        for t in range(p): out |= ((w >> (t % L)) & 1) << t
        return out
    A = sum(1 << t for t in range(1, p, 2))
    st = [(A, A, 1, 0)]; out = []
    while st:
        u, v, H, depth = st.pop(); out.append((u, v, H))
        d = (u | v) & ((1 << (2 * H)) - 1); sp = bin(d).count('1') & 1; H2 = 2 * H if sp else H
        if 2 * H2 > p or depth > 30: continue
        L2 = 2 * H2; w0 = integ(u | v, L2)
        for w in ([per(w0, L2)] if sp else [per(w0, L2), per(w0 ^ ((1 << L2) - 1), L2)]):
            st.append((v, w, H2, depth + 1))
    return out
rng = random.Random(5); bad = 0; checked = 0
for p in (4, 8, 16):
    for (u, v, H) in nodes(p):
        L = 2 * H; word = tuple(('a' if (v >> t) & 1 else ('b' if (u >> t) & 1 else 'c')) for t in reversed(range(L)))
        n = 2 * L + 8
        zs = range(1 << n) if n <= 14 else [rng.randrange(1 << n) for _ in range(400)]
        for z in zs:
            # l(y) = g(c^{-L}(y)); check l changes only bits < 2L and that the change depends only on y mod 2^{2L}
            y = z; cz = z
            for _ in range(L): cz = c_inv(cz, n)
            ly = word_act(word, cz, n)
            if (ly ^ y) >> (2 * L): bad += 1
            y2 = (y & ((1 << (2 * L)) - 1)) | (rng.randrange(1 << (n - 2 * L)) << (2 * L)); cz2 = y2
            for _ in range(L): cz2 = c_inv(cz2, n)
            if ((word_act(word, cz2, n) ^ y2) & ((1 << (2 * L)) - 1)) != ((ly ^ y) & ((1 << (2 * L)) - 1)): bad += 1
            checked += 1
print('(F) l = g o c^-L is finitary of depth <= 2L: checked', checked, 'points on T_p nodes for p = 4, 8, 16; failures', bad)
