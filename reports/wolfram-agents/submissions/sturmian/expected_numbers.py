# Numbers for the Sturmian essay, computed first (Cloud, 2026-10-23).
def std_words(d, n):
    """std 0 = [1], std 1 = [0], std (k+2) = std (k+1)^(d k) ++ std k; returns std 0 .. std n."""
    out = [[1], [0]]
    for k in range(n - 1):
        out.append(out[k + 1] * d[k] + out[k])
    return out
def cw(d, N):
    return std_words(d, N)[-1]
fib = [1] * 20
S = std_words(fib, 12)
print("Fibonacci standard words:", [''.join(map(str, w)) for w in S[:7]])
print("lengths:", [len(w) for w in S])
c = cw(fib, 14)
print("Fibonacci word, 55 bits:", ''.join(map(str, c[:55])))
# near-commutation check and the near-square table
for name, d in [("Fibonacci", fib), ("d = 2,1,3,1,2,1,3,1,...", [2, 1, 3, 1] * 5)]:
    S = std_words(d, 12); c = cw(d, 14)
    rows = []
    for n in range(1, 9):
        L = len(S[n]); l = 0
        while L + l < len(c) and c[l] == c[L + l]: l += 1
        rows.append((n, L, l, L - l))
    nc = all((S[n + 1] + S[n])[:-2] == (S[n] + S[n + 1])[:-2] and (S[n + 1] + S[n])[-2:] != (S[n] + S[n + 1])[-2:] for n in range(0, 11))
    print(name, "near-commutation:", nc, "| rows (n, |std n|, common future of (0,|std n|), slack):", rows)
# the forced left half of the Fibonacci word under the clock (as in the Corollary F essay)
T = 3000
c = cw(fib, 20)
def colv(t): return c[t // 2] if t % 2 == 0 else 0
cols = {0: [t % 2 for t in range(T)], 1: [colv(t) for t in range(T)]}
cols[-1] = [cols[0][t + 1] ^ (cols[0][t] | cols[1][t]) for t in range(T - 1)]
for m in range(2, T):
    prev, prev2 = cols[-m + 1], cols[-m + 2]
    n = len(prev) - 1
    if n <= 0: break
    cols[-m] = [prev[t + 1] ^ (prev[t] | prev2[t]) for t in range(n)]
row0 = [cols[-m][0] for m in range(0, T - 1) if -m in cols and len(cols[-m]) > 0]
blacks = [m for m, b in enumerate(row0) if b == 1]
print("forced left half of the Fibonacci word: depths", len(row0), "black cells", len(blacks), "first 30:", blacks[:30], "last", blacks[-1], "longest white gap", max(b - a for a, b in zip(blacks, blacks[1:])))
