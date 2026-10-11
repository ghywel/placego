"""GC1153: test a uniform-six spatial white-gap lift of the pure rings.

Missing inference: can the pure S/L gap bounds combine into a mixed
spatial invariant? Record searched: GC1007|white.gap|white gap|
zero.run|mixed with six|uniform|forcing|spatial|ring ->202 hits71files;
L579|qA|qB|SLLLSLSL with present|SAT|witness|membership|actual
->19 hits15files. GC709/1007/1008, L579 and GC1148/1151 read.
P1 BEFORE run: the fixed GC1007 ROOT+A+A+A forced initial left
prefix through depth180 contains a white run longer than six.
P2 (blind scope control): its already actual ROOT+A prefix qA
also has a white run longer than six, within its determined depths.
Counterfactual: all decoded runs in the two fixed prefixes are <=6.
Controls: the pure S and L words reproduce reference-ring bits and
their maximal white gaps5 and6 through depth180; literal-table
inverse edges; an independent packed bit recurrence using GC709's
left-column pulse identity must give the same initial mixed rows.
Unexpected check: compare the proposed obstruction on the actual
qA word, not just the longer relaxed concatenation. L579's existing
membership result is cited, not replayed or extended. No membership
claim for A+A+A. No solver, record maximization, word-length sweep,
unary/affine fit, graph or strip run. Failure of P1 is inconclusive,
not evidence for an all-depth uniform bound.
REFUTED-BY: no run longer than six refutes P1 or P2 respectively;
any independent-engine mismatch invalidates the computed verdict.
OUTCOME 2026-10-11 14:48 UTC: P1 and P2 HOLD. Both fixed rows
have maximal white run7 at depths30..36, bracket100000001;
the pure-ring and packed/literal inverse controls PASS. The interval
lies inside the original ENTRY=LSLSL, before the first A loop.
ADDENDUM BEFORE endpoint controls: GC709 gives the first LEFT
column from q through physical time35. Thus its first18 white-time
bits (times0..34), plus the forced odd-time left bit at35, suffice
to fix depth36. Predict all eight choices of four arbitrary odd
nearest-right patterns and the unobserved even bit at36 retain the
seven whites. Counterfactual: completing the last gap at42 or keeping
the visible bit at36 is essential. These are inverse-scope controls,
not actual membership claims for the arbitrary odd assignments.
ADDENDUM OUTCOME 2026-10-11 14:48 UTC: all8 endpoint controls
PASS; first18 visible bits100001001000010010 fix left30..36
to zero despite the arbitrary odd samples and terminal bit.
"""
from rule30_SS_record_residence import decode

H = {'S': '110100', 'L': '1101000100'}
ENTRY = 'LSLSL'
A = 'SLLLSLSL'
ROOT = '1000010010000100100001'


def gaps(row):
    out = []
    i = 1
    while i < len(row):
        if row[i]:
            i += 1
            continue
        j = i+1
        while j < len(row) and not row[j]:
            j += 1
        out.append((i, j-i))
        i = j
    return out


def packed_left(q, depth):
    # GC709 has c_-1(t)=1-q(t), with zero odd-time pulse.
    n = 2*len(q)-1
    mask = (1 << n)-1
    prev = sum((t % 2) << t for t in range(n))
    cur = sum((1-(int(q[t//2]) if t % 2 == 0 else 0)) << t
              for t in range(n))
    row = [0]
    for k in range(1, depth+1):
        row.append(cur & 1)
        n -= 1
        mask = (1 << n)-1
        nxt = ((cur >> 1) ^ (cur | prev)) & mask
        prev, cur = cur, nxt
    return row


def main():
    for letter, ring, period, expected in (
            ('S', 0x688eb74a45efb082671ee, 84, 5),
            ('L', 0x35409b1caa645d715104db5291a2fe8415260ce, 155, 6)):
        h = H[letter]
        v = tuple(int(h[t % len(h)]) for t in range(181))
        row, _ = decode(v, 0)
        assert row == [(ring >> ((-k) % period)) & 1 for k in range(181)]
        assert max(length for _, length in gaps(row)) == expected
    verdicts = []
    for name, word, depth in (('qA', ENTRY+A, 110),
                              ('qAAA', ENTRY+A*3, 180)):
        q = '1'+''.join('001' if g == 'S' else '00001' for g in word)
        assert q.startswith(ROOT)
        if name == 'qA':
            assert q == '10000100100001001000010010000100001000010010000100100001'
        full = ''.join(H[g] for g in word)+'1'
        assert full[::2] == q
        row, _ = decode(tuple(map(int, full[:depth+1])), 0)
        assert row == packed_left(q, depth)
        runs = gaps(row)
        start, length = max(runs, key=lambda z: z[1])
        print(name, 'depth='+str(depth), 'maximum='+str(length),
              'start='+str(start),
              'bracket='+''.join(map(str, row[max(0,start-1):start+length+1])),
              'actual_membership='+('L579' if name == 'qA' else 'UNCLAIMED'))
        print('left_depths_0_to_'+str(depth)+'='+''.join(map(str, row)))
        verdicts.append(length > 6)
    print('CONTROLS PASS; P1='+str(verdicts[1])+'; P2='+str(verdicts[0]))
    prefix = ROOT[:18]
    tested = 0
    for mode in range(4):
        for terminal in (0, 1):
            v = tuple(int(prefix[t//2]) if t % 2 == 0 and t < 36
                      else terminal if t == 36
                      else (0, 1, (t//2) % 2, 1-(t//2) % 2)[mode]
                      for t in range(37))
            row, _ = decode(v, 0)
            assert row[29:38] == [1]+[0]*7  # depth37 is unobserved
            tested += 1
    print('Endpoint controls PASS:', tested, 'visible_prefix='+prefix)


if __name__ == '__main__':
    main()
