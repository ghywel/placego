#!/usr/bin/env python3
"""rule30_frames.py: the owner's temporal compass (2026-10-06, via GPT's G083): motion followed along a structure, not
only change at a fixed cell. Where is Rule 30 random when the observer moves? The single-cell pattern is read along
41 moving frames, x_t(floor(v t)) for v = k/20, k = -20..20, and each frame gets the linear-complexity profile of
rule30_linear_complexity.py (fair-coin tests) plus its density and its frame difference s(t) XOR s(t+1) (the
moving-frame velocity; at v = 0 it is the fixed-cell velocity, Rule 210, section 8.70).

RUN-ON:     cpu (frames.c and linear_complexity.c via cc, Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_frames.py [LOGN=20] [JOBS=10]
            python3 tests/probes/lexicon/rule30_frames.py --instrument     (F0 and F1 only, at N = 4096)
COST:       about two minutes on ten cores at LOGN = 20.

Known before this run. The diagonals near both edges form closed systems: the right diagonal R_k(t) = x(t-k, t)
obeys R_k(t) = R_k(t-1) XOR (R_(k-1)(t-1) OR R_(k-2)(t-1)) (an accumulator: Jen's periods 2^alpha), and the left
diagonal D_k(t) = x(k-t, t) obeys D_k(t+1) = D_(k-2)(t) XOR (D_(k-1)(t) OR D_k(t)) (section 8.66: some are eventually
white). The triangle census put the uniform core right of x/t = -0.24 and the band's settled edge at -0.254 (section
8.68). Linear complexity is blind to bias alone: a biased but independent sequence still has L close to N/2, so the
density and the frame difference are reported beside it.

PREDICTIONS, written 2026-10-06 before this script's first run (only the instrument checks F0 and F1 were run, at
N = 4096, as --instrument):
  F0 (instrument, exact): the v = 0 frame equals tilt.c's centre column, bit for bit.
  F1 (instrument, exact): the frames v = -1 and v = 1 (the light-cone edges) are all black, so L = 1.
  MF1 (blind; the core is coin-like in every frame): for every k = -4..16 (v = -0.2 .. 0.8) at N = 2^LOGN:
      L_N - N/2 in [-13, 13.5], the jump count within N/4 +- 4 sqrt(N/8), the jump-height chi-square p > 0.001, and
      |z| < 4 for the density and for the frame difference.
  MF2 (blind; the left band is not): the frames v = -0.5 and v = -0.75 each fail at least one of: L_N / N >= 0.49,
      chi-square p >= 1e-6, |z(density)| <= 6, |z(frame difference)| <= 6.
  MF3 (blind, weakly held; near the right edge): the frame v = 0.95 fails at least one of the same four.
  D1 (descriptive): the table for all 41 frames; the speeds where the coin-like range begins and ends.
"""
import math
import os
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rule30_linear_complexity import run_bm, stats, TILT  # noqa: E402  (builds linear_complexity.c and tilt.c)

FR = os.path.join(tempfile.gettempdir(), 'rule30_frames')
subprocess.run(['cc', '-O3', '-o', FR, os.path.join(HERE, 'frames.c')], check=True)
K = 20


def frames(N):
    out = subprocess.run([FR, str(N), str(K)], capture_output=True, check=True).stdout.split(b'\n')
    res = {}
    for line in out:
        if line:
            k, bits = line.split(b' ')
            res[int(k)] = bits
    return res


def z(ones, n):
    return (ones - n / 2) / math.sqrt(n / 4)


def instrument(N=4096):
    fr = frames(N)
    col = subprocess.run([TILT, str(N), '0'], capture_output=True, check=True).stdout
    f0 = fr[0] == col
    f1 = fr[-K] == b'1' * N and fr[K] == b'1' * N and run_bm(fr[K])[2] == 1
    print('F0', 'PASS' if f0 else 'FAIL', '(v = 0 frame = tilt.c centre column, %d bits)' % N)
    print('F1', 'PASS' if f1 else 'FAIL', '(edges all black, L = 1)')
    return f0 and f1


def main():
    if not instrument():
        sys.exit(1)
    if '--instrument' in sys.argv:
        return
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    logn = int(args[0]) if args else 20
    jobs = int(args[1]) if len(args) > 1 else 10
    N = 1 << logn
    fr = frames(N)
    with ThreadPoolExecutor(jobs) as ex:
        futs = {k: ex.submit(run_bm, fr[k]) for k in fr}
        res = {k: stats(*f.result()) for k, f in futs.items()}
    sd = math.sqrt(N / 8)
    print('N = 2^%d; frames x_t(floor(k t / %d))' % (logn, K))
    print('%4s %6s %9s %8s %9s %5s %10s %9s %8s %8s' % ('k', 'v', 'jumps', 'chi2', 'p', 'hmax', 'L_N', 'L_N/N',
                                                    'z(dens)', 'z(diff)'))
    coin = {}
    for k in sorted(fr):
        s, r = fr[k], res[k]
        zd = z(s.count(b'1'), N)
        diff = sum(1 for a, b in zip(s, s[1:]) if a != b)
        zf = z(diff, N - 1)
        r['zd'], r['zf'] = zd, zf
        coin[k] = (-13 <= r['dev'] <= 13.5 and abs(r['K'] - N / 4) <= 4 * sd and r['p'] > 0.001 and abs(zd) < 4
                   and abs(zf) < 4)
        print('%4d %6.2f %9d %8.1f %9.2g %5d %10d %9.4f %8.1f %8.1f %s' % (k, k / K, r['K'], r['chi'], r['p'], r['hmax'],
                                                                     r['LN'], r['LN'] / N, zd, zf,
                                                                     'coin' if coin[k] else ''))

    def notcoin(k):
        r = res[k]
        return r['LN'] / N < 0.49 or r['p'] < 1e-6 or abs(r['zd']) > 6 or abs(r['zf']) > 6

    mf1 = all(coin[k] for k in range(-4, 17))
    print('MF1', 'HELD' if mf1 else 'REFUTED', [k for k in range(-4, 17) if not coin[k]])
    print('MF2', 'HELD' if notcoin(-10) and notcoin(-15) else 'REFUTED', (notcoin(-10), notcoin(-15)))
    print('MF3', 'HELD' if notcoin(19) else 'REFUTED')
    ks = [k for k in sorted(fr) if coin[k]]
    print('D1 coin-like frames: k =', ks)


if __name__ == '__main__':
    main()
