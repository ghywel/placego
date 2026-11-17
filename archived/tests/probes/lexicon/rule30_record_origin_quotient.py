"""GC1159: retain cut provenance after quotienting the first visible bit.

PREDICTIONS BEFORE controls: under q1=0, q0 flips preserve all h4 pairs
for eight specified 3-bit suffixes. C7's existing depth3/4 agreement
proves this for every continuation and every k>=4. The actual d133
root supplying the sharp139 suffix begins10000; q0=0 normalization
introduces the certified cut00000 without changing h4. The ordinary
normalized-cut acceptance counterfactual must therefore fail.
Repair: initialize both valid first-bit cut origins, advance residuals
elementwise on the shared suffix, reject only if every origin rejects.
Independent: literal Wolfram-table inversion versus GC971's XOR/OR
image; direct substring tests versus residual-subset acceptance.
Unexpected: with q1=1, unrestricted q0 flips change the first h4
letter. The no11 gate is essential, not an arbitrary global mask.
Record searched: first.*visible|first.*white|bit.?0|q.?0 with
forget|coalesc|shield|tail ->114 hits35 files; canonical|normaliz|
quotient|erase|flip with00000|first.*bit|bit.?0|q.?0 ->153 hits53 files.
C7/R4, G12/G13, GC1004..06 and GC1158 read. Existing identities reused.
Only 16 short image comparisons and one fixed existing witness root.
No solver, membership census, CUT/S/L extraction or record search.
The quotient gives no white-record bound.
OUTCOME 2026-10-11 17:43 BST, one Intel CPU process: eight q1=0
shielding comparisons and eight q1=1 negative controls PASS. The actual
78-bit root's first-bit normalization closes00000; its h4 image is
unchanged and the two-origin residual subset accepts. All17 independent
substring/subset controls PASS. C7's all-tail identity is reused; the
new cut-preserving quotient is a tier-2 sketch awaiting targeted review.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path

from rule30_record_endpoint_mask import witness, right_trace, HERE
from rule30_rrl_transducer import literal_image

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
CUTS = ('11', '00000')


def root(q):
    return tuple(2*(t % 2)+(int(q[t//2]) if t % 2 == 0 else 0)
                 for t in range(2*len(q)))


def table_image(word):
    out = []
    for (a, b) in zip(word, word[1:]):
        u, v = divmod(a, 2)
        next_u = b//2
        left = next(x for x in (0, 1) if TABLE[4*x+2*u+v] == next_u)
        out.append(2*left+u)
    return tuple(out)


def fourth_image(q):
    a = b = root(q)
    for _ in range(4):
        a, b = table_image(a), literal_image(b)
        assert a == b
    return a


def permitted(q):
    return not any(f in q for f in CUTS)


def possible_residuals(common):
    """All permitted first-bit origins; common contains bits from q1 on.

    This is the cut automaton alone, not an actual-language test.
    """
    prefixes = {''} | {f[:j] for f in CUTS for j in range(1, len(f))}

    def advance(s, bit):
        candidate = s+bit
        if any(candidate.endswith(f) for f in CUTS):
            return None
        return max((p for p in prefixes if candidate.endswith(p)), key=len)

    states = {advance('', bit) for bit in '01'} - {None}
    for bit in common:
        states = {advance(s, bit) for s in states} - {None}
    return states


def main():
    positive = negative = 0
    for q1 in '01':
        for suffix in product('01', repeat=3):
            common = q1+''.join(suffix)
            images = [fourth_image(b+common) for b in '01']
            if q1 == '0':
                assert images[0] == images[1]
                positive += 1
            else:
                assert images[0][0] ^ images[1][0] == 2
                negative += 1
            assert bool(possible_residuals(common)) == any(permitted(b+common) for b in '01')
    name = 'rule30_local_witnesses.txt'
    assert sha256((HERE/name).read_bytes()).hexdigest() == (
        '6447670cc3cc9afffc32658f376ff76cb9aa2a2130e33b8bad573dd04d07bc06')
    phase, length, right = witness(name, 133)
    assert (phase, length, len(right)) == (0, 23, 158)
    v = right_trace(right, 0, 154)
    q = ''.join(str(v[t]) for t in range(0, 155, 2))
    normalized = '0'+q[1:]
    assert q.startswith('10000') and normalized.startswith('00000')
    assert permitted(q) and not permitted(normalized)
    assert fourth_image(q) == fourth_image(normalized)
    assert possible_residuals(q[1:])
    assert any(permitted(b+q[1:]) for b in '01')
    print('C7 shielding controls', positive, 'and no11-gate negatives', negative, 'PASS')
    print('Actual 78-bit root: normalized cut rejects, same h4 image; residual union accepts PASS')
    print('All 17 direct-substring versus residual-subset controls PASS')


if __name__ == '__main__':
    main()
