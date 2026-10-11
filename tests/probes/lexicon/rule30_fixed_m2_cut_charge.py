"""GC1114 (corrected GC1116): the exact M2 rotation can pay more than rotation-free cover.

Specific missing inference: the candidate (LLSSS)^6 has length 114,
whereas GC1111/13 used an unspecified 120 rotation. Derive a sharp
weighted bound for typed101 macro words with <=2 non-M2 macros,
and the optional-wait threshold for E_m. This is pattern avoidance
in a proved overapproximation, NOT exact CA language membership.
L627 is flagged at 4b22d445, but the Git object is unavailable after
a bounded fetch failure. Treat its proposed pattern as a candidate;
NO verified absence is inferred from a flag. Receipt/ACK pending.
Record searched: M2|M_2|LLSSS|L627 with 114|132|waiting|772|228
->9 hits in 3 files; relevant GC1103/1111/1113 and spellings reused.
P1 BEFORE execution: avoiding this specific 114 pattern bounds
completed typed101 words by 16 macros and 620 physical ticks,
sharp at k=(2^4,3,2^4,3,2^6). If confirmed absent in either phase,
this pays for GC1103's whole typed101 chain independent of J.
REFUTED-BY: a legal weighted automaton path exceeding 620 ticks.
P2 BEFORE execution: E_2 avoids the cut, E_3 contains it at
visible age 19 (first M2 onset 16 plus the rotation 3). Thus the
specific receipt would cap optional waits by 2/bridge 228 ticks,
not GC1113's rotation-independent 3/266. Branching remains.
REFUTED-BY: missing pattern in E_3, or its occurrence in E_2.
Counterfactual: six M2 macros always contain the cut without a
successor. Must fail: phase 0 six-M2 word has 114 samples, but the
cut starts at phase 3 and needs three additional samples.
Controls: KMP finite falling-rank proof versus literal avoidance;
independent physical h(L)^2 h(S)^3 even samples spell the cut;
hand run splitting predicts the extremal weighted word.
Unexpected check: a terminal k=1 after five M2 macros lacks the
six following samples needed by the usual nonterminal charge.
Preserve this endpoint exception when bounding finite words.
OUTCOME: P1/P2 HELD. All 41 reachable states have a locally
verified weighted rank at most 620 and count rank at most 16.
Every KMP transition, including rejected ones, agrees with an
independent literal suffix check. The displayed 620-tick word
avoids the cut. E_3 contains it at 19; E_2 avoids it. Six M2
macros alone miss it, as does terminal 2^5,1; appending the next
macro restores the latter charge. Absence receipt remains unread
and unverified here; no actual membership or record claim.
CORRECTION GC1116: the preceding outcome was for marker-start h
blocks. L627's certified cut uses gap-ending blocks and is shifted
one sample. The correction prediction620/16 FAILED: exact ranks
are672/18 on43 states, attained by2^5,1,2^5,1,2^6. Five M2 before
M1 plus a successor now avoids the cut. E3 alone avoids it; E3 plus
its fixed A endpoint1 contains it at20, so actual bridge m<=2 still
holds. All literal transition controls pass for the corrected cut.
The executed pattern below is exactly Local's114 bits. No membership
query or blanket rotation absence is claimed.
"""
from functools import lru_cache
import rule30_mixed_m2_overlap as old

# GC1116 correction, BEFORE rechecking: Local's gap blocks end in1;
# h's even blocks begin at the marker. The L627 cut is shifted ONE
# sample. Predict sharp620/16 survives; E3 alone avoids the cut, but
# E3 plus its fixed A endpoint marker contains it. Counterfactual:
# dropping this endpoint still detects E3. It must fail. Independent
# literal transitions remain the control; no CA-membership rerun.


def pattern():
    h={'S':'110100','L':'1101000100'}
    physical=''.join(h[a] for a in 'LLSSS'*6)
    f=physical[::2]
    f=f[1:]+f[:1]
    q=old.spell((2,))
    assert f==('00001'*2+'001'*3)*6
    assert f==(q[4:]+q[:4])*6 and len(f)==114
    return f


def main():
    f=pattern()
    words={k:old.spell((k,)) for k in (1,2,3)}
    prefix=[0]*len(f)
    for i in range(1,len(f)):
        j=prefix[i-1]
        while j and f[i]!=f[j]: j=prefix[j-1]
        if f[i]==f[j]: j+=1
        prefix[i]=j
    def step(state,word):
        for bit in word:
            while state and f[state]!=bit: state=prefix[state-1]
            if f[state]==bit: state+=1
            if state==len(f): return None
        return state
    edges={}
    todo=[(0,0)]
    seen=set(todo)
    while todo:
        e,s=todo.pop()
        successors=[]
        for k,w in words.items():
            ee=e+(k!=2)
            if ee>2: continue
            ss=step(s,w)
            if ss is None: continue
            target=(ee,ss)
            successors.append((target,k,2*len(w)))
            if target not in seen: seen.add(target);todo.append(target)
        edges[e,s]=successors
    active=set()
    @lru_cache(None)
    def rank(x):
        assert x not in active,'avoidance cycle'
        active.add(x)
        value=max((ticks+rank(y) for y,k,ticks in edges[x]),default=0)
        active.remove(x)
        return value
    assert rank((0,0))==672
    assert all(rank(x)>=ticks+rank(y) for x,es in edges.items()
               for y,k,ticks in es)
    # Independent literal suffix control checks every transition, including
    # rejected edges; it does not use the KMP prefix table.
    for e,s in edges:
        for k,w in words.items():
            text=f[:s]+w
            expected=(None if f in text else
                      max(j for j in range(len(f))
                          if j==0 or text.endswith(f[:j])))
            assert step(s,w)==expected
    @lru_cache(None)
    def count_rank(x):
        return max((1+count_rank(y) for y,k,t in edges[x]),default=0)
    assert count_rank((0,0))==18
    witness=(2,)*5+(1,)+(2,)*5+(1,)+(2,)*6
    literal=old.spell(witness)
    assert f not in literal and 2*len(literal)==672
    assert f not in old.spell((2,)*6)
    assert f in old.spell((2,)*7)
    assert f not in old.spell((2,)*5+(3,))
    assert f in old.spell((2,)*5+(3,1))
    assert f not in old.spell((2,)*5+(1,))
    assert f not in old.spell((2,)*5+(1,3))
    assert f in old.spell((2,)*6+(1,))
    e2=old.spell((1,)+(2,)*4+(3,))
    e3=old.spell((1,)+(2,)*5+(3,))
    assert f not in e2+'1' and f not in e3
    assert (e3+'1').find(f)==20
    bare=[old.spell((3,1,2,2,3)),old.spell((1,2,2,3,3))]
    rr=old.rank_certificate(old.pair_graph(bare,old.spell((2,))))
    assert max(rr.values())==68
    print(dict(original_P1_P2='former rotation only',correction_prediction='REFUTED',controls='PASS',reachable_states=len(edges),
               typed_returns=18,typed_ticks=672,optional_waits=2,
               bridge_ticks=228,first_cut_sample=20,
               terminal_k1_k3_exception='retained',falling_rank='PASS',
               absence_verified='L627 both phases, received',
               pattern_shift=1,bridge_endpoint_marker=1))


if __name__=='__main__': main()
