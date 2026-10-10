#!/usr/bin/env python3
"""GC1007: recurrent 3/5-gap branching under BOTH cutoff40 phase lists.
Predictions in RULE30-GPT.md; uses L578's published handoff, no SAT.
This is a relaxed-language witness, not an actual Rule30 realization.
"""
from pathlib import Path
import re
from collections import deque
s=Path('tests/probes/lexicon/rule30_visible_language_handoff.md').read_text()
def words(section):
 return set(w for line in section.splitlines() if re.fullmatch(r'\s+[01]+(?:\s+[01]+)*\s*',line) for w in line.split())
# Only indented binary-only rows count; gap descriptions have punctuation.
W=words(s.split('## 3.')[1].split('## 4.')[0])
A=words(s.split('### 4a.')[1].split('### 4b.')[0]);D=words(s.split('### 4b.')[1].split('## 5.')[0])
B=(W-D)|A
assert (len(W),len(A),len(D),len(B))==(771,307,246,832)
assert {w for w in W if len(w)<=10}=={'11','00000','101001','0100101','010010001','0101000101','0101010000'}
F=W|B
P={''}|{w[:k] for w in F for k in range(1,len(w))}
cache={}
# Test all ending forbidden factors, not merely complete current string.
def step(q,b):
 key=q,b
 if key in cache:return cache[key]
 t=q+b
 if any(t.endswith(f) for f in F): r=None
 else:
  r=t
  while r not in P:r=r[1:]
 cache[key]=r
 return r

def advance(q,w):
 for b in w:
  q=step(q,b)
  if q is None:return None
 return q
root=advance('','1');nodes=[root];seen={root};edges={};parents={}
for q in nodes:
 edges[q]={}
 for g,code in [('S','001'),('L','00001')]:
  r=advance(q,code)
  if r is not None:
   edges[q][g]=r
   if r not in seen:
    assert len(nodes)<10000
    seen.add(r);nodes.append(r);parents[r]=(q,g)
rev={q:[] for q in nodes}
for q in nodes:
 for r in edges[q].values():rev[r].append(q)
# Small reachable graph: transitive return test yields concrete cycles.
def path(start,end):
 todo=deque([(start,'')]);visit={start}
 while todo:
  q,w=todo.popleft()
  if q==end:return w
  for g,r in edges[q].items():
   if r not in visit:visit.add(r);todo.append((r,w+g))
 return None
for q in nodes:
 loops={g:g+w for g,r in edges[q].items() if (w:=path(r,q)) is not None}
 if len(loops)==2:
  prefix='';r=q
  while r!=root:r,g=parents[r];prefix=g+prefix
  print('Counts PASS; reachable states',len(nodes),'entry',prefix,'state',q,'loops',loops)
  assert all(advance(q,''.join('001' if g=='S' else '00001' for g in w))==q for w in loops.values())
  # Direct substring checks independently of prefix automaton, including joins.
  spell=lambda w:'1'+''.join('001' if g=='S' else '00001' for g in w)
  import itertools
  for choices in itertools.product(('S','L'),repeat=5):
   w=spell(prefix+''.join(loops[g] for g in choices))
   assert not any(f in w for f in F)
  print('32 mixed-loop concatenations pass direct BOTH-phase substring controls')
  break
else:print('Prediction REFUTED: no reachable recurrent branching')
