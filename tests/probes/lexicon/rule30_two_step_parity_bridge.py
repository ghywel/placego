"""GC1093: the second-image intersection of the two white parities.

Missing inference: GC1092 covers an odd-periodic immediate successor,
not an odd-periodic slice reached two ticks later. This finite hidden
graph supplies the second-slice bridge; arbitrary earlier times remain
open. Record searched: white.parity|alternating.white|checkerboard.white
with ancestor|earlier|period|collapse ->18 hits in5 files; parity.image|
phase.intersection|white.parity with two.step|second.update|intersection
->0 hits. G122/G124, G152, GC1092 and strategy D2/D3 read.

Predictions preceded each stage. P1/P2 named spatial14/10 ancestry
controls pass (160 white-parity starts, no nonzero odd-period merger).
P3 REFUTED: the intersection is single-black period3, not the linear
two-black period3 family. P4: x parity-white on[a-2,b+2], F^2(x) odd-q
periodic on[a,b], b-a>=q+14 imply F^4(x) white on[a+3,b-q-11]. HELD
by the hand16-state table and independent finite controls. Even-q
checkerboard must fail extinction; the nonzero cycle is the unexpected
P3 countercontrol. No solver, CUT, visible-period search or record run.
Initial temporary ancestry control hit an IndexError on short cycles
before verdicts; padding fixed it, update crosschecks retained.
"""
from itertools import product

from rule30_forced_odd_period_bridge import evolve, scalar


# State (a,b,d,e) remembers consecutive free bits of both origins.
# Labels are the common two output cells. Full table, not a learned cut.
TABLE = {
    '0000': (('0000', '00'),),
    '0001': (('0010', '00'), ('0011', '00')),
    '0010': (('0101', '01'),),
    '0011': (), '0100': (), '0101': (),
    '0110': (('1000', '10'), ('1100', '10')),
    '0111': (('1010', '10'), ('1011', '10'),
             ('1110', '10'), ('1111', '10')),
    '1000': (('0100', '00'),),
    '1001': (('0110', '00'), ('0111', '00')),
    '1010': (('0001', '01'),),
    '1011': (), '1100': (), '1101': (),
    '1110': (('1001', '01'), ('1101', '01')),
    '1111': (),
}
RECURRENT = {('0000', '0000'), ('0111', '1110'),
             ('1110', '1001'), ('1001', '0111')}


def word(bits):
    return ''.join(map(str, bits))


def graph_check():
    derived = {s: [] for s in TABLE}
    packets = 0
    for a, b, c, d, e, f in product((0, 1), repeat=6):
        left = ((1-a) & b, a ^ ((1-b) & c))
        right = (d ^ ((1-e) & f), (1-e) & f)
        # Separate literal cone evaluations, retaining their two outputs.
        assert scalar(scalar((0, a, 0, b, 0, c))) == left
        assert scalar(scalar((d, 0, e, 0, f, 0))) == right
        if left == right:
            derived[word((a, b, d, e))].append(
                (word((b, c, e, f)), word(left)))
        packets += 1
    assert all(tuple(sorted(derived[s])) == TABLE[s] for s in TABLE)
    # Every nonrecurrent edge enters an acyclic part and never returns.
    targets = {t for s, choices in TABLE.items() for t, _ in choices
               if (s, t) not in RECURRENT}
    assert not targets & {s for s, _ in RECURRENT}

    def remaining(s):
        return max((1+remaining(t) for t, _ in TABLE[s]
                    if (s, t) not in RECURRENT), default=0)

    assert max(remaining(s) for s in TABLE) == 4
    paths = 0

    def walk(s, length, first=None):
        nonlocal paths
        if not length:
            assert first in RECURRENT
            paths += 1
            return
        for t, _ in TABLE[s]:
            walk(t, length-1, first if first is not None else (s, t))

    for s in TABLE:
        walk(s, 5)
    # 100100 is the nonzero second-image cycle, not a linear XOR pattern.
    singleton = (1, 0, 0)*10
    assert singleton[0] != (singleton[-1] ^ singleton[1])
    assert not any(evolve(singleton, 2)[2])
    return packets, paths


def ring(row):
    n = len(row)
    literal = tuple(row[(i-1) % n] ^ (row[i] | row[(i+1) % n])
                    for i in range(n))
    v = sum(b << i for i, b in enumerate(row))
    mask = (1 << n)-1
    left = ((v << 1) | (v >> (n-1))) & mask
    right = (v >> 1) | ((v & 1) << (n-1))
    packed = left ^ (v | right)
    assert literal == tuple((packed >> i) & 1 for i in range(n))
    return literal


def named_ancestry_controls():
    count = 0
    for q in (7, 5):
        for z in product((0, 1), repeat=q):
            x = tuple(b for a in z for b in (0, a))
            rows, seen = [], {}
            while x not in seen:
                seen[x] = len(rows)
                rows.append(x)
                x = ring(x)
            recurrent = rows[seen[x]]
            for y in rows:
                if y[:q] == y[q:]:
                    assert not any(recurrent)
            while len(rows) <= 5:
                rows.append(ring(rows[-1]))
            if rows[2][:q] == rows[2][q:]:
                assert not any(rows[5])
            count += 1
    return count


def finite_controls():
    fixtures = rejected = 0
    for q in (1, 3, 5, 7, 9):
        a, b = 10, 10+q+22
        width = b+12
        for white in (0, 1):
            for z in ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0)):
                for exterior in product((0, 1), repeat=4):
                    x = tuple(0 if i % 2 == white else z[(i//2) % 3]
                              for i in range(width))
                    x = exterior + x[4:-4] + tuple(1-v for v in exterior)
                    rows = evolve(x, 4)
                    w = rows[2]
                    if not all(w[i-2] == w[i+q-2]
                               for i in range(a, b-q+1)):
                        rejected += 1
                        continue
                    assert all(x[i] == 0 for i in range(a-2, b+3)
                               if i % 2 == white)
                    assert all(rows[4][i-4] == 0
                               for i in range(a+3, b-q-10))
                    fixtures += 1
    assert evolve((1, 0)*30, 4)[4] == (1, 0)*26
    return fixtures, rejected


def main():
    packets, paths = graph_check()
    ancestry = named_ancestry_controls()
    fixtures, rejected = finite_controls()
    print(dict(hidden_packets=packets, graph_edges=16,
               recurrent_edges=4, five_edge_paths=paths,
               maximum_exit_length=4, named_ancestry_starts=ancestry,
               finite_fixtures=fixtures, rejected_premises=rejected,
               linear_P3='REFUTED and retained',
               second_slice_bridge='ALL odd q PROOF-SKETCH',
               arbitrary_earlier_slices='OPEN', prize_bound='OPEN'))


if __name__ == '__main__':
    main()
