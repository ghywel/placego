"""GC1174: canonical-parent checkerboard limits zero inheritance.

Record searched: canonical/ancestor ->34 hits9files; inherited/checker
->2 hits2files; inheritance/half ->no hit. G122/123 (whole-row finite
past tails), GC1170 and8.82 read. This is clamped-left canonical ancestry,
not the earlier whole-row inverse convention.
PREDICTIONS BEFORE execution: for child phase p, ancestor number n has
phase(p+n)%2 and root0^floor((n+p)/2)w; n forward updates recover the
child's determined prefix. Its first n+p left depths are1010... .
Independent: literal truth-table inverse versus forward Rule30 updates.
CF: zero inheritance can persist to n=d-p; d3/p1/w100101 must fail
at n2 although its n1 parent inherits the three-zero child band.
Unexpected: black child p1 needs the first prepend at n1, not n2;
the extra checkerboard cell is essential to the half-depth budget.
No solver, membership, record census, new cuts or inverse-depth search.
OUTCOME 2026-10-13, Intel CPU: all540 ancestry/forward/checkerboard
controls PASS. The known real B d3 band inherits once, then fails
zero inheritance at its n2 formal ancestor. Phase-padding CF rejected.
"""
from itertools import product
from rule30_prefix_realization import inverse, rule


def ancestor(w, p, n):
    return inverse([0]*((n+p)//2)+list(w), (p+n)%2)


def forward(a, phase):
    return [rule(a[j+1],a[j],phase if j == 0 else a[j-1])
            for j in range(len(a)-1)]


def main():
    cases = 0
    for length in range(1,5):
        for w in product((0,1),repeat=length):
            for p in (0,1):
                child = inverse(list(w),p)[:2*length-1]
                for n in range(9):
                    a = ancestor(w,p,n)
                    assert a[:n+p] == [j%2 for j in range(1,n+p+1)]
                    for t in range(n):
                        a = forward(a,(p+n+t)%2)
                    assert a[:2*length-1] == child
                    cases += 1
    w = list(map(int,'100101'))
    child = ancestor(w,1,0)
    parent = ancestor(w,1,1)
    grandparent = ancestor(w,1,2)
    assert child[2:5] == [0]*3
    assert parent[1:6] == [0]*5
    assert grandparent[0] == 1  # cannot inherit zeros at depths1..7
    assert ancestor(w,1,1) != inverse(w,0)
    print('canonical ancestry and checkerboard controls',cases,'PASS')
    print('known actual d3 child inherits once; n2 countercontrol PASS')


if __name__ == '__main__':
    main()
