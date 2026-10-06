"""G43 BF1-BF3: parity-reader spectrum and weighted reconstruction."""
from cmath import exp
from collections import defaultdict
from fractions import Fraction
from math import cos, pi
from collatz_gpt_pair_cancellation import direct, phase


def reader(h, M):
    return 2/(M*(1+exp(-2j*pi*h/M)))


def main():
    spectra = inversions = histograms = 0
    worst = 0.0
    for a in range(1, 6):
        M = 3**a
        hats = [reader(h, M) for h in range(M)]
        for h in range(M):
            observed = sum((-1)**q*phase(-h, q, M) for q in range(M))/M
            error = abs(observed-hats[h])
            worst = max(worst, error)
            assert error < 1e-9
            spectra += 1
        for q in range(M):
            observed = sum(hats[h]*phase(h, q, M) for h in range(M))
            error = abs(observed-(-1)**q)
            worst = max(worst, error)
            assert error < 1e-9
            inversions += 1
        assert Fraction(sum((-1)**q for q in range(M)), M) == Fraction(1, M)
        # Unequal unit-frequency weights, contrasting with constant importance.
        if M >= 9:
            assert abs(hats[(M-1)//2]) > abs(hats[1])
    for T in range(1, 9):
        groups = defaultdict(list)
        for r in range(2**T):
            w, q, valid = direct(r, T)
            if valid:
                groups[sum(w)].append(q)
        for a, qs in groups.items():
            M = 3**a
            direct_mean = sum((-1)**q for q in qs)/len(qs)
            reconstructed = sum(reader(h, M)*sum(phase(h, q, M) for q in qs)/len(qs)
                                for h in range(M))
            error = abs(reconstructed-direct_mean)
            worst = max(worst, error)
            assert error < 1e-9
            histograms += 1
    for n in range(33):
        M, h = 3**(4+3*n), 2**(4+4*n)
        assert 3*h < M
        assert cos(pi*float(Fraction(h, M))) > 0.5
    print(f'BF1: {spectra} spectrum and {inversions} inversion checks, a1..5')
    print(f'BF2: {histograms} direct survivor histograms reconstructed, T1..8')
    print(f'max complex residual {worst:.3g}, tolerance1e-9')
    print('Unexpected BF3: exact uniform parity bias1/M; unit frequency weights unequal')
    print('G42 resonance weight<=2/M: 33 finite controls plus analytic geometric-ratio proof')
    print('ALL CHECKS PASS; next-bit reader only, no tail-count bound')


if __name__ == '__main__':
    main()
