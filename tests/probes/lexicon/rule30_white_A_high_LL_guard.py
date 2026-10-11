"""GC1136: exact correlated white-A to high-LL entrance selector.
Missing inference: distinguish the SS-prepared budget reset from
GC1104's absorbing white-A terminals, without a marker-only guard.
Record searched: white.A|white-SS AND case.B|00110000|high.LL|exact.gate
->10 hits6 files; GC1080,1090,1104,1131,1135 read.
P1 BEFORE run: a white-A13 source can prepare high LL only via
GC1080 case B; white13 sources admit C, and A/C cylinders are barred
by the six-tick short past. If false retain the other exact gate.
P2 BEFORE run: the high-LL decision depends on source sites14..23
only. Sites24/25 are a declared unexpected check; a varying result
means their joint information belongs in the hidden selector.
Counterfactual: white SS or the eleventh/thirteenth marker decides
high LL. GC1135 remains a required positive; GC1104's low shield
remains absorbing. The complete source25 cone fixes low19 at S6;
GC1080's proved all-tail gate supplies D-high-H-L0 equivalence.
Controls: packed extraction agrees with independent literal Rule30
on every one of8192 source cones; existing decoder is composed,
not advertised as new. A prime-cube cover is checked independently
against every finite assignment and each cube's free bits.
No solver, CUT, membership, record, strip or ancestry-age scan.
"""
from itertools import product
from rule30_sl_no_refork import bits,run
from rule30_001_high_return_gate import gate,H,D
from rule30_core_short_bridge import S
from rule30_black_A_ancestry_guard import inverse


def classify(tail):
    a,b,c,d,e,f,g,h,i,j=tail
    A=tail[:8]==bits('00100001')
    B=tail[:8]==bits('00110000') and bool(i|j)
    C=tail[:6]==bits('001011') and bool(g|h) and ((g,h)!=(1,1) or (i,j)==(0,0))
    return 'A' if A else 'B' if B else 'C' if C else None


def primes(ones,n):
    layer={(x,(1<<n)-1) for x in ones};out=set()
    while layer:
        merged=set();used=set()
        for x,m in layer:
            for j in range(n):
                b=1<<j;y=x^b
                if m&b and (y,m) in layer:
                    used.add((x,m));used.add((y,m));merged.add((x&~b,m&~b))
        out|=layer-used;layer=merged
    return sorted(out)


def selector(far):
    a,b,c,d,e,f,g,h,i,j,k,l=far
    left=(far[:6]==bits('011011') and (
        (g and h and not(i|j)) or
        (g and not h and bool(i|j)) or
        (not g and h and not(i|j) and bool(k|l))))
    right=(far[:8]==bits('01110000') and (
        bool(i^j) or (i and j and not(k|l))))
    return bool(left or right)


def main():
    accepted={0:set(),1:set()};counts={};controls=0
    for u in (0,1):
        prefix=bits('111010001101'+str(u))
        for far in product((0,1),repeat=12):
            source=prefix+far;rows=run(source,6);low=rows[6]
            assert tuple(y[4] for y in rows[:6])==S
            assert low[:10]==bits('1110010010')
            typ=classify(low[9:19]);assert bool(typ)==bool(gate(low[9:19]))
            if typ:
                x=sum(b<<j for j,b in enumerate(far));accepted[u].add(x)
                counts[(u,typ)]=counts.get((u,typ),0)+1
            controls+=1
    print('gate_counts',counts,'source_cones',controls,
          'P1_only_B',set(counts)<={(1,'B')},flush=True)
    assert not accepted[0], 'white13 transfer must be re-examined'
    ps=primes(accepted[1],12)
    for x in range(4096):
        assert (x in accepted[1])==any((x&m)==v for v,m in ps)
    support=[j+14 for j in range(12) if any((x in accepted[1])!=((x^(1<<j)) in accepted[1]) for x in range(4096))]
    print('support_sites',support,'P2_first23',all(j<=23 for j in support),
          'prime_cubes',len(ps),flush=True)
    for v,m in ps:
        print('cube', ''.join(str((v>>j)&1) if (m>>j)&1 else '-' for j in range(12)),flush=True)
    # P3 BEFORE controls: the nine prime cubes compress to these two
    # structural source families. They cover every accepted assignment.
    # Independently invert all three GC1080 gate families through S,
    # retaining its complete first-cell equations and fifth track.
    # P4 BEFORE controls: this backward reconstruction gives exactly
    # the same28 white-A25 sources, not a projected or padded set.
    inv={bits('111001001')+t for t in product((0,1),repeat=10) if classify(t)}
    sizes=[]
    for t in range(5,-1,-1):
        inv={x for y in inv for x in inverse(y,t%2) if x[4]==S[t]}
        sizes.append(len(inv));assert len(inv)<=20000,'inverse cap UNKNOWN'
    inv={x for x in inv if x[:13] in {bits('1110100011010'),bits('1110100011011')}}
    expected={bits('1110100011011')+tuple((x>>j)&1 for j in range(12)) for x in accepted[1]}
    assert inv==expected
    for far in product((0,1),repeat=12):
        assert selector(far)==(sum(b<<j for j,b in enumerate(far)) in accepted[1])
    print('compressed_two_family_guard4096 inverse_sizes',sizes,
          'inverse_sources25',len(inv),'independent_inverse_PASS',flush=True)
    # Explicit unexpected sensitivity controls: same source through23,
    # high111 in both cases, but sites24 or25 toggle its H return.
    assert not selector(bits('011011010000'))
    assert selector(bits('011011010001')) and selector(bits('011011010010'))
    for far in ('011011010000','011011010001','011011010010'):
        full=run(bits('1110100011011'+far)+(0,)*18,26)
        assert full[16][:9]==bits('111001111')
        assert (full[26][:6]==bits('111001'))==selector(bits(far))
    # Positive counter and an independent complete decoder composition.
    known=bits('1110100011011011011101001')
    assert known[:13]==bits('1110100011011')
    assert sum(b<<j for j,b in enumerate(known[13:])) in accepted[1]
    full=run(known+(0,)*18,26)
    assert tuple(y[4] for y in full[:26])==S+D+H
    assert full[26][:6]==bits('111001')
    print('GC1135_positive_and_composition_PASS complete_cube_cover_PASS',flush=True)

if __name__=='__main__':main()

# OUTCOME: P1 HELD (28 high-LL cones, all case B); P2 REFUTED:
# all12 source variables are essential, including sites24 and25.
# P3/P4 PASS: two-family formula covers all4096 assignments and
# complete inverse gives exactly the28 sources. This finite causal
# proof holds for every exterior and every even origin age, given
# the stated white-A13 premise; it is not a scan extrapolation.
