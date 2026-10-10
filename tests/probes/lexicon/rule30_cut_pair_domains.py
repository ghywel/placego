"""GC1029 pair-domain diagnostic (2026-10-10).
Bears on Q6: explaining the verified 45-bit actual-language cut.
Preregistered in RULE30-GPT.md before the scratch implementation ran.
Record searched: f46 domain/affine probes and GC1028/1029; no recorded
pair-domain proof of this cut. New evidence: explicit final-bit states
and CL197's separate two-cell obstruction.

P1 (low confidence): pair projection consistency refutes q T^10 v.
C0: 11 is refuted. C1: the independently simulated q T^13 v survives.
Unexpected control: its actual assignment survives every retained domain.
Counterfactual: a nonempty fixed point refutes P1, not the checked absence.
REFUTED-BY: target remains nonempty after all projections stabilize.
OUTCOME: P1 REFUTED. Target: 4094 unary domains, 3668 unresolved;
19668 pair domains, 17456 unrestricted; 5287 gate visits.
Positive: 5252 unary domains, 4739 unresolved; 25350 pair domains,
22697 unrestricted; 6732 visits. Both controls PASS.
Stop: no larger clusters or parameter sweep. Nonempty is inconclusive.
Run: python3 tests/probes/lexicon/rule30_cut_pair_domains.py
"""
from collections import deque,defaultdict
from itertools import combinations,product
PAIRS=list(combinations(range(4),2))
ROWS=[(a,b,c,a^(b|c)) for a,b,c in product(range(2),repeat=3)]
def solve(w):
 h=2*len(w)-2
 nodes=[(t,i) for t in range(h+1) for i in range(h-t+2)]
 dom={v:3 for v in nodes}
 for t in range(h+1):dom[t,0]=1<<(t%2)
 for k,b in enumerate(w):dom[2*k,1]=1<<int(b)
 gates=[((t,i-1),(t,i),(t,i+1),(t+1,i)) for t in range(h) for i in range(1,h-t+1)]
 pairs={}; watch=defaultdict(set)
 for j,g in enumerate(gates):
  for v in g:watch[('v',v)].add(j)
  for a,b in PAIRS:
   key=(g[a],g[b]); pairs[key]=15;watch[('p',key)].add(j)
 q=deque(range(len(gates)));pending=set(q);steps=0
 while q:
  j=q.popleft();pending.remove(j);g=gates[j];steps+=1
  ok=[r for r in ROWS if all(dom[v]&(1<<r[k]) for k,v in enumerate(g)) and all(pairs[g[a],g[b]] & (1<<(2*r[a]+r[b])) for a,b in PAIRS)]
  if not ok:return None,steps
  updates=[]
  for k,v in enumerate(g):
   m=sum(1<<x for x in {r[k] for r in ok})
   if m!=dom[v]: dom[v]=m;updates.append(('v',v))
  for a,b in PAIRS:
   key=(g[a],g[b]);m=sum(1<<x for x in {2*r[a]+r[b] for r in ok})
   if m!=pairs[key]:pairs[key]=m;updates.append(('p',key))
  for u in updates:
   for k in watch[u]:
    if k not in pending:pending.add(k);q.append(k)
 return (dom,pairs),steps
if __name__=='__main__':
 assert solve('11')[0] is None
 q='000010001010000';v='0010000101'
 for label,w in [('cut',q+'10'*10+v),('positive',q+'10'*13+v)]:
  result,n=solve(w)
  print(label,'EMPTY' if result is None else ('OPEN',len(result[0]),sum(m==3 for m in result[0].values()),len(result[1]),sum(m==15 for m in result[1].values())),'gate visits',n,flush=True)
  if label=='positive':
   assert result is not None
   seed='01111110011101010011000110001100100101111011001001101000101001111011100010100110111010000000000000000'
   actual={};r=list(map(int,seed));h=2*len(w)-2
   for t in range(h+1):
    actual[t,0]=t%2
    for i,b in enumerate(r,1):actual[t,i]=b
    p=[t%2]+r
    r=[(30>>(4*p[j]+2*p[j+1]+p[j+2]))&1 for j in range(len(r)-1)]
   dom,pairs=result
   assert all(mask&(1<<actual[key]) for key,mask in dom.items())
   assert all(mask&(1<<(2*actual[a]+actual[b])) for (a,b),mask in pairs.items())
   print('PASS positive actual assignment in every unary and pair domain;11 negative control')
