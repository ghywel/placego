#!/usr/bin/env python3
"""B159/MI326 preregistered fixed n12,3^4 JOINT-realization diagnostic.

COMMAND: python3 tests/probes/instinct/ss3_joint_lift.py --output /tmp/math-instinct-b159-joint.json
Requires /tmp/math-instinct-b159-joint compiled from sibling .cpp AFTER source push.
P1: all369600 labelled words,19344 with sorted sums,630 SS sum vectors;
    independent combination-mask enumeration agrees on EVERY fibre count.
P2 BLIND: for EVERY sorted attainable x and SS-admissible y=x-e_a+e_b,
    SOME x realization lifts to y by <=3 DISJOINT adjacent-value swaps.
    A failure refutes this stronger coupling,not SS3; retain all failed pairs.
REFERENCE: whole minimum-depth maps on FOUR fixed current-sum fibres below,
    via simple BIN paths and products of adjacency witnesses,not value matchings.
    Independently compute all target-domain inequalities and eligibility.
UNEXPECTED: all canonical target/direction distances match full value reflection
    with bin reversal,including ties and missing lifts. Audit EVERY success's
    literal partition,distinct value pairs,ownership and final target sums.
COUNTERFACTUAL: <=2 always suffices is FALSE: MI325 x=(3,12,23,28),a3,b0
    has best-fibre distance3; MI320's old five-depth sums (5,14,23,24),a0,b3
    have best-fibre distance1. Reject overlapping/nonadjacent witness controls.
CAPS: one invocation,40aggregateCPU/60wall seconds,192MiB per process,
    3M engine matching trials,4MiB engine output,70wall external watchdog.
    Stop first instrument failure/cap; retain mathematical failures. No retry,
    extension,larger n or automatic follow-on census. Raw stays outside git.
SCOPE: a new existential quantifier on an already measured domain,not a repeat
    of fixed-start distance measurements. Complete success is finite evidence
    only; no general three-move bound,UN or SS3 theorem follows.

OUTCOME MI327 (2026-10-17;prereg bad02e8b,published merge6e622b4d):
ONE invocation PARTIAL/INSTRUMENT-FAILED at whole reflection control.
Value reversal reverses the transfer,so reflected endpoints must be
(3-b,3-a),not (3-a,3-b). Source left unchanged except this receipt;
NO repair/retry. Compile clean. Independent whole fibre counts/eligible
pairs,FOUR whole path-product maps and EVERY emitted literal witness
passed BEFORE failure. Primary emitted7184 pairs,depths1:6748,2:408,3:28,
zero missing;these are retained primary output,NOT a completed P2 pass.
Reflection comparison incomplete;later CF/invalid-pair controls and
final resource/report checks NOT REACHED. Wrapper exit1 after watchdog
wall1.617354s,not a cap;no JSON report. Raw/digests MI327,outside git.
"""
import argparse
from collections import Counter
from itertools import combinations,permutations,product
import json
from pathlib import Path
import resource
import subprocess
import time

FIXTURES=((3,12,23,28),(5,14,23,24),(16,16,17,17),(7,10,23,26))
BEGAN=time.monotonic()
def budget():
    us=[resource.getrusage(w) for w in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN)]
    assert sum(u.ru_utime+u.ru_stime for u in us)<40,'aggregate CPU cap'
    assert all(u.ru_maxrss<192*1024**2 for u in us),'RSS cap (macOS bytes)'
    assert time.monotonic()-BEGAN<60,'wall cap'
def ss(t):
    if sum(t)!=66:return False
    for mask in range(1,16):
        r=3*mask.bit_count();v=sum(t[j] for j in range(4) if mask>>j&1)
        if not r*(r-1)//2<=v<=r*(23-r)//2:return False
    return True
def reference():
    counts=Counter();fixtures={t:[] for t in FIXTURES};allv=set(range(12))
    for aa in combinations(range(12),3):
        for bb in combinations(sorted(allv-set(aa)),3):
            tail=allv-set(aa)-set(bb)
            for cc in combinations(sorted(tail),3):
                dd=tuple(sorted(tail-set(cc)));t=tuple(map(sum,(aa,bb,cc,dd)))
                if t!=tuple(sorted(t)):continue
                counts[t]+=1
                if t in fixtures:fixtures[t].append((aa,bb,cc,dd))
        budget()
    maps={}
    for t,parts in fixtures.items():
        dist={(a,b):-1 for a in range(4) for b in range(4) if a!=b and ss(tuple(t[j]-(j==a)+(j==b) for j in range(4)))}
        for bins in parts:
            witness={(a,b):[(u,v) for u in bins[a] for v in bins[b] if u==v+1]
                     for a in range(4) for b in range(4) if a!=b}
            for r in range(2,5):
                for path in permutations(range(4),r):
                    key=(path[0],path[-1])
                    if key not in dist or (0<dist[key]<=r-1):continue
                    for picks in product(*(witness[a,b] for a,b in zip(path,path[1:]))):
                        flat=[v for pair in picks for v in pair]
                        if len(set(flat))==len(flat):dist[key]=r-1;break
            budget()
        maps[t]=dist
    return counts,maps

def apply_pairs(word,pairs):
    flat=[v for pair in pairs for v in pair]
    assert len(flat)==len(set(flat))
    assert all(abs(u-v)==1 and word[u]!=word[v] for u,v in pairs)
    new=word[:]
    for u,v in pairs:new[u],new[v]=new[v],new[u]
    return new

def audit(t,a,b,depth,w,mask):
    word=[w>>(2*x)&3 for x in range(12)]
    assert [word.count(j) for j in range(4)]==[3]*4
    assert tuple(sum(x for x in range(12) if word[x]==j) for j in range(4))==t
    edges=[k for k in range(11) if mask>>k&1]
    assert len(edges)==depth and not(mask&(mask<<1))
    new=apply_pairs(word,[(k,k+1) for k in edges])
    target=tuple(t[j]-(j==a)+(j==b) for j in range(4))
    assert tuple(sum(x for x in range(12) if new[x]==j) for j in range(4))==target

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU,(40,41));resource.setrlimit(resource.RLIMIT_FSIZE,(4*1024**2,4*1024**2))
    raw=Path(args.output).with_suffix('.engine.txt')
    subprocess.run(['/tmp/math-instinct-b159-joint',str(raw)],check=True,timeout=35)
    assert raw.stat().st_size<=4*1024**2
    counts={};edges={};total=None
    for line in raw.read_text().splitlines():
        f=line.split()
        if f[0]=='TOTAL':total=list(map(int,f[1:]));continue
        t=tuple(map(int,f[1:5]));assert t==tuple(sorted(t)) and ss(t)
        if f[0]=='C':assert t not in counts;counts[t]=int(f[5]);continue
        assert f[0]=='E';a,b,d,w,mask=map(int,f[5:]);assert a!=b and (t,a,b) not in edges
        target=tuple(t[j]-(j==a)+(j==b) for j in range(4));assert ss(target)
        assert d in (-1,1,2,3);edges[t,a,b]=d
        if d>0:audit(t,a,b,d,w,mask)
    rc,rm=reference();assert counts==rc
    targets=set()
    for a in range(3,31):
        for b in range(a,31):
            for c in range(b,31):
                d=66-a-b-c;t=(a,b,c,d)
                if c<=d<=30 and ss(t):targets.add(t)
    assert set(counts)==targets and all(counts.values())
    eligible={(t,a,b) for t in targets for a in range(4) for b in range(4)
              if a!=b and ss(tuple(t[j]-(j==a)+(j==b) for j in range(4)))}
    assert set(edges)==eligible
    for t,dist in rm.items():assert dist=={(a,b):d for (s,a,b),d in edges.items() if s==t}
    for (t,a,b),d in edges.items():
        rt=tuple(33-v for v in reversed(t));assert edges[rt,3-a,3-b]==d
    assert edges[(3,12,23,28),3,0]==3
    assert edges[(5,14,23,24),0,3]==1
    # Known valid word; test the physical-pair predicate directly.
    word=[0,0,0,1,1,1,2,2,3,3,2,3]
    for bad in ([(2,3),(3,4)],[(2,4)]):
        try:apply_pairs(word,bad)
        except AssertionError:pass
        else:raise AssertionError('invalid witness accepted')
    budget();us=[resource.getrusage(w) for w in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN)]
    report={'complete':True,'total':total,'fibres':len(counts),'eligible_pairs':len(edges),
            'depth_hist':dict(sorted(Counter(edges.values()).items())),
            'missing':[[*t,a,b] for (t,a,b),d in edges.items() if d<0],
            'reference_words':{str(t):counts[t] for t in FIXTURES},
            'reference_pairs':sum(map(len,rm.values())),'reflection_pairs':len(edges),
            'cpu':[u.ru_utime+u.ru_stime for u in us],'rss':[u.ru_maxrss for u in us],
            'wall':time.monotonic()-BEGAN}
    Path(args.output).write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
if __name__=='__main__':main()
