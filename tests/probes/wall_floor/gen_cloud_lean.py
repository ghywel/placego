#!/usr/bin/env python3
"""gen_cloud_lean.py (Local, L1532): writes TwoPairsWallCloud.lean from E45.txt: the 798 windows of the cloud, closed, disjoint from the lock, with a rank that bounds alternation by 17 letters."""
from collections import defaultdict
import sys
sys.setrecursionlimit(100000)
V=[];part=[];term=[];adj=[]
for l in open('E45.txt'):
    h,p,t,c,a,b,cc,d=l.split()
    V.append(int(h,16)); part.append(int(p)); term.append(int(t)); adj.append((int(a),int(b),int(cc),int(d)))
size=defaultdict(int)
for p in part: size[p]+=1
cloud=max({part[i] for i in range(len(V)) if term[i]},key=lambda p:size[p])
nodes=[i for i in range(len(V)) if part[i]==cloud]
letter=[(V[i]>>34)&2047 for i in range(len(V))]
memo={}
def r(i):
    if i in memo: return memo[i]
    best=1
    for j in set(adj[i]):
        if letter[j]!=letter[i]: best=max(best,r(j)+1)
    memo[i]=best
    return best
ranks={V[i]:r(i) for i in nodes}
print('cloud',len(nodes),'max rank',max(ranks.values()))
sv=sorted(ranks)
CH=40
NC=(len(sv)+CH-1)//CH
def tree(lo,hi):
    if lo>=hi: return '.e'
    m=(lo+hi)//2
    return f'(.n {tree(lo,m)} {sv[m]} {ranks[sv[m]]} {tree(m+1,hi)})'
head=open('cloud_head.txt').read()
mid=open('cloud_mid.txt').read()
tail=open('cloud_tail.txt').read()
chunks=''.join(f'def C{i} : List Nat := {sv[i*CH:(i+1)*CH]}\n' for i in range(NC))
qn=' ++ '.join(f'C{i}' for i in range(NC))
goods=''.join(f'theorem g{i} : ∀ n, n ∈ C{i} → Good n ∧ Good1 n := by decide +kernel\n' for i in range(NC))
def split(k,ind):
    if k==0: return f'{ind}exact g0 n hn\n'
    return f'{ind}rcases hn with hn | hn\n{ind}· skip\n'+split(k-1,ind+'  ')+f'{ind}· exact g{k} n hn\n'
out=head+'def tree : T := '+tree(0,len(sv))+'\n\n'+chunks+'\n/-- All the numbers. -/\ndef Qn : List Nat := '+qn+'\n'+mid+goods+'\ntheorem good : ∀ n, n ∈ Qn → Good n ∧ Good1 n := by\n  intro n hn\n  simp only [Qn, List.mem_append] at hn\n'+split(NC-1,'  ')+tail
open('lean/TwoPairsWallCloud.lean','w').write(out)
