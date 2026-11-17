"""GC1071: finite front selector repairs a wrong long-collar released sample.
Missing inference: determine when GC1070's first released mismatch
is healed immediately, uniformly in collar length K, rather than
assuming every mismatch has a zero lane. Record searched: zero.lane|
anti.diagonal with collar|black|repair ->1 irrelevant hit; front|
moving.frame|diagonal with collar|period.?16|four.bit|four.cell ->60
hits in28 files. GC1070 lock and GC1057 merger reused; no matching
three-cell right-moving collar selector found. No global affine model.
P1 BEFORE controls: with even K>=10, child preceding an alternating
K-collar has cell0 just before the collar and bits b,c at one,two
sites farther left. In the moving front a'=NOT a, b'=b XOR a,
c'=c XOR(b OR a), a0=0. Its three-cell state returns after8 updates.
The inner cell at release+1 is c XOR b, c, NOT c XOR b, NOT c
for K mod8=0,2,4,6. This determines the actual black shield.
P2: if that selector is1, target released samples11 repair the
forced actual released0 then1; full interiors coalesce at K+2.
The actual first W+K+4 observations lift arbitrary later target inputs.
Counterfactual: released1 alone decides whether immediate repair works;
P1 predicts different results at different front phases and b,c.
Retained hand failure: a proposed universal first-site black shield was
abandoned; all-zero front initial state has first selector0 at K=0mod8.
Do not infer a uniform zero-lane bound from the successful cases.
Unexpected prediction: target next sample0 always prevents merger.
FIRST CONTROL FAILURE retained: K10,b=c=1 has selector1 but Q_K=0,
so the target endpoint after released1 is black and masks next0.
P3 informed BEFORE revised controls: merger occurs exactly when
selector1 AND (next sample1 OR Q_K=0); check both next samples.
Keep the original negative only when the target endpoint is white.
Controls: finite four initial states and all eight clock phases, plus
literal/packed original cones at four representative even K residues.
No solver, trace-language or width census; these are invariant controls.
"""
from itertools import product
from rule30_sl_no_refork import bits, run
from rule30_trace_prefix_repair import strip, trace


def advance(a,b,c):
    return 1-a, b^a, c^(b|a)


def selector(K,b,c):
    return {0:c^b, 2:c, 4:(1-c)^b, 6:1-c}[K%8]


def main():
    cycles = mergers = failures = matched = extra = 0
    for b,c in product((0,1), repeat=2):
        states=[(0,b,c)]
        for t in range(16): states.append(advance(*states[-1]))
        assert states[8] == states[0] == states[16]
        for K in (0,2,4,6):
            assert states[K+1][2] == selector(K,b,c)
        cycles += 1
    for K in (10,12,14,16):
        W=K+4
        T=2*W-2
        for p,phase,h,k,mode in product((0,1),repeat=5):
            prefix=(p,0)+bits('01')*(K//2)
            ref=run(prefix+bits('001110')+(0,)*4,2,phase)
            child=ref[2][:W]
            actual=run(prefix+bits('0000000')+(h,k,1-h,1-k)*24,T,phase)
            b,c=actual[2][2],actual[2][1]
            state=(0,b,c)
            for t in range(K+1):
                assert actual[t+2][t+1:t+4] == state[::-1]
                state=advance(*state)
            shield=selector(K,b,c)
            assert actual[K+3][W-2] == shield
            assert actual[K+2][W-1] == 0
            assert actual[K+2][W:W+2] == (0,1)
            assert actual[K+3][W] == 1
            middle=tuple((t+mode)&1 for t in range(K-4))
            rest=tuple((t+h+k)&1 for t in range(T-2-K-2))
            target=strip(child,bits('0100')+middle+(1,1)+rest,phase)
            assert actual[K+3][:W-1] == target[K+1][:-1]
            assert actual[K+3][W-1] != target[K+1][-1]
            assert (actual[K+4][:W] == target[K+2]) == bool(shield)
            QK=actual[K+2][W-2]
            bad=strip(child,bits('0100')+middle+(1,0),phase)
            assert (actual[K+4][:W] == bad[K+2]) == bool(shield and QK == 0)
            if shield:
                assert trace(actual) == trace(ref[:2])+trace(target)
                assert actual[K+4][:W-1] == bad[K+2][:-1]
                assert (actual[K+4][:W] == bad[K+2]) == (QK == 0)
                if QK:
                    assert actual[K+4][W-1] != bad[K+2][-1]
                    failures+=1
                else:
                    extra+=1
                    fullbad=strip(child,bits('0100')+middle+(1,0)+rest,phase)
                    assert trace(actual) == trace(ref[:2])+trace(fullbad)
                mergers+=1
            matched+=1
    assert mergers == 64 and failures == extra == 32
    print({'finite_front_cycles':cycles, 'actual_front_controls':matched,
           'coupled_release_mergers':mergers, 'masked_zero_sample_mergers':extra,
           'white_target_next_sample_guards':failures,
           'literal_packed':'PASS', 'period8_selector':'PASS'})


if __name__=='__main__':
    main()
