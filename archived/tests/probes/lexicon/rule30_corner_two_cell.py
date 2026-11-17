"""GC1177: extremal P child prefix is a crop of the two-cell orbit.

Record searched: right.edge/two.cell ->2 hits2files;
checkerboard/conjug ->8 hits6files; moving/front/period ->13 hits11files.
GC755 and G249 read: their right-frame recurrence is reused, not new.
GC1176, GC1174, GC1169 and the three-shape phase convention read.

PREDICTIONS BEFORE execution, 2026-10-13:
 For named r=1,2,3,9,13 and both child phases p, let d=4r-p,
 a=2r+1-p, N=2r+1. A phase-1 parent alternating before N with
 K=9 black cells from N, followed by any tested three-bit extension,
 agrees after a updates through J=K+p-1 with the ordinary seed11
 row at T=2r-p, cropped left of X=2r-2. This is a representation
 control, not a horizon, language-membership or record census.
 Independent: full-line literal Rule30 versus the wall-driven update;
 the hand proof uses the closed right-diagonal recurrence.
 CF: the whole two-cell configuration has the desired child centre
 phase. At p1 its centre is actually white; hence the claim must fail.
 Unexpected: GC1169's real B100101 child agrees with the r1/p1 crop
 through its white band's end at depth5, then differs at depth6;
 never extrapolate a finite-core match to an infinite exterior.
 No right cut, solver, further front-diagonal or survival-time search.
"""
from itertools import product
from rule30_prefix_realization import inverse, rule


def ordinary(ticks):
    row = {-1: 1, 0: 1}
    for t in range(ticks):
        row = {i: rule(row.get(i-1,0), row.get(i,0), row.get(i+1,0))
               for i in range(-2-t, 2+t)}
    return row


def forward(row, phase):
    return [rule(row[j+1], row[j], phase if j == 0 else row[j-1])
            for j in range(len(row)-1)]


def main():
    count = 0
    for r in (1,2,3,9,13):
        for p in (0,1):
            a, n, k = 2*r+1-p, 2*r+1, 9
            out = ordinary(2*r-p)
            x, jmax = 2*r-2, k+p-1
            cropped = [out.get(x-j,0) for j in range(1,jmax+1)]
            for ext in product((0,1),repeat=3):
                parent = [j%2 for j in range(1,n)] + [1]*k + list(ext)
                for t in range(a):
                    parent = forward(parent,(1+t)%2)
                assert parent[:jmax] == cropped
                count += 1
            assert out.get(x,0) == 0  # p1 refutes whole-seed identification
            assert min(i for i,b in out.items() if b) == -1-(2*r-p)
    actual = inverse(list(map(int,'100101')),1)
    out = ordinary(1)
    crop = [out.get(-j,0) for j in range(1,7)]
    assert actual[:5] == crop[:5]
    assert actual[5] != crop[5]
    print('named corner prefix controls',count,'PASS; both centre colours white')
    print('actual B100101 matches crop through depth5, differs at6: PASS')


if __name__ == '__main__':
    main()
