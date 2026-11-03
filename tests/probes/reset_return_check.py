#!/usr/bin/env python3
"""L1375 (Local, 2026-11-03): carrying checks of GC2453 (reset law, return accounting, costly states) and a corrected
realizability test of the S = 13 extremal cycle that keeps masked inputs free.
Run: python3 tests/probes/reset_return_check.py POTENTIALS.json CYCLE.txt PERIODS

R1 every re-anchoring edge of the S = 13 strip graph (ether_strip_potentials.py's independent step) goes from phase 2
   to phase 3, and the new strip's low 8 bits are 11111001 (word = 159 mod 256); the number of distinct post-shift words.
R2 GC2453's counterexample: phase 2, cells 1..7 black, 8..13 white: the post-shift word is 159 (not 1951).
R3 the costly states (0, 2258), (1, 5982), (1, 8030): h(current), h(next) for both inputs, and the cost
   sigma = h(v) + 44 d + 7 - h(next), from the stored potentials.
R4 the extremal 44-cycle as a cycle of strip NODES: at each tick the allowed inputs are every u with
   step(node_t, u) = node_(t+1) (masked inputs stay free). A depth-first search over the right half (cell a+14 on) asks
   whether any right half realises PERIODS repetitions of the node cycle (moving input column a + 14 - 7j).
"""
import json
import sys

TAB = [[0, 0, 1, 1], [0, 1, 1, 0], [1, 1, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [0, 0, 0, 1], [0, 0, 0, 1]]
S = 13


def step(ph, s, u):
    cells = [TAB[(2 + i) % 7][ph] for i in (-1, 0)] + [(s >> j) & 1 for j in range(S)] + [u]
    new = [cells[i - 1] ^ (cells[i] | cells[i + 1]) for i in range(1, len(cells) - 1)]
    ph2 = (ph + 1) % 4
    if new[0] != TAB[2][ph2]:
        strip = [TAB[(2 + i) % 7][ph2] for i in range(-6, 0)] + new[0:S - 6]
        return ph2, sum(b << j for j, b in enumerate(strip)), -7
    return ph2, sum(b << j for j, b in enumerate(new[1:])), 0


phases = set(); low = set(); words = set(); n = 0
for ph in range(4):
    for s in range(1 << S):
        for u in (0, 1):
            ph2, s2, d = step(ph, s, u)
            if d < 0:
                n += 1; phases.add((ph, ph2)); low.add(s2 & 255); words.add(s2)
print('R1 re-anchoring edges %d: phase pairs %s; low bytes %s; distinct post-shift words %d' % (
    n, sorted(phases), sorted(low), len(words)))
g = sum(1 << (i - 1) for i in range(1, 8))
print('R2 phase 2, cells 1..7 black: post-shift word %s (inputs 0, 1)' % [step(2, g, u)[1] for u in (0, 1)])
h = json.load(open(sys.argv[1]))['pi']
node = lambda ph, s: ph * (1 << S) + s
for ph, w in ((0, 2258), (1, 5982), (1, 8030)):
    out = []
    for u in (0, 1):
        ph2, s2, d = step(ph, w, u)
        out.append((u, d, h[node(ph2, s2)], h[node(ph, w)] + 44 * d + 7 - h[node(ph2, s2)]))
    print('R3 state (%d, %d): h = %d; (input, drift, h(next), sigma): %s' % (ph, w, h[node(ph, w)], out))
lines = [l for l in open(sys.argv[2]) if l.startswith('ph')]
cyc = []
for l in lines:
    ph = int(l.split()[1]); strip = l.split('strip ')[1].split()[0]
    cyc.append((ph, sum(int(b) << j for j, b in enumerate(strip))))
P = len(cyc); PER = int(sys.argv[3])
allowed = []
for i, (ph, s) in enumerate(cyc):
    nxt = cyc[(i + 1) % P]
    allowed.append({u for u in (0, 1) if step(ph, s, u)[:2] == nxt})
print('R4 node cycle of %d ticks; inputs allowed per tick: %s' % (P, ''.join(
    '*' if len(a) == 2 else str(next(iter(a))) for a in allowed)))
ph0, s0 = cyc[0]
LO = -(P + 8) * PER - 60
cons = {}
for j in range(PER):
    for t in range(P):
        T = P * j + t; x = 14 - 7 * j
        cons.setdefault(max(x + T - 13, 1), []).append((T, x, allowed[t]))
KMAX = max(cons)


def row0(bits):
    r = 0
    for x in range(LO, 1):
        r |= TAB[(2 + x) % 7][ph0] << (x - LO)
    for j in range(S):
        r |= ((s0 >> j) & 1) << (1 + j - LO)
    for i, b in enumerate(bits):
        r |= b << (14 + i - LO)
    return r


def ok(bits):
    need = cons.get(len(bits), [])
    if not need:
        return True
    a = row0(bits); rows = {0: a}
    for T in range(1, max(t for t, _, _ in need) + 1):
        a = (a << 1) ^ (a | (a >> 1)); rows[T] = a
    return all(((rows[T] >> (x - LO)) & 1) in al for T, x, al in need)


best = [0]; nodes = [0]


def dfs(bits):
    nodes[0] += 1; best[0] = max(best[0], len(bits))
    if len(bits) >= KMAX or nodes[0] > 200000:
        return bits if len(bits) >= KMAX else None
    for b in (0, 1):
        if ok(bits + [b]):
            r = dfs(bits + [b])
            if r is not None:
                return r
    return None


r = dfs([])
print('R4 node-cycle realisation, %d period(s): %s; DFS nodes %d; deepest bit %d of %d' % (
    PER, 'REALIZED' if r else ('budget' if nodes[0] > 200000 else 'NOT realizable'), nodes[0], best[0], KMAX))
print('RESET_RETURN_DONE')
