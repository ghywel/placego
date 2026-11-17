# Numbers for the Theorem E essay, computed first (Cloud, 2026-10-23).
from math import sqrt
def mech(alpha, theta, N):
    from math import floor
    return [floor(theta + (i + 1) * alpha) - floor(theta + i * alpha) for i in range(N)]
g = (sqrt(5) - 1) / 2
c = mech(g, 0.5, 60000)
print("golden slope, intercept 1/2, first 40 bits:", ''.join(map(str, c[:40])))
print("distinct blocks p(n), n = 1..12:", [len(set(tuple(c[s:s + n]) for s in range(50000))) for n in range(1, 13)])
def collide(c, n):
    seen = {}
    for s in range(n + 2):
        f = tuple(c[s:s + n])
        if f in seen: return seen[f], s
        seen[f] = s
def table(alpha, theta):
    c = mech(alpha, theta, 20000); rows = []
    for n in [5, 10, 20, 50, 100, 200, 500, 1000, 2000]:
        i, j = collide(c, n); l = 0
        while j + l < len(c) and c[i + l] == c[j + l]: l += 1
        rows.append((n, i, j, j - i, l, j - l))
    return rows
print("collision table golden, 1/2:", table(g, 0.5))
print("collision table sqrt2-1, 0.1:", table(sqrt(2) - 1, 0.1))
print("collision table 0.261278.., 0.777:", table(1 / (3 + 1 / (1 + 1 / (4 + 1 / (1 + 1 / (3 + 1 / (1 + 1 / 4.0)))))), 0.777))
# forced left half of the golden word with intercept 1/2 under the clock
T = 3000
c = mech(g, 0.5, 2000)
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
print("forced left half (golden, 1/2): depths", len(row0), "black", len(blacks), "first 30", blacks[:30], "last", blacks[-1], "max spacing", max(b - a for a, b in zip(blacks, blacks[1:])))
