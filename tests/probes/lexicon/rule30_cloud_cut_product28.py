#!/usr/bin/env python3
"""rule30_cloud_cut_product28.py: the complete cut product over the width-28 strip graph of the collar grammar (CL303).

RUN-ON:     cpu (Python 3 standard library; about ten minutes)
COMMAND:    python3 tests/probes/lexicon/rule30_cloud_cut_product28.py

WHAT. Build the width-28 strip relaxation of GPT's RRL collar grammar (black-A macros M_k = S D H SS^k on the two
branches 101 and 111, one labelled edge per macro, states = 28-cell strip rows at macro boundaries, cell 29 free each
tick: a sound over-approximation of the real typed traces, CL285/CL294), then form its product with the Aho-Corasick
automaton of the certified absent words in hand (L631's nine SLC cuts, L627's 114-bit and L628's 117-bit M2-chain
cuts); a product edge is dropped when a cut completes inside the macro's visible word, and the automaton state is
carried across macro seams so cuts spanning several macros count. Report the cyclic strongly connected components of
the product with the k labels and branches of their internal edges. Also answer GC1124's question: which macro labels
can follow an M1 edge in the 97-state mixed component.

RESULT (first computed in Cloud's scratch on 2026-10-11 and recorded in CL303 and RULE30-PRIZE.md 8.89 Outcome 3; this
file is the self-contained re-run of that computation). Whole graph: 6,431 states, 870,080 edges, two cyclic
components (97 states, mixed labels 1, 2, 3; 10 states, pure M2). No cuts: two cyclic product SCCs (186 states; 10
states). L631's nine cuts: 62 states of label 3 only (branch 111), and the pure-M2 one. All eleven cuts: ONE cyclic
SCC, the pure-M3 self-loops (62 states, 1,073 edges). After an M1 edge the next label is always 2; the realised
consecutive label pairs are 12, 21, 23, 31 and 33. 

ADDED 2026-10-11 (CL306): GC1126's H-low route N = S, D (111 pin), H with site 5 = 0, D (101 pin), H, white SS, white
SS, 58 ticks, as a fourth macro. From all 98,304 A-type rows at width 28: 96,029 origin/end pairs, 185 N sources (none
in the macro graph), 681 N endpoints (575 in it); the closure from them adds nothing; N lies on no cycle; no N endpoint
reaches an N source again; the cut product with N is unchanged (pure M3 only with all eleven cuts). Width-20 control:
1,530 pairs and 51 endpoints, GC1126's numbers.
"""
import itertools, time, sys, re
from collections import deque
sys.setrecursionlimit(1000000)

import itertools, time, sys
sys.setrecursionlimit(100000)
B=lambda s: tuple(int(c) for c in s)
TR_SDH=B('111000')+B('0101100000')+B('0101101010'); TR_SS=B('111010')
TYPES=[B('1110100011111'),B('1110100011100'),B('1110100011101')]
PRE={6:B('111001001'),16:B('1110011011'),26:B('111010')}
VALID={B('11101')+B(w) for w in ('0000','0100','0101','0110','0111')}
def imgs(row,t,W):
    out=set()
    for b in (0,1):
        s=(t%2,)+row+(b,)
        out.add(tuple(s[i-1]^(s[i]|s[i+1]) for i in range(1,W+1)))
    return out

import itertools, time, sys
sys.setrecursionlimit(100000)
TYPESET=set(TYPES)
def sdh_flow(cur,W,pin16,entrance_valid):
    """cur: {row: label}. 26 ticks of S, D, H with the track filter on the parent's site 5; pins at 6 and 16."""
    pins={6:B('111001001'),16:pin16}
    for t,b in enumerate(TR_SDH):
        nxt={}
        for row,lab in cur.items():
            if row[4]!=b: continue
            for y in imgs(row,t,W): nxt[y]=nxt.get(y,0)|lab
        if t+1 in pins:
            p=pins[t+1]; nxt={y:o for y,o in nxt.items() if y[:len(p)]==p}
        cur=nxt
    if entrance_valid: cur={y:o for y,o in cur.items() if y[:9] in VALID}
    return cur
def ss_flow(cur,W,t0=26):
    for j,b in enumerate(TR_SS):
        nxt={}
        for row,lab in cur.items():
            if row[4]!=b: continue
            for y in imgs(row,t0+j,W): nxt[y]=nxt.get(y,0)|lab
        cur=nxt
    return cur
def closure_111(entr,W):
    seen={}; delta=dict(entr); ends={}; waves=0
    while delta:
        for x,o in delta.items(): seen[x]=seen.get(x,0)|o
        out=ss_flow(delta,W)
        for x,o in out.items():
            if x[:13] in TYPESET: ends[x]=ends.get(x,0)|o
        delta={x:o&~seen.get(x,0) for x,o in out.items()}; delta={x:o for x,o in delta.items() if o}; waves+=1
    return seen,ends,waves
def closure_101(entr,W):
    seen={}; delta=dict(entr); ends={}
    while delta:
        for x,o in delta.items(): seen[x]=seen.get(x,0)|o
        out=ss_flow(delta,W)
        for x,o in out.items():
            if x[:13] in TYPESET: ends[x]=ends.get(x,0)|o
        delta={x:o&~seen.get(x,0) for x,o in out.items() if x[:9] in VALID}; delta={x:o for x,o in delta.items() if o}
    return seen,ends
def pairs(ends,starts):
    E=set()
    for e,o in ends.items():
        for i in range(len(starts)):
            if o>>i&1: E.add((starts[i],e))
    return E
def sccs(nodes,adj):
    index={}; low={}; onst=set(); st=[]; out=[]; idx=0
    for root in nodes:
        if root in index: continue
        work=[(root,iter(adj.get(root,())))]; index[root]=low[root]=idx; idx+=1; st.append(root); onst.add(root)
        while work:
            v,it=work[-1]; adv=False
            for w in it:
                if w not in index:
                    index[w]=low[w]=idx; idx+=1; st.append(w); onst.add(w);
                    work.append((w,iter(adj.get(w,())))); adv=True; break
                elif w in onst: low[v]=min(low[v],index[w])
            if adv: continue
            work.pop()
            if work: low[work[-1][0]]=min(low[work[-1][0]],low[v])
            if low[v]==index[v]:
                comp=[]
                while True:
                    w=st.pop(); onst.discard(w); comp.append(w)
                    if w==v: break
                out.append(comp)
    return out
def recurrent(E):
    adj={}
    for a,b in E: adj.setdefault(a,set()).add(b)
    nodes=sorted({a for a,_ in E}|{b for _,b in E}); comps=sccs(nodes,adj)
    return [c for c in comps if len(c)>1 or (len(c)==1 and c[0] in adj.get(c[0],()))], adj

import itertools, time, sys
sys.setrecursionlimit(100000)
hS=B('110100'); hL=B('1101000100')
def closure_lab(entr,W,white):
    """entr: {row: labelmask} at tick 26. Returns ends {(row,k): labelmask}, seen set size."""
    seen={}; delta=dict(entr); ends={}; k=0
    while delta:
        k+=1
        for x,o in delta.items(): seen[x]=seen.get(x,0)|o
        out=ss_flow(delta,W)
        for x,o in out.items():
            if x[:13] in TYPESET: ends[(x,k)]=ends.get((x,k),0)|o
        nxt={}
        for x,o in out.items():
            if white and x[:9] not in VALID: continue
            n=o&~seen.get(x,0)
            if n: nxt[x]=n
        delta=nxt
    return ends,len(seen)
def labelled_edges(startrows,W):
    E=set(); sizes={}
    for c0 in range(0,len(startrows),4096):
        ch=startrows[c0:c0+4096]; lab={s:(1<<i) for i,s in enumerate(ch)}
        a=sdh_flow(lab,W,B('111001111'),False); a={x:o for x,o in a.items() if x[:5]==B('11101')}
        e1,n1=closure_lab(a,W,False); sizes['111']=sizes.get('111',0)+n1
        b=sdh_flow(lab,W,B('1110011011'),True); e2,n2=closure_lab(b,W,True); sizes['101']=sizes.get('101',0)+n2
        for (x,k),o in e1.items():
            for i in range(len(ch)):
                if o>>i&1: E.add((ch[i],x,'111',k))
        for (x,k),o in e2.items():
            for i in range(len(ch)):
                if o>>i&1: E.add((ch[i],x,'101',k))
    return E,sizes
def components(E):
    adj={}
    for a,b,_,_ in E: adj.setdefault(a,set()).add(b)
    nodes=sorted({a for a,_,_,_ in E}|{b for _,b,_,_ in E}); comps=sccs(nodes,adj)
    return [c for c in comps if len(c)>1 or (len(c)==1 and c[0] in adj.get(c[0],()))]
def label_table(E,c):
    cs=set(c); t={}
    for a,b,br,k in E:
        if a in cs and b in cs: t[(br,k)]=t.get((br,k),0)+1
    return dict(sorted(t.items()))

starts20=[tp+tail for tp in TYPES for tail in itertools.product((0,1),repeat=7)]
E20,_=labelled_edges(starts20,20); comps20=components(E20)
compset=sorted({x for c in comps20 for x in c})
seeds=[s+ext for s in compset for ext in itertools.product((0,1),repeat=8)]
seen=set(); frontier=list(seeds); E28=set(); rounds=0
while frontier and rounds<10:
    rounds+=1; new=[s for s in frontier if s not in seen]; seen|=set(new)
    if not new: break
    Ek,_=labelled_edges(new,28); E28|=Ek; frontier=sorted({b for a,b,_,_ in Ek})
comps28=components(E28)
big=max(comps28,key=len); cs=set(big)
adj={}
for a,b,br,k in E28:
    if a in cs and b in cs: adj.setdefault(a,[]).append((b,br,k))
print('component states',len(cs),'| internal labelled edges',sum(len(v) for v in adj.values()))

# GC1124's question: successors of M1 edges
succ={}
for a,v in adj.items():
    for b,br,k in v:
        if k==1: succ.setdefault(b,set()).update(k2 for _,_,k2 in adj.get(b,[]))
print('after an M1 edge, the next macro labels are', sorted(set().union(*succ.values())) if succ else None,
      '| M1 target states',len(succ))
pred={}
for a,v in adj.items():
    for b,br,k in v: pred.setdefault(k,set()).update(k0 for _,_,k0 in adj.get(a,[]) if False)
# the full label-pair relation (k then k')
pairs=set()
for a,v in adj.items():
    for b,br,k in v:
        for _,_,k2 in adj.get(b,[]): pairs.add((k,k2))
print('consecutive label pairs (k, next k) realised in the component:',sorted(pairs))
# cuts
cuts={   # L631's nine cake_lpr-certified SLC cuts (phase 0), copied from the ledger entry
 'f54':'000010000100100100100100001000010010010000100001001001',
 'f56':'01000010000100100100001000010010010010000100001001001000',
 'f61':'1000010000100100100100001000010010010010000100001001001001001',
 'f62':'00001001001000010000100100100100001000010010010000100001001001',
 'f63':'001001000010000100100100001000010010010010000100001001001001001',
 'f65':'00001001001001001000010000100100100001000010010010010000100001001',
 'f68':'10000100001001001001000010000100100100001000010010010010000100001001',
 'f69':'010000100001001001000010000100100100100001000010010010010000100001001',
 'f71':'10000100001001001000010000100100100100001000010010010010010000100001001'}
cuts['f114']=('00001'+'00001'+'001'+'001'+'001')*6; cuts['f117']=('001'+'001'+'001'+'00001'+'00001')*6+'001'
hS=[1,1,0,1,0,0]; hL=[1,1,0,1,0,0,0,1,0,0]
def vis(ks):
    w=[]
    for k in ks: w+=hS+hL+hL+hS*k
    return ''.join(map(str,w[0::2]))
assert cuts['f114'] in vis((2,)*9) and cuts['f117'] in vis((2,)*9)
# guard against a copying error in the hard-coded cuts: each must lie in the word L631 names for it (lengths too)
for name,w in cuts.items(): assert len(w)==int(name[1:]), name
assert all(cuts[n] in vis((3,1,2,2,2,3)) for n in ('f54','f65','f69'))
assert all(cuts[n] in vis((1,2,2,2,3,3)) for n in ('f61','f69'))
assert all(cuts[n] in vis((1,2)*8) for n in ('f56','f62','f68'))
assert all(cuts[n] in vis((1,2,3)*6) for n in ('f54','f63','f65','f71'))
# Aho-Corasick
goto=[{}]; fail=[0]; out=[set()]
for name,p in cuts.items():
    s=0
    for ch in p:
        if ch not in goto[s]: goto.append({}); fail.append(0); out.append(set()); goto[s][ch]=len(goto)-1
        s=goto[s][ch]
    out[s].add(name)
from collections import deque
q=deque()
for ch,s in goto[0].items(): q.append(s)
while q:
    r=q.popleft()
    for ch,s in goto[r].items():
        q.append(s); f=fail[r]
        while f and ch not in goto[f]: f=fail[f]
        fail[s]=goto[f][ch] if ch in goto[f] and goto[f][ch]!=s else 0
        out[s]|=out[fail[s]]
def step(s,ch):
    while s and ch not in goto[s]: s=fail[s]
    return goto[s].get(ch,0)
print('AC states',len(goto),'| cuts',sorted(cuts,key=lambda n:int(n[1:])))
def run_cuts(name_set):
    words={k:vis((k,)) for k in range(1,40)}
    dead=lambda s: bool(out[s]&name_set)
    padj={}; start=[(s,0) for s in cs]; stack=list(start); pseen=set(start)
    while stack:
        (s,a)=stack.pop()
        for b,br,k in adj.get(s,[]):
            a2=a; ok=True
            for ch in words[k]:
                a2=step(a2,ch)
                if dead(a2): ok=False; break
            if not ok: continue
            padj.setdefault((s,a),[]).append(((b,a2),br,k))
            if (b,a2) not in pseen: pseen.add((b,a2)); stack.append((b,a2))
    # Tarjan SCC
    index={}; low={}; onst=set(); st=[]; sccs=[]; cnt=[0]
    def strong(v):
        index[v]=low[v]=cnt[0]; cnt[0]+=1; st.append(v); onst.add(v)
        for w,_,_ in padj.get(v,[]):
            if w not in index: strong(w); low[v]=min(low[v],low[w])
            elif w in onst: low[v]=min(low[v],index[w])
        if low[v]==index[v]:
            comp=[]
            while True:
                w=st.pop(); onst.discard(w); comp.append(w)
                if w==v: break
            sccs.append(comp)
    for v in list(pseen):
        if v not in index: strong(v)
    res=[]
    for comp in sccs:
        S=set(comp); labs=set(); brs=set(); n=0
        for v in comp:
            for w,br,k in padj.get(v,[]):
                if w in S: labs.add(k); brs.add(br); n+=1
        if n: res.append((len(comp),n,sorted(labs),sorted(brs)))
    return len(pseen),res
NINE=set(n for n in cuts if n not in ('f114','f117'))
for title,names in (('L631 nine cuts only',NINE),('all eleven cuts',set(cuts))):
    n,res=run_cuts(names)
    print('\n==',title,': product states',n,'| cyclic SCCs',len(res))
    for size,ne,labs,brs in sorted(res,reverse=True)[:12]:
        print('   SCC states',size,'internal edges',ne,'k labels',labs,'branches',brs)
# and the cycles of each surviving SCC: simple cycles up to length 6 by k-word

# the same over the WHOLE width-28 labelled graph (every component, not only the largest)
alls={a for a,b,_,_ in E28}|{b for a,b,_,_ in E28}
adj={}
for a,b,br,k in E28: adj.setdefault(a,[]).append((b,br,k))
cs=alls
print('\nwhole W=28 graph: states',len(cs),'edges',len(E28),'components',len(comps28),
      'sizes',sorted((len(c) for c in comps28),reverse=True)[:8],'| k labels',sorted({k for *_,k in E28})[:12],'...')
small=set([c for c in comps28 if len(c)==10][0])
labs10=sorted({k for a,b,_,k in E28 if a in small and b in small})
print('second component (10 states): k labels of its internal edges',labs10)
for title,names in (('no cuts',set()),('L631 nine cuts only',NINE),('all eleven cuts',set(cuts))):
    n,res=run_cuts(names)
    print('==',title,': product states',n,'| cyclic SCCs',len(res))
    for size,ne,labs,brs in sorted(res,reverse=True)[:12]:
        print('   SCC states',size,'internal edges',ne,'k labels',labs,'branches',brs)

# ---------- N edges (GC1126's H-low route) added to the whole width-28 graph, then the cut product ----------
S_=B('111000'); D_=B('0101100000'); H_=B('0101101010'); SS_=B('111010')
def flow5(lab,t0,track,W,pinfn=None):
    cur=dict(lab); t=t0
    for bit in track:
        nxt={}
        for r,o in cur.items():
            if r[4]!=bit: continue
            for s in imgs(r,t,W): nxt[s]=nxt.get(s,0)|o
        cur=nxt; t+=1
    if pinfn: cur={r:o for r,o in cur.items() if pinfn(r)}
    return cur,t
def n_edges(startrows,W):
    E=set()
    for c0 in range(0,len(startrows),4096):
        ch=startrows[c0:c0+4096]; lab={s:(1<<i) for i,s in enumerate(ch) if s[:13] in TYPESET}
        a,t=flow5(lab,0,S_,W,lambda r: r[:9]==B('111001001'))
        a,t=flow5(a,t,D_,W,lambda r: r[:9]==B('111001111'))
        a,t=flow5(a,t,H_,W,lambda r: r[4]==0)
        a,t=flow5(a,t,D_,W,lambda r: r[:10]==B('1110011011'))
        a,t=flow5(a,t,H_,W,lambda r: r[:9] in VALID)
        a,t=flow5(a,t,SS_,W,lambda r: r[:9] in VALID)
        a,t=flow5(a,t,SS_,W,lambda r: r[:13] in TYPESET)
        assert t==58
        for x,o in a.items():
            for i in range(len(ch)):
                if o>>i&1: E.add((ch[i],x,'N','N'))
    return E

# control at W = 20 from ALL A-type rows (gc1126b: 51 endpoints, 1,530 pairs)
A20=[tp+tail for tp in TYPES for tail in itertools.product((0,1),repeat=7)]
E20n=n_edges(A20,20)
print('W=20 control: N edges',len(E20n),'(pairs)','| endpoints',len({b for a,b,_,_ in E20n}))
# N at W = 28 from ALL A-type rows
A28=[tp+tail for tp in TYPES for tail in itertools.product((0,1),repeat=15)]
EN=n_edges(A28,28); Nend={b for a,b,_,_ in EN}; Nsrc={a for a,b,_,_ in EN}
alls={a for a,b,_,_ in E28}|{b for a,b,_,_ in E28}
print('W=28 from all',len(A28),'A rows: N edges',len(EN),'| N sources',len(Nsrc),'| N endpoints',len(Nend))
print('   sources in the macro graph',len(Nsrc&alls),'| endpoints in the macro graph',len(Nend&alls))
# closure from the N endpoints: macro edges and N edges, until nothing new
EALL=set(E28)|EN; known=set(alls)|Nsrc; frontier=sorted(Nend-known); rounds=0
while frontier and rounds<8:
    rounds+=1; known|=set(frontier)
    Ek,_=labelled_edges(frontier,28); En=n_edges(frontier,28); EALL|=Ek|En
    frontier=sorted(({b for a,b,_,_ in Ek}|{b for a,b,_,_ in En})-known)
    print('  closure round',rounds,': new macro edges',len(Ek),'new N edges',len(En),
          '| next frontier',len(frontier))
adj={}
for a,b,br,k in EALL: adj.setdefault(a,[]).append((b,br,k))
cs={a for a,b,_,_ in EALL}|{b for a,b,_,_ in EALL}
compsN=components(EALL)
print('graph with N: states',len(cs),'edges',len(EALL),'components',len(compsN),
      'sizes',sorted((len(c) for c in compsN),reverse=True)[:8])
for c in compsN:
    S=set(c); labs=sorted({str(k) for a,b,_,k in EALL if a in S and b in S})
    if 'N' in labs: print('  component of size',len(c),'has internal N edges; labels',labs)
# can an N endpoint ever reach an N source again (any path)?  BFS over EALL from Nend
reach=set(Nend); stack=list(Nend)
while stack:
    x=stack.pop()
    for b,_,_ in adj.get(x,[]):
        if b not in reach: reach.add(b); stack.append(b)
print('N endpoints reach',len(reach),'states; among them N sources:',len(reach&Nsrc),
      '| macro-component states:',len(reach&alls))
visN=''.join(str(b) for b in (hS+hL*4+hS*2)[0::2]); assert len(visN)==29
def run_cuts2(name_set):
    words={k:vis((k,)) for k in range(1,40)}; words['N']=visN
    dead=lambda s: bool(out[s]&name_set)
    padj={}; start=[(s,0) for s in cs]; stack=list(start); pseen=set(start)
    while stack:
        (s,a)=stack.pop()
        for b,br,k in adj.get(s,[]):
            a2=a; ok=True
            for ch in words[k]:
                a2=step(a2,ch)
                if dead(a2): ok=False; break
            if not ok: continue
            padj.setdefault((s,a),[]).append(((b,a2),br,k))
            if (b,a2) not in pseen: pseen.add((b,a2)); stack.append((b,a2))
    index={}; low={}; onst=set(); st=[]; sccs=[]; cnt=[0]
    def strong(v):
        index[v]=low[v]=cnt[0]; cnt[0]+=1; st.append(v); onst.add(v)
        for w,_,_ in padj.get(v,[]):
            if w not in index: strong(w); low[v]=min(low[v],low[w])
            elif w in onst: low[v]=min(low[v],index[w])
        if low[v]==index[v]:
            comp=[]
            while True:
                w=st.pop(); onst.discard(w); comp.append(w)
                if w==v: break
            sccs.append(comp)
    for v in list(pseen):
        if v not in index: strong(v)
    res=[]
    for comp in sccs:
        Sx=set(comp); labs=set(); brs=set(); n=0
        for v in comp:
            for w,br,k in padj.get(v,[]):
                if w in Sx: labs.add(str(k)); brs.add(br); n+=1
        if n: res.append((len(comp),n,sorted(labs),sorted(brs)))
    return len(pseen),res
NINE=set(n for n in cuts if n not in ('f114','f117'))
for title,names in (('no cuts',set()),('L631 nine cuts',NINE),('all eleven cuts',set(cuts))):
    n,res=run_cuts2(names)
    print('== with N,',title,': product states',n,'| cyclic SCCs',len(res))
    for size,ne,labs,brs in sorted(res,reverse=True)[:12]:
        print('   SCC states',size,'internal edges',ne,'labels',labs,'branches',brs)
