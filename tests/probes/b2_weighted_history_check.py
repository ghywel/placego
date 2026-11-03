#!/usr/bin/env python3
"""L1418 (Local, 2026-11-03): exact checks for the carrying read of GC2519 (B2's weighted response and history set H).
Run: python3 tests/probes/b2_weighted_history_check.py

Edge bits R_i(t) of a finite seed under R_i(t+1) = R_i(t) + [R_(i-1)(t) OR R_(i-2)(t)] (negative bits white); L_i the least
period of the prefix R_0..R_i, d_i = log2(L_i / L_(i-1)) (L_(-1) = 1).
B1 the hand control: seed 0x889da3, lower bits, streams R0..R4, periods, word d4 d3 d2 = 100, and the four interventions
   (beta, gamma) on seed bits 1, 2: local d2 d3 and the outer d4, as in the report's table.
B2 the weighted identity F_w(G_new) + F_w(G) = beta A_w + gamma B_w + beta gamma S_w on 2,000 random (U, V, W, w, h-consistent)
   cases: V_new = V + beta, W_new = W + gamma + beta h, h(t) = sum_(u<t) (1 + U(u)).
B3 the history set H via the triple recurrence (p, q, r) against brute-force recomputation of every flag d_1..d_(j-1) for
   all four choices, on 300 random odd seeds and random bit pairs (k, k+1), j up to 14.
"""
import random
from math import log2


def streams(seed_bits, nbits, T):
    """R[i][t] for i < nbits, t < T."""
    x = list(seed_bits) + [0] * (nbits - len(seed_bits))
    R = [[0] * T for _ in range(nbits)]
    for t in range(T):
        for i in range(nbits):
            R[i][t] = x[i]
        x = [x[i] ^ ((x[i - 1] if i >= 1 else 0) | (x[i - 2] if i >= 2 else 0)) for i in range(nbits)]
    return R


def least_period(rows, T):
    for p in [1 << e for e in range(0, 20)]:
        if p > T // 2:
            return None
        if all(r[t] == r[t + p] for r in rows for t in range(T - p)):
            return p
    return None


def flags(R, T):
    L = [1]
    for i in range(len(R)):
        L.append(least_period(R[:i + 1], T))
    return [int(log2(L[i + 1] // L[i])) if L[i + 1] and L[i] else None for i in range(len(R))], L[1:]


seed = 0x889da3
bits = [(seed >> i) & 1 for i in range(24)]
T = 64
R = streams(bits, 6, T)
d, L = flags(R, T)
print('B1 seed bits R0..R5(0) =', bits[:6], '; streams R0..R4 (one period):', [''.join(map(str, R[i][:L[i]])) for i in range(5)])
print('   L1..L5 =', L[1:6], '; d4 d3 d2 =', d[4], d[3], d[2])
for be in (0, 1):
    for ga in (0, 1):
        b2 = list(bits); b2[1] ^= be; b2[2] ^= ga
        R2 = streams(b2, 6, T); d2, L2 = flags(R2, T)
        print('   (beta, gamma) = (%d, %d): R1 %s R2 %s R3 %s R4 %s; local d2 d3 = %d%d; outer d4 = %d' % (
            be, ga, ''.join(map(str, R2[1][:L2[1]])), ''.join(map(str, R2[2][:L2[2]])),
            ''.join(map(str, R2[3][:max(L2[3], 1)])), ''.join(map(str, R2[4][:L2[4]])), d2[2], d2[3], d2[4]))

rng = random.Random(2519)
okW = True
for _ in range(2000):
    P = rng.choice([2, 4, 8, 16])
    U = [rng.getrandbits(1) for _ in range(P)]; V = [rng.getrandbits(1) for _ in range(P)]
    W = [rng.getrandbits(1) for _ in range(P)]; w = [rng.getrandbits(1) for _ in range(P)]
    h = [sum(1 ^ U[u] for u in range(t)) % 2 for t in range(P)]
    G = [V[t] | W[t] for t in range(P)]
    F = lambda f: sum(w[t] & f[t] for t in range(P)) % 2
    S = F([1] * P); A = F([1 ^ W[t] ^ (V[t] & h[t]) for t in range(P)]); B = F([1 ^ V[t] for t in range(P)])
    for be in (0, 1):
        for ga in (0, 1):
            Vn = [V[t] ^ be for t in range(P)]; Wn = [W[t] ^ ga ^ (be & h[t]) for t in range(P)]
            Gn = [Vn[t] | Wn[t] for t in range(P)]
            okW &= (F(Gn) ^ F(G)) == ((be & A) ^ (ga & B) ^ (be & ga & S))
print('B2 weighted identity on 2,000 random cases, all four (beta, gamma): %s' % okW)

# B3: triple recurrence for the responses, H, and brute force
agree = total = 0
nontrivial = 0
for trial in range(300):
    nb = 16
    sb = [1] + [rng.getrandbits(1) for _ in range(nb - 1)]
    k = rng.randrange(1, 8)
    j = rng.randrange(k + 3, 15)
    TT = 1 << 13
    Rb = streams(sb, j + 1, TT); db, Lb = flags(Rb, TT)
    if None in db[:j + 1]:
        continue
    # responses (u, v, z) per bit, integrated with the same XOR update
    u = [[0] * TT for _ in range(j + 1)]; v = [[0] * TT for _ in range(j + 1)]; z = [[0] * TT for _ in range(j + 1)]
    for i in range(j + 1):
        for t in range(TT):
            if t == 0:
                u[i][0] = int(i == k); v[i][0] = int(i == k + 1); z[i][0] = 0
            else:
                a = Rb[i - 1][t - 1] if i >= 1 else 0; b = Rb[i - 2][t - 1] if i >= 2 else 0
                ua, va, za = (u[i - 1][t - 1], v[i - 1][t - 1], z[i - 1][t - 1]) if i >= 1 else (0, 0, 0)
                ub, vb, zb = (u[i - 2][t - 1], v[i - 2][t - 1], z[i - 2][t - 1]) if i >= 2 else (0, 0, 0)
                p = ((1 ^ b) & ua) ^ ((1 ^ a) & ub) ^ (ua & ub)
                q = ((1 ^ b) & va) ^ ((1 ^ a) & vb) ^ (va & vb)
                r = ((1 ^ b) & za) ^ ((1 ^ a) & zb) ^ (ua & vb) ^ (va & ub) ^ (ua & zb) ^ (za & ub) ^ (va & zb) ^ (za & vb) ^ (za & zb)
                u[i][t] = u[i][t - 1] ^ p; v[i][t] = v[i][t - 1] ^ q; z[i][t] = z[i][t - 1] ^ r
    # forcing sums over the baseline prefix period P_i = L_(i-1): the response of the forcing of bit i is the change of R_i
    # over one step, i.e. its (p, q, r) at bit i; the flag parity is the sum over P_i of the forcing
    for be in (0, 1):
        for ga in (0, 1):
            pred_ok = True
            for i in range(1, j):
                P = Lb[i - 1]
                # sum over t < P of the forcing response = response of R_i(t + P) - R_i(t) at t = 0
                ps = u[i][P] ^ u[i][0]; qs = v[i][P] ^ v[i][0]; rs = z[i][P] ^ z[i][0]
                if (be & ps) ^ (ga & qs) ^ (be & ga & rs):
                    pred_ok = False; break
            s2 = list(sb); s2[k] ^= be; s2[k + 1] ^= ga
            R2 = streams(s2, j + 1, TT); d2, L2 = flags(R2, TT)
            brute_ok = d2[:j] == db[:j]
            total += 1; agree += pred_ok == brute_ok
            nontrivial += pred_ok and (be, ga) != (0, 0)
print('B3 history set H by the triple recurrence agrees with brute-force flags in %d of %d (seed, choice) cases; '
      'nontrivial choices in H: %d' % (agree, total, nontrivial))
print('B2_WEIGHTED_DONE')
