"""CL198 macro-assisted pinning diagnostic, preregistered in RULE30-GPT.
Bears on Q6: explain the 24-cell pinning for the verified 45-bit cut.
Record searched: GC1027, GC1029, W283, CL198. New evidence: reported pinning.
P1: proved slab/packet macro premises allow unary propagation to pin row30.
C0: unstrengthened baseline; C1: leading-1 control remains nonempty.
Unexpected: check every macro premise on CL193's actual shifted packet.
REFUTED-BY: strengthened row30 still has unresolved cells. Stop, no sweep.
OUTCOME: P1 REFUTED: all three cases give 1 followed by 23 question marks.
Controls PASS. Initial harness used horizon86, too short for full packet
rows; failed with KeyError, then corrected to92 before substantive output.
Not a satisfiability verdict. CL198's pinning still needs its own proof.
Run from repository root: python3 tests/probes/lexicon/rule30_train_macro_pinning.py
"""
from collections import deque
from itertools import product
import sys
sys.path.insert(0,'tests/probes/lexicon')
from rule30_train_exit_packet import ROWS
TRUTH=(0,1,1,1,1,0,0,0)
def run(lead,macro):
 w=lead+'00010001010000'+'10'*10+'001000010';h=92
 dom={(t,i):3 for t in range(h+1) for i in range(h-t+2)}
 for t in range(h+1):dom[t,0]=1<<(t%2)
 for k,b in enumerate(w):dom[2*k,1]=1<<int(b)
 rows=tuple((a,b,c,TRUTH[4*a+2*b+c]) for a,b,c in product((0,1),repeat=3))
 cons=[(((t,i-1),(t,i),(t,i+1),(t+1,i)),rows) for t in range(h) for i in range(1,h-t+1)]
 if macro:
  for t in range(34,63,4):
   for i,b in enumerate('100110',1):dom[t,i]&=1<<int(b)
   dom[t,7]&=1<<int(t==62)
  for dt,rs in enumerate(ROWS):
   cons.append((tuple((62+dt,i) for i in range(1,8)),tuple(tuple((r>>j)&1 for j in range(7)) for r in rs)))
 watch={v:[] for v in dom}
 for j,(vs,_) in enumerate(cons):
  for v in vs:watch[v].append(j)
 queue=deque(range(len(cons)));pending=set(queue)
 while queue:
  j=queue.popleft();pending.remove(j);vs,rs=cons[j]
  ok=[r for r in rs if all(dom[v]&(1<<b) for v,b in zip(vs,r))]
  if not ok:return None
  for k,v in enumerate(vs):
   d=sum(1<<b for b in {r[k] for r in ok})
   if d!=dom[v]:
    dom[v]=d
    for n in watch[v]:
     if n not in pending:pending.add(n);queue.append(n)
 return dom
def check_macro_premises():
 seed='01111110011101010011000110001100100101111011001001101000101001111011100010100110111010000000000000000'
 r=list(map(int,seed))+[0]*110
 history=[]
 for t in range(97):
  history.append(r)
  p=[t%2]+r
  r=[(30>>(4*p[i]+2*p[i+1]+p[i+2]))&1 for i in range(len(r)-1)]
 for t in range(46,75,4):
  assert history[t][:6]==list(map(int,'100110'))
  assert history[t][6]==int(t==74)
 for dt,rs in enumerate(ROWS):
  assert sum(b<<j for j,b in enumerate(history[74+dt][:7])) in rs
 print('PASS actual shifted macro premises')

if __name__=='__main__':
 check_macro_premises()
 for lead,macro in [('0',False),('0',True),('1',True)]:
  d=run(lead,macro);assert d is not None
  print(lead,macro,''.join({1:'0',2:'1',3:'?'}[d[30,i]] for i in range(1,25)))
