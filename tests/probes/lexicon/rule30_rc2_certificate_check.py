#!/usr/bin/env python3
"""G181 static certificate checker, no producer imports/search/optimization.
Usage: python3 rule30_rc2_certificate_check.py CERTIFICATE.json
Preregistered known expectations: q8 K/h maxima14, all coverage and inequality
checks pass. Negative controls: zero K and a removed known edge rejected.
Unexpected guard: terminal edge labels remain present; lift need not attain
Kmax+11. Artifact and producing commit/checksum are recorded outside this code.
"""
import hashlib
import json
import resource
import sys
import time

EXPECTED_SHA='f8d57126f5601ec41295db803ba13271ac54523e4b39a6c5a749b3f30e76a2a7'


def verify(data,q):
    mask=(1<<q)-1
    def bit(w,t): return (w>>(t%q))&1
    def rot(w,r): return sum(bit(w,t+r)<<t for t in range(q))
    def D(w): return 0 if not w else next(t+1 for t in range(q) if bit(w,t))
    def compatible(a,b,c):
        return all(bit(c,t+1)==(bit(a,t)^(bit(b,t)|bit(c,t))) for t in range(q))
    def nu(w):
        if not w: return 0
        v=next(j for j in range(q) if sum(bit(w,t) for t in range(j,q) if (t&j)==j)%2)
        return q-v
    def phi(s):
        a,b=s
        p=next(d for d in range(1,q+1) if q%d==0 and rot(a,d)==a and rot(b,d)==b)
        return (D(a),D(b),D(a^b),p,nu(a),nu(b),nu(a^b))
    vertices=data['vertices'];states=[tuple(v['state']) for v in vertices]
    assert len(set(states))==len(states)
    assert all(len(s)==2 and all(type(w)==int and 0<=w<=mask for w in s) for s in states)
    root=data['root'];assert states[root]==(0,mask)
    edges=[]
    for row in data['edges']:
        s,t,d=row['source'],row['target'],row['delay']
        assert all(type(x)==int for x in (s,t,d))
        assert 0<=s<len(states) and 0<=t<len(states)
        a,b=states[s];bb,cc=states[t]
        assert d==D(b) and bb==rot(b,d)
        c=rot(cc,-d);assert compatible(a,b,c)
        edges.append((s,t,d))
    assert len(set(edges))==len(edges)
    outgoing={i:[] for i in range(len(states))}
    for e,(s,t,d) in enumerate(edges):outgoing[s].append(e)
    # Supplied parent certificates, not a new reachability traversal.
    for i,v in enumerate(vertices):
        if i==root:assert v['parent_edge'] is None
        else:
            pe=v['parent_edge'];assert type(pe)==int and 0<=pe<len(edges) and edges[pe][1]==i
        seen=set();j=i
        while j!=root:
            assert j not in seen;seen.add(j)
            j=edges[vertices[j]['parent_edge']][0]
    # Literal successor closedness independently of producer recursion.
    lookup={s:i for i,s in enumerate(states)};exits=0;expected_by_source={}
    for i,(a,b) in enumerate(states):
        if i!=root:
            assert bit(a,-1)==1 if a else bit(b,0)^bit(b,-1)==1
        d=D(b);children=[c for c in range(1<<q) if compatible(a,b,c)]
        expected=set()
        for c in children:
            target=(rot(b,d),rot(c,d));assert target in lookup
            expected.add((i,lookup[target],d))
        actual={edges[e] for e in outgoing[i]}
        assert actual==expected
        expected_by_source[i]=expected
        if not children:
            assert b==0 and a.bit_count()%2==1
            assert D(b)==0 and 2*D(b)-5==-5
            exits+=1
    assert len(outgoing[root])==1 and edges[outgoing[root][0]][2]==1
    labels=[phi(s) for s in states]
    L=[(labels[s],labels[t]) for s,t,d in edges]
    K={}
    for row in data['K']:
        label=tuple(tuple(x) for x in row['label']);value=row['K']
        assert label not in K and type(value)==int and value>=0
        K[label]=value
    assert set(K)==set(L), 'every label, including terminals, required'
    arcs=[]
    for i,(s,t,d) in enumerate(edges):
        for j in outgoing[t]:
            w=2*edges[j][2]-5
            assert K[L[i]]>=w+K[L[j]]
            arcs.append((i,j,w))
    h=[0]*len(states)
    for i,(s,t,d) in enumerate(edges):h[s]=max(h[s],2*d-5+K[L[i]])
    assert all(h[s]>=2*d-5+h[t] for s,t,d in edges)
    assert max(h)<=max(K.values())+max(0,2*q-5)
    summary=data['summary']
    for key,value in [('vertices',len(states)),('edges',len(edges)),('labels',len(K)),
                      ('cap_exits',exits),('K_max',max(K.values())),('h_max',max(h))]:
        assert summary[key]==value
    if q==8:
        assert max(K.values())==max(h)==14
        # Corruptions tested against the independently verified obligations.
        assert any(w>0 for i,j,w in arcs), 'zero K must violate a context inequality'
        s=lookup[(143,26)];t=lookup[(134,186)];known=(s,t,2)
        assert known in expected_by_source[s]
        assert {edges[e] for e in outgoing[s]}-{known}!=expected_by_source[s]
        terminal_labels={L[i] for i,(s,t,d) in enumerate(edges) if not outgoing[t]}
        assert terminal_labels and terminal_labels<=set(K)
        assert max(h)<max(K.values())+11
    print('q%d: parent coverage PASS; successor closedness PASS; labels/K/context/lift PASS; '
          '%d vertices/%d edges/%d labels/%d arcs; Kmax%d hmax%d; exits%d'%
          (q,len(states),len(edges),len(K),len(arcs),max(K.values()),max(h),exits))


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(120,120))
    t0=time.process_time()
    raw=open(sys.argv[1],'rb').read();assert hashlib.sha256(raw).hexdigest()==EXPECTED_SHA
    data=json.loads(raw)
    for q in (1,2,4,8):verify(data[str(q)],q)
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576
    assert rss<=128 and time.process_time()-t0<120
    print('checksum PASS; zero-K/missing-edge controls REJECTED; terminal-label/strict-bound guards PASS')
    print('CPU %.4f s RSS %.1f MiB'%(time.process_time()-t0,rss))

if __name__=='__main__':main()
