#!/usr/bin/env python3
"""L1294 T21 (Local, 2026-11-02): white-pair counts Z(u, v) = |NOT u AND NOT v| along the walls of the light-speed
cores at p = 8 and 16 (from lightspeed_core.c outputs). Predictions in reports/rule30-genealogy.md section 29.9.
Run: python3 tests/probes/lightspeed_order.py CORE8.out CORE16.out
For each wall state, follows every path forward to the cycle it enters and backward to the cycle it leaves, and checks
whether Z is non-increasing along it. Reports Z per phase and the walls where Z rises.
"""
import sys
from collections import defaultdict


def analyse(path, p):
    M = (1 << p) - 1
    A = sum(1 << t for t in range(1, p, 2))
    pc = lambda x: bin(x).count('1')

    def integ(d):
        y, s = d, 1
        while s < p:
            y ^= (y << s) & M
            s <<= 1
        return (y << 1) & M

    core = set()
    for line in open(path):
        if '(u, v)' in line:
            a = line.split('(u, v) = (')[1].split(')')[0].split(', ')
            core.add((int(a[0], 16), int(a[1], 16)))
    succ = {s: [t for t in ((s[1], integ(s[0] | s[1])), (s[1], integ(s[0] | s[1]) ^ M)) if t in core] for s in core}
    pred = defaultdict(list)
    for s in core:
        for t in succ[s]:
            pred[t].append(s)
    Z = lambda s: pc(~(s[0] | s[1]) & M)
    # states on cycles: those that can return to themselves
    def on_cycle(s):
        seen, st = set(), list(succ[s])
        while st:
            x = st.pop()
            if x == s:
                return True
            if x not in seen:
                seen.add(x); st.extend(succ[x])
        return False
    cyc = {s for s in core if on_cycle(s)}
    # phases by Z values
    comp = {}
    for s in cyc:
        if s in comp:
            continue
        group, st = {s}, [s]
        while st:
            x = st.pop()
            for y in succ[x] + pred[x]:
                if y in cyc and y not in group and on_cycle(y) and any(y == z for z in succ[x] + pred[x]):
                    group.add(y); st.append(y)
        for x in group:
            comp[x] = min(group)
    phases = defaultdict(set)
    for s, c in comp.items():
        phases[c].add(s)
    print(f'p = {p}: core {len(core)}, phase states {len(cyc)}')
    for c, g in sorted(phases.items(), key=lambda kv: len(kv[1])):
        print(f'   phase of {len(g):4d} states: Z values {sorted({Z(s) for s in g})}')
    # walls: every maximal path from a cycle state, through non-cycle states, into a cycle state
    rises, walls = 0, 0
    starts = [(s, t) for s in cyc for t in succ[s] if t not in cyc]
    for s, t in starts:
        stack = [[s, t]]
        while stack:
            path = stack.pop()
            x = path[-1]
            for y in succ[x]:
                if y in cyc:
                    walls += 1
                    zs = [Z(q) for q in path + [y]]
                    if any(zs[i + 1] > zs[i] for i in range(len(zs) - 1)):
                        rises += 1
                        if rises <= 3:
                            print(f'   wall with Z rising: Z along it {zs}')
                else:
                    stack.append(path + [y])
    print(f'   walls (paths cycle -> cycle through the wall) {walls}; with Z rising somewhere {rises}')


analyse(sys.argv[1], 8)
analyse(sys.argv[2], 16)
print('LIGHTSPEED_ORDER_DONE')
