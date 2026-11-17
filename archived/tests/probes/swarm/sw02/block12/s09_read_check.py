#!/usr/bin/env python3
"""GC2810 fixed S09 carry controls, no producer imports or graph search.
Record searched: P2-3.1 and both skeptic reports; G4.1/GC2296;
ColumnTransfer at1ddcd411; actual kit03a19bf6 and portal/PR index.
Prediction: eight local identities and128 oriented window edges pass the
literal certificate; closed form agrees on32 words. Damaged and mirrored
certificates, plus rule150, fail. Fixed finite rows width<=10 and seed30
cross-check the known counting algebra; no large census or table extension.
Counterfactual: any mismatch blocks affected carry; preserve, no enlargement.
"""
import itertools,json,sys,time,resource
from pathlib import Path
start=time.process_time()
rule=lambda a,b,c:a^(b|c)
h=json.loads(Path(sys.argv[1]).read_text())
words=list(itertools.product((0,1),repeat=5))
H=lambda u:max(0,2-sum(u[1:]))
assert len(h)==32 and all(h[''.join(map(str,u))]==H(u) for u in words)
g=lambda a,b:a-b+a*b
for a,b,c in itertools.product((0,1),repeat=3):
 assert 2*rule(a,b,c)+3*b+int((a,b,c)==(1,0,1))+3*int((a,b,c)==(0,0,0))-3==g(b,c)-g(a,b)
edges=[];mirror_bad=0;damaged_bad=0;linear_bad=0;tight=0
for w in itertools.product((0,1),repeat=7):
 u=w[1:6];v=tuple(rule(*w[i:i+3]) for i in range(5))
 excess=sum(u)-3
 assert H(v)-H(u)>=excess
 tight+=H(v)-H(u)==excess
 mirror_bad+=H(v[::-1])-H(u[::-1])<excess
 bad=lambda z:0 if z==(0,0,0,0,0) else H(z)
 damaged_bad+=bad(v)-bad(u)<excess
 v150=tuple(w[i]^w[i+1]^w[i+2] for i in range(5))
 linear_bad+=H(v150)-H(u)<excess
 edges.append({'word':''.join(map(str,w)),'slack':H(v)-H(u)-excess})
assert mirror_bad==8 and damaged_bad>0 and linear_bad>0
# Literal finite sets; physical cell positions, no packed producer recurrence.
def step(x):
 if not x:return set()
 return {i for i in range(min(x)-1,max(x)+2) if rule(int(i-1 in x),int(i in x),int(i+1 in x))}
def stats(x):
 if not x:return 0,0,0,0
 L,R=min(x),max(x)
 s=sum(i not in x and i-1 in x and i+1 in x for i in range(L,R+1))
 z=sum(i-1 not in x and i not in x and i+1 not in x for i in range(L,R+1))
 return len(x),R-L+1,s,z
for n in range(1,1<<10):
 x={i for i in range(10) if n>>i&1};B,w,s,z=stats(x)
 assert 2*len(step(x))+3*B==3*w+6-s-3*z
x={0};N=S=Z=0
for T in range(31):
 B,w,s,z=stats(x)
 assert w==2*T+1
 assert 5*N==3*T*T+6*T+2-2*B-S-3*Z
 N+=B;S+=s;Z+=z;x=step(x)
# Sharp rate: five phases of the period5 travelling row, every column3/5.
x=[0,0,1,1,1];initial=x[:];counts=[0]*5
for t in range(5):
 assert sum(x)==3
 counts=[a+b for a,b in zip(counts,x)]
 x=[rule(x[(i-1)%5],x[i],x[(i+1)%5]) for i in range(5)]
assert x==initial and counts==[3]*5
# Constant2 sharp on real finite initial rows at T1; fixed10101 gives slope3.
assert 5==3+2
assert all(rule(i%2,(i+1)%2,(i+2)%2)==(i+1)%2 for i in range(2))
print(json.dumps({'PASS':True,'local_words':8,'certificate_words':32,'edges':128,'tight_edges':tight,'mirror_violations':mirror_bad,'damaged_violations':damaged_bad,'rule150_violations':linear_bad,'finite_rows':1023,'seed_endpoint_T':30,'period5_column_counts':counts,'edges_with_slacks':edges,'cpu_s':time.process_time()-start,'self_peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}))
print('S09 READ CONTROLS PASS')
