#!/usr/bin/env python3
"""L1407 (Local, 2026-11-03): exact checks for the carrying read of GC2505/GC2506 (padded histories B and D).
Run: python3 tests/probes/mahler/padding_arithmetic_check.py

P1 strict tails: for B = p_1 0^4 p_2 0^7 ... and D = p_1 0 p_2 0 ..., p_k = (100)^k, every tail U_j of a long prefix,
   with the unknown future bounded by 1 (B) or by the minimum-gap-3 bound a (D, whose future is again D-like), is < a = 9/19;
   packet-start tails approach a (m_k = a (1 - r^(3k))).
P2 ages: B's packet starts A_k = 3k^2 - 2k - 1 and long zero runs (length 3k + 3 at 3k^2 + k - 3); D's packet starts
   (3k^2 - k - 2)/2; the height margins j c + 6 - K > 0 for k <= 2000 (c = log2(3/2)).
P3 gap words and R_L (least second origin of a repeated length-L factor) by brute force against (L+1)(L+2)/2 (B) and
   h(h+1)/2 + 1, h = ceil(L/2) (D), for L <= 30; gap means.
P4 capped slack: Z_(m+1) = min(2^(T_m+s_m), 3^s_m Z_m - 2^(T_m+s_m+1)) stays 2^T_m for 200 random gap words with gaps >= 3.
P5 the D clock: the first packet anchor 171 n_1 + 73 = 1024 v_2 (v_2 = 49 mod 342, n_1 = 293 mod 2048); for n_1 = 293 + 2048 t,
   t < 4000, the number of D digits the actual orbit of F(n) = ceil(3n/2) realizes agrees with the first k at which
   the recurrence 2^(3k+4) v_(k+1) = 3^(3k+1) v_k - 1 fails to give an odd integer (the exact equivalence of GC2506).
P6 the hand control: 293's orbit, its first 11 parities 10001001000, 25380 even at time 11, 2187 * 49 - 1 = 666 mod 1024.
"""
import math
import random
from fractions import Fraction as Fr

r = Fr(2, 3)
a = Fr(9, 19)


def history(kind, K):
    out, starts = [], []
    for k in range(1, K + 1):
        starts.append(len(out))
        out += [1, 0, 0] * k
        out += [0] * ((3 * k + 1) if kind == 'B' else 1)
    return out, starts


def tails(bits, future):
    """U_j for every j of the finite prefix, with the tail after the prefix worth `future` (a bound)."""
    n = len(bits); U = [Fr(0)] * (n + 1)
    U[n] = future * 3                       # U_n = (1/3) * sum ... ; store 3U to reuse the recursion
    for j in range(n - 1, -1, -1):
        U[j] = bits[j] + r * U[j + 1]
    return [u / 3 for u in U[:n]]


for kind, fut in (('B', Fr(1)), ('D', a)):
    bits, starts = history(kind, 9)
    U = tails(bits, fut)
    U = U[:starts[-1] + 27]                 # through the last packet's ones; later padding tails are r^d * (next start)
    mk = [U[s] for s in starts]
    print('P1 %s: %d tails checked; every tail < a: %s; max tail %.12f (a = %.12f); packet starts approach a: %s' % (
        kind, len(U), all(u < a for u in U), float(max(U)), float(a),
        all(mk[i] < mk[i + 1] for i in range(len(mk) - 1))))

ok_age = True
for k in range(1, 40):
    bitsB, stB = history('B', k)
    bitsD, stD = history('D', k)
    ok_age &= stB[-1] == 3 * k * k - 2 * k - 1 and stD[-1] * 2 == 3 * k * k - k - 2
    run_start = stB[-1] + 3 * k - 2
    ok_age &= bitsB[run_start - 1] == 1 and all(b == 0 for b in bitsB[run_start:run_start + 3 * k + 3])
c = math.log2(1.5)
marg = min((3 * k * k + k - 3) * c + 6 - (3 * k + 3) for k in range(1, 2001))
margD = min(3 * math.log2(3) + (3 * k * k - k - 2) / 2 * c + 6 - 3 * k for k in range(1, 2001))
print('P2 ages and long-run positions match for k < 40: %s; min B height margin %.3f; min D repeat margin %.3f' % (
    ok_age, marg, margD))


def gapword(kind, K):
    g = []
    for k in range(1, K + 1):
        g += [3] * (k - 1) + [(3 * k + 4) if kind == 'B' else 4]
    return g


def R(g, L):
    seen = {}
    for i in range(len(g) - L + 1):
        f = tuple(g[i:i + L])
        if f in seen:
            return i
        seen[f] = i
    return None


okR = True
for kind in ('B', 'D'):
    g = gapword(kind, 60)
    for L in range(1, 31):
        h = -(-L // 2)
        want = (L + 1) * (L + 2) // 2 if kind == 'B' else h * (h + 1) // 2 + 1
        okR &= R(g, L) == want
gB, gD = gapword('B', 50), gapword('D', 50)
print('P3 R_L formulas hold for L <= 30 (both words): %s; gap means after 50 packets: B %.4f (6 + 2/51 = %.4f), D %.4f' % (
    okR, sum(gB) / len(gB), 6 + 2 / 51, sum(gD) / len(gD)))

rng = random.Random(2505)
okZ = True
for _ in range(200):
    s = [rng.choice([3, 3, 4, 5, 9]) for _ in range(40)]
    T, Z = 0, 1
    for sm in s:
        Z = min(2 ** (T + sm), 3 ** sm * Z - 2 ** (T + sm + 1))
        T += sm
        okZ &= Z == 2 ** T
print('P4 capped slack equals 2^T for 200 random gap words with gaps >= 3: %s' % okZ)

bitsD, stD = history('D', 8)


def realized(n, bits):
    """How many leading digits of `bits` the parities of n, F(n), F(F(n)), ... realize."""
    for j, b in enumerate(bits):
        if n % 2 != b:
            return j
        n = (3 * n + 1) // 2 if n % 2 else 3 * n // 2
    return len(bits)


def predicted(t):
    """Digits guaranteed by the anchored recurrence: packets 1..k realized while v stays an odd integer."""
    v = 49 + 342 * t
    k = 2
    while k <= 8:
        num = 3 ** (3 * k + 1) * v - 1
        if num % 2 ** (3 * k + 4) or (num // 2 ** (3 * k + 4)) % 2 == 0:
            return k
        v = num // 2 ** (3 * k + 4)
        k += 1
    return 9


anchor_ok = all((171 * (293 + 2048 * t) + 73) == 1024 * (49 + 342 * t) for t in range(1000))
agree = 0
for t in range(4000):
    n1 = 293 + 2048 * t
    got = realized(n1, bitsD)
    kfail = predicted(t)
    # packets 1..kfail-1 are certified; the orbit must realize at least through their end and fail inside packet kfail
    # v_(kfail+1) is not an odd integer: packets 1..kfail are realized and the orbit fails inside packet kfail + 1
    lo = stD[kfail] if kfail < len(stD) else len(bitsD)
    hi = stD[kfail + 1] if kfail + 1 < len(stD) else len(bitsD)
    agree += (lo <= got < hi) or (kfail >= 8 and got >= stD[7])
print('P5 anchor 171 n_1 + 73 = 1024 v_2 on n_1 = 293 + 2048 t: %s; realized length falls in the packet where the '
      'recurrence first fails for %d of 4000 seeds' % (anchor_ok, agree))
orb = [293]
for _ in range(11):
    n = orb[-1]; orb.append((3 * n + 1) // 2 if n % 2 else 3 * n // 2)
print('P6 orbit of 293: %s; parities 0..10 %s (D: %s); 2187*49-1 mod 1024 = %d' % (
    orb, ''.join(str(x % 2) for x in orb[:11]), ''.join(map(str, bitsD[:11])), (2187 * 49 - 1) % 1024))
print('PADDING_ARITHMETIC_DONE')
