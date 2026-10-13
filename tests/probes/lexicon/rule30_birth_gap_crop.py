"""GC1184: a finite defect gap gives a finite ordinary-seed crop.

PREDICTIONS BEFORE execution (2026-10-13): for the named interfaces
N=3,4, gapsg=3,4, first free bit=N%2, each allowed Q/P junction,
K=17 and both child phases, one parent update yields zeros froms=N+g.
A seed withV0=1,V1=N%2,V2=1-N%2 andV_(j-N+3)=the updated parent
at j=N..s-1 gives the child left crop atX=N-3,T=N-p-1 through
J=s+K-1-a (Q) orJ=s+K-a (P), a=N-p. Crop support ends befored,
d=2N-p+g-1. Four named tails00,01,10,11 must not affect this prefix.
CF: the whole ordinary configuration realizes the child's centre/right;
p1 centre is actually white, so that identification must fail.
Independent: literal clamped Rule30 versus packed ordinary full-line
Rule30; symbolic6/7-bit junction formulas versus literal one-step image.
Unexpected: the two rightmost inward checker bits are essential; wrong
V1 may agree at T0 but must not be used in the all-time induction.
First run stopped on a negative packed bit index for a queried white
cell outside represented storage; fixed to return0 there before rerun.
No mathematical prediction or registered input changed.
OUTCOME:18 junctions,144 tail/crop controls PASS; changingV1 alters36
phase/profile crops. Symbolic junctions and all centre-phase guards pass.
No survival census, period/window search, solver or language computation.
Record searched: third.oldest|deficit withbirth|profile ->13hits10files;
birth|black.core withfinite.seed|fingerprint|crop ->9hits3files;
leading.zero withyounger|deficit|promotion ->GC1181 pointer only.
GC1174, GC1177, GC1181, GC1183 andG249 read.
"""
from itertools import product
from rule30_prefix_realization import rule
from rule30_canonical_parent_budget import forward


def ordinary(sites, ticks):
    offset = max(ticks+12, 20)
    x = sum(1 << (offset+s) for s in sites)
    for _ in range(ticks):
        x = (x << 1) ^ (x | (x >> 1))
    return lambda s: ((x >> (offset+s)) & 1) if offset+s >= 0 else 0


def main():
    controls = wrong_controls = 0
    profiles = set()
    for N in (3,4):
        r = N%2
        for g in (3,4):
            s = N+g
            for kind in ('Q','P'):
                for gap in product((0,1),repeat=g-1):
                    if gap[0] != r or (kind=='P' and gap[-1] != 1):
                        continue
                    prefix = [j%2 for j in range(1,N+1)] + list(gap)
                    proto = prefix + ([1]*20 if kind=='Q' else [0]+[1]*20)
                    img = forward(proto,r)
                    assert img[s-1:] == [0]*len(img[s-1:])
                    bits = [1,r,1-r] + img[N-1:s-1]
                    assert len(bits) == g+3
                    b = gap[1]
                    if g==3:
                        want = [1,r,1-r,1-r,b^r,
                                (1-(b|r)) if kind=='Q' else 1]
                    else:
                        c = gap[2]
                        want = [1,r,1-r,1-r,b^r,c^(b|r),
                                (1-(c|b)) if kind=='Q' else 1]
                    assert bits == want
                    profiles.add((r,g,kind,gap))
                    sites = [-i for i,b in enumerate(bits) if b]
                    for p in (0,1):
                        a,T,X = N-p,N-p-1,N-3
                        d = 2*N-p+g-1
                        J = s+17-1-a+(kind=='P')
                        out = ordinary(sites,T)
                        crop = [out(X-j) for j in range(1,J+1)]
                        wrong = set(sites) ^ {-1}
                        bad = ordinary(wrong,T)
                        wrong_controls += [bad(X-j) for j in range(1,J+1)] != crop
                        assert crop[d-1:] == [0]*len(crop[d-1:])
                        assert out(X) == 0  # never identify with phase1 centre
                        for tail in product((0,1),repeat=2):
                            parent = prefix + ([1]*17 if kind=='Q' else [0]+[1]*17) + list(tail)
                            for t in range(a):
                                parent = forward(parent,(r+t)%2)
                            assert parent[:J] == crop
                            controls += 1
    assert wrong_controls > 0
    print('wrong inward checker-bit controls differ:',wrong_controls)
    print('18 necessary junction profiles:',len(profiles),
          '; literal/packed crop and tail controls:',controls,'PASS')
    print('symbolic junctions, zero-tail support and phase1 centre guard PASS')

if __name__ == '__main__':
    main()
