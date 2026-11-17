#!/usr/bin/env python3
"""left_map.py NMAX: the left edge map T(L)_j = L_(j-2) XOR (L_(j-1) OR L_j) with L_(-1) = L_(-2) = 0 on left-frame rows of n cells
(the first n diagonals from the left edge, an autonomous system, 8.31): preimage counts, bit loss per step, the 4-state transducer table,
and the mirror with Phi. Cloud, Block 26 (M1 algebraic)."""
import sys, numpy as np
from collections import Counter
NMAX = int(sys.argv[1])
def T(L):
    n = len(L); return tuple((L[j-2] if j >= 2 else 0) ^ ((L[j-1] if j >= 1 else 0) | L[j]) for j in range(n))
def Phi(w):   # the right edge map in the same orientation: w_j' = w_j XOR (w_(j-1) OR w_(j-2)), w_(-1) = 1 (the edge), w_(-2) = 0
    n = len(w); return tuple(w[j] ^ ((w[j-1] if j >= 1 else 1) | (w[j-2] if j >= 2 else 0)) for j in range(n))
from itertools import product
for n in (6, 8, 10, 12, NMAX):
    rows = list(product((0, 1), repeat=n)); img = Counter(T(L) for L in rows); imgP = Counter(Phi(w) for w in rows)
    # prediction P-O3: preimage count of a row M = 2^(number of j in [1, n-1] with M_(j-1)... test: count vs black cells of the preimage's shallower cells
    # exact: the number of preimages of M equals the number of L with T(L) = M; compare with 2^(#black among L_0..L_(n-2)) for one preimage L
    ok = 0; tot = 0
    for M, c in img.items():
        pre = [L for L in rows if T(L) == M]
        L = pre[0]; b = sum(L[j] for j in range(0, n - 1)); tot += 1; ok += (c == 2 ** b)
    print(f"n={n}: T has {len(img)} images of {2**n} rows (Phi: {len(imgP)}, bijective={len(imgP)==2**n}); preimage counts {sorted(set(img.values()))[:8]}; "
          f"P-O3 (count = 2^(black cells among L_0..L_(n-2) of a preimage)) holds for {ok}/{tot} images; mean bits lost per step {np.log2(2**n/len(img)):.3f}")
# the transducer: state = (L_(j-1), L_(j-2)); input L_j; output L_(j-2) XOR (L_(j-1) OR L_j); next state = (L_j, L_(j-1))
print("left map T as a Mealy transducer (state (L_(j-1), L_(j-2)); input/output):")
for st in product((0, 1), repeat=2):
    print(f"  state {st}: " + ", ".join(f"in {x} -> out {st[1] ^ (st[0] | x)}, next {(x, st[0])}" for x in (0, 1)) + ("   (not invertible: both inputs give the same output)" if st[0] == 1 else ""))
print("right map Phi as a transducer (state (w_(j-1), w_(j-2)); output w_j XOR (w_(j-1) OR w_(j-2)) = input XOR f(state)): invertible at every state")
print("LEFT_MAP_DONE")
