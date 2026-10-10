#!/usr/bin/env python3
"""GC977 targeted refinement of GC976's zero pumping.
Record searched: RRL/GC976/GC970 + prefix/zero/refin ->22 hits in11 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_prefix_refine.py
Before execution: keep exact unary-zero prefixes, their terminating letters,
and accepted pure-zero lengths, intersected with GC975 factor widening.
P1: repairs the depth5 000/0000 trap; exact source containment must pass.
Blind P2: the capped phase0 K10 C32 search hits an unbounded zero-prefix
cycle before closure or C32 overflow, exposing a different lost continuation.
Limits inherited: 40 rounds, 20 seconds, 3000 states/operation, one CPU.
Independent finite toy profile controls through length5; CF dropping the
prefix filter restores pumping; U empty source remains empty. A source
zero-prefix cycle is a stop, never silently truncated or claimed a bound.
OUTCOME: C/CF/U PASS, P1 HELD. Abstract C32 overflow at round35;
P2 REFUTED (no source zero-prefix cycle). No cap, certificate or physical witness.
Stop scalar prefix patching pending recovery of the unsupported continuation.
"""
from itertools import product
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f


def refine(a):
    a=c.prune(a); rows,finals=a; chain=[]; seen=set(); q=0
    while q>=0:
        if q in seen: raise RuntimeError('unbounded source zero-prefix cycle')
        seen.add(q); chain.append(q); q=rows[q][0]
    def step(s,x):
        i,escaped=s
        if escaped: return (0,True)
        if rows[chain[i]][x]<0: return None
        return (i+1,False) if x==0 else (0,True)
    filt=t.build((0,False),step,lambda s:s[1] or chain[s[0]] in finals,c.CAP)
    b=f.widen(a)
    def both(s,x):
        i,j=s; ii=b[0][i][x]; jj=filt[0][j][x]
        return (ii,jj) if ii>=0 and jj>=0 else None
    out=t.minimize(t.build((0,0),both,lambda s:s[0] in b[1] and s[1] in filt[1],c.CAP))
    assert c.subset(a,out)
    return out


def controls():
    words={(0,0,0),(0,0,1,2),(1,0,2)}
    def step(s,x):
        v=s+(x,)
        return v if any(w[:len(v)]==v for w in words) else None
    a=t.build((),step,lambda s:s in words)
    b=f.widen(a); out=refine(a)
    for n in range(1,6):
        for w in product(range(4),repeat=n):
            end=next((i for i,x in enumerate(w) if x),n)
            profile=(w in words if end==n else any(v[:end+1]==w[:end+1] for v in words))
            assert t.accepted(out,w)==(t.accepted(b,w) and profile)
    zero=t.build(0,lambda n,x:n+1 if x==0 and n<3 else None,lambda n:n==3)
    assert t.accepted(f.widen(zero),(0,)*4)
    assert t.accepted(refine(zero),(0,)*3) and not t.accepted(refine(zero),(0,)*4)
    assert c.subset(refine(c.EMPTY),c.EMPTY)
    print('prefix refinement C/CF/U PASS',flush=True)


if __name__=='__main__':
    controls()
    f.run(refine)
