"""GC1127: a same-history entrance/exit gate for GC1126's omitted N.

Missing inference: can the admitted 58-tick H-low detour N reset
itself immediately, or does it consume a hidden A entrance bit?
Local L632 reports its 30-bit visible word present in both phases;
visible absence of N is unavailable, so keep its original A ancestry.
Record searched: H.low|low.detour|SLLLLSS with successor|charge|
potential|splice ->10 hits in 6 files; GC1126 and L632 read.
P1 BEFORE run: all productive N sources have AP13 suffix 1101,
while all N targets have suffix 1100. This gives no N-to-N pair
without fitting a new potential or importing a width refinement.
P2 BEFORE run: even if the simple 13-bit gate fails, the complete
original-origin/end relation has no matching N-to-N pair.
Counterfactual: a 20-cell A label alone pays for repeated N resets.
Retain a scalar-checked pair if this prediction fails; no new
width sweep, CUT, exact membership or periodic-N solver run.
Controls: independently scalar replay both N macros at their shared
full 20 endpoint if a pair exists; reproduce GC1126's 1,530 pairs.
Unexpected check: targets of a detour may be productive origins
without the particular displayed endpoint being one. Check every
complete interface, not only GC1126's selected witness.
P1/P2 REFUTED: sources include suffix 1101 and 1111, targets all
three AP13 types. Six complete interfaces give 9,180 NN pairs.
Unexpected: the old named M3 packet is itself a productive N
self-loop, not just an interface to a different A packet.
P3 BEFORE loop composition: N and the already known F=M3 loop
share that full 20 endpoint. NF and FN are distinct equal-duration
102-tick closed walks, each independently scalar replayed.
P4 BEFORE marker controls: every finite/infinite word over N,F
avoids all eleven certified cuts of CL303. Its FIRST-L marker
spacings are 5,19,22, with no two 19 spacings in succession. Eight
cuts contain spacing 16; f61/f114/f117 contain consecutive 19.
If a copied cut contradicts this necessary-marker argument, retain
the failure and do not request new membership work for that word.
Independent controls: physical h versus gap spelling on 511 cones;
every actual full 20 walk transition versus scalar Rule30.
Known-wrong control: adding M2 to this alphabet preserves avoidance.
Must fail on the known M2-chain cut; no actual lift claimed.
Record searched: f61|61.bit with macro|22 -> 2 hits in 2 files;
GC1121/1124 marker sources and CL303's exact 11-cut table read.
No new actual language or certified-cut extraction is performed.
OUTCOME: P1/P2 REFUTED; P3/P4 HELD. The complete relation has
30 productive origins, 51 targets, 6 shared interfaces and 9,180 NN
pairs. N and F both close at 11101000111011100000. NF and FN last
102 physical ticks, differ at tick 32, and every concatenation
avoids the 11 listed cuts by the marker argument, not by a finite
scan. All 511 cone controls and the known-wrong M2 extension check
pass. This defeats a finite charge for N in this 20-cell machine
and gives a concrete next cut target; actual lifting stays open.
No wider-strip/product/SAT/membership computation follows.
P5 BEFORE CL305 follow-up controls: although arbitrary N/F words
can contain a long F run, words over NF and FN contain at most
two consecutive F blocks. They therefore avoid all 22 reported
length-300 pure-M3 cuts: each has at least 12 successive 22 marker
spacings, whereas these walks have at most two. No membership or
certificate claim is made by this literal-spelling control.
P5 HELD: 255 complete walk cones avoid all 22 reported words;
the pure-F positive control detects those same words.
"""
import ast
from pathlib import Path
from itertools import product
import rule30_111_low_white_return as n
import rule30_black_A_111_diversion as diversion

q=n.q


def cuts():
    # Read the public cut constants without running the ten-minute product.
    tree=ast.parse(Path(__file__).with_name('rule30_cloud_cut_product28.py').read_text())
    out=None
    for node in tree.body:
        if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='cuts' for t in node.targets):
            out=ast.literal_eval(node.value);break
    assert out is not None
    out['f114']=('00001'*2+'001'*3)*6
    out['f117']=('001'*3+'00001'*2)*6+'001'
    assert all(len(v)==int(k[1:]) for k,v in out.items())
    return out


def marker_gaps(word):
    at=[i for i in range(len(word)-10) if word[i:i+11]=='10000100001']
    return at,[b-a for a,b in zip(at,at[1:])]


def cut_certificate():
    cs=cuts();kinds={}
    for name,word in cs.items():
        at,gaps=marker_gaps(word)
        assert 16 in gaps or any(gaps[i:i+2]==[19,19] for i in range(len(gaps)-1)),(name,gaps)
        kinds[name]='16' if 16 in gaps else '19,19'
    print('cut_marker_obstructions',kinds,flush=True)
    g={'N':'100'+'10000'*4+'100'*2,'F':'100'+'10000'*2+'100'*3}
    h={'N':'110100'+'1101000100'*4+'110100'*2,
       'F':'110100'+'1101000100'*2+'110100'*3}
    count=0
    for size in range(9):
        for letters in product('NF',repeat=size):
            word=''.join(g[x] for x in letters)+'1'
            assert word==''.join(h[x] for x in letters)[::2]+'1'
            assert not any(c in word for c in cs.values()),letters
            at,gaps=marker_gaps(word)
            assert all(x in (5,19,22) for x in gaps)
            assert all(gaps[i:i+2]!=[19,19] for i in range(len(gaps)-1))
            count+=1
    m2='100'+'10000'*2+'100'*2
    assert cs['f114'] in m2*8+'1'
    assert cs['f117'] in m2*8+'1'
    print('complete_NF_cones',count,'all_eleven_avoided_PASS',
          'wrong_M2_extension_rejected_PASS',flush=True)


def pure_f_controls():
    f='100'+'10000'*2+'100'*3
    n='100'+'10000'*4+'100'*2
    patterns={(f*15)[i:i+300] for i in range(22)}
    assert len(patterns)==22
    for word in patterns:
        _,gaps=marker_gaps(word)
        assert len(gaps)>=12 and all(g==22 for g in gaps)
    count=0
    for size in range(8):
        for blocks in product(('NF','FN'),repeat=size):
            letters=''.join(blocks)
            word=''.join(n if a=='N' else f for a in letters)+'1'
            assert 'FFF' not in letters
            _,gaps=marker_gaps(word)
            assert all(gaps[i:i+3]!=[22,22,22] for i in range(len(gaps)-2))
            assert not any(c in word for c in patterns)
            count+=1
    assert any(c in f*14+'1' for c in patterns)
    print('NF_FN_complete_cones',count,'all22_pure_F_300_words_avoided_PASS',
          'pure_F_positive_control_PASS',flush=True)


def main():
    starts,_,_,_,_,_,ends,_,_=n.relation()
    edges={(starts[i],z) for z,o in ends.items()
           for i in range(len(starts)) if (o>>i)&1}
    assert len(edges)==1530
    sources={a for a,z in edges};targets={z for a,z in edges}
    prefix=lambda x:''.join(map(str,q.unpack(x)[:13]))
    print(dict(productive_origins=len(sources),target_packets=len(targets),
               source_types=sorted({prefix(x) for x in sources}),
               target_types=sorted({prefix(x) for x in targets}),
               productive_interfaces=len(sources&targets)),flush=True)
    pairs=[(a,b,c) for a,b in sorted(edges) for y,c in sorted(edges) if b==y]
    print('NN_pairs',len(pairs),flush=True)
    if pairs:
        a,b,c=pairs[0]
        p,w=n.witness(a,b,2);r,v=n.witness(b,c,2)
        assert p[-1]==r[0] and len(p)+len(r)-2==116
        print('NN_witness',tuple(''.join(map(str,q.unpack(x))) for x in (a,b,c)),
              'scalar_replay_PASS',flush=True)
    target=q.pack(n.bits('11101000111011100000'))
    assert (target,target) in edges
    np,nw=n.witness(target,target,2)
    # The first composition call stopped on an import/local-variable name
    # collision before any cut control ran; use an unambiguous module name.
    fp=diversion.full_path(target,3)
    fw=''.join(str(x&1) for x in fp[:-1])
    assert fw=='110100'+'1101000100'*2+'110100'*3
    assert np[0]==np[-1]==fp[0]==fp[-1]==target
    assert len(np)+len(fp)-2==102 and nw+fw!=fw+nw
    first=next(i for i,(a,b) in enumerate(zip(nw+fw,fw+nw)) if a!=b)
    print('NF_FN_closed_walk_ticks',102,'first_visible_disagreement_physical_tick',first,
          'two_independent_scalar_loops_PASS',flush=True)
    cut_certificate()
    pure_f_controls()


if __name__=='__main__':main()
