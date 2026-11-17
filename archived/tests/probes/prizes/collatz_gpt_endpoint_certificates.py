"""G68 EC1–EC2, preregistered at cd53b87; bounded exact controls."""
from collections import Counter
from itertools import product
import json
import sys
from collatz_gpt_actual_ceiling import specification, trajectory
from collatz_gpt_barrier_offset import extremal, intercept
from collatz_gpt_first_deficit_gap import first_deficit, terminal


def positive(rho, modulus):
    return rho if rho else modulus


def bounds(word):
    binary = []
    ternary = []
    for length in range(len(word)+1):
        prefix = word[:length]
        M = 2**length
        rho = (-intercept(prefix)*pow(3**sum(prefix), -1, M)) % M
        binary.append(positive(rho, M))
        suffix = word[len(word)-length:] if length else ()
        A = 3**sum(suffix)
        rho = (intercept(suffix)*pow(2**length, -1, A)) % A
        ternary.append(positive(rho, A))
    return binary, ternary


def main():
    words = count_checks = congruences = survivors = 0
    for t in range(1, 17):
        for word in product((0, 1), repeat=t):
            if not first_deficit(word):
                continue
            words += 1
            a = sum(word)
            M, A = 2**t, 3**a
            r, K = specification(word)
            y = terminal(r, word)
            assert 0 <= y < A and M*y == A*r+intercept(word)
            m0 = int(r == 0)
            start_count = max(0, (K-r)//M-m0+1)
            terminal_count = max(0, (K-y)//A-m0+1)
            assert start_count == terminal_count
            count_checks += 1
            for m in range(m0, m0+start_count):
                n = r+M*m
                assert trajectory(n, t) == (word, True)
                assert terminal(n, word) == y+A*m
                survivors += 1
            if not a:
                assert start_count == 0
                continue
            binary, ternary = bounds(word)
            assert binary[-1] == r and ternary[-1] == y
            assert binary == sorted(binary) and ternary == sorted(ternary)
            for length, (lb, lt) in enumerate(zip(binary, ternary)):
                prefix_mod = 2**length
                suffix = word[t-length:] if length else ()
                suffix_mod = 3**sum(suffix)
                assert r % prefix_mod == lb % prefix_mod
                assert y % suffix_mod == lt % suffix_mod
                if lb > K or lt > K:
                    assert start_count == 0
                congruences += 2
            assert (r > K) == (start_count == 0) == (y > K)
    print(f'EC1: {words} words/{count_checks} equal lift counts/'
          f'{survivors} directly checked positive survivors')
    print(f'EC2: {congruences} endpoint congruences; nesting, soundness '
          'and full-length completeness pass')

    records = []
    for a in range(1, 257):
        word, _ = extremal(a)
        _, K = specification(word)
        binary, ternary = bounds(word)
        s = next((i for i, lb in enumerate(binary) if lb > K), None)
        ell = next((i for i, lt in enumerate(ternary) if lt > K), None)
        assert (s is None and ell is None) == (a == 1)
        assert a == 1 or (s is not None and ell is not None)
        records.append(dict(a=a, t=len(word), K=K, prefix=s,
                            suffix=ell, suffix_ones=(sum(word[-ell:])
                                                    if ell else 0)))
    print('Extremizers: both certificates for a2..256; neither for a1')
    print('Minimal prefix lengths:', sorted(Counter(r['prefix'] for r in records[1:]).items()))
    print('Minimal suffix lengths:', sorted(Counter(r['suffix'] for r in records[1:]).items()))
    word = tuple(map(int, '1101100'))
    r, K = specification(word)
    binary, ternary = bounds(word)
    assert binary[1] == ternary[2] == K == 1 and r > K
    assert trajectory(r, len(word)) == (word, False)
    print('CF: passing prefix1/suffix00 tests does not imply survival')
    if len(sys.argv) > 1:
        with open(sys.argv[1], 'w') as f:
            json.dump(records, f, indent=2)


if __name__ == '__main__':
    main()
