#!/usr/bin/env python3
"""rule30_halfcircle_repeat.py: GPT's GC159 request (2026-10-07, Q7): does the half-circle code c_s = floor(s beta)
mod 2, beta = 2 - sqrt 2, pass the whole necessary repeat filter b <= 2a + q + C at C = 0 on a 4,096-bit prefix? Its
derivative g_s = c_s XOR c_(s+1) is the Sturmian word of slope beta, which G135 excludes; GC158 showed the exclusion
does not transfer to c because a repetition of g may lift to a complemented repetition of c, and L096 showed that for
this beta every convergent numerator is odd.

RUN-ON:     cpu (Python 3 standard library)
COMMAND:    python3 tests/probes/lexicon/rule30_halfcircle_repeat.py
COST:       about ten seconds.

Repeat debt. For a period q, a repetition is a maximal interval [a, b] with c_s = c_(s+q) for a <= s <= b and
b + q <= N - 1 (inside the prefix of N symbols); its debt is b - 2a - q, and the filter at C = 0 asks every debt to be
at most 0. Maximal intervals suffice (shrinking an interval cannot raise the debt), and q > N/2 cannot have positive
debt in the prefix. Exact integers: for s > 0, floor(s beta) = 2s - isqrt(2 s^2) - 1 and floor(s beta + 1/2) =
2s - ((isqrt(8 s^2) - 1) // 2 + 1); both are 0 at s = 0. They are cross-checked against 60-digit decimal arithmetic for
every s used, and for the short controls each square root is bracketed between adjacent integers by hand-checkable
squares.

PREDICTIONS, published by GPT in GC159 (commit d8bb640) before this script was written or run:
  HR0 (must hold): exact generation gives the first eight bits 00110010.
  HR1 (blind): the maximum repeat debt of c (phase zero) over N = 4,096 symbols and every q from 1 to 2,048 is at most
      zero. If it fails, keep the witness and stop.
  HR2 (must hold): the XOR derivative of c is the mechanical word of slope beta and has positive repeat debt within its
      first 1,005 symbols (G135 at C = 0). The counterfactual "a derivative repetition lifts with the same period"
      must fail for c = 0101... at q = 1.
  HR3 (must hold; the phase control): floor(s beta + 1/2) mod 2 has period-7 equality for s = 0..10 and a mismatch at
      s = 11, giving debt 3; its first 19 bits are 0110010011001001101.

OUTCOME, 2026-10-07 (M5, 0.6 s; the cost line's ten seconds was generous). Instrument: the integer formulas equal
60-digit decimal floors for every s up to 4,097, and the square roots are bracketed for s up to 20. HR0 PASS (00110010).
HR1 HELD: no period q <= 2,048 has positive debt; the maximum is -1, at the trivial q = 1, [0, 0]. HR2 PASS: the
derivative is the mechanical word of slope beta, and within 1,005 symbols it has debt 235 at q = 169 (a convergent
denominator, numerator 99 odd), [a, b] = [1, 406]; the 0101... lift counterfactual fails. HR3 PASS. Descriptive, not
predicted: exactly seven periods reach debt -3, the next largest after q = 1 (-1) and q = 4 (-2), and they are the
mediant shifts q_k + q_(k+1) of beta's convergent denominators, 3, 7, 17, 41, 99, 239 and 577 (intervals [3, 6], [0, 4],
[13, 40], [30, 98], [71, 238], [170, 576], [409, 1392]), whose numerators are even; the next mediant, 1393, is cut by
the prefix (best interval [0, 984]). The convergent shifts themselves (odd numerators: 12, 29, 70, 169, 408, 985)
complement c and have only single-point repetitions. Finite evidence only: this code passes the C = 0 filter on the
prefix with margin 3 at every mediant scale, which is not an all-period statement.
"""
import decimal
from math import isqrt

N = 4096


def fl0(s):
    return 0 if s == 0 else 2 * s - isqrt(2 * s * s) - 1


def flh(s):
    return 0 if s == 0 else 2 * s - ((isqrt(8 * s * s) - 1) // 2 + 1)


def debts(w, qmax, n=None):
    """All maximal repetitions of w (prefix of n symbols): {q: (max debt, a, b)} for q = 1..qmax."""
    n = len(w) if n is None else n
    out = {}
    for q in range(1, qmax + 1):
        best = None
        s = 0
        while s + q <= n - 1:
            if w[s] == w[s + q]:
                a = s
                while s + q <= n - 1 and w[s] == w[s + q]:
                    s += 1
                b = s - 1
                d = b - 2 * a - q
                if best is None or d > best[0]:
                    best = (d, a, b)
            s += 1
        if best is not None:
            out[q] = best
    return out


def main():
    decimal.getcontext().prec = 60
    beta = 2 - decimal.Decimal(2).sqrt()
    half = decimal.Decimal(1) / 2
    ok_dec = all(int((s * beta).to_integral_value(rounding=decimal.ROUND_FLOOR)) == fl0(s) and
                 int((s * beta + half).to_integral_value(rounding=decimal.ROUND_FLOOR)) == flh(s)
                 for s in range(N + 2))
    ok_br = all((m := isqrt(2 * s * s)) ** 2 <= 2 * s * s < (m + 1) ** 2 and
                (k := isqrt(8 * s * s)) ** 2 <= 8 * s * s < (k + 1) ** 2 for s in range(1, 21))
    print('instrument: integer formulas = 60-digit decimals for s <= %d: %s; square roots bracketed for s <= 20: %s'
          % (N + 1, ok_dec, ok_br))
    c = [fl0(s) % 2 for s in range(N + 1)]
    hr0 = ''.join(map(str, c[:8])) == '00110010'
    print('HR0', 'PASS' if hr0 else 'FAIL', ''.join(map(str, c[:8])))

    D = debts(c[:N], N // 2)
    top = max(D.items(), key=lambda kv: kv[1][0])
    pos = sorted((q, v) for q, v in D.items() if v[0] > 0)
    print('HR1', 'HELD' if top[1][0] <= 0 else 'REFUTED',
          'max debt %d at q = %d, [a, b] = [%d, %d]' % (top[1][0], top[0], top[1][1], top[1][2]))
    print('  positive witnesses: %d periods' % len(pos), pos[:40])
    cert = sorted(D.items(), key=lambda kv: -kv[1][0])[:15]
    print('  largest per-period debts (q: debt, a, b):', [(q, v) for q, v in cert])

    g = [c[s] ^ c[s + 1] for s in range(N)]
    mech = all(g[s] == fl0(s + 1) - fl0(s) for s in range(N))
    Dg = debts(g[:1005], 502)
    gtop = max(Dg.items(), key=lambda kv: kv[1][0])
    alt = [s % 2 for s in range(64)]
    galt = [alt[s] ^ alt[s + 1] for s in range(63)]
    lift_fails = all(alt[s] != alt[s + 1] for s in range(63)) and debts(galt, 1)[1][0] > 0
    hr2 = mech and gtop[1][0] > 0 and lift_fails
    print('HR2', 'PASS' if hr2 else 'FAIL', 'derivative mechanical: %s; its max debt in 1,005 symbols %d at q = %d, '
          '[a, b] = [%d, %d]; 0101... lift counterfactual fails: %s' % (mech, gtop[1][0], gtop[0], gtop[1][1],
                                                                      gtop[1][2], lift_fails))

    h = [flh(s) % 2 for s in range(64)]
    eq7 = [h[s] == h[s + 7] for s in range(12)]
    hr3 = (''.join(map(str, h[:19])) == '0110010011001001101' and all(eq7[:11]) and not eq7[11]
           and debts(h[:19], 7)[7] == (3, 0, 10))
    print('HR3', 'PASS' if hr3 else 'FAIL', ''.join(map(str, h[:19])), 'period-7 equality s = 0..11:', eq7)


if __name__ == '__main__':
    main()
