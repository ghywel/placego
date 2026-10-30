#!/usr/bin/env python3
"""GC2267: fixed40-depth complete spatial-tail predecessor graph, not a root census."""
import json,os,resource,time,hashlib,itertools
from pathlib import Path
OUT=Path(os.environ['CAPPED_OUT']);assert resource.getrlimit(resource.RLIMIT_CPU)==(30,30)
start=time.process_time()
def least(w):
 n=len(w)
 for p in range(1,n+1):
  if n%p==0 and all(w[i]==w[i%p] for i in range(n)):return w[:p]
def canon(w):
 w=least(w);n=len(w);s=w+w;i=0;j=1;k=0
 while i<n and j<n and k<n:
  if s[i+k]==s[j+k]:k+=1;continue
  if s[i+k]>s[j+k]:i+=k+1;i+=i==j
  else:j+=k+1;j+=i==j
  k=0
 a=min(i,j);r=s[a:a+n]
 if n<=64:assert r==min(w[t:]+w[:t] for t in range(n))
 return r
def parents(w):
 F=[]
 for state in range(4):
  u,v=state>>1,state&1
  for y in w:u,v=y^(u|v),u
  F.append(2*u+v)
 C=set();out=set()
 for s in range(4):
  walk=[];z=s
  while z not in walk:walk.append(z);z=F[z]
  cycle=walk[walk.index(z):];key=tuple(sorted(cycle))
  if key in C:continue
  C.add(key);u,v=cycle[0]>>1,cycle[0]&1;a=[]
  for _ in cycle:
   for y in w:u,v=y^(u|v),u;a.append(u)
  assert all(a[i]^(a[i-1]|a[i-2])==w[i%len(w)] for i in range(len(a)))
  out.add(canon(tuple(a)))
 return out
# Independent literal ring enumeration of every driver of length<=4.
checks=0
for p in range(1,5):
 for w in itertools.product((0,1),repeat=p):
  w=tuple(w);literal=set()
  for q in (p,2*p,3*p):
   for a in itertools.product((0,1),repeat=q):
    if all(a[i]^(a[i-1]|a[i-2])==w[i%p] for i in range(q)):literal.add(canon(a))
  assert parents(w)==literal,(w,parents(w),literal)
  checks+=1
src=Path('/private/tmp/gc2262-backward/backward_roots.json');raw=src.read_bytes()
assert hashlib.sha256(raw).hexdigest()==os.environ['ROOT_RECEIPT_SHA256']
roots=json.loads(raw)
layer={(1,):{(1,)}};levels=[];edges=[]
for depth in range(1,41):
 assert len(layer)<=4096 and sum(map(len,layer.values()))<=4096
 levels.append({'depth':depth,'profiles':len(layer),'period_sequences':len(set().union(*layer.values())),'max_period':max(map(len,layer))})
 if depth==40:break
 nxt={}
 for w,seqs in layer.items():
  assert len(w)<=12288
  for a in parents(w):
   edges.append({'depth':depth,'child':''.join(map(str,w)),'parent':''.join(map(str,a))})
   nxt.setdefault(a,set()).update(s+(len(a),) for s in seqs)
 layer=nxt
sequences=set().union(*layer.values())
for r in roots['records']:assert tuple(r['periods']) in sequences
result={'status':'PASS','literal_driver_controls':checks,'levels':levels,'edges':edges,'period_sequences':[list(s) for s in sorted(sequences)],'final_profiles':[''.join(map(str,w)) for w in layer],'payload_cpu_s':time.process_time()-start}
(OUT/'background_closure.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS sequence_count',len(sequences),'profiles',len(layer),'CPU',result['payload_cpu_s'])
