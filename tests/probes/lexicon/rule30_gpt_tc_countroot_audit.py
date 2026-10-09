#!/usr/bin/env python3
"""GC889: independent count-root certificates from the four published F lists.
RUN-ON: cpu, Python3; COMMAND: python3 tests/probes/lexicon/rule30_gpt_tc_countroot_audit.py
Predictions in CLOUD-LOCAL before execution: odd input digests/antichains and
completed counts match; p2 six-decimal root ceiling1.129634. Controls full binary
and finite-prefix F00/01. Unexpected: the predecessor decimal fails the integer
power inequality. No SAT, layer/product or spectral replay. Uses own GC886 DP.
OUTCOME: all assertions PASS; ceilings p2/5/7/9 are1129634,1521255,
1647689,1713392 divided by10^6. No SAT membership/completeness verified.
"""
from hashlib import sha256
from pathlib import Path
from rule30_gpt_tc2_input_audit import antichain, counts, DIGEST, EXPECTED

META = {
    2: ('rule30_cloud_channel_truecount_F.txt', DIGEST, 746, EXPECTED, 40, 46),
    5: ('rule30_cloud_hole_truecount_F5.txt',
        '8ed9907554bd27e7770e2cc97e3a82be92e9399eb7c1176fa9fb624d809f10ac',
        1328, [2,4,8,16,31,60,108,183,301,506,833,1336,2089,3236,4919,7401,10953],18,271),
    7: ('rule30_cloud_hole_truecount_F7.txt',
        'fa3f71eeed0bb687bfd5461ad9c76d7816d166dd67c05dcf085c7cd91f8eaf41',
        641, [2,4,8,16,30,56,105,189,332,563,943,1549,2523,4053,6468],16,41),
    9: ('rule30_cloud_hole_truecount_F9.txt',
        'a771402f272f32f9da0c802283c6ef3f8db238e0f2b449a4d4e5b32318711624',
        270, [2,4,8,16,30,56,102,181,321,559,961,1624,2717,4530],15,1),
}


def root_ceiling(a, n):
    target = a * 10**(6*n)
    lo, hi = 0, 2000000
    assert hi**n >= target
    while lo < hi:
        mid = (lo+hi)//2
        if mid**n >= target:
            hi = mid
        else:
            lo = mid+1
    assert lo**n >= target and (lo == 0 or (lo-1)**n < target)
    return lo


def main():
    assert counts([],8)[0] == [2**n for n in range(1,9)]
    assert counts(['00','01'],8)[0] == [2]*8
    assert root_ceiling(2**8,8) == 2000000
    for p, (file,digest,nword,expected,partial,np) in META.items():
        F = Path(__file__).with_name(file).read_text().splitlines()
        assert len(F) == len(set(F)) == nword
        assert all(w and set(w) <= {'0','1'} for w in F)
        assert F == sorted(F,key=lambda w:(len(w),w))
        assert sha256('\n'.join(F).encode()).hexdigest() == digest
        assert antichain(F)
        assert max(map(len,F)) == partial
        assert sum(len(w)==partial for w in F) == np
        got, ns = counts(F,400)
        assert got[:len(expected)] == expected
        R = root_ceiling(got[-1],400)
        if p == 2:
            assert R == 1129634
        print('p',p,'PASS; prefix states',ns,'root ceiling',str(R)+'/1000000')
        print('a400',got[-1])
    print('PASS: all digests/counts/antichains; exact root ceilings and minimal predecessors')


if __name__ == '__main__':
    main()
