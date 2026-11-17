#!/usr/bin/env python3
"""Independent scalar audit of L134; no quotient construction or Local imports.
Known checks written before execution: q4 loop reward1 at feature(1,3,1);
q8 cycle reward17, nonconcatenating representatives. Counterfactual: toggle
source a(0) and demand incompatibility. Unexpected check: equal features do
not imply equal pair states. Symbolic sparse q8 family is checked separately.
"""
import time
import resource

def bit(w,t,q): return (w>>(t%q))&1

def D(w,q):
    if not w: return 0
    for j in range(q):
        if bit(w,j,q): return j+1
    raise AssertionError

def feat(pair,q):
    a,b=pair
    return D(a,q),D(b,q),D(a^b,q)

def gate(pair,q):
    a,b=pair
    return pair==(0,0) or bool(bit(a,-1,q) if a else bit(b,0,q)^bit(b,-1,q))

def valid(source,target,q,d):
    a,b=source; tb,tc=target
    c=sum(bit(tc,t-d,q)<<t for t in range(q))
    return (d==D(b,q) and gate(source,q) and gate(target,q)
            and all(bit(tb,t,q)==bit(b,t+d,q) for t in range(q))
            and all(bit(c,t+1,q)==(bit(a,t,q)^(bit(b,t,q)|bit(c,t,q))) for t in range(q)))

def main():
    started=time.process_time()
    groups=[(4,[((15,12),(9,4),3)],1),
            (8,[((203,200),(140,32),4),((236,224),(131,32),6),((227,224),(131,8),6)],17)]
    for q,edges,expected in groups:
        assert all(valid(s,t,q,d) for s,t,d in edges)
        assert all(feat(t,q)==feat(edges[(i+1)%len(edges)][0],q) for i,(_,t,_) in enumerate(edges))
        assert sum(2*d-5 for _,_,d in edges)==expected
        assert any(t!=edges[(i+1)%len(edges)][0] for i,(_,t,_) in enumerate(edges))
        for (a,b),t,d in edges:
            assert not valid((a^1,b),t,q,d)
        print('q',q,'reward',expected,'literal/gate/feature-cycle/mutation/nonconcatenation PASS')
    # q8 sparse exact-period construction: b black at2,3,7; c at1,5,7.
    assert valid((255,140),(145,84),8,3)
    assert feat((255,140),8)==feat((145,84),8)==(1,3,1)
    print('sparse q8 self-loop representative PASS, reward1')
    print('GPT Intel CPU %.4f s; RSS %.1f MiB' % (time.process_time()-started,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576))
if __name__=='__main__': main()
