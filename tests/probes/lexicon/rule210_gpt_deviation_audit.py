"""GC466 independent finite-part UQ audit; base prefix is not certified here.
Prediction: L48 graph has9 surviving deviation states, no irregular even
endpoint or zero return, life3. Shifted background must be rejected.
Independent instrument: decimal Rule210 truth table and integer time vectors.
"""
from collections import deque
L=48
F=lambda l,c,r:(210>>(4*l+2*c+r))&1

def audit(shift=0):
 def bg(c,t):return int((c+shift)%2==1 and (c-t+shift)%3!=0)
 def step(st,d):
  phase,A,B=st;c=601+phase
  v=d
  for t in range(L):
   a,b,r=bg(c-2,t),bg(c-1,t),bg(c,t)
   assert F(a,b,r)==bg(c,t+1)
   p=F(a^((A>>t)&1),b^((B>>t)&1),r^((v>>t)&1))^bg(c,t+1)
   v|=p<<(t+1)
  return ((phase+1)%6,B,v)
 irregular=0;ret=False;graph={};todo=deque()
 for phase in range(6):
  q=step((phase,0,0),1)
  if (q[2]>>L)&1:
   irregular+=int(q[0]%2==0)
  else:todo.append(q)
 while todo:
  st=todo.popleft()
  if st in graph:continue
  graph[st]=[]
  for d in (0,1):
   q=step(st,d)
   if(q[2]>>L)&1:irregular+=int(q[0]%2==0);continue
   if q[1]==q[2]==0:ret=True;continue
   graph[st].append(q);todo.append(q)
 def life(st,path=()):
  assert st not in path,'cycle'
  return 1+max((life(q,path+(st,)) for q in graph[st]),default=0)
 return len(graph),irregular,ret,max(map(life,graph),default=0)
if __name__ == '__main__':
 primary=audit(); shifted=audit(1)
 assert primary==(9,0,False,3)
 assert shifted[1]>0
 print('PASS finite graph',primary,'shifted-background irregularity',shifted[1])
