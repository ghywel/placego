#!/usr/bin/env python3
"""GC359: targeted entry26 review, CPU Python, no m17..20 or real-data replay.
Checks F19 vs F20, all start phases, 133-observation boundary, local truth table.
The initial F19 prediction was recorded before execution. The stricter timing
boundary was a post-reading unexpected guard, not a blind prediction.
Shared automaton imports are disclosed; literal truth-table control is separate.
COMMAND: python3 tests/probes/lexicon/rule30_kick_review.py
Data outside Git. Prior executions totaled about16.3 CPU seconds; no new run here.
"""
import sys,time,json
sys.path.insert(0,'tests/probes/lexicon')
import rule30_kick_layers as k
m=16;t0=time.process_time()
sets=k.settled(m,k.step_row)
out={}
for f in [19,20]:
 k.F=f;out[f]=k.kicks_from(sets,m,k.step_row)
print(json.dumps(dict(alphabets=out,cpu=time.process_time()-t0),sort_keys=True),flush=True)
# Check arbitrary starting phase against the settled slice at that phase.
maxn=0;bad=[]
for start in range(k.P):
 S=set(range(1<<(m-1)))
 for n in range(225):
  phase=(start+n)%k.P
  if S==sets[phase]:maxn=max(maxn,n);break
  if n==224:bad.append(start);break
  S=k.advance(S,phase,m,k.U[phase],k.U[(phase+1)%k.P],k.step_row)
print(json.dumps(dict(max_transitions_to_settled=maxn,unsettled=bad,cpu=time.process_time()-t0)),flush=True)

import sys,json,time
sys.path.insert(0,'tests/probes/lexicon')
import rule30_kick_layers as k
m=16;tt=time.process_time();sets=[set() for _ in range(k.P)]
for start in range(k.P):
 S=set(range(1<<(m-1)))
 for n in range(132):
  t=(start+n)%k.P;S=k.advance(S,t,m,k.U[t],k.U[(t+1)%k.P],k.step_row)
 sets[(start+132)%k.P]|=S
k.F=19
print(json.dumps(dict(after133_observations=k.kicks_from(sets,m,k.step_row),cpu=time.process_time()-tt)),flush=True)
one=k.one_turn_sets(m,k.step_row);out={}
for f in [19,20]:k.F=f;out[f]=k.kicks_from(one,m,k.step_row)
print(json.dumps(dict(one_turn=out,cpu=time.process_time()-tt)),flush=True)
# Independent local truth-table control for hidden row and observed edge.
for m in [4,5]:
 for h in range(1<<(m-1)):
  for t in [0,1]:
   for c in [0,1]:
    for inp in [0,1]:
     cells=[t,c]+[(h>>i)&1 for i in range(m-1)]+[inp]
     new=[cells[i-1]^(cells[i]|cells[i+1]) for i in range(1,m+1)]
     assert k.step_row(h,t,m,inp,c)==(sum(new[i]<<(i-1) for i in range(1,m)),new[0])
print('independent truth-table PASS',flush=True)
