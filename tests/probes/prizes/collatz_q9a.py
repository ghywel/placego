#!/usr/bin/env python3
"""collatz_q9a.py: Q9A, the counting form at the first step past Terras's free bits, at widths 27 .. 35 (Local's
run under draw-and-work, row Q9, after L220-L223 and L230; claimed in CLOUD-LOCAL.md with these predictions pushed
before the run).

RUN-ON:     cpu; collatz.c built with OpenMP (Homebrew libomp), all cores
COMMAND:    python3 tests/probes/prizes/collatz_q9a.py
COST:       minutes (to be recorded).

L220 reduced the count at T = w to one bit: S_w(w) - coin = (marginal prefixes whose T^(w-1)(r) is even) - M/2, where
M = 2 V(w - 1) - V(w) counts the prefixes alive at w - 1 with coefficient between 1 and 2, and coin = V(w)/2. At
w = 18, 20, 24, 26 the deviation was 0.62 to 1.32 times sqrt(M/4). This run measures it at every width from 27 to 35
that has marginal prefixes (27, 29, 31, 32, 34, 35; M from 312,455 to 39,993,895), counting every w-bit number's
stopping time with collatz.c (the counting form's own engine). By CZ1 (measured from w = 20 to 40), the stopping-time
count equals the coefficient count, so S_w(w) is what the reduction speaks about.

PREDICTIONS (Local's, published before the run):
  Q9A-C0 (control): at T = w - 1 the count equals V(w - 1) exactly (Terras, CZ0), and at T = w the stopping-time
         and coefficient counts agree (CZ1), at every width run.
  Q9A-P1 (blind): |S_w(w) - V(w)/2| <= 3 sqrt(M/4) at every width run (coin-like, square-root size).
  Q9A-P2 (blind): the relative excess |S_w(w) - V(w)/2| / (V(w)/2) is below 0.0005 at every width from 31 on.
OUTCOME: not yet run.
"""
import math
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BIN = os.path.join(os.environ.get('NP_SCRATCH', '/tmp'), 'collatz_omp')
L3 = math.log2(3)


def V_table(tmax):
    cur, V = {0: 1}, {0: 1}
    for t in range(1, tmax + 1):
        nxt = {}
        for a, c in cur.items():
            for b in (0, 1):
                a2 = a + b
                if a2 * L3 > t:
                    nxt[a2] = nxt.get(a2, 0) + c
        cur = nxt
        V[t] = sum(cur.values())
    return V


def main():
    omp = '/opt/homebrew/opt/libomp'
    subprocess.run(['cc', '-O2', '-Xpreprocessor', '-fopenmp', '-I' + omp + '/include', '-L' + omp + '/lib', '-lomp',
                    '-o', BIN, os.path.join(HERE, 'collatz.c')], check=True)
    V = V_table(40)
    widths = [w for w in range(27, 36) if 2 * V[w - 1] - V[w] > 0]
    c0, p1, p2 = True, True, True
    for w in widths:
        out = subprocess.run([BIN, str(w), str(w + 1)], capture_output=True, text=True, check=True).stdout
        S = {int(l.split()[1]): int(l.split()[2]) for l in out.splitlines() if l.startswith('S ')}
        St = {int(l.split()[1]): int(l.split()[3]) for l in out.splitlines() if l.startswith('S ')}
        M = 2 * V[w - 1] - V[w]
        coin = V[w] / 2
        dev = S[w] - coin
        c0 &= S[w - 1] == V[w - 1] and S[w] == St[w]
        z = dev / math.sqrt(M / 4)
        rel = abs(dev) / coin
        p1 &= abs(z) <= 3
        if w >= 31:
            p2 &= rel < 0.0005
        print('w %d: M %d, S_w(w) %d, coin %.1f, S - coin %+.1f = %+.2f sqrt(M/4), relative %.6f'
              % (w, M, S[w], coin, dev, z, rel), flush=True)
    print('Q9A-C0', 'PASS' if c0 else 'FAIL')
    print('Q9A-P1', 'HELD' if p1 else 'REFUTED')
    print('Q9A-P2', 'HELD' if p2 else 'REFUTED')


if __name__ == '__main__':
    main()
