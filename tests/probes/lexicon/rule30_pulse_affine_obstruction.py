#!/usr/bin/env python3
"""GC1008: finite affine-consistency obstruction for S/L renewal pulses.
Predictions in RULE30-GPT.md. Necessary renewal syntax, not actual right
realization; no all-depth or record claim. Literal inverse controls.
"""
T=(0,1,1,1,1,0,0,0)
N=32
samples=[]
def generate(times):
 if times[-1]>=N:
  pulse=[int(t in times) for t in range(N)]
  prev=[t%2 for t in range(N)];cur=[1-b for b in pulse];bits=[]
  for d in range(N):
   bits.append(cur[0]);nxt=[cur[t+1]^(cur[t]|prev[t]) for t in range(len(cur)-1)]
   assert all(T[4*nxt[t]+2*cur[t]+prev[t]]==cur[t+1] for t in range(len(nxt)))
   prev,cur=cur,nxt
  samples.append((pulse,bits))
 else:
  for g in (6,10):generate(times+[times[-1]+g])
generate([0])
# Deduplicate prefixes crossing the terminal horizon with different final gaps.
samples=list({tuple(q): (q,b) for q,b in samples}.values())
for d in range(1,N+1):
 pivots={};failure=None
 for i,(q,b) in enumerate(samples):
  x=1+sum(v<<(t+1) for t,v in enumerate(q[:d]));y=b[d-1];w=1<<i
  while x:
   k=x.bit_length()-1
   if k not in pivots:pivots[k]=(x,y,w);break
   a,c,z=pivots[k];x^=a;y^=c;w^=z
  if not x and y:failure=w;break
 if failure is not None:
  selected=[i for i in range(len(samples)) if failure>>i&1]
  assert len(selected)%2==0
  assert all(sum(samples[i][0][t] for i in selected)%2==0 for t in range(d))
  assert sum(samples[i][1][d-1] for i in selected)%2==1
  assert d==26 and len(selected)==4
  print('Affine closure fails first at depth',d,'samples',len(samples),'dependency',len(selected))
  for i in selected:print([t for t,v in enumerate(samples[i][0][:d]) if v], samples[i][1][d-1])
  break
else:print('No affine obstruction through32; no global inference')
