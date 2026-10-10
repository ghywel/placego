#!/usr/bin/env python3
"""GC998: exact regular spatial-row observer prototype, no free strip boundary.
Predictions were recorded in RULE30-GPT.md before the original run.
Controls PASS; candidate hits600 subset states before minimization while
processing its second visible symbol. No future-pair verdict or invariant.
COMMAND: python3 tests/probes/lexicon/rule30_spatial_row_observer.py
Budget10 seconds, state cap600; no data saved, SAT or width scan.
"""
import time,itertools
END=time.monotonic()+10
CAP=600
truth=(0,1,1,1,1,0,0,0)
def check():
 if time.monotonic()>END:raise RuntimeError('10-second cap')
def minimize(d):
 if d is None:return None
 # Every live state accepts; add the rejecting sink for refinement.
 n=len(d);rows=[[n if q<0 else q for q in row] for row in d]+[[n,n]]
 part=[0]*n+[1]
 while True:
  check();ids={};new=[]
  for i,row in enumerate(rows):
   key=(i<n,tuple(part[q] for q in row))
   if key not in ids:ids[key]=len(ids)
   new.append(ids[key])
  if new==part:break
  part=new
 reps={c:i for i,c in enumerate(part)};dead=part[n];root=part[0]
 if root==dead:return None
 order=[root];index={root:0};out=[]
 for c in order:
  row=[]
  for q in rows[reps[c]]:
   cc=part[q]
   if cc==dead:row.append(-1);continue
   if cc not in index:index[cc]=len(order);order.append(cc)
   row.append(index[cc])
  out.append(row)
 return out

def observe(d,b):
 if d is None or d[0][b]<0:return None
 # New root forbids the other first spatial bit; subsequent bits use d.
 root=[-1,-1];root[b]=d[0][b]+1
 return minimize([root]+[[q+1 if q>=0 else -1 for q in row] for row in d])
def image(d,wall):
 if d is None:return None
 start=frozenset((wall,b,d[0][b]) for b in (0,1) if d[0][b]>=0)
 if not start:return None
 sets=[start];index={start:0};out=[]
 for s in sets:
  check();row=[]
  for bit in (0,1):
   ns=set()
   for left,b,q in s:
    for c in (0,1):
     r=d[q][c]
     if r>=0 and truth[4*left+2*b+c]==bit:ns.add((b,c,r))
   ns=frozenset(ns)
   if not ns:row.append(-1);continue
   if ns not in index:
    if len(sets)==CAP:raise RuntimeError('600-state cap before minimization')
    index[ns]=len(sets);sets.append(ns)
   row.append(index[ns])
  out.append(row)
 return minimize(out)
def accepts(d,w):
 if d is None:return False
 q=0
 for b in w:
  q=d[q][b]
  if q<0:return False
 return True
# Literal controls include a restricted, prefix-closed source language.
for src in ([[0,0]],observe([[0,0]],0)):
 for wall in (0,1):
  im=image(src,wall)
  for n in range(1,5):
   actual=set()
   for w in itertools.product((0,1),repeat=n+1):
    if accepts(src,w):actual.add(tuple(truth[4*(wall if i==0 else w[i-1])+2*w[i]+w[i+1]] for i in range(n)))
   assert actual=={w for w in itertools.product((0,1),repeat=n) if accepts(im,w)}
assert observe(observe([[0,0]],0),1) is None
print('Literal spatial-image/empty-observation controls PASS',flush=True)
for w in ('100010100001010001','101000100001010001'):
 d=[[0,0]];sizes=[]
 try:
  for i,b in enumerate(w):
   d=observe(d,int(b))
   if d is None:print('REJECT',w,'at',i+1,flush=True);break
   if i+1<len(w):d=image(image(d,0),1)
   sizes.append(len(d) if d is not None else 0)
  else:print('ACCEPT',w,'sizes',sizes,flush=True)
 except RuntimeError as e:print('STOP',w,'after',len(sizes),'observations',str(e),'sizes',sizes,flush=True);break
