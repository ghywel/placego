"""GC1155: mandatory endpoint of the published depth-139 record witness.

Missing inference: which information forces this actual record to end,
and can an unobserved right bit repair its next white cell?
Record searched: terminal|endpoint|G25|GC971 with
record|witness|black.time|mask|pivot ->471 hits125 files.
G25, GC970/971/1154, GC1043 and IW's witness format read.
Reuse triangular coding; no new coding theorem or witness verification census.
P1 BEFORE execution: Local's d133,L23,p0 published witness gives
the d139,L17 suffix, with next left depth156 black. This bit is
already fixed by right sites1..155; changing sites156..158 cannot
extend the record. With this left bit flipped white, an unclamped
orbit first loses the wall at time156, while all earlier samples agree.
P2: an arbitrary terminal raw v(155) at black wall time is masked;
all four choices for v(155),v(156) reconstruct the same left156.
Counterfactual: the unused last right trace bit always supplies a free
next left cell. The black-time example must refute it.
Independent: inverse decoder with literal-edge checks versus a packed
unclamped full-row update; scalar clamped right traces for both inputs.
Unexpected: Intel's p1,d125,L21 witness has a WHITE terminal wall
at time145. Algebraically flipping that raw bit must flip left146,
preserve depths0..145, and have a unique zero choice. Those arbitrary
trace flips are not claimed realizable by the actual right half.
Only two fixed committed witness rows, eight three-bit terminal
completions, and four raw trace completions. No solver, language
membership, cut extraction, record search, entrance or depth sweep.
REFUTED-BY: a tail repairs the endpoint, a wrong first failure, or
failure of the white-time pivot contrast. No universal record bound.
ADDENDUM before comparator diagnostic: P3 the retained 78-bit actual
visible word satisfies every GC1154 comparator specification for
d139,L18,p0, despite its black left156. Compare the function's equality
test with direct repeated-block spelling; constant q must violate all
ten specifications. This is a finite source-function diagnostic, not
adoption of GC1154's pending all-depth hand premise or language work.
OUTCOME 2026-10-11 15:34 UTC: P1/P2/P3 PASS. Endpoint156 is black
under all eight right-tail and four raw-trace completions; forcing it
white first breaks the unclamped clock at156. All ten L18 comparators
pass, with their first mismatches by index4. White-time endpoint146
is[1,0] for the two terminal values, earlier left cells identical.
Input SHA256: Local6447670cc3cc9afffc32658f376ff76cb9aa2a2130e33b8bad573dd04d07bc06;
Inteldb4e0e296c55c8bf667674957e00ea4a1bb621ac38816339e5968e3ed73bcdda.
"""
from itertools import product
from pathlib import Path
import re

from rule30_SS_record_residence import decode
from rule30_record_period_comparators import specifications, violates

HERE = Path(__file__).resolve().parent


def witness(name, d):
    text = (HERE / name).read_text()
    pat = r'^d=(\d+) phase=([01]) L=(\d+) T=(\d+) cells=(\d+) verified=yes\n((?:[01]+\n?)+)'
    for m in re.finditer(pat, text, re.M):
        if int(m[1]) == d:
            phase, length, horizon, cells = map(int, m.group(2, 3, 4, 5))
            right = tuple(map(int, m[6].replace('\n', '')))
            assert len(right) == cells and horizon == d+length
            return phase, length, right
    raise AssertionError('missing committed witness')


def right_trace(right, phase, last):
    row = list(right)+(last+3)*[0]
    trace = []
    for t in range(last+1):
        trace.append(row[0])
        wall = (phase+t) % 2
        row = [((wall if j == 0 else row[j-1]) ^ (row[j] | row[j+1]))
               for j in range(len(row)-1)]+[0]
    return tuple(trace)


def full_wall(left, right, last):
    # Bit j is spatial site j-offset. Rule30 uses the left bit at j-1.
    offset = len(left)+last+3
    row = sum(b << (offset-k) for k, b in enumerate(left))
    row |= sum(b << (offset+j+1) for j, b in enumerate(right))
    width = offset+len(right)+last+5
    mask = (1 << width)-1
    trace = []
    for _ in range(last+1):
        trace.append((row >> offset) & 1)
        row = ((row << 1) ^ (row | (row >> 1))) & mask
    return tuple(trace)


def main():
    phase, length, right = witness('rule30_local_witnesses.txt', 133)
    assert (phase, length, len(right)) == (0, 23, 158)
    v = right_trace(right, phase, 156)
    left, _ = decode(v, phase)
    assert left[139:156] == [0]*17
    assert left[156] == 1
    visible = ''.join(str(v[t]) for t in range(0, 155, 2))
    assert len(visible) == 78
    mismatches = []
    for s, period, count, anchor in specifications(139, 18, 0):
        word = visible[s:s+count]
        repeated = (word[:period]*((count+period-1)//period))[:count]
        assert (word == repeated) == violates(visible, s, period, count)
        assert word != repeated and violates('0'*78, s, period, count)
        first = next(j for j in range(period, count)
                     if word[j] != word[j-period])
        mismatches.append((anchor, period, first))
    assert len(mismatches) == 10
    good = tuple(t % 2 for t in range(157))
    assert full_wall(left, right, 156) == good
    changed = left[:-1]+[0]
    bad = full_wall(changed, right, 156)
    assert bad[:156] == good[:156] and bad[156] != good[156]
    tails = 0
    for tail in product((0, 1), repeat=3):
        rr = right[:155]+tail
        vv = right_trace(rr, 0, 156)
        ll, _ = decode(vv, 0)
        assert ll == left and vv[0:155:2] == v[0:155:2]
        assert full_wall(ll, rr, 156) == good
        bad = full_wall(ll[:-1]+[0], rr, 156)
        assert bad[:156] == good[:156] and bad[156] != good[156]
        tails += 1
    for terminal in product((0, 1), repeat=2):
        ll, _ = decode(v[:155]+terminal, 0)
        assert ll == left
    ph, run, rr = witness('rule30_intel_witnesses.txt', 125)
    assert (ph, run) == (1, 21)
    vv = right_trace(rr, ph, 146)
    rows = [decode(vv[:145]+(b, vv[146]), ph)[0] for b in (0, 1)]
    assert rows[0][:146] == rows[1][:146]
    assert rows[0][125:146] == [0]*21
    assert rows[0][146] != rows[1][146]
    print('139 endpoint156=1; retained visible bits', len(visible))
    print('visible', visible)
    print('tail controls', tails, 'raw black-time controls 4 PASS')
    print('L18 comparator first mismatches (anchor,period,index)', mismatches)
    print('white-time endpoint146 values', [r[146] for r in rows], 'PASS')
    print('unclamped first failure at156 for endpoint-white countercontrol PASS')


if __name__ == '__main__':
    main()
