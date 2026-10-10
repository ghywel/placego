# GC1034 bounded diagnostic, predictions written before execution.
# Missing inference: does CL198's pinned entry strip give an autonomous visible future,
# furnishing a concrete reset state for a hidden representation?
# Record searched: CL198 + strip -> existing finite propagation only (CL198/199).
# P1: its reachable strip sets close in a phase-respecting cycle with singleton outputs.
# OUTCOME: autonomous-output prediction REFUTED at absolute time96 (66 updates),
# 2126 states; all earlier first bits singleton. Literal controls and both retained
# exterior-path replays PASS. Only the arbitrary-exterior relaxation is refuted.
# Eventual synchronization and actual-history uniqueness remain undecided. No sweep.
# Refuted by a time with two attainable first bits; capped at 160 ticks/20000 states.
# Control: packed transition agrees with literal Rule30 on every width8 row/input/phase.
# Counterfactual: a zero width8 strip with zero wall can admit first1 at tick8, not before.
# Unexpected check: retain two complete exterior histories and replay them literally;
# a relaxed-path pair is not claimed to be two actual right-half histories.
def step(s,b,u,w):
 p=s|(u<<w)
 return (((p<<1)|b)^(p|(p>>1)))&((1<<w)-1)
def literal(row,b,u):
 p=[b]+row+[u]
 return [(30>>(4*p[i]+2*p[i+1]+p[i+2]))&1 for i in range(len(row))]
for s in range(256):
 for b in (0,1):
  for u in (0,1):
   r=literal([(s>>i)&1 for i in range(8)],b,u)
   assert step(s,b,u,8)==sum(x<<i for i,x in enumerate(r))
S={0}
for t in range(1,9):
 S={step(s,0,u,8) for s in S for u in (0,1)}
 assert {s&1 for s in S}==({0} if t<8 else {0,1})
word='100110011001100000000010';initial=sum(int(c)<<i for i,c in enumerate(word))
S={initial:0};seen={}; peak=1
for k in range(161):
 t=30+k; out={s&1 for s in S};peak=max(peak,len(S))
 if len(out)>1:
  paths=[]
  for bit in (0,1):
   s=next(s for s in S if s&1==bit);path=S[s];r=list(map(int,word))
   for j in range(k):r=literal(r,(30+j)%2,(path>>j)&1)
   assert r[0]==bit and sum(v<<i for i,v in enumerate(r))==s
   paths.append(format(path,'0%db'%k)[::-1])
  print('FIRST_AMBIGUITY',t,'steps',k,'states',len(S),'peak',peak,'paths',paths);break
 key=(t%2,frozenset(S))
 if key in seen:
  print('CLOSED',seen[key],t,'states',len(S),'peak',peak);break
 seen[key]=t
 if len(S)>20000 or k==160:
  print('CAPPED',t,'states',len(S),'peak',peak);break
 nxt={}
 for s,path in S.items():
  for u in (0,1):nxt.setdefault(step(s,t%2,u,24),path|(u<<k))
 S=nxt
print('CONTROLS PASS')
