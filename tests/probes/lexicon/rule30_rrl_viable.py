#!/usr/bin/env python3
"""GC982: residual prefix-viability separator.
Record searched: RRL/GC981/GC980 + viab/coaccess/dead prefix ->3 hits in3 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_viable.py
Before execution: add zero tests5,6 to the original suffix-closed suite, and
partition by both acceptance and prefix viability for every test. P1: recovered
GC981 28-zero loss is excluded using its dead6-zero prefix; source containment
and all prefix-test preservation must pass. CF: original quotient admits it.
U: empty-source viability is false, including empty prefix. Independent toy
finite prefix enumeration through length5. Blind P2: C32 still overflows within
40 rounds. Shared total20seconds/3000states; cap never counts as closure.
OUTCOME: P1/CF/U and prefix-toy controls PASS; 44 tests block all
extensions of the recovered dead0^6 prefix, versus66 acceptance-only tests.
Candidate still overflows C32 at round37, P2 HELD, no cap or certificate.
Generic partition-feature additions stalled; seek a specific lost history constraint.
"""
import time
from itertools import product
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_history as h
import rule30_rrl_residual as z

BASE=list(z.TESTS)

def viable(a): return z.residual(a,viability=True)


def controls():
    words={(0,0,0),(0,0,1,2),(1,0,2)}
    def step(s,x):
        v=s+(x,)
        return v if any(w[:len(v)]==v for w in words) else None
    a=t.build((),step,lambda s:s in words)
    out=c.prune(viable(a))
    for n in range(6):
        for w in product(range(4),repeat=n):
            if w in z.TESTS:
                assert z.prefix_viable(out,w)==any(v[:n]==w for v in words)
    assert not z.prefix_viable(c.prune(viable(c.EMPTY)),())
    print('viability prefix/toy/U PASS',flush=True)


def run():
    start=time.monotonic(); found=[]
    def diagnostic(history,white):
        loss=h.diagnose(history,white,transform=z.residual)
        if loss is not None: found.append(loss)
    f.run(z.residual,diagnostic,seconds=20)
    assert found and found[0][0]==(0,)*28
    word,source,_,_=found[0]
    z.TESTS=sorted(set(BASE)|{(0,)*5,(0,)*6},key=lambda w:(len(w),w))
    refined=viable(source)
    assert c.subset(source,refined) and not t.accepted(refined,word)
    assert not z.prefix_viable(c.prune(refined),(0,)*6)
    print('dead6-zero prefix excluded with',len(z.TESTS),'tests; P1 PASS',flush=True)
    controls()
    remaining=int(20-(time.monotonic()-start))
    if remaining<1: print('TOTAL BUDGET STOP'); return
    f.run(viable,seconds=remaining)


if __name__=='__main__': run()
