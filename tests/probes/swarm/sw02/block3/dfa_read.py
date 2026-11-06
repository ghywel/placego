#!/usr/bin/env python3
"""Minimise a gap DFA written by lift --dfa-from, and report its recurrent structure.

Every nonempty subset is accepting: the language is the set of gap words on paths of the component. Moore refinement on
the complete automaton (with a dead state) gives the minimal DFA. Then: its strongly connected parts, each with its
simple cycles' gap words up to a bound, and the word counts by length, which must match lift's own count.
Usage: dfa_read.py FILE [MAX_CYCLES]
"""
import collections, sys
import networkx as nx
path = sys.argv[1]; maxc = int(sys.argv[2]) if len(sys.argv) > 2 else 40
T = {}; size = {}
for line in open(path):
    p = line.split()
    s = int(p[0]); size[s] = int(p[1]); T[s] = {}
    for x in p[2:]:
        g, t = x.split(':'); T[s][int(g)] = int(t)
bad = sum(t < 0 for r in T.values() for t in r.values())
print('subset states', len(T), 'unexpanded edges', bad)
letters = sorted({g for r in T.values() for g in r})
# word counts
cnt = {0: 1}; ways = collections.Counter({0: 1})
counts = []
for n in range(1, 25):
    nxt = collections.Counter()
    for s, w in ways.items():
        for g, t in T[s].items(): nxt[t] += w
    ways = nxt; counts.append(sum(ways.values()))
print('words by length 1..24:', counts)
# Moore refinement
DEAD = -1
part = {s: 0 for s in T}; part[DEAD] = 1
while True:
    sig = {s: (part[s],) + tuple(part[T[s].get(g, DEAD)] if s != DEAD else part[DEAD] for g in letters) for s in part}
    ids = {}
    new = {s: ids.setdefault(v, len(ids)) for s, v in sig.items()}
    if len(ids) == len(set(part.values())): break
    part = new
M = collections.defaultdict(dict)
for s in T:
    for g, t in T[s].items(): M[part[s]][g] = part[t]
start = part[0]
print('minimal DFA states', len(M), 'letters', letters)
G = nx.MultiDiGraph()
for s, r in M.items():
    for g, t in r.items(): G.add_edge(s, t, gap=g)
D = nx.DiGraph(); D.add_edges_from((u, v) for u, v in G.edges())
comps = [c for c in nx.strongly_connected_components(D) if len(c) > 1 or any(D.has_edge(v, v) for v in c)]
print('recurrent parts of the minimal DFA:', sorted(len(c) for c in comps))
for c in sorted(comps, key=len, reverse=True):
    H = D.subgraph(c)
    seen = set(); out = []
    for cyc in nx.simple_cycles(H):
        words = ['']
        for i, v in enumerate(cyc):
            t = cyc[(i + 1) % len(cyc)]
            ws = [d['gap'] for d in G.get_edge_data(v, t).values()]
            words = [w + str(g) for w in words for g in ws]
        for w in words:
            r = min(w[i:] + w[:i] for i in range(len(w)))
            seen.add(r)
        if len(seen) > 4000: break
    prim = sorted(seen, key=lambda w: (len(w), w))
    print(' part of', len(c), 'states:', len(prim), 'simple-cycle words; shortest', prim[:maxc])
