#!/usr/bin/env python3
"""L1676 (Local, 16 November 2026): the complete mass ladder of the Q01Gap language to popcount 90, with its roots.

For each M: H_M = the least H with NoMass M H (kit Rule30ZeroCoastBridge), and Box_M = the accepted H_M-bit prefixes
of popcount exactly M + 1 (at M = 37 these are the eight c37Roots of R30-20261115-fdf6a3).  A seed of popcount
<= M + 1 that survives to H_M restricts to a root and has no further bits, so
    H_(M+1) = 1 + max over Box_M of the root's survival as a finite seed    (H_(M+1) = H_M if Box_M is empty).
This file dumps the ladder and checks that identity at every rung with a literal simulation of the kit's acceptor.
It reuses the frozen probe of L1675 (local_q01gap_mass_table.py) for the recursion and the acceptor.
"""
import sys
import time

sys.path.insert(0, __file__.rsplit('/', 1)[0])
import local_q01gap_mass_table as MT   # noqa: E402

step_depth = MT.step_depth
KIDS = MT.KIDS
T0 = time.time()


def ladder_dfs(M, K, keep=512):
    """Per depth H: the least popcount, the exact number of prefixes attaining it, and those prefixes (up to keep)."""
    mn, cnt, arg = {}, {}, {}

    def note(H, p, val):
        m = mn.get(H)
        if m is None or p < m:
            mn[H], cnt[H], arg[H] = p, 1, [val]
        elif p == m:
            cnt[H] += 1
            if len(arg[H]) < keep:
                arg[H].append(val)
    stack = [MT.root()]
    nodes = 0
    while stack:
        s, age, Dn, Dn1, n, R, pop = stack.pop()
        r1, D1 = step_depth(Dn, Dn1, n, 1)
        base = pop + r1
        for g, age2 in KIDS[age]:
            nodes += 1
            r2, D2 = step_depth(D1, Dn, n + 1, 1 - g)
            p_odd = base + r2
            if p_odd > M:
                continue
            R2 = R | (r1 << n) | (r2 << (n + 1))
            note(n + 2, p_odd, R2)
            chk, _ = step_depth(D2, D1, n + 2, 1)
            p_even = p_odd + chk
            if p_even > M:
                continue
            note(n + 3, p_even, R2 | (chk << (n + 2)))
            if s + 1 < K:
                stack.append((s + 1, age2, D2, D1, n + 2, R2, p_odd))
    return mn, cnt, arg, nodes


def main():
    MMAX = 90
    mn, cnt, arg, nodes = ladder_dfs(MMAX, 260)
    Hlast = max(mn)
    print('L1676 mass ladder of the Q01Gap language (kit frame). %d nodes, %.0f s. mu(H) exact for 3 <= H <= %d.'
          % (nodes, time.time() - T0, Hlast))
    hor = {}
    for M in range(0, MMAX + 1):
        hs = [H for H in range(3, Hlast + 1) if mn[H] > M]
        hor[M] = hs[0] if hs else Hlast + 1
    ok_chain, ok_kit = True, True
    print('M : H_M (least H with NoMass M H), number of roots (prefixes of popcount M + 1 surviving to H_M), '
          'longest survival of a root')
    lines = []
    for M in range(0, MMAX):
        H = hor[M]
        if H <= Hlast and mn[H] == M + 1:
            roots = arg[H]
            n_roots = cnt[H]
            lives = [MT.kit_survive_len(z, 2000) for z in roots]
            nxt = 1 + max(lives)
            if n_roots <= len(roots) and nxt != hor[M + 1]:
                ok_chain = False
            if any(z.bit_count() != M + 1 or MT.kit_survive_len(z, H) != H for z in roots):
                ok_chain = False
        else:
            roots, n_roots, lives = [], 0, []
            if hor[M + 1] != H:
                ok_chain = False
        print('%2d : %3d  %4d  %s' % (M, H, n_roots, max(lives) if lives else '-'))
        lines.append((M, H, n_roots, roots))
    print('%2d : %3d' % (MMAX, hor[MMAX]))
    box37 = dict((M, r) for M, H, c, r in lines)[37]
    ok_kit = hor[37] == 102 and hor[38] == 111 and set(box37) == set(MT.C37ROOTS)
    ok_run15 = [hor[M] for M in (50, 60, 70, 80, 90)] == [148, 182, 212, 244, 278]
    print('chain identity H_(M+1) = 1 + longest root survival at every rung (literal kit acceptor): %s' % ok_chain)
    print('kit rung: H_37 = 102, H_38 = 111, roots at M = 37 equal c37Roots: %s' % ok_kit)
    print('run 15 horizons for M = 50, 60, 70, 80, 90 reproduced: %s' % ok_run15)
    print('roots (decimal), for every rung with at most 16 roots:')
    for M, H, c, roots in lines:
        if 0 < c <= 16 and M >= 30:
            print('M = %d, H = %d: %s' % (M, H, ' '.join(str(z) for z in sorted(roots))))
    print('done in %.0f s' % (time.time() - T0))


if __name__ == '__main__':
    main()
