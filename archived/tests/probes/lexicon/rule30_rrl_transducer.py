#!/usr/bin/env python3
"""GC971: exact finite-word inverse-column image for RRL certificate search.
Record searched: GC970/RRL + transducer/certificate -> 9 hits in 3 files.
COMMAND: python3 tests/probes/lexicon/rule30_rrl_transducer.py
Scope: controls only; no record census, invariant or all-depth bound.
Predictions before first execution:
 C1: initial DFA agrees with direct clock/visible tests on all pair words through length 6.
 C2: image DFA equals literal image sets at output lengths 1..3, in both phases.
 C3: every reconstructed cell satisfies the independent Rule 30 truth table.
 CF: constraining the unused terminal visible sample is equivalent; must fail.
 Unexpected U: singleton inputs produce no nonempty image, even when accepted.
Determinization has a hard state cap; a cap is a failure, never a certificate.
OUTCOME first controls: C1/C2/C3/CF/U PASS; 10,920 initial-membership cases;
initial/image state counts phase 0: 81/53, phase 1: 82/54. No bound inferred.
ADDENDUM before second execution: test every binary visible word through length 10
with two clock phases, so all seven forbidden lengths, beyond C1's short pair words,
are exercised. Compare against direct substring exclusion, not actual-language equality.
"""
from collections import deque
from itertools import product

FORBIDDEN = ('11','00000','101001','0100101','010010001','0101000101','0101010000')
# Letter = 2*u+v. All languages here exclude the empty word.

def initial(phase, forbidden=FORBIDDEN):
    prefixes = {''} | {w[:i] for w in forbidden for i in range(1,len(w))}
    def advance(s, a):
        p, suffix, pending, seen = s
        u,v = divmod(a,2)
        if u != p: return None
        if pending is not None:
            candidate = suffix + str(pending)
            if any(candidate.endswith(w) for w in forbidden): return None
            suffix = max((w for w in prefixes if candidate.endswith(w)),key=len)
        return (1-p,suffix,v if u==0 else None,True)
    start=(phase,'',None,False)
    return build(start,advance,lambda s:s[3])

def build(start,advance,accept,cap=10000):
    states=[start]; ids={start:0}; delta=[]; finals=set()
    for state in states:
        if accept(state): finals.add(ids[state])
        row=[]
        for a in range(4):
            nxt=advance(state,a)
            if nxt is None: row.append(-1); continue
            if nxt not in ids:
                if len(states)>=cap: raise RuntimeError('DFA state cap')
                ids[nxt]=len(states); states.append(nxt)
            row.append(ids[nxt])
        delta.append(row)
    return delta,finals

def accepted(dfa,word):
    if not word: return False
    delta,finals=dfa; state=0
    for a in word:
        state=delta[state][a]
        if state<0: return False
    return state in finals

def image(dfa,cap=10000):
    delta,finals=dfa
    # Read one input letter without emitting. Each later input emits one letter.
    start=frozenset((a,delta[0][a]) for a in range(4) if delta[0][a]>=0)
    def advance(subset,out):
        targets=set()
        for prev,state in subset:
            u,v=divmod(prev,2)
            for nxt in range(4):
                ns=delta[state][nxt]
                if ns<0: continue
                y=2*((nxt//2) ^ (u|v))+u
                if y==out: targets.add((nxt,ns))
        return frozenset(targets) if targets else None
    return build(start,advance,lambda ss:any(s in finals for _,s in ss),cap)

def direct_initial(word,phase,forbidden=FORBIDDEN,terminal=False):
    if not word or any(a//2 != ((t+phase)%2) for t,a in enumerate(word)): return False
    stop=len(word) if terminal else len(word)-1
    visible=''.join(str(a%2) for t,a in enumerate(word[:stop]) if (t+phase)%2==0)
    return not any(w in visible for w in forbidden)

def literal_image(word):
    return tuple(2*((word[t+1]//2) ^ ((word[t]//2)|(word[t]%2)))+word[t]//2 for t in range(len(word)-1))

def controls():
    checks=0
    for phase in (0,1):
        dfa=initial(phase); out=image(dfa)
        for n in range(1,7):
            for w in product(range(4),repeat=n):
                assert accepted(dfa,w)==direct_initial(w,phase); checks+=1
        for n in range(1,4):
            expected={literal_image(w) for w in product(range(4),repeat=n+1) if direct_initial(w,phase)}
            actual={w for w in product(range(4),repeat=n) if accepted(out,w)}
            assert expected==actual
        for w in product(range(4),repeat=4):
            y=literal_image(w)
            for t,a in enumerate(y):
                left=a//2; u=w[t]//2; v=w[t]%2
                # Wolfram table, independent of the inverse XOR/OR formula.
                neighbourhood=4*left+2*u+v
                assert ((30 >> neighbourhood)&1)==w[t+1]//2
        assert literal_image((phase*2,))==() and not accepted(out,())
        for n in range(1,11):
            for bits in product((0,1),repeat=n):
                word=[2*((t+phase)%2) for t in range(2*n+phase+1)]
                for k,b in enumerate(bits): word[2*k+phase]+=b
                visible=''.join(map(str,bits))
                assert accepted(dfa,word)==(not any(f in visible for f in FORBIDDEN))
        print('phase',phase,'initial states',len(dfa[0]),'image states',len(out[0]))
    witness=(1,2,1)  # wall 010, visible 11 only if unused terminal sample included
    assert direct_initial(witness,0) and not direct_initial(witness,0,terminal=True)
    print('C1/C2/C3/CF/U PASS; initial membership cases',checks)

def minimize(dfa):
    rows,finals=dfa
    # Include a rejecting sink, then refine exact right-language equivalence.
    sink=len(rows); rows=[[sink if x<0 else x for x in row] for row in rows]+[[sink]*4]
    blocks=[int(i in finals) for i in range(len(rows))]
    while True:
        signatures=[(i in finals,tuple(blocks[j] for j in row)) for i,row in enumerate(rows)]
        ids={}; refined=[]
        for sig in signatures:
            if sig not in ids: ids[sig]=len(ids)
            refined.append(ids[sig])
        if refined==blocks: break
        blocks=refined
    reps={}
    for i,b in enumerate(blocks): reps.setdefault(b,i)
    order=[blocks[0]]+[b for b in reps if b!=blocks[0]]
    renumber={b:i for i,b in enumerate(order)}
    return ([[renumber[blocks[j]] for j in rows[reps[b]]] for b in order],
            {renumber[b] for b in order if reps[b] in finals})

# GC972 preregistration BEFORE image-search execution:
# One CPU, 20-second alarm, 2,000 determinized states, at most 4 inverse depths/phase.
# Blind P1: minimized images through depth 4 each have at most 200 states.
# Independent control: minimization preserves membership for all words through length 3.
# Countercontrol: two wall phases have identical initial languages; must fail.
# Unexpected: state count includes the complete rejecting sink after minimization.
# No white-counter closure or record value is inferred from image sizes.
# OUTCOME GC972: P1 HELD. Complete minimized DFA counts at depths 0..4:
# phase 0: 55,54,52,50,43; phase 1: 56,55,54,52,50.
# All finite membership controls PASS; no cap reached. Counts include sink.
def search():
    import signal
    signal.signal(signal.SIGALRM,lambda *_: (_ for _ in ()).throw(RuntimeError('time cap')))
    signal.alarm(20)
    try:
        assert accepted(initial(0),(0,)) and not accepted(initial(1),(0,))
        for phase in (0,1):
            dfa=minimize(initial(phase))
            print('SEARCH phase',phase,'depth 0 states',len(dfa[0]),flush=True)
            for depth in range(1,5):
                original=image(dfa,cap=2000); reduced=minimize(original)
                for n in range(1,4):
                    for word in product(range(4),repeat=n):
                        assert accepted(original,word)==accepted(reduced,word)
                dfa=reduced
                print('SEARCH phase',phase,'depth',depth,'raw',len(original[0]),'min',len(dfa[0]),flush=True)
    except RuntimeError as e:
        print('SEARCH STOP',str(e),flush=True)
    finally: signal.alarm(0)

if __name__=='__main__':
    import sys
    if len(sys.argv)>1 and sys.argv[1]=='search': search()
    else: controls()
