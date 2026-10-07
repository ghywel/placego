#!/usr/bin/env python3
"""Independent targeted audit of Local L124, not a repeat of the HG4 global run.
Known expectations, written before execution: at q8 source(143,8), H32=9,
H33=17, maximizing path length33, elapsed91. Scalar closure and clocks
must agree. Unexpected check: no repeated clock-aligned state, despite
possible raw-pair phase repeats. Counterfactual: H0 fails q4 pulse edge.
Root ancestry is a scope check, not a prediction of rootedness. No Local
imports; no global graph, certificate relaxation or larger-period job.
Outcome: all stated controls pass; 67 memo states. Witness not rooted:
backward ancestry repeats after4746 steps at(139,0). CPU0.0123 s,
RSS10.5 MiB on GPT Intel host. Initial root encoding1 was corrected to
constant-one255 before the reported rerun; same non-rooted verdict.
"""
from functools import lru_cache
import resource
import time


def bit(w,t,q):
    return (w >> (t % q)) & 1

@lru_cache(None)
def children(a,b,q):
    out=[]
    for initial in (0,1):
        c=0; value=initial
        for t in range(q):
            c |= value << t
            value=bit(a,t,q) ^ (bit(b,t,q) | value)
        if value==initial:
            out.append(c)
    return tuple(out)


def delay(b,r,q):
    if not b: return 0
    for j in range(q):
        if bit(b,r+j,q): return j+1
    raise AssertionError('nonzero word has no black bit')


def gate(a,b,r,q):
    return bool(bit(a,r-1,q) if a else bit(b,r,q)^bit(b,r-1,q)) or (a,b)==(0,0)

@lru_cache(None)
def best(a,b,r,q,n):
    if not n: return (0,())
    d=delay(b,r,q); rr=(r+d)%q
    answer=(0,())
    for c in children(a,b,q):
        assert gate(b,c,rr,q)
        value,path=best(b,c,rr,q,n-1)
        candidate=(2*d-5+value,(c,)+path)
        if candidate[0]>answer[0]: answer=candidate
    return answer


def aligned(w,r,q):
    return sum(bit(w,r+t,q)<<t for t in range(q))


def main():
    started=time.process_time(); q=8; a,b=143,8
    assert gate(a,b,0,q)
    h32,_=best(a,b,0,q,32); h33,path=best(a,b,0,q,33)
    words=[a,b]+list(path); elapsed=0; states=[]
    for j,c in enumerate(path):
        aa,bb=words[j:j+2]; r=elapsed%q
        states.append((aligned(aa,r,q),aligned(bb,r,q)))
        assert all(bit(c,t+1,q)==(bit(aa,t,q)^(bit(bb,t,q)|bit(c,t,q))) for t in range(q))
        elapsed+=delay(bb,r,q)
    states.append((aligned(words[-2],elapsed,q),aligned(words[-1],elapsed,q)))
    assert (h32,h33,len(path),elapsed)==(9,17,33,91)
    assert 2*elapsed-5*len(path)==h33
    assert len(states)==len(set(states))
    assert children(8,8,4)==(0,)
    assert delay(8,0,4)==4 and 2*4-5>0
    # Literal predecessor equation, no graph helper or phase quotient.
    seen=set(); pair=(a,b); ancestry=0; root=(0,(1<<q)-1)
    while pair not in seen and pair!=root:
        seen.add(pair); aa,bb=pair
        predecessor=sum((bit(bb,t+1,q)^(bit(aa,t,q)|bit(bb,t,q)))<<t for t in range(q))
        pair=(predecessor,aa); ancestry+=1
    rooted=pair==root
    print('H32=%d H33=%d edges=%d elapsed=%d reward=%d; scalar/closure/gate/unique-aligned-state/CF PASS' % (h32,h33,len(path),elapsed,h33))
    print('words=',words)
    print('rooted=',rooted,'backward steps=',ancestry,'terminal=',pair)
    print('memo states=',best.cache_info().currsize)
    print('GPT host CPU %.4f s; peak RSS %.1f MiB' % (time.process_time()-started,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1048576))

if __name__=='__main__': main()
