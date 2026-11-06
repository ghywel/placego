#!/usr/bin/env python3
"""Block 3 control against wrong removal. A real row that never enters T(W) must end inside core(W). Rows: the 57 of
BN-13 that no 30-column class holds (56 deep family members and lock-7b), and R = 74 (lock-7); none enters the gate. For each dump core_W_MODE.bin,
every window of the row's tail is either in core(W) or the row has entered T(W); a tail window in neither is a failure.
Usage: tails.py ROWS_FILE REF_DIR TARGETS DUMP_DIR MODE [T]
"""
import glob, re, sys
import numpy as np
rows_file, refdir, targets, dumps, mode = sys.argv[1:6]
T = int(sys.argv[6]) if len(sys.argv) > 6 else 6000
sys.path.insert(0, refdir); import ref
tg = {}
for line in open(targets):
    if line[0] != '#':
        p = line.split(); tg[p[0]] = p[1:]
wall = set()
w = tg['wall'][1:]
for i in range(0, len(w), 2): wall.add((int(w[i]), int(w[i + 1])))
L7 = set(map(int, tg['lock7'][2:])); S7 = set(map(int, tg['sevenlock'][2:])); L7B = set(map(int, tg['lock7b'][2:]))
ETH = ['0011', '0110', '1101', '0101', '0011', '0001', '0001']
pat = {q: sum(int(ETH[(3 + p) % 7][q]) << (p - 1) for p in range(1, 63)) for q in (0, 2)}
lock, lockw = (L7, 30) if mode == 'xx' else (S7, 32)
def in_family(x, W):
    for q in (0, 2):
        for k in range(6, W - 12, 7):
            if (x ^ pat[q]) & ((1 << k) - 1): break
            if (q, (x >> k) & 0x1FFF) in wall: return True
    return False
def in_lock(x, W):
    return (W >= lockw and (x & ((1 << lockw) - 1)) in lock) or (W >= 45 and (x & ((1 << 45) - 1)) in L7B)
Rs = [int(x) for x in open(rows_file).read().split()]
tails = {}
for R in Rs:
    rows = ref.drv(ref.alt_col, R, T + 30)
    tails[R] = [rows[t] for t in range(T - (T % 2) + 1, T + 28, 2)]
bad = 0
paths = sorted(glob.glob('%s/core_*_%s.bin' % (dumps, mode)), key=lambda s: int(re.search(r'core_(\d+)_', s).group(1)))
assert paths, 'no core dumps: no control was checked'
for p in paths:
    W = int(re.search(r'core_(\d+)_', p).group(1))
    core = np.fromfile(p, dtype=np.uint64)
    mask = (1 << W) - 1
    inside = entered = 0
    for R, tail in tails.items():
        ws = np.array([x & mask for x in tail], dtype=np.uint64)
        hit = core[np.minimum(np.searchsorted(core, ws), len(core) - 1)] == ws if len(core) else np.zeros(len(ws), dtype=bool)
        if hit.all(): inside += 1
        elif any(in_family(x & mask, W) or in_lock(x & mask, W) for x in tail): entered += 1
        else: bad += 1; print('  FAIL W', W, 'R', R)
    print('W', W, 'rows with the whole tail in core', inside, 'rows in T(W) or the gate', entered, flush=True)
print('PASS' if not bad else 'FAIL %d' % bad)
sys.exit(1 if bad else 0)
