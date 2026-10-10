#!/usr/bin/env python3
"""GC973: capped exact regular-language white-counter closure attempt.
Record searched: RRL/GC970 + closure/counter -> 13 hits in 4 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_closure.py
Predictions before first run: controls (union, first-bit filtering, containment,
pruning) agree with literal membership through length 3. Blind P1: phase-0 K10
closure fits 3,000 raw states per operation for 12 rounds. C=32, one CPU,
20 seconds. CF: phase-0 language is contained in phase-1; must fail.
Unexpected: rejecting sink must be pruned before inverse-image subset construction.
A cap or finite unfinished iteration is NOT a proof. C17 is already contradicted
for K16 and hence K10 by Local L556; this attempt uses C32 instead.
OUTCOME: controls PASS; P1 HELD, no cap reached. After 12 rounds the
nonempty counter-language DFA sizes are 600,500,348,221,88,40,40.
UNFINISHED: no closure, no uniform bound. Do not extend exact iteration merely
for state counts; next seek a sound overapproximation with inclusion checks.
"""
import signal
from collections import deque
from itertools import product
import rule30_rrl_transducer as t

CAP=3000
EMPTY=([[-1]*4],set())

def union(a,b):
    def step(s,x):
        i,j=s
        ii=a[0][i][x] if i>=0 else -1
        jj=b[0][j][x] if j>=0 else -1
        return None if ii<0 and jj<0 else (ii,jj)
    return t.minimize(t.build((0,0),step,lambda s:s[0] in a[1] or s[1] in b[1],CAP))

def first(a,black):
    def step(s,x):
        i,seen=s
        if not seen and x//2!=black: return None
        j=a[0][i][x]
        return None if j<0 else (j,True)
    return t.minimize(t.build((0,False),step,lambda s:s[1] and s[0] in a[1],CAP))

def subset(a,b):
    todo=deque([(0,0,False)]); seen=set(todo)
    while todo:
        i,j,nonempty=todo.popleft()
        if nonempty and i in a[1] and j not in b[1]: return False
        for x in range(4):
            ii=a[0][i][x] if i>=0 else -1
            if ii<0: continue
            jj=b[0][j][x] if j>=0 else -1
            state=(ii,jj,True)
            if state not in seen:
                if len(seen)>=CAP: raise RuntimeError('containment cap')
                seen.add(state); todo.append(state)
    return True

def prune(a):
    rows,finals=a; live=set(finals)
    while True:
        nxt=live|{i for i,row in enumerate(rows) if any(j in live for j in row)}
        if nxt==live: break
        live=nxt
    return ([[j if j in live else -1 for j in row] for row in rows],finals)

def controls():
    a=t.initial(0); b=t.initial(1)
    u=union(a,b); f=first(a,0); p=prune(t.minimize(a))
    for n in range(1,4):
        for w in product(range(4),repeat=n):
            aa=t.accepted(a,w); bb=t.accepted(b,w)
            assert t.accepted(u,w)==(aa or bb)
            assert t.accepted(f,w)==(aa and w[0]//2==0)
            assert t.accepted(p,w)==aa
    assert subset(a,u) and subset(b,u) and not subset(a,b)
    # Complete minimization adds a reachable rejecting sink; pruning removes its edges.
    assert any(-1 in row for row in p[0])
    print('C/CF/U PASS',flush=True)

def run():
    controls()
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(20)
    inv=[EMPTY for _ in range(33)]; inv[0]=t.minimize(t.initial(0))
    try:
        for n in range(1,13):
            nxt=list(inv)
            for r,language in enumerate(inv):
                if subset(language,EMPTY): continue
                output=t.minimize(t.image(prune(language),cap=CAP))
                black,white=first(output,1),first(output,0)
                nxt[0]=union(nxt[0],black)
                if r==32:
                    if not subset(white,EMPTY):
                        print('ALLOWANCE REFUTED',n,flush=True); return
                else: nxt[r+1]=union(nxt[r+1],white)
            stable=all(subset(x,y) for x,y in zip(nxt,inv))
            inv=nxt
            print('ROUND',n,'states',[len(a[0]) for a in inv if not subset(a,EMPTY)],flush=True)
            if stable:
                # Initial containment and full inductive obligations, checked afresh.
                assert subset(t.initial(0),inv[0])
                for r,a in enumerate(inv):
                    o=t.minimize(t.image(prune(a),cap=CAP))
                    assert subset(first(o,1),inv[0])
                    assert subset(first(o,0),inv[r+1] if r<32 else EMPTY)
                print('CLOSED phase 0 K10 C32; phase 1 still required',flush=True); return
        print('UNFINISHED 12 rounds',flush=True)
    except RuntimeError as e: print('STOP',e,flush=True)
    finally: signal.alarm(0)

if __name__=='__main__': run()
