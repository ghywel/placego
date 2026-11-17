# Numbers for the Theorem A4 essay: computed here first (Cloud, 2026-10-23).
T = 400
W = 2 * T + 3
rows = [[0] * W for _ in range(T + 1)]
rows[0][T + 1] = 1
for t in range(T):
    r, n = rows[t], rows[t + 1]
    for p in range(1, W - 1):
        n[p] = r[p - 1] ^ (r[p] | r[p + 1])
def cell(t, p): return rows[t][p + T + 1]
def D(k, t): return cell(t, k - t)          # the kit's left diagonal k at time t
c0 = [cell(t, 0) for t in range(T + 1)]
c1 = [cell(t, 1) for t in range(T + 1)]
# longest common block of (c0, c1) starting at a and a'
best = []
for a2 in range(1, T + 1):
    for a in range(a2):
        n = 0
        while a2 + n <= T and c0[a + n] == c0[a2 + n] and c1[a + n] == c1[a2 + n]:
            n += 1
        best.append((n, a, a2))
best.sort(reverse=True)
print("longest common blocks (n, a, a'):", best[:8])
def M(P, t):
    """largest M with D k (t-P) = D k t for all 0 <= k <= M (M = -1 if none)."""
    m = -1
    while m + 1 <= t and D(m + 1, t - P) == D(m + 1, t):
        m += 1
    return m
print("settled width M(P, t):")
for t in (100, 200, 400):
    print(t, [(P, M(P, t)) for P in (1, 2, 4, 8, 16)])
print("the bound for the longest blocks, P = 1, 2, 4:")
for n, a, a2 in best[:6]:
    for P in (1, 2, 4):
        m = M(P, a2)
        if P <= a2 and m < a2 - a:
            print((n, a, a2), "P", P, "M", m, "bound a'-M+2P-1 =", a2 - m + 2 * P - 1, "Jen's bound a' =", a2, "holds", n <= a2 - m + 2 * P - 1)
