#!/usr/bin/env python3
"""Stream-side pull, step 1 (Local, 8 November 2026): the finite hard-core class against all rows.
By S-04's chart a constrained row's endpoint stream is hard-core up to its death exactly when its free bits up to death
have no 00. Write D(w) for the latest death among starts of exact width w and D_N(w) for the latest death among those
whose free bits f(0..N-1) have no 00 (class N). Q01 says every row dies; SEP (= QN) says only the class-N part of that.
Usage: hardcore_death.py WMIN WMAX. Exhaustive (top bit set, depth 1 black).
Prediction, before the run: D_N(w) < D(w) at most widths (the champions contain 00), P = 0.65; D_N grows with w at a
comparable rate, D_N(w) / D(w) >= 0.7 at every w >= 16, P = 0.6.
Counterfactual: D_N stays bounded or grows clearly slower: the hard-core side is quantitatively easier in finite form,
and a bound for it (an RW-type horizon) is the natural target."""
import sys
def F(y): return (y >> 1) ^ (y | (y << 1))
def run(y):
    f = []; t = 0
    while True:
        if y & 1 == 0: return t, f
        y = F(y); t += 1; f.append(y & 1); y = F(y); t += 1
wmin, wmax = int(sys.argv[1]), int(sys.argv[2])
for w in range(wmin, wmax + 1):
    D = DN = DnotN = 0; nN = 0; argN = None
    for y in range((1 << (w - 1)) | 1, 1 << w, 2):
        d, f = run(y)
        has00 = any(f[s] == 0 and f[s + 1] == 0 for s in range(len(f) - 1))
        if d > D: D = d
        if has00:
            if d > DnotN: DnotN = d
        else:
            nN += 1
            if d > DN: DN, argN = d, y
    print(f'w {w}: D {D}, D_N {DN} (witness {argN}), D_notN {DnotN}, class-N starts {nN} of {1 << (w - 2)}, ratio {DN / D:.3f}', flush=True)
