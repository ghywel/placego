"""GC1077: actual high LL cannot prepare another high fifth track.
Missing inference: GC1076 leaves b=1,Q=0,R=1 as a relaxed next-HH
choice. Derive its actual origin exclusion, rather than scan further.
Record searched: high.*high|b=1.*Q=0|Q=0.*R=1|111001111 with
ancestr|consecut|transport|gate -> 21 hits in 8 files; narrower high LL
with001.*010|consecutive.*high|adjacent.*high|never.*high|Q=1 -> 18
hits in 11 files. GC1076's sampled lack of H was not a proof.
P1 BEFORE controls: source 111001111 has time 1 sites 6..9=1000.
Write u,v,w at time 1 sites 10..12. Current high LL requires time 5
site 8=0; this forces u=0,v OR w=1. Under that condition time 5
site 9 b=NOT v. If b=1 then u=v=0,w=1, which forces time 3
sites 6..12=1110110, time 4 sites 6..11=000010, time 6 sites 6..11
111100, and time 7 sites 6..10=00001. Thus Q=1, contradicting
GC1076's next-high gate Q=0. This branch returns 010 and next D.
If b=0, GC1076 returns 001 and cannot make another high. Hence
all actual high LL return 001 or 010; no adjacent high fifth tracks
in a continuing mature S/L0 run, valid at every run length.
Counterfactual: the relaxed Q=0,R=1 branch is actual from this source.
Unexpected check: a free time 4 band 00001110 satisfies the relaxed
next-high return 111, but its site 11=1 violates the actual forced0.
Controls: 16 local time 1 gates, 8 local shield continuations, 4 closing
assignments, 48 actual origin controls on the two b=1 cylinders,
and the retained 001-to-X exit witness; literal against packed.
OUTCOME: 16 local origin gates, 8 shield continuations, 4 closing
identities and 48 actual controls PASS, in independent literal and
packed engines. The relaxed next-high witness and retained X exit
both pass. No failed prediction in this block; no cutoff bound used.
No solver, membership query, longer language scan or record run.
"""
from itertools import product
from rule30_sl_no_refork import bits, run

FIFTH=bits('0101101010')


def update(row):
    return tuple(row[k-1]^(row[k]|row[k+1]) for k in range(1,len(row)-1))


def band(row,start,end):
    rows={start:row}
    for t in range(start,end):
        rows[t+1]=update((FIFTH[t],)+rows[t])
    return rows


def main():
    gates=shields=closing=origins=0
    for u,v,w in product((0,1),repeat=3):
      for far in (0,1):
        rows=band(bits('1000')+(u,v,w)+(far,)*20,1,7)
        a,b=rows[5][2:4]
        assert (a==0)==(u==0 and bool(v|w))
        if a==0: assert b==1-v
        if a==0 and b==1:
            assert (u,v,w)==(0,0,1)
            assert rows[3][:7]==bits('1110110')
            assert rows[4][:6]==bits('000010')
            assert rows[6][:6]==bits('111100')
            assert rows[7][:5]==bits('00001')
        gates+=1
    for E,F,G in product((0,1),repeat=3):
        rows=band(bits('000010')+(E,F,G)+(0,)*12,4,7)
        assert rows[5][:5]==bits('10011')
        assert rows[5][5:7]==(1-E,E|F)
        assert rows[6][:6]==bits('111100')
        assert rows[7][:5]==bits('00001')
        shields+=1
    for R,S in product((0,1),repeat=2):
        rows=band(bits('00001')+(R,S),7,10)
        assert rows[10][1:4]==bits('010')
        closing+=1
    for prefix,extra in (('111001111101',4),('1110011111100',3)):
      for tail in product((0,1),repeat=extra):
       for far in (0,1):
        rows=run(bits(prefix)+tail+(far,)*22,20)
        assert tuple(r[4] for r in rows[:10])==FIFTH
        assert rows[10][:9]==bits('111001010')
        assert rows[5][7:10]==bits('011')
        assert rows[7][9]==1
        assert tuple(r[4] for r in rows[10:20])==bits('0101100000')
        assert rows[20][:6]==bits('111001')
        origins+=1
    exit_rows=run(bits('11100111101101')+(0,)*22,20)
    assert exit_rows[10][:9]==bits('111001001')
    assert tuple(r[4] for r in exit_rows[10:20])==bits('0101100101')
    relaxed=band(bits('00001110')+(0,)*16,4,10)
    assert relaxed[10][1:4]==bits('111')
    assert (gates,shields,closing,origins)==(16,8,4,48)
    print({'local_origin_gates':gates,'local_shields':shields,
           'closing_identities':closing,'actual_b1_origins':origins,
           'relaxed_next_high_guard':'PASS','retained_X_exit':'PASS',
           'literal_packed':'PASS'})


if __name__=='__main__': main()
