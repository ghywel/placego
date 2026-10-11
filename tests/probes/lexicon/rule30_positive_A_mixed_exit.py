"""GC1140: positive white-A entrances, mixed admission or mature X exit.
Missing inference: the12 positive GC1137 cylinders have high15=1,
but GC1082's high14=1 discharge to low001000 alone does not imply
mixed admission. Retain the original A25 cylinder and actual high14.
Record searched: white.A|GC1137|GC1139 AND positive|X.exit|high14
->25 hits14files; GC1082,1087,1136..1139 read. No positive-branch
mixed admission certificate found.
P1 BEFORE run: each positive A25 cylinder is covered by leaves
forcing either X at26 (low sites10,11=11) or C/J at36. A source
prefix extends only when its fresh-right certificate is undecided;
cap8192 nodes gives UNKNOWN, not absence. A known unguarded101
at36 outside X is a retained counter, not a fresh low assignment.
P2 BEFORE run: every X leaf has high14,15=01; every admission
leaf has high14,15=11 and low13=0 at26. If the latter fails,
retain the actual low guard and endpoint rather than assume it.
Counterfactual: the12 inherited high15 bits only stop the current
ordinary run; their low13 tails could fail the absorbing guard.
Controls: literal/packed source60 trajectories, four far patterns,
every certified row's overlap, complete dyadic cover per A25 root.
Unexpected: retain an actual X leaf and do not assert it absorbed
or excluded outside the continuing mature S/L0 regime. No solver,
CUT, membership, record, strip-widening or ancestry-age scan.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from itertools import product
from rule30_sl_no_refork import bits,run
from rule30_white_A_high_LL_guard import selector
from rule30_001000_mixed_admission import certificate,admitted
from rule30_low_core_closure import CORE

J=(bits('111001101100'),bits('11100110111110'))


def guarded_B(row):
    return (len(row)>=12 and row[:10]==bits('1110100110')
            and (row[10]==1 or row[11]==0))


def mixed_long(row):
    return row[:6]==bits('111001') and admitted(row)


def delayed_cover(roots):
    # P4 BEFORE this adaptive proof attempt: actual high11 lineages
    # admit by52 (C/J at36, guarded B at46, or C/J at52); high01
    # exits X at26. P3's same-source guarded B is new evidence for
    # this particular H/S discharge, not an ancestry-free low rule.
    # Retain any fully known noncore L0 endpoint as COUNTER;
    # cap8192 UNKNOWN. A complete cover is an all-tail certificate.
    cover={p:[] for p in roots};nodes=0;bad=None;unfinished=False
    for root in roots:
        stack=[root]
        while stack and nodes<8192:
            src=stack.pop();nodes+=1;r=certificate(src,52)
            typ=('X26' if len(r[26])>=11 and r[26][9:11]==(1,1)
                 else 'core36' if mixed_long(r[36])
                 else 'B46' if guarded_B(r[46])
                 else 'core52' if mixed_long(r[52]) else None)
            if typ:
                cover[root].append((src,typ));continue
            q=r[52]
            nonJ=all(q[:min(len(q),len(j))]!=j[:min(len(q),len(j))] for j in J)
            if (len(q)>=14 and q[:6]==bits('111001') and
                    q[6:9] not in CORE and nonJ and
                    len(r[26])>=11 and r[26][9:11]!=(1,1)):
                bad=(src,r);break
            stack.extend([src+(1,),src+(0,)])
        unfinished=bool(stack)
        if bad or unfinished:break
    print('P4_delayed_status','COUNTER' if bad else ('UNKNOWN' if unfinished else 'COVERED'),
          'nodes',nodes,flush=True)
    if bad:
        src,r=bad
        print('delayed_counter_source',''.join(map(str,src)),
              'B46',''.join(map(str,r[46])),'L52',''.join(map(str,r[52])),flush=True)
        return
    if unfinished:return
    counts=Counter();lengths=Counter();guards=Counter();controls=0;X_witness=None
    for root,leaves in cover.items():
        words=sorted(''.join(map(str,p)) for p,_ in leaves)
        assert all(not b.startswith(a) for a,b in zip(words,words[1:]))
        assert sum(Fraction(1,1<<(len(p)-25)) for p,_ in leaves)==1
        for src,typ in leaves:
            r=certificate(src,52);counts[typ]+=1;lengths[len(src)]+=1
            guards[(typ,r[16][13:15] if len(r[16])>=15 else 'unknown')]+=1
            if typ=='X26' and X_witness is None:X_witness=src
            for pattern in ((0,),(1,),(0,1),(1,0)):
                far=tuple(pattern[j%len(pattern)] for j in range(80-len(src)))
                full=run(src+far,52)
                assert all(full[t][:min(len(y),len(full[t]))]==y[:min(len(y),len(full[t]))]
                           for t,y in enumerate(r))
                if typ=='X26':assert full[16][13:15]==(0,1) and full[26][9:11]==(1,1)
                else:
                    assert full[16][13:15]==(1,1)
                    if typ=='core36':assert mixed_long(full[36])
                    elif typ=='B46':assert guarded_B(full[46]) and mixed_long(full[52])
                    else:assert mixed_long(full[52])
                controls+=1
    payload='\n'.join(sorted(''.join(map(str,p))+' '+typ for v in cover.values() for p,typ in v))+'\n'
    print('delayed_all_tail_cover_PASS','leaves',sum(counts.values()),'counts',dict(counts),
          'lengths',dict(lengths),'high_pairs',dict(guards),flush=True)
    print('delayed_cover_sha256',sha256(payload.encode()).hexdigest(),
          'independent_source80_controls',controls,'PASS',flush=True)
    assert X_witness is not None
    full=run(X_witness+(0,)*(80-len(X_witness)),52)
    print('unexpected_actual_X_source',''.join(map(str,X_witness)),
          'high_pair',full[16][13:15],
          'low26',''.join(map(str,full[26][:14])),flush=True)


def main():
    roots=[bits('1110100011011')+far for far in product((0,1),repeat=12)
           if selector(far) and run(bits('1110100011011')+far,6)[6][17:19]==(0,1)]
    assert len(roots)==12
    cover={p:[] for p in roots};nodes=0;counter=None;incomplete=False
    for root in roots:
        stack=[root]
        while stack and nodes<8192:
            src=stack.pop();nodes+=1;rows=certificate(src,36)
            low=rows[26];end=rows[36]
            if len(low)>=11 and low[9:11]==(1,1):
                cover[root].append((src,'X'));continue
            if admitted(end):
                cover[root].append((src,'core'));continue
            nonX=len(low)>=11 and low[9:11]!=(1,1)
            nonJ=all(end[:min(len(end),len(j))]!=j[:min(len(end),len(j))] for j in J)
            if nonX and len(end)>=9 and end[6:9]==bits('101') and nonJ:
                counter=(src,rows);break
            stack.extend([src+(1,),src+(0,)])
        incomplete=bool(stack)
        if counter or incomplete:break
    print('P1_status','COUNTER' if counter else ('UNKNOWN' if incomplete else 'COVERED'),
          'nodes',nodes,'covered_roots',sum(bool(v) for v in cover.values()),flush=True)
    if counter:
        src,rows=counter
        print('actual_counter_source',''.join(map(str,src)),'length',len(src),
              'high16',''.join(map(str,rows[16])),
              'low26',''.join(map(str,rows[26])),
              'end36',''.join(map(str,rows[36])),flush=True)
        for pattern in ((0,),(1,),(0,1),(1,0)):
            far=tuple(pattern[j%len(pattern)] for j in range(60-len(src)))
            r=run(src+far,36)
            assert r[26][9:11]!=(1,1) and not admitted(r[36])
            assert all(r[t][:min(len(y),len(r[t]))]==y[:min(len(y),len(r[t]))]
                       for t,y in enumerate(rows))
        print('counter_four_independent_source60_controls_PASS',flush=True)
        # P3 BEFORE this adaptive continuation: the actual bad
        # lineage's H at36 returns guarded B at46 and hence admits
        # by52; if it returns white SS/A instead, retain that reset.
        # Four complete80 controls are diagnostic, not an all-tail
        # delayed-admission proof. No fresh endpoint tail assigned.
        following=Counter()
        for pattern in ((0,),(1,),(0,1),(1,0)):
            far=tuple(pattern[j%len(pattern)] for j in range(80-len(src)))
            r=run(src+far,52)
            guardedB=(r[46][:10]==bits('1110100110') and
                      (r[46][10]==1 or r[46][11]==0))
            following[(r[46][:13],guardedB,admitted(r[52]))]+=1
        print('P3_actual_H46_S52_controls',dict(following),flush=True)
        delayed_cover(roots)
        return
    if incomplete:return
    types=Counter();lengths=Counter();guards=Counter();ends=Counter();controls=0
    witness=None
    for root,leaves in cover.items():
        words=sorted(''.join(map(str,p)) for p,_ in leaves)
        assert all(not b.startswith(a) for a,b in zip(words,words[1:]))
        assert sum(Fraction(1,1<<(len(p)-25)) for p,_ in leaves)==1
        for src,typ in leaves:
            rows=certificate(src,36);high=rows[16];low=rows[26];end=rows[36]
            pair=high[13:15] if len(high)>=15 else 'unknown'
            b=low[12] if len(low)>=13 else 'unknown'
            guards[(typ,pair,b)]+=1;types[typ]+=1;lengths[len(src)]+=1
            if typ=='X':
                assert low[9:11]==(1,1)
                if witness is None:witness=src
            else:
                assert admitted(end)
                ends[end[6:9] if end[6:9] in CORE else 'J']+=1
            for pattern in ((0,),(1,),(0,1),(1,0)):
                far=tuple(pattern[j%len(pattern)] for j in range(60-len(src)))
                r=run(src+far,36)
                assert all(r[t][:min(len(y),len(r[t]))]==y[:min(len(y),len(r[t]))]
                           for t,y in enumerate(rows))
                assert r[16][14]==1
                if typ=='X':assert r[16][13:15]==(0,1) and r[26][9:11]==(1,1)
                else:assert r[16][13:15]==(1,1) and admitted(r[36])
                controls+=1
    payload='\n'.join(sorted(''.join(map(str,p))+' '+typ for leaves in cover.values() for p,typ in leaves))+'\n'
    print('cover_PASS','leaves',sum(types.values()),'types',dict(types),
          'lengths',dict(lengths),'guards',dict(guards),'ends',dict(ends),flush=True)
    print('cover_sha256',sha256(payload.encode()).hexdigest(),
          'independent_source60_controls',controls,'PASS',flush=True)
    assert witness is not None
    r=run(witness+(0,)*(60-len(witness)),36)
    print('unexpected_actual_X_source',''.join(map(str,witness)),
          'high_pair',r[16][13:15],'low26',''.join(map(str,r[26][:14])),
          'core36',admitted(r[36]),flush=True)


if __name__=='__main__':main()

# OUTCOME: P1/P2's admission-by36 and low13-white claims REFUTED
# by the actual33-cell source, with four independent60-cell controls.
# P3's four continuations admit via guarded B46 and C/J52, motivating
# P4. P4 HELD:3012 nodes,1512 prefix-free leaves of lengths25..38,
# exact dyadic coverage of all12 A25 cylinders. Leaves:12 X26,
# 1185 C/J36,109 guarded B46,206 C/J52. All high pairs are01 on X,
# 11 on admission;6048 independent80-cell controls agree. The
# first P4 validation failed by checking C/J at52 on already-core36
# branches, though52 is not generally their renewal time; repaired
# to check each leaf's certified entry time. Earlier invocation was
# not a verification pass. An actual X source is retained; its
# exclusion is only from a continuing mature S/L0 history, not from
# arbitrary clamped trajectories. With GC1139 negative16, all white-A
# high-LL entrances enter the mixed absorbing union by52 or exit X
# at26. No general untyped admission, R_real(d) or prize claim.
