#!/usr/bin/env python3
"""GC975: bounded internal-factor widening of GC970 counter languages.
Record searched: RRL/GC970/GC974 + factor/local/widen -> 24 hits in 13 files;
GC974 excludes boundary-only widening, not this internal-factor abstraction.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_factors.py
Preregistered: retain accepted short words (<k), prefixes/suffixes k-1,
and internal factors k. Widen after every monotone union. Phase0 K10, k3,
C32, at most40 rounds, 3000 states/operation and20 seconds, one CPU.
Blind P1: k3 is too loose and admits white output beyond C32 within40 rounds.
Controls: exact source inclusion; toy finite-language profile checked against
literal factors on all words through length5. CF: boundary-compatible words
with a disallowed internal factor must reject. U: empty source stays empty.
If closure occurs, verify all GC970 exact image obligations afresh. An overflow
refutes this abstract candidate only; it is not an actual relaxed-record witness.
OUTCOME: C/CF/U PASS; abstract overflow at round34, P1 HELD.
No cap reached; no all-depth certificate or physical witness. Stop this
k3 C32 candidate; prefer counterexample-guided refinement to blind k scans.
"""
import signal
from itertools import product
import rule30_rrl_transducer as t
import rule30_rrl_closure as c


def widen(a,k=3):
    a=c.prune(a); rows,finals=a
    reachable={0}; todo=[0]
    for i in todo:
        for j in rows[i]:
            if j>=0 and j not in reachable: reachable.add(j); todo.append(j)
    def ends(w,starts):
        states=set(starts)
        for x in w: states={rows[i][x] for i in states if rows[i][x]>=0}
        return states
    short={w for n in range(1,k) for w in product(range(4),repeat=n) if t.accepted(a,w)}
    prefixes={w for w in product(range(4),repeat=k-1) if ends(w,{0})}
    suffixes={w for w in product(range(4),repeat=k-1) if ends(w,reachable)&finals}
    factors={w for w in product(range(4),repeat=k) if ends(w,reachable)}
    def step(s,x):
        w,n=s; v=w+(x,)
        if n>=k-1:
            if n==k-1 and w not in prefixes: return None
            if v not in factors: return None
        return (v[-(k-1):],min(k,n+1))
    def final(s):
        w,n=s
        return w in (short if n<k else suffixes)
    out=t.minimize(t.build(((),0),step,final,c.CAP))
    assert c.subset(a,out)
    return out


def controls():
    words={(0,1,0),(1,0,1)}
    def step(s,x):
        v=s+(x,)
        return v if any(w[:len(v)]==v for w in words) else None
    a=t.build((),step,lambda s:s in words)
    b=widen(a)
    prefixes={w[:2] for w in words}; suffixes={w[-2:] for w in words}
    for n in range(1,6):
        for w in product(range(4),repeat=n):
            want=(n>=3 and w[:2] in prefixes and w[-2:] in suffixes
                  and all(w[i:i+3] in words for i in range(n-2)))
            assert t.accepted(b,w)==want
    assert not t.accepted(b,(0,1,1,0)) # allowed boundaries, forbidden middle
    assert c.subset(widen(c.EMPTY),c.EMPTY)
    print('factor controls C/CF/U PASS',flush=True)


def run():
    controls()
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(20)
    inv=[c.EMPTY for _ in range(33)]; inv[0]=widen(t.initial(0))
    try:
        for n in range(1,41):
            nxt=list(inv)
            for r,a in enumerate(inv):
                if c.subset(a,c.EMPTY): continue
                o=t.minimize(t.image(c.prune(a),cap=c.CAP))
                nxt[0]=widen(c.union(nxt[0],c.first(o,1)))
                white=c.first(o,0)
                if r==32:
                    if not c.subset(white,c.EMPTY):
                        print('ABSTRACT OVERFLOW round',n,'C32 k3; no physical witness',flush=True); return
                else: nxt[r+1]=widen(c.union(nxt[r+1],white))
            stable=all(c.subset(x,y) for x,y in zip(nxt,inv)); inv=nxt
            if stable:
                assert c.subset(t.initial(0),inv[0])
                for r,a in enumerate(inv):
                    o=t.minimize(t.image(c.prune(a),cap=c.CAP))
                    assert c.subset(c.first(o,1),inv[0])
                    assert c.subset(c.first(o,0),inv[r+1] if r<32 else c.EMPTY)
                print('CLOSED phase0 k3 C32; phase1 required',flush=True); return
        print('UNFINISHED 40 rounds',flush=True)
    except RuntimeError as e: print('STOP',e,flush=True)
    finally: signal.alarm(0)


if __name__=='__main__': run()
