#!/usr/bin/env python3
"""GC979: retain the exact seven-letter post-zero packet exposed by GC978.
Record searched: GC978/RRL + residual/continuation/seven ->14 hits in10 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_context.py
Before execution: extend GC977's exact prefix filter through7 letters starting
at the first nonzero letter, then widen the rest. P1: excludes GC978 loss and
contains its exact union source. CF: keep1 still admits that loss. Independent
finite-toy controls through length5 and empty source. Blind P2: targeted closure
hits the 3000-state cap before closure/overflow. Same phase0 K10 C32,
40 rounds and20 seconds per bounded run. No search over packet lengths.
OUTCOME: P1 and toy/CF/U PASS. Targeted context7 closure overflows C32
at round36, no cap; P2 REFUTED. No certificate or physical witness. Park
fixed packet-length refinements; further refinement needs residual-state retention.
"""
from itertools import product
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_prefix_refine as p
import rule30_rrl_history as h


def context7(a): return p.refine(a,7)


def controls():
    p.controls() # keep1 compatibility after filter rewrite
    words={(0,0,0),(0,0,1,2),(1,0,2)}
    def step(s,x):
        v=s+(x,)
        return v if any(w[:len(v)]==v for w in words) else None
    a=t.build((),step,lambda s:s in words)
    out=context7(a)
    for n in range(1,6):
        for w in product(range(4),repeat=n):
            assert t.accepted(out,w)==(w in words) # all before packet forgetting
    assert c.subset(context7(c.EMPTY),c.EMPTY)
    print('seven-letter packet toy/U PASS',flush=True)


if __name__=='__main__':
    controls()
    f.run(p.refine,lambda history,white:h.diagnose(history,white,context7))
    f.run(context7)
