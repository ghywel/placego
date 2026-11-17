"""G72 FM1–FM2; preregistered at efce02c. Bounded exact controls."""
from collections import defaultdict
from itertools import product
import sys
from collatz_gpt_actual_ceiling import specification
from collatz_gpt_barrier_offset import extremal, intercept
from collatz_gpt_boundary_loss import admissible


def direct(n, m):
    q, a = n, 0
    bits = []
    stays = True
    for t in range(1, m+1):
        b = q % 2
        bits.append(b)
        a += b
        q = (3*q+1)//2 if b else q//2
        stays &= 3**a >= 2**t
    return tuple(bits), a, q, stays


def future_from_start(n, m):
    q, a, stays = n, 0, True
    statuses = []
    for t in range(1, m+9):
        b = q % 2
        a += b
        q = (3*q+1)//2 if b else q//2
        stays &= 3**a >= 2**t
        if t >= m:
            statuses.append(stays)
    return tuple(statuses)


def future_from_terminal(y, a, m):
    statuses = [True]
    stays = True
    for d in range(1, 9):
        b = y % 2
        a += b
        y = (3*y+1)//2 if b else y//2
        stays &= 3**a >= 2**(m+d)
        statuses.append(stays)
    return tuple(statuses)


def limit(a):
    A = 3**a
    _, maximum = extremal(a)
    return 1+(maximum-(A-2**a))//A


def main():
    starts = terminal_values = future_checks = weighted_checks = 0
    collisions = []
    for m in range(1, 13):
        expected = {}
        for word in product((0, 1), repeat=m):
            if admissible(word):
                r, _ = specification(word)
                a = sum(word)
                A = 3**a
                B = intercept(word)
                _, maximum = extremal(a)
                assert A-2**a <= B <= maximum
                y = A+(A*r+B)//2**m
                expected[2**m+r] = (a, y)
        actual = {}
        fibres = defaultdict(list)
        for n in range(2**m, 2**(m+1)):
            _, a, y, stays = direct(n, m)
            if stays:
                actual[n] = (a, y)
                assert 3**a <= y < 2*3**a
                fibres[y].append(n)
        assert actual == expected
        starts += len(actual)
        terminal_values += len(fibres)
        by_start = {}
        by_terminal = {}
        for y, group in fibres.items():
            labels = {actual[n][0] for n in group}
            assert len(labels) == 1
            a = labels.pop()
            assert len(group) <= limit(a) <= 1+a//3
            if len(group) > 1:
                collisions.append((m, a, y, group))
            prediction = future_from_terminal(y, a, m)
            by_terminal[y] = prediction
            for n in group:
                observed = future_from_start(n, m)
                assert observed == prediction
                by_start[n] = observed
                future_checks += 9
        for d in range(9):
            direct_count = sum(row[d] for row in by_start.values())
            weighted = sum(len(group)*by_terminal[y][d] for y, group in fibres.items())
            assert direct_count == weighted
            weighted_checks += 1
    print(f'FM1: {starts} admitted starts/{terminal_values} terminal values; '
          'independent word/trajectory maps, labels and fibre bounds pass')
    print('All non-singleton fibres (m,a,y,starts):', collisions)
    print(f'FM2: {future_checks} future-status checks/{weighted_checks} '
          'weighted selected-terminal counts pass')
    guard = [direct(n, 6) for n in (85, 84, 80)]
    assert all(a == 1 and y == 4 and not stays for _, a, y, stays in guard)
    assert len(guard) == 3 > limit(1) == 1
    print('CF: unrestricted three-start fibre at m6,a1,y4 refutes dropping admission')


def short_labels():
    """FM3, separately preregistered at fc268ed; no larger population."""
    starts = fibres_checked = modulus_one = 0
    for m in range(1, 13):
        s = 0
        while 3*2**s < m:
            s += 1
        fibres = defaultdict(list)
        low_labels = set()
        parity_labels = set()
        for n in range(2**m, 2**(m+1)):
            bits, a, y, stays = direct(n, m)
            if not stays:
                continue
            assert n % 2 == 1
            fibres[y].append((n, a))
            low_labels.add((y, n % 2**s))
            parity_labels.add((y, bits[:s]))
            starts += 1
            modulus_one += s == 0
        N = sum(map(len, fibres.values()))
        assert len(low_labels) == len(parity_labels) == N
        for y, group in fibres.items():
            a = group[0][1]
            assert all(label == a for _, label in group)
            A = 3**a
            _, maximum = extremal(a)
            sharp = 1+(maximum-(A-2**a))//(2*A)
            span = max(n for n, _ in group)-min(n for n, _ in group)
            assert len(group) <= sharp <= (a+5)//6
            assert 3*span < a
            fibres_checked += 1
    print(f'FM3: {starts} starts/{fibres_checked} fibres; sharp multiplicity, '
          'span and both injective labels pass')
    print('Modulus1 admitted-start checks:', modulus_one)
    guards = [direct(n, 9) for n in (625, 597)]
    assert all(a == 2 and y == 11 and not stays for _, a, y, stays in guards)
    assert 625 % 4 == 597 % 4 == 1
    assert guards[0][0][:2] == guards[1][0][:2] == (1, 0)
    expected = [(625, 938, 469, 704, 352, 176, 88, 44, 22, 11),
                (597, 896, 448, 224, 112, 56, 28, 14, 7, 11)]
    for row in expected:
        for q, following in zip(row, row[1:]):
            assert following == ((3*q+1)//2 if q % 2 else q//2)
    assert 3*abs(625-597) >= 9
    print('CF: unrestricted odd starts625/597 share both short labels; '
          'admission and span fail as predicted')


if __name__ == '__main__':
    short_labels() if '--short-labels' in sys.argv else main()
