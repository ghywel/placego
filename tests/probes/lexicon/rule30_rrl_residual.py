#!/usr/bin/env python3
"""GC980: continuation-test residual quotient, not a packet cutoff.
Record searched: RRL/GC978/GC979 + quotient/residual/partition ->2 hits in2 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_residual.py
Before execution: tests comprise all suffixes of GC978's lost word, all words
through length2, and zero words through length4; include empty word. Merge
source DFA states only when their acceptance vectors on these tests agree.
Keep nondeterministic quotient edges, then determinize. Exact source inclusion
and membership on every test must hold. P1: rejects GC978 loss at its exact
source. Independent finite-toy test controls; CF 0000 remains rejected when
000 is accepted. U: empty-word acceptance distinguishes terminal states even
though GC970 languages exclude empty words. Blind P2: C32 abstract overflow
within40 rounds, rather than closure. Limits3000states/20seconds per run.
OUTCOME: test/CF/U controls and P1 PASS. Residual closure overflows C32
at round37; P2 HELD, no cap. No certificate or physical witness. Next recover
the new quotient counterexample before changing its continuation tests.
"""
from itertools import product
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_prefix_refine as p
import rule30_rrl_history as h

LOSS=(0,)*13+(1,3,2,0,3,2,2,0)
TESTS=sorted({LOSS[i:] for i in range(len(LOSS)+1)} |
             {w for n in range(3) for w in product(range(4),repeat=n)} |
             {(0,)*n for n in range(5)},key=lambda w:(len(w),w))


def residual(a):
    a=c.prune(a); rows,finals=a
    def member(q,w):
        for x in w:
            q=rows[q][x]
            if q<0: return False
        return q in finals
    signatures=[tuple(member(q,w) for w in TESTS) for q in range(len(rows))]
    groups={}; blocks=[]
    for sig in signatures:
        if sig not in groups: groups[sig]=len(groups)
        blocks.append(groups[sig])
    delta=[[set() for _ in range(4)] for _ in groups]; accepting=set()
    for q,row in enumerate(rows):
        b=blocks[q]
        if q in finals: accepting.add(b)
        for x,j in enumerate(row):
            if j>=0: delta[b][x].add(blocks[j])
    def step(ss,x):
        out=frozenset(j for b in ss for j in delta[b][x])
        return out or None
    out=t.minimize(t.build(frozenset({blocks[0]}),step,
                          lambda ss:bool(ss&accepting),c.CAP))
    assert c.subset(a,out)
    for w in TESTS:
        if w: assert t.accepted(a,w)==t.accepted(out,w)
    return out


def controls():
    zero=t.build(0,lambda n,x:n+1 if x==0 and n<3 else None,lambda n:n==3)
    assert t.accepted(residual(zero),(0,)*3)
    assert not t.accepted(residual(zero),(0,)*4)
    assert c.subset(residual(c.EMPTY),c.EMPTY)
    assert () in TESTS and all(w[1:] in TESTS for w in TESTS if w)
    print('residual test/CF/U controls PASS',flush=True)


if __name__=='__main__':
    controls()
    f.run(p.refine,lambda history,white:h.diagnose(history,white,residual))
    f.run(residual)
