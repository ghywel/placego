"""GC1139: does the new001000 entrance reach the mixed C/J invariant?
Missing inference: GC1138 bounds one ordinary run; a later S could
reset it. GC1087 forbids resets only after entering C or its guarded J.
Record searched:111001001000|ordinary001000 AND mixed|admission|J
->6 hits3 files, GC1082/1138 ordinary-only statements. GC1078,
1084 and1087 read. No established mixed admission on this prefix.
P1 BEFORE run: every ordinary111001001000 source returns C or
one of GC1087's two J prefixes after D10. A complete source24
cone fixes the14 endpoint cells, so all4096 assignments are an
all-tail certificate, not a cutoff scan. If P1 fails retain the
first bad finite cone; do not infer its actual white-A ancestry.
Counterfactual: the low12 label omits a sparse J entrance bit.
Controls: independent literal/packed, track and old C/J guards;
all16 farther four-bit exteriors on a bad cone. Unexpected check:
an unrestricted101 high with no C past can return A; preserve
that negative control so a white-A ban is never inferred from101.
Stop at this mixed admission lemma; no solver, CUT, graph,
membership, record, widening or ancestry-age scan.
"""
from itertools import product
from rule30_sl_no_refork import bits,run
from rule30_low_core_closure import CORE,D
from rule30_core_short_bridge import update


def certificate(source,steps):
    rows=[source]
    for t in range(steps):
        old=rows[-1]
        if not old:
            rows.append(());continue
        new=update((t%2,)+old)
        if old[-1]:new+=((old[-2] if len(old)>1 else t%2)^1,)
        for far in (0,1):
            assert update((t%2,)+old+(far,))[:len(new)]==new
        rows.append(new)
    return rows


def admitted(row):
    return (row[6:9] in CORE or row[:12]==bits('111001101100')
            or row[:14]==bits('11100110111110'))


def main():
    root=bits('111001001000');counts={};bad=[];ends=set()
    for tail in product((0,1),repeat=12):
        src=root+tail;r=run(src,10);q=r[10]
        assert tuple(y[4] for y in r[:10])==D
        assert q[:6]==bits('111001')
        assert q[6:9] in CORE|{bits('101')}
        ends.add(q);key='C' if q[6:9] in CORE else ('J' if admitted(q) else 'unguarded101')
        counts[key]=counts.get(key,0)+1
        if not admitted(q):bad.append((src,r))
    print('complete_source24_cones4096','endpoint14',len(ends),
          'counts',counts,'P1_mixed_admission',not bool(bad),flush=True)
    if bad:
        src,r=bad[0]
        print('first_bad_source24',''.join(map(str,src)),
              'endpoint14',''.join(map(str,r[10])),flush=True)
        for far in product((0,1),repeat=4):
            ext=run(src+far,10)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(r))
        print('bad_exteriors16_PASS',flush=True)
    # P2 BEFORE this adaptive control: GC1138's actual tick21
    # prefix01100100011001 retains enough high-return ancestry
    # to exclude the unguarded101 outcomes at tick36. Test its
    # complete29-cell cone, phase1, rather than assigning low24.
    # A failure here still has no asserted white-A source lift.
    root_mid=bits('01100100011001');mid_counts={};mid_bad=[]
    for tail in product((0,1),repeat=15):
        src=root_mid+tail;r=run(src,15,phase=1);q=r[15]
        assert r[5][:12]==root
        assert tuple(y[4] for y in r[5:15])==D
        assert q[:6]==bits('111001')
        key='C' if q[6:9] in CORE else ('J' if admitted(q) else 'unguarded101')
        mid_counts[key]=mid_counts.get(key,0)+1
        if not admitted(q):mid_bad.append((src,r))
    print('complete_mid29_cones32768','counts',mid_counts,
          'P2_correlated_admission',not bool(mid_bad),flush=True)
    if mid_bad:
        src,r=mid_bad[0]
        print('first_bad_mid29',''.join(map(str,src)),
              'low24',''.join(map(str,r[5])),
              'endpoint14',''.join(map(str,r[15])),flush=True)
        for far in product((0,1),repeat=4):
            ext=run(src+far,15,phase=1)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(r))
        print('correlated_bad_exteriors16_PASS',flush=True)
    # P3 BEFORE the actual-lineage scope check: the retained mature
    # SS sourceV33 followed by25 displayed white cells reaches an
    # unguarded101 at44. If it misses, check only the16 retained
    # A cylinders with displayed white completions; no age search.
    # A bad fresh low or mid prefix alone does not establish this.
    from rule30_white_A_high_LL_guard import selector
    V=bits('000111011001010010000000000000000')
    candidates=[('matureSS',V+(0,)*25,8)]
    candidates += [('A25',bits('1110100011011')+tail+(0,)*25,0)
                   for tail in product((0,1),repeat=12) if selector(tail)
                   and run(bits('1110100011011')+tail,6)[6][17:19]==(1,1)]
    witness=None
    for name,src,offset in candidates:
        r=run(src,offset+36)
        if not admitted(r[offset+36]):
            witness=(name,src,offset,r);break
    print('P3_actual_lineage_unguarded',bool(witness),flush=True)
    if witness:
        name,src,offset,r=witness
        assert r[offset][:13]==bits('1110100011011')
        assert r[offset+21][:14]==root_mid
        assert r[offset+26][:12]==root
        print('actual_label',name,'source',''.join(map(str,src)),
              'length',len(src),'A_offset',offset,
              'endpoint14',''.join(map(str,r[offset+36][:14])),flush=True)
        for far in product((0,1),repeat=4):
            ext=run(src+far,offset+36)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(r))
        print('actual_lineage_exteriors16_PASS',flush=True)
    # P4 BEFORE a proof-cover attempt: retaining the full A25
    # cylinder eliminates the bad mid29 outputs, despite their
    # common14 prefix. Build fresh-right certificate leaves; prune
    # only when C/J is proved or disproved by known endpoint bits.
    # Exhaustion gives a finite all-tail cover, cap8192 UNKNOWN;
    # a counter requires an actual source leaf, not the mid image.
    J=(bits('111001101100'),bits('11100110111110'))
    roots=[src[:25] for name,src,offset in candidates if name=='A25']
    cover={p:[] for p in roots};nodes=0;counter=None;incomplete=False
    for root_A in roots:
        stack=[root_A]
        while stack and nodes<8192:
            src=stack.pop();nodes+=1;q=certificate(src,36)[36]
            if len(q)>=9 and q[6:9] in CORE:
                cover[root_A].append(src);continue
            if any(len(q)>=len(j) and q[:len(j)]==j for j in J):
                cover[root_A].append(src);continue
            if len(q)>=9 and q[6:9]==bits('101') and all(
                    q[:min(len(q),len(j))]!=j[:min(len(q),len(j))] for j in J):
                counter=(src,q);break
            stack.extend([src+(1,),src+(0,)])
        incomplete=bool(stack)
        if counter or incomplete:break
    print('actual_A_cover_nodes',nodes,'status',
          'COUNTER' if counter else ('UNKNOWN' if incomplete else 'COVERED'),
          'covered_roots',sum(bool(v) for v in cover.values()),flush=True)
    if counter:
        src,q=counter
        print('actual_A_counter',''.join(map(str,src)),'length',len(src),
              'endpoint',''.join(map(str,q)),flush=True)
    elif not incomplete:
        import hashlib
        # P5 BEFORE structural extraction: every cover leaf already
        # forces low-site13 white at26, explaining C directly via
        # GC1082's low mid01 formula. If not, retain its actual
        # sparse-bit distribution rather than inventing that lemma.
        lengths={};end_types={};low13={};triples={};controls=0
        for root_A,leaves in cover.items():
            words=sorted(''.join(map(str,p)) for p in leaves)
            assert all(not b.startswith(a) for a,b in zip(words,words[1:]))
            n=max(map(len,leaves))
            assert sum(1<<(n-len(p)) for p in leaves)==1<<(n-25)
            for src in leaves:
                q=certificate(src,36)[36]
                assert admitted(q)
                lengths[len(src)]=lengths.get(len(src),0)+1
                typ='C' if q[6:9] in CORE else 'J'
                end_types[typ]=end_types.get(typ,0)+1
                triples[q[6:9]]=triples.get(q[6:9],0)+1
                low=certificate(src,26)[26]
                b=low[12] if len(low)>12 else 'unknown'
                low13[b]=low13.get(b,0)+1
                # Independent complete-cone trajectories verify the
                # shield on four different exterior patterns. The
                # all-tail proof remains the fresh-bit induction.
                for pattern in ((0,), (1,), (0,1), (1,0)):
                    far=tuple(pattern[j%len(pattern)] for j in range(50-len(src)))
                    r=run(src+far,36)
                    assert all(r[t][:min(len(y),len(r[t]))]==y[:min(len(y),len(r[t]))]
                               for t,y in enumerate(certificate(src,36)))
                    assert admitted(r[36]);controls+=1
        print('actual_A_all_tail_cover_PASS','leaves',sum(map(len,cover.values())),
              'max_source',max(len(p) for leaves in cover.values() for p in leaves),flush=True)
        payload='\n'.join(sorted(''.join(map(str,p)) for leaves in cover.values() for p in leaves))+'\n'
        print('cover_lengths',lengths,'leaf_endpoint_types',end_types,
              'cover_sha256',hashlib.sha256(payload.encode()).hexdigest(),flush=True)
        print('independent_complete50_controls',controls,'PASS',flush=True)
        print('P5_low13',low13,'endpoint_triples',triples,flush=True)
        # P6 BEFORE the local structural proof: the inherited extra
        # white low-site13 alone forces010 at the next D return.
        local=certificate(bits('1110010010000'),10)
        print('P6_low13_exact010_prefix_attempt',local[10][:9]==bits('111001010'),
              'prefix_lengths',[len(y) for y in local],
              'endpoint',''.join(map(str,local[10])),flush=True)
        # P6b BEFORE clarifying this failed exact010 prediction:
        # the local white13 guard fixes only010 or011; the original
        # A lineage supplied more than this one bit. Complete23
        # cones distinguish a true counter from prefix loss.
        local_types={}
        for far in product((0,1),repeat=10):
            q=run(bits('1110010010000')+far,10)[10]
            assert q[:8]==bits('11100101')
            local_types[q[6:9]]=local_types.get(q[6:9],0)+1
        print('P6b_low13_complete23_cones1024',local_types,flush=True)
        mature=run(V+(0,)*25,44)
        assert mature[8][:25] in cover and admitted(mature[44])
        print('mature_SS_core44',''.join(map(str,mature[44][:14])),flush=True)
    # The inherited J premise matters: fresh101 is insufficient.
    r=run(bits('1110011011101000000000000')+(0,)*12,10)
    assert r[10][:9]==bits('111010001')
    print('unexpected_fresh101_A_control_PASS',flush=True)


if __name__=='__main__':main()

# OUTCOME: P1/P2 REFUTED by all-tail finite cones; neither fresh
# low12 nor the common mid14 guard alone implies C/J admission.
# P3 REFUTED: the retained white-completed actual candidates all
# admit. P4 HELD by a complete prefix-free cover of all16 original
# negative A25 cylinders:273 leaves, maximum source32, all in010
# at36. The4096/32768 finite cones are diagnostics, not the cover
# proof. Every cover step quantifies the fresh exterior; independent
# complete50 trajectories check each leaf. P5 HELD: all leaves retain
# low13=0 at26. P6's contiguous method loses the ninth endpoint bit,
# but the1024 complete23 cones prove generic0010000-to010 exactly;
# P6b's010-or011 prediction is strengthened to010. GC1087 then
# bars all later SS, A and high LL; the mature V33 counter admits
# by44 for every tail. The12 positive entrances and global admission
# remain outside this theorem. No all-depth record or prize claim.
