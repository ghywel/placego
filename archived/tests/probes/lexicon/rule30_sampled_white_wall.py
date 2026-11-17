"""GC1173: test a two-step zero-wall projection for the record decoder.

Record searched: two.step/white.wall ->6 hits4files; depth4/white/11
->16 hits12files; sampled/zero/wall ->11 hits6files. C7/R4 and the
Rule210 two-step control read. C7 supplies depth4 zero at white times;
this probe does not extend the old affine formulas.
Predictions BEFORE execution: with patch (A,B,0,D,E), Rule30 squared
is A XOR ((1-B)*(D OR E)), by expanding its three intermediate cells.
Independent control: all16 patches against two literal truth-table steps.
CF: retaining (0,D,E) suffices to recover A under next centre zero;
patches01010 and10010 must refute it. Both come from real root triples
000 and001 in the existing sharp132 fixture, not new language searches.
Unexpected: even their nearest-right bit D alone is identical and black;
the hidden B completely masks that right input in the second patch.
No solver, record/cut/language census, global affine fit or depth scan.
OUTCOME 2026-10-13, Intel CPU: all16 folded/literal checks PASS.
Known real root offsets1 and2 give patches01010 and10010, both next
centre zero. The projected inverse counterfactual is REFUTED.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path
from rule30_local_record_traces import OUT, blocks
from rule30_prefix_realization import inverse

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)


def step(row):
    return tuple(TABLE[4*a+2*b+c] for a,b,c in zip(row,row[1:],row[2:]))


def main():
    cases = 0
    for a,b,d,e in product((0,1), repeat=4):
        assert step(step((a,b,0,d,e)))[0] == a ^ ((1-b)*(d|e))
        cases += 1
    assert sha256(Path(OUT).read_bytes()).hexdigest() == (
        'dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e')
    q = next(x for x in blocks(OUT) if x[0] == 132)[6]
    patches = []
    for triple in ('000','001'):
        offset = q.index(triple)
        initial = inverse(list(map(int,triple)),0)
        patch = tuple(reversed(initial[1:6]))  # physical sites -6 .. -2
        assert patch == ((0,1,0,1,0) if triple == '000' else (1,0,0,1,0))
        assert step(step(patch)) == (0,)
        patches.append(patch)
        print('known real root offset',offset,'patch',''.join(map(str,patch)))
    assert patches[0][2:] == patches[1][2:] and patches[0][0] != patches[1][0]
    print('literal/folded controls',cases,'PASS; projected inverse CF REFUTED')


if __name__ == '__main__':
    main()
