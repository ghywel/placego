"""CL522: reproduce Hercher's m-cycle chain (arXiv 2201.00406v3, Theorem 21 + Lemma 22 + Theorem 23) and test the
rStation repair of the Theorem 21 sum bound (CL520-521).
Chain: given K_low, take the largest m2 <= m with (delta^m2 - 1)/(delta - 1) * log2(162/97 * X0) <= (m2/m) K_low;
v = (m2/m) K (delta-1)/(delta^m2 - 1); eps = S / (3 K log 2); Lemma 22 on (delta, delta + eps) gives the least
denominator q of a fraction in the interval; K_low <- q.  Stop when K_low > K_up(m) = 1.4784 m delta^m
(Simons-de Weger) or it stalls.
S (ORIGINAL, Hercher):  (97(m-m2)+73)/(54 X0) + 3/(2^v - 1) + 3(m2-1)/(2^v - 1)^delta      [the step with the gap]
S (REPAIR, rStation):   min( sum_i 3/max(X0, 2^(K/G(i)) - 1),  97 m/(54 X0) ),
                        G(r) = (delta^(m-r+1) - 1)/(delta - 1) + r - 1   (sorted minima: s_(r) >= K/G(r)).
Cloud's hand check of the repair lemma (CL521): r minima with s <= t start r chains; s_{i+1} < delta s_i and k_i <= s_i
give K <= t G(r) by convexity.

OUTCOME (CL522).  ORIGINAL chain (with Hercher's m2 = m and m2 = m - 1 special cases) reproduces Theorem 23 exactly:
m2 = 47, 67, 77, 82, 86, 88, 91; K > 5.267e15, 3.976e17, 4.64e18, 2.744e19, 7.769e19, 2.056e20, 7.942e21 > K_up(91)
= 2.141e20.  REPAIRED bound: m <= 91 excluded with the same final K (7.942e21), at X0 = 704*2^60 and at 2^71; m = 92, 93
not excluded at either.  CRUDE variant (the two gap terms bounded by 3/X0 each): largest excluded m is 82.  All three
rStation claims (post 24) confirmed by this independent implementation.  (A first run wrongly stalled at m = 91: an
overflow guard of mine counted minima as X0 when 2^(K/G) already exceeded X0; fixed.)
"""
import sys
from decimal import Decimal as D, getcontext
getcontext().prec = 120
LN2 = D(2).ln(); LN3 = D(3).ln(); DELTA = LN3 / LN2

def cf(x, n=200):
    out = []
    for _ in range(n):
        a = int(x); out.append(a); f = x - a
        if f == 0: break
        x = 1 / f
    return out

def lemma22_denominator(alpha, beta):
    ca, cb = cf(alpha), cf(beta)
    k = 0
    while k < min(len(ca), len(cb)) and ca[k] == cb[k]: k += 1
    terms = ca[:k] + [min(ca[k], cb[k]) + 1]
    p0, q0, p1, q1 = 1, 0, terms[0], 1
    for a in terms[1:]:
        p0, q0, p1, q1 = p1, q1, a * p1 + p0, a * q1 + q0
    return q1

def pow2(x):
    return (x * LN2).exp()

def S_bound(K, m, m2, X0, mode):
    if mode == 'orig':
        v = D(m2) / m * K * (DELTA - 1) / (DELTA ** m2 - 1)
        first = D(0) if m2 == m else (3 / X0 if m2 == m - 1 else D(97 * (m - m2) + 73) / (54 * X0))
        return first + 3 / (pow2(v) - 1) + 3 * (m2 - 1) / ((pow2(v) - 1) ** DELTA)
    tot = D(0)
    for r in range(1, m + 1):
        G = (DELTA ** (m - r + 1) - 1) / (DELTA - 1) + r - 1
        e = K / G
        if e * LN2 > (X0 + 1).ln(): continue_term = 3 / (pow2(e) - 1) if e < 100000 else D(0)
        else: continue_term = 3 / X0
        tot += continue_term
    return min(tot, D(97 * m) / (54 * X0))

def chain(m, X0, mode, K0=D(7) * D(10) ** 11, verbose=False):
    K = K0; K_up = D('1.4784') * m * DELTA ** m; steps = []
    for _ in range(60):
        m2 = 0
        for c in range(m, 0, -1):
            if (DELTA ** c - 1) / (DELTA - 1) * ((D(162) / 97 * X0).ln() / LN2) <= D(c) / m * K: m2 = c; break
        if mode == 'orig' and m2 == 0:
            S = D(97 * m) / (54 * X0)
        else:
            S = S_bound(K, m, m2, X0, mode)
        eps = S / (3 * K * LN2)
        q = D(lemma22_denominator(DELTA, DELTA + eps))
        steps.append((m2, float(eps), float(q)))
        if verbose: print('   m2', m2, 'eps %.3g' % eps, 'K >', '%.4g' % q, flush=True)
        if q <= K: return False, steps, K_up
        K = q
        if K > K_up: return True, steps, K_up
    return False, steps, K_up

if __name__ == '__main__':
    X0 = D(704) * D(2) ** 60
    print('ORIGINAL chain, m = 91, X0 = 704*2^60:')
    ok, st, Kup = chain(91, X0, 'orig', verbose=True); print('  excluded:', ok, 'K_up %.4g' % Kup)
    for X0name, X0v in (('704*2^60', D(704) * D(2) ** 60), ('2^71', D(2) ** 71)):
        print('REPAIRED chain, X0 =', X0name)
        for m in (82, 85, 88, 90, 91, 92, 93):
            ok, st, Kup = chain(m, X0v, 'repair')
            print('  m', m, 'excluded:', ok, 'final K > %.4g' % st[-1][2], 'K_up %.4g' % Kup, 'steps', len(st), flush=True)
