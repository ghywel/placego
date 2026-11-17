#!/usr/bin/env python3
"""rule30_cloud_gc1158_check.py: Cloud's targeted (tier 2) check of GPT's GC1158 seeded inverse decoder (RULE30-GPT.md
GC1158): joint initialisation and the converse, including the unused terminal root input, by an independent
implementation from the sketch and exhaustive enumeration at small depths (CL361).

RUN-ON:     cpu (Python 3 standard library; under a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1158_check.py

THE OBJECTS, as read from the sketch. Wall tau(t) = (p + t) mod 2, white = 0. Effective inputs v(t): column 1 with
the values at black wall ticks replaced by 0 (masked). X_0 = tau, X_1(t) = tau(t+1) XOR (tau(t) OR v(t)),
X_(j+1)(t) = X_j(t+1) XOR (X_j(t) OR X_(j-1)(t)); the inverse pair at depth k is (X_k, X_(k-1)); X_k(t) uses
v(t..t+k-1), so an output word of length N uses v(0..N+k-2) and the root word of length N+k has one unused terminal
value. The visible word is v at the white ticks in time order; F is a set of forbidden visible words with the usual cut
automaton (states: the empty word and proper prefixes of words of F; the longest suffix is retained; a completed word
rejects). Decoder state (phase, window = v(t..t+k-2), cut residual). Seed: the phase, the root's first k-1 effective
inputs, and the residual after the window's visible letters (joint initialisation). Step at time t with terminal
q = t+k-1: A = X_k(t) with v(q) = 0, B = X_(k-1)(t), from the window; read (a, b); require b = B; at a white q recover
r = a XOR A and feed r to the cut automaton; at a black q require a = A and r = 0; window := window[1:] + [r]; phase
flips.

CHECKS. For p in {0, 1}, k in 1..5, N in 1..5, with F the certified phase-p minimal forbidden words of length <= 10
(rule30_local_mfw44.txt) and separately the toy F = {101001}: (1) forward: every F-avoiding root (visible word of
v(0..N+k-2) avoids F) started from its own seed is accepted and the recovered inputs equal v(k-1..N+k-2); the image is
independent of the unused terminal v(N+k-1). (2) Converse: the set of accepted (seed, output word) pairs over ALL seeds
and ALL 4^N output words equals the set of (seed, image) pairs of F-avoiding roots, and each accepted path's recovered
root avoids F. (3) The k = 4, phase 0 example: visible roots 001001 and 101001 have identical pair images, the decoder
with F = {101001} accepts the first and rejects the second on its last letter, their windows coalesce after the first
(black-pivot) transition while their residuals are '' and '10'. (4) The live-state count over all accepting runs is at
most 2 S 2^ceil((k-1)/2) with S the cut automaton's live states.

PREDICTIONS (CL361, written before the run). P1 forward exactness holds throughout (0.7). P2 the converse holds
throughout (0.6; this is the step GPT asked to have checked). P3 the k = 4 example reproduces (0.7). P4 the bound
holds (0.7). Counterfactual: an accepted path whose recovered root contains a cut, or an F-avoiding root the decoder
rejects, refutes the exactness and the decoder cannot stand in for GC971's images. Unexpected check: whether the bound
is attained at some k, and whether a black-pivot companion mismatch (b != B) ever occurs on a real image (it must not).
Record searched: seeded decoder, inverse pair, cut residual (GC971, GC978, GC1158 in the ledgers only).
"""
import itertools, math
def tau(p,t): return (p+t)%2
def columns(p,v,k):
    """X_j(t) for j = 0..k and all t where defined; v: effective inputs (list)."""
    T=len(v); X=[[tau(p,t) for t in range(T+1)]]
    X.append([tau(p,t+1)^(tau(p,t)|v[t]) for t in range(T)])
    for j in range(1,k):
        X.append([X[j][t+1]^(X[j][t]|X[j-1][t]) for t in range(len(X[j])-1)])
    return X
def image(p,v,k,N):
    X=columns(p,v,k); return tuple((X[k][t],X[k-1][t]) for t in range(N))
def visible(p,v): return ''.join(str(v[t]) for t in range(len(v)) if tau(p,t)==0)
class Cuts:
    def __init__(self,F):
        self.F=set(F); self.states={''}|{w[:i] for w in F for i in range(1,len(w))}
    def step(self,s,r):
        w=s+r
        if any(w.endswith(f) for f in self.F): return None
        for i in range(len(w)+1):
            if w[i:] in self.states: return w[i:]
    def run(self,s,word):
        for r in word:
            s=self.step(s,r)
            if s is None: return None
        return s
def decode(p,k,window,cuts,outputs):
    """Seeded decoder; returns (accepted, recovered inputs, trace of (window, residual))."""
    phase=p; w=list(window); res=''; rec=[]; trace=[]
    for i,x in enumerate(w):
        if tau(p,i)==0:
            res=cuts.step(res,str(x))
            if res is None: return False,rec,trace
    trace.append((tuple(w),res))
    for t,(a,b) in enumerate(outputs):
        q=t+k-1
        ref=columns(phase,w+[0],k)       # the window as the first k-1 inputs, terminal 0, from phase at time t
        A=ref[k][0]; B=ref[k-1][0]
        if b!=B: return False,rec,trace
        if tau(phase,k-1)==0:            # terminal q white
            r=a^A; res=cuts.step(res,str(r))
            if res is None: return False,rec,trace
        else:
            if a!=A: return False,rec,trace
            r=0
        rec.append(r); w=w[1:]+[r]; phase^=1; trace.append((tuple(w),res))
    return True,rec,trace
def roots(p,L):
    free=[t for t in range(L) if tau(p,t)==0]
    for bits in itertools.product((0,1),repeat=len(free)):
        v=[0]*L
        for t,b in zip(free,bits): v[t]=b
        yield v
def load_F(p,maxlen=10):
    txt=open('tests/probes/lexicon/rule30_local_mfw44.txt').read().split('\n'); ph=None; out=[]
    for l in txt:
        if l.startswith('## phase'): ph=int(l.split(':')[0].split()[-1]); continue
        w=l.strip().split()[0] if l.strip() else ''
        if w and set(w)<={'0','1'} and ph==p and len(w)<=maxlen: out.append(w)
    return out
bad=[]; bound_hits=[]; unused_dep=0; companion_black=0
for Fname,Fof in (('certified<=10',load_F),('toy',lambda p:['101001'])):
    for p in (0,1):
        F=Fof(p); cuts=Cuts(F); S=len(cuts.states)
        for k in range(1,6):
            for N in range(1,6):
                L=N+k; good=set(); states=set()
                for v in roots(p,L):
                    img=image(p,v,k,N)
                    v2=v[:]; v2[L-1]^=1
                    if tau(p,L-1)==0 and image(p,v2,k,N)!=img: unused_dep+=1
                    avoid=cuts.run('',visible(p,v[:L-1])) is not None
                    seed=tuple(v[:k-1]); ok,rec,trace=decode(p,k,seed,cuts,img)
                    if avoid:
                        good.add((seed,img))
                        if not ok or rec!=v[k-1:L-1]: bad.append(('forward',Fname,p,k,N,v))
                        for st in trace: states.add((st,))
                    elif ok: bad.append(('accepts a cut root',Fname,p,k,N,v))
                # converse: all seeds x all outputs
                acc=set()
                for seed in roots(p,k-1):
                    seed=tuple(seed)
                    for out in itertools.product(((0,0),(0,1),(1,0),(1,1)),repeat=N):
                        ok,rec,trace=decode(p,k,seed,cuts,out)
                        if ok:
                            acc.add((seed,out)); v=list(seed)+rec+[0]
                            if cuts.run('',visible(p,v[:L-1])) is None or image(p,v,k,N)!=out:
                                bad.append(('converse',Fname,p,k,N,seed,out))
                if acc!=good: bad.append(('sets differ',Fname,p,k,N,len(acc),len(good)))
                nstates=len({(ph,st) for (st,) in states for ph in (0,)})
                limit=2*S*2**math.ceil((k-1)/2)
                if len(states)>limit: bad.append(('bound',Fname,p,k,N,len(states),limit))
                if len(states)==limit: bound_hits.append((Fname,p,k,N))
print('(1)(2) failures:',len(bad),bad[:3])
print('    image depends on the unused terminal input in',unused_dep,'cases (must be 0)')
print('(4) bound 2 S 2^ceil((k-1)/2) attained in',len(bound_hits),'cases, e.g.',bound_hits[:3])
# (3) the k = 4 example
p,k=0,4; cuts=Cuts(['101001'])
def root_from_visible(p,word):
    v=[]; it=iter(word)
    for t in range(2*len(word)): v.append(int(next(it)) if tau(p,t)==0 else 0)
    return v
v1=root_from_visible(0,'001001'); v2=root_from_visible(0,'101001'); N=len(v1)-k
img1=image(p,v1,k,N); img2=image(p,v2,k,N)
ok1,rec1,tr1=decode(p,k,tuple(v1[:k-1]),cuts,img1); ok2,rec2,tr2=decode(p,k,tuple(v2[:k-1]),cuts,img2)
# where does the second fail? run step by step by truncating the output
fail_at=next((n for n in range(1,N+1) if not decode(p,k,tuple(v2[:k-1]),cuts,img2[:n])[0]),None)
print('(3) k = 4, phase 0: images identical:',img1==img2,'| 001001 accepted:',ok1,'| 101001 accepted:',ok2,
      'rejected at output letter',fail_at,'of',N,'| initial windows',tr1[0][0],tr2[0][0],'| after first transition',
      tr1[1][0],tr2[1][0],'coalesced:',tr1[1][0]==tr2[1][0],'| residuals',repr(tr1[1][1]),repr(tr2[1][1]),
      '| first terminal q = 3 black:',tau(0,3)==1)
