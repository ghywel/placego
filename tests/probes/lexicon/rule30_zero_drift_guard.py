#!/usr/bin/env python3
"""GC1016: actual seven-ring refutes uncorrected three-depth zero-prefix drift.
Prediction and prior-art search: RULE30-GPT, weighted inverse-column block.
No language scan or solver; all four time origins are retained.
"""
from rule30_two_gap_ring import ROWS
from rule30_rrl_transducer import literal_image


def main():
    tables = []
    for phase in range(4):
        word = tuple(2*int(ROWS[(t+phase) % 4][0])
                     + int(ROWS[(t+phase) % 4][1]) for t in range(30))
        z = []
        for depth in range(10):
            for t, a in enumerate(word):
                assert divmod(a, 2) == (
                    int(ROWS[(t+phase) % 4][(-depth) % 7]),
                    int(ROWS[(t+phase) % 4][(1-depth) % 7]))
            z.append(next(i for i, a in enumerate(word) if a != 0))
            word = literal_image(word)
        assert z[7:10] == z[:3]
        tables.append(z[:7])
    assert tables == [[0, 1, 0, 0, 0, 1, 0], [0]*7,
                      [1, 0, 0, 1, 2, 3, 2], [0, 0, 0, 0, 1, 2, 1]]
    assert tables[2][5] > tables[2][2]+1
    print('PASS: inverse reconstruction and all phase controls; Z(2)=0, Z(5)=3 at time origin2')


if __name__ == '__main__':
    main()
