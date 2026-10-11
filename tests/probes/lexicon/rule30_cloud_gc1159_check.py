#!/usr/bin/env python3
"""rule30_cloud_gc1159_check.py: Cloud's targeted (tier 2) check of GPT's GC1159 first-bit quotient (RULE30-GPT.md
GC1159): with a white-start wall and a cut set containing 11, the first visible bit q0 leaves the depth-k inverse pair
unchanged for every k >= 4, so a canonical root with q0 = 0 may stand for both origins provided it is admitted when at
least one origin avoids the cuts (existential guard); ordinary normalisation (testing the canonical word itself) is
unsound and loses the actual depth-139 record image (CL364).

RUN-ON:     cpu (Python 3 standard library; under a minute)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_gc1159_check.py

CHECKS. Objects as in rule30_cloud_gc1158_check.py (masked effective inputs, X_j columns, pair (X_k, X_(k-1)), visible
word at white ticks). (1) Algebra at time 0, phase 0: X_3(0) = 1 - q1 and X_4(0) = q0 q1 for every root. (2) Image
equality: for phase 0, k = 2..8 and output lengths N = 1..4, over every pair of roots differing in q0 only, whether the
pair image differs, with and without the no11 gate (q1 = 0): expected to differ for k <= 3 and never for k >= 4 under
the gate. (3) Quotient exactness: with F the certified phase-0 words to length 10 (which contain 11 and 00000), for
k = 4..6 and N = 2..4, the image set of F-avoiding roots equals the image set of canonical roots under the existential
guard, and the ordinary-normalisation image set is a strict subset. (4) The residual-subset implementation (U seeded
with delta('', 0) and delta('', 1), rejected origins dropped, reject iff U empty) agrees with the direct two-origin
substring test on every canonical word. (5) The depth-139 witness (Local's d = 139 block, phase 0): its visible word
begins 10000, avoids F, its normalised word begins 00000 and is rejected by ordinary normalisation, and its h^4 image
over 40 output letters is identical with q0 flipped. UNEXPECTED CHECK: the same image-equality count for a black-start
wall (phase 1, first visible bit at tick 1), where GPT says the phase restriction is essential.

PREDICTIONS (CL364, written before the run). P1 the algebra holds (0.9). P2 equality for k >= 4 under the gate, failure
at k = 3, and failures at k = 4 without the gate (0.8). P3 the quotient is exact and ordinary normalisation loses
images (0.75). P4 the subset guard agrees (0.85). P5 the witness behaves as GC1159 says (0.8). Unexpected: phase 1 fails
at some k >= 4 even under the gate (0.6, from a hand computation giving X_5(0) = X_3(2) XOR q0 there).
Record searched: first visible bit, quotient, normalisation, 00000 (GC1159, C7/R4 in the ledgers and RULE30-GPT only).
"""
import itertools
def tau(p,t): return (p+t)%2
def columns(p,v,k):
    T=len(v); X=[[tau(p,t) for t in range(T+1)]]
    X.append([tau(p,t+1)^(tau(p,t)|v[t]) for t in range(T)])
    for j in range(1,k): X.append([X[j][t+1]^(X[j][t]|X[j-1][t]) for t in range(len(X[j])-1)])
    return X
def image(p,v,k,N):
    X=columns(p,v,k); return tuple((X[k][t],X[k-1][t]) for t in range(N))
def visible(p,v): return ''.join(str(v[t]) for t in range(len(v)) if tau(p,t)==0)
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
def avoids(cuts,word): return cuts.run('',word) is not None
# (1) algebra
bad1=0
for v in roots(0,8):
    X=columns(0,v,4); q0,q1=v[0],v[2]
    if X[3][0]!=1-q1 or X[4][0]!=q0*q1: bad1+=1
print('(1) phase 0: X_3(0) = 1 - q1 and X_4(0) = q0 q1 for all roots:',bad1==0)
# (2) image equality under a q0 flip
def first_visible(p): return 0 if p==0 else 1
def second_visible(p): return 2 if p==0 else 3
for p in (0,1):
    line=[]
    for k in range(2,9):
        diff_g=diff_u=tot_g=tot_u=0
        for N in range(1,5):
            L=N+k
            for v in roots(p,L):
                if v[first_visible(p)]==1: continue
                w=v[:]; w[first_visible(p)]=1
                d=image(p,v,k,N)!=image(p,w,k,N); tot_u+=1; diff_u+=d
                if L>second_visible(p) and v[second_visible(p)]==0: tot_g+=1; diff_g+=d
                elif L<=second_visible(p): tot_g+=1; diff_g+=d
        line.append('k=%d: gated %d/%d, ungated %d/%d'%(k,diff_g,tot_g,diff_u,tot_u))
    print('(2) phase %d, root pairs whose pair image changes with the first visible bit |'%p,' | '.join(line))
# (3) quotient exactness and (4) the subset guard, phase 0
F=load_F(0); cuts=Cuts(F); print('(3) F: %d certified phase-0 words to length 10; contains 11 and 00000: %s'
      %(len(F),'11' in F and '00000' in F))
def subset_guard(canon_word):
    U={s for s in (cuts.step('','0'),cuts.step('','1')) if s is not None}
    for r in canon_word[1:]:
        U={cuts.step(s,r) for s in U}; U.discard(None)
        if not U: return False
    return True
bad4=0
for k in range(4,7):
    for N in range(2,5):
        L=N+k; orig=set(); exist=set(); ordinary=set()
        for v in roots(0,L):
            vis=visible(0,v[:L-1])
            if avoids(cuts,vis): orig.add(image(0,v,k,N))
            if v[0]==0:
                alt=v[:]; alt[0]=1; vis_alt=visible(0,alt[:L-1])
                adm=avoids(cuts,vis) or avoids(cuts,vis_alt)
                if adm!=subset_guard(vis): bad4+=1
                if adm: exist.add(image(0,v,k,N))
                if avoids(cuts,vis): ordinary.add(image(0,v,k,N))
        print('    k=%d N=%d | images of F-avoiding roots %d | existential quotient %d | equal: %s'
              ' | ordinary normalisation %d (strict subset: %s)'
              %(k,N,len(orig),len(exist),orig==exist,len(ordinary),ordinary<orig))
print('(4) subset-guard disagreements with the direct two-origin test:',bad4)
# (5) the depth-139 witness
lines=open('tests/probes/lexicon/rule30_local_record_traces.txt').read().split('\n')
i=[k for k,l in enumerate(lines) if l.startswith('d=139 L=17 phase=0')][0]
blk={l.split('=')[0]:l.split('=')[1] for l in lines[i+1:i+5]}
q=blk['visible']; tr=[int(b) for b in blk['trace']]
v=[tr[t] if tau(0,t)==0 else 0 for t in range(len(tr))]
w=v[:]; w[0]^=1
print('(5) 139 witness: visible begins',q[:5],'| avoids F:',avoids(cuts,q),'| normalised begins',('0'+q[1:])[:5],
      '| ordinary normalisation accepts:',avoids(cuts,'0'+q[1:]),'| existential guard accepts:',subset_guard('0'+q[1:]),
      '| h^4 image over 40 letters identical with q0 flipped:',image(0,v,4,40)==image(0,w,4,40),
      '| h^13 over 40:',image(0,v,13,40)==image(0,w,13,40))
