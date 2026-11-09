"""GC2792: exact finite-automaton checks, minimal-forbidden language and rational entropy brackets.
The general forbidden-language construction is known (Beal et al., 2003); this applies it to the saved Rule30 DFAs.
Run only under the frozen serial stage. No physical realization or infinite-width entropy claim.
"""
import collections, hashlib, json, math, os, re, sys
from pathlib import Path
import numpy as np
from scipy.sparse import coo_matrix, eye
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import spsolve

out, local = Path(sys.argv[1]), Path(sys.argv[2])
first=int(sys.argv[3]) if len(sys.argv)>3 else 16
expected={};width=None
for line in local.read_text().splitlines():
    m=re.match(r'W=(\d+):',line)
    if m:width=int(m[1]);expected[width]=[]
    m=re.match(r'\s+\d+ gaps\s+([35]+)\s',line)
    if m:expected[width].append(m[1])

def run(tr,w):
    i=0
    for c in w:
        i=tr[i][c=='5']
        if i<0:return -1
    return i

def minimize(tr):
    n=len(tr);total=[tuple(n if x<0 else x for x in r) for r in tr]+[(n,n)]
    cl=[0]*n+[1]
    while True:
        sig=[(i==n,cl[a],cl[b]) for i,(a,b) in enumerate(total)]
        ids={};nc=[ids.setdefault(s,len(ids)) for s in sig]
        done=len(set(nc))==len(set(cl));cl=nc
        if done:break
    reps={c:i for i,c in enumerate(cl)};dead=cl[n];index={cl[0]:0};queue=[cl[0]];m=[]
    for c in queue:
        row=[]
        for t in total[reps[c]]:
            d=cl[t]
            if d==dead:row.append(-1)
            else:
                if d not in index:index[d]=len(index);queue.append(d)
                row.append(index[d])
        m.append(row)
    return m

def minimal_words(tr,depth):
    words=[];front=[('',0)]
    for _ in range(depth):
        nf=[]
        for w,i in front:
            for k,c in enumerate('35'):
                t=tr[i][k];v=w+c
                if t<0:
                    if run(tr,v[1:])>=0:words.append(v)
                else:nf.append((v,t))
        assert len(nf)<1000000,'WORD_FRONTIER_CAP';front=nf
    return words

def forbidden_basis(tr):
    pairs=[];ids={};parent=[];edges=[];terminal=[]
    def add(p,s,prev,c):
        key=(p,s)
        if key not in ids:
            assert len(ids)<200000,'PAIR_CAP';ids[key]=len(ids);pairs.append(key);parent.append((prev,c))
        return ids[key]
    for k,c in enumerate('35'):
        assert tr[0][k]>=0
        add(tr[0][k],0,-1,c)
    for i,(p,s) in enumerate(pairs):
        row=[];end=[]
        for k,c in enumerate('35'):
            a,b=tr[p][k],tr[s][k]
            assert not (a>=0 and b<0),'NOT_FACTORIAL'
            row.append(add(a,b,i,c) if a>=0 else -1)
            if a<0 and b>=0:end.append(c)
        edges.append(row);terminal.append(end)
    rev=[[] for _ in pairs]
    for i,row in enumerate(edges):
        for k,j in enumerate(row):
            if j>=0:rev[j].append((i,'35'[k]))
    # Every state is reachable. Mark precisely those with a terminal continuation.
    toward={i:(None,cs[0]) for i,cs in enumerate(terminal) if cs};q=collections.deque(toward)
    while q:
        j=q.popleft()
        for i,c in rev[j]:
            if i not in toward:toward[i]=(j,c);q.append(i)
    rows=[];cols=[]
    for i in toward:
        for j in edges[i]:
            if j in toward:rows.append(i);cols.append(j)
    n=len(pairs);matrix=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n)).tocsr()
    _,labels=connected_components(matrix,directed=True,connection='strong')
    groups=collections.defaultdict(list)
    for i in toward:groups[int(labels[i])].append(i)
    cyclic=[g for g in groups.values() if len(g)>1 or g[0] in edges[g[0]]]
    result={'pair_states':n,'productive_states':len(toward),'infinite':bool(cyclic)}
    if cyclic:
        group=min(cyclic,key=lambda g:(len(g),min(g)));members=set(group);v=min(group)
        k,j=next((k,j) for k,j in enumerate(edges[v]) if j in members)
        back={j:('',None)};todo=collections.deque([j])
        while v not in back:
            x=todo.popleft()
            for a,y in enumerate(edges[x]):
                if y in members and y not in back:back[y]=('35'[a],x);todo.append(y)
        cpath='';x=v
        while x!=j:c,x=back[x];cpath=c+cpath
        cycle='35'[k]+cpath
        prefix='';x=v
        while x>=0:x,c=parent[x];prefix=c+prefix
        suffix='';x=v
        while x is not None:x,c=toward[x];suffix+=c
        assert len(prefix)+len(cycle)+len(suffix)<4096,'PUMP_OUTPUT_CAP'
        for count in [0,1,2,5,20]:
            word=prefix+cycle*count+suffix
            assert run(tr,word)<0 and run(tr,word[:-1])>=0 and run(tr,word[1:])>=0
        result.update(prefix=prefix,cycle=cycle,suffix=suffix,checked_powers=[0,1,2,5,20])
    else:
        # Longest productive path, including first and terminal letters. Finite basis exhausts this bound.
        indeg={i:0 for i in toward}
        for i in toward:
            for j in edges[i]:
                if j in toward:indeg[j]+=1
        todo=collections.deque(i for i,d in indeg.items() if d==0);dist={i:1 for i in toward}
        while todo:
            i=todo.popleft()
            for j in edges[i]:
                if j in toward:
                    dist[j]=max(dist[j],dist[i]+1);indeg[j]-=1
                    if indeg[j]==0:todo.append(j)
        length=max((dist[i]+1 for i,x in enumerate(terminal) if x),default=0)
        result['max_length']=length;result['all_words']=minimal_words(tr,length)
    return result

def slope(tr):
    n=len(tr);a=np.array(tr);vec={0:(np.eye(1,n,0).ravel(),0.)};logs={0:0.}
    for t in range(1,4001):
        parts=[]
        for k,g in enumerate([3,5]):
            if t-g in vec:
                v,z=vec[t-g];ok=a[:,k]>=0;r=np.bincount(a[ok,k],weights=v[ok],minlength=n);parts.append((r,z))
        if parts:
            z=max(z for _,z in parts);v=sum(v*2**(j-z) for v,j in parts);m=float(v.max())
            if m:
                e=math.floor(math.log2(m));v/=2**e;z+=e;vec[t]=(v,z);logs[t]=math.log2(float(v.sum()))+z
        vec.pop(t-5,None)
    return (max(logs.get(4000-j,-math.inf) for j in range(5))-max(logs.get(3000-j,-math.inf) for j in range(5)))/1000

def entropy_certificate(tr,h):
    n=len(tr);D=10**9;rows=[];cols=[];gs=[]
    for i,r in enumerate(tr):
        for k,j in enumerate(r):
            if j>=0:rows.append(i);cols.append(j);gs.append(3+2*k)
    graph=coo_matrix((np.ones(len(rows)),(rows,cols)),shape=(n,n)).tocsr()
    _,labels=connected_components(graph,directed=True,connection='strong')
    groups=collections.defaultdict(list)
    for i,c in enumerate(labels):groups[int(c)].append(i)
    def solve(U,nodes,upper):
        idx={j:i for i,j in enumerate(nodes)};rr=[];cc=[];data=[];x=U/D
        for i in nodes:
            for k,j in enumerate(tr[i]):
                if j in idx:rr.append(idx[i]);cc.append(idx[j]);data.append(x**(-3-2*k))
        mat=coo_matrix((data,(rr,cc)),shape=(len(nodes),len(nodes))).tocsr()
        v=spsolve(eye(len(nodes),format='csr')-mat,np.ones(len(nodes))*(1 if upper else -1))
        if not np.all(np.isfinite(v)) or v.min()<=0:return None
        z=[int(round(float(a)*1e6/float(v.min()))) for a in v]
        for i in nodes:
            lhs=sum(D**(3+2*k)*U**(2-2*k)*z[idx[j]] for k,j in enumerate(tr[i]) if j in idx)
            rhs=U**5*z[idx[i]]
            if (lhs>rhs if upper else lhs<rhs):return None
        return {'numerator':U,'denominator':D,'nodes':nodes,'vector':z,'sense':'upper' if upper else 'lower'}
    for delta in [1e-6,1e-5,1e-4]:
        upper=solve(math.ceil((2**h+delta)*D),list(range(n)),True)
        lower=None
        for nodes in sorted(groups.values(),key=len,reverse=True)[:5]:
            lower=solve(math.floor((2**h-delta)*D),nodes,False)
            if lower:break
        if upper and lower:
            return {'lower':lower,'upper':upper,'display_h_interval':[math.log2(lower['numerator']/D),math.log2(upper['numerator']/D)]}
    return None

results=[]
for file in sorted(out.glob('dfa-*.txt'),key=lambda p:int(p.stem.split('-')[1])):
    w=int(file.stem.split('-')[1]);original=[list(map(int,l.split())) for l in file.read_text().splitlines()]
    if w<first:continue
    tr=minimize(original);depth=30 if w<=26 else 24;words=minimal_words(tr,depth)
    if w in expected:
        assert sorted(words)==sorted(expected[w]),('MINIMAL_WORD_MISMATCH',w)
    for word in words:
        assert run(original,word)<0 and run(original,word[:-1])>=0 and run(original,word[1:])>=0
    basis=forbidden_basis(tr);h=slope(tr);cert=entropy_certificate(tr,h)
    assert cert is not None,('ENTROPY_CERTIFICATE_NOT_FOUND',w)
    reverse=next((s for s in words if run(tr,s[::-1])>=0),None)
    result={'width':w,'dfa':len(original),'minimal_dfa':len(tr),'minimal_words_depth':depth,'minimal_words':words,'forbidden_basis':basis,'finite_slope_estimate':h,'entropy_certificate':cert,'reversal_counterexample':reverse}
    (out/f'analysis-{w}.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/f'min-dfa-{w}.json').write_text(json.dumps(tr)+'\n');results.append(result)
    print('ANALYSIS',w,'minimal DFA',len(tr),'basis infinite',basis['infinite'],'pairs',basis['pair_states'],'h interval',cert['display_h_interval'],'reverse',reverse,flush=True)
    if basis['infinite']:print('PUMP',w,basis['prefix'],basis['cycle'],basis['suffix'],flush=True)
(out/f'analysis-summary-{first}.json').write_text(json.dumps([{k:v for k,v in x.items() if k not in ['minimal_words','entropy_certificate']} for x in results],indent=2)+'\n')
if first==16:assert results[1]['forbidden_basis']['all_words']==['33','3553','3535353']
print('S16_ANALYSIS_PASS',flush=True)
