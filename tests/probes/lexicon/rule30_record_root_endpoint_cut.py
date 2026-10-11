"""GC1157: lift the sharp132 endpoint from one cylinder to its root word.

Missing inference: an endpoint certificate for every real realization of
the retained root visible word, rather than one initial right cylinder.
P1 BEFORE lookup: q+1 contains a certified phase0 minimal absent word
of length<=44, ending at the new bit; q+0 contains none.
Counterfactual: both pass cutoff44, requiring a longer cut or hidden
right relation. Do not widen or run a solver if the prediction fails.
Independent: direct substring lookup versus suffix comparison; literal
inverse reconstruction with both odd raw patterns and terminal bits.
Unexpected: the cut starts at an odd visible index, but its physical
rebase must still be white in phase0. Do not import phase1-only cuts.
Record searched: root|visible|record|R_real with prefix.*determ|
determ.*prefix|cylinder|right.*state|preimage ->258 hits94 files.
Read G25, GC1155/56, L643 and the certified44 fixture; certificates
adopted, not replayed. Only one saved root and two terminal extensions.
No language census, exact membership solver, CUT solve, S/L extraction,
RTU, relaxed-record computation, prefix-length or depth scan.
OUTCOME: q has length74. Exactly one phase0 cut occurs in q+1:
100100001001000010000101, length24, at visible index51 (physical102).
q+0 contains no listed cut. q74=0/1 gives left149=1/0, while the
17 whites at132..148 and all earlier depths agree, independent of odd
raw samples. Thus this cut forces black149 for every real realization
of q if the clock extends through149; root uniqueness remains open.
The fixture header parser was corrected before the lookup (the phase
number is followed by counts, rather than being its final token).
Finite controls COMPUTED; Implication for every realization, tier2 carrying step:
the certified phase0 cut applies after rebase at physical102.
Input digests: RT dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e;
MFW44 80eee0a74712632a4339f7cd0a7776f23dd2a45fea8e934b79e6f0aba390d378.
"""
from hashlib import sha256
from pathlib import Path
import re

from rule30_local_record_traces import blocks, OUT
from rule30_SS_record_residence import decode

HERE = Path(__file__).resolve().parent
RT_DIGEST = 'dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e'
MFW_DIGEST = '80eee0a74712632a4339f7cd0a7776f23dd2a45fea8e934b79e6f0aba390d378'
CUT = '100100001001000010000101'


def main():
    assert sha256(Path(OUT).read_bytes()).hexdigest() == RT_DIGEST
    path = HERE / 'rule30_local_mfw44.txt'
    assert sha256(path.read_bytes()).hexdigest() == MFW_DIGEST
    phase, words = None, []
    for line in path.read_text().splitlines():
        m = re.match(r'## phase ([01]):', line)
        if m:
            phase = int(m[1])
        elif phase == 0 and line and set(line) <= {'0', '1'}:
            words.append(line)
    assert len(words) == len(set(words)) == 1130
    b = next(b for b in blocks(OUT) if b[0] == 132)
    assert b[:5] == (132, 17, 0, 148, 'exact')
    q = b[6]
    assert len(q) == 74 and q[51:] == CUT[:-1] and len(CUT) == 24
    assert (2*51) % 2 == 0
    for bit in '01':
        word = q+bit
        hits = [(f, word.find(f)) for f in words if f in word]
        suffix = [(f, len(word)-len(f)) for f in words if word.endswith(f)]
        assert hits == suffix
        assert hits == ([] if bit == '0' else [(CUT, 51)])
    rows = []
    for bit in (0, 1):
        same = []
        for odd, terminal in ((0, 0), (0, 1), (1, 0), (1, 1)):
            v = tuple(int(q[t//2]) if t % 2 == 0 else odd for t in range(148))
            left, _ = decode(v+(bit, terminal), 0)
            assert left[132:149] == [0]*17 and left[149] == 1-bit
            same.append(left)
        assert all(left == same[0] for left in same)
        rows.append(same[0])
    assert rows[0][:149] == rows[1][:149]
    print('q+1: one certified24 cut at visible51, physical102; q+0: no cut PASS')
    print('Eight inverse controls: left149=1-q74, earlier prefix unchanged PASS')
    print('Phase0 physical rebase102 is white despite odd visible index51 PASS')


if __name__ == '__main__':
    main()
