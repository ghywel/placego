"""GC1109: test the identified spatial return of the new carrier pair.

Missing inference: can GC1108's finite-window pair representation
advance in depth without introducing a new temporal field?
At depths3/4 and11/12 the right column has equal even/odd
samples R_s, and the left column's odd sample is1-R_(s+1).
P1 BEFORE experiment: after eight further left columns this SAME
canonical pair class returns at19/20 on GC1106's admitted FE code.
A return could support a specific nonlinear depth update; a failed
canonical equality refutes that proposed closure, not all finite-type
routes. Do not replace it by nearby depths or run a depth sweep.
Record searched: GC1108|canonical.*pair|paired.*return|eight.column|
depth20 with left|carrier|renewal|inverse|S/L ->7hits6files; GC1107/8
and GC1007's non-pumping failure read. No prior spatial return found.
Counterfactual: the new nonlinear short field destroys the return.
Controls: the established11/12 pair class; every literal Rule30
triangle checked independently against packed circular forcing;
pure M2 and M3 output controls at the SAME specified depth.
Unexpected check: use all even samples in each temporal period,
not only the synchronized marker. A first-row pass is not closure.
No record, solver, membership, width sweep or arbitrary-depth scan.
OUTCOME: P1 REFUTED on FE and both pure-cycle controls; first
failure atphysical2 in all three. P2 HELD as a complete finite
cone: depths19/20 are1110/001. Every SLL prefix thus creates
the phase asymmetry10 at19, and a black even cell at20.
The synchronized first pair passes; checking only it misses the
defect. This specific eight-depth canonical-return route is closed.
"""
from rule30_sl_short_marker_inverse import gap_markers


def force(q,depth=20):
    n=2*len(q);mask=(1<<n)-1
    wall=sum((t%2)<<t for t in range(n))
    first=sum(v<<t for t,v in enumerate(b for a in q for b in (1-a,1)))
    columns=[wall,first]
    for _ in range(2,depth+1):
        a,b=columns[-1],columns[-2]
        shift=(a>>1)|((a&1)<<(n-1))
        c=shift^(a|b)
        assert c&~mask==0
        assert all(((30>>(4*((c>>t)&1)+2*((a>>t)&1)+((b>>t)&1)))&1)
                   ==((a>>((t+1)%n))&1) for t in range(n))
        columns.append(c)
    return [tuple((c>>t)&1 for t in range(n)) for c in columns]


def finite_cone(q):
    wall=tuple(t%2 for t in range(2*len(q)))
    first=tuple(b for a in q for b in (1-a,1))
    out=[wall,first]
    for _ in range(2,21):
        a,b=out[-1],out[-2]
        c=tuple(a[t+1]^(a[t]|b[t]) for t in range(len(a)-1))
        assert all(((30>>(4*c[t]+2*a[t]+b[t]))&1)==a[t+1]
                   for t in range(len(c)))
        out.append(c)
    return out


def failures(columns,right):
    r,a=columns[right],columns[right+1];n=len(r)
    return [(2*s,'pair',r[2*s],r[2*s+1]) for s in range(n//2)
            if r[2*s]!=r[2*s+1]]+[
           (2*s+1,'odd',a[2*s+1],1-r[(2*s+2)%n]) for s in range(n//2)
           if a[2*s+1]!=1-r[(2*s+2)%n]]


def main():
    f='SLLSSS';e='SLLS'+'SLLSS'*3+'SLLSSS'
    result={}
    for name,letters in (('FE',f+e),('M2','SLLSS'),('M3',f)):
        q=gap_markers(letters);columns=force(q)
        assert not failures(columns,3) and not failures(columns,11)
        bad=sorted(failures(columns,19))
        result[name]=dict(failures=len(bad),first=bad[0] if bad else None,
                          first_row_q=''.join(map(str,q[:11])))
    # P2 BEFORE finite-cone check: this shared SLL prefix alone forces
    # x_-19(2)=1,x_-19(3)=0, hence x_-20(2)=1 for ALL continuations.
    # Circular wrap and the M2/M3 suffix must not be needed for it.
    prefix=tuple(map(int,'10010000100'))
    finite=finite_cone(prefix)
    assert finite[19][2:4]==(1,0) and finite[20][2]==1
    result['universal_SLL_cone']={d:''.join(map(str,finite[d])) for d in range(14,21)}
    print(result)


if __name__=='__main__':main()
