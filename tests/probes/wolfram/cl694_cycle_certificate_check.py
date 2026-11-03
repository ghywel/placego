#!/usr/bin/env python3
"""GC2533 fixed replay of Cloud CL694's existing 12000x16 cycle certificate.
No seed/threshold search or extended horizon. Input: CL694_TABLE, exact pinned bytes.
One thread, no children/network. Output contains checks/digests only.
"""
import hashlib
import json
import os
from pathlib import Path
import resource
import time

start = time.monotonic()
TABLE_SHA = '3d2aea2104aa1e7eb0a02d2fc61729940c22d4cc1fab8eeb6495279bf50ead74'
K, P, T = 12000, 16, 32768

def guard():
    used = resource.getrusage(resource.RUSAGE_SELF)
    if used.ru_utime + used.ru_stime > 5 or time.monotonic() - start > 15:
        raise RuntimeError('fixed internal CPU/wall stop')

raw = Path(os.environ['CL694_TABLE']).read_bytes()
assert hashlib.sha256(raw).hexdigest() == TABLE_SHA
lines = raw.decode('ascii').splitlines()
words = [s for s in lines if not s.startswith('#')]
assert len(words) == K and all(len(s) == P and set(s) <= {'0', '1'} for s in words)
cycles = [[int(b) for b in s] for s in words]

def truth(a, b, c):
    return (30 >> (4*a + 2*b + c)) & 1

def phi(v):
    return (v << 2) ^ ((v << 1) | v)

# Independent physical coordinates/truth-table oracle, no use of phi in update.
lo, hi = -66, 66
row = [int(x == 0) for x in range(lo, hi + 1)]
v, mutant = 1, 1
cells = bad_mutant = 0
for t in range(65):
    for i, x in enumerate(range(lo, hi + 1)):
        k = x + t
        assert row[i] == ((v >> k) & 1 if k >= 0 else 0)
        cells += 1
    bad_mutant += mutant != v
    nxt = [0] * len(row)
    for i in range(1, len(row) - 1):
        nxt[i] = truth(row[i-1], row[i], row[i+1])
    row = nxt
    v = phi(v)
    mutant = (mutant << 2) ^ ((mutant << 1) ^ mutant)
assert bad_mutant > 0

def cycle_bad(cs):
    bad = 0
    for k in range(K):
        for r in range(P):
            a = cs[k-2][r] if k >= 2 else 0
            b = cs[k-1][r] if k >= 1 else 0
            bad += cs[k][(r+1) % P] != truth(a, b, cs[k][r])
        if k % 256 == 0:
            guard()
    return bad

assert cycle_bad(cycles) == 0
mut = [c[:] for c in cycles]
mut[0][0] ^= 1
mutant_cycle_failures = cycle_bad(mut)
assert mutant_cycle_failures > 0
# Known autonomous left-frame map; exactly the retained certificate's entry time.
mask = (1 << K) - 1
v = 1
for t in range(T):
    v = phi(v) & mask
    if t % 256 == 0:
        guard()
expected = sum(cycles[k][T % P] << k for k in range(K))
assert v == expected
pin = hashlib.sha256(v.to_bytes((K+7)//8, 'little')).hexdigest()
assert pin == '4b7bca7671285a480ad964c092b7793797d452421580f5ae068da89b68e749ff'
assert v != sum(mut[k][T % P] << k for k in range(K))
guard()
print(json.dumps({'status':'PASS','table_sha256':TABLE_SHA,'entry_T':T,'prefix_K':K,
    'period':P,'literal_physical_cells':cells,'wrong_OR_mutant_ticks_detected':bad_mutant,
    'literal_cycle_constraints':K*P,'mutated_cycle_constraints_failed':mutant_cycle_failures,
    'entry_exact':True,'entry_pin':pin,'mutated_entry_rejected':True,
    'cpu_self_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
    'wall_self_seconds':time.monotonic()-start},sort_keys=True))
