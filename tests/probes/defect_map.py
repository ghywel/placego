#!/usr/bin/env python3
"""L1294 T14 (Local, 2026-11-02): the defect map psi = Phi o c by cycle lifting, an independent check of the
reduction in reports/rule30-genealogy.md section 29.2. Predictions in section 29.3, written first.
Run: python3 tests/probes/defect_map.py   (seconds)

Phi(z) = z ^ ((z<<1) | (z<<2) | 3) and c(z) = z ^ ((z<<1) | (z<<2)) on Z_2, computed mod 2^n.
For q = 1, 2, 4, ..., 32: start from the single cycle at level 0 and lift. A cycle at level n with representative r and
length L (L | q) splits into two cycles of length L at level n + 1 if psi^L(r) = r mod 2^(n+1), else doubles to 2L.
Cycles of length not dividing q are dropped. F_q(n) = sum of the kept lengths at level n = #{z mod 2^n : psi^q z = z}.
"""
def phi(z, m):
    return (z ^ ((z << 1) | (z << 2) | 3)) & m


def cmap(z, m):
    return (z ^ ((z << 1) | (z << 2))) & m


def psi_ac(z, m):
    return phi(cmap(z, m), m)


def psi_ca(z, m):
    return cmap(phi(z, m), m)


def census(f, q):
    cycles = [(0, 1)]                      # (representative, length) at level 0
    n, F = 0, []
    while cycles:
        F.append(sum(L for _, L in cycles))
        m = (1 << (n + 1)) - 1
        nxt = []
        for r, L in cycles:
            y = r
            for _ in range(L):
                y = f(y, m)
            if y == r:                     # splits: both lifts are cycles of length L
                nxt.append((r, L)); nxt.append((r | (1 << n), L))
            elif 2 * L <= q:               # doubles
                nxt.append((r, 2 * L))
        cycles, n = nxt, n + 1
    return F


for name, f in (('a o c', psi_ac), ('c o a', psi_ca)):
    for q in (1, 2, 4, 8, 16, 32):
        F = census(f, q)
        print(f'{name}: q = {q:2d}: sum F = {sum(F):6d}, last level with F > 0 = {len(F) - 1:3d}, F(0..8) = {F[:9]}')
print('DEFECT_MAP_DONE')
