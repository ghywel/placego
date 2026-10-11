"""GC1137: does the white-A high-LL selector carry the sparse stop bit?
Missing inference: GC1136 recognises high-LL entrances, but a source
label does not bound renewals. Test GC1082's fifteenth bit on these
entrances, retaining their case-B low19 on the same history.
Record searched: white.A|white-SS|GC1136 AND sparse|second.high|
site.15|repeat ->29 hits15files;00110000|case.B AND fifteenth|
site.15|sparse|pair.11 ->5 hits5files. GC1080,1082,1135/36 read;
CL324 independently confirms GC1136 and is adopted, no repeated
selector census. No solver, CUT, language, graph or record run.
P1 BEFORE run: every case-B low19 permitted by a white-A origin
has its high successor's site15 black, so GC1082's sparse guard
prevents another high LL without a new short.
Counterfactual: a white-A entrance resets the high budget completely.
A retained high15=0 would refute P1; it does not alone establish
another LL and must not be advertised as a recurrent path.
Test the three case-B low19 prefixes (01/10/11), using the same
fresh-right prefix induction as GC1082. Compose only the pairs
actually produced by GC1136's 28 retained source25 cylinders.
Independent controls: each prefix implication checked for both
fresh right bits; literal/packed full cones and sparse-bit origin
label retained. Positive inherited01 prefix remains a control.
Unexpected: equal low18/19=11 might still carry a complementary
pair shield at the later high, despite losing the old01 premise.
Stop after this sparse-bit question; no age or strip widening.
"""
from itertools import product
from rule30_white_A_high_LL_guard import bits,run,selector,S,D,H
from rule30_core_short_bridge import update


def fixed_prefix(source,steps):
    rows=[source]
    for t in range(steps):
        old=rows[-1];new=update((t%2,)+old)
        if old[-1]:new+=(old[-2]^1,)
        for far in (0,1):assert update((t%2,)+old+(far,))[:len(new)]==new
        rows.append(new)
    return rows


def main():
    for pair in ('01','10','11'):
        low=bits('11100100100110000'+pair)
        rows=fixed_prefix(low,10)
        assert all(rows[t][4]==D[t] for t in range(10))
        assert rows[10][:13]==bits('1110011111000')
        print('pair',pair,'D8',''.join(map(str,rows[8])),
              'D10',''.join(map(str,rows[10])),flush=True)
    sources=[]
    # Reuse the already proved source predicate, not its decoder census.
    for far in product((0,1),repeat=12):
        if selector(far):sources.append(bits('1110100011011')+far)
    pairs={};joint={};bad=None;tested=0
    for source in sources:
        low=run(source,6)[6];pair=low[17:19];pairs[pair]=pairs.get(pair,0)+1
        # A25 plus six new bits is the complete S-D cone of high15.
        for far in product((0,1),repeat=6):
            rows=run(source+far,16)
            assert rows[16][:13]==bits('1110011111000')
            tested+=1
            key=(pair,rows[16][13:15]);joint[key]=joint.get(key,0)+1
            if not rows[16][14] and bad is None:bad=(source+far,rows)
    print('white_A_source_pairs',pairs,'complete_high15_cones',tested,
          'P1_sparse15',bad is None,'same_history_high_pairs',joint,flush=True)
    # P2 BEFORE this scope control: the retained mature SS origin
    # GC1135 V33, with six missing causal bits, permits the same
    # high14=high15=0. A failure leaves the mature-SS implication
    # unresolved, rather than treating a fresh A failure as mature.
    V=bits('000111011001010010000000000000000')
    mature=[]
    for far in product((0,1),repeat=6):
        src=V+far;rows=run(src,24)
        assert rows[2][:31]==bits('1110101101000100001000000000000')
        assert rows[8][:25]==bits('1110100011011011011101001')
        assert tuple(y[4] for y in rows[2:24])==bits('111010')+S+D
        assert rows[24][:13]==bits('1110011111000')
        if rows[24][13:15]==(0,0):mature.append((src,rows))
    print('mature_SS_cones64','high14_15_white',len(mature),
          'P2_mature_failure',bool(mature),flush=True)
    if mature:
        src,rows=mature[0]
        print('mature_source39',''.join(map(str,src)),
              'white_A8',''.join(map(str,rows[8])),
              'low14',''.join(map(str,rows[14])),
              'high24',''.join(map(str,rows[24])),flush=True)
        for tail in product((0,1),repeat=4):
            ext=run(src+tail,24)
            assert all(ext[t][:len(y)]==y for t,y in enumerate(rows))
        print('mature_exterior_controls16_PASS',flush=True)
    # P3 BEFORE a fresh-right proof control: the16 low-B11 source25
    # cylinders retain15 contiguous high cells under S-D prefix
    # induction, ending00. If it loses cells, use the complete
    # source31 cone proof, not a guessed prefix implication.
    retained=0;lengths={}
    for source in sources:
        low=run(source,6)[6]
        if low[17:19]!=(1,1):continue
        cert=fixed_prefix(source,16);last=cert[16]
        lengths[len(last)]=lengths.get(len(last),0)+1
        if len(last)>=15:
            assert last[:15]==bits('111001111100000');retained+=1
    print('P3_prefix_proof_retained',retained,'of16','lengths',lengths,flush=True)
    if bad:
        src,rows=bad
        print('sparse_failure31',''.join(map(str,src)),
              'low6',''.join(map(str,rows[6])),
              'high16',''.join(map(str,rows[16])),flush=True)

if __name__=='__main__':main()

# OUTCOME: P1 REFUTED, P2 HELD. Of the28 reviewed source25
# cylinders,12 give low18/19=01 and high15=1;16 give low18/19=11
# and high14/15=00 on every completion. All1792 complete cones
# agree. The same negative pair holds on all64 causal completions
# of GC1135 V33;16 farther-tail controls pass. No second high LL
# is inferred from this negative pair. P3 REFUTED: a contiguous
# fresh-right certificate retains enough cells on14/16 sources
# but loses the final two on2; the complete source31 cone proof
# remains valid and includes those two. Stop unconditional sparse
# stop transfer and the contiguous-prefix proof shortcut.
