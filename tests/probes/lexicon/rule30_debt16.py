#!/usr/bin/env python3
"""RD16: exact reference debt through every rooted period-32 entry.
Preregistered GPT block, no change to Local's running TM6b.
CPU Python, 120 CPU seconds, 256 MiB, 3 million transitions, 32 leaves.
P1 blind uncertain: every D_(5/2)(N5) <= 64.
P2 blind uncertain: some continuation exceeds the shared-prefix debt 26.5.
C1 literal triples and all sixteen previously certified N5 entries reproduce.
C2 independently scanned reset delays agree; natural prefix M53207 debt=26.5.
CF dropping zero-delay edges changes the synthetic adjusted sequence 2,-2,2
   from debt2 to debt4; this must be rejected.
U zero exit edge is included: it leaves debt unchanged but updates prefix minimum.
Shared constructor rq3.children: this is a new clock measurement, not an
independent implementation of the rooted tree. No asymptotic inference.
Transcripts and JSON outside Git. All controls required; cap means partial.
"""
import json, resource, time
import rule30_rq3 as rq
Q=16; FULL=(1<<Q)-1
EXPECTED=[87867,183184,196189,229338,253537,271596,291257,527724,
          551910,555813,575211,634886,645655,667052,770532,894235]

def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF)
    return r.ru_utime+r.ru_stime

def delay(w,t):
    if not w:return 0
    r=t%Q
    v=((w>>r)|(w<<(Q-r)))&FULL
    return (v&-v).bit_length()

def debt(gs):
    z=m=d=0
    for g in gs:z+=g;d=max(d,z-m);m=min(m,z)
    return d

start=cpu();steps=0;leaves=[];c2=u=True
# d,x,y,clock,min(2T-5d),debt2,min witness (depth,clock), debt witness, branch path
stack=[(0,0,FULL,0,0,0,(0,0),None,())]
shared=None
while stack:
    d,x,y,t,m,D,mi,wit,path=stack.pop()
    while True:
        if cpu()-start>120 or steps>=3000000 or len(leaves)>32 or resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>256*2**20:
            raise RuntimeError('CAP: partial, no certified debt report')
        dt=delay(y,t)
        literal_dt=next((i+1 for i in range(Q) if (y>>((t+i)%Q))&1),0)
        c2 &= dt==literal_dt
        oldD=D;t2=t+dt;z=2*t2-5*(d+1)
        if z-m>D:D=z-m;wit=(mi[0],d+1,mi[1],t2)
        if z<m:m=z;mi=(d+1,t2)
        if d+1==53207:
            assert shared is None or shared==D
            shared=D
        cs=rq.children(x,y,Q)
        steps+=1
        if not cs:
            assert y==0 and bin(x).count('1')%2==1
            u &= D==oldD and dt==0 and z==2*t-5*(d+1)
            leaves.append(dict(N5=d+1,debt2=D,witness=wit,path=path,clock=t2))
            break
        for c in cs:
            assert all(((c>>((k+1)%Q))&1)==(((x>>k)&1)^(((y>>k)&1)|((c>>k)&1))) for k in range(Q))
        if len(cs)==2:
            assert y==0 and cs[0]^cs[1]==FULL
            if not any(rq.rot(cs[0],k,Q)==cs[1] for k in range(Q)):
                stack.append((d+1,0,cs[1],t2,m,D,mi,wit,path+(d,)))
        x,y,d,t=y,cs[0],d+1,t2
leaves.sort(key=lambda r:r['N5'])
c1=[r['N5'] for r in leaves]==EXPECTED
c2 &= shared==53
for r in leaves:
    a,b,ta,tb=r['witness']
    assert r['debt2']==2*(tb-ta)-5*(b-a)
cf=debt([2,-2,2])==2 and debt([2,2])==4
out=dict(controls=dict(C1=c1,C2=c2,CF=cf,U=u),
         P1=all(r['debt2']<=128 for r in leaves),
         P2=any(r['debt2']>53 for r in leaves),
         shared_debt2=shared,leaves=leaves,steps=steps,cpu_seconds=cpu()-start)
print(json.dumps(out,indent=2))
assert all(out['controls'].values()), 'CONTROL FAILURE: retain report, do not certify'
