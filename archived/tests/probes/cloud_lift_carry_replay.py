#!/usr/bin/env python3
"""Cloud CL778, item R: replay of GPT's GC2931 and GC2933 in code written from the statements alone.

The object is the integer lift of rule 30 from one cell (Nersissian, arXiv 2609.25078):
    A_(t+1)(j) = A_t(j-1) + A_t(j) + A_t(j+1) + A_t(j) A_t(j+1),   A_0 = one 1 at j = 0,
read along left diagonals u_n(t) = 1 + A_t(n - t), which obey u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1 with
u_0 = 2 and u_n = 1 for n < 0 (CL777 section 4.2, carried by GPT in GC2931).

Part 0  the diagonal recurrence against the whole integer rows to t = 12.
Part 1  GC2931, odd primes below 200: the second clock's least period is 2d (d = ord_p(2) even) or p d (d odd);
        S = 0 or S * Sbar = d; exact balance at odd d; the second clock reaches zero inside its first period and
        the third clock is periodic one tick later.  Negative controls: "2d always", "p d always".
Part 2  GC2931, primes 2, 3, 5, 7 to depth 16: prefix periods P_n, n + 2 <= p^(2 P_n), P_n = lcm of the last two
        scalar periods.
Part 3  GC2931 and GC2933 modulo 2^64: C = lim u_3(t) + t, u_4 -> 0, u_5 - u_3 -> 0, u_6 = F(C - t) with the stated
        onsets for k <= 40, truncated valuations, least period 2^k for k <= 12.  F is computed two ways for k <= 12
        (the rising-factorial sum; the signed derangement numbers).  Negative controls: reversed phase, phase
        shifted by one, zero class shifted by one.
This is a self-check of my hand read (CL778 items 1 and 2), not a second read.  Usage: cloud_lift_carry_replay.py
"""
import math, sys, time
import numpy as np

OK = []


def check(name, cond, detail=""):
    OK.append(bool(cond))
    print(f"   [{'PASS' if cond else 'FAIL'}] {name}" + (f"  {detail}" if detail else ""))


def order(a, p):
    k, x = 1, a % p
    while x != 1:
        x = x * a % p; k += 1
    return k


def odd_primes_below(n):
    sieve = bytearray([1]) * n; sieve[0:2] = b"\0\0"
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = bytearray(len(sieve[i * i::i]))
    return [i for i in range(3, n) if sieve[i]]


def divisors(n):
    return sorted(d for d in range(1, n + 1) if n % d == 0)


def v2(x, cap):
    if x == 0:
        return cap
    return min(cap, (x & -x).bit_length() - 1)


# ---------------------------------------------------------------- part 0
def part0():
    print("== Part 0: the diagonal recurrence on the whole integer rows, t <= 12")
    T = 12
    row = {0: 1}; rows = [row]
    for _ in range(T):
        new = {}
        for j in range(min(row) - 1, max(row) + 2):
            l, c, r = row.get(j - 1, 0), row.get(j, 0), row.get(j + 1, 0)
            v = l + c + r + c * r
            if v:
                new[j] = v
        row = new; rows.append(row)
    u = lambda n, t: 1 + rows[t].get(n - t, 0)
    bad = sum(u(n, t + 1) != u(n, t) * u(n - 1, t) + u(n - 2, t) - 1 for n in range(-2, 2 * T + 3) for t in range(T))
    check("u_n(t+1) = u_n(t) u_(n-1)(t) + u_(n-2)(t) - 1 for -2 <= n <= 26, t < 12", bad == 0)
    check("u_0 = 2, u_(-1) = 1, u_1 = 2^t", all(u(0, t) == 2 and u(-1, t) == 1 and u(1, t) == 2 ** t for t in range(T + 1)))
    check("centre counts 1, 1, 4, 17, 199, 11783, 13840878", [rows[t].get(0, 0) for t in range(7)] == [1, 1, 4, 17, 199, 11783, 13840878])


# ---------------------------------------------------------------- part 1
def part1():
    print("== Part 1: the second and third clocks at the odd primes below 200 (GC2931)")
    ps = odd_primes_below(200)
    allok = dict(period=True, tail=True, sums=True, balance=True, zero=True, third=True, prefix3=True)
    claim_2d = claim_pd = 0
    rows = []
    for p in ps:
        d = order(2, p)
        P2 = 2 * d if d % 2 == 0 else p * d
        T = 4 * P2 + 2 * d + 8
        pw = [pow(2, t, p) for t in range(d)]
        x = [1] * (T + 1); y = [1] * (T + 1)
        for t in range(T):
            x[t + 1] = (pw[t % d] * x[t] + 1) % p                    # u_2(t+1) = 2^t u_2(t) + 1
            y[t + 1] = (y[t] * x[t] + pw[t % d] - 1) % p             # u_3(t+1) = u_3(t) u_2(t) + 2^t - 1
        # least period from time zero: the least divisor Q of P2 with x(t+Q) = x(t) on the whole window
        isper = lambda s, Q, t0: all(s[t + Q] == s[t] for t in range(t0, len(s) - Q))
        least0 = next((Q for Q in divisors(P2) if isper(x, Q, 0)), None)
        allok["period"] &= (least0 == P2)
        # least eventual period, judged on the second half of the window
        leastT = next((Q for Q in divisors(P2) if isper(x, Q, T // 2)), None)
        allok["tail"] &= (leastT == P2)
        claim_2d += (least0 == 2 * d); claim_pd += (least0 == p * d)
        tri = lambda j: j * (j + 1) // 2
        inv2 = pow(2, p - 2, p)
        S = sum(pow(inv2, tri(j), p) for j in range(d)) % p
        Sb = sum(pow(2, tri(j), p) for j in range(d)) % p
        allok["sums"] &= (S == 0) if d % 2 == 0 else (S * Sb % p == d % p and S != 0)
        if d % 2 == 1:
            cnt = [0] * p
            for t in range(P2):
                cnt[x[t]] += 1
            allok["balance"] &= all(c == d for c in cnt)
        z = next(t for t in range(T) if x[t] == 0)                   # first zero of the second clock
        if d % 2 == 0:
            allok["zero"] &= (x[d] == p - 1 and x[d + 1] == 0 and z <= d + 1)
        else:
            # GPT's statement: x(kd) = 1 + kS, so some 1 <= k <= p - 1 gives a zero at a multiple of d.
            # The first zero of all may come earlier, at another phase.
            lin = all(x[k * d] == (1 + k * S) % p for k in range(p + 1))
            kz = next(k for k in range(1, p) if x[k * d] == 0)
            allok["zero"] &= lin and 1 <= kz <= p - 1 and z <= kz * d
        allok["zero"] &= z < P2
        allok["third"] &= isper(y, P2, z + 1)                         # third clock P2-periodic from z + 1
        onset = next(t0 for t0 in range(T) if isper(y, P2, t0))
        pair = list(zip(x, y))
        least3 = next((Q for Q in divisors(P2) if isper(pair, Q, T // 2)), None)
        allok["prefix3"] &= (least3 == P2)
        rows.append((p, d, P2, z, onset))
    n_even = sum(order(2, p) % 2 == 0 for p in ps)
    check(f"least period of u_2 from time zero is 2d (d even) or p d (d odd), all {len(ps)} primes", allok["period"])
    check("the same on the tail (least eventual period)", allok["tail"])
    check("S = 0 at even d; S * Sbar = d and S != 0 at odd d", allok["sums"])
    check("at odd d every residue occurs exactly d times in a period", allok["balance"])
    check("u_2 reaches zero inside its first period (x(d) = -1, x(d+1) = 0 at even d; x(kd) = 1 + kS with a zero at some k <= p - 1 at odd d)", allok["zero"])
    check("u_3 is P2-periodic from one tick after the first zero of u_2", allok["third"])
    check("the prefix (u_2, u_3) has least eventual period exactly P2", allok["prefix3"])
    check("negative control: 'the period is 2d at every prime' fails", claim_2d < len(ps), f"holds at {claim_2d} of {len(ps)} (the {n_even} primes with d even)")
    check("negative control: 'the period is p d at every prime' fails", claim_pd < len(ps), f"holds at {claim_pd} of {len(ps)}")
    print("   p, d = ord_p(2), P2, first zero z of u_2, true onset of u_3's periodicity:")
    for i in range(0, len(rows), 6):
        print("     " + " | ".join(f"{p}: {d}, {P2}, {z}, {o}" for p, d, P2, z, o in rows[i:i + 6]))
    odd = [p for p, d, *_ in rows if d % 2]
    print(f"   primes with d odd ({len(odd)}): {odd}")


# ---------------------------------------------------------------- part 2
def part2():
    print("== Part 2: prefix periods to depth 16 at p = 2, 3, 5, 7 (GC2931, backward profile)")
    DEPTH, T = 16, 1 << 19
    for p in (2, 3, 5, 7):
        u = np.ones(DEPTH + 2, dtype=np.int64); u[1] = 2 % p        # index n + 1; u[0] is depth -1, u[1] is depth 0
        hist = np.empty((T, DEPTH + 2), dtype=np.uint8)
        for t in range(T):
            hist[t] = u
            nxt = u.copy()
            nxt[2:] = (u[2:] * u[1:-1] + u[:-2] - 1) % p
            u = nxt
        tail0 = T // 2
        def is_period(cols, Q):
            a = hist[tail0:T - Q, cols]; b = hist[tail0 + Q:T, cols]
            return bool((a == b).all())
        def least(cols, bound):
            # least eventual period on the tail window, searched over the divisors of a verified period
            return next(Q for Q in divisors(bound) if is_period(cols, Q))
        P = 1; out = []; ok_bound = ok_lcm = True; settled = DEPTH
        scal = {}
        for n in range(1, DEPTH + 1):
            cols = list(range(2, n + 2))
            cand = None
            for r in sorted({1, p} | set(divisors(p - 1))):
                if P * r <= (T - tail0) // 4 and is_period(cols, P * r):
                    cand = P * r; break
            if cand is None:
                settled = n - 1
                print(f"   p = {p}: depth {n} not settled inside the window (period above {(T - tail0) // 4} or a longer transient); stopping there")
                break
            P = least(cols, cand)
            scal[n] = least([n + 1], P)
            ok_bound &= (n + 2 <= p ** (2 * P))
            if n >= 2:
                ok_lcm &= (P == math.lcm(scal[n - 1], scal[n]))
            out.append((n, P, scal[n]))
        print(f"   p = {p}: (depth, prefix period, scalar period): " + " ".join(f"({n},{P},{s})" for n, P, s in out))
        check(f"p = {p}: n + 2 <= p^(2 P_n) to depth {settled}", ok_bound)
        check(f"p = {p}: P_n = lcm of the scalar periods of depths n - 1 and n, 2 <= n <= {settled}", ok_lcm)


# ---------------------------------------------------------------- part 3
def part3():
    print("== Part 3: the 2-adic cascade and depth six modulo 2^64 (GC2931, GC2933)")
    K, T, KMAX = 64, 1 << 14, 40
    M = (1 << K) - 1
    u = [[1] * (T + 1) for _ in range(8)]                             # u[n][t], n = 0..7
    u[0] = [2] * (T + 1)
    for t in range(T):
        for n in range(1, 8):
            below = u[n - 2][t] if n >= 2 else 1
            u[n][t + 1] = (u[n][t] * u[n - 1][t] + below - 1) & M
    C = (u[3][K + 2] + K + 2) & M
    check("u_3(t) + t is constant modulo 2^64 for t >= 65", all((u[3][t] + t) & M == C for t in range(K + 1, T + 1)), f"C mod 2^16 = {C & 0xFFFF}")
    vals = [v2((C - u[3][t] - t) & M, K) for t in range(1, K + 1)]
    check("v_2(C - u_3(t) - t) >= t - 1 for 1 <= t <= 64", all(v >= t - 1 for t, v in zip(range(1, K + 1), vals)),
          f"equality at {sum(v == t - 1 for t, v in zip(range(1, K + 1), vals))} of 64 ticks")
    rk = {}
    for k in range(1, KMAX + 1):
        r = 0
        while r - bin(r).count("1") < k:                              # v_2(r!) = r - s_2(r)
            r += 1
        rk[k] = r
    check("r_k <= 2k for k <= 40", all(rk[k] <= 2 * k for k in rk), "r_k: " + " ".join(str(rk[k]) for k in (1, 2, 3, 4, 8, 16, 32, 40)) + " at k = 1, 2, 3, 4, 8, 16, 32, 40")

    def true_onset(pred, k):                                          # least t0 with pred(t) for every t0 <= t <= T
        t0 = T + 1
        for t in range(T, -1, -1):
            if not pred(t, k):
                break
            t0 = t
        return t0
    m = lambda k: (1 << k) - 1
    on4 = {k: true_onset(lambda t, k: u[4][t] & m(k) == 0, k) for k in rk}
    on5 = {k: true_onset(lambda t, k: (u[5][t] - u[3][t]) & m(k) == 0, k) for k in rk}
    check("u_4 = 0 modulo 2^k from k + 1 + r_k, k <= 40", all(on4[k] <= k + 1 + rk[k] for k in rk))
    check("u_5 = u_3 modulo 2^k from k + 2 + r_k, k <= 40", all(on5[k] <= k + 2 + rk[k] for k in rk))

    R40 = rk[KMAX]; M40 = m(KMAX)
    def F_sum(x, k):                                                  # - sum_(j < r_k) (x+1)...(x+j) modulo 2^k
        tot, prod = 0, 1
        for j in range(rk[k]):
            if j:
                prod = prod * (x + j) & m(k)
            tot += prod
        return (-tot) & m(k)
    # F by the derangement numbers, all residues, k <= 12
    okF = okrec = okval = okzero = True
    for k in range(1, 13):
        D = [1] * (1 << k)
        for n in range(1, 1 << k):
            D[n] = (n * D[n - 1] + (1 if n % 2 == 0 else -1)) & m(k)
        Fd = {}
        for n in range(1 << k):
            x = (-n - 1) & m(k)
            Fd[x] = (-(D[n] if n % 2 == 0 else -D[n])) & m(k)
        Fs = [F_sum(x, k) for x in range(1 << k)]
        okF &= all(Fs[x] == Fd[x] for x in range(1 << k))
        okrec &= all(Fs[(x - 1) & m(k)] == (x * Fs[x] - 1) & m(k) for x in range(1 << k))
        okval &= all(v2(Fs[x], k) == v2((x + 2) & m(k), k) for x in range(1 << k))
        okzero &= [x for x in range(1 << k) if Fs[x] == 0] == [m(k) - 1]          # the class of -2
    check("F by the rising-factorial sum equals -(-1)^n D_n at x = -n-1, every residue, k <= 12", okF)
    check("F(x - 1) = x F(x) - 1, every residue, k <= 12", okrec)
    check("min(v_2(F(x)), k) = min(v_2(x + 2), k), every residue, k <= 12", okval)
    check("F vanishes modulo 2^k only on the class of -2, k <= 12", okzero)
    print("   F modulo 4 at x = 0, 1, 2, 3:", [F_sum(x, 2) for x in range(4)])

    G = [F_sum((C - t) & M40, KMAX) for t in range(T + 1)]            # F(C - t) modulo 2^40
    N6 = {k: k + 2 + 2 * rk[k] for k in rk}
    on6 = {k: true_onset(lambda t, k: (u[6][t] - G[t]) & m(k) == 0, k) for k in rk}
    check("u_6(t) = F(C - t) modulo 2^k for N_6(k) <= t <= 16384, k <= 40", all(on6[k] <= N6[k] for k in rk))
    check("the simpler onset 5k + 2 and statement (2): v_2(u_6(t) - F(C - t)) >= floor((t - 2)/5) for 7 <= t <= 202",
          all(N6[k] <= 5 * k + 2 for k in rk) and all(v2((u[6][t] - G[t]) & M40, KMAX) >= min(KMAX, (t - 2) // 5) for t in range(7, 203)))
    okv = all(v2(u[6][t] & m(k), k) == v2((C + 2 - t) & m(k), k) for k in rk for t in range(N6[k], T + 1))
    check("min(v_2(u_6(t)), k) = min(v_2(C + 2 - t), k) beyond N_6(k), k <= 40", okv)
    okp = True
    for k in range(1, 13):
        P = 1 << k; t0 = N6[k]
        per = all((u[6][t + P] - u[6][t]) & m(k) == 0 for t in range(t0, T + 1 - P))
        half = k >= 1 and all((u[6][t + P // 2] - u[6][t]) & m(k) == 0 for t in range(T // 2, T + 1 - P // 2)) if P > 1 else False
        okp &= per and not half
    check("least eventual period of u_6 modulo 2^k is exactly 2^k, k <= 12 (2^k is a period, 2^(k-1) is not)", okp)
    print("   k: stated onsets (u_4, u_5, u_6) against the true ones on this window")
    for k in (1, 2, 3, 4, 6, 8, 12, 16, 24, 32, 40):
        print(f"     k = {k:2d}: r_k = {rk[k]:2d} | u_4: {k + 1 + rk[k]:3d} / {on4[k]:3d} | u_5: {k + 2 + rk[k]:3d} / {on5[k]:3d} | u_6: {N6[k]:3d} / {on6[k]:3d}")
    k = 8
    rev = sum((u[6][t] - F_sum((C + t) & m(k), k)) & m(k) != 0 for t in range(N6[k], N6[k] + 1024))
    shf = sum((u[6][t] - F_sum((C - t + 1) & m(k), k)) & m(k) != 0 for t in range(N6[k], N6[k] + 1024))
    zc = sum((u[6][t] & m(k) == 0) != ((C + 1 - t) & m(k) == 0) for t in range(N6[k], N6[k] + 1024))
    check("negative control: the reversed phase F(C + t) fails (k = 8)", rev > 0, f"{rev} of 1024 ticks differ")
    check("negative control: the phase shifted by one, F(C - t + 1), fails (k = 8)", shf > 0, f"{shf} of 1024 ticks differ")
    check("negative control: zeros at t = C + 1 modulo 2^8 fails", zc > 0, f"{zc} of 1024 ticks disagree")
    # the seventh diagonal is GPT's proof target; only its measured period is printed, as a guide (no claim)
    for k in (1, 2, 3, 4, 5, 6):
        P = next(1 << e for e in range(0, 14) if all((u[7][t + (1 << e)] - u[7][t]) & m(k) == 0 for t in range(T // 2, T + 1 - (1 << e))))
        print(f"   measured, not claimed: least eventual period of u_7 modulo 2^{k} on the tail is {P}")


def main():
    t0 = time.time()
    part0(); part1(); part2(); part3()
    print(f"ALL PASS: {all(OK)} ({sum(OK)} of {len(OK)} checks); {time.time() - t0:.0f} s")


if __name__ == "__main__":
    main()
