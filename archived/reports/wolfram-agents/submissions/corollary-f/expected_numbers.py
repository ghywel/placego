# Numbers for the Corollary F essay, computed first (Cloud, 2026-10-23).
# Period-doubling: fixed point of 0 -> 01, 1 -> 00, i.e. d_n = 1 iff the 2-adic valuation of n+1 is odd.
def v2(n):
    k = 0
    while n % 2 == 0: n //= 2; k += 1
    return k
N = 4096
d = [1 if v2(n + 1) % 2 == 1 else 0 for n in range(N)]
print("period-doubling, first 32 bits:", ''.join(map(str, d[:32])))
# near-squares: the common future of 0 and 2^k
for k in range(1, 12):
    l = 0
    while 2**k + l < N and d[l] == d[2**k + l]: l += 1
    print("k", k, "l(0, 2^k) =", l, "= 2^k - 1:", l == 2**k - 1)
# the forced left half: x(0, t) = t mod 2 (the clock), x(1, 2i) = d_i (visible bits), column 1 at odd times is irrelevant;
# x(-1, t) = x(0, t+1) xor (x(0, t) or x(1, t)); x(-m, t) = x(-m+1, t+1) xor (x(-m+1, t) or x(-m+2, t)).
T = 3000
def c(t): return d[t // 2] if t % 2 == 0 else 0
cols = {0: [t % 2 for t in range(T)], 1: [c(t) for t in range(T)]}
cols[-1] = [cols[0][t + 1] ^ (cols[0][t] | cols[1][t]) for t in range(T - 1)]
for m in range(2, T):
    prev, prev2 = cols[-m + 1], cols[-m + 2]
    n = len(prev) - 1
    if n <= 0: break
    cols[-m] = [prev[t + 1] ^ (prev[t] | prev2[t]) for t in range(n)]
row0 = [cols[-m][0] for m in range(0, T - 1) if -m in cols and len(cols[-m]) > 0]
blacks = [m for m, b in enumerate(row0) if b == 1]
print("time-0 row of the forced left half, depths computed:", len(row0))
print("black cells at depths (first 40):", blacks[:40])
print("number of black cells:", len(blacks), "last black depth:", blacks[-1])
print("longest white gap between blacks:", max(b - a for a, b in zip(blacks, blacks[1:])))
# the seed's center column is not the clock
W = 2 * 24 + 3
rows = [[0] * W for _ in range(24)]
rows[0][W // 2] = 1
for t in range(23):
    for p in range(1, W - 1): rows[t + 1][p] = rows[t][p - 1] ^ (rows[t][p] | rows[t][p + 1])
print("seed center column, 20 cells:", ''.join(str(rows[t][W // 2]) for t in range(20)))
