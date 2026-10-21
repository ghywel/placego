"""Cloud's machine check for GPT's G338 (CL478): brute force over ALL tournaments on n <= 7 vertices.

For each colouring of n vertices with four ordinary colours and one *, every tournament gives (class sums, q);
group tournaments by that data and take the Phi = sum d^2 maximisers.  G338 claims every global maximiser has
at most two nontrivial strong components, with at most six vertices in them; if two, both are triangles, one
contains *, and their ordinary palettes share exactly one colour.  Also recorded: G335's rainbow property.
Prediction: 0 violations (G338 is a theorem if its two-path step is right).  Counterfactual: a violation
pins the step that fails.
"""
import itertools, sys
from collections import defaultdict

def scc_sizes(adj, n):
    # Kosaraju on tournament adjacency (adj[u] has v iff u -> v)
    order = []; seen = [False] * n
    def dfs(u):
        seen[u] = True
        for v in range(n):
            if adj[u] >> v & 1 and not seen[v]: dfs(v)
        order.append(u)
    for u in range(n):
        if not seen[u]: dfs(u)
    comp = [-1] * n; c = 0
    for u in reversed(order):
        if comp[u] != -1: continue
        stack = [u]; comp[u] = c
        while stack:
            x = stack.pop()
            for v in range(n):
                if adj[v] >> x & 1 and comp[v] == -1: comp[v] = c; stack.append(v)
        c += 1
    return comp, c

def run(n, colourings):
    pairs = list(itertools.combinations(range(n), 2)); m = len(pairs)
    tours = []
    for mask in range(1 << m):
        adj = [0] * n
        for i, (u, v) in enumerate(pairs):
            if mask >> i & 1: adj[u] |= 1 << v
            else: adj[v] |= 1 << u
        d = [bin(a).count('1') for a in adj]
        comp, c = scc_sizes(adj, n)
        sizes = defaultdict(int)
        for u in range(n): sizes[comp[u]] += 1
        tours.append((tuple(d), comp, dict(sizes)))
    viol = 0; checked = 0; maxima_with_cycles = 0
    for col in colourings:
        best = {}
        for d, comp, sizes in tours:
            key = tuple(sum(d[v] for v in range(n) if col[v] == k) for k in range(5))
            phi = sum(x * x for x in d)
            if key not in best or phi > best[key][0]: best[key] = (phi, [])
            if phi == best[key][0]: best[key][1].append((d, comp, sizes))
        for key, (phi, lst) in best.items():
            for d, comp, sizes in lst:
                checked += 1
                big = [cid for cid, s in sizes.items() if s > 1]
                if big: maxima_with_cycles += 1
                ok = len(big) <= 2 and sum(sizes[c] for c in big) <= 6
                pals = []
                for cid in big:
                    cols = [col[v] for v in range(n) if comp[v] == cid]
                    if len(set(cols)) != len(cols): ok = False      # rainbow (G335)
                    pals.append(set(cols))
                if len(big) == 2:
                    if not all(sizes[c] == 3 for c in big): ok = False
                    if not any(4 in p for p in pals): ok = False
                    inter = (pals[0] & pals[1]) - {4}
                    if len(inter) != 1: ok = False
                if not ok:
                    viol += 1
                    if viol <= 3: print('VIOLATION', n, col, key, d, sizes)
    return checked, maxima_with_cycles, viol

if __name__ == '__main__':
    import random
    rnd = random.Random(5)
    for n in (5, 6, 7):
        cols = set()
        tries = 0
        while len(cols) < (60 if n == 7 else 200) and tries < 5000:
            tries += 1
            c = [rnd.randrange(4) for _ in range(n)]; c[rnd.randrange(n)] = 4
            cols.add(tuple(c))
        print(n, 'colourings', len(cols), 'maximisers checked / with cycles / violations:', run(n, sorted(cols)), flush=True)
