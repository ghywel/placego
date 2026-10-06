"""G40 PC1/PC2: exact skeleton cubes and direct-residue Fourier controls."""
from collections import defaultdict
from cmath import exp
from math import pi


def direct(r, T):
    word = []
    q = r
    a = 0
    valid = True
    for t in range(1, T+1):
        b = q % 2
        word.append(b)
        a += b
        q = (3*q+1)//2 if b else q//2
        valid &= 3**a > 2**t
    return tuple(word), q, valid


def skeleton(w):
    return tuple('M' if w[t] != w[t+1] else str(w[t])*2
                 for t in range(0, len(w)-1, 2)) + ((str(w[-1]),) if len(w)%2 else ())


def phase(h, q, M):
    return exp(2j*pi*((h*q)%M)/M)


def main():
    cubes = flips = fouriers = 0
    worst = 0.0
    for T in range(1, 11):
        groups = defaultdict(dict)
        for r in range(2**T):
            w, q, valid = direct(r, T)
            if valid:
                assert 0 <= q < 3**sum(w)
                groups[skeleton(w)][w] = q
        for words in groups.values():
            base = max(words)  # Every mixed pair oriented10.
            a = sum(base)
            M = 3**a
            free = []
            for t in range(0, T-1, 2):
                if base[t] != base[t+1]:
                    assert base[t:t+2] == (1, 0)
                    s = sum(base[:t])
                    if 3**s > 2**(t+1):
                        free.append((t, (3**(a-s-1)*pow(2, -(T-t), M)) % M))
            assert len(words) == 2**len(free)
            cubes += 1
            for w, q in words.items():
                predicted = words[base]
                for t, delta in free:
                    if w[t:t+2] == (0, 1):
                        predicted += delta
                    v = w[:t]+(1-w[t], 1-w[t+1])+w[t+2:]
                    assert v in words
                    sign = 1 if w[t:t+2] == (1, 0) else -1
                    assert (words[v]-q) % M == (sign*delta) % M
                    flips += 1
                assert q % M == predicted % M
            for h in range(min(M, 8)):
                observed = sum(phase(h, q, M) for q in words.values())/len(words)
                expected = phase(h, words[base], M)
                for _, delta in free:
                    expected *= (1+phase(h, delta, M))/2
                error = abs(observed-expected)
                worst = max(worst, error)
                assert error < 1e-9
                fouriers += 1
        allones = next(words for words in groups.values() if (1,)*T in words)
        assert len(allones) == 1
        assert abs(abs(phase(1, allones[(1,)*T], 3**T))-1) < 1e-12
    print(f'PC1: {cubes} skeleton cubes; {flips} exact flips; {fouriers} Fourier identities')
    print(f'max complex residual {worst:.3g}; tolerance1e-9')
    print('Unexpected PC2: all-one endpoints have unit Fourier modulus through T10')
    print('ALL CHECKS PASS; no aggregate Fourier decay inferred')


if __name__ == '__main__':
    main()
