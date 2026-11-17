#!/usr/bin/env python3
"""replay_portal.py FILE (Local, L1548): an independent replay in plain Python of every finite claim in the portal form, from the literals in the file. No Lean, and none of the Lean's number tricks:
cells are lists, the backward tick is the inverse rule cell by cell. Checks closure, phases, letters, rain, ranks, the shields, and the entry row by forward ticks."""
import re,sys
s=open(sys.argv[1],encoding='utf-8').read()
A=[0,0,1,1,1,1,0,0,0,1,1]; B=[0,1,0,1,1,1,0,0,0,1,1]
def cells(n,W): return [(n>>i)&1 for i in range(W)]
def back(p1,p2,l):
    o=[]
    for b in l:
        z=b^(p1|p2); o.append(z); p2=p1; p1=z
    return o
def inp(w):
    assert w[-1]==1
    t=[]; b=1
    for _ in range(7): t.append(b); b^=1
    return w[:-1]+t
def image(w,p1,p2):
    W=len(w); i=inp(w); r=back(p1,p2,i)
    # rain resumes: cells W+2, W+3, W+4 alternate; cells W+4, W+5 are the complements of the input
    assert r[W+3]==1-r[W+2] and r[W+4]==1-r[W+3] and r[W+4]==1-i[W+4] and r[W+5]==1-i[W+5]
    return r[3:3+W]
def parse_lock(name):
    a=s.index(f'namespace {name}\n'); b=s.index(f'end {name}\n')
    t=s[a:b]
    m=re.search(r'def Ph : List \(List Nat\) := \[(.*?)\]\n\n',t,re.S).group(1)
    return [[int(x) for x in re.findall(r'\d+',p)] for p in re.findall(r'\[([^\[\]]*)\]',m+']')]
def F(b,u,v): return [0,b,1-b,1,u,1,0,v,0,1]
Fs=[F(b,u,v) for b in (0,1) for u in (0,1) for v in (0,1)]
tot=0
for name,W,let in (('LockAB',45,'AB'),('LockAAB',136,'AAB'),('LockThird',175,'BAABAA')):
    ph=parse_lock(name); k=len(ph); assert k==len(let),(name,k)
    for r,p in enumerate(ph):
        for n in p:
            w=cells(n,W); assert n>>(W-1)==1
            assert w[-11:]==(A if let[r]=='A' else B),(name,r)
            for p1 in (0,1):
                for p2 in (0,1):
                    im=image(w,p1,p2)
                    v=sum(c<<i for i,c in enumerate(im))
                    assert v in ph[(r+1)%k],(name,r,n); tot+=1
    allw=[cells(n,W) for p in ph for n in p]
    deep=[d for d in range(W-9) if all(w[d:d+10] in Fs for w in allw)]
    print(name,'windows',len(allw),'phases',k,'letters',let,'depths with a reset word in every window',deep)
# cloud
t=re.search(r'def tree : Tree := (.*)',s).group(1)
toks=re.findall(r'\(|\)|\.n|\.e|\d+',t)
pos=[0]
def node():
    if toks[pos[0]]=='(':
        pos[0]+=1; r=node(); assert toks[pos[0]]==')'; pos[0]+=1; return r
    if toks[pos[0]]=='.e':
        pos[0]+=1; return []
    assert toks[pos[0]]=='.n'; pos[0]+=1
    l=node(); v=int(toks[pos[0]]); r=int(toks[pos[0]+1]); pos[0]+=2; g=node()
    return l+[(v,r)]+g
rk=dict(node())
ph=parse_lock('LockAB'); ab={n for p in ph for n in p}
assert len(rk)==798
for n,r in rk.items():
    assert 1<=r<=17 and n not in ab and n>>44==1 and (n>>34) in (1596,1594)
    for p1 in (0,1):
        for p2 in (0,1):
            im=image(cells(n,45),p1,p2)
            v=sum(c<<i for i,c in enumerate(im))
            assert v in rk
            if v>>34!=n>>34: assert rk[v]+1<=r
            tot+=1
print('cloud',len(rk),'max rank',max(rk.values()),'images checked in all',tot)
# entry
E=int(re.search(r'def E : Nat := (0x[0-9a-f]+)',s).group(1),16)
LB=int(re.search(r'def LB : Nat := (0x[0-9a-f]+)',s).group(1),16)
N=850
row=[(E>>i)&1 for i in range(N)]
assert row[0]==1 and all(row[j+1]!=row[j] for j in range(569,N-1))
assert row[568]==row[569]
def fwd(r):
    return [r[0],r[1]^r[0]]+[r[j]^(r[j-1]|r[j-2]) for j in range(2,len(r))]
rows=[row]
for k in range(110): rows.append(fwd(rows[-1]))
ls=''
for k in range(111):
    w=rows[k][229+3*(110-k):229+3*(110-k)+11]
    ch='B' if (LB>>k)&1 else 'A'
    assert w==(B if ch=='B' else A),k
    ls+=ch
th=parse_lock('LockThird'); tw={n for p in th for n in p}
val=lambda c: sum(b<<i for i,b in enumerate(c))
assert val(rows[97][234:234+45]) in rk
assert val(rows[6][377:377+175]) in tw and val(rows[7][374:374+175]) not in tw
r110=rows[110]; assert all(r110[j+1]!=r110[j] for j in range(239,789))
inlock=[k for k in range(0,20) if val(rows[k][377+3*(6-k):377+3*(6-k)+175]) in tw]
print('entry letters, tick 0 first:',ls)
print('ticks 0..19 with the top 175 cells in the third lock:',inlock)
print('ticks in the cloud:',[k for k in range(111) if val(rows[k][234+3*(97-k):234+3*(97-k)+45]) in rk][-3:],'are the last three; count',sum(val(rows[k][234+3*(97-k):234+3*(97-k)+45]) in rk for k in range(98 if False else 111)))
print('REPLAY OK')
