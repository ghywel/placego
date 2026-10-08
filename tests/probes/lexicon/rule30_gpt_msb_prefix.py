"""GC528 transpose GC487's fixed sample into MSB-first state certificates.
Scope unchanged: positive prefixes 1..32, suffix lengths 0..4, bits through 527.
Predict all 32 Rule30 prefix profiles distinct; Thue-Morse exactly two.
Counterfactual: this finite certificate proves nonautomaticity (reject).
Unexpected: suffix 0 of length zero is empty, not an added zero digit.
Independent decimal-set and packed XOR/OR histories must agree first.
No larger trace, kernel census or asymptotic state-count fit.
"""
from rule30_gpt_selected_potential import decimal_set_step
from rule30_gpt_kernel_prefix import signatures

if __name__ == '__main__':
    T=527; off=T+2; mask=(1<<(2*off+1))-1
    row=1<<off; cells={0}; bits=[]
    for t in range(T+1):
        assert {i-off for i in range(2*off+1) if row>>i&1} == cells
        bits.append((row>>off)&1)
        if t<T:
            row=((row<<1)^(row|(row>>1)))&mask
            cells=decimal_set_step(cells)
    suffixes=[(d,r) for d in range(5) for r in range(1<<d)]
    def profiles(f):
        return {n:tuple(f((1<<d)*n+r) for d,r in suffixes) for n in range(1,33)}
    for n in range(1,33):
        for d,r in suffixes:
            suffix=format(r, f'0{d}b') if d else ''
            assert int(bin(n)[2:]+suffix,2)==(1<<d)*n+r
    p=profiles(lambda n:bits[n]); tm=profiles(lambda n:n.bit_count()&1)
    assert len(set(tm.values()))==2
    assert len(set(p.values()))==32
    assert len(set(signatures(lambda n:bits[n]).values()))==31
    witnesses=[]
    for n in range(1,33):
        for m in range(1,n):
            j=next(j for j in range(len(suffixes)) if p[n][j]!=p[m][j])
            d,r=suffixes[j]
            assert bits[(1<<d)*n+r] != bits[(1<<d)*m+r]
            witnesses.append((m,n,d,r))
    finite=lambda n:bits[n] if n<len(bits) else 0
    assert profiles(finite)==p
    print('PASS 528 independent rows; 32 MSB profiles; 2 Thue-Morse profiles; 31 original LSB signatures')
    print('MSB witnesses',witnesses)
