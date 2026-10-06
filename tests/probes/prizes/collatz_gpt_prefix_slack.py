"""G85 FP1-FP2 and G86 SR1 preregistered at2a8df48, published viaaab6d7d.
FP: 256 displacement-four pairs; condition on lower admission through5;
require prefixes11011/11111, affine relations, residues and next parity.
SR: full33-step word admitted, shifted suffix admitted, fresh deficit26;
27/31 after6 have counts5/5, states107/121. No collision search.
CF removing admission or restarting fresh must fail explicit guards.
OUTCOME: FP passes 256 pairs, 64 qualifying and 192 excluded; SR passes
full/shifted admission and fresh deficit 26. Both counterfactuals refuted.
"""
from collatz_gpt_boundary_loss import admissible


def path(n, horizon):
    bits, values = [], [n]
    for _ in range(horizon):
        b = n % 2
        bits.append(b)
        n = (3*n+1)//2 if b else n//2
        values.append(n)
    return tuple(bits), values


def first_deficit(bits, odd_credit=0, time_credit=0):
    a = odd_credit
    for k,b in enumerate(bits,1):
        a += b
        if 3**a < 2**(time_credit+k):
            return k
    return None


def main():
    qualified = excluded = 0
    for k in range(256):
        n = 8*k+3
        low, x = path(n,6)
        high, y = path(n+4,6)
        assert low[:3] == (1,1,0) and high[:3] == (1,1,1)
        assert y[3] == 3*x[3]+14
        if not admissible(low[:5]):
            excluded += 1
            continue
        qualified += 1
        assert low[:5] == (1,1,0,1,1) and high[:5] == (1,1,1,1,1)
        assert n % 32 == 27 and (n+4) % 32 == 31
        assert y[4] == 3*x[4]+20 and y[5] == 3*x[5]+29
        assert low[5] != high[5]
    low,x = path(3,5)
    high,y = path(7,5)
    assert low == (1,1,0,0,0) and high == (1,1,1,0,1)
    assert first_deficit(low) == 4
    low,x = path(27,6)
    high,y = path(31,6)
    assert sum(low) == sum(high) == 5 and (x[6],y[6]) == (107,121)
    full = (1,1,0,1,1,1)+(1,)*16+(0,)*11
    suffix = full[6:]
    assert len(full) == 33 and sum(full) == 21
    assert admissible(full) and first_deficit(full) is None
    assert first_deficit(suffix,5,6) is None
    assert not admissible(suffix) and first_deficit(suffix) == 26
    assert 2**25 < 3**16 < 2**26 and 3**21 > 2**33
    print('FP PASS256 pairs:',qualified,'admitted lower prefixes,',excluded,'excluded; no meeting assertion')
    print('SR PASS full/shifted admission, fresh deficit26; 27/31 six-step states107/121')
    print('Both counterfactuals REFUTED; no collision search')


if __name__ == '__main__':
    main()
