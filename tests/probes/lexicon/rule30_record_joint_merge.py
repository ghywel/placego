"""GC1160: a finite causal merge certificate for Local's two actual142 roots.

Predictions BEFORE computation: G12/G13 backward pair agreement certifies
the joint changes at visible8/9 using only the existing79-bit prefix (P1,
0.6). Counterfactual: saved record-band agreement need not be whole-tail
agreement; a failed prefix certificate means UNKNOWN, not nonmerger.
Unexpected: test each individual algebraic flip separately, without claiming
those intermediate words real. Independent literal Wolfram inversion versus
XOR/OR; complete finite differences versus the common-future pair criterion.
Record searched: two.*(bit|input|defect)|swap|shift.*pulse|142 with
coalesc|shield|finite.*influence|annihila|reset ->84 hits27 files.
G12 terminal agreement, G13.3, G25 and GC1158 read. G149 concerns eventual
finite support under temporal shifts, not equal deep images of these roots.
No solver, language membership, record census or affine approximation.

OUTCOME 2026-10-11 17:55 BST: P1 HELD. The listed20 pair certificates use
inputs only through physical117 (59 visible bits). For every common
continuation, all temporal columns X_j agree at every j>=117; the entire
inverse pair h^k agrees at k>=118. This threshold is sharp: X_116(0)
differs. Each individual algebraic flip merges earlier (h94, h92), so
their joint effect is not an additive combination. Both controls pass.
Adaptive check registered BEFORE running: truncate to59 visible bits,
recheck the same table, then append each of the four next-two-white-bit
choices to BOTH roots. Every common continuation must preserve the table.
The four checks support the instrument; all-continuation scope is the
backward induction, not the four tests. No all-depth record bound follows.
"""
from hashlib import sha256
from itertools import product
from pathlib import Path

from rule30_local_record_traces import blocks, OUT

TABLE = (0, 1, 1, 1, 1, 0, 0, 0)
NEW = '0010100001000101010101010101010101000100001010101010101010100010000101000010100'
# (time t, first common depth C_t, common X_C(t), common X_(C+1)(t)).
# Future at t20 is common everywhere; every row satisfies C_t+1>=C_(t+1).
CERT = ((19, 3, 1, 0), (18, 7, 1, 0), (17, 6, 0, 1),
        (16, 6, 1, 1), (15, 11, 1, 0), (14, 16, 1, 1),
        (13, 29, 1, 0), (12, 37, 1, 0), (11, 41, 1, 0),
        (10, 56, 1, 1), (9, 63, 1, 0), (8, 67, 1, 1),
        (7, 66, 0, 1), (6, 69, 1, 1), (5, 74, 1, 1),
        (4, 96, 1, 0), (3, 104, 1, 1), (2, 103, 0, 1),
        (1, 104, 1, 0), (0, 117, 1, 1))


def grid(word, literal=False):
    """Finite exact inverse triangle, phase1; no padding of white inputs."""
    n = 2*len(word)+1
    root = [int(word[(t-1)//2]) if t % 2 else 0 for t in range(n)]
    cols = {-1: root, 0: [(1+t) % 2 for t in range(n)]}
    for j in range(1, n):
        u, v = cols[j-1], cols[j-2]
        if literal:
            cols[j] = [next(a for a in (0, 1)
                            if TABLE[4*a+2*u[t]+v[t]] == u[t+1])
                       for t in range(len(u)-1)]
        else:
            cols[j] = [u[t+1] ^ (u[t] | v[t]) for t in range(len(u)-1)]
    return cols


def verify(a, b, cert=CERT):
    future = 0
    assert [t for t, _, _, _ in cert] == list(range(19, -1, -1))
    for t, c, x, y in cert:
        assert c+1 >= future
        assert (a[c][t], a[c+1][t]) == (b[c][t], b[c+1][t]) == (x, y)
        # Finite control; the theorem's tail uses the common-future induction.
        assert all(a[j][t] == b[j][t]
                   for j in range(c, len(a)-1) if t < len(a[j]))
        future = c
    return max(t+c for t, c, _, _ in cert)


def discover(a, b):
    """Same fixed original prefix cap, for the two individual controls."""
    future, cert = 0, []
    for t in range(19, -1, -1):
        for j in range(max(1, future), len(a)-1-t):
            if (a[j-1][t], a[j][t]) == (b[j-1][t], b[j][t]):
                cert.append((t, j-1, a[j-1][t], a[j][t]))
                future = j-1
                break
        else:
            return None
    verify(a, b, cert)
    return cert


def main():
    assert sha256(Path(OUT).read_bytes()).hexdigest() == (
        'dea50d7a8c9b0437491ced1b035daeb3df6d0693c605f2e315a589e90bd2413e')
    q = next(b[6] for b in blocks(OUT) if b[0] == 142 and b[2] == 1)
    assert len(q) == len(NEW) == 79
    assert [i for i in range(79) if q[i] != NEW[i]] == [8, 9]
    a, b = grid(q), grid(NEW)
    assert a == grid(q, True) and b == grid(NEW, True)
    assert verify(a, b) == 117
    assert a[116][0] != b[116][0]
    for w in (q[:59], NEW[:59]):
        assert grid(w) == grid(w, True)
    assert verify(grid(q[:59]), grid(NEW[:59])) == 117
    for tail in product('01', repeat=2):
        qa, qb = q[:59]+''.join(tail), NEW[:59]+''.join(tail)
        aa, bb = grid(qa), grid(qb)
        assert aa == grid(qa, True) and bb == grid(qb, True)
        assert verify(aa, bb) == 117
    print('20-row certificate; maximum used physical input117; 59-bit truncation and4 tails PASS')
    for i, expected in ((8, 94), (9, 92)):
        w = q[:i]+str(1-int(q[i]))+q[i+1:]
        z = grid(w)
        assert z == grid(w, True)
        cert = discover(a, z)
        assert cert is not None
        threshold = 1+max(c for _, c, _, _ in cert)
        assert threshold == expected
        assert a[threshold-2][0] != z[threshold-2][0]
        assert a[116][0] == z[116][0]
        print('Individual algebraic flip', i, 'pair merge at', threshold, 'PASS')
    print('Joint pair merge sharp at118; joint nonadditivity at X116(0) PASS')


if __name__ == '__main__':
    main()
