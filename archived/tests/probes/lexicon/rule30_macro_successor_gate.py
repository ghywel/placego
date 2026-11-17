"""GC1125: test complete macro-successor restrictions, not short cycles.
Missing inference: can the certified31/121/122 guards exclude arbitrary
splices in the existing joint21 recurrent component when k is1,2,3?
A complete endpoint restriction would move this beyond CL301's cycle list.
Record searched: M1/M3/111 with successor/next-macro/followed-by-M2/
transition-restriction ->23 hits12files; known relations and GC1124,
no complete successor lemma. Reuse GC1106's fixed representation.
P1 BEFORE run: every internal111/k1 edge's target has only101/k2
successors in the restriction to k1,2,3 of the named32-state component.
P2 BEFORE run: an internal111/k3 target has no101/k2 successor.
If both hold, once3 occurs,31 is cut and2 is unavailable, so only3
can follow. Without3, a1 forces2, after which121/122 force3.
Counterfactual: short-cycle labels already certify these endpoint facts.
Do not use that inference; inspect every origin-labelled edge pair.
Independent controls: old complete graph counts; independent scalar
whole-path replay of any counter and selected known compatible pairs.
Unexpected: a restriction may hold on a chosen named loop but fail on
other boundary-colour packets in the same recurrent component.
No solver, CUT, language membership, strip widening or record run.
P3 BEFORE the branch-completeness control: no internal101/k1 or101/k3
and no111/k2 edge exists. An unlisted branch would invalidate the
restricted successor proof; test it instead of inheriting a cycle census.
OUTCOME: P1/P2/P3 HELD. Complete internal edge counts17/104/420;
no1->1,1->3 or3->2 pairs. Unlisted101/k1,101/k3,111/k2 all empty.
Scalar two-macro controls pass. P4 numerical ceilings HELD after correcting
the direct2^5,3 normal-form branch; that endpoint failure is retained below.
29524 complete cones agree with the corrected normal form. J+640 follows
by GC706 hand composition, only for the named21 core and k in1,2,3.
No all-k coverage, admission theorem, prize proof or actual sharpness.
One20-second bounded computation; a timeout is failure, not a pass.
"""
import signal
import rule30_111_A_joint_boundary as m


def relation(starts,typ,k):
    high=m.p.bits('1110011011' if typ==101 else '111001111')
    out=m.flow({x:1<<i for i,x in enumerate(starts)},
               m.q.S+m.q.D+m.q.H,{6:m.p.bits('111001001'),16:high})
    out={x:o for x,o in out.items() if (x[0]>>4)&1}
    for _ in range(k):out=m.flow(out,m.q.SS)
    edges=set()
    for z,o in out.items():
        if z not in starts:continue
        while o:
            b=o&-o;o^=b;edges.add((starts[b.bit_length()-1],z))
    return edges


def witness(a,z,typ,k):
    track=m.q.S+m.q.D+m.q.H+m.q.SS*k
    high=m.p.bits('1110011011' if typ==101 else '111001111')
    pin={6:m.p.bits('111001001'),16:high}
    states={a};parents=[]
    for t,b in enumerate(track):
        nxt={}
        for x in sorted(states):
            if (x[0]>>4)&1!=b:continue
            for y in m.j.successors(x,t):
                if t+1 in pin:
                    pre=pin[t+1]
                    if y[0]&((1<<len(pre))-1)!=m.q.pack(pre):continue
                nxt.setdefault(y,x)
        parents.append(nxt);states=set(nxt)
    assert z in states
    path=[z]
    for row in reversed(parents):path.append(row[path[-1]])
    path.reverse()
    assert all(y in m.j.scalar_successors(x,t)
               for t,(x,y) in enumerate(zip(path,path[1:])))
    assert ''.join(str(x[0]&1) for x in path[:-1])==(
        '110100'+'1101000100'*2+'110100'*k)
    return path


def main():
    signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('20s cap')))
    signal.alarm(20)
    graph,typed,comps,named,m2,counts=m.combined_graph()
    assert len(named)==32 and len(m2)==104
    starts=sorted(named)
    r={1:relation(starts,111,1),2:relation(starts,101,2),
       3:relation(starts,111,3)}
    assert r[2]==set(m2)
    extra={(typ,k):relation(starts,typ,k) for typ,k in ((101,1),(101,3),(111,2))}
    print('unlisted_branch_counts',{str(k):len(v) for k,v in extra.items()},flush=True)
    assert not any(extra.values()),extra
    assert {(a,b) for (a,b),types in typed.items() if a in named and b in named and 101 in types}==r[2]
    assert all((a,b) in typed and typ in typed[(a,b)]
               for k,typ in ((1,111),(2,101),(3,111)) for a,b in r[k])
    pairs={(k,j):[(a,b,c) for a,b in sorted(r[k]) for y,c in sorted(r[j]) if b==y]
           for k in r for j in r}
    bad1=[(1,j,x) for j in (1,3) for x in pairs[1,j]]
    bad3=[(3,2,x) for x in pairs[3,2]]
    print('edges', {k:len(v) for k,v in r.items()},
          'pair_counts',{str(k):len(v) for k,v in pairs.items()},flush=True)
    for tag,bad in (('P1',bad1),('P2',bad3)):
        if not bad:print(tag,'HELD',flush=True);continue
        k,j,(a,b,c)=bad[0]
        p=witness(a,b,101 if k==2 else 111,k)
        q=witness(b,c,101 if j==2 else 111,j)
        assert p[-1]==q[0]
        print(tag,'REFUTED','labels',(k,j),'packets',(a,b,c),
              'physical_ticks',len(p)+len(q)-2,'scalar_replay_PASS',flush=True)
    # A known two-edge interface with both origins retained.
    for k,j in ((1,2),(3,3)):
        assert pairs[k,j]
        a,b,c=pairs[k,j][0]
        witness(a,b,101 if k==2 else 111,k)
        witness(b,c,101 if j==2 else 111,j)
    print('independent_pair_controls_PASS',flush=True)
    signal.alarm(0)




# P4 BEFORE normal-form controls: with f54/f56/f69/f114, every finite
# completed word in this exact successor relaxation has at most one
# M3 run. No-M3 duration<=298; prefix before that run<=260; suffix<=32.
# GC706 then gives actual duration<=J+640 inside this restricted core.
# Counterfactual: reject terminal121/122 immediately as in an infinite
# trace. Must fail, and would incorrectly lower the finite298 ceiling.
# First normal-form attempt FAILED at2^5,3: f114 is completed by
# M3's endpoint, so a direct leading2 run before3 has cap4, not5.
# Correct that branch; the predicted numeric ceilings remain under test.
# Controls compare the derived normal form against literal certified
# factors and the independent adjacent-label restrictions, through9 macros.


def normal_form(w):
    a=0
    while a<len(w) and w[a]==2:a+=1
    r=w[a:]
    if not r:return a<=6
    if a>5:return False
    if r in ((1,),(1,2),(1,2,1),(1,2,2)):return True
    if r[:2]==(1,2):r=r[2:]
    elif a>4:return False
    if r and r[-1]==1:r=r[:-1]
    return bool(r) and all(k==3 for k in r)


def normal_controls():
    from itertools import product
    import rule30_111_cut_markers as cuts
    import rule30_f69_macro_guard as f69
    import rule30_fixed_m2_cut_charge as m2cut
    fs=(cuts.F54,cuts.F56,f69.F69,m2cut.pattern())
    total=valid=0;max_non3=0;max_prefix=0;max_suffix=0
    for n in range(10):
        for w in product((1,2,3),repeat=n):
            total+=1
            adjacent=all((a!=1 or b==2) and not(a==3 and b==2)
                         for a,b in zip(w,w[1:]))
            q=cuts.s.visible(w)+'1'
            ok=adjacent and all(f not in q for f in fs)
            assert ok==normal_form(w),w
            if not ok:continue
            valid+=1
            cost=lambda ks:sum(26+6*k for k in ks)
            if 3 not in w:max_non3=max(max_non3,cost(w));continue
            a=w.index(3);b=len(w)-tuple(reversed(w)).index(3)
            assert all(k==3 for k in w[a:b])
            max_prefix=max(max_prefix,cost(w[:a]))
            max_suffix=max(max_suffix,cost(w[b:]))
    assert (max_non3,max_prefix,max_suffix)==(298,260,32)
    assert normal_form((2,)*5+(1,2,2))
    assert normal_form((2,)*6) and not normal_form((2,)*6+(1,))
    print('normal_form_PASS','complete_cones',total,'accepted',valid,
          'sharp_grammar_costs',(max_non3,max_prefix,max_suffix),
          'actual_restricted_core_bound','J+640; hand window composition',
          'no_all_k_or_admission_claim',flush=True)


if __name__=='__main__':
    main()
    normal_controls()
