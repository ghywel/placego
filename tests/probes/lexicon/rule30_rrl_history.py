#!/usr/bin/env python3
"""GC978: recover the first unsupported word on GC977's overflow ancestry.
Record searched: RRL/GC977/GC975 + preimage/history/spurious ->3 hits in2 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_history.py
Before execution: same capped search as GC977, saving DFA snapshots in memory.
P1: recover a word admitted by widening but rejected by its exact union source.
Blind P2: the first loss occurs above counter0 (deeper continuation information),
not at the initial clock relaxation. Do not assume any candidate is physical.
Controls: each recovered preimage satisfies independent truth-table inversion;
CF: claimed loss must reject the exact source. U: old-language inheritance steps
must be skipped before attributing a new widening loss. Limits20s/3000states.
First ancestry recovered: round15/counter13, word 0^13 13203220.
Diagnostic addendum before rerun: locate its first prefix with no exact-source
continuation by coaccessibility pruning; distinguish prefix failure from a
nonaccepting endpoint. No new closure search parameters.
OUTCOME: P1/P2 HELD. Backward ancestry first encounters loss at round15,
counter13: 0^13 13203220, exact union rejects and refined widening accepts.
First nonextendible prefix is 0^13 1320322 (length20); length19 remains
coaccessible. Twenty inverse truth-table controls PASS; no inherited skip
needed. This is not the globally earliest loss or a physical witness.
"""
from collections import deque
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_prefix_refine as p
from rule30_rrl_boundary import table_inverse


def shortest(a):
    todo=deque([(0,())]); seen={(0,False)}
    while todo:
        q,w=todo.popleft()
        if w and q in a[1]: return w
        for x,j in enumerate(a[0][q]):
            state=(j,True)
            if j>=0 and state not in seen:
                seen.add(state); todo.append((j,w+(x,)))
    raise AssertionError('empty target')


def invert(a,word):
    source=f.preimage(a,word)
    assert tuple(table_inverse(source))==word
    assert t.accepted(a,source)
    return source


def diagnose(history,white):
    word=invert(history[-1][32],shortest(white)); r=32; n=len(history)-1
    steps=0; inherited=0
    while n:
        old=history[n-1]
        assert t.accepted(history[n][r],word)
        if t.accepted(old[r],word): n-=1; inherited+=1; continue
        if r==0:
            print('STOP counter0 reset ancestry not implemented',word,flush=True); return
        image=t.minimize(t.image(c.prune(old[r-1]),cap=c.CAP))
        incoming=c.first(image,0); exact=c.union(old[r],incoming)
        if not t.accepted(exact,word):
            assert t.accepted(p.refine(exact),word)
            print('FIRST LOSS round',n,'counter',r,'word',word,
                  'inverse controls',steps+1,'inherited skips',inherited,flush=True)
            trim=c.prune(exact); state=0; dead=None
            for i,x in enumerate(word):
                state=trim[0][state][x]
                if state<0: dead=i+1; break
            print('exact source rejects; refined widening accepts; first dead prefix',
                  word[:dead] if dead else 'none (endpoint rejection)',flush=True)
            return
        word=invert(old[r-1],word); r-=1; n-=1; steps+=1
    assert r==0
    assert not t.direct_initial(word,0)
    print('INITIAL LOSS',word,'inverse controls',steps+1,'inherited skips',inherited,flush=True)


if __name__=='__main__':
    f.run(p.refine,diagnose)
