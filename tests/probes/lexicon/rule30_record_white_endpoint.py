"""GC1156: the unmasked endpoint of Local's sharp depth-132 witness.

Missing inference: does a white terminal wall supply a physical next
visible choice, or can the retained right cylinder prevent that choice?
Record searched: right|diagonal|boundary|pivot with
derivative|sensitivity|shield|endpoint|permutiv ->577 hits149 files.
Read G25, GC856, GC1004..1006, GC1155 and L643; reuse triangular coding
and the radius-one cone. No new language, solver or record census.
Predictions before execution are retained in this docstring:
P1: the fixed 145-cell RIGHT prefix for d132,L17,p0 forces left149
black for all 16 assignments at sites 146..149, and preserves all
visible samples through 148. P2: a set-valued enclosure allowing an
arbitrary exterior also fixes the unmasked terminal v148.
Counterfactual: extending an exterior always realizes both algebraic
choices at a white terminal time. P1/P2 must reject that assertion for
this one cylinder, not for all realizations of its visible prefix.
Independent: literal scalar RIGHT update versus a packed RIGHT engine
and packed unclamped full-row evolution. Unexpected: flip algebraic
v148 alone; left149 toggles, depths1..148 remain unchanged.
Only one committed witness, 16 four-bit completions, one finite
enclosure through 149. No depth, language, prefix-length or record scan.
OUTCOME 2026-10-11 15:44 UTC: P1/P2 PASS. v148=0 and left149=1
for all 16 completions. Replacing left149 by0 first breaks the
unclamped wall at149. Algebraic v148 choices0/1 give left149=1/0.
The first unknown enclosure site never comes below 82 through 149.
Finite controls COMPUTED; the all-exterior cylinder inference is
tier2, carrying step: set-valued local propagation encloses every
actual completion. No all-depth R_real bound or root-word uniqueness.
Input SHA256 dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path

from rule30_local_record_traces import blocks, OUT
from rule30_record_endpoint_mask import right_trace, full_wall
from rule30_SS_record_residence import decode

DIGEST = 'dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e'
TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def packed_trace(right, phase, last):
    width = len(right)+last+4
    mask = (1 << width)-1
    row = sum(b << j for j, b in enumerate(right))
    trace = []
    for t in range(last+1):
        trace.append(row & 1)
        row = (((row << 1) | ((phase+t) % 2))
               ^ (row | (row >> 1))) & mask
    return tuple(trace)


def enclosure(right, phase, last):
    # Large enough that no omitted initial site reaches any examined cell.
    row = [frozenset([b]) for b in right]
    row += [frozenset([0, 1]) for _ in range(last+4)]
    rows = []
    for t in range(last+1):
        rows.append(row)
        wall = frozenset([(phase+t) % 2])
        row = [frozenset(TABLE[4*a+2*b+c]
                         for a in (wall if j == 0 else row[j-1])
                         for b in row[j] for c in row[j+1])
               for j in range(len(row)-1)]
    return rows


def main():
    assert sha256(Path(OUT).read_bytes()).hexdigest() == DIGEST
    d, L, phase, T, status, tr, visible, stored, rr = next(
        b for b in blocks(OUT) if b[0] == 132)
    right = tuple(map(int, rr))
    assert (d, L, phase, T, status, len(right)) == (132, 17, 0, 148, 'exact', 145)
    enc = enclosure(right, phase, 149)
    assert enc[148][0] == frozenset([0])
    frontier = [next((j+1 for j, s in enumerate(row) if len(s) == 2), len(row)+1)
                for row in enc]
    assert min(frontier) == 82
    good = tuple(t % 2 for t in range(150))
    for tail in product((0, 1), repeat=4):
        r = right+tail
        v = right_trace(r, phase, 149)
        assert v == packed_trace(r, phase, 149)
        assert ''.join(map(str, v[:149])) == tr
        assert ''.join(map(str, v[:148:2])) == visible
        assert v[148] == 0
        left, _ = decode(v, phase)
        assert ''.join(map(str, left[1:149])) == stored
        assert left[149] == 1
        assert full_wall(left, r, 149) == good
        bad = full_wall(left[:-1]+[0], r, 149)
        assert bad[:149] == good[:149] and bad[149] != good[149]
        # Control enclosure containment on the entire cone of v148.
        row = list(r)+[0]*153
        for t in range(149):
            assert all(row[j] in enc[t][j] for j in range(149-t))
            row = [TABLE[4*(t % 2 if j == 0 else row[j-1])+2*row[j]+row[j+1]]
                   for j in range(len(row)-1)]
    v = right_trace(right, phase, 149)
    lefts = [decode(v[:148]+(b, v[149]), phase)[0] for b in (0, 1)]
    assert lefts[0][:149] == lefts[1][:149]
    assert [left[149] for left in lefts] == [1, 0]
    print('132: all 16 completions v148=0, left149=1; scalar/packed/full-wall PASS')
    print('Arbitrary-exterior enclosure v148={0}; minimum unknown site 82 PASS')
    print('Algebraic endpoint values[1,0]; endpoint-white first wall failure 149 PASS')


if __name__ == '__main__':
    main()
