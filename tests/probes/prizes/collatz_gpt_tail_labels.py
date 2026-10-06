"""G73 AT1–AT2; preregistered at 773b424.
AT1 MUST HOLD: widths2..10, horizons1..24 satisfying t<=3*2^(w-1),
exact bands, odd-count labels, carries, fibre bounds and short labels pass.
AT2 MUST HOLD: direct guard trajectories have odd counts6/5, first deficit2.
CF: without admission a terminal still determines odd count; MUST FAIL.
REFUTED-BY: starts9/13, width4, horizon13, terminal1, counts6/5.
OUTCOME 2026-10-06, GPT Intel Python, under1 s:
AT1 PASS2313 samples/fibres;27 empty ensembles retained, no admitted merges.
AT2 PASS; CF REFUTED. No entropy measurement or large count run.
"""
from collections import defaultdict
from collatz_gpt_barrier_offset import extremal


def main():
    samples = fibres_checked = empty = 0
    collisions = []
    for w in range(2, 11):
        M = 2**(w-1)
        by_time = [defaultdict(list) for _ in range(25)]
        for n in range(M, 2*M):
            y, a, B, stays = n, 0, 0, True
            bits = []
            for t in range(1, 25):
                b = y % 2
                bits.append(b)
                a += b
                B = 3**b*B+b*2**(t-1)
                y = (3*y+1)//2 if b else y//2
                A = 3**a
                stays &= A >= 2**t
                if not stays or t > 3*M:
                    continue
                assert A*M <= 2**t*y < 3*A*M
                assert 2**t*y == A*n+B
                assert n == (2**t*y)//A-B//A
                assert 0 <= B//A <= a//3
                by_time[t][y].append((n, a, tuple(bits)))
                samples += 1
        for t in range(1, min(24, 3*M)+1):
            fibres = by_time[t]
            empty += not fibres
            s = 0
            while 3*2**s < t:
                s += 1
            assert s <= w-1 and s <= t
            low_labels = set()
            parity_labels = set()
            N = 0
            for y, group in fibres.items():
                a = group[0][1]
                assert all(label == a for _, label, _ in group)
                A = 3**a
                _, maximum = extremal(a)
                sharp = 1+(maximum-(A-2**a))//(2*A)
                ns = [n for n, _, _ in group]
                assert 3*(max(ns)-min(ns)) < a
                assert len(group) <= sharp <= (a+5)//6 <= (t+5)//6
                if len(group) > 1:
                    collisions.append((w, t, a, y, ns))
                for n, _, bits in group:
                    low_labels.add((y, n % 2**s))
                    parity_labels.add((y, bits[:s]))
                N += len(group)
                fibres_checked += 1
            assert len(low_labels) == len(parity_labels) == N
    print(f'AT1: {samples} admitted start/horizon samples/{fibres_checked} '
          f'fibres; bands, carry, spans, multiplicities and labels pass; '
          f'{empty} empty ensembles retained')
    print('All non-singleton fibres (w,t,a,y,starts):', collisions)

    rows = []
    expected = [(9, 14, 7, 11, 17, 26, 13, 20, 10, 5, 8, 4, 2, 1),
                (13, 20, 10, 5, 8, 4, 2, 1, 2, 1, 2, 1, 2, 1)]
    for row in expected:
        a = 0
        deficit = None
        for t, (q, following) in enumerate(zip(row, row[1:]), 1):
            b = q % 2
            a += b
            assert following == ((3*q+1)//2 if b else q//2)
            if deficit is None and 3**a < 2**t:
                deficit = t
        rows.append((row[0], row[-1], a, deficit))
    assert rows == [(9, 1, 6, 2), (13, 1, 5, 2)]
    print('AT2 unrestricted guard (start,terminal,odd count,first deficit):', rows)
    print('CF: terminal odd-count identification fails without admission')


if __name__ == '__main__':
    main()
