"""GC1121: a common prefix transfers a bare-bridge cut to every E_m.

Missing inference (CL297/MW): which concrete tested word can exclude
all optional B waits, and do absent 117-sample FE/EF words alone kill
the bare mixed recurrence? No solver or actual-language query here.
Record searched: word-boundary E_m/bare/M3 with prefix, and117 with
avoid/three/222 -> no prior hit; GC1106/1113/1114 and CL297 reused.
P1 BEFORE execution: E0 is the first76 visible samples of EVERY
E_m=(1,2^(m+2),3), m>=0. Hand proof uses M3=M2 followed by S;
every following macro starts S. Thus an absent E0 factor kills all
these named bridges, even without the existing m<=2 charge.
REFUTED-BY: a prefix mismatch; a counter in the symbolic decomposition.
P2 BEFORE execution: both117-sample FE/EF words of CL297 contain
four FIRST-L markers with three consecutive19 gaps. Bare FE0/EF0
concatenations have at most two consecutive M2 macros, so neither
word occurs in that explicit relaxation at ANY concatenation length.
Their four234-sample concatenations are absent there too, since each
contains one of the117 words. This is not actual L membership.
REFUTED-BY: a complete finite matching path or failed marker recognition.
Counterfactual: the same bare model avoids the76-sample E0. Must fail,
since each bare generator includes E0. Also include each target itself
as a host, so the matching instrument must accept the known factor.
Independent controls: literal physical h versus gap spelling; complete
host-state matching versus the FIRST-L marker argument.
Unexpected check: M3's finite word is a prefix of M2 followed by M1.
The macro code is NOT prefix-free; a finite last macro does not fix its
following pair spacing. Preserve that distinction in MW implications.
No depth sweep, CUT, relaxed-record computation or right-half lift.
OUTCOME: P1/P2 HELD. Prefix controls at m=0,1,2,19 and independent
physical spellings pass. Complete matching dies at sample101 for FE
and at79 for EF (zero-based first unmatchable target index); the four
234-word products inherit those failures. Self-factor and bare E0
controls are accepted. All four cyclic seam controls pass. The
all-m prefix and all-length absence follow from the hand arguments,
not extrapolation from these controls. No actual membership tested.
"""

# ADDENDUM BEFORE the L630 receipt control: E0 is reported absent via
# f69 below. Predict length69 and its unique occurrence at offset2
# inside E0; the all-m prefix identity then transfers that exact cut
# to every optional-wait bridge. Counterfactual: E0 is merely a
# terminal macro coincidence not shared by E1. Must fail by P1.
# Independently verify literal physical h evens against the exact bits.
# OUTCOME: HELD. f69 has length69, uniquely at E0 offset2; all four
# prefix controls retain it at2 and physical samples4..140 (even).
# No absence replay or new membership query; provenance is Local L630
# at e68b8356, reporting cake_lpr verification of the69-bit SLC cut.

from pathlib import Path
import re


def letters(ks):
    return ''.join('SLL'+'S'*k for k in ks)


def visible(ks):
    return ''.join({'S': '100', 'L': '10000'}[a] for a in letters(ks))


def physical(ks):
    return ''.join({'S': '110100', 'L': '1101000100'}[a]
                   for a in letters(ks))


def read_words():
    s=Path(__file__).with_name('rule30_mixed_generator_words.txt').read_text()
    out={}
    for m in re.finditer(r'^(\w+) \S+ \d+ (\d+)\n((?:[01]+\n?)+)', s, re.M):
        w=m[3].replace('\n', '')
        assert len(w)==int(m[2])
        out[m[1]]=w
    return out


def factor_receipt(hosts, target):
    """All host starting states and every successor at a block seam.

    Matching the fixed target has a progress index j. Exhausting this
    exact finite product covers factors of arbitrary concatenations;
    no cutoff on the length of a host walk is involved.
    """
    states={(b,i) for b,w in enumerate(hosts) for i,c in enumerate(w)
            if c==target[0]}
    for j in range(1,len(target)):
        nxt=set()
        for b,i in states:
            options=([(b,i+1)] if i+1<len(hosts[b])
                     else [(v,0) for v in range(len(hosts))])
            nxt.update((v,k) for v,k in options if hosts[v][k]==target[j])
        states=nxt
        if not states:
            return False,j
    return bool(states),len(target)


def first_l_positions(ks):
    pos=[]
    u=0
    for k in ks:
        pos.append(u+3)
        u+=13+3*k
    return pos


def main():
    ew=lambda m: (1,)+(2,)*(m+2)+(3,)
    e0=visible(ew(0))
    assert len(e0)==76
    # Controls of the all-m symbolic proof, not an extrapolation in m.
    for m in (0,1,2,19):
        assert visible(ew(m))[:76]==e0
        assert physical(ew(m))[:152]==physical(ew(0))
        assert physical(ew(m))[::2]==visible(ew(m))
    assert letters((3,))==letters((2,))+'S'
    assert visible((2,1)).startswith(visible((3,)))

    ks_fe=(3,1,2,2,2,3)
    ks_ef=(1,2,2,2,3,3)
    stored=read_words()
    assert stored['E']==e0
    f69='010000100001001001000010000100100100100001000010010010010000100001001'
    assert len(f69)==69
    assert [i for i in range(len(e0)-68) if e0[i:i+69]==f69]==[2]
    for m in (0,1,2,19):
        assert visible(ew(m))[2:71]==f69
        assert physical(ew(m))[4:142:2]==f69
    for name,ks,start in (('FE',ks_fe,41),('EF',ks_ef,19)):
        w=visible(ks)
        assert w==stored[name]==physical(ks)[::2]
        assert len(w)==117
        for p in (start,start+19,start+38,start+57):
            assert p in first_l_positions(ks)
            assert w[p:p+11]=='10000100001'

    bare_ks=((3,)+ew(0), ew(0)+(3,))
    hosts=[visible(ks) for ks in bare_ks]
    for ks,w in zip(bare_ks,hosts):
        assert len(w)==98 and w==physical(ks)[::2]
        assert ks[-1]==3 and ks[0] in (1,3)
        assert '222' not in ''.join(map(str,ks))
        pos=first_l_positions(ks)
        # Include a complete terminal marker by appending next macro.
        extended=visible(ks+(1,))
        got=[i for i in range(len(w))
             if extended[i:i+11]=='10000100001']
        assert got==pos

    receipts={}
    for name in ('FE','EF','FEFE','EFEF','FEEF','EFFE'):
        ok,matched=factor_receipt(hosts,stored[name])
        assert not ok,name
        assert factor_receipt([stored[name]],stored[name])[0]
        receipts[name]=matched
    assert factor_receipt(hosts,e0)[0]
    # Independently spelled cycles validate arbitrary phase starts/seams.
    for a in bare_ks:
        for b in bare_ks:
            cyc=physical(a+b)[::2]
            extended=cyc*3
            assert all(stored[n] not in extended
                       for n in ('FE','EF','FEFE','EFEF','FEEF','EFFE'))
            assert e0 in extended
    print(dict(P1='HELD',P2='HELD',bare_prefix_samples=76,
               all_length_matching_receipts=receipts,
               marker_gap_obstruction='three19 gaps versus at most two',
               prefix_free_counterfactual='REFUTED',
               actual_membership_tested=False))


if __name__=='__main__':
    main()
