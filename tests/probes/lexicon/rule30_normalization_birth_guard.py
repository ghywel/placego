"""GC1182: first-bit quotient lacks the parent equality used in promotion.

BEFORE controls, 2026-10-13: use ONLY the existing actual phase0 d133
witness, its named d6/L1 checkerboard zero and d139/L17 record suffix.
P1: first-bit normalization preserves each named initial white band,
but at least one canonical inherited-zero chain changes before birth.
CF: same deep child row implies the same canonical birth age, and hence
permits GC1181 zero-prefix promotion after erasing an actual initial1.
Independent controls: truth-table inverse versus XOR/OR trace decoder;
forward two ticks versus rebuilding the suffix root. Unexpected: the
normalized root is absent (00000); preserve the actual origin rather
than calling the normalized word real. No new witness, root or depth
census, solver, cut extraction, or Local profile computation.
Record searched: normaliz/inherit ->1 unrelated hit; erasure/ancestor
->GC1174 scope warning; first.bit/birth ->GC1174 andGC1181; delayed|
shifted|interior with eras|normaliz|invisible ->23 hits12files, no carrying
normalization-birth identity. GC1159, GC1170, GC1174 andGC1181 read.

OUTCOME: P1 FAILED as an age prediction: both fixed bands have age1
under both roots. The d6 parent band changes011 to101; the d139 parent
band is unchanged. Deep image equality and two-tick equality PASS.
Neither age preservation nor age change in general follows. The exact
parent equality needed by zero-prefix promotion fails at its first free
cell, checked independently below. Retain the failure; no widening.
"""
from hashlib import sha256
from rule30_record_endpoint_mask import HERE, witness, right_trace
from rule30_prefix_realization import inverse
from rule30_canonical_parent_budget import ancestor, forward
from rule30_SS_record_residence import decode


def birth(w, d, length):
    # n is the number of inherited steps; a=n+1 is first nonzero parent.
    assert ancestor(w, 0, 0)[d-1:d+length-1] == [0]*length
    for n in range(1, d//2+2):
        a = ancestor(w, 0, n)
        lo, count = d-n, length+2*n
        band = a[lo-1:lo-1+count]
        assert len(band) == count
        if any(band):
            return n, ''.join(map(str, band))
    raise AssertionError('checkerboard must interrupt inheritance')


def main():
    assert sha256((HERE/'rule30_local_witnesses.txt').read_bytes()).hexdigest() == (
        '6447670cc3cc9afffc32658f376ff76cb9aa2a2130e33b8bad573dd04d07bc06')
    p, _, right = witness('rule30_local_witnesses.txt', 133)
    assert p == 0
    trace = right_trace(right, 0, 156)
    w = list(trace[0:155:2])
    z = [0]+w[1:]
    assert w[:5] == [1,0,0,0,0] and z[:5] == [0]*5
    x, y = inverse(w, 0), inverse(z, 0)
    decoded, _ = decode(trace, 0)
    assert x[:155] == decoded[1:156]
    assert x[3:] == y[3:]
    for d, length in ((6,1), (139,17)):
        old, new = birth(w,d,length), birth(z,d,length)
        assert old[0] == new[0] == 1
        assert (old[1], new[1]) == (('011','101') if d == 6 else ('1'*19,'1'*19))
        print('named band',d,length,'actual birth',old[0],
              'normalized birth',new[0], 'parent bands',old[1],new[1])
    rows = [x,y]
    for t in range(2):
        rows = [forward(row,t%2) for row in rows]
    assert rows[0] == rows[1] == inverse(w[1:],0)
    # a1 original parent has rootw; rebased age3 parent has root0u.
    original = ancestor(w,0,1)
    promoted = ancestor(w[1:],0,3)
    assert original[0] == promoted[0] == 1
    assert original[1] != promoted[1]  # first free cell at N+1=2
    print('normalization plus promotion: parent equality FAILS at depth2')
    print('deep child equality, independent decoder, and two-tick equality PASS')
    print('normalized00000 absent; actual origin retained; no membership inference')

if __name__ == '__main__':
    main()
