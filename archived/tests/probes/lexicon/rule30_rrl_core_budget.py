#!/usr/bin/env python3
"""GC986: exact occurrence budget for the 4422 core under K18.
Record searched: RRL|RLK|544222|4,4,2,2 + recurrent|SCC|transient -> GC985 only.
Input: Local RLK25 list published ea0ae954; no language census reproduced.
Prediction: a core-bearing cycle exists. CF: relaxed cycle is physical.
U: add missing word21. Independent controls: exhaustive literal membership
through10, plus explicit edge inequalities for the occurrence-budget potential.
Outcome: prediction REFUTED; no core-bearing cycle with/without word21.
148 reachable product states; max occurrences1, achieved by the core itself.
All controls PASS; finite potential verifies every reachable edge. This is a
computed all-length bound for one motif, not an all-depth white-record bound.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_core_budget.py
"""
import itertools,collections
F=tuple("11 00000 101001 0100101 010010001 0101000101 0101010000 01010001001 10010001001 010010000101 010100010001 100100010000 0001000010001 1001000010001 00100010000101 01000010001001 10101000010000 001000100001001 010000100010000 0101000010000101 1000100001010001 00100010001010100 001000010001010100 010000101000010001 010001000100010101".split())
assert len(F)==25
core='1000100010101'
def graph(F):
 P=sorted({''}|{w[:i] for w in F for i in range(1,len(w))},key=lambda x:(len(x),x))
 D={}
 for p in P:
  for b in '01':
   v=p+b
   if not any(v.endswith(f) for f in F):D[p,b]=max((q for q in P if v.endswith(q)),key=len)
 return P,D
def walk(D,p,w):
 for b in w:
  p=D.get((p,b))
  if p is None:return None
 return p
def path(D,start,end):
 Q=collections.deque([start]);prev={start:None}
 while Q:
  p=Q.popleft()
  if p==end:
   out=''
   while prev[p] is not None:
    p0,b=prev[p];out=b+out;p=p0
   return out
  for b in '01':
   q=D.get((p,b))
   if q is not None and q not in prev:prev[q]=(p,b);Q.append(q)
 return None
for extra in [False,True]:
 fs=F+(('000010001000100010001',) if extra else ())
 P,D=graph(fs)
 for n in range(11):
  for bits in itertools.product('01',repeat=n):
   w=''.join(bits)
   assert (walk(D,'',w) is not None)==(not any(f in w for f in fs))
 candidates=[]
 for p in P:
  if path(D,'',p) is None:continue
  q=walk(D,p,core)
  if q is None:continue
  back=path(D,q,p)
  if back is not None:candidates.append((core+back,p))
 print('extra21',extra,'states',len(P),'cycle candidates',len(candidates))
 if candidates:
  cyc,p=min(candidates,key=lambda x:(len(x[0]),x[0]))
  assert walk(D,p,cyc)==p
  expanded=cyc*((max(map(len,fs))+len(cyc)-1)//len(cyc)+2)
  assert not any(f in expanded for f in fs)
  ones=[i for i,b in enumerate(cyc) if b=='1']
  gaps=[(b-a)%len(cyc) for a,b in zip(ones,ones[1:]+[ones[0]+len(cyc)])]
  print('cycle',cyc,'gaps',gaps,'literal wrap control PASS')
print('adaptive: compute exact maximum occurrences, predicted finite from no core-bearing cycle')
P,D=graph(F)
kprefix=[core[:i] for i in range(len(core))]
start=('', ''); Q=collections.deque([start]);nodes=[start];seen={start};E=[]
while Q:
 node=Q.popleft();p,k=node
 for b in '01':
  q=D.get((p,b))
  if q is None:continue
  v=k+b;reward=int(v.endswith(core));knew=max((x for x in kprefix if v.endswith(x)),key=len)
  target=(q,knew);E.append((node,target,reward,b))
  if target not in seen:seen.add(target);nodes.append(target);Q.append(target)
V={x:-1 for x in nodes};V[start]=0;W={start:''}
for i in range(len(nodes)+1):
 change=False
 for a,b,r,letter in E:
  if V[a]>=0 and V[a]+r>V[b]:V[b]=V[a]+r;W[b]=W[a]+letter;change=True
 if not change:break
else:raise AssertionError('positive cycle')
M=max(V.values());assert M==1;v=min((W[x] for x in nodes if V[x]==M),key=lambda x:(len(x),x))
assert not any(f in v for f in F)
assert sum(v.startswith(core,j) for j in range(len(v)))==M
assert all(V[b]>=V[a]+r for a,b,r,_ in E)
print('product states',len(nodes),'maximum occurrences',M,'witness',v,'fixedpoint iterations',i+1,'edge certificate PASS')
