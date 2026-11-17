"""walk_colour.py: Erdős #582: a WalkSAT-style local search for a colouring with no one-colour triangle.

RUN-ON: cpu, python3. COMMAND: python3 tests/probes/swarm/ladder/e582/walk_colour.py M SEED SECONDS   (M = 127: G127)
Why (CL551): CaDiCaL times out at 60 s on random induced subgraphs of G127 with 90 to 100 vertices. A colouring found
by local search kills a subgraph as a Folkman candidate at once (and is verified triangle by triangle).
PREDICTIONS (before the run): on 90- and 100-vertex subgraphs the search gets close but stalls at a few one-colour
triangles; on 80 vertices it reaches 0. Counterfactual: 0 at 100 vertices means these subgraphs are colourable and
only CDCL-hard.
"""
import random, sys, time
p = 127; H = {pow(3, 3 * i, p) for i in range(42)}
adj = [set((v + s) % p for s in H) for v in range(p)]
m, seed, secs = int(sys.argv[1]), int(sys.argv[2]), float(sys.argv[3])
rnd = random.Random(seed)
vs = sorted(rnd.sample(range(p), m)) if m < p else list(range(p)); vset = set(vs)
eid = {}
for u in vs:
    for v in adj[u] & vset:
        if u < v: eid[(u, v)] = len(eid)
tris = [(eid[(u, v)], eid[(u, w)], eid[(v, w)]) for u in vs for v in adj[u] & vset if v > u for w in adj[u] & adj[v] & vset if w > v]
inc = [[] for _ in eid]
for t, (a, b, c) in enumerate(tris):
    inc[a].append(t); inc[b].append(t); inc[c].append(t)
col = [rnd.random() < .5 for _ in eid]
bad = lambda t: col[tris[t][0]] == col[tris[t][1]] == col[tris[t][2]]
badset = {t for t in range(len(tris)) if bad(t)}
best = len(badset); t0 = time.time(); flips = 0
while badset and time.time() - t0 < secs:
    t = rnd.choice(tuple(badset))     # always a random bad triangle (the first version cycled when 50 or more were bad)
    cand = tris[t]
    if rnd.random() < 0.3:
        e = rnd.choice(cand)
    else:   # flip the edge that breaks the fewest currently good triangles
        def breaks(e):
            c = col[e]; n = 0
            for s in inc[e]:
                a, b, d = tris[s]; others = [x for x in (a, b, d) if x != e]
                if col[others[0]] == col[others[1]] == (not c): n += 1
            return n
        e = min(cand, key=breaks)
    col[e] = not col[e]; flips += 1
    for s in inc[e]:
        if bad(s): badset.add(s)
        else: badset.discard(s)
    best = min(best, len(badset))
ok = not badset and all(not bad(t) for t in range(len(tris)))
print(f'm={m} seed={seed}: {len(eid)} edges, {len(tris)} triangles; best {best} one-colour triangles; '
      f'{"COLOURED (verified)" if ok else "not coloured"} after {flips} flips in {time.time()-t0:.0f}s', flush=True)
# OUTCOME (2026-10-22 15:23 BST, Cloud, CL551): the first version cycled (it picked the same bad triangle when 50 or more were
# bad); after the fix, best one-colour-triangle counts in 75 s: m = 90 (seed 7): 4; m = 100 (seed 11): 32; G127: 345.
# m = 80 (seed 7, first version) coloured in 1 s. The prediction held for m = 80 and 90; at m = 100 the walk is far
# from a colouring. Frustration grows with m; this is a measurement of the search, not a proof of anything.
