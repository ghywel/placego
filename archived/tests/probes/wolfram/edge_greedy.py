#!/usr/bin/env python3
"""Cloud, 2026-10-30 (CL652, Block 6): extend a plateau by repeated single reversals. From seed 0x415459 with wheel 34
reversed (CL650's fourteen-wheel chain at E = 15), each round reverses the one further wheel (candidates k from 32 to the
plateau's end + 1) that most lengthens the zero-run of block exponents starting at n = 34; up to 12 rounds, E_n to 72.
Needs the edge_lift binary (edge_lift.c) in the current directory. The recorded run (edge_greedy.out) reached round 9,
34 wheels at one period, before its 30-minute cap; edge_greedy_chain.out is edge_break on the final seed to n = 70."""
import subprocess, re
def E_of(seed, N=72):
    out = subprocess.run(['./edge_lift', hex(seed), str(N)], capture_output=True, text=True).stdout
    return [int(x) for x in re.search(r'E_n: (.*)', out).group(1).split()]
def run_from(E, start):
    d = [E[i] - E[i - 1] for i in range(1, len(E))]
    k = start - 1
    if k >= len(d) or d[k] != 0: return 0
    r = 0
    while k < len(d) and d[k] == 0: r += 1; k += 1
    return r
s = 0x415459 ^ (1 << 34); start = 34
E = E_of(s); L = run_from(E, start); print("round 0: plateau", L, "E at start", E[start - 1], "E_72", E[-1])
for rnd in range(1, 13):
    best = (L, None)
    for k in range(32, start + L + 2):
        L2 = run_from(E_of(s ^ (1 << k)), start)
        if L2 > best[0]: best = (L2, k)
    if best[1] is None: print("round", rnd, ": no single reversal extends; stop"); break
    L, k = best; s ^= (1 << k)
    print(f"round {rnd}: reverse wheel {k} -> plateau {L} (zero letters from n = {start}), seed {hex(s)}")
    if start + L - 1 >= 71: print("reached the window end"); break
