# Independent check (lead) of agent e552's witness for R(C4, K_{1,41}) = 49.
# R(C4, K_{1,n}) > N iff some C4-free graph on N vertices has minimum degree >= N - n.
import math, itertools
m = 24
V = [(x, s) for s in (0, 1) for x in range(m)]
idx = {v: i for i, v in enumerate(V)}
N = len(V)
adj = [set() for _ in range(N)]
def add(u, v):
    a, b = idx[u], idx[v]
    assert a != b
    adj[a].add(b); adj[b].add(a)
for x in range(m):
    for e in (9, -9): add((x, 0), ((x + e) % m, 0))
    for e in (3, -3): add((x, 1), ((x + e) % m, 1))
    for d in (0, 5, 7, 20, 21): add((x, 0), ((x + d) % m, 1))
deg = [len(a) for a in adj]
maxcommon = max(len(adj[i] & adj[j]) for i, j in itertools.combinations(range(N), 2))
# direct 4-cycle search as a second test: a-b-c-d-a with all distinct
c4 = 0
for a in range(N):
    for b in adj[a]:
        for c in adj[b]:
            if c == a: continue
            for d in adj[c]:
                if d in (a, b): continue
                if a in adj[d]: c4 += 1
edges = sum(deg) // 2
tri = sum(1 for i, j, k in itertools.combinations(range(N), 3) if j in adj[i] and k in adj[i] and k in adj[j])
n = 41
print(f"N={N} edges={edges} degrees min/max={min(deg)}/{max(deg)} max common neighbours={maxcommon} directed 4-cycles={c4} triangles={tri}")
print(f"witness gives R > N iff min degree >= N - n = {N - n}: {min(deg) >= N - n}")
print(f"Parsons upper bound n + ceil(sqrt n) + 1 = {n + math.isqrt(n - 1) + 1 + 1} (as n + floor(sqrt(n-1)) + 2 = {n + math.isqrt(n-1) + 2})")
# control: the same checker must reject a graph with a 4-cycle (add one chord that creates one)
