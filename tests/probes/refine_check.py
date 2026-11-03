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
if '--features' in sys.argv:
    # L1342: features of wholly bad (all refinements bad) against resolved (none bad) B_W states, P1024 classes
    import runpy, os
    g = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'upward_rigid.py'), run_name='lib')
    p, cols, _ = g['phases']()['P1024']; col0 = cols[0]
    Bidx = np.flatnonzero(B1)
    whole = Bidx[stay == 4]; res = Bidx[stay == 0]
    def feats(states):
        cl = states >> W; w = states & ((1 << W) - 1)
        pc = np.array([bin(int(x)).count('1') for x in w])
        run = np.array([next((j for j in range(W) if not (int(x) >> j) & 1), W) for x in w])
        pair = (w & 1) * 2 + ((w >> 1) & 1)
        blocked = np.array([(col0 >> ((int(c) + 195) % p)) & 1 for c in cl])
        return pc, run, pair, blocked
    for nm, st in (('wholly bad', whole), ('resolved', res)):
        pc, run, pair, bl = feats(st)
        rule = (pc >= 6) | (run >= 4)
        print('   %s (%d states): mismatches in window mean %.2f; run next to the front mean %.2f; (D_(R-1), D_(R-2)) '
              'counts 00/01/10/11 %s; blocked classes %.1f%%; rule (>= 6 mismatches or run >= 4) covers %.1f%%' % (
                  nm, len(st), pc.mean(), run.mean(), np.bincount(pair, minlength=4).tolist(), 100.0 * bl.mean(),
                  100.0 * rule.mean()), flush=True)
if '--features' in sys.argv:
    cnt = np.bincount(res >> W, minlength=len(SE1) >> W)
    srt = np.sort(cnt)[::-1]; tot = srt.sum(); k10 = max(1, len(srt) // 10)
    wb = np.bincount(whole >> W, minlength=len(SE1) >> W); bb = np.bincount(Bidx >> W, minlength=len(SE1) >> W)
    print('   resolved states by class: share in the top 10%% of classes %.1f%%; classes with any resolved state %d of %d; '
          'classes whose bad states are all wholly bad %d' % (100.0 * srt[:k10].sum() / tot, int((cnt > 0).sum()), len(cnt),
          int(((bb > 0) & (wb == bb)).sum())), flush=True)
print('REFINE_CHECK_DONE')
