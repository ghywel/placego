"""GC484 fixed-window exact-potential audit on the actual single-cell orbit.
C0 MUST: integer XOR/OR and independent decimal-set evolution agree through256 ticks.
C1 MUST: every sampled pair reward equals its signed spin-pair sum.
P1 BLIND: radius1 admits a nonzero-reward contradiction to h(next)-h(now)=g.
Fixed scope: radii0..3, phases2/4/8, first128 two-step transitions; no horizon chase.
CF: replacing all rewards by0 still yields an inconsistent potential; must fail.
Unexpected: include explicit temporal phases4 and8, not only a spatial window.
Controls: synthetic three-node feasible graph; nonzero self-loop infeasible.
REFUTED-BY: failed C0/C1 or radius1 remains feasible at phase2.
A graph contradiction forbids a pointwise exact local potential on these visited
transitions. It says nothing about asymptotic density, approximate potentials,
longer memory, larger radii, or paths actually concatenating on the orbit.
"""
from collections import deque

def consistent(edges):
    adj={}
    for u,v,g,t in edges:
        adj.setdefault(u,[]).append((v,g,t))
        adj.setdefault(v,[]).append((u,-g,t))
    h={};parent={}
    for root in adj:
        if root in h:continue
        h[root]=0;parent[root]=None;q=deque([root])
        while q:
            u=q.popleft()
            for v,g,t in adj[u]:
                if v not in h:
                    h[v]=h[u]+g;parent[v]=(u,t);q.append(v)
                elif h[v]!=h[u]+g:
                    def path(a):
                        out=[]
                        while parent[a] is not None:
                            a,tt=parent[a];out.append(tt)
                        return out
                    return False,{'edge_time':t,'expected_difference':g,'assigned_difference':h[v]-h[u],
                                  'constraint_times':sorted(set(path(u)+path(v)+[t]))}
    return True,None

def decimal_set_step(a):
    return {i for i in range(min(a)-1,max(a)+2)
            if (30>>(4*int(i-1 in a)+2*int(i in a)+int(i+1 in a)))&1}

if __name__=='__main__':
    assert consistent([(0,1,2,0),(1,2,-1,2),(2,0,-1,4)])[0]
    assert not consistent([(0,0,1,0)])[0]
    T=256;off=T+5;mask=(1<<(2*off+1))-1;row=1<<off;a={0};rows=[];spins=[]
    for t in range(T+1):
        rows.append(row);spins.append(1-2*((row>>off)&1))
        assert {i-off for i in range(2*off+1) if (row>>i)&1}==a
        if t<T:
            row=((row<<1)^(row|(row>>1)))&mask;a=decimal_set_step(a)
    for r in range(4):
        for phase in (2,4,8):
            def state(t):return ((rows[t]>>(off-r))&((1<<(2*r+1))-1),t%phase)
            edges=[]
            for t in range(0,T,2):
                c=(rows[t]>>off)&1;cn=(rows[t+1]>>off)&1
                g=(1-2*c)*int(c==cn);assert 2*g==spins[t]+spins[t+1]
                edges.append((state(t),state(t+2),g,t))
            ok,w=consistent(edges)
            assert consistent([(u,v,0,t) for u,v,g,t in edges])[0]
            if r==1 and phase==2:assert not ok
            print('radius',r,'phase',phase,'feasible',ok,'witness',w)
    print('PASS:257 independent rows,1536 pair identities,12 zero-reward CF controls; radius1 blind verdict HELD')
