#!/usr/bin/env python3
"""rule30_linear_complexity.py: the owner's time question (2026-10-06), measured. How simple is the centre column, and
its velocity, acceleration and jerk, as a linear difference equation?

RUN-ON:     cpu (linear_complexity.c and tilt.c via cc, driven from Python 3 with the standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_linear_complexity.py [LOGN=22] [JOBS=10]
            python3 tests/probes/lexicon/rule30_linear_complexity.py --engine     (the engine checks C0, C3 only)
COST:       about three minutes on ten cores at LOGN = 22 (Berlekamp-Massey is quadratic: about 40 s per arm of 2^22
            bits on the M5, fifteen arms; tilt.c about 35 s per CA arm).

The owner (2026-10-06): "do we consider acceleration and jerk ... not just the velocity of the state change but its
acceleration as well." RULE30-PRIZE.md section 8.70: over GF(2) the time derivative of a column x is Delta x = (1 + S) x,
x(t) XOR x(t+1); Rule 30's velocity is Rule 210 (x_{t+1} = x_t XOR R210(x_t), proved); Delta^2 = 1 + S^2 (the
acceleration is the lag-2 difference), Delta^3 = 1 + S + S^2 + S^3 (the jerk), and Delta^(2^k) = 1 + S^(2^k). Problem 1
says the centre column is never eventually periodic, that is, no polynomial P with (S^p - 1) S^m x = 0, a linear
difference equation of order m + p. The linear complexity L_n of the first n bits is the order of the shortest linear
difference equation over GF(2), with any coefficients, that the first n bits satisfy (Berlekamp-Massey finds it). An
eventually periodic column has L_n <= m + p for every n. So the profile L_n is the measurement that covers every
derivative at once.

Known before this run (PRIOR-ART.md section on Meier and Staffelbach; arXiv:1306.3546): Rule 30's centre column passes
linear complexity tests at lengths used for cryptography (L close to n/2). No published profile of the single-cell
column at millions of bits was found (searched 2026-10-06). The theory for fair coins: the jumps of the profile are
the degrees of the partial quotients of the continued fraction of the column's generating function, independent and
geometric, P(h = k) = 2^-k (there are 2^k monic polynomials of degree k, each of probability 2^-2k), so about N/4 jumps
of mean height 2. Before a jump of height h, L_n - n/2 = (1 - h)/2; just after it, h/2. Rueppel (1986): E[L_n] = n/2 +
(4 + (n mod 2))/18 + o(1). (An identity seen while writing this, not a test: the deviation L_n - n/2 averages exactly
1/4 over every segment between jumps, up to boundary terms, for any sequence; so the mean deviation is not reported.)

Two exact facts used as checks (proved here). If the first N bits of x satisfy a recurrence of order L, the N - 1 bits
of Delta x satisfy the same one; and if Delta x satisfies C of order L, x satisfies C(z)(1 + z) of order L + 1. So
L(x^N) - j <= L((Delta^j x)^(N-j)) <= L(x^N): velocity, acceleration and jerk are exactly as complex as the column, to
within their order. Reversal is NOT such an identity (0001 has L = 4, 1000 has L = 1), so the time-reversed column is
a blind arm.

Arms (N = 2^LOGN bits each):
  single:    the centre column from a single black cell (tilt.c mode 0).
  reversed:  the same N bits read backwards in time (the unexpected arm).
  vel, acc, jerk: Delta x, Delta^2 x, Delta^3 x of the single-cell column.
  row:       the centre column of Rule 30 from a row of fair coins (tilt.c mode 1, seed 1; the row comes from xorshift64*).
  coins1..8: SHA-256 in counter mode (seed s, counter i), N bits each: the fair-coin control.
  ring22:    cell 0 of Rule 30 on the ring of 22 cells from a single cell (ring_census.c's rule): eventually periodic,
             period 3,256 from the single cell, transient at most 5,477 (rule30_ring_census.txt).

PREDICTIONS, written 2026-10-06 before this script's first run (no exploratory run; the engine checks C0 and C3 were
run alone before the push, as --engine, and see no arm):
  LC1 (blind; jumps are fair-coin jumps): for single, reversed and row, the number of jumps is within N/4 +- 4 sqrt(N/8)
      (renewal variance of geometric heights), and the height histogram (1..12 and >= 13) fits 2^-k with chi-square
      p > 0.001.
  LC2 (blind; the deepest dip): for single, reversed and row, the highest jump is between 17 and 27 (for N/4 = 2^20
      independent geometric heights, probability about 0.98), so |L_n - n/2| <= 13.5 for every n <= N.
  LC3 (blind; the prize's linear form at this length): L_N >= N/2 - 13 for single, reversed and row. At LOGN = 22 this
      says no linear difference equation over GF(2) of order below 2,097,139 holds on the first 4,194,304 bits of the
      centre column, so no eventual period with preperiod + period below that.
  LC4 (blind; no derivative is biased): for single and row, the 1,024 lag differences x(t) XOR x(t+k) and the 1,024
      derivatives Delta^j x (j = 1..1,024; by Lucas's theorem Delta^j is the parity of x(t + i) over the i whose binary
      digits lie inside j's) have no |z| > 4.5 (about 0.014 expected among 2,048 under fair coins), and their mean z^2 is
      in [0.85, 1.15]; the density of black has |z| < 4.
  C0 (instrument, exact): the single cell's black count over the first 1,000,000 steps is 500,768 (Wolfram 2019; the
      rule30_tilt.py check TI0).
  C1 (control, known answer): every coins arm passes LC1, LC2, LC3 and LC4.
  C2 (counterfactual, must be seen): ring22's L_N is at most 3,256 + 5,477 = 8,733 and does not change after
      bit 2 * 8,733; LC1 and LC3 fail for it.
  C3 (engine, exact): the C engine's full profile equals a plain Python Berlekamp-Massey on 300 random strings of
      lengths 1 to 400 (and on the strings 0001 and 1000: L = 4 and 1); the m-sequence of x^31 + x^3 + 1 has L = 31.
  C4 (identity, exact): L_N(single) - j <= L(Delta^j) <= L_N(single) for j = 1, 2, 3.

OUTCOME of the first run, 2026-10-06 (LOGN = 22, N = 4,194,304; M5, ten cores, about three minutes): LC1, LC2, LC3
and LC4 HELD for every blind arm. The single cell's column has L_N = 2,097,152 = N/2 exactly; so do the time-reversed
column, the row arm, and the velocity, acceleration and jerk (C4 PASS, all equal). Jumps: single 1,047,637 (chi-square
p = 0.92), reversed 1,048,271 (p = 0.95), row 1,048,969 (p = 0.27); highest jumps 25, 20, 24 (deepest dip 12.5 below
n/2). Derivatives: single's largest |z| among 2,048 is 3.48 (lag 191), mean z^2 1.006, density z 0.69; row 3.30,
1.013. C0, C2 (ring22: L_N = 4,480, last jump at bit 8,959) and C3 PASS. C1 FAILED narrowly, and the fault is the
band's: coins6 had a highest jump of 29, above LC2's cap of 27. The band was set for one arm (about 0.4% beyond 28 per
arm) and not widened for eight (about 3%); its other three checks and the other seven arms passed.
"""
import hashlib
import math
import os
import random
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))


def build(name):
    exe = os.path.join(tempfile.gettempdir(), 'rule30_lc_' + name)
    subprocess.run(['cc', '-O3', '-o', exe, os.path.join(HERE, name + '.c')], check=True)
    return exe


LC = build('linear_complexity')
TILT = build('tilt')


def run_bm(bits):
    """bits: bytes of b'0'/b'1'. Returns (jumps [(n, L)], N, L_N)."""
    out = subprocess.run([LC, 'bm'], input=bits, capture_output=True, check=True).stdout.decode().split('\n')
    jumps, N, LN = [], None, None
    for line in out:
        f = line.split()
        if not f:
            continue
        if f[0] == 'J':
            jumps.append((int(f[1]), int(f[2])))
        elif f[0] == 'END':
            N, LN = int(f[1]), int(f[2])
    return jumps, N, LN


def py_bm_profile(s):
    """Plain Berlekamp-Massey over GF(2); s a list of 0/1. Returns the list of L after each bit."""
    n_ = len(s)
    C, B = [1] + [0] * n_, [1] + [0] * n_
    L, m, prof = 0, -1, []
    for n in range(n_):
        d = s[n]
        for i in range(1, L + 1):
            d ^= C[i] & s[n - i]
        if d:
            T = C[:]
            k = n - m
            for i in range(0, n_ + 1 - k):
                C[i + k] ^= B[i]
            if 2 * L <= n:
                L, m, B = n + 1 - L, n, T
        prof.append(L)
    return prof


def profile_from_jumps(jumps, N):
    prof, L, j = [], 0, 0
    for n in range(1, N + 1):
        while j < len(jumps) and jumps[j][0] == n:
            L = jumps[j][1]
            j += 1
        prof.append(L)
    return prof


def gammaq(a, x):
    """Regularized upper incomplete gamma Q(a, x) (series or continued fraction)."""
    if x <= 0:
        return 1.0
    gln = math.lgamma(a)
    if x < a + 1:
        ap, s, d = a, 1.0 / a, 1.0 / a
        for _ in range(10000):
            ap += 1
            d *= x / ap
            s += d
            if abs(d) < abs(s) * 1e-15:
                break
        return 1.0 - s * math.exp(-x + a * math.log(x) - gln)
    b, c, d = x + 1 - a, 1e300, 1.0 / (x + 1 - a)
    h = d
    for i in range(1, 10000):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        d = 1e-300 if abs(d) < 1e-300 else d
        c = b + an / c
        c = 1e-300 if abs(c) < 1e-300 else c
        d = 1.0 / d
        de = d * c
        h *= de
        if abs(de - 1) < 1e-15:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def stats(jumps, N, LN):
    heights, prev = [], 0
    for n, L in jumps:
        heights.append(L - prev)
        prev = L
    K = len(heights)
    obs = [0] * 14
    for h in heights:
        obs[min(h, 13)] += 1
    exp = [0.0] + [K * 2.0 ** -k for k in range(1, 13)] + [K * 2.0 ** -12]
    chi = sum((obs[k] - exp[k]) ** 2 / exp[k] for k in range(1, 14))
    p = gammaq(6.0, chi / 2)                             # 12 degrees of freedom
    # the extreme deviation |L_n - n/2| over n = 1..N, at the segment ends
    dmax, L, start = 0.0, 0, 1
    for n, Lj in jumps + [(N + 1, None)]:
        end = n - 1
        if end >= start:
            dmax = max(dmax, abs(L - start / 2), abs(L - end / 2))
        L, start = Lj, n
    return dict(K=K, hist=obs[1:], chi=chi, p=p, hmax=max(heights) if heights else 0, dmax=dmax, LN=LN, dev=LN - N / 2)


def zstats(bits):
    out = subprocess.run([LC, 'diff', '1024', '1024'], input=bits, capture_output=True, check=True).stdout.decode()
    zs = []
    for line in out.split('\n'):
        f = line.split()
        if f:
            ones, ln = int(f[2]), int(f[3])
            zs.append((ones - ln / 2) / math.sqrt(ln / 4))
    n1 = bits.count(b'1')
    zd = (n1 - len(bits) / 2) / math.sqrt(len(bits) / 4)
    zmax = max(abs(z) for z in zs)
    return dict(zmax=zmax, zmaxk=[i for i, z in enumerate(zs) if abs(z) == zmax][0], mz2=sum(z * z for z in zs) / len(zs),
                n45=sum(1 for z in zs if abs(z) > 4.5), zd=zd)


def coins(N, seed):
    out, i = bytearray(), 0
    while len(out) * 8 < N:
        out += hashlib.sha256(b'placego-coins %d %d' % (seed, i)).digest()
        i += 1
    s = ''.join(format(b, '08b') for b in out)[:N]
    return s.encode()


def delta(bits):
    return bytes(48 + (a ^ b) for a, b in zip(bits, bits[1:]))


def engine_checks():
    rng = random.Random(20261006)
    ok = True
    for t in range(300):
        n = rng.randint(1, 400)
        s = [rng.randint(0, 1) for _ in range(n)]
        j, N, LN = run_bm(''.join(map(str, s)).encode())
        if profile_from_jumps(j, N) != py_bm_profile(s):
            ok = False
            print('C3 MISMATCH at string', t, 'length', n)
            break
    for s, want in ((b'0001', 4), (b'1000', 1)):
        _, _, LN = run_bm(s)
        ok &= LN == want
        print('C3 string', s.decode(), 'L =', LN, '(want', want, ')')
    reg, seq = [1] * 31, []
    for _ in range(2000):                                 # x^31 + x^3 + 1: a(t+31) = a(t+3) + a(t)
        seq.append(reg[0])
        reg = reg[1:] + [reg[0] ^ reg[3]]
    _, _, LN = run_bm(''.join(map(str, seq)).encode())
    ok &= LN == 31
    print('C3 m-sequence L =', LN, '(want 31)')
    c0 = subprocess.run([TILT, '1000000', '0'], capture_output=True, check=True).stdout.count(b'1')
    print('C0 black count over 1,000,000 steps =', c0, '(want 500768)')
    print('C3', 'PASS' if ok else 'FAIL', '(300 random profiles, two short strings, the m-sequence); C0',
          'PASS' if c0 == 500768 else 'FAIL')
    return ok and c0 == 500768


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not engine_checks():
        sys.exit(1)
    if '--engine' in sys.argv:
        return
    logn = int(args[0]) if args else 22
    jobs = int(args[1]) if len(args) > 1 else 10
    N = 1 << logn
    with ThreadPoolExecutor(2) as ex:
        fs = ex.submit(lambda: subprocess.run([TILT, str(N), '0'], capture_output=True, check=True).stdout)
        fr = ex.submit(lambda: subprocess.run([TILT, str(N), '1', '1'], capture_output=True, check=True).stdout)
        single, row = fs.result(), fr.result()
    vel = delta(single)
    acc = delta(vel)
    jerk = delta(acc)
    arms = {'single': single, 'reversed': single[::-1], 'vel': vel, 'acc': acc, 'jerk': jerk, 'row': row,
            'ring22': subprocess.run([LC, 'ring', '22', str(N)], capture_output=True, check=True).stdout}
    for s in range(1, 9):
        arms['coins%d' % s] = coins(N, s)
    with ThreadPoolExecutor(jobs) as ex:
        futs = {k: ex.submit(run_bm, v) for k, v in arms.items()}
        zf = {k: ex.submit(zstats, arms[k]) for k in ['single', 'row'] + ['coins%d' % s for s in range(1, 9)]}
        res = {k: stats(*f.result()) for k, f in futs.items()}
        zres = {k: f.result() for k, f in zf.items()}
    sd = math.sqrt(N / 8)
    print('N = 2^%d = %d; jumps expected %d +- %.0f (4 sd)' % (logn, N, N // 4, 4 * sd))
    print('%-9s %9s %8s %9s %5s %6s %10s %8s' % ('arm', 'jumps', 'chi2', 'p', 'hmax', 'dmax', 'L_N', 'L_N-N/2'))
    for k, r in res.items():
        print('%-9s %9d %8.2f %9.4f %5d %6.1f %10d %8.1f' % (k, r['K'], r['chi'], r['p'], r['hmax'], r['dmax'], r['LN'],
                                                           r['dev']))
    for k, r in res.items():
        print('  heights', k, r['hist'])
    print('%-9s %7s %6s %6s %6s %7s' % ('arm', 'zmax', 'at', 'mz2', 'n>4.5', 'z(dens)'))
    for k, z in zres.items():
        at = ('lag %d' % (z['zmaxk'] + 1)) if z['zmaxk'] < 1024 else ('D^%d' % (z['zmaxk'] - 1023))
        print('%-9s %7.2f %8s %6.3f %6d %7.2f' % (k, z['zmax'], at, z['mz2'], z['n45'], z['zd']))

    def lc1(r):
        return abs(r['K'] - N / 4) <= 4 * sd and r['p'] > 0.001

    def lc2(r):
        return 17 <= r['hmax'] <= 27

    def lc3(r):
        return r['dev'] >= -13

    def lc4(z):
        return z['n45'] == 0 and 0.85 <= z['mz2'] <= 1.15 and abs(z['zd']) < 4

    blind = ['single', 'reversed', 'row']
    verdict = lambda b: 'HELD' if b else 'REFUTED'
    print('LC1', verdict(all(lc1(res[k]) for k in blind)), [(k, lc1(res[k])) for k in blind])
    print('LC2', verdict(all(lc2(res[k]) for k in blind)), [(k, lc2(res[k])) for k in blind])
    print('LC3', verdict(all(lc3(res[k]) for k in blind)), [(k, lc3(res[k])) for k in blind])
    print('LC4', verdict(all(lc4(zres[k]) for k in ('single', 'row'))), [(k, lc4(zres[k])) for k in ('single', 'row')])
    cs = ['coins%d' % s for s in range(1, 9)]
    c1 = all(lc1(res[k]) and lc2(res[k]) and lc3(res[k]) and lc4(zres[k]) for k in cs)
    print('C1', 'PASS' if c1 else 'FAIL', [(k, lc1(res[k]), lc2(res[k]), lc3(res[k]), lc4(zres[k])) for k in cs])
    r22 = res['ring22']
    j22, _, _ = futs['ring22'].result()
    lastjump = j22[-1][0] if j22 else 0
    c2 = r22['LN'] <= 8733 and lastjump <= 2 * 8733 and not lc1(r22) and not lc3(r22)
    print('C2', 'PASS' if c2 else 'FAIL', 'ring22 L_N =', r22['LN'], 'last jump at bit', lastjump)
    LN = res['single']['LN']
    c4 = all(LN - j <= res[k]['LN'] <= LN for j, k in ((1, 'vel'), (2, 'acc'), (3, 'jerk')))
    print('C4', 'PASS' if c4 else 'FAIL', 'L_N single', LN, 'vel', res['vel']['LN'], 'acc', res['acc']['LN'], 'jerk',
          res['jerk']['LN'])


if __name__ == '__main__':
    main()
