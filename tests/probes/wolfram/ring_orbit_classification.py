#!/usr/bin/env python3
"""Local, 2026-10-28 (L1066): complete classification of Rule 30 ring orbits with moving-frame period dividing P.

Unrestricted pair graph: every pair (a, b) of P-periodic binary sequences (2^(2P) states). From (a, b), if a OR b has
an even number of 1s over P ticks, the successors are (b, c) with c the two P-periodic integrals of a OR b (initial
bit 0 or 1); otherwise none. In column coordinates of a ring of size m (columns indexed against the motion), a closed
walk of length m is exactly a ring configuration whose moving-frame map Phi(x)[i] = x[i] XOR (x[i+1] OR x[i+2]) has
period dividing P. So the cyclic strongly connected components classify ALL such ring orbits, for every ring size.
Usage: ring_orbit_classification.py P
"""
import sys
P = int(sys.argv[1]); M = (1 << P) - 1; N = 1 << (2 * P)
def pe(g):
    y = (g << 1) & M; k = 1
    while k < P: y ^= (y << k) & M; k <<= 1
    return y
def succ(s):
    a, b = s >> P, s & M; g = a | b
    if bin(g).count("1") & 1: return ()
    base = pe(g)
    return ((b << P) | base, (b << P) | (base ^ M))
# iterative Tarjan over all N states
index = [-1] * N; low = [0] * N; onst = bytearray(N); st = []; comps = []; cnt = 0
for r in range(N):
    if index[r] != -1: continue
    work = [(r, list(succ(r)), 0)]; index[r] = low[r] = cnt; cnt += 1; st.append(r); onst[r] = 1
    while work:
        v, kids, k = work[-1]
        if k < len(kids):
            work[-1] = (v, kids, k + 1); w = kids[k]
            if index[w] == -1:
                index[w] = low[w] = cnt; cnt += 1; st.append(w); onst[w] = 1; work.append((w, list(succ(w)), 0))
            elif onst[w]: low[v] = min(low[v], index[w])
        else:
            work.pop()
            if work: low[work[-1][0]] = min(low[work[-1][0]], low[v])
            if low[v] == index[v]:
                comp = []
                while True:
                    w = st.pop(); onst[w] = 0; comp.append(w)
                    if w == v: break
                if len(comp) > 1 or v in succ(v): comps.append(comp)
fmt = lambda x: format(x, f"0{P}b")[::-1]
print(f"P={P}: {N} states, {len(comps)} cyclic components")
for c in comps:
    edges = sum(1 for v in c for w in succ(v) if w in set(c))
    print(f"  size {len(c)}, internal edges {edges}:", [(fmt(v >> P), fmt(v & M)) for v in c][:8])
