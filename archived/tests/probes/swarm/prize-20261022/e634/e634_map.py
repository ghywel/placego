#!/usr/bin/env python3
"""Erdos #634: (i) residues of x+2y for primitive Eisenstein triples; gcd(z, x+2y)=1;
(ii) UNEXPECTED CHECK: rational-lambda formal solutions of the isosceles area equation for N=19;
(iii) map of n<=100: classical, prime, and for composite non-classical n the shapes whose
area formulas still admit n arithmetically; (iv) Zhang's family: smallest non-classical N."""
import math, sys, time
T0 = time.time()
def tick():
    if time.time() - T0 > 540:
        print("TIME LIMIT HIT", flush=True); sys.exit(2)
def sq(n):
    if n < 0: return None
    r = math.isqrt(n); return r if r * r == n else None
def is_prime(n):
    if n < 2: return False
    for p in range(2, math.isqrt(n) + 1):
        if n % p == 0: return False
    return True

C = 3000
tr = []
m = 2
while m * m <= C:
    for n in range(1, m):
        if math.gcd(m, n) != 1 or (m - n) % 3 == 0: continue
        a, b, c = m*m - n*n, 2*m*n + n*n, m*m + m*n + n*n
        if c <= C: tr += [(a, b, c), (b, a, c)]
    m += 1
# (i)
res_odd, res4, badg = set(), set(), 0
for x, y, z in tr:
    s = x + 2 * y
    if s % 2: res_odd.add(s % 12)
    res4.add(s % 4)
    if math.gcd(z, s) != 1: badg += 1
print(f"(i) {len(tr)} ordered primitive triples, c<={C}: odd x+2y mod 12 in {sorted(res_odd)}; "
      f"x+2y mod 4 in {sorted(res4)}; gcd(z,x+2y)>1 count {badg}")
# (ii) unexpected: 19*y*(x+2y) a perfect square  <=>  lambda^2 = 19y/(x+2y) rational square
hits = [(x, y, z) for x, y, z in tr if sq(19 * y * (x + 2 * y)) is not None]
print(f"(ii) triples with 19*y*(x+2y) a square (rational lambda for N=19): {len(hits)} {hits[:6]}")
for x, y, z in hits[:6]:
    lam2 = 19 * y / (x + 2 * y)
    lam = math.sqrt(lam2)
    print(f"     {x,y,z}: lambda={lam:.6f}, legs lambda*z={lam*z:.6f}, base lambda*(x+2y)={lam*(x+2*y):.6f}")
# (iii) map n<=100
NMAX = 100
def classical(n):
    ok = False
    for u in range(0, math.isqrt(n) + 1):
        if sq(n - u * u) is not None: ok = True
    for f in (3, 6):
        if n % f == 0 and sq(n // f) is not None: ok = True
    return ok
def shapes(n):
    out = []
    for k in range(2, 60):
        for mm in range(1, k):
            if math.gcd(mm, k) != 1: continue
            for coef, name in ((2, 'T'), (3, 'I')):
                n0 = coef * k * k - mm * mm
                if n0 <= n and n % n0 == 0 and sq(n // n0) is not None:
                    j = sq(n // n0)
                    tag = f"{name}(k={k},m={mm},j={j})" + ("*" if j == 1 else "")
                    out.append(tag)
    for x, y, z in tr:
        s = x + 2 * y
        if s <= n and n % s == 0 and sq((n // s) * y) is not None:
            out.append(f"G2iso({x},{y},{z})")
        s = x + y
        if s <= n and n % s == 0 and sq((n // s) * y) is not None:
            out.append(f"G2a({x},{y},{z})")
        for F, nm in (((2*x + y) * (x + y), 'P1'), ((x + 2*y) * (2*x + y), 'P2'), (3 * (x + 2*y) * (x + y), 'P3')):
            if F <= n and n % F == 0 and sq(n // F) is not None:
                out.append(f"{nm}({x},{y},{z})")
    return sorted(set(out))
good, primes_bad, open_ = [], [], []
for n in range(1, NMAX + 1):
    tick()
    if classical(n): good.append(n); continue
    if is_prime(n): primes_bad.append(n); continue
    open_.append((n, shapes(n)))
print(f"(iii) classical good n<={NMAX} ({len(good)}): {good}")
print(f"      primes =3 mod 4 (7,11 published; rest preprint-claimed): {primes_bad}")
print(f"      composite non-classical ({len(open_)}): shapes admitting n arithmetically besides equilateral E"
      f" (* = j=1, excluded by the paper's Thm 37/41 if correct):")
for n, sh in open_:
    print(f"      {n}: {sh if sh else 'only E (equilateral, 2pi/3 tile)'}")
# (iv) Zhang family
zh = {}
for a in range(1, 200):
    for b in range(1, a + 1):
        tick()
        bound = 3 * (-(-(a*a + b*b + a*b - a - b) // (a * b)))
        nn = max(bound, 1)
        while nn * nn * a * b <= 20000:
            N = nn * nn * a * b
            if not classical(N):
                zh.setdefault(N, (a, b, nn))
            nn += 1
small = sorted(zh)[:12]
print(f"(iv) Zhang n^2ab (n>=bound), N<=20000 non-classical: count {len(zh)}; smallest: {[(N, zh[N]) for N in small]}")
print(f"done {time.time()-T0:.1f}s")
