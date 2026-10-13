"""GC1197: realized-row guard when the first train departure lies in a band.

PREDICTIONS BEFORE controls, 2026-10-13: with matching train prefix,
phase0 bands of length>=4 can start only at d mod56 in
{11,12,13,17,35,36,37}; phase1 length>=6 only at
{10,11,12,13,14,30,50}. Symbolic first-discrepancy residues are
p0{13,17,37},p1{14,30,50}. Counterfactual: the T1-only repair gate
does not transfer to actual-row coordinates or the phase3 reference.
Eight named bands p0d9/13/17/41,p1d14/22/30/42, L6, two farther
tails each: the first two arrivals have the predicted black verdict.
Independent: lookup versus Boolean clamped evolution; G25 inverse of
the pure visible train versus the periodic reference row. Unexpected:
L3 at p0d7 and L5 at p1d38 do not fix the next pivot; changing only
that outside-band cell changes the next black verdict. Keep the exact
clock horizon, and do not assert actual membership of these controls.
Record searched: first.departure|first.differ|train.prefix withzero.band|
white.band|record|mod56 ->22hits14files. GC1167/1194/1195, G25 and
GC1023 read. No record/crop-time/birth/profile census or Local replay.
OUTCOME: both symbolic residue sets match the prediction;16 named band
controls and the two outside-horizon pivot controls PASS. These formal
controls have not been asserted to be actual real-language records.
"""
from rule30_train_end_pivot import ROWS
from rule30_seed_prefix_scope import trace
from rule30_extremal_p_corner_read import forced_row


def A(p,t,j):return int(ROWS[(t+3*p)%4][(-j)%7])


def charge(p,ell):
    c=ell%2
    for t in range(ell):c ^= A(p,t,ell-t-1)
    return c


def main():
    allowed_ell=({13,17,37},{14,30,50})
    allowed_d=({11,12,13,17,35,36,37},{10,11,12,13,14,30,50})
    for p in (0,1):
        got=set();starts=set()
        for ell in range(56,112):
            if ell%4!=1+p or not A(p,0,ell):continue
            if charge(p,ell)!=A(p,0,ell+1):continue
            got.add(ell%56);b=ell
            while True:
                starts.add(b%56)
                if A(p,0,b-1):break
                b-=1
        assert got==allowed_ell[p] and starts==allowed_d[p]
        print('phase',p,'discrepancy classes',sorted(got),'band starts',sorted(starts))
    count=0
    for p,d,passes in ((0,9,False),(0,13,True),(0,17,True),(0,41,False),
                       (1,14,True),(1,22,False),(1,30,True),(1,42,False)):
        E=d+5;ell=next(j for j in range(d,E+1) if A(p,0,j))
        ref=forced_row([1-i%2 for i in range((E+3)//2)],p)[1:]
        assert ref[:E]==[A(p,0,j) for j in range(1,E+1)]
        for tail in ('0000','1111'):
            row=[A(p,0,j) for j in range(1,d)]+[0]*6+list(map(int,tail))
            x=trace(row,p,True);assert x==trace(row,p,False)
            assert x[:ell-1]==[A(p,t,1) for t in range(ell-1)]
            assert x[ell-1]!=A(p,ell-1,1)
            assert (x[ell]==1)==passes
            count+=1
    assert count==16
    for p,d,L in ((0,7,3),(1,38,5)):
        E=d+L-1;ell=next(j for j in range(d,E+1) if A(p,0,j))
        assert ell==E
        pref=[A(p,0,j) for j in range(1,d)]+[0]*L
        xs=[trace(pref+[repair]+[0]*3,p,True) for repair in (0,1)]
        assert xs[0][:ell]==xs[1][:ell]
        assert xs[0][ell]!=xs[1][ell]
        assert xs[1][ell]==1
    print('16 named clamped band controls PASS; two missing-next-pivot controls PASS')


if __name__=='__main__':main()
