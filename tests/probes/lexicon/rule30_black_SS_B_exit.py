"""GC1142: does a last black SS exit satisfy guarded B?
Missing inference: GC1141's676 black-marker SS entrants can exit B;
the older GC1089/1090 proof treats A but leaves B's sparse guard.
Record searched:black.SS|black.marker|GC1089 AND exit|white.A|guard|inherit
->37 hits15files; black.SS|last.black|111011111|111011110 AND
B.*guard|guarded.B|B12|white.*10 ->33 hits12files.
GC1055/56,1087/89/90/91,1098/99,1105,1141 read. Generic white-SS
bad-B counters do not supply a last-black predecessor.
P1 BEFORE run: every mature black SS return with B10=B11=0 has
B12=0. If true, GC1087 absorbs every B exit; arbitrary SS length
is handled at the last black marker, not by a cutoff.
If false retain its actual18-cell source and endpoint, then stop
that unconditional exit guard. Counterfactual: black-marker past
alone might already be insufficient before earlier H111 is retained.
Independent controls: complete six-tick literal/packed causal cones;
a fresh white-SS bad-B negative and a known guarded-B positive.
Unexpected: check whether a white-sixth SS output can itself remain
SS rather than exit A/B; that would invalidate a last-black-only
partition even if P1 held. No Local solver/graph/language/record run.
"""
from itertools import product
from collections import Counter
from rule30_sl_no_refork import bits,run
from rule30_positive_A_mixed_exit import guarded_B,mixed_long
from rule30_black_A_ancestry_guard import inverse
from rule30_001000_mixed_admission import certificate

H=bits('0101101010')


def main():
    counts=Counter();bad=None;whiten_ss=None;bad_sources=set();whiten_sources=set();good_B_sources=set()
    for pre in ('111011101','111011110','111011111'):
        for far in product((0,1),repeat=9):
            src=bits(pre)+far;r=run(src,6);end=r[6]
            assert tuple(x[4] for x in r[:6])==bits('111010')
            if end[:9]==bits('111010011'):
                counts['B']+=1
                if guarded_B(end):good_B_sources.add(src)
                if end[9]==0:
                    counts['B10white']+=1
                    if not guarded_B(end):
                        counts['badB']+=1;bad_sources.add(src)
                        if bad is None:bad=src
            if end[5]==0:
                counts['whiten']+=1
                if end[:9] not in (bits('111010001'),bits('111010011')):
                    counts['whiten_SS']+=1;whiten_sources.add(src)
                    if whiten_ss is None:whiten_ss=src
    print('counts',dict(counts),'P1',bad is None,flush=True)
    for label,src in (('badB',bad),('whiteSS',whiten_ss)):
        if src is not None:
            r=run(src+(0,)*24,12)
            print(label,'source18',''.join(map(str,src)),
                  'end6',''.join(map(str,r[6][:18])),
                  'end12',''.join(map(str,r[12][:12])),flush=True)
    negative=run(bits('11101'+'0000000000010')+(0,)*12,6)[6]
    assert negative[:12]==bits('111010011001') and not guarded_B(negative)
    positive=run(bits('111010011011011')+(0,)*12,6)[6]
    assert positive[6:9] in (bits('010'),bits('011'),bits('100'))
    print('whiteSS_negative_and_guardedB_positive_PASS',flush=True)
    # P6 BEFORE nonvacuity: some guarded-B source18 has actual
    # H111 past. Retain the first fully reconstructed source cone;
    # this is a positive control, not a further absence claim.
    positive_source=None
    for target in sorted(good_B_sources):
        rows={target[5:]}
        for t in range(9,-1,-1):
            rows={x for y in rows for x in inverse(y,H[t])}
            if t==0:rows={x for x in rows if x[:4]==bits('1111')}
            if not rows:break
            if len(rows)>200000:raise RuntimeError('positive-control inverse cap')
        if rows:
            positive_source=bits('11100')+min(rows);break
    assert positive_source is not None
    cert=certificate(positive_source,16)
    assert guarded_B(cert[16])
    for pattern in ((0,),(1,),(0,1),(1,0)):
        far=tuple(pattern[j%len(pattern)] for j in range(70-len(positive_source)))
        full=run(positive_source+far,22)
        assert guarded_B(full[16]) and mixed_long(full[22])
        assert tuple(r[4] for r in full[:16])==H+bits('111010')
        assert all(full[t][:len(y)]==y for t,y in enumerate(cert))
    print('H111_SS_guardedB_nonvacuous_source', ''.join(map(str,positive_source)),
          'end16',''.join(map(str,cert[16])), 'four_full_controls_PASS',flush=True)
    # P2 BEFORE inverse: the exact last-black bad-B counter has
    # no actual H111 predecessor at10. Cap complete layers200000;
    # a cap is UNKNOWN. If a predecessor exists retain its full
    # original prefix and certify H-SS-badB for every exterior.
    # This settles one specific counter lift, not all676 origins.
    # P3 unexpected: the whitening-SS counter is also inaccessible
    # from H111. Keep a lift if this source too has actual H past.
    # P4 BEFORE complete inverse of the offending classes: no
    # one of the17 bad-B parents or480 whitening-SS parents has
    # the two-step fifth past10 (shared by H and mature SS).
    # The full18-cell causal census exhausts each violation.
    # If true this proves a mature image guard for every SS-block
    # length; if false retain the complete earlier parent, without
    # claiming that one failed representative closes the class.
    for label,targets in (('all_badB',bad_sources),('all_whitenSS',whiten_sources)):
        rows={x[5:] for x in targets};sizes=[]
        for wall in (0,1):
            rows={x for y in rows for x in inverse(y,wall)};sizes.append(len(rows))
        print(label,'two_step_10_parents',len(rows),'sizes',sizes,
              'P4_absence',not rows,flush=True)
        if rows:print('first_two_step_parent',''.join(map(str,min(rows))),flush=True)
    # P5 BEFORE full H-past intersection: all violating classes,
    # not only their first representatives, are excluded by H111.
    # Complete-layer cap200000; cap means UNKNOWN. If false,
    # retain an actual H-origin cone and its failing SS endpoint.
    for label,targets in (('badB_rep',{bad}),('whiteSS_rep',{whiten_ss}),
                          ('all_badB',bad_sources),('all_whiteSS',whiten_sources)):
        rows={target[5:] for target in targets};sizes=[]
        shields={0:bits('1111'),1:bits('1000'),4:bits('000'),5:bits('10')}
        for t in range(9,-1,-1):
            # P7 BEFORE structural extraction: all bad-B antecedents
            # surviving the time5/time4 high shields force the
            # fourth time1 band bit black. Actual H111 makes1000.
            # If this specific bit claim fails, retain exact prefix
            # alternatives rather than invent a unary explanation.
            candidates={x for y in rows for x in inverse(y,H[t])}
            if label=='all_badB' and t==1:
                prefixes=sorted({''.join(map(str,x[:4])) for x in candidates})
                print('badB_required_Htime1_prefixes',prefixes,
                      'P7_fourth_black',all(x[3] for x in candidates),flush=True)
            rows={x for x in candidates
                  if t not in shields or x[:len(shields[t])]==shields[t]}
            sizes.append(len(rows))
            if len(rows)>200000:
                print(label,'H_inverse_UNKNOWN_cap',sizes,flush=True);break
        else:
            print(label,'H111_predecessors',len(rows),'sizes',sizes,
                  'absence_prediction',not rows,flush=True)
            if rows:
                src=bits('11100')+min(rows);cert=certificate(src,16)
                assert cert[10][:18] in targets
                if 'badB' in label:assert cert[16][:12]==bits('111010011001')
                else:assert cert[10][5]==1 and cert[16][5]==0
                for pattern in ((0,),(1,),(0,1),(1,0)):
                    far=tuple(pattern[j%len(pattern)] for j in range(70-len(src)))
                    full=run(src+far,22)
                    assert full[10][:18] in targets
                    assert tuple(r[4] for r in full[:10])==H
                    assert all(full[t][:len(y)]==y for t,y in enumerate(cert))
                print(label,'actual_H_source',''.join(map(str,src)),
                      'certificate16',''.join(map(str,cert[16])),
                      'four_independent70cell_controls_PASS',flush=True)



if __name__=='__main__':main()

# OUTCOME: final complete probe PASS. P1 REFUTED:1536 complete
# black-SS18 cones include240 B,228 white10 B,17 badB;768 whiten,
# including480 whiteSS outputs. First badB and whiteningSS sources
# have no H111 past (P2/P3 HELD), but two-step past alone does not
# exclude the complete classes (48/2560 parents; P4 REFUTED).
# Full H111 intersection excludes all17 badB roots (P5 B HELD),
# by complete inverse with reviewed high shields. At H time1 the
# surviving antecedents have0000 or0100; actual high111 gives1000.
# P7 fourth-black explanation REFUTED; first-bit contradiction is
# the actual result. WhiteningSS has80256 H111 antecedents (P5
# whitening REFUTED); a28-cell all-tail counter is retained.
# P6 guardedB exit is nonvacuous, with its28-cell H-source
# certificate and four70-cell controls proving entry by22.
# Only the FIRST SS after H111 is closed for B exits; arbitrary
# black/white SS chains, original676 admission and prize remain OPEN.
# One diagnostic used a mis-concatenated white-SS negative string;
# its first invocation failed. Corrected explicit concatenation and
# all final independent controls pass. Data stay outside git.
