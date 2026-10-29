#!/usr/bin/env python3
"""GC2151 DQ024 fixed20-pair diagnostic. See reports/rule30-edge-density-account.md.
P before run: some00pair loses >1 resource unit. CF: none. Q: noninitial10 decrements exactly1.
Unexpected: report00 resource increases. Controls: all8-bit polynomial valuations, cyclic differences,
physical orientation, published periods and original reset/countdown laws. No asymptotic claim.
Record searched: GC1960/1961/2009, kit932cf8dd RecordCharge/DifferenceOrder/RightPeriods,
portal1b82d8, PR55, Rowland2006 sections1-3. This measures existing known resources.
Fixed j<=40,t<=65536, seed1; no user-supplied expansion or automatic retry.
"""
import json
from collections import Counter

# Rowland2006 author-PDF page4: a(k)=J_k+1, k=0..40. Published data, not our new output.
CAPS = [1,3,4,6,7,9,15,16,24,25,27,29,34,36,37,39,41,43,48,49,51,
        54,55,58,60,63,64,66,69,70,72,74,77,79,80,82,84,86,90,91,93]
EXP = [next(k for k,a in enumerate(CAPS) if j<a) for j in range(41)]
PER = [1 << EXP[2*i] for i in range(21)]
assert max(PER) == 65536

def valuation(word, length):
    """Multiplicity at X=1 by the upper-subset XOR/binomial transform over F2."""
    assert length > 0 and length & (length-1) == 0 and word >> length == 0
    z, shift = word, 1
    while shift < length:
        mask = ((1 << length)-1)//((1 << shift)+1)
        z ^= (z >> shift) & mask
        shift *= 2
    return length-1 if z == 0 else min(length-1, (z & -z).bit_length()-1)

def slow_polynomial_order(word, length):
    if word == 0:
        return length-1
    r = 0
    while word.bit_count() % 2 == 0:
        q, rest = 0, word
        while rest.bit_length() > 1:
            d = rest.bit_length()-2
            q ^= 1 << d
            rest ^= 3 << d
        assert rest == 0
        word = q
        r += 1
    return min(r, length-1)

def cyclic_order(word, length):
    mask = (1 << length)-1
    z = word
    for d in range(length+1):
        if z == 0:
            return min(length-1, length-d)
        z ^= (z >> 1) | ((z & 1) << (length-1))
        z &= mask
    raise AssertionError('dyadic stream difference failed to vanish')

def main():
    for word in range(256):
        assert valuation(word,8) == slow_polynomial_order(word,8) == cyclic_order(word,8)
    # Separate physical-space update, avoiding the integer-shift recurrence in this control.
    row, x = {0:1}, 1
    for t in range(33):
        enc = sum(v << (t-p) for p,v in row.items())
        assert enc == x
        row = {p:row.get(p-1,0) ^ (row.get(p,0) | row.get(p+1,0))
               for p in range(-t-1,t+2)}
        x ^= (x << 1) | (x << 2)
    words = [bytearray((h+7)//8) for h in PER]
    period_checks = 0
    x, mask = 1, (1 << 41)-1
    for t in range(65537):
        for i,h in enumerate(PER):
            if t < h and ((x >> (2*i)) & 1):
                words[i][t//8] |= 1 << (t%8)
            if t == h:
                assert x & ((1 << (2*i+1))-1) == 1
                period_checks += 1
            if i > 0 and t == h//2:
                assert x & ((1 << (2*i+1))-1) != 1
                period_checks += 1
        if t < 65536:
            x = (x ^ ((x << 1) | (x << 2))) & mask
    resource = []
    for i,h in enumerate(PER):
        word = int.from_bytes(words[i], 'little')
        r = valuation(word,h)
        if h <= 64:
            assert r == slow_polynomial_order(word,h) == cyclic_order(word,h)
        resource.append(r)
    transitions = []
    for i in range(20):
        low = EXP[2*i+1]-EXP[2*i]
        high = EXP[2*i+2]-EXP[2*i+1]
        assert low in (0,1) and high in (0,1)
        weight = low+high
        r, rn = resource[i:i+2]
        if weight == 2:
            assert r == 0 and rn+1 == 1 << (EXP[2*i+2]-1)
        if weight == 1:
            assert r <= rn+1
        if (low,high) == (0,1):
            assert rn == PER[i]-1
        if i > 0 and (low,high) == (1,0):
            assert rn+1 == r, ('Q failed', i, r, rn)
        transitions.append({'pair':i,'diagonals':[2*i,2*i+2],'E':EXP[2*i],
                            'bits':str(low)+str(high),'r':r,'r_next':rn,'drop':r-rn})
    counts = Counter(t['bits'] for t in transitions)
    n0, n2 = counts['00'], counts['11']
    assert 20-EXP[40] == n0-n2
    losses = [t for t in transitions if t['bits']=='00' and t['drop']>1]
    rises = [t for t in transitions if t['bits']=='00' and t['drop']<0]
    print(json.dumps({'bounds':{'pairs':20,'last_diagonal':40,'last_time':65536},
        'controls':{'all_8bit_words':256,'physical_rows':33,'period_checks':period_checks,
                    'polynomial_cyclic_agreement':True,'known_resource_laws':True},
        'predictions':{'P_zero_pair_large_drop':bool(losses),'Q_exact_10_decrement':True,
                       'unexpected_zero_pair_increase':bool(rises)},
        'counts':dict(counts),'deficit':20-EXP[40],
        'large_drops':losses,'zero_pair_increases':rises,'transitions':transitions},indent=2))

if __name__ == '__main__':
    main()
