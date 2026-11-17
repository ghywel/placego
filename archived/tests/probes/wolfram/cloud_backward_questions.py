#!/usr/bin/env python3
"""GC2262: exact white-right inverse tails through40, roots<=12bits; P128 graph pilot."""
import json,os,resource,time,hashlib
from pathlib import Path
OUT=Path(os.environ['CAPPED_OUT']);assert resource.getrlimit(resource.RLIMIT_CPU)==(120,120)
start=time.process_time()
def save(n,x):
 (OUT/n).write_text(json.dumps(x,indent=2)+'\n');print(n,'saved',flush=True)
def least(word):
 n=len(word);pi=[0]*n
 for i in range(1,n):
  j=pi[i-1]
  while j and word[i]!=word[j]:j=pi[j-1]
  if word[i]==word[j]:j+=1
  pi[i]=j
 p=n-pi[-1]
 return p if n%p==0 else n
def inv(row):
 head,tail=row;h=len(head);p=len(tail);seen={};out=bytearray();u=v=0;k=0
 assert h<=16384 and p<=12288,('input_cap',h,p)
 while True:
  if k>=h:
   key=((k-h)%p,u,v)
   if key in seen: a=seen[key];break
   seen[key]=k
  y=head[k] if k<h else tail[(k-h)%p]
  z=y^(u|v);out.append(z);u,v=z,u;k+=1
  assert k<=65536,('state_cap',h,p)
 q=least(out[a:]);assert q<=12288,('period_cap',q)
 while a and out[a-1]==out[a-1+q]:a-=1
 new=(bytes(out[:a]),bytes(out[a:a+q]));assert a<=16384
 # Independent whole infinite seam audit: the local relation reduces to prefix plus an lcm cycle.
 H=max(len(new[0])+2,h);Q=max(p,q) if max(p,q)%min(p,q)==0 else p*q
 def val(r,i):
  if i<0:return 0
  return r[0][i] if i<len(r[0]) else r[1][(i-len(r[0]))%len(r[1])]
 for i in range(H+Q+2):assert val(new,i)^(val(new,i-1)|val(new,i-2))==val(row,i)
 return new
# Exact controls and inverse periodic-driver exception.
a=inv((b'\x01',b'\x00'));b=inv(a)
assert a==(b'',b'\x01') and len(b[1])==3
for tt in [b'\x00',b'\x01']:
 for pair in range(4):
  u,v=pair>>1,pair&1;seen={};i=0
  while (u,v) not in seen:seen[u,v]=i;u,v=tt[0]^(u|v),u;i+=1
  assert i-seen[u,v] in ([1] if tt==b'\x00' else [3])
# Every mixed driver through length8: finite return maps, fixed/swap cases and rank guard.
return_maps=[]
for p in range(2,9):
 for word in range(1,(1<<p)-1):
  F=[]
  for pair in range(4):
   u,v=pair>>1,pair&1
   for i in range(p):u,v=((word>>i)&1)^(u|v),u
   F.append(2*u+v)
  cycles=[];seen_states=set()
  for z in range(4):
   trail=[];x=z
   while x not in trail:
    trail.append(x);x=F[x]
   cyc=trail[trail.index(x):];key=tuple(sorted(cyc))
   if key not in cycles:cycles.append(key)
  assert all(len(c)<=2 for c in cycles)
  assert not ({1,2}<=set(map(len,cycles)))
  if len(cycles)>1:return_maps.append({'driver_bits':[(word>>i)&1 for i in range(p)],'return_map':F,'cycles':cycles})
save('mixed_driver_branches.json',return_maps)
roots={};mapping=[]
for seed in range(1,1<<12,2):
 row=(bytes((seed>>i)&1 for i in range(seed.bit_length())),b'\x00');d=0
 while True:
  nxt=inv(row)
  if nxt[1]!=b'\x00':break
  row=nxt;d+=1;assert d<=5
 root=sum(v<<i for i,v in enumerate(row[0]));roots[root]=row
 mapping.append([seed,root,d])
records=[];groups={};maxp=maxh=0
for k,(root,row) in enumerate(roots.items()):
 periods=[];prefixes=[]
 for d in range(40):
  row=inv(row);periods.append(len(row[1]));prefixes.append(len(row[0]));maxp=max(maxp,len(row[1]));maxh=max(maxh,len(row[0]))
 key=tuple(periods);groups.setdefault(key,[]).append(root)
 records.append({'root':root,'periods':periods,'prefix_lengths':prefixes,'final_head_hex':row[0].hex(),'final_tail_hex':row[1].hex()})
 if k%128==0: print('roots',k,'cpu',round(time.process_time()-start,2),flush=True)
save('backward_roots.json',{'records':records,'input_to_root':mapping,'max_period':maxp,'max_prefix':maxh,'groups':[{'periods':list(p),'count':len(r),'representatives':r[:8]} for p,r in groups.items()]})
# Compare retained exact A/B tail certificates, no new A/B ancestry search.
p=Path('/private/tmp/gc2020-crystal-fronts/certificates.json');raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='a3f887f8e55051b25d1d8d2173e9a6711ebce33c6396053f1b08e01c918d934b'
c=json.loads(raw);compare={}
for name in ('a','b'):
 seq=[r['left_period'] for r in c['rows'][name]]
 compare[name]={'period_changes':[[i,x] for i,x in enumerate(seq) if i==0 or x!=seq[i-1]],'root_first40':seq[1:41]}
assert records[0]['root']==1 and records[0]['periods']==compare['a']['root_first40']
save('retained_AB_periods.json',compare)
# New P128 closure attempt, explicit finite state budget, never silently truncate then claim closure.
def graph(P,cap):
 M=(1<<P)-1;states=[(0,M)];idx={states[0]:0};i=0;exits=0
 while i<len(states):
  a,b=states[i];g=a|b
  if g.bit_count()&1:exits+=1;i+=1;continue
  c=(g<<1)&M;d=1
  while d<P:c^=(c<<d)&M;d*=2
  for z in (c,c^M):
   v=(b,z)
   if v not in idx:
    if len(states)==cap:return {'period':P,'status':'STATE_CAP_NOT_CLOSED','states':len(states),'processed':i,'frontier':len(states)-i,'exits':exits}
    idx[v]=len(states);states.append(v)
  i+=1
 return {'period':P,'status':'CLOSED','states':len(states),'processed':i,'frontier':0,'exits':exits}
assert graph(16,1000)['states']==67
r=graph(128,200000);save('period128_pilot.json',r)
save('summary.json',{'status':'PASS_WITH_GRAPH_DISPOSITION','roots':len(records),'sequence_groups':len(groups),'max_period':maxp,'max_prefix':maxh,'graph':r,'payload_cpu_s':time.process_time()-start})
