import itertools,subprocess,re,sys,time
from wall_replay import feasible  # run from tests/probes
words=[]
for bits in itertools.product('AB',repeat=11):
    w=''.join(bits)
    if 'BB' in w or 'AAA' in w: continue
    words.append(w)
t0=time.time(); bad=[]; 
for w in words:
    r,n=feasible(w)
    if not r: bad.append(w)
    print(w,r,n,round(time.time()-t0,1),flush=True)
    if time.time()-t0>200: print('time cap'); break
print('infeasible',bad)
