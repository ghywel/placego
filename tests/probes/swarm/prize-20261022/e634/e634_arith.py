#!/usr/bin/env python3
"""Erdos #634 arithmetic checks (one core, <10 min).

Checks:
 1. Primitive Eisenstein triples (a,b,c), c^2=a^2+ab+b^2: brute force vs parametrisation
    (m^2-n^2, 2mn+n^2, m^2+mn+n^2), gcd(m,n)=1, m>n>0, m != n mod 3, up to swap.
 2. Lemma 16 of Beeson-Rosu: a+b composite for every primitive triple.
 3. Group-2 isosceles shapes: N prime iff exists primitive triple with one leg y=s^2 and x+2y=N.
    Prediction: for N = 3 mod 4 this needs y=m^2-n^2 (Pythagorean), first prime 71; 19 impossible.
    Cross-check by direct brute force (independent of the parametrisation).
 4. Group-1 hard shapes: N0 = 2k^2-m^2 (triquadratic), 3k^2-m^2 (isosceles-beta), 0<m<k, gcd=1.
    Prediction: for primes = 3 mod 4, T iff p=7 mod 8; I iff p=11 mod 12.
 5. Table 4 examples of Beeson-Rosu: exact area ratios by Heron, angle shapes.
"""
import math, sys, time

T0 = time.time()
LIMIT_S = 540

def tick():
    if time.time() - T0 > LIMIT_S:
        print("TIME LIMIT HIT", flush=True); sys.exit(2)

def isqrt_exact(n):
    if n < 0: return None
    r = math.isqrt(n)
    return r if r * r == n else None

def is_prime(n):
    if n < 2: return False
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: return False
        i += 6
    return True

# ---------- 1. triples ----------
C = 2500
brute = set()
for a in range(1, C + 1):
    tick()
    for b in range(1, C + 1):
        if math.gcd(a, b) != 1: continue
        c2 = a * a + a * b + b * b
        if c2 > C * C: break
        c = isqrt_exact(c2)
        if c is not None:
            brute.add((a, b, c))
param = set()
m = 2
while m * m <= C:
    for n in range(1, m):
        if math.gcd(m, n) != 1 or (m - n) % 3 == 0: continue
        a, b, c = m * m - n * n, 2 * m * n + n * n, m * m + m * n + n * n
        if c <= C:
            param.add((a, b, c)); param.add((b, a, c))
    m += 1
print(f"[1] primitive triples with c<={C}: brute={len(brute)} param={len(param)} equal={brute == param}")
if brute != param:
    print("   brute-param:", sorted(brute - param)[:10], " param-brute:", sorted(param - brute)[:10])

# ---------- 2. Lemma 16 ----------
bad16 = [(a, b, c) for (a, b, c) in brute if is_prime(a + b)]
print(f"[2] Lemma 16 (a+b composite): counterexamples among {len(brute)} triples: {len(bad16)} {bad16[:5]}")

# ---------- 3. Group-2 isosceles, prime N ----------
P = 200000
iso_primes = {}
m = 2
while m * m <= 2 * P:
    tick()
    for n in range(1, m):
        if math.gcd(m, n) != 1: continue
        a, b, c = m * m - n * n, 2 * m * n + n * n, m * m + m * n + n * n
        g = math.gcd(a, b)  # =3 when m=n mod 3
        a, b, c = a // g, b // g, c // g
        for (x, y, case) in ((a, b, 'A' if g == 1 else 'A3'), (b, a, 'B' if g == 1 else 'B3')):
            s = isqrt_exact(y)
            if s is None: continue
            p = x + 2 * y
            if p <= P and is_prime(p):
                iso_primes.setdefault(p, []).append((x, y, c, case, (m, n)))
    m += 1
p3 = sorted(p for p in iso_primes if p % 4 == 3)
p1 = sorted(p for p in iso_primes if p % 4 == 1)
print(f"[3] Group-2 isosceles prime N <= {P}: {len(iso_primes)} primes; =1 mod 4: {len(p1)}, =3 mod 4: {len(p3)}")
print("    first =3 mod 4:", [(p, iso_primes[p][0]) for p in p3[:8]])
print("    first =1 mod 4:", [(p, iso_primes[p][0][:3]) for p in p1[:8]])
cases3 = {}
for p in p3:
    for t in iso_primes[p]:
        cases3[t[3]] = cases3.get(t[3], 0) + 1
cases1 = {}
for p in p1:
    for t in iso_primes[p]:
        cases1[t[3]] = cases1.get(t[3], 0) + 1
print("    parametrisation cases for p=3 mod 4:", cases3, " for p=1 mod 4:", cases1)
# direct brute force, independent of the parametrisation
direct = []
for p in range(3, 20001, 4):
    if not is_prime(p): continue
    s = 1
    while 2 * s * s < p:
        x = p - 2 * s * s
        y = s * s
        if math.gcd(x, y) == 1 and isqrt_exact(x * x + x * y + y * y) is not None:
            direct.append((p, x, y)); break
        s += 1
print(f"    direct brute force, primes =3 mod 4 up to 20000 with a solution: {[d[0] for d in direct]}")
print(f"    agrees with parametrised list: {[d[0] for d in direct] == [p for p in p3 if p <= 20000]}")
print(f"    19 has a solution: {19 in iso_primes}")

# ---------- 4. Group-1 hard shapes ----------
def rep(p, coef):
    out = []
    k = 1
    while k * k <= p:  # m<k => coef*k^2 - m^2 > (coef-1)k^2 >= k^2
        m2 = coef * k * k - p
        if m2 > 0:
            mm = isqrt_exact(m2)
            if mm is not None and 0 < mm < k and math.gcd(mm, k) == 1:
                out.append((k, mm))
        k += 1
    return out

mismatch = []
table = []
for p in range(3, 100001, 4):
    if not is_prime(p): continue
    tick()
    Tr, Ir = rep(p, 2), rep(p, 3)
    predT, predI = (p % 8 == 7), (p % 12 == 11)
    if bool(Tr) != predT or bool(Ir) != predI:
        mismatch.append((p, Tr[:1], Ir[:1]))
    if p <= 400:
        table.append((p, p % 24, Tr[:1], Ir[:1], p in iso_primes))
print(f"[4] primes =3 mod 4 up to 100000: mismatches with (T iff 7 mod 8, I iff 11 mod 12): {len(mismatch)} {mismatch[:5]}")
print("    p, p mod 24, T rep (k,m), I rep (k,m), G2-isosceles arithmetically possible")
for row in table:
    print("   ", row)
free = [r[0] for r in table if not r[2] and not r[3] and not r[4]]
print("    primes =3 mod 4 <= 400 where T, I and G2-iso are all arithmetically void:", free)

# ---------- 5. Table 4 examples ----------
def heron16(x, y, z):
    return (x + y + z) * (-x + y + z) * (x - y + z) * (x + y - z)

def angles(x, y, z):
    A = math.acos((y * y + z * z - x * x) / (2 * y * z))
    B = math.acos((x * x + z * z - y * y) / (2 * x * z))
    return A, B, math.pi - A - B

examples = [((3, 5, 7), (39, 55, 49), 143), ((7, 8, 13), (91, 176, 195), 330),
            ((24, 11, 31), (961, 1426, 1155), 4830), ((5, 16, 19), (76, 76, 148), 37)]
for tile, tri, Nclaim in examples:
    a, b, c = tile
    assert a * a + a * b + b * b == c * c
    r = heron16(*tri)
    t = heron16(a, b, c)
    num, den = r, t
    g = math.gcd(num, den); num //= g; den //= g
    N = isqrt_exact(num) if den == 1 else None
    al, be, ga = angles(a, b, c)
    combos = []
    for ang in angles(*tri):
        best = None
        for i in range(0, 5):
            for j in range(0, 5):
                if abs(i * al + j * be - ang) < 1e-9:
                    best = (i, j)
        combos.append(best)
    print(f"[5] tile {tile} tri {tri}: N^2 ratio={num}/{den}, N={N}, claim={Nclaim}, ok={N == Nclaim}; "
          f"tri angles as (i*alpha+j*beta): {combos}")

print(f"done in {time.time() - T0:.1f}s")
