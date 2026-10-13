"""GC1178: fixed-window corner quotient, keeping a black-failure stop.

Record searched: right.prefix/modul ->no hit; corner/period ->16 hits
11files; seed11/word ->1 unrelated hit. G249, GC1176/77 read.
PREDICTIONS BEFORE execution (2026-10-13): at h3, the proved general
modulus M_h=2^(ceil((4h+3)/3)-1) is16. Named positive aliases
1/17,2/18,9/25,13/29,16/32 have identical low6 white-arrival bits,
black-failure time and demanded visible bits before that failure.
Independent: literal ordinary seed11 snapshots versus packed clamped
left evolution. No higher h, longer deadline, cut or seed census.
CF: incrementing r by1 always preserves this window; r1/r2 must refute.
Unexpected: residue0 is represented by positive r16/r32, not an actual
corner at r0; r2's failed first black test must suppress later samples.
"""
from rule30_corner_two_cell import ordinary
from rule30_prefix_realization import packed


def window(r,h):
    x = 2*r-2
    row = ordinary(2*r)
    low = {j: row.get(x-j,0) for j in range(1,2*h+1)}
    # Only times0..2h-1 use this known prefix; no guessed farther bit.
    bits = packed(low,0,2*h-1)
    fail = next((t for t in range(1,2*h,2) if bits[t] == 0), None)
    stop = 2*h if fail is None else fail
    word = ''.join(str(1-bits[t]) for t in range(0,stop,2))
    return tuple(low.values()),fail,word


def main():
    h = 3
    m = 1 << ((4*h+5)//3-1)  # ceil((4h+3)/3)-1
    assert m == 16
    for r in (1,2,9,13,16):
        a,b = window(r,h),window(r+m,h)
        assert a == b,(r,a,b)
        print('alias',r,r+m,'failure',a[1],'pre-failure word',a[2],'PASS')
    assert window(1,h) != window(2,h)
    assert window(2,h)[1:] == (1,'1')
    assert window(16,h)[1:] == (1,'1')
    print('wrong increment and stopped-word/positive-residue0 controls PASS')
    print('NO NEW WINDOW LENGTH OR DEADLINE SCAN')


if __name__ == '__main__':
    main()
