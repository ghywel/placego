#!/usr/bin/env python3
"""GC922 fixed doubling/clock control; no tree enumeration or peer imports.
Predictions in CLOUD-LOCAL at 02:06 BST, before the first literal run:
P1 a=10111011 absorbs at29; P2 root clocks coalesce modulo4;
P3 at least one doubled integration separates modulo8 (blind).
Controls: fixed-period reset preserves old coalescence; bit-flipped child fails.
Unexpected: some source clocks differ by4 despite equal old residue.
Outcome: all held; both children split (cardinality2 is post hoc).
Full-line clocks only, no birth-clamp or universal re-coalescence claim.
"""
import json

def main():
    a=list(map(int,'10111011'));q=len(a)
    def S(v):return v[1:]+v[:1]
    def B(p):
        x,y=p
        return ([s^(u|v) for s,u,v in zip(S(y),x,y)],x[:])
    p=(a,[0]*q);back=[p]
    for _ in range(64):
        if not any(p[0]+p[1]):break
        p=B(p);back.append(p)
    else:raise RuntimeError('ancestry cap: incomplete')
    assert len(back)-1==29
    path=list(reversed(back[:-1]))
    assert path[0]==([0]*q,[1]*q)
    # Independent forward scalar compatibility of every reconstructed triple.
    for (x,y),(y2,z) in zip(path,path[1:]):
        assert y2==y
        assert all(z[(t+1)%q]==(x[t]^(y[t]|z[t])) for t in range(q))
    def F(w,t):
        if not any(w):return t
        return t+1+next(k for k in range(q) if w[(t+k)%q])
    clock=list(range(q))
    for x,y in path[:-1]:clock=[F(y,t) for t in clock]
    assert len({t%4 for t in clock})==1
    assert any(t-u==4 for t in clock for u in clock)
    assert all(a[(t-1)%q]==1 for t in clock), 'source arrival gate'
    assert [F([0]*q,t) for t in clock]==clock
    assert len({F(a,t)%4 for t in clock})==1
    branches=[]
    for first in (0,1):
        c=[first]
        for x in a:c.append(c[-1]^x)
        assert c.pop()==first
        assert S(c)==[x^y for x,y in zip(a,c)]
        bad=c[:];bad[0]^=1
        assert S(bad)!=[x^y for x,y in zip(a,bad)]
        out=[F(c,t) for t in clock]
        branches.append(dict(child=''.join(map(str,c)),times=out,residues=sorted({t%q for t in out})))
    assert any(len(b['residues'])>1 for b in branches)
    print(json.dumps(dict(absorption=len(back)-1,root_clocks=clock,branches=branches,
                         P1=True,P2=True,P3=True,C_fixed=True,C_flip=True,U=True,
                         forward_replay=True),indent=2))

if __name__=='__main__':main()
