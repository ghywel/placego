"""GC1191: reuse G13's decoder for primitive checkerboard-gap fingerprints.

PREDICTIONS BEFORE controls, 2026-10-13: the named words10111 and11001
are the reviewed Q/P corner seeds;110001 is a primitive P gap; the two
fixed words1011+00000+1 and1011+00000000+1 reconstruct Q gaps of zeros.
Each accepted word reconstructs a unique gap and reproduces its full
seed by an independent Wolfram-table forward step. These are only five
named inputs, not a deficit/profile census or size sweep.
CF: header+last1 alone is sufficient;1011111 must reject because the
terminal reconstructed pair is00. Unexpected:0100 resets all G13
states, but a synchronizing body is not by itself a valid primitive
birth; acceptance still requires the labelled terminal edge.
Record searched: primitive|fingerprint|birth.gap withregular|automaton|
four.state ->3 unrelated hits1file; seed|gap withtriangular.invert|
four.state.inverse ->G13 andold board references. G13.1/2, GC1184,
GC1187 andGC1189 read. The four-state transition is reused, not new.
ADDENDUM BEFORE controls: include either first child sample beta.
The header is[1,r,1-r,r XOR beta], and the initial pair after it is
(r,r XOR(1-beta)). The additional fixed word1101 has beta0 and is a
primitive P with an empty gap. Also test the stronger reset counter:
body010011 contains0100 and ends1, but its terminal pair00 must reject.
No earlier input or prediction is removed.
OUTCOME: all six named inverse/independent-forward controls PASS.
Header-only and both reset-body negatives rejected as predicted.
No solver, record/profile/survival census, period scan or membership.
"""
TABLE=(0,1,1,1,1,0,0,0)


def decode(word):
    if len(word)<4 or word[0]!='1' or word[-1]!='1':return None
    r=int(word[1])
    if int(word[2]) != 1-r:return None
    beta=r ^ int(word[3])
    a,b=r,r ^ (1-beta)
    gap=[b]
    for bit in word[4:]:
        c=int(bit) ^ (a|b)
        gap.append(c)
        a,b=b,c
    # The last reconstructed bit is the boundary cell at s, not a gap.
    typ = 'Q' if (a,b)==(0,1) else 'P' if (a,b)==(1,0) else None
    if typ is None:return None
    return r,tuple(gap[:-1]),typ,beta


def seed_from_parent(r,gap,typ):
    # Fixed N3/4 depending parity, with enough tail for one update only.
    N=4 if r==0 else 3
    s=N+len(gap)+1
    row=[j%2 for j in range(1,N+1)]+list(gap)
    row += [1]*5 if typ=='Q' else [0]+[1]*5
    image=[TABLE[4*row[j+1]+2*row[j]+(r if j==0 else row[j-1])]
           for j in range(len(row)-1)]
    return ''.join(map(str,[1,r,1-r]+image[N-1:s-1]))


def main():
    inputs=('1101','10111','11001','110001','1011'+'0'*5+'1','1011'+'0'*8+'1')
    for w in inputs:
        d=decode(w);assert d is not None
        r,gap,typ,beta=d
        assert seed_from_parent(r,gap,typ)==w
        print(w,'->',typ,'first sample',beta,'gap',''.join(map(str,gap)))
    assert decode('1011111') is None
    assert decode('1011'+'0100') is None
    assert decode('1011'+'010011') is None # resets, ends1, finalpair00
    print('six named inverse/independent forward controls PASS; three negative controls PASS')

if __name__=='__main__':main()
