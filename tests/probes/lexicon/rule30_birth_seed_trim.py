"""GC1187: trailing-zero fingerprints extend the same birth band inward.

PREDICTIONS BEFORE execution, 2026-10-13: four fixed formal parent
paths, not a census, with K29,L13 and both child phases:
 N6/g5/Q gap0111 -> h4, Delta3, deficit1;
 N6/g6/Q gap00001 -> h7, Delta1, deficit3 (same deficit);
 N7/g6/Q gap10101 -> h6, Delta2, deficit2;
 N7/g5/P gap1011 -> h7, Delta0, deficit3 (primitive).
At each path's intermediate ancestor, both the old and extended band
must inherit zeros, and both selected parent intervals must be nonzero
at exactly agea=N-p. Four named two-bit tails must not repair the
first nonzero parent or change the determined extended band.
Independent: packed ordinary-seed left support versus literal parent
paths; the proof, not the controls, identifies a path as canonical when
it comes from an actual child. No real membership of these paths claimed.
CF: every profile with a zero last nominal bit drops its deficit. The
N6/g6/Q path must retain j3 after a one-cell extension.
Unexpected: real B100101's restricted d5/L1 band extends to d3/L3 at
same age2, below the d>=6 exclusion domain; do not erase that case.
Record searched: trim|trailing.zero|support withbirth|deficit|inward
->24hits10files; GC1181 extensions, GC1184's proved finite-gap crop,
GC1186's class guard and the exact white triangle read.
OUTCOME: all32 fixed-path comparisons PASS, with sharp inward edge.
The same-deficit one-cell case and actual small-depth exception held.
No survival, language, record or profile census; no solver or Local run.
"""
from itertools import product
from rule30_prefix_realization import inverse
from rule30_canonical_parent_budget import ancestor, forward
from rule30_birth_gap_crop import ordinary

FIXTURES = ((6,5,'Q','0111',4),(6,6,'Q','00001',7),
            (7,6,'Q','10101',6),(7,5,'P','1011',7))


def birth_path(rows,p,d,L):
    a=len(rows)-1
    assert rows[-1][d-1:d+L-1] == [0]*L
    for n in range(1,a+1):
        lo,count=d-n,L+2*n
        band=rows[-1-n][lo-1:lo-1+count]
        assert len(band)==count
        if any(band):return n
    raise AssertionError('must reach black birth parent')


def main():
    comparisons=0
    for N,g,typ,text,want_h in FIXTURES:
        gap=list(map(int,text));r=N%2;s=N+g
        prefix=[j%2 for j in range(1,N+1)]+gap
        proto=prefix+([1]*40 if typ=='Q' else [0]+[1]*40)
        U=forward(proto,r)
        bits=[1,r,1-r]+U[N-1:s-1]
        h=max(i for i,b in enumerate(bits) if b)
        assert h==want_h
        Delta=g+2-h
        z=N+h-2
        assert U[z-1:]==[0]*len(U[z-1:])
        for p in (0,1):
            a=N-p;d=2*N+g-p-1;L=13;dt=d-Delta
            assert dt>=6 and (dt-p)//2+1-a==(h-1)//2
            seed=ordinary([-i for i,b in enumerate(bits) if b],a-1)
            assert seed(N-3-(dt-1))==1
            for tail in product((0,1),repeat=2):
                path=[prefix+([1]*29 if typ=='Q' else [0]+[1]*29)+list(tail)]
                for t in range(a):path.append(forward(path[-1],(r+t)%2))
                assert birth_path(path,p,d,L)==birth_path(path,p,dt,L+Delta)==a
                assert path[-1][dt-2]==1  # sharp white edge
                comparisons+=1
    # Known real child: verify its canonical paths, not just a formal gap.
    w=list(map(int,'100101'))
    for d,L in ((5,1),(3,3)):
        assert ancestor(w,1,0)[d-1:d+L-1]==[0]*L
        assert ancestor(w,1,1)[d-2:d+L]==[0]*(L+2)
        assert any(ancestor(w,1,2)[d-3:d+L+1])
    print('four fixed paths, sharp support and same-birth tail controls:',comparisons,'PASS')
    print('one-cell trimming keeps j3; real d5->d3 age2 boundary guard PASS')

if __name__=='__main__':main()
