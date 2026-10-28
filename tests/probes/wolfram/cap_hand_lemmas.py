#!/usr/bin/env python3
"""GC2037 independent checks of the relaxed hand lemma, not another cap scan."""
import hashlib,itertools,json,os
from pathlib import Path
TRUTH=(0,1,1,1,1,0,0,0)
def evolve(w,t,literal=True):
 a=list(map(int,w))
 for _ in range(t):a=[TRUTH[4*l+2*c+r] if literal else l^(c|r) for l,c,r in zip(a,a[1:],a[2:])]
 return ''.join(map(str,a))
def pre(w):
 out=[]
 for u,v in itertools.product((0,1),repeat=2):
  a=[0]*len(w)+[u,v]
  for j in reversed(range(len(w))):a[j]=int(w[j])^(a[j+1]|a[j+2])
  s=''.join(map(str,a));assert evolve(s,1)==w;out.append(s)
 return out
prefixes=['01001','01010','01011','11100','11101'];count=0
for p in prefixes:
 for tail in itertools.product('01',repeat=8):
  w=p+''.join(tail);two=evolve(w,2);four=evolve(w,4)
  assert four==evolve(w,4,False)
  assert two[:3] not in ('001','100')
  assert two[:6]!='010011'
  assert four!='00010';count+=1
for v in itertools.product('01',repeat=3):
 w='01111110'+''.join(v);r=str(1-int(v[0]));assert evolve(w,3)=='10'+r+'1'+str(1-int(r))
anc=['00010']
for _ in range(4):anc=[p for w in anc for p in pre(w)]
assert len(anc)==256
counter=next(w for w in anc if w.startswith('01000'))
assert evolve(counter,4)=='00010'
out={'status':'PASS','local_cases':count,'cap_prefix_cases':8,'inverse_cases':340,
     'relaxed_condition_counterexample':counter,'target':'00010',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(Path(os.environ['CAPPED_OUT'])/'result.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
