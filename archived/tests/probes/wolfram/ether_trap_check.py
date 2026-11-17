#!/usr/bin/env python3
"""ether_trap_check.py T KIT_RULE30ETHER_LEAN: Lowry's ether wall trap (kit Rule30Ether) replayed: parse etherTable and the 109 wallStates from the Lean
source, replay wallOK (head condition and closure under every right input), map each inserted-edge alignment onto the kit's ether
labelling, and find the first time the configuration is in the trap (ether columns ending in a B3, then a wall state). Cloud, Block 23."""
import sys, re, numpy as np
T = int(sys.argv[1])
src = open(sys.argv[2]).read()   # path to the kit's lean/Ruliology/CellularAutomata/Rule30Ether.lean (kit main f1cb20be)
tab = src[src.index('def etherTable'):src.index('def ether (j')]
etherTable = [[1 if v == 'true' else 0 for v in re.findall(r'true|false', row)] for row in re.findall(r'\[((?:true|false)(?:, (?:true|false))*)\]', tab)]
assert len(etherTable) == 7 and all(len(r) == 4 for r in etherTable)
ws = src[src.index('def wallStates'):src.index('/-- Closure under every right input')]
wallStates = set()
for m in re.finditer(r'\((\d), \[([truefals, ]+)\]\)', ws):
    wallStates.add((int(m.group(1)), tuple(1 if v == 'true' else 0 for v in m.group(2).split(', '))))
print(f"parsed etherTable {etherTable} and {len(wallStates)} wall states")
def ether(j, phi): return etherTable[j % 7][phi % 4]
def rule(a, b, c): return a ^ (b | c)
def lin3(cells):   # cells = [left] + strip + [right]; returns the strip's next values
    return tuple(rule(cells[i-1], cells[i], cells[i+1]) for i in range(1, len(cells) - 1))
# replay wallOK
ok = True
for (phi, s) in wallStates:
    if not (len(s) == 13 and phi < 4): ok = False
    if ether(2, phi) == 0 and s[0] != ether(3, phi): ok = False; print("head condition fails", phi, s)
    for x in (0, 1):
        nxt = ((phi + 1) % 4, lin3((ether(2, phi),) + s + (x,)))
        if nxt not in wallStates: ok = False; print("closure fails", phi, s, x)
print("wallOK replayed:", ok)
# the ether is a rule-30 orbit (check): column j at phase phi+1 = rule(ether(j-1,phi), ether(j,phi), ether(j+1,phi))
assert all(ether(j, p + 1) == rule(ether(j - 1, p), ether(j, p), ether(j + 1, p)) for j in range(7) for p in range(4)), "ether_rule"
# my lab ether from the ring orbit, and its map onto the kit's labelling
y = np.array([1,0,0,0,0,0,0], dtype=np.uint8); N = 7
def cst(s): return s ^ (np.roll(s, 1) | np.roll(s, 2))
orb = [y.copy()]; cur = cst(y)
while not np.array_equal(cur, y): orb.append(cur.copy()); cur = cst(cur)
orb = np.array(orb); q = len(orb)
def E(x, t, r, s): return int(orb[(t + s) % q][((t - x) + r) % N])
def step(rw):
    n = np.zeros_like(rw); n[1:-1] = rw[:-2] ^ (rw[1:-1] | rw[2:]); return n
entries = {}; nomatch = 0
WL = 2*T + 100; WR = T + 60; W = WL + WR; c = WL
for r in range(N):
    for s in range(q):
        # find (c0, c1): E(x, t) = ether(x + c0, t + c1)
        maps = [(c0, c1) for c0 in range(7) for c1 in range(4) if all(E(x, t, r, s) == ether(x + c0, t + c1) for x in range(-7, 8) for t in range(0, 8))]
        if not maps: nomatch += 1; continue
        c0, c1 = maps[0]
        bg = np.array([E(x, 0, r, s) for x in range(-WL, WR)], dtype=np.uint8); pert = bg.copy(); pert[c] = 1; pert[c+1:] = 0
        b = pert.copy(); found = None
        for t in range(T + 1):
            # leftmost mismatch
            Erow = np.array([E(x, t, r, s) for x in range(-40, 60)], dtype=np.uint8); seg = b[c-40:c+60]
            d = np.flatnonzero(seg ^ Erow); xmin = int(d.min()) - 40
            # candidate B3 columns x_B < xmin with x_B + c0 = 2 mod 7, everything <= x_B ether (true by xmin), strip x_B+1..x_B+13 a wall state
            for xB in range(xmin - 1, xmin - 8, -1):
                if (xB + c0) % 7 != 2: continue
                strip = tuple(int(v) for v in b[c + xB + 1: c + xB + 14]); phi = (t + c1) % 4
                if (phi, strip) in wallStates: found = (t, xB, xmin); break
            if found: break
            if t < T: b = step(b)
        entries[(r, s)] = found
ent = [v for v in entries.values() if v]
print(f"alignments mapped onto the kit's ether: {196 - nomatch} of 196; entered the trap by T={T}: {len(ent)} of {len(entries)}")
if ent:
    t1s = [v[0] for v in ent]; print(f"  entry times: min {min(t1s)}, median {sorted(t1s)[len(t1s)//2]}, max {max(t1s)}; (x_B, x_min at entry) examples: {[(v[1], v[2]) for v in ent[:6]]}")
miss = [k for k, v in entries.items() if not v]
print("  alignments not entering:", miss[:10])
print("ETHER_TRAP_DONE")
