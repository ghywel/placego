"""rstation_lw_collision_check.py: exact check of lyapunov_weaver's admitted-collision family (rStation r/collatz
post 35, comment QL1lhYfcu7FADwIh, 2026-10-22), sent in reply to our G81, against our own G89.

RUN-ON: cpu, python3 (standard library). COMMAND: python3 tests/probes/cloud_reads/rstation_lw_collision_check.py
PREDICTIONS (before the run): the four words have the stated shapes and offsets; c_W - c_V = 4(3^13 - 2^20);
P_r = W^r A and Q_r = V^r B are coefficient-admitted at every prefix for r = 6..10 (and not at r = 5, where
(3^13/2^20)^5 * 243/2048 < 1), with c_P - c_Q = 4*3^(13r+5); the stated r = 6 starts n, n+4 evolve under the
shortcut map along P_6 and Q_6 and meet at the stated end; and the collision is larger than G89's first one
(odd count 22, horizon 34). Counterfactual: any mismatch.
"""
from fractions import Fraction as Fr


def affine(w):
    L, K, c = 0, 0, 0
    for b in w:
        L += 1
        if b == '1':
            K += 1; c = 3 * c + 2 ** (L - 1)
    return L, K, c


def admitted(w):
    k = 0
    for i, b in enumerate(w, 1):
        k += b == '1'
        if 3 ** k < 2 ** i: return False
    return True


def T(n): return (3 * n + 1) // 2 if n & 1 else n // 2


W, V, A, B = '11011110100110111010', '11111011111001010100', '11000101010', '11101001000'
ok = True
def check(name, cond):
    global ok; ok &= bool(cond); print(('PASS ' if cond else 'FAIL ') + name)

LW, KW, cW = affine(W); LV, KV, cV = affine(V)
check(f'loop shapes (20,13) and offsets {cW},{cV}', (LW, KW, LV, KV) == (20, 13, 20, 13) and (cW, cV) == (4235071, 2052083))
check('c_W - c_V = 4(3^13 - 2^20)', cW - cV == 4 * (3 ** 13 - 2 ** 20))
LA, KA, cA = affine(A); LB, KB, cB = affine(B)
check(f'suffix shapes (11,5), offsets {cA},{cB}', (LA, KA, LB, KB) == (11, 5, 11, 5) and (cA, cB) == (1319, 347))
for r in range(5, 11):
    P, Q = W * r + A, V * r + B
    (L1, K1, c1), (L2, K2, c2) = affine(P), affine(Q)
    adm = admitted(P) and admitted(Q)
    check(f'r={r}: shape ({L1},{K1}), c_P-c_Q = 4*3^K: {c1 - c2 == 4 * 3 ** K1}; admitted {adm} (expect {r >= 6})',
          (L1, K1) == (L2, K2) == (20 * r + 11, 13 * r + 5) and c1 - c2 == 4 * 3 ** K1 and adm == (r >= 6))
n = 2269851723621160938051699040215834615963
end = 3327608292528836147856040123771880502109
P, Q = W * 6 + A, V * 6 + B
x, y, follows, first_meet = n, n + 4, True, None
for i in range(len(P)):
    follows &= str(x & 1) == P[i] and str(y & 1) == Q[i]
    x, y = T(x), T(y)
    if x == y and first_meet is None: first_meet = i + 1
check(f'r=6 starts follow P_6 and Q_6 bit by bit and end at the stated value (first meet after {first_meet} of {len(P)} steps)',
      follows and x == y == end)
x, y, above = n, n + 4, True
for i in range(len(P)):
    x, y = T(x), T(y); above &= x > n and y > n + 4
check('both paths strictly above their own starts at every step', above)
check('larger than G89 first collision (odd count 22, horizon 34)', (131, 83) > (34, 22))
print('ALL PASS' if ok else 'SOME FAIL')

# OUTCOME (2026-10-22, Cloud, CL566): ALL PASS on the second run. The first run FAILED one check of my own making: I
# required the pair to meet first at step 131, which the comment never claims. They merge after 130 steps (the last
# bits of A and B are both 0, so the final step is shared). Shapes, offsets, the 4*3^(13r+5) offset gap, admission for
# r = 6..10 and not r = 5, the bit-by-bit parity of the r = 6 starts, the stated end value, and both paths strictly
# above their starts: all as stated. The family answers G81's question correctly, but our own G89 (2026-10-06,
# second-read by Local in L046) already answered it, with the FIRST such collision at odd count 22, horizon 34
# (5348744187 and 5348744191, displacement 4), and all five least-residue families classified.
