#!/usr/bin/env python3
"""GC1008: finite affine-consistency obstruction for S/L renewal pulses.
Predictions in RULE30-GPT.md. Four obstruction prefixes are actual visible
words by L578 complete lists; no infinite realization or record bound.
Literal inverse controls.
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

# Scope check against Local's complete actual phase lists (L578), no SAT.
from pathlib import Path
import re
handoff=Path('tests/probes/lexicon/rule30_visible_language_handoff.md').read_text()
def listed(section):
 return {w for line in section.splitlines()
         if re.fullmatch(r'\s+[01]+(?:\s+[01]+)*\s*',line)
         for w in line.split()}
W=listed(handoff.split('## 3.')[1].split('## 4.')[0])
A=listed(handoff.split('### 4a.')[1].split('### 4b.')[0])
D=listed(handoff.split('### 4b.')[1].split('## 5.')[0])
B=(W-D)|A
assert (len(W),len(A),len(D),len(B))==(771,307,246,832)
assert {w for w in W if len(w)<=10}=={'11','00000','101001','0100101','010010001','0101000101','0101010000'}
for i in selected:
 q=samples[i][0]
 assert q[25]==0
 visible=''.join(str(q[t]) for t in range(0,25,2))
 assert len(visible)==13
 membership=tuple(not any(f in visible for f in F) for F in (W,B))
 print('Actual visible',visible,'W/B',membership)
 assert membership==(True,True)
print('Actual four-prefix scope PASS using complete published lists; no infinite closure claim')
