#!/usr/bin/env python3
"""L1340 T51 (Local, 2026-11-02): the refinement lemma between the W and W + 2 window automata of P1024.
reports/rule30-genealogy.md section 55 (predictions written first). Run: python3 tests/probes/refine_check.py MASKS_W.npz MASKS_W2.npz

A (W + 2)-state (c << (W + 2)) | w' projects to the W-state (c << W) | (w' & (2^W - 1)) (the window's first W cells,
D_(R-1) .. D_(R-W)). Reported: refinements of A_W and of S_E_W outside A_(W+2) and S_E_(W+2); B_(W+2) states whose
projection is not in B_W; and, for each B_W state, how many of its 4 refinements stay in B_(W+2).
"""
import sys
import numpy as np
m1 = np.load(sys.argv[1]); m2 = np.load(sys.argv[2])
W = int(m1['W']); W2 = int(m2['W']); assert W2 == W + 2
SE1, A1, B1 = m1['SE'], m1['A'], m1['B']; SE2, A2, B2 = m2['SE'], m2['A'], m2['B']
N2 = len(SE2); idx = np.arange(N2, dtype=np.int64)
proj = ((idx >> W2) << W) | (idx & ((1 << W) - 1))
good2 = SE2 | A2
print('W = %d -> %d: states %d -> %d' % (W, W2, len(SE1), N2))
print('   refinements of A_W outside A_W2 + S_E_W2: %d of %d' % (int((A1[proj] & ~good2).sum()), int(A1[proj].sum())))
print('   refinements of S_E_W outside A_W2 + S_E_W2: %d of %d (in B_W2: %d)' % (
    int((SE1[proj] & ~good2).sum()), int(SE1[proj].sum()), int((SE1[proj] & B2).sum())))
print('   B_W2 states whose projection is not in B_W: %d of %d' % (int((B2 & ~B1[proj]).sum()), int(B2.sum())))
stay = np.bincount(proj[B2], minlength=len(SE1))[B1]
hist = np.bincount(stay, minlength=5)
print('   refinements of each B_W state staying in B_W2 (0..4): %s; mean %.3f; B share %.4f -> %.4f' % (
    hist.tolist(), float(stay.mean()), B1.mean(), B2.mean()))
print('REFINE_CHECK_DONE')
