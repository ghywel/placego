"""G44 IB1/IB2: exact parity-tail variation and finite-ensemble injection."""
from collections import Counter
from fractions import Fraction


def word(n, d):
    label = 0
    for j in range(d):
        b = n % 2
        label |= b << j
        n = (3*n+1)//2 if b else n//2
    return label


def main():
    checks = injections = 0
    for a in range(1, 6):
        M = 3**a
        for d in range(1, 10):
            B = 2**d
            perm = [word(n, d) for n in range(B)]
            assert len(set(perm)) == B
            labels = [word(M+q, d) for q in range(M)]
            assert labels == [perm[(M+q) % B] for q in range(M)]
            counts = Counter(labels)
            tv = sum(abs(Fraction(counts.get(v, 0), M)-Fraction(1, B)) for v in range(B))/2
            r = M % B
            assert tv == Fraction(r*(B-r), B*M)
            if B >= M:
                assert len(counts) == M and set(counts.values()) == {1}
                assert tv == 1-Fraction(M, B)
                injections += 1
            checks += 1
        for d in (12, 16):
            label = word(M, d)
            mass = Fraction(sum(word(M+q, d) == label for q in range(M)), M)
            assert mass == Fraction(1, M)
            assert mass > Fraction(1, 2**d)
    print(f'IB1: {checks} exact TV/parity-bijection checks; {injections} injected ensembles')
    print('Unexpected IB2: 10 actual-prefix cylinders retain mass1/M at d12,d16')
    print('ALL CHECKS PASS; no contradiction to the special stopping-time count')


if __name__ == '__main__':
    main()
