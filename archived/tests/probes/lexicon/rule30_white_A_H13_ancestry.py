"""GC1145: original white-A lineage forces exactly two H13 prefixes.
Missing inference: retain an original-A constraint across S-D and
whitening, beyond GC1143's failed generic H111 carrier.
Record searched:676|non.LL|original.A AND
ancestry|white.SS|whiten|guard ->51hits20files.
GC1099/1100/1136/1141/1143/1144 sources read.
P1 before: GC1144's pin13 transfers from the eleven D111 A19
cylinders. REFUTED: three force H13=1110011111110 for all tails.
44 initial full80cell literal/packed controls agree with certificates.
P2 before adaptive cover: every eleven-root H10 is black, and
H10..13 have at most4 patterns. Split only the next original bit
until H13 is certified, cap8192 total nodes; cap UNKNOWN stops.
P2 HELD:81 nodes,46 leaves, exactly1110 or1000, maxsource25.
P4 before final image classification: high-LL selector iff H13=1000
in this original-A lineage; check all704 A25 assignments against
the reviewed selector and unique causal leaf, not a new trajectory scan.
Counterfactual: retaining H13 still loses original-A correlations.
P3 before: these two H13 prefixes guard all subsequent white-A/B
SS exits. Reuse existing width20 only; stop at first bad exit.
P3 REFUTED: badB at third SS, explicit scalar path retained;
no widened strip, actual-lift inverse or cosmetic carrier variant.
Independent controls: fresh-right induction at every leaf, complete
prefix-free/Kraft cover, every reached scalar edge, four complete
literal/packed histories per leaf. Unexpected check: original24/25
can change H-low versus S while H10 stays black; verify known
GC1136 sensitivity controls. The stronger same-H13 guess fails. No Local or Cloud run duplicated.
"""
from collections import Counter,deque
from fractions import Fraction
from hashlib import sha256
import rule30_pin13_SS_exit_guard as a
from rule30_001000_mixed_admission import certificate
from rule30_white_A_high_LL_guard import selector
q=a.q;g=a.g;bits=a.bits;run=a.run
WORDS=('010001','010010','010011','011010','011011','011100',
       '100001','100100','100101','100110','100111')
PINS={'1110011111110','1110011111000'}

def cover():
    nodes=0;leaves=[];counts=Counter();controls=0
    for word in WORDS:
        root=bits('1110100011011'+word);stack=[root];sub=[]
        while stack:
            assert nodes<8192,'UNKNOWN node cap; stop'
            src=stack.pop();nodes+=1;rows=certificate(src,16)
            if len(rows[16])<13:
                stack.extend((src+(1,),src+(0,)));continue
            h=''.join(map(str,rows[16][:13]));assert h in PINS
            sub.append(src);leaves.append((''.join(map(str,src)),h));counts[h[9:]]+=1
            for pat in ((0,),(1,),(0,1),(1,0)):
                full=run(src+tuple(pat[j%len(pat)] for j in range(80-len(src))),26)
                assert all(full[t][:len(r)]==r for t,r in enumerate(rows))
                controls+=1
        assert sum((Fraction(1,1<<(len(s)-19)) for s in sub),Fraction(0))==1
        assert all(not s[:len(t)]==t for i,s in enumerate(sub) for j,t in enumerate(sub) if i!=j)
        # Complete cylinder membership at the maximum source width,
        # independently of the adaptive stopping traversal.
        n=max(map(len,sub))
        for u in range(1<<(n-19)):
            src=root+tuple((u>>j)&1 for j in range(n-19))
            assert sum(src[:len(s)]==s for s in sub)==1
    digest=sha256(''.join(s+' '+h+'\n' for s,h in sorted(leaves)).encode()).hexdigest()
    assert set(h for s,h in leaves)==PINS
    print('cover_nodes',nodes,'leaves',len(leaves),'H10..13',dict(counts),
          'maxsource',max(len(s) for s,h in leaves),'digest',digest,
          'prefix_free_complete_Kraft_PASS','literal_packed_controls',controls,flush=True)
    # Exact all-tail counter to pin0100 transfer, no selected exterior.
    for word in ('010001','100101','100111'):
        assert ''.join(map(str,certificate(bits('1110100011011'+word),16)[16]))=='1110011111110'
    sensitive=('011011010000','011011010001','011011010010')
    hs=[];returns=[]
    for far in sensitive:
        src=bits('1110100011011'+far);r=run(src+(0,)*55,26)
        hs.append(''.join(map(str,r[16][:13])));returns.append(''.join(map(str,r[26][:9])))
        assert bool(selector(bits(far)))==bool(r[26][:6]==bits('111001'))
    print('unexpected_source24_25_sensitivity_H13',hs,'H_return_prefix9',returns,flush=True)
    # Independently compose the complete cover with the reviewed
    # original-A high-LL selector. 25 is its full source support.
    joint=Counter()
    for word in WORDS:
        root='1110100011011'+word
        for u in range(64):
            src=root+''.join(str((u>>j)&1) for j in range(6))
            labels=[h for s,h in leaves if src.startswith(s)]
            assert len(labels)==1
            h=labels[0];ll=bool(selector(bits(src[13:])))
            joint[(h[9:],ll)]+=1
    print('P4_image_selector_joint_counts',dict(joint),flush=True)
    assert joint=={('1110',False):676,('1000',True):28}
    print('P4_original_A_H13_exactly_decodes_LL_selector_PASS',flush=True)
    return leaves

def carrier():
    starts={q.pack(bits(p))|(u<<13) for p in PINS for u in range(128)}
    ends=a.checked_flow(starts,g.H);ent={x for x in ends if x&g.MASK9 in g.SS_TYPES}
    pred={x:None for x in ent};todo=deque(sorted(ent));seen=set();bad=None;terms=Counter()
    while todo:
        x=todo.popleft();seen.add(x)
        for z in sorted(a.checked_flow({x},g.SS)):
            if z&g.MASK9 in g.SS_TYPES:
                if z not in pred:pred[z]=x;todo.append(z)
            else:
                typ=a.classify(z);terms[typ]+=1
                if typ in ('bad_B','white_A_high111'):bad=(x,z);break
        if bad:break
    print('two_pin_sources',len(starts),'Hends',len(ends),'SSent',len(ent),'SSprocessed',len(seen),
          'edge_terminal_types',dict(terms),'P3_guard',bad is None,flush=True)
    assert bad is not None,'Unexpected guard; review complete closure separately'
    x,z=bad;mac=[x]
    while pred[mac[-1]] is not None:mac.append(pred[mac[-1]])
    mac.reverse();mac.append(z)
    _,hp=g.flow(starts,g.H,True);path=[mac[0]]
    for row in reversed(hp):path.append(row[path[-1]])
    path.reverse()
    for x,y in zip(mac,mac[1:]):path+=g.path_to(x,y,g.SS)[1:]
    assert all(y in q.scalar_successors(x,t) for t,(x,y) in enumerate(zip(path,path[1:])))
    assert len(mac)-1==3 and a.classify(z)=='bad_B'
    print('retained_counter',a.classify(z),'SS_count',len(mac)-1,'Hsource',a.fmt(path[0]),
          'endpoints',[a.fmt(x) for x in mac],'complete_scalar_path_PASS',flush=True)
    # This has an H13 from the image but is not a demonstrated lift
    # from the ORIGINAL A row. No actual counter is claimed.

if __name__=='__main__':cover();carrier()
