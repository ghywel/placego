"""GC693, preregistered7f2a6897: one joint spatial inverse automaton.
Prediction: a finite target with two finite guarded predecessors exists.
Counterfactual: at most one finite branch for every finite guarded target.
Outcome: target100010011, predecessors1100101 and1010011, all zero-tailed.
This is existence reachability, not a seed census or infinite survival claim.
"""
from collections import deque
import json
TABLE=(0,1,1,1,1,0,0,0)
def edge(s,b):
 c0,c,d0,d,a0,a,e0,e=s
 child=(c,b^(c|c0),d,b^(d|d0),a,c^(a|a0),e,d^(e|e0))
 for previous,current,new,output in ((c0,c,child[1],b),(d0,d,child[3],b),
                                   (a0,a,child[5],c),(e0,e,child[7],d)):
  assert TABLE[4*new+2*current+previous]==output
 return child
start=(0,0,0,1,1,1,1,1)
first=edge(start,1)
parents={first:(None,1)};q=deque([first]);found=None
while q:
 s=q.popleft()
 if s==(0,)*8:found=s;break
 for b in (0,1):
  child=edge(s,b)
  if child not in parents:parents[child]=(s,b);q.append(child)
word=[]
if found is not None:
 s=found
 while s is not None:
  s,b=parents[s];word.append(b)
 word.reverse()
def inverse(target,wall,near,n):
 a=[wall,near]
 for i in range(1,n):a.append((target[i-1] if i<=len(target) else 0)^(a[i]|a[i-1]))
 return a[1:]
def forward(a,wall):
 old=[wall]+a+[0,0]
 return [TABLE[4*old[i+1]+2*old[i]+old[i-1]] for i in range(1,len(old)-1)]
cert=None
if word:
 target=word[:]
 while target and not target[-1]:target.pop()
 n=len(word)+16
 mids=[inverse(target,0,c,n) for c in (0,1)]
 olds=[inverse(mid,1,1,n+16) for mid in mids]
 assert all(not any(x[-12:]) for x in mids+olds)
 for a,mid in zip(olds,mids):
  f=forward(a,1);g=forward(f,0)
  assert f[:len(mid)]==mid and not any(f[len(mid):])
  assert g[:len(target)]==target and not any(g[len(target):])
 trim=lambda a: ''.join(map(str,a[:max([0]+[i+1 for i,v in enumerate(a) if v])]))
 cert=dict(target=trim(target),intermediates=[trim(x) for x in mids],predecessors=[trim(x) for x in olds],literal_checks=sum(len(forward(a,1))+len(forward(forward(a,1),0)) for a in olds))
print(json.dumps(dict(visited=len(parents),reachable_zero=found is not None,target_word_length=len(word),certificate=cert),sort_keys=True))
