#!/usr/bin/env python3
"""GC983: preserve exact phase0 origin language through all black resets.
Record searched: GC982/RRL + history/constraint/counter ->23 hits in13 files;
new L558/L559 received in e6688e59. No duplicate language census.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_origin.py
Before execution: phase0 origin starts white; every reset output starts black.
Keep origin exact; quotient only the black reset component. Source: K10's
seven certified words plus Local's absent words17 and21, NOT full K18.
P1: white-first reset language equals the initial DFA at every reset update.
Controls include exact two-way containment and all residual test/viability
checks. CF: reject initial words violating the known21-word constraint.
U: empty black component must preserve the origin unchanged. Blind P2:
C32 overflows within40 rounds;20seconds/3000states. No all-depth bound
unless full image obligations close. C17 already fails throughK20 by L559.
OUTCOME: P1 and origin/empty-black/forbidden21 controls PASS. White-first
origin remains exactly equal at every reset update. C32 abstract overflow
round38, P2 HELD; no certificate or physical witness. Input is nine certified
words, not fullK18. Remaining overapproximation is in black-reset feedback.
"""
import rule30_rrl_transducer as t
import rule30_rrl_closure as c
import rule30_rrl_factors as f
import rule30_rrl_residual as z

WORDS=t.FORBIDDEN+('00100010001010100','000010001000100010001')
INITIAL=t.initial(0,WORDS)
z.TESTS=sorted(set(z.TESTS)|{(0,)*5,(0,)*6},key=lambda w:(len(w),w))


def viable(a): return z.residual(a,viability=True)


def reset(a):
    white=c.first(a,0)
    assert c.subset(white,INITIAL) and c.subset(INITIAL,white)
    out=c.union(INITIAL,viable(c.first(a,1)))
    assert c.subset(a,out)
    assert c.subset(c.first(out,0),INITIAL) and c.subset(INITIAL,c.first(out,0))
    return out


if __name__=='__main__':
    assert c.subset(reset(INITIAL),INITIAL)
    visible=WORDS[-1]
    word=tuple(x for b in visible for x in (int(b),2))+(0,)
    assert not t.direct_initial(word,0,WORDS) and not t.accepted(INITIAL,word)
    print('origin/empty-black/forbidden21 controls PASS',flush=True)
    f.run(viable,origin=INITIAL,reset=reset)
