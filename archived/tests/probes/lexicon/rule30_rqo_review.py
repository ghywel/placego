#!/usr/bin/env python3
"""Independent targeted RQO audit, no Local imports or quotient traversal.
Known preexecution expectations: reached five-edge segment starting aligned
(143,26) at depth270, rewards[-1,-1,-1,3,3]; two-edge segment ending
aligned(137,206) at depth320, rewards[1,3]; feature joins close, total7.
Unexpected check: both splices agree in labels but differ as actual states.
Counterfactual: toggling source bit0 breaks every representative recurrence.
Temporal orders from binomial substitution at X=1, independently checked
against cyclic derivative annihilation on witness words only.
"""
import time
import resource
q=8

def bit(w,t): return (w>>(t%q))&1

def rot(w,d): return sum(bit(w,t+d)<<t for t in range(q))

def D(w,r): return 0 if not w else next(j+1 for j in range(q) if bit(w,r+j))

def compat(a,b,c):
    return all(bit(c,t+1)==(bit(a,t)^(bit(b,t)|bit(c,t))) for t in range(q))

def order(w):
    if not w: return 0
    v=next(j for j in range(q) if sum(bit(w,t) for t in range(j,q) if (t&j)==j)%2)
    n=0; z=w
    while z:
        z=sum((bit(z,t)^bit(z,t+1))<<t for t in range(q));n+=1
        assert n<=q
    assert n==q-v
    return n

def feat(s):
    a,b=s
    p=next(d for d in (1,2,4,8) if rot(a,d)==a and rot(b,d)==b)
    return (D(a,0),D(b,0),D(a^b,0),p,order(a),order(b),order(a^b))

def ancestry(end,depth):
    back=[end];a,b=end
    for _ in range(depth):
        a,b=sum((bit(b,t+1)^(bit(a,t)|bit(b,t)))<<t for t in range(q)),a
        back.append((a,b))
    assert (a,b)==(0,255)
    path=back[::-1]
    assert all(bb==b and compat(a,b,c) for (a,b),(bb,c) in zip(path,path[1:]))
    clocks=[]
    for start in range(q):
        times=[start]
        for a,b in path[:-1]: times.append(times[-1]+D(b,times[-1]))
        clocks.append(times)
    choices=[t for t in clocks if t[-1]%q==0]
    assert choices,'aligned endpoint must have a root-clock witness'
    return path,choices[0]

def edge(s,t,d):
    a,b=s;c=rot(t[1],-d)
    assert rot(b,d)==t[0] and compat(a,b,c) and D(b,0)==d
    assert not compat(a^1,b,c)
    assert bit(a,-1)==bit(b,d-1)==1
    return (s,t,d)

t0=time.process_time()
path,clocks=ancestry((143,26),270)
s=(143,26); first=[]
for d in (2,2,2,4,4):
    a,b=s
    kids=[c for c in range(256) if compat(a,b,c)]
    assert len(kids)==1
    c=kids[0];t=(rot(b,d),rot(c,d))
    first.append(edge(s,t,d));s=t
path2,times2=ancestry((137,206),320)
second=[]
for k,d in ((318,3),(319,4)):
    s=tuple(rot(w,times2[k]) for w in path2[k])
    t=tuple(rot(w,times2[k+1]) for w in path2[k+1])
    assert times2[k+1]-times2[k]==d
    second.append(edge(s,t,d))
assert feat(first[-1][1])==feat(second[0][0])
assert feat(second[-1][1])==feat(first[0][0])
assert first[-1][1]!=second[0][0]
assert second[-1][1]!=first[0][0]
all_edges=first+second
assert [2*d-5 for s,t,d in all_edges]==[-1,-1,-1,3,3,1,3]
assert sum(d for s,t,d in all_edges)==21
assert sum(2*d-5 for s,t,d in all_edges)==7
assert order(0)==0 and order(255)==1
assert feat((183,176))!=feat((133,208))
for s,t,d in all_edges:
    assert all(order(rot(w,r))==order(w) for w in (*s,*t) for r in range(q))
    print(s,'->',t,'delay',d,'features',feat(s),'->',feat(t))
print('RQO ancestry/root-clock/edge/order/feature joins PASS; 7 edges, elapsed21, reward7')
print('splices:',first[-1][1],second[0][0],';',second[-1][1],first[0][0])
print('root clocks: firstsource',clocks[-1],'; second endpoints',times2[318:321])
print('CPU %.4f s RSS %.1f MiB'%(time.process_time()-t0,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576))
